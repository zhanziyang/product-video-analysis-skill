import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = ROOT / "skills" / "product-video-analysis"


class SkillStructureTests(unittest.TestCase):
    def test_skill_frontmatter_and_required_references(self):
        text = (SKILL_ROOT / "SKILL.md").read_text()
        self.assertTrue(text.startswith("---\n"))
        self.assertRegex(text, r"(?m)^name: product-video-analysis$")
        self.assertRegex(text, r"(?m)^description: Use when ")
        references = [
            "full-analysis-standard.md", "evidence-labeling.md", "animation-taxonomy.md",
            "timing-functions.md", "sound-design-framework.md", "product-story-strategy.md",
            "pdf-structure.md", "quality-checklist.md",
        ]
        for filename in references:
            self.assertIn(filename, text)
            self.assertTrue((SKILL_ROOT / "references" / filename).exists())

    def test_full_standard_has_all_numbered_modules(self):
        text = (SKILL_ROOT / "references" / "full-analysis-standard.md").read_text()
        headings = re.findall(r"^## (\d+)\.", text, flags=re.MULTILINE)
        self.assertEqual([int(value) for value in headings], list(range(1, 26)))

    def test_referenced_relative_files_exist(self):
        text = (SKILL_ROOT / "SKILL.md").read_text()
        paths = re.findall(r"`((?:references|templates)/[^`]+)`", text)
        for relative in paths:
            self.assertTrue((SKILL_ROOT / relative).exists(), relative)


if __name__ == "__main__":
    unittest.main()
