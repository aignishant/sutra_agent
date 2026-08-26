---
day: 4
phase: 1
phase_name: "Foundations"
title: "Tools by hand — schemas, the call, the result turn"
ids: ["AG-04"]
principles: [1, 2, 4, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18]
kind: lab
plan_version: "v2.2.1"
parts: 16
generated: "2026-08-25"
status: written
lab_scaffolded: false
commit: ""
---

# Day 4 — Tools by hand: schemas, the call, the result turn

> **Yesterday (Day 3):** you hand-rolled the loop — a protocol made of a paragraph and a
> `startswith`, a dispatch table that was the whole security boundary, a brake, and a deliberate
> failure. You finished by writing down nine things a line of text cannot express.
> **Today:** six of those nine get fixed. The model's tool request stops being text and becomes a
> typed call with named, validated arguments; your parser is deleted; and the tool's result goes back
> through a channel of its own. Then you find out precisely what a schema does *not* buy you.
> **Tomorrow (Day 5):** the loop itself goes to a framework — and you will evaluate it against a list
> of seams you wrote yourself.

---

## §1 Where we are

Yesterday you built a form and asked people to fill it in correctly.

That is not a metaphor for something technical — it is genuinely what a text protocol is. You wrote
out a shape, you handed it over with the request, and you hoped. Most of the time it came back right.
When it did not, you found out at the far end: after the reply had been produced, after you had paid
for it, at the point where your own code tried to make sense of a sentence somebody else had written.

Now imagine the same form online, where the date box refuses letters and the Submit button stays grey
until the required fields are filled. The rules did not change. Nobody got stricter. What moved is
*where the rules live* — out of the reader's head and into the form itself — so they are applied at
the moment of writing rather than at the moment of reading.

That is today. And there is a second thing that comes with it, which is easier to miss and matters
more: the request to *do something* stops travelling in the same channel as the documents your tools
return. Yesterday a command and a knowledge-base article were both text in one list, told apart by a
prefix you invented that morning. Today they are different kinds of thing.

The day ends by being precise about what none of that fixed.

---

## §2 The map

Sixteen parts in seven sections, then one paper. The day climbs `foundation → working →
production`, spends two whole sections on the limits of what it just built, ends with a deliberate
failure and a parked shortcut — and only then shows you the paper whose premise you implemented and
whose method you did not.

### Section 1 — `01-the-schema`: rules a machine can read

What a schema is, how a tool is described, and which field the model actually reads.

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [The form that rejects itself](parts/01-the-schema/1.1-the-form-that-rejects-itself.md) | What is a schema, and who does the rejecting? | `foundation` |
| 1.2 | [Declaring a tool](parts/01-the-schema/1.2-declaring-a-tool.md) | Which six keys replace yesterday's hand-typed menu? | `working` |
| 1.3 | [The description is the prompt](parts/01-the-schema/1.3-the-description-is-the-prompt.md) | Three fields fail loudly and one fails silently — which, and why? | `working` |

### Section 2 — `02-the-round-trip`: the exchange, end to end

Where the request lives now, what comes back, what you send in reply, and what must be copied verbatim.

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [Two channels, not one](parts/02-the-round-trip/2.1-two-channels-not-one.md) | What did separating commands from data actually prevent — and what did it leave untouched? | `foundation` |
| 2.2 | [The call comes back parsed](parts/02-the-round-trip/2.2-the-call-comes-back-parsed.md) | What replaces yesterday's parser, and what new coupling does it create? | `working` |
| 2.3 | [The tool-result turn](parts/02-the-round-trip/2.3-the-tool-result-turn.md) | Why does a result carry the id of the call it answers? | `working` |
| 2.4 | [Re-send the steps as received](parts/02-the-round-trip/2.4-resend-the-steps-as-received.md) | Why is the model's own turn copied rather than rebuilt? | `working` |

### Section 3 — `03-rebuilding-the-loop`: the same agent, a new protocol

Assembly, and the diff that tells you which half of yesterday was scaffolding.

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [One door, one new parameter](parts/03-rebuilding-the-loop/3.1-one-door-one-new-parameter.md) | Why does `tools` go through `ask` rather than around it? | `working` |
| 3.2 | [The loop that shrank](parts/03-rebuilding-the-loop/3.2-the-loop-that-shrank.md) | What got deleted, and what survived untouched? | `working` |
| 3.3 | [Two calls in one turn](parts/03-rebuilding-the-loop/3.3-two-calls-in-one-turn.md) | The model asked for two tools at once — now what? | `working` |

