---
day: 63
phase: 9
phase_name: "Durability and humans"
title: "Approval gates — design (what needs a human, and why)"
ids: ["SEC-05", "ADK-47"]
principles: [1, 2, 4, 7, 8, 10, 11, 13, 15, 16, 17, 18]
kind: concept
plan_version: "v2.2.1"
parts: 25
generated: "2026-09-06"
status: written
lab_scaffolded: true
commit: ""
---

# Day 63 — Approval gates: design

> **Yesterday (Day 62):** the four shapes a human can occupy in a run — approve or reject, edit,
> answer a question, take over — and the fact that waiting is a state rather than a pause in the code.
> **Today:** *which* actions get a human, on what evidence, decided by whom, and what happens when
> they say no. The output is not code; it is a policy table with an argument on every row, and a
> failing check that says what "built" will mean.
> **Tomorrow (Day 64):** the build. `sutra/approvals.py`, the gate on the triage graph's write step,
> and ADK-76's HITL resumption for standalone nodes.

---

## §1 Where we are

There is a shop near the bus stand with a sign taped to the counter: **ID REQUIRED**. The first week
the owner checked properly. By the second month he is asked two hundred times a day for ten-rupee
top-ups, and his eyes go to the card and register that a card exists. The afternoon somebody buys a
connection on somebody else's card, he hands it back without a pause.

He did not get careless. He got asked two hundred times a day.

That is the whole of today, and it is why this is a design day rather than a build day. An approval
gate is not made of code — the code is four lines and it always works. It is made of **somebody's
attention**, and attention is a supply with a fixed size that runs out during a shift. Every other
control in this curriculum is indifferent to how many times it fires. Day 40's tool filter checks the
ten-thousandth call exactly as carefully as the first. A gate does not, because the gate is a person,
and the number of times you ask them is a number you chose.

So the question people ask — *"should a human approve this?"* — has no useful answer, because the
honest reply is almost always yes. The question that produces a working system is:

> **Which** actions, on **what** evidence, decided by **whom**, and what happens when they say no?

Today answers all four, against Sutra's own ten actions, using one recorded overnight batch —
twenty-seven tickets, one hundred and forty-nine actions, forty-one of them writes, six of those
wrong, written down in advance the way Day 50 wrote its answer key before tuning anything.

The day spends **no model calls at all**. Every number in it came from a run.

---

## §2 The map

Twenty-five parts in seven sections, then one paper. The day climbs from *what a gate is* to *what
the framework actually offers*, and it hands Day 64 a red test rather than a summary.

### 1 — The gate that means nothing

*What a gate is made of, and why "gate everything" is the least safe option on the list.*

| # | Part | Answers | Level |
| --- | --- | --- | --- |
| 1.1 | [A control that fires on everything](parts/01-the-gate-that-means-nothing/1.1-a-control-that-fires-on-everything.md) | Why did asking 41 times catch fewer mistakes than asking 11? | foundation |
| 1.2 | [A permission is not a gate](parts/01-the-gate-that-means-nothing/1.2-a-permission-is-not-a-gate.md) | What does an approval do that an allowlist cannot? | foundation |
| 1.3 | [The four questions](parts/01-the-gate-that-means-nothing/1.3-the-four-questions.md) | What must a gate design actually decide? | working |

### 2 — Sorting the actions

*The axes that decide which actions are candidates — and the one axis that is not allowed in.*

| # | Part | Answers | Level |
| --- | --- | --- | --- |
| 2.1 | [Reversible, and the cost of the undo](parts/02-sorting-the-actions/2.1-reversible-and-the-cost-of-the-undo.md) | Is "reversible" a property of the code or of the person it happened to? | working |
| 2.2 | [Blast radius counted in people](parts/02-sorting-the-actions/2.2-blast-radius-counted-in-people.md) | Who is affected, and does the count change the verdict? | working |
| 2.3 | [The undo nobody asks for](parts/02-sorting-the-actions/2.3-the-undo-nobody-asks-for.md) | What happens when a reversible mistake is never reported? | working |
| 2.4 | [Defeated by its own volume](parts/02-sorting-the-actions/2.4-defeated-by-its-own-volume.md) | Why is frequency a design fact rather than a people problem? | production |

### 3 — The policy table

*The artefact: one row per action, a verdict, and a sentence somebody can disagree with.*

