# walker-jumpman-clawd — Game brief

Version 0.3.0-draft · September 18, 2026 · **Silent draft by Zelda (/gdd reverse + draft, silent). Not reviewed. No gate signed.**

Concept as given by Bear, 2026-09-18: Clawd, a coding agent, goes through an agentic loop on every level: task A, task B, and so on until the level is done. The obstacles are the things an agent faces: bugs, malware, and vague paths (unclear instructions). This is a rough draft that will change.

**This game is** a short 2D platformer **for** keyboard players who know what a coding agent is, or are about to learn, **delivering** the feeling of finishing a loop of small tasks despite hostile and ambiguous conditions **through** one fixed-height jump, ordered task stations, and instant retry. **Space between** the walker-jumpman First Steps slice and a Celeste-style readable-death platformer with a one-screen loop of goals. **Succeeds if the player feels** "I was the agent. I got the job done, and I can say exactly what broke and why."

## What exists today `[OBSERVED]`

A playable Godot 4.7.2 slice, First Steps, with movement, one jump with coyote and buffer windows, spikes, a fall boundary, retry, pause, finish and replay. Clawd is drawn from 18 code-driven animations; gameplay uses six of them. 25 mechanics checks, 9 keyboard checks and 162 animation samples pass. No task stations, no malware, no vague paths, no level extension. Zero human playtests.

## What this draft proposes `[ASSUMPTION]` unless tagged otherwise

- Every level is a loop of ordered tasks. Touching a task station completes it. The finish is a soft gate until every task is done.
- Bugs are the existing spikes, renamed. Malware is a patrolling hazard that undoes a completed task if it touches Clawd. A vague path is a signed fork where the sign is ambiguous and the wrong branch costs time, never a life.
- The direct route through a level is always visible. Vague paths hide *which way*, never *where you land*.

## The biggest unresolved question

Whether "malware undoes a task" reads as an interesting setback or as a punishment that breaks the retry promise. It is decided by a human playing a greybox, not by this document. See `decisions.md` Q-01.