### Section 4 — `04-the-limits`: what a schema does not buy

The two failures that survive validation entirely.

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [Validated is not correct](parts/04-the-limits/4.1-validated-is-not-correct.md) | An argument passes every check and means the wrong thing — which metric sees it? | `production` |
| 4.2 | [The tool that is never called](parts/04-the-limits/4.2-the-tool-that-is-never-called.md) | Why is forcing a call the *last* thing you try? | `production` |

### Section 5 — `05-containment`: blast radius, updated

Yesterday there was one list. Today there are two, and a third layer that does not exist yet.

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [The declaration is the new boundary](parts/05-containment/5.1-the-declaration-is-the-new-boundary.md) | Two lists in two files — which direction of drift is dangerous? | `production` |
| 5.2 | [The argument a schema cannot check](parts/05-containment/5.2-the-argument-a-schema-cannot-check.md) | Whose ticket is it, and why can no schema ever answer that? | `production` |

### Section 6 — `06-failure-lab`: the deliberate failure

Today's failure, staged on purpose (plan §17.7).

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 6.1 | [💥 The call id you did not echo](parts/06-failure-lab/6.1-the-call-id-you-did-not-echo.md) | Two perfect results, two wrong questions — why does it look like model flakiness? | `production` |

### Section 7 — `07-the-automatic-door`: 🅿️ parked, for reading not building

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 7.1 | [🅿️ Automatic function calling, declined](parts/07-the-automatic-door/7.1-automatic-function-calling-declined.md) | The SDK will run the whole loop — so why not let it, and how is that different from tomorrow? | `production` |

### The paper — read after the parts

*"The model decides when to call a tool" is not this project's idea. It lives in this day's
`papers/` directory rather than in `parts/`, because where an idea came from is a different errand
from what the day teaches — and this one is the curriculum's clearest case of a paper whose premise
won completely and whose method was abandoned.*

| Paper | What it answers | Level |
| --- | --- | --- |
| [*Toolformer: Language Models Can Teach Themselves to Use Tools*](papers/01-toolformer.md) | How does the model know *when* to reach for a tool — and why is your only lever a description? | `production` |

---

## §3 Setup — run this

**Nothing is installed today.** `google-genai` arrived on Day 2 and is all today needs; function
calling is a feature of the API you already have, not a package. Verify that and create the day's
three files:

```bash
# 1 - confirm Day 3 actually landed. Today imports from it.
uv run python -c "from sutra.loop import TOOLS, _cost_table, _user_turn; print('day 3 ok:', sorted(TOOLS))"

# 2 - re-read the version you are building against (Principle 7)
uv pip show google-genai | head -3

# 3 - today's three files
touch sutra/tools.py sutra/agent.py tests/test_agent.py

# 4 - a scratchpad
mkdir -p days/day-04-tools-by-hand/lab

# 5 - the gate, before you write anything
./m check
```

If step 1 raises `ModuleNotFoundError` or a missing name, **finish Day 3 first.** Today's
`sutra/agent.py` imports `TOOLS`, `_cost_table` and `_user_turn` from it, and — deliberately —
`sutra/loop.py` is not edited at all today.

`pyproject.toml` and `uv.lock` do not change. If they do, something was installed that this day did
not ask for.

---

## §4 Build brief

Two new modules and one new test file. `sutra/loop.py` is **left alone** — Day 3's text protocol stays
in the repository as the fallback lane (Day 9) and as the comparison this day exists to make.

**`sutra/tools.py`** — declarations only. No functions, no imports from the SDK:

| Symbol | What it does | Taught in |
| --- | --- | --- |
| `LOOKUP_TICKET` | the declaration for `lookup_ticket` | 1.2 |
| `SEARCH_KB` | the declaration for `search_kb` | 1.2, 1.3 |
| `DECLARATIONS` | the list sent on every call | 1.2 |

**`sutra/agent.py`** — the loop over native function calling:

