# Day 12 — CHECKLIST

**IDs closed:** ADK-13
**Principles served:** 1, 2, 4, 6, 8, 9, 10, 11, 13, 15, 16, 17, 18
**Parts:** 16 across 6 sections, plus one paper

> `./m done 12` refuses to commit while any box below is unticked. It cannot tell whether you were
> honest — that part is yours.

## Demo command

```bash
uv run python days/day-12-structured-output/lab/capability.py
uv run python days/day-12-structured-output/lab/silenced.py
cd days/day-12-structured-output/lab/papers/guided-generation && uv run python generate.py && uv run python generate.py --no-guide && cd -
uv run python -m pytest tests/test_schema.py -q -m "not live"
./m check && uv run python scripts/trace.py && git log --oneline -1
```

Expected: `output_schema_and_tools = False`; four honest answers rejected and spam filed as billing;
`{"urgency": 99}` valid in 5 lookups against invalid prose in 72; a green schema suite; then
`OK all green`, then `traceability: 23/199 closed, 0 problem(s)`, then one commit reading
`day 12: structured output - a shape on the way out - closes ADK-13`.

---

## Before you write anything

- [ ] `./m check` is green and `scripts/trace.py` shows Day 11's count before you change anything
- [ ] Ran `lab/shape.py` and can name the two fields it sets (1.1)
- [ ] Ran `lab/capability.py` **early** and wrote down which path your machine is on (3.1, `TODO(me)`)
- [ ] Can say why all sixteen of today's lab scripts cost nothing
- [ ] Read `sutra/desk/agent.py`'s instruction once, knowing today changes what most of it applies to

## ADK-13 — the two fields (section 1)

- [ ] Ran `lab/shape.py` and saw `mime` and `response_schema` appear together (1.1)
- [ ] Added a tool to the schema agent and watched both fields go back to `None` (1.1)
- [ ] Can say who enforces the schema on the no-tools path, and what a prompt instruction is instead
      (1.1)
- [ ] Ran `lab/address.py` and saw the code fence in the unparsed version (1.2)
- [ ] Saw `ticket_id` **disappear** because it was `null` (1.2)
- [ ] Can say the one line ADK runs for `output_key`, and which day you met it (1.2, Day 11 2.1)
- [ ] Ran `lab/accepts.py` and saw three different Python types come back (1.3)
- [ ] Fed the raw-dict case a reply that does not match its schema and watched it be accepted (1.3)
- [ ] Can name the five shapes and say which one skips validation (1.3)
- [ ] Ran `lab/as_a_tool.py` and compared the two declarations (1.4)
- [ ] Can say when `input_schema` takes effect and when it is inert (1.4)

## Writing a schema somebody can fill in (section 2)

- [ ] Ran `lab/fillable.py` and saw the nested version was the **larger** declaration (2.1)
- [ ] Can give the five rules, and the test for whether a schema asks the right participant (2.1)
- [ ] Ran `lab/optional.py` and found the two rows that are identical (2.2)
- [ ] Can say why `needs_human: false` survives and `ticket_id: null` does not (2.2)
- [ ] Can give the three declarations and the sentence each says to the model (2.2)
- [ ] Ran `lab/dropped.py` and read the `lost` line (2.3)
- [ ] Changed `urgency` to a `Literal` and watched the range reappear in the `enum` (2.3)
- [ ] Can say **why** descriptions and bounds are lost, in terms of `inspect.Parameter` (2.3)
- [ ] Can say where the dropped constraint went and what it costs each time it fires (2.3)
- [ ] Ran `lab/the_prompt_again.py` and read 522 against 282 (2.4)
- [ ] Can say the right lever for shrinking a schema and the wrong one (2.4)
- [ ] Can say why the workaround column's smaller number is not good news (2.4)

## The path Sutra is actually on (section 3)

- [ ] Ran `lab/capability.py` and saw an agent with **both** `output_schema` and `tools` construct with
      no error (3.1)
- [ ] Read `basic.py`'s three-line `if` for yourself (3.1)
- [ ] Can state the old rule, the current rule, and the expression that decides (3.1)
- [ ] Can say which Day-5 decision put Sutra on the workaround path (3.1)
- [ ] Ran `lab/the_cost.py` and saw `set_model_response` in the declared tools (3.2)
- [ ] Printed the **whole** system instruction and read the appended paragraph (3.2, `TODO(me)`)
- [ ] Can name the two things ADK adds, and which one is the enforcement (3.2)
- [ ] Can say why nothing downstream notices the workaround (3.2)
- [ ] Ran `lab/the_bill.py` and read the `enforced by` row (3.3)
- [ ] Can say what the workaround path is **cheaper than**, and by how much (3.3)
- [ ] Recorded a decision about the LiteLLM lane, either way (3.3, `TODO(me)`)

