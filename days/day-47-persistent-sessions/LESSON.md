---
day: 47
phase: 7
phase_name: "Memory and retrieval"
title: "Persistent sessions — database-backed"
ids: ["ADK-29"]
principles: [1, 2, 4, 7, 8, 9, 10, 11, 13, 15, 16, 17, 18]
kind: lab
plan_version: "v2.2.1"
parts: 20
generated: "2026-09-05"
status: written
lab_scaffolded: true
commit: ""
---

# Day 47 — Persistent sessions: database-backed

> **Yesterday (Day 46):** the line between a session and a memory. A session is one conversation and
> `MemoryService` is recall across conversations, and `sutra/memory/` was created to hold the second
> one.
> **Today:** the first one, made durable. The conversation stops living in a dictionary inside one
> process and starts living in four tables in a file — which is what makes a restart survivable, a
> second instance possible, a deletion request answerable, and a backup something you can get wrong.
> **Tomorrow (Day 48):** what is worth keeping out of what today made keepable. Retention as data,
> expiry, supersession, and erasure as an obligation.

---

## §1 Where we are

[Day 43](../day-43-stateless-by-default/LESSON.md) built `sutra_mcp/app.py` so that any instance
answers any request, because no instance keeps anything between them. That day's
[4.1](../day-43-stateless-by-default/parts/04-where-state-goes/4.1-down-out-or-nowhere.md) said the
state has to go *down* — into a store every instance can reach — and left the store as a promise.

This is the day the promise is kept, for the one piece of state that matters most: the conversation
itself.

The shape of it is a shopkeeper who kept his credit accounts in chalk on the shutter, until it
rained. The book he bought the next week is slower — every sale is a line to write, and twice a month
he starts a new volume — and he has never lost a month since. Everything in this day is a version of
that trade: the file is slower than the dictionary, and the file is still there tomorrow.

**Statelessness is not the absence of state.** It is state that lives somewhere other than the
process, so any process can pick it up. A stateless server needs a durable session store *more* than
a sticky one does, not less.

Four things to know before you read a part.

**This day installs nothing.** `sqlite3` is in the standard library and `aiosqlite` is already a
dependency of `google-adk`. The class this day uses needs no extra;
[2.2](parts/02-reaching-the-service/2.2-the-driver-you-do-not-have.md) is the part about the one that
does and why we are not paying for it. `git diff pyproject.toml uv.lock` must be empty when you
finish.

**The class you need is not exported, and the documentation points somewhere else.**
`google.adk.sessions.__all__` names seven things and `SqliteSessionService` is not one of them, even
though the ADK's own CLI registers `sqlite://` to it. Meanwhile adk.dev tells you to use
`DatabaseSessionService` with `sqlite+aiosqlite:///./my_agent_data.db` — a URL this installation has
no factory for, which falls through to a class that needs SQLAlchemy, which is not installed.
Section 2 is those two facts with the source quoted; §8 names every file that was read.

**Almost every mechanism in this day already has a failure attached to it, and none of them raise.**
An in-memory store after a restart returns `None`, which is what it also returns for a session id
that never existed. A relative path resolved from the wrong directory is a second, empty database. A
migration that lost every transcript reports matching row counts. A file copy of a live store opens
cleanly and is missing everything. Sections 3 to 7 are each an argument that the check you would have
written is the wrong check.

**And one thing genuinely goes well.** [Day 43](../day-43-stateless-by-default/LESSON.md) measured
four processes silently losing seventy of a hundred increments. Here, four processes doing a hundred
appends to one SQLite file lose nothing, and a fifth writer holding a stale copy is *refused* rather
than allowed to overwrite. Section 4 is why that is a better failure, and what it costs.

---

## §2 The map

Twenty parts in seven sections, plus one paper. This is a one-ID day, so the sections are ADK-29
taken in the order the questions actually arrive — *what does a restart cost*, *how do I reach the
store*, *what does one write really do*, *what happens when two workers meet*, *what happens as the
store grows*, *how do I remove somebody*, and *how do I not lose the file*. The day climbs
`foundation → working → production`.

### Section 1 — `01-what-restart-costs`: the store, opened and read (ADK-29)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [The book that survives the shutter](parts/01-what-restart-costs/1.1-the-book-under-the-shutter.md) | Two processes, one session id, and a `None` that means nothing was lost | `foundation` |
| 1.2 | [A session is four tables](parts/01-what-restart-costs/1.2-a-session-is-four-tables.md) | The schema, the JSON column, and the cascade that does not fire | `foundation` |
| 1.3 | [Three scopes, three tables](parts/01-what-restart-costs/1.3-three-scopes-three-tables.md) | Four prefixes, three tables, and one deliberate absence | `working` |

