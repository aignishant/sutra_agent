---
day: 36
paper: "doi:10.1145/53990.54016"
title: "Promises: linguistic support for efficient asynchronous procedure calls in distributed systems"
ids: ["MCP-14"]
level: production
prerequisites: ["../parts/03-the-handle/3.1-a-name-the-server-mints.md"]
prev: "../parts/06-in-production/6.3-the-store-is-the-stateful-thing.md"
next: ""
---

# Promises: linguistic support for efficient asynchronous procedure calls in distributed systems

> **Promises: linguistic support for efficient asynchronous procedure calls in distributed systems**
> · `doi:10.1145/53990.54016` · 1988 · PLDI '88, pages 260–267 ·
> `https://doi.org/10.1145/53990.54016`

## One-line answer

A call to something far away should hand the caller a **placeholder for the answer** straight away, so
the caller keeps working and collects the answer only when it actually needs it — which is the task
handle you spent today building, proposed thirty-eight years earlier and given a type.

## The story

You are having two rooms done and the builder will not order the windows until the doors have arrived.

The doors come from one place and the windows from another. Neither supplier has heard of the other.
Nothing about the doors changes anything about the windows. But the builder works in one order, from
the top of the list downwards, so he rings the door people, waits until the doors turn up, and only then
rings the window people and waits again.

You point this out and he is not being difficult — this is simply how he has always worked, and it has
always been fine, because when everything is in the van outside there is no waiting to speak of. It only
becomes ridiculous when the things you are waiting for are somewhere else and slow.

The whole job takes three weeks instead of one, and every day of the difference is the builder standing
about, holding a list, waiting for permission to do the next thing on it.

## The idea in plain language

By 1988 the way one program called another program on a different machine was well established. It was
the **remote procedure call**: you write what looks like an ordinary function call, the system packs up
the arguments, sends them across the network, waits for a reply, unpacks it and returns it. Day 15's
paper part
[`Implementing remote procedure calls`](../../day-15-toolsets-and-openapi/papers/01-implementing-remote-procedure-calls.md)
is where that idea was built.

It was a good idea and it had one property nobody could get around: **it blocks**. The caller stops at
the call and does nothing until the answer comes back. Locally that is invisible. Across a network it is
the builder standing in the hall, and if you have three independent calls to make you pay for all three
in sequence even though the machines answering them have never heard of one another.

This paper proposes the fix, and the shape of the fix is what makes it worth reading now: it is **a
type**.

A **promise** is a value you can hold that stands for an answer that has not arrived. The call returns
one immediately. The caller carries on. Later, when it genuinely needs the answer, it **claims** the
promise: if the answer has arrived, it gets it at once; if not, it waits then. The promise has two
states — **blocked** while the answer is outstanding, and **ready** once it has arrived — and claiming a
ready promise costs nothing.

Three things about that design are worth naming in plain words, because they are the reasons it
survived.

**It is typed.** A promise for a number is a different thing from a promise for a ticket, and the
compiler knows. The alternative designs of the era handed you an untyped token and left you to remember
what it stood for — which is exactly the position an MCP client is in today when it holds a `taskId`
string, and exactly why part [3.1](../parts/03-the-handle/3.1-a-name-the-server-mints.md) had to be
careful about what a handle is allowed to mean.

**Failures come back too.** If the far end raises an error, that error is delivered to the caller **at
the moment of claiming**, in the normal way errors are delivered. The failure is not lost because the
caller had walked away, and it is not delivered at some random earlier moment either. Today's
equivalent is the `failed` status carrying the JSON-RPC error, collected by whoever polls.

**The waiting moves.** Nothing gets faster. The far end takes exactly as long as it always did. What
changes is **who waits and when** — and it turns out that almost all of the cost of blocking was the
waiting you did before you needed to.

