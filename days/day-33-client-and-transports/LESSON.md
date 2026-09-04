---
day: 33
phase: 5
phase_name: "MCP I: the protocol"
title: "The client side — Sutra plugs into its first MCP server"
ids: ["MCP-02", "MCP-03"]
principles: [1, 2, 4, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18]
kind: lab
plan_version: "v2.2.1"
parts: 19
generated: "2026-09-04"
status: written
lab_scaffolded: true
commit: ""
---

# Day 33 — The client side: Sutra plugs into its first MCP server

> **Yesterday (Day 32):** the protocol, read and not yet spoken. The 2026-07-28 revision deleted the
> handshake, headers took over routing, listings became cacheable, and the pinned SDK turned out to
> speak the revision before that one.
> **Today:** Sutra grows a client. `sutra/mcp/client.py` gets `connect_stdio`, `connect_http` and
> `list_tools`, and by the end a tool that lives in another process is listed by name with zero model
> calls spent.
> **Tomorrow (Day 34):** the other end. `sutra_mcp/server.py` and `sutra_mcp/tools.py` put
> `lookup_ticket` and `search_kb` on the wire, and today's client is what you test it with.

---

## §1 Where we are

Yesterday you learned to read a protocol. Today Sutra speaks it, and the first thing to notice is how
little of that is visible from the agent.

Think about the office printer. You click Print in the same place in the same menu you always do, and
a minute later there are warm pages in a tray down the corridor, on a machine you did not choose and
have been in the same room with twice. The corridor is invisible and that is the entire value. Then
one Tuesday nothing comes out, the screen says the job went fine, and you walk down the corridor to
find an empty paper tray — and now the corridor is the only thing that matters, and the thing on your
screen cannot tell you about it, because it never knew.

That is `McpToolset` in one paragraph. It is Sutra's MCP client wearing a toolset's clothes: one
object in `tools=[...]`, exactly the abstraction Day 15 introduced, with a process boundary hidden
inside it. On a good day an MCP tool is indistinguishable from the local Python functions of Day 10.
On a bad day it can time out, be down, have its process die, or rename itself between two runs, and
none of those things can happen to a local function.

Four things to know before you read a part.

**Today writes real project code, and installs nothing.** `sutra/mcp/__init__.py` and
`sutra/mcp/client.py` are yours to write. `mcp==1.29.1` and `google-adk==2.7.1` are already pinned;
`git diff pyproject.toml uv.lock` must be empty when you finish.

**There are two transports and they are the same protocol.** stdio launches the server as a child
process and pipes newline-delimited JSON-RPC through its standard streams. Streamable HTTP posts each
message to one URL. The specification says protocol semantics are identical on every binding, so the
choice between them is operational: does anything other than this client need to reach this server?
The old HTTP+SSE transport is 🅿️ **parked** — deprecated since revision `2025-03-26`, with the
shortest removal clock in the spec's registry — and this day recognises it and never builds on it.

**Almost everything that goes wrong here goes wrong quietly.** A wrong command constructs perfectly
and fails four layers later with an error that does not name it. A missing `tool_filter` is a
successful run in which the model was handed a tool that deletes every ticket. A `print` in a server
either produces a traceback you ignore or eats a reply, and which one depends on a trailing newline
nobody was thinking about.

**And this day connects to a fake on purpose.** `lab/fake_desk_server.py` is eighty lines of
hand-written JSON-RPC with no MCP SDK in it, so every byte on the wire is readable in one file. It is
labelled a fake because Day 34 writes the real server, and because Principle 4 says you build the
mechanism before you adopt the library.

---

## §2 The map

Nineteen parts in six sections, no paper part — two are cited as addresses to papers taught earlier.
The day climbs `foundation → working → production`: section 1 is the client as an object, sections 2
and 3 are the two transports, section 4 is the choice between them, section 5 is the failure lab and
section 6 is the production face.

