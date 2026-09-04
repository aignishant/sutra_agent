# Day 43 — CHECKLIST

**IDs closed:** MCP-20, MCP-21
**Principles served:** 1, 2, 4, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18
**Parts:** 19 across 6 sections, no paper part

> `./m done 43` refuses to commit while any box below is unticked. It cannot tell whether you were
> honest — that part is yours.

## Demo command

```bash
curl -sL https://modelcontextprotocol.io/specification/versioning | grep -o "specification/2026-07-28" | head -1
uv run python days/day-43-stateless-by-default/lab/scan.py sutra sutra_mcp; echo "exit: $?"
uv run python days/day-43-stateless-by-default/lab/scan.py days/day-43-stateless-by-default/lab/shapes.py; echo "exit: $?"
cd days/day-43-stateless-by-default/lab
uv run python deploy_shape.py
uv run python twoup.py; echo "exit: $?"
uv run python twoup.py --shared; echo "exit: $?"
uv run python twoup.py --pinned; echo "exit: $?"
uv run python twoup.py --stateful; echo "exit: $?"
uv run python race.py --unsafe; echo "exit: $?"
uv run python race.py; echo "exit: $?"
uv run python health.py; echo "exit: $?"
uv run python health.py --shared; echo "exit: $?"
cd -
./m depth 43 && ./m check && ./m trace && git log --oneline -1
```

Expected: `specification/2026-07-28`; then six findings in `sutra/` and none in `sutra_mcp/` with
`exit: 1`, then five findings from `shapes.py` with `exit: 1`; then `manager.stateless : True` and
`False` from two objects built in one process; then `behaviours that did not survive: 3` and
`exit: 1`, then `0` and `exit: 0`, then `0` and `exit: 0` **on the same broken server** because the
caller was pinned, then a `404` carrying `Session not found`; then `counter says: 30` against
`counter says: 100`; then two identical `liveness` blocks with `exit: 1` and `exit: 0`. Then
`OK day 43 19 parts`, `./m check` green, a traceability line with `0 problem(s)`, and one commit.

## Setup

- [ ] `./m brief 43` read, and the two IDs confirmed as MCP-20, MCP-21
- [ ] **The specification freshness gate was run first**, with `curl -sL`, and
      `modelcontextprotocol.io/specification/versioning` still names **2026-07-28** as current — if it
      had moved, you stopped and amended (Principle 14)
- [ ] You ran the same command **without** `-L`, saw it print nothing, and understood why a gate that
      fails silently is worse than one that fails loudly
- [ ] **No `uv add` and no `uv sync --upgrade` was run** — `git diff pyproject.toml uv.lock` is empty
- [ ] You know that `uvicorn` and `starlette` are installed only because `mcp==1.29.1` requires them,
      and you can say why today does not pin them directly
- [ ] Nothing outside `days/day-43-stateless-by-default/` and `sutra_mcp/app.py` was touched

## Section 1 — `01-accidental-state`

- [ ] **1.1** read · ran `twoup.py` · **found the three lines under `-- the handle --` and said what
      happened to Line 2** · explained a module-level dictionary without using the word "state"
- [ ] **1.2** read · ran `twoup.py` and `twoup.py --shared` · **named the one line that changes
      between the two cache blocks** · said the difference between a *stale* cache and *inconsistent*
      caches and which one an expiry fixes
- [ ] **1.3** read · moved `store.py`'s `sqlite3.connect` to module level, ran the scan, read the
      finding, and put it back · **named three pieces of per-instance state that hold no data** ·
      said which of them fails with a message and which fail in silence
- [ ] **1.4** read · ran `deploy_shape.py` and `twoup.py --stateful` · **said which line of
      `deploy_shape.py`'s output predicts the 404** · found `_server_instances` in the installed SDK
      yourself and said why the scan can never see it

## Section 2 — `02-finding-the-state`

- [ ] **2.1** read · ran `scan.py scan.py` and got zero · **said why every constant in it is a
      `frozenset` or a tuple** · changed one to a plain set, watched it fire, and put it back
- [ ] **2.2** read · ran `scan.py shapes.py` and got five findings from four shapes · **said why
      `SEEN` is reported twice and why that is not a duplicate** · confirmed lines 26 and 27 of
      `shapes.py` are silent · named the four shapes and which one is evidence of intent
- [ ] **2.3** read · deleted the reason after `stateless-ok:` in `dispatcher.py`, watched the finding
      return, and restored it · **said which of `dispatcher.py`'s two original findings was fixed
      rather than waived, and why that was right for that line and not the other**
- [ ] **2.4** read · ran the scan over `sutra` and `sutra_mcp` and got six findings and a zero ·
      **said out loud what that zero actually proves** · said why `return len(findings)` is a bug

## Section 3 — `03-two-instances`

