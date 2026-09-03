---
day: 22
phase: 3
phase_name: "State, context & discipline"
title: "Structured logging — every turn tells its story"
ids: ["OPS-04"]
principles: [1, 2, 3, 8, 9, 10, 11, 12, 15, 16, 17, 18]
kind: lab
plan_version: "v2.2.1"
parts: 12
generated: "2026-09-03"
status: written
lab_scaffolded: false
commit: ""
---

# Day 22 — Structured logging: every turn tells its story

> **Yesterday (Day 21):** errors surface instead of being swallowed, and a plugin classifies,
> substitutes and escalates. It announced all of that with `print()`, and Day 21's own
> [2.4](../day-21-errors-surface-not-swallow/parts/02-four-hooks/2.4-the-ladder.md) said the debt out
> loud: *anything you rescue at rung one has to be counted at rung one.*
> **Today:** the counting. One JSON object per line, written by stdlib `logging`, with a correlation
> id on every line — including the failure line, whose hook does not obviously offer one. You will
> also leak a customer's email into a log file on purpose and then stop it.
> **Tomorrow (Day 23):** testing agents — unit tests for tools and callbacks, which assert against
> exactly the lines you write today.

---

## §1 Where we are

The smoke detector story from yesterday had a sequel nobody tells.

The battery got replaced. The detector works. And it is the only thing in that house that keeps a
record of nothing at all — it beeps when there is smoke, and if you ask it whether it beeped last
Tuesday, or how many times this month, or which room, it has no answer, because a beep is a message
to whoever is in the hall and not a record of anything.

That is where Sutra is this morning. Yesterday's plugin *knows* when a tool fails. What it does with
the knowledge is shout it at a terminal that will be closed by Thursday.

Four things worth knowing before you start.

**A print answers none of the questions you will actually ask.** Five real questions — how many
before lunch, which tool, which conversation, retry or substitute, same customer as last time — and
a well-written `print` answers zero of them without a human reading it. The same news as ten JSON
fields costs 249 characters against 54, and that is the whole trade.

**Timestamps do not order a log.** Forty lines written in a tight loop landed in **one or two distinct
milliseconds**, so sorting by time returned `step_10` first. This is the second time in three days the
clock has been too coarse — [Day 20](../day-20-context-engineering-compaction/LESSON.md)'s compaction
trigger hit the same wall — and one integer per line fixes it.

**One line controls ADK's own logging.** Every logger inside ADK is `google_adk.<module>`, 205 of
them, so `logging.getLogger("google_adk").setLevel(...)` took a run's captured records from **8 to 0**
with Sutra's own log untouched at 1,235 bytes. That is the `grep -v` you have been typing since Day 20,
made permanent.

**And a log file is a copy of your data.** One `detail` field carrying a database driver's exception
put a customer's email address and a bearer token on disk. A nine-line filter removed both and cost 39
bytes.

---

## §2 The map

Twelve parts in four sections, and **one paper**. The day climbs
`foundation → working → production`: section 1 is the line itself, section 2 wires it to a real run,
section 3 is the failure lab, and section 4 is what changes when the log gets big.

**Read the paper last.** *Time, clocks, and the ordering of events in a distributed system*
(`doi:10.1145/359545.359563`) is the 1978 answer to the problem
[1.4](parts/01-a-line-you-can-query/1.4-timestamps-are-not-an-order.md) leaves open — a counter works
inside one process, and Sutra is about to have several. Principle 4 at the scale of a day.

### Section 1 — `01-a-line-you-can-query`: what a log line is

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [A print is not a log](parts/01-a-line-you-can-query/1.1-a-print-is-not-a-log.md) | Five questions, five `no`s | `foundation` |
| 1.2 | [One JSON object per line](parts/01-a-line-you-can-query/1.2-one-json-object-per-line.md) | Thirty lines of stdlib, four fields for free | `working` |
| 1.3 | [Levels are a routing decision](parts/01-a-line-you-can-query/1.3-levels-are-routing.md) | Who reads it, not how bad it is | `working` |
| 1.4 | [Timestamps are not an order](parts/01-a-line-you-can-query/1.4-timestamps-are-not-an-order.md) | Forty lines, one millisecond | `working` |

