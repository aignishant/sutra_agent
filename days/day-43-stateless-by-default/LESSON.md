---
day: 43
phase: 6
phase_name: "MCP II: production"
title: "Stateless by default — deploy-shaped servers"
ids: ["MCP-20", "MCP-21"]
principles: [1, 2, 4, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18]
kind: lab
plan_version: "v2.2.1"
parts: 19
generated: "2026-09-05"
status: written
lab_scaffolded: true
commit: ""
---

# Day 43 — Stateless by default: deploy-shaped servers

> **Yesterday (Day 42):** the whole desk agent went behind an MCP server with `to_mcp_server`, so a
> stranger's host can call Sutra as a tool — agent-as-tool, with agent-as-peer parked until A2A.
> **Today:** the server is run **twice**, behind one address, and every behaviour you have built
> since Day 34 is asked whether it survives being answered by whichever copy happened to be next.
> Three of four do not. Then you find the state statically, move it, and write `sutra_mcp/app.py` —
> the module a platform imports.
> **Tomorrow (Day 44):** the other end of the wire. `sutra/mcp/hardening.py` gets retries, timeouts
> and the no-held-connection rule, because a client that assumes a server is always there is the
> mirror image of today's mistake.

---

## §1 Where we are

[Day 32](../day-32-mcp-stateless-core/LESSON.md) explained why MCP deleted its handshake. The
argument was arithmetic: three interchangeable copies of a server behind one address, one held
session, and two of every four requests land on a copy that never met you. You read it, you agreed
with it, and you have been building on that basis ever since.

Nothing you have run has ever tested it.

Every server in Phase 5 and Phase 6 has been one process on one laptop answering one caller, and
under those conditions a dictionary at module level and a row in a database behave identically. That
is not a small caveat. It is the reason this class of bug reaches production at all: the mistake is
invisible in exactly the conditions you develop in, and obvious in exactly the conditions you
deploy in.

So today is not "the stateless lesson" again. Day 32 asked *why is the architecture stateless*. Today
asks a narrower and much more practical question: **the protocol no longer holds state for you, so
where did yours go?**

The answer is that it went into module level, one convenient line at a time, and nobody decided it.
A dictionary because passing it around was tedious. A cache because a read felt slow. A counter
because somebody wanted a number in the logs. An open connection because opening one per call seemed
wasteful. None of those is a design decision anybody would defend, because none of them was ever
taken as one.

The day has four movements. **Find it** — a static scan over `sutra_mcp/` that exits non-zero. **Prove
it** — two real instances behind a round-robin, running the ordinary request sequence, with an
ablation switch. **Move it** — down into a store, out into the payload, or nowhere at all, and then
the second half of that fix, which is that shared and safe are different words. **Ship it** —
`sutra_mcp/app.py`, an object rather than a program, satisfying a container contract you can read for
nothing and will not pay to use.

The deploy target itself is **🅿️ parked**, and the reason is Principle 15: every managed container
platform needs a billing account. What is not parked is the contract those platforms publish, which
turns out to be exactly the list this day derives from first principles.

---

## §2 The map

Nineteen parts in six sections, no paper part — two cite Day 32's as an address. The sections are
**stages of one investigation** rather than one per ID: section 1 is what accumulates, section 2 is
how you find it without running anything, section 3 is the two-instance test, section 4 is where the
state goes instead, section 5 is the module a platform imports, and section 6 is the two things
production gets wrong afterwards. The day climbs `foundation → working → production`.

### Section 1 — `01-accidental-state`: the state nobody decided to add (MCP-20)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [The dictionary nobody called state](parts/01-accidental-state/1.1-the-dictionary-nobody-called-state.md) | One dictionary per process, and the sentence that lost a line | `foundation` |
| 1.2 | [The cache that becomes a second opinion](parts/01-accidental-state/1.2-the-cache-that-becomes-a-second-opinion.md) | Stale is one bug; inconsistent is a worse one | `foundation` |
| 1.3 | [The state that is not a dictionary](parts/01-accidental-state/1.3-the-state-that-is-not-a-dictionary.md) | Connections, pools, files, locks, context vars, seeds | `working` |
| 1.4 | [The session your SDK keeps for you](parts/01-accidental-state/1.4-the-session-your-sdk-keeps-for-you.md) | `_server_instances`, and one keyword argument | `working` |

