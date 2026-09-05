---
day: 59
phase: 8
phase_name: "Workflows and multi-agent"
title: "Phase gate + failure lab — loops, runaway agents, containment"
ids: ["AG-21", "SEC-04"]
principles: [1, 2, 4, 7, 8, 10, 11, 13, 14, 15, 16, 17, 18]
kind: gate
plan_version: "v2.2.1"
parts: 24
generated: "2026-09-05"
status: written
lab_scaffolded: true
commit: ""
---

# Day 59 — Phase gate and failure lab: loops, runaway agents, containment

> **Yesterday (Day 58):** the triage graph v1. Intake, classify, research, draft and review wired
> into one graph that takes a real ticket from the archive to a drafted, reviewed reply — the Phase 8
> deliverable, running end to end.
> **Today:** the uncomfortable half. You will build four runaways **on purpose**, inside a padded
> cell, watch which brakes catch which, find two brakes that do not hold, and then audit whether
> Phase 8 is honestly finished. The day spends **zero** model calls and would have spent fourteen.
> **Tomorrow (Day 60):** Phase 9 opens with durable execution — resume, replay and idempotency,
> which is the half of "kill it mid-run" that today deliberately does not build.

---

## §1 Where we are

Phase 8 gave Sutra a machine that runs on its own. Day 53 replaced the agent tree with a graph of
nodes and edges, Day 54 gave it sequential, parallel and loop shapes, Day 55 gave it delegation,
Day 56 planning, Day 57 an orchestrator and a critic, and Day 58 wired all of it into a desk that
takes a ticket and produces a reviewed reply without anybody watching.

That is the most capability this project has ever had in one run, and Principle 13 says **blast
radius before capability**. Until this week the principle was easy to honour, because nothing could
run for long by itself: a tool call either returned or it raised. Today it stops being easy.

Here is the day as a scene. There is a tap in the back washroom of a flat that does not quite close.
It drips. You go away for three weeks and come back to a bill. Nothing broke. The tap did its job,
the pipe did its job, the drain did its job. What was missing was anybody deciding that enough water
had come out.

Every runaway in this day is that tap. Not a broken part — a **missing stop**. A critic that asks for
one more revision, which is what a critic is for. Two desks that each correctly route a question to
the other. A planner that splits a task into three, three times. A research loop that reads one more
page. Each of those is a component working exactly as designed, and each of them, given a graph and
nobody watching, will run until something outside it says no.

So the day has two jobs and they feed each other. **The failure lab** builds the runaways and
measures which brakes catch them, and it finds two brakes that look right and are not: a rule written
in a prompt, and a fuse set to zero. **The gate** then takes that evidence and answers the question
Phase 8 cannot leave without answering — is this finished? — with six criteria, each of which is a
command with an exit code rather than an opinion.

Three of the six come out green. Two come out amber. One is red for a reason that has nothing to do
with Phase 8, and the day says so rather than rounding it up.

---

## §2 The map

Twenty-four parts in six sections, plus one paper. Section 1 is the taxonomy: four shapes, one per
part, each measured. Section 2 is the ladder of brakes, from the tightest to the outermost, and the
argument that decides where each one belongs. Section 3 is the failure lab proper — four brakes that
do not hold, with the real output. Section 4 is the property all of it is for: stopping is an answer.
Section 5 is the Phase 8 gate, one acceptance criterion per part. Section 6 is what a professional
carries away and what Phase 9 takes over. The day climbs `foundation → working → production`.

### Section 1 — `01-four-runaways`: "runaway" is four failures wearing one word

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [A runaway is a missing stop, not a mistake](parts/01-four-runaways/1.1-a-runaway-is-a-missing-stop.md) | why every runaway here is built from correct parts | `foundation` |
| 1.2 | [The critic who is never satisfied](parts/01-four-runaways/1.2-the-critic-who-is-never-satisfied.md) | 13 calls with no brake, 4 with a fuse, and a default of 500 | `working` |
| 1.3 | [Two caps, one rally, twice the work](parts/01-four-runaways/1.3-two-caps-one-rally-twice-the-work.md) | two desks capped at 3 produced a rally of 7 | `working` |
| 1.4 | [The shape that grows by a power](parts/01-four-runaways/1.4-the-shape-that-grows-by-a-power.md) | branch 2, depth 5 → 63 calls against a tier of 20 | `working` |
| 1.5 | [💥 The quiet runaway the fuse cannot see](parts/01-four-runaways/1.5-the-quiet-runaway-the-fuse-cannot-see.md) | 201 iterations under `max_llm_calls=4`, no error | `working` |

