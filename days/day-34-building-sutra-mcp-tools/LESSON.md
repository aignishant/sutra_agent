---
day: 34
phase: 5
phase_name: "MCP I: the protocol"
title: "Building `sutra-mcp` I — tools over the wire"
ids: ["MCP-04", "MCP-05", "MCP-06"]
principles: [1, 2, 4, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18]
kind: lab
plan_version: "v2.2.1"
parts: 19
generated: "2026-09-04"
status: written
lab_scaffolded: true
commit: ""
---

# Day 34 — Building `sutra-mcp` I: tools over the wire

> **Yesterday (Day 33):** the client side. `sutra/mcp/client.py` got `connect_stdio`, `connect_http`
> and `list_tools`, and a tool living in another process was listed by name for zero model calls.
> **Today:** the other end. `sutra_mcp/` stops being empty: `server.py` and `tools.py` put
> `lookup_ticket` and `search_kb` on the wire, and the interesting part is not that it works — it is
> everything the two functions now have to carry that they never needed as plain Python.
> **Tomorrow (Day 35):** the other two capabilities. Resources and prompts register into the same
> `build_server()` you design today.

---

## §1 Where we are

Sutra's two tools have been ordinary Python functions since Day 3. They read a dictionary, they
return a string, and they are correct. Nothing outside Sutra's own process has ever been able to call
one.

Think of a small business that has always worked by word of mouth. The work is good, the regulars
know exactly what it can do, and none of that is written down anywhere, because everyone who needs to
know is already in the room. The day it puts a board over the door and a printed sheet in the window,
none of the work changes — and suddenly everything that was understood has to be *stated*. What is on
offer. What it costs. What happens if it cannot be done. A stranger who has never spoken to anybody
here has to be able to read the sheet and get it right.

That is today. **Crossing the boundary does not change the work; it changes who may ask for it, and
therefore what has to be written down.** By tonight `sutra_mcp/server.py` and `sutra_mcp/tools.py`
exist and any MCP host on your machine can ask Sutra's ticket archive a question without importing a
line of Sutra's code.

Four things to know before you read a part.

**Today writes real project code and installs nothing.** `sutra_mcp/server.py` and
`sutra_mcp/tools.py` are yours to type. `mcp==1.29.1` is already pinned; `git diff pyproject.toml
uv.lock` must be empty when you finish.

**Six later days register into the file you design today.** Days 35, 36, 37, 39, 41, 42 and 43 each
add a module to `sutra_mcp/` and one line to `build_server()`. Section 1 fixes that shape, and it is
the one decision today that is expensive to change later.

**The two forms of one function differ in four ways, and each one is a part.** A return value became
a result object. An exception became a field. Python objects became JSON. And a new class of failure
appeared that has nothing to do with the work. Sections 2, 3 and 4 are those differences, and section
4 is Principle 10 at the protocol level: *the tool failed* and *the call failed* are two different
sentences and a client acts on them differently.

**And the server you build is honestly a revision behind.** Day 32 found that `mcp==1.29.1` tops out
at `2025-11-25` while the specification is at `2026-07-28`. Section 5 stops treating that as a
footnote: you send four raw requests to your own server and read what it actually answers —
`server/discover` refused, business refused before a handshake, `2025-11-25` negotiated. Then you
write every line so the day the pin moves is a dependency bump rather than a rewrite.

---

## §2 The map

Nineteen parts in six sections, no paper part — two are cited as addresses to papers taught earlier.
This is a protocol day, so the sections are **lifecycle stages** rather than one per ID: section 1 is
the server object, section 2 is a function becoming a declaration, section 3 is the two calls,
section 4 is the two kinds of failure, section 5 is the lifecycle itself, and section 6 is what
happens after it ships. The day climbs `foundation → working → production`.

### Section 1 — `01-the-server-object`: what you are building (MCP-04)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [Three things and no fourth](parts/01-the-server-object/1.1-three-things-and-no-fourth.md) | A name, a declaration, handlers — and nothing else | `foundation` |
| 1.2 | [A server you build, not one that runs](parts/01-the-server-object/1.2-a-server-you-build-not-one-that-runs.md) | Why `build_server()` returns and `run()` blocks | `foundation` |
| 1.3 | [The name is an identity](parts/01-the-server-object/1.3-the-name-is-an-identity.md) | Where the string goes, and what it does not prove | `working` |
| 1.4 | [The shape later days register into](parts/01-the-server-object/1.4-the-shape-later-days-register-into.md) | One cabinet, one drawer per day | `working` |

