---
day: 39
phase: 6
phase_name: "MCP II: production"
title: "Database tools — Toolbox versus hand-written"
ids: ["MCP-15", "ADK-25", "ADK-78"]
principles: [1, 2, 4, 7, 8, 9, 10, 11, 13, 15, 16, 17, 18]
kind: lab
plan_version: "v2.2.1"
parts: 20
generated: "2026-09-04"
status: written
lab_scaffolded: true
commit: ""
---

# Day 39 — Database tools: Toolbox versus hand-written

> **Yesterday (Day 38):** the failure and migration lab. You drove Sutra's client against a
> malformed server and a slow one, and met the three client features MCP formally deprecated —
> Roots, Sampling and Logging — and the multi-round-trip `InputRequiredResult` shape that replaces
> them. Phase 5 closed.
> **Today:** Phase 6 opens, and the archive stops being a Python dictionary. Sutra gets a real SQL
> store, hand-written database tools with five separate brakes on them, and an honest look at the
> first-party server that would have generated those tools for you.
> **Tomorrow (Day 40):** tool filtering and allowlists — the general machinery for deciding which
> tools an agent may hold, and the MCP security posture that goes with it.

---

## §1 Where we are

You gave the plumber a key so he could get in and fix the tap while you were at work.

He did fix the tap. He was recommended by a neighbour, he was there for less than an afternoon, and
he left the key under the mat as agreed. Nothing went wrong and nothing was ever going to.

But look at what you actually handed over. Not access to the bathroom — the key opens the front door,
and behind the front door is every room in the flat, the cupboard with the papers in it, and the
locker. It opens on the days you are at work and on the days you are not, and it will open next
month, because a key is not an appointment. The word "capability" is doing a lot of quiet work in
that sentence, and none of it was in the conversation you had, which was about a tap.

That is the shape of today. Sutra's ticket archive has been five entries in a Python dictionary since
Day 3, and today it becomes a real SQLite database — durable, shared, queryable, exactly what a
support desk needs. The moment it does, `sutra_mcp` grows a tool that reads it, and that tool is a
key you cut.

An agent with `SELECT` on a ticket archive is a research assistant. An agent with the same connection
and no brakes is an incident. So this is the sharpest day in the curriculum for Principle 13 — blast
radius before capability — and it is worth being precise about what "brakes" means, because the
industry's usual answer is a sentence in the tool description asking the model to behave.

**We measured what that sentence is worth.** A read-write connection, a tool whose description says
*"read only"*, and one `UPDATE`: **205 tickets closed, no error, success reported.** The description
was not ignored. It was never consulted, because a description is text sent to a model and the
`UPDATE` went to a database.

Then we built five real brakes and attacked each one on purpose. **All five held.** They are not five
spellings of one idea — read-only says nothing about a query returning the wrong rows, and a row
limit says nothing about a query that runs forever — and section 2 is one part per brake, each with
the attack it stops and the attack it does not.

Four things to know before you read a part.

**The injection you meet today does not delete anything.** It returns five rows where the filter said
two should be hidden, with `status: ok` and exit code zero. That is the ordinary shape of SQL
injection in an agent tool: not a dropped table, but a `WHERE` clause quietly ceasing to apply.

**A ceiling costs nothing and its absence costs everything.** Forty thousand matching tickets
serialise to about 1.7 million tokens — **173% of the model's entire input window**, so the request
cannot be sent. Two hundred rows is **0.9%**. The measurement is in section 5 and it is arithmetic,
not a model call.

**MCP Toolbox for Databases is 🅿️ parked, and it is parked after being looked at properly.** It is a
real, current, first-party server — version 1.9.0, about fifty databases — and section 4 quotes its
actual SQLite recipe, including a tool named `execute_sql` whose entire description is *"Use this
tool to execute SQL."* Sutra hand-writes instead, for three stated reasons and with a written trigger
for revisiting the decision.

