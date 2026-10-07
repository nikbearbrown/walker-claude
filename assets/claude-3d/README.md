# Claude mascot, 3D

## What this is, what was found
The Claude mascot (the one at the end of your videos) as a 3D model in Blender, built so the next video can animate it for a game. It is 9 boxes in one mesh (108 triangles), 0.86 m tall, with a 9-bone rig whose channels match, one for one, the 18 named animations of the 2D mascot (idle, bounce, wave, look, walk, run, think, type, sleep, error, nod, shake, dance, stretch, crouch, jump, spin, celebrate).

What matters:
- **The shape is not redrawn from the screenshots.** The toolkit already holds the mascot's exact geometry and all 18 animation formulas (`brutalist.art/runtime/remotion/src/scenes/ClaudeMascotScene.tsx`: torso 96×60, arms 20×20, eyes 11×10, legs 11×26, body `#dd775b`, eyes black). The 3D model uses those numbers, so it is the same mascot, including its lopsided legs (the fourth leg sits flush with the torso's right edge).
- **The 3D part is invented, and it is yours to change:** depth (torso 48 deep, arms 20, legs 11, eyes 3 with 1.5 proud of the face) and the scale (1 pixel unit = 1 cm). The 2D scene has no depth.
- **The rig works, tested by posing, not by animating.** `renders/sheet-poses.png` poses the rig at one extreme frame of each of the 18 animations, using the 2D scene's own maths. No animation clips exist yet; that is the next video.
- **I did not use the Blender MCP.** This was built with a Blender script, the same route the Assignment 3 film calls the fallback. Using the MCP means installing `uv` and the MCP for Blender add-on, running `claude mcp add` (a change to your Claude Code configuration), and opening a local socket that runs any Python sent to it. I did not do that without your word. Say so and I will try it in a throwaway Blender profile, and report what happens, honestly.

## Files
| File | What it is |
|---|---|
| `claude_mascot.glb` | the model + rig for a game engine (+Y up, 13.9 KB). Godot 4.7.2 imports it with a 9-bone Skeleton3D, 2 surfaces, bounds 1.36 × 0.86 × 0.495 m, node scale 1 |
| `claude_mascot.blend` | the Blender source |
| `build_mascot.py` | builds the model, rig, `.blend` and `.glb` (`Blender -b --factory-startup --python-exit-code 1 --python build_mascot.py`) |
| `render_mascot.py`, `make_sheets.py` | the renders and contact sheets |
| `renders/turnaround/` and `sheet-turnaround.png` | 8 angles, every 45 degrees, front = 0 |
| `renders/ortho/` and `sheet-orthographic.png` | front, back, left, right, top, bottom |
| `renders/wireframe.png` | the 108 triangles' edges |
| `renders/poses/` and `sheet-poses.png` | one rig pose test per named animation |
| `renders/rig-diagram.png` | where each bone's joint is |
| `ANIMATION-PLAN.md` | each animation mapped to bone channels; what the next video needs |

## The model
Dimensions 1.360 × 0.495 × 0.860 m (x, y, z), 108 triangles, 2 materials (`ClaudeBody` #dd775b, `ClaudeEye` black), rotation 0, scale 1. Origin at the centre of the underside of the feet, centred on the torso, lowest point z = 0. The front faces −Y (Blender's front view). Every part is rigidly skinned (weight 1.0) to one bone.

## Rig
9 bones, all children of `Root` (at the feet): `Arm.L`, `Arm.R` (at each arm's centre), `Eye.L`, `Eye.R` (at each eye's top edge), `Leg.1`–`Leg.4` (at each leg's top). Every bone points straight up, so in bone-local space **Y = up, X = right, Z = toward the front**. Scaling a bone's Y shrinks a leg toward the body and an eye toward its top edge, as the 2D rectangles do; scaling `Root` squashes and stretches around the feet, which is what the 2D scene's "foot-anchor" formula does by hand.

## Checks run (2026-10-06)
Blender 5.1.2 build log (dimensions, 108 triangles, lowest z 0); `.glb` JSON read back (skin joints, 2 materials, bounds); Godot 4.7.2 headless import and skeleton/bounds print; every render looked at; the torso's rendered colour (217, 117, 89) against the canonical (221, 119, 91).

## Open decisions for you
1. **Scale and depth.** 1 px = 1 cm gives a 0.86 m mascot, 1.36 m with its arms out. Too big for your game? One number (`U` in `build_mascot.py`).
2. **Spin.** The 2D scene fakes a spin by flipping scaleX (its "pixel-art law" allows only translation and axis-aligned scale). In 3D the model can turn for real; the pose test shows a real quarter-turn. Keep the flip, or turn it?
3. **MCP or script.** See above.
4. **Next video.** The 18 animations as keyed actions (the 2D formulas port directly), then a Godot AnimationPlayer scene.
