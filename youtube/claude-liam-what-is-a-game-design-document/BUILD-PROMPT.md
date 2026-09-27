# Rebuild What Is a Game Design Document?

From `books/`:

```
ai deep explainer Liam persona "What is a Game Design Document?" — sources: the two transcripts in SOURCES.md; example: walker-jumpman-clawd/design/GDD.md; reuse scenes from claude-liam-walker-jumpman-clawd-gdd and -gdd-deck
```

REEL = walker-jumpman-clawd/youtube/claude-liam-what-is-a-game-design-document. From `brutalist.art/`:

1. `python3 runtime/scripts/generate_audio_kokoro.py REEL`
2. `python3 REEL/build.py lock` · `python3 runtime/scripts/align.py REEL --model base` · `python3 REEL/build.py cues`
3. `./art run REEL --height 1080` (renders scenes.py Manim beats with gates A/W/B, Remotion beats, compiles the previz, GATE V, GATE T)
4. inspect `_qc/` frames and `qc-sheet.png`; fix scene source; rerun
5. `./art final REEL --height 2160 --fps 30 --out REEL/exports/landscape` · `python3 runtime/scripts/loudness_check.py REEL --mp4 …`

Liam, Kokoro am_onyx, Teardown. Zero vox beats: the evidence is text, code and diagrams. Never publish.