**Today installs nothing.** `sqlite3` is in Python's standard library. `git diff pyproject.toml
uv.lock` must be empty when you finish, and `docs/PACKAGES.md` gains no rows.

---

## §2 The map

Twenty parts in six sections, plus **one paper**, read last. The day climbs
`foundation → working → production`: section 1 is the archive growing up, section 2 is one part per
brake, section 3 is the ADK surface, section 4 is the alternative you are not building, section 5 is
the failure lab and section 6 is the production face.

### Section 1 — `01-the-archive`: the dictionary becomes a database (MCP-15)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [The numbers on the back of a bill](parts/01-the-archive/1.1-the-numbers-on-the-back-of-a-bill.md) | Three properties a dict does not have, and a fourth difference that is not about storage | `foundation` |
| 1.2 | [One file, one engine](parts/01-the-archive/1.2-one-file-one-engine.md) | A whole SQL engine in the standard library, and no billing account | `foundation` |
| 1.3 | [A door, not a hallway](parts/01-the-archive/1.3-a-door-not-a-hallway.md) | `search_tickets(term, limit)` against `execute_sql(sql)` | `working` |

### Section 2 — `02-the-five-brakes`: blast radius before capability (MCP-15)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [💥 The argument that became syntax](parts/02-the-five-brakes/2.1-the-argument-that-became-syntax.md) | Five rows past a filter that said two were hidden | `working` |
| 2.2 | [The connection that cannot write](parts/02-the-five-brakes/2.2-the-connection-that-cannot-write.md) | `mode=ro`, and the refusal coming from the engine | `working` |
| 2.3 | [The statements you allow](parts/02-the-five-brakes/2.3-the-statements-you-allow.md) | An authorizer, and why `ATTACH` is a read | `working` |
| 2.4 | [A ceiling the caller cannot raise](parts/02-the-five-brakes/2.4-a-ceiling-the-caller-cannot-raise.md) | Clamp, bind, and ask for one row more than you return | `working` |
| 2.5 | [The query that never ends](parts/02-the-five-brakes/2.5-the-query-that-never-ends.md) | A budget on work, because `LIMIT` bounds the answer | `working` |
| 2.6 | [Which brakes actually held](parts/02-the-five-brakes/2.6-which-brakes-actually-held.md) | 5 held, and the sentence in the description held nothing | `production` |

### Section 3 — `03-the-adk-side`: how ADK sees a database tool (ADK-25)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [What the model is told](parts/03-the-adk-side/3.1-what-the-model-is-told.md) | The docstring goes across whole, and it is all there is | `working` |
| 3.2 | [A database server through McpToolset](parts/03-the-adk-side/3.2-a-database-server-through-mcptoolset.md) | A launch spec plus a filter, before anything runs | `working` |

### Section 4 — `04-toolbox-parked`: the server you are not building (ADK-25, ADK-78)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [🅿️ The server you did not write](parts/04-toolbox-parked/4.1-the-server-you-did-not-write.md) | Sources, tools, toolsets — and the real prebuilt recipe | `working` |
| 4.2 | [Who writes the SQL](parts/04-toolbox-parked/4.2-who-writes-the-sql.md) | Reviewed statement or unreviewed one — the decision, with its expiry | `production` |
| 4.3 | [🅿️ The extras map](parts/04-toolbox-parked/4.3-the-extras-map.md) | Twenty-three extras, read off the installed metadata | `production` |

### Section 5 — `05-failure-lab`: the deliberate failures

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [💥 Forty thousand rows](parts/05-failure-lab/5.1-forty-thousand-rows.md) | 173% of the window, from a query that did nothing wrong | `production` |
| 5.2 | [💥 The label that stayed](parts/05-failure-lab/5.2-the-label-that-stayed.md) | A description and a schema, drifting in two directions | `production` |
| 5.3 | [💥 The write with no undo](parts/05-failure-lab/5.3-the-write-with-no-undo.md) | 203 closed, 200 wanted, and no way to say which three | `production` |

### Section 6 — `06-in-production`: after it ships

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 6.1 | [The connection you do not hold](parts/06-in-production/6.1-the-connection-you-do-not-hold.md) | `database is locked`, reported by the wrong component | `production` |
| 6.2 | [When SQLite is not the database](parts/06-in-production/6.2-when-sqlite-is-not-the-database.md) | What survives Postgres, and the three brakes that improve | `production` |
| 6.3 | [The audit that reads your file](parts/06-in-production/6.3-the-audit-that-reads-your-file.md) | To check something is there, search; to check it is nowhere, parse | `production` |

### The paper — read it **after** the parts

| Paper | Identifier | What it argued |
| --- | --- | --- |
| [A Relational Model of Data for Large Shared Data Banks](papers/01-relational-model.md) | `doi:10.1145/362384.362685` (1970) | Ask about named relations, never about how the data is stored, so the storage can change underneath a working program |

Principle 4 at the scale of a day: write the queries by hand, watch a description drift away from a
schema, list what survives a change of engine — *then* read the argument that made all three
possible. Every claim in that paper has a part in this day that met it as a mechanism first:
declarative queries in [1.2](parts/01-the-archive/1.2-one-file-one-engine.md), the logical view in
[5.2](parts/05-failure-lab/5.2-the-label-that-stayed.md), and physical independence in
[6.2](parts/06-in-production/6.2-when-sqlite-is-not-the-database.md).

---

## §3 Setup — run this

**No package is added today, and none is upgraded.** `sqlite3` is in Python's standard library and
`docs/PACKAGES.md` gains no rows. `git diff pyproject.toml uv.lock` must print nothing when the day
ends.

```bash
# 1 - the day's lab
cd days/day-39-database-tools
mkdir -p lab/papers/relational-model

