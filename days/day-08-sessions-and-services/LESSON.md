---
day: 8
phase: 1
phase_name: "Foundations"
title: "Sessions, runs & in-memory services — the conversation gets an address"
ids: ["ADK-06", "ADK-07"]
principles: [1, 2, 4, 6, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18]
kind: lab
plan_version: "v2.2.1"
parts: 16
generated: "2026-08-27"
status: written
lab_scaffolded: false
commit: ""
---

# Day 8 — Sessions, runs & in-memory services: the conversation gets an address

> **Yesterday (Day 7):** you stopped reading the answer and started reading the run. The event, its
> identifiers, the `partial` flag, the yield contract, and a database on your disk with your own
> conversations in it.
> **Today:** the book those events go into. A session has six fields and a three-part address; a run
> is what happens between one message and the agent being done; and the four services underneath are
> interfaces with throwaway implementations — which is why everything you build today survives
> exactly as long as the process does.
> **Tomorrow (Day 9):** the same agent pointed at four free providers — Gemini, Groq, OpenRouter and
> a model running on your own machine — and the first honest benchmark table of the project.

---

## §1 Where we are

Think about a library. Not a big one — the sort with one room, one librarian and a card index.

You want a book. She finds your card, sees you have two out already, writes the new one on the card,
stamps a date, and hands it over. Thirty seconds. And in those thirty seconds, four completely
different things happened, all of which you would have called "the library" a moment earlier.

There is **your card** — one per member, with your name and a number on it. That is a session: a
conversation with an address, and the address is how she found it among four hundred others.

There are **the shelves**, where the books actually are. That is a service: a place things live,
which she talks to through a fixed set of moves — find, take, put back — and which could be shelves,
or a stockroom, or a second building, without changing how she asks.

There is **this visit**: come in, ask, get the book, leave. That is a run. It happens inside your
membership and does not end it.

And there is **the card index**, which is what makes the whole thing possible and which nobody
thanks. Lose the shelves and you have lost some books. Lose the index and you have lost the library,
because a room full of books nobody can find is a room full of books.

Now the part of the story that is actually today's subject.

Imagine a librarian who keeps all of it in her head. No cards, no index, just an extremely good
memory. It works, and it works well, right up to the evening she goes home — and the next morning
every member is a new member.

That is `InMemorySessionService`. It is not a bad librarian. It is a librarian with no cards, and
everything today builds is exactly as durable as the process it runs in. The point of the day is not
to be disappointed by that. It is to know precisely which of the four things above you have, which
you do not, and what changes on Day 86 when you get the rest.

---

## §2 The map

Sixteen parts in five sections, and no papers today — this day's subject is a framework's storage
model, which is a tool rather than an idea with a citable origin, and §17.4 row 6 is explicit that a
tool does not get a paper invented for it.

The day climbs `foundation → working → production`: section 1 is the session, section 2 is the run
inside it, section 3 is the four services underneath, section 4 is what "in memory" costs, and
section 5 breaks the address on purpose.

### Section 1 — `01-the-session`: ADK-06, the conversation as an object

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [A conversation with an address](parts/01-the-session/1.1-a-conversation-with-an-address.md) | Six fields — which are the address and which are the contents? | `foundation` |
| 1.2 | [Three parts to one key](parts/01-the-session/1.2-three-parts-to-one-key.md) | Get one of three wrong and you get `None` — why is that right, and what do you do about it? | `working` |
| 1.3 | [The register and the key board](parts/01-the-session/1.3-the-register-and-the-key-board.md) | One question decides whether something is an event or a state value | `working` |
| 1.4 | [Minted, or chosen](parts/01-the-session/1.4-minted-or-chosen.md) | Three good reasons to name a session yourself, and two not to | `working` |

### Section 2 — `02-the-run`: ADK-06, what happens between one message and the next

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [One dish from one recipe](parts/02-the-run/2.1-one-dish-from-one-recipe.md) | Run, turn, session — which has an address, and what groups the events of one run? | `foundation` |
| 2.2 | [The complaint book](parts/02-the-run/2.2-the-complaint-book.md) | Why does a session always have one more event than your loop counted? | `working` |
| 2.3 | [A journey and a pass](parts/02-the-run/2.3-a-journey-and-a-pass.md) | Nothing ends a session. What does that cost, and what does `GetSessionConfig` actually fix? | `production` |

