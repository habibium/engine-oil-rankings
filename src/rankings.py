"""Shared ranking logic for the images (build_images.py) and the website (build_site.py)."""
import copy
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COLUMNS = json.loads((ROOT / "src" / "columns.json").read_text(encoding="utf-8"))

# Suggested change intervals (city km, highway km) for Bangladesh's heat.
INTERVALS = {"synthetic": (3000, 4000), "semi": (2500, 3500), "mineral": (2000, 3000)}
API_ORDER = {"SH": 0, "SL": 1, "SM": 2, "SN": 3, "SN Plus": 4, "SP": 5}
BASE_SCORE = {"mineral": 1, "semi": 2, "synthetic": 3}
TYPE_LABEL = {"synthetic": "Synthetic", "semi": "Semi-synthetic", "mineral": "Mineral"}
RANKINGS = ("protection", "performance", "value")


def num(v):
    return v if isinstance(v, (int, float)) and not isinstance(v, bool) else None


def slug(grade):
    return re.sub(r"[^a-z0-9]+", "-", grade.lower()).strip("-")


def file_stem(grade):
    return grade.lower().replace("-", "")


def load_grades():
    grades = [load_grade(p) for p in sorted((ROOT / "data").glob("*.json"))]
    return sorted(grades, key=lambda g: g["grade"])


def load_grade(path):
    g = json.loads(Path(path).read_text(encoding="utf-8"))
    g["slug"] = slug(g["grade"])
    g["stem"] = file_stem(g["grade"])
    for o in g["oils"]:
        city, hwy = INTERVALS[o["type"]]
        o["city_km"], o["hwy_km"] = city, hwy
        o["tk_city"] = round(o["price"] / city, 2)
        o["tk_hwy"] = round(o["price"] / hwy, 2)
        o["has_datasheet"] = o["kv100"] is not None
        o["sport_score"] = sport_score(o) if o["has_datasheet"] else None
    return g


def sport_score(o):
    s = 2 if o["ester"] == "Yes" else 0
    s += o["type"] == "synthetic"
    s += bool(o["jaso_reg"])
    s += (o["vi"] or 0) >= 150
    s += o["kv40"] is not None and o["kv40"] <= 70
    s += num(o["hths"]) is not None and o["hths"] >= 3.3
    return int(s)


def _extremes(scores, want_best=True, want_worst=True):
    scores = [(i, s) for i, s in scores if s is not None]
    if len(scores) < 2:
        return set(), set()
    hi, lo = max(s for _, s in scores), min(s for _, s in scores)
    if hi == lo:
        return set(), set()
    return ({i for i, s in scores if s == hi} if want_best else set(),
            {i for i, s in scores if s == lo} if want_worst else set())


def marks(oils):
    """Per column: (ids coloured best, ids coloured worst). Values given only as a minimum ("≥2.9") are skipped."""
    out = {}
    for c in COLUMNS:
        k, kind = c["key"], c["kind"]
        if kind in ("num", "price") and c["dir"]:
            sign = 1 if c["dir"] == "high" else -1
            out[k] = _extremes([(o["id"], None if num(o.get(k)) is None else sign * o[k]) for o in oils])
        elif kind == "api":
            out[k] = _extremes([(o["id"], API_ORDER.get(o["api"])) for o in oils])
        elif kind == "jaso":
            out[k] = _extremes([(o["id"], 2 if o["jaso_reg"] else 1) for o in oils])
        elif kind == "base":
            out[k] = _extremes([(o["id"], BASE_SCORE[o["type"]]) for o in oils], want_best=False)
        elif kind == "ester":
            out[k] = ({o["id"] for o in oils if o["ester"] == "Yes"}, set())
        else:
            out[k] = (set(), set())
    return out


def _first(oils, pred=lambda o: True):
    return next((o["name"] for o in oils if pred(o)), None)


