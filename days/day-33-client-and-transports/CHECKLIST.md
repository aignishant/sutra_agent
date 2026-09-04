# Day 33 — CHECKLIST

**IDs closed:** MCP-02, MCP-03
**Principles served:** 1, 2, 4, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18
**Parts:** 19 across 6 sections, no paper part

> `./m done 33` refuses to commit while any box below is unticked. It cannot tell whether you were
> honest — that part is yours.

## Demo command

```bash
curl -s https://modelcontextprotocol.io/specification/versioning | grep -o "specification/2026-07-28" | head -1
uv run python -c "from sutra.mcp.client import connect_stdio, connect_http, list_tools; print('client ok')"
uv run python days/day-33-client-and-transports/lab/list_tools.py
uv run python days/day-33-client-and-transports/lab/list_tools.py --filtered
uv run python days/day-33-client-and-transports/lab/list_tools.py --repeat 2>&1 | grep -c "tools/list"
uv run python days/day-33-client-and-transports/lab/list_tools.py --repeat --ttl 2>&1 | grep -c "tools/list"
uv run python days/day-33-client-and-transports/lab/leak.py
uv run python days/day-33-client-and-transports/lab/frame.py
uv run python days/day-33-client-and-transports/lab/http_shape.py
uv run python days/day-33-client-and-transports/lab/http_shape.py --bad-accept
uv run python days/day-33-client-and-transports/lab/http_shape.py --bad-origin
uv run python days/day-33-client-and-transports/lab/http_shape.py --get
uv run python days/day-33-client-and-transports/lab/legacy_sse.py; echo "exit: $?"
uv run python days/day-33-client-and-transports/lab/noisy_stdout.py --quiet; echo "exit: $?"
uv run python days/day-33-client-and-transports/lab/noisy_stdout.py --line;  echo "exit: $?"
uv run python days/day-33-client-and-transports/lab/noisy_stdout.py --glued; echo "exit: $?"
uv run python days/day-33-client-and-transports/lab/missing_command.py --real
uv run python days/day-33-client-and-transports/lab/missing_command.py
./m depth 33 && ./m check && ./m trace && git log --oneline -1
```

Expected: `specification/2026-07-28`; then `client ok`; then three tool names, then two;
then **3** against **1**; then the tidy server's goodbye before the parent's next line and the leaked
one's after its last; then **1** line against **12**; then `application/json` and then
`text/event-stream` with two progress records; then `400`, then `403`, then `405`; then
`legacy still importable : ['mcp.client.sse.sse_client',
'google.adk.tools.mcp_tool.SseConnectionParams']` and `exit: 1`; then `exit: 0`, `exit: 0` **with a
traceback above it**, and `exit: 1` after a timeout; then three tools, then
`shutil.which  : None` followed by `[WinError 2]`. Then `OK day 33 19 parts`, `OK all green`, a
traceability line with `0 problem(s)`, and one commit.

## Setup

- [ ] `./m brief 33` read, and the two IDs confirmed as MCP-02, MCP-03
- [ ] **The specification freshness gate was run first** and
      `modelcontextprotocol.io/specification/versioning` still names **2026-07-28** as current — if it
      had moved, you stopped and amended (Principle 14)
- [ ] **No `uv add` and no `uv sync --upgrade` was run** — `git diff pyproject.toml uv.lock` is empty
- [ ] `sutra_mcp/` is untouched and `sutra_mcp/__init__.py` is still empty — Day 34 fills it
- [ ] `sutra/mcp/` created, and you know that Days 37, 40 and 44 add modules beside `client.py`

## Section 1 — `01-the-connector`

- [ ] **1.1** read · ran `list_tools.py` and got three names · **found those names in
      `fake_desk_server.py` and confirmed `list_tools.py` mentions none of them** · said which of the
      three MCP roles `McpToolset` is
- [ ] **1.2** read · ran `missing_command.py` **both ways** and saw `constructed   : ok` printed by the
      failing arm · **set `GHOST` to `"npx"` and watched the failure change into a timeout**
- [ ] **1.3** read · named the five steps in order · ran `--repeat` and `--repeat --ttl` and counted
      `tools/list` lines · **reversed `TOOLS` in the fake server and watched the printed order not
      change** · chose the TTL Sutra will use and wrote down what it costs when a tool is deleted
- [ ] **1.4** read · ran `--filtered` and saw `desk_wipe_tickets` disappear · **read the description
      the server sends with it and said where that sentence ends up** · broke one letter of
      `READ_ONLY` and saw two names in, one out, exit 0
- [ ] **1.5** read · ran `leak.py` and located both `stdin closed, exiting` lines relative to the
      `PARENT:` lines · **added `await leaked.close()` and watched the second goodbye move** · said who
      calls `close()` when the toolset is attached to an agent

## Section 2 — `02-stdio`