### Section 2 — `02-reaching-the-service`: getting hold of the thing (ADK-29)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [The class that is not exported](parts/02-reaching-the-service/2.1-the-class-that-is-not-exported.md) | Three routes to one class, and which one carries a promise | `working` |
| 2.2 | [The driver you do not have](parts/02-reaching-the-service/2.2-the-driver-you-do-not-have.md) | The documented URL has no factory, and the fix is to install nothing | `working` |
| 2.3 | [The URL that names a file](parts/02-reaching-the-service/2.3-the-url-that-names-a-file.md) | Three slashes against four, and a wrong path that is not an error | `working` |
| 2.4 | [Handing the runner a store](parts/02-reaching-the-service/2.4-handing-the-runner-a-store.md) | One constructor argument, and why `adk web` already disagrees with you | `working` |
| 2.5 | [🅿️ The lounge you cannot enter](parts/02-reaching-the-service/2.5-the-lounge-you-cannot-enter.md) | What the managed store gives and takes, at a billing account's price | `production` |

### Section 3 — `03-writes-that-survive`: what one `append_event` really does (ADK-29)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [The ticket torn in two](parts/03-writes-that-survive/3.1-the-ticket-torn-in-two.md) | Three changes, one transaction, and a `BEGIN` you will not find | `working` |
| 3.2 | [What a restart still loses](parts/03-writes-that-survive/3.2-what-a-restart-still-loses.md) | Three partials sent, one event stored, one customer with a reference number | `production` |
| 3.3 | [💥 The pragma nobody set](parts/03-writes-that-survive/3.3-the-pragma-nobody-set.md) | 100 of 100 appends land, and four of four workers die on a locked file | `production` |

### Section 4 — `04-two-workers`: the same conversation, twice (ADK-29)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [Refused, not overwritten](parts/04-two-workers/4.1-refused-not-overwritten.md) | Optimistic concurrency, one column, and a `ValueError` subclass | `production` |
| 4.2 | [💥 The read that raises nothing](parts/04-two-workers/4.2-the-read-that-raises-nothing.md) | A refund approved on a closed ticket, with `exceptions : 0` | `production` |
| 4.3 | [Losing the race on purpose](parts/04-two-workers/4.3-losing-the-race-on-purpose.md) | 16 attempts and 1 line, against 11 attempts and 6 | `production` |

### Section 5 — `05-shape-and-size`: what happens as the store gets old (ADK-29)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [The store the code cannot read](parts/05-shape-and-size/5.1-the-store-the-code-cannot-read.md) | A schema that already changed once, and a migration that cannot run here | `working` |
| 5.2 | [💥 The migration that passed](parts/05-shape-and-size/5.2-the-migration-that-passed.md) | 1000 rows in, 1000 rows out, 1000 conversations gone | `production` |
| 5.3 | [The session that never ended](parts/05-shape-and-size/5.3-the-session-that-never-ended.md) | 4.4ms at one turn, 54.2ms at four hundred, and the limit that belongs in SQL | `production` |

### Section 6 — `06-forgetting-on-purpose`: removing somebody, and not publishing them (ADK-29)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 6.1 | [Delete the session, keep the customer](parts/06-forgetting-on-purpose/6.1-delete-the-session-keep-the-customer.md) | Sessions 0, events 0, `user_states` 1 — and no error | `production` |
| 6.2 | [💥 A store in a public repository](parts/06-forgetting-on-purpose/6.2-a-store-in-a-public-repo.md) | Two `.gitignore` lines, and why you ask git rather than read them | `production` |

### Section 7 — `07-in-production`: the copy you have not opened (ADK-29)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 7.1 | [The backup nobody restored](parts/07-in-production/7.1-the-backup-nobody-restored.md) | 200 turns written, 0 restored, and a file that opens perfectly | `production` |

### The paper — read it **after** the parts

| Paper | What it claims | Level |
| --- | --- | --- |
| [Principles of transaction-oriented database recovery](papers/01-transaction-oriented-recovery.md) | The transaction is the unit, ACID is what it promises, and recovery is a method rather than a hope | `production` |

