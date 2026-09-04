# Day 34 — CHECKLIST

**IDs closed:** MCP-04, MCP-05, MCP-06
**Principles served:** 1, 2, 4, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18
**Parts:** 19 across 6 sections, no paper part

> `./m done 34` refuses to commit while any box below is unticked. It cannot tell whether you were
> honest — that part is yours.

## Demo command

```bash
curl -s https://modelcontextprotocol.io/specification/versioning | grep -o "specification/2026-07-28" | head -1
uv run python days/day-34-building-sutra-mcp-tools/lab/gate.py; echo "exit: $?"
uv run python days/day-34-building-sutra-mcp-tools/lab/schema.py
uv run python days/day-34-building-sutra-mcp-tools/lab/coerce.py
uv run python days/day-34-building-sutra-mcp-tools/lab/both.py
uv run python days/day-34-building-sutra-mcp-tools/lab/cacheable.py
uv run python days/day-34-building-sutra-mcp-tools/lab/order.py
uv run python days/day-34-building-sutra-mcp-tools/lab/drive.py
uv run python days/day-34-building-sutra-mcp-tools/lab/wire.py
uv run python days/day-34-building-sutra-mcp-tools/lab/escape.py
uv run python days/day-34-building-sutra-mcp-tools/lab/escape.py --guarded
uv run python days/day-34-building-sutra-mcp-tools/lab/escape.py --guarded 2>&1 1>/dev/null | head -8
uv run python days/day-34-building-sutra-mcp-tools/lab/stale.py --one-deploy
uv run python days/day-34-building-sutra-mcp-tools/lab/stale.py --two-deploys
./m depth 34 && ./m check && ./m trace && git log --oneline -1
```

Expected: `specification/2026-07-28`; then the gate — `findings: 1` and `exit: 1` before you write
the package, `findings: 0` and `exit: 0` after. Then two full tool declarations with
`lookup_ticketArguments` in one of the titles; then six coercion rows of which the last turns
`'04521'` into `4521`; then four cases of which two agree across both call paths and two do not; then
`['tools']` against `['cacheScope', 'tools', 'ttlMs']`; then `same array : False` and then `True`;
then four calls with `isError` False, False, True, True; then four probes of which only the two
involving `initialize` get a result; then a leaked DSN and then an exception class name, with a full
traceback on stderr; then `Unknown tool: close_ticket` against a retirement sentence. Then
`OK day 34 19 parts`, `./m check` green, a traceability line with `0 problem(s)`, and one commit.

## Setup

- [ ] `./m brief 34` read, and the three IDs confirmed as MCP-04, MCP-05, MCP-06
- [ ] **The specification freshness gate was run first** and
      `modelcontextprotocol.io/specification/versioning` still names **2026-07-28** as current — if it
      had moved, you stopped and amended (Principle 14)
- [ ] **No `uv add` and no `uv sync --upgrade` was run** — `git diff pyproject.toml uv.lock` is empty
- [ ] `sutra/mcp/` is untouched — that is Day 33's client package, and today is server-side only
- [ ] You know which seven later days add modules to `sutra_mcp/`, and that none of them adds a second
      server

## Section 1 — `01-the-server-object`

- [ ] **1.1** read · ran the one-liner that builds a `FastMCP` and prints its name · **named the three
      things a server is and the fourth thing the 2026-07-28 revision refuses** · found the
      statelessness sentence on the specification's `basic/index` page yourself
- [ ] **1.2** read · ran `schema.py` and confirmed it imported `serve.py` **without starting a
      server** · found the `if __name__ == "__main__":` line and said what happens to a test suite
      without it · **called `.run()` from inside an `async def` and saw
      `RuntimeError: Already running asyncio in this thread`**
- [ ] **1.3** read · ran `wire.py` and found the `serverInfo` block · **said what the `version` field
      is actually reporting** · decided, in writing, what Sutra's `serverInfo.version` should be and
      why · named three places outside this repository that hold a copy of the server's name
- [ ] **1.4** read · **drew the import arrow between `server.py` and `tools.py` and said which
      direction it must never run** · reproduced a circular import on purpose and read
      `partially initialized module` · said what a Day 35 file adds and where

## Section 2 — `02-function-to-declaration`

- [ ] **2.1** read · ran `schema.py` · **found the field in the output that no human chose**
      (`lookup_ticketArguments`) · used `@server.tool` without parentheses and read the `TypeError` ·
      deleted a docstring and confirmed the description became `""` with no complaint
- [ ] **2.2** read · **called `search_kb` with the exact words its own description recommends and got
      no match** · read the body and named a behaviour the description does not carry · rewrote the
      description so a stranger would get it right
- [ ] **2.3** read · ran `coerce.py` and **found the row where `'04521'` went in and `4521` came out**
      · read the `validate_input=False` comment in the SDK · changed `wants_integer`'s hint to `str`
      and said which rows flipped
