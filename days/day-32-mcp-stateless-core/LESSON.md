---
day: 32
phase: 5
phase_name: "MCP I: the protocol"
title: "MCP 2026 — the stateless core, governance and the registry"
ids: ["MCP-01", "MCP-26", "MCP-32"]
principles: [1, 2, 4, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18]
kind: concept
plan_version: "v2.2.1"
parts: 20
generated: "2026-09-04"
status: written
lab_scaffolded: true
commit: ""
---

# Day 32 — MCP 2026: the stateless core, governance and the registry

> **Yesterday (Day 31):** the quality gate. `./m check` became the standing definition of green —
> lint, format, tests, the skills lint and the `:free` lint in one command — and Phase 4 closed.
> **Today:** Phase 5 opens, and the first thing it does is check its own foundations. MCP is Sutra's
> data boundary; the protocol rewrote itself on 2026-07-28; and the pinned SDK in this repository
> turns out to speak the revision before that one.
> **Tomorrow (Day 33):** the client side — Sutra grows its first MCP client and connects out, over
> stdio and Streamable HTTP, with SSE as parked legacy reading.

---

## §1 Where we are

The shop's entire stock list is in one notebook, and the notebook never leaves the till.

It is accurate. The owner can find anything in it in seconds, and it has never once been wrong. But no
supplier can read it, so nobody can tell him he is about to run out. He cannot send it to anyone, so a
customer asking *"do you have this?"* has to come in and ask. And when he finally buys a computer, the
notebook does not move across — it gets typed in again, by hand, by whoever has an evening free.

That is Sutra this morning. `TICKETS` and `KB` are Python dictionaries inside `sutra/loop.py`. The
vendor status page from Day 15 is a stub you wrote yourself. `sutra/desk/skills.py` reads Markdown off
your own disk. Every piece of data Sutra touches lives inside its own process, and nothing outside can
offer Sutra data or receive it.

The plan has always said what fixes this: **the data boundary is MCP.** Every data source becomes a
server; Sutra itself becomes one. Phase 5 is where that promise starts being kept, and it starts with
fourteen days of protocol.

Four things to know before you read a single part.

**Today writes no project code, and installs nothing.** The mechanism being taught is what is *absent*
from the wire, and you cannot see an absence through a library that hides it. This is Principle 4 with
a network hat on: understand the protocol, then let an SDK be a convenience rather than a mystery.

**MCP shipped its largest revision on 2026-07-28, and it deleted the handshake.** Old MCP was a phone
call — you dial `initialize`, stay connected, hang up. New MCP is the web — every request is
self-contained, any instance answers any request, nothing depends on a held connection. That single
reframe is what section 2 exists for, and the arithmetic behind it is stark: three instances behind a
round-robin dispatcher, one held session, and **two of four requests are refused** on the happy path
with nothing broken.

**Statelessness bought two things that look like details and are not.** The method and tool name now
ride in HTTP headers, so a gateway can route and throttle without parsing a body — and a server must
reject a request whose headers disagree with its body, with `-32020`, because otherwise the gateway
policed something the server never ran. List results became cacheable, and **60 requests become 1**.

**And the day has a finding you were not expecting.** The `mcp` SDK pinned in this repository reports
`LATEST_PROTOCOL_VERSION = '2025-11-25'`. The specification is at `2026-07-28`. Nothing is broken
today and something would have broken on Day 34, which is exactly what §8 is for.

---

## §2 The map

Twenty parts in six sections, plus **one paper**, read last. The day climbs
`foundation → working → production`: section 1 is what MCP is and why it is Sutra's boundary, section 2
is the reframe that ended sessions, section 3 is what statelessness bought, section 4 is who owns the
socket, section 5 is the failure lab and section 6 is the production face.

