"""Regression gate of the showcase. Run from the repository root:  python3 -I -m unittest discover -s tests -v"""
import json
import os
import re
import subprocess
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import facts as factsmod  # noqa: E402

ENV = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
PAGES = ["README.md", "README.ru.md"] + ["guide/" + n for n in sorted(os.listdir(os.path.join(ROOT, "guide"))) if n.endswith(".md")]


def read(p):
    return open(os.path.join(ROOT, p), encoding="utf-8").read()


def run(*a):
    return subprocess.run([sys.executable, "-I"] + list(a), cwd=ROOT, capture_output=True, text=True, env=ENV)


class ShowcaseTest(unittest.TestCase):
    def test_no_loss_hard_checks_pass(self):
        r = run("tools/verify_no_loss.py")
        self.assertEqual(r.returncode, 0, r.stdout[-2000:])
        self.assertIn("RESULT: PASS", r.stdout)

    def test_archive_is_byte_identical_to_tag(self):
        old = subprocess.run(["git", "show", "pre-showcase-2026-11:README.md"], cwd=ROOT, capture_output=True).stdout
        self.assertEqual(old, open(os.path.join(ROOT, "archive/README_2026-11-19_pre-showcase.md"), "rb").read())

    def test_visuals_build_and_are_in_sync(self):
        d = os.path.join(ROOT, "guide", "assets")
        snap = {}
        for dp, _, fs in os.walk(d):
            for f in fs:
                snap[os.path.join(dp, f)] = open(os.path.join(dp, f), "rb").read()
        r = run("tools/build_visuals.py")
        self.assertEqual(r.returncode, 0, r.stdout[-1500:] + r.stderr[-1500:])
        for p, b in snap.items():
            self.assertEqual(b, open(p, "rb").read(), "generated file drifted: " + p)

    def test_every_diagram_has_twin_and_metadata(self):
        d = os.path.join(ROOT, "guide", "assets", "diagrams")
        names = os.listdir(d)
        for n in names:
            twin = n.replace(".en.svg", ".ru.svg") if n.endswith(".en.svg") else n.replace(".ru.svg", ".en.svg")
            self.assertIn(twin, names)
            svg = read("guide/assets/diagrams/" + n)
            for need in ("<title", "<desc", "viewBox", 'role="img"'):
                self.assertIn(need, svg)

    def test_numbers_match_computed_facts(self):
        F = factsmod.facts()
        self.assertEqual((F["docs"], F["topics"], F["published"], F["todo"], F["image_meta"]), (29, 9, 4, 25, 36))
        for page in ("README.md", "README.ru.md"):
            t = read(page)
            for token in ("29", "9", "18", "2", "25", "36"):
                self.assertTrue(re.search(r"\b%s\b" % token, t), page + " lacks " + token)
        for slug, n in F["topics_by_slug"].items():
            self.assertTrue(re.search(r"\[`topics/%s\.md`\]" % re.escape(slug), read("README.md")))
            self.assertTrue(re.search(r"\| %d \| \[`topics/%s\.md`\]" % (n, re.escape(slug)), read("README.md")), slug)

    def test_no_forbidden_wording_or_pii(self):
        banned = re.compile(r"ASRP memory|memory records|owner ruling|решение владельца|memory-policy|asrp\.memory", re.I)
        patent_bad = re.compile(r"patent (was |is |has been )?(granted|issued)|выдан[а-я]* патент|in force|действителен", re.I)
        for p in PAGES + ["tools/waivers.json"]:
            t = read(p)
            self.assertIsNone(banned.search(t), p)
            self.assertIsNone(patent_bad.search(t), p)
            self.assertEqual(set(re.findall(r"[\w.+-]+@[\w-]+\.[\w.-]+", t)) - {"info@asrp.tech"}, set(), p)
            self.assertNotRegex(t, r"private repository|приватный репозиторий")

    def test_links_resolve(self):
        r = run("tools/verify_no_loss.py")
        self.assertIn("H7_broken_links                  0", r.stdout)


if __name__ == "__main__":
    unittest.main()