The paper pairs promises with a second idea, **call-streams**: a channel on which a caller can send a
sequence of calls to the same server without waiting for each reply, with the order preserved. Promises
are what make a stream usable, because without them there is nothing to hold for each outstanding call.
Together they allow **pipelining** — a second call sent before the first has answered.

## Why Sutra needs it

Because everything in section 3 of this day is this paper's claim, re-derived from network failures
instead of from language design.

Part [1.1](../parts/01-the-blocking-call/1.1-the-call-you-cannot-leave.md) measured the cost of the
blocking call: a client that gave up at half a second while the server finished the correct answer a
second later and threw it away. Part
[3.1](../parts/03-the-handle/3.1-a-name-the-server-mints.md) replaced it with a handle returned in
milliseconds. That is the same move — hand the caller a stand-in immediately — and part
[4.1](../parts/04-the-tasks-extension/4.1-four-messages-on-the-wire.md)'s `CreateTaskResult` is that
move written into a protocol.

Read the paper **after** the parts, which is what this directory is for. You have already hit the
problem, built the mechanism and found its sharp edges. Now you can see which half of the 1988 proposal
you reinvented, and which half the field quietly left behind.

## The mechanism

The proposal has three pieces, and it is worth being precise about how they fit.

**One — the promise as a first-class typed value.** A stream call does not return the callee's result.
It returns a promise whose type is parameterised by the result's type. That value can be stored in a
variable, put in a data structure, and passed to another procedure. This is the piece that made it a
*linguistic* proposal rather than a library: the type system knows the difference between an answer and
a claim on an answer, so the compiler can stop you using one where the other belongs.

**Two — the two states, and `claim`.** A promise begins **blocked** and becomes **ready** when the reply
arrives. `claim` is the only way to get the value out. On a ready promise it returns immediately; on a
blocked one it waits. The important consequence is that the waiting is now **at the point of use**
rather than at the point of call, and in most programs those are far apart — which is where the saving
comes from. Claiming twice is allowed and cheap, because a ready promise stays ready. That is the same
property part [4.2](../parts/04-the-tasks-extension/4.2-five-statuses-and-the-terminal-rule.md) calls
the terminal rule: an answer, once final, does not change, so it can be collected any number of times.

**Three — call-streams and the order guarantee.** A stream is a channel from one caller to one callee
that preserves the order of the calls sent on it. Because a caller does not have to wait for a reply
before sending the next call, a stream can hold several outstanding calls at once, and the replies come
back in order. That is pipelining, and it is where the paper's efficiency argument lives: on a slow
network, the time to make ten calls approaches the time to make one, rather than ten times it.

The shape of the whole thing:

```mermaid
sequenceDiagram
    participant C as caller
    participant S as remote server

    rect rgb(245, 235, 235)
        Note over C,S: blocking RPC - the caller waits at the call
        C->>S: stat(tickets)
        S-->>C: 759
        C->>S: stat(articles)
        S-->>C: 855
        C->>S: stat(drafts)
        S-->>C: 644
    end

    rect rgb(235, 242, 235)
        Note over C,S: promises - the caller waits at the use
        C->>S: stat(tickets)
        C->>S: stat(articles)
        C->>S: stat(drafts)
        Note over C: three blocked promises; the caller is free
        S-->>C: 759
        S-->>C: 855
        S-->>C: 644
        Note over C: claim x3 - all ready, nothing waits
    end
```

Both blocks contain the same three calls and the same three answers. The only difference is where the
caller's own time goes.

## The paper in one demo

Two files. One slow operation, called three times, with a switch that turns promises off.

```text
days/day-36-long-jobs-and-tasks/lab/papers/promises/
├── work.py   # the one slow operation both arms call
└── run.py    # the promise, the two arms, and the switch
```

`work.py` — the callee, deliberately dumb, because the paper's claim is about the caller:

```python
"""The one slow operation both arms of the demo call. Nothing else lives here.

`stat` is a stand-in for any call whose answer takes a while to arrive: a remote
service, a disk scan, an index build. It sleeps and returns a number. It is
deliberately dumb, because the paper's claim is about *the caller*, not about the
callee: the callee is slow either way.
"""

from __future__ import annotations

import time

LATENCY_S = 0.4  # what one remote answer costs, whoever asks for it


def stat(name: str) -> int:
    """Return one 'remote' answer, slowly.

    Args:
        name: which statistic to fetch. Only used to make the answer distinct.

    Returns:
        A deterministic integer, so both arms print the same numbers.
    """
    time.sleep(LATENCY_S)
    return sum(ord(c) for c in name)
```

**Line by line:**

- `LATENCY_S = 0.4` is the cost of one remote answer and it is the **same in both arms**. This is the
  control: nothing the paper proposes makes the callee faster, so if the two arms differed here the
  demo would be measuring the wrong thing.
- `time.sleep` rather than real network traffic, because a network would add noise and a second failure
  mode, and the claim under test has nothing to do with either.
- `sum(ord(c) for c in name)` returns a deterministic integer per name, so both arms print identical
  answers and any difference in the output is definitely about ordering rather than about results.
- The docstring's last sentence is the file's whole reason to exist: *the callee is slow either way.*
- There is nothing else in the file. No client, no promise, no configuration — if it could be deleted
  and the claim would still land, it should be deleted, and this is what is left.

`run.py` — the promise, in nine lines, plus the two arms:

```python
class Promise:
    """A claim on an answer that does not exist yet.

    The paper's contribution in nine lines: the call returns *this* immediately,
    a thread computes the answer, and `claim()` blocks only if the caller asks
    before the answer landed.
    """

    def __init__(self, fn, *args) -> None:
        self._value: int | None = None
        self._thread = threading.Thread(target=self._run, args=(fn, args))
        self._thread.start()

    def _run(self, fn, args) -> None:
        self._value = fn(*args)

    def claim(self) -> int:
        """Block until the answer is here, then hand it over."""
        self._thread.join()
        assert self._value is not None
        return self._value
```

**Line by line:**

- The work starts **inside `__init__`**. Constructing the promise *is* making the call, which is the
  paper's shape: there is no separate "start it" step, because in the proposal the call itself is what
  returns the promise.
- `self._value: int | None = None` is the promise's state. `None` means **blocked** and a value means
  **ready** — the paper's two states, expressed as the cheapest possible thing.
- `self._thread.start()` returns immediately, so `__init__` returns immediately, so the caller has a
  promise and its freedom in the same statement.
- `claim` calls `join()`, which returns at once if the thread has already finished. That is the "claiming
  a ready promise costs nothing" property, obtained for free from the standard library rather than
  hand-rolled.
- `assert self._value is not None` after the join documents the invariant: past the join, the promise is
  ready by construction. It is an assertion rather than a check because a `None` here would mean the
  threading model was wrong, not that the answer was missing.
- What this deliberately does **not** have is the paper's typing. A real `promise[int]` is a distinct
  type the compiler tracks; this is a Python class holding an `int | None`. That gap is the honest
  distance between the proposal and the demo, and it is the subject of *In production* below.

```python
def blocking_arm() -> tuple[list[int], str]:
    """Ask, wait, ask, wait, ask, wait."""
    answers = []
    log = []
    for name in NAMES:
        log.append(f"call {name}")
        answers.append(stat(name))
        log.append(f"  got {name}")
    return answers, " | ".join(log)


def promise_arm() -> tuple[list[int], str]:
    """Ask three times, do the caller's own work, then claim three times."""
    log = []
    promises = []
    for name in NAMES:
        log.append(f"call {name}")
        promises.append(Promise(stat, name))
    log.append("  caller free")
    answers = [p.claim() for p in promises]
    log.append("  claimed 3")
    return answers, " | ".join(log)
```

**Line by line:**

- `blocking_arm` appends `call` and then `got` for each name, so the log itself shows the interleaving:
  every call is immediately followed by its answer, which is what blocking means written down.