### Section 2 — `02-finding-the-state`: a check that reads the code (MCP-20)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [Reading the code without running it](parts/02-finding-the-state/2.1-reading-the-code-without-running-it.md) | Why parse rather than import, and what `tree.body` is | `foundation` |
| 2.2 | [The four shapes worth flagging](parts/02-finding-the-state/2.2-the-four-shapes-worth-flagging.md) | Four rules, and everything immutable left alone | `working` |
| 2.3 | [The waiver that has a reason on it](parts/02-finding-the-state/2.3-the-waiver-that-has-a-reason-on-it.md) | Fix the shape, waive with a reason, or lose the check | `working` |
| 2.4 | [A scan that can go red](parts/02-finding-the-state/2.4-a-scan-that-can-go-red.md) | Exit codes, and green that means nothing | `production` |

### Section 3 — `03-two-instances`: two instances, one URL (MCP-21)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [The dispatcher that knows nothing](parts/03-two-instances/3.1-the-dispatcher-that-knows-nothing.md) | Why the balancer must be stupid on purpose | `working` |
| 3.2 | [The same question, twice, one URL](parts/03-two-instances/3.2-the-same-question-twice-one-url.md) | Four behaviours in, one out, and an exit code | `working` |
| 3.3 | [💥 Two answers to one question](parts/03-two-instances/3.3-two-answers-to-one-question.md) | Both calls succeeded and the model reconciles them | `production` |
| 3.4 | [💥 Three a day, per instance](parts/03-two-instances/3.4-three-a-day-per-instance.md) | A limit times the replica count, chosen by an autoscaler | `production` |
| 3.5 | [💥 The handle B had never heard of](parts/03-two-instances/3.5-the-handle-b-had-never-heard-of.md) | The right interface over the wrong storage | `production` |

### Section 4 — `04-where-state-goes`: down, out, or nowhere (MCP-21)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [Down, out, or nowhere](parts/04-where-state-goes/4.1-down-out-or-nowhere.md) | Three destinations and what each one costs | `working` |
| 4.2 | [Shared is not the same as safe](parts/04-where-state-goes/4.2-shared-is-not-the-same-as-safe.md) | 100 increments, 30 counted, and one keyword | `production` |

### Section 5 — `05-deploy-shape`: the module a platform imports (MCP-20)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [An object, not a program](parts/05-deploy-shape/5.1-an-object-not-a-program.md) | What `sutra_mcp/app.py` exports and must not contain | `working` |
| 5.2 | [🅿️ The platform you are not paying for](parts/05-deploy-shape/5.2-the-platform-you-are-not-paying-for.md) | Five contract rules, none of which needs an account | `production` |

### Section 6 — `06-in-production`: what gets it wrong afterwards

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 6.1 | [💥 The health check that says yes](parts/06-in-production/6.1-the-health-check-that-says-yes.md) | Liveness, readiness, and a green tick over a blown budget | `production` |
| 6.2 | [Sticky sessions, the anaesthetic](parts/06-in-production/6.2-sticky-sessions-the-anaesthetic.md) | The fix that works today and bills you on the next deploy | `production` |

**No paper part today.** Two parts carry §6 *The paper behind it* as an address to
*Principled design of the modern Web architecture* (`doi:10.1145/514183.514185`), taught on
[Day 32](../day-32-mcp-stateless-core/papers/01-modern-web-architecture.md):
[1.1](parts/01-accidental-state/1.1-the-dictionary-nobody-called-state.md) and
[4.1](parts/04-where-state-goes/4.1-down-out-or-nowhere.md). A paper is taught once in the whole
curriculum.

**Read the sections in order.** Section 2's rules are section 1's list; section 3 exists because
section 2 cannot see everything; section 4 is section 3's fix and section 5 is where the fix is
delivered.

---

