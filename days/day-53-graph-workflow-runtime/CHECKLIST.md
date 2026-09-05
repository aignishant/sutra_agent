# Day 53 — Definition of done

`./m done 53` refuses to commit until every box is ticked. Tick a box only when you have actually run
the thing, not when you have read it.

## Before you start

- [ ] Day 52's parts and checklist are done, and the Phase 7 gate is met — the desk answers
      *"have we seen anything like this before?"* at $0.
- [ ] `uv run python -c "import google.adk; print(google.adk.__version__)"` prints **2.7.1**, and
      `uv run python -c "from google.adk.workflow import Workflow, node, Edge, START, JoinNode, DEFAULT_ROUTE; print('ok')"`
      prints `ok`.
- [ ] `uv run python days/day-53-graph-workflow-runtime/lab/gate.py; echo "exit: $?"` is **red** before
      you write anything — **0/5 checks pass, exit 1** — and you have read all five failing lines.
- [ ] `lab/` scaffolded per §3 — twenty-two files plus `papers/dryad/`.
- [ ] `git diff pyproject.toml uv.lock` is empty and stays empty. **No package is added today.**

## Section 1 — the node

- [ ] **1.1** read · ran `unit.py` · saw **one event**, `intake is a FunctionNode`, and the graph
      holding **two** nodes when you only wrote one · reached
      `ValueError: Missing value for parameter "ticket" ... It was not found in state` by renaming the
      parameter · can say why the message mentions *state* and not the edge
- [ ] **1.2** read · ran `kinds.py` · saw all four rows say **True** and the bare function say
      **False** · noticed that only the plain function was *converted*, and that `LlmAgent` and
      `Workflow` went in and came out as themselves · nested `inner` inside another `Workflow` and
      confirmed it is accepted
- [ ] **1.3** read · ran `arrives.py` · saw `node_input = 'checkout is down'` against
      `state = {'raw_ticket': '  Checkout   is   DOWN  '}` · can state the rule for what fills a
      parameter that is called neither `node_input` nor `ctx`
- [ ] **1.4** read · ran `leaves.py` · saw `output`, `message` and `route` on **one** event and all
      three `None` on the next · deleted `output=` and watched the next node receive `None` while the
      human still saw a confident sentence
- [ ] **1.5** read · ran `stream.py` · saw first event at **+0.41s against +1.24s** with both runs
      finishing together · raised `PAUSE` to `1.0` and wrote down both first-event times · can name
      the two things trap #3 says appending breaks

## Section 2 — the edge

- [ ] **2.1** read · ran `edges.py` · saw the three edges printed from `flow.graph.edges` and the same
      three run · can say what a node knows about its successor
- [ ] **2.2** read · saw **`same edges? True`** for the chain and the spelled-out version · made
      `("START", intake, classify, draft, classify)` and got
      `Unconditional cycle detected: classify -> draft -> classify` · can say how many edges a chain of
      five nodes produces
- [ ] **2.3** read · ran `routes.py` and `routes.py --default` · saw the fourth ticket produce
      **1 event** and then **2** · read the warning
      *"none were matched by the emitted route(s): unrecognised. The branch will end."* · changed a
      label's spelling and watched a ticket vanish
- [ ] **2.4** read · ran `fanout.py` and `fanout.py --serial` · saw **0.45s against 0.84s**, and saw
      that the serial version fed one search the *other search's output* · made `search_kb` a blocking
      `def` and wrote down the new time · can say what a `JoinNode` waits for
- [ ] **2.5** read · ran `carry.py` · saw `from_edge` and `from_state` arrive by different routes ·
      deleted the state write and saw `None`, then switched `.get` to `[...]` and compared the two
      failures · can state the one-sentence test for edge versus state

## Section 3 — the graph is checked

- [ ] **3.1** read · ran `validate.py` · saw **six** validation errors, each naming the offending
      nodes · added a seventh case pointing an edge **at** `START` and got
      `START node must not have incoming edges.` · can name two mistakes validation cannot catch
- [ ] **3.2** read · ran `cycle.py` · saw **7 events** from a four-node graph with `draft` and `review`
      each appearing three times · ran `cycle.py --illegal` and saw the cycle printed back at you ·
      set `MAX_ATTEMPTS = 1` and counted the events · can name an infinite loop the check allows
- [ ] **3.3** read · ran `orphan.py` · saw `escalate_to_finance in the graph? False` and watched a
      billing ticket get a confident wrong answer from the knowledge base · ran
      `orphan.py --disconnected` and saw the half-wired version rejected · wired the billing route and
      watched the node appear

## Section 4 — the composition model

