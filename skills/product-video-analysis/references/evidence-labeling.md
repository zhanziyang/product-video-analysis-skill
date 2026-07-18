# Evidence Labeling

Every nontrivial claim must carry one of these labels in the report or its data model.

| Label | Meaning | Acceptable evidence | Example |
|---|---|---|---|
| **Verified** | Confirmed externally or explicitly supplied | Official product site, release notes, creator breakdown, original project file | “OnePay Next is described by OnePay as an internal experimentation mechanism.” |
| **Observed** | Directly visible or measurable | Video frame, waveform, metadata, transcript, rendered UI | “The token scales from small center framing to nearly full frame.” |
| **Estimated** | Numerically reverse-engineered | Frame sampling, waveform analysis, curve fitting, approximate BPM | “Estimated duration: 14 frames; approximate back-out curve.” |
| **Inferred** | Interpretive or production hypothesis | Creative reasoning, likely software, probable layer structure | “The delayed brand reveal likely reduces early advertising resistance.” |

## Rules

1. A screenshot supports what appears, not why it was chosen.
2. Frame sampling can estimate timing but cannot reveal exact keyframe values.
3. A visual resemblance to a named easing is not proof of the original easing preset.
4. Product facts that may have changed require current official verification.
5. If no official source is available, write “I cannot verify this” and keep the claim inferred.
6. Technical suggestions may be presented as recommended implementations, distinct from inferred original implementations.

## Preferred phrasing

- **Observed:** “Between 06.20 and 06.43, the object enlarges and its edge highlight becomes visible.”
- **Estimated:** “The motion resembles a back-out scale entrance with roughly 5–8% overshoot.”
- **Inferred:** “This controlled overshoot likely makes the brand object feel responsive without becoming playful.”
- **Verified:** “The official product page describes the feature as…”
