# Day 62 - Human-in-the-loop patterns

IDs closed: AG-23, ADK-46 · source: `days/day-62-human-in-the-loop/`

## Parts

### 1.1 - Four questions wearing one name
`days/day-62-human-in-the-loop/parts/01-the-shape-of-the-wait/1.1-four-questions-wearing-one-name.md` · level `foundation` · ids AG-23

"Human in the loop" is not one design but four — approve, edit, answer, take over — and they differ in what the person is shown, what they are allowed to do, what the run does meanwhile, and what happens when nobody replies.

### 1.2 - Waiting is a state, not a pause
`days/day-62-human-in-the-loop/parts/01-the-shape-of-the-wait/1.2-waiting-is-a-state-not-a-pause.md` · level `foundation` · ids AG-23

A run that holds a worker slot while a person thinks is a bug, and the measurement is blunt: on the same twelve tickets with two workers, holding finishes 5 and never starts 5, while writing the run down finishes 9 and holds no slot at all.

### 1.3 - Late, twice, or never
`days/day-62-human-in-the-loop/parts/01-the-shape-of-the-wait/1.3-late-twice-or-never.md` · level `foundation` · ids AG-23

A human is a dependency with no timeout, no retry semantics and no guarantee of replying at all, and the naive handler gets exactly one of the four possible histories right: it sends the reply twice when answered twice, and sends it after the deadline when answered late.

### 2.1 - The gate that returns one bit
`days/day-62-human-in-the-loop/parts/02-approve-or-reject/2.1-the-gate-that-returns-one-bit.md` · level `working` · ids ADK-46

require_confirmation=True on a FunctionTool turns one tool call into two: the call the model asked for, which does not run, and a second call named adk_request_confirmation carrying the exact arguments a person must agree to.

### 2.2 - Decided per call, not per wiring
`days/day-62-human-in-the-loop/parts/02-approve-or-reject/2.2-decided-per-call-not-per-wiring.md` · level `working` · ids ADK-46

require_confirmation accepts a function of the tool's own arguments, so the same tool with the same wiring stops for a person on one ticket and not on another: measured, ticket 4633 with a refund of 2400 stops and sends nothing, while ticket 4610 with no refund goes straight through.

### 2.3 - What a 'no' has to carry
`days/day-62-human-in-the-loop/parts/02-approve-or-reject/2.3-what-a-no-has-to-carry.md` · level `working` · ids ADK-46

A rejection reaches the model as the fixed string {'error': 'This tool call is rejected.'} and nothing else — measured, a reason attached to the refusal is discarded, and the agent asks the same person the same question a second time.

### 3.1 - The human changes the answer
`days/day-62-human-in-the-loop/parts/03-edit/3.1-the-human-changes-the-answer.md` · level `working` · ids ADK-46

tool_context.request_confirmation(hint=..., payload=...) sends the work itself to the person and takes back whatever they hand over, so the text that reached the customer was 132 characters the reviewer wrote, not the 156 characters the agent drafted.

### 3.2 - Approve one thing, run another
`days/day-62-human-in-the-loop/parts/03-edit/3.2-approve-one-thing-run-another.md` · level `production` · ids ADK-46

An approval is only worth anything if the call that runs is the call the person saw, and ADK 2.7.1 enforces that by re-reading the session's own history: change the ticket after the ask and the run raises ValueError: Function call arguments mismatch for ID 'fc-t-1'. and sends nothing.

### 3.3 - What the record says the customer got
`days/day-62-human-in-the-loop/parts/03-edit/3.3-what-the-record-says-the-customer-got.md` · level `production` · ids AG-23

An approval record with three fields answers 2 of 5 questions anybody will actually ask about it later, and the three it cannot answer are the three that decide whether the approval meant anything.

### 4.1 - A missing fact is not a missing permission
`days/day-62-human-in-the-loop/parts/04-ask-a-question/4.1-a-missing-fact-is-not-a-missing-permission.md` · level `working` · ids ADK-46

request_input stops the run for information rather than for permission, and the difference is visible in the pause itself: the call carries a message and a response_schema instead of an originalFunctionCall, because there is no action waiting to be allowed.

### 4.2 - A question with edges
`days/day-62-human-in-the-loop/parts/04-ask-a-question/4.2-a-question-with-edges.md` · level `working` · ids ADK-46

get_user_choice asks the same question as request_input with the answers enumerated instead of open — the pause carries {'options': ['ORD-8871', 'ORD-8874', 'neither']} rather than a message and a response_schema — and the choice between them is a choice about who does the work of interpreting the reply.

### 4.3 - The question you should not have asked
`days/day-62-human-in-the-loop/parts/04-ask-a-question/4.3-the-question-you-should-not-have-asked.md` · level `production` · ids AG-23