### Section 1 — `01-the-socket`: what MCP is, and why the boundary is the point (MCP-01)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [The plug that fits](parts/01-the-socket/1.1-the-plug-that-fits.md) | Day 4's declaration, spoken between processes | `foundation` |
| 1.2 | [Host, client, server](parts/01-the-socket/1.2-host-client-server.md) | Three words, three jobs, one client per server | `foundation` |
| 1.3 | [Tools, resources, prompts](parts/01-the-socket/1.3-tools-resources-prompts.md) | Split by who is in control, not by content | `foundation` |
| 1.4 | [Not just another API](parts/01-the-socket/1.4-not-just-another-api.md) | Seven fixed methods against a generated client | `working` |
| 1.5 | [One gate to guard](parts/01-the-socket/1.5-one-gate-to-guard.md) | A boundary you can point at, and its price | `working` |

### Section 2 — `02-the-reframe`: the phone call became the web (MCP-26)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [The call that remembered you](parts/02-the-reframe/2.1-the-call-that-remembered-you.md) | Four messages before the first useful one | `foundation` |
| 2.2 | [Three instances, one URL](parts/02-the-reframe/2.2-three-instances-one-url.md) | 4/4 against 2/4, and why sticky sessions lose | `working` |
| 2.3 | [Every request introduces itself](parts/02-the-reframe/2.3-every-request-introduces-itself.md) | `_meta`, and 184 bytes forever | `working` |
| 2.4 | [The optional question](parts/02-the-reframe/2.4-server-discover-the-optional-question.md) | MUST for servers, MAY for clients | `working` |

### Section 3 — `03-headers-and-caches`: what statelessness bought (MCP-26)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [The label on the envelope](parts/03-headers-and-caches/3.1-the-label-on-the-envelope.md) | Three required headers, and who reads them | `working` |
| 3.2 | [The header that must match](parts/03-headers-and-caches/3.2-the-header-that-must-match.md) | `-32020`, and why refusing beats choosing | `working` |
| 3.3 | [Lists you may keep](parts/03-headers-and-caches/3.3-lists-you-may-keep.md) | 60 → 3 → 1, and a hash that changed | `working` |
| 3.4 | [State that travels in the payload](parts/03-headers-and-caches/3.4-state-that-travels-in-the-payload.md) | Handles: the state moved, it did not vanish | `working` |

### Section 4 — `04-governance-and-registry`: who owns the socket (MCP-32)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [A standard nobody owns](parts/04-governance-and-registry/4.1-a-standard-nobody-owns.md) | The foundation, the SEPs, the twelve-month window | `foundation` |
| 4.2 | [The registry, queried live](parts/04-governance-and-registry/4.2-the-registry-queried-live.md) | Metadata, not code — and no key | `working` |
| 4.3 | [A name that proves its publisher](parts/04-governance-and-registry/4.3-a-name-that-proves-its-publisher.md) | Identity is not safety | `working` |

### Section 5 — `05-failure-lab`: the deliberate failures

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [💥 The tutorial from four months ago](parts/05-failure-lab/5.1-the-tutorial-from-four-months-ago.md) | The SDK is a document, and it has a date | `production` |
| 5.2 | [💥 The header that lied](parts/05-failure-lab/5.2-the-header-that-lied.md) | The forgery attacks the gateway, not the server | `production` |

### Section 6 — `06-in-production`: after it ships

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 6.1 | [Routing without reading](parts/06-in-production/6.1-routing-without-reading.md) | Six decisions, zero bodies parsed | `production` |
| 6.2 | [Before you depend on a server](parts/06-in-production/6.2-before-you-depend-on-a-server.md) | Six intake questions, one exit code | `production` |

### The paper — read it **after** the parts

| Paper | Identifier | What it argued |
| --- | --- | --- |
| [Principled design of the modern Web architecture](papers/01-modern-web-architecture.md) | `doi:10.1145/514183.514185` (2002) | An architecture's useful properties come from the constraints it accepts, each with a named price |

Principle 4 at the scale of a day: measure the failure yourself, *then* read the argument. Every
constraint in that paper has a part in this day that met it as a mechanism first — statelessness in
[2.2](parts/02-the-reframe/2.2-three-instances-one-url.md), cacheability in
[3.3](parts/03-headers-and-caches/3.3-lists-you-may-keep.md), layering in
[6.1](parts/06-in-production/6.1-routing-without-reading.md), the uniform interface in
[1.4](parts/01-the-socket/1.4-not-just-another-api.md).

