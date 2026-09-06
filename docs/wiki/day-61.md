# Day 61 - Pause/resume & checkpoints in ADK

IDs closed: ADK-44, ADK-45 · source: `days/day-61-pause-resume-checkpoints/`

## Parts

### 1.1 - The call that dropped and the call that ended
`days/day-61-pause-resume-checkpoints/parts/01-two-ways-to-stop/1.1-the-call-that-dropped-and-the-call-that-ended.md` · level `foundation` · ids ADK-44

A run that is killed and a run that raises leave the same checkpoint in the log — measured, the identical {"scored": ["4521", "4633"]} — and differ by exactly one extra event, which is the only thing telling you whether picking it up again is sensible or reckless.

### 1.2 - The token you keep while you fetch a photocopy
`days/day-61-pause-resume-checkpoints/parts/01-two-ways-to-stop/1.2-the-token-you-keep-while-you-fetch-a-photocopy.md` · level `foundation` · ids ADK-44

There is no runner.pause() in ADK: an invocation pauses only when an event carries a long-running function call nobody has answered yet, and the node is then frozen at status 4 WAITING with that call's id sitting in interrupts and a slot called resume_inputs waiting for the reply.

### 1.3 - Bring the cloth or bring the receipt
`days/day-61-pause-resume-checkpoints/parts/01-two-ways-to-stop/1.3-bring-the-cloth-or-bring-the-receipt.md` · level `working` · ids ADK-44

A start and a resume are the same method with different arguments, and giving it neither is refused in two different ways depending on the shape of your root — a BaseAgent root gets the documented ValueError, while a Workflow root never reaches that guard and fails later with a pydantic ValidationError about a missing string.

### 2.1 - Two people writing in one notebook
`days/day-61-pause-resume-checkpoints/parts/02-inside-the-box/2.1-two-people-writing-in-one-notebook.md` · level `working` · ids ADK-45

event.actions.agent_state is not one kind of record but two sharing a field — the graph writes a map of node statuses and a custom agent writes its own private object — and in a fifteen-event run that is six of the first, four of the second, and five events carrying neither.

### 2.2 - Opening the fuse box
`days/day-61-pause-resume-checkpoints/parts/02-inside-the-box/2.2-opening-the-fuse-box.md` · level `working` · ids ADK-45

The graph's checkpoint is a small readable map of node name to status — measured on a killed run it is summarise: 3 and dedupe: 2, five of eight fields left at their defaults and omitted — and the station that never started is not in the map at all.

### 2.3 - The recipe and the pan
`days/day-61-pause-resume-checkpoints/parts/02-inside-the-box/2.3-the-recipe-and-the-pan.md` · level `working` · ids ADK-45

A checkpoint holds only what you deliberately put in it — measured, three plausible local variable names appear zero times in the whole store — and the three things it structurally cannot hold are your locals, any handle owned by the dead process, and the fact that an effect already left the building.

### 2.4 - How often you press save
`days/day-61-pause-resume-checkpoints/parts/02-inside-the-box/2.4-how-often-you-press-save.md` · level `production` · ids ADK-45

Checkpoint frequency is a straight trade of storage against redone work — measured on the drill, one checkpoint per candidate costs 7,408 bytes and loses nothing, one at the end costs 1,852 bytes and loses three candidates — and the right answer is decided by what a unit of work costs, not by what a checkpoint costs.

### 3.1 - The mark on the doorframe
`days/day-61-pause-resume-checkpoints/parts/03-the-agents-own-note/3.1-the-mark-on-the-doorframe.md` · level `working` · ids ADK-45

A custom agent gets its own checkpoint — a BaseAgentState subclass written with ctx.set_agent_state and read back with _load_agent_state — and when that agent is the App's root it works exactly as advertised: killed after two candidates, a fresh process loads DedupeState(scored=['4521', '4633']) and skips them.

### 3.2 - A blank page and no page at all
`days/day-61-pause-resume-checkpoints/parts/03-the-agents-own-note/3.2-a-blank-page-and-no-page-at-all.md` · level `working` · ids ADK-45

_load_agent_state returns None when there is no checkpoint, not a defaulted object — its body is four lines and the first branch is if ctx.agent_states is None or self.name not in ctx.agent_states — so the if state is None branch is the only thing between a first run and AttributeError: 'NoneType' object has no attribute 'scored'.

### 3.3 - The rough column nobody marks
`days/day-61-pause-resume-checkpoints/parts/03-the-agents-own-note/3.3-the-rough-column-nobody-marks.md` · level `production` · ids ADK-45

The identical agent that resumes correctly as a root agent gets agent_states keys = [] when it is a node inside a Workflow — its checkpoints are in the log, six of them, written by the same code to the same file — and it rescores every candidate from the start because nothing ever hands them back.