Of seven questions the agent asked a person about one ticket, five had their answers on that ticket already — and the two that genuinely needed a person were both judgements about what to do rather than facts about what happened.

### 5.1 - The pattern with no resume
`days/day-62-human-in-the-loop/parts/05-take-over/5.1-the-pattern-with-no-resume.md` · level `working` · ids AG-23

Take-over is the only one of the four patterns where the correct next step is for the run to end, and every piece of machinery built for the other three — the answer, the anchor, the resume — is the wrong shape for it.

### 5.2 - The run nobody closed
`days/day-62-human-in-the-loop/parts/05-take-over/5.2-the-run-nobody-closed.md` · level `production` · ids AG-23

A take-over that nobody records leaves a run at state: "open" with no error raised anywhere — still open: 1 against still open: 0 for the same work, the same reply count, and no way for the system to tell the difference.

### 6.1 - A default is a decision nobody made
`days/day-62-human-in-the-loop/parts/06-nobody-answered/6.1-a-default-is-a-decision-nobody-made.md` · level `working` · ids AG-23

There is no safe timeout policy: on the same ten approvals with four unanswered, approve sends 2 wrongly, reject holds back 2 that should have gone, and escalate gets nothing wrong and finishes nothing — leaving 4 still open.

### 6.2 - The answer to a question that no longer exists
`days/day-62-human-in-the-loop/parts/06-nobody-answered/6.2-the-answer-to-a-question-that-no-longer-exists.md` · level `production` · ids AG-23

While the question waits, the world moves: the digest of what the reviewer was shown goes from 41b4d09f1d1b to a0ecddf0b4d6, and a system that does not compare them sends a reply about a refund of 2400 on a ticket whose refund is now 0.

### 6.3 - Where the question goes
`days/day-62-human-in-the-loop/parts/06-nobody-answered/6.3-where-the-question-goes.md` · level `production` · ids AG-23

The question, the answer and the resume can each run in a different operating-system process — measured, three pids for one run — and the only thing joining them is the record in the pending store, which is why that record's fields are a design decision rather than bookkeeping.

### 7.1 - The tick box nobody reads
`days/day-62-human-in-the-loop/parts/07-what-the-human-sees/7.1-the-tick-box-nobody-reads.md` · level `production` · ids AG-23

An approval screen cannot catch a mistake in a field it does not display: measured against eight planted mistakes, the one-line screen catches 1 of 8, the summary 5 of 8, and the full card 8 of 8 — and the reviewer is the same person in all three.

### 7.2 - The card that makes checking possible
`days/day-62-human-in-the-loop/parts/07-what-the-human-sees/7.2-the-card-that-makes-checking-possible.md` · level `production` · ids AG-23

The full approval card does not merely show more fields — it performs the comparison the reviewer would otherwise have to do in their head, printing refund on the ticket 2400, refund promised in the draft 24000 and they disagree YES, which turns reading into noticing.

### 7.3 - Where ADK confirmation will not go
`days/day-62-human-in-the-loop/parts/07-what-the-human-sees/7.3-where-adk-confirmation-will-not-go.md` · level `production` · ids ADK-46

ToolConfirmation carries exactly three fields — hint, confirmed, payload — and the rejection branch of FunctionTool.run_async in google-adk==2.7.1 reads none of them except confirmed, so the deadline, the outcome vocabulary, the pending store and the reason for a refusal are all yours to build.

### 8.1 - The backlog is the real limit
`days/day-62-human-in-the-loop/parts/08-in-production/8.1-the-backlog-is-the-real-limit.md` · level `production` · ids AG-23

At 100% of tickets gated the queue never levels off — it goes 2, 20, 40, 60 and keeps climbing — and at 25% gated it stays flat at zero with the same single reviewer, which makes how much you gate a capacity decision rather than a safety preference.

### 8.2 - The three numbers to put on a wall
`days/day-62-human-in-the-loop/parts/08-in-production/8.2-the-three-numbers-to-put-on-a-wall.md` · level `production` · ids AG-23

A human-in-the-loop gate needs three standing measurements — the age of the oldest open question, the share of decisions that changed something, and the share of interruptions that were avoidable — because every failure in this day is invisible to a queue-depth dashboard.

## Papers - read after the parts

### doi:10.1016/0005-1098(83)90046-8 - Ironies of automation
`days/day-62-human-in-the-loop/papers/01-ironies-of-automation.md`

Automating the routine part of a job leaves the human the hard part and takes away the practice that made them good at it — and the demo below measures both halves: with the machine on the operator's own error rate is 59.4% against 0.0% with it off, while the system's error rate goes the other way, 26.8% against 50.0%.