---

## §3 Setup — run this

**No package is added today, and no package is upgraded.** `git diff pyproject.toml uv.lock` must be
empty when you finish. The `mcp` SDK is already pinned at `1.29.1`; §8 records what it can and cannot
speak, and the decision about that pin belongs to a plan amendment, not to a reading day.

```bash
# 1 - the day's lab
cd days/day-32-mcp-stateless-core
mkdir -p lab/papers/modern-web-architecture

# 2 - section 1: the boundary check
touch lab/boundary_check.py

# 3 - section 2: the envelope, and the cost of the probe
touch lab/letter.py lab/discover_cost.py

# 4 - section 3: headers, caches, handles
touch lab/headers.py lab/cache_math.py lab/handles.py

# 5 - section 4: the registry
touch lab/registry.py

# 6 - section 5: the failure lab
touch lab/sdk_era.py lab/forge.py

# 7 - section 6: the edge, and the intake
touch lab/gateway.py lab/server_intake.py

# 8 - the paper demo
touch lab/papers/modern-web-architecture/instance.py
touch lab/papers/modern-web-architecture/client.py
cd -

# 9 - the gate, before anything else: has the specification moved?
curl -sL https://modelcontextprotocol.io/specification/versioning | grep -o "specification/2026-07-28" | head -1
```

**Step 9 is the gate, and it is not ceremony.** This whole day, the addendum it implements and the
next thirteen days are written against revision **2026-07-28**. If that page names a newer current
revision, stop: amend the plan first, then write code (Principle 14). It printed
`specification/2026-07-28` on 2026-09-04.

**Nothing moves into `sutra/` or `sutra_mcp/` today.** `sutra_mcp/__init__.py` stays empty; Day 34
fills it. Everything in this day is reading, protocol, and eleven scripts in `lab/` that between them
make zero model calls.

**Read the parts in order and the paper last.** Section 2 depends on section 1's vocabulary, section 3
depends on section 2's property, and the paper is only worth reading once you have measured the thing
it argues for.

---

## §4 Build brief

Eleven lab scripts, none of which touch a model. Each belongs to the part that teaches it.

| File | What it does | Taught in |
| --- | --- | --- |
| `lab/boundary_check.py` | AST scan for agent-side modules reaching past the boundary | 1.5 |
| `lab/letter.py` | the 2025 and 2026 shapes of one tool call, and the byte cost of `_meta` | 2.3 |
| `lab/discover_cost.py` | request counts for probe-first against straight-in | 2.4 |
| `lab/headers.py` | derive the three headers from a body; validate; `-32020` | 3.1, 3.2 |
| `lab/cache_math.py` | 60 → 3 → 1, and the hash that changes when the order does | 3.3 |
| `lab/handles.py` | a session against a handle, across three workers | 3.4 |
| `lab/registry.py` | one HTTPS GET to the official registry; namespaces | 4.2, 4.3 |
| `lab/sdk_era.py` | which revision does the installed SDK actually speak | 5.1 |
| `lab/forge.py` | a forged `Mcp-Name` against the validator | 5.2 |
| `lab/gateway.py` | route, throttle and reject on headers alone | 6.1 |
| `lab/server_intake.py` | six intake questions as an exit code | 6.2 |

`lab/papers/modern-web-architecture/` holds the paper demo — `instance.py` and `client.py` — and it is
**given complete** in the paper part. It is teaching material, not a rep: type it, run both arms, and
compare your output with the transcript.

**`TODO(me)` markers left for you:**

- **1.3** — decide whether `lookup_ticket` should become a **resource** on Day 35, and write down the
  cost of the change as well as the benefit.
- **1.5** — decide what else belongs in `FORBIDDEN` for Sutra specifically, then decide whether
  `boundary_check.py` should `assert` rather than print, and which day should own that gate.
- **2.3** — write the single envelope-builder function Sutra's client should use, and the test that
  asserts its version string against what `server/discover` advertises.
