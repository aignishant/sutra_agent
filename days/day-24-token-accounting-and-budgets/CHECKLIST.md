# Day 24 — CHECKLIST

**IDs closed:** OPS-07, AG-11
**Principles served:** 1, 2, 7, 8, 10, 11, 14, 15, 16, 17, 18
**Parts:** 13 across 5 sections, plus 1 paper

> `./m done 24` refuses to commit while any box below is unticked. It cannot tell whether you were
> honest — that part is yours.

## Demo command

```bash
cd days/day-24-token-accounting-and-budgets/lab
uv run python count_the_cost.py                           # 0 generations (count_tokens)
uv run python history_costs_again.py                      # 0 generations (count_tokens)
uv run python -m pytest test_quota_demo.py                # green, no key
CHECK_FIRST=1 uv run python refuse_before_spending.py     # 0 generations
CHECK_FIRST=0 uv run python refuse_before_spending.py     # 0 generations
CLASSIFY=1 uv run python retry_spent_the_budget.py        # 0 generations
CLASSIFY=0 uv run python retry_spent_the_budget.py        # 0 generations
COUNT_ATTEMPTS=1 uv run python counted_the_wrong_thing.py # 0 generations
COUNT_ATTEMPTS=0 uv run python counted_the_wrong_thing.py # 0 generations
PER_USER=1 uv run python budget_per_what.py               # 0 generations
PER_USER=0 uv run python budget_per_what.py               # 0 generations
MODE=degrade uv run python degrade_dont_fail.py           # 0 generations
MODE=fail    uv run python degrade_dont_fail.py           # 0 generations
MODE=pretend uv run python degrade_dont_fail.py           # 0 generations
cd papers/token-bucket
BUCKET=1 uv run python run.py                             # 0 generations
BUCKET=0 uv run python run.py                             # 0 generations
cd -
uv run python -m pytest tests/test_quota.py -q -m "not live"
./m check && uv run python scripts/trace.py && git log --oneline -1
```

Expected: **4.55 / 2.21 / 0.80 characters per token**, with a four-character ticket id costing five;
**151 tokens of conversation charged as 786**; `8 passed`; **`20 of 20` against `25 of 20`**;
**1 request against 3** for the same refusal; **16 and 16 against 16 and 11**, believing 9 remain when
4 do; **20 served with two people refused against 14 served with nobody refused**; `degraded via
handbook` / `RuntimeError` / `ok via model` for the same sentence; then **5 served against 10, and
2x the limit at the boundary**. Then your own suite green, `OK all green`,
`traceability: 45/199 closed, 0 problem(s)`, and one commit.

## Setup

- [ ] `days/day-24-token-accounting-and-budgets/lab/` exists with the nine scripts
- [ ] `lab/papers/token-bucket/` exists with `bucket.py` and `run.py`
- [ ] No `uv add` was needed — `google-genai` and the stdlib are the whole toolbox
- [ ] Confirmed the two counting scripts need `GOOGLE_API_KEY` and spend **0** generations
- [ ] Confirmed every other script runs with **no key at all**

## Section 1 — `01-what-a-request-costs`

- [ ] **1.1** read · ran `count_the_cost.py` · **added two samples of your own and wrote your
      characters-per-token prediction down first** · said out loud why a word count cannot estimate a
      token count
- [ ] **1.2** read · ran `history_costs_again.py` · **added four turns and checked the multiplier
      against (n+1)/2** · said out loud why turn eight costs more than turn one for the same length of
      message
- [ ] **1.3** read · re-read the 429 body and found the word `requests` in the metric name · said out
      loud one optimisation that is worthless on a per-request tier

## Section 2 — `02-two-ceilings`

- [ ] **2.1** read · ran the ledger tests green · **deleted the per-day branch and read the message on
      the failing assertion, not the test name** · said out loud the correct response to each ceiling
- [ ] **2.2** read · found `quotaId`, `quotaValue` and `retryDelay` in the captured body · **left the
      `rpm` TODO alone or captured it properly — no guessed number** · said out loud why the HTTP
      status is not enough to classify a 429
- [ ] **2.3** read · **wrote your own provider table and marked every cell measured or estimated** ·
      counted how many are measured · said out loud the three moves that remain when "spend more" is
      unavailable

## Section 3 — `03-counting-before-spending`

- [ ] **3.1** read · confirmed `grep -c "import time" quota.py` prints `0` · **tried to write the
      daily-reset test against a real clock and noticed what it would need** · said out loud why the
      ledger is timestamps rather than a counter