# 2 - section 1: the archive
touch lab/seed_lab.py

# 3 - section 2: the five brakes
touch lab/injection.py lab/brakes.py

# 4 - section 3: the ADK surface
touch lab/adk_tools.py lab/toolset_shape.py

# 5 - section 5: the failure lab
touch lab/flood.py lab/drift.py lab/undo.py

# 6 - section 6: production
touch lab/hold.py lab/brake_audit.py

# 7 - the paper demo
touch lab/papers/relational-model/layout.py
touch lab/papers/relational-model/answer.py
cd -

# 8 - where the real archive will live, and the check that git already ignores it
mkdir -p sutra/data
grep -n "sqlite3" .gitignore
```

**Step 8 is a check, not an edit.** `.gitignore` already carries `*.db` and `*.sqlite3` under the
heading *"runtime artifacts: never commit a session store"*, written on Day 0, so
`sutra/data/tickets.sqlite3` is ignored the moment it exists and **no new line is needed**. Confirm
it rather than assuming it, and add nothing if it is there.

The reason it matters is worth stating even though the work is already done. That file is
**generated** — rebuilt by `build_archive()` and never committed. A generated file in git drifts from
the script that generates it, and within a month nobody knows which is authoritative. And it is
Principle 9's neighbour: a database file is exactly the kind of artefact that accidentally acquires
real data, on a repository that goes public in Phase 14.

**Nothing else moves into `sutra/` today.** `sutra/loop.py` keeps its `TICKETS` dict; today's tools
live in `sutra_mcp/db_tools.py` and are registered into the server
[Day 34](../day-34-building-sutra-mcp-tools/LESSON.md) built. Retiring the dict is a later decision,
and making it today would mean editing a module three earlier days depend on.

**Read the parts in order and the paper last.** Section 2 needs section 1's vocabulary, section 4's
decision needs section 2's evidence, and the paper is only worth reading once you have written the
queries it argues for.

---

## §4 Build brief

Two things to write in the project, plus ten lab scripts that between them make zero model calls.

### The project files

| File | What it holds | Taught in |
| --- | --- | --- |
| `sutra_mcp/db_tools.py` | the hand-written SQL-backed tools and their brakes | 1.3, 2.1–2.5, 2.4, 6.1 |
| `sutra/data/tickets.sqlite3` | the archive itself — **generated, gitignored** | 1.2 |

`sutra_mcp/db_tools.py` is expected to export:

- `ARCHIVE` — the `Path` to `sutra/data/tickets.sqlite3`.
- `build_archive(path=ARCHIVE) -> Path` — creates the schema and seeds it from the same ticket world
  `sutra/loop.py` has served since Day 4. The **only** writer in the module, and not a tool.
- `connect_readonly() -> sqlite3.Connection` — the single place `sqlite3.connect` is called on the
  read path, carrying `mode=ro`, the authorizer and the step budget.
- `lookup_ticket(ticket_id: str) -> dict` — one ticket by id, `not_found` as data.
- `search_tickets(term: str, limit: int = 3) -> dict` — bound, clamped, with a `truncated` flag.
- `register_db_tools(server) -> None` — registers the two tools into the server object
  `build_server()` returns, in the same shape
  [Day 35](../day-35-resources-and-prompts/LESSON.md) uses for `register_resources(server)`.
  **Do not redefine `build_server()`** — Day 34 owns it.

### The lab scripts

| File | What it does | Taught in |
| --- | --- | --- |
| `lab/seed_lab.py` | builds a lab copy of the archive, resizable for the flood | 1.1, 1.2 |
| `lab/injection.py` | one argument, formatted and bound, side by side | 2.1 |
| `lab/brakes.py` | six brakes, six attacks, exit code = the number that failed | 2.2–2.6 |
| `lab/adk_tools.py` | the declaration ADK builds from a docstring | 3.1 |
| `lab/toolset_shape.py` | what an `McpToolset` will launch, before it launches | 3.2 |
| `lab/flood.py` | rows, characters, tokens, share of the window | 5.1 |
| `lab/drift.py` | the description's columns against the table's | 5.2 |
| `lab/undo.py` | a bulk write with and without a log | 5.3 |
| `lab/hold.py` | a held read transaction against a writer | 6.1 |
| `lab/brake_audit.py` | reads `sutra_mcp/db_tools.py` and counts the brakes | 6.3 |

`lab/papers/relational-model/` holds the paper demo — `layout.py` and `answer.py` — and it is **given
complete** in the paper part. It is teaching material, not a rep: type it, run both arms, and compare
your output with the transcript.

**`TODO(me)` markers left for you:**

- **1.2** — decide whether `sutra/loop.py`'s `TICKETS` dict should be deleted or kept as a fixture,
  and which day owns that change.
- **2.3** — write the action-code-to-name lookup the authorizer's log line needs, since `sqlite3`
  provides none, and decide what level that line logs at in a server.
- **2.5** — move the step counter off the module and into a closure created per statement, so two
  concurrent tool calls do not share a budget. Then decide the budget's number and say what machine
  you measured it on.
- **2.6** — add a sixth row to the brake table: **where** each brake is enforced. Decide which of the
  five you would be unhappy to have only in application code.
- **3.1** — write the test that asserts on the tool declaration: the name, the required list, and
  that the description states the row ceiling.
- **4.2** — write the decision as an ADR, including the trigger that expires it. Say what would have
  to be true for Sutra to adopt Toolbox, in one sentence a reviewer could check.
- **5.1** — provoke the context overflow once and record the provider's exact refusal in your notes,
  then decide the payload byte cap that goes beside the row cap.
- **5.2** — make `drift.py` read the description off the live tool object rather than a pasted
  constant, and decide which test file it belongs in.
- **5.3** — decide Sutra's write-tool policy before there is a write tool: does every bulk write log
  its previous values, does it return ids rather than a count, and does it sit behind
  `require_confirmation`?
- **6.2** — write down, in the repository, the table of what survives a move to Postgres. Add the row
  the day did not: what happens to the `truncated` flag under replication lag.
- **6.3** — extend `formatted_sql` to catch `term + "WHERE ..."`, where the literal is on the right,
  and decide whether the audit belongs in `./m check` today or on Day 45.

---

## §5 The eval that must be able to fail

Four checks, all with an exit code, all on zero model calls.

**The brake audit is the day's gate**, and it is RED before you write anything:

```bash
cd days/day-39-database-tools/lab && uv run python brake_audit.py; echo "exit: $?"
```

Measured on 2026-09-04: `findings: 6` and `exit: 1` — the file does not exist and all five brakes are
missing. It goes to `findings: 0` and `exit: 0` when `sutra_mcp/db_tools.py` carries all five. Then
replace one bound statement with an f-string and watch it come back with a line number.

**The brake lab is the one that proves they work rather than counting them:**

```bash
cd days/day-39-database-tools/lab && uv run python brakes.py; echo "exit: $?"
```

Measured the same day: five HELD, `exit: 0`, and brake 0 — the sentence in the description — FAILED
with `attack returned 205`. Add `sqlite3.SQLITE_ATTACH` to `ALLOWED` and it goes to `exit: 1`.

**The drift check is red on purpose and stays red until you fix the description:**

```bash
cd days/day-39-database-tools/lab && uv run python drift.py; echo "exit: $?"
```

`findings: 2` and `exit: 1`: `priority` promised and absent, `opened_on` present and undocumented.

**The paper demo is the ablation, and both arms must be run:**

```bash
cd days/day-39-database-tools/lab/papers/relational-model
LAYOUT=v1 uv run python answer.py
LAYOUT=v2 uv run python answer.py
cd -
```

Both approaches survive `v1`. Under `v2`, `navigate` returns `[]` — a wrong answer, not an error —
and `query` returns the same three ids it always did.

**And the rest, each of which can be broken on purpose:**

```bash
cd days/day-39-database-tools/lab
uv run python seed_lab.py
uv run python injection.py
uv run python adk_tools.py
uv run python toolset_shape.py
uv run python flood.py
uv run python undo.py
uv run python hold.py
cd -
```

---

## §6 Request budget

**Free-tier Gemini**, 20 generate requests per day per model (`gemini-3.7-flash`, roster re-verified
2026-09-04).

| What | Generations |
| --- | --- |
| every part in every section | **0** |
| all ten lab scripts | **0** |
| the paper demo, both arms | **0** |
| building the ADK tool declaration | **0** — inspection, not generation |
| **Total planned** | **0 of 20** |

**Zero, and it is not a compromise.** Everything today is a database, a file and some arithmetic. The
one place a model call would be natural — provoking the context overflow in
[5.1](parts/05-failure-lab/5.1-forty-thousand-rows.md) — is left as a `TODO(me)` with the exact
command, because the failure can be *measured* with `json.dumps` and a division, and measuring it
costs nothing. Your whole day's quota is still there tomorrow.

**Cost: $0.** No managed database, no cloud project, no binary downloaded.

---

## §7 Traps

- **`sqlite3.connect` creates the file if it is missing.** A typo in the path gives you a working
  connection to a brand new empty database and `no such table` on the first query (1.2).
- **`uri=True` is not optional and its absence is silent.** Without it, `file:archive.sqlite3?mode=ro`
  is treated as a **filename**; you get a file with that literal name and no brakes at all (2.2).
- **A missing `commit()` loses the whole write with no error.** The `finally` closes the connection
  and SQLite discards the transaction. `seeded ...: 0 tickets` and exit code 0 (1.2).
- **The driver blocking stacked statements is not a defence.** `execute` compiles one statement and
  raises `You can only execute one statement at a time`, which stops the loud attack and does nothing
  about the `OR` that changes an answer (2.1).
- **`mode=ro` does not stop a read from being wrong.** The injection returned closed tickets through a
  read-only connection quite happily (2.1, 2.2).
- **`ATTACH` is a read.** A read-only connection will open a second database file and query across it
  unless an authorizer says no (2.3).
- **`SQLITE_IGNORE` is not a gentler `SQLITE_DENY`.** The statement succeeds and the column comes back
  `NULL`, and the model reports that as a fact (2.3).
- **`not authorized` is the entire error message.** No action, no table, no column. Log the action
  code from inside the callback or you are guessing (2.3).
- **`LIMIT` without `ORDER BY` means "some of them".** It looks deterministic on a small table and is
  not, and it is the thing that breaks on a move to another engine (2.4, 6.2).
- **A row cap is not a byte cap.** Five rows of a 40 KB body is 200 KB. Trim text columns with
  `substr` in the engine, not in Python (2.4, 5.1).
- **`set_progress_handler(fn, n)`: `n` is the sampling interval, not the budget.** Two numbers
  multiply, and **zero means continue** — a handler that falls off the end returns `None`, which is
  falsy, which means "keep going" (2.5).
- **`interrupted` is the same message whether your budget fired or somebody cancelled.** Record which
  from inside the handler (2.5).
- **The docstring goes to the model whole.** There is no per-parameter description field being
  populated, so the `Args:` block is the only prose the model has (3.1).
- **`MCPToolset` is deprecated in favour of `McpToolset`**, and `DeprecationWarning` is hidden by
  default (3.2).
- **`StdioServerParameters` comes from the `mcp` package, not from ADK** (3.2).
- **`ImportError: cannot import name 'McpToolset'` usually means the wrong interpreter**, not a
  missing package — the `mcp_tool` package swallowed its own import error at debug level (3.2).
- **A toolset with no `tool_filter` has whatever tool list that server ships next Tuesday** (3.2).
- **Toolbox's prebuilt recipes ship inside the binary**, so upgrading it can change your agent's tool
  surface with no change to your configuration (4.1).
- **`google-adk[all]` is a trap.** Every cloud SDK, every sandbox provider, every driver — all of them
  yours to patch (4.3).
- **A schema migration and a tool docstring live in different files and nothing connects them.** The
  quiet direction of that drift produces no error at all (5.2).
- **A bulk write returns a count, not ids.** After `commit()` there is nothing to roll back and no way
  to say which rows were the mistake (5.3).
- **A held read transaction blocks writers**, and the error lands on the writer while the tool that
  caused it reports nothing (6.1).

---

## §8 Verify before you code

Fetched or run on **2026-09-04**, the day this was written.

**ADK — the installed package is the authority, and the page is named beside it:**

- `https://adk.dev/tools-custom/function-tools/` — read. *"The ADK framework automatically inspects
  your Python function's signature—including its name, docstring, parameters, type hints, and default
  values—to generate a schema."* · *"The docstring of your function serves as the tool's
  **description** and is sent to the LLM."* · *"A parameter is considered **required** if it has a
  type hint but **no default value**."* · the recommendation to return a `dict` with a `status` key.
