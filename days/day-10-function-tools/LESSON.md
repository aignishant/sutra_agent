---
day: 10
phase: 2
phase_name: "Models & tools"
title: "Function tools in ADK — the forms print themselves"
ids: ["ADK-10", "ADK-11"]
principles: [1, 2, 4, 6, 8, 9, 10, 11, 13, 15, 16, 17, 18]
kind: lab
plan_version: "v2.2.1"
parts: 16
generated: "2026-08-27"
status: written
lab_scaffolded: false
commit: ""
---

# Day 10 — Function tools in ADK: the forms print themselves

> **Yesterday (Day 9):** one agent, four free providers, and a benchmark table with dates on it. The
> model became a string you can swap, and a paper about choosing which one.
> **Today:** Sutra gets its hands back. The declarations you wrote by hand on Day 4 are generated from
> the functions you wrote on Day 3, the dispatch table disappears, and the handbook that promised a
> knowledge base on Day 6 finally has one.
> **Tomorrow (Day 11):** `ToolContext` — how a tool finds out *who is asking*, and reads and writes
> the session state it has been running beside all week.

---

## §1 Where we are

A shop that used to write bills by hand gets a billing machine.

Before: a pad of numbered slips and a pen. Item, rate, quantity, amount, total at the bottom, and the
arithmetic done in the margin. It works — millions of shops run like this — and it has a particular
kind of failure. Not the arithmetic; people who do it all day are fast and accurate. The failures are
the copying. A rate that changed last week and is still being written as the old one. A slip where
the item name is abbreviated so far that nobody can reconcile it at the end of the month. A total
that is right for the items listed and the items listed are missing one.

After: a scanner, and a printer. Item, rate, quantity and total all come off the same record, so
they cannot disagree with each other.

Ask the shopkeeper what changed and you will not get "we make fewer mistakes". You will get something
more precise: **a whole category of mistake stopped being possible**, because the two things that
used to be copied from each other are now one thing, printed twice.

And what did not change is everything that was ever a judgement. What to stock. What to charge. Which
customer gets credit. Whether to take the item back.

Days 3 and 4 were the pad and the pen, and they were worth doing — you cannot review a machine you
have never done by hand. Today the machine arrives. Four things you wrote disappear, and the two that
were always the real work stay: **the functions, and the words that describe them.**

There is one more thing today, and it is the point rather than a footnote. Since Day 5 Sutra's
instruction has promised a knowledge base. Since Day 6 you have known that was a bug, and the fix was
a sentence admitting the agent could not see anything. Today the knowledge base exists — and that
sentence becomes the lie. A handbook describes a machine, and when the machine changes the handbook is
wrong until somebody changes it too.

---

## §2 The map

