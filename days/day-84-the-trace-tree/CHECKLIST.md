# Day 84 — checklist

**Definition of done.** `./m done 84` refuses to commit while any box is unticked. A box is ticked
when you have run the thing, not when you have read about it.

**The demo command for the whole day:**

```bash
cd days/day-84-the-trace-tree/lab && uv run python tree.py; echo "exit: $?"
```

---

## Setup

- [ ] `days/day-84-the-trace-tree/lab/` exists with the fifteen files listed in the hub's §3.
- [ ] `git check-ignore -v days/day-84-the-trace-tree/lab/_desk.py` prints a matching rule.
- [ ] `git diff pyproject.toml uv.lock` is empty. No package is added today.
- [ ] Ran the two-provider snippet from §3 and saw
      `Overriding of current TracerProvider is not allowed`.
- [ ] Read `_desk.py` and can say which parts of it are ADK's and which one line is scripted.

## Section 1 — what a trace is

- [ ] Read [1.1 A trace is a tree, not a log](parts/01-what-a-trace-is/1.1-a-trace-is-a-tree.md);
      ran both arms and can say how many model turns contained a tool call, from the tree.
- [ ] Can say why `execute_tool ticket` sits under `generate_content` rather than under the agent.
- [ ] Read [1.2 Three numbers make the tree](parts/01-what-a-trace-is/1.2-three-numbers-make-the-tree.md);
      ran `--shuffle` and can say what the shuffled run proves that the ordered one does not.
- [ ] Dropped the root from `ids.py` after the shuffle, predicted the exit code, checked, put it back.
- [ ] Read [1.3 The run that left no trace](parts/01-what-a-trace-is/1.3-the-run-that-left-no-trace.md);
      ran both arms and found the eleventh span in the wired run.
- [ ] Can say what `span.is_recording()` returns with no provider, and what ADK does with that.

## Section 2 — what ADK records

- [ ] Read [2.1 Agent, tool and model](parts/02-what-adk-records/2.1-agent-tool-and-model.md);
      dumped `--one execute_tool` and `--one invoke_agent` and can say which carries the session id.
- [ ] Can name the five span kinds and say why `call_llm` and `generate_content` are two spans.
- [ ] Read [2.2 The attributes are a contract](parts/02-what-adk-records/2.2-the-attributes-are-a-contract.md);
      ran it and can state what fraction of the attributes are portable.
- [ ] Ran `attrs.py --one invocation` and saw the root span's attribute list.
- [ ] Read [2.3 Every function in the tree](parts/02-what-adk-records/2.3-every-function-in-the-tree.md);
      ran both arms and saw ten spans against sixty.
- [ ] Ran `OTEL_SDK_DISABLED=true uv run python auto.py` and can say which of the two numbers in that
      output was the surprise.

## Section 3 — where spans go

- [ ] Read [3.1 A processor and an exporter](parts/03-where-spans-go/3.1-a-processor-and-an-exporter.md);
      can point at the part of one line that decides *when* and the part that decides *where*.
- [ ] Read [3.2 A sink that outlives the process](parts/03-where-spans-go/3.2-a-sink-that-outlives-the-process.md);
      ran `sink.py --keep`, opened the database with `sqlite3`, and deleted it.
- [ ] Ran the naive `select count(*) from spans where session_id = '<id>'` and got seven, not ten.
- [ ] Can say why `get_all_spans_for_session` uses two queries.
- [ ] Read [3.3 The queue that went with the process](parts/03-where-spans-go/3.3-the-queue-that-went-with-the-process.md);
      ran both arms and saw zero of ten against ten of ten.
- [ ] Can say why the `before shutdown` count is zero in **both** runs.
- [ ] Added `atexit.register(provider.shutdown)` to `flush.py`, predicted the count, checked.

## Section 4 — what a trace costs

- [ ] Read [4.1 The bill is bytes](parts/04-what-a-trace-costs/4.1-the-bill-is-bytes.md);
      ran all three arms and worked out both multipliers.
- [ ] Changed `INVOCATIONS_PER_DAY` to your own traffic and looked at the yearly figure.
- [ ] Read [4.2 The prompt inside the span](parts/04-what-a-trace-costs/4.2-the-prompt-inside-the-span.md);
      ran both arms and saw six attributes against zero.