- `https://adk.dev/tools-custom/mcp-tools/` — read. `McpToolset(connection_params=…, tool_filter=…)`;
  `StdioConnectionParams(server_params=StdioServerParameters(command=…, args=…, env=…))` from
  `google.adk.tools.mcp_tool.mcp_session_manager`; `StreamableHTTPConnectionParams(url=…, headers=…)`;
  and the explicit recommendation to *"Filter MCP tools using `tool_filter` to limit exposed
  functionality"*. Note that `https://adk.dev/tools/mcp-tools/` is now a redirect to this page.
- `.venv/Lib/site-packages/google/adk/tools/mcp_tool/__init__.py` — exports `McpToolset`/`MCPToolset`,
  `McpTool`/`MCPTool`, `StdioConnectionParams`, `StreamableHTTPConnectionParams`,
  `SseConnectionParams`, `to_mcp_server`, `adk_to_mcp_tool_type`, `gemini_to_json_schema`, inside a
  `try/except ImportError` that logs *"MCP Tool is not installed"* at debug level.
- `.venv/Lib/site-packages/google/adk/tools/mcp_tool/mcp_session_manager.py` —
  `StdioConnectionParams(server_params: StdioServerParameters, timeout: float = 5.0)`. The default is
  read from the class, not assumed.
