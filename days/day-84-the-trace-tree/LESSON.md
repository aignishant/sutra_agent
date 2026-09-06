---
day: 84
phase: 13
phase_name: "Observability & deployment"
title: "Tracing — the trace tree, and what ADK puts in it"
ids: ["ADK-63", "ADK-74", "OPS-16"]
principles: [1, 2, 7, 8, 9, 10, 11, 13, 15, 16, 17, 18]
kind: lab
plan_version: "v2.2.1"
parts: 13
generated: "2026-09-07"
status: written
lab_scaffolded: true
commit: ""
---

# Day 84 — Tracing: the trace tree, and what ADK puts in it

> **Yesterday (Day 83):** the Phase 12 gate came back **three pass, four fail and one that cannot be
> determined**. Its sharpest finding was that the trajectory rubric had been grading a transcript
> containing **zero of three** recorded tool calls — a judge asked about tool use, shown none.
> **Today:** Phase 13 opens, and the desk gets an instrument that produces that same information
> itself. One question becomes **ten spans, five levels deep**, emitted by ADK's own code at zero
> provider requests. Then the four things nobody tells you: the run that produced five events and no
> trace at all, the plugin that turns ten spans into sixty and eight thousand bytes into a hundred
> and thirty-three thousand, the batch processor that delivered **zero of ten**, and the customer's
> own sentence sitting in six span attributes by default.
> **Tomorrow (Day 85):** the API surface — `api_server` and FastAPI endpoints — which is where the
> first process boundary appears and the three identifiers have to start crossing it.

---

## §1 Where we are

The flat-pack wardrobe, and the two pieces of paper in the box.

One is a list of forty-one steps. You can follow it and have no idea what you are building, and if
step twenty-two goes wrong you cannot tell whether that was a door or a back panel, because a list
has no shape. The other is the exploded diagram: every piece drawn floating a little away from where
it belongs, with thin lines showing what goes into what. Nobody follows the diagram. You look at it
once at the start and again the moment something does not fit, and both times it answers the
question the list cannot — **which part is this a part of?**

Day 22 gave this desk logs. A log is the list: one line per event, in the order things finished,
which for nested work is close to the reverse of the order they started. An agent's work is nested
by construction — the runner invokes an agent, which calls a model, which asks for a tool, whose
result goes back — and how deep that goes is decided at run time by the model, so it is not in the
source and cannot be read off it.

Today the desk gets the diagram. And because ADK emits it, this day's measurements are not drawings
of what a trace *would* look like: `_desk.py` is a real `LlmAgent` behind a real `InMemoryRunner`,
with the Day 80 registry seam supplying a scripted model, so every span below came out of ADK's own
instrumentation at **zero provider requests**.

What comes out is a five-level tree in which the tool call sits under the model turn that asked for
it. What also comes out, once you look at where the spans go and what is written on them, is four
findings that each have the same shape as the last three days' — an instrument that is not installed
looks exactly like a world with nothing to report:

- **Zero spans, zero errors, zero warnings** from a run that produced five events and a correct
  answer, because no tracer provider was installed and every ADK instrumentation call begins with
  `if not span.is_recording(): return`.
- **Ten spans became sixty** and 8,051 bytes became 133,220 with `AutoTracingPlugin` fitted — six
  times the spans, sixteen and a half times the storage.
- **Zero of ten spans delivered** from a process that used `BatchSpanProcessor` and exited without
  calling `shutdown()`. The queue drains every five seconds or on shutdown; the desk finished in
  milliseconds.
- **Six span attributes carrying the customer's own sentence**, by default — plus twenty-one more
  under `adk.fn.*` when the automatic plugin is fitted with ADK's content switch already off,
  because the switch does not reach the plugin.

---

## §2 The map

Five sections. Section 1 is what a trace is and the state it is in before anybody turns it on.
Section 2 is what ADK writes and what it writes on it. Section 3 is where the spans go. Section 4 is
what that costs, in bytes and in exposure. Section 5 is reading one, and the list.