### Section 1 — `01-the-connector`: what a client is, in code (MCP-02)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [The tool that lives somewhere else](parts/01-the-connector/1.1-the-tool-that-lives-somewhere-else.md) | `McpToolset` is the client, disguised as a toolset | `foundation` |
| 1.2 | [Constructing is not connecting](parts/01-the-connector/1.2-constructing-is-not-connecting.md) | A wrong address builds perfectly | `foundation` |
| 1.3 | [Before the model sees a tool](parts/01-the-connector/1.3-before-the-model-sees-a-tool.md) | Five steps, and two of them can hide a tool | `working` |
| 1.4 | [The allowlist is a constructor argument](parts/01-the-connector/1.4-the-allowlist-is-an-argument.md) | An instruction requests; a tool list grants | `working` |
| 1.5 | [Somebody has to give it back](parts/01-the-connector/1.5-somebody-has-to-give-it-back.md) | What `close()` releases, and who calls it | `working` |

### Section 2 — `02-stdio`: the local wire (MCP-03)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [Connecting is launching](parts/02-stdio/2.1-connecting-is-launching.md) | The address is a command line | `foundation` |
| 2.2 | [One message per line](parts/02-stdio/2.2-one-message-per-line.md) | One newline, no framing header, no recovery | `working` |
| 2.3 | [The only place left to talk](parts/02-stdio/2.3-the-only-place-left-to-talk.md) | stderr, and what a client must not conclude from it | `working` |
| 2.4 | [Closing up](parts/02-stdio/2.4-closing-up.md) | Close stdin, wait, escalate — and restart is a recovery | `working` |

### Section 3 — `03-streamable-http`: the remote wire (MCP-03)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [One endpoint, one trip per question](parts/03-streamable-http/3.1-one-endpoint-one-trip.md) | One URL, one POST per message, no connect step | `working` |
| 3.2 | [Handed over, or told to wait](parts/03-streamable-http/3.2-handed-over-or-told-to-wait.md) | A JSON object or a request-scoped stream | `working` |
| 3.3 | [Standing up is how you cancel](parts/03-streamable-http/3.3-standing-up-is-how-you-cancel.md) | The one place the transports really differ | `working` |
| 3.4 | [What a URL costs](parts/03-streamable-http/3.4-what-a-url-costs.md) | `Origin`, localhost, and DNS rebinding | `production` |

### Section 4 — `04-choosing-a-wire`: the decision (MCP-02 · MCP-03)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [The same errand, two ways to run it](parts/04-choosing-a-wire/4.1-the-same-errand-two-ways.md) | Identical semantics, one operational question | `working` |
| 4.2 | [🅿️ The route with a withdrawal date](parts/04-choosing-a-wire/4.2-the-route-with-a-withdrawal-date.md) | HTTP+SSE: recognise it, never build on it | `production` |

### Section 5 — `05-failure-lab`: the deliberate failures

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [💥 The log line that ate the reply](parts/05-failure-lab/5.1-the-log-line-that-ate-the-reply.md) | One newline decides logged-and-ignored or gone | `production` |
| 5.2 | [💥 The spanner that was not in the boot](parts/05-failure-lab/5.2-the-spanner-not-in-the-boot.md) | Four layers accept a command that does not exist | `production` |

### Section 6 — `06-in-production`: after it ships

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 6.1 | [The connection you must not hold](parts/06-in-production/6.1-the-connection-you-must-not-hold.md) | Reuse connections, depend on none of them | `production` |
| 6.2 | [Ten servers, ten clients](parts/06-in-production/6.2-ten-servers-ten-clients.md) | Ten failure domains, one critical path | `production` |

**No paper part today.** Two parts carry §6 *The paper behind it* as an address to a paper taught
earlier: [1.1](parts/01-the-connector/1.1-the-tool-that-lives-somewhere-else.md) cites
*Implementing remote procedure calls* (`doi:10.1145/2080.357392`, taught on Day 15) and
[3.1](parts/03-streamable-http/3.1-one-endpoint-one-trip.md) cites *Principled design of the modern
Web architecture* (`doi:10.1145/514183.514185`, taught on Day 32). A paper is taught once in the whole
curriculum; every later day links to it.

