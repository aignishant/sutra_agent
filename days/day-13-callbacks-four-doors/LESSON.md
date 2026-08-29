---
day: 13
phase: 2
phase_name: "Models & tools"
title: "Callbacks — four doors and one rule"
ids: ["ADK-14", "ADK-15"]
principles: [1, 2, 4, 6, 8, 9, 10, 11, 13, 15, 16, 17, 18]
kind: lab
plan_version: "v2.2.1"
parts: 19
generated: "2026-08-29"
status: written
lab_scaffolded: false
commit: ""
---

# Day 13 — Callbacks: four doors and one rule

> **Yesterday (Day 12):** the answer got a declared shape and an address in session state — and the
> mechanism turned out to be a tool ADK writes for you rather than the provider enforcing anything.
> **Today:** you get to stand inside the agent. Six places where the framework will call a function of
> yours, one rule that decides what happens next, and the discovery that the rule as documented is not
> quite the rule as implemented.
> **Tomorrow (Day 14):** plugins — the same six doors at application scope, running *before* today's
> callbacks and able to stop them.

---

## §1 Where we are

A shop with a chime on the door.

The owner does not stand at the entrance all day. She screws a chime to the door frame once, in the
morning, and after that she never touches it. Somebody walks in, the door swings, the chime sounds,
and she looks up from the back room.

Most of the time she looks up and carries on. The chime was information. But sometimes she calls out
"we're closed, sorry" before the person has taken three steps — and then the whole visit does not
happen. Same chime, same wiring. The difference is entirely in what she does when it sounds.

That is the day. You wire six functions to an agent, once, and never call them. ADK calls them: before
the model, after the model, before a tool, after a tool, and on the two occasions when something
raised. And at each one you decide whether you are watching or whether you are stopping the thing that
was about to happen.

**The rule is one sentence, and it is not the one in the documentation.** Return `None` and the thing
behind the door happens; return anything else and your value replaces it. That is what everybody
learns and it is what ADK's own field docstrings say. The code checks something slightly different,
and the gap is wide enough that an empty dictionary silently stops every tool call in your agent
without raising anything. Section 4 is that gap, measured.

Two more things worth knowing before you start.

**Today costs nothing.** Every one of the nineteen lab scripts runs against a local model object that
reads its replies off a list — a real `BaseLlm` subclass, so the real flow runs, with real callbacks
and real session state, for zero requests and no key. You build it in part 1.3 and every later script
imports it. It is also what makes the day's tests runnable on a fresh clone.

**And the day ends with a failure that has no error message.** One `return` statement added to a
logging callback stops every tool in the agent from running and feeds the model your log record
instead. Nothing raises. The bug report you get says the model is hallucinating. Section 5 is that,
on purpose.

---

## §2 The map

Nineteen parts in six sections, and **no papers today**. Callbacks are an SDK surface, not a research
result: there is no citable origin document behind "a framework calls your function at a fixed point",
and §17.4.2 is explicit that a subtopic about a tool, a command or an SDK surface does not get a
manufactured one. The nearest real paper — *Toolformer* (`arXiv:2302.04761`) — was taught on
[Day 4](../day-04-tools-by-hand/papers/01-toolformer.md), and the honesty argument running through
sections 3 and 5 is Principle 10 rather than anybody's published claim.

The day climbs `foundation → working → production`: section 1 is what a callback is and the rules
every door shares, section 2 is the model pair, section 3 is the tool pair, section 4 is where the
shared rule stops behaving as documented, section 5 breaks it, and section 6 is how you test one and
what belongs in one.

### Section 1 — `01-the-four-doors`: the mechanics every door shares

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [The function you never call](parts/01-the-four-doors/1.1-the-function-you-never-call.md) | Six fields, and why nothing ran when you attached one | `foundation` |
| 1.2 | [The names are the contract](parts/01-the-four-doors/1.2-the-names-are-the-contract.md) | ADK calls by keyword, so a sensible rename is a `TypeError` | `working` |
| 1.3 | [`None` means carry on](parts/01-the-four-doors/1.3-none-means-carry-on.md) | One rule, six doors — and the scripted model the day runs on | `working` |
| 1.4 | [A list, not just a function](parts/01-the-four-doors/1.4-a-list-not-just-a-function.md) | The order you write them in is a policy decision | `working` |