### Section 2 — `02-function-to-declaration`: a function becomes a declaration (MCP-04 · MCP-06)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [The decorator that writes your schema](parts/02-function-to-declaration/2.1-the-decorator-that-writes-your-schema.md) | Four things read off your function, four fields out | `working` |
| 2.2 | [The schema is all they get](parts/02-function-to-declaration/2.2-the-schema-is-all-they-get.md) | The declaration is the entire user manual | `working` |
| 2.3 | [💥 The argument that changed on the way in](parts/02-function-to-declaration/2.3-the-argument-that-changed-on-the-way-in.md) | `'04521'` in, `4521` out, no error | `production` |
| 2.4 | [What the caller can no longer assume](parts/02-function-to-declaration/2.4-what-the-caller-can-no-longer-assume.md) | Four things that change, and the body is not one | `working` |

### Section 3 — `03-the-two-calls`: `tools/list` and `tools/call` (MCP-06)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [The list, and who may keep it](parts/03-the-two-calls/3.1-the-list-and-who-may-keep-it.md) | `ttlMs`, `cacheScope`, and one key against three | `working` |
| 3.2 | [The same order every time](parts/03-the-two-calls/3.2-the-same-order-every-time.md) | Two caches a shuffled list damages | `working` |
| 3.3 | [One call, one result](parts/03-the-two-calls/3.3-one-call-one-result.md) | Content, structured content, and the same text twice | `working` |

### Section 4 — `04-two-kinds-of-no`: the tool failed, or the call failed (MCP-06)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [The tool said no](parts/04-two-kinds-of-no/4.1-the-tool-said-no.md) | `isError: true`, written for the model | `working` |
| 4.2 | [The call never happened](parts/04-two-kinds-of-no/4.2-the-call-never-happened.md) | A JSON-RPC error, and where the SDK diverges | `working` |
| 4.3 | [💥 The message that escaped](parts/04-two-kinds-of-no/4.3-the-message-that-escaped.md) | A DSN in a text block, and the guard that moves it | `production` |

### Section 5 — `05-lifecycle`: the handshake, and its absence (MCP-05)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [The handshake that is now history](parts/05-lifecycle/5.1-the-handshake-that-is-now-history.md) | Three states a server used to hold | `foundation` |
| 5.2 | [What your server actually answers](parts/05-lifecycle/5.2-what-your-server-actually-answers.md) | Four probes, four findings, one honest verdict | `working` |
| 5.3 | [Building for the revision you are not on](parts/05-lifecycle/5.3-building-for-the-revision-you-are-not-on.md) | Six rows that need no newer library | `production` |

### Section 6 — `06-in-production`: after it ships

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 6.1 | [💥 The tool you deleted is still being called](parts/06-in-production/6.1-the-tool-you-deleted-is-still-called.md) | Removing a tool is two deployments | `production` |
| 6.2 | [Red before you ship it](parts/06-in-production/6.2-red-before-you-ship-it.md) | Six statements and an exit code | `production` |

**No paper part today.** Two parts carry §6 *The paper behind it* as an address to a paper taught
earlier: [2.4](parts/02-function-to-declaration/2.4-what-the-caller-can-no-longer-assume.md) cites
*Implementing remote procedure calls* (`doi:10.1145/2080.357392`, taught on Day 15) and
[4.1](parts/04-two-kinds-of-no/4.1-the-tool-said-no.md) cites *End-to-end arguments in system design*
(`doi:10.1145/357401.357402`, taught on Day 21). A paper is taught once in the whole curriculum;
every later day links to it.

**Read the sections in order.** Section 2 needs section 1's server object, sections 3 and 4 need
section 2's declaration, and section 5's probes only mean something once you know what the four
probes are asking for.

---

## §3 Setup — run this