- **2.4** — decide and write down what Sutra's client does on **stdio** and what it does over
  **HTTP**: probe first, or straight in, and where the answer is cached.
- **3.2** — extend `validate` with the two things it does not do: Base64 sentinel decoding for
  `Mcp-Name`, and numeric comparison for integer `Mcp-Param-*` values.
- **3.3** — choose the `ttlMs` and `cacheScope` that `sutra_mcp`'s `tools/list` will return on Day 34,
  and write down what must happen *before* a tool is deleted.
- **3.4** — decide Sutra's handle policy: how it is generated, who owns it, when it expires, and what
  error an unknown handle returns.
- **4.2** — pick one registry server a support desk could plausibly use, and write down its full name,
  version and namespace. Day 33 wants a candidate; Day 16's grounding fallback wants one too.
- **5.1** — write the assertion Day 34 needs: the SDK's supported versions contain the revision Sutra
  targets. Decide what it should say when it goes red.
- **6.1** — decide the real `LIMITS` for Sutra's two tools, and say what unit they should be in once
  you accept that a call is not a cost.
- **6.2** — extend `server_intake.py` to accept a package-only server (no `remotes`), and decide where
  the server provenance ledger lives and who generates it.

---

## §5 The eval that must be able to fail

Three checks, all with an exit code, all on zero model calls.

**The intake check** is the day's gate:

```bash
uv run python days/day-32-mcp-stateless-core/lab/server_intake.py; echo "exit: $?"
```

Measured on 2026-09-04: `findings: 3` and `exit: 1`. That is **red on purpose** — the version is stale,
nobody has called `server/discover`, and no human name is attached. Fill `CLAIMED_REVISION` and
`REVIEWED_BY` and set `isLatest` to `True`, and it goes to `findings: 0` and `exit: 0`. Then take
`ac.tandem` out of `ALLOWED_NAMESPACES` and watch the one finding appear that paperwork cannot answer.

**The era check** is the one that is red today and nobody expected it:

```bash
uv run python days/day-32-mcp-stateless-core/lab/sdk_era.py
```

Measured the same day: `SDK speaks the current revision : False`, with
`SUPPORTED_PROTOCOL_VERSIONS : ['2024-11-05', '2025-03-26', '2025-06-18', '2025-11-25']`. Change
`SPEC_REVISION` to `2025-11-25` and it goes green for the wrong reason, which is exactly the assertion
Day 34 has to get right.

**The paper demo** is the ablation, and both arms must be run:

```bash
cd days/day-32-mcp-stateless-core/lab/papers/modern-web-architecture
STATELESS=1 uv run python client.py
STATELESS=0 uv run python client.py
cd -
```

`served 4/4` against `served 2/4`, from the same three servers answering the same four questions.

**And the rest, each of which can be broken on purpose:**

```bash
uv run python days/day-32-mcp-stateless-core/lab/boundary_check.py
uv run python days/day-32-mcp-stateless-core/lab/letter.py
uv run python days/day-32-mcp-stateless-core/lab/discover_cost.py
uv run python days/day-32-mcp-stateless-core/lab/headers.py
uv run python days/day-32-mcp-stateless-core/lab/cache_math.py
uv run python days/day-32-mcp-stateless-core/lab/handles.py
uv run python days/day-32-mcp-stateless-core/lab/gateway.py
uv run python days/day-32-mcp-stateless-core/lab/registry.py
cd days/day-32-mcp-stateless-core/lab && uv run python forge.py && cd -
```

Three of those have a named break in their own part: add `import sqlite3` under `sutra/` and watch
`boundary_check.py` name the file; make `validate` return `None` and watch the forgery pass; remove the
version check from `gateway.py` and watch a `2025-11-25` request get routed like any other.

---

## §6 Request budget

**Free-tier Gemini**, 20 generate requests per day per model (`gemini-3.7-flash`, roster re-verified
2026-09-04).