- [ ] Ran `ADK_CAPTURE_MESSAGE_CONTENT_IN_SPANS=false uv run python attrs.py --one execute_tool` and
      confirmed `tool_call_args` is `{}` too.
- [ ] Reproduced the twenty-one-attribute measurement with the plugin fitted and the switch off, and
      can say why one of those two results is reassuring and the other is not.

## Section 5 — in production

- [ ] Read [5.1 Reading a trace](parts/05-in-production/5.1-reading-a-trace.md);
      ran both arms and counted how many traceback lines precede the one naming `_desk.py`.
- [ ] Can say which of the three `ERROR` spans is the cause and how you know.
- [ ] Made `ticket` return `{"error": ...}` instead of raising, saw the status column, put it back.
- [ ] Read [5.2 What a real tracing setup adds](parts/05-in-production/5.2-what-to-pin-above-the-till.md);
      mapped the seven-step sequence onto the nine items and found the step no item covers.

## The paper — after the parts

- [ ] Read [papers/01 The trace tree at scale](papers/01-the-trace-tree-at-scale.md).
- [ ] Ran `demo.py` and `demo.py --off` in `lab/papers/dapper/` and saw 88 spans against 800.
- [ ] Removed the `ParentBased` wrapper from `head_sampler`, predicted `incomplete traces`, checked,
      and put it back.
- [ ] Set `RATIO` to `0.01` and can say what happened to `failing traces kept` and what that means
      for somebody holding a support ticket.
- [ ] Can name the paper's four contributions and the one condition under which sampling is the
      wrong thing to copy.

## The build brief

- [ ] `sutra/tracing.py` written — `setup()`, `sink()`, `shutdown()`, `capture_content`, `sampler`,
      `trace_id_filter`.
- [ ] `setup()` logs one line naming the exporter and the sampler.
- [ ] `shutdown()` is registered in the same function that installs the provider.
- [ ] The sampler is set explicitly, even though always-on is the right answer at this volume.
- [ ] `tests/test_tracing.py` written — the `is_recording()` assertion, the flush test, the
      no-content-in-attributes test, and the root-span-context test that fails today.
- [ ] **The content-capture policy decided per environment**, and written down rather than inherited.
- [ ] **The Flash-Lite allowance**, still open since Day 78 — noted as unmoved, and not blocking
      anything in this day.

## The evals, including ones that go red on demand

- [ ] `uv run python gate.py` runs and reports 0 of 6 — `sutra/tracing.py` is the build brief.
- [ ] `tree.py` and `tree.py --flat` both exit `0`.
- [ ] `ids.py` and `ids.py --shuffle` both exit `0`.
- [ ] `norecord.py` exits `1`; `--wire-it` exits `0`.
- [ ] `attrs.py` exits `1` — two span kinds carry no `gen_ai.operation.name`.
- [ ] `auto.py` exits `0`; `--off` exits `1`.
- [ ] `sink.py` exits `0`.
- [ ] `flush.py` exits `1`; `--shutdown` exits `0`.
- [ ] `cost.py` exits `0`.
- [ ] `leak.py` exits `1`; `--off` exits `0`.
- [ ] `answer.py` exits `0`.
- [ ] `papers/dapper/demo.py` exits `0`; `--off` exits `1`.
- [ ] **Break it and watch it go red:** removed `provider.force_flush()` from `sink.py`, predicted
      what the row count would be, ran it, and put it back.

## The request budget

- [ ] Confirmed **zero** provider requests were made today, to every provider.
- [ ] Can state what this day costs in the currency it actually spends, at all three settings, and
      say why the existing budget machinery cannot see it.

## Ledger & commit

- [ ] `./m depth 84` green.
- [ ] `./m trace` regenerated; day 84 closes exactly `ADK-63`, `ADK-74`, `OPS-16`.
- [ ] `./m wiki` regenerated.
- [ ] `docs/PROGRESS.md` row appended, verbatim from the hub's §11, with the real commit hash.
- [ ] `docs/PAPERS.md` — the `Google Technical Report dapper-2010-1` row added.
- [ ] Committed with the message in the hub's §11.
