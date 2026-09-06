---
day: 62
phase: 9
phase_name: "Durability and humans"
title: "Human-in-the-loop patterns"
ids: ["AG-23", "ADK-46"]
principles: [1, 2, 4, 7, 8, 10, 11, 13, 15, 16, 17, 18]
kind: lab
plan_version: "v2.2.1"
parts: 22
generated: "2026-09-06"
status: written
lab_scaffolded: true
commit: ""
---

# Day 62 — Human-in-the-loop patterns

> **Yesterday (Day 61):** pause and resume stopped being an accident. A checkpoint became a thing
> you could open and read, a run became something a different process could pick up, and the
> question of *what a checkpoint must contain* got a written answer.
> **Today:** the reason a run pauses on purpose. Four patterns wearing one name — approve, edit,
> answer, take over — each with its own record, its own resume and its own way of failing quietly.
> Every number in the day comes from a run, and the day spends no model calls.
> **Tomorrow (Day 63):** the policy. Which of the desk's actions actually need a person, on what
> evidence, and what happens when they say no.

---

## §1 Where we are

Day 60 established that a run is not the process it happens to be running in, and Day 61 made a
paused run something you can write down, put away, and pick up again somewhere else. Both of those
were about surviving a *crash*. Today the run stops for the most ordinary reason in any real
system: it has reached something it should not do alone.

Here is the day as a scene. You take a shirt to a tailor to be altered, and over the next week he
needs you four times. Once he holds it up with the sleeves pinned and asks whether he should cut —
you say yes, and he cuts. Once he has already pinned the hem and shows you his work; you fold it
up another finger's width yourself and hand it back. Once he telephones because he has run out of
the grey thread and cannot carry on until you tell him which shade is acceptable. And once he
tells you the collar is beyond saving, and you take the shirt home as it is.

Four interruptions. In a notebook they would all go under one heading: *waiting for customer*. And
that heading would be useless, because he needed a decision, then a correction, then a fact, then
somebody to take the job off him. The first three end with him carrying on. The fourth ends with
him stopping.

Every system that says "we put a human in the loop" has built the first one and bent the other
three into its shape. Today is about building all four properly, and then about the harder half:
the interruption that happens, is answered, is recorded — and changes nothing, because the screen
showed a ticket number and two buttons.

---

## §2 The map

Twenty-two parts in eight sections, then one paper. The day climbs from *what the four patterns
are* through *how ADK implements the ones it implements* to *why a working gate is mostly code the
framework does not give you*.

### Section 1 — the shape of the wait

What "human in the loop" actually names, and the two facts that are true of all four patterns:
waiting must not hold anything, and the person is an unreliable dependency.

| Part | What it answers | Level |
| --- | --- | --- |
| [1.1 — Four questions wearing one name](parts/01-the-shape-of-the-wait/1.1-four-questions-wearing-one-name.md) | What are the four patterns and how do they differ? | foundation |
| [1.2 — Waiting is a state, not a pause](parts/01-the-shape-of-the-wait/1.2-waiting-is-a-state-not-a-pause.md) | What does it cost to hold a worker slot while a person thinks? | foundation |
| [1.3 — Late, twice, or never](parts/01-the-shape-of-the-wait/1.3-late-twice-or-never.md) | What are the three ways a human answer goes wrong? | foundation |

### Section 2 — approve or reject

The pattern with the smallest answer, and ADK's machinery for it.

| Part | What it answers | Level |
| --- | --- | --- |
| [2.1 — The gate that returns one bit](parts/02-approve-or-reject/2.1-the-gate-that-returns-one-bit.md) | What does `require_confirmation=True` actually do to a call? | working |
| [2.2 — Decided per call, not per wiring](parts/02-approve-or-reject/2.2-decided-per-call-not-per-wiring.md) | How does one tool stop for a person on one ticket and not another? | working |
| [2.3 — What a "no" has to carry](parts/02-approve-or-reject/2.3-what-a-no-has-to-carry.md) | What does the agent learn from a rejection, and what is thrown away? | working |

### Section 3 — edit

The person returns a new version of the work rather than a verdict on it, and every record that
said "the agent sent this" is now wrong.

| Part | What it answers | Level |
| --- | --- | --- |
| [3.1 — The human changes the answer](parts/03-edit/3.1-the-human-changes-the-answer.md) | How does a payload travel out to a person and back changed? | working |
| [3.2 — Approve one thing, run another](parts/03-edit/3.2-approve-one-thing-run-another.md) | What stops an approval being reused for a different call? | production |
| [3.3 — What the record says the customer got](parts/03-edit/3.3-what-the-record-says-the-customer-got.md) | Which questions can your approval record actually answer? | production |