### Section 3 — `03-the-services`: ADK-07, the four things underneath

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [The tap and the pipe](parts/03-the-services/3.1-the-tap-and-the-pipe.md) | What does the interface hide from your code, and what does it not hide from your operations? | `foundation` |
| 3.2 | [Three drawers deep](parts/03-the-services/3.2-three-drawers-deep.md) | Reads give you a copy and writes go by address — what breaks because of the second one? | `working` |
| 3.3 | [Ctrl+F is not understanding](parts/03-the-services/3.3-ctrl-f-is-not-understanding.md) | The free memory service matches words, not meaning — where exactly does that fail? | `working` |
| 3.4 | [The cloakroom, and the one you were not given](parts/03-the-services/3.4-the-cloakroom-and-the-one-you-were-not-given.md) | Which of the four services does a runner leave empty, and why is that a decision? | `working` |
| 3.5 | [The furnished flat](parts/03-the-services/3.5-the-furnished-flat.md) | One line gives you three services and an app name you never chose | `production` |

### Section 4 — `04-what-in-memory-means`: the cost, stated plainly

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [The tab you did not save](parts/04-what-in-memory-means/4.1-the-tab-you-did-not-save.md) | Four ordinary events end a process — how many of them are faults? | `production` |
| 4.2 | [Two counters, two notebooks](parts/04-what-in-memory-means/4.2-two-counters-two-notebooks.md) | Why is a second process a quieter failure than a restart? | `production` |
| 4.3 | [🅿️ The shop that bought a computer](parts/04-what-in-memory-means/4.3-the-shop-that-bought-a-computer.md) | The swap is one line — so what are the three things that are not? | `production` |

### Section 5 — `05-failure-lab`: the deliberate failure

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [💥 The name called in the waiting room](parts/05-failure-lab/5.1-the-name-called-in-the-waiting-room.md) | One mismatch, three symptoms — and only one of them looks like a problem | `production` |

---

## §3 Setup — run this

**No new packages today.** Day 5's `google-adk` 2.7.1 carries the whole day, and `aiosqlite` — which
sections 4 and 5 lean on — is already a base dependency of it rather than an extra.

```bash
# 1 - confirm where you are starting from
./m check
uv run python -c "import google.adk, aiosqlite; print(google.adk.__version__, aiosqlite.__version__)"

# 2 - the lab scratchpad for today
mkdir -p days/day-08-sessions-and-services/lab
cd days/day-08-sessions-and-services/lab
touch anatomy.py near_misses.py register_and_board.py ids.py
touch one_run.py off_by_one.py growth.py
touch interfaces.py drawers.py keyword_memory.py cloakroom.py no_credentials.py furnished.py
touch forgetful.py forgetful_sqlite.py split_brain.py three_stores.py mismatch.py
cd -

# 3 - the one new module under sutra/ and the one new test file
touch sutra/desk/sessions.py
touch tests/test_sessions.py

# 4 - confirm the lab's databases will never be committed
git check-ignore -v days/day-08-sessions-and-services/lab/anything.db
```

**Write `sutra/desk/sessions.py` first.** It is the day's one product deliverable, it is short, and
every other file today either imports from it or exists to justify a line in it.

**Two files under `sutra/` change today** — `sessions.py` is new, and `run_once.py`, `stream.py` and
`multi_turn.py` each lose their local `APP_NAME`/`USER_ID` constants and import them instead. Nothing
else: `sutra/loop.py`, `sutra/agent.py`, `sutra/config.py`, `sutra/desk/agent.py` and yesterday's
`sutra/desk/events.py` are untouched.

---

## §4 Build brief

**`sutra/desk/sessions.py`** — new, and the module that stops today's failure lab from being your
Tuesday:

| Symbol | What it does | Taught in |
| --- | --- | --- |
| `APP_NAME`, `USER_ID` | the single home for two strings that currently live in three files | 1.2, 5.1 |
| `default_service()` | returns a `BaseSessionService`; one line to change on Day 86 | 3.1 |
| `start(service, *, user_id)` | begin a conversation and return it | 1.1 |
| `fetch(service, *, app_name, user_id, session_id)` | get, or raise `SessionNotFound` with the whole address in the message | 1.2 |
| `announce(service, *, app_name)` | log the effective app name and store, once | 5.1 |

**`sutra/desk/run_once.py`, `stream.py`, `multi_turn.py`** — each currently declares or imports its
own `APP_NAME` and `USER_ID`. They now import both from `sutra/desk/sessions.py`, and each builds its
service through `default_service()` rather than naming `InMemorySessionService` directly (3.1, 3.5).

**`days/day-08-sessions-and-services/lab/`** — seventeen small scripts, each given whole in the part
that needs it. **Every one of them costs zero requests.**

**`tests/test_sessions.py`** — the structural suite. See §5.

**`TODO(me)` markers left for you:**

- **1.4** — write the four-line get-or-create described in 1.4's production section, the
  create-then-catch way, and run it twice to prove the second call finds the first call's session.
- **2.3** — decide, and write down in `sessions.py` as a dated comment, **what ends a session in
  Sutra**. The part gives three real answers and a recommendation; it does not make the choice.
- **4.1** — decide what `default_service()` should return when an environment variable says
  `SUTRA_STORE=sqlite`. Do not build the whole Day 86 swap; decide the shape and write down why.
- **5.1** — add `announce()` to whichever entry points you keep, and satisfy yourself it prints
  before anything else can go wrong.
- **§5** — decide whether `tests/test_sessions.py` keeps the `asyncio.run` wrapper or adopts
  `pytest-asyncio`. The wrapper costs one line per test and no dependency; the plugin costs a
  dependency and no lines. Write down the number of async tests at which your answer changes.
- **3.3** — add one query to `lab/keyword_memory.py` that you are confident *should* match, watch it
  fail, and write down the two words that would have had to be identical.

---

## §5 The eval that must be able to fail

Every assertion below runs against `InMemorySessionService` with no model, no key and no quota. Two
of them assert a **negative** — that a wrong address returns nothing — which is the kind of test
people skip and the kind today's failure lab exists to justify.

Every session method is `async`, and this is the first test file whose subject is awaitable. There is
a well-known plugin for that — `pytest-asyncio` — and today deliberately does not use it, because the
alternative is `asyncio.run` and one wrapper line per test. The plan's own rule is that adding a
dependency to avoid writing ten lines is an anti-pattern, and here it would be avoiding one. Whether
that stays true when there are forty async tests is a real question, and it is one of today's
`TODO(me)` items rather than something this document settles for you.

```python
# tests/test_sessions.py
import asyncio

import pytest
from google.adk.events import Event, EventActions
from google.adk.sessions import BaseSessionService

from sutra.desk.sessions import APP_NAME, USER_ID, SessionNotFound, default_service, fetch, start


def test_the_default_service_is_typed_against_the_interface() -> None:
    """3.1: nothing outside sessions.py may know which implementation this is."""
    assert isinstance(default_service(), BaseSessionService)


def test_a_fresh_session_has_the_address_we_asked_for() -> None:
    """1.1: three parts, and all three come from one module."""

    async def check() -> None:
        session = await start(default_service())
        assert (session.app_name, session.user_id) == (APP_NAME, USER_ID)
        assert session.events == [] and session.state == {}

    asyncio.run(check())


def test_fetch_raises_with_the_whole_address_in_the_message() -> None:
    """1.2: a near miss must not be indistinguishable from any other near miss."""

    async def check() -> None:
        service = default_service()
        with pytest.raises(SessionNotFound) as caught:
            await fetch(service, app_name=APP_NAME, user_id=USER_ID, session_id="not-a-real-id")
        for part in (APP_NAME, USER_ID, "not-a-real-id"):
            assert part in str(caught.value)

    asyncio.run(check())


def test_a_wrong_user_id_finds_nothing() -> None:
    """1.2: the security-relevant near miss, asserted rather than assumed."""

    async def check() -> None:
        service = default_service()
        session = await start(service)
        found = await service.get_session(
            app_name=APP_NAME, user_id="someone_else", session_id=session.id
        )
        assert found is None

    asyncio.run(check())


def test_state_arrives_only_through_an_event() -> None:
    """1.3 and Day 7's 1.4: a delta on an event is the only way in."""

    async def check() -> None:
        service = default_service()
        session = await start(service)
        await service.append_event(
            session,
            Event(
                author="sutra_desk",
                invocation_id="run-1",
                actions=EventActions(state_delta={"ticket_id": "4521"}),
            ),
        )
        stored = await fetch(service, app_name=APP_NAME, user_id=USER_ID, session_id=session.id)
        assert stored.state == {"ticket_id": "4521"}

    asyncio.run(check())


# TODO(me): the sixth test - assert that mutating a fetched session changes nothing (3.2).
```

