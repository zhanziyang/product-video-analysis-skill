# Codex Execution Guide

The portable scripts live inside `skills/product-video-analysis/scripts/` so they are installed with the skill. The files in this directory provide stable convenience entry points and Codex-specific workflow notes.

## Recommended order

1. Inspect the source video and product identity.
2. Run frame extraction.
3. Run audio analysis.
4. Build the 25-module coverage ledger.
5. Research official product sources when current facts matter.
6. Draft the report manifest and detailed segment pages.
7. Validate the manifest.
8. Generate the PDF using the host's PDF tooling.
9. Render every PDF page to images and visually inspect it.

## Commands

```bash
python codex/frame-extraction.py video.mp4 analysis/frames
python codex/audio-analysis.py video.mp4 analysis/audio.json
python codex/validate-report.py analysis/report.json
```

## Important distinction

Scripts produce measurements and evidence. They do not prove original animation presets, creative intent, software, or layer organization. Those claims remain Estimated or Inferred.
