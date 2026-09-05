---
day: 47
paper: "doi:10.1145/289.291"
title: "Principles of transaction-oriented database recovery"
ids: ["ADK-29"]
level: production
prerequisites: ["../parts/03-writes-that-survive/3.1-the-ticket-torn-in-two.md"]
prev: "../parts/07-in-production/7.1-the-backup-nobody-restored.md"
next: ""
---

# Principles of transaction-oriented database recovery

## One-line answer

This is the paper that turned "did the write go through?" from an argument into a question with a
defined answer: it named the transaction as the unit of work, gave that unit four properties —
atomicity, consistency, isolation, durability — and set out the logging and recovery methods that
make the properties true after a crash.

## The story

The cash machine takes your card, thinks for a while, and shows a message you do not have time to
read before the screen clears. No cash comes out. Your phone buzzes: **debited, ₹4,000.**

You go into the branch the next morning.

The first person says the transaction failed, so the money will come back on its own in three or four
working days. The second person, a desk further along, says the money has left your account, which
means the transaction succeeded, and you should file a claim against the cash machine. The
supervisor says that the machine's own record is what settles it and the machine's record comes at
the end of the day.

Three people, three answers, and none of them lying. They disagree about **when a transfer becomes a
fact.** One of them thinks it is when the money leaves. One thinks it is when the cash is counted
out. One thinks it is when the day's tally is done. Until they share an answer to that question, they
cannot even have the argument properly, because they are not arguing about the same event.

What eventually fixes this is not a better machine. It is everybody agreeing, in advance and in
writing, on the exact moment a transfer counts — and keeping a record from which that moment can be
reconstructed after the power comes back.

## The idea in plain language

Before this paper, every database system had recovery code, and every one of them meant something
slightly different by "the write happened". There was a great deal of engineering and very little
shared vocabulary, so two systems could not be compared, a claim could not be checked, and a student
could not be taught the subject as a subject.

The paper's first contribution is the **transaction**: a sequence of operations that the system
treats as one unit of work, with a beginning, and an end that is either a **commit** — make it
permanent — or an **abort** — make it as though it never began.

Its second and more famous contribution is the four properties that unit is given. The initials
spell **ACID**, and the reason the acronym is worth knowing is not that it is catchy; it is that
each letter is a promise a reviewer can hold you to.

| Letter | Property | What it promises |
| --- | --- | --- |
| A | Atomicity | All of the transaction happens, or none of it. There is no observable half. |
| C | Consistency | A transaction takes the database from one valid state to another valid state. |
| I | Isolation | A transaction behaves as though it ran alone, whatever else is running. |
| D | Durability | Once committed, it survives — including a crash a moment later. |

Two of those need a second sentence, because they are the ones people mis-state.

**Consistency is about your rules, not the database's.** The database enforces what you declared —
keys, types, foreign keys — and it has no idea that a session's `turn_count` should equal the number
of its events. Consistency is the transaction being written so that the rule holds at both ends; the
database's job is to make sure nobody sees the middle. That is exactly
[3.1](../parts/03-writes-that-survive/3.1-the-ticket-torn-in-two.md)'s finding, and exactly
[5.2](../parts/05-shape-and-size/5.2-the-migration-that-passed.md)'s: a store can satisfy every
constraint it knows about and still be wrong.

**Durability means committed, not received.** A write you sent and a write that committed are
different things, which is the whole of
[3.2](../parts/03-writes-that-survive/3.2-what-a-restart-still-loses.md): the streamed partials were
sent, seen by a customer, and never committed, so the store owes them nothing.

The third contribution is the part people forget the paper has, and it is the half that makes the
promises real: a **taxonomy of the failures** a recovery method has to survive, and the logging
methods that survive them.

## Why Sutra needs it

Because every mechanism in this day is one of this paper's, and the vocabulary is how you argue about
them.

[3.1](../parts/03-writes-that-survive/3.1-the-ticket-torn-in-two.md) showed one `append_event`
writing an event row, patching the session's state and moving `update_time`, inside one transaction,
and named the word *atomic*. That is A.
[4.1](../parts/04-two-workers/4.1-refused-not-overwritten.md) showed a second writer refused because
its copy was stale — an isolation problem, solved optimistically. That is I.
[3.2](../parts/03-writes-that-survive/3.2-what-a-restart-still-loses.md) drew the line at the last
committed event. That is D, and the line is exactly where this paper puts it.
[7.1](../parts/07-in-production/7.1-the-backup-nobody-restored.md) is the paper's third failure class
— media failure — which no amount of logging survives and only a second copy does.

