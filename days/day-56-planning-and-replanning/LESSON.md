---
day: 56
phase: 8
phase_name: "Workflows and multi-agent"
title: "Planning patterns — plan-and-execute, replanning"
ids: ["AG-17", "AG-18"]
principles: [1, 2, 4, 7, 8, 10, 11, 13, 15, 16, 17, 18]
kind: lab
plan_version: "v2.2.1"
parts: 23
generated: "2026-09-05"
status: written
lab_scaffolded: true
commit: ""
---

# Day 56 — Planning patterns: plan-and-execute and replanning

> **Yesterday (Day 55):** the agent learned to choose a *colleague*. A call that comes back and a
> hand-over that does not, priced in requests, with a routing loop that spent twelve of them going
> nowhere.
> **Today:** the agent chooses the *steps*. It writes a list before it does anything, walks the list,
> and — the half that makes it honest — finds out what to do when the list turns out to be built on
> something false. Every number in this day comes from a run, and the day spends **zero** model
> calls.
> **Tomorrow (Day 57):** multi-agent design — an orchestrator, and a Writer↔Critic loop where the
> thing being revised is the answer rather than the plan.

---

## §1 Where we are

Day 53 gave you a graph you draw before anything runs. Day 54 taught it to go in order, in parallel
and round a loop. Day 55 taught one agent to hand work to another. All three decide **structure** in
advance, and all three are the right way to build most of a system.

Today is about the request that does not fit in a drawn structure, and it arrives at a support desk
constantly: *"Compare tickets 4521 and 4610 and tell me whether 4633 is the same underlying bug, then
find the article with the fix."* Nobody drew that. It is three or four different pieces of work whose
identity depends on the sentence somebody typed a second ago.

There are exactly two ways to handle it, and the day is built on the difference between them.

One is to go and look at the first thing, read it, and decide the next thing from what you just read.
That is the market without a list: every step is a sensible response to what is in front of you, and
you come home with a full bag and no rice.

The other is to read the whole request first and write the list down before you move. That is reading
all five exam questions before you pick up your pen: it costs a moment of not writing, and it buys
you the shape of the whole task before you commit to any of it.

The obvious lesson is that the list wins. **The measurement says something more interesting.** Run
both over the same request with the same answer key and they score the same — and miss completely
different things. The list covers everything you *named* and reaches nothing you did not; the trail
finds an article you could never have named and quietly drops a ticket you asked about by name. Two
strategies, one number, two different holes. That result is part 2.3 and it decides which stage of
Day 58's triage graph gets which strategy.

Then the second half of the day, which is where planning earns its keep or does not. A plan is a
**prediction**, and predictions are wrong. Some of that wrongness is loud — the ticket does not exist,
the step fails, you replan. Most of it is not. A step succeeds and tells you nothing. A ticket is
merged and closed while you are working and still reads perfectly. Every step in the plan runs and
the question is not answered, and the exit code is zero.

Five parts of this day are deliberate failures, and four of them produce **no error at all**. That is
the day's real subject: an executor whose definition of failure is *the step raised* is blind to
almost everything that actually goes wrong with a plan.

Two IDs, and they are the two halves: **AG-17** is writing the list, **AG-18** is what you do when the
world disagrees with it.

---

## §2 The map

Twenty-three parts in six sections, then one paper. Sections 1 to 3 are AG-17 — what a plan *is*, the
two ways to decide one, and walking it. Sections 4 and 5 are AG-18 — how a plan dies, and the second
edition. Section 6 is production, and the day climbs `foundation → working → production`.

### Section 1 — `01-what-a-plan-is`: the artefact, and what having one lets you do

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [A plan is a list, not a paragraph](parts/01-what-a-plan-is/1.1-a-plan-is-a-list-not-a-paragraph.md) | four questions you can ask of data and not of prose | `foundation` |
| 1.2 | [What a step has to carry](parts/01-what-a-plan-is/1.2-what-a-step-has-to-carry.md) | three fields, three readers, and 3 of 6 candidates executable | `foundation` |
| 1.3 | [The plan you can read before it runs](parts/01-what-a-plan-is/1.3-the-plan-you-can-read-before-it-runs.md) | `3/4` scored, and two editions differenced, before anything executes | `working` |