- `.venv/Lib/site-packages/google/adk/tools/mcp_tool/mcp_toolset.py` — the full `McpToolset.__init__`
  signature, including `tool_filter`, `tool_name_prefix`, `tool_list_cache_ttl_seconds`,
  `require_confirmation`, `header_provider`, `progress_callback` and `elicitation_callback`. Also
  `MCPToolset.__init__`, which raises `DeprecationWarning: MCPToolset class is deprecated, use
  McpToolset instead.`
- Running `lab/adk_tools.py` emits `UserWarning: [EXPERIMENTAL] feature
  FeatureName.JSON_SCHEMA_FOR_FUNC_DECL is enabled.` — the `parameters_json_schema` key in the
  declaration is behind a feature flag in `google-adk==2.7.1`. Recorded, not worked around.

**The extras (ADK-78) — read off the installed distribution rather than a web page:**

```bash
grep -i "^Provides-Extra" .venv/Lib/site-packages/google_adk-2.7.1.dist-info/METADATA
grep -i "^Requires-Dist:.*extra ==" .venv/Lib/site-packages/google_adk-2.7.1.dist-info/METADATA
```

Twenty-three extras. `toolbox` resolves to exactly one package, `toolbox-adk>=1,<2`; `db` is
`sqlalchemy>=2,<3` plus `sqlalchemy-spanner>=1.14`; `redis` is `redis>=4.2`; `slack` is
`slack-bolt>=1.22`; `e2b` is `e2b>=2,<3`; `daytona` is `daytona>=0.191`.

