# SCRIPT — What Is a Game Design Document?
# slug: claude-liam-what-is-a-game-design-document · Liam (in for Bear), Kokoro am_onyx


## B00 — COLD OPEN

Hej, this is Liam, in for Bear. Two videos about game design documents landed in Bear's queue this week, from two studios with very different games. They agree on one thing and disagree on nearly everything else. So I asked Claude to read both, and to explain what a design document actually is using a document we can open: the one Zelda wrote for Bear's Clawd platformer this morning.


## B01 — BLUF

A game design document is the living outline of your game. It exists so that someone else can build it, and that someone is usually you, a few weeks from now, after the idea has changed. Everything else about the format follows from that one job.


## B02 — ACT I · THE ONE REASON

Act one. The one reason.


## B03 — ACT I · THE ONE REASON

The first video puts it plainly: every design document exists to explain your game to someone else. That is the whole reason. If you are working alone you might think that lets you off. It does not, because the someone else is you, three weeks in, when the idea in your head has quietly changed and the version you started building is the only record.


## B04 — ACT I · THE ONE REASON

Things change, and the document is where the change is written down instead of lost. Bear's starter game had twenty optional cherries in its design. One day later, the loop concept replaced them with ordered tasks. The record of no says why: two collectible systems serving one goal is bloat. Without that line, the cherries come back in a month as a new idea.


## B05 — ACT I · THE ONE REASON

So do you need one at all? The honest test from the first video: if the game is small enough to keep in your head, build it and keep it there. The moment you would forget a decision the project depends on, you need the document. The Clawd draft crossed that line on day one; it raised eight open questions before anyone wrote a line of code.


## B06 — ACT I · THE ONE REASON

The second video calls the same thing risk management: you anticipate the problems before core development, when solving them is cheap. In the Clawd document the riskiest mechanic, malware that undoes a finished task, has an acceptance test written before the mechanic exists. T-22: task A done, touch malware, expect dying, A open, ledger flips. A row today, a script later. That is a risk caught on paper.


## B07 — ACT II · WHAT GOES IN

Act two. What goes in.


## B08 — ACT II · WHAT GOES IN

Both videos start in the same place: a high-level description of what the player does, and the design pillars, the handful of goals every later decision gets compared against. The first video says up to four or five, and resist adding more. Then mechanics and controls, so you can tell what it plays like. Then, only if it matters, look, sound, story, and a rough timeline. Detail arrives when the game earns it.


## B09 — ACT II · WHAT GOES IN

Here are Clawd's four. Read the landing. Earn another try. Close the loop. Small, complete game. Two of them already exist in code and two are new. Pillars earn their place the day two of them collide: Zelda had to rule that vague paths may hide which way but never where you land, and that malware may undo one task but must name it. Without pillars there is nothing to rule with.


## B10 — ACT II · WHAT GOES IN

The second video's core loop question: what is the one thing the player does over and over? Answer it at three scales and you have most of the design. Clawd's micro loop exists: read a landing, commit, land or fail with a named cause. The meso loop is the proposal: task A, B, C, a gate, the flag. Solid is code. Dashed is the document. A good document never lets you confuse the two.


## B11 — ACT II · WHAT GOES IN

Mechanics and controls, so it is possible to get an idea of what the game will be like to play. For Clawd that is ten lines: speed one sixty, jump velocity minus three twenty, six ticks of coyote time. The tests assert those numbers. The document points at the file instead of restating it, which is the right move once code exists; the code is the truth and the document is the map.


## B12 — ACT II · WHAT GOES IN

The second video's strongest argument is scope. A document defines what is in and what is out, which is the only known cure for feature creep. Zelda tags every Clawd feature. Eight of fifteen came out core, fifty-three percent, over her forty percent line. She tried to reprioritize twice, could not get under without removing the loop, and wrote Bear two options instead of choosing. A document that argues is doing its job.


## B13 — ACT II · WHAT GOES IN