### 1 — What a trace is

*The tree, the three numbers that rebuild it, and the default state of every Python process.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [A trace is a tree, not a log](parts/01-what-a-trace-is/1.1-a-trace-is-a-tree.md) | Ten spans, five levels, and why a log is the deepest step first | `foundation` |
| 1.2 | [Three numbers make the tree](parts/01-what-a-trace-is/1.2-three-numbers-make-the-tree.md) | Rebuilt from a shuffled pile, and the forty-eight bytes that cross a boundary | `foundation` |
| 1.3 | [The run that left no trace](parts/01-what-a-trace-is/1.3-the-run-that-left-no-trace.md) | 💥 Five events, zero spans, zero warnings | `working` |

### 2 — What ADK records

*Three kinds of span, the attributes on them, and the plugin that adds fifty more.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [Agent, tool and model](parts/02-what-adk-records/2.1-agent-tool-and-model.md) | Why the tool span is a child of the model turn, and what nesting does to durations | `working` |
| 2.2 | [The attributes are a contract, half-kept](parts/02-what-adk-records/2.2-the-attributes-are-a-contract.md) | 37 of 68 portable, and a root span with none at all | `working` |
| 2.3 | [Every function in the tree](parts/02-what-adk-records/2.3-every-function-in-the-tree.md) | `AutoTracingPlugin`: ten spans to sixty, and one environment variable to zero | `production` |

### 3 — Where spans go

*Timing and destination are two decisions, and one of them loses everything on exit.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [A processor and an exporter](parts/03-where-spans-go/3.1-a-processor-and-an-exporter.md) | Which half decides *when* and which decides *where* | `working` |
| 3.2 | [A sink that outlives the process](parts/03-where-spans-go/3.2-a-sink-that-outlives-the-process.md) | `SqliteSpanExporter`, and the obvious query that returns seven of ten | `working` |
| 3.3 | [The queue that went with the process](parts/03-where-spans-go/3.3-the-queue-that-went-with-the-process.md) | 💥 Zero of ten delivered, one line apart from ten of ten | `production` |

### 4 — What a trace costs

*A different currency from every other cost in this curriculum.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [The bill is bytes, not requests](parts/04-what-a-trace-costs/4.1-the-bill-is-bytes.md) | 1.18 GB a year by default, 19.45 with the plugin, 0.62 with content off | `production` |
| 4.2 | [The prompt inside the span](parts/04-what-a-trace-costs/4.2-the-prompt-inside-the-span.md) | 💥 Six copies of the customer's sentence, and the switch that misses twenty-one more | `production` |

### 5 — In production

*Reading one when it matters, and the nine things that are missing.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [Reading a trace when something failed](parts/05-in-production/5.1-reading-a-trace.md) | 142 lines of traceback against five spans, and why three say `ERROR` | `production` |
| 5.2 | [What a real tracing setup adds](parts/05-in-production/5.2-what-to-pin-above-the-till.md) | Nine items, three of which are the same function | `production` |

### Papers — read after the parts

| # | Paper | What it gives this day |
| --- | --- | --- |
| 01 | [The trace tree at scale](papers/01-the-trace-tree-at-scale.md) | `Google Technical Report dapper-2010-1` — the span tree, propagation through common libraries, root sampling and out-of-band collection. The demo keeps eleven per cent of the spans with **zero** incomplete traces; the ablation keeps everything, and both arms show head sampling losing half the failures |

---

## §3 Setup — run this

```bash
mkdir -p days/day-84-the-trace-tree/lab/papers/dapper
cd days/day-84-the-trace-tree/lab
touch _desk.py _otel.py
touch tree.py ids.py norecord.py attrs.py auto.py
touch sink.py flush.py cost.py leak.py answer.py gate.py
touch papers/dapper/sampling.py papers/dapper/demo.py
```

