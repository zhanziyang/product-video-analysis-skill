# Product Video Analysis Skill

A reusable Agent Skill for turning launch videos, product promos, app demos, and motion-design references into complete, illustrated learning reports.

The defining rule is simple:

> New detail must extend the analysis. It must never silently replace an existing module.

This repository packages the full standard used to create the 63-page OnePay Next breakdown: product strategy, narrative, copy, sound, animation naming, estimated easing, frame evidence, implementation guidance, exercises, and PDF quality control.

## What it covers

- Product background and communication objective
- Creative proposition and underlying planning logic
- Full narrative and copy architecture
- Music, voice-over, sound effects, tempo, and motion density
- Timecoded screenshots and dense sampling around fast animation
- Animation names such as scale pop, back-out overshoot, masked wipe, zoom-through, match cut, type-on, text scramble, carousel, parallax, odometer, and light sweep
- Estimated duration, frame count, property changes, easing family, cubic-bezier approximation, anticipation, overshoot, bounce, and follow-through
- Why the motion, copy, and sound fit the product's actual characteristics
- After Effects, Figma, 3D, editing, and web implementation approaches
- Simplified recreations, staged exercises, and transfer to another product
- Rendered-PDF inspection and report validation

## Install

List the skill first:

```bash
npx skills add zhanziyang/product-video-analysis-skill --list
```

Install only this skill globally for Codex:

```bash
npx skills add zhanziyang/product-video-analysis-skill   --skill product-video-analysis   -g -a codex -y
```

Install for multiple supported agents:

```bash
npx skills add zhanziyang/product-video-analysis-skill   --skill product-video-analysis   -g -a codex -a claude-code -a cursor -y
```

Local development installation:

```bash
npx skills add ./product-video-analysis-skill   --skill product-video-analysis -a codex -y
```

## Example prompt

```text
Use the product-video-analysis skill to create a complete illustrated
frame-by-frame breakdown of this product launch video.

Preserve every module in the full analysis standard. Identify animation
names, estimated timing curves, sound cues, copy strategy, product-feature
mapping, implementation methods, staged recreation exercises, and produce
a visually verified PDF.
```

## Repository layout

```text
skills/product-video-analysis/
  SKILL.md
  references/             Deep analysis standards and taxonomies
  templates/              Report and shot-level contracts
  examples/               Condensed worked example
  scripts/                Portable FFmpeg/Python helpers
codex/                     Codex-specific execution notes and wrappers
tests/                     Structural, validator, audio, and video tests
docs/                      Methodology, design spec, and implementation plan
```

## Quick workflow

```bash
python skills/product-video-analysis/scripts/frame_extraction.py video.mp4 analysis/frames
python skills/product-video-analysis/scripts/audio_analysis.py video.mp4 analysis/audio.json
python skills/product-video-analysis/scripts/validate_report.py report.json
```

The scripts automate evidence gathering. They do not determine the creator's actual intent or original project settings. Those remain interpretations and must be labeled accordingly.

## Evidence labels

Every claim uses one of four labels:

- **Verified** — supported by an official product source or explicit source material
- **Observed** — directly visible or measurable in the supplied video/audio
- **Estimated** — reverse-engineered timing, values, BPM, frame counts, or curves
- **Inferred** — interpretation of creative intent, software choice, or production structure

## Requirements

- Python 3.10+
- FFmpeg and FFprobe for the Codex helper scripts
- A PDF generation route available to the host agent
- Web access only when product background requires verification

The core skill remains useful without the scripts, but mechanical frame/audio analysis will be less precise.

## Testing

```bash
python -m unittest discover -s tests -v
python tests/run-validation.py
```

The CI suite checks skill structure, required analysis modules, video frame extraction, click-track BPM estimation, and report validation.

## Limits

This skill reverse-engineers completed videos. It cannot verify hidden source-project details unless the original files or creator documentation are provided. Cubic-bezier values, exact keyframes, software choices, and sound libraries must be presented as estimates or inferences.

## License

MIT. Publicly usable and modifiable. This repository is maintained by its owner; external contributions are not assumed to be accepted.
