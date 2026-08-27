---
day: 7
phase: 1
phase_name: "Foundations"
title: "Events & streaming — the record the runtime was keeping anyway"
ids: ["ADK-04", "ADK-05"]
principles: [1, 2, 4, 6, 8, 10, 11, 12, 13, 15, 16, 17, 18]
kind: lab
plan_version: "v2.2.1"
parts: 16
generated: "2026-08-27"
status: written
lab_scaffolded: false
commit: ""
---

# Day 7 — Events & streaming: the record the runtime was keeping anyway

> **Yesterday (Day 6):** you wrote the one thing ADK did not take — the instruction — turned it into
> a six-section handbook you can probe, and watched a cooperative model describe a search it never
> ran.
> **Today:** you stop reading the answer and start reading the run. `async for event in ...` has been
> in your code since Day 5 and today it stops being a formality: the event object, the four fields
> that identify it, the flag that says whether it has finished arriving, the contract that makes a
> custom agent *yield* rather than return, and the database on your disk that has been recording all
> of it since yesterday.
> **Tomorrow (Day 8):** sessions, runs and the in-memory services — the book the events go into, its
> three-part address, and what "in memory" costs you when the process ends.

---

## §1 Where we are

Somewhere in your house there is a parcel you are waiting for, and a page that tells you where it is.

`Picked up.` `Reached the sorting centre.` `Out for delivery.` Each line has a time next to it. Each
one appeared while you were not looking. Nobody ever deletes one, and nobody ever edits one — if the
parcel goes to the wrong city, the page does not quietly correct itself, it adds a new line saying so.

Now notice what you actually wanted from that page. You wanted one thing: **where is my parcel.** What
they gave you is a list of everything that has happened to it, and the answer to your question is
simply the last line.

They could have built the other page. One box, one sentence, updated in place. It would be easier to
read and it would answer your question just as well, right up to the first time something went wrong
— at which point it would tell you the parcel is delayed, and nothing else. No way to see where it
stopped, no way to see how long it sat there, no way to tell a slow route from a lost box.

The history costs more to keep and answers questions nobody thought to ask.

Your agent has been building exactly that page since Day 5, and you have been reading the last line
off it and throwing the rest away. Today you read the rest. And at the end of the day you point the
same reader at a database `adk web` has been quietly writing since yesterday, and read a conversation
you had with Sutra back out of your own disk — which is the moment debugging stops being "run it
again and see" and becomes "go and look".

There is a second half. Because the page updates *while you watch*, a reader can be shown each line
as it appears instead of waiting for the last one. That is streaming, and it is genuinely a smaller
idea than it sounds: the model already produces its answer one piece at a time, so the only question
is whether anybody gets to see the pieces. Nothing is faster. The waiting is different, and the
difference is the whole point.

---

## §2 The map

Sixteen parts in six sections, and no papers today — this day's subject is an SDK's own event model,
which is a tool rather than an idea with a citable origin, and the plan is explicit that a tool does
not get a paper invented for it (§17.4 row 6).

The day climbs `foundation → working → production`: section 1 is the object, section 2 is what
changes when it arrives in pieces, section 3 is the contract your own code has to honour, section 4
is the brakes, section 5 breaks the contract on purpose, and section 6 reads a run that already
happened.

### Section 1 — `01-the-event-object`: ADK-04, what an event is

The record itself: what it holds, which of its fields survived the 1.x → 2.x rename, and the three
questions its identifiers answer.

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [An event is a line in a ledger, not a message](parts/01-the-event-object/1.1-an-event-is-a-line-in-a-ledger.md) | Why does a framework hand you a history instead of an answer? | `foundation` |
| 1.2 | [The fields that were renamed](parts/01-the-event-object/1.2-the-fields-that-were-renamed.md) | Trap #2 — where do you go when the tutorial and the package disagree? | `working` |
| 1.3 | [`is_final_response()` is not "the last one"](parts/01-the-event-object/1.3-is-final-response-is-not-the-last-one.md) | Which events answer `True`, and why can there be several? | `working` |
| 1.4 | [The half of an event that is not text](parts/01-the-event-object/1.4-the-half-that-is-not-text.md) | An agent changes a stored value — who actually writes it? | `working` |
| 1.5 | [Which run, which agent, which branch](parts/01-the-event-object/1.5-which-run-which-agent-which-branch.md) | Four identifiers, four different questions — which one groups a turn? | `production` |