**Read the sections in order.** Section 2 and section 3 both depend on section 1's vocabulary, and
section 4's decision is not meaningful until you have met both wires.

---

## §3 Setup — run this

**No package is added today, and no package is upgraded.** `mcp` stays at `1.29.1` and `google-adk`
at `2.7.1`. `git diff pyproject.toml uv.lock` must be empty when you finish. The finding recorded in
Day 32 §8 — that PyPI's `mcp` is at `2.1.1` and speaks `2026-07-28` while this repository is pinned at
`1.29.1` — still stands, is still not a bug today, and is still a plan decision rather than a day's
decision (Principle 14). §8 below says exactly what it costs you.

```bash
# 1 - the day's lab
cd days/day-33-client-and-transports
mkdir -p lab

# 2 - the far end, and the smallest client
touch lab/fake_desk_server.py lab/list_tools.py

# 3 - the stdio parts
touch lab/frame.py lab/leak.py

# 4 - the http parts
touch lab/http_shape.py

# 5 - the parked transport, and the failure lab
touch lab/legacy_sse.py lab/noisy_stdout.py lab/missing_command.py
cd -

# 6 - the package you are about to write (the learner types every line)
mkdir -p sutra/mcp
touch sutra/mcp/__init__.py sutra/mcp/client.py

# 7 - the freshness gate, before anything else
curl -sL https://modelcontextprotocol.io/specification/versioning | grep -o "specification/2026-07-28" | head -1
```

**Step 7 is the gate and it is the same one Day 32 ran.** Everything in this day is written against
revision **2026-07-28**. If that page names a newer current revision, stop and amend the plan before
writing code (Principle 14). It printed `specification/2026-07-28` on 2026-09-04.

**`sutra/mcp/` is yours and it is shared.** You own `__init__.py` and `client.py`. Day 37 adds
`auth.py`, Day 40 adds `filtering.py` and Day 44 adds `hardening.py` to the same package. Keep
`__init__.py` empty or exporting only what you wrote; later days add modules, never a second package.

**Nothing goes into `sutra_mcp/` today.** It stays empty. Day 34 fills it.

---

## §4 Build brief

### The project code — `sutra/mcp/`, and you type every line

Two files, three public symbols. The parts give you every mechanism; the decisions are yours.

| File | Public symbols | What it must do |
| --- | --- | --- |
| `sutra/mcp/__init__.py` | — | Create the package. Keep it empty, or re-export the three names below. Days 37, 40 and 44 add modules beside `client.py`. |
| `sutra/mcp/client.py` | `connect_stdio`, `connect_http`, `list_tools` | Build a toolset for one server over one transport, and report what that server currently offers. |

- `connect_stdio(command, args, *, tool_filter=None, timeout=5.0) -> McpToolset` — a plain `def`, not
  a coroutine, because adk.dev requires the toolset to be constructible synchronously in `agent.py`
  (1.1). It connects to nothing; say so in the first line of the docstring (1.2), and say who must
  call `close()` (1.5).
- `connect_http(url, *, headers=None, tool_filter=None, timeout=5.0) -> McpToolset` — the same shape
  with a URL instead of a command line. Two functions rather than one with a flag, for the reason in
  4.1.
- `async def list_tools(toolset) -> list[str]` — names only, re-callable after anything underneath has
  been replaced (6.1).

**`TODO(me)` markers left for you:**

- **1.2** — decide where the preflight lives. Write `shutil.which` for the stdio command and something
  equivalent for a URL, then decide whether `connect_*` calls it, or whether it is a separate
  `preflight()` called from startup and the health check. Say which, in a comment, with the reason.
- **1.3** — choose the `tool_list_cache_ttl_seconds` Sutra's clients will use, and write down what has
  to happen *before* a tool is removed from a server given that number. Day 32's 3.3 `TODO(me)` picked
  the server-side `ttlMs`; these two numbers have to agree.
- **1.4** — write the startup assertion: the number of tools surviving `tool_filter` must equal the
  number of names in the filter, and a mismatch fails. Decide whether it raises or logs, and which
  day owns making it a test.