### Section 2 — `02-the-model-doors`: ADK-14, before and after the model

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [What is actually in the request](parts/02-the-model-doors/2.1-what-is-actually-in-the-request.md) | One question, two model calls, and 98 characters of instruction you did not write | `working` |
| 2.2 | [Editing the request in place](parts/02-the-model-doors/2.2-editing-the-request-in-place.md) | Mutating and returning are different operations, not variations | `working` |
| 2.3 | [The call that never happened](parts/02-the-model-doors/2.3-the-call-that-never-happened.md) | Three questions, one request — and the counter that is not incremented | `production` |
| 2.4 | [Reading the reply first](parts/02-the-model-doors/2.4-reading-the-reply-first.md) | The last point before the reply becomes an event anything can read | `working` |
| 2.5 | [The door that fires on every chunk](parts/02-the-model-doors/2.5-the-door-that-fires-on-every-chunk.md) | One model call, three firings, and a reply no firing ever saw | `production` |

### Section 3 — `03-the-tool-doors`: ADK-15, before and after a tool

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [The chokepoint, restored](parts/03-the-tool-doors/3.1-the-chokepoint-restored.md) | Day 3's dispatch table, back — and now it can read session state | `working` |
| 3.2 | [Refusing a tool call honestly](parts/03-the-tool-doors/3.2-refusing-a-tool-call-honestly.md) | The same veto said three ways, and only one of them is not a lie | `production` |
| 3.3 | [The result, on its way back](parts/03-the-tool-doors/3.3-the-result-on-its-way-back.md) | 415 characters into 188, and the email that never reached the provider | `working` |
| 3.4 | [The doors that only open on an error](parts/03-the-tool-doors/3.4-the-doors-that-only-open-on-an-error.md) | Trap #4, and the one `return` that turns an outage into a lie | `production` |

### Section 4 — `04-where-the-rule-bites`: where the shared rule stops being simple

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [Truthy is not the same as not-`None`](parts/04-where-the-rule-bites/4.1-truthy-is-not-the-same-as-not-none.md) | Seven return values, and two functions whose order flips the outcome | `production` |
| 4.2 | [The plugin goes first](parts/04-where-the-rule-bites/4.2-the-plugin-goes-first.md) | Your callback is not the outermost layer, and can be skipped entirely | `production` |
| 4.3 | [The tool you did not write](parts/04-where-the-rule-bites/4.3-the-tool-you-did-not-write.md) | Yesterday's schema meets today's guard: one tool in, two tools out | `production` |

### Section 5 — `05-failure-lab`: the deliberate failure

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [💥 The note that became the result](parts/05-failure-lab/5.1-the-note-that-became-the-result.md) | One `return` in a logger, every tool silently disabled, no error anywhere | `production` |

### Section 6 — `06-in-production`: testing it, and what belongs in it

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 6.1 | [Testing a callback without a model](parts/06-in-production/6.1-testing-a-callback-without-a-model.md) | Four assertions you can call directly, and the fifth that needs a run | `production` |
| 6.2 | [What belongs in a callback](parts/06-in-production/6.2-what-belongs-in-a-callback.md) | Identical on your laptop, twice apart at four concurrent runs | `production` |

---

## §3 Setup — run this

**No new packages today.** `google-adk` 2.7.1 carries the whole day, and the local scripted model
means nothing new is installed and nothing is called over the network.

```bash
# 1 - confirm where you are starting from
./m check

# 2 - the lab scratchpad for today
mkdir -p days/day-13-callbacks-four-doors/lab
cd days/day-13-callbacks-four-doors/lab

# the shared test double - write this one FIRST, from part 1.3
touch scripted.py

# section 1
touch wiring.py names.py one_rule.py a_list.py
# section 2
touch the_request.py shaping.py shortcut.py redact.py per_chunk.py
# section 3
touch register.py refusal.py return_leg.py error_doors.py
# section 4
touch falsy.py gate_order.py injected.py
# section 5
touch poisoned.py
# section 6
touch cost_of_a_door.py
cd -

# 3 - what changes under sutra/ today
cat sutra/desk/agent.py     # gains one field
ls sutra/desk/              # callbacks.py is new
```

**Every lab script is run from inside `lab/`**, because they all `from scripted import ...` and that
only resolves when `lab/` is the working directory:

```bash
cd days/day-13-callbacks-four-doors/lab && uv run python one_rule.py
```

