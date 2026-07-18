# Animation Taxonomy

Use these names as common descriptive vocabulary, not as claims about the creator's original presets.

## Transform entrances and exits

| Name | Visual signature | Typical properties | Product implication |
|---|---|---|---|
| Fade in/out | Visibility changes without spatial travel | Opacity | Calm, neutral, editorial |
| Slide in/out | Element travels from an edge or offset | Position, opacity | Navigation, continuity |
| Push transition | Incoming scene displaces outgoing scene | Position, masks | Progress, sequence |
| Zoom in/out | Camera or layer scale changes continuously | Scale/camera Z | Focus, scope, intensity |
| Zoom-through | Camera passes through an object into the next scene | Camera Z, mask, blur | Discovery, portal, connected worlds |
| Scale pop | Fast scale-up followed by settle | Scale, opacity | Responsiveness, confirmation |
| Back-out overshoot | Target is exceeded once, then settles | Scale/position/rotation | Energy with control |
| Bounce | One or more impacts with diminishing rebounds | Position/scale | Playfulness, physicality |
| Elastic | Oscillatory stretch around target | Scale/position | Expressive, rubbery, rarely suitable for serious finance |
| Drop-in | Gravity-like downward entry with impact | Position, scale, shadow | Tangibility, weight |
| Float-in | Slow decelerating entry with slight drift | Position, opacity | Premium, calm, ambient |

## Typography

| Name | Visual signature | Typical implementation |
|---|---|---|
| Type-on | Characters appear sequentially | Text animator, source-text stepping |
| Text scramble | Random glyphs resolve into final copy | Character offset, expressions |
| Word replacement | One word swaps while sentence structure remains | Masks, source text, crossfade |
| Word pivot | A retained word bridges two claims | Position lock + replacement |
| Tracking reveal | Letter spacing compresses into readable text | Tracking + opacity |
| Line mask reveal | Text appears through a moving matte | Mask/track matte |
| Kinetic typography | Type position/scale/timing carries narrative emphasis | Text animators, layout precomps |
| Font morph | Weight, width, or type style changes continuously | Variable font axis or crossfade |
| Odometer | Digits roll vertically | Clipped number columns |
| Caption step-on | Words or phrases enter on speech beats | Stepped text blocks |

## Shape, UI, and object motion

| Name | Visual signature | Typical implementation |
|---|---|---|
| Masked wipe | A matte reveals the next element | Shape layer matte |
| Stroke draw-on | Line appears as if drawn | Trim Paths |
| Morph | One contour transforms into another | Path interpolation |
| Card stack | Cards enter with offset position/rotation | Parent null + stagger |
| Carousel | Items move horizontally through a viewport | Position + clipping mask |
| List scroll | Content moves vertically inside fixed UI | Precomp + mask |
| Panel slide-in | Side sheet or inspector enters | Position + shadow |
| Dropdown unfold | Menu expands from control | Scale Y/mask + opacity |
| Tooltip pop | Small contextual surface appears near target | Scale pop + fade |
| Cursor choreography | Cursor guides attention and triggers state changes | Position path + click timing |
| Tab morph | Selected state moves between tabs | Underline/shape interpolation |
| Progress fill | Bar or ring fills to represent completion | Scale X, trim paths |

## Camera and spatial motion

| Name | Visual signature | Typical implementation |
|---|---|---|
| Camera push-in | Slow move toward subject | 3D camera Z |
| Pull-back reveal | Camera retreats to expose wider system | Camera Z/scale |
| Parallax | Foreground and background move at different rates | Layered depth |
| Orbit | Camera rotates around subject | 3D camera/null |
| Dolly zoom | Perspective changes while subject size stays similar | Camera Z + focal length |
| Rack focus / defocus | Sharpness transfers between depth layers | Camera DOF/blur |
| Floating field | Many elements drift in 3D or pseudo-3D | Randomized positions + depth |

## Transition and continuity devices

| Name | Visual signature | Why it works |
|---|---|---|
| Match cut | Similar shape/position/action bridges shots | Makes discontinuity feel intentional |
| Anchor match cut | One persistent object occupies matching screen space | Preserves attention anchor |
| Object continuity | Same branded object survives across worlds | Builds visual identity |
| Hard cut on beat | Instant cut aligned to a musical transient | Precision and energy |
| Whip pan | Fast directional blur bridges scenes | Momentum |
| Light sweep | Highlight travels across object or logo | Polish, reveal, materiality |
| Glow bloom | Light expands rapidly then settles | Energy, activation |
| Pixel/particle dissolve | Object breaks into particles or pixels | Digital transformation |
| Horizon wipe | Bright line sweeps across a horizon | Futuristic scale |
| Defocus transition | Scene blurs before replacement | Soft continuity |

## Motion-principle distinctions

### Overshoot vs bounce

- **Overshoot:** crosses the target once and returns. Usually reads as confident and responsive.
- **Bounce:** collides with a boundary and rebounds one or more times. Usually reads as playful or physical.
- **Elastic:** oscillates around the target with visible springiness. Usually reads as expressive rather than precise.

Do not label every scale settle as bounce. Inspect whether the value crosses the target, how many times, and whether the motion implies impact.