The practical value is that these words let you ask a precise question in a design review. "Is this
safe?" has no answer. "Is this atomic, and against which of the three failure classes?" does, and the
answer is checkable.

And Sutra needs the honest half too. This paper is written about **one database system**, and Sutra
is a distributed thing — several instances, an MCP server in another process, a model on somebody
else's machine. Knowing which half of the paper still applies to that is the difference between using
a transaction correctly and reaching for one where none exists.

## The mechanism

Written out as method, in the order the paper builds it.

**One: the transaction paradigm.** Work is bracketed. A transaction begins, does its operations, and
ends in exactly one of two ways: it **commits**, and everything it did becomes permanent and visible;
or it **aborts**, and everything it did is undone as though it never started. There is no third
outcome. A crash in the middle is not a third outcome — it is an abort that the system performs on
the transaction's behalf when it comes back up.

**Two: three classes of failure**, because a method that handles one may be useless against another.

| Class | What happened | What it costs | What survives it |
| --- | --- | --- | --- |
| Transaction failure | One transaction cannot complete — it aborts, or is aborted | that transaction's work | undoing its changes |
| System failure | The process or the machine stops; volatile memory is lost, the disk is intact | everything not yet on stable storage | a log on stable storage |
| Media failure | The storage itself is lost or damaged | the database | an archive copy plus a log |

The distinction is the useful part. A system failure is survived by a log, because the disk is still
there. A media failure is not survived by a log on that same disk, because the log is on the disk
that went. **They are different problems and they need different equipment**, which is why
[7.1](../parts/07-in-production/7.1-the-backup-nobody-restored.md) is a separate part from
[3.1](../parts/03-writes-that-survive/3.1-the-ticket-torn-in-two.md).

**Three: the log, and the rule that makes it work.** The system keeps a sequential record of what
each transaction changed — enough to undo a change (the old value) and enough to redo it (the new
value). The rule attached to that record is the **write-ahead log protocol**, and it is two clauses:

- before a changed data page may be written to the database, its **undo** information must already be
  on stable storage; otherwise a crash mid-write leaves a change nobody can reverse;
- before a transaction may be considered committed, its **redo** information must already be on
  stable storage; otherwise a crash immediately after the commit loses work the system has promised.

"Write ahead" is the whole idea in two words: **the description of the change reaches durable storage
before the change does.** SQLite's rollback journal, which
[3.1](../parts/03-writes-that-survive/3.1-the-ticket-torn-in-two.md) watched appear on disk with a
size, is the undo half. SQLite's WAL mode, which
[7.1](../parts/07-in-production/7.1-the-backup-nobody-restored.md) measured at 2.3 megabytes, is the
redo half.

**Four: what the buffer manager is allowed to do**, which decides what recovery has to do. Two
independent questions:

- **Steal or no-steal**: may a page changed by a transaction that has not committed be written to the
  database? If yes (*steal*), the buffer manager is free, and recovery must be able to **undo**.
- **Force or no-force**: must every page a transaction changed be written to the database before its
  commit returns? If yes (*force*), a commit is expensive, and recovery never needs to **redo**.

Those two questions crossed give four strategies, and they are the paper's most useful table because
they explain why real systems look the way they do.

| Strategy | Recovery must undo | Recovery must redo | Commit cost |
| --- | --- | --- | --- |
| No-steal / force | no | no | high — every page flushed at commit |
| Steal / force | yes | no | high |
| No-steal / no-force | no | yes | low, but the buffer is constrained |
| **Steal / no-force** | **yes** | **yes** | **low** |

Steal/no-force is the fast one and the demanding one, and it is what serious engines choose: the
buffer manager does what it likes, commits are cheap because they only force the *log*, and the price
is that recovery must be able to do both halves.

**Five: checkpoints.** Without them, recovery after a system failure would have to read the log from
the beginning of time. A checkpoint writes a marker plus enough state that recovery can start from
there instead. The paper's point is that checkpoints trade recovery time against runtime cost, and
that the cheaper kinds — the ones that do not stop the world — buy their cheapness by making recovery
do more work.