| What | Generations |
| --- | --- |
| every part in every section | **0** |
| all eleven lab scripts | **0** |
| the paper demo, both arms | **0** |
| the registry query | **0** — one HTTPS GET, no key |
| **Total planned** | **0 of 20** |

**Zero, and that is the point.** A protocol is text on a wire: it is inspected, not generated. Today's
only network traffic is HTTPS GETs to the specification site, to the registry, to PyPI and to a raw
file on GitHub, plus three local HTTP servers on `127.0.0.1`. Your whole day's quota is still there
tomorrow, which is when Day 33 starts spending it.

**Cost: $0.**

---

## §7 Traps

- **The date on the tutorial is part of the tutorial.** Everything written before 2026-07-28 opens with
  `initialize`. It is correct material for a revision that still exists, and following it now means
  hand-building machinery the protocol deleted (5.1).
- **A library is a document too.** `mcp==1.29.1` tops out at `2025-11-25`. Nothing in `pyproject.toml`
  says so and `uv sync` will not tell you (5.1, §8).
- **`400 Bad Request` does not mean "old server".** A modern server also returns 400 for an unsupported
  version, a missing capability and a header mismatch. Read the **body** before falling back to
  `initialize` (2.1).
- **A `_meta` key spelt wrongly is silently ignored.** `_meta` is an open extension point, so a
  lower-case `v` in `protocolVersion` produces a request with no version at all (2.3).
- **`_meta` is inside `params`, not beside it** (2.3).
- **The error codes were renumbered in this revision.** `HeaderMismatch` moved `-32001` → `-32020`,
  `MissingRequiredClientCapability` `-32003` → `-32021`, `UnsupportedProtocolVersion` `-32004` →
  `-32022`, and resource-not-found `-32002` → `-32602`. An older document is wrong about the numbers
  and right about the concepts (3.2, 3.3).
- **Header names are case-insensitive; header values are not.** `Tools/Call` does not match
  `tools/call` (3.2).
- **Do not "helpfully" prefer the body over a mismatched header.** The gateway has already acted on the
  header, and choosing a winner hides that it acted on a request that did not run (3.2, 5.2).
- **`server/discover` is not a handshake.** Nothing is remembered afterwards, so keep handling `-32022`
  on every request no matter what discovery said (2.4).
- **`ttlMs` is milliseconds.** `3600` is not what you meant, and nothing will tell you (3.3).
- **`ttlMs` is also how long a client may keep calling a tool you deleted.** Removing a tool is two
  deployments (3.3).
- **`cacheScope: "public"` on user-specific data is a shared proxy serving one customer's ticket to the
  next caller.** One JSON field, no error, no log line (3.3).
- **A shuffled tool list is a new cache key** — for the client's cache and for the model provider's
  prompt cache. Sort it (3.3).
- **A module-level dict in a server is a session by another name** (2.2, 3.4).
- **A handle with no expiry is a table that only grows**, and a sequential handle is enumerable (3.4).
- **A verified namespace proves authorship, not safety.** `io.github.acme` and `io.github.acme-mcp` are
  both correctly verified and are not the same publisher (4.3).
- **A registry listing is not a security review.** The project says so itself (4.2).
- **An intermediary must check `MCP-Protocol-Version` before trusting any other header**, because only
  a current-revision server promises to reject a lie (6.1).

---

## §8 Verify before you code

Fetched or run on **2026-09-04**, the day this was written.

**The specification — the freshness gate (Principle 14):**

- `https://modelcontextprotocol.io/specification` — the current revision is **2026-07-28**; every
  section card on the page links under `/specification/2026-07-28/`, and the page's own "Key Details"
  now reads *"Stateless, self-contained requests"* and *"Per-request capability negotiation"*.
- `https://modelcontextprotocol.io/specification/versioning` — states it outright: *"The **current**
  protocol version is **2026-07-28**."* **It has not moved.** The plan and Addendum 01 remain correct
  and no amendment is required on that count.