### Section 2 — `02-the-stream`: ADK-05, when the answer arrives in pieces

Why streaming exists, the flag that carries it, the duplicate it produces, and the rule that a piece
still arriving has changed nothing.

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [The number read out loud](parts/02-the-stream/2.1-the-number-read-out-loud.md) | Which latency number does streaming change, and which does it not? | `foundation` |
| 2.2 | [The `partial` flag](parts/02-the-stream/2.2-the-partial-flag.md) | Three values, not two — what does the third one mean? | `working` |
| 2.3 | [The board and the printed sheet](parts/02-the-stream/2.3-the-board-and-the-printed-sheet.md) | You receive the answer twice; ADK gives you three options and one of them is a trap | `working` |
| 2.4 | [A partial event changes nothing](parts/02-the-stream/2.4-nothing-is-credited-until-the-receipt.md) | What is left in the session when a stream dies halfway? | `production` |

### Section 3 — `03-the-yield-contract`: trap #3, and the window it opens

The generator contract, the dirty read it creates, and an emitter of your own that reports a failure
instead of dressing it up.

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [One paper at a time](parts/03-the-yield-contract/3.1-one-paper-at-a-time.md) | What do the four guarantees of yield-process-resume actually buy you? | `working` |
| 3.2 | [Saved is not submitted](parts/03-the-yield-contract/3.2-saved-is-not-submitted.md) | You can read the value — so why is it not kept? | `production` |
| 3.3 | [Your own emitter, including the bad reading](parts/03-the-yield-contract/3.3-your-own-emitter.md) | What does a swallowed error look like to the logger, the trace and the eval? | `working` |

### Section 4 — `04-the-brakes`: containment before capability

Sutra grows tools on Day 10. Principle 13 says the containment story arrives first.

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [The meter that cuts off](parts/04-the-brakes/4.1-the-meter-that-cuts-off.md) | Day 3's step budget, now a framework field — what does it count, and over what scope? | `production` |
| 4.2 | [The note the machine refuses](parts/04-the-brakes/4.2-the-note-the-machine-refuses.md) | Two objects, one library, opposite answers to a typo — and both are right | `working` |

### Section 5 — `05-failure-lab`: the deliberate failure

Trap #3, committed on purpose, twice, with the two different errors it produces (plan §17.7).

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [💥 The mechanic who billed at the end](parts/05-failure-lab/5.1-the-mechanic-who-billed-at-the-end.md) | Why does the session holding exactly one event make this the hardest bug of the week? | `production` |

### Section 6 — `06-reading-a-run`: the recording you already have

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 6.1 | [The camera you already installed](parts/06-reading-a-run/6.1-the-camera-you-already-installed.md) | Yesterday's conversations are on your disk — what is in them, and what does that oblige you to do? | `production` |

---

## §3 Setup — run this

**No new packages today.** Day 5's `google-adk` 2.7.1 carries the whole day. `aiosqlite`, which part
6.1 leans on, is already a base dependency of `google-adk` rather than an extra — confirm rather than
assume:

```bash
# 1 - confirm where you are starting from
./m check
uv run python -c "import google.adk, aiosqlite; print(google.adk.__version__, aiosqlite.__version__)"

# 2 - the lab scratchpad for today
mkdir -p days/day-07-events-and-streaming/lab
cd days/day-07-events-and-streaming/lab
touch first_event.py fields.py two_spellings.py finality.py actions.py
touch felt_time.py count_chunks.py partial_changes_nothing.py
touch yielding.py dirty_read.py emitter.py
touch brakes.py counter.py strictness.py
touch collecting_a.py collecting_b.py replay.py
cd -

# 3 - the two new files under sutra/ and the one new test file
touch sutra/desk/events.py sutra/desk/stream.py
touch tests/test_events.py

# 4 - check the recording from yesterday is there and is ignored
ls -la sutra/desk/.adk/
git check-ignore -v sutra/desk/.adk/session.db
```