### Section 2 — `02-where-a-brake-goes`: four brakes, four altitudes, one placement rule

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [A guard is only a guard if it is outside](parts/02-where-a-brake-goes/2.1-a-guard-is-only-a-guard-if-it-is-outside.md) | the same rule: 21 calls, 4 calls, 3 calls | `working` |
| 2.2 | [The loop counter, checked before the quality condition](parts/02-where-a-brake-goes/2.2-the-loop-counter.md) | 3 against 4, and the cap that survives a 429 | `working` |
| 2.3 | [The run fuse: what `max_llm_calls` counts](parts/02-where-a-brake-goes/2.3-the-run-fuse.md) | scope is the invocation; the blind spot is total | `working` |
| 2.4 | [The circuit breaker: the brake denominated in requests](parts/02-where-a-brake-goes/2.4-the-circuit-breaker.md) | 0 calls when it refuses, 1 when it logs | `production` |
| 2.5 | [The kill switch and what it leaves on the floor](parts/02-where-a-brake-goes/2.5-the-kill-switch-and-what-it-leaves.md) | two kills, identical state, one call apart | `production` |

### Section 3 — `03-brakes-that-do-not-hold`: the failure lab

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [💥 The guard the agent can talk past](parts/03-brakes-that-do-not-hold/3.1-the-guard-the-agent-can-talk-past.md) | and the guard that is code and gets routed around | `production` |
| 3.2 | [💥 Three retries become twenty-seven](parts/03-brakes-that-do-not-hold/3.2-three-retries-become-twenty-seven.md) | 27 calls for one request; 1 with a shared budget | `production` |
| 3.3 | [💥 The fuse set to zero, which is no fuse at all](parts/03-brakes-that-do-not-hold/3.3-the-fuse-set-to-zero.md) | 16 calls under a limit of 0, and a warning nobody sees | `production` |
| 3.4 | [💥 The brake loosened for one ticket](parts/03-brakes-that-do-not-hold/3.4-the-brake-loosened-for-one-ticket.md) | 60 a night becomes 204, no test fails | `production` |

### Section 4 — `04-fail-stop`: the property all of it is for

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [Stopping is an answer; continuing is not](parts/04-fail-stop/4.1-stopping-is-an-answer.md) | the honest run exits 1 and the invented one exits 0 | `production` |
| 4.2 | [What a refusal has to say to be worth anything](parts/04-fail-stop/4.2-what-a-refusal-has-to-say.md) | five fields, and one decision instead of six tasks | `production` |

### Section 5 — `05-the-gate`: the Phase 8 audit, one criterion per part

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [Criterion 1 — the triage graph runs end to end](parts/05-the-gate/5.1-criterion-1-end-to-end.md) | 5 calls answered, 0 for an unknown ticket · 🟢 | `production` |
| 5.2 | [Criterion 2 — every shape has a brake, and the brake is tested](parts/05-the-gate/5.2-criterion-2-every-shape-has-a-brake.md) | 4×4, and one row covered by a single cell · 🟢 | `production` |
| 5.3 | [Criterion 3 — the eval goes red when a brake is removed](parts/05-the-gate/5.3-criterion-3-the-eval-goes-red.md) | four checks, four ways to break them · 🟢 | `production` |
| 5.4 | [Criterion 4 — the request budget is measured, not estimated](parts/05-the-gate/5.4-criterion-4-the-budget-is-measured.md) | 14 would-be, 0 actual — and 60 a night · 🟡 | `production` |
| 5.5 | [Criterion 5 — the freshness check](parts/05-the-gate/5.5-criterion-5-the-freshness-check.md) | three pins behind, one with no ledger row · 🟡 | `production` |
| 5.6 | [Criterion 6 — the IDs, and the verdict written down](parts/05-the-gate/5.6-criterion-6-the-ids-and-the-verdict.md) | what a gate does with a phase that is not green · 🔴 | `production` |

