# Day 54 — Definition of done

`./m done 54` refuses to commit until every box is ticked. Tick a box only when you have actually run
the thing, not when you have read it.

## Before you start

- [ ] Day 53's parts and checklist are done, and
      `python -c "from google.adk.workflow import START, Edge, FunctionNode, JoinNode, Workflow; print('ok')"`
      prints `ok`. If it does not, today cannot start (P2).
- [ ] `uv run python days/day-54-sequential-parallel-loop/lab/gate.py; echo "exit: $?"` is **red**
      before you write anything, and you have read the one finding it reports.
- [ ] `lab/` scaffolded per §3 — twenty-one files plus the two-file paper demo — and
      `sutra/flow.py` and `tests/test_flow.py` created empty.
- [ ] `git diff pyproject.toml uv.lock` is empty and stays empty. No package is added today.

## Section 1 — one after another (ADK-35)

- [ ] **1.1** read · ran `chain.py` and `chain.py --swap` · saw the same three nodes return
      **`queue:auth`** in one order and **`queue:other`** in the other, with no error either time ·
      reached `Graph validation failed. The following nodes are unreachable from START` on purpose ·
      can say what `START` is
- [ ] **1.2** read · ran `visible.py` and `visible.py --forget` · saw `assign` bound `ticket_id` from
      **state** and then fall back to **`UNKNOWN`** · removed the default and reached
      `Missing value for parameter "ticket_id" ... It was not found in state and has no default
      value.` · can state the binding rule for a parameter that is not called `node_input`
- [ ] **1.3** read · ran `plain.py` · saw the nested calls and the graph return the identical string ·
      saw `__START__` in the printed node list · added a fourth stage to the graph and counted the
      edits each version needed
- [ ] **1.4** read · ran `refuse.py` · saw all **five** `Graph validation failed` messages · added a
      sixth case with no `START` at all · can say what distinguishes those five from the
      `Missing value for parameter` error

## Section 2 — at the same time (ADK-36)

- [ ] **2.1** read · ran `fanout.py`, `--sequential` and `--nojoin` · saw **all three `:start`
      entries before any `:end`** in the fan-out and strict pairing in the chain · saw `collect` run
      **three times** · reached
      `multiple terminal nodes produced output (3). A workflow must have at most one terminal output.`
- [ ] **2.2** read · ran `join.py` and `join.py --plain` · saw `summarise received dict` once against
      `summarise received str` three times · ran `stall.py` and `stall.py --match` · saw the join
      **never fire** with only a `WARNING` as evidence · ran `stall.py --none` and saw `None` land in
      the join dict rather than stalling it
- [ ] **2.3** read · ran `order.py` and `order.py --fresh 8` · saw **1 distinct start order and 1
      join order in one process, and 1 start order against 5 join orders across eight processes** ·
      can say why `list(results.values())[0]` passes CI
- [ ] **2.4** read · ran `race.py`, `--swap` and `--keyed` · saw **`confidence='low'` in both
      declaration orders** · saw both values survive once keyed · changed the slow branch's sleep to
      `0` and wrote down what happened to the stability
- [ ] **2.5** read · ran `concurrency.py` with no flag, `--limit 1` and `--limit 2` · saw peak in
      flight go **6 → 1 → 2** and the trace change from a climb to strict pairs · can say what
      `max_concurrency` does **not** protect you from

## Section 3 — around again (ADK-37)

- [ ] **3.1** read · ran `loop.py` and `loop.py --rounds 5` · saw **three drafts then publish**, and
      then five · changed `"accept"` to `"approved"` in one place only and found the
      `has conditional/DEFAULT edges but none were matched` warning · added a `DEFAULT_ROUTE` edge
      and re-ran
- [ ] **3.2** read · ran `cycle.py` and `cycle.py --routed` · saw
      `Unconditional cycle detected: critic -> writer -> critic` and then a graph that built ·
      built a four-node cycle and read the path in the message · can state exactly what the runtime
      guarantees about cycles
- [ ] **3.3** read · ran `carry.py` · saw `node_input` be a **`Content` on pass one** and
      **`str(revise)` on passes two and three** · added a second run in the same process and saw
      **`state.rounds=1` beside `module=4`** · can say where the previous draft has to come from
- [ ] **3.4** read · ran `runaway.py` and `runaway.py --watch 40` · saw **21** and then **41** writer
      passes with the graph still going · can say who decided when it stopped
