# SCRIPT — Clawd Closes the Loop: The GDD
# slug: claude-liam-walker-jumpman-clawd-gdd
# voice: Liam (in for Bear), Kokoro am_onyx


## B00 — COLD OPEN (ClaudeComposerAsk)

Hola, this is Liam, in for Bear. Bear's game is Walker Jumpman Clawd: a coding agent as a platformer hero. This week he gave Zelda, Walker's design persona, one paragraph: every level is an agentic loop, task A, task B, until done, and the obstacles are bugs, malware and vague instructions. Zelda wrote the full design document in silent mode. I read all sixteen sections. Here is what it commits to, what exists, and what nobody has decided.

*[On screen: Reconstructed Walker prompt and the two output lines that frame the film]*


## B01 — BLUF (BrutalistHesitantWriter)

Clawd Closes the Loop is a platformer built on a coding-agent loop, not wearing one. Each level is an agentic loop: tasks in order, and bugs, malware and vague paths as the obstacles. The document says which of that exists and which is a guess, line by line. That honesty is the thing worth watching.

*[On screen: Hesitant writer corrects theme to loop; the corrected sentence is the film claim]*


## B02 — STATUS (GodotDesignBoard)

First, what is real. The First Steps slice runs in Godot 4.7.2: move, one jump with coyote and buffer windows, spikes, a fall line, a half-second retry, a finish and a replay. Clawd is drawn from eighteen code animations; play uses six. Twenty-five mechanics checks, nine keyboard checks and a hundred sixty-two animation samples pass. Task stations, malware, the fork: none of it is code. And no human has played any of it.

*[On screen: Observed capture beside the logline; four status cards light in narration order]*


## B03 — VISION (GodotDesignBoard)

The vision in one line: I am the agent, I close the loop. Not a hero with a move list, a worker who finishes despite conditions. The audience is narrowed on purpose: keyboard players who know or are learning what a coding agent does. The promise is the First Steps promise kept: every failure names its cause, every level ends with a receipt. And the document names its own biggest hole before anyone else can.

*[On screen: Vision excerpt with four commitments lighting as spoken]*


## B04 — PILLARS (GodotDesignBoard)

Four pillars, two of them inherited from the starter and observed in code: read the landing, and earn another try. Two are new and proposed: close the loop, and small complete game. Zelda ran the collision test and ruled twice. Vague paths may hide which way, never where you land. Malware may undo one task, must name it, and the station stays reachable. Those rulings are the first two decisions in the log.

*[On screen: Pillar cards light in order; the collision ruling stays on the left]*


## B05 — LOOP (GodotDesignBoard)

Three scales. Micro is shipped: read a landing, commit, land or fail with a name. Meso is the draft: enter, task A, task B, task C, the gate opens, the flag. The red dashed return is malware sending B back to open. The grey one is a wrong branch looping to the fork. Zelda's honesty test: strip the theme and it is ordered checkpoints plus a patrol that resets one. Still a game. A greybox decides, not this diagram.

*[On screen: Three-scale loop diagram; cards light per scale]*


## B06 — PX GOALS (GodotDesignBoard)

Seven player experience goals, each a testable feeling. Four are already covered by the existing suites: in control, I understand the mistake, one more try, playable muted. Three are new. Progress inside the level when a task ticks. Closure when the results say tasks, time, retries. And the one with no test at all: a wrong branch was my read, not a trick. That last one only a human can grade.

*[On screen: PX goal cards light; PX-07 flagged as untestable by machine]*


## B07 — MECHANICS OBSERVED (ClaudeCodeBeat)

The observed mechanics live in ten lines of tuning. Speed one sixty, acceleration twelve eighty, jump velocity minus three twenty, gravity nine sixty, six ticks of coyote, six of buffer. The tests assert those numbers: a fifty-three pixel rise, one jump per floor contact, a held jump that does not bounce. Everything the loop proposes sits on top of this file, and the document is careful to say it changes none of it.

*[On screen: Real tuning.gd contents; the observed movement contract]*


## B08 — OBSTACLES (GodotDesignBoard)

Now the three obstacles, which is the whole concept. A bug is the spike that exists: stationary, three exact triangles, costs the attempt. Malware is proposed: it patrols a fixed segment, and on contact it costs the attempt and re-opens the last task. A vague path is proposed: a fork with a sign that is true but incomplete; the wrong branch costs time, never a life. Each column ends with what it may not do. That row is the design.

*[On screen: Obstacle taxonomy with three cards lighting per column]*


## B09 — SYSTEMS (GodotDesignBoard)

The state machine does not change. Menu, playing, paused, dying, complete, exactly what session dot g d owns today. The proposed ledger is an event inside playing: station contact ticks a task and the game keeps running. The proposed gate is a condition, not a state: touch the flag with a task open and the HUD says loop not closed, B open, and nothing transitions. One owner for the ledger, or it drifts from the stations after a retry.

*[On screen: State machine with the two proposed additions dashed]*


## B10 — PROGRESSION (GodotDesignBoard)

Progression is two rows and a blank. First Steps exists: twenty to sixty seconds to learn the jump and read a spike. Level one, Close the loop, is proposed: one to three minutes, three tasks, one patrol, one fork, and the drop-off risk written next to it is the malware undo. Level two is a blank the document refuses to fill. No new abilities ever; difficulty is layout only. The flag is the one hard gate.

