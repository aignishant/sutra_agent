---
day: 58
phase: 8
phase_name: "Workflows and multi-agent"
title: "The triage graph v1 — intake→classify→research→draft→review, end to end"
ids: ["ADK-41", "ADK-42"]
principles: [1, 2, 4, 7, 8, 10, 11, 13, 15, 16, 17, 18]
kind: capstone
plan_version: "v2.2.1"
parts: 24
generated: "2026-09-05"
status: written
lab_scaffolded: true
commit: ""
---

# Day 58 — The triage graph v1, end to end

> **Yesterday (Day 57):** multi-agent design. The orchestrator pattern, and a Writer↔Critic loop with
> a rubric it can actually fail against — the component this day gives a seat on the floor.
> **Today:** assembly. Five stages — intake, classify, research, draft, review — wired into one graph
> that takes a ticket reference at one end and produces a reviewed reply at the other. Ten stations,
> two of which would call a model, six declared seams, four lanes, and **zero requests spent**
> measuring all of it.
> **Tomorrow (Day 59):** the Phase 8 gate and the failure lab — loops, runaway agents and
> containment. Today builds the thing tomorrow breaks on purpose.

---

## §1 Where we are

Phase 7 gave the desk a memory it can search. Phase 8 has spent five days on the pieces of a process:
nodes and edges, sequence and parallelism and loops, delegation, planning, a writer and a critic.
Today they stop being pieces.

Think about the accident and emergency department of a large hospital on a busy evening. The room is
full of people — someone taking your name at the door, a nurse with a blood pressure cuff, a clerk
finding your old file, a porter, a technician running the sample, somebody filing the result. And one
doctor.

Almost nobody in that room is a doctor, and that is the design rather than a shortage. The scarce
thing is one person's judgement, so every job that does not need judgement has been moved to somebody
who is not the doctor. The room works because of that ratio, not in spite of it.

This floor has ten stations and **two of them would call a model**. The mouth looks up a reference.
Two clerks search — one by meaning over the ticket archive, one by words over the knowledge base —
and neither spends a request, because retrieval is arithmetic. A join waits. An adapter declares a
type. A stamp extracts citations. Eight stations, zero requests, and every one of them is a station
somebody might have reached for a model to write.

That ratio is what makes the day's arithmetic survivable. The pinned model has a free allowance of
twenty requests **per day**. A ticket that gets a reply costs three, or five if the critic sends the
draft back once. Measured across the whole fifty-two ticket archive the mean is 2.08, which is 9.6
tickets a day. Get the ratio wrong and it is four.

The day ends where an honest assembly day has to end: with what the finished floor gets wrong. It
answers a ticket that does not exist when one check is removed. It sends a reply the critic approved
and nobody can act on. And it escalates 54% of the archive to a human — a lane designed as the
exception, quietly become the process.

## §2 The map

Eight sections, in build order. Section 1 is **the shape of the thing** — the ratio, the seams, and
the one station allowed to decide what is real. Sections 2 to 4 are **the stages themselves**, one
section each for the guess, the research floor and the drafting box. Section 5 is **the wiring**.
Sections 6 and 7 are ADK-42: **the run as an accountable fact**, and what it means to accept one.
Section 8 is the production face, and it is where the measurements stop being flattering.

### Section 1 — the floor (ADK-41)

*What assembly actually is: a ratio, a set of declared seams, and one station that decides what is real.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [Ten stations, two of which think](parts/01-the-floor/1.1-ten-stations-two-of-which-think.md) | How many stages need a model, and what does the answer cost? | foundation |
| 1.2 | [The baton has a declared shape](parts/01-the-floor/1.2-the-baton-has-a-declared-shape.md) | What travels between two stations, and who enforces it? | working |
| 1.3 | [One station decides what is real](parts/01-the-floor/1.3-one-station-decides-what-is-real.md) | Where does validation belong, and why is a miss a route? | working |

### Section 2 — the guess and the honest exit (ADK-41)