**Write `sutra/desk/events.py` first**, before any of the lab scripts. Part 1.5 gives it whole, six
of today's lab scripts import it, and it costs nothing to run. Everything today is easier once one
event fits on one line.

**Three files under `sutra/` change today** — `events.py` and `stream.py` are new, and `run_once.py`
loses one placeholder line. Nothing else: `sutra/loop.py`, `sutra/agent.py`, `sutra/config.py` and
`sutra/desk/agent.py` are untouched, and `sutra/desk/agent.py` in particular still carries yesterday's
handbook exactly as you left it.

---

## §4 Build brief

**`sutra/desk/events.py`** — new, and the most reused thing you write this week:

| Symbol | What it does | Taught in |
| --- | --- | --- |
| `text_of(event)` | the event's text, or `None` when it carries something that is not text | 1.1, 1.5 |
| `kind_of(event)` | the kind, derived from the content — there is no `type` field | 1.2, 1.5 |
| `describe(event)` | one readable line: run id, author, kind, finality, body | 1.5 |

**`sutra/desk/stream.py`** — new. `stream_once(question)` with
`RunConfig(streaming_mode=StreamingMode.SSE)`, printing chunks as they arrive and keeping the
aggregate; plus `is_displayable_chunk(event)`, the filter that survives Day 10 (2.2, 2.3).

**`sutra/desk/run_once.py`** — one line changes. The placeholder
`print(f"[event] {type(event).__name__}")`, which prints `Event` every time and therefore says
nothing, becomes `print(describe(event))` (1.5).

**`days/day-07-events-and-streaming/lab/`** — seventeen small scripts, each given whole in the part
that needs it. Fifteen of them cost **zero requests**.

**`tests/test_events.py`** — the structural suite. See §5.

**`TODO(me)` markers left for you:**

- **1.5** — `kind_of` has a gap, and part 6.1 makes you find it with real data: two of your own
  stored events came back labelled `other` with an empty body. Work out what they are, and decide
  whether `kind_of` should name them or whether `other` is the honest answer.
- **3.3** — `describe` does not show `error_code`, so an error event is indistinguishable from an
  empty one on a trace line. Add it, and decide where in the line it goes without pushing the body
  off the screen.
- **1.3 / 4.1** — `sutra/desk/run_once.py` keeps only the **last** final response. Part 1.3 showed
  that is a decision, not a fact. Decide it deliberately and write down which you chose and why.
- **2.2** — paste your own `--trace` output into your notes, from your own run. This document
  deliberately prints none: a fabricated transcript in a day about reading real ones would be the
  exact failure it teaches.
- **6.1** — `lab/replay.py` prints every session in the database. Give it a session id argument, as
  the review comment in 6.1 asks for, and say in one line why that matters more than convenience.

---

## §5 The eval that must be able to fail

Every assertion below runs on **hand-built events**. No runner, no model, no key, no quota — which is
the point rather than a saving: the behaviours that break in streaming are precisely the ones you
want to test often, and a test that costs a request gets run rarely.

```python
# tests/test_events.py
import inspect

from google.adk.events import Event, EventActions
from google.genai import types

from sutra.desk.events import describe, kind_of, text_of


def spoke(text: str, **kwargs) -> Event:
    """A plain text event from the agent."""
    return Event(
        author="sutra_desk",
        invocation_id="run-1",
        content=types.Content(role="model", parts=[types.Part(text=text)]),
        **kwargs,
    )


def test_a_partial_event_is_never_final() -> None:
    """2.2: a chunk is not an answer, whatever it contains."""
    assert spoke("Ticket 45", partial=True).is_final_response() is False


def test_a_chunk_is_labelled_a_chunk() -> None:
    """1.5: kind_of checks partial before it checks text, and order decides this."""
    assert kind_of(spoke("Ticket 45", partial=True)) == "chunk"


def test_a_state_only_event_has_no_text() -> None:
    """1.1: text_of returns None, never an empty string, for an event that said nothing."""
    bookkeeping = Event(
        author="sutra_desk",
        invocation_id="run-1",
        actions=EventActions(state_delta={"ticket_id": "4521"}),
    )
    assert text_of(bookkeeping) is None
    assert kind_of(bookkeeping) == "state"


def test_describe_survives_an_event_with_no_content() -> None:
    """1.5: the trace line must never be the thing that crashes the trace."""
    assert "sutra_desk" in describe(Event(author="sutra_desk", invocation_id="run-1"))


def test_the_streaming_entry_point_is_a_coroutine_function() -> None:
    """5.1: the isasyncgenfunction check, pointed at the file it protects."""
    from sutra.desk.stream import stream_once

    assert inspect.iscoroutinefunction(stream_once)


# TODO(me): the sixth test - a tool-call event must never be labelled "text" (1.5, 2.3).
```

