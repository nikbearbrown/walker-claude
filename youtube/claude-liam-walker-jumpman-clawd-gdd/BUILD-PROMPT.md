# Rebuild Clawd Closes the Loop: The GDD

From `books/`:

```
godot-gdd walker /Users/bear/Documents/CoWork/bear-textbooks/books/walker-jumpman-clawd design/GDD.md
```

REEL = walker-jumpman-clawd/youtube/claude-liam-walker-jumpman-clawd-gdd. Steps, all from `brutalist.art/`:

1. `python3 runtime/scripts/generate_audio_kokoro.py REEL`
2. `python3 REEL/scripts/build.py lock` (pads to frame, −1.5 dBTP limit into audio/<id>-lim.wav, +1.0 s tail on the spoken outro)
3. `python3 runtime/scripts/align.py REEL --model base` then `python3 REEL/scripts/build.py cues`
4. `python3 runtime/scripts/remotion_scenes.py REEL`
5. `./art godot-gdd --check REEL --gdd ../walker-jumpman-clawd/design/GDD.md`
6. `./art run REEL --height 1080` · inspect `_qc/` frames · `python3 runtime/scripts/type_check.py REEL`
7. `./art final REEL --height 2160 --fps 30 --out REEL/exports/landscape` · `python3 runtime/scripts/loudness_check.py REEL --mp4 REEL/exports/landscape/claude-liam-walker-jumpman-clawd-gdd.mp4`

Liam, Kokoro am_onyx, Teardown. Never publish; no game change; no paid generation.