**MCP Toolbox for Databases (ADK-25):**

- `https://mcp-toolbox.dev/` — current version **1.9.0**, released 2026-08-14 per the site footer;
  around fifty database integrations; configuration organised as **Sources**, **Tools** and
  **Toolsets**; prebuilt configurations offered per integration.
- `https://raw.githubusercontent.com/googleapis/mcp-toolbox/main/internal/prebuiltconfigs/tools/sqlite.yaml`
  — the SQLite prebuilt configuration, 117 lines, quoted directly in 4.1 and 4.2. Source
  `sqlite-source` with `database: ${SQLITE_DATABASE}`; tool `execute_sql` of type
  `sqlite-execute-sql` with the description *"Use this tool to execute SQL."*; tool `list_tables` of
  type `sqlite-sql` carrying a fixed information-schema statement; toolset `sqlite_database_tools`.
- `https://pypi.org/pypi/toolbox-adk/json` — `toolbox-adk` **1.4.0**, released 2026-09-01, summary
  *"Agent Development Kit Integration for MCP Toolbox"*. This is the ADK-side client, not the server.
- **Nothing was downloaded.** No binary, no extra, no package. Toolbox is 🅿️ parked (4.1).
- `https://mcp-toolbox.dev/resources/prebuilt/sqlite/` and
  `https://mcp-toolbox.dev/resources/sources/sqlite/` both returned **404** on this date; the
  documentation has moved under `/integrations/`. The custom-`tools.yaml` field names in 4.1 are
  therefore marked `TODO(verify: …)` rather than presented as verified — the prebuilt file above is
  quoted from the repository and is exact.