- [ ] **3.5** read · ran `guard.py`, `--cap 2` and `--no-guard` · saw the cap end the run at **3** and
      at **2**, with `stopped_by: 'cap'` in the final state, and saw the unguarded version reach
      **13** · added a third `escalate` route with its own node · can name the three parts of a guard
      and which is usually missing

## Section 4 — where they meet

- [ ] **4.1** read · ran `triage.py` and `triage.py --strict` · saw all three shapes in one output ·
      saw **`draft v2 from [revise]`** and can explain exactly why the research vanished · moved the
      back edge to `classify` and counted the extra research calls
- [ ] **4.2** read · ran `blast.py` and `blast.py --degrade` · saw **three `:start` entries and no
      `:end`** when the branch raised · saw the join fire with `kb:UNAVAILABLE` when it degraded ·
      can say why returning `""` instead is a Principle 10 violation
- [ ] **4.3** read · ran `retry.py`, `--no-retry` and `--timeout` · saw **9 calls for 3 rounds** and
      **6 events**, then **1 call and a dead graph** · reached
      `NodeTimeoutError: Node 'slow_search' timed out after 0.2 seconds.` · predicted the total for
      `ROUNDS = 5` and `max_attempts=5` before running it

## Section 5 — the old shapes (trap #1)

- [ ] **5.1** read · ran `oldshapes.py` and `oldshapes.py --quiet` · saw all three deprecated classes
      construct, saw the three `DeprecationWarning` lines in `__main__` and **nothing** from inside a
      module · saw `LoopAgent.max_iterations` default to `None` · wrote the 2.x equivalent of a
      `LoopAgent` on paper
- [ ] **5.2** read · can name the three junctions that move · translated one real 1.x example found
      online into an edge list and marked the two things the page did not contain

## The paper — read after the parts

- [ ] **01** [Communicating sequential processes](papers/01-communicating-sequential-processes.md)
      read · ran `demo.py` and `demo.py --shared` from
      `lab/papers/communicating-sequential-processes/` · saw **200 runs → 1 distinct result** with
      channels and **200 runs → 2 distinct results** (118/82) with a shared variable · changed the
      demo to a single shared channel and counted the results again · can say which side of the
      paper's central trade ADK's session state sits on

## Build brief (§4)

- [ ] `sutra/flow.py` has `research_graph()`, `review_loop()` and `triage_graph()`, and every
      `TODO(me)` in the hub's §4 is resolved by code you wrote.
- [ ] `research_graph()` sets `max_concurrency` and holds a `JoinNode`, and each branch writes its
      own state key.
- [ ] `review_loop()` has a routed back edge, `MAX_ROUNDS`, and records **why** it stopped.
- [ ] `triage_graph()` still has the research available to the drafter on pass two — verified by a
      run that loops at least twice, not by reading the code.

## Tests

- [ ] `tests/test_flow.py` asserts `research_graph()` constructs and holds a `JoinNode`.
- [ ] `tests/test_flow.py` asserts `review_loop()` stops at `MAX_ROUNDS` with a never-accepting
      critic, and that the run records the cap as the reason.
- [ ] `tests/test_flow.py` runs `triage_graph()` end to end with stubs and **loops at least twice**.
- [ ] **Break it, watch it go red, fix it:** remove the cap from `review_loop`, run the test, watch
      it fail or hang, put the cap back. Write down what the failure looked like.
- [ ] `uv run python -m pytest tests/test_flow.py -q` passes.

## Request budget

- [ ] **0** model generations were made writing, running or testing anything in this day, including
      the paper demo's 400 runs. If you spent any, write down where and why.

## Gates and ledger

- [ ] `uv run python days/day-54-sequential-parallel-loop/lab/gate.py; echo "exit: $?"` now exits
      **0**, and you watched each of the six findings disappear.
- [ ] `./m depth 54` green.
- [ ] `./m check` green (ruff, format, pytest, depth, trace, wiki).
- [ ] `docs/PAPERS.md` has the `doi:10.1145/359576.359585` row, verified 2026-09-05.
- [ ] `docs/PROGRESS.md` has the day 54 row, hash filled in after committing.
- [ ] Committed as `day 54: sequential, parallel and loop patterns — closes ADK-35, ADK-36, ADK-37`.