### Section 2 — `02-two-ways-to-decide`: reacting against planning, measured

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [Deciding with your eyes on the last thing you read](parts/02-two-ways-to-decide/2.1-deciding-with-your-eyes-on-the-last-thing.md) | 4/4 on three parts, and a budget of 10 that changes nothing | `working` |
| 2.2 | [Deciding once, from the whole request](parts/02-two-ways-to-decide/2.2-deciding-once-from-the-whole-request.md) | one request instead of four, and the article it cannot name | `working` |
| 2.3 | [💥 The two strategies miss different things](parts/02-two-ways-to-decide/2.3-the-two-strategies-miss-different-things.md) | both 4/6, missing different things — the day's central finding | `production` |
| 2.4 | [What a plan costs in requests](parts/02-two-ways-to-decide/2.4-what-a-plan-costs-in-requests.md) | 20 investigations a day against 5, until the third edition | `working` |

### Section 3 — `03-walking-the-plan`: the executor, by hand and then in ADK

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [The executor is a loop with a list in its hand](parts/03-walking-the-plan/3.1-the-executor-is-a-loop-with-a-list.md) | Day 3's loop with the thinking deleted; 5 steps, 0 decisions | `working` |
| 3.2 | [What a step is allowed to see](parts/03-walking-the-plan/3.2-what-a-step-is-allowed-to-see.md) | a comparison of two tickets it was never handed, reporting `ok` | `working` |
| 3.3 | [A plan that outlives its process](parts/03-walking-the-plan/3.3-a-plan-that-outlives-its-process.md) | 957 bytes of JSON, and a second process finishing the job | `working` |
| 3.4 | [The same executor as an ADK workflow](parts/03-walking-the-plan/3.4-the-same-executor-as-an-adk-workflow.md) | `@node(rerun_on_resume=True)`, `ctx.run_node`, and trap #1 | `working` |

### Section 4 — `04-when-a-plan-dies`: four ways a plan stops being true, two of them silent

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [A shop shut for lunch and a shop closed down](parts/04-when-a-plan-dies/4.1-a-shop-shut-for-lunch-and-a-shop-closed-down.md) | 1 hiccup, 3 contradictions, and the question that separates them | `working` |
| 4.2 | [Retrying a contradiction](parts/04-when-a-plan-dies/4.2-retrying-a-contradiction.md) | the hiccup clears on attempt 2; nine attempts learn nothing | `working` |
| 4.3 | [💥 The step that worked and told you nothing](parts/04-when-a-plan-dies/4.3-the-step-that-worked-and-told-you-nothing.md) | 3/3 succeeded, 1/3 informative, exit 0 | `production` |
| 4.4 | [💥 The plan that outlived the world](parts/04-when-a-plan-dies/4.4-the-plan-that-outlived-the-world.md) | 0 contradictions, 0 replans, 1 reply into a closed ticket | `production` |

### Section 5 — `05-the-second-edition`: replanning, and the brake on it

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [Let the seam out, or re-cut the cloth](parts/05-the-second-edition/5.1-let-the-seam-out-or-recut-the-cloth.md) | patch 2/3 against rewrite 3/3, and who decides | `working` |
| 5.2 | [The work already paid for](parts/05-the-second-edition/5.2-the-work-already-paid-for.md) | 4 steps and 0 repeats against 5 steps and 1 | `working` |
| 5.3 | [The brake, and the sentence it prints](parts/05-the-second-edition/5.3-the-brake-and-the-sentence-it-prints.md) | `MAX_REPLANS = 1`, an escalation, and exit 1 | `production` |
| 5.4 | [💥 Two plans taking turns](parts/05-the-second-edition/5.4-two-plans-taking-turns.md) | 12 editions, 60% of a day's quota, nothing completed | `production` |

