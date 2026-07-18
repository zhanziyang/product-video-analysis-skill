#!/usr/bin/env python3
"""Validate a product-video analysis manifest without third-party packages."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

REQUIRED_MODULES = {
    1: "Product background and core value",
    2: "Communication objective",
    3: "Creative proposition",
    4: "Planning logic",
    5: "Full narrative structure",
    6: "Copy architecture",
    7: "Music, sound effects, and voice-over",
    8: "Tempo and motion-density map",
    9: "Timecoded screenshot breakdown",
    10: "Animation terminology",
    11: "Property changes",
    12: "Estimated duration and frame count",
    13: "Timing function and graph shape",
    14: "Motion principles",
    15: "Composition, typography, color, and depth",
    16: "Transition system",
    17: "Motion-to-product mapping",
    18: "Copy-image-motion-sound coordination",
    19: "Implementation methods",
    20: "Project organization",
    21: "Simplified recreation",
    22: "Staged training plan",
    23: "Transferable methodology",
    24: "Application to the user's product",
    25: "Continuous-frame appendix",
}
REQUIRED_EVIDENCE_LABELS = {"Verified", "Observed", "Estimated", "Inferred"}
REQUIRED_ANIMATION_FIELDS = {
    "name", "evidence", "properties", "durationSeconds", "durationFrames",
    "timingFamily", "soundCue", "productMeaning",
}


def validate(data: dict) -> list[str]:
    errors: list[str] = []
    if not str(data.get("title", "")).strip():
        errors.append("title is required")

    source = data.get("source")
    if not isinstance(source, dict):
        errors.append("source must be an object")
    else:
        for key in ("durationSeconds", "fps"):
            value = source.get(key)
            if not isinstance(value, (int, float)) or value <= 0:
                errors.append(f"source.{key} must be greater than zero")

    labels = set(data.get("evidenceLabels", []))
    missing_labels = REQUIRED_EVIDENCE_LABELS - labels
    if missing_labels:
        errors.append(f"missing evidence labels: {', '.join(sorted(missing_labels))}")

    modules = data.get("modules")
    if not isinstance(modules, list):
        errors.append("modules must be a list")
    else:
        by_id = {item.get("id"): item for item in modules if isinstance(item, dict)}
        for module_id, title in REQUIRED_MODULES.items():
            item = by_id.get(module_id)
            if item is None:
                errors.append(f"missing module {module_id}: {title}")
            elif item.get("status") != "complete":
                errors.append(f"module {module_id} is not complete: {title}")

    shots = data.get("shots")
    if not isinstance(shots, list) or not shots:
        errors.append("shots must be a non-empty list")
    else:
        for index, shot in enumerate(shots):
            prefix = f"shots[{index}]"
            if not isinstance(shot, dict):
                errors.append(f"{prefix} must be an object")
                continue
            screenshots = shot.get("screenshots")
            if not isinstance(screenshots, list) or len(screenshots) < 3:
                errors.append(f"{prefix}.screenshots must contain before/middle/after evidence")
            if not str(shot.get("productMapping", "")).strip():
                errors.append(f"{prefix}.productMapping is required")
            animations = shot.get("animations")
            if not isinstance(animations, list) or not animations:
                errors.append(f"{prefix}.animations must be non-empty")
                continue
            for animation_index, animation in enumerate(animations):
                aprefix = f"{prefix}.animations[{animation_index}]"
                if not isinstance(animation, dict):
                    errors.append(f"{aprefix} must be an object")
                    continue
                missing = REQUIRED_ANIMATION_FIELDS - set(animation)
                if missing:
                    errors.append(f"{aprefix} missing fields: {', '.join(sorted(missing))}")
                if animation.get("evidence") not in {"Observed", "Estimated", "Inferred"}:
                    errors.append(f"{aprefix}.evidence must be Observed, Estimated, or Inferred")
                if not isinstance(animation.get("properties"), list) or not animation.get("properties"):
                    errors.append(f"{aprefix}.properties must be a non-empty list")

    pdf_qa = data.get("pdfQa")
    if not isinstance(pdf_qa, dict):
        errors.append("pdfQa must be an object")
    else:
        for key in ("renderedAllPages", "noOverflow", "screenshotsLegible"):
            if pdf_qa.get(key) is not True:
                errors.append(f"pdfQa.{key} must be true")
    return errors


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    args = parser.parse_args()
    data = json.loads(args.manifest.read_text(encoding="utf-8"))
    errors = validate(data)
    if errors:
        print("Report validation failed:")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)
    print("Report validation passed: all required modules, shot fields, evidence labels, and PDF QA flags are complete.")


if __name__ == "__main__":
    main()