*The one station allowed to guess, the form it must fill, and the lane where the machine declines.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [A verdict is a form, not a paragraph](parts/02-the-guess/2.1-a-verdict-is-a-form.md) | Why is the classifier's output a schema? | working |
| 2.2 | [The route is an action, not the answer](parts/02-the-guess/2.2-the-route-is-an-action.md) | How does a station say where the run goes next? | working |
| 2.3 | [The one model call, pinned and refused](parts/02-the-guess/2.3-the-one-model-call.md) | Which model, constrained how, and what happens on a 429? | working |
| 2.4 | [The lane that declines the work](parts/02-the-guess/2.4-the-lane-that-declines-the-work.md) | Why is escalation checked before anything expensive? | working |

### Section 3 — the research floor (ADK-41)

*Two retrievers, a fan-in, and what a lane actually costs.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [Two clerks who disagree about "similar"](parts/03-the-research-floor/3.1-two-clerks-who-disagree.md) | Why two different searches, and how often does each find anything? | working |
| 3.2 | [The join hands over a dict keyed by node name](parts/03-the-research-floor/3.2-the-join-hands-over-a-dict.md) | What does a `JoinNode` give its successor? | working |
| 3.3 | [What a lane costs](parts/03-the-research-floor/3.3-what-a-lane-costs.md) | What is the unit of cost in a pipeline? | production |

### Section 4 — the box (ADK-41)

*The writer-critic loop as one node, its brake, and the stamp at the end of the floor.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [The newsroom drops in as one node](parts/04-the-box/4.1-the-newsroom-drops-in-as-one-node.md) | How does a whole workflow become a station? | working |
| 4.2 | [The brake belongs to the critic](parts/04-the-box/4.2-the-brake-belongs-to-the-critic.md) | Who counts the rounds, and what ships when they run out? | working |
| 4.3 | [The stamp that may not change the answer](parts/04-the-box/4.3-the-stamp-that-may-not-change-the-answer.md) | Why must the last station be pure? | working |

### Section 5 — the graph (ADK-41)

*The wiring itself, and the two channels a station reads from.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [The edge list is the floor plan](parts/05-the-graph/5.1-the-edge-list-is-the-floor-plan.md) | What does composition-as-data buy you? | working |
| 5.2 | [On the edge or in the register](parts/05-the-graph/5.2-on-the-edge-or-in-the-register.md) | Where does a station's information come from? | working |

### Section 6 — the run as a fact (ADK-42)

*A run is finished when you can account for it — and two of these parts are what happens when you cannot.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 6.1 | [The event stream is the story](parts/06-the-run/6.1-the-event-stream-is-the-story.md) | How do you read a run you did not watch? | working |
| 6.2 | [State is the case file](parts/06-the-run/6.2-state-is-the-case-file.md) | What can you ask about a run after it ends? | working |
| 6.3 | [A reply to a ticket that does not exist](parts/06-the-run/6.3-a-reply-to-a-ticket-that-does-not-exist.md) | 💥 What does a pipeline do to bad input? | production |
| 6.4 | [The seam that drifted](parts/06-the-run/6.4-the-seam-that-drifted.md) | 💥 Where does a failure surface, and what does swallowing it cost? | production |

### Section 7 — acceptance (ADK-42)

*Node tests prove stations. A pipeline needs statements about whole runs.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 7.1 | [Every part passed, the thing does not fit](parts/07-acceptance/7.1-every-part-passed.md) | What can a run-level invariant see that a unit test cannot? | production |
| 7.2 | [The gate that goes red](parts/07-acceptance/7.2-the-gate-that-goes-red.md) | Why is the eval written before the code? | production |

### Section 8 — in production

*Three measurements that are not flattering, and the ones that matter most.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 8.1 | [The green run that helped nobody](parts/08-in-production/8.1-the-green-run-that-helped-nobody.md) | 💥 How does a retrieval miss lower the reviewer's standard? | production |
| 8.2 | [A gate that fires on half the traffic](parts/08-in-production/8.2-a-gate-that-fires-on-half-the-traffic.md) | 💥 What happens to a control whose rate is 54%? | production |
| 8.3 | [Thirty nodes, a queue and a timeout](parts/08-in-production/8.3-thirty-nodes-a-queue-and-a-timeout.md) | What changes when the floor is fed by a queue? | production |

