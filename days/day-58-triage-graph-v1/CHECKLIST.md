# Day 58 — Definition of done

`./m done 58` refuses to commit until every box is ticked. Tick a box only when you have actually run
the thing, not when you have read it.

## Before you start

- [ ] Day 57's parts and checklist are done, and the writer-critic box works standalone. Today gives
      it a seat; it does not rewrite it (P2).
- [ ] `uv run python days/day-58-triage-graph-v1/lab/gate.py; echo "exit: $?"` is **red** before you
      write anything, and you have read all **seven** findings rather than only counted them.
- [ ] `lab/` scaffolded per §3 — twenty-six files, two of them copied from Day 50's lab.
- [ ] `uv run python -c "import google.adk; print(google.adk.__version__)"` prints `2.7.1`.
- [ ] `git diff pyproject.toml uv.lock` is empty and stays empty. No package is added today.

## Section 1 — the floor

- [ ] **1.1** read · ran `ratio.py` and `model.py` · saw **10 stations, 2 that think** and
      **9.6 tickets per day** on a twenty-request allowance · saw the framework default
      `gemini-3.5-flash` differ from the repo's pin · can name the eight stations that spend nothing
- [ ] **1.2** read · ran `batons.py` and both arms of `seam.py` · watched a `dict` arrive as a
      `TriageResult` · reached the `ValidationError` naming `dynamic node 'downstream'`, the missing
      field and `input_value={'category': 'auth'}` · can say which side of a seam carries the
      annotation and why
- [ ] **1.3** read · ran `mouth.py` · saw `8842` and `''` both take the **not_found** lane at **0
      model calls** while `KB-104` cost 5 · ran `python -m doctest _stations.py` · can explain why
      normalising and existence-checking are two functions

## Section 2 — the guess and the honest exit

- [ ] **2.1** read · ran `escalate.py --sweep` · saw **26 of 52 tickets classified `other`** · found
      why `ticket:4506` is one of them · added `billing` to the rule's word list and re-ran
- [ ] **2.2** read · ran `escalate.py` · saw **3 stations / 1 call against 12 / 5** · ran the
      `Event(output='x', rout='ESCALATE')` one-liner and saw `route is: None` with **no exception** ·
      can say which channel the graph reads
- [ ] **2.3** read · ran `model.py` · saw the pin, the `output_schema`, both retry ladders and
      `requests sent 0` · read the `gemini-3.7-flash` row in `docs/PACKAGES.md` and can say how its
      quota number was obtained · can give the three honest responses to a 429, in order
- [ ] **2.4** read · ran `escalate.py` and `escalate.py --sweep` · saw the lane take **54%** ·
      changed `needs_human` to `category == "security"` and can say where the 26 tickets went

## Section 3 — the research floor

- [ ] **3.1** read · ran `clerks.py` and `clerks.py --sweep` · saw the archive clerk find
      **ticket:4610 for ticket:4521** across a vocabulary gap · saw **kb 8% against archive 100%** ·
      can say why both of those numbers are failures
- [ ] **3.2** read · ran `join.py` · saw the join's dict **keyed by node name** with `kb_clerk` first ·
      renamed `kb_clerk` without updating `assemble_evidence` and saw an empty `EvidenceBlock` with
      nothing raised
- [ ] **3.3** read · ran `price.py` · saw **0 / 1 / 3 / 5** per lane and **108 calls over 52 tickets,
      mean 2.08** · set `KNOBS.brake` to 1 and can say whether the saving was a cost cut or a quality
      cut

## Section 4 — the box

- [ ] **4.1** read · ran `box.py` · saw `draft_review_box` is a `Workflow` with 2 edges and 5 nested
      paths in the outer stream · can name the one thing the closed door does **not** protect
- [ ] **4.2** read · ran `brake.py`, `--brake 1` and `--brake 0` · saw **2 rounds / 5 calls** become
      **1 round / 3 calls FLAGGED** · saw `--brake 0` and `--brake 1` produce identical output and
      can say why · can give the argument for the critic owning the count
- [ ] **4.3** read · ran `stamp.py` · saw `reply is draft True` and `run twice, same True` on both
      cases · saw a reply cite **nothing** and be recorded honestly · can give the test for whether a
      field is safe for the last station to add

