---
day: 12
phase: 2
phase_name: "Models & tools"
title: "Structured output — a shape on the way out"
ids: ["ADK-13"]
principles: [1, 2, 4, 6, 8, 9, 10, 11, 13, 15, 16, 17, 18]
kind: lab
plan_version: "v2.2.1"
parts: 16
generated: "2026-08-27"
status: written
lab_scaffolded: false
commit: ""
---

# Day 12 — Structured output: a shape on the way out

> **Yesterday (Day 11):** one extra parameter connected a tool to the session it was running beside —
> state, identity, the event it becomes part of — and the second half of the day was the design
> discipline that keeps that power safe.
> **Today:** the same move on the answer. Day 10 gave the model's *requests* a declared shape; today its
> *replies* get one, it lands in state under a name, and the whole thing turns out to run on a mechanism
> that is not the one everybody assumes.
> **Tomorrow (Day 13):** callbacks — before and after the model, before and after a tool, holding the
> same context object Day 11 introduced.

---

## §1 Where we are

The queue at a government office, and the two windows.

At the first window there is a person who will listen to anything. You explain your problem in your own
words, they nod, they ask a question, they write something on a pad. It is a good conversation and at
the end you are given a slip of paper with a sentence on it.

At the second window they will not take the slip. They want the form — the printed one, with the boxes
— because the second window is not a person listening, it is a person **entering data**, and a sentence
does not go into a box.

So somebody, at some point, sat down and worked out which boxes there should be. That exercise is
harder than it looks and it is the whole of today. Too few boxes and the form cannot hold what people
actually come in with. Too many and everybody fills in the ones they cannot answer. And there has to be
a box for *"this is not what this form is for"*, or the first person with an unusual problem produces a
completed form that says something false.

Everything Sutra has produced so far has been the first window. From today it produces the form — and
Phase 8's router is the second window, which cannot read sentences.

Two things about today are worth flagging before you start.

**The mechanism is not the one you will assume.** "The provider enforces the schema" is true for an
agent with no tools and **false for Sutra**, and the thing that happens instead is a tool ADK writes and
an instruction ADK appends. Section 3 is that, measured. It is the most surprising part of the day and
it changes what you should write in your schemas.

**And the schema will lie to you if you let it.** A valid answer is not a true one, and a required
field is an order to always have an answer. Sections 4 and 5 are the two ways that goes wrong, and the
second is today's failure lab.

---

## §2 The map

Sixteen parts in six sections, and one paper.

The paper is **Efficient Guided Generation for Large Language Models** (`arXiv:2307.09702`), which is
the machinery underneath *"the provider guarantees the shape"* — a finite-state machine over the
structure and a precomputed index over the vocabulary. Read it **after** the parts: Principle 4 at the
scale of a day. The last part points at it.

The day climbs `foundation → working → production`: section 1 is the two fields, section 2 is writing a
schema somebody can fill in, section 3 is what really happens when an agent has tools, section 4 is what
a schema cannot check, section 5 breaks it, and section 6 is the hand-off and the tests.

### Section 1 — `01-the-shape-on-the-way-out`: ADK-13, the two fields

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [A shape on the answer](parts/01-the-shape-on-the-way-out/1.1-a-shape-on-the-answer.md) | Two fields on the request, and who enforces them | `foundation` |
| 1.2 | [The answer with an address](parts/01-the-shape-on-the-way-out/1.2-the-answer-with-an-address.md) | Day 11's `state_delta`, written by the framework — and the field that vanishes | `working` |
| 1.3 | [What `output_schema` accepts](parts/01-the-shape-on-the-way-out/1.3-what-output-schema-accepts.md) | Five shapes, three Python types out, one with no validation | `working` |
| 1.4 | [🅿️ The sheet you fill in before you are called](parts/01-the-shape-on-the-way-out/1.4-the-sheet-you-fill-in-before-you-are-called.md) | The mirror field, and the one situation where it does anything | `production` |