- **1.5** — decide whether `connect_stdio` and `connect_http` should return async context managers
  instead of bare toolsets, and write down what that would cost inside an ADK agent, which wants a
  plain object in `tools=[...]`.
- **2.4** — write Sutra's restart policy for a stdio server that dies: how many attempts, what backoff,
  and what it logs. Day 44 will formalise it; today decide the numbers and why.
- **3.4** — write the URL allowlist for `connect_http`: which schemes, which hosts, and whether
  redirects are followed. Decide what happens at startup when a configured URL is not on it.
- **4.1** — design the server record — name, transport, command or URL, allowed tools, TTL, who
  approved it — and decide where it lives. Days 40, 44 and 45 all read it.
- **6.2** — decide, in writing, what the agent does when one of several servers will not answer:
  degrade with the others' tools, or fail the turn. Then write the concurrent listing that implements
  your answer, keyed by server name.

### The lab — eight scripts, all of which run, none of which call a model

| File | What it does | Taught in |
| --- | --- | --- |
| `lab/fake_desk_server.py` | the far end: hand-written JSON-RPC over stdin and stdout, three tools, one of them destructive | 1.1, 2.1, 2.3 |
| `lab/list_tools.py` | `McpToolset` over stdio; `--filtered`, `--repeat`, `--ttl` | 1.1, 1.3, 1.4 |
| `lab/leak.py` | two toolsets, one closed and one not, in one process | 1.5, 6.2 |
| `lab/frame.py` | compact against pretty-printed: 1 message becomes 12 | 2.2 |
| `lab/http_shape.py` | a loopback MCP endpoint and a hand-written POST; `--bad-accept`, `--bad-origin`, `--get` | 3.1, 3.2, 3.4 |
| `lab/legacy_sse.py` | which transports the installed packages still export | 4.2 |
| `lab/noisy_stdout.py` | `--quiet`, `--line`, `--glued`: one newline decides the outcome | 5.1 |
| `lab/missing_command.py` | a command that is not on `PATH`; `--real` for the control | 1.2, 5.2 |

These are teaching material and they are given complete in the parts. Type them, run them, and break
them where the *Check yourself* sections ask you to.

---

## §5 The eval that must be able to fail

Four checks with exit codes, all on zero model calls.

**The client check** is the day's gate, and it is red until `sutra/mcp/client.py` exists:

```bash
uv run python -c "from sutra.mcp.client import connect_stdio, connect_http, list_tools; print('client ok')"; echo "exit: $?"
```

Before you write the file it is `ModuleNotFoundError: No module named 'sutra.mcp'` and `exit: 1`.
After, it prints `client ok` and `exit: 0`. That is the whole definition of done for the build brief,
and it can go red the moment somebody renames a function.

**The allowlist ablation** is the security check, and both arms must be run:

```bash
uv run python days/day-33-client-and-transports/lab/list_tools.py
uv run python days/day-33-client-and-transports/lab/list_tools.py --filtered
```

Measured on 2026-09-04: `['desk_ping', 'desk_ticket_count', 'desk_wipe_tickets']` against
`['desk_ping', 'desk_ticket_count']`. One argument of difference, and one tool that deletes every
ticket removed from the model's reach. Now change one letter in `READ_ONLY` and watch two names in
become one name out with no warning at all.

**The cache ablation** is the arithmetic:

```bash
uv run python days/day-33-client-and-transports/lab/list_tools.py --repeat 2>&1 | grep -c "tools/list"
uv run python days/day-33-client-and-transports/lab/list_tools.py --repeat --ttl 2>&1 | grep -c "tools/list"
```

Three against one, for identical output. Day 32's cacheable listings, as a constructor argument.

**The parked-transport check** is red today and is meant to be:

```bash
uv run python days/day-33-client-and-transports/lab/legacy_sse.py; echo "exit: $?"
```

