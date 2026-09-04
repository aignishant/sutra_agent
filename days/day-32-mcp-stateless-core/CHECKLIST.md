# Day 32 — CHECKLIST

**IDs closed:** MCP-01, MCP-26, MCP-32
**Principles served:** 1, 2, 4, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18
**Parts:** 20 across 6 sections, plus 1 paper

> `./m done 32` refuses to commit while any box below is unticked. It cannot tell whether you were
> honest — that part is yours.

## Demo command

```bash
curl -s https://modelcontextprotocol.io/specification/versioning | grep -o "specification/2026-07-28" | head -1
uv run python days/day-32-mcp-stateless-core/lab/boundary_check.py
uv run python days/day-32-mcp-stateless-core/lab/letter.py
uv run python days/day-32-mcp-stateless-core/lab/discover_cost.py
uv run python days/day-32-mcp-stateless-core/lab/headers.py
uv run python days/day-32-mcp-stateless-core/lab/cache_math.py
uv run python days/day-32-mcp-stateless-core/lab/handles.py
uv run python days/day-32-mcp-stateless-core/lab/sdk_era.py
uv run python days/day-32-mcp-stateless-core/lab/gateway.py
uv run python days/day-32-mcp-stateless-core/lab/registry.py
uv run python days/day-32-mcp-stateless-core/lab/server_intake.py; echo "exit: $?"
cd days/day-32-mcp-stateless-core/lab && uv run python forge.py && cd -
cd days/day-32-mcp-stateless-core/lab/papers/modern-web-architecture
STATELESS=1 uv run python client.py
STATELESS=0 uv run python client.py
cd -
./m depth 32 && ./m check && ./m trace && git log --oneline -1
```

Expected: `specification/2026-07-28`; then `none`; then two eras with `self_contained` `False` then
`True` and **184** bytes; then a table where probing costs one extra request in three rows out of four;
then three derived headers, `validate(honest) -> None`, and two `-32020` bodies; then **60 → 3 → 1**
and two different hashes; then three refusals against three accumulations; then
`SDK speaks the current revision : False` with `LATEST_PROTOCOL_VERSION : 2025-11-25`; then six gateway
decisions and `bodies parsed by the gateway: 0`; then five real registry entries; then `findings: 3`
and `exit: 1`; then the forged header rejected; then **`served 4/4`** against **`served 2/4`**. Then
`OK day 32 20 parts + 1 papers`, `OK all green`, a traceability line with `0 problem(s)`, and one
commit.

## Setup

- [ ] `./m brief 32` read, and the three IDs confirmed as MCP-01, MCP-26, MCP-32
- [ ] **The specification freshness gate was run first** and `modelcontextprotocol.io/specification`
      still names **2026-07-28** as current — if it had moved, you stopped and amended (Principle 14)
- [ ] **No `uv add` and no `uv sync --upgrade` was run** — `git diff pyproject.toml uv.lock` is empty
- [ ] `sutra/` and `sutra_mcp/` are untouched; `sutra_mcp/__init__.py` is still empty

## Section 1 — `01-the-socket`

- [ ] **1.1** read · ran the `TOOLS` command and named what is trapped in one process · read the
      example `tools/call` and **named every one of the five parts of it out loud**
- [ ] **1.2** read · drew the host / client / server picture from memory · said how many clients a host
      with four servers has, and why the model has no arrow to any server
- [ ] **1.3** read · classified both of Sutra's tools as tool / resource / prompt and **wrote down the
      cost of changing each**, not just the benefit
- [ ] **1.4** read · pasted the ten-line fixed-vocabulary demo into a file, ran it, **added a third
      server dict and confirmed `use` needed no edit**
- [ ] **1.5** read · wrote `boundary_check.py` and ran it green · **added `import sqlite3` under
      `sutra/`, watched the offender appear, and took it out** · decided what else belongs in
      `FORBIDDEN`

## Section 2 — `02-the-reframe`

- [ ] **2.1** read · listed the four messages the old protocol spent before the first useful one ·
      said what the server had to remember afterwards
- [ ] **2.2** read · ran both arms of the paper demo and **saw `4/4` against `2/4`** · set `PORTS` to a
      single port, watched the stateful arm pass, and put the three back