- `answers.append(stat(name))` is an ordinary function call, and that is the point — an RPC is designed
  to look exactly like this, which is why the cost is so easy to miss.
- `promise_arm` builds all three promises **before** claiming any. Claiming inside the loop would give
  you the blocking arm with more machinery, and it is the single most common way people accidentally
  un-do a promise-based design.
- `caller free` is logged between the calls and the claims, and it stands for whatever real work the
  caller would be doing there. In this demo there is none, which is the conservative choice: the arms
  differ only in ordering, not in what they compute.
- `[p.claim() for p in promises]` claims in the order the calls were made, so the answers come out in the
  same order as the blocking arm — the demo is comparing like with like.
- Both functions return `(answers, log)` rather than printing, so `main` can prove the answers are equal
  as well as showing that the order of events differs.

The switch:

```python
PROMISES = os.environ.get("PROMISES", "1") != "0"
```

**Line by line:**

- One environment variable, read once. `PROMISES=0` selects the world before the paper; `PROMISES=1`, the
  default, selects the world after it.
- Everything else in the file is shared between the two arms. If the switch also changed the latency,
  the number of calls, or the work done between them, the comparison would prove nothing.

Run both arms:

```bash
cd days/day-36-long-jobs-and-tasks/lab/papers/promises
PROMISES=0 uv run python run.py
PROMISES=1 uv run python run.py
cd -
```

**Line by line:**

- `cd` into the demo's own directory because `run.py` imports `work` as a sibling module — the demo is
  self-contained and does not depend on being run from the repository root.
- Both arms make **zero model calls** and use no network. There is no key, no quota and no cost.
- Run them in this order so the "before" is fresh in your mind when the "after" prints.

Measured on 2026-09-04, the idea **off**:

```text
arm            : blocking
answers        : [759, 855, 644]
order of events: call tickets |   got tickets | call articles |   got articles | call drafts |   got drafts
wall clock     : 1.20s for 3 calls of 0.40s each
```

And the idea **on**:

```text
arm            : promise
answers        : [759, 855, 644]
order of events: call tickets | call articles | call drafts |   caller free |   claimed 3
wall clock     : 0.40s for 3 calls of 0.40s each
```

**Identical answers. 1.20s against 0.40s.** Nothing was made faster: each call still costs `0.40s`, and
the second arm's total is exactly one call's worth because the three overlap. The `order of events` line
is the paper in one line of output — `call, got, call, got, call, got` against `call, call, call, caller
free, claimed 3`.

Note what the number is measuring. It is a program reporting how long it ran, which is a measurement,
not a schedule; the demo exists to produce it, and the comparison is the whole claim.

## When it breaks

The paper's claim does not hold everywhere, and three limits are worth naming.

**When the calls depend on each other.** Promises buy overlap, and there is no overlap to buy if call
two needs call one's answer. A caller that claims immediately after calling has written the blocking arm
with extra objects — and the demo shows exactly this if you move the `claim` inside the loop.

**When the callee cannot take concurrent work.** Three overlapping calls are three units of load
arriving at once. If the server behind them is single-threaded, or is rate limited, or is a database
with a small connection pool, the overlap does not happen and the caller has gained nothing while
making the far end's day harder. Part
[4.3](../parts/04-the-tasks-extension/4.3-polling-is-a-budget.md)'s arithmetic is the modern version of
this warning.

**When the caller does not survive.** This is the limit that matters most for Sutra, and it is the one
the 1988 design does not address, because it was not the problem being solved. A promise lives **in the
caller's process**. If the process dies, the promise dies, and the answer has nowhere to go — which is
precisely the failure part [1.1](../parts/01-the-blocking-call/1.1-the-call-you-cannot-leave.md)
measured. A promise makes a caller *free*; it does not make the work *durable*. That distinction is the
whole reason MCP has task handles rather than promises: a handle is a name in shared storage, and a
promise is an object on a heap.

