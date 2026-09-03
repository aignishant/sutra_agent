# Day 22 - Structured logging — every turn tells its story

IDs closed: OPS-04 · source: `days/day-22-structured-logging/`

## Parts

### 1.1 - A print is not a log
`days/day-22-structured-logging/parts/01-a-line-you-can-query/1.1-a-print-is-not-a-log.md` · level `foundation` · ids OPS-04

print("[safety_net] kb lookup failed for KB-104") and a ten-field JSON line carry the same news, and only one of them can answer how many times before lunch — five questions, and the print answers none of them without a human reading it.

### 1.2 - One JSON object per line
`days/day-22-structured-logging/parts/01-a-line-you-can-query/1.2-one-json-object-per-line.md` · level `working` · ids OPS-04

A logging.Formatter subclass that returns json.dumps(...) turns every call to log.info(..., extra={...}) into one machine-readable line in a file — about thirty lines of stdlib, no dependencies, and the four fields nobody has to remember.

### 1.3 - Levels are a routing decision
`days/day-22-structured-logging/parts/01-a-line-you-can-query/1.3-levels-are-routing.md` · level `working` · ids OPS-04

A level is not an opinion about how bad something is — it is the answer to who should find out, and at the default INFO threshold five of six happenings are written and the sixth is silently discarded.

### 1.4 - Timestamps are not an order
`days/day-22-structured-logging/parts/01-a-line-you-can-query/1.4-timestamps-are-not-an-order.md` · level `working` · ids OPS-04

Forty log lines written in a tight loop landed in one or two distinct milliseconds, so sorting the file by timestamp did not recover the order they happened in — and a monotonic counter, one extra field, did.

### 2.1 - One line per happening
`days/day-22-structured-logging/parts/02-wiring-the-run/2.1-one-line-per-happening.md` · level `working` · ids OPS-04

Four plugin hooks — before_run, on_event, on_tool_error, after_run — produce a complete six-line record of one invocation, and the plugin that writes them decides nothing: it is a flight recorder, not a policy.

### 2.2 - The correlation id, and the hook that hides it
`days/day-22-structured-logging/parts/02-wiring-the-run/2.2-the-correlation-id.md` · level `working` · ids OPS-04

Every line needs the same invocation_id or the log is a pile rather than a record — and the one hook that most needs it, on_tool_error_callback, is handed no invocation context, so the id has to come from tool_context.invocation_id.

### 2.3 - ADK logs too, and one line controls all of it
`days/day-22-structured-logging/parts/02-wiring-the-run/2.3-adk-logs-too.md` · level `working` · ids OPS-04

Every logger inside ADK is named google_adk.<module> — 205 call sites of it — so logging.getLogger("google_adk").setLevel(...) is the whole control surface: ERROR captured 0 records from a run and DEBUG captured 8, from three modules, with Sutra's own log untouched at 1,235 bytes either way.

### 3.1 - 💥 The log that leaked
`days/day-22-structured-logging/parts/03-failure-lab/3.1-the-log-that-leaked.md` · level `production` · ids OPS-04

One detail field carrying a database driver's exception put a customer's email address and a bearer token into a log file on disk — two secrets in 231 bytes — and a nine-line logging.Filter removed both while keeping everything an operator needs.

### 3.2 - 💥 The line nobody can correlate
`days/day-22-structured-logging/parts/03-failure-lab/3.2-the-line-nobody-can-correlate.md` · level `production` · ids OPS-04

Two conversations at once, seven lines in one file, one of them a failure: with a correlation id the question "did priya's request fail?" is answered no, from three lines; without it, the honest answer is unanswerable — and the file looks identically healthy either way.

### 4.1 - What to log and what to count
`days/day-22-structured-logging/parts/04-in-production/4.1-what-to-log-and-what-to-count.md` · level `production` · ids OPS-04

A log answers what happened to this one and a counter answers how often — three of five real questions need a specific line and two need a number, and at five million runs a day the lines are 6.15 GB while the counters are the same size they were at twenty runs.

### 4.2 - A log file only grows
`days/day-22-structured-logging/parts/04-in-production/4.2-a-log-file-only-grows.md` · level `production` · ids OPS-04

RotatingFileHandler bounded 200 lines to 6,445 bytes across four files — and silently discarded 96 of them, including the first line ever written, which is the trade it makes and does not mention.

### 4.3 - Testing that you logged
`days/day-22-structured-logging/parts/04-in-production/4.3-testing-that-you-logged.md` · level `production` · ids OPS-04

Eight cases assert that the line is one JSON object, carries its four required fields, keeps every extra, survives an unserialisable value, and has been scrubbed of three secret shapes — and breaking the formatter turns three of them red, two with a bare KeyError and one with a message that actually explains itself.

## Papers - read after the parts

### doi:10.1145/359545.359563 - Time, clocks, and the ordering of events in a distributed system
`days/day-22-structured-logging/papers/01-time-clocks-ordering.md`

It argued that physical clocks cannot order the events of a distributed system, defined an ordering built from what could have caused what, and showed that a single counter per process plus one rule for messages is enough to produce it.