| Symbol | What it does | Taught in |
| --- | --- | --- |
| `SYSTEM` | role, sequencing, honesty — and nothing about format | 3.2 |
| `_result_turn(call, output)` | the `function_result` turn, carrying `call_id` | 2.3 |
| `_dispatch(call)` | step → tool call, via `TOOLS`; misses return text | 2.2 |
| `run_loop(client, question, *, max_steps=6)` | think → act → observe, bounded | 3.2, 3.3 |
| `main()` | dispatch from `sys.argv`; exit non-zero on bad usage | 3.2 |

**`sutra/mechanics.py`** — one change only: `ask` gains a keyword-only `tools` parameter defaulting to
`None` (3.1). Every Day 2 caller is untouched.

**`TODO(me)` markers left for you:**

- **1.2** — write the `search_kb` declaration yourself from the shape of `LOOKUP_TICKET`, and decide
  for yourself whether `query` gets an `enum`. Part 1.2 argues one way; make sure you can say why.
- **§5** — the eighth test, described below.
- **6.1** — restore the deliberately broken pairing when the failure lab is done.

---

## §5 The eval that must be able to fail

Seven tests, all offline, all free. The two structural ones — the signature bind and the set equality
— are the most valuable things you will write today, because they hold whatever the model does.

```python
# tests/test_agent.py
import inspect
import types

from sutra.agent import _dispatch, _result_turn, run_loop
from sutra.loop import TOOLS
from sutra.tools import DECLARATIONS


class FakeCall:
    """One function_call step, without an SDK or a network."""

    def __init__(self, name: str, arguments: dict, id_: str) -> None:
        self.type, self.name, self.arguments, self.id = "function_call", name, arguments, id_


def test_declared_and_dispatchable_are_the_same_set() -> None:
    declared = {d["name"] for d in DECLARATIONS}
    assert declared == set(TOOLS), (
        f"declared but not dispatchable: {declared - set(TOOLS)}; "
        f"dispatchable but not declared: {set(TOOLS) - declared}"
    )


def test_declared_properties_bind_to_the_real_signatures() -> None:
    for d in DECLARATIONS:
        props = list(d["parameters"]["properties"])
        inspect.signature(TOOLS[d["name"]]).bind(**dict.fromkeys(props, "x"))


def test_required_names_only_declared_properties() -> None:
    for d in DECLARATIONS:
        assert set(d["parameters"]["required"]) <= set(d["parameters"]["properties"])


def test_result_turn_echoes_the_call_id_and_wraps_in_a_list() -> None:
    call = FakeCall("lookup_ticket", {"ticket_id": "4521"}, "fc_a1")
    turn = _result_turn(call, "Title: Keeps getting logged out.")
    assert turn["type"] == "function_result"
    assert turn["call_id"] == "fc_a1"
    assert turn["result"] == [{"type": "text", "text": "Title: Keeps getting logged out."}]


def test_an_unknown_tool_comes_back_as_text() -> None:
    result = _dispatch(FakeCall("send_email", {"to": "boss@corp"}, "fc_x"))
    assert "Unknown tool" in result and "send_email" in result


class AlwaysActs:
    """A fake client that never finishes: one function_call, forever."""

    def __init__(self) -> None:
        self.calls, self.interactions, self.last_input = 0, self, None

    def create(self, **kwargs: object) -> object:
        self.calls += 1
        self.last_input = kwargs.get("input")
        step = FakeCall("lookup_ticket", {"ticket_id": "4521"}, f"fc_{self.calls}")
        return types.SimpleNamespace(
            steps=[step],
            output_text=None,
            usage=None,
        )


def test_the_step_budget_is_still_a_hard_ceiling() -> None:
    client = AlwaysActs()
    answer = run_loop(client, "anything", max_steps=3)
    assert client.calls == 3
    assert "Stopped after 3 steps" in answer


# TODO(me): the eighth test, and it is the one that matters most. Build a fake
# whose first interaction holds TWO function_call steps with different ids, then
# assert that the payload sent on the second call contains two function_result
# turns whose call_ids match - AND that the first one's text is the ticket, not
# the article. An id-only assertion passes the swap in part 6.1.
```

**How to watch it go RED before it goes green:**