| # | Part | Answers | Level |
| --- | --- | --- | --- |
| 3.1 | [The write inventory](parts/03-the-policy-table/3.1-the-write-inventory.md) | What can this agent actually do, counted rather than remembered? | working |
| 3.2 | [The table and the argument](parts/03-the-policy-table/3.2-the-table-and-the-argument.md) | Why keep both a suggested and a decided verdict? | production |
| 3.3 | [The rows that are not gated](parts/03-the-policy-table/3.3-the-rows-that-are-not-gated.md) | What does leaving an action alone cost, and who wrote that down? | working |
| 3.4 | [The Tuesday a tool arrives](parts/03-the-policy-table/3.4-the-tuesday-a-tool-arrives.md) | What does the gate do with a name it has never seen? | production |

### 4 — What the approver sees

*An approval is only worth what the approver could judge from what was in front of them.*

| # | Part | Answers | Level |
| --- | --- | --- | --- |
| 4.1 | [Approving bytes, not pointers](parts/04-what-the-approver-sees/4.1-approving-bytes-not-pointers.md) | After a resume, what exactly did the human approve? | working |
| 4.2 | [The request and the diff](parts/04-what-the-approver-sees/4.2-the-request-and-the-diff.md) | Why are three of three mistakes invisible on the request screen? | working |
| 4.3 | [Separation of duty](parts/04-what-the-approver-sees/4.3-separation-of-duty.md) | When are two signatures one pair of eyes? | production |
| 4.4 | [The four facts a record must hold](parts/04-what-the-approver-sees/4.4-the-four-facts-a-record-must-hold.md) | What will an incident review ask, and can your record answer it? | production |

### 5 — When nobody answers

*Sutra's batch runs overnight. Absence is not the exception here; it is every night.*

| # | Part | Answers | Level |
| --- | --- | --- | --- |
| 5.1 | [Fail closed or fail open](parts/05-when-nobody-answers/5.1-fail-closed-or-fail-open.md) | Which of Sutra's gated actions is safer to perform than to hold? | production |
| 5.2 | [The answer nobody gave](parts/05-when-nobody-answers/5.2-the-answer-nobody-gave.md) | How many of the night's approvals were answered by a constant? | production |
| 5.3 | [The key with the neighbour](parts/05-when-nobody-answers/5.3-the-key-with-the-neighbour.md) | What separates a break-glass path from a hole in the policy? | production |

### 6 — Gates that are decoration

*The failure lab. Four ways a gate stays green while doing nothing.*

| # | Part | Answers | Level |
| --- | --- | --- | --- |
| 6.1 | [The road the gate is not on](parts/06-gates-that-are-decoration/6.1-the-road-the-gate-is-not-on.md) | Six tickets closed, three approvals asked — what failed? | production |
| 6.2 | [The field the agent writes](parts/06-gates-that-are-decoration/6.2-the-field-the-agent-writes.md) | What happens when the gated party supplies the gate's input? | production |
| 6.3 | [Ask until somebody says yes](parts/06-gates-that-are-decoration/6.3-ask-until-somebody-says-yes.md) | Is your rejection a decision or a delay? | production |
| 6.4 | [The sweep nobody runs](parts/06-gates-that-are-decoration/6.4-the-sweep-nobody-runs.md) | Is your design right, or merely right on a good night? | production |

### 7 — The two doors

*ADK-47: what the framework actually offers, read off the installed package and the live docs.*

| # | Part | Answers | Level |
| --- | --- | --- | --- |
| 7.1 | [The door on the tool](parts/07-the-two-doors/7.1-the-door-on-the-tool.md) | What does `require_confirmation` accept, and why can Sutra not use it? | working |
| 7.2 | [The door in the graph](parts/07-the-two-doors/7.2-the-door-in-the-graph.md) | Where does the human's reply go when the run resumes? | production |
| 7.3 | [What Day 64 is handed](parts/07-the-two-doors/7.3-what-day-64-is-handed.md) | What does "built" mean, stated as a command that exits zero? | production |

### Papers — read after the parts

| # | Paper | Identifier |
| --- | --- | --- |
| 01 | [Well-formed transactions and separation of duty](papers/01-well-formed-transactions.md) | `doi:10.1109/SP.1987.10001` |

---

## §3 Setup — run this

No package is added today. `git diff pyproject.toml uv.lock` is empty before you start and empty when
you finish.

```bash
mkdir -p days/day-63-approval-gates-design/lab/papers/well-formed-transactions
cd days/day-63-approval-gates-design/lab

# shared fixtures - the recorded batch, the action facts, the policy table
touch _runs.py _actions.py _policy.py

# section 1-2: what a gate is made of, and sorting the actions
touch everything.py permission.py four.py undo.py radius.py visible.py volume.py

# section 3: the policy table
touch inventory.py table.py free.py unknown.py

# section 4: what the approver sees
touch bind.py diff.py duty.py record.py

# section 5: when nobody answers
touch absent.py timeout.py breakglass.py

# section 6: gates that are decoration
touch around.py talkpast.py shopping.py stamp.py

# section 7 + the eval
touch doors.py gate.py

# the paper demo
touch papers/well-formed-transactions/cw.py papers/well-formed-transactions/demo.py
```