### Section 2 — `02-wiring-the-run`: attaching it to a real invocation

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [One line per happening](parts/02-wiring-the-run/2.1-one-line-per-happening.md) | Six lines, one complete account of a turn | `working` |
| 2.2 | [The correlation id, and the hook that hides it](parts/02-wiring-the-run/2.2-the-correlation-id.md) | The failure line's id comes from somewhere else | `working` |
| 2.3 | [ADK logs too, and one line controls all of it](parts/02-wiring-the-run/2.3-adk-logs-too.md) | 8 records against 0, from one `setLevel` | `working` |

### Section 3 — `03-failure-lab`: the deliberate failures

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [💥 The log that leaked](parts/03-failure-lab/3.1-the-log-that-leaked.md) | Two secrets on disk, in 231 bytes | `production` |
| 3.2 | [💥 The line nobody can correlate](parts/03-failure-lab/3.2-the-line-nobody-can-correlate.md) | *Unanswerable*, from a log that looks healthy | `production` |

### Section 4 — `04-in-production`: when the log gets big

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [What to log and what to count](parts/04-in-production/4.1-what-to-log-and-what-to-count.md) | 6.15 GB a day, and the questions that need a number | `production` |
| 4.2 | [A log file only grows](parts/04-in-production/4.2-a-log-file-only-grows.md) | Bounded at 6,445 bytes, and 96 lines deleted | `production` |
| 4.3 | [Testing that you logged](parts/04-in-production/4.3-testing-that-you-logged.md) | Eight green, three red, one useful message | `production` |

### The paper — read after the parts

| # | Paper | What it answers | Level |
| --- | --- | --- | --- |
| 01 | [Time, clocks, and the ordering of events in a distributed system](papers/01-time-clocks-ordering.md) | `doi:10.1145/359545.359563` — ordering without a clock | `production` |

---

## §3 Setup — run this

**No new packages today.** Python's stdlib `logging` is the whole toolbox, which is CLAUDE.md's
*prefer the stdlib* rule getting an easy win. `docs/PAPERS.md` gains one row (§11).

```bash
# 1 - ignore the log directory BEFORE you create it
grep -q '^logs/' .gitignore || printf 'logs/\n' >> .gitignore
git check-ignore -v logs/sutra.jsonl     # must print a matching rule

# 2 - the day folder's lab, and the paper's demo folder
cd days/day-22-structured-logging
mkdir -p lab/papers/time-clocks-ordering
cd lab

# 3 - the eleven lab scripts, in reading order
touch print_vs_log.py jsonl.py levels.py ordering.py
touch log_the_run.py adk_own_logs.py
touch leaked.py no_correlation.py
touch what_to_count.py rotation.py test_logging_demo.py

# 4 - the paper's two-file demo
touch papers/time-clocks-ordering/clock.py papers/time-clocks-ordering/run.py
cd -

# 5 - what changes under sutra/ and tests/ today
ls sutra/                    # logging_setup.py is new; plugins.py gains the Flight recorder
ls tests/                    # test_logging.py is the eval
```

**Step 1 is not optional and it is first for a reason.** `logs/` will contain a customer's email
address by the time you reach
[3.1](parts/03-failure-lab/3.1-the-log-that-leaked.md), and a log file committed to a repository that
goes public in Phase 14 is the worst possible version of that part's lesson. `git check-ignore -v`
prints the rule that matched, so it is a check rather than a hope.

The paper's demo runs from inside its own folder because `run.py` imports `clock` by bare name. The
scripts are listed in reading order, which is the order the parts introduce them.

**Run `print_vs_log.py` first.** It is the argument for the whole day in one table, it takes no
setup, and it costs nothing.

