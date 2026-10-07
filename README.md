# walker-claude — one Claude figure, many games, one teaching project

**What this is.** A single Godot project built around the Claude figure (the mascot at the end of the videos). Each *level* is a different game, and each one exists to teach one thing: how to build that kind of game with **Walker + Claude Code + Blender + Godot** (and other tools as we add them). It is primarily a teaching game: the code, the assets, the briefs and the logs are meant to be read, copied and rebuilt.

**Where it came from.** It starts as a copy, with history, of [walker-jumpman-clawd](https://github.com/nikbearbrown/walker-jumpman-clawd) (a Jumpman platformer whose hero is Clawd, the 2D Claude figure with 18 animations). That repository stays as it was; this one is where new work lands.

**What exists today (and nothing more is claimed):**
| Level | Kind | State |
|---|---|---|
| Jumpman | 2D platformer | The inherited game, in [`godot/`](godot/): the First Steps level with Clawd, the 18-animation gallery, the design package and the design films' sources. See [docs/walker-jumpman-clawd-README.md](docs/walker-jumpman-clawd-README.md). |
| Claude in 3D | 3D asset (no level yet) | [`assets/claude-3d/`](assets/claude-3d/): the Claude mascot as a 3D model, rigged with nine bones for the same 18 animations; built in Blender by script, and separately through the Blender MCP. No Godot level uses it yet. |

**Planned (not built):** a 3D level starring the 3D Claude; a mobile level (touch controls, export to a phone); further 2D levels; levels that exercise Blender-made assets and other tools. See [LEVELS.md](LEVELS.md). Each new level, asset and tool gets added here, with the brief that produced it.

## Run the inherited game
```sh
godot --path godot
```
(Godot 4.x; Enter starts; A/D or arrows move; Space jumps; R retries.) On Mac, double-click `walker-jumpman-clawd.command`; for the 18-animation gallery, `clawd-gallery.command`.

## Rules of this repository
- Every level has a written brief before it is built, and a log of what was tried (`FRICTIONAL.md`, `CHANGE-BRIEF.md`, and the level's own notes).
- Claims are checked: sizes, scales and behaviour are read back by a script that is not the AI that built them.
- Generated media (video, audio, builds) stays out of git (see `.gitignore`); sources, scripts, briefs and small assets are committed.
- No level is called finished until a human has played it.