### Section 6 — `06-in-production`: the run-level check, the human, and what is not built

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 6.1 | [💥 Every step ran and nothing was answered](parts/06-in-production/6.1-every-step-ran-and-nothing-was-answered.md) | 3/3 and exit 0, turned into `UNANSWERED` and exit 1 | `production` |
| 6.2 | [The plan somebody reads first](parts/06-in-production/6.2-the-plan-somebody-reads-first.md) | reads, writes, irreversible — a card computed from the plan alone | `production` |
| 6.3 | [The step you cannot take back](parts/06-in-production/6.3-the-step-you-cannot-take-back.md) | same three actions, evidence 0 against evidence 2 | `production` |
| 6.4 | [🅿️ Plan repair, hierarchy and search](parts/06-in-production/6.4-plan-repair-hierarchy-and-search.md) | three techniques not built, each with the number that changes it | `production` |

### The paper — read **after** the parts

| # | Paper | What it claimed |
| --- | --- | --- |
| 01 | [Strips: a new approach to the application of theorem proving to problem solving](papers/01-strips.md) | a plan can be searched for mechanically if actions are written as precondition, add list and delete list — `doi:10.1016/0004-3702(71)90010-5` |

**Read it last, and read it after you have written the executor.** That order is Principle 4 at the
scale of a day: you will have spent the day hand-rolling a representation of actions and discovering
by measurement that your steps have no way to say what they depend on, and the 1971 document that
proposed the field's answer is a great deal more interesting when you already know what it is
answering.

---

## §3 Setup — run this

**No package is added today and no pin moves.** `google-adk` stays at `2.7.1`. Everything else in the
day is the Python standard library. `git diff pyproject.toml uv.lock` must be empty when you finish.

```bash
# 1 - the day's lab
cd days/day-56-planning-and-replanning
mkdir -p lab/papers/strips

# 2 - the two shared modules every script imports
touch lab/_world.py lab/_model.py

# 3 - section 1: what a plan is
touch lab/shape.py

# 4 - section 2: the two strategies
touch lab/cover.py lab/price.py

# 5 - section 3: walking the plan
touch lab/walk.py lab/resume.py lab/dynamic.py

# 6 - section 4: how a plan dies
touch lab/classify.py lab/silent.py

# 7 - section 5: the second edition
touch lab/patch.py lab/brake.py

# 8 - section 6: production
touch lab/notgoal.py lab/review.py lab/irreversible.py

# 9 - the day's gate
touch lab/gate.py

# 10 - the paper demo
touch lab/papers/strips/strips.py lab/papers/strips/demo.py
cd -

# 11 - the test file you fill in today (you type every line)
touch tests/test_planning.py

# 12 - confirm the ADK symbols this day uses actually exist
python -c "from google.adk import Context; import inspect; print(inspect.signature(Context.run_node))"
python -c "from google.adk.workflow import node; import inspect; print(inspect.signature(node))"
```

**Steps 11 and 12 are the ones that matter.** Step 12 is Principle 8 in its cheapest form: if either
signature has moved, part 3.4 is wrong and the fix is to check `https://adk.dev/graphs/dynamic/` and
amend the day, not to hunt for a working import.

Every script in `lab/` is run **from inside `lab/`**, because `_world` and `_model` are imported as
top-level modules. From the repository root you get `ModuleNotFoundError: No module named '_world'`.

---

## §4 Build brief

### The project code — `sutra/planning.py`, new today, and you type every line

