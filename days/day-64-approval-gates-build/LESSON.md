---
day: 64
phase: 9
phase_name: "Durability and humans"
title: "Approval gates — build; HITL resumption for standalone nodes & NodeTool"
ids: ["ADK-48", "ADK-76"]
principles: [1, 2, 4, 7, 8, 10, 11, 13, 15, 16, 17, 18]
kind: lab
plan_version: "v2.2.1"
parts: 25
generated: "2026-09-06"
status: written
lab_scaffolded: true
commit: ""
---

# Day 64 — Approval gates: build

> **Yesterday (Day 63):** the design. Which actions need a human, judged by blast radius and
> reversibility, and the argument that a gate firing on everything is the same as no gate at all. It
> ended with a policy table and nothing that could act on it.
> **Today:** the table becomes code, and the desk grows a sixth station. Two gate mechanisms — one on
> a tool, one on a graph node — the machinery that binds an answer to the call it answers, and the
> eval that goes red when any of it is removed. Zero model calls; every number here came from a run.
> **Tomorrow (Day 65):** the Phase 9 gate. The triage graph gets killed mid-run at four different
> moments, and has to come back and finish with a human's approval still honoured.

---

## §1 Where we are

Phase 9 has been building the ability to stop. Day 60 separated the run from the process and made a
half-finished run something you can pick up again. Day 61 wrote down what a checkpoint contains.
Day 62 laid out the four shapes a human can occupy in a loop. Day 63 decided which of the desk's
actions are worth stopping for.

None of that has stopped anything yet. The triage graph still ends at a drafted reply, because Day 58
had nowhere safe to put the send.

Think of the tailor's final fitting. He measures, he cuts, he stitches — and then, before the shirt
goes in the bag, you put it on and stand in front of the mirror. For a plain shirt he barely looks up
and it costs nobody anything. For the one you are having made for a wedding, he walks around you,
pins the side, and says come back once more. The fitting is not a separate shop. It is one step in
the same sequence, in the same room, and its position is what makes it work: after the work is done,
and before the thing leaves.

Today adds that step. The desk gets a gate between the drafted reply and the send, and most tickets
walk straight through it without disturbing anybody. The ones that move money or leave the building
stop, a person is asked, and the run ends — properly ends, no process held open — until somebody
answers.

The day spends most of its length on the ways that go wrong, because almost all of them are quiet. A
graph can pause, ask a real person, receive a real rejection, record it faithfully in an audit trail,
and send the email anyway. Every dashboard stays green. Only a check that asks whether the *effect*
happened can tell the difference, and building that check is where the day ends.

---

## §2 The map

Seven sections. Section 1 turns Day 63's table into a decision function. Sections 2 and 4 are the two
places a gate can live — on a tool, and inside a graph — and section 3 is the machinery between them
that makes an answer trustworthy. Section 5 is the audit trail, which turns out to be something you
read rather than write. Section 6 wires it into the desk and tests it. Section 7 is what the gate
costs once real people are behind it.

### 1 · The policy is data

*Turning "which actions need a human" into something a program can ask and a person can review.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [A gate is a decision about one action](parts/01-the-policy-is-data/1.1-a-gate-is-a-decision-about-one-action.md) | Is the gate about the agent, the tool, or the call? | foundation |
| 1.2 | [The policy is a file, not a habit](parts/01-the-policy-is-data/1.2-the-policy-is-a-file-not-a-habit.md) | Why the list of gated actions is data with a reason on every row | working |
| 1.3 | [The arguments decide, not the tool](parts/01-the-policy-is-data/1.3-the-arguments-decide-not-the-tool.md) | Why a tool-level gate is wrong for 20 of 24 real calls | working |
| 1.4 | [The guard that was only added in three places](parts/01-the-policy-is-data/1.4-the-guard-that-was-only-added-in-three-places.md) | What happens when the check lives at the call sites | production |

### 2 · The tool gate

*ADK's own mechanism: one argument on a `FunctionTool`, and what comes back when it fires.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [One argument turns a tool into a gate](parts/02-the-tool-gate/2.1-one-argument-turns-a-tool-into-a-gate.md) | How `require_confirmation` stops the body running | working |
| 2.2 | [What comes back when the tool refuses](parts/02-the-tool-gate/2.2-what-comes-back-when-the-tool-refuses.md) | Why a refusal message is part of your prompt | working |
| 2.3 | [A rejection is not a failure](parts/02-the-tool-gate/2.3-a-rejection-is-not-a-failure.md) | Three states, one boolean, and why that is a bug | working |

### 3 · Binding the answer

