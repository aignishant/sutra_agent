# Day 59 — Definition of done

`./m done 59` refuses to commit until every box is ticked. Tick a box only when you have actually run
the thing, not when you have read it.

Today has two personalities and both keep the same rule: **every demo has a maximum spend written
down before it runs.** Today's is zero, by construction — every model in the lab is a `CountingLlm`.

## Before you start

- [ ] Day 58's parts and checklist are done, and its triage graph runs end to end. If it does not,
      today has nothing to break (P2).
- [ ] `uv run python days/day-59-runaway-agents-contained/lab/gate.py; echo "exit: $?"` is **red**
      before you write anything, and you have read the finding rather than only counted it.
- [ ] `lab/` scaffolded per §3 — twenty-three files including the two-file paper demo — and
      `tests/test_containment.py` created empty.
- [ ] Both §3 verification commands ran: `max_llm_calls` default prints **500**, and
      `BasePlugin.before_model_callback` prints its keyword-only signature.
- [ ] `git diff pyproject.toml uv.lock` is empty and stays empty. No package is added today.

## Section 1 — four runaways

- [ ] **1.1** read · ran `_fake.CountingLlm` and found the `RunawayGuard` line · can say in one
      sentence why the lab wall is **not** a brake Sutra has · can name the four shapes and, for
      each, which stop is missing rather than which part is broken
- [ ] **1.2** read · ran `loop.py --wall 12` and saw **13 calls, stopped by the LAB** · ran
      `loop.py --fuse 4` and saw **4 calls and `LlmCallsLimitExceededError`** · ran `fuse.py
      --default` and saw **500 against a tier of 20** · added a second route to `review` and
      re-measured
- [ ] **1.3** read · ran `pingpong.py` and saw **both caps hold at 3 while the rally reached 7** ·
      ran `--cap 2` and saw **5** · ran `--fuse 4` and saw the fuse end it at 4 · predicted the rally
      length at `--cap 5` before running it
- [ ] **1.4** read · ran `fanout.py --depth 2` (**13 calls, 7 left of 20**) and `--branch 2 --depth
      5` (**63 calls, −43 remaining**) · found the depth at which branching 3 first exceeds 20 · can
      say which of branching and depth you would argue about in review
- [ ] **1.5** 💥 read · ran `quiet.py` and `quiet.py --wall 200` and saw **201 iterations under a
      fuse of 4 with no error at all** · gave `look_for_more` a real exit route and confirmed the run
      ends without the lab wall · can explain why a per-node timeout does not stop it

## Section 2 — where a brake goes

- [ ] **2.1** read · ran all three arms of `outside.py` and saw **21, 4, 3** · ran
      `--obedient --in-graph` and predicted the count first · can state the five-second test for
      whether something is a guard and apply it to "the agent is instructed not to send more than one
      email per ticket"
- [ ] **2.2** read · ran `counter.py` and `--quality-first` and saw **3 against 4** · ran
      `--critic-fails --quality-first` and saw **the cap was never consulted** · changed `critic()`
      to return `False` instead of raising and wrote down what stops the loop
- [ ] **2.3** read · ran `fuse.py` at 4 and 8 and got exactly the cap both times · read the
      enforcement in `invocation_context.py` · computed the fuse you would set for the desk's
      synchronous path and wrote the sentence justifying it
- [ ] **2.4** read · ran `breaker.py --spent 18` (**0 model calls, refused**) and
      `--spent 18 --swallow` (**1 model call, run "finished"**) · saw ADK wrap the raising plugin and
      **name it** in the `RuntimeError` · predicted `--spent 16`, then changed `FLOOR` to 5 and said
      which prediction moved
- [ ] **2.5** read · ran `kill.py` at `classify`, `draft` and `review` · saw **`--at draft` and
      `--at review` leave byte-identical state and differ by a spent model call** · ran
      `--at research` and wrote down what a resume from that state would re-do

## Section 3 — brakes that do not hold

- [ ] **3.1** 💥 read · ran the inbound-edge count and saw **`draft` has 2** · added a third edge
      into `writer` in `outside.py` and confirmed whether the cap still holds · can say why "it is
      code, not a prompt" is not a sufficient answer
- [ ] **3.2** 💥 read · ran `storm.py` (**27 calls, −7 remaining**), `--layers 4` (**81**) and
      `--budget-aware` (**1**) · found the attempts-per-layer that keeps three layers inside 20 and
      said whether you would ship it
- [ ] **3.3** 💥 read · ran `zero.py` and `--show-warning` and saw **16 calls under a limit of 0** ·
      tried `max_llm_calls=-1` and `=1` and `sys.maxsize` and know which warns, which builds and
      which raises · can say why the library's warning did not help
- [ ] **3.4** 💥 read · ran `loosen.py` (**2 findings at the shipped settings**), `--revisions 8`
      (**60 → 204**) and `--revisions 8 --batch 30` (**510, and one *fewer* finding**) · found a
      combination with zero findings and said whether that desk is one you would ship
- [ ] Can state, without looking: **a brake is a term in an inequality, not a number.**

## Section 4 — fail-stop