**The paper:**

- `https://api.crossref.org/works/10.1145/362384.362685` — title *"A relational model of data for
  large shared data banks"*, issued 1970-06. The abstract quoted in the paper part is that record's
  abstract, read the same day. `doi:10.1145/362384.362685` already has its dated row in
  `docs/PAPERS.md`, as does the 1983 CACM reprint `doi:10.1145/357980.358007`, which is named in the
  paper part as the one **not** to cite.

**The engine:**

```bash
uv run python -c "import sqlite3; print(sqlite3.sqlite_version, sqlite3.version)"
```

`sqlite3` is standard library, so there is no version to pin and no `docs/PACKAGES.md` row. The
engine version is whatever your Python was compiled against, which is a fact worth printing and not
a fact you control.

---

## §9 Say it in an interview

"Our agent's ticket archive was a Python dictionary — five entries in a module, so adding a ticket
meant a pull request. We moved it to SQLite, which is the whole engine in the standard library and
one file on disk, and the interesting part of that day was not the migration. It was that the moment
the archive became real, the tool that reads it became a capability we had to reason about.

The thing I would lead with is the control experiment. Almost every database tool I have seen carries
a line in its description saying it is read-only. We tested that sentence like a brake: read-write
connection, tool description saying read-only, one `UPDATE`. It closed 205 tickets and reported
success. The description was not ignored — it was never consulted, because a description is text sent
to a model and the `UPDATE` went to a database.

So we built five real brakes and attacked each one separately. Parameter binding, a read-only
connection URI, a SQLite authorizer allowing exactly SELECT, READ and FUNCTION, a `LIMIT` bound
server-side after clamping the caller's number, and a step budget through the progress handler. All
five held, and the reason we did them as five and not one is that they do not substitute for each
other: read-only says nothing about a query returning the wrong rows, and a row limit says nothing
about a query that runs forever.