**How to watch each one go RED before it goes green:**

```bash
uv run python -m pytest tests/test_events.py -q -m "not live"   # RED: sutra/desk/events.py is empty
# ... write text_of, kind_of and describe from part 1.5 ...
uv run python -m pytest tests/test_events.py -q -m "not live"   # green
```

Then break each one on purpose:

- In `kind_of`, move the `if event.partial` check **below** the text check, and watch
  `test_a_chunk_is_labelled_a_chunk` go red. That is 1.5's ordering argument, proved rather than
  asserted.
- In `text_of`, change `return joined or None` to `return joined`, and watch
  `test_a_state_only_event_has_no_text` go red on the difference between "no text" and "empty text".
- Delete the `if not event.content` guard in `text_of` and watch
  `test_describe_survives_an_event_with_no_content` fail with the `AttributeError` from part 1.1 —
  the one you will otherwise meet for the first time on Day 10, inside a loop you have already paid
  for.
- Break `stream_once` the way section 5 breaks a custom agent — remove `async` — and watch the last
  test go red before anything tries to run it.

---

## §6 Request budget

**Free-tier Gemini only**, 20 requests per day (`docs/PACKAGES.md`, 2026-08-25). Today is the
cheapest day since Day 1, because almost everything about events can be studied on events you build
yourself.

| What | Model calls |
| --- | --- |
| all of section 1 · 2.1 · 2.4 · all of section 3 · all of section 4 · 5.1 · 6.1 | **0** |
| 2.2 — one streamed question | 1 |
| 2.2 — the same question again with `--trace` | 1 |
| 2.3 — `count_chunks.py`, the short default question | 1 |
| 2.3 — `count_chunks.py` again with a question that forces a long answer | 1 |
| one message in `adk web`, to see the same events in the UI | 1 |
| **Total** | **5** |

**Do the free things first**, and this is not frugality — it is sequencing. Fifteen of the seventeen
lab scripts need no key at all, and every one of them teaches something you would otherwise try to
learn by staring at a streamed answer. In particular, run `lab/replay.py` (6.1) **before** you spend
anything: it reads yesterday's conversations off your disk, and reading a run you already paid for is
strictly better than buying a new one.

**If you run out**, the day does not stop. Only 2.2 and 2.3 need quota at all, and both are about
watching a shape you can already describe. Read the stored runs instead and do the streaming pair
tomorrow.

**Cost: $0.**

---

## §7 Traps

- **Trap #2 — the event fields were renamed in 2.0.** Every event-handling snippet you find is
  probably 1.x. There is no `type` field and never will be; the kind of an event is derived from its
  content. Check `Event.model_fields` on the version you have installed, not a page. (1.2)
- **Trap #3 — yield, don't append.** A custom agent that collects events into a list and returns them
  fails two different ways: `SyntaxError: 'return' with value in async generator` if you left a
  `yield` in, and `AttributeError: 'coroutine' object has no attribute 'aclose'` if you did not. The
  second leaves **one** event in the session — the user's message — which reads as "the agent said
  nothing" and sends you looking at the model. (3.1, 5.1)
- **`is_final_response()` is not "the last event."** Several events per run can answer `True`, one
  per agent in a multi-agent run, and an empty state-change event answers `True` too. Never `break`
  on it: breaking abandons a frozen generator and silently drops everything the runtime had left to
  commit. (1.3)
- **Forgetting the parentheses.** `if event.is_final_response:` is always true — a bound method is
  truthy — and produces no error at all. Every event prints, and you conclude streaming is broken.
  (1.1, 1.3)