| Symbol | Shape | What it must do |
| --- | --- | --- |
| `Step` | frozen dataclass | `action` from a closed set, `argument`, `why` (1.1, 1.2) |
| `Plan` | frozen dataclass | `goal` plus an ordered tuple of `Step` (1.1) |
| `MAX_REPLANS` | `int` | the brake, **with a comment naming the run and the date** (5.3) |
| `plan` | `(str) -> Plan` | decide every step from the whole request, once (2.2) |
| `execute` | `(Plan, ...) -> Result` | walk the steps; report `UNANSWERED` when the goal is not met (3.1, 6.1) |
| `classify` | `(str) -> str` | a failure string to `hiccup` or `contradiction` (4.1) |
| `replan` | `(Plan, Step, str, list) -> Plan` | a second edition, carrying the completed work (5.1, 5.2) |
| `answered` | `(str, list[str]) -> bool` | the goal's answer condition against the evidence (6.1) |

- **Irreversible actions are named in the module**, in one set, and the executor puts them last. The
  gate greps for the word (6.3).
- **`MAX_REPLANS` carries its measurement in a comment**, with a date. A bare number fails the gate,
  for the same reason Day 50 refused a bare `TOP_K`.
- **`execute` must be able to say `UNANSWERED`.** A run where every step succeeded and the goal was
  not reached is not a successful run (6.1, Principle 10).

**`TODO(me)` markers left for you:**

- **2.3** — decide which strategy Day 58's *research* stage should use, and write the reason as one
  sentence in the module docstring. Then decide the same for its *intake* stage, and notice that the
  answer is different.
- **2.4** — set `MAX_REPLANS` and write the row of `price.py --replan` it came from beside it,
  including the judgement-step count you assumed for the triage flow.
- **3.2** — the hard one. Decide whether your `Step` gets an `id` and a `needs` list. Four separate
  parts of this day (3.2, 3.3, 5.1, 6.3) all failed for want of that one field. Write down what it
  would cost you and what you would gain, and then decide.
- **4.1** — write `classify`. Then write down the two real-world failures that will fool it, and the
  field you would need from the tool to stop guessing.
- **5.1** — decide whether `replan` patches or rewrites. It may do either; what it may not do is
  decide by preference. Say what it scores and against what.
- **6.1** — write the answer condition for **one** goal type your desk actually handles, and say how
  you would know if its false-alarm rate was too high.
- **6.3** — list every action in `sutra/` that changes something outside the process, and mark the
  ones that are not obviously irreversible but are.
- **6.4** — write the ADR: the median plan length above which you add hierarchy, and the edition
  count above which planning stops being cheaper than reacting. Both numbers are in this day.

### The tests — `tests/test_planning.py`, and you type every line

| Test | What it pins |
| --- | --- |
| `test_a_plan_step_cannot_be_edited_in_place` | `pytest.raises(FrozenInstanceError)` — a second edition is a new object (1.1) |
| `test_a_step_with_an_unknown_action_is_rejected_at_plan_time` | the closed set, checked before execution (1.2) |
| `test_classify_separates_a_rate_limit_from_a_missing_record` | the two kinds, on two real failure strings (4.1) |
| `test_replan_does_not_re_execute_completed_steps` | sunk capital carried forward (5.2) |
| `test_the_brake_escalates_instead_of_replanning_for_ever` | `MAX_REPLANS` reached, non-zero result, nothing invented (5.3) |
| `test_a_run_where_every_step_succeeded_can_still_be_unanswered` | the answer condition, going red (6.1) |

The last one is the one people leave out, and it is the only test in the list that fails on a run
where nothing went wrong.

### The lab — sixteen scripts and a two-file paper demo, none of which calls a model

