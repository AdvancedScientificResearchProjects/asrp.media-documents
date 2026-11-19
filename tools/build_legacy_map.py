#!/usr/bin/env python3
"""Keeps links to the previous README's section anchors working, invisibly.

    python3 tools/build_legacy_map.py

The previous README used long bilingual heading anchors (for example
`#-paths-to-money--пути-к-деньгам`). Other pages and repositories may still link to them, so
each of those anchors is kept as an empty `<a name="…">` placed directly above the README
section that now covers the same topic. Nothing is rendered; the README itself does not refer
to its earlier layout. The anchor lines are generated (marker `<!-- legacy-anchors -->`); do
not edit them by hand.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from inventory import inventory  # noqa: E402

ARCHIVE = "archive/README_2026-11-19_pre-showcase.md"
MARK = "<!-- legacy-anchors -->"
# (first line, last line) of the archived README -> heading of the README.md section that covers it
RANGES = [
    (1, 44, "At a glance"), (45, 58, "Quick navigation"), (59, 78, "What this hub is"),
    (79, 99, "Documents by topic"), (100, 111, "Documents catalog"), (112, 137, "Structure"),
    (138, 153, "Security"), (154, 190, "ASRP ecosystem"), (191, 216, "Contact"),
    (217, 237, "Disclaimer"), (238, 241, "Navigation index"),
]
# heading of README.md section -> heading of README.ru.md section
RU = {"At a glance": "Коротко", "Quick navigation": "Быстрая навигация", "What this hub is": "Что это за хаб",
      "Documents by topic": "Документы по темам", "Documents catalog": "Каталог документов", "Structure": "Структура",
      "Security": "Безопасность", "ASRP ecosystem": "Экосистема ASRP", "Contact": "Контакты",
      "Disclaimer": "Отказ от ответственности", "Navigation index": "Навигационный индекс"}


def main():
    heads = inventory(open(ARCHIVE, encoding="utf-8").read())["headings"]
    by_section = {}
    for h in heads:
        for a, b, sec in RANGES:
            if a <= h["line"] <= b:
                by_section.setdefault(sec, []).append(h["anchor"])
    for path, conv in (("README.md", lambda k: "## " + k), ("README.ru.md", lambda k: "## " + RU[k])):
        lines = [ln for ln in open(path, encoding="utf-8").read().split("\n") if not ln.startswith(MARK)]
        out, placed = [], set()
        targets = {conv(k): v for k, v in by_section.items()}
        for ln in lines:
            if ln in targets and ln not in placed:
                placed.add(ln)
                out.append(MARK + "".join('<a name="%s"></a>' % a for a in targets[ln]))
            out.append(ln)
        missing = set(targets) - placed
        if missing:
            raise SystemExit("%s has no section for: %s" % (path, sorted(missing)))
        open(path, "w", encoding="utf-8").write("\n".join(out))
        print("%s: %d legacy anchors kept above %d sections" % (path, sum(len(v) for v in targets.values()), len(placed)))


if __name__ == "__main__":
    main()
