# Day 41 — CHECKLIST

**IDs closed:** MCP-18, MCP-19, MCP-29
**Principles served:** 1, 2, 4, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18
**Parts:** 19 across 6 sections, no paper part

> `./m done 41` refuses to commit while any box below is unticked. It cannot tell whether you were
> honest — that part is yours.

## Demo command

```bash
curl -s https://modelcontextprotocol.io/specification/versioning | grep -o "specification/2026-07-28" | head -1
uv run python days/day-41-capabilities-and-mcp-apps/lab/gate.py; echo "exit: $?"
uv run python days/day-41-capabilities-and-mcp-apps/lab/declared.py
uv run python days/day-41-capabilities-and-mcp-apps/lab/client_meta.py
uv run python days/day-41-capabilities-and-mcp-apps/lab/undeclared.py
uv run python days/day-41-capabilities-and-mcp-apps/lab/drift.py; echo "exit: $?"
uv run python days/day-41-capabilities-and-mcp-apps/lab/apps_sketch.py
uv run python days/day-41-capabilities-and-mcp-apps/lab/csp.py
uv run python days/day-41-capabilities-and-mcp-apps/lab/interpolate.py
uv run python days/day-41-capabilities-and-mcp-apps/lab/stale.py
uv run python days/day-41-capabilities-and-mcp-apps/lab/stale.py --two-deploys
./m depth 41 && ./m check && ./m trace && git log --oneline -1
```

Expected: `specification/2026-07-28`; then the gate — `findings: 1` and `exit: 1` before you write
the module, `findings: 0` and `exit: 0` after. Then four declarations of which the last is an empty
`FastMCP` claiming three families; then two `_meta` envelopes differing by 86 bytes; then
`prompts/list -> error -32601: Method not found`; then `promises: 4  broken: 2` with `exit: 1`; then
one `ui://` resource, two tools and `the model may see: ['close_ticket']`; then three CSP cases of
which only the third has an origin in `connect-src`; then `buttons in the page : 2` against
`buttons in the page : 1`; then the same withdrawal with and without the middle deployment. Then
`OK day 41 19 parts`, `./m check` green, a traceability line with `0 problem(s)`, and one commit.

## Setup

- [ ] `./m brief 41` read, and the three IDs confirmed as MCP-18, MCP-19, MCP-29
- [ ] **The specification freshness gate was run first** and
      `modelcontextprotocol.io/specification/versioning` still names **2026-07-28** as current — if it
      had moved, you stopped and amended (Principle 14)
- [ ] **No `uv add`, no `uv sync --upgrade`, no `npm install`** — `git diff pyproject.toml uv.lock` is
      empty and no Node project was cloned
- [ ] `sutra/mcp/` is untouched — that is the client package from Days 33 and 40; today is
      protocol- and server-side
- [ ] You know that `capabilities.py` is **one module and one line in `build_server()`**, and which
      direction the import arrow between `server.py` and it must run

## Section 1 — `01-what-a-server-declares`

- [ ] **1.1** read · ran `declared.py` · **said what `"tools": {"listChanged": false}` promises and
      what it does not** · printed `ServerCapabilities.model_fields` and named the one field that is
      not a method family
- [ ] **1.2** read · ran arm D and saw **three families from an empty `FastMCP`** · found
      `get_capabilities` in the SDK and named the handler it tests per family · added a tool to arm D
      and confirmed the declaration did not change
- [ ] **1.3** read · **gave the exact identifier of the MCP Apps extension from memory** · confirmed
      `'extensions' in ServerCapabilities.model_fields` is `False` yourself · found the two
      `create_initialization_options()` calls in `fastmcp/server.py` and said why an extension claim
      cannot reach the wire
- [ ] **1.4** read · ran `client_meta.py` · **said how often a client declares and why it is not
      once** · named the error code a server returns for a capability the client did not declare, and
      the HTTP status beside it · read §6 and followed the link to Day 32's paper part

## Section 2 — `02-discovery-without-sessions`

- [ ] **2.1** read · **said which field of a `server/discover` reply answers "does this server do
      prompts", and why the answer is an absence** · wrote the reply `undeclared.py`'s server would
      send · chose a `ttlMs` for the declaration and said why it differs from the tool list's
- [ ] **2.2** read · **ran the five-string grep yourself and got zero five times** · printed
      `LATEST_PROTOCOL_VERSION` and `SUPPORTED_PROTOCOL_VERSIONS` · wrote the two lines saying what
      `capabilities.py` can do and what it can only record
- [ ] **2.3** read · ran `undeclared.py` · **named the three JSON-RPC codes and said which has no
      useful retry** · added an empty `list_prompts` handler and said which of the two outcomes Day
      45's audit should record as a finding

## Section 3 — `03-declared-versus-implemented`

- [ ] **3.1** read · **named the three ways a declaration and an implementation drift** · said which
      one fails in the safe direction and why that makes it worse · said which of `drift.py`'s two
      broken promises an error dashboard would have caught