- **`event.partial` is three-valued.** `None` = never streamed, `True` = a chunk, `False` = the
  assembled version. `elif not event.partial` matches two of the three and is the duplicate-printing
  bug. Write `is False`. (2.2)
- **You receive the answer twice on a streaming run.** Chunks *and* one aggregated event, by design,
  because the aggregate is the only one that gets committed. Pick a rule — chunks for a human,
  aggregate for a batch — and never deduplicate by comparing strings. (2.3, 2.4)
- **Partial function-call arguments stream too.** A filter that only checks `partial` will print
  half-built JSON into a chat window from Day 10 onward. Check `get_function_calls()` as well. (2.3)
- **A partial event changes nothing.** Not appended, no `state_delta` applied. A stream that dies
  halfway leaves no record of itself, so a retry looks like a first attempt. (2.4)
- **`RunConfig` belongs to the call, not the runner.** `runner.run_config = ...` attaches a new
  attribute to an ordinary Python object, silently, and nothing streams. Pass it to `run_async`.
  (2.2, 4.2)
- **A change you can read is not a change that was kept.** State written but not yet carried by a
  yielded event is a dirty read: visible to the rest of the run, gone if the run dies. And a failed
  run is **not** rolled back — it leaves the prefix it already committed. (3.2)
- **`max_llm_calls` defaults to 500 and turns off at 0**, with nothing but a log warning. It counts
  model calls per run, which is a blast-radius brake and not a daily budget. Hitting it means read
  the events, not raise the number. (4.1)
- **`RunConfig` forbids unknown keys and `Event` ignores them.** One typo stops you at the door and
  the other vanishes. Check `Model.model_config` on anything you configure, and read the field back
  when it is permissive. (4.2)
- **`SqliteSessionService` is not exported from `google.adk.sessions`.** Import it from
  `google.adk.sessions.sqlite_session_service`; Python's "Did you mean: 'BaseSessionService'?"
  suggestion points at an abstract class. (6.1)
- **`adk web` stored your sessions under `app_name='sutra.desk'`**, not `'sutra'`. Your own runner
  uses `'sutra'`. Same store, different name, and a session is found by name — which is tomorrow's
  failure lab. (6.1)

---

## §8 Verify before you code

Every source below was checked on **2026-08-26** while this day was written. Principle 8: re-check on
the day you use them. This table is evidence, not a substitute.

| Source | What it settled |
| --- | --- |
| `adk.dev/events/` | An event "captures user messages, agent replies, requests to use tools (function calls), tool results, state changes, control signals, and errors"; the field list (`author`, `invocation_id`, `id`, `timestamp`, `content`, `partial`, `actions`, `branch`); `is_final_response()` as the helper to filter on rather than reimplement; `state_delta` / `artifact_delta` / `transfer_to_agent` / `escalate` / `skip_summarization` on `actions`; the append flow through `SessionService` |
| `adk.dev/runtime/event-loop/` | The yield-process-resume cycle, quoted in 3.1; the dirty-read paragraph quoted in 3.2; "Streaming events: Marked `partial=True`; Runner forwards them upstream immediately but **skips processing `actions`**" |
| `adk.dev/runtime/runconfig/` | `streaming_mode` defaults to `StreamingMode.NONE`; `max_llm_calls` defaults to 500; "Set to 0 or negative for unlimited (not recommended for production)"; values ≥ `sys.maxsize` raise |
| the installed `google-adk` 2.7.1 | `Event.model_fields` (34 fields) and `EventActions.model_fields` (13), pasted in 1.2 · `Event`'s `extra='ignore'` against `RunConfig`'s `extra='forbid'` · `BaseSessionService.append_event`'s `if event.partial: return event` · `StreamingMode`'s SSE docstring including the "Duplicate text issue" and its three options · `LlmCallsLimitExceededError` and the increment-then-check order · `SqliteSessionService`'s absence from `google.adk.sessions.__all__` · `aiosqlite` as a base dependency, not an extra |

**Five claims in this day that no page states**, established by running code rather than by reading.
Re-run them; if your version disagrees, **your terminal wins** and you fix the document:

