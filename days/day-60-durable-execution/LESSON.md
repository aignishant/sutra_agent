---
day: 60
phase: 9
phase_name: "Durability and humans"
title: "Durable execution — resume, replay, idempotency"
ids: ["AG-22", "ADK-43"]
principles: [1, 2, 4, 7, 8, 10, 11, 13, 15, 16, 17, 18]
kind: lab
plan_version: "v2.2.1"
parts: 23
generated: "2026-09-05"
status: written
lab_scaffolded: true
commit: ""
---

# Day 60 — Durable execution: resume, replay, idempotency

> **Yesterday (Day 59):** Phase 8 closed with the failure lab. The triage graph runs end to end,
> loops and fan-outs have guards, and a runaway is contained rather than survived — the gate's
> criterion was that a graph which cannot be stopped is not shippable.
> **Today:** the opposite failure. Not a run that will not stop, but one that stops and cannot be
> picked up again. Three separate ideas — **replay**, **resume**, **idempotency** — and the honest
> arithmetic for each, measured on the triage graph. The day spends **zero model calls**.
> **Tomorrow (Day 61):** ADK's checkpoint surface properly — pause, resume and what a checkpoint
> holds — which is the framework half of the mechanism today builds by hand.

---

## §1 Where we are

Phase 8 ended with a graph that works. Five stations, one command, a ticket in at one end and a
drafted, reviewed reply out of the other. Day 59 made sure it could be stopped.

Now do something ordinary to it. Somewhere between the third station and the fourth, the laptop
lid closes, or the container is rescheduled, or somebody types Ctrl-C because they thought it had
hung. Nothing dramatic. The kind of thing that happens on a Tuesday.

What have you got?

Under Phase 8's rules: nothing. The run lived inside one Python process, and the process **was**
the run. Start again from the top — and pay again for every model call you had already paid for,
out of an allowance that does not refill until tomorrow. Or, if the interruption landed one step
later, after the ticket was closed and before anything recorded that it was closed, start again
and close it a second time. Both of those are the same problem seen from two sides.

Here is the shape of the day as a scene. A support desk runs a night shift, and at two in the
morning the clerk goes home mid-ticket. At six another clerk sits down at the same desk. The only
question that decides whether this desk is a product or a toy is: **what can the morning clerk
do?** If the night clerk kept everything in their head, nothing — start over. If they wrote a line
in a book after each thing they finished, the morning clerk reads the book, skips what is done,
and carries on.

