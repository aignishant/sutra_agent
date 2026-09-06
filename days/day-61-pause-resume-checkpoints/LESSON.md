---
day: 61
phase: 9
phase_name: "Durability and humans"
title: "Pause/resume & checkpoints in ADK"
ids: ["ADK-44", "ADK-45"]
principles: [1, 2, 4, 7, 8, 10, 11, 13, 15, 16, 17, 18]
kind: lab
plan_version: "v2.2.1"
parts: 21
generated: "2026-09-06"
status: written
lab_scaffolded: true
commit: ""
---

# Day 61 — Pause/resume and checkpoints in ADK

> **Yesterday (Day 60):** durable execution, built by hand. Resume, replay and idempotency as three
> separate problems, an event log as the source of truth, and a first look at ADK's own surface —
> including the measured fact that 2.7.1 **skips** the node that was running when the process died.
> **Today:** the framework half, properly. What ADK counts as a pause, what a checkpoint actually
> contains when you open it, and the two different checkpoints that share one field — one of which
> is written faithfully and never read back. The day spends **zero model calls**.
> **Tomorrow (Day 62):** human-in-the-loop patterns — the four shapes a person can occupy in a run,
> all of which are built on the one pause condition this day measures.

---

## §1 Where we are

Day 60 built the mechanism by hand and then looked at what ADK does. Today is the other order:
start from what the framework actually does, measured, and let the surprises land.

Here is the day as a scene. A man is going down a long list of parcels in a sorting office, marking
each one off on a sheet on his clipboard as he finishes it. Halfway down, his shift ends abruptly —
somebody needs the trolley — and he goes home.

Two questions decide whether this office works.

The first: **does the sheet survive?** If he took the clipboard home, the next person starts the list
again and every parcel already handled is handled twice. If he left it on the trolley, they carry on
from where he stopped.

The second, and it is the one nobody thinks of: **does anybody hand the sheet to the next person?**
Because the sheet can be sitting there, filled in correctly, in the right place, and if the next man
is given a fresh one from the drawer he starts at the top regardless. The sheet was written. The
sheet was kept. Nobody read it.

That second question is today's finding. ADK gives a custom agent a way to keep its own progress
sheet, and the mechanism works exactly as documented — when that agent is the root of the App. Put
the identical agent inside a graph, which is where every station in Sutra lives, and the sheets are
written into the log, six of them, and the agent is handed an empty dictionary on resume and starts
its list again. Nothing raises. The checkpoints are in the file. You can read them while the work is
being repeated.

The day is arranged so that lands as a measurement rather than a claim. Section 1 establishes what
stopping and resuming even mean here — including that there is no `pause()` method and never was.
Section 2 opens a real checkpoint file and reads it field by field. Section 3 is the agent's own
note: it working, it failing, and the repair, which turns out to have two halves where everybody
ships one. Section 4 runs the whole thing end to end — start, kill with a real `os._exit`, pick up
in a fresh process. Section 5 breaks it three ways, and the third is the sharpest thing in the day:
a run that failed *politely* is harder to resume than one that was destroyed, and deleting a single
event from its log proves it. Section 6 asks what all this costs in things other than bytes.

Every number below came out of a run on this machine. Nothing here is spent on a model.

---

## §2 The map

Read the parts in order. Each section builds one idea and hands it to the next.

### Section 1 — `01-two-ways-to-stop`

*What it means for a run to stop, and what a resume actually is. The vocabulary the rest of the day
uses.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [The call that dropped and the call that ended](parts/01-two-ways-to-stop/1.1-the-call-that-dropped-and-the-call-that-ended.md) | A killed run and a failed run leave the same checkpoint — so what tells them apart? | foundation |
| 1.2 | [The token you keep while you fetch a photocopy](parts/01-two-ways-to-stop/1.2-the-token-you-keep-while-you-fetch-a-photocopy.md) | There is no `pause()`. What actually makes an invocation pause? | foundation |
| 1.3 | [Bring the cloth or bring the receipt](parts/01-two-ways-to-stop/1.3-bring-the-cloth-or-bring-the-receipt.md) | A start and a resume are one method. What happens when you pass neither? | working |

### Section 2 — `02-inside-the-box`

