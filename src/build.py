import html
import json
import sys

INTERVALS = {"synthetic": (3000, 4000), "semi": (2500, 3500), "mineral": (2000, 3000)}
API_ORDER = {"SH": 0, "SL": 1, "SM": 2, "SN": 3, "SN Plus": 4, "SP": 5}
BASE_SCORE = {"mineral": 1, "semi": 2, "synthetic": 3}


def num(v):
    return v if isinstance(v, (int, float)) and not isinstance(v, bool) else None


def fmt(v, d=1):
    if v is None:
        return "—"
    if isinstance(v, str):
        return v
    s = f"{v:,.{d}f}"
    return s.replace("-", "−")


def extremes(rows, key, direction):
    vals = [(i, num(r.get(key))) for i, r in enumerate(rows)]
    vals = [(i, v) for i, v in vals if v is not None]
    if len(vals) < 2:
        return set(), set()
    hi, lo = max(v for _, v in vals), min(v for _, v in vals)
    if hi == lo:
        return set(), set()
    best_v, worst_v = (hi, lo) if direction == "high" else (lo, hi)
    return {i for i, v in vals if v == best_v}, {i for i, v in vals if v == worst_v}


def cat_extremes(rows, scorer, want_best=True, want_worst=True):
    scores = [(i, scorer(r)) for i, r in enumerate(rows)]
    scores = [(i, s) for i, s in scores if s is not None]
    if len(scores) < 2:
        return set(), set()
    hi, lo = max(s for _, s in scores), min(s for _, s in scores)
    if hi == lo:
        return set(), set()
    best = {i for i, s in scores if s == hi} if want_best else set()
    worst = {i for i, s in scores if s == lo} if want_worst else set()
    return best, worst


def build(data, tpl):
    rows = data["oils"]
    for r in rows:
        city, hwy = INTERVALS[r["type"]]
        r["city_km"], r["hwy_km"] = city, hwy
        r["tk_city"] = round(r["price"] / city, 2)
        r["tk_hwy"] = round(r["price"] / hwy, 2)

    cols = [
        dict(key="price", label="Price", unit="৳ per litre", dir="low", kind="price"),
        dict(key="base", label="Base oil", unit="API group", dir=None, kind="base"),
        dict(key="ester", label="Ester", unit="", dir=None, kind="ester"),
        dict(key="api", label="API", unit="newer is better", dir=None, kind="api"),
        dict(key="jaso", label="JASO", unit="registered is better", dir=None, kind="jaso"),
        dict(key="kv40", label="Viscosity 40°C", unit="cSt · for reference", dir=None, kind="num", d=1),
        dict(key="kv100", label="Viscosity 100°C", unit="cSt · ↑ thicker hot film", dir="high", kind="num", d=1),
        dict(key="vi", label="Viscosity index", unit="↑ higher is better", dir="high", kind="num", d=0),
        dict(key="hths", label="HTHS 150°C", unit="mPa·s · ↑ higher is better", dir="high", kind="num", d=1),
        dict(key="flash", label="Flash point", unit="°C · ↑ higher is better", dir="high", kind="num", d=0),
        dict(key="pour", label="Pour point", unit="°C · ↓ lower is better", dir="low", kind="num", d=0),
        dict(key="noack", label="Evaporation (Noack)", unit="% · ↓ lower is better", dir="low", kind="num", d=1),
        dict(key="tbn", label="TBN acid neutraliser", unit="mg KOH/g · ↑ higher is better", dir="high", kind="num", d=1),
        dict(key="sa", label="Sulfated ash", unit="% · detergent metals, for reference", dir=None, kind="num", d=2),
        dict(key="city_km", label="Change every: city", unit="km · suggested", dir=None, kind="km"),
        dict(key="hwy_km", label="Change every: highway", unit="km · suggested", dir=None, kind="km"),
        dict(key="tk_city", label="Taka/km: city", unit="↓ lower is better", dir="low", kind="num", d=2),
        dict(key="tk_hwy", label="Taka/km: highway", unit="↓ lower is better", dir="low", kind="num", d=2),
    ]

    marks = {}
    for c in cols:
        if c["kind"] in ("num", "price") and c["dir"]:
            marks[c["key"]] = extremes(rows, c["key"], c["dir"])
        elif c["kind"] == "api":
            marks[c["key"]] = cat_extremes(rows, lambda r: API_ORDER.get(r["api"]))
        elif c["kind"] == "jaso":
            marks[c["key"]] = cat_extremes(rows, lambda r: 2 if r["jaso_reg"] else 1)
        elif c["kind"] == "base":
            marks[c["key"]] = cat_extremes(rows, lambda r: BASE_SCORE[r["type"]], want_best=False)
        elif c["kind"] == "ester":
            marks[c["key"]] = ({i for i, r in enumerate(rows) if r["ester"] == "Yes"}, set())
        else:
            marks[c["key"]] = (set(), set())

    def cell(c, i, r):
        best, worst = marks[c["key"]]
        cls = "best" if i in best else "worst" if i in worst else ""
        v = r.get(c["key"])
        if c["kind"] == "price":
            text = f"৳{v:,}"
        elif c["kind"] == "km":
            text = f"{v:,}"
        elif c["kind"] == "jaso":
            text = f'{html.escape(r["jaso"])}<span class="sub">{html.escape(r["jaso_note"])}</span>'
        elif c["kind"] in ("base", "ester", "api"):
            text = html.escape(v) if v else "—"
        else:
            text = html.escape(fmt(v, c.get("d", 1)))
        if text == "—":
            cls = (cls + " na").strip()
        return f'<td class="{cls} c-{c["key"]}">{text}</td>'

    head = "".join(
        f'<th class="c-{c["key"]}">{html.escape(c["label"])}<span class="unit">{html.escape(c["unit"])}</span></th>'
        for c in cols
    )
    body = []
    for i, r in enumerate(rows):
        rank = r.get("rank")
        badge = "ref" if rank is None else "top" if rank <= 3 else "rest"
        tds = "".join(cell(c, i, r) for c in cols)
        body.append(
            f'<tr><td class="c-rank"><div class="rank {badge}">{rank if rank is not None else "–"}</div></td>'
            f'<td class="c-name"><div class="name">{html.escape(r["name"])}</div>'
            f'<div class="sub">{html.escape(r["sub"])}</div></td>{tds}</tr>'
        )

    return (
        tpl.replace("{{HEAD}}", head)
        .replace("{{BODY}}", "\n".join(body))
        .replace("{{PICKS}}", data["picks_html"])
        .replace("{{TITLE}}", html.escape(data["title"]))
        .replace("{{LEDE}}", html.escape(data["lede"]))
    )


if __name__ == "__main__":
    data = json.load(open(sys.argv[1], encoding="utf-8"))
    out = build(data, open(sys.argv[2], encoding="utf-8").read())
    open(sys.argv[3], "w", encoding="utf-8").write(out)
    print("rows:", len(data["oils"]))