### Section 2 — `02-schemas-in-practice`: writing one somebody can fill in

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [A schema a model can fill](parts/02-schemas-in-practice/2.1-a-schema-a-model-can-fill.md) | Five rules, and why the database-shaped version was the *larger* one | `working` |
| 2.2 | [Optional, default, and null](parts/02-schemas-in-practice/2.2-optional-default-and-null.md) | Three instructions, and two replies that arrive identical | `working` |
| 2.3 | [The descriptions that do not arrive](parts/02-schemas-in-practice/2.3-the-descriptions-that-do-not-arrive.md) | Every description and both bounds, gone — and where the constraint went | `production` |
| 2.4 | [The schema is the prompt again](parts/02-schemas-in-practice/2.4-the-schema-is-the-prompt-again.md) | 522 characters on every turn, and the wrong way to shrink it | `working` |

### Section 3 — `03-schema-and-tools-together`: the path Sutra is actually on

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [The rule that changed](parts/03-schema-and-tools-together/3.1-the-rule-that-changed.md) | A rule everybody knows, still on the docs, no longer true | `working` |
| 3.2 | [The tool ADK injects](parts/03-schema-and-tools-together/3.2-the-tool-adk-injects.md) | A tool you did not write and an instruction you did not write | `working` |
| 3.3 | [What that costs you](parts/03-schema-and-tools-together/3.3-what-that-costs-you.md) | The bill, itemised — and what it is cheaper than | `production` |

### Section 4 — `04-when-a-schema-lies`: what it cannot check

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [Valid is not true](parts/04-when-a-schema-lies/4.1-valid-is-not-true.md) | Five triages, four valid, one right | `production` |
| 4.2 | [The field that was always filled](parts/04-when-a-schema-lies/4.2-the-field-that-was-always-filled.md) | What `required` actually instructs, and the one-character fix | `production` |

### Section 5 — `05-failure-lab`: the deliberate failure

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [💥 The schema that silenced the agent](parts/05-failure-lab/5.1-the-schema-that-silenced-the-agent.md) | Four honest answers, all rejected, and spam filed as billing | `production` |

### Section 6 — `06-in-the-graph`: the hand-off, and the tests

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 6.1 | [`output_key` is how agents talk](parts/06-in-the-graph/6.1-output-key-is-how-agents-talk.md) | Three pieces you already have, assembled into Phase 8's wiring | `production` |
| 6.2 | [Testing structured output for free](parts/06-in-the-graph/6.2-testing-structured-output-for-free.md) | Four assertions with no key, and the fifth question you cannot ask | `production` |

### The paper — read after the parts

| Paper | What it settles | Level |
| --- | --- | --- |
| [01 — Efficient Guided Generation for Large Language Models](papers/01-guided-generation.md) | Why "the provider guarantees the shape" is affordable at all — an FSM and one index | `production` |

---

## §3 Setup — run this

**No new packages today.** `google-adk` 2.7.1 and the Pydantic it already depends on carry the whole
day.

```bash
# 1 - confirm where you are starting from
./m check

# 2 - the lab scratchpad for today
mkdir -p days/day-12-structured-output/lab
cd days/day-12-structured-output/lab
touch shape.py address.py accepts.py as_a_tool.py
touch fillable.py optional.py dropped.py the_prompt_again.py
touch capability.py the_cost.py the_bill.py
touch valid_not_true.py always_filled.py
touch silenced.py
touch handoff.py testing.py
cd -

# 3 - the paper's demo is GIVEN, not an exercise. It is already on disk:
ls days/day-12-structured-output/lab/papers/guided-generation/

# 4 - what changes under sutra/ today
cat sutra/desk/agent.py     # gains two fields
cat sutra/desk/tools.py     # unchanged today
```

**Run `lab/shape.py` before you read anything else.** Two lines of output, and they are the whole of
section 1.

**Then run `lab/capability.py` early**, before you form a mental model of how this works. It prints
`False`, and everything in section 3 follows from that one boolean.

**Two files under `sutra/` change today** — a new `sutra/desk/schemas.py`, and two fields added to
`sutra/desk/agent.py`. `sutra/desk/tools.py` is **unchanged**: today is about the answer, not the tools.

---

## §4 Build brief

**`sutra/desk/schemas.py`** — new, and the day's centrepiece:

| Symbol | What it is | Taught in |
| --- | --- | --- |
| `Triage` | one required `outcome` discriminator; `category`, `urgency`, `summary` all optional | 5.1, 4.2, 2.2 |
| `outcome: Literal["triaged", "unclear", "not_a_ticket"]` | the field that lets the desk decline | 5.1 |
| `category: Literal[...] \| None` | closed set, nullable, no `"other"` | 2.1, 5.1 |
| `urgency: Literal[1,2,3,4,5] \| None` | the range in the **type**, because `ge`/`le` does not reach the model on Sutra's path | 2.3 |

**`sutra/desk/agent.py`** — two new fields: `output_schema=Triage` and `output_key="triage"`. Nothing
else.

**`days/day-12-structured-output/lab/`** — sixteen scripts. **All sixteen cost zero requests.**

**`days/day-12-structured-output/lab/papers/guided-generation/`** — **already written for you.** The
paper's demo is teaching material, not an exercise; read it, run it, and run the ablation.

**`tests/test_schema.py`** — see §5.

**`TODO(me)` markers left for you:**

- **§1 and 4.2** — write out the `required` list of your `Triage` and justify each field on it, out
  loud. If you cannot say why a field always has an answer, take it off the list.
- **5.1** — decide whether `outcome` has three values or more. `"unclear"` and `"not_a_ticket"` need
  different handling downstream; a `"spam"` value might too. Write down the downstream action for each.
- **2.3** — decide where `urgency`'s 1–5 range lives: in a `Literal`, in the field name, or in the
  agent's instruction. Pick one and say why the other two are worse.
- **3.1** — run `capability.py` on **your** machine and record the resolved variant. If it is not
  `GEMINI_API`, your `.env` differs from this document's assumption and section 3 reads differently for
  you.
- **The persona problem.** Day 6's handbook has a voice, a tone and a refusal policy. With
  `output_schema` set, most of that now applies to **one field** — `summary`. Re-read
  `sutra/desk/agent.py`'s instruction and decide what is still doing work, what is now dead text, and
  what has to move. This is
  [Day 10, part 5.2](../day-10-function-tools/parts/05-wiring-sutra/5.2-the-first-aid-box-with-bandages.md)
  happening again for a new reason, and it is the most interesting decision of the day.
- **6.1** — Sutra has no second agent yet, so nothing reads `state["triage"]`. Write down what the first
  consumer will be and what it will need, before Phase 8 decides for you.
- **3.3** — decide whether Sutra's structured output is worth moving to a LiteLLM lane for the native
  path. It is a real, zero-budget option and it is a different model. Record the decision either way.

---

## §5 The eval that must be able to fail

One new file, four assertions, **no API key required**. These run on a fresh clone with no `.env`.

```python
# tests/test_schema.py
import json

from google.adk.tools.set_model_response_tool import SetModelResponseTool
from google.adk.utils._schema_utils import validate_schema
from pydantic import ValidationError

from sutra.desk.schemas import Triage

GOLDEN = [
    ('{"outcome": "not_a_ticket"}', {"outcome": "not_a_ticket"}),
    (
        '```json\n{"outcome": "triaged", "category": "billing", "urgency": 4, '
        '"summary": "Charged twice."}\n```',
        {
            "outcome": "triaged",
            "category": "billing",
            "urgency": 4,
            "summary": "Charged twice.",
        },
    ),
]


def test_the_schema_can_decline() -> None:
    """5.1: with no refusal value, every input gets a confident answer."""
    outcomes = Triage.model_fields["outcome"].annotation.__args__
    assert len(outcomes) > 1, "outcome must offer something other than success"


def test_only_the_outcome_is_required() -> None:
    """4.2: a required field is an instruction to always have an answer."""
    declared = SetModelResponseTool(Triage)._get_declaration().parameters_json_schema
    assert declared["required"] == ["outcome"]


def test_golden_replies_parse_to_the_expected_value() -> None:
    """1.2: fences are stripped and null fields are dropped."""
    for said, expected in GOLDEN:
        assert validate_schema(Triage, said) == expected


