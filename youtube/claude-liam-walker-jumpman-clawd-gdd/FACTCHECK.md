# FACTCHECK — Clawd Closes the Loop: The GDD

All claims checked against design/GDD.md (sha256 438eff052361f676…), the Godot source at commit 382f2ba, and CLAWD-STATUS.json.

| Claim (beat) | Source | Status |
|---|---|---|
| Godot 4.7.2, GL Compatibility, 640×360, 60 ticks (B02, B14) | godot/project.godot | VERIFIED |
| 25 mechanics, 9 keyboard, 162 animation samples pass; human_playtest pending (B02, B18) | CLAWD-STATUS.json | VERIFIED (automated results, not human approval) |
| 18 animations, 6 used in play (B02) | clawd_art.gd ANIMATIONS; player.gd visual_animation() | VERIFIED |
| speed 160, accel 1280, jump −320, gravity 960, coyote 6, buffer 6 (B07) | tuning.gd | VERIFIED |
| 53.3 px rise asserted by a test (B07) | tests/test_game.gd fixed-jump-and-no-double | VERIFIED |
| layer names 4 Hazard / 5 Goal vs code 8 / 16 (B14) | project.godot [layer_names]; session.gd:38,40 | VERIFIED |
| CORE 8/15 = 53%; 47% and 43% after re-prioritization (B12) | GDD §11 | VERIFIED (arithmetic checked) |
| Two decided items D-01, D-02; eight open questions (B04, B16) | design/decisions.md | VERIFIED |
| Task stations, malware, fork are not code (B02, B08) | godot/ tree at 382f2ba; AGENTS.md | VERIFIED |
| Malware undo contingency: 2 s freeze (B15) | GDD §14 R-01 | VERIFIED |

## Not verified, by design

- Every PX goal is a hypothesis; no human session has been run. The film says so in B02, B06, B15, B18.
- The level-1 diagram coordinates are placeholders; B11 labels them not simulated.
- Dates and version numbers in narration are limited to the engine version the project pins.
