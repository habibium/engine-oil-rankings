import copy
import json
import sys

sys.path.insert(0, sys.argv[1])
import build  # noqa: E402

base_dir, data_path, tpl_path, out_dir = sys.argv[1:5]
data = json.load(open(data_path, encoding="utf-8"))
tpl = open(tpl_path, encoding="utf-8").read()
oils = data["oils"]
INTERVAL_CITY = {"synthetic": 3000, "semi": 2500}


def pick(label, name):
    return f'<div class="pick"><b>{label}:</b> {name}</div>'


def has_datasheet(o):
    return o["kv100"] is not None


def sport_score(o):
    s = 2 if o["ester"] == "Yes" else 0
    s += o["type"] == "synthetic"
    s += bool(o["jaso_reg"])
    s += (o["vi"] or 0) >= 150
    s += o["kv40"] is not None and o["kv40"] <= 70
    s += isinstance(o["hths"], (int, float)) and o["hths"] >= 3.3
    return int(s)


def tk_city(o):
    return o["price"] / INTERVAL_CITY[o["type"]]


def ranked(order, unranked=()):
    rows, n = [], 0
    for o in order:
        o = copy.deepcopy(o)
        if o["name"] in unranked:
            o["rank"] = None
        else:
            n += 1
            o["rank"] = n
        rows.append(o)
    return rows


variants = {}

variants["protection"] = dict(
    title="10W-30 motorcycle oils ranked by engine protection: base oil, verified specs and lab data",
    lede="Synthetics rank above semi-synthetics. Within each group, oils whose JASO MA2 registration is on JASO's own list come first; then the API rating and the makers' published lab data (evaporation loss, flash point, HTHS, TBN) set the order. Oils with no published datasheet are listed last, unranked. Oils commonly sold in Bangladesh, November 2026 prices; running cost per km is on the right.",
    picks_html=pick("Best protection", "Ravenol Motobike 4-T Ester")
    + pick("Best value, verified synthetic", "Liqui Moly Motorbike 4T Street")
    + pick("Cheapest per km", "Sinopec Xplore 4T"),
    oils=ranked(oils, unranked={o["name"] for o in oils if o["rank"] is None}),
)

perf_pool = sorted(
    [o for o in oils if has_datasheet(o)],
    key=lambda o: (-sport_score(o), o["type"] != "synthetic", -(o["vi"] or 0)),
)
perf_rows = []
for o in perf_pool + [o for o in oils if not has_datasheet(o)]:
    o = copy.deepcopy(o)
    if has_datasheet(o):
        o["sub"] = f'{o["sub"]} · sport score {sport_score(o)}/7'
    perf_rows.append(o)
variants["performance"] = dict(
    title="10W-30 motorcycle oils ranked for performance and sporty feel",
    lede="Feel can't be read off a datasheet, so this ranks the formulation features linked to quick revving, smooth shifting and a firm clutch: ester content (2 points), full-synthetic base, JASO MA2 registration on JASO's list, viscosity index 150 or higher, viscosity at 40 °C of 70 cSt or less, and HTHS 3.3 or higher (1 point each; sport score out of 7). Ties go to the full synthetic, then the higher viscosity index. Oils with no datasheet are listed last, unranked. November 2026 Bangladesh prices.",
    picks_html=pick("Top sport formulation", perf_pool[0]["name"])
    + pick("Runner-up", perf_pool[1]["name"])
    + pick("Best semi-synthetic for sport", next(o["name"] for o in perf_pool if o["type"] == "semi")),
    oils=ranked(perf_rows, unranked={o["name"] for o in oils if not has_datasheet(o)}),
)

verified = [o for o in oils if o["jaso_reg"] and has_datasheet(o)]
rest = [o for o in oils if o not in verified]
value_order = sorted(verified, key=tk_city) + sorted(rest, key=tk_city)
variants["value"] = dict(
    title="10W-30 motorcycle oils ranked by value for money",
    lede="Oils that publish a datasheet and whose JASO MA2 registration is on JASO's own list come first, ordered by city running cost (Taka/km); the rest follow, also by Taka/km. Taka/km already allows for the longer change interval of synthetic oils. Oils commonly sold in Bangladesh, November 2026 prices.",
    picks_html=pick("Best value overall", value_order[0]["name"])
    + pick("Best-value synthetic", next(o["name"] for o in value_order if o["type"] == "synthetic"))
    + pick("Best-value ester oil", next(o["name"] for o in value_order if o["ester"] == "Yes")),
    oils=ranked(value_order),
)

for key, v in variants.items():
    out = build.build(v, tpl)
    open(f"{out_dir}/{key}.html", "w", encoding="utf-8").write(out)
    print(key, [(o["rank"], o["name"]) for o in v["oils"]])
