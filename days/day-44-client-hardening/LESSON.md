---
day: 44
phase: 6
phase_name: "MCP II: production"
title: "Client hardening — retries, timeouts, no held connections"
ids: ["MCP-22", "MCP-23"]
principles: [1, 2, 4, 7, 8, 10, 11, 13, 14, 15, 16, 17, 18]
kind: lab
plan_version: "v2.2.1"
parts: 19
generated: "2026-09-05"
status: written
lab_scaffolded: true
commit: ""
---

# Day 44 — Client hardening: retries, timeouts, no held connections

> **Yesterday (Day 43):** `sutra_mcp/app.py` became a deploy-shaped ASGI application where any
> instance answers any request, because nothing is kept between them.
> **Today:** the other end of that sentence. The client stops trusting time — every call gets a
> deadline, only the calls that may be repeated are retried, the retries are bounded and jittered and
> eventually switched off, and Sutra keeps a catalogue instead of a connection.
> **Tomorrow (Day 45):** the Phase 6 gate. `tools/mcp_audit.py` reads everything Days 32 to 44 built
> and says whether it is production-shaped.

---

## §1 Where we are

[Day 38](../day-38-failure-and-migration-lab/LESSON.md) was the day things went wrong on purpose. A
server that answered in six seconds instead of fifty milliseconds and a client with no clock. A
reply that arrived twice. An answer about the wrong ticket. A leave application submitted twice
because the page hung. That day ended with a test file, `tests/test_mcp_failures.py`, and an
instruction: **write down which tests stay red and why — that list is Day 44's specification.**

This is the day you earn those back.

The shape of it is the difference between two shopkeepers, both of whom have a supplier who is
sometimes unreliable. The first one rings again the moment the line drops, then again, then again,
and by the afternoon he has ordered the same delivery four times and two of them are on their way. He
is busy and he feels responsible. The second one has a rule written on a card by the phone: reads may
be repeated, orders may not, ring back after this long and not before, and if the line has been dead
three times running then stop ringing and go and find another supplier for today. He looks lazier.
His customers get one delivery.

**A retry is not free and it is not always safe.** That is the sentence the whole day hangs on, and
it is why the order of the sections is what it is: idempotency comes first, before deadlines, before
backoff, before anything. A retry loop that has not answered "may I do this twice?" is a machine for
sending two lorries of cement.

Four things to know before you read a part.

**This day writes one project file and installs nothing.** `sutra/mcp/hardening.py` is yours to type,
in the package [Day 33](../day-33-client-and-transports/LESSON.md) created and
[Day 40](../day-40-filtering-and-allowlists/LESSON.md) added `filtering.py` to. `git diff
pyproject.toml uv.lock` must be empty when you finish.

**Three of the day's most important facts were read out of the installed libraries, not the docs.**
`mcp==1.29.1` gives a client session **no read timeout at all** by default. ADK's Streamable HTTP
path uses `sse_read_timeout` — three hundred seconds — as the per-call deadline rather than the
`timeout=5.0` Day 33 sets. And ADK retries every failed tool call **once**, on any exception, without
asking whether the tool is idempotent. Section 2 part 4 is those three findings with the source
quoted; §8 names every file.

