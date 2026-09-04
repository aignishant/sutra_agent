---
day: 36
phase: 5
phase_name: "MCP I: the protocol"
title: "Long jobs — progress, task handles and the Tasks extension"
ids: ["MCP-10", "MCP-14", "MCP-28"]
principles: [1, 2, 4, 7, 8, 10, 11, 13, 14, 15, 16, 17, 18]
kind: lab
plan_version: "v2.2.1"
parts: 18
generated: "2026-09-04"
status: written
lab_scaffolded: true
commit: ""
---

# Day 36 — Long jobs: progress, task handles and the Tasks extension

> **Yesterday (Day 35):** resources and prompts. `sutra_mcp` grew the two surfaces that are not tools —
> data the client fetches, and templates the user chooses — and every one of them answered before the
> caller had time to blink.
> **Today:** the first piece of work that cannot. A re-index of the ticket archive will not fit inside a
> request, so the tool stops returning the answer and starts returning **a name for the work**.
> **Tomorrow (Day 37):** auth and enterprise — badges, questions and policy. The `owner` column you
> write into the task row today is the field Day 37 finally has something real to put in.

---

## §1 Where we are

Every tool `sutra_mcp` has ever served finished before anybody could get bored.

`lookup_ticket` reads a dictionary. `search_kb` scans a handful of strings. Day 35's resources read a
file. The request arrives, the work happens, the answer goes back on the same connection, and the whole
thing is over in the time it takes to blink. That shape has been correct every single time, which is why
nobody has ever had to think about it.

Phase 7 breaks it. Day 49 builds an embedding index over the whole ticket archive, and "re-index the
archive" is not a dictionary lookup — it reads thousands of tickets and computes something for each one.
Put that inside a request handler and you have a request that stays open for the length of the job, and
a connection is the least durable thing in the system.

Here is the sequence that makes it real. The client's deadline fires. The connection closes. The server,
which never knew anybody was waiting, finishes the job correctly a moment later and discovers there is
nowhere to put the answer. The work succeeded and was thrown away — and the client cannot even ask what
happened, because the only name that work ever had was a request id that died with its stream.

So today the tool hands back a **claim on the answer** instead of the answer. Three ideas, in the order
they have to be understood.

**Progress tells you a job is alive, and nothing else.** `notifications/progress` exists, it is easy,
and it is a trap if you stop there: it is opt-in by the caller, advisory for the server, and it dies
with the connection it rides on. It is narration, and narration cannot be asked a question tomorrow.

**A handle is the state.** The server mints an opaque name, writes the row to shared storage **before**
answering, and hands the name back. Day 32 taught the rule; today you build it, and you decide the
policy Day 32 left as a `TODO(me)`: how a handle is generated, who owns it, when it expires, and what
error an unknown one returns.

**The Tasks extension is that handle, standardised.** `io.modelcontextprotocol/tasks` gives it four
messages, five statuses, three verbs and a terminal rule — so any client can drive any server's long
jobs. Build first, adopt after (Principle 4).

And the day has a finding, again. The `mcp` package pinned in this repository *does* have tasks in it,
and they are the **wrong tasks**: the pre-2026 experimental API, with `tasks/result` and `tasks/list`
that the extension removed, no `tasks/update`, and fields spelt `ttl` and `pollInterval` rather than
`ttlMs` and `pollIntervalMs`. The package says so itself in a deprecation warning Python hides by
default. Part 4.4 reads it out loud and §8 records which half of this day could actually be run.

---

## §2 The map

Eighteen parts in six sections, plus **one paper**, read last. The day climbs
`foundation → working → production`: section 1 is why a long job cannot ride a request, section 2 is
progress and its limits, section 3 is the handle and its policy, section 4 is the standardised form,
section 5 is cancellation, and section 6 is what you own afterwards.

### Section 1 — `01-the-blocking-call`: why long work cannot live in a request (MCP-10)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [The call you cannot leave](parts/01-the-blocking-call/1.1-the-call-you-cannot-leave.md) | The work succeeded and the answer was discarded | `foundation` |
| 1.2 | [The timeout ladder](parts/01-the-blocking-call/1.2-the-timeout-ladder.md) | Raising your rung moves the failure, and worsens it | `working` |
| 1.3 | [Work with no name](parts/01-the-blocking-call/1.3-work-with-no-name.md) | A request id names a message, not a job | `working` |

