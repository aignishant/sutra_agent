---
day: 84
paper: "Google Technical Report dapper-2010-1"
title: "The trace tree at scale"
ids: ["ADK-63"]
level: production
prerequisites: ["../parts/01-what-a-trace-is/1.2-three-numbers-make-the-tree.md"]
prev: "../parts/05-in-production/5.2-what-to-pin-above-the-till.md"
next: "../LESSON.md"
---

# Paper 01 — The trace tree at scale

> **Dapper, a Large-Scale Distributed Systems Tracing Infrastructure**
> Google, Inc., 2010. Report identifier `dapper-2010-1`.
>
> The claim this day borrows: a tracing system for a real production estate has to satisfy three
> constraints at once — **low overhead**, **application-level transparency** and **ubiquitous
> deployment** — and the design that satisfies all three is a per-request tree of spans, propagated
> through a small number of common libraries, **sampled** at the root, and collected out of band.

## One-line answer

Everything in this day — the span, the parent link, the propagated context, the sampler — is one
document's answer to a question nobody could answer in 2010: *what happened to this one request, on
these thousands of machines?*

## The story

The complaint that was transferred four times.

Somebody rings about a bill. The first person takes the details and says it is a billing matter, and
transfers. Billing says the charge came from the delivery side, and transfers. Delivery says it was
raised by the warehouse system, and transfers. The warehouse says it looks like a billing entry, and
offers to transfer.

Every one of those four people was competent, helpful, and correct about their own part. Not one of
them could see the whole thing, because there was no *whole thing* anywhere — there were four
systems, each with a complete and accurate record of its own involvement, and nothing that carried
the caller's problem across the joins.

The caller, who can see all four, is the only entity in the entire arrangement with the end-to-end
view, and she is the one person who does not know how any of it works.

## The idea in plain language

By the late 2000s a single web search at Google touched thousands of machines across dozens of
services. Every one of those services had logs. None of them had the request.

The paper's first contribution is a **data model**, and it is the one in part
[1.1](../parts/01-what-a-trace-is/1.1-a-trace-is-a-tree.md): a trace is a tree of spans, a span is a
unit of work with a start and an end, and each span names its parent. The document also introduces
*annotations* — timestamped notes attached to a span — which is what OpenTelemetry calls span
events, and which part [5.1](../parts/05-in-production/5.1-reading-a-trace.md) used to carry an
exception message.

The second is **propagation**. The tree only survives if the trace id and the caller's span id
travel with the call, and the paper's insight about how to achieve that is organisational rather
than technical: instrument a *small number of ubiquitous libraries* — the RPC layer, the threading
primitives, the control-flow helpers — rather than asking every team to instrument their own code.
That is what "application-level transparency" means: a team gets tracing by using the standard
libraries everybody already uses, and does nothing.

The third is **sampling**, and it is the one this day's demo isolates. Tracing every request at that
scale was not affordable, so Dapper traced a fraction — and crucially made the decision **once, at
the root**, recording it in the propagated context so that every span in a chosen trace was kept and
every span in an unchosen one cost nothing. A trace is complete or absent. Never partial.

The fourth is **out-of-band collection**: spans are written to local logs and collected by a separate
daemon, rather than being sent inline with the request. The failure in part
[3.1](../parts/03-where-spans-go/3.1-a-processor-and-an-exporter.md) — a synchronous exporter putting
the trace backend on the critical path — is the thing that design exists to prevent, and
`BatchSpanProcessor` is the same idea inside a process.

## Why Sutra needs it

Because Phase 13 is about to create exactly the conditions the paper was written for. Day 85 puts an
HTTP boundary in front of the desk; Day 86 puts it in a container; Day 88 puts a tool server in a
second container beside it. At that point the desk is a distributed system, and every one of those
joins is a place where a request is handed over and the caller's context has to go with it.

And because Principle 4 is *build first, compare after*. This day built the tree by hand, watched
ADK emit it, exported it, broke it and read it. Reading the proposal now lands on something already
familiar, which is the whole reason the paper comes last.

## The mechanism

The paper's method, written out as the four decisions rather than paraphrased as an abstract:

**Trace, span, parent, annotation.** A trace id is generated at the root. Each span gets its own id
and records its parent's. Annotations are timestamped and attached to a span. Nothing points
downward — a parent has no list of its children — which is what allows a child emitted from a
different machine, later, to still land in the right place.

**Instrument the libraries, not the applications.** The tracing code lives in the RPC layer and the
threading helpers. Application authors get spans for free and, importantly, *cannot forget to add
them*. The paper is explicit that this restriction to a small set of common libraries was key to its
success.

**Sample at the root, obey the decision everywhere.** The keep-or-drop decision is made once and
propagated. This is the difference between a system whose traces are cheap and complete and one
whose traces are cheap and full of holes.

**Collect out of band.** Spans go to local log files; a daemon collects them. The application never
waits for the tracing infrastructure.