Measured the same day: `legacy still importable : ['mcp.client.sse.sse_client',
'google.adk.tools.mcp_tool.SseConnectionParams']` and `exit: 1`. It is red because both libraries
still ship a transport with a removal clock and neither warns you at import. It goes green only when
they stop, which is not your decision to make.

**And the failure lab, where the exit codes are the point:**

```bash
uv run python days/day-33-client-and-transports/lab/noisy_stdout.py --quiet; echo "exit: $?"
uv run python days/day-33-client-and-transports/lab/noisy_stdout.py --line;  echo "exit: $?"
uv run python days/day-33-client-and-transports/lab/noisy_stdout.py --glued; echo "exit: $?"
uv run python days/day-33-client-and-transports/lab/missing_command.py --real; echo "exit: $?"
uv run python days/day-33-client-and-transports/lab/missing_command.py;        echo "exit: $?"
uv run python days/day-33-client-and-transports/lab/frame.py
uv run python days/day-33-client-and-transports/lab/leak.py
uv run python days/day-33-client-and-transports/lab/http_shape.py
uv run python days/day-33-client-and-transports/lab/http_shape.py --bad-accept
uv run python days/day-33-client-and-transports/lab/http_shape.py --bad-origin
uv run python days/day-33-client-and-transports/lab/http_shape.py --get
```

`--quiet` and `--line` both exit 0 and only one of them is correct; `--glued` exits 1 after a
timeout. That pair is the most important two lines in this day.

---

## §6 Request budget

**Free-tier Gemini**, 20 generate requests per day per model (`gemini-3.7-flash`, roster re-verified
2026-09-04).

| What | Generations |
| --- | --- |
| every part in every section | **0** |
| all eight lab scripts, every flag | **0** |
| the allowlist and cache ablations | **0** |
| `sutra/mcp/client.py` and its check | **0** |
| **Total planned** | **0 of 20** |

**Zero, and it is not an accident.** Everything this day teaches is observable without a model:
`tools/list` is a protocol call, an allowlist is a list comparison, and a framing bug is arithmetic on
a string. The only network traffic is one HTTPS GET to the specification site in §3 and three local
HTTP servers on `127.0.0.1`. Attaching the toolset to an agent and watching a model choose a tool is
worth doing once — it costs two or three generations and it teaches nothing this day has not already
shown you.

**Cost: $0.**

---

## §7 Traps

- **`McpToolset(...)` connects to nothing.** A missing command, a dead URL and a server that is not a
  server all construct perfectly and fail at the first `await get_tools()` (1.2, 5.2).
- **The exception is a `ConnectionError`, never a `FileNotFoundError`.** `except FileNotFoundError`
  around `get_tools()` catches nothing (5.2).
- **On Windows the missing-command error does not name the file.** `[WinError 2]` and nothing else;
  on Linux the same failure names it. Add `shutil.which` yourself (5.2).
- **A stdio child does not inherit your environment.** The SDK passes a small allowlist from
  `get_default_environment()`. `NOISY=1 uv run ...` never reaches the server; merge into that dict
  instead (2.1, 5.1).
- **`tool_filter=None` grants every tool the server ships, including ones it has not shipped yet**
  (1.4).
- **A `tool_filter` whose names no longer match produces an empty tool list and no error.** The agent
  simply answers from its own knowledge (1.4).
- **`tool_list_cache_ttl_seconds` is seconds; the protocol's `ttlMs` is milliseconds.** Two layers,
  two units, no warning (1.3).
- **The TTL is also how long you may keep advertising a tool you deleted.** ADK does not subscribe to
  `notifications/tools/list_changed` (1.3).
- **Four names are reserved by ADK** — `adk_request_confirmation`, `adk_request_credential`,
  `adk_request_input`, `transfer_to_agent`. An MCP tool with one of those is dropped with a warning
  and no error (1.3).
- **A `print` to stdout in a stdio server is either a logged traceback you ignore or a destroyed
  reply, and the difference is a trailing newline** (2.2, 5.1).
- **Pretty-printed JSON is valid JSON and invalid framing.** `indent=2` turns one message into twelve
  (2.2).
