# LEVELS.md — the plan (a plan, not a record)

Every level is a different game around the Claude figure. Each one teaches one set of skills. Status is honest: only "built" means it exists and has been played.

| # | Level | Kind | Teaches | Status |
|---|---|---|---|---|
| 1 | Jumpman (First Steps) | 2D platformer | scenes, input, TileMap-style levels, animation states, collision | inherited, built (see `godot/`) |
| 2 | Clawd gallery | 2D showcase | the 18 animations as data | inherited, built |
| 3 | Claude in 3D | 3D | importing a Blender asset (.glb), bones and animation players, 3D movement and collision | asset built (`assets/claude-3d/`); level not started |
| 4 | Claude on mobile | mobile | touch input, screen sizes, export to a phone | not started |
| 5+ | to be decided with Professor Bear | any | Blender-made assets, particles, audio, UI, AI-driven characters, other tools | not started |

## How a level gets added
1. Write the brief (what it teaches, what is built, how it is checked, predicted failures).
2. Build it with Walker + Claude Code (+ Blender/the MCP for assets) and log what happened.
3. Check it with a script that is not the builder; play it; record what a human found.
4. Commit sources, scripts and the brief; keep generated media out.