- [ ] **3.2** read · ran both `refuse_before_spending.py` arms · **saw `20 of 20` against `25 of 20`** ·
      said out loud the three-word order of operations for spending a request
- [ ] **3.3** read · ran the suite in 0.06s · **added the exact-boundary case at `MINUTE` and predicted
      the answer first** · said out loud the three ways to test time-dependent code and what each costs

## Section 4 — `04-failure-lab`

- [ ] **4.1** read · ran both `retry_spent_the_budget.py` arms · **counted the attempt lines: one
      against three** · set `MAX_ATTEMPTS = 5` and worked out the fraction of a day one refusal would
      cost · said out loud which ceiling is worth retrying
- [ ] **4.2** read · ran both `counted_the_wrong_thing.py` arms · **added three more retried questions
      and watched the disagreement grow while the question count barely moved** · said out loud which
      direction the error always goes

## Section 5 — `05-in-production`

- [ ] **5.1** read · ran both `budget_per_what.py` arms · **moved Asha's fourteen requests to the end
      and predicted which numbers would change** · said out loud the two failures you are choosing
      between
- [ ] **5.2** read · ran all three modes · **compared the two identical `refund window` answers and
      said what a log consumer can do with one and not the other** · listed every desk function as
      needs / nice / does not need the model

## The paper — read after the parts

- [ ] **`papers/01-the-leaky-bucket.md`** read · ran **both arms** of the demo
- [ ] Saw the fixed window serve **10 of 10 — 2x the limit — in three seconds** while reporting no
      violation
- [ ] Moved `ARRIVALS` away from the boundary, re-ran both arms, and can say why this bug survives
      testing
- [ ] Can name what the bucket does **not** solve: fairness between senders, and distributed
      enforcement
- [ ] Answered out loud: *what did this paper actually claim, and what do we do differently now?*
- [ ] Named one thing from it in use today and one thing the field replaced

## Build brief

- [ ] `sutra/quota.py` written: `Ceiling`, `Ledger`, `used`, `refusal`, `spend`, `ceiling_from`
- [ ] `Ceiling` is **frozen** and carries no token or currency field
- [ ] `refusal()` returns a **sentence or `None`**, never a boolean
- [ ] The **day ceiling is checked first**, and a test proves it
- [ ] `spend()` is called on every **attempt**, and there is exactly one place in the repo that calls it
- [ ] `grep -c "import time" sutra/quota.py` prints `0`
- [ ] `sutra/plugins.py` extended so the budget is checked **before** the request goes out
- [ ] The budget check is a **third** object beside Day 21's `Policy` and Day 22's `Flight`, not merged
- [ ] Decided and wrote down where the ledger's state lives across a restart
- [ ] `git diff` reviewed before committing

## The eval that must be able to fail

- [ ] `tests/test_quota.py` written; the whole file passes with no key and no network
- [ ] Watched it RED **before** writing `sutra/quota.py`, not after
- [ ] **Broke it on purpose:** deleted the per-day branch — two of eight red
- [ ] **Broke it a second way:** swapped the two `if`s so the minute check runs first
- [ ] **Broke it a third way:** pruned the deque to `MINUTE` instead of `DAY`
- [ ] **Broke it a fourth way:** incremented on success instead of on attempt
- [ ] Read all four failure messages and confirmed at least one names the *words* of the refusal rather
      than just a boolean
- [ ] Wrote down, in one sentence, what this whole suite still fails to notice
- [ ] Fixed everything; suite green again

## Request budget

- [ ] Total generations for the day: **0 of 20**
- [ ] Confirmed by running the whole demo command and checking your provider dashboard afterwards
- [ ] The `rpm` number is either **captured from a real 429 and recorded with a date**, or still a
      `TODO` — and in no case a plausible guess

## Ledger

- [ ] `docs/PROGRESS.md` row appended:
      `| 24 | <date> | OPS-07, AG-11 | 13 (+1 paper) | <hash> | ✅ |`
- [ ] `docs/PAPERS.md` row appended:
      `| New directions in communications (or which way to the information age?) | doi:10.1109/MCOM.1986.1092946 | 1986 | 2026-09-04 | 24 | days/day-24-token-accounting-and-budgets/papers/01-the-leaky-bucket.md |`
- [ ] `docs/PACKAGES.md` — the quota row added if you captured the RPM, otherwise the TODO recorded
- [ ] `./m depth 24` green
- [ ] `./m trace` shows OPS-07 and AG-11 closed, `45/199`, 0 problems
- [ ] `./m check` green

## Commit

- [ ] `day 24: token accounting and budgets - denominated in quota, not dollars - closes OPS-07, AG-11`