**How to watch each one go RED before it goes green:**

```bash
uv run python -m pytest tests/test_sessions.py -q -m "not live"   # RED: sutra/desk/sessions.py is empty
# ... write the five symbols from parts 1.1, 1.2, 3.1 and 5.1 ...
uv run python -m pytest tests/test_sessions.py -q -m "not live"   # green
```

Then break each one on purpose:

- In `fetch`, change the message to a bare `"session not found"` and watch the third test go red
  naming the part it could not find. That test is asserting on a **message**, which is unusual and
  is exactly right here: the message is the feature.
- Change `default_service()` to return `None` and watch the first test go red — the one-line guard
  against somebody "simplifying" the factory away.
- In `test_a_wrong_user_id_finds_nothing`, change `"someone_else"` to `USER_ID` and watch it go red.
  Then put it back and read it again: that test passes because a lookup **fails**, which is the
  shape of every security assertion you will write in Phase 10.
- Assign directly to `stored.state` in the fifth test and watch nothing change (3.2), which is the
  sixth test asking to be written.

---

## §6 Request budget

**Zero.** Not "cheap" — zero.

| What | Model calls |
| --- | --- |
| all seventeen lab scripts | **0** |
| `tests/test_sessions.py` | **0** |
| every part of every section | **0** |
| **Total** | **0** |

Today is the first day since Day 0 that needs no model at all, and that is a property of the subject
rather than a saving: sessions, runs and services are plumbing, and plumbing can be tested by running
water through it. Custom `BaseAgent` subclasses stand in for the model everywhere a run is needed —
the technique from
[Day 7, part 3.1](../day-07-events-and-streaming/parts/03-the-yield-contract/3.1-one-paper-at-a-time.md)
— which is worth noticing as a technique and not only as a saving: **an agent that does not call a
model is the right tool for testing everything except the model.**

If yesterday's streaming pair ate your quota, today costs you nothing and tomorrow's benchmark will
want plenty.

**Cost: $0.**

---

## §7 Traps

- **A session is found by three things, not one.** `app_name` + `user_id` + `session_id`, all of
  them, and a wrong one returns `None` rather than a near miss. Three different causes, one
  indistinguishable symptom. (1.2)
- **Your repository already has three different app names.** `"sutra"` in `run_once.py`,
  `"sutra.desk"` in the database `adk web` wrote, and `"InMemoryRunner"` if you use the convenience
  constructor. None is wrong; none can see the others' sessions. (1.2, 3.5, 5.1)
- **`get_session` returns a copy.** Changing what you fetched changes nothing anybody else can see —
  and on a persistent store it fails differently, so the symptom moves while the rule does not.
  Changes travel in events. (1.1, 3.2)
- **`append_event` to an address the store does not know logs a warning and silently does nothing**,
  while still returning an `Event`. From the call site, success and failure are identical. (3.2, 5.1)
- **A session always has one more event than your loop counted** — the runner appends the user's
  message before your agent runs. A session with exactly one event means the question got in and
  nothing came back. (2.2)
- **`yield_user_message=True` does nothing when your root is a custom `BaseAgent`.** It is honoured on
  the node runtime path — which is what an `LlmAgent` root uses — and no error tells you which one
  you are on. (2.2)