- [ ] **3.2** read · ran `drift.py` and read the exit code · **found the `ErrorData(code=0, ...)` line
      in the SDK yourself** · added `export_archive` to `IMPLEMENTED` and watched `broken` fall to 1 ·
      said what the exit code should be for an empty catalogue and defended it
- [ ] **3.3** read · **listed the seven pre-declared mechanisms from memory and named the one Sutra
      has not built** · stated the rule in one sentence · said what property a client loses when a
      server can mint something at call time

## Section 4 — `04-a-server-that-draws`

- [ ] **4.1** read · ran `apps_sketch.py` · **named the three moving parts and said which cannot run
      here** · set `record_verdict` to `["model", "app"]` and said what a prompt-injected model could
      then do
- [ ] **4.2** read · ran `apps_sketch.py` twice and confirmed the byte count is identical · **added a
      random value to `PANEL_HTML` and named which of the five host abilities that destroyed** · said
      what `visibility: ["app"]` takes away from the model
- [ ] **4.3** read · ran `csp.py` · **named the two separate controls people mean by "sandboxed
      iframe"** · added a `frameDomains` case and said which directive changed · said which direction
      a host may move the policy
- [ ] **4.4** read · **said how many messages travel directly between the panel and the server** ·
      named the one event field that cannot be forged · chose the `ui/` method you would disable first
      and said what it costs
- [ ] **4.5** read · **gave the three parking reasons in order of weight and the trigger to re-open**
      · filled the two `TODO(me)` rows of the sketch table and added a ninth · named the fact about
      the outside world that reason 2 depends on

## Section 5 — `05-failure-lab`

- [ ] **5.1** read · ran `interpolate.py` and **counted two buttons in arm A and one in arm B** ·
      added `html.escape` to `improvised` and said what is still wrong · named the property assignment
      that decides text from markup
- [ ] **5.2** read · ran `stale.py` **both ways** · **said which arm a client would have noticed** ·
      wrote `sutra-mcp`'s withdrawal procedure with the number of milliseconds in it and said where
      that number is recorded

## Section 6 — `06-in-production`

- [ ] **6.1** read · ran `gate.py` before writing anything and got `findings: 1` · **broke exactly one
      statement on purpose after it went green, read the finding that named it, and put it back** ·
      said why `audit()` belongs in the gate and not in `build_server()`
- [ ] **6.2** read · **answered questions 1 to 6 in writing for the server `apps_sketch.py` builds,
      using only its output and `csp.py`'s** · answered 7, 8 and 9 for Sutra's host · said which of
      the three you are least confident about

## The build

- [ ] `sutra_mcp/capabilities.py` exists and **you typed every line**
- [ ] `register_capabilities(server) -> None` matches Day 34's registration signature exactly, and
      `build_server()` gained **one line** and nothing else
- [ ] The import arrow runs one way: `server.py` imports `capabilities`, and `capabilities` imports
      nothing from `server.py`
- [ ] `DECLARED_FAMILIES` is a `frozenset` and every member is a real `ServerCapabilities` field
- [ ] `EXTENSIONS` and `UI_RESOURCES` are **empty together**, with the parking reason and its trigger
      in a comment beside them
- [ ] `audit(server)` returns **sentences**, in both directions, sorted — and is called from the gate,
      never from `build_server()`
- [ ] The `TODO(me)` markers in §4 are still `TODO(me)` — none of them was quietly solved for you
- [ ] `uv run python days/day-41-capabilities-and-mcp-apps/lab/gate.py` prints `findings: 0`

## The eval

- [ ] The gate was **red first** — `ImportError: cannot import name 'capabilities' from 'sutra_mcp'` —
      before you wrote the module
- [ ] `drift.py` was run and its exit code read; the count was changed on purpose and changed back
- [ ] The withdrawal ablation was run **both ways** and both outputs recorded
- [ ] At least three of the named breaks were performed on purpose and reverted
- [ ] The five-string SDK grep was run **by you**, not read off this page, and printed zero five times

## The budget

- [ ] Total generations spent: **0 of 20**
- [ ] No `GOOGLE_API_KEY` was needed by anything in this day
- [ ] The only network traffic was HTTPS GETs to the specification site and the pages in §8

## The ledger

- [ ] `docs/PROGRESS.md` row pasted from §11, with the real date and hash
- [ ] `docs/PACKAGES.md` — **no new row**; nothing was installed, nothing upgraded, no npm package
- [ ] `docs/PAPERS.md` — **no new row**; `doi:10.1145/514183.514185` already has its row and is taught
      on Day 32
- [ ] `docs/SKILL_PROVENANCE.md` — **no new row**
- [ ] `./m depth 41` green · `./m check` green · `./m trace` prints `0 problem(s)`
- [ ] `git status` shows no `.env`; commit message is the one in §11