`doi:10.1145/289.291`, 1983. One part cites it as an address:
[3.1](parts/03-writes-that-survive/3.1-the-ticket-torn-in-two.md), which is where the words
*atomic*, *transaction* and *commit* are first used. A paper is taught once in the whole curriculum,
so read the parts first and the paper last —
[7.1](parts/07-in-production/7.1-the-backup-nobody-restored.md) points you at it.

**Read section 2 before you write a line of `persistence.py`.** Sections 3 to 7 all assume you have
a store; section 2 is the part where the obvious way to get one is wrong twice.

---

## §3 Setup — run this

**No package is added today, and no package is upgraded.** `google-adk` stays at `2.7.1`.
`git diff pyproject.toml uv.lock` must be empty when you finish.

```bash
# 1 - the day's lab
cd days/day-47-persistent-sessions
mkdir -p lab lab/papers/transaction-oriented-recovery

# 2 - section 1: what a restart costs
touch lab/amnesia.py lab/tables.py lab/scopes.py

# 3 - section 2: reaching the service
touch lab/reach.py lab/driver.py lab/urls.py

# 4 - section 3: writes that survive
touch lab/writes.py lab/restart.py lab/locked.py

# 5 - section 4: two workers
touch lab/stale.py lab/staleread.py lab/recover.py

# 6 - section 5: shape and size
touch lab/oldschema.py lab/dropped.py lab/grow.py

# 7 - sections 6 and 7, and the day's gate
touch lab/forget.py lab/leak.py lab/backup.py lab/gate.py

# 8 - the paper demo
touch lab/papers/transaction-oriented-recovery/store.py
cd -

# 9 - the project file you are about to fill (you type every line)
touch sutra/memory/persistence.py

# 10 - the freshness gate, before anything else
uv run python -c "import google.adk, aiosqlite, importlib.util as u; print(google.adk.__version__, 'sqlalchemy:', u.find_spec('sqlalchemy') is not None)"
```

**Step 10 is this day's freshness gate.** It must print `2.7.1` and `sqlalchemy: False`. If the
version has moved, section 2's three routes and section 5's schema check are the first things to
re-verify — run `lab/reach.py` and `lab/oldschema.py`, which are written as tripwires for exactly
that. If `sqlalchemy` is suddenly `True`, somebody added an extra and
[2.2](parts/02-reaching-the-service/2.2-the-driver-you-do-not-have.md)'s decision needs re-opening
(Principle 14).

**`sutra/memory/` is yours and it is shared.** Day 46 created the package and owns `__init__.py` and
`service.py` (memory — recall *across* conversations). You are adding `persistence.py` beside them,
and Day 48 adds `policy.py`. Three files, three subjects, one package. **Do not re-create the
package.**

The store itself lives at `data/sessions.sqlite3`, which does not exist yet and is created on first
use. `.gitignore` already carries `*.db` and `*.sqlite3`;
[6.2](parts/06-forgetting-on-purpose/6.2-a-store-in-a-public-repo.md) is why you check that with
`git check-ignore` rather than by reading the file.

---

## §4 Build brief

### The project code — `sutra/memory/persistence.py`, and you type every line

One file, three public symbols. The parts give you every mechanism; the decisions are yours.

| Symbol | Shape | What it must do |
| --- | --- | --- |
| `SESSION_DB` | a `Path` | The store's **absolute** location, anchored to the repository rather than to the working directory (2.3, 2.4). |
| `session_service` | `() -> BaseSessionService` | Build the durable store: parent directory created, absolute `sqlite:///` URL, return typed as the base class (2.1, 2.3, 2.4). |
| `purge_user` | `async (app_name, user_id) -> int` | Erase one customer completely — every session, every event, and the `user_states` row the API cannot reach — in one transaction, returning the number of rows removed (6.1). |

- **`SESSION_DB`** — exported as a `Path` so a caller can ask it questions: does it exist, how big is
  it, is git ignoring it. The gate and
  [6.2](parts/06-forgetting-on-purpose/6.2-a-store-in-a-public-repo.md) both do.
- **`session_service()`** — a **function**, not a module-level object, so nothing is constructed at
  import time (Day 43's
  [1.1](../day-43-stateless-by-default/parts/01-accidental-state/1.1-the-dictionary-nobody-called-state.md)).
  It carries the unexported import from
  [2.1](parts/02-reaching-the-service/2.1-the-class-that-is-not-exported.md) **exactly once in the
  whole project**, with a comment naming the ADK version and the date you checked it.
- **`purge_user(...)`** — the deletion loop plus the one `DELETE` the interface does not offer, inside
  one `BEGIN IMMEDIATE ... COMMIT` (3.1), and it must **not** touch `app_states` (6.1). Returning a
  count rather than `None` is what lets the caller log what was removed.
