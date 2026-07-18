---
name: product-video-analysis
description: Use when a user asks for a frame-by-frame breakdown of a launch video, product promo, app demo, or motion-design reference, especially when the analysis must cover animation terminology, easing, sound, copy, product strategy, implementation, screenshots, exercises, or an illustrated PDF.
license: MIT
compatibility: Works with general Agent Skills hosts. Python 3.10+, FFmpeg, and FFprobe are recommended for automated frame and audio analysis; PDF creation depends on host tools.
metadata:
  author: zhanziyang
  version: "1.0.0"
---

# Product Video Analysis

## Core principle

Build a complete learning artifact, not a highlight reel. **Adding animation detail never permits removing strategy, narrative, design, implementation, exercise, or evidence modules.**

## Required reading

Before analysis, read:

- `references/full-analysis-standard.md`
- `references/evidence-labeling.md`
- `references/animation-taxonomy.md`
- `references/timing-functions.md`
- `references/sound-design-framework.md`
- `references/product-story-strategy.md`
- `references/pdf-structure.md`
- `references/quality-checklist.md`

Use `templates/analysis-outline.md` as the report contract and `templates/animation-breakdown.md` for every important motion event.

## Workflow

1. **Confirm evidence access.** Obtain the actual video. Do not substitute a generic web result for a missing private file.
2. **Create a coverage ledger.** Copy all 25 required modules from the full standard. Keep the ledger visible until final validation.
3. **Measure before interpreting.** Record duration, dimensions, frame rate, shot changes, dense frame samples, audio transients, silence, and BPM candidates. Use the scripts when available.
4. **Verify product truth.** When the product is identifiable and current information matters, research official sources. Separate official facts from interpretation.
5. **Model the strategy.** Map product truth → communication problem → creative proposition → proof sequence → reveal → close.
6. **Analyze every important motion event.** Name it, describe property changes, estimate duration/frames, classify easing, note anticipation/overshoot/bounce/follow-through, identify sound cues, and explain product relevance.
7. **Use screenshot sequences.** A single still cannot prove timing. Use before/middle/after frames and denser samples for fast actions.
8. **Explain implementation.** Provide plausible AE/Figma/3D/editing/web methods, clearly labeled as inferred when source files are unavailable.
9. **Teach transfer.** Include a simplified recreation, staged exercises, reusable rules, and an example applied to the user's product.
10. **Generate and inspect the PDF.** Render every page to images; check clipping, blank pages, tiny text, missing screenshots, duplicated frames, and unreadable charts.
11. **Validate completeness.** Run `scripts/validate_report.py` against the report manifest. Do not deliver while any required module or shot field is missing.

## Non-negotiable evidence language

Use **Verified**, **Observed**, **Estimated**, and **Inferred** exactly as defined in `references/evidence-labeling.md`. Never present reverse-engineered keyframes, cubic-bezier values, software choices, or creative intent as original production facts.

## Stop conditions

Do not claim a complete report when:

- any of the 25 modules is absent;
- animation analysis lacks screenshot evidence;
- new detail replaced a previously required section;
- inferred technical settings are written as facts;
- the PDF has not been rendered and visually inspected.