- **A client must not treat a server's stderr as errors.** Healthy servers are noisy there; the spec
  says **SHOULD NOT** (2.3).
- **Both of a child's streams are pipes, so both are block-buffered.** Forget to flush and replies sit
  in a buffer while the client times out (2.3).
- **`Accept` MUST list both `application/json` and `text/event-stream`.** The server chooses the reply
  shape per request (3.1, 3.2).
- **`400` from an MCP endpoint does not mean "old server".** Modern servers use `400` for version
  mismatches and header validation. Read the body (3.1, 4.2).
- **GET and DELETE to the MCP endpoint are `405` in this revision.** The standalone SSE stream and
  sessions are gone (3.1).
- **A proxy that buffers deletes your streaming behaviour silently.** `X-Accel-Buffering: no` (3.2).
- **Cancellation is a message on stdio and a hang-up over HTTP**, and over HTTP
  `notifications/cancelled` is not sent at all (3.3).
- **`Origin` is validated only when present**, because non-browser clients do not send one — and it is
  compared as a whole string, never with `startswith` (3.4).
- **`0.0.0.0` and `127.0.0.1` differ by seven characters and by an entire threat model** (3.4).
- **`SseConnectionParams` sits in the same `__all__` as the two live transports with no deprecation
  warning** (4.2).
- **Forgetting `close()` is invisible in a script**, because the interpreter exiting cleans up for
  you. It is not invisible in a service (1.5).
- **Duplicate tool names across two servers do not error.** The model picks one. `tool_name_prefix`
  exists for this (6.2).

---

## §8 Verify before you code

Fetched or run on **2026-09-04**, the day this was written.

**The specification — the transports, read in full:**

- `https://modelcontextprotocol.io/specification/versioning` — the current revision is still
  **2026-07-28**. The freshness gate in §3 passes and no amendment is required.
- `https://modelcontextprotocol.io/specification/2026-07-28/basic/transports` — *"Protocol semantics
  are identical on every transport"*, the two standard bindings, the per-binding cancellation rule,
  and the custom-transport requirements. This is 4.1's whole argument.
- `https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/stdio` — the launch, the
  framing MUSTs, the stdout/stderr rules, the three-step shutdown, the unexpected-termination rule,
  and the `server/discover` era probe. Sections 2.1 to 2.4 came from this page.
- `https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http` — the
  single MCP endpoint, the `Accept` MUST, the two reply shapes, cancellation by closing the stream,
  the `Origin`/localhost/auth rules, the backward-compatibility procedure, and the HTTP+SSE
  deprecation warning naming SEP-2596. Sections 3.1 to 3.4 and 4.2 came from this page.
- `https://modelcontextprotocol.io/specification/2026-07-28/deprecated` — the registry. HTTP+SSE:
  deprecated in `2025-03-26`, migration path Streamable HTTP, earliest removal *"Three months after
  SEP-2596 reaches Final"* — the shortest clock on the page, against *"First revision released on or
  after 2027-07-28"* for Roots, Sampling, Logging and Dynamic Client Registration.

**The ADK — the page, and then the installed source:**

- `https://adk.dev/tools-custom/mcp-tools/` — the import lines
  (`from google.adk.tools.mcp_tool import McpToolset`,
  `from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams`,
  `from mcp import StdioServerParameters`), the `StdioConnectionParams` and
  `StreamableHTTPConnectionParams` examples, `tool_filter` as *"a specific subset of tools"*, and the
  deployment constraint: *"the agent and its McpToolset must be defined **synchronously** in your
  `agent.py` file"*.
- `https://adk.dev/mcp/` — read, and it says only that *"An ADK agent can act as an MCP client and use
  tools provided by external MCP servers"* before deferring to the page above. Noted rather than
  cited.
- `.venv/Lib/site-packages/google/adk/tools/mcp_tool/__init__.py` — exports `McpToolset`/`MCPToolset`,
  `McpTool`/`MCPTool`, `StdioConnectionParams`, `StreamableHTTPConnectionParams`,
  `SseConnectionParams`, `to_mcp_server`, `adk_to_mcp_tool_type`, `gemini_to_json_schema`, inside a
  `try/except ImportError` that logs *"MCP Tool is not installed"* at **debug** level — which is below
  the default, so the message exists and nobody sees it (1.1).