*The checkpoint as an object on disk: what is in it, what is not, and how often to write one.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [Two people writing in one notebook](parts/02-inside-the-box/2.1-two-people-writing-in-one-notebook.md) | Two different records share `agent_state`. Who writes each? | working |
| 2.2 | [Opening the fuse box](parts/02-inside-the-box/2.2-opening-the-fuse-box.md) | What does the graph's checkpoint actually contain? | working |
| 2.3 | [The recipe and the pan](parts/02-inside-the-box/2.3-the-recipe-and-the-pan.md) | What can a checkpoint structurally *not* hold? | working |
| 2.4 | [How often you press save](parts/02-inside-the-box/2.4-how-often-you-press-save.md) | Storage against redone work — which side decides? | production |

### Section 3 — `03-the-agents-own-note`

*ADK-45's real subject: a custom agent's own checkpoint. It works, it fails, and the repair has two
halves.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [The mark on the doorframe](parts/03-the-agents-own-note/3.1-the-mark-on-the-doorframe.md) | How does an agent keep progress inside one node? | working |
| 3.2 | [A blank page and no page at all](parts/03-the-agents-own-note/3.2-a-blank-page-and-no-page-at-all.md) | `None` or an empty object — why is the difference load-bearing? | working |
| 3.3 | [The rough column nobody marks](parts/03-the-agents-own-note/3.3-the-rough-column-nobody-marks.md) | 💥 Six checkpoints written, none read back. Why? | production |
| 3.4 | [Write it on the shared board](parts/03-the-agents-own-note/3.4-write-it-on-the-shared-board.md) | 💥 The repair, and the half of it that reports success while losing work | production |
| 3.5 | [Handing back the key](parts/03-the-agents-own-note/3.5-handing-back-the-key.md) | 💥 `end_of_agent=True` clears the note. What does a second resume do? | production |

### Section 4 — `04-the-drill`

*The whole thing end to end: baseline, a real kill, a pickup in a fresh process, and the switch
everybody forgets.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [The monthly generator test](parts/04-the-drill/4.1-the-monthly-generator-test.md) | What are the known-good numbers to read every later run against? | working |
| 4.2 | [Pulling the plug mid-cycle](parts/04-the-drill/4.2-pulling-the-plug-mid-cycle.md) | 💥 What does a real kill leave behind, and why not `sys.exit`? | working |
| 4.3 | [The mason who comes back in the morning](parts/04-the-drill/4.3-the-mason-who-comes-back-in-the-morning.md) | Three nodes, three fates on resume — and what got redone | working |
| 4.4 | [Written on the back of your hand](parts/04-the-drill/4.4-written-on-the-back-of-your-hand.md) | 💥 `is_resumable` is set and the run is unreachable. What is missing? | production |

### Section 5 — `05-failure-lab`

*Three ways this breaks, each measured with a control so the cause is proved rather than guessed.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [Two clerks checking one delivery](parts/05-failure-lab/5.1-two-clerks-checking-one-delivery.md) | 💥 Two checkpoint classes, two `extra` policies. Which drift is caught? | production |
| 5.2 | [Marked present by default](parts/05-failure-lab/5.2-marked-present-by-default.md) | 💥 ADK invents a checkpoint nobody wrote. When, and what does it break? | production |
| 5.3 | [The clerk who wrote REJECTED in pen](parts/05-failure-lab/5.3-the-clerk-who-wrote-rejected-in-pen.md) | 💥 Why is a politely-failed run harder to resume than a destroyed one? | production |

### Section 6 — `06-in-production`

*What this costs in things that are not bytes.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 6.1 | [The batch number on the strip](parts/06-in-production/6.1-the-batch-number-on-the-strip.md) | The drift no validator can catch, and what a version stamp really does | production |
| 6.2 | [The photocopy in the drawer](parts/06-in-production/6.2-the-photocopy-in-the-drawer.md) | Durability made a second copy of the customer's words. Now what? | production |

There is no `papers/` directory today. The two ideas this day leans on are taught already: the
checkpoint-interval trade-off in Day 47's
[transaction-oriented recovery](../day-47-persistent-sessions/papers/01-transaction-oriented-recovery.md),
cited by 2.4, and the recorded-global-state idea in Day 60's
[distributed snapshots](../day-60-durable-execution/papers/01-distributed-snapshots.md), cited by 4.3.

---

## §3 Setup — run this

No package is added today. `google-adk` is already pinned at `2.7.1` in `pyproject.toml`, and
`docs/PACKAGES.md` carries its row.

```bash
cd days/day-61-pause-resume-checkpoints
mkdir -p lab
cd lab
git diff ../../../pyproject.toml ../../../uv.lock   # must stay empty all day
```