### Section 4 — ask a question

The agent is missing an input rather than permission. Different pause, different answer shape, and
the only pattern where the interruption is sometimes a bug.

| Part | What it answers | Level |
| --- | --- | --- |
| [4.1 — A missing fact is not a missing permission](parts/04-ask-a-question/4.1-a-missing-fact-is-not-a-missing-permission.md) | How does `request_input` differ from a confirmation? | working |
| [4.2 — A question with edges](parts/04-ask-a-question/4.2-a-question-with-edges.md) | When should the answers be enumerated instead of open? | working |
| [4.3 — The question you should not have asked](parts/04-ask-a-question/4.3-the-question-you-should-not-have-asked.md) | How many of the agent's questions were answerable from the ticket? | production |

### Section 5 — take over

The one pattern where the correct next step is for the run to end, and the leak that follows when
nothing records it.

| Part | What it answers | Level |
| --- | --- | --- |
| [5.1 — The pattern with no resume](parts/05-take-over/5.1-the-pattern-with-no-resume.md) | What does a run do when the person does the job themselves? | working |
| [5.2 — The run nobody closed](parts/05-take-over/5.2-the-run-nobody-closed.md) | What does a failure look like when its signature is the absence of an event? | production |

### Section 6 — nobody answered

Deadlines, staleness, and the record that has to survive three processes.

| Part | What it answers | Level |
| --- | --- | --- |
| [6.1 — A default is a decision nobody made](parts/06-nobody-answered/6.1-a-default-is-a-decision-nobody-made.md) | Which timeout policy is safe? | working |
| [6.2 — The answer to a question that no longer exists](parts/06-nobody-answered/6.2-the-answer-to-a-question-that-no-longer-exists.md) | What if the world moved while the question waited? | production |
| [6.3 — Where the question goes](parts/06-nobody-answered/6.3-where-the-question-goes.md) | What must the pending record contain to survive three processes? | production |

### Section 7 — what the human sees

The machinery can be perfect and the decision can still fail to happen.

| Part | What it answers | Level |
| --- | --- | --- |
| [7.1 — The tick box nobody reads](parts/07-what-the-human-sees/7.1-the-tick-box-nobody-reads.md) | What can an approval screen possibly catch? | production |
| [7.2 — The card that makes checking possible](parts/07-what-the-human-sees/7.2-the-card-that-makes-checking-possible.md) | How do you turn a reading task into a noticing task? | production |
| [7.3 — Where ADK confirmation will not go](parts/07-what-the-human-sees/7.3-where-adk-confirmation-will-not-go.md) | What does the framework give you, and what must you build? | production |

### Section 8 — in production

The arithmetic that decides whether the gate works at all, and what to measure once it ships.

| Part | What it answers | Level |
| --- | --- | --- |
| [8.1 — The backlog is the real limit](parts/08-in-production/8.1-the-backlog-is-the-real-limit.md) | How much can you gate before the gate becomes a wall? | production |
| [8.2 — The three numbers to put on a wall](parts/08-in-production/8.2-the-three-numbers-to-put-on-a-wall.md) | How would you know the gate had stopped working? | production |

### Papers — read after the parts

Principle 4 at the scale of a day: build the mechanism first, then read the proposal.

| Paper | Why it is here |
| --- | --- |
| [Ironies of automation](papers/01-ironies-of-automation.md) — `doi:10.1016/0005-1098(83)90046-8` | Why automating the routine part makes the human's remaining part harder, and why a reviewer gets worse at exactly the job you are adding them to do |

---

## §3 Setup — run this

The lab is already scaffolded. Confirm it and confirm the day adds nothing:

```bash
cd days/day-62-human-in-the-loop/lab
ls *.py | wc -l        # 21
ls papers/ironies-of-automation/
```

No package is added today. `google-adk==2.7.1` is already pinned in `pyproject.toml` and recorded
in `docs/PACKAGES.md`; the day uses `FunctionTool`, `ToolContext`, `request_input`,
`get_user_choice`, `InMemoryRunner` and `App` from it, and nothing else.

```bash
git diff pyproject.toml uv.lock   # must be empty, and stay empty
```

The twenty-one scripts, grouped by what they are for:

