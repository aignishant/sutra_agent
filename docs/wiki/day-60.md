# Day 60 - Durable execution — resume, replay, idempotency

IDs closed: AG-22, ADK-43 · source: `days/day-60-durable-execution/`

## Parts

### 1.1 - The run is not the process
`days/day-60-durable-execution/parts/01-what-a-run-is/1.1-the-run-is-not-the-process.md` · level `foundation` · ids AG-22

A run that exists only inside a running program dies with that program, and the measurement is exact: the triage graph killed after its fourth stage costs five model calls instead of three, because the two it had already paid for left no trace anybody can find.

### 1.2 - Died or failed
`days/day-60-durable-execution/parts/01-what-a-run-is/1.2-died-or-failed.md` · level `foundation` · ids AG-22

A run that died should be resumed and a run that failed should not, and the only reason your system can tell them apart is that the failing one had time to write down that it was failing — which the dying one, by definition, did not.

### 1.3 - What is safe to resume
`days/day-60-durable-execution/parts/01-what-a-run-is/1.3-what-is-safe-to-resume.md` · level `working` · ids AG-22

Four of the triage graph's five stages can be run again with no consequence and the fifth cannot, and the measurement is blunt: re-running all five produces two closure rows for one ticket, and nothing in the code notices.

### 2.1 - The log is the run
`days/day-60-durable-execution/parts/02-the-log-is-the-run/2.1-the-log-is-the-run.md` · level `working` · ids AG-22

Everything a resuming process needs — which stages finished, what they produced, what comes next — is computed from the log and from nothing else, and on a run killed after research that is three lines of a text file rebuilt into five state fields.

### 2.2 - Replay is not re-execution
`days/day-60-durable-execution/parts/02-the-log-is-the-run/2.2-replay-is-not-re-execution.md` · level `working` · ids AG-22

Rebuilding a run's state by reading its log costs zero model calls and reproduces all seven fields exactly, while rebuilding it by running the stages again costs three and reproduces nothing exactly — and confusing the two is how a "recovery" ends up more expensive than the original run.

### 2.3 - Three things that break replay
`days/day-60-durable-execution/parts/02-the-log-is-the-run/2.3-three-things-that-break-replay.md` · level `working` · ids AG-22

Three ordinary things make a step give a different answer the second time — the clock, randomness, and the model — and only the first two have a fix that costs nothing: seeding the generator makes sample reproduce exactly, and nothing you can do makes time.time() do the same.

### 2.4 - Recording the model so a replay is a replay
`days/day-60-durable-execution/parts/02-the-log-is-the-run/2.4-recording-the-model-so-a-replay-is-a-replay.md` · level `production` · ids AG-22

A resumed run that re-asks the model can get a different answer than the one the customer has already been given — measured, the same ticket is labelled auth-bug before the crash and data-loss after it, and routed to two different teams — so the model's reply is recorded in the log like any other value learned from outside.

### 2.5 - The cut that includes the message in the air
`days/day-60-durable-execution/parts/02-the-log-is-the-run/2.5-the-cut-that-includes-the-message-in-the-air.md` · level `production` · ids AG-22

A snapshot taken by photographing each part of a system in turn records a state the system was never in — measured, a desk holding ten tickets reports eleven, on every single attempt — and the repair is not a faster photograph but recording what was in transit between the parts.

### 3.1 - The uncertainty gap
`days/day-60-durable-execution/parts/03-doing-it-twice/3.1-the-uncertainty-gap.md` · level `working` · ids AG-22

Between doing a thing and writing down that you did it there is a gap no ordering can close, and both orderings are measurably wrong: log-second closes the ticket twice, log-first leaves it never closed and nothing complains.

### 3.2 - Naturally idempotent, or made so
`days/day-60-durable-execution/parts/03-doing-it-twice/3.2-naturally-idempotent-or-made-so.md` · level `working` · ids AG-22

An operation that names the result it wants is idempotent for free, an operation that names an action is not, and the measurement is three calls: closed / closed / closed against 1 / 2 / 3.

### 3.3 - The key names the intention
`days/day-60-durable-execution/parts/03-doing-it-twice/3.3-the-key-names-the-intention.md` · level `working` · ids AG-22

An idempotency key must be derived from the intention rather than minted per attempt, and the difference is the entire mechanism: three attempts with a fresh key each leave three closure rows, three attempts with a key derived from the run leave one.

### 3.4 - The ledger and the atomic window
`days/day-60-durable-execution/parts/03-doing-it-twice/3.4-the-ledger-and-the-atomic-window.md` · level `production` · ids AG-22

A correct key written in a separate transaction from the effect it protects still allows two closures for one ticket, because the crash lands between the two commits — the key and the effect must be one write or the fix has a gap of its own.