- `.venv/Lib/site-packages/google/adk/tools/mcp_tool/mcp_toolset.py` — the keyword-only constructor
  and every argument used today: `tool_filter`, `tool_name_prefix`, `tool_list_cache_ttl_seconds`,
  `errlog`, `header_provider`, `progress_callback`. The only two `ValueError`s it can raise. The
  five-step `get_tools()`, the reserved-name skip, the sort-by-name comment, and the `close()`
  docstring quoted in 1.5.
- `.venv/Lib/site-packages/google/adk/tools/mcp_tool/mcp_tool.py` — `_RESERVED_TOOL_NAMES` resolves to
  `['adk_request_confirmation', 'adk_request_credential', 'adk_request_input', 'transfer_to_agent']`,
  read by running it rather than by reading the constants it is built from.
- `.venv/Lib/site-packages/google/adk/tools/mcp_tool/mcp_session_manager.py` — `StdioConnectionParams`
  (`server_params`, `timeout=5.0`), `StreamableHTTPConnectionParams` (`url`, `headers`, `timeout=5.0`,
  `sse_read_timeout=60*5.0`, `terminate_on_close=True`), `SseConnectionParams`, and the
  `retry_on_errors` decorator that *"will automatically retry the action once"*.

**The MCP SDK — the wire, read rather than assumed:**

- `.venv/Lib/site-packages/mcp/client/stdio/__init__.py` — `StdioServerParameters`
  (`command`, `args`, `env`, `cwd`, `encoding`), `get_default_environment()` and its per-platform
  allowlist, the `stdout_reader` buffer-and-split loop quoted in 2.2, the `stdin_writer`, and the
  shutdown `finally` with `PROCESS_TERMINATION_TIMEOUT = 2.0`.
- `.venv/Lib/site-packages/mcp/shared/session.py` — the receive loop's
  `if isinstance(message, Exception)` branch, which is why a stray line is logged and survived rather
  than fatal (2.2, 5.1).
- `.venv/Lib/site-packages/mcp/client/streamable_http.py` — `streamable_http_client` is the current
  name and `streamablehttp_client` is marked `@deprecated("Use streamable_http_client instead.")`.
- `.venv/Lib/site-packages/mcp/client/sse.py` — `sse_client` still present, no deprecation decorator,
  no warning at import (4.2).

**The SDK-era gap, restated because it bounds what today proves.** `mcp==1.29.1` reports
`LATEST_PROTOCOL_VERSION = "2025-11-25"` and
`SUPPORTED_PROTOCOL_VERSIONS = ["2024-11-05", "2025-03-26", "2025-06-18", "2025-11-25"]`, and
`InitializeRequest` is still exported. So the client you build today performs an `initialize`
handshake on the wire, and `lab/fake_desk_server.py` answers one — which is why it declares
`PROTOCOL_VERSION = "2025-11-25"` rather than `2026-07-28`. Everything section 3 teaches about
Streamable HTTP is verified against the specification and demonstrated with a hand-written client in
`lab/http_shape.py`; it is **not** demonstrated through the pinned SDK, because the pinned SDK cannot
speak that revision. Day 32 §8 recorded that PyPI's `mcp` is at `2.1.1` and does speak `2026-07-28`.
Nothing is bumped here: a day pins only what it installs, and this one installs nothing.

**Two live lookups, re-run today:**

```bash
curl -s https://pypi.org/pypi/mcp/json | uv run python -c "import sys,json;print(json.load(sys.stdin)['info']['version'])"
uv run python days/day-33-client-and-transports/lab/legacy_sse.py
```

**No paper was verified today.** Both identifiers cited — `doi:10.1145/2080.357392` and
`doi:10.1145/514183.514185` — already have dated rows in `docs/PAPERS.md` and are taught on Days 15
and 32. Neither is re-taught here; both are addresses.