| Files | Purpose |
| --- | --- |
| `_desk.py` `_pending.py` `_scripted.py` | the shared fixtures: one ticket archive, the parked-question store, and a model that reads its replies off a list so no provider is called |
| `approve.py` `perticket.py` `retry.py` | section 2 — the static gate, the per-call condition, and what a rejection carries |
| `edit.py` `tamper.py` `audit.py` | section 3 — the payload round trip, the anchor check, the audit record |
| `ask.py` `avoidable.py` | section 4 — the two question tools, and how many questions were avoidable |
| `takeover.py` | section 5 — both arms, recorded and unrecorded |
| `default.py` `stale.py` `roundtrip.py` | section 6 — timeout policies, the freshness guard, three processes one run |
| `stamp.py` `card.py` | section 7 — what each interface can catch, and the card itself |
| `waiting.py` `unreliable.py` `backlog.py` | the arithmetic: slots, unreliable answers, queue growth |
| `gate.py` | the eval, red until the build brief is done |
| `papers/ironies-of-automation/` | the paper demo, with its ablation switch |

---

## §4 Build brief

Create `sutra/hitl.py` and `tests/test_hitl.py`. The lab proves what each piece has to do; the
module is where you write it.

- `TODO(me)` — `ask(question_id, shown, anchor, deadline)`: write a pending question. Its docstring
  must say that the record carries what the person was **shown**, because `gate.py` checks for it,
  and 3.3 is the argument for why.
- `TODO(me)` — `digest(shown)`: a short hash of the evidence, canonicalised. Decide which fields go
  in it. 6.2 shows both failures — too many fields and every approval is stale, too few and the
  guard passes on a change that mattered.
- `TODO(me)` — `answer(question_id, decision)`: refuse a second answer and refuse an answer after
  the deadline, as one indivisible step. 1.3 measured what the naive version costs.
- `TODO(me)` — `EXPIRED` and `ON_TIMEOUT`: name the expired state and name the timeout policy.
  6.1 is the argument that a policy you did not choose is still a policy.
- `TODO(me)` — `resume(question_id)`: re-check the digest and the anchor before acting. 3.2 and 6.2
  are the two checks; they are different and you need both.
- `TODO(me)` — an outcome enum wide enough for approve, reject and take over, plus `agent_sent`.
  5.1 is why a boolean cannot carry it.
- `TODO(me)` — `oldest_open(records, now)` and `yield_rate(decisions)` from 8.2. Run the first one
  against the store `takeover.py --naive` leaves behind, and decide whether the missing `asked_at`
  is a bug in the record or in the function.
- `TODO(me)` — in `lab/tamper.py`, add `anchor_only()` returning just the anchor from a real pause,
  so 3.2's exercise runs. Writing it is how you find out what your own record must store to make
  the same comparison ADK makes.
- `TODO(me)` — in `lab/ask.py`, add a `--wrong` flag that answers `'ORD-0000'`. Nothing objects.
  That is 4.1's point about a fact being trusted completely.

---

## §5 The eval that must be able to fail

```bash
uv run python days/day-62-human-in-the-loop/lab/gate.py; echo "exit: $?"
```

Six checks against `sutra/hitl.py`, which does not exist yet. Red before the build brief:

```text
  [FAIL] sutra/hitl.py imports  (cannot import name 'hitl' from 'sutra' (...\sutra\__init__.py))

  0/6 checks pass - sutra/hitl.py has not been written yet
  see the build brief in LESSON.md section 4
exit: 1
```

Each check names the part it comes from, so a red line is an address rather than a complaint. When
all six pass, break one on purpose — delete `EXPIRED` — and watch it go red again. A check you have
not seen fail is a check you have not tested (Principle 11).

---

## §6 Request budget

**Zero.** No provider is called at any point today.

| Provider | RPM used | RPD used |
| --- | --- | --- |
| Gemini (AI Studio free tier) | 0 | 0 |
| Groq | 0 | 0 |
| OpenRouter `:free` | 0 | 0 |
| Ollama (local) | 0 | 0 |

Every run that needs a model uses `_scripted.py`, a `BaseLlm` subclass that returns entries from a
list. That is not a shortcut around the zero-budget rule — it is what makes the day's transcripts
reproducible, because a real model would answer differently on the second run and the numbers in
these parts could not be checked.

---

## §7 Traps

1. **Assuming "human in the loop" is one thing.** It is four, and a design that handles approve
   handles none of the others. 1.1.
2. **Holding a worker slot while a person thinks.** Measured: five of twelve tickets never started.
   The fix is not more workers. 1.2.
3. **No state on the pending question.** A double-click sends two replies; a late answer sends one
   the system had already recorded as not sent. 1.3.
4. **Expecting a rejection to carry a reason.** In `google-adk==2.7.1` the rejection branch returns
   a fixed string and the payload is never read, so the model retries and the person is asked
   twice. 2.3 and 7.3.
5. **Forgetting `tool_context` in the tool signature.** ADK strips it from the declaration, so the
   schema looks identical and the pause silently never happens. 3.1.