**Six: recovery itself**, which is now a short algorithm. On restart, read the log from the last
checkpoint. Sort the transactions into those that committed before the crash — the **winners** — and
those that did not — the **losers**. **Redo** the winners, so that committed work that had not
reached the database gets there. **Undo** the losers, so that uncommitted changes that had reached
the database get reversed. When both passes finish, the database contains exactly the committed work
and nothing else, and that is the definition of correct that the paper set out to make sayable.

## The paper in one demo

One file, no framework, no model, standard library only. A session store with the one invariant the
paper is about, a write that is two rows, and a switch that removes the transaction boundary.

```text
days/day-47-persistent-sessions/lab/papers/transaction-oriented-recovery/
└── store.py     the store, the crash, the recovery check, and the ablation
```

The invariant is deliberately tiny: **`sessions.turn_count` equals the number of rows in `events` for
that session.** One turn is two rows in two tables. Either both land or neither does.

```python
# days/day-47-persistent-sessions/lab/papers/transaction-oriented-recovery/store.py
"""The paper in one file: a session write crashed on purpose, then recovered.

One turn of a conversation is two rows - the event itself, and the session
counter that says how many turns there are. Writing one without the other is a
torn write. The paper's contribution is the boundary that makes those two rows
one indivisible step, so a process killed between them leaves the store as if
the write had never started.

    python store.py                    # the boundary is on
    python store.py --no-transaction   # the ablation: same code, no boundary

Each run rebuilds the store from nothing, writes two complete turns, then spawns
a child process that starts a third turn and dies between the two rows. The
parent reopens the file and checks one invariant: turn_count == number of events.
Exit code 0 when the store is consistent, 1 when a half-written turn survived.

Zero model calls. Standard library only - sqlite3 ships with Python.
"""

from __future__ import annotations

import os
import sqlite3
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent
DB = HERE / "desk.sqlite3"
SESSION = "ticket-4521"

SCHEMA = """
CREATE TABLE IF NOT EXISTS sessions (
    id         TEXT PRIMARY KEY,
    turn_count INTEGER NOT NULL
);
CREATE TABLE IF NOT EXISTS events (
    session_id TEXT NOT NULL,
    seq        INTEGER NOT NULL,
    text       TEXT NOT NULL,
    PRIMARY KEY (session_id, seq)
);
"""
```

**Line by line:**

- The docstring names the ablation in its second paragraph, because a demo whose switch is only in
  the argument parser is a demo somebody will run one arm of.
- `os` is imported for `os._exit` alone. Nothing else in this file needs it, and that one call is the
  reason it is here — see the walkthrough on `append`.
- `subprocess` is imported because the crash has to happen in a **different process**. A crash
  simulated inside the same process cannot be honest: the connection object, its buffers and its
  `finally` blocks all survive.
- `SCHEMA` is two tables and nothing else. There is no `event_data`, no `app_name`, no timestamp,
  because none of them are the paper's contribution and every one of them would be a line a reader
  has to hold in their head. If a column could be deleted and the claim still landed, it is deleted.
- `turn_count INTEGER NOT NULL` on `sessions` is the second row of the write, and it is the entire
  reason there is an invariant to break. Storing it would be a mistake in a real system — a count you
  can derive is a count you can disagree with — and here it is the point: **the paper is about facts
  that must be true together.**
- `PRIMARY KEY (session_id, seq)` gives the events an order, so the report below can print the
  transcript and a reader can see which turn is the half-written one.

```python
# store.py (continued)
def connect() -> sqlite3.Connection:
    """Open the store in autocommit mode so the transaction boundary is ours alone.

    isolation_level=None stops the driver from opening and closing transactions
    behind our back, which is the only way the ablation can be honest: with the
    driver managing transactions, turning ours off would still leave one.
    """
    conn = sqlite3.connect(DB, isolation_level=None)
    conn.row_factory = sqlite3.Row
    return conn


def reset() -> None:
    """Delete the store and its journal, then create the two empty tables."""
    for suffix in ("", "-journal", "-wal", "-shm"):
        Path(str(DB) + suffix).unlink(missing_ok=True)
    conn = connect()
    conn.executescript(SCHEMA)
    conn.execute("INSERT INTO sessions (id, turn_count) VALUES (?, 0)", (SESSION,))
    conn.close()
```

**Line by line:**