### Section 6 — `06-in-production`: the discipline, and the boundary

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 6.1 | [Brakes are a system with an invariant](parts/06-in-production/6.1-brakes-are-a-system.md) | two relations, and no single number fixes them | `production` |
| 6.2 | [🅿️ What Phase 9 takes over](parts/06-in-production/6.2-what-phase-nine-takes-over.md) | deadlines, bulkheads and resumption, deliberately not built | `production` |

### The paper — read it **after** the parts

| # | Paper | What it gives you |
| --- | --- | --- |
| 01 | [Fail-stop processors](papers/01-fail-stop-processors.md) · `doi:10.1145/357369.357371` | why halting on a detected fault makes every other component cheaper to design — and why the field kept the failure model and dropped the device |

**Read the sections in order.** Section 2 is unreadable without section 1's four shapes, section 3 is
a set of failures of section 2's brakes, and section 5 audits evidence that sections 1 to 4 produce.
Read the paper last: Principle 4 at the scale of a day, so that "what survived and what did not"
lands on brakes you have already watched fire.

---

## §3 Setup — run this

**No package is added today and no pin moves.** `google-adk` stays at `2.7.1`, `google-genai` at
`2.19.0`. Everything in this day is the standard library plus ADK, which is already installed.
`git diff pyproject.toml uv.lock` must be empty when you finish.

```bash
# 1 - the day's lab
cd days/day-59-runaway-agents-contained
mkdir -p lab lab/papers/fail-stop

# 2 - the three shared modules everything imports
touch lab/_fake.py lab/_desk.py lab/_ledger.py

# 3 - section 1: the four runaways
touch lab/loop.py lab/pingpong.py lab/fanout.py lab/quiet.py

# 4 - section 2: the four brakes
touch lab/outside.py lab/counter.py lab/fuse.py lab/breaker.py lab/kill.py

# 5 - section 3: the brakes that do not hold
touch lab/storm.py lab/zero.py lab/loosen.py

# 6 - section 4: fail-stop
touch lab/refuse.py

# 7 - section 5: the six criteria
touch lab/endtoend.py lab/guards.py lab/budget.py lab/fresh.py lab/ids.py

# 8 - the day's gate
touch lab/gate.py

# 9 - the paper demo
touch lab/papers/fail-stop/processor.py lab/papers/fail-stop/demo.py
cd -

# 10 - the test file you fill in today (you type every line)
touch tests/test_containment.py

# 11 - confirm the runtime surfaces this day depends on
python -c "from google.adk.agents.run_config import RunConfig; print(RunConfig.model_fields['max_llm_calls'].default)"
python -c "import inspect; from google.adk.plugins.base_plugin import BasePlugin; print(inspect.signature(BasePlugin.before_model_callback))"
```

**Steps 11 are the ones that matter.** The first prints `500`, which is the number
[2.3](parts/02-where-a-brake-goes/2.3-the-run-fuse.md) prices against this project's free tier. The
second prints the plugin hook signature that [2.4](parts/02-where-a-brake-goes/2.4-the-circuit-breaker.md)
hangs the quota breaker on. If either fails, the ADK install is not what this day assumes and nothing
below is valid.

`lab/_desk.py` is the lab's own copy of Day 58's five-station triage graph, with every station a
plain function. That duplication is deliberate and confined to `lab/`, for the same reason Day 50
kept its own copy of the retrieval arithmetic: every measurement in this day must be reproducible
from a fresh checkout without the project module being finished.

---

## §4 Build brief

### The project code — `sutra/containment.py`, and you type every line

One new module. Nothing in `sutra/` is rewritten.

| Symbol | Shape | What it must do |
| --- | --- | --- |
| `MAX_REVISIONS` | `int` | the loop cap, with a comment naming the run it came from (2.2) |
| `RUN_FUSE` | `int` | the value passed to `RunConfig(max_llm_calls=...)`, with its arithmetic (2.3, 6.1) |
| `DAILY_FLOOR` | `int` | the ledger level below which the breaker refuses, with its reason (2.4) |
| `QuotaBreakerPlugin` | `BasePlugin` | refuses in `before_model_callback`; **raises**, never returns (2.4) |
| `brake_report` | `() -> list[str]` | the arithmetic from 6.1, as findings, so CI can run it |

