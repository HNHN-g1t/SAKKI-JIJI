"""data/questions.json を src/template.html に埋めこんで index.html を作る。

使い方:  python3 apps/jiji-quiz/tools/build.py   （Windows は py -3）
問題データの形もここで確かめる（おかしければ止まる）。
"""
import json
import sys
from pathlib import Path

APP = Path(__file__).resolve().parent.parent
data = json.loads((APP / "data/questions.json").read_text(encoding="utf-8"))

errors = []
cats = {c["id"] for c in data["courses"]}
ids = set()
for q in data["questions"]:
    qid = q.get("id", "?")
    for k in ("id", "cat", "when", "q", "choices", "exp", "link", "src", "checked"):
        if not q.get(k):
            errors.append(f"{qid}: {k} がない")
    if qid in ids:
        errors.append(f"{qid}: id が重複")
    ids.add(qid)
    if q.get("cat") not in cats:
        errors.append(f"{qid}: cat「{q.get('cat')}」がコースにない")
    if q.get("area") not in ("jp", "world"):
        errors.append(f"{qid}: area は jp か world")
    ch = q.get("choices", [])
    if len(ch) != 4 or len(set(ch)) != 4:
        errors.append(f"{qid}: 選択肢はちがう4つにする")
for c in cats:
    if not any(q["cat"] == c for q in data["questions"]):
        errors.append(f"コース {c} に問題がない")
if errors:
    print("\n".join(errors))
    sys.exit(1)

payload = {"courses": data["courses"], "questions": data["questions"]}
js = json.dumps(payload, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
tpl = (APP / "src/template.html").read_text(encoding="utf-8")
assert tpl.count("/*__DATA__*/null") == 1
(APP / "index.html").write_text(tpl.replace("/*__DATA__*/null", js), encoding="utf-8", newline="\n")
print(f"wrote apps/jiji-quiz/index.html（{len(data['questions'])}問・{len(cats)}コース）")