- [ ] **2.3** read · ran `letter.py` · **deleted `_meta` from `NEW_CALL`, saw `self_contained: False`,
      and put it back** · named the three keys and which one is only a SHOULD
- [ ] **2.4** read · ran `discover_cost.py` · **wrote down what Sutra's client will do on stdio and
      what it will do over HTTP**, and where the answer is cached

## Section 3 — `03-headers-and-caches`

- [ ] **3.1** read · wrote `derive` · **changed the method to `tools/list` and confirmed `Mcp-Name`
      disappears rather than becoming empty** · named where each header is copied from
- [ ] **3.2** read · wrote `validate` and `error` · ran all three outcomes · **lower-cased the header
      values, watched `Tools/Call` pass, and put it back**
- [ ] **3.3** read · ran `cache_math.py` and saw **60 → 3 → 1** · saw the two hashes differ · chose the
      `ttlMs` and `cacheScope` `sutra_mcp` will return on Day 34
- [ ] **3.4** read · ran `handles.py` · **added a fourth worker created after the handle was minted and
      watched it serve** · wrote down Sutra's handle expiry and ownership policy

## Section 4 — `04-governance-and-registry`

- [ ] **4.1** read · opened the versioning page yourself and confirmed the current revision · **found
      one SEP number in this day and read what it proposed**
- [ ] **4.2** read · ran `registry.py` and got real entries · **ran it against a misspelt path and read
      the HTTP 404 body** · noticed the same server name appearing at several versions
- [ ] **4.3** read · reversed one namespace into a domain and **checked whether the `remotes` URL lives
      there** · wrote the provenance row for one candidate server

## Section 5 — `05-failure-lab`

- [ ] **5.1** read · ran `sdk_era.py` and **saw `SDK speaks the current revision : False`** · ran both
      live lookups and saw `2.1.1` and `("2026-07-28",)` · **did not change the pin**
- [ ] **5.2** read · ran `forge.py` and got `-32020` · **made `validate` return `None`, watched the
      forgery pass, and put it back** · said who the forgery actually attacks

## Section 6 — `06-in-production`

- [ ] **6.1** read · ran `gateway.py` · **removed the version check and watched a `2025-11-25` request
      get routed** · put it back · decided real `LIMITS` for Sutra's two tools
- [ ] **6.2** read · ran `server_intake.py` and got `findings: 3`, `exit: 1` · **filled the two blanks
      and the `isLatest` flag and watched it go green** · then removed the namespace from the allowlist

## The paper

- [ ] `papers/01-modern-web-architecture.md` read **after** the parts, not before
- [ ] The six constraints named out loud, each with the property it buys **and the price it charges**
- [ ] Both arms of the demo run, and **your own** output compared with the transcript in the part
- [ ] `PORTS = (8801,)` tried, `4/4` seen in the stateful arm, and the three ports restored
- [ ] Said out loud which half of the paper the industry dropped, and what MCP uses instead of it
- [ ] Noted why `doi:10.1145/337180.337228` is **not** the version to cite

## The eval

- [ ] `server_intake.py` printed `findings: 3` and `exit: 1` before you filled anything in
- [ ] `sdk_era.py` printed `False` against the pinned SDK, and you understand why that is a Day 34
      problem and not a Day 32 fix
- [ ] The paper demo was run **both ways** and the two served-counts recorded
- [ ] At least three of the named breaks were performed on purpose and reverted

## The budget

- [ ] Total generations spent: **0 of 20**
- [ ] No `GOOGLE_API_KEY` was needed by anything in this day
- [ ] The only network traffic was HTTPS GETs to the specification site, the registry, PyPI and a raw
      GitHub file — plus three servers on `127.0.0.1`

## The ledger

- [ ] `docs/PROGRESS.md` row pasted from §11, with the real date and hash
- [ ] `docs/PACKAGES.md` — **no new row**; the `mcp` 2.1.1 finding is recorded in §8, not in the ledger
- [ ] `docs/PAPERS.md` — **no new row**; both DOIs already have theirs
- [ ] `docs/SKILL_PROVENANCE.md` — **no new row**
- [ ] `./m depth 32` green · `./m check` green · `./m trace` prints `0 problem(s)`
- [ ] `git status` shows no `.env`; commit message is the one in §11