- **Every brake constant carries a comment naming the run it came from**, with the date.
  `lab/gate.py` fails the day on a bare number, which is the ritual half of Principle 7 pointed at a
  containment parameter — the same rule Day 50 applied to `TOP_K`.
- **`QuotaBreakerPlugin` must raise.** A version that logs and returns `None` is measured in
  [2.4](parts/02-where-a-brake-goes/2.4-the-circuit-breaker.md) at one model call against zero, and
  `gate.py` checks that the module contains a `raise` at all.
- `RUN_FUSE` must be **greater than zero**. [3.3](parts/03-brakes-that-do-not-hold/3.3-the-fuse-set-to-zero.md)
  is the reason, and the startup assertion in that part is the shape to copy.

**`TODO(me)` markers left for you:**

- **2.2** — choose `MAX_REVISIONS` and write, in the comment beside it, **where a capped draft goes**.
  Accepted-at-the-cap and accepted-on-merit are different outcomes and the customer cannot tell them
  apart unless you route them differently.
- **2.3** — choose `RUN_FUSE` from the worst case, not from a round number. Write the arithmetic in
  the comment: [5.1](parts/05-the-gate/5.1-criterion-1-end-to-end.md) measures five calls per
  answered ticket at two revisions, and [6.1](parts/06-in-production/6.1-brakes-are-a-system.md)
  gives the two relations it has to satisfy.
- **2.4** — choose `DAILY_FLOOR` and say in the comment **what the reserve is for**. Zero is the
  wrong answer and the part explains why; the number you pick should be justified by something you
  intend to spend it on.
- **3.1** — run the inbound-edge count from
  [3.1](parts/03-brakes-that-do-not-hold/3.1-the-guard-the-agent-can-talk-past.md) against your own
  desk, find the node with more than one inbound edge, and write down whether every path into it
  passes a limit.
- **5.2** — the coverage table has one row covered by a single cell. Decide whether to build a run
  deadline or to accept the risk, and write the decision down with the trigger for revisiting it. If
  you accept it, that is an ADR.
- **6.1** — `loosen.py` is red at the shipped settings and no single constant fixes it. Decide what
  the nightly batch size actually is, and write the sentence that says what you are giving up.

### The tests — `tests/test_containment.py`, and you type every line

Five test functions, named as sentences, all offline and all fast:

| Test | What it pins |
| --- | --- |
| `test_run_fuse_is_a_positive_number` | `RUN_FUSE > 0`, because zero disables it (3.3) |
| `test_every_brake_constant_carries_its_provenance` | a comment beside each of the three (Principle 7) |
| `test_the_breaker_raises_rather_than_returning` | `pytest.raises(QuotaExhausted)` below the floor (2.4) |
| `test_the_breaker_permits_when_there_is_headroom` | the guard against a rule so strict it refuses everything |
| `test_brake_report_is_red_when_the_batch_exceeds_the_quota` | the arithmetic from 6.1, as a test |

The fourth is the one people leave out, and it is the same omission Day 50 warned about: a refusal
rule with no positive test passes perfectly while refusing everything.

### The lab — twenty-one scripts, all of which run, none of which call a model

