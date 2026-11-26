#!/usr/bin/env python3
"""Checks for the free Anti-Slop Rules pack. Run: python3 tests/test_free.py"""
import os
import re
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def prose(text):
    text = re.sub(r"(?s)```.*?```", "", text)
    return re.sub(r"`[^`\n]*`", "", text)


class TestFree(unittest.TestCase):
    def files(self):
        for dp, _, fn in os.walk(ROOT):
            for f in fn:
                if f.endswith((".md", ".mdc")):
                    yield os.path.join(dp, f)

    def test_skill_frontmatter(self):
        t = open(os.path.join(ROOT, "skills", "de-slop-lite", "SKILL.md"), encoding="utf-8").read()
        m = re.match(r"---\nname: de-slop-lite\ndescription: (.+?)\n---\n", t, re.S)
        self.assertTrue(m)

    def test_cursor_rule_frontmatter(self):
        t = open(os.path.join(ROOT, "templates", "anti-slop.mdc"), encoding="utf-8").read()
        self.assertTrue(t.startswith("---\ndescription:"))
        self.assertIn("globs:", t.split("---")[1])

    def test_no_em_dashes_or_hype_in_our_prose(self):
        banned = ["\u2014", "blazing fast", "game-changer", "seamless", "delve", "certainly!"]
        for p in self.files():
            text = prose(open(p, encoding="utf-8").read()).lower()
            for b in banned:
                self.assertNotIn(b, text, f"{b!r} in {p}")

    def test_rule_count(self):
        t = open(os.path.join(ROOT, "slop-rules.md"), encoding="utf-8").read()
        self.assertEqual(len(re.findall(r"(?m)^\d+\. ", t)), 12)


if __name__ == "__main__":
    unittest.main()