**Nothing today needs a key.** Logging is pure computation over a `LogRecord`, and the two ADK scripts
use the recording models from Day 21. The whole day, including the test suite and the paper's demo,
runs offline.

**`sutra/logging_setup.py` is new**; `sutra/plugins.py` is **extended, not replaced** — Day 14's
plugin and Day 21's error policy both stay, and the recorder is a *second* plugin beside them (§4).

---

## §4 Build brief

**`sutra/logging_setup.py`** — new:

| Symbol | What it is | Taught in |
| --- | --- | --- |
| `JsonLines` | the `logging.Formatter` subclass; four fields for free | 1.2 |
| `Scrub` | the `logging.Filter` that removes known secret shapes | 3.1 |
| `SECRETS` | the pattern list, shared by the filter and the tests | 3.1, 4.3 |
| `get_logger(name)` | idempotent; sets the handler, the formatter and `propagate = False` | 1.2 |
| `configure(level, adk_level)` | called once at startup; sets both hierarchies | 1.3, 2.3 |

**`sutra/plugins.py`** — extended with a `Flight` recorder: `before_run`, `on_event`,
`on_tool_error`, `after_run`, one line each, **returning `None` from every hook**. It goes in
`plugins=[Flight(...), Policy(...)]` beside Day 21's policy — two objects, because a recorder that can
decide can corrupt the record of what was decided (2.1).

**`tests/test_logging.py`** — new. Eight cases, no key; see §5.

**`TODO(me)` markers left for you:**

- **1.2** — decide whether `event` or `message` is the right name for the first field, and write one
  sentence defending your choice. It is an interface with consumers from Day 23 onwards.
- **1.3** — set Sutra's two thresholds from environment variables, then log the assembled prompt at
  `DEBUG` and confirm it is absent at `INFO` and present at `DEBUG`.
- **1.4** — add `seq` to `JsonLines` itself rather than passing it per call, so no call site can
  forget. Then say what happens to it across a process restart, and whether that matters.
- **2.2** — grep your own plugin for every `log.` call and confirm each one carries an
  `invocation_id`. The tool-error hook is the one to check twice.
- **3.1** — add a fourth entry to `SECRETS` for something a *Sutra* tool could leak, write the
  exception that would carry it, and confirm the filter catches it. Then write one that defeats all
  four.
- **3.2** — attach the id via a `contextvars.ContextVar` and a filter instead of per call site, so it
  is structurally impossible to omit.
- **4.1** — count Sutra's own lines per run and bytes per line, and redo the projection with your
  numbers rather than the ones in the file.
- **4.3** — write the **integration** test the parts admit is missing: run one invocation, read the
  file, assert six lines sharing one `invocation_id`. No key needed.
- **The paper** — set both `skew_ms` values to `0` and run the `LOGICAL=0` arm. It passes. Say why
  that is the trap rather than the fix.

---

## §5 The eval that must be able to fail

Six tests, **eight cases** (one is parametrised over three secret shapes), no key and no network. All
are shown with their walkthrough in
[4.3](parts/04-in-production/4.3-testing-that-you-logged.md).

They assert four things about a line — that it is one JSON object with no embedded newline, that the
four required fields are always present, that every `extra` field arrives, and that an unserialisable
value cannot make the logging call raise — plus one per secret shape, that the scrub still works.

**How to watch it go RED before it goes green:**

```bash
uv run python -m pytest tests/test_logging.py -q -m "not live"   # RED: no sutra/logging_setup.py yet
# ... write the symbols from §4 ...
uv run python -m pytest tests/test_logging.py -q -m "not live"   # green
```

Then break it on purpose. Measured on 2026-09-03, by deleting the one line in `JsonLines.format` that
copies `extra` into the payload:

| Break this | Which cases go red | What it is telling you |
| --- | --- | --- |
| `payload.update({...})` for `extra` | three of eight | the fields are the whole point (1.2) |
| a pattern in `SECRETS` | one of the three scrub cases | which pattern, by name (3.1) |
| `default=str` in `json.dumps` | the unserialisable case | logging can now break the run (1.2) |

**And the finding that came out of writing that table:** two of the three red messages were bare
`KeyError: 'tool'` and `KeyError: 'obj'`, while the third said
*"a failure line with no invocation_id cannot be correlated"*. The difference is `line["tool"]` versus
`line.get(...)` with a message — and it is **four consecutive days** on which deliberately failing a
green suite has exposed a weak assertion. Day 19 found two, Day 20 a `StopIteration`, Day 21 a bare
`assert False`, today two `KeyError`s. **Running the suite red is how you review the suite.**

**What this suite does not catch, and the parts say so:** all eight cases pass in a system where the
plugin was never installed and the log file is empty. The integration test in §4's `TODO(me)` list is
the one that catches that.

---

## §6 Request budget

**Free-tier Gemini**, 20 generate requests per day per model.

| What | Generations |
| --- | --- |
| nine pure-Python lab scripts | **0** |
| `log_the_run.py` and `adk_own_logs.py` (recording models) | **0** |
| the test suite, eight cases | **0** |
| the paper's demo, both arms | **0** |
| **Total required** | **0 of 20** |

**Zero, for the second day running.** Logging is computation over a `LogRecord` — there is nothing to
ask a model. The two scripts that involve ADK use Day 21's recording models, and the paper's demo has
no model, no network and no dependency beyond the stdlib.

The one thing in this day that cost a request was captured on a previous day and reused: the database
exception in [3.1](parts/03-failure-lab/3.1-the-log-that-leaked.md) is realistic rather than real, but
the 429 body quoted in Day 21 and the model roster in Day 20 were both live. Capturing an artefact
once and keeping it as a fixture is the right way to spend quota.

**Cost: $0.**

---

## §7 Traps

- **`logs/` must be gitignored before the first run**, and §3 checks it with `git check-ignore`. By
  [3.1](parts/03-failure-lab/3.1-the-log-that-leaked.md) that directory contains a customer's email
  address, and this repository goes public in Phase 14.
- **A duplicated handler doubles every line**, silently. `logging.getLogger` returns the *same* object
  every call, so `get_logger` without an `if not logger.handlers` guard writes twice and every metric
  derived from the log is exactly twice as high (1.2).
- **A level lives in two places.** The logger *and* each handler, and a record must clear both. Worse,
  `log.isEnabledFor(WARNING)` consults only the logger — it returned `True` while the handler was
  discarding every warning (1.3).
- **`extra={"name": ...}` raises.** `KeyError: "Attempt to overwrite 'name' in LogRecord"`, and the
  same for `msg`, `args`, `levelname`, `module`, `filename`, `lineno`. Prefer `user_id` over `name`
  (1.2).
- **Delete the log file *before* creating the logger.** On Windows an open `FileHandler` holds a lock:
  `PermissionError: [WinError 32] The process cannot access the file because it is being used by
  another process` (2.1).
- **`on_tool_error_callback` gets no `invocation_context`.** The id comes from
  `tool_context.invocation_id` — and in `google-adk` 2.7.1 `ToolContext` and `CallbackContext` are both
  the same `Context` class (2.2).
- **`google-adk` has an underscore.** `logging.getLogger("google-adk")` does not fail; it creates a
  new, unrelated logger and governs nothing, silently (2.3).
- **Set the ADK level *before* importing anything that uses ADK.** It logs during import and during
  `App` construction, so a late `setLevel` loses records and still prints a number (2.3).
- **Rotation is deletion.** `RotatingFileHandler` bounded 200 lines to four files and discarded 96 of
  them, oldest first, with nothing in the log saying so (4.2).
- **Ids never go in metric labels.** An unbounded label turns a fixed-cost counter into a per-event
  cost with extra steps (4.1).

---

