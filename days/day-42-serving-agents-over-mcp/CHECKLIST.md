# Day 42 — CHECKLIST

**IDs closed:** MCP-33, ADK-26
**Principles served:** 1, 2, 4, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18
**Parts:** 19 across 6 sections, plus one paper part

> `./m done 42` refuses to commit while any box below is unticked. It cannot tell whether you were
> honest — that part is yours.

## Demo command

```bash
curl -sL https://modelcontextprotocol.io/specification/versioning | grep -o "2026-07-28" | head -1
uv run python -c "from google.adk.tools.mcp_tool import to_mcp_server; import inspect; print(inspect.signature(to_mcp_server))"
uv run python days/day-42-serving-agents-over-mcp/lab/gate.py; echo "exit: $?"
uv run python days/day-42-serving-agents-over-mcp/lab/served_surface.py
uv run python days/day-42-serving-agents-over-mcp/lab/connections.py
uv run python days/day-42-serving-agents-over-mcp/lab/blocks.py
uv run python days/day-42-serving-agents-over-mcp/lab/blocks.py --deaf
uv run python days/day-42-serving-agents-over-mcp/lab/granted.py
uv run python days/day-42-serving-agents-over-mcp/lab/granted.py --narrowed
uv run python days/day-42-serving-agents-over-mcp/lab/price.py
uv run python days/day-42-serving-agents-over-mcp/lab/price.py --tools-only
uv run python days/day-42-serving-agents-over-mcp/lab/recurse.py
uv run python days/day-42-serving-agents-over-mcp/lab/recurse.py --guarded
uv run python days/day-42-serving-agents-over-mcp/lab/slow.py
uv run python days/day-42-serving-agents-over-mcp/lab/slow.py --patient
uv run python days/day-42-serving-agents-over-mcp/lab/throttled.py
uv run python days/day-42-serving-agents-over-mcp/lab/throttled.py --guarded
uv run python days/day-42-serving-agents-over-mcp/lab/guarded_import.py
uv run python days/day-42-serving-agents-over-mcp/lab/guarded_import.py --debug
cd days/day-42-serving-agents-over-mcp/lab/papers/a-note-on-distributed-computing && REMOTE=0 uv run python shop.py && REMOTE=1 uv run python shop.py && cd -
./m depth 42 && ./m check && ./m trace && git log --oneline -1
```

Expected: `2026-07-28`; then `(agent: 'BaseAgent', *, name: 'Optional[str]' = None, instructions:
'Optional[str]' = None, runner: 'Optional[Runner]' = None) -> 'FastMCP'`; then the gate — `findings:
1` and `exit: 1` before you write the module, `findings: 0` and `exit: 0` after. Then one tool named
`sutra_kb_answerer` with `outputSchema: null`; then two sessions across two connections, all four
calls as `user=mcp_user`; then `blocks : 2` with and without the progress line; then `tools the
caller sees : ['sutra_desk']` against `tools the caller reaches: ['lookup_ticket', 'search_kb',
'close_ticket', 'refund']`, and the narrowed arm reaching one; then `calls answered : 6` against
`calls answered : 40`; then `agent runs executed: 8` against `1` with the identical caller-visible
answer; then an `McpError` timeout against `KB-104 explains the logout loop.`; then 543 characters
against 32; then `__all__ : []` with the reason invisible and then visible. Then `3` believed and `3`
gone, against `3` believed and **`4`** gone. Then `OK day 42 19 parts`, `./m check` green, a
traceability line with `0 problem(s)`, and one commit.

## Setup

- [ ] `./m brief 42` read, and the two IDs confirmed as MCP-33, ADK-26
- [ ] **The specification freshness gate was run first** and
      `modelcontextprotocol.io/specification/versioning` still names **2026-07-28** as current — if it
      had moved, you stopped and amended (Principle 14). You used `curl -sL`, not `curl -s`
- [ ] **`to_mcp_server`'s signature was printed from the installed package**, not read off this page,
      and it matched
