# Condensed Worked Example: OnePay Next

This excerpt demonstrates evidence separation and shot-level detail. It is not the complete report.

## Product truth

- **Verified:** OnePay described OnePay Next as a mechanism for rapidly testing new ideas with small teams and real users.
- **Inferred:** A concept-led film is suitable because the product proposition concerns experimentation and organizational speed, not only a single interface feature.

## Creative proposition

**Inferred:** “The best financial products begin as simple ideas that become more curious, intuitive, and personal through experimentation.”

## Segment: idea resolves into brand token

- **Time range:** approximately 04.90–07.10
- **Observed:** Code-like braces and symbols contract around a small blue circular object. The object enlarges, gains dimensional shading, and takes over the frame.
- **Common names:** object continuity; 2D-to-3D handoff; scale-up reveal; camera/scale push; light-material reveal.
- **Estimated properties:** scale roughly 12% → 100%+, opacity 0 → 100%, 3D Y rotation begins after the object becomes dominant, background exposure falls.
- **Estimated timing:** about 1.0–1.4 seconds for the main enlargement; strong ease-out with a soft settle. No clear multi-rebound bounce.
- **Estimated curve:** expo-like ease-out, approximately `cubic-bezier(0.19, 1, 0.22, 1)` for the scale envelope; the rotation likely uses a slower ease-in-out.
- **Observed sound:** a transition swell and low accent align with the object becoming dominant.
- **Inferred product meaning:** the idea is not merely described; it becomes a branded, tangible experiment. Continuity makes the brand feel like the result of thought rather than an inserted logo.
- **Recommended recreation:** build the braces and token as separate precomps; parent to a shared null for the handoff; use motion blur; switch from a flat pre-render to a 3D render at matched size and screen position.

## Copy-image-motion-sound coordination

| Channel | Contribution |
|---|---|
| Copy | Names the origin: a simple idea |
| Image | Shows code-like symbols and a forming token |
| Motion | Demonstrates transformation and continuity |
| Sound | Gives the transition weight and marks the moment of materialization |

## Transferable rule

When a launch video moves from abstract promise to brand reveal, preserve one visual object across the transition. The object should change function—not merely remain on screen—so the viewer experiences the brand as the consequence of the idea.
