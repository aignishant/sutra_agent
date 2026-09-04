# Day 36 — CHECKLIST

**IDs closed:** MCP-10, MCP-14, MCP-28
**Principles served:** 1, 2, 4, 7, 8, 10, 11, 13, 14, 15, 16, 17, 18
**Parts:** 18 across 6 sections, plus 1 paper

> `./m done 36` refuses to commit while any box below is unticked. It cannot tell whether you were
> honest — that part is yours.

## Demo command

```bash
curl -sL https://modelcontextprotocol.io/specification/versioning | grep -o "specification/2026-07-28" | head -1
curl -s https://modelcontextprotocol.io/extensions/tasks/overview | grep -o "cancellation is cooperative" | head -1
uv run python days/day-36-long-jobs-and-tasks/lab/blocking.py
uv run python days/day-36-long-jobs-and-tasks/lab/timeout_ladder.py
uv run python days/day-36-long-jobs-and-tasks/lab/no_name.py
uv run python days/day-36-long-jobs-and-tasks/lab/progress.py
uv run python days/day-36-long-jobs-and-tasks/lab/tickets.py
uv run python days/day-36-long-jobs-and-tasks/lab/tenancy.py; echo "exit: $?"
uv run python days/day-36-long-jobs-and-tasks/lab/policy.py; echo "exit: $?"
uv run python days/day-36-long-jobs-and-tasks/lab/wire_shapes.py
uv run python days/day-36-long-jobs-and-tasks/lab/poll.py
uv run python days/day-36-long-jobs-and-tasks/lab/sdk_tasks.py
CHECKPOINTS=1 uv run python days/day-36-long-jobs-and-tasks/lab/cancel.py
CHECKPOINTS=0 uv run python days/day-36-long-jobs-and-tasks/lab/cancel.py
uv run python days/day-36-long-jobs-and-tasks/lab/reaper.py
uv run python days/day-36-long-jobs-and-tasks/lab/idempotency.py
cd days/day-36-long-jobs-and-tasks/lab/papers/promises
PROMISES=0 uv run python run.py
PROMISES=1 uv run python run.py
cd -
./m depth 36 && ./m check && ./m trace && git log --oneline -1
```

Expected: `specification/2026-07-28`, then `cancellation is cooperative`; then a client giving up at
`0.51s` while the server finishes at `1.21s` and discards the answer; then the ladder failing at the
client and then at the proxy; then `jobs started : 2`; then **4 notifications** and then **0**; then a
handle minted in `0.002s` and redeemed by `i2` and `i3`; then `tasks reachable : 10 of 10` and
`exit: 1`; then `findings: 2` and `exit: 1`; then four JSON messages and six transition decisions; then
`2101 / 211 / 18` requests; then `mcp version : 1.29.1` with `tasks/update in this SDK: False` and the
deprecation warning; then `cancelled` with `2 of 8` and `completed` with `8 of 8`; then a reaper that
says `working` and later `failed`; then `jobs running : 2` and `jobs running : 1`; then **`1.20s`**
against **`0.40s`**. Then `OK day 36 18 parts + 1 papers`, `./m check` green, a traceability line with
`0 problem(s)`, and one commit.

## Setup

- [ ] `./m brief 36` read, and the three IDs confirmed as MCP-10, MCP-14, MCP-28
- [ ] **Both freshness gates run first** — the versioning page still names **2026-07-28**, and the Tasks
      extension page still says cancellation is cooperative. If either had moved, you stopped and
      amended the plan (Principle 14)
- [ ] **No `uv add` and no `uv sync --upgrade` was run** — `git diff pyproject.toml uv.lock` is empty
- [ ] Day 32 part 3.4 re-read, so today's handle policy is the answer to a question you already have

## Section 1 — `01-the-blocking-call`

- [ ] **1.1** read · ran `blocking.py` and saw the server finish **after** the client gave up · raised
      `CLIENT_DEADLINE_S` to win, then raised `CHUNKS` and lost again · named the three different things
      a timeout can mean
- [ ] **1.2** read · ran `timeout_ladder.py` both ways · **added a fifth rung with a smaller patience
      and watched a safe job become unsafe** · wrote down which rung you actually control
- [ ] **1.3** read · ran `no_name.py` · **tried to write a line inside `server_call` that refuses the
      duplicate, and worked out why you cannot** · said what a JSON-RPC request id names

## Section 2 — `02-progress`

- [ ] **2.1** read · ran `progress.py` · **moved `_meta` out of `params` and watched the notifications
      vanish with no error** · put it back · said who chooses the progress token
- [ ] **2.2** read · **opened `.venv/Lib/site-packages/mcp/server/fastmcp/server.py` and read
      `report_progress` yourself**, including the `# pragma: no cover` · confirmed in the `Context`
      docstring that the parameter name is free and the annotation is not
- [ ] **2.3** read · **deleted the `delivered.clear()` and watched the second arm report notifications it
      never produced** · put it back · said the one question a handle answers and progress cannot

## Section 3 — `03-the-handle`

