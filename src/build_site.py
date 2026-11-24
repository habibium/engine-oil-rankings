"""Builds the GitHub Pages site into the given folder: site/ + one JSON per grade + PDFs, PNGs and datasheets."""
import json
import shutil
import sys
from pathlib import Path

import rankings as R

out = Path(sys.argv[1])
shutil.rmtree(out, ignore_errors=True)
shutil.copytree(R.ROOT / "site", out)
shutil.copytree(R.ROOT / "output", out / "downloads")
shutil.copytree(R.ROOT / "datasheets", out / "datasheets")
shutil.copytree(R.ROOT / "docs" / "sources", out / "sources")
(out / "data").mkdir()

SPORT = {"key": "sport_score", "label": "Sport score", "unit": "out of 7 · ↑ sportier", "dir": "high", "kind": "num", "d": 0}
columns = [SPORT] + R.COLUMNS

index = []
for g in R.load_grades():
    marks = R.marks(g["oils"])
    marks["sport_score"] = R._extremes([(o["id"], o["sport_score"]) for o in g["oils"]])
    oils = []
    for o in g["oils"]:
        cells = {}
        for c in columns:
            text, sub = R.cell_text(c, o)
            best, worst = marks[c["key"]]
            cells[c["key"]] = {
                "t": text,
                "sub": sub,
                "v": R.sort_value(c, o),
                "m": "best" if o["id"] in best else "worst" if o["id"] in worst else None,
            }
        oils.append({k: o[k] for k in ("id", "name", "sub", "type", "datasheets")} | {"cells": cells})
    ranks = {}
    for key, v in R.rankings(g).items():
        ranks[key] = {
            "title": v["title"],
            "lede": v["lede"],
            "picks": [{"label": label, "name": name} for label, name in v["picks"]],
            "order": [r["id"] for r in v["rows"]],
            "rank": {r["id"]: r["rank"] for r in v["rows"]},
            "pdf": f'downloads/{g["stem"]}-oils-ranked-by-{key}.pdf',
            "png": f'downloads/{g["stem"]}-oils-ranked-by-{key}.png',
        }
    types = [t for t in R.TYPE_LABEL if any(o["type"] == t for o in g["oils"])]
    doc = {k: g[k] for k in ("grade", "slug", "region", "updated", "scope", "notes", "sources")} | {
        "types": [{"id": t, "label": R.TYPE_LABEL[t]} for t in types],
        "columns": columns,
        "rankings": ranks,
        "oils": oils,
    }
    (out / "data" / f'{g["slug"]}.json').write_text(json.dumps(doc, ensure_ascii=False), encoding="utf-8")
    index.append({"grade": g["grade"], "slug": g["slug"], "count": len(oils), "updated": g["updated"]})
    print(f'{g["grade"]}: {len(oils)} oils')

(out / "data" / "grades.json").write_text(json.dumps(index, ensure_ascii=False), encoding="utf-8")