**Write `scripted.py` before anything else.** It is given complete in
[part 1.3](parts/01-the-four-doors/1.3-none-means-carry-on.md) and eighteen of the nineteen scripts
import it. Nothing else today works until it does.

**Then run `falsy.py` early**, before you have settled into believing the documented rule. It prints
seven lines and two of them contradict the documentation.

**Two files under `sutra/` change today** — a new `sutra/desk/callbacks.py`, and one field added to
`sutra/desk/agent.py`. `sutra/desk/tools.py` and `sutra/desk/schemas.py` are **unchanged**: callbacks
wrap around capability, they never reimplement it.

---

## §4 Build brief

**`sutra/desk/callbacks.py`** — new, and the day's centrepiece:

| Symbol | What it is | Taught in |
| --- | --- | --- |
| `audit_tool_calls` | the observer: one structured line per tool call, argument **names** only | 3.1, 6.2 |
| `blocked(reason, next_step)` | the one refusal shape every guard in the codebase returns | 3.2 |
| `block_forbidden_queries` | the override: refuses credential searches, legibly, without echoing the query | 3.2, 4.1 |
| `FORBIDDEN` | the term list — deliberately naive; the detector is Day 30's problem | 3.2 |
| `FRAMEWORK_TOOLS` | `{"set_model_response"}` — audited, never transformed | 4.3 |

**`sutra/desk/agent.py`** — one new field:

```text
before_tool_callback=[audit_tool_calls, block_forbidden_queries]
```

The order is the policy (1.4): the observer first, so the audit trail contains the refusals. Nothing
else in that file changes.

**`days/day-13-callbacks-four-doors/lab/`** — nineteen scripts. **All nineteen cost zero requests.**

**`tests/test_callbacks.py`** — see §5.

**`TODO(me)` markers left for you:**

- **3.1** — decide what `audit_tool_calls` logs. The allow-list of argument names whose *values* may
  be recorded is a security decision, and `query` is not on it. Write the list and justify each name.
- **3.2** — write the `next` field for each refusal. A refusal with no way forward is a retry loop;
  a refusal that quotes the query is a credential in the transcript. Both are one sentence to get
  wrong.
- **4.1** — go through every callback you have written today and answer, per branch: can this return
  a falsy non-`None` value? Fix any that can.
- **4.3** — decide `FRAMEWORK_TOOLS`' policy. Audit it, tagged by origin, is this document's
  recommendation; skipping it in the audit is a defensible different answer. Pick one and write down
  why. Then run `injected.py` on **your** machine and record whether
  `capabilities.output_schema_and_tools` is `False` for you as it is here.
- **5.1** — the three-step exercise in part 5.1, and the third step is the one that matters: name the
  assertion in your own suite that would have caught the poisoned observer. There isn't one yet.
- **6.1** — decide where the shared `ScriptedModel` lives when Day 25 wants it too: `tests/scripted.py`,
  or replaced by whatever the eval framework provides. Do not move it today; write down the trigger.
- **6.2** — measure `cost_of_a_door.py` at 16 concurrent runs on your machine and write the two
  numbers into `docs/PACKAGES.md`'s behaviour notes if they differ materially from this document's.
- **The plugin question.** Everything you attach today is per-agent. Tomorrow moves the audit up a
  layer. Before reading Day 14, write down which of today's two callbacks you think belongs in a
  plugin and why — then check yourself against 4.2's one question: *if somebody adds a new agent next
  quarter and forgets this rule, is that a bug or a choice?*

---

## §5 The eval that must be able to fail

One new file, five assertions, **no API key required**. These run on a fresh clone with no `.env`, and
the full file with its walkthrough is
[part 6.1](parts/06-in-production/6.1-testing-a-callback-without-a-model.md).

Four of the five call the callback directly — it is a plain function, so building the three keyword
arguments and asserting on the return value covers everything about *what it decides*. The fifth needs
a whole agent run, because *"did the tool actually run?"* is a fact about the framework's behaviour
given your return value, and it is the only assertion that goes red on
[5.1](parts/05-failure-lab/5.1-the-note-that-became-the-result.md)'s poisoned observer.

**How to watch it go RED before it goes green:**

```bash
uv run python -m pytest tests/test_callbacks.py -q -m "not live"   # RED: sutra/desk/callbacks.py is empty
# ... write the module from §4 ...
uv run python -m pytest tests/test_callbacks.py -q -m "not live"   # green
```