- **Log the choice once at start-up**, at INFO, naming the class and the resolved path
  ([2.4](parts/02-reaching-the-service/2.4-handing-the-runner-a-store.md)). One line removes the
  entire class of confusion about which store a process is using.

**`TODO(me)` markers left for you:**

- **1.3** — write down which facts the desk currently re-derives from the transcript and should be
  `user:` keys instead, and say for each one what happens to it when
  [6.1](parts/06-forgetting-on-purpose/6.1-delete-the-session-keep-the-customer.md)'s erasure runs.
- **2.1** — write the tripwire test. `lab/reach.py` asserts three facts about the ADK; move the
  version of it you want to keep into `tests/`, so a `uv sync` that breaks the unexported import
  fails in the suite rather than on a box.
- **2.3** — decide whether `SESSION_DB` comes from an environment variable or from the repository
  root, and write down what happens in a container if it is relative. Then decide what the code does
  when the configured path is *not* absolute: refuse, or resolve.
- **2.4** — decide Sutra's `app_name` and write it as one constant. It is the first component of
  every session's primary key, so say in a comment what changing it would do to a store that already
  has sessions in it.
- **2.5** — write the comparison that would justify moving to a managed session store, with the four
  numbers this day measures in it. Then say which of the four Sutra does not yet have a way to
  observe in production.
- **3.3** — decide whether Sutra sets `journal_mode=WAL` on the store at creation, and whether it
  catches `RuntimeError` as well as `sqlite3.OperationalError` where the service is constructed.
  Write down the busy timeout you are inheriting and where it comes from.
- **4.3** — decide where the retry boundary sits for a session write, and write the three-step
  loop — re-read, re-apply, write — with a bounded attempt count. Then say what Sutra does on the
  last failure, and where that lands relative to Day 44's `with_retries`.
- **5.3** — choose a `num_recent_events` for the desk, write the reason beside the number, and list
  what has to move into `user:` state for a bounded window to still be correct.
- **6.1** — write down every place a customer's words land besides the session store, and say which
  of them `purge_user` reaches. The honest list is longer than one file.
- **7.1** — write the backup command and its restore drill as one script, ending in a read through
  `session_service()`. Decide how often it runs and where the copies go.

### The lab — nineteen scripts and one paper demo, none of which calls a model

| File | What it does | Taught in |
| --- | --- | --- |
| `lab/amnesia.py` | two processes, one session id, two stores | 1.1 |
| `lab/tables.py` | the four tables, one event row, and an orphan the cascade did not take | 1.2 |
| `lab/scopes.py` | four prefixes written, three tables checked, one key nowhere | 1.3 |
| `lab/reach.py` | three routes to `SqliteSessionService`, as a tripwire | 2.1 |
| `lab/driver.py` | the missing extra, the documented URL, and the one that resolves | 2.2 |
| `lab/urls.py` | seven strings, four of which name the same file | 2.3 |
| `lab/writes.py` | one `append_event`, three changes, before and after | 3.1 |
| `lab/restart.py` | three partials sent, one event stored, a process killed mid-turn | 3.2 |
| `lab/locked.py` | 4 × 25 appends, three arms, and four workers dead at construction | 3.3 |
| `lab/stale.py` | two handles, one refusal, and a one-line fix | 4.1 |
| `lab/staleread.py` | a refund approved on a closed ticket, zero exceptions | 4.2 |
| `lab/recover.py` | six workers, blind retries against re-reading retries | 4.3 |
| `lab/oldschema.py` | a thousand sessions in the old schema, and the door that is locked | 5.1 |
| `lab/dropped.py` | a migration whose row counts match and whose transcripts are gone | 5.2 |
| `lab/grow.py` | load cost at 1, 50, 100, 200 and 400 turns, two arms | 5.3 |
| `lab/forget.py` | erase a customer two ways, and count what is left | 6.1 |
| `lab/leak.py` | what a store would publish, and what git says about it | 6.2 |
| `lab/backup.py` | a live store copied two ways, and actually restored | 7.1 |
| `lab/gate.py` | the day's assertions about `sutra/memory/persistence.py`, as an exit code | §5 |

`lab/papers/transaction-oriented-recovery/store.py` is the paper demo and it is **given complete** in
the paper part. It is teaching material, not a rep: type it, run both arms, and compare your output
with the transcripts.

---

## §5 The eval that must be able to fail

Nine checks with exit codes or ablations, all on zero model calls.

