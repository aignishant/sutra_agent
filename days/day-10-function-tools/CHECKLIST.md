# Day 10 — CHECKLIST

**IDs closed:** ADK-10, ADK-11
**Principles served:** 1, 2, 4, 6, 8, 9, 10, 11, 13, 15, 16, 17, 18
**Parts:** 16 across 7 sections, no papers

> `./m done 10` refuses to commit while any box below is unticked. It cannot tell whether you were
> honest — that part is yours.

## Demo command

```bash
uv run python days/day-10-function-tools/lab/watch_the_loop.py 2>&1 >/dev/null
uv run python -m pytest tests/test_tools.py -q -m "not live"
./m check && uv run python scripts/trace.py && git log --oneline -1
```

Expected: a trace with `call` and `result` events between the question and the answer; a green tool
suite; then `OK all green`, then `traceability: 20/199 closed, 0 problem(s)`, then one commit reading
`day 10: function tools in ADK - the forms print themselves - closes ADK-10, ADK-11`.

---

## Before you write anything

- [ ] `./m check` is green and `scripts/trace.py` shows Day 9's count before you change anything
- [ ] Ran `lab/generated.py` and can say what the four rows of the declaration come from (1.1)
- [ ] Opened `sutra/tools.py` — Day 4's hand-written declarations — and read it once, knowing today
      decides its fate (5.1)
- [ ] Can say why fourteen of today's sixteen lab scripts cost nothing

## ADK-10 — the declaration is generated (section 1)

- [ ] Ran `lab/generated.py` and compared the generated schema with `LOOKUP_TICKET` line by line (1.1)
- [ ] Found **more than two** differences between them (1.1)
- [ ] Tried `tools=[lookup_ticket()]` on purpose and read all **three** validation errors (1.1)
- [ ] Ran `lab/docstring.py` and saw the whole docstring in the description (1.2)
- [ ] Counted the description characters and compared with Day 4's declaration (1.2)
- [ ] Saw `per-parameter 'description' fields: 0` and can say where the `Args:` lines went (1.2)
- [ ] Ran `lab/docstring_flag.py` and confirmed the finding holds on **both** code paths (1.2)
- [ ] Can give the four things a tool docstring owes, in order (1.2)
- [ ] Ran `lab/hints.py` and can say what decides whether a parameter is required (1.3)
- [ ] Saw `ticket_id : {}` for the unannotated one and understood what the model is being asked (1.3)
- [ ] Added a `Literal[...]` parameter, predicted both output lines, then ran it (1.3)
- [ ] Can say the one case where adding an `enum` would be a mistake, and why Day 4 decided that (1.3)
- [ ] Ran `lab/late.py` and saw construction validate nothing (1.4)
- [ ] Removed `sloppy` and ran it again, so you have seen the check pass as well as fail (1.4)
- [ ] Can name the other two ADK fields that derive late, and what all three have in common (1.4)

## ADK-11 — what a tool returns (section 2)

- [ ] Ran `lab/returns.py` and read the **miss** column down the page (2.1)
- [ ] Can say why a boolean cannot carry the three outcomes you actually have (2.1)
- [ ] Can say what one extra key turns "nothing found" into (2.1)
- [ ] Ran `lab/wrapping.py` and saw both sides of the `{"result": ...}` wrap (2.2)
- [ ] Can say **where** the wrapping happens, and why that matters when writing a test (2.2)
- [ ] Looked at `{"result": null}` and can say what the model can and cannot conclude from it (2.2)
- [ ] Ran `lab/failing_tools.py` and saw all four shapes (2.3)
- [ ] Set `INDEX_IS_UP = True` and ran it again (2.3)
- [ ] Can give the one question that decides between returning a result and raising (2.3)
- [ ] Can say what a caught-and-apologised failure looks like to the runtime, the trace and an eval
      (2.3)

## The dispatch you deleted (section 3)

- [ ] Ran `lab/seams.py` and read both declarations side by side (3.1)
- [ ] Can name the five things ADK took and the four you kept (3.1)
- [ ] Can say the class of bug that disappeared, and why it went without anybody being more careful
      (3.1)
- [ ] Ran `lab/watch_the_loop.py` and saw `call` and `result` events (3.2)
- [ ] **Counted the model calls** one triage cost, and wrote the number down (3.2, `TODO(me)`)
- [ ] Can say which of the four event kinds answer `True` to `is_final_response()` (3.2)
- [ ] Ran `lab/runaway.py` and watched `max_llm_calls` stop it (3.3)
- [ ] `DESK_RUN_CONFIG` written with **your** arithmetic in the comment, not this document's number
      (3.3, `TODO(me)`)