- `https://modelcontextprotocol.io/specification/2026-07-28/changelog` — every mechanism in sections 2
  and 3 came from here, with its SEP number: `SEP-2575` (handshake removed, `server/discover` added),
  `SEP-2567` (sessions removed, state handles), `SEP-2243` (`Mcp-Method`/`Mcp-Name`, `x-mcp-header`),
  `SEP-2549` (`ttlMs`, `cacheScope`), `SEP-2322` (MRTR, `resultType`), `SEP-2596` (feature lifecycle),
  `SEP-2577` (Roots, Sampling and Logging deprecated).
- `https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http` — the
  header table, the `-32020` rule, the two complete example requests, the Base64 sentinel encoding and
  the backward-compatibility rules.
- `https://modelcontextprotocol.io/specification/2026-07-28/server/discover` — the MUST/MAY asymmetry,
  and both example messages.

**Governance and the registry:**

- `https://blog.modelcontextprotocol.io/posts/2025-12-09-mcp-joins-agentic-ai-foundation/` — the
  donation, dated 2025-12-09, and the member list quoted in 4.1.
- `https://modelcontextprotocol.io/registry` — namespace verification via GitHub, DNS or HTTP
  challenges; the preview warning; the delegation of security scanning.
- `https://registry.modelcontextprotocol.io/v0/servers?limit=5` — queried live and returning real
  entries; the output in 4.2 is that response.

**The installed packages — the authoritative API surface, read rather than guessed:**

- `.venv/Lib/site-packages/mcp/types.py` and `mcp/shared/version.py` —
  `LATEST_PROTOCOL_VERSION = "2025-11-25"`, `DEFAULT_NEGOTIATED_VERSION = "2025-03-26"`,
  `SUPPORTED_PROTOCOL_VERSIONS = ["2024-11-05", "2025-03-26", "2025-06-18", "2025-11-25"]`, and
  `InitializeRequest` still exported. **The pinned SDK does not speak 2026-07-28.**
- `.venv/Lib/site-packages/google/adk/tools/mcp_tool/__init__.py` — exports `McpToolset`/`MCPToolset`,
  `McpTool`/`MCPTool`, `StdioConnectionParams`, `StreamableHTTPConnectionParams`,
  `SseConnectionParams`, `to_mcp_server`, `adk_to_mcp_tool_type`, `gemini_to_json_schema`, all inside
  a `try/except ImportError` that logs *"MCP Tool is not installed"*. **No ADK symbol is used in any
  part today** — Day 33 is where they arrive, and this is recorded so that day starts from a read
  surface rather than a memory.
- `https://adk.dev/mcp/` — read, and it names no MCP revision and no SDK version. Noted rather than
  cited: for this phase the installed package is the authority, and the ADK page defers to its own API
  reference.

**Two live lookups, and one flag for the plan (Principle 14):**

```bash
curl -s https://pypi.org/pypi/mcp/json | uv run python -c "import sys,json;print(json.load(sys.stdin)['info']['version'])"
curl -s https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/v2.1.1/src/mcp-types/mcp_types/version.py | grep -A1 "^MODERN_PROTOCOL_VERSIONS"
```

They printed `2.1.1` and
`MODERN_PROTOCOL_VERSIONS: Final[tuple[str, ...]] = ("2026-07-28",)`. So the published SDK has caught
up and **this repository's pin has not**. Nothing is changed today: a version bump is a plan decision
with a `docs/PACKAGES.md` row behind it, and it belongs to whoever writes Day 33 or Day 34. It is
recorded here so that decision is made deliberately rather than discovered.

**One correction to Addendum 01, recorded, no structural change.** The addendum describes AAIF as
*"Anthropic, OpenAI, Block as co-founders; AWS, Google, Microsoft supporting"*. The live announcement
gives the same three co-founders and adds Cloudflare and Bloomberg to the support list. Same story, two
more names; the addendum's interview line survives unchanged (4.1).

**No paper was verified today.** `doi:10.1145/514183.514185` was assigned with its row already in
`docs/PAPERS.md`; its metadata — *ACM Transactions on Internet Technology*, volume 2, issue 2, pages
115–150, May 2002 — and the abstract quoted in the paper part came from the Crossref record for that
DOI, read the same day.

---