**No package is added today, and no package is upgraded.** `mcp` stays at `1.29.1` and
`google-adk` at `2.7.1`. `git diff pyproject.toml uv.lock` must be empty when you finish. Day 32 §8
and Day 33 §8 both recorded that PyPI's `mcp` is at `2.1.1` and speaks `2026-07-28` while this
repository is pinned a revision behind; §8 below says exactly what that costs today, and the bump is
still a plan decision rather than a day's decision (Principle 14).

```bash
# 1 - the day's lab
cd days/day-34-building-sutra-mcp-tools
mkdir -p lab

# 2 - the server itself, and the three ways to look at it
touch lab/serve.py lab/schema.py lab/drive.py lab/wire.py

# 3 - section 2: the declaration and what it lets through
touch lab/coerce.py lab/both.py

# 4 - section 3: the list, its order, its cache hints
touch lab/order.py lab/cacheable.py

# 5 - section 4 and section 6: the failures
touch lab/escape.py lab/stale.py

# 6 - the day's gate
touch lab/gate.py
cd -

# 7 - the package you are about to fill (you type every line)
touch sutra_mcp/server.py sutra_mcp/tools.py

# 8 - the freshness gate, before anything else
curl -sL https://modelcontextprotocol.io/specification/versioning | grep -o "specification/2026-07-28" | head -1
```

**Step 8 is the gate and it is the same one Days 32 and 33 ran.** Everything in this day is written
against revision **2026-07-28**. If that page names a newer current revision, stop and amend the plan
before writing code (Principle 14). It printed `specification/2026-07-28` on 2026-09-04.

**`sutra_mcp/` is yours and it is shared.** You own `__init__.py`, `server.py` and `tools.py`. Day 35
adds `resources.py` and `prompts.py`, Day 36 adds `tasks.py`, Day 37 adds `auth.py`, Day 39 adds
`db_tools.py`, Day 41 adds `capabilities.py`, Day 42 adds `agent_server.py` and Day 43 adds `app.py`.
Every one of those is a module beside yours and a line inside `build_server()`, never a second
server. [1.4](parts/01-the-server-object/1.4-the-shape-later-days-register-into.md) is the argument.

**`sutra/mcp/` is untouched today.** That is Day 33's client package. The lab drives your server with
a throwaway client in `lab/drive.py`, because the client is not what is being taught.

---

## §4 Build brief

### The project code — `sutra_mcp/`, and you type every line

Two files, three public symbols. The parts give you every mechanism; the decisions are yours.

| File | Public symbols | What it must do |
| --- | --- | --- |
| `sutra_mcp/server.py` | `build_server`, `SERVER_NAME` | Construct the `FastMCP` object, call the registrations, return it. Never start it. |
| `sutra_mcp/tools.py` | `register_tools` | Declare `lookup_ticket` and `search_kb` on a server it is handed. |

- `build_server() -> FastMCP` — no arguments, returns the configured object, blocks on nothing
  (1.2). Name it `"sutra-mcp"` from a module constant (1.3). Pass `stateless_http=True` with a
  comment saying which transport that affects (5.3). Put the `run()` call under
  `if __name__ == "__main__":` and nowhere else.
- `register_tools(server: FastMCP) -> None` — takes a server, attaches tools, returns nothing (1.4).
  Days 35 onward add `register_resources` and `register_prompts` beside it with the same signature.
- **Import the implementations, do not retype them.** `lookup_ticket` and `search_kb` already exist
  in `sutra/loop.py` and have since Day 3. One implementation, two doors (2.4). Two copies of
  `search_kb` that drift apart is a support desk that answers differently depending on which agent
  asked.

**`TODO(me)` markers left for you:**

- **1.3** — decide what `serverInfo.version` should report, given that `FastMCP` in `mcp==1.29.1`
  has no constructor argument for it and defaults to the **library's** version. Reach through
  `server._mcp_server.version`, pin Sutra's own version somewhere, or accept the wrong number — and
  write down which and why, because Day 45's audit will read that field.
- **1.4** — decide whether `sutra_mcp/__init__.py` stays empty or re-exports `build_server`, and say
  what that buys the six later days that import from this package.
- **2.1** — decide where each tool's `description` comes from: the docstring, or an explicit
  `description=` argument fed from `sutra/tools.py`, which already holds the model-facing text you
  wrote on Day 4. Then say what has to happen so the two never drift.
