# ANIMATION-PLAN.md — the 18 animations on the 3D rig

## In short
Every animation in `ClaudeMascotScene.tsx` uses only a handful of channels: whole-body offset and scale, each arm's vertical offset, the eyes' sideways offset and height, each leg's vertical offset. The rig has a bone for each. Port the 2D formulas (they take a frame number and fps) into keyframes per bone, and all 18 animations exist; `render_mascot.py` already ports them to pose the sheet (`state()` and `apply_pose()`).

## Channel map (2D → 3D bone, bone-local axes: X right, Y up, Z toward the front; 1 px = 0.01 m)
| 2D channel | 3D bone and channel |
|---|---|
| `mascotTx` | `Root` location X, minus the 2D centre-anchor term `48(1−scaleX)` (the 3D origin already sits at the body's centre) |
| `mascotTy` (down is positive) | `Root` location Y (up) = −(`mascotTy` − `86(1−scaleY)`) × 0.01; the foot-anchor term is free because `Root` is at the feet |
| `mascotScaleY` | `Root` scale Y |
| `mascotScaleX` | `Root` scale X, and scale Z (depth) so the body squashes as a box |
| `leftArmTy`, `rightArmTy` | `Arm.L`, `Arm.R` location Y = −Ty × 0.01 |
| `eyeTx` | `Eye.L` and `Eye.R` location X = `eyeTx` × 0.01 |
| `leftEyeH`, `rightEyeH` (10 = open) | `Eye.L`, `Eye.R` scale Y = H / 10 (shrinks toward the eye's top edge, as the 2D rect does) |
| `legNTy` | `Leg.N` location Y = −Ty × 0.01 |
| `legNH` (26 = full) | `Leg.N` scale Y = H / 26 (shrinks toward the body) |

## The 18, and what each needs
| Animation | Channels it drives | Pose-test result |
|---|---|---|
| idle | Root Y bob; both eyes blink (scale Y 10→0→10 every 80 frames) | neutral pose OK |
| bounce | Root Y lift, Root scale X/Y/Z (squash and stretch) | OK |
| wave | `Arm.R` Y oscillation | OK (arm moves up) |
| look | both eyes X | OK |
| walk, run | legs 1+3 and 2+4 lift alternately; Root X sway and a Y hop | OK; opposite leg pairs raised |
| think | eyes X; `Arm.L` Y | OK |
| type | both arms down 8 px; fast Y jitter | OK |
| sleep | eyes scale Y 10→2 (a thin line at the eye's top edge) | OK, matches the 2D sleep frame |
| error | Root X shake | OK |
| nod | Root scale Y dips (feet planted) | OK |
| shake | Root X side to side | OK |
| dance | Root Y hop and scale, arms in antiphase, Root X sway | OK |
| stretch | Root scale Y 0.75–1.25, feet planted | OK |
| crouch | Root scale Y down to 0.75 | OK |
| jump | Root Y lift to 35 px, squash on landing | OK |
| spin | **changes in 3D**: the 2D scene flips scaleX (cos) to avoid rotating pixel rects; here `Root` rotates for real about its vertical axis (bone-local Y) | OK; a negative X scale would flip the normals, so it is not used |
| celebrate | both arms up with the jump, side hop | OK |

## "Possibly others" — what the rig also allows
Rotation of any bone (arms swinging, a body lean) works because every part is rigidly skinned to its own bone; the 2D scene forbade it only to keep its pixel edges crisp. In 3D, boxes stay crisp under rotation, so a swing is possible, but it moves away from the mascot's look as it exists in the 2D videos. Decide per animation.

## What the next video needs
1. Keyed actions for the 18 animations (one Blender Action each, 24 fps, looping), sampled from the ported formulas; check them against the 2D scene's frames.
2. A Godot scene with an AnimationPlayer driving the Skeleton3D's bone tracks, and a small state machine (idle ↔ walk ↔ run ↔ jump, plus one-shots) for the game.
3. A decision on scale and on spin (see `README.md`).
Known limits: the rig is rigid-boxes only (no deformation); the eyes are black boxes 1.5 cm proud of the face (they are bone-driven, not textures); the model is untextured, flat-coloured.