**The gate** is the day's definition of done, and it is red until you have written the module:

```bash
uv run python days/day-47-persistent-sessions/lab/gate.py; echo "exit: $?"
```

Measured on 2026-09-05, before anything was written:
`- sutra.memory.persistence is not importable: ModuleNotFoundError: No module named 'sutra.memory'`,
`findings: 1`, `exit: 1`. When it prints `findings: 0` and `exit: 0`, six statements are true: the
module imports; it exports `SESSION_DB`, `session_service` and `purge_user`; git ignores the resolved
store path; `session_service()` is not still returning `InMemorySessionService`; a session written
through one service object is visible to another; and `purge_user` leaves nothing behind. Then break
exactly one on purpose — delete the `user_states` statement from `purge_user` — and watch
`purge_user left 1 rows behind` appear.

**The erasure ablation** is the day's sharpest failure, and both arms must be run:

```bash
cd days/day-47-persistent-sessions/lab
uv run python forget.py; echo "exit: $?"
uv run python forget.py --purge; echo "exit: $?"
cd -
```

`user_states 1 → 1` and `exit: 1` against `1 → 0` and `exit: 0`, with `other customers intact: True`
in both. The API-only arm reports success and leaves the customer's phone number in the file.

**The migration ablation**, both arms:

```bash
cd days/day-47-persistent-sessions/lab
uv run python dropped.py; echo "exit: $?"
uv run python dropped.py --safe; echo "exit: $?"
cd -
```

`row-count check : PASS` in **both**, and `readable after : 0` against `1000`. The check everybody
writes cannot tell them apart.

**The backup ablation**, both arms:

```bash
cd days/day-47-persistent-sessions/lab
uv run python backup.py; echo "exit: $?"
uv run python backup.py --vacuum; echo "exit: $?"
cd -
```

`turns restored : 0` of 200 against `200` of 200 — from a copy that opened without complaining.

**The paper's ablation**, both arms:

```bash
cd days/day-47-persistent-sessions/lab/papers/transaction-oriented-recovery
uv run python store.py; echo "exit: $?"
uv run python store.py --no-transaction; echo "exit: $?"
cd -
```

`turn_count 2 / events 2 / consistent` against `turn_count 2 / events 3 / TORN`, and a rollback
journal of 8 720 bytes on the disk in the first arm and absent in the second.

**And the rest, each of which has a named break in its own part:**

```bash
cd days/day-47-persistent-sessions/lab
uv run python amnesia.py; uv run python amnesia.py --memory
uv run python tables.py
uv run python scopes.py
uv run python reach.py
uv run python driver.py
uv run python urls.py
uv run python writes.py
uv run python restart.py; uv run python restart.py --complete
uv run python locked.py; uv run python locked.py --wal; uv run python locked.py --blocked
uv run python stale.py; uv run python stale.py --refetch
uv run python staleread.py; uv run python staleread.py --fresh
uv run python recover.py; uv run python recover.py --blind
uv run python oldschema.py
uv run python grow.py; uv run python grow.py --recent
uv run python leak.py forget.sqlite3; uv run python leak.py forget.sqlite3 --as-if-tracked
cd -
```

`amnesia.py --memory`, `restart.py`, `locked.py --blocked`, `stale.py`, `staleread.py`,
`recover.py --blind`, `grow.py` and `leak.py --as-if-tracked` **exit 1 on purpose**. That is the
finding, not a bug in the lab. `locked.py --blocked` prints a full traceback ending in
`RuntimeError: Error accessing database ...: database is locked`, raised from `__init__`.

---

## §6 Request budget

**Free-tier Gemini**, 20 generate requests per day per model (`gemini-3.7-flash`, roster re-verified
2026-09-04).

| What | Generations |
| --- | --- |
| every part in every section | **0** |
| all nineteen lab scripts, every flag | **0** |
| the paper demo, both arms | **0** |
| `sutra/memory/persistence.py` and the gate | **0** |
| **Total planned** | **0 of 20** |

**Zero, and it is the point rather than an economy.** Nothing this day teaches involves a model. A
session is rows in a file; a restart is a process ending; a transaction is two statements and a
commit; a lock is a lock. Every measurement here is a row count, a byte count or a millisecond, and
every one of them is reproducible on a machine with no API key at all.

Wiring the durable store into the desk and having a real conversation survive a restart is worth
doing once, costs two or three generations, and proves nothing `amnesia.py` has not already proved
with two processes and no model.

**Cost: $0.**

---

## §7 Traps