- `isolation_level=None` is the single most important line in the demo, and the docstring explains
  why at length because without it the ablation is a lie. Python's `sqlite3` driver defaults to
  opening a transaction before the first write and committing on `commit()`
  ([3.1](../parts/03-writes-that-survive/3.1-the-ticket-torn-in-two.md)). Leave that on and the
  `--no-transaction` arm still runs inside a transaction, and the demo proves nothing.
- `conn.row_factory = sqlite3.Row` makes rows subscriptable by column name, so the report reads
  `row["turn_count"]` instead of `row[0]`. In a teaching file that is the difference between a reader
  following the invariant and counting tuple positions.
- `reset()` deletes the journal and write-ahead files as well as the database. A leftover `-journal`
  from a previous crashed run would be applied on the next open, and the demo would appear to fix
  itself.
- `unlink(missing_ok=True)` rather than a `try/except FileNotFoundError`, because three of those four
  files are absent on any given run and absence is not an error here.
- `executescript(SCHEMA)` is used for the schema and **nowhere else**, because `executescript` commits
  any open transaction before it runs — the trap
  [5.2](../parts/05-shape-and-size/5.2-the-migration-that-passed.md) names. Here there is no open
  transaction, so it is safe.
- The session row starts at `turn_count = 0` with no events, which is a consistent state. The demo
  begins correct so that any inconsistency at the end came from the crash.

```python
# store.py (continued)
def append(text: str, *, atomic: bool, crash: bool) -> None:
    """Append one turn: insert the event row, then bump the session counter.

    Those two rows are one fact - this conversation now has N turns, and here
    they are. `atomic` decides whether they are also one write.
    """
    conn = connect()
    seq = conn.execute(
        "SELECT COALESCE(MAX(seq), 0) + 1 AS n FROM events WHERE session_id = ?",
        (SESSION,),
    ).fetchone()["n"]

    if atomic:
        conn.execute("BEGIN IMMEDIATE")

    conn.execute(
        "INSERT INTO events (session_id, seq, text) VALUES (?, ?, ?)",
        (SESSION, seq, text),
    )

    if crash:
        journal = Path(str(DB) + "-journal")
        print(f"  child: wrote event seq={seq}, about to die before the counter")
        print(f"  child: rollback journal on disk: {journal.exists()}")
        sys.stdout.flush()
        os._exit(9)  # no commit, no rollback, no close, no finally - a real death

    conn.execute("UPDATE sessions SET turn_count = turn_count + 1 WHERE id = ?", (SESSION,))
    if atomic:
        conn.execute("COMMIT")
    conn.close()
```

**Line by line:**

- `*, atomic, crash` are keyword-only. Two booleans in a row is the argument list people get the
  wrong way round, and `append(text, True, False)` would be unreadable at the call site.
- The `SELECT COALESCE(MAX(seq), 0) + 1` runs **before** the `BEGIN`, deliberately: it is a read that
  informs, and putting it inside would lengthen the transaction for no benefit. In a system with
  concurrent writers it would belong inside, and that difference is
  [4.2](../parts/04-two-workers/4.2-the-read-that-raises-nothing.md)'s subject.
- `if atomic: conn.execute("BEGIN IMMEDIATE")` — the **entire** ablation, one statement. `IMMEDIATE`
  rather than a plain `BEGIN` so the write lock is taken at the start rather than at the first write;
  with one process it makes no difference to the outcome and it is the form
  [3.1](../parts/03-writes-that-survive/3.1-the-ticket-torn-in-two.md) told you to write.
- The `INSERT` is row one of the two-row fact. Under `isolation_level=None` **and** no `BEGIN`, this
  statement commits by itself, immediately — which is exactly what makes the ablation arm torn.
- `print(... journal.exists())` before dying is the paper's mechanism made visible: with the
  boundary on, a rollback journal is on the disk at this instant, holding the pages needed to put the
  file back. With it off there is no journal, because there is nothing to roll back.
- `sys.stdout.flush()` before `os._exit`, because `os._exit` does not flush buffers and the two lines
  above would otherwise never appear.
- `os._exit(9)` and not `sys.exit(9)`. `sys.exit` raises `SystemExit`, which unwinds the stack, runs
  `finally` blocks, and closes the connection — and a closed connection rolls back. That would make
  the ablation arm pass, for the wrong reason, and the demo would be worthless. **`os._exit` is the
  honest kill**, and this is the same choice
  [3.2](../parts/03-writes-that-survive/3.2-what-a-restart-still-loses.md) made.
