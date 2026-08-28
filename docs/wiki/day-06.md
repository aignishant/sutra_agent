# Day 06 - Instructions & personas — the string the framework did not take

IDs closed: AG-05, ADK-03 · source: `days/day-06-instructions-and-personas/`

## Parts

### 1.1 - An instruction is a handbook, not a wish
`days/day-06-instructions-and-personas/parts/01-writing-the-handbook/1.1-handbook-not-a-wish.md` · level `foundation` · ids AG-05

An instruction is a specification of behaviour you can check, not a description of the mood you hope for, and the test that separates the two is whether you can name the message that would fail if the line were deleted.

### 1.2 - The six sections a handbook needs
`days/day-06-instructions-and-personas/parts/01-writing-the-handbook/1.2-six-sections-of-a-handbook.md` · level `working` · ids AG-05

An instruction that works has six named sections — role, scope, refusal script, honesty, tone and one worked example — and the reason there are six is that each one closes a different failure that happens when it is missing.

### 1.3 - Protocol does not belong in prose
`days/day-06-instructions-and-personas/parts/01-writing-the-handbook/1.3-protocol-does-not-belong-in-prose.md` · level `working` · ids AG-05

An instruction may say who the agent is and what it must refuse, but never what shape its output must be, because a shape asked for in prose is a request the model can decline and a shape declared in a schema is a rule the machinery enforces.

### 1.4 - Contradictions are randomised behaviour
`days/day-06-instructions-and-personas/parts/01-writing-the-handbook/1.4-contradictions-are-randomised-behaviour.md` · level `production` · ids AG-05

Two instructions that cannot both be obeyed do not produce a compromise, they produce a coin toss — the model breaks one of them on every turn, and which one it breaks changes from turn to turn with nothing in your code to explain it.

### 1.5 - Every line is a tax
`days/day-06-instructions-and-personas/parts/01-writing-the-handbook/1.5-every-line-is-a-tax.md` · level `production` · ids AG-05

The instruction is re-sent in full on every single turn, so a line is not a one-off cost but a standing charge — and the only line that is worth paying for forever is one whose absence would change an answer.

### 2.1 - A line you cannot probe
`days/day-06-instructions-and-personas/parts/02-testing-a-persona/2.1-a-line-you-cannot-probe.md` · level `working` · ids AG-05

A probe is a message written so that the answer is wrong if a specific line is not being followed, and a line for which you cannot write one has not been shown to do anything — which means it can never be safely removed either.

### 2.2 - The three probes every persona owes
`days/day-06-instructions-and-personas/parts/02-testing-a-persona/2.2-the-three-probes.md` · level `working` · ids AG-05

Before any persona ships it must survive three specific messages — a scope probe, an honesty probe and a happy-path probe — because those three cover the three ways an agent embarrasses you: doing something it should not, saying something untrue, and doing the right thing badly.

### 2.3 - When probes become an evalset
`days/day-06-instructions-and-personas/parts/02-testing-a-persona/2.3-when-probes-become-an-evalset.md` · level `production` · ids AG-05

A probe you run by hand tells you the agent is fine today; the same probe saved into a file that runs without you tells you the day it stops being fine — and the hard part of that conversion is not the file, it is finding something countable to assert.

### 3.1 - Where your instruction lands
`days/day-06-instructions-and-personas/parts/03-the-instruction-fields/3.1-where-your-instruction-lands.md` · level `working` · ids ADK-03

The string you put in instruction does not reach the model as your message — ADK renders it, then appends it to a dedicated system_instruction slot in the request, which is a different channel from the conversation and can already contain text you did not write.

### 3.2 - Two fields, two readers
`days/day-06-instructions-and-personas/parts/03-the-instruction-fields/3.2-two-fields-two-readers.md` · level `working` · ids ADK-03

instruction is read by your own model, on every turn, and description is read by other agents' models, when deciding whether to send work here — so writing either one for the wrong reader breaks either behaviour or routing, and neither failure looks like a bug.