- **`from google.adk.sessions import SqliteSessionService` raises.** The class is not in that
  package's `__all__` and not in its lazy-import map; the module import is the way in, and it is what
  the ADK's own CLI does (2.1).
- **adk.dev's SQLite URL, `sqlite+aiosqlite:///./my_agent_data.db`, has no registered factory** on
  `google-adk==2.7.1`. It falls through to `DatabaseSessionService`, which raises
  `ImportError: The 'sqlalchemy' package is required ... pip install google-adk[db]` (2.2).
- **`sqlite://` with the third slash missing is an in-memory service**, silently. One character
  between durable and amnesiac (2.1).
- **Three slashes is relative, four is absolute** — and a relative path is relative to the *process's*
  working directory, so the same string names different files from different callers. Neither form
  fails (2.3).
- **A wrong path is not an error; it is a second, empty database.** SQLite creates the file and the
  service creates the tables (2.3).
- **A missing parent directory gives `sqlite3.OperationalError: unable to open database file`** — six
  words, no path — and it arrives at the first write, not at construction (2.3).
- **Constructing `SqliteSessionService` reads the disk.** `__init__` calls `_is_migration_needed`, so
  a locked or old file fails before you have a runner (3.3, 5.1).
- **That failure surfaces as `RuntimeError`, not `sqlite3.OperationalError`.** A handler written for
  database errors will not catch it — and under WAL the same situation raises the *other* type in a
  different frame (3.3).
- **`adk web` and `adk run` default to per-agent SQLite at `<agent>/.adk/session.db`.** Your own
  `Runner` does not. Testing persistence through the dev UI proves nothing about your code (2.4).
- **…and on Cloud Run or Kubernetes the CLI switches back to in-memory**, at WARNING level, because
  container disk is not durable (2.4).
- **`get_session` returns `None` for a session that never existed and for one you just lost.** There
  is no error to find in a log (1.1).
- **A hand-run `DELETE FROM sessions` leaves the events behind.** The cascade needs
  `PRAGMA foreign_keys = ON`, and SQLite's default is off; the service sets it on its own connections
  and your connection does not inherit that (1.2, 6.1).
- **`temp:` keys are stripped before the write, on purpose** — so a "cache" in `temp:` is recomputed
  every turn, and a working note *without* the prefix is on a disk forever (1.3).
- **`json_patch` treats a `null` value as a delete.** Writing `{"user:tier": None}` because a lookup
  failed erases the tier rather than recording "unknown" (1.3).
- **Streaming partials are never stored.** `append_event` returns before touching the database when
  `event.partial` is set, so a crash mid-answer leaves the question with nothing after it — and the
  customer has already read the answer (3.2).
- **`update_time` comes from the event's clock, not the database's.** Two machines with skewed clocks
  produce a stored timestamp in the future, and every append from the slower one is refused (4.1).
- **`StaleSessionError` subclasses `ValueError`.** An `except ValueError` anywhere near a session
  turns a loud refusal into a silently dropped turn (4.1).
- **The store guards writes and not reads.** Deciding from `session.state` a minute after loading it
  raises nothing and can be wrong; a successful write afterwards is not evidence the decision was
  current (4.2).
- **A retry that does not re-read is refused identically every time** and spends the whole attempt
  budget. Re-reading without re-applying is worse: a fresh timestamp over a stale decision (4.3).
- **The ADK's own migration command imports SQLAlchemy**, which this repository does not install — so
  the fix named in the schema error does not run here (5.1).
- **A migration verified by row counts is not verified.** A thousand rows in, a thousand rows out,
  every constraint satisfied, every transcript empty (5.2).
- **`get_session` reads and deserialises every event by default.** The fix is
  `GetSessionConfig(num_recent_events=N)`, which becomes a `LIMIT`; slicing `session.events` in Python
  pays for all of them first (5.3).
- **…and a bounded window means the agent cannot see the start of the conversation.** Facts that must
  survive have to be in `user:` state, not in the transcript (5.3, Day 48).
- **`delete_session` cannot remove a customer.** User state is keyed on `(app_name, user_id)` with no
  session in the key, and there is no `delete_user` on the interface (6.1).
- **`list_sessions` returns a `ListSessionsResponse`**, not a list — the sessions are on `.sessions`,
  and they carry no events (6.1).
- **`.gitignore` does not apply to a file git already tracks.** Adding the line after the first commit
  fixes nothing, and the history keeps the file after you remove it (6.2).