6. **Trusting the framework's anchor check on a path the framework cannot see.** ADK compares the
   confirmation against its own session history. An approval that comes back through your own queue
   page is a second path, and it must do its own comparison. 3.2.
7. **Gating a missing fact.** Two buttons cannot supply an order number. 4.1.
8. **Modelling take-over as a rejection.** The rejection rate then mixes "the draft was wrong" with
   "the customer telephoned", and those need opposite responses. 5.1.
9. **No timeout policy.** *Wait for ever* is a policy, and it is the one nobody would choose. 6.1.
10. **A one-line approval screen.** Measured ceiling: 1 of 8 planted mistakes catchable. 7.1.
11. **Gating everything.** At 100% gated the queue grows without limit and a second reviewer only
    halves the slope. 8.1.

**1.x → 2.x note.** This day does not touch one of plan §5.1's four traps directly, but trap #4 is
adjacent throughout: `tamper.py` disables ADK's own logger only because the runtime **surfaces**
the mismatch exception before re-raising it, which is 2.x behaving correctly. A gate that caught
that exception and returned a string would hide the one failure this section exists to detect.

---

## §8 Verify before you code

Fetched on 2026-09-06:

- `https://adk.dev/tools-custom/function-tools/` — long-running function tools, `request_input`,
  `get_user_choice`, `require_confirmation`, and `tool_context.request_confirmation`.

Read from the installed `google-adk==2.7.1`, because the pages above do not state them:

- `google/adk/tools/tool_confirmation.py` — `ToolConfirmation` has exactly three fields: `hint`,
  `confirmed`, `payload`. There is no reason, no deadline, no approver identity.
- `google/adk/tools/function_tool.py` — the rejection branch is
  `return {'error': 'This tool call is rejected.'}`, and it does not read `payload`. That is the
  source of 2.3's measured finding, and it is deliberate rather than a bug.
- `google/adk/tools/long_running_tool.py` — "pause" is `self.is_long_running = True` beside a
  function that returns `None`.

**A discrepancy worth recording.** Nothing in the fetched page describes what a rejection returns
to the model, or that a reason attached to a confirmation is discarded. Both were established by
running `retry.py` and then confirmed against the installed source. This day teaches the installed
behaviour, and 7.3 says explicitly that code must depend on `confirmed` being `False` and never on
that string, because the string is not part of any published contract.

**ADK-76** — HITL resumption for standalone nodes and `NodeTool` — belongs to Day 64 and is
deliberately not covered here.

---

## §9 Say it in an interview

"We put a human in front of the send step, and the first thing we got wrong was thinking that was
one feature. It is four: approve, edit, answer, take over. They look identical from outside — the
run stops and somebody is interrupted — and they need different records and different resume
paths. Take-over was the one that hurt: reviewers were pressing reject when they had already
settled the ticket on the phone, so our rejection rate mixed 'bad draft' with 'customer rang in'
and we spent weeks improving drafting that was fine. The second thing we got wrong was the screen.
I took eight mistakes we had actually shipped and mapped each to the field it was in: our one-line
approval card could have caught one of the eight. That is a ceiling, not a prediction — real
reviewers do worse. The fix was not training, it was putting the reply text on the card and
computing the comparisons for them, so the job became noticing rather than reading. And I would
say the framework gives you less of this than people expect. ADK's confirmation is genuinely good
at the pause and at refusing an answer whose anchor does not match the call. Everything that makes
it a control — the pending store, the state that stops a duplicate, the deadline, the outcome
vocabulary, the freshness digest, the card — was ours."

---

## §10 Done when

`CHECKLIST.md` in this folder, every box ticked. The day is done when you can explain the four
patterns without looking, when `gate.py` goes from red to green and back to red on purpose, and
when you can say what your approval screen can and cannot catch. Not before, and not because a
number of sittings have passed.

---

## §11 Ledger & commit

`docs/PROGRESS.md` — append verbatim, filling the hash after committing:

```text
| 62 | 2026-09-06 | AG-23, ADK-46 | 22 (+1 paper) | <hash> | ⚠️ |
```

`docs/PAPERS.md` — already appended on 2026-09-06:

```text
| Ironies of automation | doi:10.1016/0005-1098(83)90046-8 | 1983 | 2026-09-06 | 62 | `days/day-62-human-in-the-loop/papers/01-ironies-of-automation.md` |
```

`docs/PACKAGES.md` — no row. No package is added today.

`docs/SKILL_PROVENANCE.md` — no row. No third-party skill is used today.

Commit message:

```text
day 62: human-in-the-loop patterns - closes AG-23, ADK-46
```