| File | What it does | Taught in |
| --- | --- | --- |
| `lab/_world.py` | six tickets, four articles, an answer key, and `run_step` with three outcomes | all |
| `lab/_model.py` | two choosers differing in one line: which text they score against | 2.1, 2.2 |
| `lab/shape.py` | prose against data; step validation; coverage; a diff of two editions | 1.1–1.3 |
| `lab/cover.py` | both strategies, three request shapes, one answer key | 2.1–2.3 |
| `lab/price.py` | requests per strategy, and what editions plus judgement steps do to it | 2.4 |
| `lab/walk.py` | the executor, and what each step is handed | 3.1, 3.2 |
| `lab/resume.py` | a run written to JSON, killed, and resumed by a second process | 3.3 |
| `lab/dynamic.py` | the same executor as an ADK dynamic workflow, zero model calls | 3.4 |
| `lab/classify.py` | six failures sorted into two kinds, then retried three times each | 4.1, 4.2 |
| `lab/silent.py` | a step that succeeded and said nothing; a plan the world outran | 4.3, 4.4 |
| `lab/patch.py` | patch against rewrite, scored; and a replan that redoes paid work | 5.1, 5.2 |
| `lab/brake.py` | `MAX_REPLANS`, the escalation sentence, and twelve editions without one | 5.3, 5.4 |
| `lab/notgoal.py` | every step green, the goal unanswered, and the check that says so | 6.1 |
| `lab/review.py` | the approval card, and the trace of the same run | 6.2 |
| `lab/irreversible.py` | the same three actions, reordered, with the evidence count | 6.3 |
| `lab/gate.py` | the day's definition of done, as seven findings | §5 |
| `lab/papers/strips/` | STRIPS in two files, with the delete list as an ablation switch | paper |

---

## §5 The eval that must be able to fail

**The gate** is the day's definition of done, and it is red until `sutra/planning.py` is written:

```bash
uv run python days/day-56-planning-and-replanning/lab/gate.py; echo "exit: $?"
```

Measured on 2026-09-05, before anything was written: `1-7: sutra.planning is not importable: No
module named 'sutra.planning'`, `findings: 1`, `exit: 1`.

When it prints `findings: 0` and `exit: 0`, seven statements are true: the eight symbols exist,
`MAX_REPLANS` carries a dated comment naming its measurement, `classify` returns different kinds for
a 429 and a missing id, `answered` is callable, the module mentions irreversible steps, `execute`
can report `UNANSWERED`, and the brake is not set above three. Then break exactly one on purpose —
delete the date from the comment beside `MAX_REPLANS` — and watch finding 2 appear.

**Two run-level checks with exit codes**, both of which go red on a run where nothing failed:

```bash
cd days/day-56-planning-and-replanning/lab
uv run python notgoal.py --check; echo "exit: $?"     # UNANSWERED, exit 1
uv run python brake.py; echo "exit: $?"                # ESCALATE, exit 1
cd -
```

**The paper's ablation**, which is an eval in its own right:

```bash
cd days/day-56-planning-and-replanning/lab/papers/strips
uv run python demo.py; echo "exit: $?"              # consistent, exit 0
uv run python demo.py --no-delete; echo "exit: $?"  # INCONSISTENT, exit 1
cd -
```

**The test suite**, offline and red as shipped, because `tests/test_planning.py` is empty until you
write it:

```bash
uv run python -m pytest tests/test_planning.py -q -m "not live"
```

**And every measurement in the day, re-runnable:**

```bash
cd days/day-56-planning-and-replanning/lab
uv run python shape.py; uv run python shape.py --validate
uv run python shape.py --score; uv run python shape.py --diff
uv run python cover.py; uv run python cover.py --reactive
uv run python cover.py --shapes; uv run python cover.py --reactive --shapes --budget 10
uv run python price.py; uv run python price.py --replan
uv run python walk.py; uv run python walk.py --carry
uv run python resume.py --clean; uv run python resume.py --start; uv run python resume.py --resume
uv run python dynamic.py
uv run python classify.py; uv run python classify.py --retry
uv run python silent.py --useless; uv run python silent.py --stale
uv run python patch.py; uv run python patch.py --sunk
uv run python brake.py; uv run python brake.py --max 0; uv run python brake.py --oscillate
uv run python notgoal.py; uv run python notgoal.py --check
uv run python review.py; uv run python review.py --trace
uv run python irreversible.py; uv run python irreversible.py --ordered
cd -
```