There is no `papers/` directory today. This is a build day: it composes ideas taught earlier, and the
three papers it leans on — ReAct (Day 3), the end-to-end arguments (Day 21) and RAG (Day 49) — are
cited and linked from the parts that use them rather than re-taught.

## §3 Setup — run this

```bash
mkdir -p days/day-58-triage-graph-v1/lab
cd days/day-58-triage-graph-v1/lab
cp ../../day-50-chunking-and-top-k/lab/_archive.py .
cp ../../day-50-chunking-and-top-k/lab/_index.py .
touch _stations.py _drive.py ratio.py batons.py mouth.py seam.py escalate.py clerks.py \
      join.py price.py box.py brake.py stamp.py model.py shape.py register.py \
      stream.py casefile.py launder.py drift.py swallow.py invariants.py scale.py gate.py
```

`_archive.py` and `_index.py` are copied from Day 50 rather than imported, for the reason Day 50 gave
when it copied them from Day 49: a number printed in a part must be reproducible from a fresh
checkout, whether or not `sutra/retrieval.py` has been typed yet.

**No package is added today.** `google-adk==2.7.1` was pinned on Day 5 and `docs/PACKAGES.md` has its
dated row. Confirm what you are actually running before you start:

```bash
uv run python -c "import google.adk; print(google.adk.__version__)"
uv run python -c "from google.adk.workflow import Workflow, node, JoinNode, START, RetryConfig; print('ok')"
uv run python -c "from google.adk.agents.llm_agent import LlmAgent; print(LlmAgent._default_model)"
```

Run on 2026-09-05 those printed `2.7.1`, `ok`, and `gemini-3.5-flash` — the last one being the model
you get if you forget to pin, which is **not** this project's pin (§7, trap 2).

`git diff pyproject.toml uv.lock` must be empty today and stay empty.

## §4 Build brief

Three modules and a test file. The lab has a working copy of all of it; the point of typing it into
`sutra/` is that the graph becomes the product rather than a demonstration.

```python
# sutra/triage.py
"""The stations and the batons. Six declared seams, ten stations, no wiring."""


class TicketText(BaseModel):
    """What intake produces: a ref that is known to exist, and its text."""

    # TODO(me): ref, text.


# TODO(me): TriageResult, EvidenceBlock, ReviewedDraft, FinalReply - the other four batons.
#           TriageResult carries the range guard; see part 2.1.


def intake(node_input: str) -> Event:
    """Station 1: turn a request into a fact, or route on the fact that it is not one."""
    # TODO(me): normalise, then check existence, then route NO_SUCH_TICKET or FOUND.
    #           Two separate functions - part 1.3 says why.
    ...
```

```python
# sutra/graph.py  (extends Day 53's file)


def build_triage_graph_v1() -> Workflow:
    """The floor: six edge entries, ten stations, three terminal nodes."""
    # TODO(me): START -> intake; intake routes; classify routes, one of them fanning
    #           out to both clerks; both clerks -> the join; then the chain to finalize.
    ...
```

```python
# sutra/acceptance.py
"""Run-level invariants. Each one is a sentence from a part, quantified over the corpus."""


def escalated_runs_produce_no_draft() -> bool:
    """No run that took the escalation lane left a draft behind."""
    # TODO(me): drive every ticket, check state.
    ...


# TODO(me): replies_cite_something(), run_stays_in_budget(limit). Part 7.1 has the shapes.
```

**What each piece is for:**

- `sutra/triage.py` holds the batons **and** the stations, so that "what does this pipeline pass
  around" is answered by opening one file (part 1.2's production note).
- `build_triage_graph_v1()` is a function so a validation error surfaces at the call site rather than
  at import, and so every test gets a fresh graph (part 5.1).
- `sutra/acceptance.py` is separate from the tests on purpose: the same functions are called by
  `tests/` today and by Day 59's phase gate tomorrow.
- Then `tests/test_triage_graph.py`: the graph builds, the five stages are present, a miss routes
  `NO_SUCH_TICKET`, an escalated run has no draft, a handled run reaches `finalize`, and **one test
  you break on purpose and watch go red**.

