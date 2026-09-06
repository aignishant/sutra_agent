# Day 76 — Definition of done

`./m done 76` refuses to commit until every box is ticked. Tick a box only when you have actually run
the thing, not when you have read it. Two of today's scripts **read** the package rather than running
anything against a model, and they say so in their own output — do not tick them as measurements.

## Before you start

- [ ] Day 75's parts and checklist are done.
- [ ] `lab/` scaffolded per §3 — five Python files, plus two under `lab/papers/endpoints/`.
- [ ] `git check-ignore -v days/day-76-vad-and-non-blocking-tools/lab/_live.py` prints a matching rule.
- [ ] `git diff pyproject.toml uv.lock` is empty and stays empty. No package is added today.
- [ ] `uv run python days/day-76-vad-and-non-blocking-tools/lab/gate.py; echo "exit: $?"` is **red**
      on all six checks before you write anything.
- [ ] You read `_live.py` first, and can say what `BLOCKING` changes and — more importantly — what it
      does not.

## Section 1 — the tool in the middle

- [ ] **1.1** read · you can say what a caller experiences during a tool call on an open line that
      they cannot experience in a request
- [ ] **1.2** read · you can name the four steps of the round trip and say which of them the runtime
      does rather than the model
- [ ] **1.3** read · ran `freeze.py` and `freeze.py --blocking` · recorded **4 audio slices against
      0** and **exit 0 against exit 1** · you can say why `async def` appears in both runs

## Section 2 — when the answer comes back

- [ ] **2.1** read · ran `scheduling.py` · recorded the four `FunctionResponseScheduling` values and
      what the package's own docstring says each does
- [ ] **2.2** read · you picked a scheduling for one tool of your own and wrote down what it is wrong
      for
- [ ] **2.3** read · you decided what the caller hears during a wait, and can say what makes a filler
      line a lie rather than a courtesy

## Section 3 — deciding when they stopped

- [ ] **3.1** read · ran `vadconfig.py` · recorded the five `AutomaticActivityDetection` fields and
      the two `ActivityHandling` values, against the ADK version you have installed
- [ ] **3.2** read · you can describe, in one sentence each, the caller's experience at both ends of
      the end-of-speech sensitivity dial
- [ ] **3.3** read · you can say which of Day 75's two measured arms corresponds to `NO_INTERRUPTION`

## Section 4 — in production

- [ ] **4.1** read · you can name the signal that would have caught a frozen line, and say why the
      error rate is not it
- [ ] **4.2** read · you cut the list to the three you would build first, with a sentence each

## The paper — read it last

- [ ] `papers/01-endpoint-detection.md` read **after** the parts, not before
- [ ] Ran the demo both ways from `lab/papers/endpoints/`: with zero crossings the endpoints are
      exact and **0 frames** are clipped (exit 0); with `--off` the word is detected as frames 12–27
      instead of 8–31 and **8 frames** are clipped (exit 1)
- [ ] You can say why a fricative defeats an energy threshold, and what replaces loudness as the
      signal
- [ ] You noticed that the Crossref record carries **no abstract**, and can say what that means about
      how carefully the paper document attributes its claims

## Build brief

- [ ] `sutra/livetools.py` written: `TOOLS`, every tool awaiting rather than blocking, and at least
      one declaring `is_long_running` or `response_scheduling`
- [ ] You wrote down what the caller hears while a tool runs, and why
- [ ] You gave each tool its own timeout, separate from the session deadline
- [ ] `tests/test_livetools.py` written, including the test that something else runs while a slow
      tool waits
- [ ] `uv run python gate.py; echo "exit: $?"` re-run · you can say which of the six cleared

## Repo hygiene

- [ ] `./m depth 76` green — eleven parts and one paper
- [ ] `./m trace` green, and ADK-56 and ADK-77 close on this day and no others
- [ ] `./m wiki` run, so `docs/WIKI.md` and `docs/wiki/day-76.md` are not stale
- [ ] `uv run ruff format --check days/day-76-vad-and-non-blocking-tools` clean
- [ ] `uv run ruff check days/day-76-vad-and-non-blocking-tools/lab` clean
- [ ] `docs/PROGRESS.md` row appended verbatim from §11, with the real commit hash and the `⚠️` the
      gate actually earned — no rounding up (P10)
- [ ] `docs/PAPERS.md` row for `doi:10.1002/j.1538-7305.1975.tb02840.x` present and dated (P7,
      §17.4.1)