Then break each one on purpose:

| Break this | Which test goes red | What it is telling you |
| --- | --- | --- |
| add `return summary` to `audit_tool_calls` | 1 **and** 5 | an observer became an override, and every tool stopped running |
| make the guard `return {}` on the carry-on path | 2 and 5 | falsy is not `None` at this door (4.1) |
| drop the `next` field from the refusal | 3 | the model's only remaining move is to retry the forbidden call |
| put the query into the refusal message | 4 | the credential is now in the transcript, permanently |
| rename a parameter to `arguments` | all five | the names are the contract (1.2) |

Only the last row fails everything, which is the point of the first four: they say *what* broke.

**And one thing left undone deliberately.** The sixth test — *does the guard block the queries that
matter?* — is `@pytest.mark.skip` with a `TODO(me)`, because every query in the file is one you thought
of. It proves nothing about what a real customer sends. That is Day 25, and a skipped test that says
so is more honest than a green suite that implies a guarantee it cannot make.

---

## §6 Request budget

**Free-tier Gemini**, 20 requests per day (`docs/PACKAGES.md`, 2026-08-25).

| What | Model calls |
| --- | --- |
| all nineteen lab scripts, all six sections | **0** |
| the whole test suite | **0** |
| the failure lab | **0** |
| **Total required** | **0 of 20** |

Three days in a row at zero, and today for a new reason: the day runs on a `BaseLlm` subclass that
reads its replies off a list. The flow is real — real callbacks, real tool dispatch, real events, real
session state — and the network is not involved. That is not a shortcut around the subject; a callback
is a function ADK calls, and whether the model on the other side is a provider or a list changes
nothing about when it is called or what its return value does.

**Optional, and worth one request if you have quota:** attach `audit_tool_calls` to the real desk and
run one triage against `gemini-3.7-flash`. Two things a scripted model cannot show you — what the
model actually decides to put in `args`, and the `set_model_response` call arriving from
[Day 12](../day-12-structured-output/parts/03-schema-and-tools-together/3.2-the-tool-adk-injects.md)'s
injection in a real trace rather than a scripted one.

**Cost: $0.**

---

## §7 Traps

- **A callback is attached as a function object, not called** — `before_model_callback=announce`, never
  `announce()`. The parentheses fire it at construction. (1.1)
- **ADK calls callbacks by keyword**, so parameter names are an interface. ADK's own source says the
  type aliases look positional but *"the framework has always invoked them by keyword"*. (1.2)
- **Model doors take `callback_context`; tool doors take `tool_context`.** Same class in 2.7.1, two
  names, and you must use the right one in the right place. (1.2)
- **Tool doors call the argument dict `args`.** Day 14's plugins call it `tool_args`. (1.2, 4.2)
- **A callback that raises takes the whole turn down** — through `DynamicNodeFailError`, which is a
  wrapper and not the cause. (1.2, 6.2)
- **Every callback field also accepts a list**, run left to right, stopping at the first value. (1.4)
- **A tuple is accepted** — Pydantic coerces it to a list — but a `None` left in a list fails at
  construction with two errors, because the field's type is a union. (1.4)
- **`contents` is the whole conversation, resent every turn.** One user question with one tool call is
  two requests, and the second carries three turns. (2.1)
- **`config.system_instruction` is not what you wrote.** ADK appends an identity line; an output schema
  appends more. 49 characters became 98. (2.1)
- **The request is passed by reference and ADK's docstring says you may mutate it.** Mutating shapes
  the call; returning cancels it. They are different operations. (2.2)
- **Use `append_instructions`, not `+=`** — the field may be `None`, a `str` or a `Content`. (2.2)
- **A before-model callback fires once per model call, not once per turn**, so an unconditional append
  repeats itself all invocation. (2.2)
- **A short-circuit is not counted against `max_llm_calls`** — `increment_llm_call_count()` is
  downstream of the callback, so the run's real iteration ceiling rises. (2.3)
- **Match a short-circuit on something a tool result cannot produce.** After the first model call, the
  newest `role="user"` entry is the tool's result. (2.3)
- **The model doors trade in `LlmResponse`; the tool doors trade in dicts.** A bare string reaches
  `AttributeError: 'str' object has no attribute 'content'`. (2.3)
- **`after_model_callback` fires once per *yielded response*, not per model call** — three yields,
  three firings, and no firing ever sees the whole reply. Check `partial` on the first line. (2.5)
