# Day 65 - Phase gate — kill it mid-run; durable triage with human approval

IDs closed: OPS-11 · source: `days/day-65-kill-it-mid-run/`

## Parts

### 1.1 - A gate is a drill, not a review
`days/day-65-kill-it-mid-run/parts/01-drill-not-review/1.1-a-gate-is-a-drill.md` · level `foundation` · ids OPS-11

A phase gate is not a meeting where you look at the work and agree it is finished; it is the afternoon you break the thing on purpose, and Phase 9's break is a real process killed at four different moments while it is carrying a real ticket.

### 1.2 - A criterion ends in an exit code
`days/day-65-kill-it-mid-run/parts/01-drill-not-review/1.2-a-criterion-ends-in-an-exit-code.md` · level `foundation` · ids OPS-11

A gate criterion has to name the input, the path, the cost and the number that counts as failing, because a criterion two people can interpret differently is a criterion that gets interpreted generously by whoever wants to be finished.

### 1.3 - The runbook comes first
`days/day-65-kill-it-mid-run/parts/01-drill-not-review/1.3-the-runbook-comes-first.md` · level `working` · ids OPS-11

Write the drill as a numbered list of commands before you run it, because a procedure written while you still have your wits about you is the same procedure you will need on the night you have none, and every deviation from it during the drill is a finding.

### 2.1 - What has to be on disk before you can kill anything
`days/day-65-kill-it-mid-run/parts/02-the-instrument/2.1-what-has-to-be-on-disk.md` · level `working` · ids OPS-11

The drill can only test what survives the process, so the instrument keeps three separate files — how far the run got, who decided what, and what actually changed in the world — and anything not in one of them did not happen.

### 2.2 - A process you can actually kill
`days/day-65-kill-it-mid-run/parts/02-the-instrument/2.2-a-process-you-can-actually-kill.md` · level `working` · ids OPS-11

An exception is not a crash, so the drill runs the work in a real child process and stops it with os._exit, which skips every finally and loses every buffered byte — measured here as finally running in two cases out of three and nothing at all reaching the file in the third.

### 2.3 - Four moments, and why the moment is the experiment
`days/day-65-kill-it-mid-run/parts/02-the-instrument/2.3-four-moments.md` · level `working` · ids OPS-11

"Kill it mid-run" is not one test but four, because the interesting thing about a crash is never that it happened — it is which two writes it landed between, and the four gaps in this system fail in four different ways.

### 3.1 - K1 — killed after the work, before the checkpoint
`days/day-65-kill-it-mid-run/parts/03-four-kills/3.1-killed-before-the-checkpoint.md` · level `working` · ids OPS-11

A crash between doing a stage and recording it means the stage runs again on resume, which is correct and is not free: the run log shows the research request paid for twice and the whole run costs five provider requests instead of four.

### 3.2 - K2 — killed after the checkpoint, before the gate
`days/day-65-kill-it-mid-run/parts/03-four-kills/3.2-killed-after-the-checkpoint.md` · level `working` · ids OPS-11

A crash after a stage has been recorded costs nothing to redo, and the resumed run proves it by reinstating four stages and spending exactly one request on the only stage that had not finished.

### 3.3 - K3 — killed while parked, waiting for the human
`days/day-65-kill-it-mid-run/parts/03-four-kills/3.3-killed-while-parked.md` · level `working` · ids OPS-11

A run waiting for a person is the easiest thing in the world to kill correctly, because it is not holding anything — and the drill proves that by killing it from outside, with a signal the run has no code path for, and watching the resume cost zero requests.

### 3.4 - K4 — killed inside the effect window
`days/day-65-kill-it-mid-run/parts/03-four-kills/3.4-killed-inside-the-effect-window.md` · level `production` · ids OPS-11

Between doing a thing and recording that you did it there is a gap, and a crash in that gap is unrecoverable in principle — so the only fix is to make the doing and the recording one write, which is what this drill's keyed mode is and why K4 is the kill that decides the phase.

### 3.5 - Two closes, and none — the failure that exits zero
`days/day-65-kill-it-mid-run/parts/03-four-kills/3.5-two-closes-and-none.md` · level `production` · ids OPS-11

Both ways of getting the effect window wrong end in a process that exits 0, prints close, and looks exactly like success — one having closed the ticket twice and the other having closed it never — which is why the drill counts rows in a file instead of reading exit codes.

### 4.1 - Four questions, three months later
`days/day-65-kill-it-mid-run/parts/04-the-trail/4.1-four-questions-three-months-later.md` · level `working` · ids OPS-11