| File | What it does | Taught in |
| --- | --- | --- |
| `lab/_fake.py` | `CountingLlm`, the lab wall, and the two drivers | all |
| `lab/_desk.py` | Day 58's five stations as plain functions, with `kill_at` and `leaky_intake` | 2.5, 5.1 |
| `lab/_ledger.py` | the quota ledger, the floor and `QuotaExhausted` | 2.4 |
| `lab/loop.py` | the never-satisfied critic, with and without a fuse | 1.2 |
| `lab/pingpong.py` | two desks, two caps, one rally | 1.3 |
| `lab/fanout.py` | branching against depth, priced against the free tier | 1.4 |
| `lab/quiet.py` | 201 iterations under a fuse of 4 | 1.5 |
| `lab/outside.py` | the same rule in a prompt and in an edge | 2.1, 3.1 |
| `lab/counter.py` | cap-then-quality against quality-then-cap, and a 429 | 2.2 |
| `lab/fuse.py` | `max_llm_calls` at two settings, and the default priced | 2.3 |
| `lab/breaker.py` | the plugin, raising and swallowing | 2.4 |
| `lab/kill.py` | three kill points and what each leaves | 2.5 |
| `lab/storm.py` | retries multiplying, and one shared budget | 3.2 |
| `lab/zero.py` | a fuse of zero, with and without the warning | 3.3 |
| `lab/loosen.py` | the brake arithmetic, as findings with an exit code | 3.4, 6.1 |
| `lab/refuse.py` | fail-stop, carry-on and a thin refusal | 4.1, 4.2 |
| `lab/endtoend.py` | three tickets, three paths, criterion 1 | 5.1 |
| `lab/guards.py` | four shapes against four brakes, criterion 2 | 5.2 |
| `lab/budget.py` | would-be against actual, criterion 4 | 5.4 |
| `lab/fresh.py` | pins, ledger rows and the manual list, criterion 5 | 5.5 |
| `lab/ids.py` | Phase 8's IDs against the day hubs, criterion 6 | 5.6 |
| `lab/gate.py` | the day's definition of done, as findings | §5 |
| `lab/papers/fail-stop/` | the paper, made runnable, with its ablation | paper 01 |

---

## §5 The eval that must be able to fail

Four checks with exit codes, and every one of them runs on zero model calls.

**The gate** is the day's definition of done, and it is red until the module is written:

```bash
uv run python days/day-59-runaway-agents-contained/lab/gate.py; echo "exit: $?"
```

Measured on 2026-09-05, before anything was written: `1-5: sutra\containment.py does not exist yet`,
`findings: 1`, `exit: 1`. When it prints `findings: 0` it means five symbols exist, three constants
carry their provenance, the module raises somewhere, and both `endtoend.py` and `guards.py` are green.

**The three criteria that can be broken on purpose**, which is Principle 11 with evidence:

```bash
cd days/day-59-runaway-agents-contained/lab
uv run python endtoend.py; echo "exit: $?"          # 0
uv run python endtoend.py --leaky-intake; echo "exit: $?"   # 1
uv run python guards.py; echo "exit: $?"            # 0
uv run python guards.py --drop "loop cap"; echo "exit: $?"  # 1
uv run python loosen.py; echo "exit: $?"            # 1, and it should be
cd -
```

**`loosen.py` is red at the shipped settings on purpose.** It reports that a nightly batch of twelve
tickets needs sixty model calls against a free tier of twenty. That is a real finding about this
project, not a broken script, and [6.1](parts/06-in-production/6.1-brakes-are-a-system.md) works
through why no single constant fixes it.

**The test suite**, offline and green:

```bash
uv run python -m pytest tests/test_containment.py -q -m "not live"
```

Red as shipped, because `tests/test_containment.py` is empty until you write it.

**And every measurement in the day, re-runnable:**

```bash
cd days/day-59-runaway-agents-contained/lab
uv run python loop.py --wall 12; uv run python loop.py --fuse 4
uv run python pingpong.py; uv run python pingpong.py --cap 2; uv run python pingpong.py --fuse 4
uv run python fanout.py --depth 2; uv run python fanout.py --branch 2 --depth 5
uv run python quiet.py; uv run python quiet.py --wall 200
uv run python outside.py; uv run python outside.py --obedient; uv run python outside.py --in-graph
uv run python counter.py; uv run python counter.py --quality-first
uv run python counter.py --critic-fails; uv run python counter.py --critic-fails --quality-first
uv run python fuse.py; uv run python fuse.py --cap 8; uv run python fuse.py --default
uv run python breaker.py; uv run python breaker.py --spent 18; uv run python breaker.py --spent 18 --swallow
uv run python kill.py; uv run python kill.py --at draft; uv run python kill.py --at review
uv run python storm.py; uv run python storm.py --layers 4; uv run python storm.py --budget-aware
uv run python zero.py; uv run python zero.py --show-warning
uv run python refuse.py; uv run python refuse.py --carry-on; uv run python refuse.py --thin
uv run python budget.py; uv run python fresh.py; uv run python ids.py
cd papers/fail-stop
FAILSTOP=1 uv run python demo.py; FAILSTOP=0 uv run python demo.py
cd -
```