The lab holds **26 Python files**: four shared helpers and twenty-two scripts the parts run.

| file | what it is | first used by |
| --- | --- | --- |
| `_store.py` | `FileSessionService` — `InMemorySessionService` flushed to JSON after every event | everything |
| `_drill.py` | the three-station drill: `summarise`, `dedupe` (a custom agent), `report` | everything |
| `_run.py` | `start`, `resume`, `fresh` — the two calls of [1.3](parts/01-two-ways-to-stop/1.3-bring-the-cloth-or-bring-the-receipt.md) | everything |
| `_chain.py` | a bare three-node chain, no custom agent, for 5.3's controlled experiment | 5.3 |
| `twostops.py` `pausepoint.py` `handle.py` | section 1 | 1.1–1.3 |
| `layers.py` `box.py` `notinbox.py` `locals.py` `often.py` | section 2 | 2.1–2.4 |
| `pen.py` `none.py` `instead.py` `endof.py` | section 3 | 3.1–3.5 |
| `drill.py` `kill.py` `pickup.py` `storage.py` | section 4 | 4.1–4.4 |
| `drift.py` `ghost.py` `polite.py` | section 5 | 5.1–5.3 |
| `stamp.py` `leaks.py` | section 6 | 6.1–6.2 |
| `gate.py` | the eval | §5 |

Then create the file today's build brief asks for, empty:

```bash
touch ../../../sutra/checkpoints.py
```

**A note on `_store.py`.** Day 47 decided not to install SQLAlchemy, and that stands — so
`DatabaseSessionService` raises `ImportError` in this repo. The lab's thirty-line file-backed service
exists because a day about reading checkpoints needs a store you can `cat`.
[4.4](parts/04-the-drill/4.4-written-on-the-back-of-your-hand.md) states that openly rather than
letting the helper pass as the real thing.

---

## §4 Build brief

Write `sutra/checkpoints.py`: the drill's scoring station, done properly, with everything this day
measured folded in.

```python
# sutra/checkpoints.py
"""A resumable list-processing station for the triage graph."""


class DedupeState(BaseAgentState):
    """TODO(me): the fields this station needs to survive a kill.

    Include a schema_version whose default is a value no real checkpoint would carry
    (part 6.1), and think about a cursor rather than an accumulator (part 2.4).
    """


class Dedupe(BaseAgent):
    """TODO(me): the station.

    - Load on entry and branch on `is None` explicitly, not with `or` (part 3.2).
    - Skip already-done items before doing any work (part 3.1).
    - Write the result before claiming the item as done (part 2.4).
    - set_agent_state AND yield the state event — setting alone writes nothing (part 3.1).
    - Set end_of_agent=True when the list finishes (part 3.5).
    - Check the schema_version and refuse rather than resume on a mismatch (part 6.1).
    """
```

**TODO(me), in order:**

1. **Decide where the progress lives.** [3.3](parts/03-the-agents-own-note/3.3-the-rough-column-nobody-marks.md)
   measured that an agent's own state is not restored inside a graph, and
   [3.4](parts/03-the-agents-own-note/3.4-write-it-on-the-shared-board.md) measured the two-part
   repair. Sutra's stations are nodes. Write down which mechanism you are using and why, in a
   comment, before writing the class.