- [ ] **4.1** read · ran all three arms of `refuse.py` · saw **the honest refusal exit 1 and the
      invented answer exit 0** · listed every claim the `--carry-on` output makes about the world and
      marked each as verified or not
- [ ] **4.2** read · compared the five-field refusal against `Sorry, something went wrong` · wrote
      the customer-facing rendering of the same refusal and decided which fields it may contain · can
      say why a `likely cause` field would be a mistake

## Section 5 — the Phase 8 gate

- [ ] **5.1** read · ran `endtoend.py` (**5 / 5 / 0 calls, `exit: 0`**) and `--revisions 4`
      (**9 calls**) · ran `--leaky-intake` and watched criterion 1 go red · edited
      `EXPECTED["8842"]["max_model_calls"]` to 1 and can say what still passing tells you
- [ ] **5.2** read · ran `guards.py`, `--drop "loop cap"` (**red**) and `--with deadline` · can say
      why the `fuse` and `budget` columns are identical · added a fifth shape and decided which brake
      catches it
- [ ] **5.3** read · ran `gate.py` **red before writing anything** · ran all three breakage flags and
      saw three non-zero exits · found a second way to break one check and said whether it breaks the
      system or the check
- [ ] **5.4** read · ran `budget.py` and saw **14 would-be against 0 actual** · ran `loosen.py` and
      saw **60 a night against 20** · worked out the largest nightly batch that fits
- [ ] **5.5** read · ran `fresh.py` (**1 finding: `mcp` has no ledger row**) · ran the three PyPI
      commands it printed · opened the MCP specification page and wrote today's date beside the
      revision you found
- [ ] **5.6** read · ran `ids.py` (**7 of 7, `exit: 0`**) and `ids.py --all` · wrote the one-sentence
      Phase 8 verdict in your own words and checked it against the table · can name what the ID audit
      does **not** establish

## Section 6 — in production

- [ ] **6.1** read · ran `loosen.py` and `--revisions 1 --batch 4` · wrote the pull-request
      description for a change raising `MAX_REVISIONS` to 3 — four numbers and one sentence
- [ ] **6.2** 🅿️ read · confirmed `FunctionNode.timeout` and `NodeTimeoutError` exist and that
      **neither is a run deadline** · wrote down the two things a resume of the `--at review` kill
      would need that are not in the printed state

## The paper — read after the parts

- [ ] **`papers/01-fail-stop-processors.md`** read · ran the demo both ways and saw
      **HALTED / exit 1** against **114 accepted / exit 0** · moved the downstream's total check
      above its halted check and wrote down what it then accepts · can answer out loud: what did the
      paper claim, and what do we do differently now?

## The build brief

- [ ] `sutra/containment.py` written — `MAX_REVISIONS`, `RUN_FUSE`, `DAILY_FLOOR`,
      `QuotaBreakerPlugin`, `brake_report` — every line typed by you
- [ ] Each of the three constants carries a comment naming the run it came from, with the date
- [ ] `RUN_FUSE > 0`, with the startup assertion from 3.3, and the arithmetic in the comment
- [ ] `QuotaBreakerPlugin` **raises**; there is no path where it logs and returns `None`
- [ ] The six `TODO(me)` decisions from §4 are made and written down, including the one that is an
      ADR (the run-deadline decision from 5.2)

## The tests

- [ ] `tests/test_containment.py` written — five tests, all offline
- [ ] `uv run python -m pytest tests/test_containment.py -q -m "not live"` is green
- [ ] **Break it and watch it go red:** set `RUN_FUSE = 0`, run the suite, see
      `test_run_fuse_is_a_positive_number` fail, then put it back
- [ ] **Break it a second time:** delete the comment after `DAILY_FLOOR`, watch
      `test_every_brake_constant_carries_its_provenance` fail, then restore it

## The gate

- [ ] `uv run python days/day-59-runaway-agents-contained/lab/gate.py; echo "exit: $?"` prints
      `findings: 0` and `exit: 0`
- [ ] `./m depth 59` green
- [ ] `./m trace` run, and day 59's IDs are exactly `AG-21, SEC-04`
- [ ] The Phase 8 verdict is written down as a count — **four green, two amber** — with each amber
      stated as a condition and the command that clears it
- [ ] `./m check` run, and its **red** state named honestly in the ledger row rather than omitted

## Request budget

- [ ] **0 of 20** free-tier Gemini generations spent. `budget.py` printed `ACTUAL calls to a
      provider: 0`, and if it ever prints anything else the would-be totals above it are no longer
      would-be

## Ledger & commit

- [ ] `docs/PROGRESS.md` row appended, with the real hash and the `⚠️` that
      [5.6](parts/05-the-gate/5.6-criterion-6-the-ids-and-the-verdict.md) justifies
- [ ] `docs/PACKAGES.md` row for `mcp==1.29.1` pasted from §11 — the finding two gates have now made
- [ ] `docs/PAPERS.md` row for `doi:10.1145/357369.357371` present
- [ ] `docs/SKILL_PROVENANCE.md` unchanged, and Day 29's pinned row re-checked as part of the
      freshness ritual
- [ ] Committed as `day 59: phase gate + runaway containment lab - closes AG-21, SEC-04`
- [ ] `git ls-files` free of any secret; `.env` still ignored
