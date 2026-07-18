# Timing Functions and Curve Estimation

Timing values in a finished video are reverse-engineered estimates unless source keyframes are provided.

## Common easing families

| Name | Approximate cubic-bezier | Graph character | Typical use |
|---|---|---|---|
| Linear | `(0, 0, 1, 1)` | Constant velocity | Mechanical scroll, data flow, background drift |
| Standard ease | `(0.25, 0.1, 0.25, 1)` | Gentle acceleration and deceleration | Neutral UI movement |
| Ease-out | `(0.16, 1, 0.3, 1)` | Fast start, long settle | Entrances, camera landing |
| Ease-in | `(0.7, 0, 0.84, 0)` | Slow start, fast exit | Exits, launches |
| Ease-in-out | `(0.65, 0, 0.35, 1)` | Symmetrical S curve | Repositioning, scene moves |
| Sharp ease-out | `(0.22, 1, 0.36, 1)` | Immediate response, controlled stop | Product UI, scale/position entrances |
| Expo-like ease-out | `(0.19, 1, 0.22, 1)` | Very fast initial change, soft tail | Premium camera pushes, reveals |
| Back-out approximation | `(0.34, 1.56, 0.64, 1)` | Crosses target, returns once | Pop, sticker, confirmation |
| Back-in approximation | `(0.36, 0, 0.66, -0.56)` | Small reverse anticipation, then exit | Energetic removal |

Cubic-bezier cannot represent a true multi-bounce spring. For bounce, elastic, or physical spring behavior, describe the successive extrema or use a spring model.

## Spring description

When a spring is more appropriate, report:

- initial displacement;
- target value;
- number of crossings;
- approximate damping: low, medium, high;
- estimated settle time;
- peak overshoot percentage;
- whether velocity appears continuous at edit boundaries.

Example:

```text
Estimated: scale 82% → 106% → 99% → 100% over 16 frames.
Classification: highly damped spring / back-out approximation.
The target is crossed twice, so “bounce” is defensible; if crossed once, prefer “overshoot.”
```

## Duration guide

| Motion | 24 fps | 30 fps | 60 fps | Typical perception |
|---|---:|---:|---:|---|
| UI click response | 2–5 f | 3–6 f | 5–12 f | Immediate |
| Micro entrance | 6–10 f | 8–13 f | 15–26 f | Snappy |
| Standard entrance | 10–18 f | 12–22 f | 24–44 f | Readable |
| Camera transition | 12–30 f | 15–38 f | 30–75 f | Cinematic |
| Logo settle | 18–48 f | 22–60 f | 45–120 f | Deliberate |

These are diagnostic ranges, not mandatory recipes.

## Estimation workflow

1. Identify the first frame with measurable departure from rest.
2. Identify the first stable target frame.
3. Sample at least 4–7 intermediate frames for simple easing; more for springs.
4. Measure normalized progress for position, scale, or opacity.
5. Plot progress against normalized time.
6. Classify the family before offering a cubic-bezier approximation.
7. State uncertainty caused by motion blur, cuts, retiming, or sparse sampling.

## After Effects Graph Editor interpretation

- A steep speed graph at the beginning and a long tail suggests ease-out.
- A value graph that crosses the target suggests overshoot.
- Multiple shrinking crossings suggest a damped spring or bounce.
- A flat segment followed by a sudden change suggests hold or stepped interpolation.
- Different axes may use different timing; do not assume a single curve controls everything.