- **2.2** — rewrite `search_kb`'s description so that a caller who has never seen the code sends a
  query that works. It must state the matching rule and give one example of a query that misses.
- **2.3** — write the body-level type check for `lookup_ticket` and decide whether it returns a
  sentence or raises. Then decide what `ticket_id`'s type must be if the archive ever holds an id
  with a leading zero.
- **3.1** — choose `sutra_mcp`'s `ttlMs` and `cacheScope`. Day 32's 3.3 asked for the first and Day
  33's 1.3 asked for the client's matching number, in a different unit. Write both down together, and
  write down what must be true before a tool is deleted.
- **3.2** — decide where the sort lives, and write the test that asserts the exact tool list in
  order. Say what should happen to that test when Day 35 adds a tool.
- **4.1** — classify every failure your two tools can have into *fact*, *retryable* and *permanent*,
  and write the message each one returns. The messages are read by a model, not by you.
- **4.3** — write `FORBIDDEN` for Sutra: the tokens that must never appear in a tool error message.
  Then decide which day owns turning `is_safe` into a test over every tool's failure path.
- **5.3** — write the assertion Day 32's 5.1 asked for: the installed SDK supports the revision Sutra
  targets. It is red. Decide, in writing, what it should say when it goes red and why neither
  lowering the target nor deleting it is allowed.
- **6.2** — extend `lab/gate.py` with one check it does not make today, and say why you chose that one
  over the other candidates.

### The lab — eleven scripts, all of which run, none of which call a model

| File | What it does | Taught in |
| --- | --- | --- |
| `lab/serve.py` | the lab twin of `sutra_mcp/server.py` + `tools.py`, standing alone | 1.1, 1.2, 1.4 |
| `lab/schema.py` | both tool declarations exactly as `tools/list` carries them | 2.1, 2.2 |
| `lab/coerce.py` | two tools, one type hint apart; `'04521'` in, `4521` out | 2.3 |
| `lab/both.py` | the same function in-process and over MCP, four arguments each | 2.4 |
| `lab/cacheable.py` | what the pinned SDK sends against what 2026-07-28 requires | 3.1 |
| `lab/order.py` | registration order against sorted order | 3.2 |
| `lab/drive.py` | a throwaway client: four calls, one of each outcome | 3.3, 4.1, 4.2 |
| `lab/escape.py` | three ordinary failures, unguarded and guarded | 4.3 |
| `lab/wire.py` | four raw JSON-RPC probes, one fresh server each | 1.3, 5.1, 5.2 |
| `lab/stale.py` | a removed tool, in one deployment and in two | 6.1 |
| `lab/gate.py` | the day's six assertions, as an exit code | 6.2 |

These are teaching material and they are given complete in the parts. Type them, run them, and break
them where the *Check yourself* sections ask you to.

---

## §5 The eval that must be able to fail

Four checks with exit codes, all on zero model calls.

**The gate** is the day's definition of done, and it is red until you have written the package:

```bash
uv run python days/day-34-building-sutra-mcp-tools/lab/gate.py; echo "exit: $?"
```

Measured on 2026-09-04, before anything was written:
`- sutra_mcp.server.build_server is not importable: ModuleNotFoundError: No module named
'sutra_mcp.server'`, `findings: 1`, `exit: 1`. When it prints `findings: 0` and `exit: 0`, six
statements are true of `sutra_mcp/`. Then break exactly one of them on purpose — swap the two
registration lines and watch `tools/list is ['search_kb', 'lookup_ticket'], not ['lookup_ticket',
'search_kb'] in that order`.

**The retirement ablation** is the production check, and both arms must be run:

```bash
uv run python days/day-34-building-sutra-mcp-tools/lab/stale.py --one-deploy
uv run python days/day-34-building-sutra-mcp-tools/lab/stale.py --two-deploys
```

`isError : True` with `Unknown tool: close_ticket` against `isError : False` with a sentence telling
the model the tool is retired and not to retry. Same removal, same cached list, two very different
hours for the person on the other end.

**The leak ablation** is the security check, and both arms must be run:

```bash
uv run python days/day-34-building-sutra-mcp-tools/lab/escape.py
uv run python days/day-34-building-sutra-mcp-tools/lab/escape.py --guarded
uv run python days/day-34-building-sutra-mcp-tools/lab/escape.py --guarded 2>&1 1>/dev/null | head -8
```

