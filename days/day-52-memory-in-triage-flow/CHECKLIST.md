# Day 52 — Definition of done

`./m done 52` refuses to commit until every box is ticked. Tick a box only when you have actually run
the thing, not when you have read it. This is a **gate day**: a box you tick without running is
exactly the failure the day is about.

## Before you start

- [ ] Day 51's parts and checklist are done, and `days/day-51-caching-the-quota-lifeline/LESSON.md`
      exists. Until it does, `lab/ids.py` reports `ADK-31` and `OPS-10` open and Phase 7 cannot be
      green (P2).
- [ ] `uv run python days/day-52-memory-in-triage-flow/lab/gate.py; echo "exit: $?"` is **red**
      before you write anything, and you have read all **six** findings rather than only counted
      them.
- [ ] `lab/` scaffolded per §3 — twenty-two files, two of them copied from Day 50's lab.
- [ ] `git diff pyproject.toml uv.lock` is empty and stays empty. No package is added today.
- [ ] `tests/test_memory_flow.py` created empty, so `G11` has something to point at.

## Section 1 — the promise

- [ ] **1.1** read · ran `endtoend.py` and `endtoend.py --archive-only` · saw **65 rows against 61**
      and the top answer change from `memo:7101` at **0.439** to `ticket:4521` at **0.415** · found
      the control question whose score moved from **0.236 to 0.233** and can say why · can state the
      sentence Phase 7 exists to answer
- [ ] **1.2** read · ran `gate.py` from the repository root · counted **6 findings, exit 1** · picked
      the two findings that are not missing modules and decided **fixed** or **filed** for each ·
      can give the three results a criterion can have and say which one gets deleted

## Section 2 — the run

- [ ] **2.1** read · ran both arms · wrote G01 down as a sentence containing **0.439** and **0.345** ·
      found a `GOLD` question in `_archive.py` that would make a **bad** G01 and can say in one line
      why · can explain what a passing criterion proves if it passes with the feature removed
- [ ] **2.2** read · ran `cite.py` and `cite.py --strip` · split
      `memo:7101:resolution:signed-out-of-the-dashboard` into its four fields and said what each is
      for · can name the field that exists only because a correction and the fact it corrects come
      from one conversation · can state the difference between *checkable* and *grounded*

## Section 3 — the write path

- [ ] **3.1** read · ran `filed.py` and `filed.py --no-write` · saw **6 proposed = 5 kept + 1
      refused**, and **4 live** · saw the store-less run report **61 index rows against 65** · can
      say why `case:7115` was refused and why `memo:7108:account_fact:billing-account` was not live,
      and that those are different kinds of absence
- [ ] **3.2** read · ran `ruled.py` and `ruled.py --unruled` · saw `rows with no reason []` become
      `['hunch']` and the refused guess become a stored memo · wrote a better `why` for the
      `account_fact` row that names what **400 days** was sized against · can say why `authority`
      exists when memos already carry a date
- [ ] **3.3** read · ran `redacted.py` and `redacted.py --after` · saw **0 rows matching** become
      **2 rows matching** while the displayed answer stayed identical · added a third pattern to
      `PII_PATTERNS`, re-ran, and **wrote down one class still not covered**
- [ ] Ran the three write-path scripts back to back and can state, without looking, how many of the
      six proposed candidates reach the index and why

## Section 4 — the read path

- [ ] **4.1** read · ran `ranked.py` and `ranked.py --k 3` · saw **0/10, 10/10, 9/10 answered** and
      **4/4, 4/4, 0/4 impostors** · saw the printer question score **0.386** with
      `informative terms: []` · identified the one gold question the shipped path loses and wrote the
      one-sentence defence of losing it
- [ ] **4.2** read · ran `constants.py`, `constants.py --bare` and `constants.py --project` · saw
      findings go **0 → 1** from deleting two comment lines, with no behaviour change · saw the
      project report **5 tuned constants missing** · **decided which module owns `TOP_K`** and wrote
      the reason
- [ ] **4.3** read · ran `saidnothing.py` and `saidnothing.py --silent` · saw all **4/4**
      unanswerable questions produce the sentence, and `kb:KB-104` come back at **0.233** for
      contrast · wrote down the sentence the desk must **never** say and the claim it makes that the
      desk cannot support

## Section 5 — the zero claim

- [ ] **5.1** read · ran `budget.py` and `budget.py --asserted` · saw **14 questions, 14 retrieval
      calls, 0 network requests, 14 model requests, 6617 prompt characters** · found one code path
      that could make a request and would not be counted, and said where the counter must move
- [ ] **5.2** read · ran `indexcost.py` and `indexcost.py --embedded` · saw **65 rows, 0 provider
      requests, 2.7 ms** against **15 requests of a 20/day tier** · worked out on paper what the
      parked lane costs per day at **400 questions** and said which lane that rules out
- [ ] **5.3** read · ran `cacheprefix.py` and `cacheprefix.py --k 6` · saw the cacheable share fall
      **41% → 36%** and the largest variable half grow **1,491 → 2,077 characters** · noticed the
      **57-character** variable half and can say which question produces it · added a sentence to
      `INSTRUCTION` and recorded which way the share moved

## Section 6 — the failure lab