## §3 Setup — run this

**No package is added today and none is upgraded.** `mcp` stays at `1.29.1`, `google-adk` at
`2.7.1`. `git diff pyproject.toml uv.lock` must be empty when you finish. `uvicorn` and `starlette`
are already installed because `mcp==1.29.1` requires them — §8 records the versions and what pinning
them directly would cost.

```bash
# 1 - the day's lab
cd days/day-43-stateless-by-default
mkdir -p lab

# 2 - section 2: the static scan
touch lab/scan.py lab/shapes.py

# 3 - section 3: two instances behind one URL
touch lab/leaky_server.py lab/dispatcher.py lab/twoup.py

# 4 - section 4: where the state goes, and whether it is safe there
touch lab/store.py lab/race.py

# 5 - sections 5 and 6: the deploy shape and the health check
touch lab/deploy_shape.py lab/health.py
cd -

# 6 - the module you are about to write (you type every line)
touch sutra_mcp/app.py

# 7 - the freshness gate, before anything else
curl -sL https://modelcontextprotocol.io/specification/versioning | grep -o "specification/2026-07-28" | head -1
```

**Step 7 is the gate**, and it has changed since Day 34 wrote it: that page now answers a redirect,
so the same command **without `-L` prints nothing at all** and looks exactly like a failed check. It
printed `specification/2026-07-28` on 2026-09-05, so nothing has moved and no amendment is required
(Principle 14). A gate whose silent failure is indistinguishable from its pass is worth noticing on a
day about exactly that.

**Three ports and one file.** The lab uses `8900` for the dispatcher, `8901` and `8902` for the two
instances, and writes `lab/shared.sqlite3` and `lab/race.sqlite3`. Nothing listens on anything but
`127.0.0.1`, and every process is started and stopped by the probe itself — you never run three
terminals by hand.

**`sutra_mcp/` is yours and it is shared.** `server.py` and `tools.py` are Day 34's, `resources.py`
and `prompts.py` are Day 35's, `tasks.py` is Day 36's, `auth.py` is Day 37's, `db_tools.py` is Day
39's, `capabilities.py` is Day 41's, `agent_server.py` is Day 42's. Today adds `app.py` beside them,
and it is the only module in the package that registers nothing.

---

## §4 Build brief

### The project code — `sutra_mcp/app.py`, and you type every line

One file, one public name. The parts give you every mechanism; the decisions are yours.

| File | Public symbols | What it must do |
| --- | --- | --- |
| `sutra_mcp/app.py` | `app` | Import `build_server`, build the ASGI application, assert the transport, start nothing. |

- `app` is an ASGI application object, built by calling `build_server().streamable_http_app()`. No
  `if __name__ == "__main__":`, no `run()`, no argument parsing (5.1).
- The port and the bind address come from the environment with local defaults, never from `sys.argv`
  (5.1, 5.2).
- The module must import quickly and do no work at import beyond building objects (5.1).

**`TODO(me)` markers left for you:**

- **1.4** — decide where `stateless_http` is recorded so `app.py` can read it back, and write the
  assertion. `app.state` is a Starlette namespace the SDK does not populate with this flag, and
  reaching into `server.session_manager.stateless` uses a private attribute. Pick one, say why, and
  say what the assertion should do on a running server rather than at import.
- **2.2** — add a fifth rule to `lab/scan.py`: a mutable default argument, `def f(seen: dict = {})`.
  Then decide whether it belongs in the same check as the other four, given that it is per process
  but not per module.
- **2.4** — make the scan report how many files it parsed, and fail when that is zero. Then decide
  what a missing target path should do, and write the reason in a comment — the lab's answer (print
  and continue) is arguable and is not the answer for a pipeline.
- **3.2** — point `twoup.py` at your own `sutra_mcp` package instead of the lab's leaky server, and
  record which of the four behaviours survive. That result, not the lab's, is what Day 45 audits.
- **4.1** — decide the expiry policy for every handle `sutra_mcp` mints: how long an unfinished draft
  or task record is worth keeping, what deletes it, and what an expired handle returns. The `drafts`
  table in `lab/store.py` has no `expires_at` column and that is a real gap, not a simplification.