```bash
uv run python -m pytest tests/test_agent.py -q      # RED: no sutra/tools.py yet
# ... write sutra/tools.py, then sutra/agent.py, from parts 1.2 -> 3.3 ...
uv run python -m pytest tests/test_agent.py -q      # green
```

Then break each one and watch it fail — **a test you have never seen fail is a test you do not know
works:**

- Rename `ticket_id` to `ticketId` in the declaration only, and watch the bind test go red. That is
  the `TypeError` from 2.2, caught before anything is sent.
- Add a key to `TOOLS` with a stub function and watch the set-equality test go red. Note that
  **nothing else in the project would have told you** (5.1).
- Move `required` inside the field and watch the third test go red — the `400` from 1.2, caught
  offline.
- Change `_result_turn` to build `result` as a plain string instead of a list, and watch the fourth
  test go red on the shape rather than on the text.

---

## §6 Request budget

**Free-tier Gemini only.** No other provider is touched, and no tool makes a network call.

| What | Model calls |
| --- | --- |
| the steps probe (2.1) | 1 |
| 2.1 check yourself | 1 |
| the first real run (3.2) | 3 |
| 3.2 check yourself | 3 |
| the transposed id (4.1) | ~2 |
| 4.1 check yourself | ~2 |
| the tool-choice experiments (4.2) | ~3 |
| 4.2 check yourself | 3 |
| 💥 the failure lab (6.1) | ~4 |
| 6.1 after restoring | ~3 |
| **Total** | **~25** |

**Slightly less than yesterday, and for a reason worth noticing:** almost every check in this day is a
pure-function test or a structural assertion over your own source, and those are free. When a day's
most valuable tests cost nothing, run them constantly.

**Do not run the `tool_choice: "any"` experiment at the loop level without `max_steps=2`.** Part 4.2
explains why it cannot terminate; at the default of six it costs six calls to demonstrate something
two will show.

**Your limits are not in this document.** Free-tier numbers are per project, in AI Studio, and RPD
resets at midnight Pacific.

**Cost: $0.** Principle 15 — quota is the currency.

---

## §7 Traps

- **Tools are interaction-scoped.** `tools=DECLARATIONS` must go on **every** call inside the loop, not
  once before it. Forgetting it produces a model that talks about what it cannot do, with **no error**.
  This is the day's most common mistake. (2.4, 3.1, 4.2)
- **`output_text` is `None` on a tool-calling turn.** The model asked rather than answered, so there is
  no prose. Read `steps`; `output_text` is one view of it. (2.1)
- **The declaration's property names are Python keyword arguments.** `tool(**call.arguments)` means a
  rename on either side is a runtime `TypeError` on a paid call. Test the bind. (2.2)
- **Two `type` keys at two levels.** `"type": "function"` describes the tool; `"type": "object"` inside
  `parameters` is JSON Schema. Confusing them is the first `400`. (1.2)
- **`required` sits beside `properties`, not inside the field.** Requiredness is a fact about the
  object. (1.2)
- **`enum` over a vocabulary that grows is a validated lie.** A constrained decoder picks the nearest
  allowed value rather than reporting that none fit. (1.2, 4.1)
- **Copy the model's steps, never rebuild them.** `step.model_dump()`. A reconstructed turn loses the
  call id and anything the provider added. (2.4)
- **Answer every call before replying.** An unanswered `function_call` is rejected — including when the
  tool failed. A failure is still a result. (2.3, 3.3)
- **Carry the call to its result; do not `zip`.** Correct today, a silent data-swap the day execution
  goes concurrent. (3.3, 6.1)
- **`tool_choice: "any"` on every call removes the loop's exit.** The model can never say it is
  finished, so every run ends on the step budget. Scope it to one turn. (4.2)
- **Never declare a caller identity.** Anything the model can fill is attacker-controlled; identity
  arrives out of band, keyword-only, undeclared. (5.2)
- **`1.x → 2.x` trap #4 is unchanged.** Still no `try` around `_dispatch`. A domain miss returns text;
  a defect raises. (2.2, 3.2)

---

## §8 Verify before you code

Every page below was fetched on **2026-08-25** while this day was written. Principle 8: re-fetch on
the day you use them — this list is evidence, not a substitute.