**No package is added today.** `git diff pyproject.toml uv.lock` must be empty and stay empty.
`opentelemetry-api` and `opentelemetry-sdk` are already installed, as transitive dependencies of
`google-adk==2.7.1` — verified with `uv run python -c "import importlib.metadata as m;
print(m.version('opentelemetry-sdk'))"` on 2026-09-07, which printed `1.42.1`.

**What each file is for:**

- `_desk.py` is the file to read first: a real `LlmAgent` with two real tools and a `ScriptedDesk`
  registered through `LLMRegistry`, so ADK's runner, flows, tool executor and telemetry all run
  unmodified and nothing calls a provider.
- `_otel.py` is the one place a tracer provider is installed, because installing one is global and
  one-shot. It also holds the tree walk every script shares.
- `tree.py`, `ids.py`, `norecord.py` are section 1; `attrs.py`, `auto.py` are section 2; `sink.py`,
  `flush.py` are section 3; `cost.py`, `leak.py` are section 4; `answer.py` is section 5.
- `gate.py` is the day's eval against `sutra/tracing.py`.
- `papers/dapper/` holds the paper's demo: `sampling.py` is head sampling and nothing else.

Every script is its own process, deliberately. Confirm why before you start:

```bash
cd days/day-84-the-trace-tree/lab
uv run python -c "from opentelemetry import trace; from opentelemetry.sdk.trace import TracerProvider; trace.set_tracer_provider(TracerProvider()); trace.set_tracer_provider(TracerProvider())"
```

**Why:**

- The second call prints `Overriding of current TracerProvider is not allowed` and is ignored. A
  provider is process-global and one-shot, which is why `_otel.collect()` is called exactly once per
  script and why there is no single script that demonstrates everything.

---

## §4 Build brief

The teaching is in `parts/`, the measurements are in `lab/`, and what is left is the piece that
belongs in the product. Day 82 promoted the comparison, Day 83 the gate; today promotes the
instrument.

**`sutra/tracing.py`** — the desk's tracing setup, as one function called from one place.

- `TODO(me)`: `setup()` building a `TracerProvider`, adding a processor, calling
  `set_tracer_provider` — and **logging one line** naming the exporter and the sampler. Part 1.3
  measured what a missing provider looks like, and it looks like nothing.
- `TODO(me)`: `sink()` returning the exporter for this environment. `SqliteSpanExporter` locally;
  the production answer is Day 86's, and the point is that only this function changes.
- `TODO(me)`: `shutdown()` registered at the same moment the provider is installed, in the same
  function, so the two cannot drift. Part 3.3 measured zero of ten spans without it.
- `TODO(me)`: `capture_content` — read the environment, decide explicitly, and put the decision in
  the startup line. Part 4.2 measured six attributes carrying the customer's sentence by default.
- `TODO(me)`: `sampler` set explicitly rather than left at `ALWAYS_ON`. At this volume always-on is
  the right answer and it should still be a written decision — the paper part says why.
- `TODO(me)`: `trace_id_filter` — a `logging.Filter` that reads the current span context and adds
  `trace_id` to every record, so Day 22's logs and today's spans join.

**`tests/test_tracing.py`**

- `TODO(me)`: a test that `setup()` leaves `trace.get_tracer(__name__).start_span("x").is_recording()`
  true. That is part 1.3's probe as an assertion, and it is the one test that catches the silent
  failure.
- `TODO(me)`: a test that spans reach the exporter after `shutdown()` and not before, using
  `BatchSpanProcessor`. Part 3.3's measurement as a test.
- `TODO(me)`: a test that no span attribute contains a known phrase from the user's message when
  content capture is off. Part 4.2's scan, pointed at the product.
- `TODO(me)`: a test that the root span carries `app.name` and `session.id`. It fails today, because
  part 2.2 measured the root carrying zero attributes.

**Two `TODO(me)`s that are not code:**

- **Decide the content-capture policy per environment** and write it down. One environment variable,
  and the reason it needs a decision rather than a default is Principle 13: this is the first
  capability whose blast radius is a copy of the conversation.