You can watch that failure in the demo. Kill `run.py` mid-flight in the promise arm and there is nothing
left anywhere — no file, no row, no name — because the promises were local variables.

## In production

**What survived, and it is almost everything.** The word *promise* is in JavaScript, and *future* — the
same idea under the other 1970s name — is in Java, Scala, Rust, Python and C++. Python's
`concurrent.futures.Future` and the `await` in the tool you wrote in part
[2.2](../parts/02-progress/2.2-reporting-from-inside-a-tool.md) are direct descendants: a value standing
for an answer that has not arrived, claimed at the point of use, delivering exceptions at claim time
exactly as the paper specified. The typed placeholder is now so ordinary that most people using it have
never wondered where it came from.

The idea also survived at a completely different scale, which is what today has been about. **Handle
plus poll is the web's version of a promise.** A long HTTP operation returns `202 Accepted` and a status
URL; a cloud API returns an operation id; MCP returns a `CreateTaskResult` with a `taskId`. The
placeholder has become a string in a payload instead of a value on a heap, and the claim has become a
poll instead of a `claim` — but the move is the same one: hand the caller a stand-in immediately and let
it come back for the answer.

**What did not survive.** Two things, and they are instructive.

The **linguistic** half — promises as a language feature with compiler support, integrated into a
specific distributed programming language — did not last in that form. What spread was the *pattern*,
implemented as library types in general-purpose languages, without the language integration the title
argues for. The idea was portable; the vehicle was not.

And **call-streams** essentially vanished. The ordered channel with several outstanding calls, and the
pipelining it enabled, never became a mainstream abstraction. What replaced it is less elegant and more
robust: independent, self-contained requests with no ordering guarantee between them, which is exactly
the constraint MCP adopted on 2026-07-28 when it removed sessions. Day 32's paper part
[`Principled design of the modern Web architecture`](../../day-32-mcp-stateless-core/papers/01-modern-web-architecture.md)
is the argument for why — an ordered stream is a form of shared state between two endpoints, and shared
state is what a stateless architecture trades away on purpose.

**The review comment a senior engineer leaves,** on code that has read the paper and stopped there:
*"These are futures held in the request handler, so they die with the process. That is fine for three
parallel reads and wrong for a re-index — if the pod is rolled we lose the work and the client has
nothing to ask about. In-process promises for things that finish inside one request; a durable handle
for anything that outlives it."*

**The interview question:** *"where do promises and futures come from, and is a task handle the same
thing?"* An honest answer: *"the 1988 PLDI paper on promises proposed them as a typed language feature
for asynchronous remote calls — the call returns a placeholder immediately, the caller carries on, and
claiming it blocks only if the answer has not arrived, with exceptions delivered at claim time. That
half is everywhere now, as futures and promises in essentially every mainstream language. A task handle
is the same move at a different scale, with one crucial difference: a promise lives in the caller's
process and dies with it, while a handle is a name in shared storage that survives the caller, the
connection and the server instance. So the paper solved 'the caller should not have to wait', and MCP's
Tasks extension solves 'and the work should still be findable after everyone involved has restarted'.
The part of the paper the field dropped is call-streams — ordered pipelined calls on a channel — because
that is shared state between two endpoints, which is exactly what stateless protocols give up on
purpose."*

## Check yourself

```bash
cd days/day-36-long-jobs-and-tasks/lab/papers/promises
PROMISES=1 uv run python run.py
cd -
```

Now edit `promise_arm` so that it claims each promise inside the loop, immediately after creating it.
Run it again: the wall clock goes back to the blocking arm's number and the `order of events` line goes
back to `call, got, call, got`. You have written the blocking version using promises, which is the most
common way this idea is un-done in real code.

**Out loud, without scrolling up:** say what a promise's two states are and when claiming one costs
nothing, and say the one property a task handle has that a promise does not.