## When a schema lies (section 4)

- [ ] Ran `lab/valid_not_true.py` and saw four of five accepted (4.1)
- [ ] Wrote a sixth candidate wrong in a new way and predicted the verdict first (4.1, `TODO(me)`)
- [ ] Can give the three ways an answer is wrong while valid, and which no check will catch (4.1)
- [ ] Can say what tightening the schema buys, and what it costs on Sutra's path (4.1)
- [ ] Ran `lab/always_filled.py` and saw the **honest** answer rejected (4.2)
- [ ] Can say what `required` actually instructs the model to do (4.2)
- [ ] Can say why making a field nullable is a breaking change (4.2)
- [ ] Justified every field in `Triage`'s `required` list, out loud (4.2, `TODO(me)`)

## 💥 The failure lab (section 5)

- [ ] Ran `lab/silenced.py` and saw all four honest attempts rejected (5.1)
- [ ] Read the one thing `Closed` accepts, and can say what that means for spam (5.1)
- [ ] Added `"other"` and a fifth attempt, and confirmed the original four **still** fail (5.1)
- [ ] Can say why an escape hatch on a field is different from one on the answer (5.1)
- [ ] `Triage` has an `outcome` discriminator with a written downstream action per value (5.1,
      `TODO(me)`)

## In the graph (section 6)

- [ ] Ran `lab/handoff.py` and read the rendered instruction (6.1)
- [ ] Noticed the value is Python's `repr`, not JSON (6.1)
- [ ] Seeded `{"outcome": "not_a_ticket"}` and worked out what the responder would write (6.1)
- [ ] Can name the three pieces the hand-off is made of and where you met each (6.1)
- [ ] Wrote down what the first consumer of `state["triage"]` will be (6.1, `TODO(me)`)
- [ ] Ran `lab/testing.py` with **no `GOOGLE_API_KEY` set** and saw four passes (6.2)
- [ ] Can give the four free assertions and the question none of them can answer (6.2)
- [ ] Can say why a golden fixture should contain a code fence (6.2)

## The paper — after the parts, not before

- [ ] Read [`papers/01-guided-generation.md`](papers/01-guided-generation.md) **after** finishing the
      parts
- [ ] Ran the demo and **the ablation**, and compared 5 examinations against 72
- [ ] Can say what the index maps, and why it can be built before generation starts
- [ ] Noticed the guided run produced `99` — valid, and the wrong number (4.1)
- [ ] Can say the one situation where building the index is not worth it
- [ ] Can say which half of the paper is now infrastructure and which half is niche
- [ ] `docs/PAPERS.md` row present, with the title copied from the arXiv record and the date you
      looked it up

## Wiring Sutra

- [ ] `sutra/desk/schemas.py` written, with `outcome` as the only required field
- [ ] `urgency`'s range lives somewhere the model will see it, and you can say why not the other two
      places (2.3, `TODO(me)`)
- [ ] `category` has **no** `"other"` value (5.1, 2.1)
- [ ] `sutra/desk/agent.py` sets `output_schema` and `output_key` and nothing else
- [ ] Decided what happens to Day 6's persona instruction now that most of it applies to `summary`
      (`TODO(me)`)
- [ ] `sutra/desk/tools.py` **unchanged** — checked with `git diff --stat`, not assumed

## Tests — each one red, then green

- [ ] `tests/test_schema.py` written and passing (§5)
- [ ] Reduced `outcome` to one value, watched the first go red, put it back
- [ ] Made `summary` required, watched the second go red, put it back
- [ ] Renamed a field, watched the third go red, put it back
- [ ] Changed `urgency` to `int`, watched the fourth go **green when it should not**, put it back
- [ ] The fifth test is a `TODO(me)` naming Day 25, not a test that pretends
- [ ] Day 10's and Day 11's tests still pass unchanged
- [ ] `uv run python -m pytest -q -m "not live"` green across the whole suite

## The request budget

- [ ] Spent **0** requests, or knows exactly which optional run cost the ones it spent (§6)
- [ ] `GOOGLE_GENAI_USE_VERTEXAI=FALSE` still set, and `require_free_tier()` still runs at import

## Ledger & commit

- [ ] `docs/PROGRESS.md` row appended, with the real date, the real hash and 16 parts
- [ ] `docs/PACKAGES.md` — no row owed, unless your resolved variant differs from this document's
- [ ] `docs/PAPERS.md` — the `arXiv:2307.09702` row present and dated
- [ ] `./m check` green: ruff, format, pytest, depth, trace
- [ ] `uv run python scripts/trace.py` shows ADK-13 closed and no problems
- [ ] `sutra/loop.py`, `sutra/agent.py` and `sutra/desk/tools.py` are **unchanged**
- [ ] One commit, message exactly as in the hub's §11, naming the persona decision