- **The Flash-Lite allowance**, still open from Day 78 and now blocking a sixth list. Nothing in
  today's day needs it — tracing spends no requests at all — which is exactly why it is worth noting
  that it has not moved.

---

## §5 The eval that must be able to fail

```bash
cd days/day-84-the-trace-tree/lab
uv run python gate.py; echo "exit: $?"
```

Six checks against `sutra/tracing.py`, all red today because the module is the build brief. A check
that cannot run counts as a **failure**, never as skipped (Principle 11).

Every measurement in this day encodes its verdict in an exit code, and each has an arm that goes red:

```bash
uv run python tree.py; echo "exit: $?"                   # 0 — one trace, one root, ten spans
uv run python tree.py --flat; echo "exit: $?"            # 0 — the same spans, deepest first
uv run python ids.py; echo "exit: $?"                    # 0 — the tree from three numbers
uv run python ids.py --shuffle; echo "exit: $?"          # 0 — the same, in a random order
uv run python norecord.py; echo "exit: $?"               # 1 — five events, zero spans
uv run python norecord.py --wire-it; echo "exit: $?"     # 0 — eleven spans, same work
uv run python attrs.py; echo "exit: $?"                  # 1 — two span kinds with no operation name
uv run python auto.py; echo "exit: $?"                   # 0 — fifty extra spans
uv run python auto.py --off; echo "exit: $?"             # 1 — the plugin added nothing
uv run python sink.py; echo "exit: $?"                   # 0 — ten spans survived a file
uv run python flush.py; echo "exit: $?"                  # 1 — zero of ten delivered
uv run python flush.py --shutdown; echo "exit: $?"       # 0 — ten of ten
uv run python cost.py; echo "exit: $?"                   # 0 — 8,051 bytes an invocation
uv run python leak.py; echo "exit: $?"                   # 1 — six attributes carry the question
uv run python leak.py --off; echo "exit: $?"             # 0 — none do
uv run python answer.py; echo "exit: $?"                 # 0 — the failing step is named
```

Three of those belong in a pipeline, in this order: **`norecord.py` first**, because there is no
point checking what is in a trace before checking that one exists; then `flush.py`, because a trace
that is never delivered is the same as one never recorded; then `leak.py`, whose owner is whoever
signs off the data policy.

Note the two pairs where the **ablation exits 0**. `norecord.py --wire-it` and `leak.py --off` are
both the *good* state, so here the red arms are the honest ones — which is a change from the last
three days, where the arm that hid the finding was the one that passed.

The paper's demo does the same for its own claim: `demo.py` exits `0` having stored eleven per cent
of the spans with zero incomplete traces, and `demo.py --off` exits `1` having stored all of them.

---

## §6 Request budget

**Zero provider requests, to every provider.**

| Provider | Requests today | Against |
| --- | --- | --- |
| Google AI Studio (Gemini) | 0 | free tier |
| Groq | 0 | numbers not published without a signed-in session, checked 2026-09-07 |
| OpenRouter `:free` | 0 | free tier |
| Ollama (local) | 0 | n/a |

Everything in this day is ADK's real machinery. The runner, the flows, the tool executor and every
line of `google.adk.telemetry` run unmodified; `ScriptedDesk` replaces only the sentence that would
have come back over the network, through the `LLMRegistry` seam Day 80 established. The spans are
ADK's own spans with ADK's own attribute names on them.

**This day's cost is in a currency this repository has never counted.** Part 4.1 is the arithmetic:
8,051 bytes per invocation by default, which is 1.18 GB a year at four hundred invocations a day —
and 19.45 GB with `AutoTracingPlugin` fitted, and 0.62 GB with message content capture off. None of
that touches a provider allowance, and none of it is visible to the budget machinery Days 24, 78 and
81 built.

---

## §7 Traps

1. **Reading a trace as a log.** Finishing order puts the deepest, smallest step first and the whole
   invocation last — part 1.1.