*An approval has to be tied to the exact call it approves, and to be applied exactly once.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [The question has to be written down somewhere](parts/03-binding-the-answer/3.1-the-question-has-to-be-written-down.md) | Where a pending approval lives, and what keys it | working |
| 3.2 | [The request carries a copy of the call](parts/03-binding-the-answer/3.2-the-request-carries-a-copy-of-the-call.md) | Why the proposal is stored twice on purpose | working |
| 3.3 | [Approve one thing, execute another](parts/03-binding-the-answer/3.3-approve-one-thing-execute-another.md) | Time-of-check-to-time-of-use, measured 4 of 4 | production |
| 3.4 | [One approval, delivered twice](parts/03-binding-the-answer/3.4-one-approval-delivered-twice.md) | Why at-least-once delivery sends two emails | production |
| 3.5 | [The key names the decision, not the attempt](parts/03-binding-the-answer/3.5-the-key-names-the-decision.md) | The two ways an idempotency key is wrong | production |

### 4 · The node gate

*ADK-76: a standalone node that stops for a human, and everything that behaves surprisingly around it.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [A node that stops and asks](parts/04-the-node-gate/4.1-a-node-that-stops-and-asks.md) | How a graph pauses without holding a process | working |
| 4.2 | [Where the answer lands when the run comes back](parts/04-the-node-gate/4.2-where-the-answer-lands.md) | Why the asking node never sees the reply | working |
| 4.3 | [The human said no and the reply went anyway](parts/04-the-node-gate/4.3-the-human-said-no-and-the-reply-went-anyway.md) | Why an edge fires on completion, not on approval | production |
| 4.4 | [Asking the same person the same question twice](parts/04-the-node-gate/4.4-asking-the-same-person-twice.md) | What `rerun_on_resume` costs and what it buys | production |
| 4.5 | [NodeTool, and where it actually lives](parts/04-the-node-gate/4.5-nodetool-and-where-it-lives.md) | A real API that is not on the supported surface | production |

### 5 · The record

*The audit trail is derived from events that already exist — provided you put the right things in them.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [The decision is already written down](parts/05-the-record/5.1-the-decision-is-already-written-down.md) | Why you read the trail out rather than writing it | working |
| 5.2 | [What the record has to answer](parts/05-the-record/5.2-what-the-record-has-to-answer.md) | The six fields, and the two everybody omits | production |

### 6 · Wiring the desk

*The sixth station, the roads that go round it, and the check that catches both.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 6.1 | [The sixth station](parts/06-wiring-the-desk/6.1-the-sixth-station.md) | The gate as one node with two routed edges | working |
| 6.2 | [Three roads to one function](parts/06-wiring-the-desk/6.2-three-roads-to-one-function.md) | Complete mediation, failing 1 of 3 | production |
| 6.3 | [The check that goes red when the gate goes](parts/06-wiring-the-desk/6.3-the-check-that-goes-red-when-the-gate-goes.md) | Why asserting on the pause passes when broken | production |

### 7 · In production

*What the gate costs once the approver is a person with other work.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 7.1 | [The queue in front of the approver](parts/07-in-production/7.1-the-queue-in-front-of-the-approver.md) | The policy sets an arrival rate at a queue you did not model | production |
| 7.2 | [The deadline the approval must beat](parts/07-in-production/7.2-the-deadline-the-approval-must-beat.md) | Four things to do with an unanswered proposal, all wrong | production |
| 7.3 | [Who is allowed to say yes](parts/07-in-production/7.3-who-is-allowed-to-say-yes.md) | The gate records who approved and never checks | production |

**No papers of its own today.** Day 63 carries the separation-of-duty paper. Two already-taught papers
are cited and linked where they carry a part: *The protection of information in computer systems*
(`doi:10.1109/PROC.1975.9939`, Day 40) in 1.1 and 6.2, and *Principles of transaction-oriented
database recovery* (`doi:10.1145/289.291`, Day 47) in 3.4 and 5.1.

---

## §3 Setup — run this

```bash
cd days/day-64-approval-gates-build
ls lab
```

Nineteen files, all written for you — this is a day whose lab is teaching material rather than a rep,
because every claim in the parts is a measured run. The helpers are `_actions.py` (the effects
ledger), `_adk.py` (real `ToolContext` and `InvocationContext` with no model behind them),
`_policy.py` + `policy.json` (section 1's decision function), and `_replay.py` (the events an approval
round trip leaves).

No package is added today.

```bash
git diff pyproject.toml uv.lock
```

That must be empty and stay empty. `google-adk` stays pinned at **2.7.1**, verified in
`docs/PACKAGES.md`; every symbol this day uses was checked against the installed package rather than
against a tutorial.

Create the two files the build brief asks for, empty:

```bash
mkdir -p sutra
touch sutra/approval.py sutra/approval_policy.json
touch tests/test_approval.py
```

---

## §4 Build brief

