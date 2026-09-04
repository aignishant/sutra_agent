# Day 35 — CHECKLIST

**IDs closed:** MCP-07, MCP-08, MCP-09
**Principles served:** 1, 2, 4, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18
**Parts:** 19 across 6 sections, no paper part

> `./m done 35` refuses to commit while any box below is unticked. It cannot tell whether you were
> honest — that part is yours.

## Demo command

```bash
curl -sL https://modelcontextprotocol.io/specification/versioning | grep -o "2026-07-28" | head -1
uv run python days/day-35-resources-and-prompts/lab/surface.py
uv run python days/day-35-resources-and-prompts/lab/decision_cost.py
cd days/day-35-resources-and-prompts/lab
uv run python read_shelf.py
SHELF=shelf_strict.py uv run python read_shelf.py
uv run python card_probe.py
SHELF=shelf_strict.py uv run python card_probe.py
cd -
uv run python days/day-35-resources-and-prompts/lab/template_match.py
uv run python days/day-35-resources-and-prompts/lab/linked_card.py
uv run python days/day-35-resources-and-prompts/lab/cache_hint.py;    echo "exit: $?"
uv run python days/day-35-resources-and-prompts/lab/subscribe_probe.py
uv run python days/day-35-resources-and-prompts/lab/stale_list.py
uv run python days/day-35-resources-and-prompts/lab/traversal.py;     echo "exit: $?"
STRICT=1 uv run python days/day-35-resources-and-prompts/lab/traversal.py; echo "exit: $?"
uv run python days/day-35-resources-and-prompts/lab/context_cost.py;  echo "exit: $?"
uv run python days/day-35-resources-and-prompts/lab/injection.py;     echo "exit: $?"
uv run python days/day-35-resources-and-prompts/lab/shelf_audit.py;   echo "exit: $?"
./m depth 35 && ./m check && ./m trace && git log --oneline -1
```

Expected: `2026-07-28`; then four resources, two tools and one prompt; then **12** decisions and
**3.0** lost turns against **0** and **0.0**; then the same six exchanges twice, differing on one line
— `code=0` against `code=-32602`; then three `code=0` rows against two `-32602` rows and one
`NO ERROR`; then `ticket://4521/history` and `doc://../../.env` not matching while
`doc://..%2F..%2F.env` does; then **244** bytes against **205**; then
`missing required caching fields: 12` and `exit: 1`; then `SubscriptionsListenRequest … NO`; then
**1920** against **80**; then `reads that escaped the published root: 2` / `exit: 1` and then `0` /
`exit: 0`; then `703.1%  NO` and `exit: 1`; then `unsafe renderings: 1` and `exit: 1`; then the audit's
findings and `exit: 0` once both modules are written. Then `OK day 35 19 parts`, `OK all green`, a
traceability line with `0 problem(s)`, and one commit.

## Setup

- [ ] `./m brief 35` read, and the three IDs confirmed as MCP-07, MCP-08, MCP-09
- [ ] **The specification freshness gate was run first** and
      `modelcontextprotocol.io/specification/versioning` still names **2026-07-28** as current — if it
      had moved, you stopped and amended (Principle 14)
- [ ] **No `uv add` and no `uv sync --upgrade` was run** — `git diff pyproject.toml uv.lock` is empty
- [ ] `sutra_mcp/server.py` and `sutra_mcp/tools.py` are Day 34's and were **not edited**
- [ ] Nothing under `sutra/` changed

## Section 1 — `01-who-initiates`

- [ ] **1.1** read · ran `surface.py` · **added one row to `CANDIDATES` for a capability Sutra does not
      have yet and saw which door the rule sent it through** · said out loud why `search_kb` is
      correctly a tool despite being read-only
- [ ] **1.2** read · ran `decision_cost.py` · **changed `MISS_RATE` to the smallest number you would
      honestly defend** and said what evidence would settle it · said what a model does when it forgets
      to call a tool
- [ ] **1.3** read · answered Day 32's open question **in writing**, with the cost as well as the
      benefit · listed the three things that now exist twice · **named the one a shared reader does not
      fix**

## Section 2 — `02-the-shelf`

- [ ] **2.1** read · ran `read_shelf.py` and read the `resources/list` line field by field · **said
      which fields a program needs and which exist only for a person** · stated what
      `MUST NOT vary per-connection` forbids and its one exception
- [ ] **2.2** read · saw `contents is a list of 1` · **changed `archive_summary` to return `bytes` and
      re-read it**, then said which field changed and what your reading code would have done
- [ ] **2.3** read · ran **both** shelves and put the two `(the miss)` lines side by side · **changed
      `not_found` in `shelf_strict.py` to raise a plain `ValueError` and recreated the `code=0`
      transcript** · said why an empty `contents` array is forbidden
- [ ] **2.4** read · ran `template_match.py` · **added the `"ticket://45 21"` case and predicted the
      answer before running it** · said which list a template appears in and named one address it
      promises that the server does not hold

## Section 3 — `03-the-card`

- [ ] **3.1** read · read `prompts/list` beside `resources/list` and said which a person picks from ·
      **said who authors a prompt's content and who decides when it is used** · explained why naming a
      tool inside a prompt is a hope