`brake.py`, `notgoal.py --check` and `demo.py --no-delete` **exit non-zero on purpose**. Those are
findings, not broken scripts.

---

## §6 Request budget

**Free-tier Gemini**, 20 generate requests per day per model (read off a live 429 on Day 2, recorded
in `docs/PACKAGES.md`).

| What | Generations |
| --- | --- |
| every part in every section | **0** |
| all sixteen lab scripts, every flag | **0** |
| the STRIPS demo, both arms | **0** |
| `sutra/planning.py`, the gate and the six tests | **0** |
| **Total planned** | **0 of 20** |

**Zero, and the zero is load-bearing rather than frugal.** Both choosers in `_model.py` are scoring
functions, every node in `dynamic.py` is a plain Python function, and the STRIPS planner is a
breadth-first search over frozensets. That is what lets this day's central claim — two strategies,
same score, different misses — be a *measurement* you can re-run on every change rather than a
sampling result that moves when you look at it again.

Part 2.4 is the day where quota is the subject rather than the budget: **one planning request against
one per step**, which on this free tier is twenty investigations a day against five, until the third
edition turns the arithmetic round.

**Cost: $0.**

---

## §7 Traps

- **A plan written as prose cannot be counted, scored, differenced or gated** — and the parser
  somebody writes for the numbered markdown list breaks the day the model writes `1)` instead of
  `1.` (1.1).
- **Field validation only checks fields.** `compare(4521)` has a legal action, a non-empty argument
  and a reason, and it runs, and it compares one thing against nothing (1.2).
- **A requirement set can be empty**, and then a plan that does nothing scores `0/0` with
  `misses: none` (1.3).
- **Raising a reactive loop's turn budget does not improve its coverage.** It stopped at four steps
  with ten available, because nothing left resembled what it had just read (2.1).
- **A planner can only reach what the request's own words can reach.** It read every ticket named and
  missed the article with the fix, because the request said "the article with the fix" (2.2).
- **Two strategies scoring 4/6 missed entirely different things**, and only one of them skipped a
  ticket the request named. Never report the fraction without the list (2.3).
- **Planning stops being cheaper at the third edition** once any step needs its own model call —
  five requests against reacting's four (2.4).
- **An ordered list is not a dependency graph.** A comparison step ran with zero earlier results and
  reported `ok` (3.1, 3.2).
- **A checkpoint with no `status` cannot tell a resume from a re-run**, and resuming a finished run
  reports `cursor at step 5 of 4` and exits zero (3.3).
- **Trap #1 (plan §5.1):** in 2.x a node is a unit of work and an agent is one kind of node. A
  dynamic workflow full of plain functions costs zero generations (3.4).
- **An ADK node name must be a valid Python identifier** — `step-1` raises a `ValidationError` — while
  a custom `run_id` must contain a non-numeric character. Two rules pointing opposite ways (3.4).
- **`parameter_binding="node_input"` binds by name from the dict**, so the child's parameters are the
  dict's keys and not a parameter called `node_input` (3.4).
- **`rerun_on_resume=True` re-runs the orchestrator body from the top**, so anything with an effect
  in that body happens again on every resume (3.4).
- **One failure in six was a hiccup and three were contradictions.** "Retry everything" is wrong
  three times out of four (4.1).
- **A retried contradiction returns byte-identical results.** Nine attempts, six wasted requests,
  nothing learned (4.2).
- **A permission error and an outage both look like "does not exist"**, and the agent then confidently
  reports that a real ticket is missing (4.1).
- **A step can succeed and tell you nothing.** 3/3 succeeded, 1/3 informative, exit 0 (4.3).
- **A closed ticket still reads**, so a plan the world moved under produces zero contradictions and
  sends a reply nobody will see (4.4).
- **A patch can only remove.** When the dead step was the only route to part of the goal, the patched
  plan runs cleanly and cannot succeed — 2/3 against the rewrite's 3/3 (5.1).