---

## §9 Say it in an interview

"Our agent's tools were Python functions in the same process, so nothing outside could offer it data.
Phase 5 moved that boundary onto MCP, and this was the day the client side became real code.

The shape that surprised me is that ADK packages the MCP client as a *toolset* — the same abstraction
we already used for a generated OpenAPI client. One object in the agent's tool list, and from the
agent's point of view an MCP tool is indistinguishable from a local function. That is the value and it
is also the risk: a local function cannot time out, cannot have its process die, and cannot rename
itself between two runs.

The thing I would want to be asked about is what happens before the model sees anything. `get_tools()`
is five steps — connect, `tools/list`, wrap each entry as a framework tool, filter, sort — and two of
those can make a tool invisible with no error anywhere. The sort is not tidiness: the framework's own
comment says a server's listing order is not contractual and an unstable order would invalidate the
prompt cache every turn. And the filter is the smallest security decision in the whole phase. The
server we connect to advertises a tool that deletes every ticket with no undo, and its description
says so, in the model's context, on every turn. One constructor argument removes it. The reason it has
to be the tool list and not the instruction is that an instruction is a request competing with
whatever text arrives from a customer, and a tool list is a grant.

On transports: two live ones, and the spec is explicit that protocol semantics are identical on every
binding, so the choice is operational. stdio launches the server as a child process and pipes
newline-delimited JSON-RPC — no port, no TLS, no auth, because it has our own authority — and it is
unbeatable as a development loop. Streamable HTTP posts each message to one URL, and the moment you do
that the server has an address, which means `Origin` validation, a bind interface and authentication.
I would call that a blast-radius change rather than a config change, and it happens by editing one
class name. The old HTTP+SSE transport with the held GET stream has been deprecated since the
2025-03-26 revision and has the shortest removal clock in the spec's registry; both our libraries
still export it with no warning at import, so we turned that into a check that runs and exits non-zero.

The most useful thing we found was in the failure lab. A `print` to stdout in a stdio server breaks the
protocol in two different ways depending on whether the text ends with a newline. With one, the client
logs a parse error and the real reply is the next line, so the call succeeds — you get a traceback
followed by the right answer, and everybody reads the answer. Without one, the log text glues onto the
front of the reply, the reply is destroyed, and the client times out and reports a `ConnectionError`
with an empty reason, so you debug it as a network problem. The dangerous case is the one that works,
because it survives every test you have and becomes the fatal case the first time two writes interleave
under load."

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked and `./m depth 33` is green. Defined by
understanding and green checks, never by elapsed time — a part is finished when you could explain it
to someone else without the page open.

**Phase 5's gate** is `sutra-mcp` serving tools statelessly, on Day 38. Today closes the client half:
Sutra can connect out over either live transport, list what a server offers, decide what the model is
allowed to see, and recognise the transport it must not build on. Day 34 writes the server this client
will be pointed at, and the `TODO(me)` items about the cache TTL and the server record are the
decisions that day needs already made.

---

## §11 Ledger & commit

**`docs/PROGRESS.md`** — append:

```text
| 33 | <date> | MCP-02, MCP-03 | 19 | <hash> | ✅ |
```

**`docs/PACKAGES.md`** — **no new rows.** Nothing was installed and nothing upgraded: `mcp` stays at
`1.29.1`, `google-adk` at `2.7.1`, and `gemini-3.7-flash` stays pinned as recorded on 2026-08-26. The
SDK-era gap in §8 is a plan decision with its own amendment, not a row on a day that installs nothing.

**`docs/PAPERS.md`** — **no new rows.** `doi:10.1145/2080.357392` and `doi:10.1145/514183.514185`
already have dated rows and are taught on Days 15 and 32; this day cites both as addresses and teaches
neither.

**`docs/SKILL_PROVENANCE.md`** — no new rows. No skill was added or changed.

**The commit:**

```text
day 33: the client side - Sutra plugs into its first MCP server - closes MCP-02, MCP-03
```