def rankings(g):
    """The three orderings of one grade: title, lede, picks and rows (each row a copy of the oil with "rank")."""
    oils, grade, region, updated = g["oils"], g["grade"], g["region"], g["updated"]
    by_tk = lambda o: o["tk_city"]

    verified = [o for o in oils if o["jaso_reg"] and o["has_datasheet"]]
    value_order = sorted(verified, key=by_tk) + sorted([o for o in oils if o not in verified], key=by_tk)

    protection_order = sorted([o for o in oils if o["protection_rank"] is not None], key=lambda o: o["protection_rank"])
    protection_order += [o for o in oils if o["protection_rank"] is None]

    perf_pool = sorted([o for o in oils if o["has_datasheet"]],
                       key=lambda o: (-o["sport_score"], o["type"] != "synthetic", -(o["vi"] or 0)))
    perf_order = perf_pool + [o for o in oils if not o["has_datasheet"]]

    out = {
        "protection": dict(
            title=f"{grade} motorcycle oils ranked by engine protection: base oil, verified specs and lab data",
            lede=("Synthetics rank above semi-synthetics. Within each group, oils whose JASO MA2 registration is on JASO's own list come first; "
                  "then the API rating and the makers' published lab data (evaporation loss, flash point, HTHS, TBN) set the order. "
                  f"Oils with no published datasheet are listed last, unranked. Oils commonly sold in {region}, {updated} prices; running cost per km is on the right."),
            picks=[("Best protection", protection_order[0]["name"]),
                   ("Best value, verified synthetic", _first(value_order, lambda o: o["type"] == "synthetic" and o in verified)),
                   ("Cheapest per km", min(oils, key=by_tk)["name"])],
            order=protection_order,
            unranked={o["id"] for o in oils if o["protection_rank"] is None},
        ),
        "performance": dict(
            title=f"{grade} motorcycle oils ranked for performance and sporty feel",
            lede=("Feel can't be read off a datasheet, so this ranks the formulation features linked to quick revving, smooth shifting and a firm clutch: "
                  "ester content (2 points), full-synthetic base, JASO MA2 registration on JASO's list, viscosity index 150 or higher, viscosity at 40 °C of 70 cSt or less, "
                  "and HTHS 3.3 or higher (1 point each; sport score out of 7). Ties go to the full synthetic, then the higher viscosity index. "
                  f"Oils with no datasheet are listed last, unranked. {updated} {region} prices."),
            picks=[("Top sport formulation", _first(perf_pool)),
                   ("Runner-up", perf_pool[1]["name"] if len(perf_pool) > 1 else None),
                   ("Best semi-synthetic for sport", _first(perf_pool, lambda o: o["type"] == "semi"))],
            order=perf_order,
            unranked={o["id"] for o in oils if not o["has_datasheet"]},
        ),
        "value": dict(
            title=f"{grade} motorcycle oils ranked by value for money",
            lede=("Oils that publish a datasheet and whose JASO MA2 registration is on JASO's own list come first, ordered by city running cost (Taka/km); "
                  "the rest follow, also by Taka/km. Taka/km already allows for the longer change interval of synthetic oils. "
                  f"Oils commonly sold in {region}, {updated} prices."),
            picks=[("Best value overall", _first(value_order)),
                   ("Best-value synthetic", _first(value_order, lambda o: o["type"] == "synthetic")),
                   ("Best-value ester oil", _first(value_order, lambda o: o["ester"] == "Yes"))],
            order=value_order,
            unranked=set(),
        ),
    }
    for v in out.values():
        v["picks"] = [(label, name) for label, name in v["picks"] if name]
        rows, n = [], 0
        for o in v["order"]:
            o = copy.deepcopy(o)
            if o["id"] in v["unranked"]:
                o["rank"] = None
            else:
                n += 1
                o["rank"] = n
            rows.append(o)
        v["rows"] = rows
    return out


def fmt(v, d=1):
    if v is None:
        return "—"
    if isinstance(v, str):
        return v
    return f"{v:,.{d}f}".replace("-", "−")


def cell_text(col, o):
    """Display text and optional sub-line for one cell, shared by the images and the website."""
    v, kind = o.get(col["key"]), col["kind"]
    if kind == "price":
        return f"৳{v:,}", None
    if kind == "km":
        return f"{v:,}", None
    if kind == "jaso":
        return o["jaso"], o["jaso_note"]
    if kind in ("base", "ester", "api"):
        return (v if v else "—"), None
    return fmt(v, col.get("d", 1)), None


def sort_value(col, o):
    """Number used to sort a column on the website; None sorts last in both directions."""
    v, kind = o.get(col["key"]), col["kind"]
    if kind == "api":
        return API_ORDER.get(v)
    if kind == "jaso":
        return (2 if o["jaso_reg"] else 0) + (0.5 if v == "MA2" else 0)
    if kind == "base":
        return BASE_SCORE[o["type"]]
    if kind == "ester":
        return 1 if v == "Yes" else 0
    if isinstance(v, str):
        m = re.search(r"-?\d+(\.\d+)?", v)
        return float(m.group()) if m else None
    return num(v)