2. **Expecting a parent to know its children.** Children point up and nothing points down, which is
   what lets a child be emitted later, from elsewhere, and still land — part 1.2.
3. **Assuming tracing is on.** No provider means `NonRecordingSpan`, `is_recording()` false, and
   every ADK instrumentation call returning early — part 1.3.
4. **Summing nested durations.** A model span contains its tool span, so adding them double-counts;
   the number that means anything is self time — part 2.1.
5. **Building dashboards on the vendor attribute family.** 31 of 68 attributes are
   `gcp.vertex.agent.*`, and the root span has none of either — part 2.2.
6. **Turning on automatic instrumentation by default.** Sixty spans instead of ten, and 133,220
   bytes instead of 8,051 — part 2.3.
7. **Using a synchronous processor with a network exporter.** The exporter then runs inside the
   traced code path, so a slow backend becomes a slow desk — part 3.1.
8. **Writing `WHERE session_id = ?` against the span table.** Seven of ten rows, missing the root;
   ADK's own accessor does two queries for exactly this reason — part 3.2.
9. **Exiting without `shutdown()`.** Zero of ten spans delivered, and no error anywhere — part 3.3.
10. **Budgeting tracing in requests.** It spends none; it spends storage, and the switches that move
    it are not traffic — part 4.1.
11. **Inheriting the content-capture default.** The customer's sentence in six attributes, and
    twenty-one more under `adk.fn.*` that the switch does not reach — part 4.2.
12. **Alerting on every span with status `ERROR`.** One failure marks its whole ancestor chain, so a
    naive count multiplies incidents by tree depth — part 5.1.

---

## §8 Verify before you code

Fetched on 2026-09-07:

| What | Where | What it said |
| --- | --- | --- |
| Paper record | <https://research.google/pubs/dapper-a-large-scale-distributed-systems-tracing-infrastructure/> | *Dapper, a Large-Scale Distributed Systems Tracing Infrastructure*, Google, Inc. (2010); archive path `dapper-2010-1.pdf` |
| ADK CLI | `uv run adk telemetry --help` | `enable`, `disable`, `status` — **usage telemetry**, not tracing. Two different things share the word in one CLI |
| Installed versions | `uv run python -c "import importlib.metadata …"` | `google-adk 2.7.1`, `opentelemetry-sdk 1.42.1`, `opentelemetry-api 1.42.1`; `opentelemetry-exporter-otlp` **absent** |

**ADK and OpenTelemetry symbols verified against the installed packages**, not only against docs.
`google.adk.plugins.auto_tracing_plugin.AutoTracingPlugin` takes `name`, `extra_scope_prefixes`,
`tracer`, `max_repr_len`, `max_recorded_yields` and `max_walk_depth` (`DEFAULT_MAX_WALK_DEPTH = 30`),
and guards everything on `auto_tracing_helpers.tracer_will_record`, which is
`not isinstance(tracer, NoOpTracer)`. `google.adk.telemetry.tracing` defines
`ADK_CAPTURE_MESSAGE_CONTENT_IN_SPANS` with the comment *"By default some ADK spans include
attributes with potential PII data"*, pins `Schemas.V1_36_0`, and imports several attribute keys from
`opentelemetry.semconv._incubating`. `SqliteSpanExporter.__init__` is keyword-only on `db_path`, and
`get_all_spans_for_session` deliberately queries by trace id in two steps. `BatchSpanProcessor`
defaults are `_DEFAULT_SCHEDULE_DELAY_MILLIS = 5000`, `_DEFAULT_MAX_QUEUE_SIZE = 2048`,
`_DEFAULT_MAX_EXPORT_BATCH_SIZE = 512`, and its queue-full line is `Queue full, dropping Span.`
A second `set_tracer_provider` logs `Overriding of current TracerProvider is not allowed`.

