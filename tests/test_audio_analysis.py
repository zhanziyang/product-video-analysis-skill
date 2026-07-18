import importlib.util
import math
import shutil
import struct
import tempfile
import unittest
import wave
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills" / "product-video-analysis" / "scripts" / "audio_analysis.py"
spec = importlib.util.spec_from_file_location("audio_analysis", SCRIPT)
module = importlib.util.module_from_spec(spec)
assert spec.loader
spec.loader.exec_module(module)


@unittest.skipUnless(shutil.which("ffmpeg"), "ffmpeg is required")
class AudioAnalysisTests(unittest.TestCase):
    def test_detects_roughly_120_bpm_click_track(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "clicks.wav"
            sample_rate = 22050
            duration = 8.0
            samples = [0] * int(sample_rate * duration)
            for beat in [i * 0.5 for i in range(int(duration / 0.5))]:
                start = int(beat * sample_rate)
                for j in range(int(0.025 * sample_rate)):
                    if start + j < len(samples):
                        envelope = math.exp(-j / (0.006 * sample_rate))
                        samples[start + j] += int(22000 * envelope * math.sin(2 * math.pi * 1200 * j / sample_rate))
            with wave.open(str(path), "wb") as wav:
                wav.setnchannels(1)
                wav.setsampwidth(2)
                wav.setframerate(sample_rate)
                wav.writeframes(b"".join(struct.pack("<h", max(-32768, min(32767, value))) for value in samples))
            result = module.analyze(path, sample_rate=sample_rate, window_ms=20.0)
            bpms = [item["bpm"] for item in result["bpm_candidates"]]
            self.assertTrue(any(abs(bpm - 120) < 4 for bpm in bpms), bpms)
            self.assertGreaterEqual(len(result["transients"]), 8)


if __name__ == "__main__":
    unittest.main()