### Section 2 — `02-progress`: what `notifications/progress` can and cannot do (MCP-10)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [The token you have to ask for](parts/02-progress/2.1-the-token-you-have-to-ask-for.md) | No `progressToken`, no progress — and no error | `working` |
| 2.2 | [Reporting from inside a tool](parts/02-progress/2.2-reporting-from-inside-a-tool.md) | `Context`, and a report call that is always safe | `working` |
| 2.3 | [Progress is narration, not state](parts/02-progress/2.3-progress-is-narration-not-state.md) | The one question a handle answers and progress cannot | `working` |

### Section 3 — `03-the-handle`: the state that travels in the payload (MCP-14)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [A name the server mints](parts/03-the-handle/3.1-a-name-the-server-mints.md) | Durable before the response, redeemable anywhere | `working` |
| 3.2 | [💥 The handle anyone can guess](parts/03-the-handle/3.2-the-handle-anyone-can-guess.md) | Fifteen guesses, ten of ten tasks reachable | `production` |
| 3.3 | [Sutra's handle policy](parts/03-the-handle/3.3-sutras-handle-policy.md) | Five rules, as a check that goes red | `production` |

### Section 4 — `04-the-tasks-extension`: the standardised form (MCP-28)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [Four messages on the wire](parts/04-the-tasks-extension/4.1-four-messages-on-the-wire.md) | Opt-in, `CreateTaskResult`, `tasks/get`, terminal | `foundation` |
| 4.2 | [Five statuses and the terminal rule](parts/04-the-tasks-extension/4.2-five-statuses-and-the-terminal-rule.md) | Why a retry is a new task, never a rewind | `working` |
| 4.3 | [Polling is a budget](parts/04-the-tasks-extension/4.3-polling-is-a-budget.md) | 2101 requests against 18, same answer | `production` |
| 4.4 | [💥 Which dialect your SDK speaks](parts/04-the-tasks-extension/4.4-which-dialect-your-sdk-speaks.md) | The pinned SDK has the tasks the spec removed | `production` |

### Section 5 — `05-cancellation`: asking a job to stop (MCP-28)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [Cancel is a request, not a switch](parts/05-cancellation/5.1-cancel-is-a-request-not-a-switch.md) | Cooperative, acknowledged, and not a promise | `working` |
| 5.2 | [💥 The checkpoint that makes cancel real](parts/05-cancellation/5.2-the-checkpoint-that-makes-cancel-real.md) | Identical wire traffic, opposite outcomes | `production` |

### Section 6 — `06-in-production`: what you own afterwards

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 6.1 | [💥 The task that says working forever](parts/06-in-production/6.1-the-task-that-says-working-forever.md) | A lease, because a dead worker writes no status | `production` |
| 6.2 | [The job that ran twice](parts/06-in-production/6.2-the-job-that-ran-twice.md) | The one message that can still duplicate work | `production` |
| 6.3 | [The store is the stateful thing](parts/06-in-production/6.3-the-store-is-the-stateful-thing.md) | Eight obligations, one component, no scaling out | `production` |

### The paper — read it **after** the parts

| Paper | Identifier | What it argued |
| --- | --- | --- |
| [Promises: linguistic support for efficient asynchronous procedure calls in distributed systems](papers/01-promises.md) | `doi:10.1145/53990.54016` (1988) | A remote call should return a typed placeholder at once, so the caller waits at the point of use rather than the point of call |

Principle 4 at the scale of a day: build the mechanism, measure its failures, *then* read the proposal.
A task handle is that paper's promise with one property added — it outlives the caller.

---

## §3 Setup — run this

**No package is added today, and no package is upgraded.** `git diff pyproject.toml uv.lock` must be
empty when you finish. `mcp` stays at `1.29.1`; part 4.4 records exactly what that pin can and cannot
speak, and moving it is a plan amendment (Principle 14), not something a lesson does on its way past.

```bash
# 1 - the day's lab
cd days/day-36-long-jobs-and-tasks
mkdir -p lab/papers/promises

# 2 - section 1: the blocking call and its ladder
touch lab/blocking.py lab/timeout_ladder.py lab/no_name.py

# 3 - section 2: progress
touch lab/progress.py

# 4 - section 3: the handle, its tenancy hole, and the policy
touch lab/tickets.py lab/tenancy.py lab/policy.py

# 5 - section 4: the extension on the wire, the poll budget, the SDK probe
touch lab/wire_shapes.py lab/poll.py lab/sdk_tasks.py

# 6 - section 5: cooperative cancellation, with an ablation switch
touch lab/cancel.py

# 7 - section 6: the reaper and the idempotency key
touch lab/reaper.py lab/idempotency.py

# 8 - the paper demo
touch lab/papers/promises/work.py lab/papers/promises/run.py
cd -

# 9 - the gate, before anything else: has the specification moved?
curl -sL https://modelcontextprotocol.io/specification/versioning | grep -o "specification/2026-07-28" | head -1

# 10 - and does the extension still say what this day says it says?
curl -s https://modelcontextprotocol.io/extensions/tasks/overview | grep -o "cancellation is cooperative" | head -1
```

**Steps 9 and 10 are the gate and they are not ceremony.** This day is written against revision
**2026-07-28** and against the Tasks extension as published on 2026-09-04. If the versioning page names
a newer revision, or if the extension page no longer says cancellation is cooperative, stop and amend
the plan first (Principle 14). On 2026-09-04 they printed `specification/2026-07-28` and
`cancellation is cooperative`.

**Read the parts in order and the paper last.** Section 2 only makes sense once section 1 has shown you
what is broken, section 3 is the fix section 2 could not be, and sections 4 and 5 standardise what
section 3 built by hand.

---

## §4 Build brief

Thirteen lab scripts, none of which touch a model. Each belongs to the part that teaches it.

| File | What it does | Taught in |
| --- | --- | --- |
| `lab/blocking.py` | a client with a deadline against a server that does not know | 1.1 |
| `lab/timeout_ladder.py` | which rung fires, and where the failure moves when you raise yours | 1.2 |
| `lab/no_name.py` | two requests, one errand, two re-indexes | 1.3 |
| `lab/progress.py` | `notifications/progress` with a token and without one | 2.1, 2.2, 2.3 |
| `lab/tickets.py` | mint, store, redeem — from an instance that did not exist yet | 3.1 |
| `lab/tenancy.py` | sequential handles against random ones, with an exit code | 3.2 |
| `lab/policy.py` | Sutra's five handle rules as a check that is red as shipped | 3.3 |
| `lab/wire_shapes.py` | the four extension messages, and the terminal-transition rule | 4.1, 4.2 |
| `lab/poll.py` | request counts for three polling cadences | 4.3 |
| `lab/sdk_tasks.py` | which tasks dialect `mcp==1.29.1` actually speaks | 4.4 |
| `lab/cancel.py` | cooperative cancellation, with the checkpoint as an ablation switch | 5.1, 5.2 |
| `lab/reaper.py` | a lease, a dead worker, and the sweep that notices | 6.1 |
| `lab/idempotency.py` | one key, one job, however many times the client asks | 6.2 |

`lab/papers/promises/` holds the paper demo — `work.py` and `run.py` — and it is **given complete** in
the paper part. It is teaching material, not a rep: type it, run both arms, and compare your output with
the transcript.

**The project code this day asks for: `sutra_mcp/tasks.py`.** Three public functions, registered into
the server `build_server()` from [Day 34](../day-34-building-sutra-mcp-tools/LESSON.md) already
returns:

- `start_task(archive: str, idempotency_key: str) -> dict` — mints the handle, writes the row **before**
  returning, hands the work to something the request does not own.
- `get_task(task_id: str) -> dict` — reads the row for the calling owner, returns status and, on a
  terminal status, the result or the error.
- `cancel_task(task_id: str) -> dict` — records the intent and acknowledges; it does not stop anything
  itself.

**`TODO(me)` markers left for you:**

- **1.2** — write down the shortest deadline anywhere between Sutra and `sutra_mcp` in your own setup,
  and say which of those rungs you can change.
- **2.1** — decide where Sutra's client generates its `progressToken`, and how it guarantees uniqueness
  across concurrent requests.
- **2.2** — decide the reporting granularity for the Day 49 re-index: every item, every batch, or every
  one per cent — and write down why.
- **3.3** — implement rules 2 and 3 in `lab/policy.py` and get it to `findings: 0`. Then choose the two
  TTL values Sutra will use — one for an unfinished task, one for a collected result — and write down
  the reasoning, not just the numbers.
- **3.3** — decide where the TTL sweep runs and what alerts when it stops running.
- **4.1** — decide whether Sutra's client declares `io.modelcontextprotocol/tasks` on every request or
  only on the tools that might be long, and say what breaks if you get it wrong.
- **4.3** — write the shared polling loop: start at `pollIntervalMs`, back off, cap under `ttlMs`, add
  jitter. Decide whether it lives here or waits for Day 44's `sutra/mcp/hardening.py`.
- **4.4** — write the assertion that fails when the pinned SDK's task field names stop matching what
  `sutra_mcp` sends. Decide what it should say when it goes red.
- **5.2** — choose the checkpoint interval for the Day 49 re-index and state the cancellation latency it
  implies.
- **6.1** — choose Sutra's lease duration and heartbeat interval, and say what ratio between them you
  are comfortable with under load.
- **6.2** — decide the shape of Sutra's idempotency key for the Day 73 nightly run, and say what makes
  two nights different intentions.
- **6.3** — map each of the eight store obligations to a method on `TaskStore`. One of them maps to
  none; decide whether that is a gap in the interface or a job for something outside it.

---

## §5 The eval that must be able to fail

Four checks, all on zero model calls, two of them **red on purpose**.

**The handle policy** is the day's gate, and it is the answer to Day 32's `TODO(me)`:

```bash
uv run python days/day-36-long-jobs-and-tasks/lab/policy.py; echo "exit: $?"
```

Measured on 2026-09-04: `findings: 2` and `exit: 1` — rule 2 (a caller can read a handle it does not
own) and rule 3 (handles are minted with no `ttl_ms`). Set `CHECK_OWNER = True` and give `TTL_MS` a
value and it goes to `findings: 0`, `exit: 0`. Then set `HANDLE_BYTES = 8` and watch rule 1 appear with
the real entropy of the shorter handle.

**The tenancy probe** is the security finding:

```bash
uv run python days/day-36-long-jobs-and-tasks/lab/tenancy.py; echo "exit: $?"
```

Measured the same day: `tasks reachable : 10 of 10` from fifteen guesses against the sequential store,
`0 of 10` against the random one with an owner check, `findings: 1`, `exit: 1`.

**The cancellation ablation** must be run **both ways**, and the two acknowledgements compared:

```bash
CHECKPOINTS=1 uv run python days/day-36-long-jobs-and-tasks/lab/cancel.py
CHECKPOINTS=0 uv run python days/day-36-long-jobs-and-tasks/lab/cancel.py
```

`cancelled` with `2 of 8` chunks against `completed` with `8 of 8` — from identical wire traffic. The
line to stare at is the acknowledgement, which is byte-identical in both runs.

**The paper demo** is the other ablation, and both arms are required:

```bash
cd days/day-36-long-jobs-and-tasks/lab/papers/promises
PROMISES=0 uv run python run.py
PROMISES=1 uv run python run.py
cd -
```

`1.20s` against `0.40s` for the same three calls and the same three answers.

**And the rest, each of which has a named break in its own part:**

```bash
uv run python days/day-36-long-jobs-and-tasks/lab/blocking.py
uv run python days/day-36-long-jobs-and-tasks/lab/timeout_ladder.py
uv run python days/day-36-long-jobs-and-tasks/lab/no_name.py
uv run python days/day-36-long-jobs-and-tasks/lab/progress.py
uv run python days/day-36-long-jobs-and-tasks/lab/tickets.py
uv run python days/day-36-long-jobs-and-tasks/lab/wire_shapes.py
uv run python days/day-36-long-jobs-and-tasks/lab/poll.py
uv run python days/day-36-long-jobs-and-tasks/lab/sdk_tasks.py
uv run python days/day-36-long-jobs-and-tasks/lab/reaper.py
uv run python days/day-36-long-jobs-and-tasks/lab/idempotency.py
```

Named breaks worth performing on purpose: move `_meta` out of `params` in `progress.py` and watch the
notifications vanish silently; move `store.put` below the thread start in `tickets.py` and poll a
freshly-minted handle; set `LEASE_S = 0.01` in `reaper.py` and watch a healthy worker be reaped.

---

## §6 Request budget

**Free-tier Gemini**, 20 generate requests per day per model (`gemini-3.7-flash`, roster re-verified
2026-09-04).

| What | Generations |
| --- | --- |
| every part in every section | **0** |
| all thirteen lab scripts | **0** |
| the cancellation ablation, both arms | **0** |
| the paper demo, both arms | **0** |
| **Total planned** | **0 of 20** |

**Zero, and deliberately so.** The subject is the protocol *around* slow work, not the work itself, so
the slow work is a `time.sleep` and a counter. Real embeddings cost quota and arrive on Day 49. Today's
only network traffic is two HTTPS GETs to the specification site in §3, and both of them are freshness
gates rather than lessons.

**Cost: $0.**

---

## §7 Traps

- **Progress is opt-in by the caller, and its absence is silent.** No `progressToken` in `_meta` means
  the SDK's `report_progress` returns before sending anything — no error, no warning, no log line
  (2.1, 2.2).
- **`_meta` is inside `params`, not beside it.** Put it in the wrong place and the request is still
  valid, still answered, and carries no metadata at all (2.1, 4.1).
- **Progress dies with the connection and cannot be asked about later.** A broken stream loses the
  in-flight request; the client must re-issue with a **new** request id (1.3, 2.3).
- **Raising a timeout does not buy time.** The shortest rung on the path fires, most rungs are not
  yours, and the replacement error is worse (1.2).
- **Write the task row *before* returning the handle.** Return first and a crash hands out a name for
  nothing (3.1).
- **A sequential task id is a directory of everyone else's jobs.** Fifteen guesses reached ten of ten
  tasks in the demo (3.2).
- **Not-found and not-yours must be the same error, byte for byte.** A different message confirms the
  handle is real (3.2, 3.3).
- **An unknown handle is `-32602`, not `-32603`.** It is a bad argument, not a server fault (3.3).
- **A handle with no expiry is a table that only grows**, and a TTL written but never swept is a policy
  nobody implemented (3.3, 6.1).
- **`ttlMs` and `pollIntervalMs` are milliseconds.** `3600` is not what you meant and nothing will tell
  you (4.1).
- **Never return a `CreateTaskResult` to a client that did not declare the extension** — it will try to
  read `content` out of a handle and crash (4.1).
- **A terminal status never changes.** A retry is a new task with a new id, never a rewind, or every
  client that cached the old answer now disagrees with you (4.2).
- **Read `status` before `result`.** A running task's `result` is legitimately `None` (4.2).
- **Your backoff cap must stay under `ttlMs`**, or you come back after the sweep and the answer looks
  like a job that never existed (4.3).
- **The pinned `mcp` has the *experimental* tasks API**, not the extension: `tasks/result` and
  `tasks/list` are present, `tasks/update` is not, and the fields are `ttl` and `pollInterval` (4.4).
- **`DeprecationWarning` is hidden by default.** A whole feature can be built on a deprecated API in
  silence (4.4).
- **`tasks/cancel` acknowledges an intent; it does not stop anything.** Report the terminal status, not
  the acknowledgement (5.1).
- **Only the worker may write `cancelled`,** because only the worker knows it stopped (5.1).
- **No checkpoint, no cancellation** — and from outside, a server that ignores cancels is
  indistinguishable from one that has not got there yet (5.2).
- **A row says `working` because someone wrote it, not because anything is working.** A killed worker
  writes no status; only a lease can tell slow from dead (6.1).
- **A lease shorter than the heartbeat interval reaps healthy jobs under load** (6.1).
- **The one message that can still duplicate work is the response carrying the handle** (6.2).
- **The idempotency key is client-chosen; the task id is server-minted.** Only the client knows two
  requests are one intention (6.2).
- **Instances scale out; the store does not.** Two stores are two worlds (6.3).

---

## §8 Verify before you code

Fetched or run on **2026-09-04**, the day this was written.

**The specification and the extension:**

- `https://modelcontextprotocol.io/extensions/tasks/overview` — the whole of section 4 and section 5:
  the extension identifier `io.modelcontextprotocol/tasks`, the five statuses and which three are
  terminal, `CreateTaskResult` with `resultType: "task"`, `taskId`, `ttlMs` and `pollIntervalMs`,
  `tasks/get` / `tasks/update` / `tasks/cancel`, `inputRequests` / `inputResponses`, the rule that a
  task must be *"durably created before sending the response"*, the rule that a server must *"never
  return a task to a client that did not declare support"*, and the sentence that section 5 is built
  on: *"Cancellation is cooperative — the server acknowledges the intent but is not obligated to stop
  the work."* It also names `notifications/tasks` over `subscriptions/listen` as the optional push
  alternative to polling.
- `https://modelcontextprotocol.io/specification/2026-07-28/basic/utilities/progress` — all of section
  2: `progressToken` in the request `_meta`, tokens **MUST** be a string or integer and **MUST** be
  unique across active requests, the `notifications/progress` shape with `progress` / `total` /
  `message`, `progress` **MUST** increase, both parties **SHOULD** rate limit, and notifications
  **MUST** stop after completion.
- `https://modelcontextprotocol.io/specification/2026-07-28/changelog` — three lines this day leans on:
  major change 6 (tasks moved out of the core into the extension, `tasks/result` replaced by
  `tasks/get`, `tasks/update` added, `tasks/list` removed — SEP-2663); major change 9 (SSE
  resumability and `Last-Event-ID` removed; *"A broken response stream loses the in-flight request;
  clients MUST re-issue it as a new request with a new request ID"*); and major change 4 (request-scoped
  notifications such as `notifications/progress` flow on the response stream of the request they relate
  to, not on `subscriptions/listen`).
- `https://modelcontextprotocol.io/specification/versioning` — the freshness gate. The current revision
  is still **2026-07-28**; no amendment is required on that count.

**The installed package — the authoritative API surface, read rather than guessed:**

- `.venv/Lib/site-packages/mcp/types.py` — `TaskStatus` is
  `Literal['working', 'input_required', 'completed', 'failed', 'cancelled']`, which matches the
  extension exactly. `Task` has fields `taskId`, `status`, `statusMessage`, `createdAt`,
  `lastUpdatedAt`, **`ttl`** and **`pollInterval`** — *not* `ttlMs` and `pollIntervalMs`.
  `CreateTaskResult` has `meta` and `task`.
- The method strings the SDK's request classes declare include `tasks/get`, `tasks/cancel`,
  **`tasks/result`** and **`tasks/list`**, and do **not** include `tasks/update`. Both of the first two
  were removed by the 2026 redesign, which dates this SDK precisely.
- `.venv/Lib/site-packages/mcp/server/lowlevel/server.py` — `Server.experimental` is decorated
  deprecated: *"The experimental tasks API is deprecated and will be removed in mcp 2.0: tasks
  (SEP-1686) were removed from the MCP specification and are expected to return as a separate MCP
  extension."* The same string is in `mcp/client/session.py`.
- `.venv/Lib/site-packages/mcp/server/fastmcp/server.py` — `Context` is injected into tools by type
  annotation, and `async def report_progress(self, progress, total=None, message=None)` reads
  `request_context.meta.progressToken` and **returns silently** when it is `None`, with a
  `# pragma: no cover` on that branch.
- `mcp` version read from the installed distribution: **1.29.1**;
  `LATEST_PROTOCOL_VERSION = "2025-11-25"`.

**Which half of this day could actually be run against the pin.** Recorded here rather than glossed
over:

| Runnable against `mcp==1.29.1` | Taught against the specification only |
| --- | --- |
| the five statuses and the terminal rule | `tasks/update` and `inputRequests` / `inputResponses` |
| the handle mechanism (ordinary tool arguments — needs no extension) | the `ttlMs` / `pollIntervalMs` field names |
| `notifications/progress` and `Context.report_progress` | the per-request extension capability declaration |
| the method names `tasks/get` and `tasks/cancel` | `notifications/tasks` over `subscriptions/listen` |

Everything in the right-hand column is implemented by hand in `lab/wire_shapes.py` as plain
dictionaries, which is exactly why that script builds messages instead of importing models.

**No ADK symbol is used anywhere in this day.** Nothing here touches `google.adk`.

**No paper was verified today.** `doi:10.1145/53990.54016` already had its dated row in
`docs/PAPERS.md`; the venue and pagination in the paper part's citation block — PLDI '88, pages
260–267, June 1988 — came from the Crossref record for that DOI, read the same day.

---

## §9 Say it in an interview

"Our MCP server was fine until we had to add something slow — re-indexing a ticket archive. The naive
version does the work in the request handler, and I built that on purpose first so I could measure it:
the client timed out at half a second, the server finished the correct answer a second later, and the
answer was thrown away because the only place it could have gone was a connection that had closed.

The instinct is to raise the timeout, and I would push back on that in a design review. The deadline
that ends the call is the shortest one on the path, and most of them are not yours — a proxy, a load
balancer, the host. I modelled the ladder: raising my own client's timeout just moved the failure to the
reverse proxy and turned a clear MCP timeout into an HTTP 504 from a box I do not own.

So the fix is a change of shape rather than a change of number. The tool returns immediately with a
server-minted opaque handle, and the row is written to shared storage *before* the response goes out —
that ordering is the bit people get wrong, because if you return first and crash, the client is holding
a name for a job you have no record of. Then the client polls. I proved the property with three server
instances sharing one store: an instance created after the job started can answer a poll about it.

Two things I would flag from that build. First, the handle is a security surface. I ran the version with
sequential ids and no owner column: one legitimate handle, fifteen guesses typed by hand, and every task
in the deployment was reachable including the other tenant's. Random token, owner on the row, and the
same not-found message whether it does not exist or is not yours — a different message is an enumeration
oracle. Second, cancellation is honest in the spec in a way people miss: `tasks/cancel` is cooperative,
the server acknowledges an intent and is not obligated to stop. So the client reports the terminal
status, not the acknowledgement, and on the server side the cancel only lands where the work stops to
look. I built the ablation for that — checkpoint on, two of eight chunks indexed; checkpoint off, all
eight — and the acknowledgement is byte-identical in both runs, which means a test that asserts on
messages cannot tell the two implementations apart. You have to count the work.

The last thing I would say is that all of this is an old idea. The 1988 promises paper argued that a
remote call should hand the caller a typed placeholder immediately so it waits at the point of use
rather than the point of call — that is futures in every language now. A task handle is the same move
with one property added: it lives in shared storage, so it outlives the caller, the connection and the
server instance. And I would be honest about what statelessness bought: the state did not go away, it
moved into a store that now owns durability, ownership, expiry, leases and idempotency — and that store
is the one component you cannot fix by adding another copy of it."

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked and `./m depth 36` is green. Defined by
understanding and green checks, never by elapsed time — a part is finished when you could explain it to
someone else without the page open.

**Phase 5's gate** is `sutra-mcp` serving tools statelessly, on Day 38. Today is the day the word
"statelessly" is finally paid for: you can say where the state went, what it costs, and what a handle
must guarantee. Day 37 adds the authentication that gives the `owner` column something real to hold, and
Day 38 drives the client against a server built to misbehave.

---

## §11 Ledger & commit

**`docs/PROGRESS.md`** — append:

```text
| 36 | <date> | MCP-10, MCP-14, MCP-28 | 18 (+1 paper) | <hash> | ✅ |
```

**`docs/PACKAGES.md`** — **no new rows.** Nothing was installed and nothing upgraded: `mcp` stays at
`1.29.1`. The finding that its tasks API is the removed experimental one is recorded in §8 and taught in
part 4.4; it becomes a row only when something is actually installed.

**`docs/PAPERS.md`** — **no new rows.** `doi:10.1145/53990.54016` already has its dated row, and it is
taught here in [`papers/01-promises.md`](papers/01-promises.md).

**`docs/SKILL_PROVENANCE.md`** — no new rows. No skill was added or changed.

**The commit:**

```text
day 36: long jobs - progress, task handles and the Tasks extension - closes MCP-10, MCP-14, MCP-28
```
