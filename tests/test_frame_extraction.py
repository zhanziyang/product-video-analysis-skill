import json
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills" / "product-video-analysis" / "scripts" / "frame_extraction.py"


@unittest.skipUnless(shutil.which("ffmpeg") and shutil.which("ffprobe"), "ffmpeg and ffprobe are required")
class FrameExtractionTests(unittest.TestCase):
    def test_extracts_regular_frames_and_manifest(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            temp = Path(temp_dir)
            video = temp / "test.mp4"
            subprocess.run([
                "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
                "-f", "lavfi", "-i", "color=c=red:s=320x180:d=1:r=30",
                "-f", "lavfi", "-i", "color=c=blue:s=320x180:d=1:r=30",
                "-filter_complex", "[0:v][1:v]concat=n=2:v=1:a=0[out]",
                "-map", "[out]", "-c:v", "libx264", "-pix_fmt", "yuv420p", str(video),
            ], check=True)
            output = temp / "analysis"
            subprocess.run([
                "python", str(SCRIPT), str(video), str(output),
                "--interval", "0.5", "--width", "320", "--scene-threshold", "0.1",
            ], check=True)
            manifest = json.loads((output / "frame_manifest.json").read_text())
            self.assertAlmostEqual(manifest["metadata"]["duration_seconds"], 2.0, delta=0.1)
            self.assertGreaterEqual(len(manifest["samples"]), 5)
            for sample in manifest["samples"]:
                self.assertTrue((output / sample["file"]).exists())


if __name__ == "__main__":
    unittest.main()