- [ ] Checked it is passed to `run_async` and not attached to the runner (3.3)
- [ ] Can name the three limits and their scopes, and say why the default of 500 is not a decision
      (3.3)

## Tool shapes (section 4)

- [ ] Ran `lab/long_running.py` and read the `NOTE:` ADK appended to the description (4.1)
- [ ] Can say which of `LongRunningFunctionTool`'s two effects is a prompt rather than a guarantee
      (4.1)
- [ ] Can say what the `job_id` is for and what breaks without it (4.1)
- [ ] Ran `lab/confirmation.py` and saw the conditional gate fire on the large amount only (4.2)
- [ ] Can say why a gate on every tool call is worse than no gate (4.2)
- [ ] Confirmed `sutra/desk/tools.py` contains **only read tools** (4.2)

## Wiring Sutra (section 5)

- [ ] `sutra/desk/tools.py` written, with both *when not to use this* sentences (5.1)
- [ ] `TICKETS` holds records rather than strings (5.1, 2.1)
- [ ] Every return is a dict with a status, and every miss echoes its input (5.1, 2.1)
- [ ] `sutra/desk/agent.py` registers both tools with **no parentheses** (5.1)
- [ ] The agent's `description` no longer says it cannot look anything up (5.1)
- [ ] Decided what happens to `sutra/tools.py` and did it in this commit (5.1, `TODO(me)`)
- [ ] Decided whether `search_kb` returning only the first match stays (5.1, `TODO(me)`)
- [ ] The honesty section rewritten: what it **can** see, what it still cannot, and `not_found` named
      (5.2)
- [ ] Ran the trace and confirmed the tool-call count is **not zero** (5.2, 3.2)
- [ ] Re-ran Day 6's three probes and wrote a verdict for each (5.2, `TODO(me)`)
- [ ] Noticed the honesty probe's correct answer has **changed**, and wrote down what that means for
      an evalset (5.2, `TODO(me)`)
- [ ] Replaced or deleted Day 6's now-vacuous guard test, and said which in the commit message (5.2,
      `TODO(me)`)

## 💥 The failure lab (section 6)

- [ ] Ran `lab/no_label.py` and saw **both** versions raise (6.1)
- [ ] Can say the one thing an annotation buys and the one thing it does not (6.1)
- [ ] Can name the six layers that accept an untyped parameter (6.1)
- [ ] Removed one annotation from `sutra/desk/tools.py`, watched the test go red, put it back (6.1)
- [ ] Can say why a better docstring is not a fix, and why a defensive cast is not a substitute (6.1)

## Limits (section 7)

- [ ] Ran `lab/what_a_schema_cannot_say.py` and saw five `True`s (7.1)
- [ ] Can name the four questions a schema cannot answer, and which mechanism answers each on which
      day (7.1)
- [ ] Can say why tightening a schema is usually the wrong response to any of the four (7.1)
- [ ] Can say what prompt injection produces, and why shape-checking layers pass it through (7.1)

## Tests — each one red, then green

- [ ] `tests/test_tools.py` written and passing (§5)
- [ ] Removed a type hint, watched the first test go red naming the tool and parameter, put it back
- [ ] Renamed `search_kb`, watched the second go red, and can say why a rename is a contract change
- [ ] Dropped the id from the `not_found` return, watched the third go red, put it back
- [ ] Returned a bare string from a tool, watched the fifth go red, put it back
- [ ] Wrote the sixth test: the handbook claims only capabilities that exist (`TODO(me)`)
- [ ] `uv run python -m pytest -q -m "not live"` green across the whole suite

## The request budget

- [ ] Spent **9 or fewer** requests, and know which parts they went to (§6)
- [ ] Ran all fourteen zero-cost scripts before any that costs quota
- [ ] `GOOGLE_GENAI_USE_VERTEXAI=FALSE` still set, and `require_free_tier()` still runs at import

## Ledger & commit

- [ ] `docs/PROGRESS.md` row appended, with the real date, the real hash and 16 parts
- [ ] `docs/PACKAGES.md` — confirmed no row is owed, unless your version's schema behaviour differs
      from this document's, in which case it is a row
- [ ] `docs/PAPERS.md` — confirmed no row is owed, and can say why Toolformer is not re-taught
- [ ] `./m check` green: ruff, format, pytest, depth, trace
- [ ] `uv run python scripts/trace.py` shows ADK-10 and ADK-11 closed and no problems
- [ ] `sutra/loop.py` and `sutra/agent.py` are **unchanged** — checked with `git diff --stat`, not
      assumed
- [ ] One commit, message exactly as in the hub's §11, naming what happened to `sutra/tools.py`