The unguarded arm hands the caller a filesystem path and a full connection string. The guarded arm
hands it an exception class name and an instruction, and the third command shows the operator getting
*more* than before — a whole traceback on stderr. Nothing about this can be detected by a test that
only checks `isError`.

**And the rest, each of which can be broken on purpose:**

```bash
uv run python days/day-34-building-sutra-mcp-tools/lab/schema.py
uv run python days/day-34-building-sutra-mcp-tools/lab/coerce.py
uv run python days/day-34-building-sutra-mcp-tools/lab/both.py
uv run python days/day-34-building-sutra-mcp-tools/lab/cacheable.py
uv run python days/day-34-building-sutra-mcp-tools/lab/order.py
uv run python days/day-34-building-sutra-mcp-tools/lab/drive.py
uv run python days/day-34-building-sutra-mcp-tools/lab/wire.py
```

Three of those have a named break in their own part: change `wants_integer`'s hint to `str` in
`coerce.py` and watch which rows flip; set `CACHE_SCOPE` to `"private"` in `cacheable.py` and say
which caller that protects; delete a docstring in `serve.py` and watch `schema.py` print an empty
description with no complaint from anything.

---

## §6 Request budget

**Free-tier Gemini**, 20 generate requests per day per model (`gemini-3.7-flash`, roster re-verified
2026-09-04).

| What | Generations |
| --- | --- |
| every part in every section | **0** |
| all eleven lab scripts, every flag | **0** |
| the retirement and leak ablations | **0** |
| `sutra_mcp/server.py`, `sutra_mcp/tools.py` and the gate | **0** |
| **Total planned** | **0 of 20** |

**Zero, and it is not an accident.** A server does not need a model to be a server. Everything today
teaches is observable by asking the server questions: a schema is a JSON object, a tool call is a
request and a reply, coercion is a type name printed from inside a function, and a leaked connection
string is a substring. The only network traffic is one HTTPS GET to the specification site in §3;
every other process runs on your own machine and most of them do not even open a socket. Attaching
the server to an agent and watching a model choose `lookup_ticket` is worth doing once, costs two or
three generations, and teaches nothing this day has not already shown you.

**Cost: $0.**

---

## §7 Traps

- **`@server.tool` without parentheses** raises *"The @tool decorator was used incorrectly"*. The SDK
  is kind here; most decorator factories are not (2.1).
- **A missing docstring is an empty description, not an error.** `""`, not `None`, so a check written
  against `None` passes (2.1, 6.2).
- **The whole docstring goes on the wire** — the `Args:` block, the blank lines and the indentation —
  and into the model's context on every turn (2.1, 2.2).
- **Renaming a parameter is a breaking change**, because the parameter name is in `inputSchema` (2.1).
- **A `str` return produces an `outputSchema` that boxes it as `{"result": ...}`**, and the same text
  then comes back twice, once in `content` and once in `structuredContent` (2.1, 3.3).
- **A JSON string sent to an `int` parameter is coerced, not refused**, so `'04521'` arrives as
  `4521` with no error on either side. Identifiers are `str`, always (2.3).
- **`FastMCP` disables the low-level server's input validation** and converts before it validates. The
  schema you publish is not the thing that runs (2.3).
- **`ttlMs` is milliseconds.** `3600` is three and a half seconds and nothing will tell you (3.1).
- **`cacheScope: "public"` on a list that varies by caller** lets a shared proxy serve one caller's
  tool list to another. It is a security field wearing a performance field's clothes (3.1).
- **`tools/list` comes back in registration order**, which is the order of lines in `build_server()`,
  which a formatter is allowed to change. Sort it (3.2).
- **`result.content[0].text` assumes a non-empty list whose first block is text.** True today, not
  guaranteed (3.3).
- **A tool error is a successful call.** Nothing is raised, so `try/except` around `call_tool` catches
  none of it (2.4, 4.1).
- **A missing record is not an error.** `isError: true` for a miss teaches the model to retry the same
  absent id (4.1).
- **A broad `except` that turns an unreachable database into "not found"** tells a customer we have no
  record of them, with no error anywhere (4.1).
