# Day 22 — CHECKLIST

**IDs closed:** OPS-04
**Principles served:** 1, 2, 3, 8, 9, 10, 11, 12, 15, 16, 17, 18
**Parts:** 12 across 4 sections, plus 1 paper

> `./m done 22` refuses to commit while any box below is unticked. It cannot tell whether you were
> honest — that part is yours.

## Demo command

```bash
# logs/ must be ignored BEFORE anything writes to it
git check-ignore -v logs/sutra.jsonl

cd days/day-22-structured-logging/lab
uv run python print_vs_log.py                    # 0 generations
uv run python jsonl.py                           # 0 generations
THRESHOLD=INFO  uv run python levels.py          # 0 generations
THRESHOLD=DEBUG uv run python levels.py          # 0 generations
SEQ=0 uv run python ordering.py                  # 0 generations
SEQ=1 uv run python ordering.py                  # 0 generations
FAIL=1 uv run python log_the_run.py              # 0 generations
FAIL=0 uv run python log_the_run.py              # 0 generations
VERBOSE=0 uv run python adk_own_logs.py          # 0 generations
VERBOSE=1 uv run python adk_own_logs.py          # 0 generations
REDACT=0 uv run python leaked.py                 # 0 generations
REDACT=1 uv run python leaked.py                 # 0 generations
CORRELATE=0 uv run python no_correlation.py      # 0 generations
CORRELATE=1 uv run python no_correlation.py      # 0 generations
uv run python what_to_count.py                   # 0 generations
ROTATE=0 uv run python rotation.py               # 0 generations
ROTATE=1 uv run python rotation.py               # 0 generations
uv run python -m pytest test_logging_demo.py -q
cd papers/time-clocks-ordering
LOGICAL=0 uv run python run.py                   # 0 generations
LOGICAL=1 uv run python run.py                   # 0 generations
cd -
uv run python -m pytest tests/test_logging.py -q -m "not live"
./m check && uv run python scripts/trace.py && git log --oneline -1
```

Expected: five questions and five `no`s; four JSON lines sharing one millisecond; five of six
happenings kept at `INFO`; **40 lines in 1–2 distinct timestamps** and `step_10` first without a
counter; **six log lines with one shared `invocation_id`**, then five; **8 ADK records against 0**
with our log at 1,235 bytes either way; two secrets on disk, then none; *unanswerable*, then
*no (3 lines)*; 6.15 GB/day at five million runs; 200 lines bounded to 6,445 bytes with 96 gone; then
`8 passed`; then the reply ordered **before** the request by physical clocks and after it by logical
ones. Then `OK all green`, then `traceability: 41/199 closed, 0 problem(s)`, then one commit.

## Setup

- [ ] `logs/` added to `.gitignore` **before** the first run, and `git check-ignore -v` printed the
      matching rule
- [ ] `days/day-22-structured-logging/lab/` exists with the eleven scripts
- [ ] `lab/papers/time-clocks-ordering/` exists with `clock.py` and `run.py`
- [ ] No `uv add` was needed — confirmed the stdlib is the whole toolbox
- [ ] Confirmed the whole day runs with **no `GOOGLE_API_KEY` set at all**

## Section 1 — `01-a-line-you-can-query`

- [ ] **1.1** read · ran `print_vs_log.py` · said out loud three things a log line has that a print
      does not, and the question that tells them apart
- [ ] **1.2** read · ran `jsonl.py` · **triggered the `KeyError` by passing `extra={"name": ...}`** ·
      said out loud the four fields the formatter supplies and what `extra=` does
- [ ] **1.3** read · ran both `levels.py` thresholds · said out loud the question that separates
      `WARNING` from `ERROR`, and what a level does *not* change
- [ ] **1.4** read · ran both `ordering.py` arms · **saw 40 lines share one or two timestamps** ·
      deleted the `shuffle` line and watched the broken arm report success · said out loud the three
      reasons a timestamp cannot order a log

## Section 2 — `02-wiring-the-run`

- [ ] **2.1** read · ran both `log_the_run.py` arms · **saw six lines, then five** · said out loud the
      four hooks and why a recorder returns `None` from all of them
- [ ] **2.2** read · confirmed the `tool_error` line carries the same id as the other five · deleted
      `tool_context.invocation_id` and confirmed nothing warned · said out loud which hook has no
      invocation context