### 3.3 - The static instruction that moves yours
`days/day-06-instructions-and-personas/parts/03-the-instruction-fields/3.3-the-static-instruction-that-moves-yours.md` · level `production` · ids ADK-03

Setting static_instruction does not add a second system prompt — it takes over the system slot and demotes your instruction into an ordinary user message, which is a change in how much authority your handbook carries, made by a field that looks like an optimisation.

### 3.4 - The deprecated global instruction
`days/day-06-instructions-and-personas/parts/03-the-instruction-fields/3.4-the-deprecated-global-instruction.md` · level `production` · ids ADK-03

global_instruction still works, is deprecated in favour of GlobalInstructionPlugin, and has a trap worse than its deprecation: it is read only from the root agent, so the same field on any other agent is silently ignored with no warning and no error.

### 4.1 - The instruction is a template, not a string
`days/day-06-instructions-and-personas/parts/04-state-templating/4.1-the-instruction-is-a-template.md` · level `working` · ids ADK-03

ADK reads your instruction as a fill-in-the-blank form: anything in curly braces that looks like a state key is replaced with a value from the session before the model sees it, which makes the handbook per-conversation — and makes every stray brace in it a live wire.

### 4.2 - Hard and soft contracts: {var} and {var?}
`days/day-06-instructions-and-personas/parts/04-state-templating/4.2-hard-and-soft-contracts.md` · level `production` · ids ADK-03

{var} says this agent cannot function without this value and fails the whole turn when it is missing; {var?} says use it if you have it and quietly renders nothing — so the question mark is not a safety switch you add everywhere, it is a decision about whether the value is load-bearing.

### 4.3 - A callable turns templating off
`days/day-06-instructions-and-personas/parts/04-state-templating/4.3-a-callable-turns-templating-off.md` · level `production` · ids ADK-03

instruction accepts a function as well as a string, and the moment you pass a function ADK stops substituting state into the result — so a {var} in the returned text is delivered to the model as the literal characters {var} unless your function does the substitution itself.

### 5.1 - The glass engine — adk web
`days/day-06-instructions-and-personas/parts/05-the-dev-ui/5.1-the-glass-engine.md` · level `working` · ids ADK-03

adk web sutra/desk serves a local developer UI that shows you a turn's events, state and timings instead of just its answer — which turns "it feels wrong" into "event three shows this", and that is the only kind of bug report worth making.

### 5.2 - Reading a turn's anatomy
`days/day-06-instructions-and-personas/parts/05-the-dev-ui/5.2-reading-a-turns-anatomy.md` · level `working` · ids ADK-03

A turn in the Events panel answers three questions in order — what was sent, what came back, and where the time went — and settling the first one before theorising about the second is the habit that separates debugging from guessing.

### 5.3 - An unauthenticated server on your machine
`days/day-06-instructions-and-personas/parts/05-the-dev-ui/5.3-an-unauthenticated-server.md` · level `production` · ids ADK-03

adk web starts a server with no login on any of its endpoints, and the only thing standing between that and everyone on your network is a default host of 127.0.0.1 — one flag away from being gone.

### 6.1 - 💥 The handbook that promised equipment
`days/day-06-instructions-and-personas/parts/06-failure-lab/6.1-the-handbook-that-promised-equipment.md` · level `production` · ids AG-05

Most "the model hallucinated" reports are not a model problem: the instruction promised a capability the runtime did not provide, and the model — being cooperative — closed the gap, which means the fabrication was specified rather than invented.

## Papers - read after the parts

### arXiv:2203.02155 - Training language models to follow instructions with human feedback
`days/day-06-instructions-and-personas/papers/01-instructgpt.md`

Making a language model bigger does not make it better at doing what you asked, and fine-tuning it on human demonstrations and human preference comparisons does — so instruction following is a trained behaviour, not a property of scale, and the whole practice of writing a handbook rests on somebody having done that training.

