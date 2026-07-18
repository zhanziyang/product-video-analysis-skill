import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills" / "product-video-analysis" / "scripts" / "validate_report.py"
spec = importlib.util.spec_from_file_location("validate_report", SCRIPT)
module = importlib.util.module_from_spec(spec)
assert spec.loader
spec.loader.exec_module(module)


class ValidateReportTests(unittest.TestCase):
    def load(self, name):
        return json.loads((ROOT / "tests" / "fixtures" / name).read_text())

    def test_complete_report_passes(self):
        self.assertEqual(module.validate(self.load("complete_report.json")), [])

    def test_incomplete_report_reports_structural_failures(self):
        errors = module.validate(self.load("incomplete_report.json"))
        joined = "\n".join(errors)
        self.assertIn("missing evidence labels", joined)
        self.assertIn("missing module 25", joined)
        self.assertIn("screenshots must contain before/middle/after evidence", joined)
        self.assertIn("missing fields", joined)
        self.assertIn("pdfQa.renderedAllPages must be true", joined)


if __name__ == "__main__":
    unittest.main()