Several of these end with `stopped by the LAB, not by the system`. That phrase is not decoration: it
marks the demos where **nothing Sutra ships would have stopped the run**, and telling those apart
from the ones a brake caught is the whole reading of section 1.

---

## §6 Request budget

**Free-tier Gemini**, 20 generate requests per day per model (roster and limit recorded in
`docs/PACKAGES.md` from a live 429 on Day 2).

| What | Generations |
| --- | --- |
| every part in every section | **0** |
| all twenty-one lab scripts, every flag | **0** |
| the paper demo, both arms | **0** |
| `sutra/containment.py`, the gate and the five tests | **0** |
| **Total planned** | **0 of 20** |

**Zero, and the zero is what makes the day possible rather than merely cheap.** Every model in this
lab is a `CountingLlm` — a real `BaseLlm` subclass that returns a canned string and counts itself —
so the runtime treats it as a model, `max_llm_calls` fuses on it and the plugin hooks fire around it,
while no socket is ever opened. `budget.py` prints the two numbers side by side: **fourteen would-be
provider calls, zero actual.**

That distinction is the reason a day about runaway spending can be re-run every time somebody changes
a brake, instead of once, by whoever had quota left. Studying a runaway with a live model is the one
experiment in this curriculum you genuinely cannot afford.

**Cost: $0.**

---

## §7 Traps

- **A runaway is a missing stop, not a broken part.** Every component in all four shapes is working
  as designed (1.1).
- **The brake that caught the last shape is the wrong brake for the next one.** A loop counter that
  is perfect on the tight loop is off by more than a factor of two on the ping-pong (1.1, 1.3).
- **Per-agent caps do not compose.** Two desks capped at three hand-offs each produced a rally of
  seven, with both caps respected (1.3).
- **Depth is the exponent, branching is the base.** Branch 2 at depth 5 is 63 calls — three times the
  daily free tier from one run (1.4).
- **`max_llm_calls` counts model calls and nothing else.** A retrieval loop ran 201 iterations under
  a fuse of 4 with no error at all (1.5).
- **A rule in a prompt is not a limit.** The same instruction produced 21 calls and 4 calls; the same
  rule in an edge condition produced 3, every time (2.1, 3.1).
- **Check the cap before the quality condition.** Quality-first costs one wasted call per capped run,
  and a critic that 429s means the cap is never consulted at all (2.2).
- **ADK's default `max_llm_calls` is 500**, which is twenty-five times this project's whole daily
  quota. Leaving it alone is choosing to have no run-level brake (2.3).
- **`max_llm_calls=0` means unbounded, not forbidden.** The library warns, into a logger a normal
  script never configures (3.3).
- **A breaker that logs instead of raising is a counter with an opinion.** Refusing cost 0 model
  calls; swallowing cost 1 and reported the run as finished (2.4).
- **Retries multiply.** Three attempts at three layers is 27 provider calls for one request, and the
  error being retried is a quota error (3.2).
- **Brakes are terms in an inequality.** Raising the revision cap from 2 to 8 took the nightly worst
  case from 60 calls to 204, and no test failed (3.4, 6.1).
- **A guard in code can still be routed around.** The desk's `draft` station already has two inbound
  edges; a third would bypass any limit that lives on one of them (3.1).
- **A kill leaves work done that is not work recorded.** Killing at `draft` and at `review` left
  byte-identical state and differed by a spent model call (2.5).
- **The honest path exits 1 and the invented answer exits 0.** Every alert, CI job and dashboard you
  own currently prefers the lie unless you fix it deliberately (4.1).
- **A refusal that carries nothing has paid the whole cost of fail-stop and collected none of the
  benefit** (4.2).
- **A check that has never gone red is a check with no evidence behind it** (5.3).
- **A freshness check scoped to what a script can read has quietly redefined itself** (5.5).
- **Trap #4 (plan §5.1) is the day's spine**: every brake here raises, and every version of a brake
  that returns instead was measured and was worse (2.4, 4.1).