## Section 5 — the graph

- [ ] **5.1** read · ran `shape.py` · pasted the output into a mermaid renderer · saw **6 authored
      lines become 11 edges** · constructed the broken graph and reached
      `The following nodes are unreachable from START: ['escalate_lane', 'finalize']` · can name the
      three terminal stations
- [ ] **5.2** read · ran `register.py` · saw which parameters come from the edge and which from
      state · renamed `ticket_text` in `intake` only and saw the clerks return nothing with no error ·
      can say why the writer's `node_input` is unannotated

## Section 6 — the run as a fact

- [ ] **6.1** read · ran `stream.py`, `stream.py 8842` and `stream.py ticket:4562` · reconstructed
      the 4562 run's lane and cost **from the stream alone** · can say which single fact tells you a
      run finished
- [ ] **6.2** read · ran `casefile.py` on 4610, 4521 and 4562 · saw **7 of 8 questions answered** and
      `flagged` come back `-- not recorded --` · can say why that sentinel beats `False`
- [ ] **6.3** read · ran `launder.py` and `launder.py --off` · saw **2 stations / 0 calls** become
      **10 / 3** and a reply reading `Thanks for reporting ticket:8842` · noticed it quoted a real
      customer's ticket · can say why laundering **improves** your metrics
- [ ] **6.4** read · ran `drift.py --drift` and saw the traceback land **in `writer`**, two stations
      from the cause · ran `swallow.py --swallow` and saw
      `Dear customer, Sorry, I could not search the archive` with **exit 0** · can name the five
      things a swallowed exception costs

## Section 7 — acceptance

- [ ] **7.1** read · ran `invariants.py` · saw **5 node tests pass and 4 of 24 replies cite a
      source** · can explain why no station is at fault · added a sixth invariant of your own and ran
      it
- [ ] **7.2** read · ran `gate.py` and saw **0/7, exit 1** · added an eighth check and confirmed it
      is red · can map every check back to a sentence in a part

## Section 8 — in production

- [ ] **8.1** read · ran `stream.py ticket:4521` and `casefile.py ticket:4521` · saw an **APPROVED,
      first-round, three-call run whose reply contains no fix** · added a rubric item for empty
      evidence and can say who now has more work
- [ ] **8.2** read · ran `escalate.py --sweep` · saw **28 escalations of which 26 are `other`** and
      severity carrying **1 ticket in 52** · widened two rule word lists and recorded the new rate ·
      can say why "stop escalating `other`" is the dangerous fix
- [ ] **8.3** read · ran `scale.py` and `scale.py --retry` · reached
      `NodeTimeoutError: Node 'slow_clerk' timed out after 0.05 seconds.` · saw **3 events for 1
      result** on the retry arm · can say why a branch that times out before a join is worse than one
      that raises

## Build brief

- [ ] `sutra/triage.py` written: five batons and the stations, `TODO(me)` markers solved by you.
- [ ] `sutra/graph.py` gains `build_triage_graph_v1()`, and it is a **function**.
- [ ] `sutra/acceptance.py` written: `escalated_runs_produce_no_draft`, `replies_cite_something`,
      `run_stays_in_budget`.
- [ ] `tests/test_triage_graph.py` written, including one test you **break on purpose, watch go red,
      and fix**.

## Gates

- [ ] `uv run python days/day-58-triage-graph-v1/lab/gate.py; echo "exit: $?"` exits **0**, or exits
      1 **only** on the citation invariant — and you have written down which, and why that is a
      retrieval finding rather than a gate to weaken.
- [ ] `uv run python -m pytest -q -m "not live"` passes.
- [ ] `./m depth 58` is green: 24 parts.
- [ ] `./m trace` shows day 58 closing exactly `ADK-41, ADK-42`.
- [ ] Request budget honest: **0** requests to every provider today, and you can say why that was
      possible.

## Ledger

- [ ] `docs/PROGRESS.md` row pasted from §11, with the real hash.
- [ ] `docs/PACKAGES.md` — no new row, and you confirmed the installed version rather than assuming.
- [ ] `docs/PAPERS.md` — no new row; the three cited papers already have theirs.
- [ ] Committed: `day 58: the triage graph v1 end to end - closes ADK-41, ADK-42`, and `git ls-files`
      is free of any secret.