- **The runner does not stamp `invocation_id` on events your agent yields.** Set it from
  `ctx.invocation_id` or your trace has a blank column and your turns cannot be grouped. (2.1)
- **`create_session` with an id that already exists raises `AlreadyExistsError`** — and the message
  contains only the id, not the app or user. Check-then-create is a race; create-then-catch is not.
  (1.4)
- **Whitespace is not a session id.** `session_id="  "` mints a UUID instead. (1.4)
- **`InMemoryMemoryService` matches words, not meaning.** `logout` does not match `logged out`, `3`
  does not match `three`, and `signed out` matches for the wrong reason — the word *out*. It is
  genuinely good at exact identifiers and nothing else. (3.3)
- **Nothing ends a session.** No idle timeout, no length limit. The event list only grows, and every
  turn re-sends all of it, so the cost is quadratic and shows up as a tokens-per-minute limit rather
  than a request limit. (2.3)
- **`GetSessionConfig` changes what you read, not what exists** — and not what the runner loads. It
  is not a fix for context length. (2.3)
- **In memory means in this process.** Every deploy, every idle-container restart and every Ctrl+C
  takes every session with it, silently, with no flush and no error. Four of the six ways a process
  ends are normal operation. (4.1)
- **Two processes have two stores.** Half of each conversation lands where the next request will not
  read it, both transcripts are internally correct, and nothing errors. Sticky sessions convert this
  into an outage on every deploy rather than fixing it. (4.2)
- **`InMemoryRunner` cannot be given a real session service** — the constructor does not take one.
  Anything built on it has to be rewritten rather than reconfigured on Day 86. (3.5)
- **`SqliteSessionService` is not exported from `google.adk.sessions`**, and
  `DatabaseSessionService` needs the `db` extra, which fails at import time on the day you swap
  rather than the day you installed. (3.1, 4.3)
- **The credential service is `None` by default** and that is deliberate: secrets do not get a
  convenient default. (3.4)

---

## §8 Verify before you code

Every source below was checked on **2026-08-26** while this day was written. Principle 8: re-check on
the day you use them. This table is evidence, not a substitute.

| Source | What it settled |
| --- | --- |
| `adk.dev/sessions/session/` | A session is "a single conversation thread"; its properties (`id`, `appName`, `userId`, `events`, `state`, `lastUpdateTime`); the four implementations and what each needs; `InMemorySessionService` — "all conversation data is lost if the application restarts"; `DatabaseSessionService` requires the `db` extra and uses row-level locking; the v1.22.0 schema change requiring migration |
| `adk.dev/sessions/state/` | The `app:`, `user:` and `temp:` scopes and what each shares; that state must be JSON-serialisable; and the explicit warning that direct mutation "will likely NOT be saved by DatabaseSessionService or VertexAiSessionService" |
| the installed `google-adk` 2.7.1 | `Session.model_fields` (six) · `BaseSessionService.__abstractmethods__` (four — `append_event` is concrete) · `AlreadyExistsError`'s exact message · `SessionNotFoundError(ValueError)` and its message · that `get_session` copies and `append_event` addresses · the silent-append warning text · `InMemoryMemoryService`'s keyword algorithm · `InMemoryArtifactService`'s version numbering and `user:` namespace · `InMemoryRunner`'s `app_name` default of `'InMemoryRunner'` and its `credential_service=None` · `SqliteSessionService`'s positional path and its migration `RuntimeError` · `StaleSessionError`'s docstring |

**Five claims in this day that no page states**, established by running code rather than by reading.
Re-run them; if your version disagrees, **your terminal wins** and you fix the document:

```bash
uv run python days/day-08-sessions-and-services/lab/drawers.py       # 3.2 - the silent append
uv run python days/day-08-sessions-and-services/lab/keyword_memory.py # 3.3 - 'signed out' matches on "out"
uv run python days/day-08-sessions-and-services/lab/furnished.py     # 3.5 - app_name = 'InMemoryRunner'
uv run python days/day-08-sessions-and-services/lab/off_by_one.py    # 2.2 - the extra event
uv run python days/day-08-sessions-and-services/lab/mismatch.py      # 5.1 - three faces of one bug
```