- **Every exception's `str()` becomes caller-facing text**, so a `FileNotFoundError` leaks a path and
  a `ConnectionError` can leak a DSN with its password (4.3).
- **The SDK reports an unknown tool as `isError: true`, not as a JSON-RPC error**, so a client cannot
  detect a stale tool list by branching on `isError` (4.2, 6.1).
- **`server/discover` is a MUST for a server and `mcp==1.29.1` does not implement it.** Not fixable at
  your layer (5.2).
- **A `-32602` reply can mean "before initialization" and say "invalid request parameters".** The real
  sentence is on the server's stderr, where the caller cannot see it (5.1, 5.2).
- **`stateless_http=True` does nothing on stdio.** `run_stdio_async` passes no `stateless` argument,
  and even on HTTP the handshake still happens — it just stops pinning you to an instance (5.3).
- **A module-level dict a handler writes to is a session**, and it works perfectly until there are
  two instances (5.3).
- **Removing a tool in one deployment ships errors for a whole TTL**, and adding a required parameter
  is a removal in disguise (6.1).
- **A `print` at import time in a stdio server** either produces a parse error the client survives or
  destroys a reply, depending on a trailing newline — Day 33's
  [5.1](../day-33-client-and-transports/parts/05-failure-lab/5.1-the-log-line-that-ate-the-reply.md)
  is the anatomy, and `lab/gate.py` is the check that catches it before launch (6.2).

---

## §8 Verify before you code

Fetched or run on **2026-09-04**, the day this was written.

**The specification — the freshness gate and the three pages this day is built on:**

- `https://modelcontextprotocol.io/specification/versioning` — *"The **current** protocol version is
  [**2026-07-28**]"*. It has not moved; the gate in §3 passes and no amendment is required. This page
  also states the negotiation model that replaced the handshake and points at the backward-
  compatibility rules for `2025-11-25` and earlier.
- `https://modelcontextprotocol.io/specification/2026-07-28/server/tools` — everything in sections 2,
  3 and 4: the `tools/list` and `tools/call` shapes, the deterministic-order **SHOULD** and its two
  stated reasons, the *"MUST NOT vary per-connection"* rule and its authorization exemption, the
  `Tool` fields, the tool-name rules, `x-mcp-header`, the content block types, `structuredContent`,
  the output-schema **MUST**, the *Stateful Tools* handle guidance, and the two error mechanisms with
  the `-32602` *"Unknown tool"* example and the `isError: true` example.
- `https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/caching` — the whole of
  3.1: which results **MUST** carry hints, `ttlMs` semantics and the absent/zero/negative rules,
  the `cacheScope` table, how to choose between the two values, the interaction with `listChanged`
  notifications, pagination, and the security note that a `"public"` response may be shared between
  callers even from an authenticated endpoint.
- `https://modelcontextprotocol.io/specification/2026-07-28/basic/index` — the statelessness
  paragraph quoted in 1.1 and 5.3, the required `_meta` keys and the `-32602` rule for a request
  missing them, the `resultType` rules, and the error-code partition (`-32000`–`-32019` legacy,
  `-32020`–`-32099` reserved, `-32020`/`-32021`/`-32022` defined).

**The installed SDK — the authoritative API surface, read rather than guessed:**

- `.venv/Lib/site-packages/mcp/server/fastmcp/__init__.py` — `__all__` is
  `["FastMCP", "Context", "Image", "Audio", "Icon"]`. `mcp/server/__init__.py` also exports the
  low-level `Server`, `NotificationOptions` and `InitializationOptions`.
- `.venv/Lib/site-packages/mcp/server/fastmcp/server.py` — the full `FastMCP.__init__` signature
  including `stateless_http: bool = False`; the fact that it constructs the low-level server with
  **no `version` argument** (1.3); `run(transport=..., mount_path=...)` and its
  *"Note this is a synchronous function"* docstring plus `anyio.run(self.run_stdio_async)` (1.2);
  `add_tool(...)` and `tool(...)` signatures with `structured_output` *"auto-detects based on the
  function's return type annotation"* (2.1, 3.2); `remove_tool`; `run_stdio_async`, which passes no
  `stateless` (5.3); and `self._mcp_server.call_tool(validate_input=False)` with the comment
  *"FastMCP does ad hoc conversion of incoming data before validating"* (2.3).