- **4.2** — go through `sutra_mcp/tasks.py` and `sutra_mcp/db_tools.py` and find every
  read-modify-write. For each one, decide between a single conditional `UPDATE` and an explicit
  `BEGIN IMMEDIATE`, and write down which and why.
- **4.2** — choose Sutra's `busy_timeout`. The default is zero. Say what number you chose and what
  happens to a caller who waits that long.
- **6.1** — write `readyz` for `sutra_mcp`: decide which dependencies it checks, which it must not
  check, and how long its answer is cached. Then say which of the two endpoints the deployment's
  traffic probe should use.
- **6.2** — write Sutra's position on session affinity as three sentences somebody could paste into
  a ticket, including the one narrow case where it is legitimate.

### The lab — nine scripts, all of which run, none of which call a model

| File | What it does | Taught in |
| --- | --- | --- |
| `lab/scan.py` | the static scan; four rules, a waiver, an exit code | 2.1, 2.2, 2.3, 2.4 |
| `lab/shapes.py` | one file holding one of each shape, plus two that must not fire | 2.2 |
| `lab/leaky_server.py` | a deploy-shaped MCP server with three deliberate leaks | 1.1, 1.2, 3.3, 3.4, 3.5, 6.1 |
| `lab/dispatcher.py` | the round-robin, thirty lines, no memory | 3.1 |
| `lab/twoup.py` | the probe: four behaviours, four arms, an exit code | 3.2, 3.5, 6.2 |
| `lab/store.py` | the shared store: handles, quota, ticket status | 4.1 |
| `lab/race.py` | four processes, 100 increments, with and without a transaction | 4.2 |
| `lab/deploy_shape.py` | what the ASGI object is, without opening a socket | 1.4, 5.1 |
| `lab/health.py` | liveness green, correctness red, in one run | 6.1 |

These are teaching material and they are given complete in the parts. Type them, run them, and break
them where the *Check yourself* sections ask you to.

---

## §5 The eval that must be able to fail

Four checks with exit codes, all on zero model calls.

**The scan** is the static gate, and its most instructive property is that it is green on an empty
package:

```bash
uv run python days/day-43-stateless-by-default/lab/scan.py sutra sutra_mcp; echo "exit: $?"
uv run python days/day-43-stateless-by-default/lab/scan.py days/day-43-stateless-by-default/lab/shapes.py; echo "exit: $?"
```

Measured on 2026-09-05: six findings in `sutra/` and none in `sutra_mcp/`, `exit: 1`; then five
findings from `shapes.py`, `exit: 1`. The six are all constants written as mutable types — fix the
shape rather than waive them, and watch the count fall. The zero from `sutra_mcp/` is not a pass, it
is an empty directory, and 2.4 is about the difference.

**The two-instance probe** is the day's real gate, and it has four arms:

```bash
cd days/day-43-stateless-by-default/lab
uv run python twoup.py; echo "exit: $?"
uv run python twoup.py --shared; echo "exit: $?"
uv run python twoup.py --pinned; echo "exit: $?"
uv run python twoup.py --stateful; echo "exit: $?"
```

`behaviours that did not survive: 3` and `exit: 1`, then `0` and `exit: 0`. The third arm is the
warning: the **same broken server** passes when the caller is pinned to one instance, which is what
session affinity buys and what 6.2 is about. The fourth prints a real `404 Session not found` from
the SDK's own session table.

**The lost-update ablation** is section 4's check, and both arms must be run:

```bash
cd days/day-43-stateless-by-default/lab
uv run python race.py --unsafe; echo "exit: $?"
uv run python race.py; echo "exit: $?"
```

`counter says: 30` against `counter says: 100`, from four processes and a hundred increments. Then
break it a third way on purpose: change `BEGIN IMMEDIATE` to a plain `BEGIN` and watch three of four
workers die with `sqlite3.OperationalError: database is locked`.

**The health-check ablation** is section 6's, and the point is what does *not* change:

```bash
cd days/day-43-stateless-by-default/lab
uv run python health.py; echo "exit: $?"
uv run python health.py --shared; echo "exit: $?"
```

`exit: 1` then `exit: 0`, and the two `liveness` blocks are byte-for-byte identical. A check that
prints the same thing for a correct system and a broken one has no discriminating power over
anything this day is about.

**And the one that opens no socket:**

```bash
cd days/day-43-stateless-by-default/lab
uv run python deploy_shape.py
```

`manager.stateless : True` then `False`, from two objects built in one process. That line is what
`app.py`'s assertion has to end up checking.

---

## §6 Request budget

**Free-tier Gemini**, 20 generate requests per day per model (`gemini-3.7-flash`, roster re-verified
2026-09-05).

| What | Generations |
| --- | --- |
| every part in every section | **0** |
| all nine lab scripts, every flag | **0** |
| the four probe arms and the lost-update ablation | **0** |
| `sutra_mcp/app.py` and the scan over `sutra_mcp/` | **0** |
| **Total planned** | **0 of 20** |

**Zero, and it could not be otherwise.** Nothing today is a question about language. It is a question
about *where a value lives*, and every one of those is answered by two processes, one file and a
counter. The only network traffic leaving your machine is the HTTPS GET to the specification site in
§3; the rest is `127.0.0.1` talking to itself on three ports.

Attaching a model to any of this would make the runs slower, non-deterministic and expensive, and
would not add a single fact. 3.3 is the closest the day comes to needing one, and even there the
point is made by two lines of tool output that a model *would* have read.

**Cost: $0.**

---

## §7 Traps

- **A module-level dictionary is one dictionary per process**, and a function that writes to it is
  remembering something, whatever it feels like while you are typing it (1.1).
- **A failure can be a successful call.** `ERROR B: unknown handle` came back as an ordinary tool
  result, so nothing counting errors saw it (1.1, 3.5).
- **`lru_cache` has no expiry.** It evicts on size and for no other reason, so a stale entry lives
  until the process does (1.2).
- **Two caches are not "stale", they are inconsistent** — there is no single answer to be wrong, and
  a per-process cache cannot be invalidated by another process (1.2, 3.3).
- **A model reads both contradictory answers in one turn** and produces a fluent sentence describing
  events that never happened (3.3).
- **State hides in things that hold no data**: a connection, a pool, an open file, a `threading.Lock`,
  a `ContextVar`, a seeded generator (1.3).
- **A `threading.Lock` locks one process.** The code looks careful and the mutual exclusion is per
  instance (1.3).
- **`pool_size × instances × workers` is the number your database sees**, and the middle term is
  chosen by an autoscaler (1.3, 5.1, 5.2).
- **`check_same_thread=False` is not the fix** for the SQLite thread error; it replaces a loud failure
  with a shared transaction (1.3).
- **`stateless_http` defaults to `False`**, so an SDK session dictionary is on by default, and with two
  instances that is `404 Session not found` on half the follow-up requests (1.4, 3.5).
- **The scan cannot see the SDK's session dictionary**, because it is an attribute of a library's
  object rather than a name in your file. The most consequential state in the day is invisible to the
  static check (1.4, 2.2).
- **`Final` is not immutable.** It stops the name being rebound and does nothing about the dictionary
  (2.2).
- **`return len(findings)` is a bug.** An exit code is one byte, so 256 findings exit 0 (2.4).
- **A green scan can mean "nothing to read".** `sutra_mcp/` scans clean today because it is empty
  (2.4).
- **A proxy that drops response headers hides the bugs you are hunting** — this lab's first dispatcher
  swallowed `mcp-session-id` and accidentally tested the stateless path (3.1).
- **Retries make instance-affinity bugs look like noise.** A failure rate of one over the replica
  count that disappears on retry is state in a process, not a race (1.4, 3.5).
- **A shared counter is not a safe counter.** Read-modify-write loses updates; 100 increments counted
  as 30 (4.2).
- **`BEGIN` is not `BEGIN IMMEDIATE`.** A deferred transaction takes the lock after the read, and on
  write-ahead logging it then fails outright rather than waiting (4.2).