- [ ] **4.1** read · ran `tree.py` · saw
      **`Agent 'classify' already has a parent agent, current parent: 'incident_flow'`** · saw
      `log_it` reached from **two** incoming edges and both tickets arrive at it · added a third branch
      into `log_it` without changing `log_it`
- [ ] **4.2** read · can give the **four** criticisms of a `SequentialAgent` composition · wrote out
      the edge list that a real 1.x tutorial's flow becomes · can say why wrapping a `SequentialAgent`
      in a `Workflow` fixes none of the four
- [ ] **4.3** read · ran `legacy.py` and saw **three** deprecation warnings · ran `hidden.py` and saw
      the first block print **nothing** and `simplefilter('default')` capture **1 of 2** · can explain
      both · knows what the sentence *"Workflow cannot yet be used as an LlmAgent sub-agent"* rules out
- [ ] **4.4** read · ran `shape.py` · saw **9 nodes, 9 edges, 3 routed, 1 DEFAULT_ROUTE, terminal
      `['human_queue', 'review']`** and the generated diagram · extended `mermaid` to print each node's
      class name · can name one thing a generated diagram still cannot tell you

## Section 5 — the first real graph

- [ ] **5.1** read · ran `triage.py` · saw **7 events, 7 events, 3 events** for the three tickets ·
      saw `draft`'s output carry the **raw** ticket from state and the sources from the join · ran
      `triage.py "my invoice is wrong"` · can name the two nodes that become agents on Day 58 and say
      why the other seven must not
- [ ] **5.2** read · ran all four `halfway.py` variants · saw **1 against 2 events** for the route typo
      and **2 against 5** for the starved join, both exit 0 · confirmed the starved join produced **no
      warning at all** · broke `triage.py`'s real graph by narrowing `ANSWERABLE` on one edge and found
      the node it stopped at

## Section 6 — in production

- [ ] **6.1** read · ran all four `boom.py` modes · saw the traceback land on **your** line, saw
      `--swallow` feed `"lookup failed"` into the next node, saw **three** `flaky` events with the
      first two `None`, and saw `NodeTimeoutError: Node 'slow' timed out after 0.3 seconds.` · added
      `exceptions=["ConnectionError"]` and changed the raise to `KeyError`, then counted the attempts
- [ ] **6.2** read · ran `shape.py` and reviewed the four numbers as if someone else wrote it · wrote
      the three shape assertions as a test, ran it green, deleted the `DEFAULT_ROUTE` edge and watched
      it go red · can say what an unexpected terminal node means

## Papers — after the parts

- [ ] **01 Dryad** read · ran `papers/dryad/job.py` and `job.py --sequential` · saw **1.53s against
      2.03s** with character-for-character identical results · added a fifth vertex and predicted both
      times before running · can answer out loud: what did the paper claim, and what do we do
      differently now

## The build

- [ ] `sutra/graph.py` written: `build_triage_graph()` is a **function**, `ANSWERABLE` is a `StrEnum`,
      and `graph_report()` returns the four numbers from 6.2.
- [ ] The nodes live outside `sutra/graph.py`. That file is wiring only.
- [ ] `tests/test_graph.py` written, with at least: the graph builds · the five stages are nodes · a
      `DEFAULT_ROUTE` exists · an incident **reaches `review`** (assert on the terminal node, not on
      the exit code) · the shape assertions from 6.2.
- [ ] **Break it on purpose and watch it go red:** delete the `DEFAULT_ROUTE` edge, run the tests, see
      the failure, put it back. Then narrow one research edge's route list, run the incident test, and
      confirm the terminal-node assertion catches the starved join.
- [ ] `uv run python days/day-53-graph-workflow-runtime/lab/gate.py; echo "exit: $?"` exits **0**, with
      **5/5 checks pass**.

## Gates and ledger

- [ ] `uv run ruff check .` and `uv run ruff format --check .` clean.
- [ ] `uv run python -m pytest -q -m "not live"` green.
- [ ] `./m depth 53` green — **21 parts + 1 paper**.
- [ ] `./m trace` shows ADK-32, ADK-33 and ADK-34 closed by day 53, and nothing else closed today.
- [ ] `./m wiki` regenerated.
- [ ] **Request budget honoured: 0 requests to every provider.** `git grep -n "generate_content"` in
      today's lab returns nothing.
- [ ] `docs/PROGRESS.md` row appended.
- [ ] `docs/PAPERS.md` row for `doi:10.1145/1272998.1273005` present.
- [ ] **No** `docs/PACKAGES.md` row — `google-adk==2.7.1` was pinned on Day 5 and is unchanged.
- [ ] Committed as
      `day 53: the graph Workflow Runtime - nodes, edges, the 2.x composition model - closes ADK-32, ADK-33, ADK-34`
