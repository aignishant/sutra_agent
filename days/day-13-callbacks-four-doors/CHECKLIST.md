# Day 13 — CHECKLIST

**IDs closed:** ADK-14, ADK-15
**Principles served:** 1, 2, 4, 6, 8, 9, 10, 11, 13, 15, 16, 17, 18
**Parts:** 19 across 6 sections, no papers

> `./m done 13` refuses to commit while any box below is unticked. It cannot tell whether you were
> honest — that part is yours.

## Demo command

```bash
cd days/day-13-callbacks-four-doors/lab
uv run python falsy.py
uv run python poisoned.py
uv run python injected.py
cd -
uv run python -m pytest tests/test_callbacks.py -q -m "not live"
./m check && uv run python scripts/trace.py && git log --oneline -1
```

Expected: seven return values of which five skip the tool; a run where `>> lookup_ticket actually
ran` is **absent** and the model was told your log record; one tool in and two tools out; then five
passed and one skipped; then `OK all green`, then `traceability: 25/199 closed, 0 problem(s)`, then
one commit reading `day 13: callbacks - four doors and one rule - closes ADK-14, ADK-15`.

---

## Before you write anything

- [ ] `./m check` is green and `scripts/trace.py` shows Day 12's count before you change anything
- [ ] Wrote `lab/scripted.py` **first**, from part 1.3, and can say why `generate_content_async`
      yields rather than returns (1.3, trap #3)
- [ ] Can say why all nineteen of today's lab scripts cost nothing, without using the word "mock"
- [ ] Ran every lab script from **inside** `lab/`, and know why `from scripted import ...` needs that

## Section 1 — the mechanics every door shares

- [ ] Ran `lab/wiring.py` and saw `fired so far: 0` (1.1)
- [ ] Can name all six hooks and say which two are parked today (1.1)
- [ ] Added `before_tool_callback=announce` to the same agent and confirmed nothing fired (1.1)
- [ ] Ran `lab/names.py` and read **which** parameter name the `TypeError` complains about (1.2)
- [ ] Renamed a parameter of `right` and confirmed the message names the one you did not write (1.2)
- [ ] Can recite the parameter names for `before_tool_callback` and `after_tool_callback` (1.2)
- [ ] Ran `lab/one_rule.py` and saw `model calls: 0` on the short-circuit (1.3)
- [ ] Changed `veto` to `return None` and watched `the tool actually ran` come back (1.3)
- [ ] Can state the one rule in a single sentence (1.3)
- [ ] Ran `lab/a_list.py` and confirmed `3 never` is absent from case **a** (1.4)
- [ ] Saw case **b**'s missing audit line and can say why that is an ordering bug, not a logging bug
      (1.4)
- [ ] Moved `never` to the front and predicted the output **before** running it (1.4)

## ADK-14 — the model doors (section 2)

- [ ] Ran `lab/the_request.py` and saw one question produce **two** requests (2.1)
- [ ] Can name the four fields of an `LlmRequest` (2.1)
- [ ] Can say why the tool result appears in `contents` with `role="user"` (2.1)
- [ ] Added a second tool and watched both `declared tools` and the instruction length change (2.1)
- [ ] Ran `lab/shaping.py` and saw the turn count go 1, 3, 5 and then 1, 2, 2 (2.2)
- [ ] Changed `add_a_rule` to `return llm_request` and read the error before undoing it (2.2)
- [ ] Can say the difference between mutating `llm_request` and returning a value (2.2)
- [ ] Can say why `append_instructions` exists instead of `+=` (2.2)
- [ ] Ran `lab/shortcut.py` and saw `model calls actually made: 1 of 3 questions` (2.3)
- [ ] Added `"hi"` to `CANNED`, asked `"hi there"`, confirmed it was **not** matched (2.3)
- [ ] Can say why a skipped call does not count against `max_llm_calls` (2.3)
- [ ] Ran `lab/redact.py` and saw the key removed while the sentence survived (2.4)
- [ ] Removed the first guard line, scripted an empty reply, read the `AttributeError`, put it back
      (2.4)
- [ ] Can say why the very first line of an after-model callback checks that `content` exists (2.4)
- [ ] Ran `lab/per_chunk.py` and saw **one** model call produce **three** firings (2.5)
- [ ] Split a key across two fragments, attached `redact.py`'s guard, and watched it come through
      (2.5)
- [ ] Can say the two lines of defence a production after-model callback starts with (2.5)

## ADK-15 — the tool doors (section 3)

- [ ] Ran `lab/register.py` and saw one invocation id down the column (3.1)
- [ ] Saw `kb_searches: 2` survive in **session state**, not in a module variable (3.1)
- [ ] Mutated `args["query"]` in the callback and confirmed the tool received the change (3.1)
- [ ] Can name the three parameters `before_tool_callback` receives and what each is for (3.1)
- [ ] Ran `lab/refusal.py` and confirmed `>> search_kb actually ran` appears in **none** of the three
      (3.2)
- [ ] Sat with what case **a** would make your agent tell a customer (3.2)
- [ ] Can name the three fields an honest refusal carries and what each is for (3.2)
- [ ] Can say what the model uses to tell your refusal from a real tool result — and that it cannot
      (3.2)
- [ ] Ran `lab/return_leg.py` and saw 415 characters become 188 (3.3)
- [ ] Confirmed `customer_email` and `internal_notes` never reached the model (3.3)
- [ ] Added a second returning `after_tool_callback` and confirmed it never runs (3.3, 4.1)
- [ ] Can say why a truncating callback must add a field saying it truncated (3.3)
- [ ] Ran `lab/error_doors.py` and saw all three cases: raise, log-and-raise, substitute (3.4)
- [ ] Changed `honest` to return a cheerful `status: ok` and read what the model would be told (3.4)
- [ ] Can say which exceptions a production error hook refuses to substitute for, and why (3.4)
- [ ] Can name 1.x → 2.x trap #4 and say what ADK 2.x does instead (3.4)

## Section 4 — where the rule bites

- [ ] Ran `lab/falsy.py` and confirmed `>> the tool actually ran` is missing from cases b, c, d, f
      (4.1)
- [ ] Saw `0` and `False` arrive at the model as `{'result': ...}` (4.1)
- [ ] Can explain why case **e** and case **f** differ, in terms of the loop's assignment (4.1)
- [ ] Predicted what `[returns({}), returns({})]` does before running it (4.1)
- [ ] Went through every callback you wrote today and checked each branch for a falsy return
      (4.1, `TODO(me)`)
- [ ] Ran `lab/gate_order.py` and confirmed `2 agent before_tool_callback` is absent from case **b**
      (4.2)
- [ ] Added a `before_model_callback` at both layers and confirmed the same ordering (4.2)
- [ ] Can give the one question that decides plugin versus callback (4.2)
- [ ] Ran `lab/injected.py` and saw two tool names where you wrote one (4.3)
- [ ] Recorded whether `capabilities.output_schema_and_tools` is `False` on **your** machine
      (4.3, `TODO(me)`)
- [ ] Removed `output_schema` and confirmed `set_model_response` and `state['triage']` both vanish
      (4.3)
- [ ] Decided the `FRAMEWORK_TOOLS` policy and wrote down why (4.3, `TODO(me)`)

## 💥 Failure lab (section 5)

- [ ] Ran `lab/poisoned.py` and confirmed `>> lookup_ticket actually ran` is missing from case **b**
- [ ] Read the `the model was told:` line in case **b** and can say what the model would answer from
- [ ] Made the `{"status": "logged", ...}` edit and wrote one sentence on why it is worse (5.1 step 2)
- [ ] Wrote down the assertion in your own suite that would have caught it — **before** reading 6.1
      (5.1 step 3, `TODO(me)`)
- [ ] Can say what the bug report will say when this happens in production
- [ ] Removed the `return` and confirmed the agent healed

## Section 6 — testing it, and what belongs in it

- [ ] Wrote `tests/test_callbacks.py` and watched it go **RED** before writing
      `sutra/desk/callbacks.py`
- [ ] Test 1 green: the observer returns `None`
- [ ] Test 2 green: an ordinary query is not blocked
- [ ] Test 3 green: a credential query is blocked, with a `status` and a `next`
- [ ] Test 4 green: the refusal does not echo the query
- [ ] Test 5 green: the tool actually ran on the ordinary path
- [ ] **Broke it on purpose:** added `return summary` to `audit_tool_calls`, watched **two** tests go
      red, and fixed it
- [ ] **Broke it on purpose:** made the guard return `{}` on the carry-on path, watched tests 2 and 5
      go red, and fixed it
- [ ] **Broke it on purpose:** renamed a parameter to `arguments`, watched **all five** go red, and
      fixed it
- [ ] Left the sixth test skipped with its `TODO(me)`, and can say what a green suite would be
      implying without it
- [ ] Can say which of the five assertions needs a whole agent run, and why the other four do not
      (6.1)
- [ ] Can say what a `Mock` tool context would do to test 2 (6.1)
- [ ] Ran `lab/cost_of_a_door.py` and saw blocking and async diverge only under concurrency (6.2)
- [ ] Raised concurrency to 16 and watched which line moved (6.2, `TODO(me)`)
- [ ] Can say how many times the doors fire for one question on an agent making two tool calls (6.2)
- [ ] Can list three things that belong in a callback and three that do not (6.2)

## The build

- [ ] `sutra/desk/callbacks.py` exists with `audit_tool_calls`, `blocked`, `block_forbidden_queries`,
      `FORBIDDEN` and `FRAMEWORK_TOOLS`
- [ ] `audit_tool_calls` is annotated `-> None` and has **no `return` statement at all**
- [ ] `block_forbidden_queries` is annotated `-> dict | None` and returns `None` on every carry-on
      path
- [ ] The refusal never quotes the query, and you checked by reading it rather than by assuming
- [ ] Wrote the allow-list of argument names whose values may be logged, and justified each
      (3.1, `TODO(me)`)
- [ ] `sutra/desk/agent.py` attaches the two as a **list**, observer first, and nothing else changed
- [ ] `sutra/desk/tools.py` and `sutra/desk/schemas.py` are **unchanged** — confirmed with `git diff`
- [ ] Wrote down which of the two callbacks you think belongs in a plugin, before reading Day 14
      (`TODO(me)`)

## Budget & gate

- [ ] Total model calls today: **0 of 20** — and you can say why the day needed none
- [ ] If you spent the optional request, you recorded what a real run showed that a scripted one
      cannot
- [ ] `uv run ruff check .` clean
- [ ] `uv run ruff format --check .` clean
- [ ] `uv run python -m pytest -q -m "not live"` green
- [ ] `./m depth 13` green
- [ ] `./m check` prints `OK all green`

## Ledger & commit

- [ ] `docs/PROGRESS.md` row appended with the **date and hash you actually observed**:
      `| 13 | <date> | ADK-14, ADK-15 | 19 | <hash> | ✅ |`
- [ ] `docs/PACKAGES.md` — no new rows, **unless** your machine's `output_schema_and_tools` or your
      concurrency numbers disagree with the day, in which case you added the row
- [ ] `docs/PAPERS.md` — no new rows, and you can say why today teaches no paper
- [ ] `docs/SKILL_PROVENANCE.md` — no new rows
- [ ] `git status` shows no `.env`
- [ ] Committed: `day 13: callbacks - four doors and one rule - closes ADK-14, ADK-15`
- [ ] `uv run python scripts/trace.py` shows ADK-14 and ADK-15 closed and `0 problem(s)`