- **A replanner not told what is already done buys it again**, and on a step that sends something
  that is a customer answered twice (5.2).
- **Raising `MAX_REPLANS` to make escalations stop makes planning the expensive strategy**, and
  nothing announces it (5.3).
- **Every edition of an oscillation is individually correct.** Twelve editions, no error anywhere,
  60% of a day's free tier (5.4).
- **Nothing in this day catches a run where every step succeeded and the goal was not reached**
  except a condition written down before the plan existed (6.1).
- **A review card computing "reads" as "everything that is not a reply" will tell an approver that a
  plan which closes a ticket only reads things** (6.2).
- **Every recovery mechanism here assumes the step can be run again.** Ordering the irreversible step
  last is the cheapest fix and it makes the step late, not correct (6.3).

---

## §8 Verify before you code

Read or fetched on **2026-09-05**, the day this was written.

- **`https://adk.dev/graphs/dynamic/`** — the dynamic workflow page. Source for: `@node` on an async
  orchestrator; `rerun_on_resume=True` being required for any orchestrator that calls `ctx.run_node`,
  with the body re-running from the top and completed children skipped; `ctx.run_node` returning
  normally when a child interrupts; the rule that a custom `run_id` must contain at least one
  non-numeric character; and the page's own division of labour between graphs and dynamic workflows.
- **The installed package**, `google-adk==2.7.1`, introspected rather than remembered:

```bash
python -c "from google.adk.workflow import node; import inspect; print(inspect.signature(node))"
python -c "from google.adk import Context; import inspect; print(inspect.signature(Context.run_node))"
python -c "from google.adk import Context; print([m for m in dir(Context) if not m.startswith('_')])"
```

  The first two produced the signatures quoted in part 3.4, including `parameter_binding`, `timeout`
  and `retry_config`. The third confirmed `run_node` is on `Context` and that `Context` is **not** in
  `google.adk.workflow` — the natural guess, and a real `ImportError`.

- **`https://api.crossref.org/works/10.1016/0004-3702(71)90010-5`** — the registration record for
  today's paper, which is where the title, journal, volume, pages and year in
  [`papers/01-strips.md`](papers/01-strips.md) are copied from. The DOI itself redirects to a
  publisher host that returns no readable body, so the registration record is the source and the
  paper part says so. Row added to `docs/PAPERS.md`, dated.
- **`arXiv:2210.03629`, *ReAct: Synergizing Reasoning and Acting in Language Models*, 2022** — already
  in `docs/PAPERS.md`, taught on Day 3 at
  [`papers/01-react.md`](../day-03-loop-hand-rolled/papers/01-react.md). Cited as an address by part
  2.1; not re-taught.

**Two discrepancies worth recording rather than smoothing over.** Plan §5 names `google-adk` **2.6.3**
as the baseline and this repository pins **2.7.1**; a patch ahead of the plan's baseline is what
Principle 7 expects, and it is recorded in `docs/PACKAGES.md`, but the day states it rather than
letting a reader discover it. And the Crossref record capitalises the paper's acronym as `Strips`
while the paper and the literature write `STRIPS` — the citation uses the record's form and the prose
uses the conventional one, on purpose.

**What no documentation says**, and therefore had to be measured: everything in section 2. There is
no page anywhere that will tell you whether planning or reacting covers your requests better,
because the answer depends on whether your requests name what they need. That is why the answer key
exists and why both strategies are run over the same one.

---

## §9 Say it in an interview

*"Day 56 was the day my agent stopped deciding one step at a time and wrote the list down first — and
the interesting part was that the measurement did not say what I expected.*

