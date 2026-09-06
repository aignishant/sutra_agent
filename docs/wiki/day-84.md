# Day 84 - Tracing — the trace tree, and what ADK puts in it

IDs closed: ADK-63, OPS-16, ADK-74 · source: `days/day-84-the-trace-tree/`

## Parts

### 1.1 - A trace is a tree, not a log
`days/day-84-the-trace-tree/parts/01-what-a-trace-is/1.1-a-trace-is-a-tree.md` · level `foundation` · ids ADK-63

A log tells you what happened in the order it finished; a trace tells you what happened inside what else — and for an agent, where one question becomes ten nested steps, the second question is the only one anybody actually asks.

### 1.2 - Three numbers make the tree
`days/day-84-the-trace-tree/parts/01-what-a-trace-is/1.2-three-numbers-make-the-tree.md` · level `foundation` · ids ADK-63

A span carries a trace id, its own span id and its parent's span id, and those three numbers are enough to rebuild the whole shape from a shuffled pile — which is what makes a trace survive being split across processes, queues and machines that never speak to each other.

### 1.3 - The run that left no trace
`days/day-84-the-trace-tree/parts/01-what-a-trace-is/1.3-the-run-that-left-no-trace.md` · level `working` · ids ADK-63, OPS-16

Tracing is off unless somebody turns it on, and "off" in OpenTelemetry does not mean broken or loud — it means every span is a NonRecordingSpan, every instrumentation call returns early, and a run that produced five events and a correct answer leaves zero spans and zero warnings.

### 2.1 - Agent, tool and model — the three spans ADK writes
`days/day-84-the-trace-tree/parts/02-what-adk-records/2.1-agent-tool-and-model.md` · level `working` · ids ADK-63, ADK-74

ADK instruments its own framework boundaries — one span per agent invocation, one per model call and one per tool execution — and the shape those produce is a five-level tree in which the tool call sits under the model turn that asked for it, not under the agent.

### 2.2 - The attributes are a contract, half-kept
`days/day-84-the-trace-tree/parts/02-what-adk-records/2.2-the-attributes-are-a-contract.md` · level `working` · ids ADK-74

Half of what ADK writes on a span uses the OpenTelemetry GenAI conventions and half uses its own gcp.vertex.agent. names, so a backend that only speaks the standard reads thirty-seven of sixty-eight attributes — and two span kinds, including the root of every trace, carry no gen_ai.operation.name at all.

### 2.3 - Every function in the tree — AutoTracingPlugin
`days/day-84-the-trace-tree/parts/02-what-adk-records/2.3-every-function-in-the-tree.md` · level `production` · ids ADK-74

AutoTracingPlugin monkey-patches every in-scope Python function to emit a span, which takes this desk from ten spans to sixty and from eight thousand bytes to a hundred and thirty-three thousand — a complete picture that is sixteen times the size and, for most questions, harder to read than the ten.

### 3.1 - A processor and an exporter
`days/day-84-the-trace-tree/parts/03-where-spans-go/3.1-a-processor-and-an-exporter.md` · level `working` · ids OPS-16

A finished span goes to a processor, which decides when to hand it on, and then to an exporter, which decides where it goes — and separating those two jobs is why you can change backends without touching batching, and change batching without touching backends.

### 3.2 - A sink that outlives the process
`days/day-84-the-trace-tree/parts/03-where-spans-go/3.2-a-sink-that-outlives-the-process.md` · level `working` · ids OPS-16

ADK ships SqliteSpanExporter, which writes every span to a local file with its parent link intact at zero cost and no network — and its projection keeps only four columns beside the JSON blob, so three of this desk's ten spans, including the root, land with no session id.

### 3.3 - The queue that went with the process
`days/day-84-the-trace-tree/parts/03-where-spans-go/3.3-the-queue-that-went-with-the-process.md` · level `production` · ids OPS-16

BatchSpanProcessor holds finished spans in memory and hands them on every five seconds, so a process that exits without calling shutdown() delivers zero of ten spans — with no error, no warning, and a run that was correct from end to end.

### 4.1 - The bill is bytes, not requests
`days/day-84-the-trace-tree/parts/04-what-a-trace-costs/4.1-the-bill-is-bytes.md` · level `production` · ids OPS-16

Tracing costs zero provider requests and eight thousand bytes an invocation, which is a gigabyte a year at this desk's traffic — and the two switches that move that number most are the automatic plugin, which multiplies it by sixteen, and content capture, which halves it.

### 4.2 - The prompt inside the span
`days/day-84-the-trace-tree/parts/04-what-a-trace-costs/4.2-the-prompt-inside-the-span.md` · level `production` · ids OPS-16

By default ADK writes the whole model request and response into span attributes, so the customer's own sentence appears six times in one trace — in a stream that is copied to a dashboard, a collector and a vendor, none of which is behind the approval gate the session store sits behind.

### 5.1 - Reading a trace when something failed
`days/day-84-the-trace-tree/parts/05-in-production/5.1-reading-a-trace.md` · level `production` · ids ADK-63, OPS-16

A failing tool produces a hundred-and-forty-line framework traceback and a five-span trace, and the trace answers the three questions a person actually has — which step, under which parent, with which arguments — while marking every ancestor ERROR so the deepest error span is the cause.

### 5.2 - What a real tracing setup adds
`days/day-84-the-trace-tree/parts/05-in-production/5.2-what-to-pin-above-the-till.md` · level `production` · ids OPS-16

The lab produces real ADK spans, reconstructs the tree, exports it to a file that survives the process and finds the cause of a failure — and the distance between that and something a team can rely on is nine things, of which the first three take under two hours and make the other six possible.

## Papers - read after the parts

### Google Technical Report dapper-2010-1 - The trace tree at scale
`days/day-84-the-trace-tree/papers/01-the-trace-tree-at-scale.md`

Everything in this day — the span, the parent link, the propagated context, the sampler — is one document's answer to a question nobody could answer in 2010: what happened to this one request, on these thousands of machines?