- The `UPDATE` is row two. Everything between the `INSERT` and here is the window the paper exists to
  close.
- `COMMIT` is where the two rows become one fact. Before it, nothing is visible to another connection
  and nothing survives a crash; after it, both are permanent. That instant is the paper's whole
  subject.

```python
# store.py (continued)
def journal_bytes() -> int:
    """Size of the rollback journal, or -1 when there is no journal file."""
    journal = Path(str(DB) + "-journal")
    return journal.stat().st_size if journal.exists() else -1


def report(atomic: bool) -> int:
    """Reopen the store cold and check the invariant. Returns the exit code."""
    before = journal_bytes()
    conn = connect()
    turn_count = conn.execute(
        "SELECT turn_count FROM sessions WHERE id = ?", (SESSION,)
    ).fetchone()["turn_count"]
    rows = conn.execute(
        "SELECT seq, text FROM events WHERE session_id = ? ORDER BY seq", (SESSION,)
    ).fetchall()
    conn.close()

    torn = turn_count != len(rows)
    print()
    print(f"boundary        : {'BEGIN IMMEDIATE .. COMMIT' if atomic else 'none (ablation)'}")
    print(f"journal at crash: {before} bytes" if before >= 0 else "journal at crash: absent")
    print(f"turn_count      : {turn_count}")
    print(f"events stored   : {len(rows)}  {[r['text'] for r in rows]}")
    print(f"verdict         : {'TORN - half a turn survived' if torn else 'consistent'}")
    return 1 if torn else 0


def main() -> int:
    """Run one arm end to end: two clean turns, one crash, then recovery."""
    atomic = "--no-transaction" not in sys.argv

    if "--child" in sys.argv:
        append("reset the print spooler", atomic=atomic, crash=True)
        return 0  # unreachable: the child calls os._exit

    reset()
    append("printer offline since tuesday", atomic=atomic, crash=False)
    append("still offline after a reboot", atomic=atomic, crash=False)
    print("parent: two complete turns committed")
    sys.stdout.flush()

    args = [sys.executable, str(HERE / "store.py"), "--child"]
    if not atomic:
        args.append("--no-transaction")
    done = subprocess.run(args, cwd=HERE, check=False)
    print(f"parent: child exited with {done.returncode}")

    return report(atomic)


if __name__ == "__main__":
    raise SystemExit(main())
```

**Line by line:**

- `journal_bytes()` is read **before** the connection is opened, and that ordering is the whole
  measurement. Opening the database is what triggers SQLite's recovery: it sees an orphaned journal,
  rolls the pages back, and deletes it. Read the size afterwards and you would always get `-1`.
- `report` opens the store **cold**, in the parent, after the child is gone. That is what makes it a
  recovery check rather than an inspection of state somebody is holding.
- `turn_count != len(rows)` is the invariant, expressed as one comparison. It is the application's
  rule, not the database's — every row is valid, every key is unique, and the store still disagrees
  with itself. That is the paper's *consistency* in one line of Python.
- The transcript is printed rather than counted, so a reader can see *which* sentence is the extra
  one in the torn arm and recognise it as the turn the child was in the middle of.
- `atomic = "--no-transaction" not in sys.argv` makes the boundary the **default**. A demo whose safe
  behaviour is opt-in teaches the wrong habit even when the reader never notices.
- `if "--child" in sys.argv` makes one file both parent and child. `sys.executable` re-runs the same
  interpreter, so it works under `uv run` without the child needing its own environment.
- The `--no-transaction` flag is forwarded to the child explicitly, because the child is a fresh
  process and inherits nothing from the parent's parsing. Forgetting that line is how an ablation
  quietly stops ablating.
- `check=False` on `subprocess.run`, because the child is **expected** to exit non-zero — it dies
  with code 9. `check=True` would raise and hide the result.

Run both arms:

```bash
cd days/day-47-persistent-sessions/lab/papers/transaction-oriented-recovery
uv run python store.py; echo "exit: $?"
uv run python store.py --no-transaction; echo "exit: $?"
```

**Line by line:**