The `TODO(me)` markers stay unsolved. The lab is the reference; typing it is the exercise.

## §5 The eval that must be able to fail

```bash
uv run python days/day-58-triage-graph-v1/lab/gate.py; echo "exit: $?"
```

Run it **now, before writing anything.** Measured on 2026-09-05:

```text
  FAIL  import                                 ModuleNotFoundError: No module named 'sutra.triage'
  FAIL  batons                                 ModuleNotFoundError: No module named 'sutra.triage'
  FAIL  builds                                 ModuleNotFoundError: No module named 'sutra.graph'
  FAIL  mouth                                  ModuleNotFoundError: No module named 'sutra.triage'
  FAIL  escalation writes nothing              ModuleNotFoundError: No module named 'sutra.acceptance'
  FAIL  citation invariant                     ModuleNotFoundError: No module named 'sutra.acceptance'
  FAIL  budget                                 ModuleNotFoundError: No module named 'sutra.acceptance'

  0/7 checks pass
exit: 1
```

Seven checks, seven failures, exit 1. Each is a sentence from a part turned into something a machine
can refuse, and the failure list is a better build specification than §4 is, because it cannot
describe anything it will not later verify.

One warning about the fifth check. When the build brief is done, `citation invariant` will go from
red to **red** — failing for a real reason rather than a missing import, because four of twenty-four
replies cite a source (part 7.1). That is the gate working, not the gate broken. Fixing it is a
retrieval problem, and the tempting alternative is to weaken the check.

## §6 Request budget

| Provider | Requests today |
| --- | --- |
| Gemini (`GOOGLE_API_KEY`) | **0** |
| Groq | **0** |
| OpenRouter | **0** |
| Ollama | **0** |

Zero, and the zero is load-bearing rather than incidental. The two stations that would call a model —
`classify` and the writer-critic loop — are deterministic stand-ins whose call is **counted** by a
meter instead of made. That is what lets this day drive all fifty-two tickets through the graph
repeatedly and quote real numbers for every lane.

The arithmetic those counts produce is what matters for tomorrow:

| Lane | Stations | Requests |
| --- | --- | --- |
| not found | 2 | 0 |
| escalated | 3 | 1 |
| replied, no revision | 10 | 3 |
| replied, one revision | 12 | 5 |

Across the archive: **108 requests for 52 tickets, a mean of 2.08**, against a free tier of twenty a
day. That is 9.6 tickets. Budget with the worst lane, not the mean — part 3.3 shows why the mean
puts you out of quota by lunchtime.

## §7 Traps

1. **Trap #1 — the node model** (plan §5.1). Composition is a list of edges, not a nesting. Two edges
   into one `JoinNode` is the thing a tree cannot express, and it is the whole research floor (5.1).
2. **The framework default model is not your pin.** `LlmAgent._default_model` on 2.7.1 is
   `gemini-3.5-flash`; this repo pins `gemini-3.7-flash`. Leave `model=` off and you run on a model
   whose free-tier allowance you never measured (2.3, **ADK-73**).
3. **Trap #3 — yield, don't append.** A station that buffers its events emits nothing until it
   finishes, so a run killed inside it leaves no record it was ever there (6.1).
4. **Trap #4 — don't swallow exceptions.** A station that catches an error and returns a friendly
   string has *succeeded*: no retry fires, the span is green, the error rate stays zero, and the
   apology becomes the body of the reply (6.4).
5. **A misspelled `Event` keyword is silently dropped.** `Event` ignores unknown fields, so
   `rout="ESCALATE"` sets no route, no edge matches, and the branch ends with exit code 0 (2.2).
6. **A `JoinNode` waits for completion, not for a value.** A branch that finishes without an output
   leaves the join with a hole, and the failure surfaces downstream of the station that caused it
   (3.2, 8.3).
7. **State-bound parameters have defaults, so a missing key looks like an empty value.** A clerk
   whose `ticket_text` was never written searches for nothing and reports success (5.2).
8. **A rubric guarded on the evidence gets easier as retrieval gets worse.** The critic requires a
   citation only when an article was found, so a retrieval miss is an implicit pass (8.1).