The learner writes `sutra/approval.py`. The lab shows every mechanism working; this is where you
build the desk's own.

- `sutra/approval_policy.json` — the policy as **data**, one row per action, with `gated`, an optional
  `when` clause on the arguments, and a `because` on **every** row including the ungated ones.
  `TODO(me)`: decide the rows for Sutra's real actions. Day 63's table is the input; part 1.2 is the
  shape.
- `sutra/approval.py`
  - `needs_approval(action: str, args: dict) -> bool` — pure, no input/output, raises on an action
    with no row. `TODO(me)`.
  - `pending(action: str, args: dict, asked_by: str) -> dict` — build the pending record: the
    proposal, the evidence, the policy version, the key. Part 5.2 lists what it must contain.
    `TODO(me)`.
  - `decide(answer: dict, *, action: str) -> str` — return `"sent"`, `"refused"` or `"already done"`.
    Must use `is True`, and must be idempotent on the key from part 3.5. `TODO(me)`.
- `tests/test_approval.py` — one test per check in §5, plus **one that breaks it on purpose**:
  remove the idempotency key, watch check 6 go red, put it back. `TODO(me)`.

Two things this day deliberately does **not** solve, both named in the parts and both real:

- **Expiry.** Part 7.2 measures staleness and the gate never checks it. Adding `expires_at` means
  first choosing what happens when it fires, and that is a decision, not a default.
- **Authorisation.** Part 7.3 shows `by` is an unverified string. Fixing it needs an authenticated
  transport, which belongs to the deployment rather than to the lab.

---

## §5 The eval that must be able to fail

```bash
cd days/day-64-approval-gates-build/lab
uv run python gate.py; echo "exit: $?"
```

Six checks against `sutra/approval.py`. It is **red now** — `0/6`, exit 1 — because the module does
not exist, and each check reports as *skipped* rather than passing, since a check that cannot run has
not passed.

