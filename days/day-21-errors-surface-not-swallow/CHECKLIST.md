# Day 21 — CHECKLIST

**IDs closed:** ADK-23, SEC-02
**Principles served:** 1, 2, 3, 4, 8, 10, 11, 12, 13, 15, 16, 17, 18
**Parts:** 14 across 5 sections, plus 1 paper

> `./m done 21` refuses to commit while any box below is unticked. It cannot tell whether you were
> honest — that part is yours.

## Demo command

```bash
cd days/day-21-errors-surface-not-swallow/lab
uv run python three_shapes.py                    # 0 generations
uv run python fact_not_sentence.py               # 0 generations
uv run python three_responses.py                 # 0 generations
SWALLOW=1 uv run python who_hears_it.py          # 0 generations
SWALLOW=0 uv run python who_hears_it.py          # 0 generations
RESCUE=1 uv run python rescue.py                 # 0 generations
RESCUE=0 uv run python rescue.py                 # 0 generations
POLICY=substitute FAILURES=1 uv run python model_error.py
POLICY=propagate FAILURES=1 uv run python model_error.py
CLASSIFY=1 uv run python retry_made_it_worse.py  # 0 generations
CLASSIFY=0 uv run python retry_made_it_worse.py  # 0 generations
HONEST=1 uv run python fallback_that_lied.py     # 0 generations
HONEST=0 uv run python fallback_that_lied.py     # 0 generations
REDACT=1 uv run python give_up_honestly.py       # 0 generations
REDACT=0 uv run python give_up_honestly.py       # 0 generations
SAFE=1 uv run python handler_that_broke.py       # 0 generations
SAFE=0 uv run python handler_that_broke.py       # 0 generations
uv run python where_policy_lives.py              # 0 generations
uv run python -m pytest test_errors_demo.py -q
cd papers/end-to-end-arguments
END_TO_END=1 uv run python transfer.py           # 0 generations
END_TO_END=0 uv run python transfer.py           # 0 generations
cd -
uv run python -m pytest tests/test_errors.py -q -m "not live"
./m check && uv run python scripts/trace.py && git log --oneline -1
```

Expected: three shapes with one reaching only the model; 42 chars against 78 and one question prose
cannot answer; six failures ending in substitute or escalate; **three error hooks against zero**; a
rescue stopping the ladder at the first rung; a model 429 substituted then propagated; **one call
against four** and 19 requests left against 16; *"I could not reach the knowledge base"* against
*"KB-104 has no content recorded"*; four internal details leaked in 433 characters; the original
`TimeoutError` missing from what raised; 11 places against 1. Then `8 passed`, then three hops all
reporting success while `identical: False`, then `OK all green`, then
`traceability: 40/199 closed, 0 problem(s)`, then one commit.

## Setup

- [ ] `days/day-21-errors-surface-not-swallow/lab/` exists with the twelve scripts
- [ ] `lab/papers/end-to-end-arguments/` exists with `link.py` and `transfer.py`
- [ ] No `uv add` was needed — confirmed `google-adk==2.7.1` already pinned
- [ ] Confirmed the whole day runs with **no `GOOGLE_API_KEY` set at all**

## Section 1 — `01-who-hears-it`

- [ ] **1.1** read · ran `three_shapes.py` · said out loud the three parties, and which shape reaches
      only one of them
- [ ] **1.2** read · ran `fact_not_sentence.py` · said out loud the test that separates a fact from a
      sentence, and the one field prose can never carry
- [ ] **1.3** read · ran `three_responses.py` · said out loud the three responses, which is never
      terminal, and which failure escalates immediately

## Section 2 — `02-four-hooks`

- [ ] **2.1** read · ran `RESCUE=0 rescue.py` · **saw three hooks fire in order** · said out loud what
      trap #4 is and what a tool's own `try`/`except` removes
- [ ] **2.2** read · ran `RESCUE=1 rescue.py` · said out loud the two hooks that can rescue, what each
      returns, and what fires after a successful rescue
- [ ] **2.3** read · **watched `on_agent_error_callback` return a dict and the run raise anyway** ·
      said out loud what its docstring promises
- [ ] **2.4** read · ran the tool-failure and model-failure ladders back to back · said out loud the
      two entry points and what a rescue does to your run-level error rate