- [ ] **2.4** read · ran `both.py` · **said which two of the four cases agree across both call paths
      and which Day 3 decision is why** · named the four things that change when a function is exposed

## Section 3 — `03-the-two-calls`

- [ ] **3.1** read · ran `cacheable.py` and saw one key against three · **set `CACHE_SCOPE` to
      `"private"` and said which caller that protects** · chose `sutra_mcp`'s `ttlMs` and wrote it
      down beside the client TTL from Day 33's 1.3, in both units
- [ ] **3.2** read · ran `order.py` and saw `False` then `True` · **found the specification sentence
      naming the two reasons deterministic order matters** · decided where the sort lives
- [ ] **3.3** read · ran `drive.py` · **printed `result.structuredContent` and explained why the same
      text appears twice** · named the two assumptions in `result.content[0].text`

## Section 4 — `04-two-kinds-of-no`

- [ ] **4.1** read · **justified each of `drive.py`'s four `isError` values in one sentence** · said
      why a missing ticket is not an error · wrote one tool error message that names the field, the
      rule, the value and the fix
- [ ] **4.2** read · ran `drive.py` and `wire.py` and **compared a result carrying `isError` with a
      reply carrying `error`** · said which of the two the SDK uses for an unknown tool and which the
      specification asks for · said what a client should do instead of branching on `isError`
- [ ] **4.3** read · ran `escape.py` **both ways** and the stderr command · **found the connection
      string in the unguarded output** · said what the operator gained in the guarded run · wrote
      `FORBIDDEN` for Sutra

## Section 5 — `05-lifecycle`

- [ ] **5.1** read · named the three handshake messages and the three things the server used to store
      · **compared probe 2's reply with probe 4's second reply and said what changed between them**
- [ ] **5.2** read · ran `wire.py` · **read both `(stderr)` lines and said which of the two `-32602`
      replies is a fair description of what happened** · confirmed `2026-07-28` is not in
      `SUPPORTED_PROTOCOL_VERSIONS` yourself
- [ ] **5.3** read · found `stateless_http=True` in `serve.py` and **said which transport it affects
      and which it does not** · wrote the SDK-revision assertion, saw it go red, and **wrote down why
      neither lowering the target nor deleting it is allowed**

## Section 6 — `06-in-production`

- [ ] **6.1** read · ran `stale.py` **both ways** · **said which arm a model can act on correctly** ·
      wrote Sutra's tool-retirement procedure, including the case where a parameter becomes required
- [ ] **6.2** read · ran `gate.py` before writing anything and got `findings: 1` · **broke exactly one
      of the six on purpose after it went green, read the finding that named it, and put it back** ·
      said which of the six exists because of stdio rather than because of MCP

## The build

- [ ] `sutra_mcp/server.py` and `sutra_mcp/tools.py` exist and **you typed every line**
- [ ] `build_server()` takes no arguments, returns the object, and blocks on nothing; the only
      `.run()` call is under `if __name__ == "__main__":`
- [ ] `register_tools(server)` takes a server, returns `None`, and constructs nothing
- [ ] **`lookup_ticket` and `search_kb` are imported from `sutra/loop.py`, not retyped** — one
      implementation, two doors
- [ ] The server's name is exactly `sutra-mcp`, from a module constant
- [ ] The `TODO(me)` markers in §4 are still `TODO(me)` — none of them was quietly solved for you
- [ ] `uv run python days/day-34-building-sutra-mcp-tools/lab/gate.py` prints `findings: 0`

## The eval

- [ ] The gate was **red first** — `ModuleNotFoundError: No module named 'sutra_mcp.server'` — before
      you wrote the package
- [ ] The retirement ablation was run **both ways** and both outputs recorded
- [ ] The leak ablation was run **both ways**, plus the stderr command, and all three recorded
- [ ] At least three of the named breaks were performed on purpose and reverted
- [ ] `wire.py` was run and its verdict written down: this server speaks `2025-11-25`

## The budget

- [ ] Total generations spent: **0 of 20**
- [ ] No `GOOGLE_API_KEY` was needed by anything in this day
- [ ] The only network traffic was one HTTPS GET to the specification site (and optionally PyPI)

## The ledger

- [ ] `docs/PROGRESS.md` row pasted from §11, with the real date and hash
- [ ] `docs/PACKAGES.md` — **no new row**; nothing was installed and nothing upgraded
- [ ] `docs/PAPERS.md` — **no new row**; both DOIs already have theirs and are taught on Days 15 and 21
- [ ] `docs/SKILL_PROVENANCE.md` — **no new row**
- [ ] `./m depth 34` green · `./m check` green · `./m trace` prints `0 problem(s)`
- [ ] `git status` shows no `.env`; commit message is the one in §11
