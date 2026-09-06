# Day 70 — Definition of done

`./m done 70` refuses to commit until every box is ticked. Tick a box only when you have actually run
the thing, not when you have read it. Several boxes ask you to record a pair of numbers, because most
of this day is one count disagreeing with another.

## Before you start

- [ ] Day 69's parts and checklist are done. Today closes Phase 10's second promise.
- [ ] `lab/` scaffolded per §3 — sixteen files, plus two under `lab/papers/two-choices/`.
- [ ] `git check-ignore -v days/day-70-the-quota-router/lab/_lane.py` prints a matching rule (P9).
- [ ] `git diff pyproject.toml uv.lock` is empty and stays empty. No package is added today.
- [ ] `uv run python days/day-70-the-quota-router/lab/gate.py; echo "exit: $?"` is **red** on all six
      checks before you write anything.
- [ ] You read `lab/_lane.py` before any part. Every number this day prints comes out of it.

## Section 1 — what headroom is

- [ ] **1.1** read · can define **limit**, **window** and **pool**, and say which of the three people
      get wrong
- [ ] **1.2** read · ran `windows.py` · saw a fixed window approve a burst of twice the limit across
      its edge · can say why your dashboard and the provider's disagree without either being wrong
- [ ] **1.3** read · ran `windows.py --sliding` · can say what a sliding window costs per request and
      what it buys
- [ ] **1.4** read · ran `twowindows.py` · recorded that routing on the minute alone empties
      OpenRouter's day by **`t=244s`** and drops 78
- [ ] **1.5** read · ran `twowindows.py --both` and `--ratio` · recorded **222 / 225 / 233** served
      and the three `t=` figures · can say why comparing raw remaining across lanes is comparing
      numbers in different units

## Section 2 — choosing a lane

- [ ] **2.1** read · ran `_router.py`'s decision through `headroom.py` · can say why routing is
      scheduling and therefore cannot live in an agent's configuration
- [ ] **2.2** read · ran `headroom.py --capacity` · can say why capability filtering runs **before**
      headroom is consulted
- [ ] **2.3** read · ran `headroom.py --arrivals` · recorded the four policies' served counts · can
      state the condition under which greedy is the right rule
- [ ] **2.4** read · ran `stale.py`, `stale.py --rounds`, `stale.py --sweep` and `--workers` · can say
      what randomisation is actually doing and what it is not

## Section 3 — the plugin

- [ ] **3.1** read · ran `hooks.py --observe` · saw the router **choose** `groq` while `gemini`
      answered, with `calls the router intercepted: 0` · can quote what adk.dev says about plugin
      hooks being global and agent callbacks local
- [ ] **3.2** read · ran `hooks.py` · saw `intercepted: 1` and `['groq']` answer · can name the three
      return values and say which one a router needs
- [ ] **3.3** read · ran `modelfield.py` · recorded `rerouted by setting the field: False` and can
      explain why the field really changed and `gemini` really answered
- [ ] **3.4** read · ran `desk.py` and `desk.py --naked` · recorded the spread
      **`{'gemini': 4, 'groq': 9, 'openrouter': 11, 'ollama': 0}`** against **`{'gemini': 24}`** · can
      say why `ollama` got nothing and whether that is right

## Section 4 — when a lane says no

- [ ] **4.1** read · can say why a 429 is an instruction rather than an error, and what a client
      should do when the refusal carries no `retry-after`
- [ ] **4.2** read · ran `cold.py` and `cold.py --hammer` · recorded **11 attempts / 10 served** against
      **40 attempts / 10 served** · can say what the 29 extra refusals bought
- [ ] **4.3** read · ran `dry.py` · recorded `spread {'gemini': 10, 'groq': 0, 'openrouter': 20,
      'ollama': 0}` and the `soonest headroom in 60s` refusal · can say why `groq` is at 0
- [ ] **4.4** read · ran `dry.py --degrade` · saw `'reason' in skills: False` and no error reach the
      caller · can state the rule that separates an acceptable downgrade from this one

## Section 5 — failure lab

- [ ] **5.1** read · ran `failopen.py` and `failopen.py --strict` · recorded the **gap of 40** and
      that `succeeded` is 20 in both · can point at the one line that is the whole bug
- [ ] **5.2** read · ran the restart demonstration · recorded what the restarted router believes
      against what the provider has · can say why this and 6.1 are the same root cause
- [ ] **5.3** read · ran `pool.py` and `pool.py --pooled` · recorded **20 sent / 10 refused** against
      **10 sent / 10 held back / 0 refused** · can say what the pool key actually is and how you find
      out

## Section 6 — in production

- [ ] **6.1** read · ran the two-worker demonstration · recorded **13 and 13 against a ceiling of 20,
      provider saw 26, six over** · can say why the lane that breaks is the one with the most headroom
- [ ] **6.2** read · ran the gauge command and `budget.py` · can say why *requests sent* is the wrong
      thing to alert on and what single extra series turns a level into a warning
- [ ] **6.3** read · can state in one sentence what this day built (an estimator, not an enforcer) and
      name the four parked items with the condition that would change each

## The paper — read it last

- [ ] `papers/01-the-power-of-two-choices.md` read **after** the parts, not before
- [ ] Ran the demo both ways from `lab/papers/two-choices/`: with `d=2` the `worst peak` column stays
      at 12–13 from 4 lanes to 64; with `--off` it climbs to 24
- [ ] Can say which column carries the argument and why (the fullest lane is the one that 429s first)
- [ ] Can answer part 2.4's closing question: what has to be true before sampling two is worth
      anything — and can say honestly why Sutra does not need it yet

## Build brief

- [ ] `sutra/routing.py` written: a `BasePlugin` router, `headroom()` over both windows as a share,
      counting on attempt, cold lanes from `retry-after`, and raising rather than degrading
- [ ] The module docstring opens with *estimator, not enforcer* and lists the four parked items with
      their trigger conditions
- [ ] `tests/test_routing.py` written, including the non-quota-failure test that would have caught 5.1
- [ ] `uv run python gate.py; echo "exit: $?"` re-run · you can say which of the six checks cleared
- [ ] `uv run python desk.py --naked` still differs from `uv run python desk.py`. If they ever agree,
      the router has stopped routing

## Repo hygiene

- [ ] `./m depth 70` green — twenty-three parts and one paper
- [ ] `./m trace` green, and OPS-12 and ADK-49 close on this day and no others
- [ ] `./m wiki` run, so `docs/WIKI.md` and `docs/wiki/day-70.md` are not stale
- [ ] `uv run ruff format --check days/day-70-the-quota-router` clean
- [ ] `docs/PROGRESS.md` row appended verbatim from §11, with the real commit hash and the `⚠️` the
      gate actually earned — no rounding up (P10)
- [ ] `docs/PAPERS.md` row for `doi:10.1109/71.963420` present and dated, with the record checked live
      rather than recalled (P7, §17.4.1)