---

## §8 Verify before you code

Read or fetched on **2026-09-05**, the day this was written.

- **`RunConfig.max_llm_calls`** — the field, its default of `500`, and the `> 0` enforcement
  condition were read from the installed `google-adk==2.7.1`:
  `python -c "from google.adk.agents.run_config import RunConfig; print(RunConfig.model_fields['max_llm_calls'].default)"`,
  and the enforcement itself in `google/adk/agents/invocation_context.py`,
  `_InvocationCostManager.increment_and_enforce_llm_calls_limit`. The adk.dev page consulted was
  `https://adk.dev/runtime/runconfig/`.
- **`BasePlugin.before_model_callback`** — signature verified with
  `python -c "import inspect; from google.adk.plugins.base_plugin import BasePlugin; print(inspect.signature(BasePlugin.before_model_callback))"`,
  giving `(self, *, callback_context: 'CallbackContext', llm_request: 'LlmRequest') ->
  'Optional[LlmResponse]'`. The adk.dev page consulted was `https://adk.dev/plugins/`.
- **`google.adk.workflow` exports** — `python -c "import google.adk.workflow as w; print(sorted(n for n in dir(w) if not n.startswith('_')))"`
  gives `BaseNode, DEFAULT_ROUTE, Edge, FunctionNode, JoinNode, Node, NodeTimeoutError, RetryConfig,
  START, Workflow, node`. **`NodeTimeoutError` and `FunctionNode.timeout` are per-node, not per-run**,
  which is the finding behind [5.2](parts/05-the-gate/5.2-criterion-2-every-shape-has-a-brake.md)'s
  empty deadline column.
- **`State.to_dict()`** — `python -c "from google.adk.sessions.state import State; print([m for m in dir(State) if not m.startswith('_')])"`.
  `dict(ctx.state)` raises `KeyError: 0`, which cost a debugging pass and is written up in
  [2.5](parts/02-where-a-brake-goes/2.5-the-kill-switch-and-what-it-leaves.md).
- **The pins, live** — `google-adk` pinned 2.7.1, latest **2.8.0**; `google-genai` pinned 2.19.0,
  latest **2.22.0**; `mcp` pinned 1.29.1, latest **2.1.1**. All three read from
  `https://pypi.org/pypi/<name>/json` today. **All three are deliberately held**, and the `mcp` major
  is blocked upstream by `google-adk`'s `mcp<2` constraint.
- **The MCP spec revision** — `https://modelcontextprotocol.io/specification/` still points at
  `schema/2026-07-28/`. Unchanged, so Addendum 01 Part 2 does not fire.
- **`doi:10.1145/357369.357371`** — *Fail-stop processors: an approach to designing fault-tolerant
  computing systems*, ACM TOCS 1(3):222–238, 1983. Verified against the Crossref record at
  `https://api.crossref.org/works/10.1145/357369.357371`; the ACM Digital Library page returns 403
  without a subscription. Row added to `docs/PAPERS.md` today.

**What no documentation says**, and what therefore had to be measured: which brake catches which
runaway. There is no page anywhere that will tell you that a per-agent cap of three produces a rally
of seven, or that a fuse of four never fires on a loop that makes no model calls. That is what
section 1 is for.

---

## §9 Say it in an interview

*"Day 59 was the phase gate for our multi-agent work, and it had two halves. The first was a failure
lab: I built four runaways on purpose behind a fake model, so the whole day cost zero provider
requests and would have cost fourteen.*

*The thing I would lead with is that 'runaway' is four different failures wearing one word, and they
are caught by different brakes. A tight loop — a critic that always asks for one more revision — is
caught by a loop counter. A ping-pong between two agents is not: I capped both desks at three
hand-offs, both caps held exactly, and the system did seven, because a counter can only count what
passes through the desk it lives in. That one is caught by the run-level fuse, which counts model
calls for the whole invocation and never asks who is calling. A fan-out bomb is the same fuse's
problem, and the number that surprised me there was branching two at depth five: sixty-three calls
against a daily free tier of twenty, from settings that both sound conservative. And the fourth
shape, the one I had not thought about before, is a loop that makes no model calls at all — a
retrieval loop. I ran two hundred and one iterations of one under `max_llm_calls=4` and the fuse
never fired, because it is implemented inside the LLM flow and the loop never enters it. That is not
a weak brake, it is an absent one, and we do not have a run deadline, so that row of our coverage
table is held up by a single loop counter somebody remembered to write.*