- **A file copy of a live store in WAL mode is missing everything since the last checkpoint** and
  opens perfectly. Use `VACUUM INTO`, which takes only a read lock (7.1).
- **`VACUUM INTO` refuses to overwrite an existing target** — deliberately, so this morning's bad copy
  cannot replace last night's good one (7.1).
- **A plain `VACUUM` takes an exclusive lock** and kills every service constructed during it. So does
  a naive backup, a schema migration, and any maintenance job that opens the store to write (3.3, 5.2).

---

## §8 Verify before you code

Fetched or read on **2026-09-05**, the day this was written.

**The ADK documentation:**

- `https://adk.dev/sessions/session/` — fetched. It names **three** session services:
  `InMemorySessionService`, `DatabaseSessionService` and `VertexAiSessionService`. It **does not
  mention `SqliteSessionService` at all**. For SQLite it gives
  `DatabaseSessionService(db_url="sqlite+aiosqlite:///./my_agent_data.db")` and names the extra as
  `pip install google-adk[db]`. Both of those are the subject of
  [2.2](parts/02-reaching-the-service/2.2-the-driver-you-do-not-have.md): on this installation that
  URL has no registered factory and that class cannot be constructed.
- `https://adk.dev/docs/sessions/session/` returned **HTTP 404**. The live page is the path with no
  `/docs/` segment, which is the same shape Days 33, 40 and 44 recorded.

**The installed ADK — the authoritative surface here, read rather than guessed:**

- `.venv/Lib/site-packages/google/adk/sessions/__init__.py` — `__all__` holds `BaseSessionService`,
  `Session`, `State`, `StateSchemaError`, `InMemorySessionService`, `DatabaseSessionService`,
  `VertexAiSessionService`. `SqliteSessionService` is **absent**, from the list and from the lazy
  `__getattr__` map, so the package import genuinely raises (2.1).
- `.venv/Lib/site-packages/google/adk/sessions/sqlite_session_service.py` — the schema
  (`app_states`, `user_states`, `sessions`, `events`, with `event_data TEXT NOT NULL` and
  `ON DELETE CASCADE`), `_parse_db_path`'s three-versus-four-slash rule, `PRAGMA foreign_keys = ON` on
  every connection, `__init__` calling `_is_migration_needed`, the `if event.partial: return event`
  first line of `append_event`, the `update_time` comparison that raises `StaleSessionError`,
  `delete_session`'s single `DELETE FROM sessions`, and `get_session`'s
  `ORDER BY timestamp DESC, id DESC` plus optional `LIMIT` (1.2, 1.3, 2.3, 3.1, 3.2, 4.1, 5.1, 5.3,
  6.1).
- `.venv/Lib/site-packages/google/adk/sessions/base_session_service.py` — `GetSessionConfig` with
  `num_recent_events` and `after_timestamp`, both `Optional` and both `None` by default; the seven
  public methods (`create_session`, `get_session`, `list_sessions`, `delete_session`,
  `get_user_state`, `append_event`, `flush`) and the absence of any `delete_user`; `flush`'s
  docstring saying it may be a no-op for a non-buffering implementation (3.2, 5.3, 6.1).
- `.venv/Lib/site-packages/google/adk/cli/service_registry.py` — `sqlite_session_factory` imports
  `SqliteSessionService` from its module, treats `sqlite://` with an empty path as in-memory, and
  strips one leading slash; `postgresql` and `mysql` are registered to `database_session_factory`.
  Registered schemes on this installation: `agentengine`, `memory`, `mysql`, `postgresql`, `sqlite`
  (2.1, 2.2).
- `.venv/Lib/site-packages/google/adk/utils/_dependency.py` — `missing_extra(package, extra)`
  **returns** an `ImportError` naming the exact `pip install google-adk[<extra>]` command, which is
  the message `DatabaseSessionService` and `VertexAiSessionService` both raise (2.2, 2.5).
- `.venv/Lib/site-packages/google/adk/sessions/migration/migrate_from_sqlalchemy_sqlite.py` — the
  module the schema error names. It imports `sqlalchemy` at module scope, so it cannot run in this
  environment (5.1).
- `.venv/Lib/site-packages/google/adk/sessions/vertex_ai_session_service.py` —
  `VertexAiSessionService(project=None, location=None, agent_engine_id=None, *,
  express_mode_api_key=None)`; the first real call raises `ImportError` naming the `gcp` extra (2.5).
- `.venv/Lib/site-packages/google/adk/errors/_stale_session_error.py` — `StaleSessionError`
  subclasses `ValueError`, and the source says so for backwards compatibility (4.1).