*[On screen: Progression cards; the deliberate blank row]*


## B11 — WORLD (GodotDesignBoard)

World, narrative, characters, all three in one breath, because the document keeps them thin on purpose. The world is the codebase: sixty hertz physics, one jump, no lore. The narrative is emergent from the ledger, delivered by HUD copy, sign text and Clawd's poses: nod on a tick, shake on an undo, think at a fork. One character. Clawd may never gain an ability because an animation exists. That constraint is inherited from the change brief and it holds.

*[On screen: Level flow over real geometry; world, narrative, character cards]*


## B12 — SCOPE (GodotDesignBoard)

Here is the number that matters. Fifteen features, eight tagged core: fifty-three percent, over Zelda's forty percent line. She tried to reprioritize: demote the pause feature that already exists, forty-seven. Fold the gate into the stations, forty-three. Still over, and the next cut removes the loop itself. So silent mode did what it should: changed no tags, and wrote two options for Bear. Cut to a reduced MVP, or keep core and extend the timeline. There is no timeline on record.

*[On screen: Feature dependency map with the CORE overage and two options]*


## B13 — OUT OF SCOPE (GodotDesignBoard)

The record of no. Double jump, wall jump, dash: out forever, the art suggested them and the design refused. The starter's twenty cherries: superseded by tasks, because two collectible systems serving one goal is bloat. Moving platforms, chasing malware, task types, save files, remapping: each deferred with a reopen condition. The animation gallery as gameplay: permanently excluded, with a date. A no with a reason is a design decision. A silent omission is not.

*[On screen: Out-of-scope cards with reasons]*


## B14 — TECHNICAL (ClaudeCodeBeat)

Technical is mostly observed: Godot four point seven two, G L compatibility, six forty by three sixty logical, sixty ticks, every visual drawn in code, no image files, no export produced yet. And one thing the reverse pass caught that the starter never wrote down. The project file names layer four Hazard and layer five Goal. The code puts spikes on eight and the goal on sixteen. Nothing breaks today. The first person who edits by layer name will be confused. Logged as D-02, decided, not yet applied.

*[On screen: Real project.godot layer block beside the two session.gd lines that disagree]*


## B15 — RISKS (GodotDesignBoard)

Seven risks, three that can kill it. R-01: malware undo reads as punishment. The whole bet rests on it being a setback, and only a person playing a greybox can say. R-07: zero human playtests, which was true for the starter and is still true. R-03: fifty-three percent core with no timeline, which is how a semester example becomes a semester. Each has an owner, a trigger and a contingency. The contingency for R-01 is a two-second freeze instead of an undo.

*[On screen: Three risk cards light on their IDs]*


## B16 — OPEN QUESTIONS AND TESTS (GodotDesignBoard)

Eight open questions and six proposed tests. Q-01, does undo feel like a setback. Q-02, do finished tasks survive a death. Q-04, cut or extend. Q-08, does the loop need a verify step. The tests are written before the code: T-22, task A done, touch malware, expect dying and A open and the ledger showing the flip. That is the acceptance test for the riskiest mechanic, and it exists today as a row, not a script.

*[On screen: Open questions and the proposed test that guards the riskiest mechanic]*


## B17 — ZELDA NOTES (GodotDesignBoard)

Silent mode does not argue; it writes the argument down. Zelda's notes at the end are the pushback she would have spoken. One: task A, B until done is a checklist; a real loop has a verify step, and verify is where agents actually fail. Two: malware undo is the only mechanic that makes the theme mechanical, so build it first in a greybox. Three: the vague path is fair only if the wrong branch is boring. And the first fix: answer Q-01 and Q-04 before anyone writes a line.

*[On screen: Zelda notes as four cards]*


## B18 — VERDICT (ClaudeVerdictArtifact)

The verdict. What exists: a tested First Steps slice with Clawd drawn in code. What is proposed: ordered tasks, a gated flag, a malware patrol that undoes work, a fork that costs time. What the document does well: every claim carries its provenance, every no has a reason, and the tests are written before the code. What it cannot do: sign a gate, choose between cut and extend, or tell you whether an undo feels fair. Those three are Bear's, and one of them needs a person holding a keyboard.

*[On screen: Verdict artifact: exists, proposed, strong, cannot, next]*


## B19 — YOUR TURN (ClaudeComposerAsk)

Your turn. Take a game idea you have, or a repo you already started, and paste this into Claude. Use the Walker gdd skill. If there is code, run reverse first and tag every claim observed, inferred, assumption or missing. Then draft the sixteen sections silently, report the core percentage, and end with the three questions a human must answer before anyone writes code. Watch for two things in the answer: whether the core percentage comes with both options, and whether the questions are ones only you can answer. If Claude answers them for you, that is the failure the tags exist to catch. Liam, in for Bear.

*[On screen: Handoff prompt typed in the composer, read aloud and discussed]*


## B20 — OUTRO (ClaudeTitleOutro)

Clawd Closes the Loop: The GDD. At Nik Bear Brown.

*[On screen: Locked title outro, spoken, no music]*