### 3.4 - Write it on the shared board
`days/day-61-pause-resume-checkpoints/parts/03-the-agents-own-note/3.4-write-it-on-the-shared-board.md` · level `production` · ids ADK-45

Moving progress from the agent's own state into ctx.state makes it survive — but on its own that is half a repair, and the half produces a run that scores two of four candidates, reports success and exits 0; the second half is rerun_on_resume=True, and only both together give four of four.

### 3.5 - Handing back the key
`days/day-61-pause-resume-checkpoints/parts/03-the-agents-own-note/3.5-handing-back-the-key.md` · level `production` · ids ADK-45

end_of_agent=True writes a final event whose agent_state is null — the note is torn up on purpose — and resuming an already-finished invocation is therefore not a no-op: with rerun_on_resume=True it rescores all four candidates and takes the log from 15 events to 25, while with it False nothing runs at all.

### 4.1 - The monthly generator test
`days/day-61-pause-resume-checkpoints/parts/04-the-drill/4.1-the-monthly-generator-test.md` · level `working` · ids ADK-44

Before you break anything you need a known-good baseline, and the drill's is exact: 15 events, 10 checkpoints, 0 model requests, printed by a run that finishes normally — every later number in this section is read against those three.

### 4.2 - Pulling the plug mid-cycle
`days/day-61-pause-resume-checkpoints/parts/04-the-drill/4.2-pulling-the-plug-mid-cycle.md` · level `working` · ids ADK-44

os._exit(9) is the closest thing Python has to a power cut — no handlers, no flush, zero bytes of stderr — and what it leaves behind is exactly seven events: three graph checkpoints tracking the stations and two agent checkpoints holding two of four candidates.

### 4.3 - The mason who comes back in the morning
`days/day-61-pause-resume-checkpoints/parts/04-the-drill/4.3-the-mason-who-comes-back-in-the-morning.md` · level `working` · ids ADK-44

A brand-new process finishes the run the dead one started — summarise is skipped as already completed and report runs for the first time, ending at all three nodes status 3 — but the log goes 7 → 19 rather than to the baseline's 15, and the extra four events are the dedupe list being scored a second time.

### 4.4 - Written on the back of your hand
`days/day-61-pause-resume-checkpoints/parts/04-the-drill/4.4-written-on-the-back-of-your-hand.md` · level `production` · ids ADK-44

is_resumable=True and a durable store are two separate decisions, and getting only the first gives you a run that is configured to be resumable and cannot be found: same App, same flag, an in-memory service in a fresh process, and the resume dies on SessionNotFoundError: Session not found: S1.

### 5.1 - Two clerks checking one delivery
`days/day-61-pause-resume-checkpoints/parts/05-failure-lab/5.1-two-clerks-checking-one-delivery.md` · level `production` · ids ADK-45

The two checkpoint classes in ADK 2.7.1 disagree about drift: BaseAgentState is {'extra': 'forbid'} and raises extra_forbidden on a field it no longer knows, while NodeState is {'extra': 'ignore'} and accepts the same drift silently — so the strict one is the one you write, and its strictness is luck rather than design.

### 5.2 - Marked present by default
`days/day-61-pause-resume-checkpoints/parts/05-failure-lab/5.2-marked-present-by-default.md` · level `production` · ids ADK-45

An agent that produces output and never checkpoints gets a checkpoint invented for it: both stored agent_state values in the log are null, and on resume _load_agent_state returns Progress(done=[]) rather than None — so "not None" stops meaning "I have real progress".

### 5.3 - The clerk who wrote REJECTED in pen
`days/day-61-pause-resume-checkpoints/parts/05-failure-lab/5.3-the-clerk-who-wrote-rejected-in-pen.md` · level `production` · ids ADK-44

Two runs stopped at the same point with identical checkpoints resume differently: the destroyed process resumes cleanly to exit code 0, the one that raised refuses — and deleting the single error event from its store, changing nothing else, makes it resume cleanly too.

### 6.1 - The batch number on the strip
`days/day-61-pause-resume-checkpoints/parts/06-in-production/6.1-the-batch-number-on-the-strip.md` · level `production` · ids ADK-45

A checkpoint whose fields are unchanged and whose meaning changed parses without complaint — StampedState(schema_version=1, scored=['4521'], results={'4521': 3}), no error anywhere — and the only thing that turns that silent wrong answer into a refusal is a version field your code compares.

### 6.2 - The photocopy in the drawer
`days/day-61-pause-resume-checkpoints/parts/06-in-production/6.2-the-photocopy-in-the-drawer.md` · level `production` · ids ADK-45

Turning on resumability makes a second copy of the customer's words with a different lifetime from the first — the ticket text appears 4 times in a store that exists only because of checkpointing — so what goes into a checkpoint is a data-boundary decision, not a convenience one.