- [ ] **No `uv add`, no `uv sync --upgrade`** — `git diff pyproject.toml uv.lock` is empty, and you
      know PyPI is at `google-adk==2.8.0` while this repository stays at `2.7.1`, and why
- [ ] `sutra/mcp/` is untouched — that is the client package from Days 33 and 40; today is
      entirely server-side
- [ ] You know that today **does not** add a line to `build_server()`, and can say why in one sentence

## Section 1 — `01-the-back-office`

- [ ] **1.1** read · ran `served_surface.py` · **found the one field a caller gets to decide *when* to
      use this tool** · said what is different about a served agent versus a served function without
      using the words "agent" or "protocol"
- [ ] **1.2** read · **deleted `description=` from `served_surface.py`, ran it, and read ADK's
      fallback string on the wire** · put it back · named the two things `name=` sets · confirmed for
      yourself that `to_mcp_server(agent, "x")` raises `TypeError`
- [ ] **1.3** read · ran `connections.py` · **found `_MCP_USER_ID` in the ADK source and counted how
      many places read it** · said whether passing your own `Runner` changes any of them · named the
      four services and which two Day 47 replaces
- [ ] **1.4** read · ran `gate.py` · **added `from sutra_mcp import agent_server` to
      `sutra_mcp/server.py`, watched the gate go red, and took it out** · said why `to_mcp_server`
      cannot follow the `register_x(server)` convention

## Section 2 — `02-what-crosses-the-counter`

- [ ] **2.1** read · **said what a caller sending `{"request": ""}` gets, and what it costs** ·
      searched the output for `minLength` and found nothing · named the two pieces of prose a served
      agent publishes
- [ ] **2.2** read · ran `blocks.py` **both ways** and diffed them · **changed the final PNG MIME type
      to `application/pdf` and named the block type that came back** · said which kind of part is
      always dropped and why it does not even become a progress notification
- [ ] **2.3** read · ran `connections.py` · **added a third connection that closes and reopens, and
      predicted `turns` before running it** · said what the session map is keyed on · named one
      ordinary client behaviour that resets a conversation with no error
- [ ] **2.4** read · ran `granted.py` **both ways** · **added a second sub-agent and watched the reach
      grow while the visible tool list did not** · said why a caller cannot apply Day 40's filtering
      here, and named the one lever you have instead

## Section 3 — `03-tool-or-peer`

- [ ] **3.1** read · printed `to_mcp_server`'s signature and read `to_a2a`'s off the file with `sed` ·
      **confirmed for yourself that `import a2a` fails here, and can say why that is correct** ·
      listed every argument in one signature and not the other
- [ ] **3.2** read · ran the paper demo **both arms** · **said which run has a number that disagrees
      with itself, and named the line of `shop.py` that made the caller wrong** · named the three
      outcomes of a remote call and which has no local equivalent · read §6 and followed the link
- [ ] **3.3** read · ran `granted.py --narrowed` · **wrote Sutra's verdict in one sentence in your own
      words** · gave the single fact about `to_mcp_server` that makes "serve the desk and restrict it
      in the instruction" unworkable · listed the three things deliberately 🅿️ parked

## Section 4 — `04-what-a-call-costs`

- [ ] **4.1** read · ran `price.py` **both arms** · **added `5` to `TOOL_ROUND_TRIPS` and said how
      many calls that version of the desk serves** · gave the formula for generations per served call
- [ ] **4.2** read · **set `CALLS_PER_DAY` to your own honest number and read the answered count** ·
      named the two things you would have to build before letting a second team mount it · said which
      six calls get answered and why that is worse than the number looks
- [ ] **4.3** read · **printed `Tool.model_fields` and `ToolAnnotations.model_fields` yourself** ·
      confirmed a served tool's `annotations` is `None` · counted the sentences in the description and
      matched each to one of the four jobs · listed every infrastructure fact `throttled.py`'s
      unguarded arm leaks

## Section 5 — `05-failure-lab`