**Two things that look like traps and are not**, both checked rather than assumed. Fetching a tracer
*before* the provider is installed is fine — `get_tracer` returns a `ProxyTracer` that resolves
lazily, and `tracer_will_record` is `True` for it. And `ADK_CAPTURE_MESSAGE_CONTENT_IN_SPANS=false`
clears `tool_call_args` and `tool_response` as well as `llm_request` and `llm_response`; what it does
**not** touch is `AutoTracingPlugin`'s `adk.fn.*` attributes, measured at twenty-one still carrying
the user's question.

**The 1.x → 2.x trap this day pays for is ADK-74**: `AutoTracingPlugin` is a 2.2 feature and has no
1.x equivalent, so there is no migration guidance to inherit and the defaults are the only guide.
The measurement in part 2.3 is what a default is worth.

---

## §9 Say it in an interview

*"We added OpenTelemetry to an agent framework, and the interesting parts were not the data model.
One question produced ten spans five levels deep, with the tool call nested under the model turn
that requested it — which is causally right and means the model span's duration contains the tool's,
so any dashboard that sums durations is double-counting. Four findings were worth the day. First,
the default state of a Python process is not tracing: no provider means every span is a
NonRecordingSpan, ADK's instrumentation returns early on `is_recording()`, and a run that produced
five events and a correct answer left zero spans, zero errors and zero warnings — which looks
identical to a quiet system. Second, the auto-instrumentation plugin took us from ten spans to sixty
and from eight thousand bytes an invocation to a hundred and thirty-three thousand, so it is a
diagnostic rather than a default. Third, and this is the one I would lead with, we used the batch
span processor correctly and delivered zero of ten spans, because the process exited before the
five-second timer and nothing called shutdown — a scheduled job is the worst case for that and there
is no error anywhere. Fourth, the framework writes the whole model request into a span attribute by
default, so the customer's sentence was in six attributes of one trace, and the environment variable
that turns that off does not reach the auto-instrumentation plugin, which still had it in
twenty-one. The trace pipeline is a data store and it usually sits outside whatever review the
primary database went through."*

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked, and you have actually run the commands rather
than read them. `./m done 84` refuses to commit until they are.

The day is finished when you can be handed a slow or broken request and know which three questions
the trace answers that a traceback cannot — which step, with which arguments, and did it happen to
anybody else — and when you can say, without looking, what your own service does when the process
exits with spans still in the queue.

---

## §11 Ledger & commit

**`docs/PROGRESS.md`** — append this row:

```text
| 84 | 2026-09-07 | ADK-63, ADK-74, OPS-16 | 13 | <hash> | ⚠️ |
```

The gate column is `⚠️` and means it. `./m depth` is green over this day and every measurement in it
was run. What is not green: `sutra/tracing.py` is the build brief and `lab/gate.py` reports 0 of 6,
by design. Three findings carry forward — the root span carries zero attributes so nothing a person
searches by is on the span they search for; the content-capture switch does not reach
`AutoTracingPlugin`; and this repository still has no answer to where traces go in a deployment,
which is Day 86's question.

**`docs/PACKAGES.md`** — no new rows. No package is added today; `opentelemetry-api` and
`opentelemetry-sdk` arrive with `google-adk==2.7.1` and are used as-is.

**`docs/PAPERS.md`** — one new row:

```text
| Dapper, a Large-Scale Distributed Systems Tracing Infrastructure | Google Technical Report dapper-2010-1 | 2010 | 2026-09-07 | 84 | `days/day-84-the-trace-tree/papers/01-the-trace-tree-at-scale.md` |
```

The title and the report identifier were copied from the publication record at `research.google` on
2026-09-07 — the record, not the memory (§17.4.1 rule 5). This paper has no DOI; it is a formal
technical report, which §17.4.2 permits, and the report number is the identifier.

**`docs/SKILL_PROVENANCE.md`** — no new rows. No third-party skill is used today.

**Commit:**

```text
day 84: tracing - the trace tree, and what adk puts in it - closes ADK-63, ADK-74, OPS-16
```
