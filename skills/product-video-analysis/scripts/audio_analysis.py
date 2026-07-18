#!/usr/bin/env python3
"""Analyze audio energy, transients, silence, and BPM candidates.

The script converts input audio/video to mono 16-bit PCM with FFmpeg, then uses
only Python's standard library for windowed RMS and autocorrelation.
"""
from __future__ import annotations

import argparse
import array
import json
import math
import shutil
import statistics
import subprocess
import tempfile
import wave
from pathlib import Path


def require_binary(name: str) -> None:
    if shutil.which(name) is None:
        raise SystemExit(f"Required binary not found: {name}")


def convert_to_wav(source: Path, destination: Path, sample_rate: int) -> None:
    subprocess.run([
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(source),
        "-vn", "-ac", "1", "-ar", str(sample_rate), "-c:a", "pcm_s16le", str(destination),
    ], check=True)


def read_pcm(path: Path) -> tuple[int, list[int]]:
    with wave.open(str(path), "rb") as wav:
        if wav.getsampwidth() != 2 or wav.getnchannels() != 1:
            raise ValueError("Expected mono 16-bit PCM WAV")
        sample_rate = wav.getframerate()
        samples = array.array("h", wav.readframes(wav.getnframes()))
    return sample_rate, samples.tolist()


def rms_windows(samples: list[int], sample_rate: int, window_ms: float) -> list[float]:
    size = max(1, int(sample_rate * window_ms / 1000.0))
    values = []
    for start in range(0, len(samples), size):
        chunk = samples[start:start + size]
        if not chunk:
            break
        mean_square = sum(value * value for value in chunk) / len(chunk)
        values.append(math.sqrt(mean_square) / 32768.0)
    return values


def percentile(values: list[float], q: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    index = min(len(ordered) - 1, max(0, int(round((len(ordered) - 1) * q))))
    return ordered[index]


def onset_envelope(rms: list[float]) -> list[float]:
    return [0.0] + [max(0.0, rms[i] - rms[i - 1]) for i in range(1, len(rms))]


def detect_transients(envelope: list[float], window_seconds: float) -> list[dict]:
    positive = [value for value in envelope if value > 0]
    threshold = percentile(positive, 0.50)
    if threshold <= 0:
        return []
    events = []
    last_index = -9999
    minimum_gap = max(1, int(0.08 / window_seconds))
    for index, value in enumerate(envelope):
        if value >= threshold and index - last_index >= minimum_gap:
            events.append({"time_seconds": round(index * window_seconds, 3), "strength": round(value, 6)})
            last_index = index
    return events


def detect_silence(rms: list[float], window_seconds: float, threshold_db: float, min_duration: float) -> list[dict]:
    amplitude_threshold = 10 ** (threshold_db / 20.0)
    minimum_windows = max(1, int(math.ceil(min_duration / window_seconds)))
    regions = []
    start = None
    for index, value in enumerate(rms + [1.0]):
        silent = value <= amplitude_threshold
        if silent and start is None:
            start = index
        if not silent and start is not None:
            if index - start >= minimum_windows:
                regions.append({
                    "start_seconds": round(start * window_seconds, 3),
                    "end_seconds": round(index * window_seconds, 3),
                    "duration_seconds": round((index - start) * window_seconds, 3),
                })
            start = None
    return regions


def autocorrelation_bpm(envelope: list[float], window_seconds: float, min_bpm: int, max_bpm: int) -> list[dict]:
    if len(envelope) < 8 or max(envelope, default=0.0) <= 0:
        return []
    mean = statistics.fmean(envelope)
    centered = [value - mean for value in envelope]
    min_lag = max(1, int(round(60.0 / max_bpm / window_seconds)))
    max_lag = min(len(centered) - 1, int(round(60.0 / min_bpm / window_seconds)))
    scores = []
    for lag in range(min_lag, max_lag + 1):
        score = sum(centered[i] * centered[i - lag] for i in range(lag, len(centered)))
        normalization = math.sqrt(
            sum(centered[i] ** 2 for i in range(lag, len(centered))) *
            sum(centered[i - lag] ** 2 for i in range(lag, len(centered)))
        )
        normalized = score / normalization if normalization else 0.0
        bpm = 60.0 / (lag * window_seconds)
        scores.append((normalized, bpm, lag))
    scores.sort(reverse=True)
    candidates = []
    for score, bpm, lag in scores:
        if all(abs(bpm - item["bpm"]) > 2.5 for item in candidates):
            candidates.append({"bpm": round(bpm, 2), "confidence": round(max(0.0, score), 4), "lag_windows": lag})
        if len(candidates) == 5:
            break
    return candidates


def analyze(source: Path, sample_rate: int = 22050, window_ms: float = 20.0) -> dict:
    require_binary("ffmpeg")
    with tempfile.TemporaryDirectory() as temp_dir:
        wav_path = Path(temp_dir) / "audio.wav"
        convert_to_wav(source, wav_path, sample_rate)
        actual_rate, samples = read_pcm(wav_path)
    rms = rms_windows(samples, actual_rate, window_ms)
    window_seconds = window_ms / 1000.0
    envelope = onset_envelope(rms)
    duration = len(samples) / actual_rate if actual_rate else 0.0
    peak_rms = max(rms, default=0.0)
    mean_rms = statistics.fmean(rms) if rms else 0.0
    return {
        "source": str(source),
        "duration_seconds": round(duration, 3),
        "sample_rate": actual_rate,
        "window_ms": window_ms,
        "levels": {
            "mean_rms": round(mean_rms, 6),
            "peak_rms": round(peak_rms, 6),
            "mean_dbfs": round(20 * math.log10(max(mean_rms, 1e-9)), 2),
            "peak_dbfs": round(20 * math.log10(max(peak_rms, 1e-9)), 2),
        },
        "transients": detect_transients(envelope, window_seconds),
        "silence_regions": detect_silence(rms, window_seconds, threshold_db=-42.0, min_duration=0.25),
        "bpm_candidates": autocorrelation_bpm(envelope, window_seconds, min_bpm=60, max_bpm=180),
        "note": "BPM and transient results are estimates and should be checked against the soundtrack by ear.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--sample-rate", type=int, default=22050)
    parser.add_argument("--window-ms", type=float, default=20.0)
    args = parser.parse_args()
    if not args.source.exists():
        raise SystemExit(f"Source not found: {args.source}")
    report = analyze(args.source, args.sample_rate, args.window_ms)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"Audio analysis written to {args.output}")


if __name__ == "__main__":
    main()