def test_bad_replies_are_rejected() -> None:
    """4.1: the schema catches shape. Only shape."""
    for said in ('{"outcome": "maybe"}', '{"outcome": "triaged", "urgency": 9}', "not json"):
        try:
            validate_schema(Triage, said)
        except (ValidationError, ValueError, json.JSONDecodeError):
            continue
        raise AssertionError(f"schema accepted {said!r}")


# TODO(me): the fifth test - is the triage CORRECT? It cannot live here. See Day 25.
```

**How to watch each one go RED before it goes green:**

```bash
uv run python -m pytest tests/test_schema.py -q -m "not live"   # RED: sutra/desk/schemas.py is empty
# ... write the module from §4 ...
uv run python -m pytest tests/test_schema.py -q -m "not live"   # green
```

Then break each one on purpose:

- Reduce `outcome` to `Literal["triaged"]` and watch the first go red. Read its message: it is the only
  assertion in the suite that is about whether the agent can be honest.
- Make `summary` required and watch the second go red. That is
  [4.2](parts/04-when-a-schema-lies/4.2-the-field-that-was-always-filled.md) as a gate.
- Rename `summary` to `text` and watch the third go red — a schema change is a contract change for
  everything downstream.
- Change `urgency` from `Literal[1,2,3,4,5]` to `int` and watch the fourth go **green when it should not
  be**: `9` is now a valid integer. Put it back, and notice that the test only caught it because the
  constraint was in the *type*.

**And one thing to leave undone deliberately.** The fifth test — *is the triage correct?* — cannot be
written here. Four of the five candidates in
[4.1](parts/04-when-a-schema-lies/4.1-valid-is-not-true.md) pass every assertion above. That is Day 25,
and leaving a `TODO(me)` where a lie would fit is the point.

---

## §6 Request budget

**Free-tier Gemini**, 20 requests per day (`docs/PACKAGES.md`, 2026-08-25).

| What | Model calls |
| --- | --- |
| all sixteen lab scripts, all six sections | **0** |
| the paper's demo and its ablation | **0** |
| the whole test suite | **0** |
| **Total required** | **0 of 20** |

Two days in a row at zero, for the same reason: a schema is a class, a request is an object, and both
can be assembled and inspected without sending anything.

**Optional, and worth it if you have quota:** run one real triage with the new agent and watch the
trace. On Sutra's path you will see a `set_model_response` function call go past that nothing in your
code created ([3.2](parts/03-schema-and-tools-together/3.2-the-tool-adk-injects.md)). Two or three
requests, and it is the only thing today that a real run shows you and a script cannot.

**Cost: $0.**

---

## §7 Traps

- **`output_schema` sets two fields on the request** — `response_mime_type="application/json"` and
  `response_schema` — and only when the agent has no tools, or the model can take both. (1.1, 3.1)
- **`response_schema` on `generate_content_config` raises.** ADK's validator: *"Response schema must be
  set via LlmAgent.output_schema."* (1.1)
- **`output_key` writes through `event.actions.state_delta`** — the same object a tool writes to. There
  is no second state mechanism. (1.2)
- **With a schema, what lands in state is a parsed `dict`**, code fence stripped and every `None` field
  **dropped**. `state["triage"]["order_id"]` is a `KeyError`, not a `None`. (1.2, 2.2)
- **`output_schema` turns off streaming text accumulation for `output_key`** — you cannot accumulate half
  a JSON document. (1.2)
- **Five schema shapes are accepted**, and a raw `dict` schema is **not validated at all** —
  `validate_schema` falls through to `json.loads`. (1.3)
- **`input_schema` does nothing unless the agent is used as a tool** by another agent. (1.4)
- **The database-shaped schema is the *larger* declaration.** Nesting costs characters and buys no
  constraint. (2.1)
- **A default that is not `None` survives `exclude_none`; a default of `None` never does.** Two optional
  fields, two different fates. (2.2)
- **`Field(description=...)`, `ge` and `le` do not reach the model on the tools path.** Only name, type
  and default survive, because the declaration is rebuilt from `inspect.Parameter` objects. `Literal`
  survives, because the enum is part of the type. (2.3)
- **A dropped bound becomes a retry**, not a missing constraint — Pydantic rejects and the model is asked
  to call again, at the cost of a model call. (2.3, 3.3)
- **The schema is prompt text, sent every turn** — 522 characters for three readable fields. The lever is
  field count, never shorter names. (2.4)
- **"`output_schema` means no tools" is a 1.x rule** and is still on adk.dev. ADK 2.x supports both; a
  model capability decides how. (3.1)
- **That capability is `True` only on Vertex AI** for Gemini, and Sutra is on the Gemini API — so Sutra
  is permanently on the workaround path, by a Day 5 decision. `LiteLlm` declares `True`. (3.1)
- **On the workaround path ADK injects a tool called `set_model_response`** and appends 297 characters of
  instruction you did not write. Enforcement is a **prompt**. (3.2)
- **The happy path costs no extra model call** — the final event is built from the function response
  directly. Only a rejection costs one. (3.3)
- **Callbacks and traces will show a tool call nobody on your team wrote.** Any code that indexes tools
  by name meets `set_model_response`. (3.2)
- **A schema checks shape and not meaning.** For one ticket, four of five candidate triages validate and
  one is right — and the one it rejects is an integer out of range. (4.1)
- **`required` instructs the model to always have an answer**, so a required field for a fact the input
  may lack is a fabrication machine. (4.2)
- **Making a field nullable is a breaking change for its readers**, because `exclude_none` drops it. (4.2)
- **A schema with no way to decline forces a confident answer to spam.** All four honest replies are
  invalid; the only accepted answer is a triage. (5.1)
- **Adding `"other"` to a category enum is the wrong fix** — it collects uncertainty, not impossibility.
  Add a discriminator instead. (5.1)
- **The instruction template inserts Python's `repr`**, not JSON — single quotes. (6.1)
- **A consumer that does not branch on the discriminator writes a polite reply to spam.** (6.1)
- **A test asserting `validate_schema(...)` is truthy passes for wrong answers.** Compare to an expected
  value. (6.2)

---

## §8 Verify before you code

Every source below was checked on **2026-08-27** while this day was written. Principle 8: re-check on
the day you use them. This table is evidence, not a substitute.

| Source | What it settled |
| --- | --- |
| `adk.dev/agents/llm-agents/` | *"Using `output_schema` with `tools` in the same LLM request is only supported by specific models, including Gemini 3.0."* · the example comment *"NO tools parameter here - using output_schema prevents tool use"* · `output_key`: *"the text content of the agent's final response will be automatically saved to the session's state dictionary under this key"* · `input_schema`: *"the user message content passed to this agent must be a JSON string conforming to this schema"* |
| `arxiv.org/abs/2307.09702` | the paper's exact title, year and abstract, and the name of the reference implementation. Recorded in `docs/PAPERS.md` with today's date. |
| the installed `google-adk` 2.7.1 | the `output_schema` docstring's *"The ADK supports using `output_schema` and `tools` together"* · `basic.py`'s `if not agent.tools or model.capabilities.output_schema_and_tools` · `gemini_output_schema_and_tools` returning `VERTEX_AI and is_gemini_model(...)` · `LiteLlm.capabilities` returning `output_schema_and_tools=True` · `_output_schema_processor`'s appended instruction, verbatim · `SetModelResponseTool` rebuilding parameters from `inspect.Parameter(name, KEYWORD_ONLY, annotation, default)` · its validation-error text · `validate_schema`'s `_strip_json_code_fence` then `model_dump(exclude_none=True)` · `llm_agent.py`'s `event.actions.state_delta[self.output_key] = result` · `create_final_model_response_event` building the final event with no further model call |

**Eight claims in this day that no page states**, established by running code rather than by reading.
Re-run them; if your version disagrees, **your terminal wins** and you fix the document:

```bash
uv run python days/day-12-structured-output/lab/shape.py       # 1.1 - two fields, no tools
uv run python days/day-12-structured-output/lab/address.py     # 1.2 - the null field disappears
uv run python days/day-12-structured-output/lab/dropped.py     # 2.3 - descriptions and bounds gone
uv run python days/day-12-structured-output/lab/capability.py  # 3.1 - False, on the Gemini API
uv run python days/day-12-structured-output/lab/the_cost.py    # 3.2 - both paths, side by side
uv run python days/day-12-structured-output/lab/the_bill.py    # 3.3 - the itemised difference
uv run python days/day-12-structured-output/lab/valid_not_true.py  # 4.1 - four of five valid
uv run python days/day-12-structured-output/lab/silenced.py    # 5.1 - four honest answers rejected
```

The one to run twice is `capability.py`. Everything in section 3 is downstream of the boolean it prints,
and if your environment resolves to `VERTEX_AI` then half of this day describes a path you are not on.

---

## §9 Say it in an interview

> "Structured output is two fields and one surprise. The fields are an output schema — a Pydantic model
> on the agent — and an output key, which is where the answer lands in session state; together they turn
> an agent from something you converse with into a node that produces a typed value. On the simple path
> the framework puts a JSON mime type and a response schema on the request, and the provider constrains
> decoding, so non-conforming output can't be produced rather than being asked for. The surprise is what
> happens when the agent also has tools. Most model APIs won't take a response schema and a tool list in
> one request, so the framework injects a tool called `set_model_response` whose parameters are your
> schema's fields, appends an instruction saying the final answer must come through it, and validates
> the arguments with Pydantic. That's invisible from outside — the final event is fabricated to look
> like a normal answer — and it has genuinely different guarantees: enforcement is a sentence in a
> prompt, and field descriptions and numeric bounds don't survive into what the model is shown, so a
> bound becomes a retry loop instead of an instruction. So I'd always check which path a given agent is
> on, and log it. The two design rules I'd argue for regardless: `required` means 'this has an answer for
> every possible input', because a required field the input can't answer is an instruction to fabricate;
> and the schema needs a discriminator so the agent can say 'I can't do this' — without one, spam comes
> back as a confident, valid, stored triage with no error anywhere. And I'd be careful with the word
> validated: for one ticket I can write five outputs where four pass the schema and one is right."

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked — honestly. `./m done 12` refuses to commit while
any box is unticked, and it cannot tell whether you were truthful. That part is yours.

The day is finished when `sutra/desk/schemas.py` holds a `Triage` whose only required field is a
discriminator you can justify; when `urgency`'s range lives somewhere the model will actually see it;
when `sutra/desk/agent.py` sets `output_schema` and `output_key` and nothing else changed; when you have
run `capability.py` and written down which path your machine is on; when you have decided what happens
to Day 6's persona now that most of it applies to one field; when the four tests pass and you have
watched each of them go red for its own reason; when the fifth test is a `TODO(me)` rather than a lie;
when you have run the paper's demo **and** its ablation and can say what the index maps; and when
`sutra/desk/tools.py` is **unchanged**.

---

## §11 Ledger & commit

Paste these **with the values you actually observed** (Principle 7), not the ones printed here.

**`docs/PROGRESS.md`** — append one row:

```text
| 12 | <date> | ADK-13 | 16 | <hash> | ✅ |
```

**`docs/PACKAGES.md`** — **no new rows.** Nothing was installed today.

One thing is worth a row **if your machine disagrees with this document**: the resolved
`GoogleLLMVariant` and the `output_schema_and_tools` boolean that follows from it. That is a
behavioural fact about a pinned dependency in a particular environment, which is what that ledger is
for.

**`docs/PAPERS.md`** — one row, and it should already be there from when you looked the paper up:

```text
| Efficient Guided Generation for Large Language Models | arXiv:2307.09702 | 2023 | <date> | 12 | `days/day-12-structured-output/papers/01-guided-generation.md` |
```

Principle 7 pointed at the literature: the title is copied from the arXiv record, not from memory, and
the date is the day you looked.

**`docs/SKILL_PROVENANCE.md`** — no rows. First entries arrive on Day 29.

**`docs/adr/`** — no new ADR is required, and there are two decisions worth recording in the commit
message: what happened to Day 6's persona instruction, and whether Sutra stays on the Gemini lane
knowing it means the workaround path. **If your ADK version no longer injects `set_model_response`, or
now carries `Field` metadata into the synthesized declaration, stop and re-read Principle 14 before
editing anything** — both are behaviour changes in a pinned dependency, and the plan is amended first.

**Commit message:**

```text
day 12: structured output - a shape on the way out - closes ADK-13
```
