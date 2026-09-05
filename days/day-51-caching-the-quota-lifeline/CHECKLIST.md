# Day 51 — Definition of done

`./m done 51` refuses to commit until every box is ticked. Tick a box only when you have actually run the
thing, not when you have read it.

## Before you start

- [ ] Day 50's parts and checklist are done, and
      `uv run python days/day-50-chunking-and-top-k/lab/sweep.py` still prints its seven rows. If it does
      not, today's `_desk.py` fixture is quoting numbers that no longer hold (P2).
- [ ] `python -c "from google.adk.apps.app import App; print('context_cache_config' in App.model_fields)"`
      prints **True**. If it prints `False` or raises, the installed ADK is not `2.7.1` and today stops
      rather than adapts (P8, P14).
- [ ] `uv run python days/day-51-caching-the-quota-lifeline/lab/gate.py; echo "exit: $?"` is **red**
      before you write anything — `1-7: sutra.cache is not importable` and `exit: 1`.
- [ ] `lab/` scaffolded per §3 — sixteen scripts plus `lab/papers/storage-hierarchies/` — and
      `sutra/cache.py` and `tests/test_cache.py` created empty.
- [ ] `git diff pyproject.toml uv.lock` is empty and stays empty. No package is added today.

## Section 1 — two caches, two currencies

- [ ] **1.1** read · ran `prefix.py` and `shrink.py` · saw **660 + 4,952 + 512 = 6,124 characters, and 39
      left after a hit** · deleted one `FunctionDeclaration` from `_desk.TOOLS` and wrote down what one
      tool costs · can say which of the four pieces of a request are identical between two questions
- [ ] **1.2** read · ran `savings.py` and `savings.py --ttl 900` · saw **99% of characters and 0 requests**
      from the context cache against **54 of 120 requests** from the response cache · can say which of the
      two caches is capable of returning a wrong answer, and why the other one is not
- [ ] **1.3** read · ran `collide.py --show` and read the merged pairs · wrote the one-sentence promise
      that leaving one field out of `cache_key` makes · can explain why a key missing a field shows a
      *higher* hit rate

## Section 2 — the context cache

- [ ] **2.1** read · ran `cacheable.py` and `cacheable.py --tool` · saw **`contents[:0] of 1` on a cold
      start** and the prefix stay at 4 when a sixth user turn was added · added a `"model"` turn to
      `_desk.TURNS`, predicted the new count **before** running, and was right
- [ ] **2.2** read · ran `shrink.py` · saw **6,124 → 39 characters**, `tools` become `None` and not `[]` ·
      can name the four things ADK changes on the outgoing request
- [ ] **2.3** read · ran `fingerprint.py` and `fingerprint.py --tools` · saw **a trailing space MOVE it and
      the reversed tool list not** · ran `lifecycle.py --drift 1` and saw **200 caches, 399 extra API
      calls, 1.0 turns served per cache** · changed `MODEL` to `gemini-2.5-flash`, predicted, checked,
      changed it back
- [ ] **2.4** read · ran `lifecycle.py`, `--intervals 100` and `--intervals 1` · saw **19 caches with 0
      expiries and 18 reuse deaths**, then **3 caches with 2 expiries**, then **100 caches and 199 extra
      calls** · found the `--intervals` value where the death cause switches (it is between 80 and 90)

## Section 3 — the floor we never reach

- [ ] **3.1** read · ran `floors.py` and `floors.py --min 8000` · saw all **three refusal log lines
      verbatim** and watched arm 3 change its reason when only `min_tokens` moved · set `MODEL` to
      `gemini-2.5-flash`, re-ran, and can say which arm changed verdict
- [ ] **3.2** read · ran `prefix.py` and `prefix.py --k 20` · saw **1,521 of 4,096, 37.1%, 2,575 short**,
      and **71.4% still short at k=20** · can name the three wrong ways to close the gap and say what is
      wrong with each
- [ ] **3.3** read · ran `prefix.py --archive` · saw the only **`CACHEABLE`** verdict in the day, at
      **4,700 tokens and 114.7%** · computed the corpus size that would exceed a 32,000-token window ·
      can name two Day 50 correctness properties the pasted archive would cost

## Section 4 — the ADK config

- [ ] **4.1** read · ran both `python -c` commands from §3 step 9 · reproduced
      `Extra inputs are not permitted` by passing `context_cache_config` to an `LlmAgent` · can say why
      the setting cannot be per agent, and name the 1.x → 2.x trap it is an instance of
- [ ] **4.2** read · constructed a fingerprint-only `CacheMetadata` and an active one and printed both ·
      triggered the validator message about `cache_name, expire_time, and invocations_used` · confirmed
      `is_active` does **not** exist in Python · can name the three states and what each one means
- [ ] **4.3** read · ran `lifecycle.py --ttl 300` and saw it produce **exactly the default output** ·
      swept `--intervals` and found the crossover between 80 and 90 · changed `SECONDS_BETWEEN_TURNS` to
      5 and found the new crossover · wrote the relationship as one inequality

## Section 5 — the response cache

- [ ] **5.1** read · ran `hitrate.py` and the paper demo's `stack.py` · saw **78 / 83 / 58 / 37%** and the
      curve go flat at **size 10** · counted the distinct normalised questions yourself and confirmed the
      ceiling is 50 of 60 · can say what it means if a measured hit rate exceeds the ceiling
- [ ] **5.2** read · ran `hitrate.py` and `collide.py` · saw the tenant cost **25 points** on the 60-ask
      log and the tenant-blind key score **92% with 73% of hits wrong** on `TENANT_LOG` · can state the
      test for whether a field belongs in a key