- **A tool-door callback sees every tool**, so branch on `tool.name` before touching `args`. (3.1, 4.3)
- **A refusal dict reaches the model as if the tool produced it.** `{"status": "ok", "results": []}` is
  a lie your own agent will repeat to a customer. (3.2)
- **A refusal with no `next` field becomes a retry loop**; a refusal that quotes the query puts the
  credential in the transcript forever. (3.2)
- **Two `after_tool_callback` transformers do not compose** — the chain stops at the first that returns
  a value, so the second never runs. (3.3, 4.1)
- **Truncating without saying so is a lie of omission.** One `"truncated"` field fixes it. (3.3)
- **`on_*_error_callback` returning `None` re-raises; returning a value swallows the exception.**
  Allow-list the transient failures; never substitute for your own bugs. (3.4)
- **1.x → 2.x trap #4:** do not catch exceptions inside a tool to hide them. 2.x surfaces them through
  the runtime *so that* the error hooks can act on them. (3.4)
- **The documented rule and the implemented rule differ.** The docstring says *"until a callback does
  not return None"*; the code breaks on **truthy** and then checks `is None` before running the tool.
  An empty dict falls between: the tool is skipped and the model gets `{}`. (4.1)
- **A falsy non-dict is rewrapped** — returning `0` reaches the model as `{'result': 0}`. (4.1)
- **`[returns None, returns {}]` and `[returns {}, returns None]` do opposite things**, because the loop
  assigns unconditionally and the last one wins. (4.1)
- **Plugins run before agent callbacks at every door**, and a plugin that returns a value means your
  callback never executes at all — not overruled, skipped. (4.2)
- **`Runner(plugins=[...])` is deprecated in 2.7.1**; plugins belong on an `App`. (4.2)
- **`tools=[...]` is not the complete list of tools your callbacks will see.** With an output schema on
  the Gemini API path, `set_model_response` arrives too — audit it, never transform it. (4.3)
- **A stray `return` in a logging callback disables every tool in the agent**, with no error, and
  reports as the model hallucinating. (5.1)
- **A `Mock` tool context makes a guard take the wrong branch and the test pass.** Write a five-line
  stub. (6.1)
- **A blocking callback holds the event loop**, so it is indistinguishable from an async one on a
  single run and more than twice as slow at four concurrent runs. (6.2)

---

## §8 Verify before you code

Every source below was checked on **2026-08-29** while this day was written. Principle 8: re-check on
the day you use them. This table is evidence, not a substitute.

| Source | What it settled |
| --- | --- |
| `adk.dev/callbacks/types-of-callbacks/` | the six hooks and their documented signatures · *"Every callback field also accepts a list of functions instead of a single function."* · `before_model_callback` returning an `LlmResponse` *"skips"* the model call · the error hooks stop *"on any value that is not `None`"* while the tool hooks stop on a truthy value |
| `adk.dev/callbacks/` | the callbacks index and the per-agent framing that separates a callback from tomorrow's plugin |
| the installed `google-adk` 2.7.1 | the six `LlmAgent` callback fields and their `Union[_Single…, list[…]]` type aliases · the comment *"The callback type aliases are declared positionally, but the framework has always invoked them by keyword"* in `base_llm_flow.py` · `if response := await self._handle_before_model_callback(...)` returning **above** `increment_llm_call_count()` · `_handle_after_model_callback` called inside the `async for llm_response in agen:` loop · the `canonical_before_tool_callbacks` loop's unconditional `function_response = callback_result` followed by `if function_response:` and then `if function_response is None:` · `_run_on_tool_error_callbacks`' `if error_response is not None: ... else: raise tool_error` · `plugin_manager.run_before_tool_callback` awaited before the agent's loop · `LlmRequest.append_instructions` · `BasePlugin`'s *"plugins applies globally to all agents added in the runner"* and the `Runner(plugins=...)` deprecation note |

**Eleven claims in this day that no page states**, established by running code rather than by reading
it. Re-run them; if your version disagrees, **your terminal wins** and you fix the document:

```bash
cd days/day-13-callbacks-four-doors/lab
uv run python names.py            # 1.2 - the TypeError, and which name it complains about
uv run python one_rule.py         # 1.3 - model calls: 0 on a short-circuit
uv run python a_list.py           # 1.4 - the audit that never happens
uv run python the_request.py      # 2.1 - one question, two requests, 98 chars of instruction
uv run python shaping.py          # 2.2 - the history that stopped growing
uv run python per_chunk.py        # 2.5 - one model call, three firings
uv run python register.py         # 3.1 - one invocation id, a counter in session state
uv run python error_doors.py      # 3.4 - None re-raises; a dict swallows
uv run python falsy.py            # 4.1 - seven return values, five surprises
uv run python injected.py         # 4.3 - one tool in, two tools out
uv run python poisoned.py         # 5.1 - the tool that did not run, and no error
```

The two to run twice are `falsy.py` and `poisoned.py`. Everything in section 4 is downstream of the
first, and section 5 is the reason the day has a rule about `return` statements at all.

---

## §9 Say it in an interview

> "Callbacks are how you get inside an agent without forking the framework. ADK gives an agent six
> hooks — before and after the model, before and after every tool, and one each for when those raise —
> and you attach plain functions to them at construction. The framework calls them by keyword, so the
> parameter names are an interface rather than a style choice, and there's one rule across all six:
> return `None` and the underlying thing happens, return anything else and your value replaces it. So
> a before-tool hook that returns a dict genuinely stops the tool from executing, and that dict is
> handed to the model as though the tool had produced it. That last part is a design problem, not a
> mechanism problem — returning an empty success is the common mistake and it's a lie your own agent
> then repeats to a customer, so a refusal needs a status the model can branch on, a reason it can
> relay, and a suggested compliant action, or it just retries the forbidden call until it hits the
> limit. Two things I'd flag from having actually run this. The documented rule says the chain stops
> when a callback doesn't return `None`; the code breaks on a *truthy* value and then checks `is None`
> before running the tool, so an empty dict falls between the two and silently skips the tool — and
> two identical callbacks in the opposite order give opposite results. And the sharpest failure is
> that observers and overrides look the same at the attachment site: one stray `return` in a logging
> callback disables every tool in the agent, produces no error at all, and gets reported as the model
> hallucinating. My rules since are that observers end with no return statement and are annotated
> `-> None`, and that there's one test asserting the tool actually ran on the ordinary path — which is
> the only assertion that catches it."

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked — honestly. `./m done 13` refuses to commit while
any box is unticked, and it cannot tell whether you were truthful. That part is yours.

The day is finished when `sutra/desk/callbacks.py` holds an observer that ends with no `return` and a
guard that returns either `None` or a fully-populated refusal; when `sutra/desk/agent.py` attaches them
as a list in an order you can defend; when you have run `falsy.py` and can say what `{}` does at the
tool door and why; when you have run `poisoned.py` and watched an agent triage a ticket it never read;
when the five tests pass and you have watched each go red for its own reason; when the sixth is a
`TODO(me)` rather than a lie; when you have decided what `FRAMEWORK_TOOLS` policy the desk uses and
recorded whether your machine agrees with this document's `output_schema_and_tools: False`; and when
`sutra/desk/tools.py` and `sutra/desk/schemas.py` are **unchanged**.

---

## §11 Ledger & commit

Paste these **with the values you actually observed** (Principle 7), not the ones printed here.

**`docs/PROGRESS.md`** — append one row:

```text
| 13 | <date> | ADK-14, ADK-15 | 19 | <hash> | ✅ |
```

**`docs/PACKAGES.md`** — **no new rows.** Nothing was installed today.

Two things are worth a row **if your machine disagrees with this document**, because both are
behavioural facts about a pinned dependency in a particular environment, which is what that ledger is
for: the `output_schema_and_tools` boolean `injected.py` prints, and the concurrency numbers from
`cost_of_a_door.py` if the blocking and async lines do **not** diverge for you.

**`docs/PAPERS.md`** — **no new rows.** Today teaches no paper and cites none; see §2 for why.

**`docs/SKILL_PROVENANCE.md`** — no rows. First entries arrive on Day 29.

**`docs/adr/`** — no new ADR is required, and there is one decision worth recording in the commit
message: the order of the `before_tool_callback` list, and why the observer goes first. **If your ADK
version no longer breaks the tool-callback chain on a truthy value, or now treats an empty dict as
carry-on, stop and re-read Principle 14 before editing anything** — that is a behaviour change in a
pinned dependency, and the plan is amended first.

**Commit message:**

```text
day 13: callbacks - four doors and one rule - closes ADK-14, ADK-15
```
