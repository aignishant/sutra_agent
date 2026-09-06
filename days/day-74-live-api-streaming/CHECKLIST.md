# Day 74 — Definition of done

`./m done 74` refuses to commit until every box is ticked. Tick a box only when you have actually run
the thing, not when you have read it. Most of today's measurements are pairs — a mode against its
alternative — so most boxes ask for both numbers.

## Before you start

- [ ] Day 73's parts and checklist are done.
- [ ] `lab/` scaffolded per §3 — seven Python files, plus two under `lab/papers/response-time/`.
- [ ] `git check-ignore -v days/day-74-live-api-streaming/lab/_fake.py` prints a matching rule.
- [ ] `git diff pyproject.toml uv.lock` is empty and stays empty. No package is added today.
- [ ] `uv run python days/day-74-live-api-streaming/lab/gate.py; echo "exit: $?"` is **red** on all
      six checks before you write anything.
- [ ] You read `_fake.py` first, and can say what the `stream` argument changes about what it yields.

## Section 1 — the blank screen

- [ ] **1.1** read · you can state what streaming changes and what it does not, without using the
      word *faster*
- [ ] **1.2** read · you found the `stream=run_config.streaming_mode == StreamingMode.SSE` line in
      the installed package **yourself**, and recorded the version you found it in (P8)
- [ ] **1.3** read · ran `modes.py` and `modes.py --none` · recorded **6 events against 1** and
      **13% against 100%** of the answer needed before the first render

## Section 2 — the final chunk

- [ ] **2.1** read · ran `partials.py` · recorded **180 characters against an answer of 90** · can
      say why nothing raised
- [ ] **2.2** read · can state both correct rules and say which you would use, and what happens to
      each when the turn does not finish
- [ ] **2.3** read · you can name three things other than text that arrive as partials, and say what
      a text-only renderer does with them

## Section 3 — the wire

- [ ] **3.1** read · ran `wire.py` · read the bytes it printed and can say what ends a message
- [ ] **3.2** read · ran `wire.py --naive` · recorded **90 characters sent, 77 received** and
      **exit 1** · can say why the lost text was not an error
- [ ] **3.3** read · you can name two things between your process and the reader that would defeat
      the stream without changing your code

## Section 4 — the bill for voice

- [ ] **4.1** read · ran `livecheck.py` · recorded the required argument of `run_live` and the
      **11** live-only `RunConfig` fields, against the ADK version you have installed
- [ ] **4.2** read · 🅿️ you opened <https://ai.google.dev/gemini-api/docs/live-api> **in a browser**
      and wrote down what it says about the free tier on your date — because the served HTML does not
      contain it and this day's page could not verify it (P7)

## Section 5 — in production

- [ ] **5.1** read · ran `cancel.py` and `cancel.py --finish` · recorded **2 consumed / 1 stored**
      against **6 consumed / 2 stored** · saw `Root node desk was cancelled.` on stderr yourself
- [ ] **5.2** read · you can name what a reconnecting client sends and what the server has to keep
      for it to work

## The paper — read it last

- [ ] `papers/01-response-time.md` read **after** the parts, not before
- [ ] Ran the demo both ways from `lab/papers/response-time/`: streaming leaves **0 of 4** turns
      outside the goal band (exit 0); `--off` leaves **3 of 4** (exit 1), with the total time
      **identical at 25.20s** in both runs
- [ ] You noticed that `SECONDS_PER_TOKEN` is a stated **assumption** and not a measurement, and can
      say why the comparison is still valid
- [ ] You can name the three thresholds and say which one the demo's exit code is checking

## Build brief

- [ ] `sutra/stream.py` written: `collect(events)` that reads `event.partial`, `answer(..., mode)`
      with the mode as a parameter, and a `frame(chunk)` that splits on newlines
- [ ] You chose between partials-only and final-only and wrote the reason in the docstring
- [ ] You decided what happens when the client disconnects mid-turn, and wrote it down
- [ ] `tests/test_stream.py` written, including the answer-once test and the newline round-trip
- [ ] `uv run python gate.py; echo "exit: $?"` re-run · you can say which of the six cleared

## Repo hygiene

- [ ] `./m depth 74` green — thirteen parts and one paper
- [ ] `./m trace` green, and ADK-52 and ADK-53 close on this day and no others
- [ ] `./m wiki` run, so `docs/WIKI.md` and `docs/wiki/day-74.md` are not stale
- [ ] `uv run ruff format --check days/day-74-live-api-streaming` clean
- [ ] `uv run ruff check days/day-74-live-api-streaming/lab` clean
- [ ] `docs/PROGRESS.md` row appended verbatim from §11, with the real commit hash and the `⚠️` the
      gate actually earned — no rounding up (P10)
- [ ] `docs/PAPERS.md` row for `doi:10.1145/1476589.1476628` present and dated (P7, §17.4.1)