- [ ] **3.1** read · started `dispatcher.py` alone and watched it fail to reach a backend ·
      **named the two request headers that must not be forwarded and why** · said what the balancer
      needs to know about MCP (nothing)
- [ ] **3.2** read · ran both arms · **said why the probe compares answers instead of counting
      errors** · named the one behaviour of four that survived · found the line that sets the exit
      code · said why the probe sends `2025-11-25` and not `2026-07-28`
- [ ] **3.3** read · **found the two consecutive `lookup` lines that disagree** · said why
      "invalidate the cache on write" is not available at this design · named four things this
      failure does not produce that monitoring would have caught
- [ ] **3.4** read · read the `spent` column downwards in both arms · **said what a limit of twenty
      means on four instances and why dividing by four is not the fix** · changed `QUOTA_LIMIT` to 1
      and predicted both arms before running
- [ ] **3.5** read · ran all three handle blocks · **said what an opaque handle does and does not
      guarantee** · gave the one-glance tell that a handle's data is stuck on one instance · said
      which of the three failures a JSON-RPC error dashboard would have shown

## Section 4 — `04-where-state-goes`

- [ ] **4.1** read · ran `scan.py store.py` and got zero · **placed a task record, the protocol
      version, a spend counter and a summary cache into the three destinations** · found the column
      the `drafts` table is missing
- [ ] **4.2** read · ran `race.py` **both ways** and recorded `30` against `100` · **changed
      `BEGIN IMMEDIATE` to `BEGIN`, watched three workers die with `database is locked`, and said
      why** · then put it back · said which of `BEGIN` and `BEGIN IMMEDIATE` prevents a lost update

## Section 5 — `05-deploy-shape`

- [ ] **5.1** read · ran `deploy_shape.py` and the ASGI server against `leaky_server:app` ·
      **named the two uvicorn log lines that correspond to the lifespan** · said what `app.py`
      exports, what it must not contain, and where the port comes from
- [ ] **5.2** read · ran the server on `127.0.0.1` and then on `0.0.0.0` · **said which host is wrong
      in which environment and why neither is a code change** · named the five things a container
      platform requires · **confirmed no deploy command was run and no billing account exists**

## Section 6 — `06-in-production`

- [ ] **6.1** read · ran `health.py` **both ways** · **compared the two `liveness` blocks and
      confirmed they are identical** · said the difference between liveness and readiness · named one
      dependency that must not be in a readiness check
- [ ] **6.2** read · ran `twoup.py --pinned` on the broken server and got zero failures ·
      **said what the pinned run's cache answered after the status changed** · named the four moments
      at which affinity stops holding · wrote Sutra's position on affinity as three sentences

## The build

- [ ] `sutra_mcp/app.py` exists and **you typed every line**
- [ ] It exports exactly one public name, `app`, built from `build_server()`
- [ ] There is **no `if __name__ == "__main__":` block** and no `run()` call in it
- [ ] Nothing in it reads `sys.argv`; the port and bind address come from the environment
- [ ] The transport assertion is written, and you decided **where** the flag is read from and why
- [ ] `uv run python -c "import sutra_mcp.app"` returns rather than blocking
- [ ] The `TODO(me)` markers in §4 are still `TODO(me)` — none of them was quietly solved for you

## The eval

- [ ] The scan was **red first**, on `sutra/`, before you trusted it anywhere
- [ ] The two-instance probe was run in **all four arms** and every output recorded
- [ ] The `--pinned` arm was run and you wrote down why a passing run there is a warning
- [ ] The lost-update ablation was run **both ways** and the numbers recorded
- [ ] The health ablation was run **both ways** and the identical liveness blocks noted
- [ ] At least three of the named breaks were performed on purpose and reverted
- [ ] You pointed `twoup.py` at your own `sutra_mcp` package and recorded which behaviours survived

## The budget

- [ ] Total generations spent: **0 of 20**
- [ ] No `GOOGLE_API_KEY` was needed by anything in this day
- [ ] The only traffic leaving your machine was the HTTPS GETs in §3 and §8

## The ledger

- [ ] `docs/PROGRESS.md` row pasted from §11, with the real hash
- [ ] `docs/PACKAGES.md` — **no new row**; nothing installed, nothing upgraded, and the deferred
      `uvicorn` / `starlette` rows left in §11 for the day that builds a container
- [ ] `docs/PAPERS.md` — **no new row**; `doi:10.1145/514183.514185` already has its row and is
      taught on Day 32
- [ ] `docs/SKILL_PROVENANCE.md` — **no new row**
- [ ] `./m depth 43` green · `./m check` green · `./m trace` prints `0 problem(s)`
- [ ] `git status` shows no `.env`, no `lab/*.sqlite3` and no `__pycache__`; commit message is the one
      in §11