- `cd` first, because the store is written beside the script and the child is launched with `cwd=HERE`.
- The first command is the boundary arm and the second is the ablation. One flag, no other difference.
- **Zero model calls, and no third-party package.** `sqlite3` is in the standard library, so this demo
  runs on a clean Python with no network.

Measured on 2026-09-05. The boundary arm first:

```text
parent: two complete turns committed
  child: wrote event seq=3, about to die before the counter
  child: rollback journal on disk: True
parent: child exited with 9

boundary        : BEGIN IMMEDIATE .. COMMIT
journal at crash: 8720 bytes
turn_count      : 2
events stored   : 2  ['printer offline since tuesday', 'still offline after a reboot']
verdict         : consistent
exit: 0
```

And the ablation, same code, one statement removed:

```text
parent: two complete turns committed
  child: wrote event seq=3, about to die before the counter
  child: rollback journal on disk: False
parent: child exited with 9

boundary        : none (ablation)
journal at crash: absent
turn_count      : 2
events stored   : 3  ['printer offline since tuesday', 'still offline after a reboot', 'reset the print spooler']
verdict         : TORN - half a turn survived
exit: 1
```

Read the two runs side by side, because everything the paper claims is in the difference.

**`rollback journal on disk: True` against `False`.** At the instant the child died, the boundary arm
had an 8 720-byte file beside the database holding the original contents of every page it was about
to change. That file is the write-ahead protocol on your disk with a size: the undo information
reached stable storage *before* the change did, which is the only reason the change could be
reversed by a process that had not yet been started.

**`turn_count: 2` and `events stored: 2` against `2` and `3`.** In the boundary arm the half-written
turn is not repaired — it is *absent*. The store came back exactly as it was before the crashed
transaction began, which is the paper's definition of an abort. In the ablation the insert had
already committed on its own, so the event is permanent and the counter that describes it is not.

**And nothing is corrupt in either run.** The torn store passes every check SQLite can perform: the
row is well formed, the primary key is unique, the column types are right. It is *wrong* — in a way
only the application's own rule can see, and it will stay wrong for as long as the file exists,
because there is no log from which anybody could work out what should have happened.

## When it breaks

**Where the paper's claim does not hold, starting with the one that matters most.**

**The transaction boundary is one database.** Everything in this paper assumes the unit of work sits
inside a single system that owns its own log. Sutra's turn does not: it touches the session store, an
MCP server in another process, and a model on somebody else's machine. There is no transaction that
spans those. The desk can commit a session write and fail to send the email, and no `COMMIT` anywhere
helps, because the email is not in the log. Day 42's paper
[*A note on distributed computing*](../../day-42-serving-agents-over-mcp/papers/01-a-note-on-distributed-computing.md)
is the argument about why pretending otherwise fails, and Day 44's
[idempotency](../../day-44-client-hardening/parts/01-what-may-be-repeated/1.1-the-button-you-can-press-twice.md)
is what the field uses instead.

**Isolation as written is expensive, and almost nobody buys it.** The I promises a transaction behaves
as though it ran alone. Making that true for every pair of transactions costs concurrency, so real
databases ship weaker default levels — read committed, snapshot isolation — under which specific
anomalies are possible and documented. A system claiming "we use ACID transactions" has usually not
checked which isolation level it is actually running at, and the anomalies that level permits are the
bugs it will have.

**Durability is a promise about a device.** A commit returns when the log record is on *stable
storage*, and whether the disk you have is stable storage is a hardware question. A drive with a
volatile write cache that lies about flushing turns D into an aspiration, and the failure is
invisible until a power cut. The paper is not wrong; it is stating a requirement that somebody below
you has to actually meet.

**Consistency is the letter that does no work.** A, I and D are properties the system provides. C is a
property *you* provide, by writing transactions that take valid states to valid states, and the
system's contribution is only that nobody sees the middle. It is in the acronym largely because the
acronym needed a vowel, and treating it as a guarantee is how
[5.2](../parts/05-shape-and-size/5.2-the-migration-that-passed.md) happens: every constraint
satisfied, a thousand transcripts gone.

**And what the demo above does not prove.** It proves atomicity against one failure class — a system
failure, in the paper's taxonomy. It says nothing about media failure: delete `desk.sqlite3` and both
arms lose everything equally, because a log on a disk cannot survive the disk.
[7.1](../parts/07-in-production/7.1-the-backup-nobody-restored.md) is the equipment for that class,
and it is separate on purpose.