Two things are worth saying about the third decision, because they are the ones people get wrong.

It has to be **at the root**, not per span, or a kept trace has gaps where the sampler said no. And
it has to be **deterministic in the trace id**, so that a downstream service which was not told the
decision can compute the same answer from the id alone — which is exactly how OpenTelemetry's
`TraceIdRatioBased` works, and why it is a hash of the trace id rather than a random draw.

## The paper in one demo

A small end-to-end project implementing the sampling contribution and nothing else.

```text
days/day-84-the-trace-tree/lab/papers/dapper/
├── sampling.py  # head sampling: the root decides, children inherit
└── demo.py      # 200 invocations, one in fifty fails; --off keeps everything
```

`sampling.py` is the whole idea in two functions:

```python
def head_sampler(ratio: float) -> Sampler:
    """Keep `ratio` of traces, whole. The root decides; children inherit."""
    return ParentBased(root=TraceIdRatioBased(ratio))


def keep_everything() -> Sampler:
    """The ablation: no sampling at all."""
    return ALWAYS_ON
```

**Line by line:**

- `TraceIdRatioBased(ratio)` hashes the trace id and keeps that fraction. It is deterministic, so the
  same trace id gets the same answer in every process that sees it — the decision survives a network
  hop without anybody sending it.
- `ParentBased(root=...)` is the half people leave out. It says: *if there is a parent, do what the
  parent decided; only if this span is a root, ask the ratio sampler.* Without it, every span would
  be sampled independently and a kept trace would be full of holes.
- Both are OpenTelemetry's own classes, so the demo measures the real mechanism rather than a
  re-implementation of it.
- `ALWAYS_ON` for the ablation, which is the SDK's default and is what a `TracerProvider()` with no
  `sampler` argument uses.

`demo.py` runs a desk two hundred times, four spans each, with one invocation in fifty hitting a
broken path:

```python
def desk(tracer: trace.Tracer, number: int) -> None:
    """One invocation: agent -> model -> tool -> answer, four spans, sometimes broken."""
    with tracer.start_as_current_span("invoke_agent desk") as agent:
        agent.set_attribute("invocation", number)
        with tracer.start_as_current_span("call_llm"):
            with tracer.start_as_current_span("execute_tool ticket") as tool:
                if number % FAILS_EVERY == 0:
                    tool.set_attribute("error.type", "TimeoutError")
                    agent.set_attribute("error.type", "TimeoutError")
```

**Line by line:**

- Four nested spans in the shape part
  [2.1](../parts/02-what-adk-records/2.1-agent-tool-and-model.md) measured from ADK, written by hand
  here so the demo has no dependency beyond OpenTelemetry — the claim under test is about the
  sampler, not about ADK.
- `number % FAILS_EVERY == 0` makes failure rare and deterministic, which is what the paper's
  problem looks like: the traces you want are the ones there are fewest of.
- The error marker is set on both the tool and the agent, mirroring the status propagation part
  [5.1](../parts/05-in-production/5.1-reading-a-trace.md) measured.
- No model, no network, no file. The demo is arithmetic over spans.

And the measurement is three counts:

```python
    per_trace = Counter(span.context.trace_id for span in spans)
    kept = len(per_trace)
    partial = [t for t, n in per_trace.items() if n != SPANS_PER_INVOCATION]
```

**Line by line:**

- Counting spans **per trace id** is what makes "whole or absent" checkable: a trace with fewer than
  four spans was sampled inconsistently.
- `partial` is the check that would fail if the sampler were per span rather than parent-based, and
  it is the reason `ParentBased` is in `sampling.py` rather than a bare ratio sampler.

Run it:

```bash
cd days/day-84-the-trace-tree/lab/papers/dapper
uv run python demo.py; echo "exit: $?"
```

**Line by line:**

- No flag: head sampling at one in ten, which is the paper's condition.

Measured on 2026-09-07:

```text
sampling: head, ratio 0.1
200 invocations, 4 spans each, one in 50 fails

  traces produced:        200
  traces stored:          22
  spans stored:           88
  storage against 'keep everything': 11%
  incomplete traces:      0
  failing traces kept:    2 of 4 that happened

  88 spans instead of 800, and every
  stored trace is whole - a sampled trace is complete or absent, never partial
exit: 0
```

**Eleven per cent of the storage, zero incomplete traces.** Twenty-two traces out of two hundred,
every one of them four spans deep. That is the contribution: the saving is real and it costs nothing
in legibility, because what is kept is kept whole.

And the ablation:

```bash
uv run python demo.py --off; echo "exit: $?"
```

**Line by line:**

- `--off` swaps `ALWAYS_ON` in and changes nothing else. It exits `1`, because the demo's job is to
  reproduce the claim and this arm deliberately does not.

Measured on 2026-09-07:

```text
sampling: off - keep every trace
200 invocations, 4 spans each, one in 50 fails

  traces produced:        200
  traces stored:          200
  spans stored:           800
  storage against 'keep everything': 100%
  incomplete traces:      0
  failing traces kept:    4 of 4 that happened

  every trace was kept, so nothing was saved and nothing was lost
  at four hundred invocations a day this is the whole bill, for ever
exit: 1
```

Eight hundred spans against eighty-eight, for the same two hundred requests.

## When it breaks

The demo also measures the paper's real limitation, and it is in the line most people skip.

**`failing traces kept: 2 of 4`.** Head sampling makes its decision at the root, *before anything has
gone wrong*, so it cannot prefer failures. At one in ten it keeps roughly one in ten of them, and the
four failures in this run became two. For a statistical question — *what fraction of requests fail?*
— that is fine. For the question anybody actually asks — *why did this customer's request fail?* —
it is a coin flip, and at a realistic production ratio of one in a thousand it is worse than a coin
flip.

That is not a flaw in the paper; it is the trade the paper made deliberately, for a system whose
purpose was performance analysis across an estate. It is a flaw in copying the design without
copying the purpose.

**The claim does not hold when the failure is what you are sampling for.** The field's answer,
arrived at afterwards, is **tail sampling**: buffer every span of a trace in a collector, wait until
the trace finishes, then decide — keep all errors, keep the slow ones, keep a small fraction of the
rest. It costs memory in a separate process and it is why part
[5.2](../parts/05-in-production/5.2-what-to-pin-above-the-till.md) parks it.

**And it does not hold at low volume.** A desk answering four hundred requests a day gets no benefit
from sampling at all — part [4.1](../parts/04-what-a-trace-costs/4.1-the-bill-is-bytes.md) measured
a gigabyte a year for keeping everything. Sampling is a technique for a scale this system does not
have, and applying it here would buy nothing and lose traces.

## In production

**What survived, essentially unchanged.** The data model, completely. Trace, span, parent,
annotation — those four words are the OpenTelemetry data model, and the `traceparent` HTTP header
that every modern service speaks is this paper's propagation idea with a specification around it.
The instrument-the-libraries strategy survived as *auto-instrumentation*, which is what part
[2.3](../parts/02-what-adk-records/2.3-every-function-in-the-tree.md) measured a version of.
Out-of-band collection survived as the collector-and-agent architecture that every vendor ships, and
as `BatchSpanProcessor` inside a process.

**What survived in modified form.** Sampling. Head sampling is still everywhere and is still the
default, and the important production systems have moved the *interesting* decision to the tail. The
paper's fixed low ratio has become adaptive sampling — a rate that adjusts to keep a target volume —
which nothing in the original describes.

**What did not survive.** The assumption of a homogeneous estate. The design leans on everybody
using the same RPC library, which is what made transparent instrumentation possible; outside one
company that is not true, and the twenty years since have been spent replacing that assumption with
a standard — first OpenTracing and OpenCensus, then OpenTelemetry — so that heterogeneous systems can
produce one tree. The paper's mechanism won and its precondition had to be rebuilt as an agreement.

**What it means for this repository, concretely.** The default `TracerProvider()` uses `ALWAYS_ON`,
which is the right choice at this volume and is a choice nobody made. Part
[5.2](../parts/05-in-production/5.2-what-to-pin-above-the-till.md) item 6 is to set it explicitly and
say so in the startup line, so that the day traffic grows the decision is visible rather than
inherited.

**The review comment a senior engineer leaves:** *"Do not add sampling yet — a gigabyte a year is
nothing and we would lose traces we want. Do set the sampler explicitly to always-on and log it, so
the day somebody changes it, it is a diff."*

**The interview question:** *"How would you keep tracing costs down?"* The answer that shows
experience does not start with a ratio. It asks what the traces are for: if they are for
performance statistics, head sampling at the root is correct and cheap; if they are for debugging
individual failures, head sampling actively destroys the thing you need, and the answer is tail
sampling or nothing.

## Check yourself

```bash
cd days/day-84-the-trace-tree/lab/papers/dapper
uv run python demo.py; echo "exit: $?"
uv run python demo.py --off; echo "exit: $?"
```

Eighty-eight spans and eight hundred. Both runs report `incomplete traces: 0`. Say why that is the
line that proves the paper's design rather than the storage figure.

Now break the design deliberately: in `sampling.py`, change `head_sampler` to return
`TraceIdRatioBased(ratio)` without the `ParentBased` wrapper. Predict what happens to
`incomplete traces` and to the exit code before you run it, then put it back.

Then change `RATIO` to `0.01` and say what happens to `failing traces kept` — and what that means
for somebody holding a support ticket.

**Out loud, without scrolling up:** name the paper's four contributions, say which one this demo
isolates, and name the one condition under which that contribution is the wrong thing to copy.

**Next:** back to the hub — [`LESSON.md`](../LESSON.md).
