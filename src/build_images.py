"""Writes one HTML page per grade and ranking to the given folder; render.sh prints them to PDF and PNG."""
import html
import sys
from pathlib import Path

import rankings as R

out_dir = Path(sys.argv[1])
out_dir.mkdir(parents=True, exist_ok=True)
tpl = (R.ROOT / "src" / "template.html").read_text(encoding="utf-8")
esc = html.escape


def table(rows, marks):
    head = "".join(f'<th class="c-{c["key"]}">{esc(c["label"])}<span class="unit">{esc(c["unit"])}</span></th>' for c in R.COLUMNS)
    body = []
    for r in rows:
        tds = []
        for c in R.COLUMNS:
            best, worst = marks[c["key"]]
            cls = "best" if r["id"] in best else "worst" if r["id"] in worst else ""
            text, sub = R.cell_text(c, r)
            inner = esc(text) + (f'<span class="sub">{esc(sub)}</span>' if sub else "")
            if text == "—":
                cls = (cls + " na").strip()
            tds.append(f'<td class="{cls} c-{c["key"]}">{inner}</td>')
        rank = r["rank"]
        badge = "ref" if rank is None else "top" if rank <= 3 else "rest"
        body.append(
            f'<tr><td class="c-rank"><div class="rank {badge}">{rank if rank is not None else "–"}</div></td>'
            f'<td class="c-name"><div class="name">{esc(r["name"])}</div>'
            f'<div class="sub">{esc(r["sub"])}</div></td>{"".join(tds)}</tr>'
        )
    return head, "\n".join(body)


for g in R.load_grades():
    marks = R.marks(g["oils"])
    for key, v in R.rankings(g).items():
        rows = v["rows"]
        if key == "performance":
            for r in rows:
                if r["sport_score"] is not None:
                    r["sub"] = f'{r["sub"]} · sport score {r["sport_score"]}/7'
        head, body = table(rows, marks)
        picks = "".join(f'<div class="pick"><b>{esc(label)}:</b> {esc(name)}</div>' for label, name in v["picks"])
        page = (tpl.replace("{{HEAD}}", head).replace("{{BODY}}", body).replace("{{PICKS}}", picks)
                .replace("{{TITLE}}", esc(v["title"])).replace("{{LEDE}}", esc(v["lede"]))
                .replace("{{GRADE}}", esc(g["grade"])).replace("{{PRICE_NOTE}}", esc(g["notes"]["prices"]))
                .replace("{{EXCLUDED}}", esc(g["notes"]["excluded"])).replace("{{SOURCES}}", esc(g["sources"])))
        name = f'{g["stem"]}-oils-ranked-by-{key}'
        (out_dir / f"{name}.html").write_text(page, encoding="utf-8")
        print(name, [(r["rank"], r["name"]) for r in rows])