| Source | What it settled |
| --- | --- |
| `ai.google.dev/gemini-api/docs/function-calling` | The declaration dict (`type`/`name`/`description`/`parameters`); `tools=[...]` on `interactions.create`; `interaction.steps` with `step.type`/`.name`/`.arguments`/`.id`; the `function_result` turn (`type`/`name`/`call_id`/`result`); the **stateless example** using `store=False` and `step.model_dump()`; parallel calls; `generation_config={"tool_choice": ...}` with modes `auto`/`any`/`none` and the `allowed_tools` form |
| `ai.google.dev/gemini-api/docs/interactions` | `tools` is **interaction-scoped** and does not persist across `previous_interaction_id`; **automatic function calling (Python) is not available** on this surface — it belongs to legacy `generateContent` |
| `pypi.org/pypi/google-genai/json` | **2.19.0**, unchanged since Day 2's lookup on 2026-08-24. Nothing is installed today |
| `pypi.org/pypi/google-adk/json` | **2.7.1** — a forward reference for tomorrow, and already ahead of plan §5's 2.6.3 baseline, which §5 itself instructs you to re-verify on install day |

**No ADK symbol is used today.** ADK is not installed until Day 5; part 7.1's `FunctionTool` mention is
a forward reference, verified rather than remembered, and it does not run.

The one thing to read off a live object rather than a page:

```bash
uv run python -c "
from google import genai
from sutra.config import load_env
from sutra.tools import DECLARATIONS
load_env()
i = genai.Client().interactions.create(model='gemini-3.7-flash', store=False,
    input=[{'type':'user_input','content':[{'type':'text','text':'status of ticket 4521?'}]}],
    tools=DECLARATIONS)
print([s.type for s in i.steps])
print({k: v for k, v in i.steps[0].model_dump().items()})
"
```

One model call. If the field names it prints disagree with anything above, **the object wins** and the
correction gets a dated note — Principle 7 records what was observed.

---

## §9 Say it in an interview

> "The day I actually understood function calling was the day I'd already built the same agent with a
> text protocol, because then the diff told me what it was for. Most of my code disappeared — the
> parser, the format instructions in the prompt, the tool menu, the retry-with-coaching branch, and
> every near-miss those existed to absorb. The call arrives as a step with a name and an arguments
> dict that's already typed, so dispatch is a table lookup and a keyword unpack. What surprised me was
> what *didn't* change: the dispatch table that decides what may actually run, the rule that a domain
> miss returns text and a defect raises, the step budget, and appending both halves of the exchange.
> That split told me where design effort belongs — the things that survive a protocol rewrite are the
> real system. The other thing I'd say is what a schema doesn't buy. It validates shape, not meaning:
> the model will happily send me a perfectly typed ticket id for a ticket that doesn't exist, or one
> belonging to a different customer, and every validator I have is happy about both. So I think of it
> as three layers — shape at the provider, domain in the tool, authority in my code — and only the
> first one moved. The failure I design against is the well-typed wrong argument, because it produces
> a successful call, a successful tool run and a plausible answer, with no error anywhere."

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked — honestly. `./m done 4` refuses to commit while
any box is unticked, and it cannot tell whether you were truthful. That part is yours.

The day is finished when `sutra/agent.py` triages ticket 4521 in three steps with a cited `KB-104`;
when it reports a miss on ticket 4512 rather than diagnosing it anyway; when you have watched two tool
results filed against the wrong calls and restored the pairing; when the seven offline tests are green
and you have seen each of them go red; and when `sutra/loop.py` is **unchanged**.

---

## §11 Ledger & commit

Paste these **with the values you actually observed** (Principle 7), not the ones printed here.

**`docs/PROGRESS.md`** — append one row:

```text
| 4 | <date> | AG-04 | 16 | <hash> | ✅ |
```

**`docs/PACKAGES.md`** — **no rows today.** Nothing was installed; function calling is a feature of the
`google-genai` you already pinned on Day 2. If you have a row to add, find out what pulled it in before
you commit.

**`docs/SKILL_PROVENANCE.md`** — no rows. First entries arrive on Day 29.

**`docs/adr/`** — no new ADR. Today rests on ADR-0006 (Interactions-API-first) and adds no decision the
plan has not already made.

**Commit message:**

```text
day 04: tools by hand - schemas, the call, the result turn - closes AG-04
```