The injection result is the one that changed how I think about it. Everybody pictures DROP TABLE, and
most drivers block that anyway — `sqlite3` refuses a second statement outright. What we actually got
from one crafted search term against a formatted statement was five rows where the tool's own
`status = 'open'` filter said two should be hidden. No error, success reported. The filter was still
there in the source; it had just been outvoted by an `OR` the caller supplied. And the usual trigger
for this in a support system is not an attacker, it is a ticket body with an apostrophe in it.

The other number worth quoting is the flood. Forty thousand matching tickets serialised to about 1.7
million tokens, which is 173% of the model's window — so the request cannot be sent at all, and the
failure surfaces at the generation call with a token-count error, one layer away from the query, on a
tool that reported `status: ok`. What made the ceiling easy to argue for was the other end of the
table: two hundred rows is 0.9% of the window. The cap costs you nothing.

On the build-versus-adopt question, I did look at MCP Toolbox for Databases properly. It is a Go
binary that serves about fifty databases over MCP from a YAML file, and it has two modes that are
really different products. Its custom mode is good — you declare each tool's statement with bound
parameters, so the tools are narrow and you get pooling and auth for free. Its prebuilt SQLite recipe
gives you a tool called `execute_sql` whose whole description is 'Use this tool to execute SQL', with
no statement and therefore no row limit. So I stopped framing it as generated versus hand-written and
started framing it as: was the statement reviewed before it ran, or authored by the model at request
time? We hand-write because our store is one SQLite file, so pooling and auth buy us nothing, and
because the tool result shape is ours — that is how we return a `truncated` flag. I wrote the trigger
into the decision record: the day this is Postgres with a second service, re-run the comparison, and
I expect it to flip.

And we made the whole thing checkable. One script attacks the five brakes and exits with the number
that failed. Another reads the tool file and looks for each brake by its source shape, and parses it
with `ast` to prove no statement is built by formatting — searching finds a thing that is present,
but proving something is nowhere needs a parser, because `SELECT` appears in comments and docstrings
too. That one ships with its blind spot written next to it."

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked and `./m depth 39` is green. Defined by
understanding and green checks, never by elapsed time — a part is finished when you could explain it
to someone else without the page open.

**Phase 6's gate** is the full MCP audit of `sutra-core` on Day 45. Today contributes two things to
it: a real data source behind MCP with a stated containment story, and an executable check that the
containment is still there. Day 40 generalises `tool_filter` into Sutra's filtering machinery, and
the `TODO(me)` about where each brake is enforced is the decision that day will want already made.

---

## §11 Ledger & commit

**`docs/PROGRESS.md`** — append:

```text
| 39 | <date> | MCP-15, ADK-25, ADK-78 | 20 (+1 paper) | <hash> | ✅ |
```

**`docs/PACKAGES.md`** — **no new rows.** Nothing was installed and nothing upgraded. `sqlite3` is
Python's standard library, so it has no pin; `google-adk` stays at `2.7.1` and `mcp` at `1.29.1`. The
findings that MCP Toolbox for Databases is at 1.9.0 and `toolbox-adk` at 1.4.0 are recorded in §8 for
whoever revisits the decision in [4.2](parts/04-toolbox-parked/4.2-who-writes-the-sql.md); neither is
a row until something is installed.

**`docs/PAPERS.md`** — **no new rows.** `doi:10.1145/362384.362685` already has its dated row and is
taught here in [`papers/01-relational-model.md`](papers/01-relational-model.md). The 1983 CACM
reprint `doi:10.1145/357980.358007` also has its row and is named in that part as the one *not* to
cite.

**`docs/SKILL_PROVENANCE.md`** — no new rows. No skill was added or changed.

**`.gitignore`** — **no new lines.** `*.db` and `*.sqlite3` have been there since Day 0, so
`sutra/data/tickets.sqlite3` is already ignored. §3 checks this rather than appending to it.

**The commit:**

```text
day 39: database tools - Toolbox versus hand-written - closes MCP-15, ADK-25, ADK-78
```