- **SQLite's `busy_timeout` defaults to zero**, which is where most of the "SQLite cannot do
  concurrency" folklore comes from (4.2).
- **An ASGI module has no arguments of its own.** Reading `sys.argv` there gets you the server's
  argument, `leaky_server:app` (5.1).
- **A `run()` at module level hangs the import**, with no error and no log line — just a container
  that never becomes ready (5.1).
- **`127.0.0.1` is the specification's local advice and a container platform requires `0.0.0.0`.**
  Both are right; a hard-coded default is wrong in one of them (5.2).
- **Everything at module level runs once per worker, not once per container.** Four workers on three
  containers is twelve copies (5.1).
- **A liveness check answers a question nothing in this day asks.** Every failure here happens on a
  process that is running perfectly (6.1).
- **A readiness check wired to an optional dependency takes the whole fleet out at once** (6.1).
- **Session affinity makes every failure in this day disappear**, turns an inconsistent cache into a
  consistently wrong one, and comes back on the next rolling deploy (6.2).

---

## §8 Verify before you code

Fetched or run on **2026-09-05**, the day this was written.

**The specification — the freshness gate and the two pages this day is built on:**

- `https://modelcontextprotocol.io/specification/versioning` — still names **2026-07-28** as the
  current revision. The gate in §3 passes and no amendment is required. **Note the redirect**: the
  page answers `308` now, so Day 34's gate command needs `curl -sL` or it silently prints nothing.
- `https://modelcontextprotocol.io/specification/2026-07-28/basic/index` — the *Statelessness*
  section, quoted in 1.4: *"A server processes each request independently; no state should be
  inferred from previous requests, even those on the same connection or stream."* It carries four
  bullets, of which two are load-bearing today: servers **MUST NOT** rely on prior requests over the
  same connection to establish context, and state spanning multiple requests **MUST** be referenced
  by an explicit identifier the client passes on each request — which is 3.5's whole subject, stated
  as a requirement.
- `https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http` —
  *"Revision 2026-07-28 changed the behavior of Streamable HTTP. […] Changes included: Removal of the
  GET stream endpoint. Removal of protocol-level sessions."*; *"The server MUST provide a single HTTP
  endpoint path (hereafter referred to as the MCP endpoint) that supports POST."*; the
  `Mcp-Method` / `Mcp-Name` required-header table; and *"When running locally, servers SHOULD bind
  only to localhost (127.0.0.1) rather than all network interfaces (0.0.0.0)."* The same page records
  that revisions `2025-03-26` through `2025-11-25` assigned sessions via `Mcp-Session-Id` and that
  *"None of these mechanisms are part of"* the current revision — which is what the installed SDK is
  still doing (1.4).

**The container contract — for the parked topic, so 5.2 quotes rather than remembers:**

- `https://cloud.google.com/run/docs/container-contract` — *"The ingress container within an instance
  must listen for requests on 0.0.0.0 on the port to which requests are sent. Notably, the ingress
  container should not listen on 127.0.0.1. By default, requests are sent to 8080 […] Cloud Run
  injects the PORT environment variable into the ingress container."* Read, not used: nothing on this
  day deploys anything (Addendum 02).

**The installed SDK — the authoritative API surface, read rather than guessed:**

- `.venv/Lib/site-packages/mcp/server/streamable_http_manager.py` — `self._server_instances: dict[str,
  StreamableHTTPServerTransport]` with the comment *"Session tracking (only used if not stateless)"*;
  the `if self.stateless:` dispatch; `_handle_stateless_request` creating a fresh transport per
  request with *"No session ID needed in stateless mode"* and passing `stateless=True` to
  `self.app.run(...)`; and the unknown-session branch returning HTTP **404** with
  `JSONRPCError(code=INVALID_REQUEST, message="Session not found")` — the exact body 3.5 measured.
  Also `raise RuntimeError("Task group is not initialized. Make sure to use run().")`, which is what
  a missing lifespan produces (5.1).