That is Principle 8 working rather than failing: a convenience constructor that names your app for
you is real whether or not a page mentions it, and the way you find out is to print the name.

---

## §9 Say it in an interview

> "Sessions are the part people underestimate, because in a demo they just work. A session is one
> conversation with a three-part address — app, user, session id — and the two things I'd want a team
> to internalise are what happens when the address is wrong and what 'in memory' actually means. On
> the address: get one of the three wrong and the lookup returns nothing rather than raising, which is
> the right design and means 'session not found' is a symptom with three causes and no evidence. In
> one repository I had three different app names live at once — a constant in the code, one a dev tool
> had derived from a folder path, and a framework default — and none of them was wrong. The fix isn't
> clever: log the effective app name and store once at startup, and raise on a failed lookup with the
> whole address in the message. On 'in memory': the risk people name is crashes, and the real risk is
> that the process ends on every deploy and most platforms restart idle containers anyway, so the loss
> is scheduled rather than exceptional — and there's no flush, no shutdown hook and no error, so it
> shows up as a handful of 'the bot forgot me' reports on the afternoon you released. The quieter
> version is two replicas: half of each conversation goes into a store the next request won't read,
> every individual process's log looks perfectly coherent, and there's no single place the bug is
> visible. That's what convinces people to move the store out of the process, rather than the
> restart."

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked — honestly. `./m done 8` refuses to commit while
any box is unticked, and it cannot tell whether you were truthful. That part is yours.

The day is finished when `sutra/desk/sessions.py` owns `APP_NAME` and `USER_ID` and nothing else
declares them; when `fetch` raises with all three parts of the address in the message and you have
seen it do so; when `default_service()` is the only place in the repository that names an
implementation; when you have watched one run produce four events and the session hold five; when you
have made `append_event` fail silently on purpose and can say what the call site saw; when you have
run the same script twice and seen a session survive with SQLite and not survive without it; when you
can name the four services and say which one a runner leaves empty and why; when
`tests/test_sessions.py` has gone red and green for each of its assertions and you have decided, in
writing, whether it keeps the `asyncio.run` wrapper; and when you have written down, in
`sessions.py`, what ends a session in Sutra.

---

## §11 Ledger & commit

Paste these **with the values you actually observed** (Principle 7), not the ones printed here.

**`docs/PROGRESS.md`** — append one row:

```text
| 8 | <date> | ADK-06, ADK-07 | 16 | <hash> | ✅ |
```

**`docs/PACKAGES.md`** — **no new rows.** Nothing was installed today. `aiosqlite` is present because
`google-adk` 2.7.1 requires it (`Requires-Dist: aiosqlite>=0.21`, not an extra), so it is ADK's pin
and not Sutra's, and it does not get a row of its own.

If you decide the `asyncio.run` wrapper is not worth keeping and add `pytest-asyncio`, **that is a
row**, and you look the version up before you pin it (Principle 7):

```bash
curl -s https://pypi.org/pypi/pytest-asyncio/json | python -c "import sys,json; d=json.load(sys.stdin)['info']; print(d['version'], d['requires_python'])"
```

If that lookup fails, the row says `TODO(<that exact command>)` and **not a guess**.

**`docs/PAPERS.md`** — no rows. Today's subject is a framework's storage model, which is a tool
rather than an idea with a citable origin document.

**`docs/SKILL_PROVENANCE.md`** — no rows. First entries arrive on Day 29.

**`docs/adr/`** — no new ADR today, but **one is owed on Day 86** and the decision starts here: which
session store Sutra deploys with, and what its retention is. Part 4.3 is the reading; the ADR is that
day's. **If your ADK version has changed what `append_event` does with an address it does not
recognise — raising instead of warning, say — stop and re-read Principle 14 before editing anything**,
because that is an ecosystem change and the plan is amended first.

**Commit message:**

```text
day 08: sessions, runs & in-memory services - the conversation gets an address - closes ADK-06, ADK-07
```