- `.venv/Lib/site-packages/mcp/server/lowlevel/server.py` — `_make_error_result` (4.1); the
  `except Exception as e: return self._make_error_result(str(e))` branch that catches both tool
  failures and unknown tools (4.2); the output-schema validation block (3.3);
  `server_version=self.version if self.version else pkg_version("mcp")` (1.3); and the `run(...)`
  parameter comment on `stateless` quoted in 5.3.
- `.venv/Lib/site-packages/mcp/server/session.py` — `InitializationState` with its three members, the
  `_received_request` match statement including the ping exemption and
  `RuntimeError("Received request before initialization was complete")`, and
  `InitializationState.Initialized if stateless else InitializationState.NotInitialized` (5.1, 5.3).
- `.venv/Lib/site-packages/mcp/server/fastmcp/tools/base.py` —
  `raise ToolError(f"Error executing tool {self.name}: {e}") from e`, the line that makes every
  exception message caller-facing (4.1, 4.3).
- `.venv/Lib/site-packages/mcp/server/fastmcp/tools/tool_manager.py` —
  `raise ToolError(f"Unknown tool: {name}")` (4.2).
- `.venv/Lib/site-packages/mcp/server/streamable_http_manager.py` — `stateless` *"creates a
  completely fresh transport for each request with no session tracking"* (5.3).
- `.venv/Lib/site-packages/mcp/types.py` — `CallToolResult` fields, and
  `model_config = ConfigDict(extra="allow")`, which is why a hand-built `ListToolsResult` can carry
  `ttlMs` and `cacheScope` on this SDK (3.1).

**No ADK symbol is used anywhere in this day.** Day 33 owns the client and its `McpToolset`; today is
entirely server-side and the only library imported is `mcp`. `https://adk.dev/mcp/` was read and says
only that an ADK agent can act as an MCP client, deferring to the page Day 33 already cited. Noted
rather than cited.

**Three live commands, re-run today:**

```bash
curl -sL https://modelcontextprotocol.io/specification/versioning | grep -o "specification/2026-07-28" | head -1
curl -s https://pypi.org/pypi/mcp/json | uv run python -c "import sys,json;print(json.load(sys.stdin)['info']['version'])"
uv run python -c "from mcp.shared.version import SUPPORTED_PROTOCOL_VERSIONS as v; from mcp.types import LATEST_PROTOCOL_VERSION as l; print(l, v)"
```

They printed `specification/2026-07-28`, then `2.1.1`, then
`2025-11-25 ['2024-11-05', '2025-03-26', '2025-06-18', '2025-11-25']`. **The gap Day 32 recorded is
still open and this day does not close it.** `SUPPORTED_PROTOCOL_VERSIONS` is importable only from
`mcp.shared.version`; `from mcp.types import SUPPORTED_PROTOCOL_VERSIONS` raises `AttributeError`.
Nothing is bumped: a day pins only what it installs, and this one installs nothing.

**What that gap costs, stated plainly** — because this is the day it stops being abstract. The server
you build does not implement `server/discover`, which the current revision makes a **MUST** for
servers. It requires the deleted `initialize` handshake before it will answer `tools/list` over stdio.
It sends no `resultType`, and no `ttlMs` or `cacheScope`, so a modern client treats its tool list as
immediately stale. Section 5 measures all four with raw requests rather than asserting them, and 5.3
is the list of the things that are already right anyway.

**No paper was verified today.** Both identifiers cited — `doi:10.1145/2080.357392` and
`doi:10.1145/357401.357402` — already have dated rows in `docs/PAPERS.md` and are taught on Days 15
and 21. Neither is re-taught here; both are addresses.

---

## §9 Say it in an interview

"Our agent's tools were Python functions in the same process. This was the day we put two of them on
the wire as an MCP server, and the interesting part was not that it worked — the body of the function
did not change at all — it was everything around it that had to.