## §8 Verify before you code

Fetched on **2026-09-05**, and every API claim in this day is checked against them plus the installed
`google-adk==2.7.1`:

- <https://adk.dev/graphs/> — `Workflow`, edges as tuples and chains, nodes, nested workflows
- <https://adk.dev/graphs/data-handling/> — `node_input`, `output`, `ctx.state`, and `input_schema` /
  `output_schema`, which the page says *"makes the contract explicit and validates it at runtime"*
- <https://adk.dev/graphs/routes/> — `JoinNode` as the fan-in barrier keyed by predecessor node name;
  *"a predecessor that finishes without an output leaves the join with no value for that branch, and
  the resulting failure appears downstream, away from the node that caused it"*; *"attach a retry
  configuration to any node that can fail"*; and *"a graph cycle is not bounded automatically"*

Every symbol was also introspected against the installed package rather than taken from the page —
`RetryConfig`'s fields, `NodeTimeoutError`, `LlmAgent._default_model`, and the fact that `Event` is
configured with `extra="ignore"` were all read from 2.7.1 directly, and two of them are traps above.

One discrepancy worth recording rather than hiding: the plan's §5 baseline names `google-adk` 2.6.3
and the repo pins 2.7.1. A patch ahead of the baseline is what Principle 7 expects, so no amendment
is needed, but this day states the version it actually checked.

## §9 Say it in an interview

*"The system is a support-triage pipeline: intake, classify, research, draft, review, as a graph
rather than an agent tree. The number I lead with is that ten stations do the work and two of them
call a model — the classifier and a writer-critic loop — because everything else is a lookup, vector
arithmetic or string handling. That ratio is why it runs on a free tier at all: a ticket costs three
model calls, five if the critic sends the draft back, and a ticket we decline costs one, because the
escalation check runs before anything expensive. Across our fifty-two ticket archive that is 2.08 on
average against a twenty-a-day allowance.*

*Structurally the two things I would defend are the seams and the mouth. Every edge carries a
declared Pydantic type, so a station that stops honouring its contract fails at the seam with the
node name, the missing field and the payload that arrived — before the receiving node's body runs.
And exactly one station decides what is real, so everything downstream is entitled to trust its
input. I turned that check off once to see what it costs: the floor produced a reviewed,
critic-approved reply about a ticket that does not exist, quoting a real customer's ticket back at
the requester, for three model calls and exit code zero.*

*What I would want to talk about is what the run-level checks found, because none of it was
detectable from unit tests. All five node tests pass, and four of twenty-four replies cite a source —
our keyword retriever misses the knowledge-base article for the very ticket it was written about, and
the critic only requires a citation when retrieval found one, so a retrieval miss silently lowers the
bar instead of raising an alarm. And the escalation lane, which I designed as the exception, takes
54% of traffic, twenty-six of twenty-eight because the classifier did not recognise the ticket rather
than because it needs a human. Both of those are properties of the assembly. No station is at fault
for either."*

## §10 Done when

See [`CHECKLIST.md`](CHECKLIST.md). The day is done when every box is ticked, `gate.py` exits 0, and
`./m depth 58` is green — not when you have read to the bottom of this page.

## §11 Ledger & commit

`docs/PROGRESS.md` — append:

```text
| 58 | 2026-09-05 | ADK-41, ADK-42 | 24 | <hash> | ⚠️ |
```

`docs/PACKAGES.md` — **no new row.** `google-adk==2.7.1` was pinned on Day 5 and re-verified today
with `uv run python -c "import google.adk; print(google.adk.__version__)"`. The `gemini-3.7-flash`
row from Day 2 is unchanged and no model was called.

`docs/PAPERS.md` — **no new row.** Today teaches no paper. It cites three already in the ledger —
`arXiv:2210.03629` (Day 3), `doi:10.1145/357401.357402` (Day 21) and `arXiv:2005.11401` (Day 49) —
and links the parts that teach them.

`docs/SKILL_PROVENANCE.md` — no row. No third-party skill was used today.

Commit:

```text
day 58: the triage graph v1 end to end - closes ADK-41, ADK-42
```