## §8 Verify before you code

Fetched or read on **2026-09-03**, the day this was written:

- The installed `google-adk` 2.7.1 source, `google/adk/plugins/base_plugin.py` — the
  `on_event_callback`, `before_run_callback` and `after_run_callback` signatures, and the fact that
  `on_event_callback` may return an `Event` to modify what is persisted.
- The same tree, counted: **205** call sites of `getLogger("google_adk." + __name__)` and no logger
  created any other way. That count is the evidence for
  [2.3](parts/02-wiring-the-run/2.3-adk-logs-too.md)'s claim.
- `google/adk/agents/context.py` — that `ToolContext` and `CallbackContext` both resolve to `Context`,
  and that it exposes `invocation_id`, `user_id`, `agent_name`, `session`, `state`, `function_call_id`,
  `branch` and `run_id`.
- Python's own `logging` and `logging.handlers` behaviour, checked by running it rather than read: the
  `LogRecord` built-in attribute set, the `KeyError` on a colliding `extra` key, the logger-versus-
  handler level split, and `logging`'s handler-error reporting compared with `print` raising.
- `https://api.crossref.org/works/10.1145/359545.359563` — the paper's exact title, journal, volume,
  pages and year, from the machine-readable record rather than from memory (§17.4.1 rule 5).

**No adk.dev page was needed today**, and saying so is the honest version of Principle 8: today's
subject is the standard library, and the two ADK facts used are both in the installed source where
they can be counted rather than trusted.

---

## §9 Say it in an interview

"Our agent's error handling was solid and completely unobservable. The plugin knew when a tool failed
and announced it with a `print`, so a week later nobody could answer *how many times, which
conversation, which customer*. That's the gap structured logging closes, and it's about thirty lines
of stdlib — a `logging.Formatter` subclass that returns `json.dumps` of a dict built from the record.

Three things I'd tell anyone doing it. Put a correlation id on **every** line, and check the failure
lines specifically: in ADK the tool-error hook isn't handed an invocation context, so five of our six
lines got the id the easy way and the failures were orphaned until we pulled it off `tool_context`.
Don't trust the timestamp for ordering — we wrote forty lines in a tight loop and they landed in one
or two milliseconds, so sorting by time gave us step 10 first; a monotonic counter per line fixes it,
and across processes you need the counter to travel with the request, which is Lamport's rule from
1978 and is what a trace context actually is.

And treat the log as a copy of your data. One `detail` field holding a database driver's exception put
a customer's email address and a bearer token on disk, because the driver helpfully includes the
statement and its parameters. A nine-line `logging.Filter` removed both and cost thirty-nine bytes —
but the stronger defence is an allowlist of fields, because a redaction filter is a blocklist and the
first unfamiliar exception format defeats it.

The whole thing tests offline, which surprised me — logging is pure computation over a `LogRecord`.
When I broke the formatter on purpose, three of eight cases went red and only one of the three had a
message worth reading. That's been true every day this week."

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked and `./m depth 22` is green. Defined by
understanding and green checks, never by elapsed time — a part is finished when you could explain it
to someone else without the page open.

---

## §11 Ledger & commit

**`docs/PROGRESS.md`** — append:

```text
| 22 | <date> | OPS-04 | 12 (+1 paper) | <hash> | ✅ |
```

**`docs/PACKAGES.md`** — no new rows. Nothing was installed today.

**`docs/PAPERS.md`** — append:

```text
| Time, clocks, and the ordering of events in a distributed system | doi:10.1145/359545.359563 | 1978 | 2026-09-03 | 22 | `days/day-22-structured-logging/papers/01-time-clocks-ordering.md` |
```

**`.gitignore`** — one line, added in §3 before anything ran:

```text
logs/
```

**`docs/SKILL_PROVENANCE.md`** — no new rows. No skills were sourced today.

**The commit:**

```text
day 22: structured logging - every turn tells its story - closes OPS-04
```