- `.venv/Lib/site-packages/mcp/server/fastmcp/server.py` — `FastMCP.__init__` with
  `host: str = "127.0.0.1"`, `port: int = 8000`, `streamable_http_path: str = "/mcp"`,
  `json_response: bool = False` and **`stateless_http: bool = False`**; `streamable_http_app()`
  building the session manager lazily and returning
  `Starlette(debug=…, routes=…, middleware=…, lifespan=lambda app: self.session_manager.run())`;
  `custom_route(path, methods, …)` whose docstring names health checks and states that such routes
  *"will not require authorization"* (6.1); and `run_streamable_http_async` importing `uvicorn` and
  using `self.settings.host` and `self.settings.port`.
- `.venv/Lib/site-packages/mcp-1.29.1.dist-info/METADATA` — `Requires-Dist: uvicorn>=0.31.1` and
  `Requires-Dist: starlette>=0.27`, which is why §3 adds no package.

**Live commands, re-run today:**

```bash
curl -sL https://modelcontextprotocol.io/specification/versioning | grep -o "specification/2026-07-28" | head -1
uv run python -c "import uvicorn, starlette; print(uvicorn.__version__, starlette.__version__)"
curl -s https://pypi.org/pypi/uvicorn/json | uv run python -c "import sys,json;print(json.load(sys.stdin)['info']['version'])"
curl -s https://pypi.org/pypi/starlette/json | uv run python -c "import sys,json;print(json.load(sys.stdin)['info']['version'])"
```

They printed `specification/2026-07-28`, then `0.52.4 1.6.0`, then `0.52.4`, then `1.6.0`. Installed
and current agree for both.

**The package decision, stated plainly.** This day's commands run an ASGI server that is present only
because `mcp` requires it. That is a real dependency of the deploy path chosen by a transitive
requirement rather than by you, and the correct answer eventually is
`uv add "uvicorn==0.52.4" "starlette==1.6.0"`. **It was deliberately not run**, and nothing in this
day installs anything: a day pins only what it installs, and pinning two direct dependencies for a
deployment this repository does not perform would be taking a decision before its day. §11 carries
the `docs/PACKAGES.md` rows for the day that does build a container.

**No ADK symbol is used anywhere in this day.** Today is entirely server-side and transport-shaped;
`google-adk` is not imported by any lab script.

**No paper was verified today.** `doi:10.1145/514183.514185` already has its dated row in
`docs/PAPERS.md` and is taught on Day 32. It is cited twice here, as an address, and never re-taught.

---

## §9 Say it in an interview

"We had an MCP server that everybody believed was stateless, including me, because the protocol had
removed sessions and we had read the changelog. This was the day we ran it twice.

The rig is three processes on a laptop: two instances of the server and a thirty-line round-robin in
front of them. Round-robin specifically, because anything that survives strict alternation survives
every friendlier routing policy, and a balancer with any memory of callers can hide exactly the bug
you are looking for. Then we sent the ordinary request sequence — a read, a write, two more reads, a
handle minted and used, and a quota spent past its limit — and compared answers rather than status
codes.

Four behaviours, three failed. A per-process `lru_cache` in front of ticket status meant two
consecutive reads of the same ticket came back `open` and `resolved`; both were HTTP 200 and the
database was correct the whole time, so nothing anywhere recorded a problem. A daily budget kept in an
`itertools.count` allowed six requests against a limit of three, because each instance was counting
correctly to three. And a draft handle minted on one instance was unknown on the other — which was the
interesting one, because the *interface* was right. It was an opaque server-minted handle travelling
as an ordinary tool argument, exactly what the specification asks for. The handle pattern is about
naming and carrying; it says nothing about where the data lives. The tell in review is a handle with
the instance name inside it: if the identity has to be in the string, the data is on that instance.

The one nobody had written was the SDK's. The Python server keeps a dictionary of sessions inside each
process and the constructor defaults to using it, so with two replicas a follow-up request came back
`404 Session not found` — and then succeeded on retry, which is why this looks like flakiness in
production. Any intermittent failure whose success rate is one over the replica count is state in a
process, not a race.