That book is today's subject, and the day is really three questions about it. What do you write in
it (§2's sections 1 and 2). What do you do about the one action that cannot be un-done — closing
the ticket — when the book cannot tell you whether it already happened (section 3). And what does
the framework already do for you, which turns out to be more than expected in one direction and
considerably less in another (section 4).

The last of those is where the day earns its keep. ADK will resume a graph for you, and by default
it **skips the node that was running when the process died** — so the run completes, reports
success, and the work of that stage never happens. Nobody guesses that correctly. It is measured
in [4.4](parts/04-the-adk-surface/4.4-the-node-that-dies-is-the-node-that-does-not-run.md).

---

## §2 The map

Twenty-three parts in seven sections, then one paper. The day climbs
`foundation → working → production`, and the sections are the three ideas, then the framework,
then the application to Sutra, then breaking it, then the operational face.

### Section 1 — what a run is · `parts/01-what-a-run-is/`

*The vocabulary and the sorting. What dies when a process dies, how to tell a crash from a
failure, and which steps you are allowed to run again.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [The run is not the process](parts/01-what-a-run-is/1.1-the-run-is-not-the-process.md) | Why a crash costs 5 model calls for a run that needs 3 | `foundation` |
| 1.2 | [Died or failed](parts/01-what-a-run-is/1.2-died-or-failed.md) | Which endings should be retried, and how you tell | `foundation` |
| 1.3 | [What is safe to resume](parts/01-what-a-run-is/1.3-what-is-safe-to-resume.md) | Four pure stages, one effectful, and what that decides | `working` |

### Section 2 — the log is the run · `parts/02-the-log-is-the-run/`

*Replay. The event log as the source of truth, what it can and cannot answer, and the three
things that stop a re-execution from reproducing a run.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [The log is the run](parts/02-the-log-is-the-run/2.1-the-log-is-the-run.md) | Rebuilding 5 state fields from 3 lines of a file | `working` |
| 2.2 | [Replay is not re-execution](parts/02-the-log-is-the-run/2.2-replay-is-not-re-execution.md) | Reading a record versus doing the work again | `working` |
| 2.3 | [Three things that break replay](parts/02-the-log-is-the-run/2.3-three-things-that-break-replay.md) | The clock, randomness, the model — and which one a seed fixes | `working` |
| 2.4 | [Recording the model so a replay is a replay](parts/02-the-log-is-the-run/2.4-recording-the-model-so-a-replay-is-a-replay.md) | One ticket triaged two ways, and the cassette that stops it | `production` |
| 2.5 | [The cut that includes the message in the air](parts/02-the-log-is-the-run/2.5-the-cut-that-includes-the-message-in-the-air.md) | Why ten tickets are counted as eleven, every time | `production` |

### Section 3 — doing it twice · `parts/03-doing-it-twice/`

*Idempotency. The gap that no ordering closes, and the key that makes it survivable.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [The uncertainty gap](parts/03-doing-it-twice/3.1-the-uncertainty-gap.md) | Both orderings are wrong; which failure do you choose? | `working` |
| 3.2 | [Naturally idempotent, or made so](parts/03-doing-it-twice/3.2-naturally-idempotent-or-made-so.md) | Naming a result versus naming an action | `working` |
| 3.3 | [The key names the intention](parts/03-doing-it-twice/3.3-the-key-names-the-intention.md) | Three closure rows become one | `working` |
| 3.4 | [The ledger and the atomic window](parts/03-doing-it-twice/3.4-the-ledger-and-the-atomic-window.md) | Why the key must be written in the effect's transaction | `production` |
| 3.5 | [Exactly-once is about effects](parts/03-doing-it-twice/3.5-exactly-once-is-about-effects.md) | What "exactly-once" can and cannot mean | `production` |

### Section 4 — the ADK surface · `parts/04-the-adk-surface/`

*ADK-43. What `google-adk==2.7.1` gives you, what it documents about its own limits, and the
default that loses a stage.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [One field on the App](parts/04-the-adk-surface/4.1-one-field-on-the-app.md) | `ResumabilityConfig`, and the contract in its docstring | `working` |
| 4.2 | [The invocation id is the claim ticket](parts/04-the-adk-surface/4.2-the-invocation-id-is-the-claim-ticket.md) | How a resume is spelled, and the four argument cases | `working` |
| 4.3 | [What ADK writes into the log](parts/04-the-adk-surface/4.3-what-adk-writes-into-the-log.md) | The real markers in a real session after a real crash | `production` |
| 4.4 | [The node that dies is the node that does not run](parts/04-the-adk-surface/4.4-the-node-that-dies-is-the-node-that-does-not-run.md) | 💥 The default that silently skips the failed stage | `production` |

### Section 5 — the triage graph made durable · `parts/05-triage-made-durable/`

*The synthesis. Sorting Sutra's own five stages, and deciding where the checkpoints go.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [Five stages, three kinds](parts/05-triage-made-durable/5.1-five-stages-three-kinds.md) | The classification the rest of the phase acts on | `production` |
| 5.2 | [Where the boundary goes](parts/05-triage-made-durable/5.2-where-the-boundary-goes.md) | 618 bytes against three model requests | `production` |

### Section 6 — the failure lab · `parts/06-failure-lab/`

*Breaking it on purpose. The two failures that survive everything above.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 6.1 | [The resume that met different code](parts/06-failure-lab/6.1-the-resume-that-met-different-code.md) | 💥 A deploy between the crash and the resume | `production` |
| 6.2 | [Four kills, four answers](parts/06-failure-lab/6.2-four-kills-four-answers.md) | 💥 Five kill points, and the one that goes red | `production` |

### Section 7 — in production · `parts/07-in-production/`

*What it costs to run, and the six questions a reviewer asks.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 7.1 | [What a checkpoint costs](parts/07-in-production/7.1-what-a-checkpoint-costs.md) | Bytes, growth shape, and three retention rules | `production` |
| 7.2 | [What a reviewer asks](parts/07-in-production/7.2-what-a-reviewer-asks.md) | The six-question checklist · 🅿️ durable execution engines | `production` |

### Papers — read **after** the parts

*Principle 4 at the scale of a day: build the mechanism, then read the proposal.*

| # | Paper | Why it is here |
| --- | --- | --- |
| 01 | [Distributed snapshots](papers/01-distributed-snapshots.md) — `doi:10.1145/214451.214456` | Where "consistent cut" comes from, and why production mostly avoids needing it |

---

## §3 Setup — run this

No package is added today. `google-adk` stays at the version already pinned, and everything else
is the standard library.

```bash
cd days/day-60-durable-execution
mkdir -p lab/papers/distributed-snapshots
touch lab/_ticket.py lab/_log.py lab/_effects.py lab/_stages.py lab/_runner.py
touch lab/nolog.py lab/died.py lab/whatstate.py lab/safe.py lab/nokey.py
touch lab/resume.py lab/rebuild.py lab/replay.py lab/clock.py lab/secondopinion.py
touch lab/cut.py lab/inflight.py lab/atleastonce.py lab/natural.py lab/keys.py
touch lab/atomic.py lab/adk.py lab/version.py lab/size.py lab/kills.py lab/gate.py
touch lab/papers/distributed-snapshots/snapshot.py lab/papers/distributed-snapshots/demo.py
touch ../../tests/test_durable.py
```

What each line is for:

- `lab/` holds twenty-five scripts and the two-file paper demo. The five beginning with an
  underscore are shared modules the others import — the ticket fixture, the log, the effect store,
  the five stages and the runner — so that every script measures the *same* run rather than its
  own.
- `lab/papers/distributed-snapshots/` is where §17.4.2 puts a paper's demo. It is given complete
  in the paper part; it is not a `TODO(me)`.
- `tests/test_durable.py` is created empty. It is yours to fill from §4, and it is the only file
  outside `days/` that today touches.

Confirm the pin rather than assuming it, and confirm the day can run at all:

```bash
grep google-adk ../../pyproject.toml
uv run python -c "import google.adk; print(google.adk.__version__)"
uv run python lab/gate.py; echo "exit: $?"
```

What each line is for:

- The `grep` and the `import` must agree. Principle 7: the pin is a claim and the import is the
  fact.
- `gate.py` must print a finding and exit `1` **before** you write anything. A day whose eval is
  green at the start has an eval that cannot go red.

---

## §4 Build brief

Everything below is yours to write. The parts explain each mechanism and the lab demonstrates it;
`sutra/durable.py` is where it becomes Sutra's.

**`sutra/durable.py`** — the durability primitives, four functions:

```python
def record_step(...): ...        # TODO(me): append one event for a finished step
def finished_steps(...): ...     # TODO(me): the steps the log says are done, in order
def resume(...): ...             # TODO(me): fold the log, then run from the first missing step
def idempotency_key(...): ...    # TODO(me): derive a stable key — see part 3.3
```

What each line is for:

- `record_step` and `finished_steps` are [2.1](parts/02-the-log-is-the-run/2.1-the-log-is-the-run.md)'s
  pair. Write them against the session store from Day 47, not against a JSONL file — the lab uses
  a file so the log can be read with your eyes, and Sutra should not.
- `resume` is [2.2](parts/02-the-log-is-the-run/2.2-replay-is-not-re-execution.md)'s split: replay
  above the log's end, re-execute below it. It must not import a stage function.
- `idempotency_key` is [3.3](parts/03-doing-it-twice/3.3-the-key-names-the-intention.md), and
  `gate.py` checks that two calls with the same arguments return the same string. Deriving it from
  anything that moves — a clock, a UUID — fails that check.

**`sutra/mcp_client.py`** — `close_ticket` finally earns its place:

```python
# TODO(me): add close_ticket to IDEMPOTENT_TOOLS, once it carries a request_id.
```

What each line is for:

- Day 44 left `close_ticket` out of that set on purpose, with a note saying it stays out until it
  carries a key. Adding it before the key exists is the one edit that would make this day a lie.

**Also yours:**

- Turn resumability on in the app factory, not inline —
  [4.1](parts/04-the-adk-surface/4.1-one-field-on-the-app.md)'s production note says why.
- Set `rerun_on_resume` **explicitly on every node** of the triage graph. Leaving it unset takes
  the default, and the default is
  [4.4](parts/04-the-adk-surface/4.4-the-node-that-dies-is-the-node-that-does-not-run.md).
- A schema version on every event, and a resume that refuses on mismatch —
  [6.1](parts/06-failure-lab/6.1-the-resume-that-met-different-code.md). This is row 6 of
  [7.2](parts/07-in-production/7.2-what-a-reviewer-asks.md)'s table, and it is honestly red until
  you write it.

---

## §5 The eval that must be able to fail

```bash
cd days/day-60-durable-execution/lab
uv run python gate.py; echo "exit: $?"
```

Red before the build brief is done, on 2026-09-05:

```text
  FAIL  sutra/durable.py does not exist - the build brief's first TODO(me) is unwritten

1 finding(s). Day 60's build brief is not done.
exit: 1
```

`gate.py` checks six things, and the one worth knowing about is the last: it calls
`idempotency_key` twice with identical arguments and fails if the two results differ. That check
is why a `uuid4()` implementation cannot pass — it is
[3.3](parts/03-doing-it-twice/3.3-the-key-names-the-intention.md)'s three-rows-versus-one made
mechanical.

Then make it go red a second way, on purpose, which is the box the checklist actually cares about:
once `sutra/durable.py` exists and `gate.py` is green, change `idempotency_key` to append
`str(time.time())` and run it again. It must fail. If it does not, the check is not checking.

The other eval today is the paper demo's ablation, which is a real RED/GREEN pair:

```bash
cd lab/papers/distributed-snapshots
uv run python demo.py; echo "exit: $?"                # verdict: consistent, exit 0
uv run python demo.py --no-markers; echo "exit: $?"   # verdict: IMPOSSIBLE, exit 1
```

---

## §6 Request budget

**Zero.** Not "a few". Zero calls to every provider.

| Provider | Requests today | Against a free-tier limit of |
| --- | --- | --- |
| Gemini (AI Studio) | 0 | RPM/RPD per `docs/PACKAGES.md` |
| Groq | 0 | — |
| OpenRouter (`:free`) | 0 | — |
| Ollama (local) | 0 | — |

Every stage that would call a model is a deterministic function carrying a **cost label** rather
than a network call: `_stages.py` has `COST = {"intake": 0, "classify": 1, "research": 0,
"draft": 1, "review": 1}`, and the scripts count those labels. That is what makes every number in
this day reproducible on a machine with no API key, and it is why the arithmetic in
[1.1](parts/01-what-a-run-is/1.1-the-run-is-not-the-process.md) and
[5.2](parts/05-triage-made-durable/5.2-where-the-boundary-goes.md) can be checked rather than
believed.

`adk.py` constructs real ADK apps, runners, sessions and graphs, and runs them — with plain
functions as nodes, so the whole resume machinery is exercised at zero cost. One model string is
named (`gemini-2.5-flash`, in `secondopinion.py`, as the model a recording was made against) and
never called.

---

## §7 Traps

1. **The trap this day exists for: ADK's default skips the node that died.** Not re-runs it —
   *skips* it, and continues to its successor. The run completes with no error and the stage's
   work never happens. `rerun_on_resume=True` per node is the fix, and it is
   [4.4](parts/04-the-adk-surface/4.4-the-node-that-dies-is-the-node-that-does-not-run.md).
2. **The edge value is not restored on a resume.** A node whose `node_input` is annotated `str`
   gets `None` and pydantic raises. Anything a resumed node needs belongs in `ctx.state`.
3. **Trap #1 from plan §5.1 (the node model).** Resumability lives on the `App` around a
   `Workflow` of nodes. A 1.x `sub_agents` tree has no resumability story, and every tutorial you
   find will show you one.
4. **Trap #4 from plan §5.1 (don't swallow exceptions).** A resume path that catches broadly to
   "be safe" turns a crash into a recorded failure, or a failure into a retry loop.
   [1.2](parts/01-what-a-run-is/1.2-died-or-failed.md) shows `BaseException` marking a Ctrl-C as a
   work failure and making a resumable run unresumable.
5. **A `commit()` between the effect and the key** undoes the key entirely. One transaction, two
   inserts — [3.4](parts/03-doing-it-twice/3.4-the-ledger-and-the-atomic-window.md).
6. **A stage-boundary crash test proves nothing about the gap.** The bug lives *inside* the
   effectful stage, and `crash_after` cannot reach it. In a real system, the same trap is testing
   with `SIGTERM`, which drains gracefully — [6.2](parts/06-failure-lab/6.2-four-kills-four-answers.md).
7. **`ResumabilityConfig` is `@experimental` in 2.7.1** and says so at runtime. Pin the version
   and test the resume path; do not assume it survives a minor bump.
8. **Inherited red:** `./m check` still fails on `tests/test_persona.py:7` (`I001`), dating to
   Day 15 and recorded in `docs/PROGRESS.md`. Nothing today touches it; `tests/` is learner code.

---

## §8 Verify before you code

Fetched on **2026-09-05**, and what each one settled:

| Source | What it gave |
| --- | --- |
| `https://adk.dev/runtime/resume/` | `ResumabilityConfig(is_resumable=True)` on the `App`; resume via `runner.run_async(..., invocation_id=...)`; **"Tools in an agent are run at least once, and may run more than once"**; *"Do not modify a stopped agent workflow before resuming it"*; Web UI and CLI resume unsupported |
| `https://adk.dev/graphs/dynamic/` | Node executions are tracked and completed sub-nodes are skipped on resume; the `rerun_on_resume` knob |
| `https://adk.dev/integrations/temporal/`, `.../restate/` | 🅿️ the durable-execution engines ADK integrates with (awareness only — both need a server, so Addendum 02 rules them out as a requirement) |
| `https://api.crossref.org/works/10.1145/214451.214456` | The paper's exact title, journal, volume, issue, pages and year. The DOI landing page returned no usable body; Crossref is the record actually opened |
| installed `google-adk==2.7.1` | Everything the docs do not state: `NodeStatus`'s seven values, `EventActions.agent_state` / `end_of_agent`, the two `ValueError` texts, and the `[EXPERIMENTAL]` warning — read with `inspect.getdoc`, `model_fields` and the installed source |

**Where the docs and the package disagree, this day teaches the package.** Two things are worth
recording as amendments-in-waiting rather than silently absorbed:

- `adk.dev/graphs/dynamic/` documents `rerunOnResume` in camel case; the installed Python
  decorator takes `rerun_on_resume`. A naming difference, not a behavioural one.
- The plan's §5 baseline says `google-adk` **2.6.3**; the repo pins **2.7.1**. A patch ahead is
  what Principle 7 expects, and it is noted here rather than passed over.

---

## §9 Say it in an interview

"We had a triage pipeline that ran fine and could not survive being interrupted, which on
Kubernetes means it could not survive a Tuesday. I split the problem into three, because they get
conflated and they have different fixes. Replay is rebuilding where you were by reading a record —
ours rebuilt seven state fields for zero model calls. Resume is continuing from the first step the
record does not mention. Idempotency is the one people underestimate: there is a gap between doing
a thing and writing down that you did it, and no ordering closes it, so you pick which failure you
want. We took effect-first, which means at-least-once, and paid for it with a key derived from the
run id, the step and the subject, written in the same transaction as the effect. That took a
kill-inside-the-write from two closure rows to one.

The thing that surprised me was the framework. ADK resumes a graph, and by default it *skips* the
node that was running when the process died and carries on to the next one — so the run completes,
reports success, and that stage's work never happened. I measured it: the failing node's body ran
exactly once across a crash and a resume, its successor ran anyway, and the value it was supposed
to produce was simply missing. There is a per-node flag that changes it, and turning it on is what
makes the idempotency work load-bearing rather than theoretical. I would not have found that from
the documentation; I found it by killing a run and counting."

---

## §10 Done when

See [`CHECKLIST.md`](CHECKLIST.md). Every box is something you have run, not something you have
read. The day is done when you can answer
[7.2](parts/07-in-production/7.2-what-a-reviewer-asks.md)'s six questions about Sutra without
looking, and when `gate.py` is green **and you have made it go red again on purpose**.

---

## §11 Ledger & commit

**`docs/PROGRESS.md`** — append this row:

```text
| 60 | <date> | AG-22, ADK-43 | 23 (+1 paper) | <hash> | ⚠️ |
```

**`docs/PACKAGES.md`** — no row. No package was added today; `git diff pyproject.toml uv.lock`
must be empty.

**`docs/PAPERS.md`** — this row was appended when the day was written:

```text
| Distributed snapshots: determining global states of distributed systems | doi:10.1145/214451.214456 | 1985 | 2026-09-05 | 60 | `days/day-60-durable-execution/papers/01-distributed-snapshots.md` |
```

**`docs/SKILL_PROVENANCE.md`** — no row. No third-party skill was sourced today.

**The commit:**

```text
day 60: durable execution — resume, replay, idempotency — closes AG-22, ADK-43
```
