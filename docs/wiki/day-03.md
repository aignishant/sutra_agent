# Day 03 - The loop, hand-rolled — think, act, observe

IDs closed: AG-03 · source: `days/day-03-loop-hand-rolled/`

## Parts

### 1.1 - The navigator and the driver — what an agent is, mechanically
`days/day-03-loop-hand-rolled/parts/01-loop-anatomy/1.1-the-navigator-and-the-driver.md` · level `foundation` · ids AG-03

An agent is a loop around a stateless text model: the model reads the transcript and proposes an action as text, your code executes it and writes the result back, and this repeats until the model says it is done or your loop says enough — the model never touches the world, it only ever asks.

### 1.2 - The transcript is the world — the loop is a for-statement over Day 2's list
`days/day-03-loop-hand-rolled/parts/01-loop-anatomy/1.2-the-transcript-is-the-world.md` · level `foundation` · ids AG-03

The agent's entire universe is the list of turns you re-send on every call — not what your code did, not what your terminal shows, only what got written back — so the loop is nothing more exotic than a for statement that appends to Day 2's history list and sends it again.

### 2.1 - Tools are plain functions — there is no magic in a tool
`days/day-03-loop-hand-rolled/parts/02-tools-and-dispatch/2.1-tools-are-plain-functions.md` · level `foundation` · ids AG-03

A tool is an ordinary function that takes a string and returns a string — you can call it yourself, test it yourself, and run it a thousand times without spending a single token, because nothing about a function becomes special when a model asks for it.

### 2.2 - The dispatch table is the boundary — one dict stands between a sentence and your filesystem
`days/day-03-loop-hand-rolled/parts/02-tools-and-dispatch/2.2-the-dispatch-table-is-the-boundary.md` · level `working` · ids AG-03

The model names a tool in text and your loop looks that name up in a dictionary you wrote — so the set of things an agent can do is exactly the set of keys in that dict, which makes one small Python object the security boundary of the entire system.

### 2.3 - A failed tool is an observation, not a crash — two species of error
`days/day-03-loop-hand-rolled/parts/02-tools-and-dispatch/2.3-a-failed-tool-is-an-observation.md` · level `working` · ids AG-03

An error the model could do something about must come back as a readable observation so the model can react, while an error in your own code must raise and stop the run — and confusing the two gives you either an agent that cannot recover or an agent that hides its own bugs.

### 3.1 - A contract enforced by politeness — the system prompt is the whole protocol
`days/day-03-loop-hand-rolled/parts/03-the-protocol/3.1-a-contract-enforced-by-politeness.md` · level `working` · ids AG-03

The only thing that makes a model's reply machine-readable today is a paragraph of instructions asking it nicely to use a fixed shape — a contract with no compiler, no validator and no penalty for breaking it, which is why it works most of the time and why "most of the time" is a bug.

### 3.2 - Parsing a reply you did not write — read what is unambiguous, ignore the rest
`days/day-03-loop-hand-rolled/parts/03-the-protocol/3.2-parsing-a-reply-you-did-not-write.md` · level `working` · ids AG-03

The parser's job is not to understand the model's reply but to find the one directive in it that is unambiguous, ignore everything else on the page, and return nothing at all when there is nothing legible — because a parser that guesses is worse than a parser that fails.

### 4.1 - Assembling the loop — twenty lines where only the order matters
`days/day-03-loop-hand-rolled/parts/04-running-the-loop/4.1-assembling-the-loop.md` · level `working` · ids AG-03

Every piece of the loop already exists and every piece is trivial — the whole difficulty of this part is the sequence, because almost every agent-loop bug is something happening one line before or one line after it should.

### 4.2 - The first real run — reading a trace, and proving the answer was earned
`days/day-03-loop-hand-rolled/parts/04-running-the-loop/4.2-the-first-real-run.md` · level `working` · ids AG-03

A correct answer is not evidence that the loop worked — the only proof is a fact in the final answer that exists nowhere except in a tool result, which is why today's knowledge base contains a detail the model could not have known.

### 4.3 - The honest failure — the run that must end in 'I could not find it'
`days/day-03-loop-hand-rolled/parts/04-running-the-loop/4.3-the-honest-failure.md` · level `production` · ids AG-03

The hardest behaviour to get out of an agent is not a correct answer but a refusal to give one — a model is shaped to complete, so an empty tool result is an invitation to invent, and the run where nothing is found is the only run that tests whether your agent is trustworthy.

### 5.1 - The step budget — the brake ships with the engine
`days/day-03-loop-hand-rolled/parts/05-containment/5.1-the-step-budget.md` · level `production` · ids AG-03

The loop's bound must be a fixed number your code chose, enforced by a for over a range that nothing inside the body can extend — because the thing deciding whether to continue is the model, and the model is precisely the component that might be wrong.

### 5.2 - The transcript is a bill — why a six-step run costs far more than six calls
`days/day-03-loop-hand-rolled/parts/05-containment/5.2-the-transcript-is-a-bill.md` · level `production` · ids AG-03

Every step re-sends the entire transcript, so a run's cost is not the number of steps but the sum of a growing list — which makes a limit on step count a weak limit on step cost, and makes the length of a tool's output a budget decision rather than a formatting one.

### 6.1 - 💥 The goldfish loop — delete one line and watch the agent forget forever
`days/day-03-loop-hand-rolled/parts/06-failure-lab/6.1-the-goldfish-loop.md` · level `production` · ids AG-03

Remove the line that writes the tool's result back into the transcript and the agent repeats the same action until the step budget stops it — and the reason this is today's most valuable failure is that the model's behaviour is correct at every step, so every instinct you have will point at the wrong component.

### 7.1 - 🅿️ What a schema would have caught — the ceiling of a text protocol
`days/day-03-loop-hand-rolled/parts/07-the-text-protocol-ceiling/7.1-what-a-schema-would-have-caught.md` · level `production` · ids AG-03

Today's loop works, and it has a ceiling made of nine specific leaks — each one a thing the text protocol cannot express — and naming all nine now is what turns tomorrow's function calling from ceremony into a list of fixes with your name on it.

## Papers - read after the parts

### arXiv:2210.03629 - ReAct: Synergizing Reasoning and Acting in Language Models — the loop you just built
`days/day-03-loop-hand-rolled/papers/01-react.md`

The think → act → observe loop you hand-rolled today is a 2022 paper almost line for line, and its finding was not "let the model use tools" — it was that reasoning and acting are worse separately than together, which is why your SYSTEM prompt asks for a thought before every action.

