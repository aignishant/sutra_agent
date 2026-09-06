# Day 76 - VAD events and non-blocking tools — the conversation doesn't freeze mid-tool

IDs closed: ADK-56, ADK-77 · source: `days/day-76-vad-and-non-blocking-tools/`

## Parts

### 1.1 - The wait nobody sees
`days/day-76-vad-and-non-blocking-tools/parts/01-the-tool-in-the-middle/1.1-the-wait-nobody-sees.md` · level `foundation` · ids ADK-56, ADK-77

A tool call is invisible in a request and unavoidable on a line: when the caller sent one message and is waiting for one answer, nobody can tell whether that wait was spent thinking or looking something up — but when the line is open the caller is present for the wait, can hear the silence, and is entitled to speak into it, and every design question on this day follows from that one change in who is in the room.

### 1.2 - The sequence, measured
`days/day-76-vad-and-non-blocking-tools/parts/01-the-tool-in-the-middle/1.2-the-sequence-measured.md` · level `working` · ids ADK-56, ADK-77

A tool call inside a live session is a four-step round trip in which the runtime does the middle two — the model asks for the tool and does not finish its turn, the runtime runs it, the runtime hands the result back through the connection's send_content, and only then does the model answer — and knowing which two steps are the model's and which two are the runtime's is what makes every measurement in the rest of this day readable.

### 1.3 - The line that goes dead
`days/day-76-vad-and-non-blocking-tools/parts/01-the-tool-in-the-middle/1.3-the-line-that-goes-dead.md` · level `production` · ids ADK-56, ADK-77

With the lookup written as await asyncio.sleep(...), 4 slices of the caller's audio reach the model's connection while the tool is still running; with the identical lookup written as time.sleep(...), 0 do — and the tool is declared async def in both cases.

### 2.1 - Three schedulings
`days/day-76-vad-and-non-blocking-tools/parts/02-when-the-answer-comes-back/2.1-three-schedulings.md` · level `working` · ids ADK-56, ADK-77

A tool result has to reach the model, and on an open line there is a second question a request never had to ask — when should the model react to it? The installed package answers it with a field and three values: SILENT, WHEN_IDLE and INTERRUPT, documented as "Controls when the model reacts to the tool's response".

### 2.2 - Choosing one
`days/day-76-vad-and-non-blocking-tools/parts/02-when-the-answer-comes-back/2.2-choosing-one.md` · level `production` · ids ADK-56, ADK-77

Every one of the three schedulings is wrong for something, which makes this a per-tool decision rather than a per-system one — and leaving response_scheduling unset is not abstaining from the decision, it is taking whatever default the model happens to apply to a tool nobody thought about.

### 2.3 - What to say while you wait
`days/day-76-vad-and-non-blocking-tools/parts/02-when-the-answer-comes-back/2.3-what-to-say-while-you-wait.md` · level `production` · ids ADK-56, ADK-77

On an open line the silence during a tool call has to be filled with something, and whatever fills it is content — so "I'm just checking that for you" is a claim about what is happening, and a desk that says it after the lookup has already failed, or while no lookup is running at all, has produced a plausible sentence that is not true.

### 3.1 - The knobs
`days/day-76-vad-and-non-blocking-tools/parts/03-deciding-when-they-stopped/3.1-the-knobs.md` · level `working` · ids ADK-56, ADK-77

Day 75 found two candidates for deciding that a caller has stopped speaking — the far end working it out from the sound, or the client saying so — and left the first one looking like a fixed property of the service. It is not. It is a disabled flag and five named settings, every one of which is a decision somebody has to make.

### 3.2 - Sensitivity is a trade
`days/day-76-vad-and-non-blocking-tools/parts/03-deciding-when-they-stopped/3.2-sensitivity-is-a-trade.md` · level `production` · ids ADK-56, ADK-77

End-of-speech sensitivity and silence duration are one dial with a bad outcome at each end — turn it one way and the system decides you have finished while you are drawing breath, turn it the other and it sits there in silence after you actually have — and no value avoids both, so every setting is a choice about which of the two complaints you would rather receive.

### 3.3 - Interruption is a setting
`days/day-76-vad-and-non-blocking-tools/parts/03-deciding-when-they-stopped/3.3-interruption-is-a-setting.md` · level `production` · ids ADK-56, ADK-77

Whether the caller speaking cuts off the answer is not a property of the framework and not a bug to avoid — it is a field with a name, ActivityHandling, whose value NO_INTERRUPTION is exactly the ablation Day 75 part 2.2 built to prove barge-in mattered, which means somebody has to choose it and there are flows where the "wrong" choice is the right one.

### 4.1 - The silence you cannot see
`days/day-76-vad-and-non-blocking-tools/parts/04-in-production/4.1-the-silence-you-cannot-see.md` · level `production` · ids ADK-56, ADK-77

A frozen line raises nothing, ends cleanly and gives the caller the right answer — its only trace is a log four lines shorter than it should have been — so the signal cannot be an error rate or a failure count; it has to be the gap between the things that were supposed to be arriving.

### 4.2 - What a real one adds
`days/day-76-vad-and-non-blocking-tools/parts/04-in-production/4.2-what-a-real-one-adds.md` · level `production` · ids ADK-56, ADK-77

The lab runs a tool inside a live session correctly, and the distance between that and a tool layer you would let a stranger talk to is not vague "hardening" — it is a list of nine specific things, and almost every one of them is about what happens when a tool is slow, cancelled or wrong, which is exactly the ground the happy path never walks over.

## Papers - read after the parts

### doi:10.1002/j.1538-7305.1975.tb02840.x - An Algorithm for Determining the Endpoints of Isolated Utterances
`days/day-76-vad-and-non-blocking-tools/papers/01-endpoint-detection.md`

Finding where a word starts sounds like a question about loudness, and it is not: the first sound of "safe" or "four" is quieter than the room. The method that fixed this uses energy to find a confident interior and then a second, completely different measurement — how often the signal changes sign — to walk outwards to the real edges. Switching that second pass off in the demo below clips 8 frames off a 24-frame word, four at each end.