**MCP-23 is a rule about dependency, not about closing sockets.** After
[Day 32's reframe](../day-32-mcp-stateless-core/parts/02-the-reframe/2.1-the-call-that-remembered-you.md)
there is no session on a connection, so a held connection buys nothing and costs a process or a
socket. But section 5 measures what reconnecting actually costs — about a second per request on stdio
against single-digit milliseconds of work — and states the rule in the form that survives that
measurement: **nothing on a connection may be load-bearing.**

**And the day ends where Principle 10 says it must.** Section 6 is what the client says when every
deadline has fired and every attempt is spent. A hardened client fails *more often and faster* than a
naive one, and all of that is a net loss if the top of the stack returns `None`.

---

## §2 The map

Nineteen parts in six sections, plus one paper. This is a two-ID day, so sections 1 to 4 are MCP-22
taken in the order the decisions actually have to be made — *may I repeat this*, *how long do I
wait*, *how long between attempts*, *when do I stop* — section 5 is MCP-23, and section 6 is where
both IDs meet in one policy module. The day climbs `foundation → working → production`.

### Section 1 — `01-what-may-be-repeated`: the question that comes before all the others (MCP-22)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [The button you can press twice](parts/01-what-may-be-repeated/1.1-the-button-you-can-press-twice.md) | Idempotency, and two closure emails against one | `foundation` |
| 1.2 | [A timeout is an unknown, not a failure](parts/01-what-may-be-repeated/1.2-a-timeout-is-an-unknown.md) | Three worlds, one sentence | `foundation` |
| 1.3 | [The line drawn through every call Sutra makes](parts/01-what-may-be-repeated/1.3-the-line-through-every-call.md) | Which MCP calls may be repeated, and the safe default | `working` |
| 1.4 | [The key that makes a write repeatable](parts/01-what-may-be-repeated/1.4-the-key-that-makes-a-write-repeatable.md) | One name for one intention, recorded with the effect | `working` |

### Section 2 — `02-the-deadline`: how long you are prepared to wait (MCP-22)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [Two clocks, not one](parts/02-the-deadline/2.1-two-clocks-not-one.md) | Connect and call are different failures | `working` |
| 2.2 | [💥 The deadline that is never reached](parts/02-the-deadline/2.2-the-deadline-never-reached.md) | 4.50s against 2.00s, and dead configuration | `production` |
| 2.3 | [`with_timeout`, the wrapper that guarantees a clock](parts/02-the-deadline/2.3-with-timeout.md) | Bounding your waiting, not their working | `working` |
| 2.4 | [The numbers your libraries already chose](parts/02-the-deadline/2.4-the-numbers-your-libraries-chose.md) | No default deadline, 300s on HTTP, one free retry | `production` |

### Section 3 — `03-backing-off`: how long between attempts (MCP-22)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [Waiting longer each time](parts/03-backing-off/3.1-waiting-longer-each-time.md) | Base, multiplier, cap — and which one is left out | `working` |
| 3.2 | [The same wait is the wrong wait](parts/03-backing-off/3.2-the-same-wait-is-the-wrong-wait.md) | 640 shed against 246, for one `uniform` call | `working` |
| 3.3 | [The server told you when to come back](parts/03-backing-off/3.3-the-server-said-when.md) | `429`, `Retry-After`, and the 429 you must not wait out | `working` |
| 3.4 | [`with_retries`, and why attempts are a budget](parts/03-backing-off/3.4-with-retries.md) | 27 requests nobody configured | `production` |

### Section 4 — `04-when-to-stop-asking`: the fourth defence (MCP-22)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [💥 The retry that took the server down](parts/04-when-to-stop-asking/4.1-the-retry-that-took-it-down.md) | Same 40 answered, 520 requests, 13s instead of 5 | `production` |
| 4.2 | [The switch that refuses before it asks](parts/04-when-to-stop-asking/4.2-the-switch-that-refuses-first.md) | Three states, and the one line that lets it close | `production` |

### Section 5 — `05-no-held-connections`: the MCP-specific half (MCP-23)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [The chair you are holding for nobody](parts/05-no-held-connections/5.1-the-chair-you-hold-for-nobody.md) | Four expired reasons, and a handle that returns `""` | `working` |
| 5.2 | [Keep the catalogue, not the connection](parts/05-no-held-connections/5.2-keep-the-catalogue-not-the-connection.md) | `ttlMs` is what replaced the held session | `working` |
| 5.3 | [What reconnecting actually costs](parts/05-no-held-connections/5.3-what-reconnecting-costs.md) | 1.07s per connect on stdio, measured | `production` |

### Section 6 — `06-the-last-word`: where both IDs meet (MCP-22 · MCP-23)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 6.1 | [What you say when all of it has failed](parts/06-the-last-word/6.1-what-you-say-when-it-all-failed.md) | Swallow, invent, or escalate — and the missing field | `production` |
| 6.2 | [One policy, not a hundred try/excepts](parts/06-the-last-word/6.2-one-policy-not-a-hundred.md) | One door, and the check that it is used | `production` |

### The paper — read it **after** the parts

| Paper | What it claims | Level |
| --- | --- | --- |
| [The tail at scale](papers/01-the-tail-at-scale.md) | The slow call, not the failed one, is what breaks a system at scale | `production` |

`doi:10.1145/2408776.2408794`, 2013. Two parts cite papers taught on earlier days as addresses:
[1.2](parts/01-what-may-be-repeated/1.2-a-timeout-is-an-unknown.md) cites *End-to-end arguments in
system design* (`doi:10.1145/357401.357402`, Day 21) and
[3.2](parts/03-backing-off/3.2-the-same-wait-is-the-wrong-wait.md) cites *New directions in
communications* (`doi:10.1109/MCOM.1986.1092946`, Day 24). A paper is taught once in the whole
curriculum.

**Read the sections in order, and read section 1 before you write a line of code.** Sections 2, 3 and
4 are all machinery for repeating a call, and every one of them is dangerous applied to a call that
should not be repeated.

---

## §3 Setup — run this

**No package is added today, and no package is upgraded.** `mcp` stays at `1.29.1` and `google-adk`
at `2.7.1`. `git diff pyproject.toml uv.lock` must be empty when you finish.

```bash
# 1 - the day's lab
cd days/day-44-client-hardening
mkdir -p lab lab/papers/the-tail-at-scale

# 2 - section 1: what may be repeated
touch lab/idem.py lab/unknown.py lab/repeatable.py lab/key.py

# 3 - section 2: the deadline
touch lab/clocks.py lab/budget.py lab/wrap.py lab/sdkclock.py lab/slow_mcp_server.py

# 4 - section 3: backing off
touch lab/backoff.py lab/jitter.py lab/retry_after.py lab/attempts.py

# 5 - section 4: when to stop asking
touch lab/storm.py lab/breaker.py

# 6 - section 5: no held connections
touch lab/held.py lab/catalog.py lab/cost.py

# 7 - section 6 and the day's gate
touch lab/escalate.py lab/scattered.py lab/one_door.py lab/onepolicy.py lab/gate.py

# 8 - the paper demo
touch lab/papers/the-tail-at-scale/backend.py lab/papers/the-tail-at-scale/fanout.py
cd -

# 9 - the project file you are about to fill (you type every line)
touch sutra/mcp/hardening.py

# 10 - the freshness gate, before anything else
curl -sL https://modelcontextprotocol.io/specification/versioning | grep -o "specification/2026-07-28" | head -1
```

**Step 10 is the gate and it is the same one Days 32, 33 and 34 ran.** Everything in this day is
written against revision **2026-07-28**. If that page names a newer current revision, stop and amend
the plan before writing code (Principle 14).

**`sutra/mcp/` is yours and it is shared.** Day 33 created the package and owns `client.py`
(`connect_stdio`, `connect_http`, `list_tools`). Day 37 added `auth.py`. Day 40 added `filtering.py`
(`ServerPolicy`, `allowlist`, `deny`, `REGISTRY`, `NEVER`). You are adding `hardening.py` beside
them — a fourth module, not a rewrite of any of the three.

---

## §4 Build brief

### The project code — `sutra/mcp/hardening.py`, and you type every line

One file, five public symbols. The parts give you every mechanism; the decisions are yours.

| Symbol | Shape | What it must do |
| --- | --- | --- |
| `with_timeout` | `(fn, seconds, *, label) -> T` | Bound the caller's waiting on any callable, whether or not it has a timeout of its own (2.3). |
| `with_retries` | `(fn, *, idempotent, budget, policy) -> T` | Attempt once for a write, up to the policy for a read, backing off and honouring `Retry-After` (1.1, 3.1, 3.3, 3.4). |
| `RETRYABLE` | a mapping | Which `(server, tool)` pairs may be repeated, **with a written reason per row** (1.3). |
| `RetryPolicy` | a frozen dataclass | `base`, `multiplier`, `cap`, `attempts`, `jitter` — as data, not literals (3.1, 3.2). |
| `Deadline` | a class | An instant, with `remaining()`; every hop asks for the minimum of its own budget and what is left (2.2). |

- **`with_timeout(fn, seconds, *, label)`** — `fn` takes no arguments; the caller closes over what it
  needs. Raise the built-in `TimeoutError` with `label` in the message, because the SDK's own message
  says only `ClientRequest` (2.4). Say in the docstring that the work is **not** stopped (2.3).
- **`with_retries(fn, *, idempotent, ...)`** — `idempotent` is required and has no default. Attempt
  exactly **one** time when it is false; never zero (1.1). Take the budget from
  [2.2](parts/02-the-deadline/2.2-the-deadline-never-reached.md), not a bare integer.
- **`RETRYABLE`** — keyed on `(server_key, tool_name)` and never on the bare name (1.3). A tool that
  is absent is a write.
- **The no-held-connection rule** is not a symbol; it is a property of the module and of everything
  beside it. Nothing under `sutra/mcp/` holds a session, client or connection at module scope, and
  every toolset Sutra constructs is closed (5.1). `lab/gate.py` checks the first half.

**`TODO(me)` markers left for you:**

- **1.3** — write `RETRYABLE` for every tool `sutra_mcp` currently serves, with a reason per row and
  the date you decided. Then decide whether `start_task` belongs there, given Day 36's
  [3.3](../day-36-long-jobs-and-tasks/parts/03-the-handle/3.3-sutras-handle-policy.md), and write
  down what the server would have to promise for it to qualify.
- **1.4** — decide where Sutra's idempotency key travels: a declared tool argument, or the request's
  `_meta`. Then say what has to change in
  [`sutra_mcp/tools.py`](../day-34-building-sutra-mcp-tools/LESSON.md) for `close_ticket` to honour
  one, and whether the key should be required rather than optional.
- **2.1** — choose a connect deadline and a per-tool call deadline for every server in Day 40's
  `REGISTRY`, and write the reason beside each number. They should not all be the same.
- **2.2** — decide how Sutra's remaining budget travels to a server in another process, given that
  MCP defines no field for it. Then decide what `sutra_mcp` should do with one when it arrives.
- **2.4** — write the test that asserts the *effective* `read_timeout_seconds` on both transports, so
  that a library upgrade cannot move it silently. It should fail today if you set nothing.
- **3.1** — choose `base`, `multiplier` and `cap` per server, and say which real failure the base is
  sized against.
- **3.3** — write the `retry_delay(...)` function that handles both `Retry-After` forms, bounds the
  delay by the remaining budget, and returns `None` for the 429 that means the daily quota is gone
  (Day 24's [2.2](../day-24-token-accounting-and-budgets/parts/02-two-ceilings/2.2-reading-the-ceiling-off-a-refusal.md)).
- **3.4** — decide Sutra's attempt budget, and write down what the total is at the bottom of the stack
  **including ADK's free retry**. That number goes in Day 45's audit.
- **4.2** — decide the breaker's threshold, cooldown and granularity, and write down which failure
  classes count towards it. A `-32602` must not.
- **5.2** — decide what Sutra does with an absent `ttlMs`, and whether to use ADK's
  `tool_list_cache_ttl_seconds` or Sutra's own cache. Say what you lose either way.
- **5.3** — write down, per transport, what Sutra holds between requests and what breaks if it is
  taken away. The correct second column is "nothing".
- **6.1** — write the escalation payload for a **write**, and get the `outcome_known` sentence right.
- **6.2** — decide which paths `onepolicy.py`'s successor scans and which are excluded, with a reason
  per exclusion. Then decide whether it belongs in Day 45's `tools/mcp_audit.py` or in `./m check`
  directly.

### The lab — nineteen scripts, all of which run, none of which call a model

| File | What it does | Taught in |
| --- | --- | --- |
| `lab/idem.py` | two closure emails against one, on one flag | 1.1 |
| `lab/unknown.py` | three worlds on the server, one sentence at the client | 1.2 |
| `lab/repeatable.py` | every call Sutra makes, classified, with the default flipped | 1.3 |
| `lab/key.py` | the same write twice, with and without a key the server remembers | 1.4 |
| `lab/clocks.py` | two real sockets, two failures, two numbers | 2.1 |
| `lab/budget.py` | 4.50s against 2.00s, and an attempt that asks for time it does not have | 2.2 |
| `lab/wrap.py` | `with_timeout`, and the work that finished after nobody was waiting | 2.3 |
| `lab/slow_mcp_server.py` | a real `FastMCP` stdio server whose only tool sleeps | 2.4, 5.3 |
| `lab/sdkclock.py` | the SDK's real defaults, in three arms | 2.4 |
| `lab/backoff.py` | four ladders against one eight-second outage | 3.1 |
| `lab/jitter.py` | 200 callers, four rungs, with and without `uniform` | 3.2 |
| `lab/retry_after.py` | a real `429` from a real socket, honoured and ignored | 3.3 |
| `lab/attempts.py` | 3 × 3 × 3 against one shared budget | 3.4 |
| `lab/storm.py` | a queue simulation: same 40 answered, 520 requests, 12.9s | 4.1 |
| `lab/breaker.py` | three states, three arms, one missing reset | 4.2 |
| `lab/held.py` | five held pipes, a deploy, and an empty string | 5.1 |
| `lab/catalog.py` | twelve requests, two catalogue fetches | 5.2 |
| `lab/cost.py` | what a stdio reconnect really costs, measured | 5.3 |
| `lab/escalate.py` | swallow, invent, escalate | 6.1 |
| `lab/scattered.py`, `lab/one_door.py`, `lab/onepolicy.py` | four call sites two ways, and the scan | 6.2 |
| `lab/gate.py` | the day's six assertions about `sutra/mcp/hardening.py`, as an exit code | §5 |

`lab/papers/the-tail-at-scale/` holds the paper demo — `backend.py` and `fanout.py` — and it is
**given complete** in the paper part. It is teaching material, not a rep: type it, run both arms, and
compare your output with the transcripts.

---

## §5 The eval that must be able to fail

Five checks with exit codes or ablations, all on zero model calls.

**The gate** is the day's definition of done, and it is red until you have written the module:

```bash
uv run python days/day-44-client-hardening/lab/gate.py; echo "exit: $?"
```

Measured on 2026-09-05, before anything was written:
`- sutra.mcp.hardening is not importable: ModuleNotFoundError: No module named 'sutra.mcp'`,
`findings: 1`, `exit: 1`. When it prints `findings: 0` and `exit: 0`, six statements are true: a
deadline that fires, a read that is retried, a write that is attempted exactly once, a bounded retry
budget, `close_ticket` absent from `RETRYABLE`, and no session held at module scope anywhere in
`sutra/mcp/`. Then break exactly one on purpose — add `"close_ticket"` to `RETRYABLE` and watch the
fifth finding appear.

**The one-door scan** is the check that the policy is used, and it must be run both ways:

```bash
cd days/day-44-client-hardening/lab
uv run python onepolicy.py scattered.py; echo "exit: $?"
uv run python onepolicy.py one_door.py; echo "exit: $?"
cd -
```

`findings: 4` and `exit: 1` against `findings: 0` and `exit: 0`. Line 28 of `scattered.py` — the
function that *does* retry — is one of the four findings, and understanding why is the point.

**The idempotency ablation** is the day's thesis, and both arms must be run:

```bash
cd days/day-44-client-hardening/lab
uv run python idem.py
uv run python idem.py --safe
cd -
```

Two closure notices against one. The careful arm's caller gets an exception instead of a result, and
that is the trade.

**The paper's ablation**, both arms:

```bash
cd days/day-44-client-hardening/lab/papers/the-tail-at-scale
uv run python fanout.py
uv run python fanout.py --hedge
cd -
```

Page p50 of `559.1ms` against `18.9ms`, and `63.4%` of pages over 100ms against `0.9%`, for `1.0%`
extra load.

**And the rest, each of which has a named break in its own part:**

```bash
cd days/day-44-client-hardening/lab
uv run python unknown.py
uv run python repeatable.py; uv run python repeatable.py --optimistic
uv run python key.py; uv run python key.py --key
uv run python clocks.py
uv run python budget.py; uv run python budget.py --shrink
uv run python wrap.py
uv run python sdkclock.py; uv run python sdkclock.py --call; uv run python sdkclock.py --session
uv run python backoff.py
uv run python jitter.py; uv run python jitter.py --jitter
uv run python retry_after.py; uv run python retry_after.py --honour
uv run python attempts.py; uv run python attempts.py --budget
uv run python storm.py; uv run python storm.py --retry
uv run python breaker.py; uv run python breaker.py --breaker; uv run python breaker.py --sticky
uv run python held.py; uv run python held.py --per-call
uv run python catalog.py; uv run python catalog.py --cache
uv run python cost.py
uv run python escalate.py
cd -
```

`sdkclock.py --session` **fails on purpose**, with a traceback ending in
`McpError: Timed out while waiting for response to ClientRequest. Waited 1.0 seconds.` — a
one-second session-wide deadline kills `initialize()` on Windows. That is the finding, not a bug in
the lab.

---

## §6 Request budget

**Free-tier Gemini**, 20 generate requests per day per model (`gemini-3.7-flash`, roster re-verified
2026-09-04).

| What | Generations |
| --- | --- |
| every part in every section | **0** |
| all nineteen lab scripts, every flag | **0** |
| the paper demo, both arms | **0** |
| `sutra/mcp/hardening.py` and the gate | **0** |
| **Total planned** | **0 of 20** |

**Zero, and it is the point rather than an economy.** Everything this day teaches is about time and
about what a caller does with an unknown, and neither needs a model. A timeout is a clock. A retry is
a loop. A queue is arithmetic. A `429` comes from a `http.server` on `127.0.0.1`. The two scripts
that speak real MCP — `sdkclock.py` and `cost.py` — talk to a `FastMCP` server on this machine whose
only tool sleeps.

Attaching the hardened client to the desk agent and watching a model survive a slow tool is worth
doing once, costs two or three generations, and teaches nothing this day has not already measured.

**Cost: $0.**

---

## §7 Traps

- **A timeout is not a failure, it is an unknown.** The work may have completed. Any error message
  saying "the call failed" is a claim the client cannot support (1.2).
- **A retry loop with no idempotency test is a duplicate-write machine.** Ask "may I?" before "how
  many times?" (1.1).
- **A tool that is idempotent today can stop being so in a one-line commit** that never mentions
  retries. Keep the *reason* beside every row, not just the name (1.3).
- **An idempotency key minted inside the retry loop does nothing** and looks correct in review. It
  must be minted above the loop (1.4).
- **`ClientSession(read_timeout_seconds=...)` defaults to `None`, which is `anyio.fail_after(None)`,
  which waits forever.** The default is not long; it is absent (2.4).
- **Over Streamable HTTP, ADK's per-call deadline comes from `sse_read_timeout` (300s), not from the
  `timeout=5.0` you set.** Read `session_context.py` (2.4).
- **ADK retries every failed tool call once, on any exception, at INFO level.** If your logs are at
  WARNING, a duplicate `close_ticket` leaves no trace anywhere (2.4, 3.4).
- **A `float` where `read_timeout_seconds` wants a `timedelta`** fails with `AttributeError:
  'float' object has no attribute 'total_seconds'` at the moment of the first timeout, not at
  construction (2.4).
- **A session-wide read timeout also bounds `initialize()`**, and on stdio `initialize` includes
  launching a Python interpreter (2.4).
- **An inner timeout larger than the caller's own budget never fires.** Your tuned numbers are dead
  configuration and nothing says so (2.2).
- **A negative or zero remaining budget must not become a zero-second call.** Do not attempt at all
  (2.2).
- **A retry ladder with no cap has an attempt that waits eight minutes** for a caller who left (3.1).
- **Exponential backoff with no jitter reproduces the original spike at every rung.** Backoff spreads
  one client's attempts; it does nothing about the fleet (3.2).
- **`Retry-After` comes in two forms**, and `int()` on the HTTP-date form raises `ValueError` inside
  the error handler, replacing the 429 entirely (3.3).
- **The 429 that means "your daily quota is gone" must not be slept off inside a request** (3.3).
- **Three layers of "up to three attempts" is twenty-seven requests** and nobody wrote twenty-seven
  down (3.4).
- **During an overload, retries add load to the thing that has run out of capacity** — and because
  giving up ends the wait and not the work, the abandoned attempts are still in the queue (4.1).
- **A retry storm shows a request-rate spike with a *zero* error rate.** It looks like a healthy
  server (4.1).
- **A breaker that never resets its failure counter closes and re-opens on the first ordinary blip**,
  and stays broken for one client after everybody else has recovered (4.2).
- **A breaker fed by a bare `except Exception` opens on a `-32602` typo** and stops calling a healthy
  server (4.2).
- **A dead stdio connection returns `""` from `readline()`, not an exception** — and `json.loads("")`
  raises `JSONDecodeError: Expecting value: line 1 column 1 (char 0)`, which sends people looking for
  a malformed response that does not exist (5.1).
- **`ttlMs` is milliseconds.** Treating it as seconds caches a tool list a thousand times too long
  (5.2).
- **`cacheScope: "private"` under a single cache key serves one caller's tool list to another** (5.2).
- **On stdio, connecting is launching a process** — about a second per request on this machine. A
  blanket "reconnect every time" makes the stdio path a hundred times slower (5.3).
- **`PROCESS_TERMINATION_TIMEOUT = 2.0`**: the SDK waits two seconds for a stdio child to terminate
  and then kills the process tree (5.3).
- **A hardened client fails more often and faster than a naive one.** If the top of the stack returns
  `None`, you have built a quieter outage (6.1).
- **"The ticket was not closed" is a claim you cannot support after a timeout.** The truthful sentence
  is that the outcome is unknown (6.1).
- **A policy module nobody is required to use is used for a fortnight.** The check that it is used is
  the control, not the module (6.2).

---

## §8 Verify before you code

Fetched or read on **2026-09-05**, the day this was written.

**The specification:**

- `https://modelcontextprotocol.io/specification/versioning` — the freshness gate in §3. Everything
  here targets **2026-07-28**.
- `https://modelcontextprotocol.io/specification/2025-11-25/basic/utilities/cancellation` — fetched
  and read. It confirms what section 4 assumes: cancellation is a **notification**, the receiver
  **SHOULD** stop and free resources but **MAY** ignore it, *"cancellation notifications may arrive
  after request processing has completed"*, and the sender **SHOULD** ignore any response that
  arrives afterwards. There is no mechanism by which a client can *know* that abandoned work stopped,
  which is why 4.1's simulation leaves the abandoned request in the queue.

**The installed SDK — the authoritative surface, read rather than guessed:**

- `.venv/Lib/site-packages/mcp/client/session.py` — `ClientSession.__init__(..., read_timeout_seconds:
  timedelta | None = None, ...)` and `call_tool(name, arguments, read_timeout_seconds=None,
  progress_callback=None, *, meta=None)`. **Both default to `None`** (2.4).
- `.venv/Lib/site-packages/mcp/shared/session.py` — `send_request`'s precedence block: request read
  timeout wins over session read timeout, `anyio.fail_after(timeout)` with `timeout=None` waits
  forever, and the failure is `McpError` carrying `httpx.codes.REQUEST_TIMEOUT` (408) with the message
  `"Timed out while waiting for response to {request.__class__.__name__}. Waited {timeout} seconds."`
  — which is always `ClientRequest` (2.3, 2.4).
- `.venv/Lib/site-packages/mcp/shared/_httpx_utils.py` — `MCP_DEFAULT_TIMEOUT = 30.0` and
  `MCP_DEFAULT_SSE_READ_TIMEOUT = 300.0`, applied by `create_mcp_http_client()` as
  `httpx.Timeout(30.0, read=300.0)` (2.4).
- `.venv/Lib/site-packages/mcp/client/streamable_http.py` — the current
  `streamable_http_client(url, *, http_client=None, terminate_on_close=True)` takes **no timeout at
  all**; timeouts move onto the `httpx.AsyncClient` you pass. The older
  `streamablehttp_client(url, headers, timeout=30, sse_read_timeout=60*5, ...)` is decorated
  `@deprecated("Use `streamable_http_client` instead.")`, and `StreamableHTTPTransport`'s `headers`,
  `timeout`, `sse_read_timeout` and `auth` parameters now emit a `DeprecationWarning` and **are
  ignored** (2.4).
- `.venv/Lib/site-packages/mcp/client/stdio/__init__.py` — `stdio_client(server, errlog=sys.stderr)`
  takes no timeout, and `PROCESS_TERMINATION_TIMEOUT = 2.0` bounds how long the SDK waits for a child
  to terminate before killing the process tree (5.3).
- `.venv/Lib/site-packages/mcp/types.py` — `LATEST_PROTOCOL_VERSION = "2025-11-25"` and
  `DEFAULT_NEGOTIATED_VERSION = "2025-03-26"`. The pin is still a revision behind what Sutra targets,
  exactly as Day 32's [5.1](../day-32-mcp-stateless-core/parts/05-failure-lab/5.1-the-tutorial-from-four-months-ago.md)
  recorded.
- `.venv/Lib/site-packages/google/adk/tools/mcp_tool/mcp_session_manager.py` —
  `StdioConnectionParams(server_params, timeout: float = 5.0)`;
  `StreamableHTTPConnectionParams(url, headers=None, timeout: float = 5.0, sse_read_timeout: float =
  60 * 5.0, terminate_on_close: bool = True, httpx_client_factory=create_mcp_http_client)`; the
  `retry_on_errors` decorator, which catches `except Exception` and retries **once** unless the task
  is cancelling; and `create_session`, which pools sessions in `self._sessions` keyed by merged
  headers and returns a stored one when it is still connected and on the same event loop (2.4, 5.1).
- `.venv/Lib/site-packages/google/adk/tools/mcp_tool/session_context.py` — the branch that decides
  the session read timeout: `timedelta(seconds=self._timeout)` for **stdio**, and
  `timedelta(seconds=self._sse_read_timeout)` for **SSE and Streamable HTTP**, with the comment
  *"For SSE and Streamable HTTP clients, use the sse_read_timeout instead of the connection timeout as
  the read_timeout for the session."* This is the day's most surprising finding (2.4).
- `.venv/Lib/site-packages/google/adk/tools/mcp_tool/mcp_tool.py` — `@retry_on_errors` sits directly
  on `McpTool._run_async_impl`, and the body calls `session.call_tool(...)` with **no**
  `read_timeout_seconds` (2.4).
- `.venv/Lib/site-packages/google/adk/tools/mcp_tool/mcp_toolset.py` — `McpToolset.__init__` takes
  `tool_filter`, `tool_name_prefix`, `tool_list_cache_ttl_seconds` (default `None`, must be positive
  when set) and `require_confirmation`; the cache is an `OrderedDict` bounded at
  `_MAX_TOOL_LIST_CACHE_ENTRIES = 64` and is keyed by headers, and it takes a TTL in **seconds** that
  you supply rather than the `ttlMs` the server sent (5.2).

**The ADK documentation:**

- `https://adk.dev/tools-custom/mcp-tools/` — read on 2026-09-05. It does **not** document any of the
  timeout defaults above, which is why the installed source is the authority here. What it does carry
  and this day relies on: the exit-stack pattern is *"crucial for ensuring the connection (and
  potentially the server process) is properly terminated when the ADK agent finishes"*, the
  `await toolset.close()` example, and the acknowledgement that *"MCP establishes stateful, persistent
  connections between a client and server instance"* which *"can pose challenges for scaling and
  deployment"* — a sentence written against the older model, and precisely the challenge section 5
  answers.
- `https://adk.dev/docs/tools/mcp-tools/` returned **HTTP 404**. The live page is the
  `tools-custom` path used by Days 33 and 40.

**Three live commands, re-run today:**

```bash
curl -sL https://modelcontextprotocol.io/specification/versioning | grep -o "specification/2026-07-28" | head -1
uv run python -c "from mcp.types import LATEST_PROTOCOL_VERSION as l; print(l)"
uv run python -c "from mcp.shared._httpx_utils import MCP_DEFAULT_TIMEOUT as t, MCP_DEFAULT_SSE_READ_TIMEOUT as s; print(t, s)"
```

---

## §9 Say it in an interview

*"The client-hardening day is the one where I stopped writing retry loops and started writing a retry
policy, and the order turned out to matter more than the mechanism. The first thing is not backoff,
it is idempotency: a timeout is not a failure, it is an unknown — the work may have completed and the
answer got lost — so before anything else I ask whether this call is one I can afford to have happened
twice. Reads yes, writes no, and a tool nobody has classified is a write. I proved that to myself
with a fake wire that drops the first reply: symmetric retries sent two closure emails to one
customer, and the asymmetric policy sent one and handed the caller an error instead. The caller was
less happy. The customer was.*

*Then the arithmetic. Three layers of 'up to three attempts' is twenty-seven requests at the bottom
and nobody configured twenty-seven, so attempts became a budget on the request rather than a constant
in a function. And retries during an overload make things worse, not better — I measured it with a
queue simulation: two hundred callers against a server doing forty a second answered exactly forty
people with retries on and with them off, but the retry run cost 520 requests instead of 200 and the
queue took thirteen seconds to drain instead of five. The retries helped nobody and tripled the
damage, because giving up ends your wait and not the server's work.*

*The part I did not expect was how much of this had already been decided for me. I read the installed
libraries instead of the docs, and found that an MCP client session has no read timeout at all by
default, that over Streamable HTTP the ADK connection's per-call deadline comes from
`sse_read_timeout` — three hundred seconds — rather than the five-second `timeout` you set, and that
ADK retries every failed tool call once on any exception without asking whether the tool is
idempotent. Three defaults, none documented, all of them load-bearing.*

*And the last part is the one I would defend hardest, because it is the one that gets cut. All of
this makes a client fail more often and faster — the breaker refuses calls that would have worked,
the budget stops early. That is only an improvement if the failure arrives at the top as something a
human can act on: what was attempted, how many times, what is not known, and whether it is worth
retrying later. A retry ladder that ends in a `return None` has broken the only principle that
mattered."*

---

## §10 Done when

See [`CHECKLIST.md`](CHECKLIST.md). Every box is ticked because you ran the thing, not because you
read about it. `./m done 44` refuses to commit until they are.

---

## §11 Ledger & commit

**`docs/PROGRESS.md` — append this row** (fill in the hash after committing):

```markdown
| 44 | 2026-09-05 | MCP-22, MCP-23 | 19 (+1 paper) | <hash> | ⚠️ |
```

**`docs/PACKAGES.md` — no new rows today.** No package is added and no pin is moved.

**`docs/PAPERS.md` — no new rows today.** *The tail at scale* (`doi:10.1145/2408776.2408794`) was
verified on 2026-09-04 and its row already exists, naming this day and
`days/day-44-client-hardening/papers/01-the-tail-at-scale.md`.

**`docs/SKILL_PROVENANCE.md` — no new rows today.**

**Git commit message:**

```
day 44: client hardening — retries, timeouts, no held connections — closes MCP-22, MCP-23
```
