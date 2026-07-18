#!/usr/bin/env python3
from pathlib import Path
import runpy

script = Path(__file__).resolve().parents[1] / "skills" / "product-video-analysis" / "scripts" / "frame_extraction.py"
runpy.run_path(str(script), run_name="__main__")