*I built both strategies as the same code differing in one line: which text the chooser scores its
options against. Reactive scores against the last observation; planning scores against the whole
request, once. Then I ran both over the same requests with an answer key I wrote first. On a
four-part request they both scored four out of six, and they missed completely different things.
Planning read every ticket the request named and reached neither knowledge base article, because the
request said 'the article with the fix' and that phrase has no words in common with the article.
Reacting found the article — it picked up the vocabulary from reading a ticket — and never reached a
ticket the request named outright, because by then it was following a different thread. So planning
fails by omitting what you did not say, and reacting fails by omitting what you did. An identical
coverage number for both is exactly the thing that would have made me ship the wrong one.*

*The cost side is clearer. Planning is one model call whatever the request contains; reacting is one
per step. On a twenty-request daily free tier that is twenty investigations a day against five. But
that only holds while the plan works first time — I priced it as the edition count grows, and at
three editions with two judgement steps in the plan, planning costs five requests against reacting's
four. So my replan cap of one is a cost control, not a safety feature, and the comment beside the
constant says which row of the table it came from.*

*The half I would actually lead with is that four of my five deliberate failures produce no error at
all. A step succeeded and returned a real knowledge base article about the wrong subject — three of
three green, one of three informative. A ticket was merged and closed between planning and execution,
and because a closed ticket still reads, the run finished with zero contradictions, zero replans and
a reply sent to a ticket nobody was watching. And the worst one: every step succeeded and the goal
was never answered, exit code zero, evidence about invoices in answer to a question about sign-in.
Retry needs a failure, replan needs a contradiction, and my pre-execution coverage check only asks
whether the plan touched the required things — this plan touched things, they were the wrong things.
The only thing that caught it was an answer condition written down with the goal before the plan
existed, and when it fires the run says UNANSWERED and exits one rather than summarising three
successful steps. That is the part that is hard to ship, because an honest 'I could not determine
this' scores worse on every metric than a confident wrong answer.*

*One more, on containment. I turned the replan cap off and watched two plan editions take turns for
twelve rounds — each one a correct response to the failure it was shown, because the replanner only
sees the last failure. Twelve planning requests, sixty per cent of the day's quota, nothing
completed, and no error anywhere. The cap does not make the plan correct. It makes the failure finite
and makes the system say so.*

*And the thing four different parts of the day kept asking for was one missing field. My steps have
an order and no dependencies, so a comparison ran with zero earlier results and reported success, I
could not parallelise, I could not safely resume in the middle, and my patch had to guess which steps
died with the failure by matching on strings. Step ids and an explicit inputs list would have fixed
all four. Reading the 1971 STRIPS paper afterwards was slightly humbling, because preconditions and
delete lists are precisely that field, and the demo makes it concrete: with delete lists the planner
finds a correct four-step plan, and with them switched off it finds a four-step plan of the same
length that the validator refuses, because it thinks it can merge a duplicate into a ticket it has
already closed."*

---

## §10 Done when

See [`CHECKLIST.md`](CHECKLIST.md). Every box is ticked because you ran the thing, not because you
read about it. `./m done 56` refuses to commit until they are.

---

## §11 Ledger & commit

**`docs/PROGRESS.md` — append this row** (fill in the hash after committing):

```markdown
| 56 | 2026-09-05 | AG-17, AG-18 | 23 (+1 paper) | <hash> | ⚠️ |
```

**`docs/PACKAGES.md` — no new rows today.** No package is added, no pin moves, and nothing is
installed. `google-adk` stays at `2.7.1`.

**`docs/PAPERS.md` — one new row, already appended:**

```markdown
| Strips: A new approach to the application of theorem proving to problem solving | doi:10.1016/0004-3702(71)90010-5 | 1971 | 2026-09-05 | 56 | `days/day-56-planning-and-replanning/papers/01-strips.md` |
```

*ReAct* (`arXiv:2210.03629`, 2022) already has its row from Day 3 and is cited as an address by part
2.1 rather than re-taught.

**`docs/SKILL_PROVENANCE.md` — no new rows today.**

**Git commit message:**

```
day 56: plan-and-execute and replanning — closes AG-17, AG-18
```