And the sections you might skip. Both videos list art direction, audio, story and a timeline. Clawd's document keeps all four honest: every visual is code-drawn, so no art files; narrative is emergent from the ledger, no cutscenes; characters are Clawd, and only Clawd; and the timeline is a blank with a question number on it, because none exists. Writing the blank is better than pretending.


## B14 — ACT III · FORMAT MATTERS

Act three. Format matters.


## B15 — ACT III · FORMAT MATTERS

The first video proves format with a house. You know exactly how your house should look, but you cannot build houses, so you hire a builder and now you have to explain it. Imagine doing that in a word document. Even a perfect description is useless in that format. A blueprint holds the same information and the builder can use it. Decide what goes in, then decide how to present it.


## B16 — ACT III · FORMAT MATTERS

One way to do that is the one-page method, from Stone Librande's twenty-ten GDC talk. One page, one focus: a map, a chart, a drawing, with the detail in callouts that all point back at it. One page is about as much as anyone will read, including you. And the page can grow as big as it needs to, as long as everything on it still links to the focus. Otherwise you have several documents in one place.


## B17 — ACT III · FORMAT MATTERS

This is what a one-page design looks like in Clawd's package: the session state machine. One focus, the five states the code already has. The callouts are the two proposals, drawn dashed: a ledger tick inside playing, and a gate that refuses to transition while a task is open. Everything on the page links to the machine. A reader who has never seen the code can argue with it.


## B18 — ACT III · FORMAT MATTERS

Format also depends on who it is for. A pitch to an investor explains the market and the audience and why it will sell. The document you make first is the one that helps you design, and the second video adds where it lives: a shared document at first, then a wiki or a tool with version control once the team grows, so you can see later why a decision was made. The key is one place everyone knows.


## B19 — ACT III · FORMAT MATTERS

Clawd keeps that history as a plain file. Version, date, author. Sections added, decisions logged, questions opened and closed, and the why: the cherries went because two collectible systems served one goal. A change log without design reasoning is a timestamp. This one is eight lines and it already answers the question a new teammate asks first.


## B20 — ACT IV · LIVING, THEN FROZEN

Act four. Living, then frozen.


## B21 — ACT IV · LIVING, THEN FROZEN

The standard definition calls it a living document: it changes as limits and new abilities are discovered. The second video adds the part people skip. Once production starts, you freeze it. Not untouchable, but the core mechanics, the story arc and the primary features stop moving, because a core change late ripples into delays, cost and creep. After the freeze, changes are small, and each one carries a written reason.


## B22 — ACT IV · LIVING, THEN FROZEN

Neither video had a tool for the hardest part: telling what in the document is real. Clawd's draft tags every claim. Observed, with a file and a line. Inferred. Assumption. Missing. So the same page can hold the game that exists, a tested First Steps slice, and the game that is proposed, tasks, malware, a fork, without letting a reader mistake one for the other. That is the freeze, made visible.


## B23 — ACT IV · LIVING, THEN FROZEN

One last thing a document can do that a meeting cannot. It keeps the argument. Zelda's notes at the end of the Clawd draft are the pushback she would have spoken: the loop is a checklist until it has a verify step; the malware undo is the whole bet, greybox it first; the first fix is to answer two questions before anyone codes. Nobody was in the room. The document was.


## B24 — VERDICT

The verdict. A game design document exists to explain the game to someone else, and that someone is usually you later. Start with the concept and four or five pillars, add mechanics, and let detail arrive when the game earns it. Pick the format the reader can use; a page with one focus beats a novel nobody opens. Keep it living until production, then freeze it and log every change with a reason. And tag what is real. The two videos give you the first four. The Clawd document shows the fifth.


## B25 — YOUR TURN

Your turn. Take a game idea, yours or one you admire, and paste this into Claude. Write me a one-page design document for this game: the core concept in two sentences, four pillars with the feature that honors each and the feature that violates it, the core loop at three scales, and a list of what is out of scope with a reason for each. Then tell me which single decision I will most regret leaving unwritten. Watch that last answer. If it is a mechanic, you have a document. If it is a feeling, you have a pitch. Liam, in for Bear.


## B26 — OUTRO

What Is a Game Design Document? At Nik Bear Brown.