The three underscored files are imported by almost everything else, which is why they are created
first. `_runs.py` holds the recorded batch and its ground-truth `wrong` flags, `_actions.py` holds the
ten actions and their facts, and `_policy.py` holds `POLICY` together with `suggest()`, `gate_for()`
and `threshold_allows()`. Every other file is a single measurement that one part runs, and the
grouping above matches the §2 map so that a part and its script are easy to find from each other. The
`papers/` subdirectory holds the paper demo (plan §17.4.2): two files, given complete in the paper
document, because a demo is teaching material rather than a rep.

`google-adk` is already pinned at `2.7.1` in `pyproject.toml`, verified in `docs/PACKAGES.md`. Only
`doors.py` imports it.

---

## §4 Build brief

The lab is complete and runnable. What is **not** built is Sutra's own approval module, and that is
tomorrow's job — today only writes down what it has to be.

Create `sutra/approvals.py`:

- `TODO(me)`: port `POLICY`, `Row`, `gate_for()` and `threshold_allows()` out of the lab and into the
  package. Keep the `because` sentences verbatim; they are the reviewable half.
- `TODO(me)`: decide whether `suggest()` comes with them. It is a scoring function with no runtime
  role, and [3.2](parts/03-the-policy-table/3.2-the-table-and-the-argument.md) argues it earns its
  place at review time. Write down which you chose and why, in the module docstring.
- `TODO(me)`: add the `fails_open` column from
  [5.1](parts/05-when-nobody-answers/5.1-fail-closed-or-fail-open.md). Three of four closed, one open.
  It is a column, not a module constant.
- `TODO(me)`: add the `timeout_hours` column and set it from the rota's real reading time, not from a
  number that sounds careful ([5.2](parts/05-when-nobody-answers/5.2-the-answer-nobody-gave.md)).

Create `tests/test_approvals.py`:

- `TODO(me)`: one test per check that `lab/gate.py` currently reports as `cannot check` — five of
  them. Each is a sentence from this day turned into an assertion.
- `TODO(me)`: at least one test that goes RED when you break it on purpose. Delete a `because` and
  watch it fail; put it back.

Do **not** wire the gate into the triage graph today. Day 64 does that, and it needs
[7.2](parts/07-the-two-doors/7.2-the-door-in-the-graph.md)'s resumption behaviour in front of it.

---

## §5 The eval that must be able to fail

```bash
cd days/day-63-approval-gates-design/lab
uv run python gate.py; echo "exit: $?"
```

Red today, and it should be: `6 finding(s)`, `exit: 1`. One finding is that `sutra/approvals.py` does
not exist; the other five are checks that **cannot run** until it does, and they are counted as
failures rather than skipped, because a check that cannot run has not passed.

The five are the day's arguments made mechanical: every action classified, the lookup fails closed on
an unknown name, every row carries a non-empty reason, the threshold is stated exactly once, and no
gate verdict is hard-coded outside the policy module.

Day 64 is finished when that command exits `0`. What it still will not prove is that the gate is
*reached* — [7.3](parts/07-the-two-doors/7.3-what-day-64-is-handed.md) says so explicitly, and that
check belongs to Day 64's wiring and Day 65's audit.

---

## §6 Request budget

**Zero.** No provider is contacted today.

| Provider | Requests | Why |
| --- | --- | --- |
| Gemini (AI Studio free tier) | 0 | no model is called; `doors.py` constructs ADK objects and inspects them |
| Groq | 0 | — |
| OpenRouter (`:free`) | 0 | — |
| Ollama (local) | 0 | — |

Every number in every part comes from a deterministic script over a recorded batch. The approvers,
the drafts and the classifications are scripted, which is what makes the comparisons repeatable and
the pasted output honest.

---

## §7 Traps

1. **Gating everything and calling it the safe default.** It is the least safe option on the list once
   attention is finite, and [1.1](parts/01-the-gate-that-means-nothing/1.1-a-control-that-fires-on-everything.md)
   measures it: 41 asks caught 2 of 6, 11 asks caught 4 of 4.
2. **A `because` that restates the verdict.** *"Gated because it is risky"* is a row with nothing in
   it. Test: could a reader disagree with this sentence using only what you wrote down?
3. **`POLICY.get(action, NEVER)`.** That default says *"assumed safe because nobody said otherwise"*
   and nobody would write that sentence in a design document. `gate_for()` fails closed for this
   reason.