- [ ] **3.1** read · ran `tickets.py` and saw `i3` — created after the job began — serve a poll ·
      **moved `store.put` below the thread start, polled immediately, and got `unknown task`** · put it
      back
- [ ] **3.2** read · ran `tenancy.py` and saw **`10 of 10`** reachable from fifteen guesses ·
      **set `check_owner=True` on the first probe and watched the leak close** · said what it did *not*
      close
- [ ] **3.3** read · ran `policy.py` and got `findings: 2`, `exit: 1` · **implemented rules 2 and 3 and
      got it to `findings: 0`** · set `HANDLE_BYTES = 8` and watched rule 1 appear with the real entropy
- [ ] **Sutra's handle policy written down** — generation, ownership, the two TTL values with the
      reasoning behind them, the unknown-handle error code, and the identical-message rule

## Section 4 — `04-the-tasks-extension`

- [ ] **4.1** read · ran `wire_shapes.py` · **misspelt `EXT` and confirmed the request is still valid
      and declares nothing** · named the four messages in order and who decides a call becomes a task
- [ ] **4.2** read · **added `("completed", "completed")` to the transitions and watched it refused** ·
      said what the correct way to retry a failed task is
- [ ] **4.3** read · ran `poll.py` and saw **2101 / 211 / 18** · raised `CAP_MS` above the job and saw
      the final gap exceed the job · said which server-supplied number the cap must stay under
- [ ] **4.4** read · ran `sdk_tasks.py` · **saw `tasks/result` and `tasks/list` present and
      `tasks/update` absent**, and the fields spelt `ttl` and `pollInterval` · read the deprecation
      warning · **did not change the pin**
- [ ] The runnable / spec-only table in §8 checked against your own `sdk_tasks.py` output

## Section 5 — `05-cancellation`

- [ ] **5.1** read · ran the `CHECKPOINTS=1` arm · **compared the acknowledgement with the final
      status** · made the client wait longer than the job and got the terminal-state refusal
- [ ] **5.2** read · ran **both** arms · **confirmed the acknowledgement line is identical in both** ·
      moved the check after the `done` increment and watched `statusMessage` change · moved it outside
      the loop and watched cancellation stop working entirely

## Section 6 — `06-in-production`

- [ ] **6.1** read · ran `reaper.py` and saw the row still say `working` after the worker was gone ·
      **set `LEASE_S = 0.01` and watched a healthy worker be reaped** · put it back · **removed the
      terminal guard and watched a completed job be marked failed**
- [ ] **6.2** read · ran `idempotency.py` and saw `jobs running : 2` against `1` · **replayed the same
      key with a different archive and decided out loud whether the server should have refused**
- [ ] **6.3** read · **mapped all eight store obligations to methods on `TaskStore`** · found the one
      that maps to none · said which component cannot be scaled by adding a copy

## The build

- [ ] `sutra_mcp/tasks.py` written with `start_task`, `get_task` and `cancel_task`
- [ ] The task row is written **before** `start_task` returns, and you can say why
- [ ] The handle is `secrets.token_urlsafe(16)` with a `tsk_` prefix, never a counter
- [ ] Every read filters on the owner, and not-found and not-yours return the identical error
- [ ] `cancel_task` records an intent and does **not** write `cancelled` itself
- [ ] Registered into the server `build_server()` returns, without duplicating anything Day 34 owns
- [ ] Every `TODO(me)` in §4 either done or written down as a decision with its reasoning

## The paper

- [ ] `papers/01-promises.md` read **after** the parts, not before
- [ ] Both arms of the demo run, and **your own** `1.20s` / `0.40s` compared with the transcript
- [ ] The `claim` moved inside the loop, the wall clock seen to go back to the blocking arm's number,
      and then reverted
- [ ] Said out loud which half of the paper is in every language today and which half the field dropped
- [ ] Said the one property a task handle has that an in-process promise does not

## The eval

- [ ] `policy.py` printed `findings: 2` and `exit: 1` **before** you implemented anything
- [ ] `tenancy.py` printed `10 of 10` and `exit: 1` before you fixed anything
- [ ] The cancellation ablation was run **both ways** and the two acknowledgements compared
- [ ] The paper demo was run **both ways** and the two wall clocks recorded
- [ ] At least three of the named breaks were performed on purpose and reverted

## The budget

- [ ] Total generations spent: **0 of 20**
- [ ] No `GOOGLE_API_KEY` was needed by anything in this day
- [ ] The only network traffic was two HTTPS GETs to the specification site, both freshness gates

## The ledger

- [ ] `docs/PROGRESS.md` row pasted from §11, with the real date and hash
- [ ] `docs/PACKAGES.md` — **no new row**; the SDK finding is recorded in §8 and taught in 4.4
- [ ] `docs/PAPERS.md` — **no new row**; `doi:10.1145/53990.54016` already has its dated row
- [ ] `docs/SKILL_PROVENANCE.md` — **no new row**
- [ ] `./m depth 36` green · `./m check` green · `./m trace` prints `0 problem(s)`
- [ ] `git status` shows no `.env`; commit message is the one in §11