| # | Check | The innocent change that turns it red |
| --- | --- | --- |
| 1 | the module exposes `needs_approval` / `pending` / `decide` | rename one |
| 2 | `sutra/approval_policy.json` exists — the policy is data | inline the rules as `if` statements |
| 3 | an ungated action is not stopped | gate every write (part 7.1's naive policy) |
| 4 | a gated action is stopped | drop the `when` clause from a rule |
| 5 | a rejection prevents the effect | stop reading the answer (part 4.3) |
| 6 | one approval delivered twice acts once | put a timestamp in the key (part 3.5) |

Asserting that a **pause happened** would pass in three situations where the desk is broken; part 6.3
measures one of them going `weak assertion True / strong assertion False` on the same run.

---

## §6 Request budget

**Zero.** No provider is called today.

| Provider | Requests | Notes |
| --- | --- | --- |
| Gemini free tier | 0 | `gemini-2.5-flash` is named in `_adk.py` so an `LlmAgent` can be constructed; it is never invoked |
| Groq | 0 | — |
| OpenRouter | 0 | — |
| Ollama | 0 | — |

Every measurement in this day drives ADK's real code paths with the arguments supplied directly —
`FunctionTool.run_async` needs a `ToolContext`, not a model, and a graph node can be a plain function.
That is why the numbers are reproducible and why the day costs nothing.

There is a second budget this day introduces, denominated in a person's attention rather than in
requests: part 7.1 measures the real policy queueing **4 of 24** calls a shift and the naive one
queueing **14**, against an approver who clears twelve.

---

## §7 Traps

1. **The gate is on the tool, not on the function.** Three roads reach `close_ticket` and one honours
   the policy (part 6.2). A second `FunctionTool` around the same function is ungated and looks
   entirely innocent in review.
2. **`confirmed=False` is the default, not a rejection** (part 2.3). Nobody-asked and a person-said-no
   both read `False`; only the presence of the confirmation object distinguishes them.
3. **Truthiness inverts a decision.** A client that sends the string `'false'` passes
   `if not answer.get('approved')`. Use `is True` — measured in part 4.3, and the reason `desk.py`
   carries a comment on that line.
4. **An edge fires on completion, not on approval** (part 4.3). A graph that pauses, asks and records
   a rejection will still run the next node unless the successor reads the answer or the edge is
   routed.
5. **`rerun_on_resume` cuts both ways.** Off, the asking node never runs again and the answer goes to
   the successor; on, the body restarts from the top and an unguarded `yield` re-asks for ever
   (part 4.4). Trap #3 of plan §5.1 — yield, do not append — is what makes the pause possible at all.
6. **A wrong interrupt id fails silently.** The resume completes, the run does not advance, and
   `effects` is empty with no warning (parts 4.1 and 6.1). It is indistinguishable from a rejection
   unless you read the station trace.
7. **`NodeTool` is private.** It imports only from `google.adk.tools._node_tool`, is absent from
   `__all__`, and appears nowhere in the docs (part 4.5).

---

## §8 Verify before you code

Fetched on **2026-09-06**:

- `https://adk.dev/runtime/resume/` — the resume API, `ResumabilityConfig`, and the sentence this day
  leans on: *"Tools in an agent are run at least once, and may run more than once when resuming a
  workflow."* Note `https://adk.dev/runtime/resumability/` is a **404**; the page is `/resume/`.
- `https://adk.dev/graphs/dynamic/` — `RequestInput`, interrupt ids, and both halves of
  `rerun_on_resume`: with it false *"the resume payload is routed to the node's successor as input,
  bypassing the interrupted node"*, and with it true *"the node body re-runs from the top"*.
- `https://adk.dev/tools/confirmation/` and `https://adk.dev/tools/confirmation` — both return a
  redirect stub with no body; `https://adk.dev/tools/tool-confirmation/` is a **404**. The tool
  confirmation surface in §2 was therefore verified **against the installed package** rather than
  against a page, and the parts say so.

Verified against installed `google-adk==2.7.1` by introspection and by reading the source:

- `FunctionTool.__init__` takes exactly `(self, func, require_confirmation)`.
- `ToolConfirmation` declares exactly `hint`, `confirmed`, `payload`, and is decorated
  `@experimental(FeatureName.TOOL_CONFIRMATION)` — it emits
  `UserWarning: [EXPERIMENTAL] feature FeatureName.TOOL_CONFIRMATION is enabled.` on first use.
- `RequestInput` declares `interrupt_id`, `payload`, `message`, `response_schema`.
- `node()` accepts `rerun_on_resume` — snake-case in Python, written `rerunOnResume` in the docs.

**Three places the docs and the installed package disagree.** All are taught as the installed
behaviour, per Principle 14, and are recorded here rather than smoothed over:

1. **`ResumabilityConfig` is documented as required to enable resume.** Measured on 2026-09-06, this
   day's graph resumes **identically with and without it**. The parts set it anyway — it is what the
   documentation specifies — and say why.
2. **A node that `return`s a `RequestInput` pauses too**, not only one that `yield`s it. The habit is
   still `yield`; part 4.1 states the measured behaviour rather than the assumed rule.
3. **`NodeTool` is named by Addendum 01's ADK-76 and is not on the public surface**:
   `from google.adk.tools import NodeTool` raises `ImportError`,
   `'NodeTool' in google.adk.tools.__all__` is `False`, and it appears on no adk.dev page fetched
   today. It works when imported from `google.adk.tools._node_tool`. Part 4.5 teaches it as a pinned,
   unsupported dependency.

Plan §5 gives the ADK baseline as 2.6.3; this repository pins 2.7.1. A patch ahead is what Principle 7
expects, and `docs/PACKAGES.md` carries the row.

---

## §9 Say it in an interview

"We put a human approval step in front of the one action our support agent takes that cannot be
undone — sending a reply to a customer. The part that took the longest was not the pause; it was
learning that a pause is not a gate. Our first version paused correctly, asked a real person, received
a rejection, wrote it into the audit trail, and sent the email anyway, because in a graph the edge to
the next node fires when the previous node finishes, not when a human agrees. Everything on every
dashboard was green. So the test we kept is the one that asserts on the effect: make the approver say
no, then check nothing was sent. I can name the change that turns each of our six checks red, which
is the difference between a test and a comment. The other two things I would tell a team building this:
bind the approval to the exact call, because the arguments can change between the question and the
answer and we measured a naive gate accepting all four of a swapped, invented, ungated and honest
approval; and count what the policy costs a person, because gating every write took us from four
proposals a shift to fourteen against an approver who clears twelve, and a queue that never drains is
how approvals turn into clicks."

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked — which means read, run and answered out loud,
not skimmed. `./m done 64` refuses to commit until they are.

The day is finished when you can say, without looking, why asserting that the gate paused is a weaker
test than asserting that the reply did not go out, and can name a situation where the first passes and
the desk is broken.

---

## §11 Ledger & commit

**`docs/PROGRESS.md`** — append this row:

```text
| 64 | 2026-09-06 | ADK-48, ADK-76 | 25 | <hash> | ⚠️ |
```

**`docs/PACKAGES.md`** — no new row. No package is added today.

**`docs/PAPERS.md`** — no new row. This day teaches no paper of its own; it cites
`doi:10.1109/PROC.1975.9939` (Day 40) and `doi:10.1145/289.291` (Day 47), both already in the ledger.

**`docs/SKILL_PROVENANCE.md`** — no new row.

The commit message:

```text
day 64: approval gates, built — closes ADK-48, ADK-76
```