Sixteen parts in seven sections, and no papers today. Day 4 already taught the paper this subject
comes from — *Toolformer* (`arXiv:2302.04761`), in
[day-04's papers](../day-04-tools-by-hand/papers/01-toolformer.md) — and §17.4.2 is explicit that a
paper is taught once in the curriculum and cited afterwards. Today's subject is the framework's own
surface, which is a tool rather than an idea with a citable origin.

The day climbs `foundation → working → production`: section 1 is where the declaration comes from,
section 2 is what a tool gives back, section 3 is what ADK took and what still needs a brake, section
4 is two tool shapes you will need later, section 5 wires Sutra, section 6 breaks it on purpose, and
section 7 says what none of it can do.

### Section 1 — `01-the-form-fills-itself`: ADK-10, the declaration is generated

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [The declaration you no longer write](parts/01-the-form-fills-itself/1.1-the-declaration-you-no-longer-write.md) | Four things ADK reads off a function — and what class of bug that deletes | `foundation` |
| 1.2 | [The docstring is the description](parts/01-the-form-fills-itself/1.2-the-docstring-is-the-description.md) | Where do your `Args:` lines actually end up? Not where you think | `working` |
| 1.3 | [Type hints are the schema](parts/01-the-form-fills-itself/1.3-type-hints-are-the-schema.md) | Annotated, defaulted, unannotated — three rows, and the third is a trap | `working` |
| 1.4 | [The wrapper that arrives late](parts/01-the-form-fills-itself/1.4-the-wrapper-that-arrives-late.md) | Yesterday's `canonical_model` shape, applied to tools | `working` |

### Section 2 — `02-what-a-tool-returns`: ADK-11, the result is prompt text

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [Return a dict with a status](parts/02-what-a-tool-returns/2.1-return-a-dict-with-a-status.md) | Why a boolean cannot carry the three outcomes you actually have | `working` |
| 2.2 | [The bare value the spec rewrites](parts/02-what-a-tool-returns/2.2-the-bare-value-the-spec-rewrites.md) | A key you never chose, and where the wrapping happens | `working` |
| 2.3 | [A failed tool is still a result](parts/02-what-a-tool-returns/2.3-a-failed-tool-is-still-a-result.md) | Three ways to not succeed, and the one that is always wrong | `production` |

### Section 3 — `03-the-dispatch-you-deleted`: the loop moved, the brake did not

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [What the courier took](parts/03-the-dispatch-you-deleted/3.1-what-the-courier-took.md) | Five things gone, four kept — and what the two lists have in common | `working` |
| 3.2 | [The loop you no longer write](parts/03-the-dispatch-you-deleted/3.2-the-loop-you-no-longer-write.md) | One user message is now several model calls. Count them | `working` |
| 3.3 | [The brakes still matter](parts/03-the-dispatch-you-deleted/3.3-the-brakes-still-matter.md) | Today Sutra can loop for the first time. The default of 500 is not a decision | `production` |

### Section 4 — `04-tool-shapes`: two shapes you will need later

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [🅿️ The tailor's receipt](parts/04-tool-shapes/4.1-the-tailors-receipt.md) | Work that outlives the turn — and the note ADK writes into your description | `production` |
| 4.2 | [🅿️ Are you sure?](parts/04-tool-shapes/4.2-are-you-sure.md) | A person between the decision and the action, on the tools that write | `production` |

### Section 5 — `05-wiring-sutra`: the desk gets its hands back

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [Two tools, ported](parts/05-wiring-sutra/5.1-two-tools-ported.md) | One thing genuinely changes in the port. Which? | `working` |
| 5.2 | [The first-aid box with bandages](parts/05-wiring-sutra/5.2-the-first-aid-box-with-bandages.md) | Day 6's fix is now the bug — and the test that enforced it expires silently | `production` |

### Section 6 — `06-failure-lab`: the deliberate failure

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 6.1 | [💥 The jar with no label](parts/06-failure-lab/6.1-the-jar-with-no-label.md) | One missing word, six layers, and a `TypeError` four files from the cause | `production` |

### Section 7 — `07-limits`: what none of it can do

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 7.1 | [What a schema still cannot say](parts/07-limits/7.1-what-a-schema-still-cannot-say.md) | Four questions, four mechanisms, and the one people reach for wrongly | `production` |

---

## §3 Setup — run this

**No new packages today.** Day 5's `google-adk` 2.7.1 and Day 9's `litellm` carry the whole day, and
nothing here installs anything.

```bash
# 1 - confirm where you are starting from
./m check

# 2 - the lab scratchpad for today
mkdir -p days/day-10-function-tools/lab
cd days/day-10-function-tools/lab
touch generated.py docstring.py docstring_flag.py hints.py late.py
touch returns.py wrapping.py failing_tools.py
touch seams.py watch_the_loop.py runaway.py
touch long_running.py confirmation.py
touch no_label.py what_a_schema_cannot_say.py
cd -

# 3 - the one new module under sutra/ and the one new test file
touch sutra/desk/tools.py
touch tests/test_tools.py

# 4 - what Day 4 wrote, still on disk. You decide its fate today (5.1).
cat sutra/tools.py
```

**Write `sutra/desk/tools.py` first** (part 5.1). Two of today's lab scripts import it and the whole
of section 5 depends on it. It is given complete in 5.1 and costs nothing to type.

**Run `lab/generated.py` before you read anything else.** Fourteen of today's sixteen lab scripts cost
zero requests, and the first one shows the day's whole idea in six lines of output.

**Three files under `sutra/` change today** — `desk/tools.py` is new, `desk/agent.py` gains
`tools=[...]` and a revised instruction and description, and `desk/run_once.py` gains a `RunConfig`.
Nothing else: `sutra/loop.py` and `sutra/agent.py` are **deliberately untouched**, because Principle 4
says the hand-rolled version stays as the comparison.

---

## §4 Build brief

**`sutra/desk/tools.py`** — new, and the day's centrepiece:

| Symbol | What it is | Taught in |
| --- | --- | --- |
| `TICKETS`, `KB` | Day 3's synthetic data, with tickets as records rather than strings | 5.1, 2.1 |
| `lookup_ticket(ticket_id)` | Day 3's function, Day 4's description as its docstring, a dict return | 5.1 |
| `search_kb(query)` | the same, with the *when not to use this* sentence in both directions | 5.1, 1.2 |

**`sutra/desk/agent.py`** — three changes: `tools=[lookup_ticket, search_kb]` (5.1), a `description`
that no longer says the agent cannot look anything up (5.1), and an honesty section that names what it
*can* see and what it still cannot (5.2).

**`sutra/desk/run_once.py`** — one new constant, `DESK_RUN_CONFIG = RunConfig(max_llm_calls=8)`, and
one new argument on `run_async` (3.3).

**`days/day-10-function-tools/lab/`** — sixteen scripts. **Fourteen cost zero requests.**

**`tests/test_tools.py`** and an edit to **`tests/test_persona.py`** — see §5.

**`TODO(me)` markers left for you:**

- **5.1** — decide what happens to `sutra/tools.py`, Day 4's hand-written declarations. Delete it, or
  keep it with a header saying it is a Day 4 artefact. Leaving it undecided is the one option that is
  wrong.
- **5.1** — `search_kb` returns the **first** matching article and there could be two. That is Day 3's
  behaviour, carried across knowingly. Write down whether it stays.
- **5.2** — re-run Day 6's three probes and write a verdict for each. The honesty probe had a correct
  answer yesterday that is wrong today; say what that means for an evalset you have not built.
- **5.2** — Day 6's `test_the_handbook_promises_no_equipment_the_agent_lacks` is now vacuous. Replace
  it with the version in 5.2, or delete it and say why in the commit message.
- **3.2** — count the model calls one triage costs you, and write the number down. Day 24's budget
  starts from it.
- **3.3** — decide Sutra's `max_llm_calls` from your own arithmetic rather than copying 8, and put the
  arithmetic in the comment.

---

## §5 The eval that must be able to fail

Two files. The new one is free; the edit to the old one is the more interesting half, because it is
about a test that **stopped testing without failing**.

```python
# tests/test_tools.py
import asyncio

from sutra.desk.agent import root_agent
from sutra.desk.tools import lookup_ticket, search_kb


def test_every_tool_parameter_has_a_type() -> None:
    """6.1: an untyped parameter reaches the model as {} and fails inside the tool."""

    async def check() -> list[str]:
        problems = []
        for tool in await root_agent.canonical_tools():
            schema = tool._get_declaration().parameters_json_schema or {}
            for name, spec in schema.get("properties", {}).items():
                if "type" not in spec:
                    problems.append(f"{tool.name}({name})")
        return problems

    assert asyncio.run(check()) == []


def test_the_tools_are_registered_by_name() -> None:
    """1.1: the function's name is the tool's name - so a rename is a contract change."""
    names = {t.name for t in asyncio.run(root_agent.canonical_tools())}
    assert names == {"lookup_ticket", "search_kb"}


def test_a_miss_says_what_it_missed_on() -> None:
    """2.1: the input echoed back is what turns 'nothing found' into a usable sentence."""
    assert lookup_ticket("9999") == {"status": "not_found", "ticket_id": "9999"}
    assert search_kb("nothing like this")["query"] == "nothing like this"


def test_every_return_carries_a_status() -> None:
    """2.1, 2.3: one vocabulary, so the handbook can say one thing about failure."""
    for result in (
        lookup_ticket("4521"),
        lookup_ticket("9999"),
        search_kb("keeps getting logged out"),
        search_kb("nothing like this"),
    ):
        assert result["status"] in {"ok", "not_found", "error"}


def test_no_tool_returns_a_bare_value() -> None:
    """2.2: a non-dict return arrives at the model under a key you did not choose."""
    for result in (lookup_ticket("4521"), search_kb("keeps getting logged out")):
        assert isinstance(result, dict)


# TODO(me): the sixth test - assert the handbook claims only capabilities that exist (5.2).
```

**How to watch each one go RED before it goes green:**

```bash
uv run python -m pytest tests/test_tools.py -q -m "not live"   # RED: sutra/desk/tools.py is empty
# ... write the module from part 5.1 ...
uv run python -m pytest tests/test_tools.py -q -m "not live"   # green
```

Then break each one on purpose:

- Remove `: str` from `lookup_ticket`'s parameter and watch the first test go red naming the tool and
  the parameter. That is 6.1, as an assertion.
- Rename `search_kb` to `kb_search` and watch the second go red — then read it again and notice that
  **renaming a function is a change to what the model is offered**, which is why the test exists.
- Change the `not_found` return to `{"status": "not_found"}` without the id, and watch the third go
  red. That single key is 2.1's whole argument.
- Return a bare string from `search_kb` and watch the fifth go red. Then look at what
  [2.2](parts/02-what-a-tool-returns/2.2-the-bare-value-the-spec-rewrites.md) says the model would
  have received.

And the edit to `tests/test_persona.py`, which is the day's real lesson about tests:

```bash
uv run python -m pytest tests/test_persona.py -q -m "not live"
```

It is **green**, and one of its tests no longer runs — `if not root_agent.tools:` is now `False`.
Part [5.2](parts/05-wiring-sutra/5.2-the-first-aid-box-with-bandages.md) gives the replacement.
**A test that silently stops testing is worse than one that fails**, and today is the day to notice
one.

---

## §6 Request budget

**Free-tier Gemini**, 20 requests per day (`docs/PACKAGES.md`, 2026-08-25). Today is cheap, and the
cheapness has a cause: a tool is a Python function, and a declaration is generated from it, so almost
everything can be inspected without a model.

| What | Model calls |
| --- | --- |
| all of section 1 · all of section 2 · 3.1 · all of section 4 · 5.1 · 6.1 · 7.1 | **0** |
| 3.2 — `watch_the_loop.py`, one triage with two tools | 2–3 |
| 3.3 — `runaway.py`, capped at 3 by `max_llm_calls` | up to 3 |
| 5.2 — Day 6's three probes, re-run against the new handbook | 3 |
| **Total** | **8–9 of 20** |

**Notice what 3.2 costs.** One user message, two or three model calls — which is the day's most
important operational fact and is *why* it appears in this table rather than being asserted in prose.
Yesterday a triage cost one request. Today it costs three, and nothing in the diff says so.

**Do the free things first.** Fourteen of the sixteen lab scripts need no key, including the whole
failure lab and both of section 4. If quota is tight, everything except section 3.2, 3.3 and 5.2's
probes works on a plane.

**Cost: $0.**

---

## §7 Traps

- **`tools=[lookup_ticket()]` — with parentheses.** Calls your function at construction and puts the
  return value in the list. Pydantic catches it with **three** errors, and the three names are the
  whole menu of what `tools` accepts: a callable, a `BaseTool`, or a `BaseToolset`. (1.1)
- **The whole docstring becomes the description**, `Args:` and `Returns:` included — 474 characters
  for a well-written tool, sent on every turn whether or not the tool is called. Implementation notes
  and TODOs in a tool docstring go to the model. (1.2)
- **Parameter descriptions do not become schema fields.** On `google-adk` 2.7.1, neither code path
  puts a `description` on a parameter — your `Args:` lines are read as prose inside the tool
  description. Write them to be read that way. (1.2)
- **An unannotated parameter becomes `{}`** — required, named, no type. The model guesses from the
  parameter's name, usually correctly, until it does not. (1.3, 6.1)
- **`*args` and `**kwargs` are ignored entirely** by ADK and invisible to the model. (1.3)
- **A default answers a question on the model's behalf.** ADK's own docs: *"Do not add defaults for
  information the model should derive from the user request."* (1.3)
- **`agent.tools` holds plain functions**; the `FunctionTool` is built by `canonical_tools()`, which
  is `async`. A broken signature survives import, unit tests and `./m check` — the same late
  derivation as Day 9's `canonical_model`. (1.4)
- **A non-dict return is wrapped as `{"result": ...}`** on its way into the conversation, because the
  function-response format requires an object. A dictionary is passed through untouched, keys and all.
  (2.2)
- **A tool returning `None` gives the model `{"result": null}`** — which cannot say whether the action
  succeeded, so the model invents. The fabrication is caused by the tool. (2.2)
- **Catching an exception and returning an apology string** produces a *successful* tool call: green
  trace, green dashboard, and the only record of the failure is prose nothing parses. (2.3)
- **`not_found` is not an error.** Give it its own status, or your error rate counts every mistyped
  ticket number. (2.3)
- **One user message is now several model calls.** A quota budgeted per turn is wrong the day you add
  a tool. (3.2)
- **A display loop that does not filter on `is_final_response()`** shows the user the model's internal
  function calls. Day 7 warned about this; today is the first day it can happen. (3.2)
- **`max_llm_calls` defaults to 500**, which on a twenty-a-day tier means the provider stops you first
  and you lose the whole day instead of the run. Set it just above your real workload. (3.3)
- **`RunConfig` goes on the call, not the runner.** `runner.max_llm_calls = 8` attaches an attribute
  nothing reads. (3.3)
- **`LongRunningFunctionTool` appends a note to your description** telling the model not to call again
  after a pending status — which is a **prompt**, not a lock. (4.1)
- **A confirmation gate on every tool is a gate people click through.** The callable form of
  `require_confirmation` receives the tool's arguments; use it. (4.2)
- **The handbook now denies a capability the agent has.** Day 6's honesty section is false as of
  today, and an agent told it cannot look things up will not. (5.2)
- **Day 6's guard test is now vacuous** — `if not root_agent.tools:` is `False`. It still passes and
  its body never runs. (5.2)
- **A schema constrains shape and nothing else**, and ADK does **not** coerce scalar arguments — an
  `int` parameter handed a string raises inside your function exactly as an unannotated one does. The
  annotation changes what the model sends, not what your function receives. (6.1, 7.1)

---

## §8 Verify before you code

Every source below was checked on **2026-08-27** while this day was written. Principle 8: re-check on
the day you use them. This table is evidence, not a substitute.

| Source | What it settled |
| --- | --- |
| `adk.dev/tools-custom/function-tools/` | that a function in `tools` is wrapped automatically; that the docstring becomes the description and the type hints and defaults the schema; that a **dict with a `status` key** is the preferred return and a non-dict is wrapped under `"result"`; that `*args`/`**kwargs` are *"ignored by the ADK framework"*; and the warning *"Use defaults only for values that are truly optional. Do not add defaults for information the model should derive from the user request."* |
| `adk.dev/context/` | that a `ToolContext` parameter is **excluded from the schema shown to the model**; `state`, `actions`, `function_call_id`, the artifact methods and `search_memory` — read today, taught tomorrow |
| the installed `google-adk` 2.7.1 | `FunctionTool.__init__(func, *, require_confirmation=...)` · `LongRunningFunctionTool(FunctionTool)` and the `NOTE:` it appends verbatim · that `agent.tools` holds the raw callables and `canonical_tools()` wraps them · that the generated declaration carries `parameters_json_schema` (feature `JSON_SCHEMA_FOR_FUNC_DECL`, **EXPERIMENTAL, default on**) and **no per-parameter `description`** on either code path · that `_build_function_response_content` wraps a non-dict result with the comment *"Specs requires the result to be a dict."* · that `_prepare_invocation_args` converts **Pydantic-model** parameters only, so scalars are **not** coerced |

**Five claims in this day that no page states**, established by running code rather than by reading.
Re-run them; if your version disagrees, **your terminal wins** and you fix the document:

```bash
uv run python days/day-10-function-tools/lab/docstring.py     # 1.2 - zero per-parameter descriptions
uv run python days/day-10-function-tools/lab/hints.py         # 1.3 - an unannotated parameter is {}
uv run python days/day-10-function-tools/lab/late.py          # 1.4 - construction validates nothing
uv run python days/day-10-function-tools/lab/wrapping.py      # 2.2 - both sides of the {"result": ...} wrap
uv run python days/day-10-function-tools/lab/no_label.py      # 6.1 - the annotated version raises too
```

The last one is the one to run twice. It contradicts a reasonable assumption — that a type hint
protects your function — and the correction is more useful than the assumption was.

---

## §9 Say it in an interview

> "The thing I'd want to convey about tool calling in a modern framework is how little of it is
> magic. You write a Python function; the framework reads its name, its docstring and its type hints
> and generates the JSON declaration the model sees. That's the whole trick, and the reason it matters
> isn't convenience — it's that there's now one artefact instead of two, so the declaration can't
> drift from the implementation the way a hand-written one does. I know the split because I wrote the
> hand-rolled version first: the declarations, the dispatch table, the response part and the loop all
> went to the framework, and what stayed was the function, its description and what it returns when it
> fails. Three things I'd want a team to get right. Return a dict with a status rather than a string,
> because *found*, *not found* and *the lookup broke* are three outcomes and a boolean only holds two
> — and because a bare value gets wrapped under a key you didn't choose. Never catch an exception and
> return an apology: the runtime counts that as a successful tool call, so the trace is green, the
> eval scores it as a response, and the only record of the failure is prose nothing parses. And
> annotate every parameter, but know exactly what that buys — it constrains what the model sends, and
> the framework doesn't coerce scalars, so if a wrong type arrives anyway your function gets it. A
> schema is a request the model was asked to honour, not something the runtime enforces, which is also
> why a schema-perfect tool call is exactly what prompt injection produces."

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked — honestly. `./m done 10` refuses to commit while
any box is unticked, and it cannot tell whether you were truthful. That part is yours.

The day is finished when `sutra/desk/tools.py` holds two functions whose docstrings you would be happy
for a model to read; when every parameter has a type and a test asserts it; when every return carries
a status and a miss carries its input; when `sutra/desk/agent.py` registers both tools, advertises
them in its `description`, and no longer claims it cannot look anything up; when you have watched a
single question produce two tool calls and three model calls, and written that number down; when
`max_llm_calls` is a number you chose with the arithmetic beside it; when you have made a parameter
untyped on purpose and watched the test go red; when you have decided what happens to `sutra/tools.py`
and to Day 6's expired test; when Day 6's three probes have been re-run and given verdicts; and when
`sutra/loop.py` and `sutra/agent.py` are **unchanged**.

---

## §11 Ledger & commit

Paste these **with the values you actually observed** (Principle 7), not the ones printed here.

**`docs/PROGRESS.md`** — append one row:

```text
| 10 | <date> | ADK-10, ADK-11 | 16 | <hash> | ✅ |
```

**`docs/PACKAGES.md`** — **no new rows.** Nothing was installed today.

There is one thing worth a row if you observe it differently: `JSON_SCHEMA_FOR_FUNC_DECL` is an
**experimental** feature that is **on by default** in 2.7.1, and it decides whether a tool declaration
carries `parameters` or `parameters_json_schema`. That is a dated behavioural observation rather than
a version pin, so it belongs in your lab notes — unless your version disagrees with this document, in
which case it is a `PACKAGES.md` row, because a behaviour change in a pinned dependency is exactly
what that ledger is for.

**`docs/PAPERS.md`** — no rows. *Toolformer* (`arXiv:2302.04761`) is this subject's paper and Day 4
already taught it; §17.4.2 says a paper is taught once and cited afterwards.

**`docs/SKILL_PROVENANCE.md`** — no rows. First entries arrive on Day 29.

**`docs/adr/`** — no new ADR, and one decision worth recording in the commit message instead: what you
did with `sutra/tools.py`. **If your ADK version has changed what an unannotated parameter generates,
or has started coercing scalar arguments, stop and re-read Principle 14 before editing anything** —
both are behaviour changes in a pinned dependency, and the plan is amended first.

**Commit message:**

```text
day 10: function tools in ADK - the forms print themselves - closes ADK-10, ADK-11
```
