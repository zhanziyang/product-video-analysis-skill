#!/usr/bin/env python3
import subprocess
from pathlib import Path

root = Path(__file__).resolve().parents[1]
script = root / "skills" / "product-video-analysis" / "scripts" / "validate_report.py"
complete = root / "tests" / "fixtures" / "complete_report.json"
incomplete = root / "tests" / "fixtures" / "incomplete_report.json"

subprocess.run(["python", str(script), str(complete)], check=True)
failed = subprocess.run(["python", str(script), str(incomplete)], check=False)
if failed.returncode == 0:
    raise SystemExit("Expected incomplete report validation to fail")
print("Validation fixture checks passed.")
