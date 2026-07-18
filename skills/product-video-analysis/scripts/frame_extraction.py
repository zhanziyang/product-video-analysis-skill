#!/usr/bin/env python3
"""Extract regular and scene-change frames with a manifest.

Requires ffmpeg and ffprobe. Uses only Python's standard library.
"""
from __future__ import annotations

import argparse
import json
import math
import shutil
import subprocess
from pathlib import Path


def run(cmd: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, check=True, text=True, capture_output=True)


def require_binary(name: str) -> None:
    if shutil.which(name) is None:
        raise SystemExit(f"Required binary not found: {name}")


def probe(video: Path) -> dict:
    result = run([
        "ffprobe", "-v", "error", "-select_streams", "v:0",
        "-show_entries", "stream=width,height,avg_frame_rate,r_frame_rate,duration",
        "-show_entries", "format=duration", "-of", "json", str(video),
    ])
    payload = json.loads(result.stdout)
    stream = payload["streams"][0]
    duration = float(stream.get("duration") or payload["format"]["duration"])
    rate_text = stream.get("avg_frame_rate") or stream.get("r_frame_rate") or "0/1"
    numerator, denominator = [float(part) for part in rate_text.split("/")]
    fps = numerator / denominator if denominator else 0.0
    return {
        "duration_seconds": duration,
        "fps": fps,
        "width": int(stream["width"]),
        "height": int(stream["height"]),
    }


def timestamp_name(seconds: float) -> str:
    millis = int(round(seconds * 1000))
    return f"t_{millis:08d}ms.jpg"


def extract_at(video: Path, output: Path, seconds: float, width: int) -> None:
    run([
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
        "-ss", f"{seconds:.3f}", "-i", str(video), "-frames:v", "1",
        "-vf", f"scale={width}:-2", "-q:v", "2", str(output),
    ])


def detect_scene_times(video: Path, threshold: float) -> list[float]:
    cmd = [
        "ffmpeg", "-hide_banner", "-i", str(video), "-an", "-sn",
        "-vf", f"scale=320:-2,select='gt(scene,{threshold})',showinfo", "-f", "null", "-",
    ]
    proc = subprocess.run(cmd, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    times: list[float] = []
    for line in proc.stderr.splitlines():
        marker = "pts_time:"
        if marker not in line:
            continue
        raw = line.split(marker, 1)[1].split()[0]
        try:
            times.append(float(raw))
        except ValueError:
            continue
    return times


def unique_times(values: list[float], duration: float, min_gap: float = 0.04) -> list[float]:
    cleaned = sorted(max(0.0, min(duration, value)) for value in values)
    result: list[float] = []
    for value in cleaned:
        if not result or value - result[-1] >= min_gap:
            result.append(value)
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("video", type=Path)
    parser.add_argument("output_dir", type=Path)
    parser.add_argument("--interval", type=float, default=0.5, help="Regular sampling interval in seconds")
    parser.add_argument("--scene-threshold", type=float, default=0.30)
    parser.add_argument("--scene-padding", type=float, default=0.12, help="Frames before and after each detected cut")
    parser.add_argument("--width", type=int, default=1280)
    args = parser.parse_args()

    require_binary("ffmpeg")
    require_binary("ffprobe")
    if not args.video.exists():
        raise SystemExit(f"Video not found: {args.video}")
    if args.interval <= 0:
        raise SystemExit("--interval must be greater than zero")

    metadata = probe(args.video)
    duration = metadata["duration_seconds"]
    fps = metadata["fps"] or 30.0
    # Seeking exactly to container duration can land after the final decodable frame.
    sample_end = max(0.0, duration - max(0.10, 3.0 / fps))
    regular_count = int(math.floor(sample_end / args.interval)) + 1
    regular_times = [min(sample_end, i * args.interval) for i in range(regular_count)]
    if regular_times[-1] < sample_end - 0.02:
        regular_times.append(sample_end)

    scene_times = detect_scene_times(args.video, args.scene_threshold)
    dense_times: list[float] = []
    for cut in scene_times:
        dense_times.extend([cut - args.scene_padding, cut, cut + args.scene_padding])

    samples = unique_times(regular_times + dense_times, sample_end)
    frames_dir = args.output_dir / "frames"
    frames_dir.mkdir(parents=True, exist_ok=True)

    manifest_samples = []
    for seconds in samples:
        filename = timestamp_name(seconds)
        destination = frames_dir / filename
        extract_at(args.video, destination, seconds, args.width)
        manifest_samples.append({
            "time_seconds": round(seconds, 3),
            "timecode": f"{int(seconds // 60):02d}:{seconds % 60:06.3f}",
            "file": str(destination.relative_to(args.output_dir)),
            "kind": "scene-dense" if any(abs(seconds - t) <= args.scene_padding + 0.001 for t in scene_times) else "regular",
        })

    manifest = {
        "source": str(args.video),
        "metadata": metadata,
        "settings": {
            "interval_seconds": args.interval,
            "scene_threshold": args.scene_threshold,
            "scene_padding_seconds": args.scene_padding,
            "output_width": args.width,
        },
        "detected_scene_times": [round(t, 3) for t in scene_times],
        "samples": manifest_samples,
    }
    args.output_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = args.output_dir / "frame_manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"Extracted {len(samples)} frames to {frames_dir}")
    print(f"Manifest: {manifest_path}")


if __name__ == "__main__":
    main()