Four things change when a function becomes a tool. The return value becomes a result object with
content blocks and a structured half. Exceptions stop propagating, because a stack does not cross a
process boundary, so a tool failure comes back as an ordinary reply with an `isError` flag. Arguments
become JSON. And a new class of failure appears that has nothing to do with the work — timeouts, a
dead process, a tool renamed between two calls. That is the 1984 RPC argument, and the practical
version is that a remote call has three outcomes rather than two, so read-only tools are safe to
retry and write tools have to be idempotent by design.

The distinction I would want to be asked about is the two kinds of failure. `isError: true` means the
tool ran and could not do the job, and the spec says clients *should* hand those to the model because
they enable self-correction — so the message is written for the model: name the field, state the
rule, give the value, say what a corrected call looks like. A JSON-RPC error replaces the result
entirely: nothing ran, and clients only *may* pass those on, because a model cannot usually fix a
malformed request by adjusting a parameter. The line I would defend is that a missing record is not an
error. Our ticket lookup returns 'no ticket with that id' with `isError` false, because the tool
answered the question, and returning an error there teaches the model to retry the same absent id.

The failure lab found the thing I would actually change in someone else's codebase. The SDK catches
every exception from a tool body and puts `str(exception)` into a text block that goes to the model
and into the transcript. We measured three ordinary failures: a `KeyError` handed the caller a bare
key, a `FileNotFoundError` handed it our directory layout, and a connection error handed it a full
DSN with the password in it. Every one of those calls was `isError: true`, which is correct, so
nothing anywhere raised an alarm. Now every tool body is wrapped: `log.exception` for the operator
with the whole traceback, and a re-raised error carrying the exception class name, a correlation
reference and an instruction. The operator ends up with more than before and the caller with less.

Two operational things I did not expect. Removing a tool is two deployments, because the tool list is
cacheable — the `ttlMs` you choose is also how long a client may keep calling something you deleted,
so the first deploy keeps the name and returns a retirement message and the second one removes it a
TTL later. And the tool list has to be sorted, because order is what a client's cache and the model
provider's prompt cache key on, and our SDK returns registration order, which is the order of lines in
a function that a formatter is allowed to change.

The honest part is the version. Our pinned SDK tops out at the revision before the one we are building
against, and rather than assert that from a changelog we sent four raw JSON-RPC requests to our own
server and read the replies. It refuses `server/discover`, which the current revision makes mandatory;
it refuses `tools/list` until the deleted handshake; it negotiates `2025-11-25`. None of that is
fixable at our layer. What is fixable is everything our own code decides — no server-side session
state, sorted lists, model-facing descriptions, correct `isError` use, scrubbed errors — and all of
those are already what the new revision wants. So the bump, when it comes, is a dependency change
rather than a rewrite."

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked and `./m depth 34` is green. Defined by
understanding and green checks, never by elapsed time — a part is finished when you could explain it
to someone else without the page open.

**Phase 5's gate** is `sutra-mcp` serving tools statelessly, on Day 38. Today builds the server half:
`sutra_mcp/` has a shape six later days register into, two tools are on the wire with declarations a
stranger can use, failure has two names and both are honest, and you can say what revision your server
actually speaks because you asked it. Day 35 adds resources and prompts to the same `build_server()`,
and the `TODO(me)` items about the `ttlMs`, the description source and the retirement procedure are
the decisions the rest of Phase 5 needs already made.

---

## §11 Ledger & commit

**`docs/PROGRESS.md`** — append:

```text
| 34 | <date> | MCP-04, MCP-05, MCP-06 | 19 | <hash> | ✅ |
```

**`docs/PACKAGES.md`** — **no new rows.** Nothing was installed and nothing upgraded: `mcp` stays at
`1.29.1`, `google-adk` at `2.7.1`, and `gemini-3.7-flash` stays pinned as recorded on 2026-08-26. The
SDK-era gap in §8 is measured here rather than fixed here; the bump is a plan amendment with its own
row, not a side effect of a day that installs nothing.

**`docs/PAPERS.md`** — **no new rows.** `doi:10.1145/2080.357392` and `doi:10.1145/357401.357402`
already have dated rows and are taught on Days 15 and 21; this day cites both as addresses and teaches
neither.

**`docs/SKILL_PROVENANCE.md`** — no new rows. No skill was added or changed.

**The commit:**

```text
day 34: building sutra-mcp I - tools over the wire - closes MCP-04, MCP-05, MCP-06
```