- [ ] **5.1** read · ran `recurse.py` **both arms** · **confirmed the caller-visible answer is
      identical in both** · raised `CEILING` to 20, multiplied the runs by three, compared with 20 ·
      said what actually stops a self-calling served agent
- [ ] **5.2** read · ran `slow.py` **both arms** · **set `LEGS` to 5 and said what number the caller
      would have needed, and how they could have known it** · said what the server does when a
      caller's timeout fires
- [ ] **5.3** read · ran `throttled.py` **both arms** and counted the characters in each ·
      **listed every fact about Sutra's infrastructure recoverable from the unguarded output** ·
      named the one SDK line that turns an exception into caller-facing text · said why the guarded
      arm returns `isError: false`

## Section 6 — `06-in-production`

- [ ] **6.1** read · ran `guarded_import.py` **both arms** · **counted the imports inside the single
      `try` in `mcp_tool/__init__.py` yourself** and said how many root causes produce the identical
      message · named the four separate risks and which one needs a logging change to see
- [ ] **6.2** read · **ran `gate.py` before writing anything and got `findings: 1`** · broke exactly
      one statement on purpose after it went green, read the finding that named it, and put it back ·
      named the three things the gate deliberately does not check and which you would fix first

## The paper

- [ ] [`papers/01-a-note-on-distributed-computing.md`](papers/01-a-note-on-distributed-computing.md)
      read **after** the parts, not before
- [ ] The demo was run **both ways** and both outputs recorded: `3` and `3`, against `3` and **`4`**
- [ ] `DROP_REPLY_ON_CALL` changed to `1`, the disagreement predicted **before** running, then run
- [ ] **Out loud:** the four differences named, the decisive one identified with its reason, and one
      thing in a system you have used that exists only because of it

## The build

- [ ] `sutra_mcp/agent_server.py` exists and **you typed every line**
- [ ] `build_agent_server() -> FastMCP` returns and blocks on nothing; `run(...)` is under
      `if __name__ == "__main__":` and nowhere else
- [ ] `SERVED_AGENT_NAME`, `SERVED_DESCRIPTION` and `REACH` are module constants, not literals buried
      in a call
- [ ] The agent served is **not** `build_desk()` — it is a narrow read-only agent built for the door,
      with `sub_agents=[]` written explicitly
- [ ] `search_kb` is **imported** from `sutra/loop.py`, not retyped
- [ ] `sutra_mcp/server.py` gained **nothing** — no import, no line in `build_server()`
- [ ] The description says what fits, what does not, that a call runs a model, and that retries are
      not automatic
- [ ] All nine `TODO(me)` markers in §4 are still `TODO(me)` — none was quietly solved for you
- [ ] `uv run python days/day-42-serving-agents-over-mcp/lab/gate.py` prints `findings: 0`

## The eval

- [ ] The gate was **red first** — `ModuleNotFoundError: No module named 'sutra_mcp.agent_server'` —
      before you wrote the module
- [ ] The recursion ablation was run **both ways** and both outputs recorded
- [ ] The leak ablation was run **both ways** and both character counts recorded
- [ ] The paper demo was run **both ways** and both final numbers recorded
- [ ] At least three of the named breaks were performed on purpose and reverted

## The budget

- [ ] Total generations spent: **0 of 20**
- [ ] No `GOOGLE_API_KEY` was needed by anything in this day, and no lab script called a model
- [ ] The only network traffic was two HTTPS GETs — the specification versioning page and PyPI

## The ledger

- [ ] `docs/PROGRESS.md` row pasted from §11, with the real hash
- [ ] `docs/PACKAGES.md` — **no new row**; nothing installed, nothing upgraded, `a2a` extra not added
- [ ] `docs/PAPERS.md` — **no new row**; `doi:10.1007/3-540-62852-5_6` already has its dated row and
      is taught here for the first time
- [ ] `docs/SKILL_PROVENANCE.md` — **no new row**
- [ ] `./m depth 42` green · `./m check` green · `./m trace` prints `0 problem(s)`
- [ ] `git status` shows no `.env`; commit message is the one in §11