An audit trail is not a log you can read — it is a set of specific questions somebody will ask when everyone has forgotten, and the test of it is whether each question can be answered from rows on disk with nobody available to interpret them.

### 4.2 - The trail that cannot answer
`days/day-65-kill-it-mid-run/parts/04-the-trail/4.2-the-trail-that-cannot-answer.md` · level `production` · ids OPS-11

Store a pointer to the payload instead of the payload, and the system keeps working perfectly while two of the four audit questions silently stop having answers — a failure with no error, no alarm and no symptom until somebody asks.

### 4.3 - What a record must contain
`days/day-65-kill-it-mid-run/parts/04-the-trail/4.3-what-a-record-must-contain.md` · level `production` · ids OPS-11

A field belongs in an audit record only if you can name the question it answers, and the rule that follows — every field maps to a question, every question maps to a field — is what keeps a trail from thinning one reasonable decision at a time.

### 5.1 - Criterion 1 — it resumes, once
`days/day-65-kill-it-mid-run/parts/05-seven-criteria/5.1-it-resumes-once.md` · level `production` · ids OPS-11

The headline criterion of Phase 9 is one command over four kills, and it passes only when every kill ends in exit 0 and exactly one close — two conditions, because either one alone is passable by a broken system.

### 5.2 - Criterion 2 — the gate cannot be bypassed
`days/day-65-kill-it-mid-run/parts/05-seven-criteria/5.2-the-gate-cannot-be-bypassed.md` · level `production` · ids OPS-11

Four attempts to reach the write without a valid decision — pending, rejected, re-decided and tampered — and the fourth is the one that matters, because approving one text and executing another is a bypass that leaves the gate looking perfectly intact.

### 5.3 - Criterion 3 — the trail answers from rows
`days/day-65-kill-it-mid-run/parts/05-seven-criteria/5.3-the-trail-answers-from-rows.md` · level `working` · ids OPS-11

Section 4's four questions become a command that exits non-zero when any of them cannot be answered from files alone, which turns "we have an audit trail" from a claim about intentions into a check that fails in the build.

### 5.4 - Criterion 4 — the budget is measured
`days/day-65-kill-it-mid-run/parts/05-seven-criteria/5.4-the-budget-is-measured.md` · level `production` · ids OPS-11

Durability is not free — a kill before a checkpoint costs a repeated request — and the criterion is that the price is a number somebody counted from the log rather than an assumption, because a cost nobody measures is a cost that grows.

### 5.5 - Criterion 5 — the freshness check
`days/day-65-kill-it-mid-run/parts/05-seven-criteria/5.5-the-freshness-check.md` · level `production` · ids OPS-11

Every phase gate re-asks whether the world moved under the code — the framework, the protocol revision, the free tiers — and reports findings with dates, because "we checked and nothing had changed" is a result and silence is not.

### 5.6 - Criterion 6 — every day is written
`days/day-65-kill-it-mid-run/parts/05-seven-criteria/5.6-every-day-is-written.md` · level `working` · ids OPS-11

A phase cannot be green while a day inside it is unwritten, and the check reads the plan's day map on one side and the folders on disk on the other — never assuming a day exists because the plan mentions it.

### 5.7 - Criterion 7 — no open IDs in the phase
`days/day-65-kill-it-mid-run/parts/05-seven-criteria/5.7-no-open-ids.md` · level `working` · ids OPS-11

Every concept the plan assigns to Phase 9 must be declared by a day that exists, and the check compares the plan's assignment against each hub's own frontmatter — reporting the difference rather than asserting that there is none.

### 5.8 - The verdict — green, or a named list
`days/day-65-kill-it-mid-run/parts/05-seven-criteria/5.8-the-verdict.md` · level `production` · ids OPS-11

The gate runs all seven criteria, prints the label of every failing one, and refuses to summarise — because a phase is either green or it is a specific list of things that are not done, and "mostly green" is not a state anything can act on.

### 6.1 - Draining versus killing, and why you must test the crash
`days/day-65-kill-it-mid-run/parts/06-in-production/6.1-draining-versus-killing.md` · level `production` · ids OPS-11

Real systems stop processes politely almost every time, which is exactly why the polite path is the only one that ever gets tested — and the ungraceful stop, which is the one that loses data, is met first in production unless you go and cause it.

### 6.2 - Rotate the drill
`days/day-65-kill-it-mid-run/parts/06-in-production/6.2-rotate-the-drill.md` · level `production` · ids OPS-11

A gate that runs the same four kills for ever stops measuring durability and starts measuring compliance with four kills, so the criteria are a list you add rows to — and part 1.1's warning, that a gate which finds nothing has not looked, is a standing instruction rather than an observation about today.