2. **Namespace the session-state key** by the station's name, so two stations cannot collide
   ([3.4](parts/03-the-agents-own-note/3.4-write-it-on-the-shared-board.md)'s *When it breaks*).
3. **Set `rerun_on_resume`** on the node, with a comment saying it is a correctness setting and not a
   performance one — and note what it costs on a duplicate resume
   ([3.5](parts/03-the-agents-own-note/3.5-handing-back-the-key.md)).
4. **Stamp the schema version** and compare with `!=`, not `<`
   ([6.1](parts/06-in-production/6.1-the-batch-number-on-the-strip.md)).
5. **Apply the four questions** to every field before you put it in
   ([6.2](parts/06-in-production/6.2-the-photocopy-in-the-drawer.md)). Store an id where an id will
   do.
6. **Write `tests/test_checkpoints.py`** with the only test that catches
   [3.3](parts/03-the-agents-own-note/3.3-the-rough-column-nobody-marks.md): kill the run, resume it,
   and assert the second attempt does **less** work than the first. A structural test will not.

Do not copy `_drill.py`. It is a teaching fixture with `kill_after` and print statements in it.

---

## §5 The eval that must be able to fail

`lab/gate.py` checks six things about `sutra/checkpoints.py`, each naming the part that tells you
what to build. It is red now.

```bash
cd days/day-61-pause-resume-checkpoints/lab
uv run python gate.py; echo "exit: $?"
```

```text
  [FAIL] checkpoints.py exists                        see part 3.1
  [FAIL] DedupeState subclasses BaseAgentState        see part 3.1
  [FAIL] the None branch is handled                   see part 3.2
  [FAIL] already-done items are skipped on entry      see part 3.3
  [FAIL] end_of_agent is set when the list finishes   see part 3.5
  [FAIL] a schema_version is stamped and checked      see part 6.1

  0/6 checks pass
exit: 1
```

Six red, exit 1. It goes green as you write the file — and then **break it on purpose**: delete the
`end_of_agent` call, watch check five go red, put it back.

`gate.py` is a structural check and it cannot see
[3.3](parts/03-the-agents-own-note/3.3-the-rough-column-nobody-marks.md)'s bug — a station can pass
all six and still restart its list on every resume. That is the point of build-brief item 6, and it
is why the kill-and-count test is the one that matters.

---

## §6 Request budget

**Zero.** No provider is called today, by any script, at any point.

| provider | requests today | RPM/RPD used |
| --- | --- | --- |
| Gemini (AI Studio free tier) | 0 | 0 / 0 |
| Groq | 0 | 0 / 0 |
| OpenRouter (`:free`) | 0 | 0 / 0 |
| Ollama (local) | 0 | n/a |

The drill's scoring is `len(set(a.split()) & set(b.split()))` — set intersection over two strings. No
model is constructed, no key is read, nothing opens a socket. That is deliberate:
[2.4](parts/02-inside-the-box/2.4-how-often-you-press-save.md)'s argument is that checkpoint cadence
is decided by what an item costs, and the honest way to make that argument is with an item that costs
nothing and then say what changes when it costs a request.

---

## §7 Traps

1. **Looking for `runner.pause()`.** There is none. `dir(Runner)` filtered for pause, suspend and
   stop returns `[]`. A pause is a *consequence* of an unanswered long-running function call
   ([1.2](parts/01-two-ways-to-stop/1.2-the-token-you-keep-while-you-fetch-a-photocopy.md)).
2. **Assuming a written checkpoint is a read checkpoint.** Six in the log, none restored, no error
   ([3.3](parts/03-the-agents-own-note/3.3-the-rough-column-nobody-marks.md)). Only a behavioural
   test catches it.
3. **Stopping at half the repair.** Progress in session state survives *and* the node is skipped, so
   the run finishes with half its list done and exit code 0
   ([3.4](parts/03-the-agents-own-note/3.4-write-it-on-the-shared-board.md)).
4. **`set_agent_state` without a yield.** It returns `None` and writes nothing; the event carries the
   state ([3.1](parts/03-the-agents-own-note/3.1-the-mark-on-the-doorframe.md)). This is plan §5.1
   **trap #3** — yield as you go, do not collect and return.
5. **Swallowing the exception to keep a run resumable.** Plan §5.1 **trap #4**. It converts a loud
   refusal into a quiet wrong answer
   ([5.3](parts/05-failure-lab/5.3-the-clerk-who-wrote-rejected-in-pen.md)).
6. **Testing durability with `sys.exit` or an exception.** Both let `finally` blocks and buffer
   flushes run. `os._exit` runs nothing
   ([4.2](parts/04-the-drill/4.2-pulling-the-plug-mid-cycle.md)).
7. **Testing a resume inside one process.** It passes with an in-memory service and proves nothing
   ([4.4](parts/04-the-drill/4.4-written-on-the-back-of-your-hand.md)).
8. **Comparing a resumed run's event count against the clean baseline.** The resumed store holds
   both attempts — 19 against 15 is correct, not a leak
   ([4.1](parts/04-the-drill/4.1-the-monthly-generator-test.md),
   [4.3](parts/04-the-drill/4.3-the-mason-who-comes-back-in-the-morning.md)).
9. **`mcp==1.29.1` still has no row in `docs/PACKAGES.md`.** Day 52's gate found it, Day 59's gate
   found it again. Not this day's to fix, and worth not being surprised by.

---

## §8 Verify before you code

Fetched on **2026-09-06**:

- **<https://adk.dev/runtime/resume/>** — the resume API, the *"at least once"* guarantee, and the
  instruction that custom agents *"generate and save the agent state for each completed step"* with
  *"an `end_of_agent=True` status upon successful completion"*.
- **<https://adk.dev/graphs/dynamic/>** — `rerun_on_resume`: true means *"the node body re-runs from
  the top"*, false means *"the resume payload is routed to the node's successor as input, bypassing
  the interrupted node"*.

Every symbol was **also** introspected against the installed `google-adk==2.7.1` — `NodeStatus`,
`NodeState`, `BaseAgentState`, `InvocationContext.set_agent_state`, `BaseAgent._load_agent_state`,
`InvocationContext.populate_invocation_agent_states` and `Runner.run_async` — because on four points
the docs and the package do not line up, and the day teaches the package:

1. **The docs describe the custom-agent checkpoint pattern without saying where the agent must sit.**
   Measured, it is read back when the agent is the App's root and **not** when it is a node inside a
   `Workflow` ([3.3](parts/03-the-agents-own-note/3.3-the-rough-column-nobody-marks.md)). This is the
   day's central finding and it is not in any page.
2. **`rerunOnResume` in the docs is `rerun_on_resume` in the installed Python.** Day 60 recorded this
   first; it still holds.
3. **`Runner.run_async`'s docstring promises `ValueError` when neither `new_message` nor
   `invocation_id` is given.** That guard sits on the legacy `BaseAgent` path. A `Workflow` root is a
   `BaseNode` that is not a `BaseAgent`, branches earlier, and produces a pydantic `ValidationError`
   about a string instead ([1.3](parts/01-two-ways-to-stop/1.3-bring-the-cloth-or-bring-the-receipt.md)).
   Both behaviours are real; the missing information is which root shape you have.
4. **An unknown invocation id is not rejected as unknown.** No not-found error; the run proceeds and
   fails downstream ([1.3](parts/01-two-ways-to-stop/1.3-bring-the-cloth-or-bring-the-receipt.md)),
   and it still appends events to the session
   ([4.3](parts/04-the-drill/4.3-the-mason-who-comes-back-in-the-morning.md)).

Plan §5 names `google-adk` 2.6.3 as the baseline; this repo pins **2.7.1**, which is what everything
above was measured against.

---

## §9 Say it in an interview

"Durability in ADK is two mechanisms sharing one field, and I learned the difference the hard way.
The graph keeps a map of node statuses — completed, running, or absent if it never started — and that
one works: I killed a run mid-list and the resuming process skipped the finished station, re-entered
the one that died and ran the last one for the first time. The second mechanism is a custom agent's
own state object, and that is where it got interesting. As the App's root agent it round-trips
perfectly; killed after two of four items, the resume loaded them and skipped them. The identical
class as a node inside a workflow gets an empty `agent_states` dictionary and starts the list again —
while its six checkpoints sit in the log, including one written by the resuming process directly
underneath one with more progress in it. Nothing raises, and every structural check you could write
passes, so the only test that catches it is behavioural: kill it, resume it, assert the second
attempt does less work than the first. The repair turned out to have two halves too. Moving progress
into session state makes it survive, but ADK skips the node that was running when the process died,
so the state comes back and nobody reads it and the run finishes with half its work done and exit
code zero — which is worse than the original bug, because that one wasted effort and got the right
answer. You need `rerun_on_resume=True` as well. And the thing I would tell anybody building on this:
a run that failed politely enough to log an exception is harder to resume than one that was
destroyed. I stopped the same node both ways, got identical checkpoints, and only the destroyed one
came back — deleting the single error event from the other one's log made it resume cleanly."

---

## §10 Done when

`CHECKLIST.md` is fully ticked: every part read and its check-yourself run, `sutra/checkpoints.py`
written until `lab/gate.py` is green, the kill-and-count test written and seen to go red before it
goes green, and the request budget confirmed at zero.

Done is defined by understanding and green checks. Not by how much of it you got through in one
sitting.

---

## §11 Ledger & commit

**`docs/PROGRESS.md`** — append this row:

```text
| 61 | 2026-09-06 | ADK-44, ADK-45 | 21 | <hash> | ⚠️ |
```

**`docs/PACKAGES.md`** — no row. No package was added today; `git diff pyproject.toml uv.lock` is
empty.

**`docs/PAPERS.md`** — no row. No paper is taught today; 2.4 and 4.3 cite papers already taught on
Days 47 and 60 and link to those parts.

**`docs/SKILL_PROVENANCE.md`** — no row. No third-party skill is used today.

**Commit:**

```text
day 61: pause/resume and checkpoints in ADK — closes ADK-44, ADK-45
```