- [ ] **3.2** read · ran `card_probe.py` **both ways** and compared row by row · **added the
      `{"ticket_id": ""}` case and predicted each server's answer first** · named the one thing about
      an argument the protocol cannot describe
- [ ] **3.3** read · saw `role=user type=text` and the argument woven in · **changed `triage_ticket` to
      return two messages and re-ran it**, then said what an indexing client would have missed · named
      the role that does not exist and what that costs
- [ ] **3.4** read · ran `linked_card.py` and read **244 against 205** · **pasted a realistic long
      ticket into `TICKET_TEXT` and re-ran it** · said at roughly what size the link becomes obviously
      right, and what a host that ignores links hands the model

## Section 4 — `04-freshness`

- [ ] **4.1** read · ran `cache_hint.py` and got `12` and `exit: 1` · **added `resources/subscribe` to
      `REQUIRED_ON` and explained why that row is not a finding** · said what
      `cacheScope: "private"` forbids in terms of tokens, and what a client assumes when `ttlMs` is
      absent
- [ ] **4.2** read · ran `subscribe_probe.py` and saw the SDK has the 2025 mechanism and not the 2026
      one · **changed `WATCHERS` to 4000 and read the three rows again** · **wrote down, in one
      paragraph, whether `sutra-mcp` declares `subscribe` and why** · said what a client must do after
      a stdio reconnect
- [ ] **4.3** read · ran `stale_list.py` and read **1920 against 80** · **changed `CLIENTS` to 400 and
      read the one-day row** · chose the `ttlMs` for `resources/list` and **wrote the removal procedure
      into the deploy notes** · said why a `-32602` burst after a deploy is not a client bug

## Section 5 — `05-failure-lab`

- [ ] **5.1** read · ran **both** arms and saw `2` escapes become `0` · **added the double-encoded
      `"doc://..%252Fsecret.env"` case and predicted both handlers before running** · said why blocking
      the characters `..` is not a fix
- [ ] **5.2** read · ran `context_cost.py` and saw `703.1%  NO` · **added an `archive://open` design and
      saw which side of the line it landed on** · said why a design that fits can be worse than one
      that does not
- [ ] **5.3** read · ran `injection.py` and read the naive rendering of the hostile argument line by
      line · **changed `re.fullmatch` to `re.match` and watched the count go up** · said why stripping
      newlines is not a fix

## Section 6 — `06-in-production`

- [ ] **6.1** read · ran `shelf_audit.py` and said which day the finding belongs to · **said why
      `load_server()` collects findings instead of raising** · stated what importing
      `sutra_mcp/resources.py` should do
- [ ] **6.2** read · **removed `mime_type` from `archive_summary`, re-ran `read_shelf.py`, and said
      whether a host could tell your choice from the SDK's default** · named the three annotation
      fields and which one a host uses to decide what to drop

## The build

- [ ] `sutra_mcp/resources.py` and `sutra_mcp/prompts.py` exist and **you typed every line**
- [ ] Both expose exactly one public function taking the server — `register_resources(server)` and
      `register_prompts(server)` — and **importing either module has no side effects**
- [ ] Neither imports `sutra_mcp.server`, and the assembly happens in one place
- [ ] Both doors onto the ticket store go through **one** shared reader, with the comment saying why
      the two miss paths differ
- [ ] A resource miss raises `McpError` with `INVALID_PARAMS`; there is **no** polite sentence and
      **no** empty `contents` anywhere on the resource surface
- [ ] Every resource, template and prompt carries `title`, `description`, `mime_type` and
      `annotations`, and the prompt's argument has a description with an example in it
- [ ] The `ticket_id` argument is validated with an **anchored** pattern, and a bad one is refused
      rather than stripped
- [ ] The `TODO(me)` markers in §4 are still `TODO(me)` — none of them was quietly solved for you

## The eval

- [ ] `shelf_audit.py` was **red first**, and you watched the finding change as each piece arrived
- [ ] The error-code ablation was run **both ways** and the two `(the miss)` lines recorded
- [ ] The traversal ablation was run **both ways**: `2` escapes and `exit: 1`, then `0` and `exit: 0`
- [ ] `injection.py` exited **1** on the naive template, and you can say what the fenced arm did instead
- [ ] `cache_hint.py` exited **1**, and you understand that this red belongs to the pin and is not
      yours to fix today
- [ ] At least three of the named breaks were performed on purpose and reverted

## The budget

- [ ] Total generations spent: **0 of 20**
- [ ] No `GOOGLE_API_KEY` was needed by anything in this day
- [ ] The only network traffic was one HTTPS GET to the specification site (and optionally PyPI); every
      server in the lab was a child process on this machine

## The ledger

- [ ] `docs/PROGRESS.md` row pasted from §11, with the real date and hash
- [ ] `docs/PACKAGES.md` — **no new row**; nothing was installed and nothing upgraded
- [ ] `docs/PAPERS.md` — **no new row**; both identifiers already have theirs and are taught on Days 19
      and 32
- [ ] `docs/SKILL_PROVENANCE.md` — **no new row**
- [ ] `./m depth 35` green · `./m check` green · `./m trace` prints `0 problem(s)`
- [ ] `git status` shows no `.env`; commit message is the one in §11