```bash
uv run python days/day-07-events-and-streaming/lab/partial_changes_nothing.py   # 2.4
uv run python days/day-07-events-and-streaming/lab/yielding.py                  # 3.1
uv run python days/day-07-events-and-streaming/lab/collecting_b.py              # 5.1
uv run python days/day-07-events-and-streaming/lab/strictness.py               # 4.2
uv run python days/day-07-events-and-streaming/lab/replay.py sutra/desk/.adk/session.db  # 6.1
```

That is Principle 8 working rather than failing: a partial event that leaves no trace is real whether
or not a page mentions it, and the way you find out is to append one and count.

---

## §9 Say it in an interview

> "The thing that clicked for me about agent frameworks is that they don't return an answer, they
> hand you a stream of events, and the answer is just the last useful one. Once you see that, a lot
> of things stop being separate features. Tracing, streaming, resuming a killed run, a UI that shows
> tool calls — they're all reading the same record, and none of them needs the agent to cooperate.
> The two things I'd want a team to know are both about the shape of that stream. First,
> `is_final_response` doesn't mean 'the last event' — it means 'complete enough to show a person',
> and there can be several per run, so breaking out of the loop on the first one abandons the
> generator and drops whatever the runtime still had to commit. Second, when you turn streaming on
> you get the answer twice: the chunks, and a final aggregated event. That looks like a bug and it
> isn't — the partials are never persisted, so the aggregated one is the only thing that reaches
> storage. Which also means a stream that dies halfway leaves no record at all, so a client retry
> looks like a first attempt, and that's an idempotency problem rather than a display problem. The
> bug that cost me the most was a custom agent that collected its events and returned a list instead
> of yielding them — it fails inside the framework with an `AttributeError` about `aclose`, and the
> session still contains one event because the runtime appends the user's message before calling the
> agent. So the symptom is 'the agent answered nothing' and you go and check your API key. The
> diagnostic is one line of `inspect`, and it's in our test suite now."

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked — honestly. `./m done 7` refuses to commit while
any box is unticked, and it cannot tell whether you were truthful. That part is yours.

The day is finished when `sutra/desk/events.py` turns any event into one line you can read at a
glance; when `sutra/desk/stream.py` prints a streamed answer once rather than twice and you can say
which of ADK's three options you took and why; when you have watched a custom agent yield and seen
your loop print an event *before* the agent's next line ran; when you have broken that agent both
ways and can name the keyword that decides which error you get; when you have appended a partial
event and counted zero; when you can say what `max_llm_calls` counts and over what scope; when
`tests/test_events.py` has gone red and green for each of its assertions and you have written the
sixth; and when you have read a conversation from yesterday out of `sutra/desk/.adk/session.db` and
then confirmed, again, that the file is not going to GitHub.

---

## §11 Ledger & commit

Paste these **with the values you actually observed** (Principle 7), not the ones printed here.

**`docs/PROGRESS.md`** — append one row:

```text
| 7 | <date> | ADK-04, ADK-05 | 16 | <hash> | ✅ |
```

**`docs/PACKAGES.md`** — **no new rows.** Nothing was installed today. `aiosqlite` 0.22.1 is present
because `google-adk` 2.7.1 requires it (`Requires-Dist: aiosqlite>=0.21`, no extra), so it is not a
Sutra pin and does not get a row of its own. If your own `uv run python -c "import aiosqlite;
print(aiosqlite.__version__)"` disagrees, that is not a row either — it is a note in your lab README,
because the version is chosen by ADK and not by you.

**`docs/PAPERS.md`** — no rows. Today's subject is a framework's event model, which is a tool rather
than an idea with a citable origin document, and §17.4 row 6 is explicit that a tool does not get a
paper invented for it.

**`docs/SKILL_PROVENANCE.md`** — no rows. First entries arrive on Day 29.

**`docs/adr/`** — no new ADR. Today adopts nothing the plan has not already prescribed. **If your ADK
version has moved `partial`, renamed `is_final_response`, or changed what `append_event` does with a
partial event, stop and re-read Principle 14 before editing anything** — that is an ecosystem change,
and the plan is amended first.

**Commit message:**

```text
day 07: events & streaming - the record the runtime was keeping anyway - closes ADK-04, ADK-05
```