## §9 Say it in an interview

"Our agent had everything in-process — the ticket store was a Python dict — so nothing outside could
give it data and it could not give data to anything. We put MCP at the data boundary, which means every
data source is a server and eventually the agent is one too. The reason that is worth a network hop is
that it gives security exactly one gate to guard, and it lets the thing behind the socket be replaced
without touching the agent.

The part I would emphasise is what the 2026-07-28 revision changed, because it is a good example of a
protocol correcting itself in public. MCP used to open with an `initialize` handshake and hold a
session, and the session was pinned to whichever instance answered it. We measured that: three
instances behind a round-robin dispatcher, one held session, and two out of four requests get refused
on the happy path with nothing broken. The old workaround was sticky sessions, which pins conversations
to instances and takes away the point of running three. So the revision deleted the handshake. Every
request now carries its protocol version, capabilities and client identity in a `_meta` block — about
184 bytes, repeated forever — and in exchange any instance answers anything.

Two consequences that sound like details and are not. The method and tool name are mirrored into HTTP
headers, so a gateway routes, rate limits and counts per tool without parsing a body — and the server
*must* reject a request whose headers disagree with the body, with `-32020`, because otherwise the
gateway policed a request that never ran. And list results became cacheable with a TTL and a scope,
which took a working session's tool listings from sixty requests to one. The catch is a staleness
window: for as long as the TTL says, a client can be offering a tool you deleted, so removing a tool is
two deployments.

On governance — and this is the reason I was comfortable betting a data boundary on it — MCP was
donated to the Agentic AI Foundation under the Linux Foundation in December 2025, co-founded by
Anthropic, Block and OpenAI with support from Google, Microsoft, AWS, Cloudflare and Bloomberg. There
is a numbered public proposal process and a minimum twelve-month deprecation window, so changes arrive
as scheduled events with migration paths. There is also an official registry, and it is worth being
precise about what it proves: names are reverse-DNS and you must verify the domain or the GitHub
account, so it proves authorship. It explicitly does not do security scanning.

The most useful thing we found was accidental. We ran six lines that printed the installed SDK's
supported protocol versions, and our pinned version topped out at the revision *before* the one we
were building against, while the current release already spoke the new one. Nothing was broken yet, and
it would have been the day we wrote a server. The habit I took away is that the date on a document is
part of the document — and a library is a document."

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked and `./m depth 32` is green. Defined by
understanding and green checks, never by elapsed time — a part is finished when you could explain it to
someone else without the page open.

**Phase 5's gate** is `sutra-mcp` serving tools statelessly, on Day 38. Today closes the protocol half:
you can read a modern request with your eyes, say what the revision changed and why, name who governs
the socket, and query the registry. Day 33 connects a client, Day 34 writes the server, and the two
`TODO(me)` items about `ttlMs` and the handle policy are the decisions that day will need already made.

---

## §11 Ledger & commit

**`docs/PROGRESS.md`** — append:

```text
| 32 | <date> | MCP-01, MCP-26, MCP-32 | 20 | <hash> | ✅ |
```

**`docs/PACKAGES.md`** — **no new rows.** Nothing was installed and nothing upgraded: `mcp` stays at
`1.29.1`, `google-adk` at `2.7.1`, and `gemini-3.7-flash` stays pinned as recorded on 2026-08-26. The
finding that PyPI's `mcp` is at `2.1.1` and speaks `2026-07-28` is recorded in §8 for whoever decides
the bump; it is not a row until something is installed.

**`docs/PAPERS.md`** — **no new rows.** `doi:10.1145/514183.514185` already has its dated row, and it
is taught here in [`papers/01-modern-web-architecture.md`](papers/01-modern-web-architecture.md). The
ICSE 2000 version `doi:10.1145/337180.337228` also has its row and is named in that part as the one
*not* to cite.

**`docs/SKILL_PROVENANCE.md`** — no new rows. No skill was added or changed.

**The commit:**

```text
day 32: MCP 2026 - the stateless core, governance and the registry - closes MCP-01, MCP-26, MCP-32
```
