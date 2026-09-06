# Day 72 — Definition of done

`./m done 72` refuses to commit until every box is ticked. Tick a box only when you have actually run
the thing, not when you have read it. This day's measurements are pairs — a strategy against its
alternative — so most boxes ask for both numbers.

## Before you start

- [ ] Day 71's parts and checklist are done.
- [ ] `lab/` scaffolded per §3 — eight Python files, plus two under
      `lab/papers/binary-exponential-backoff/`.
- [ ] `git check-ignore -v days/day-72-backoff-with-honesty/lab/_provider.py` prints a matching rule.
- [ ] `git diff pyproject.toml uv.lock` is empty and stays empty. No package is added today.
- [ ] `uv run python days/day-72-backoff-with-honesty/lab/gate.py; echo "exit: $?"` is **red** on all
      six checks before you write anything.
- [ ] You read `_provider.py` first, and can say why `Refused` and `Unavailable` are separate classes.

## Section 1 — the ladder

- [ ] **1.1** read · you fetched <https://ai.google.dev/gemini-api/docs/troubleshooting> **yourself**
      and recorded what it says on your date, rather than trusting the part's quote (P7)
- [ ] **1.2** read · ran `ladder.py`, `ladder.py --flat` and `ladder.py --opens 40` · recorded that
      the ladder reaches **ok in 5 attempts** while flat retry **gives up**, and that a window at 40s
      defeats both
- [ ] **1.3** read · can say what the attempt budget and the cap each prevent, and what uncapped
      doubling reaches by attempt 10

## Section 2 — the number the server gave you

- [ ] **2.1** read · ran `retryafter.py` and `retryafter.py --ladder` · recorded **2 attempts / 1
      wasted** against **6 attempts / 6 wasted** · can say why honouring it means waiting *longer* on
      the clock and why that is the right trade
- [ ] **2.2** read · ran `retryafter.py --silent` · can say which of Sutra's providers send the header
      and how you would find out
- [ ] **2.3** read · ran the falsy-check demonstration · can say why `retry_after or default` is a bug
      and name the earlier day that found the same shape in a guardrail

## Section 3 — after the last retry

- [ ] **3.1** read · ran `honest.py` and `honest.py --invent` · recorded **exit 0** for the escalation
      and **exit 1** for the invented answer · can say why the exit codes are that way round
- [ ] You can point at the line in your own code that runs after a retry loop, and say which of the
      two things it does
- [ ] **3.2** read · ran the idempotency demonstration and saw the effect happen twice · can state the
      difference between a refusal and a timeout in one sentence

## Section 4 — everyone at once

- [ ] **4.1** read · ran `jitter.py` · recorded **6 distinct instants** and **40 requests at t=1.0s**
- [ ] **4.2** read · ran `jitter.py --jitter` · recorded **123 distinct instants** and the retry burst
      down to **7** · noticed the first burst is still **40** in both runs and can say why
- [ ] You can name the fix for a synchronised *first* attempt, which is not jitter

## Section 5 — in production

- [ ] **5.1** read · ran `builtin.py` and `builtin.py --plain` · recorded **4 model calls against 1**
      · can say what `ReflectAndRetryToolPlugin` *is* good for and when you would adopt it
- [ ] **5.2** read · ran `gate.py` · can say why the error rate is the wrong signal for a system that
      retries, and name the two numbers that are the right ones

## The paper — read it last

- [ ] `papers/01-binary-exponential-backoff.md` read **after** the parts, not before
- [ ] Ran the demo both ways from `lab/papers/binary-exponential-backoff/`: doubling on delivers
      **16 of 16** with **17 collisions** (exit 0); `--off` delivers **0 of 16** with **400
      collisions** (exit 1)
- [ ] Can name the two separate ingredients the paper contributes — randomness and doubling — and say
      which one this day's ladder drops
- [ ] Noticed that the citation's title is assembled from the record's `title` **and** `subtitle`
      fields, and can say why that matters (§17.4.1 rule 5)

## Build brief

- [ ] `sutra/backoff.py` written: `with_backoff(call, *, attempts)`, `retry-after` honoured with
      `is not None`, jitter, and an `Escalated` carrying `attempts` and `waited`
- [ ] You decided the jitter range and said why in the docstring
- [ ] You decided which exception types are retryable at all, and wrote the reason down
- [ ] `tests/test_backoff.py` written, including the exhausted-budget test and the `retry_after=0.0`
      test
- [ ] `uv run python gate.py; echo "exit: $?"` re-run · you can say which of the six cleared

## Repo hygiene

- [ ] `./m depth 72` green — twelve parts and one paper
- [ ] `./m trace` green, and SEC-15 and OPS-13 close on this day and no others
- [ ] `./m wiki` run, so `docs/WIKI.md` and `docs/wiki/day-72.md` are not stale
- [ ] `uv run ruff format --check days/day-72-backoff-with-honesty` clean
- [ ] `uv run ruff check days/day-72-backoff-with-honesty/lab` clean
- [ ] `docs/PROGRESS.md` row appended verbatim from §11, with the real commit hash and the `⚠️` the
      gate actually earned — no rounding up (P10)
- [ ] `docs/PAPERS.md` row for `doi:10.1145/360248.360253` present and dated (P7, §17.4.1)