- [ ] **6.1** read · ran `emptystore.py` and `emptystore.py --reachability` · saw **six identical
      health signals** across a filled and an empty store, with the empty one scoring **0.415** ·
      saw reachability go **True / False** · designed the canary memo's two fields
- [ ] **6.2** read · ran `staleindex.py` and `staleindex.py --stamped` · saw a **live** memo report
      `reachable: False`, the same top answer in both arms, and `ticket:4633` move **0.314 → 0.285** ·
      can name the case the row count catches that the timestamp does not, **and** the reverse
- [ ] **6.3** read · ran `greenonnothing.py` and `greenonnothing.py --strict` · saw **`PHASE 7
      GREEN`, exit 0** and **5 findings, exit 1** from the same repository · found the line in
      `gate.py` that decides whether it checks the project or the lab, and can say what the findings
      count becomes if it points at the lab
- [ ] **Break it, watch it go red, fix it:** edit `lab/gate.py` so `load()` returns `None` instead of
      the exception on an import failure, and make `main` skip a `None` module. Run it: `findings`
      drops from **6 to 2** and the four `G01` lines vanish. Put it back. You have just written
      `lenient()` by hand.

## Section 7 — the phase boundary

- [ ] **7.1** read · ran `freshness.py` · saw **3 pins settled, 4 rows amber**, and
      **`pins with no dated ledger row: ['mcp']`** · ran the live `google-adk` command yourself and
      wrote the version and today's date down · can say the three things Principle 14 requires before
      that version could be adopted
- [ ] **7.2** read · ran `ids.py` and `grep -cE '^\| 5[12] ' docs/PROGRESS.md` · wrote your own
      verdict for all **six** of plan section 15's conditions with the command beside each · applied
      the rule and wrote the one-word answer · can name the two conditions no script can answer
- [ ] **7.3** read · ran `handover.py` and `handover.py --trace` · saw **2 of 4 steps node-shaped**
      and both failures reaching `RULES` · wrote the one-line signature change that fixes
      `what_to_keep` and said what the default must be for no call site to change

## The build brief

- [ ] `sutra/memory/service.py`, `sutra/memory/persistence.py`, `sutra/memory/policy.py` and
      `sutra/retrieval.py` all import, and `gate.py`'s four `G01` findings are gone
- [ ] **`TOP_K` has one owner.** The other module imports it, and the comment beside the owner says
      why it is the owner (§4, first `TODO(me)`)
- [ ] `what_to_keep` and `what_to_forget` take `rules` as a keyword argument with a default, and
      `handover.py` reports **4 of 4 node-shaped**
- [ ] The PII classes this project does **not** cover are written down, next to `PII_PATTERNS`
- [ ] The desk's standing instruction is written as one constant, in front of the rows, ending with
      the sentence that hands over
- [ ] The canary memo is designed and filed, and its reachability check runs somewhere that is not a
      lab script
- [ ] The index file carries the newest source timestamp it saw and its row count, **both taken from
      the data and not from the clock**
- [ ] The Gemini free-tier embedding limit is re-verified from AI Studio while signed in, recorded
      with the date, and [5.2](parts/05-the-zero-claim/5.2-the-lane-we-did-not-buy.md)'s arithmetic
      corrected if it moved

## The tests

- [ ] `tests/test_memory_flow.py` exists with five test functions, named as sentences
- [ ] `test_a_filed_memo_is_reachable_by_ref` — the canary, as a test
- [ ] `test_proposed_equals_kept_plus_refused` — 3.1's identity
- [ ] `test_no_stored_row_matches_a_pii_pattern` — run against the store, not the code
- [ ] `test_an_unanswerable_question_returns_no_rows` — asserts `== []`, not falsiness
- [ ] `test_the_shipped_read_path_rejects_every_impostor` — 4.1's third column
- [ ] **Break one, watch it go red, fix it:** lower `SIM_FLOOR` to `0.0` and confirm the impostor
      test fails. Put it back.
- [ ] `uv run python -m pytest -q -m "not live"` passes

## The gate

- [ ] `uv run python days/day-52-memory-in-triage-flow/lab/gate.py; echo "exit: $?"` reports
      **`findings: 0`** and **exit 0**
- [ ] `uv run ruff check --fix tests/test_persona.py` has been run, and `./m check` is green — the
      `I001` failure from Day 15 that keeps plan section 15 rule 3 red (§7, trap 6)
- [ ] `./m depth 52` is green — **19 parts**
- [ ] `./m trace` shows `AG-15` closed by day 52, and no open ID from Phase 7 or earlier
- [ ] `./m wiki` regenerated

## Request budget

- [ ] Model calls today: **0** to every provider. `git diff` shows no `.env` change and no key used.
- [ ] `budget.py` was run and its counts recorded: **14 model requests, 0 network requests**.

## Ledger & commit

- [ ] `docs/PROGRESS.md` row appended, verbatim from §11, with the real hash and an honest gate
      column
- [ ] `docs/PACKAGES.md` row for `mcp==1.29.1` appended, with the date you verified it — the finding
      this day's freshness check produced
- [ ] `docs/PAPERS.md` — nothing to add. This day teaches no paper.
- [ ] Committed as `day 52: phase gate — memory wired into the triage flow — closes AG-15`