The fix has two halves and the second one is the half people skip. State goes down into a shared
store, out into the payload, or nowhere because it was a cache of something cheap — but moving a
counter into a database only fixes reachability. We measured the second half: four processes doing a
hundred increments as read-then-write landed on thirty. Seventy successful updates overwritten. That
needs the arithmetic in the database — `UPDATE … SET n = n + 1 WHERE n < limit` — or an explicit
`BEGIN IMMEDIATE`, and `IMMEDIATE` matters, because a deferred transaction takes the lock after the
read and on write-ahead logging then fails outright.

The thing I would want to be asked about is session affinity, because it is the fix somebody will
propose. We ran it: same broken server, caller pinned to one instance, three failures became zero
without touching a line of code. It is an anaesthetic. The state is still in the wrong place, the
cache now serves a stale answer *consistently* rather than inconsistently, and the pinning stops
holding on exactly the three events you run several instances for — a deploy, a scale-up and a crash.
My rule is that if affinity failing would give a wrong answer rather than a slow one, the design is
broken. And with MCP there is nothing left to protect anyway, because the 2026 revision removed
protocol-level sessions.

We shipped two things. A static scan over the server package — parse the files rather than import
them, flag mutable module-level containers, stateful calls, cache decorators and `global` statements,
waive with a written reason, exit non-zero — and an entry-point module that exports one ASGI object,
reads its port from the environment and starts nothing. Neither of those is clever. What made them
worth having is that we watched both go red first, on real code."

---

## §10 Done when

- Two instances answered the same URL and you can name which behaviours survived and which did not.
- The three failures were each observed, not read about: the cache disagreement, the six-of-six
  quota, and the handle refused by the instance that did not mint it.
- `twoup.py --stateful` printed a real `404 Session not found` and you can say why request 3 worked.
- `twoup.py --pinned` passed on the broken server, and you can say why that is a warning.
- `race.py` was run both ways and the lost updates counted.
- The scan is written, has been red on real code, and its waiver requires a reason.
- `sutra_mcp/app.py` exists, exports `app`, contains no `__main__` block, and asserts the transport.
- The `TODO(me)` markers in §4 are still unsolved.
- **Total generations spent: 0 of 20.**
- `./m depth 43` green, `./m check` green, `./m trace` reports `0 problem(s)`, one commit.

---

## §11 Ledger & commit

**`docs/PROGRESS.md`** — append:

```text
| 43 | 2026-09-05 | MCP-20, MCP-21 | 19 | <hash> | ✅ |
```

**`docs/PACKAGES.md`** — **no new rows.** Nothing was installed and nothing upgraded: `mcp` stays at
`1.29.1`, `google-adk` at `2.7.1`, `gemini-3.7-flash` as pinned on 2026-08-26. `uvicorn 0.52.4` and
`starlette 1.6.0` are present as transitive requirements of `mcp==1.29.1` and are used, not pinned —
§8 states why that decision is deferred. **On the day a container is actually built**, the rows to
append are:

```text
| uvicorn | 0.52.4 | <date> | <day> | ASGI server for `sutra_mcp/app.py`. Present since day 34 as a transitive requirement of `mcp==1.29.1` (`Requires-Dist: uvicorn>=0.31.1`); pinned directly here because the deploy command names it. PyPI current 0.52.4 on 2026-09-05. |
| starlette | 1.6.0 | <date> | <day> | The ASGI framework `FastMCP.streamable_http_app()` returns. Transitive via `mcp==1.29.1` (`Requires-Dist: starlette>=0.27`); pinned directly once `app.py` is deployed. PyPI current 1.6.0 on 2026-09-05. |
```

**`docs/PAPERS.md`** — **no new rows.** `doi:10.1145/514183.514185` already has its row and is taught
on Day 32; this day cites it twice, as an address, in 1.1 and 4.1.

**`docs/SKILL_PROVENANCE.md`** — no new rows. No skill was added or changed.

**The commit:**

```text
day 43: stateless by default - deploy-shaped servers - closes MCP-20, MCP-21
```