- [ ] **2.1** read · **ran `fake_desk_server.py` by hand, typed a `tools/list` message at it, and read
      the reply** · closed its stdin from the keyboard · named two things stdio does not need
- [ ] **2.2** read · ran `frame.py` and saw **1 line against 12** · **found the surviving
      `line one\nline two` in the pretty-printed output** and said why that newline was harmless
- [ ] **2.3** read · ran the same command with `2>/dev/null` and then `1>/dev/null` and got two
      disjoint halves · **confirmed exactly one function in the fake server writes to stdout** · said
      what the client is required *not* to conclude from stderr
- [ ] **2.4** read · ran `list_tools.py` and saw `stdin closed, exiting` at the end · performed step 1
      by hand with `Ctrl-D` · **said why "restart and retry" is complete under this revision and was
      not under the previous one**

## Section 3 — `03-streamable-http`

- [ ] **3.1** read · ran `http_shape.py` and saw two POSTs to one URL · ran `--get` and got `405` ·
      **found the two lines in the script that make GET and DELETE the same handler**
- [ ] **3.2** read · saw `application/json` for one request and `text/event-stream` for the other ·
      **changed `_stream`'s loop to five records and counted them** · found the one record with an `id`
      and said why only it has one
- [ ] **3.3** read · **broke out of the response loop early and watched a request get cancelled with
      no message sent** · wrote out the stdio `notifications/cancelled` message and said why it has no
      top-level `id`
- [ ] **3.4** read · ran `--bad-origin` and got `403` · **deleted the three `origin` lines, watched the
      same request succeed, and put them back** · explained DNS rebinding out loud

## Section 4 — `04-choosing-a-wire`

- [ ] **4.1** read · ran the stdio lab and the HTTP lab and **found the `tools/list` request in each
      transcript** · said which of the differences between them is about MCP (none)
- [ ] **4.2** read · ran `legacy_sse.py` and got `exit: 1` · **opened
      `.venv/Lib/site-packages/google/adk/tools/mcp_tool/__init__.py` and found `SseConnectionParams`
      in `__all__` beside the two live ones** · said what the first step of a legacy tutorial looks
      like

## Section 5 — `05-failure-lab`

- [ ] **5.1** read · ran all three modes · **saw `--line` exit 0 with a traceback above the correct
      answer** and `--glued` exit 1 after a timeout · read the `input_value=` field in both and said
      what each one confesses
- [ ] **5.2** read · ran both arms · **counted the two `Error on session runner task` lines and said
      why there are two** · set `GHOST` to a file that exists and is not executable, and read the third
      message

## Section 6 — `06-in-production`

- [ ] **6.1** read · **confirmed there is no `connect()` call and no connection-state variable anywhere
      in `list_tools.py`** · gave the two meanings of "connection" and named three ordinary events that
      close the transport one
- [ ] **6.2** read · ran `leak.py` and traced which `[fake-desk]` lines belong to which toolset ·
      **decided, in writing, what the agent does when one of several servers will not answer**

## The build

- [ ] `sutra/mcp/__init__.py` and `sutra/mcp/client.py` exist and **you typed every line**
- [ ] `connect_stdio` and `connect_http` are plain `def`s, not coroutines, and their docstrings say in
      the first line that they connect to nothing and that the caller must `close()`
- [ ] `list_tools` returns names, not `McpTool` objects, and is safe to call twice
- [ ] The `TODO(me)` markers in §4 are still `TODO(me)` — none of them was quietly solved for you
- [ ] `uv run python -c "from sutra.mcp.client import connect_stdio, connect_http, list_tools"` prints
      `client ok`

## The eval

- [ ] The client check was **red first** — `ModuleNotFoundError: No module named 'sutra.mcp'` — before
      you wrote the package
- [ ] The allowlist ablation was run **both ways** and the two tool lists recorded
- [ ] The cache ablation printed **3** and then **1**
- [ ] `legacy_sse.py` exited **1**, and you understand why that red is informational and not yours to
      fix
- [ ] At least three of the named breaks were performed on purpose and reverted

## The budget

- [ ] Total generations spent: **0 of 20**
- [ ] No `GOOGLE_API_KEY` was needed by anything in this day
- [ ] The only network traffic was one HTTPS GET to the specification site (and optionally PyPI), plus
      servers on `127.0.0.1`

## The ledger

- [ ] `docs/PROGRESS.md` row pasted from §11, with the real date and hash
- [ ] `docs/PACKAGES.md` — **no new row**; nothing was installed and nothing upgraded
- [ ] `docs/PAPERS.md` — **no new row**; both DOIs already have theirs and are taught on Days 15 and 32
- [ ] `docs/SKILL_PROVENANCE.md` — **no new row**
- [ ] `./m depth 33` green · `./m check` green · `./m trace` prints `0 problem(s)`
- [ ] `git status` shows no `.env`; commit message is the one in §11