**Two facts read out of Python itself, not out of the ADK:**

- `sqlite3.connect(..., timeout=5.0)` is the driver's default and it sets the busy timeout, which
  `aiosqlite` passes through and the session service does not override. SQLite's own default is zero
  (3.3).
- `PRAGMA foreign_keys` defaults to **off**, so a cascade only fires on a connection that switched it
  on (1.2, 6.1).

**Three live commands, re-run today:**

```bash
uv run python -c "import google.adk; print(google.adk.__version__)"
uv run python -c "from google.adk.sessions import __all__ as a; print(sorted(a)); print('SqliteSessionService' in a)"
uv run python -c "from google.adk.cli.service_registry import get_service_registry as r; print(type(r().create_session_service('sqlite:///./x.sqlite3')).__name__)"
```

---

## §9 Say it in an interview

*"The persistent-sessions day is the one where I stopped believing that 'we use a database' is an
answer. Swapping `InMemorySessionService` for the SQLite one is genuinely a single constructor
argument on the runner — the agent, the tools and the prompts are untouched — and everything
interesting is what that one line does not solve.*

*The first surprise was getting hold of the class at all. `SqliteSessionService` is not in
`google.adk.sessions.__all__`, so the obvious import raises, while the framework's own CLI reaches it
by importing the module directly. Meanwhile the documentation tells you to use the general database
service with a `sqlite+aiosqlite://` URL, and on our version that scheme has no registered factory,
so it falls through to a class that needs SQLAlchemy, which is an optional extra we do not install.
The answer was to install nothing, use the SQLite service, and put the unexported import in exactly
one module with the version and date beside it and a test that fails on upgrade.*

*Then the measurements, and two of them went against what I expected. Four processes doing a hundred
appends to one SQLite file lost nothing and took four seconds, because Python's driver defaults to a
five-second busy timeout, so writers queue rather than fail — the folklore about SQLite and
concurrency is mostly about SQLite's own default of zero, which nobody uses. And enabling WAL changed
nothing there, because WAL separates readers from writers and that workload was four writers. What
does break it is anything holding the file longer than the timeout, and all four workers died at
*construction*, because the ADK's constructor reads the file to check the schema version.*

*The part I would put in a design doc is that most of the failures in this area do not raise. An
in-memory store after a restart returns `None`, which is what it also returns for a session that
never existed. A relative path resolved from the wrong directory is a second empty database. A
migration that dropped a column reported matching row counts and had lost a thousand transcripts. A
file copy of a live store restored zero of two hundred turns and opened perfectly. In every one of
those the check somebody had written was structurally incapable of seeing the bug, so the discipline
I took away is that verification has to read: open the thing and get a known sentence back out.*

*And the one that is a policy question rather than an engineering one — deleting a customer. The API
has `delete_session`, and looping it over `list_sessions` removes every conversation and every turn
and looks complete. It leaves the user-scoped state row exactly where it was, because that row is
defined as outliving conversations, and there is no `delete_user` anywhere on the interface. So the
last statement of an erasure is one you write yourself, and you verify it by counting rows in the
file rather than by trusting a return value — including a count of somebody else's rows, because an
erasure that took too much is a different incident."*

---

## §10 Done when

See [`CHECKLIST.md`](CHECKLIST.md). Every box is ticked because you ran the thing, not because you
read about it. `./m done 47` refuses to commit until they are.

---

## §11 Ledger & commit

**`docs/PROGRESS.md` — append this row** (fill in the hash after committing):

```markdown
| 47 | 2026-09-05 | ADK-29 | 20 (+1 paper) | <hash> | ⚠️ |
```

**`docs/PACKAGES.md` — no new rows today.** No package is added and no pin is moved. `sqlite3` is in
the standard library and `aiosqlite` is already a dependency of `google-adk==2.7.1`. The package this
day deliberately does **not** install is SQLAlchemy, via `uv add "google-adk[db]"`; if a future day
needs it — Postgres instead of a file — that is the command, and it earns a dated row then.

**`docs/PAPERS.md` — no new rows today.** *Principles of transaction-oriented database recovery*
(`doi:10.1145/289.291`) was verified on 2026-09-04 and its row already exists, naming this day and
`days/day-47-persistent-sessions/papers/01-transaction-oriented-recovery.md`.

**`docs/SKILL_PROVENANCE.md` — no new rows today.**

**Git commit message:**

```
day 47: persistent sessions — database-backed — closes ADK-29
```