## In production

**What survived, and it is a great deal.**

**The vocabulary won completely.** "Is that atomic?" is a question every reviewer asks and everybody
understands the same way. ACID is on the front page of database documentation, in interview questions,
and in the marketing of systems that do not provide it — which is itself evidence of how thoroughly
the terms became the standard by which people expect to be judged. Before this paper there was no
compact way to say what a system promised.

**Write-ahead logging is in every serious engine**, and it is usually the default. SQLite has both
halves — a rollback journal by default and a WAL mode you switch on, and this day measured both:
8 720 bytes of undo journal in the demo above, 2.3 megabytes of redo log in
[7.1](../parts/07-in-production/7.1-the-backup-nobody-restored.md). Postgres has one. MySQL's InnoDB
has one. The steal/no-force strategy the paper identified as the demanding one is the one they all
chose, for the reason the table gave: it is the fast one, and recovery code is written once.

**Undo/redo recovery became a standard algorithm.** The winners-and-losers pass this paper describes
was refined into the recovery method that modern engines implement, with fine-grained logging and
restartable recovery, and the shape is still recognisably this one: read forward from a checkpoint,
redo what committed, undo what did not.

**What did not survive.**

**The assumption that one database is the transaction boundary.** This is the big one, and it was
broken not by a better idea but by systems getting bigger than one database. Distributed transactions
that hold a lock across two systems while both agree to commit are available, well understood, and
largely avoided in application architecture, because they turn two systems' availability into a
product rather than a maximum. What replaced them is not a stronger guarantee — it is a weaker one
applied more carefully: break the work into steps, make each step safe to repeat, and compensate for
the ones that cannot be undone. Sutra's version of that is Day 44's idempotency key and Day 36's task
handle.

**Strict isolation as a default.** The paper's I is serialisability. What shipped is a menu, with the
cheap options at the top and the strong one rarely selected, and a generation of engineers who have
never checked which one they are using.

**And one thing the field added that is not here.** The paper is about a system recovering *itself*.
It says nothing about recovering from a correct transaction that should not have been run — the
migration that passed, the erasure that took too much, the deploy that wrote nonsense. No amount of
ACID protects against a committed mistake, and the equipment for that is a second copy and a restore
drill, which is why this day ends at
[7.1](../parts/07-in-production/7.1-the-backup-nobody-restored.md) and not here.

**The review comment a senior engineer leaves:** *"this closes the ticket in one statement and appends
the transcript event in another, with an `await` between them, and the design doc says the write is
atomic. Atomic against what? Those are two transactions, so a crash in between leaves a closed ticket
with no record of who closed it — and if the second one goes to a different system entirely then
there is no transaction available at all and we need an idempotency key instead. Say which failure
class we are protecting against, in the doc."*

**The interview question:** *"what does ACID mean and which letter do people get wrong?"* The honest
answer: *"Atomicity — all or nothing, no observable half. Isolation — a transaction behaves as though
it ran alone. Durability — once committed, it survives a crash. And consistency, which is the one
people get wrong: it is not a guarantee the database gives you, it is a property of the transactions
you write. The database enforces the constraints you declared and has no idea that a session's turn
count should equal its number of events, so a store can satisfy every constraint and still be wrong.
I proved that to myself with a two-table store and a process killed between the two rows of one
logical write: with a `BEGIN IMMEDIATE ... COMMIT` the store came back with two turns and a count of
two, without it three turns and a count of two, and neither file was corrupt in any sense a database
integrity check can detect. The other half worth saying is what has stopped applying: the paper
assumes a single system owns the transaction, and once your work spans a database and a service in
another process there is no transaction — you get idempotency and compensation instead."*

## Check yourself

```bash
cd days/day-47-persistent-sessions/lab/papers/transaction-oriented-recovery
uv run python store.py; echo "exit: $?"
uv run python store.py --no-transaction; echo "exit: $?"
```

Now change `os._exit(9)` to `sys.exit(9)` and run the ablation arm again. It passes. Work out which
of the paper's mechanisms the Python interpreter performed on your behalf, and say why that makes the
test worthless.

**Out loud, without scrolling up:** say what this paper claimed in one sentence, name its three
failure classes and which one a log cannot survive, and say which of the four letters is a promise
you make rather than one you are given.