- [ ] **2.3** read · ran both `adk_own_logs.py` arms · **saw 0 records against 8** · said out loud the
      name that governs every ADK logger and what `propagate = False` protects

## Section 3 — `03-failure-lab`

- [ ] **3.1** read · ran `REDACT=0 leaked.py` and **read a customer's email address out of a file on
      disk** · said out loud the audience for a log file and the defence stronger than redaction
- [ ] **3.2** read · ran both `no_correlation.py` arms · **tried to answer the question from the
      uncorrelated file with `grep` and failed** · said out loud which question an uncorrelated log
      still answers correctly

## Section 4 — `04-in-production`

- [ ] **4.1** read · ran `what_to_count.py` · said out loud the rule for choosing a line or a number,
      and the field that must never be a metric label
- [ ] **4.2** read · ran both `rotation.py` arms · **saw 104 lines of 200 survive** · said out loud
      the ceiling formula and the one deployment where you would not rotate
- [ ] **4.3** read · ran `test_logging_demo.py` green · said out loud the four things worth asserting
      and what the whole suite fails to notice

## The paper — read after the parts

- [ ] **`papers/01-time-clocks-ordering.md`** read · ran both demo arms and **watched the reply be
      ordered before the request**
- [ ] Traced IR2 by hand: the desk's counter went from 0 to 3, and you can say why it skipped 1 and 2
- [ ] Set both `skew_ms` to `0`, ran the `LOGICAL=0` arm, saw it pass, and can say why that is the trap
- [ ] Answered out loud: *what did this paper actually claim, and what do we do differently now?*
- [ ] Named one thing from it in use today and one thing the field replaced

## Build brief

- [ ] `sutra/logging_setup.py` written: `JsonLines`, `Scrub`, `SECRETS`, `get_logger`, `configure`
- [ ] `get_logger` is idempotent — checked by calling it twice and confirming one handler
- [ ] `propagate = False` set, and confirmed by seeing no duplicate lines on the terminal
- [ ] `default=str` present in `json.dumps`, and confirmed by logging an `object()`
- [ ] `seq` supplied by the formatter, not per call site, so no call site can forget it
- [ ] `Scrub` attached where it sees **every** line, including anything logged under `google_adk`
- [ ] `sutra/plugins.py` extended with a `Flight` recorder that returns `None` from every hook
- [ ] `Flight` and Day 21's `Policy` are **two objects** in `plugins=[...]`, not one merged class
- [ ] Every `log.` call in `sutra/` carries an `invocation_id` — the tool-error hook checked twice
- [ ] Day 14's plugin behaviour and Day 21's error policy both still present and unchanged
- [ ] `git diff` reviewed before committing

## The eval that must be able to fail

- [ ] `tests/test_logging.py` written; the whole file passes with no key and no network
- [ ] Watched it RED **before** writing `sutra/logging_setup.py`, not after
- [ ] **Broke it on purpose:** deleted the `extra` copy in `JsonLines.format` — three of eight red
- [ ] **Broke it a second way:** removed a pattern from `SECRETS` — one scrub case red, by name
- [ ] **Broke it a third way:** removed `default=str` — the unserialisable case red
- [ ] Compared the three failure messages and improved at least one bare `KeyError` into a message
      you would want at 2am
- [ ] Wrote the **integration** test the parts admit is missing: one invocation, six lines, one
      shared `invocation_id`
- [ ] Fixed everything; suite green again

## Request budget

- [ ] Total generations for the day: **0 of 20**
- [ ] Confirmed by running the whole demo command with no `GOOGLE_API_KEY` in the environment
- [ ] `logs/` is still ignored, and `git status` shows no log file

## Ledger

- [ ] `docs/PROGRESS.md` row appended:
      `| 22 | <date> | OPS-04 | 12 (+1 paper) | <hash> | ✅ |`
- [ ] `docs/PAPERS.md` row appended:
      `| Time, clocks, and the ordering of events in a distributed system | doi:10.1145/359545.359563 | 1978 | 2026-09-03 | 22 | days/day-22-structured-logging/papers/01-time-clocks-ordering.md |`
- [ ] `.gitignore` carries `logs/`
- [ ] `docs/PACKAGES.md` — confirmed no new rows are needed
- [ ] `./m depth 22` green
- [ ] `./m trace` shows OPS-04 closed, `41/199`, 0 problems
- [ ] `./m check` green

## Commit

- [ ] `day 22: structured logging - every turn tells its story - closes OPS-04`