4. **Approving a pointer.** A ticket id survives a resume; the draft behind it does not. Store the
   payload and its fingerprint ([4.1](parts/04-what-the-approver-sees/4.1-approving-bytes-not-pointers.md)).
5. **Showing the request instead of the diff.** Four closes differ by four digits. Three of them are
   wrong and none of the tells is in a field the action changes.
6. **Two signatures on the agent's own summary.** That is not separation of duty; it caught 0 of 4.
7. **A timeout shorter than the rota's reading time.** Then the constant decides everything and leaves
   the same log line a person would ([5.2](parts/05-when-nobody-answers/5.2-the-answer-nobody-gave.md)).
8. **`require_confirmation` typed next to a tool.** That is a second place a gate verdict lives.
   Build tools *from* the table; `gate.py` greps for exactly this.
9. **ADK trap, and it is documented rather than in the package:** tool confirmation lists
   `DatabaseSessionService` as unsupported, and Day 47 chose exactly that. A feature's compatibility
   list is part of its API.
10. **The default resumption bypasses the node that asked.** Code written after `yield RequestInput`
    never runs unless `rerun_on_resume=True` — the same rule Day 60 measured for crash resumes, and it
    fails silently.

---

## §8 Verify before you code

Fetched on 2026-09-05 (paper record re-checked 2026-09-06):

| What | URL | What it said |
| --- | --- | --- |
| Tool confirmation | `https://adk.dev/tools-custom/confirmation/` | *"The Tool Confirmation feature is experimental and has some known limitations."* `DatabaseSessionService` and `VertexAiSessionService` listed as unsupported. `require_confirmation` takes a boolean or a callable predicate. |
| Graph human input | `https://adk.dev/graphs/human-input/` | `RequestInput` pauses the workflow. Default `rerunOnResume: false` — *"the reply is routed to the node's successor as input, bypassing the interrupted node"*. A response schema *"does not reformat a human reply"*. |
| The paper record | `https://api.crossref.org/works/10.1109/SP.1987.10001` | *A Comparison of Commercial and Military Computer Security Policies*, 1987 IEEE Symposium on Security and Privacy, 1987. |

Everything in section 7 was **also** introspected against installed `google-adk==2.7.1` rather than
taken from the page — `doors.py` calls `FunctionTool.check_require_confirmation` and reads
`ToolConfirmation.model_fields` and `RequestInput.model_fields` directly.

Two notes where the docs and the package differ, recorded rather than smoothed over:

- The documentation writes `rerunOnResume`; the installed Python is `rerun_on_resume`. Day 60 recorded
  the same thing.
- The `DatabaseSessionService` limitation exists **only** on the documentation page. Every signal
  available from the package says tool confirmation works: the symbols import, the tools construct,
  and the predicate returns correct answers.

---

## §9 Say it in an interview

"We put a human in front of the agent's customer-visible writes, and the first version gated every
write, which is what everybody builds. I had a recorded night — twenty-seven tickets, forty-one
writes, six of them wrong — and gating everything caught two of the six, because four were past the
twentieth item in the queue and nobody reads item thirty-eight at three in the morning. Gating only
the customer-visible and irreversible actions cut the queue to eleven and caught four out of four. It
lets two internal-note mistakes through on purpose, and that trade is written in the policy table with
the reason and the count. The thing I would defend hardest is that the policy is data in one module
with a sentence per row, and there is a test that fails the build if a gate verdict appears anywhere
else — because the alternative is finding out during an incident that a node had its own opinion. The
failure that surprised me most was the one where nothing broke: a note-writing tool grew a status
field, six tickets got closed, three approvals were asked for, and no default fired because the tool's
name was known and its row said never. Our fail-closed default protects us from new tools and cannot
see an old tool with a new effect."

---

## §10 Done when

`CHECKLIST.md` is fully ticked, and `./m done 63` refuses to commit until it is.

The day is finished when you can state, without scrolling, which of Sutra's ten actions are gated and
why the ungated ones are not — and when `lab/gate.py` is red for the right six reasons rather than for
a missing import.

---

## §11 Ledger & commit

`docs/PROGRESS.md` — append:

```text
| 63 | 2026-09-06 | SEC-05, ADK-47 | 25 (+1 paper) | <hash> | ⚠️ |
```

`docs/PAPERS.md` — already appended when the citation was verified:

```text
| A Comparison of Commercial and Military Computer Security Policies | doi:10.1109/SP.1987.10001 | 1987 | 2026-09-05 | 63 | `days/day-63-approval-gates-design/papers/01-well-formed-transactions.md` |
```

`docs/PACKAGES.md` — no new row. No package was added today.

Commit:

```text
day 63: approval gates - design (what needs a human, and why) - closes SEC-05, ADK-47
```