*The second half was about where a brake goes, and the measurement I would show is three runs of one
graph. Same rule — 'never revise more than three times' — first as a sentence in the instruction,
which produced twenty-one model calls with an uncooperative stub and four with a compliant one, and
then as an edge condition, which produced three, every time. Same rule, same model. The test I use
now is: after the run, can I tell whether the guard held without reading the model's output? If not,
it is a request rather than a control. And the corollary that caught me out is that being code is not
sufficient — a cap living in a critic node gets routed around the moment somebody adds a retry edge
into the writer, which is a smaller and more obviously correct change than the guard was.*

*The gate itself came out three green, two amber, one red, and I would rather talk about the ambers.
Our request budget is measured, not estimated — five model calls per answered ticket, zero for one we
refuse at intake — and then multiplying by a nightly batch of twelve gives sixty against an allowance
of twenty. Nobody had ever multiplied those two numbers. No single constant fixes it either; I
checked, and it is a product decision about batch size rather than a tuning one. The freshness check
found a package pinned four phases ago with no row in our package ledger, which nothing was ever
going to surface because nothing was broken — and our previous phase gate had found the same thing,
which told me our findings were being collected and not acted on.*

*The line I took away is from the paper the day teaches — fail-stop processors, 1983. A component
that can only ever produce a result makes every result untrustworthy, because nobody downstream can
tell an invented one from a real one. I built both policies over the same failure: the refusing one
printed what failed, why, what was still true and what happens next; the continuing one produced a
fluent support reply recommending a fix that appears nowhere in our archive. The second one reads
better. And the honest one exited 1 while the fabricating one exited 0, so every alert we own scored
the lie as the success — which is a thing you have to go and fix, or your own tooling will erode the
property."*

---

## §10 Done when

See [`CHECKLIST.md`](CHECKLIST.md). Every box is ticked because you ran the thing, not because you
read about it. `./m done 59` refuses to commit until they are.

---

## §11 Ledger & commit

**`docs/PROGRESS.md` — append this row** (fill in the hash after committing):

```markdown
| 59 | 2026-09-05 | AG-21, SEC-04 | 24 (+1 paper) | <hash> | ⚠️ |
```

The gate column is `⚠️` and it means it. `./m depth 59` is green, and
[5.6](parts/05-the-gate/5.6-criterion-6-the-ids-and-the-verdict.md) records why the phase is not:
days 56, 57 and 58 have no hubs on disk at the time this gate ran, so nine Phase 8 IDs are open, and
`./m check` is red on a pre-existing ruff error in `tests/test_persona.py` dating to Day 15.

**`docs/PACKAGES.md` — one row, and it is a correction rather than an addition.** The freshness check
in [5.5](parts/05-the-gate/5.5-criterion-5-the-freshness-check.md) found `mcp` pinned with no ledger
row, which has stood since Phase 5:

```markdown
| `mcp` | 1.29.1 | 2026-09-05 | pinned since Phase 5 with no row; recorded here by the Day 59 freshness check. Held at 1.x: `google-adk==2.7.1` requires `mcp<2,>=1.24`, so 2.1.1 is blocked upstream. |
```

**`docs/PAPERS.md` — one new row, added today:**

```markdown
| Fail-stop processors: an approach to designing fault-tolerant computing systems | doi:10.1145/357369.357371 | 1983 | 2026-09-05 | 59 | `days/day-59-runaway-agents-contained/papers/01-fail-stop-processors.md` |
```

**`docs/SKILL_PROVENANCE.md` — no new rows today.** Day 29's pinned row was re-checked as part of the
freshness ritual and is unchanged.

**Git commit message:**

```
day 59: phase gate + runaway containment lab - closes AG-21, SEC-04
```