## Section 3 — `03-policy`

- [ ] **3.1** read · ran both `retry_made_it_worse.py` arms · said out loud which field distinguishes
      the two 429s and what `Please retry in 58s` on the daily one actually means
- [ ] **3.2** read · ran both `fallback_that_lied.py` arms · **watched a true-sounding sentence be
      false** · said out loud what `found: False` claims versus `status: unavailable`
- [ ] **3.3** read · ran `REDACT=0 give_up_honestly.py` and read the four leaks · said out loud the
      two audiences a failure has and what each gets

## Section 4 — `04-failure-lab`

- [ ] **4.1** read · ran both `who_hears_it.py` arms · **saw the hook count go three → zero** · said
      out loud what the user was told while the knowledge base was down
- [ ] **4.2** read · ran both `handler_that_broke.py` arms · **saw the original `TimeoutError`
      disappear from what raised** · said out loud where the log line has to go

## Section 5 — `05-in-production`

- [ ] **5.1** read · ran `where_policy_lives.py` · said out loud the two rows that matter more than
      the line count, and what a tool should contribute if not the policy
- [ ] **5.2** read · ran `test_errors_demo.py` green · said out loud the two seams you fake, and the
      single assertion that catches a swallowed exception

## The paper — read after the parts

- [ ] **`papers/01-end-to-end-arguments.md`** read · ran both demo arms and saw `3/3` hops succeed
      while `identical: False`
- [ ] Read the five enumerated threats and worked out how many a reliable network protects you from
- [ ] Answered out loud: *what did this paper actually claim, and what do we do differently now?*
- [ ] Named the paper's own limit on its argument (the *Performance aspects* section)

## Build brief

- [ ] `sutra/errors.py` written: `Failure`, `classify`, `is_retryable`, `substitute`,
      `public_message`, `LEAKS`
- [ ] `Failure` is a `dataclass`, and the default for `retryable` has one sentence saying why it is
      the safe default
- [ ] `sutra/plugins.py` extended with all four error hooks
- [ ] The **first statement** of `on_tool_error_callback` is the structured record, before any policy
- [ ] `substitute()` always emits `status` — verified by reading it, not by remembering
- [ ] `public_message()` is a **lookup**, not a format string with the exception interpolated
- [ ] **Every `try`/`except` removed from every tool under `sutra/`** — `git diff` reviewed hit by hit
- [ ] `grep -rn "except Exception" sutra/` returns only places with a comment saying why
- [ ] Day 14's existing plugin behaviour still present and unchanged

## The eval that must be able to fail

- [ ] `tests/test_errors.py` written; the whole file passes with no key and no network
- [ ] Watched it RED **before** writing `sutra/errors.py`, not after
- [ ] **Broke it on purpose:** put a `try`/`except` back in a tool — five of eight red
- [ ] **Broke it a second way:** `Runner(agent=...)` instead of `app=` — noted which tests catch it
- [ ] **Broke it a third way:** removed `status` from the substitute — noted which tests catch it
- [ ] Noticed at least one failure message you would not want to debug at 11pm, and improved it
- [ ] Fixed all three; suite green again

## Request budget

- [ ] Total generations for the day: **0 of 20**
- [ ] Confirmed by running the whole demo command with no `GOOGLE_API_KEY` in the environment
- [ ] The real 429 body used in 3.1 and 3.3 is a captured fixture, not a fresh call

## Ledger

- [ ] `docs/PROGRESS.md` row appended:
      `| 21 | <date> | ADK-23, SEC-02 | 14 (+1 paper) | <hash> | ✅ |`
- [ ] `docs/PAPERS.md` row appended:
      `| End-to-end arguments in system design | doi:10.1145/357401.357402 | 1984 | 2026-09-03 | 21 | days/day-21-errors-surface-not-swallow/papers/01-end-to-end-arguments.md |`
- [ ] `docs/PACKAGES.md` — confirmed no new rows are needed
- [ ] `./m depth 21` green
- [ ] `./m trace` shows ADK-23 and SEC-02 closed, `40/199`, 0 problems
- [ ] `./m check` green

## Commit

- [ ] `day 21: error handling - surface, don't swallow - closes ADK-23, SEC-02`