- [ ] **5.3** read · ran `collide.py --show` and `ops.py --break-key` · saw the hit rate climb **78 → 83 →
      85 → 87%** while `wrong` went **0 → 0 → 1 → 3** · added a third trap pair to `_log.TRAPS` and
      predicted which recipes merge it before running
- [ ] **5.4** read · ran `stale.py`, `--ttl 1800` and `--revalidate` · saw **17 served, 5 wrong, 2 calls**,
      then **5 served, 0 wrong, 14 calls**, then **19 calls for 19 asks** · added a third change and found
      the TTL that produces exactly one wrong answer · can say why `ttl.py --revalidate` is an oracle and
      not a result
- [ ] **5.5** read · ran `ttl.py` and `ttl.py --revalidate` · saw stale go **0,0,0,0,0,1,5** and calls go
      **60 → 10** · can say why the TTL cannot be tuned from the hit rate, and name the TTL where the free
      lunch ends · moved `CHANGES["refund-window"]` to 2000 and re-swept

## Section 6 — proving the saving

- [ ] **6.1** read · ran `savings.py` and `savings.py --ttl 21600` · saw **6.0 days of free tier against
      3.3**, and at ttl 21600 **exactly 1.0 days with 5 wrong answers** · wrote the two-line report for
      the second one in the unit of the bill
- [ ] **6.2** read · ran `ops.py --lines 12` and `ops.py --break-key` · saw the hit rate go **45% → 50%**
      while alarm 2 fired at **3 of 30 hits** · set `ALARM_AGE_CEILING_S = 3000` and decided whether the
      alarm it fires is a real problem · can name the field that is always omitted and say what it alone
      detects
- [ ] **6.3** read · ran `stampede.py`, `--fill 20` and `--agents 12` · saw **6 calls against 1**, and 30%
      of the daily free tier on one question · found an `--agents`/`--fill` pair that spends the whole
      20-request quota on one question · can name the two ways the single-flight fix itself fails

## Section 7 — in production

- [ ] **7.1** read · ran `python -c "print(hash('same string'))"` twice in **two separate processes** and
      saw two different numbers · listed the three things in `.env` that must never reach a cache key and
      named the log or metric that would have carried them · can describe the timing channel in one
      sentence
- [ ] **7.2** read · ran `hitrate.py` and `stack.py` · counted the distinct `answer_id` values and
      confirmed the semantic ceiling is **51 of 60, 85%** — two points above exact matching · wrote the
      three trigger conditions as three sentences with numbers in them

## The paper — read after the parts

- [ ] **`papers/01-storage-hierarchies.md`** read · ran `stack.py` and `stack.py --ablate` and saw
      **identical curves from 1 pass / 351 reads against 12 passes / 3,226 reads** · ran the `diff` and
      got **no output** · computed the stack distances of `A B A C B A` by hand and checked them against
      the table · can answer, out loud: *what did this paper actually claim, and what do we do
      differently now?*

## The build brief

- [ ] `sutra/cache.py` written by hand — three constants, `cache_key`, `ResponseCache`,
      `context_cache_config` — with **every constant carrying a comment naming the run it came from**
- [ ] `CACHE_INTERVALS` chosen, with the `lifecycle.py` run in the comment **and** which of the two
      limits is binding at that value
- [ ] `CACHE_TTL_SECONDS` chosen off the sweep, with **the cost written down**: the wrong answers it
      accepts on this traffic, or the word `zero`
- [ ] `CACHE_MIN_TOKENS` set to the provider's floor, with the measurement, the date, **and the trigger
      condition** under which context caching would start working
- [ ] the agent-id question decided, with the one-sentence promise written in the `cache_key` docstring
- [ ] the `question_class` values decided — two or three, each one a class whose TTL you would set
      differently
- [ ] the pasted-archive ADR written, both columns, ending with a corpus size that would change the answer
- [ ] the single-flight decision written down: not needed yet, what would make it necessary, and what the
      wait deadline would be
- [ ] the three parked triggers from 7.2 written as three sentences with numbers in them

## The tests

- [ ] `tests/test_cache.py` written by hand — all six functions, named as sentences
- [ ] `uv run python -m pytest tests/test_cache.py -q -m "not live"` is **green**
- [ ] **break it on purpose:** delete the `tenant` argument from `cache_key`, watch
      `test_cache_key_separates_two_tenants` go **red**, and watch `gate.py` finding 4 appear. Then fix it
      and watch both go green again
- [ ] `uv run python days/day-51-caching-the-quota-lifeline/lab/gate.py; echo "exit: $?"` prints
      `findings: 0` and `exit: 0`

## The evals

- [ ] the paper demo ablation `diff` prints **nothing** and exits `0`
- [ ] every command in §5's re-run list has been run at least once and none of them raised
- [ ] `uv run ruff check .` and `uv run ruff format --check .` are clean
- [ ] `uv run python scripts/depth_check.py 51` prints `OK day 51  23 parts + 1 papers`

## Request budget

- [ ] **0 generations spent.** `savings.py`, `stampede.py` and `prefix.py` quote the 20-a-day ceiling from
      `docs/PACKAGES.md`; none of them call a model
- [ ] `floors.py --live` either **not run**, or run once and its real output pasted into part 3.1 in place
      of the `TODO(me)` — never an invented transcript (P10)

## The ledger

- [ ] `docs/PROGRESS.md` row appended, with the real hash after committing
- [ ] `docs/PAPERS.md` row for `doi:10.1147/sj.92.0078` present, and you have opened
      <https://doi.org/10.1147/sj.92.0078> yourself and seen the title match
- [ ] `docs/PACKAGES.md` — confirmed **no** new rows are needed today
- [ ] committed as `day 51: caching — context and response caching as the quota lifeline — closes ADK-31, OPS-10`