### 3.5 - Exactly-once is about effects
`days/day-60-durable-execution/parts/03-doing-it-twice/3.5-exactly-once-is-about-effects.md` · level `production` · ids AG-22

Nothing can force a request to be delivered once — three attempts deliver three times, with and without deduplication — but the effect can be forced to one, and "exactly-once" is only ever a claim about the second line.

### 4.1 - One field on the App
`days/day-60-durable-execution/parts/04-the-adk-surface/4.1-one-field-on-the-app.md` · level `working` · ids ADK-43

ADK's entire durable-execution surface is one boolean on the App — ResumabilityConfig(is_resumable=True), default False — and the class's own docstring states the guarantee in two sentences that between them contain everything section 3 spent five parts establishing.

### 4.2 - The invocation id is the claim ticket
`days/day-60-durable-execution/parts/04-the-adk-surface/4.2-the-invocation-id-is-the-claim-ticket.md` · level `working` · ids ADK-43

A resume is an ordinary run_async call with the old invocation id and no new message, and the runner refuses with a ValueError naming both requirements when you give it neither — which is also the error you get when resumability is off, so the message is not evidence about the switch.

### 4.3 - What ADK writes into the log
`days/day-60-durable-execution/parts/04-the-adk-surface/4.3-what-adk-writes-into-the-log.md` · level `production` · ids ADK-43

ADK's checkpoint is not a separate file — it is extra events in the session, carrying an agent_state field with a per-node status map, and after a crash the dead run's own record shows classify at status 3, completed and research frozen at status 2, running.

### 4.4 - The node that dies is the node that does not run
`days/day-60-durable-execution/parts/04-the-adk-surface/4.4-the-node-that-dies-is-the-node-that-does-not-run.md` · level `production` · ids ADK-43

By default a resumed ADK graph skips the node that was running when the process died and continues with its successor — measured, research runs once across both attempts, draft runs anyway, and the value research was supposed to produce is simply missing — and @node(rerun_on_resume=True) is the switch that changes it.

### 5.1 - Five stages, three kinds
`days/day-60-durable-execution/parts/05-triage-made-durable/5.1-five-stages-three-kinds.md` · level `production` · ids AG-22, ADK-43

The triage graph's five stages sort into three durability classes — freely replayable, replayable only if the answer was recorded, and effectful — and each class gets a different rerun_on_resume setting and a different obligation.

### 5.2 - Where the boundary goes
`days/day-60-durable-execution/parts/05-triage-made-durable/5.2-where-the-boundary-goes.md` · level `production` · ids AG-22, ADK-43

A checkpoint boundary is a place where nothing is in flight, and the whole engineering decision is how much work you are willing to lose between two of them — measured on the triage graph, a per-stage boundary costs at most one request of rework and a per-run boundary costs three.

### 6.1 - The resume that met different code
`days/day-60-durable-execution/parts/06-failure-lab/6.1-the-resume-that-met-different-code.md` · level `production` · ids AG-22

A log written by yesterday's code and resumed by today's is read without complaint and produces a wrong answer — the resumed run drafts against ticket=None and nothing raises — and the fix is a schema stamp on every event, which turns a silent wrong answer into a refusal.

### 6.2 - Four kills, four answers
`days/day-60-durable-execution/parts/06-failure-lab/6.2-four-kills-four-answers.md` · level `production` · ids AG-22, ADK-43

Killing the same run at five different moments produces four identical good outcomes and one bad one — two closures and a record that disagrees with the world — and the whole of this day is the difference between those two rows.

### 7.1 - What a checkpoint costs
`days/day-60-durable-execution/parts/07-in-production/7.1-what-a-checkpoint-costs.md` · level `production` · ids AG-22

Durability is paid for in bytes of customer text kept for as long as a run might be resumed — 618 bytes a run, eleven megabytes for ninety days of a small desk — and the number is small enough that the real decision is retention rather than storage.

### 7.2 - What a reviewer asks
`days/day-60-durable-execution/parts/07-in-production/7.2-what-a-reviewer-asks.md` · level `production` · ids AG-22, ADK-43

Six questions decide whether a durable system is durable — where the state lives, what is replayed versus re-executed, which steps have effects, what the key is derived from, whether the key is written atomically with the effect, and what happens on a version mismatch — and a design that cannot answer all six has a gap somewhere specific.

## Papers - read after the parts

### doi:10.1145/214451.214456 - Distributed snapshots: determining global states of distributed systems
`days/day-60-durable-execution/papers/01-distributed-snapshots.md`

A system can record a global state that it could genuinely have been in without stopping, by sending markers along its channels and letting each part decide from the markers what belongs in the snapshot — and the demo shows the alternative losing two tokens out of six.

