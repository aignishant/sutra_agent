---
day: 11
phase: 2
phase_name: "Models & tools"
title: "Tool context and tool design — the parameter the model never sees"
ids: ["ADK-12", "AG-06"]
principles: [1, 2, 4, 6, 8, 9, 10, 11, 13, 15, 16, 17, 18]
kind: lab
plan_version: "v2.2.1"
parts: 16
generated: "2026-08-27"
status: written
lab_scaffolded: false
commit: ""
---

# Day 11 — Tool context and tool design: the parameter the model never sees

> **Yesterday (Day 10):** the declarations wrote themselves. A Python function became a tool, the
> dispatch table disappeared, and Sutra's desk got its hands back — two read tools over synthetic data.
> **Today:** those hands find out *where they are*. One extra parameter connects a tool to the session
> it has been running beside all week — the state, the event it is about to become part of, and who is
> asking — and the second half of the day is the design discipline that stops that power being a
> liability.
> **Tomorrow (Day 12):** structured output — making the model's *answer* a shape you declared, the way
> today made its *arguments* one.

---

## §1 Where we are

A new person starts on the phones at a service desk.

Day one, they are given a script and a phone. They can answer questions from the script perfectly well,
and there is a specific limit to what they can do: everything they know has to be said to them by the
caller. Who are you? Which ticket? What did you buy? All of it arrives through the handset, and if the
caller says something wrong, the wrong thing is what the desk acts on.

Day two, somebody sits them in front of the actual system. Now the screen already shows who is calling,
what they bought, what they asked about last month. The caller says "it's still not working" and that
sentence is *enough*, because everything the sentence leaves out is on the screen.

That is the whole of ADK-12 in one image, and there are two things to notice about it.

The first is what got **better**. Fewer questions, shorter calls, and — the important one — the caller
can no longer tell the desk who they are. Yesterday, identity arrived through the handset; today it is
on the screen, and the screen is fed by the system rather than by whoever is speaking.

The second is what got **more dangerous**. A person with a screen can look up records that are not the
caller's, and can type things into fields that other people will read later. On day one that was
impossible. The capability and the risk arrived in the same training session, which is exactly why
Principle 13 says *blast radius before capability*.

So today has two halves, and the second is not an appendix. **Sections 1 and 2** are the mechanism:
what the context is, how ADK finds it, and what a state write actually does. **Sections 3 and 4** are
AG-06 — tool design — and they exist because a tool that can reach the session is a tool that can be
designed badly in new ways. Section 5 breaks it on purpose. Section 6 makes it testable and names the
two doors we are deliberately not opening.

One more thing about the shape of today: **nothing here needs a model.** Sixteen lab scripts, zero
requests. That is not frugality, it is the subject — a context is a Python object and a schema is
generated from a signature, so all of it can be read off the machine in front of you.

---

## §2 The map

Sixteen parts in six sections, and no papers today. There is no research paper behind "a framework
passes a context object to a callback"; it is an engineering convention, and the tool-design half is
craft rather than a citable result. The paper this day's ancestry belongs to — *Toolformer*
(`arXiv:2302.04761`) — was taught on
[Day 4](../day-04-tools-by-hand/papers/01-toolformer.md), and §17.4.2 says a paper is taught once and
cited afterwards. Tomorrow has one.

The day climbs `foundation → working → production`: section 1 is the parameter itself, section 2 is
state from inside a tool, section 3 is how to design a tool at all, section 4 is what it is allowed to
do, section 5 breaks it, and section 6 is how you test it and what is parked.

### Section 1 — `01-the-extra-parameter`: ADK-12, the injected argument

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [The parameter the model never sees](parts/01-the-extra-parameter/1.1-the-parameter-the-model-never-sees.md) | A parameter in Python, absent from the schema. Where did it go? | `foundation` |
| 1.2 | [Detected by type, not by name](parts/01-the-extra-parameter/1.2-detected-by-type-not-by-name.md) | Two ways ADK finds it, and the third case that produces neither | `working` |
| 1.3 | [One card, several doors](parts/01-the-extra-parameter/1.3-one-card-several-doors.md) | Six doors, and not one of them is new machinery | `working` |
| 1.4 | [The folded paper under the chair leg](parts/01-the-extra-parameter/1.4-the-folded-paper-under-the-chair.md) | `= None` changes nothing for ADK and everything for your traceback | `working` |

### Section 2 — `02-state-from-a-tool`: ADK-12, the write is an event edit

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [Writing on the carbon copy](parts/02-state-from-a-tool/2.1-writing-on-the-carbon-copy.md) | One assignment, two dictionaries, and Day 7's `state_delta` finally filled in | `working` |
| 2.2 | [Reading what you did not fetch](parts/02-state-from-a-tool/2.2-reading-what-you-did-not-fetch.md) | The same call, twice, honestly returning two different answers | `working` |
| 2.3 | [What not to put on the noticeboard](parts/02-state-from-a-tool/2.3-what-not-to-put-on-the-noticeboard.md) | 1615 bytes against 27, a secret's route to the provider, and the `temp:` prefix | `production` |

### Section 3 — `03-designing-a-tool`: AG-06, tool design

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [One tool, one job](parts/03-designing-a-tool/3.1-one-tool-one-job.md) | Why a `mode` parameter costs you the schema's ability to say "required" | `working` |
| 3.2 | [Name it for the model](parts/03-designing-a-tool/3.2-name-it-for-the-model.md) | The name is a prompt, ADK validates nothing, and duplicates only warn | `working` |
| 3.3 | [Arguments the model can supply](parts/03-designing-a-tool/3.3-arguments-the-model-can-supply.md) | Four kinds of input, of which exactly one is a parameter | `working` |
| 3.4 | [Two tools that overlap](parts/03-designing-a-tool/3.4-two-tools-that-overlap.md) | 3.1's rule pushed too far — and a metric that punishes the fix | `production` |

### Section 4 — `04-blast-radius`: AG-06 and ADK-12, containment

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [The line between read and write](parts/04-blast-radius/4.1-the-line-between-read-and-write.md) | One question sorts every tool you will ever write, and the strongest containment is not building it | `production` |
| 4.2 | [The identity a tool needs](parts/04-blast-radius/4.2-the-identity-a-tool-needs.md) | Closes Day 10's third open question. `user_id` is never a parameter | `production` |

### Section 5 — `05-failure-lab`: the deliberate failure

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [💥 The previous patient's file](parts/05-failure-lab/5.1-the-previous-patients-file.md) | Two conversations, one global, `status: ok` twice, and the wrong person's session | `production` |

### Section 6 — `06-in-production`: testing it, and what is parked

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 6.1 | [A tool without a model](parts/06-in-production/6.1-a-tool-without-a-model.md) | Four cheap objects, three assertions, no key and no quota | `production` |
| 6.2 | [🅿️ Artifacts and memory from a tool](parts/06-in-production/6.2-artifacts-and-memory-from-a-tool.md) | The two doors Sutra is not opening — and the rule that applies anyway | `production` |

---

## §3 Setup — run this

**No new packages today.** Day 5's `google-adk` 2.7.1 carries the whole day, and nothing here installs
anything. The `pytest-asyncio` question from
[Day 8](../day-08-sessions-and-services/parts/02-the-run/2.1-one-dish-from-one-recipe.md) is still open
and today makes it slightly more pressing — see §4.

```bash
# 1 - confirm where you are starting from
./m check

# 2 - the lab scratchpad for today
mkdir -p days/day-11-tool-context/lab
cd days/day-11-tool-context/lab
touch invisible.py detection.py doors.py no_default.py
touch carbon.py reading.py noticeboard.py
touch one_job.py names.py arguments.py overlap.py
touch blast_radius.py identity.py
touch crossed.py
touch without_a_model.py parked_doors.py
cd -

# 3 - what changes under sutra/ today
git diff --stat            # empty; you are about to edit two files
cat sutra/desk/tools.py    # yesterday's two tools, both pure functions
cat sutra/desk/sessions.py # Day 8's USER_ID constant - today it starts to matter
```

**Run `lab/invisible.py` before you read anything else.** Two functions, one extra parameter, and a
schema that is identical for both. Four lines of output carry the day's first half.

**Two files under `sutra/` change today** — `desk/tools.py` gains a context on one of its two tools and
an owner on its ticket records, and `tests/test_tools.py` gains a fixture and three tests. Nothing
else. `sutra/desk/agent.py` is **unchanged**: today changes what a tool can see, not what the agent is.

---

## §4 Build brief

**`sutra/desk/tools.py`** — three changes, and one deliberate non-change:

| Change | What it is | Taught in |
| --- | --- | --- |
| `TICKETS` records gain an `owner` | data that belongs to somebody, for the first time | 4.2 |
| `lookup_ticket(ticket_id, tool_context)` | ownership from `tool_context.user_id`, `not_found` for a non-owner, and one state write | 4.2, 2.1 |
| the `not_found` shape | identical for *does not exist* and *is not yours* | 4.2 |
| **`search_kb(query)` unchanged** | it needs nothing from the context, so it takes nothing | 4.1 |

That last row is the decision worth defending in review. It would be easy to add a context to both
tools for symmetry; **the cheapest tool is one that takes no context**, and `search_kb` is one.

**`tests/test_tools.py`** — the fixture from
[6.1](parts/06-in-production/6.1-a-tool-without-a-model.md) plus three assertions. See §5.

**`days/day-11-tool-context/lab/`** — sixteen scripts. **All sixteen cost zero requests.**

**`TODO(me)` markers left for you:**

- **4.2** — `sutra/desk/sessions.py` has a `USER_ID` constant. Decide whether it stays a constant, and
  write down what would have to change for Sutra to serve two people. The answer is short and it is
  the whole of Phase 11 in miniature.
- **4.1** — write down which of Sutra's tools are reads and which will be writes, before any write
  exists. Then decide whether `tools/reads.py` and `tools/writes.py` is worth doing now or on the day
  the first write lands.
- **6.1** — decide where the context fixture lives: `tests/conftest.py` or the test file. If
  `conftest.py`, that is a new file and it is a small architectural decision about the test suite.
- **6.1** — the `pytest-asyncio` question, again, and today it is sharper: every tool test is now
  `async`. Either adopt it with a `PACKAGES.md` row, or keep wrapping in `asyncio.run` and write down
  why.
- **2.2** — `search_kb` could read a language preference from state. Decide whether Sutra wants that
  yet, and if not, write the sentence saying why not.
- **3.4** — run the overlap check over Sutra's two real tools and record the number. It is the
  baseline against which the fourth and fifth tools will be judged.
- **3.2** — decide whether a tool-name uniqueness and format check belongs in `./m check` now or at
  the Day 31 quality gate.

---

## §5 The eval that must be able to fail

One file, extended. The interesting property of today's tests is that they assert on something no test
so far has touched: **what the tool wrote**, not only what it returned.

```python
# tests/test_tools.py - the three new tests. Keep Day 10's five.
import asyncio

from google.adk.agents import LlmAgent
from google.adk.agents.invocation_context import InvocationContext
from google.adk.events import EventActions
from google.adk.sessions import InMemorySessionService
from google.adk.tools import ToolContext

from sutra.desk.tools import lookup_ticket


async def make_context(user_id: str, **state) -> tuple[ToolContext, EventActions]:
    """A ToolContext over a fresh session, plus the actions its writes land on."""
    service = InMemorySessionService()
    session = await service.create_session(app_name="sutra", user_id=user_id, state=dict(state))
    agent = LlmAgent(name="sutra_desk", model="gemini-3.7-flash", instruction="x")
    invocation = InvocationContext(
        session_service=service, invocation_id="inv-test", agent=agent, session=session
    )
    actions = EventActions()
    context = ToolContext(invocation, event_actions=actions, function_call_id="fc-1")
    return context, actions


def test_the_owner_gets_their_ticket() -> None:
    """4.2: identity comes from the context, and the owner is allowed."""

    async def check() -> dict:
        context, _ = await make_context("TODO(me): the owner of ticket 4521")
        return lookup_ticket("4521", context)

    assert asyncio.run(check())["status"] == "ok"


def test_someone_else_gets_the_same_answer_as_a_missing_ticket() -> None:
    """4.2: 'forbidden' would confirm the ticket exists. It must not."""

    async def check() -> tuple[dict, dict]:
        first, _ = await make_context("u-not-the-owner")
        second, _ = await make_context("u-not-the-owner")
        return lookup_ticket("4521", first), lookup_ticket("9999", second)

    not_yours, missing = asyncio.run(check())
    assert not_yours == missing


def test_a_refused_lookup_writes_nothing() -> None:
    """2.1, 4.2: the delta is the record. A refusal must leave no trace."""

    async def check() -> dict:
        context, actions = await make_context("u-not-the-owner")
        lookup_ticket("4521", context)
        return actions.state_delta

    assert asyncio.run(check()) == {}
```

**How to watch each one go RED before it goes green:**

```bash
uv run python -m pytest tests/test_tools.py -q -m "not live"   # RED: lookup_ticket takes no context yet
# ... make the change from part 4.2 ...
uv run python -m pytest tests/test_tools.py -q -m "not live"   # green
```

Then break each one on purpose:

- Delete the owner check from `lookup_ticket` and watch the second test go red. Read the failure: it
  says a non-owner got a different answer from a missing ticket, which is the information leak stated
  as a diff.
- Change the refusal to `{"status": "forbidden", "owner": record["owner"]}` and watch the same test go
  red for a second reason. Both reasons are the same reason.
- Move the state write above the ownership check and watch the third go red. That is the most likely
  real version of this bug and the test exists for it.
- Give the context parameter a `= None` default and watch **nothing** go red — the tests always supply
  one. That is [1.4](parts/01-the-extra-parameter/1.4-the-folded-paper-under-the-chair.md)'s argument
  arriving from the other side: the default is invisible to exactly the thing you would hope catches
  it.

**And one test to write yourself.** Day 10's suite asserted `names == {"lookup_ticket", "search_kb"}`.
Today, add the assertion that **no tool declares a parameter named `user_id`** — four lines over
`canonical_tools()`, no network, and it makes 4.2's rule permanent instead of remembered.

---

## §6 Request budget

**Free-tier Gemini**, 20 requests per day (`docs/PACKAGES.md`, 2026-08-25).

| What | Model calls |
| --- | --- |
| all sixteen lab scripts, all six sections | **0** |
| the whole test suite | **0** |
| **Total** | **0 of 20** |

Today spends nothing, and the reason is worth stating rather than enjoying: **a context is an object
and a declaration is generated from a signature.** Every claim in this day is a property of code you
have on disk, so every claim can be checked by running it. Nothing today depends on what a model
*decides*, which is the only thing that costs money.

**Optional, if you have quota and want it:** run
[Day 10's `watch_the_loop.py`](../day-10-function-tools/lab/) against today's `lookup_ticket` and find
the `state_delta` on the function-response event. Two or three requests, and it turns
[2.1](parts/02-state-from-a-tool/2.1-writing-on-the-carbon-copy.md)'s mechanism into something you have
watched happen in a real run rather than assembled by hand. It is the only thing today that a real run
shows you and a script cannot.

**Cost: $0.**

---

## §7 Traps

- **The context parameter is excluded from the schema, not hidden by convention.** ADK removes it
  before the declaration is generated, so the model never learns it exists. (1.1)
- **Detection is by annotation first, name second.** The first parameter annotated with a context type
  wins whatever it is called; only if none is annotated does ADK look for the literal name
  `tool_context`. (1.2)
- **A parameter that is neither annotated nor named `tool_context` is offered to the model** — no
  error, and your function receives whatever string the model invented. (1.2)
- **`ToolContext is Context` is `True`.** So is `CallbackContext`. One class, three names; the alias you
  choose is documentation for the reader. (1.2)
- **`tool_context: ToolContext = None` changes nothing for ADK** and converts a `TypeError` at the call
  site into an `AttributeError` inside your body, on whichever branch touches state first. (1.4)
- **A state write goes into `session.state` immediately** — before any event exists. That is a dirty
  read, and it is why the in-memory service hides the next trap. (2.1)
- **`state._delta` *is* `actions.state_delta`** — the same object, so one assignment stages the change on
  the event that will carry your tool's result. (2.1)
- **A nested in-place mutation produces no delta.** `state["counts"]["x"] += 1` never calls
  `__setitem__`, works perfectly on the in-memory service, and stops working on Day 22. (2.1)
- **`State` is not a `dict`.** No `keys()`, no `items()`, no iteration — `dict(state)` raises
  `KeyError: 0` because Python falls back to integer indexing. Use `.to_dict()`. (2.1, 2.2)
- **A tool that reads state has inputs the schema never mentions**, so the same call can honestly
  return two different answers and the transcript will not say why. Echo what you resolved. (2.2)
- **Every state write is stored forever**, so state takes handles rather than payloads — 1615 bytes
  against 27 on one small article. (2.3)
- **Instructions are templated against state**, so a secret in state can reach the model provider with
  nobody making a second mistake. (2.3)
- **`temp:` opts out of persistence, not of visibility.** ADK trims those keys from the event delta
  before storage, and they are readable by everything else in the invocation. (2.3)
- **A tool with an `action` parameter cannot mark the arguments some actions need as required** — the
  business rule degrades into an English sentence in a description. (3.1)
- **You cannot gate half a tool.** `require_confirmation` attaches to a tool, not to a branch inside
  one, so merging tools merges their blast radii. (3.1, 4.1)
- **The tool name is the Python function's `__name__`**, sent verbatim, so a rename in a refactor is a
  prompt change. (3.2)
- **ADK validates nothing about a tool name** — spaces, hyphens and leading digits are all declared
  cheerfully and rejected, if at all, by the provider at request time. (3.2)
- **Two tools with the same name produce a `logging.warning`, not an error.** Both declarations go to
  the model and only the last-registered one can be dispatched to. (3.2)
- **A model given a required field it cannot answer produces something the right shape.** A date with
  no clock, an id it found earlier in the conversation. (3.3)
- **A hallucinated identifier fails loudly in tests and silently in production**, because production
  identifier spaces are dense enough that an invented id resolves to a real record. (3.3)
- **Measuring whole descriptions punishes the correct fix** for overlapping tools, because a good fix
  cross-references the sibling tool. Measure summary lines. (3.4)
- **Gating reads makes the system less safe**, because a person clicking yes forty times an hour will
  click yes on the one that mattered. (4.1)
- **`user_id` as a parameter is an authorisation decision handed to a text generator** that is reading
  ticket bodies written by strangers. (4.2)
- **`tool_context.user_id` is not authorisation and is not a source of truth** — the ownership check is
  still your code, and the value is only as good as whatever your server passed to `create_session`.
  (4.2)
- **A context stashed in a module-level variable is safe until the function gains an `await`**, and the
  diff that introduces the bug is a diff about something else. (5.1)
- **The context always has `save_artifact` and `search_memory`** whether or not the service was
  configured; the failure is a `ValueError` at runtime, inside a tool, in front of a user. (6.2)

---

## §8 Verify before you code

Every source below was checked on **2026-08-27** while this day was written. Principle 8: re-check on
the day you use them. This table is evidence, not a substitute.

| Source | What it settled |
| --- | --- |
| `adk.dev/context/` | that `ToolContext` is what a tool receives and is **excluded from the schema shown to the model**; that it carries `state`, `actions`, `function_call_id`, the artifact methods and `search_memory`; and that `function_call_id` is *"crucial for linking authentication requests or responses back correctly"* |
| `adk.dev/tools-custom/function-tools/` | that a `ToolContext` parameter is added by declaring it in the signature and is not part of what the model fills in; the dict-with-a-status return shape carried over from Day 10 |
| the installed `google-adk` 2.7.1 | `find_context_parameter` — *"the name of the first parameter that is annotated with Context or a type alias of Context (e.g., ToolContext, CallbackContext)"*, with the literal-name fallback · `ToolContext is Context` → `True` · `Context.__init__` building `State(value=session.state, delta=self._event_actions.state_delta)` · `functions.py`'s *"State deltas are not applied here — they are collected in `tool_context.actions.state_delta` and applied later when the session service processes the events"* · the function-response event built with `actions=tool_context.actions` · `State` having `__getitem__`/`__contains__`/`get`/`to_dict` and **no** `__iter__` · `base_session_service._trim_temp_delta_state` removing `temp:` keys before storage · `LlmRequest.append_tools` logging *"Duplicate tool name %r: the previously registered tool is shadowed and can no longer be called."* while advertising both declarations |

**Eight claims in this day that no page states**, established by running code rather than by reading.
Re-run them; if your version disagrees, **your terminal wins** and you fix the document:

```bash
uv run python days/day-11-tool-context/lab/detection.py     # 1.2 - the third row is offered to the model
uv run python days/day-11-tool-context/lab/doors.py         # 1.3 - eleven doors present on 2.7.1
uv run python days/day-11-tool-context/lab/no_default.py    # 1.4 - the default changes nothing for ADK
uv run python days/day-11-tool-context/lab/carbon.py        # 2.1 - state._delta IS actions.state_delta
uv run python days/day-11-tool-context/lab/noticeboard.py   # 2.3 - temp: trimmed from the stored delta
uv run python days/day-11-tool-context/lab/one_job.py       # 3.1 - a merged tool cannot require a reason
uv run python days/day-11-tool-context/lab/names.py         # 3.2 - duplicates warn and shadow
uv run python days/day-11-tool-context/lab/crossed.py       # 5.1 - two ok statuses, one wrong session
```

The last one is the one to run twice. Delete the `await` from the broken version and it starts
producing correct output with the bug still in it — which is the most useful thing this day can show
you about why the failure survives review.

---

## §9 Say it in an interview

> "The thing I'd want to get across about tool context is that it isn't a feature, it's a connection.
> A tool used to be a pure function of its arguments, which made it pleasant and useless for anything
> that needed to know where it was. Adding one parameter — detected by its type annotation, excluded
> from the schema the model sees — connects it to the session state, the event actions for that step,
> the identity of whoever is asking, and the artifact and memory services. None of that is new
> machinery; it's the subsystems the runtime already had, reachable from inside a tool for the first
> time. Two mechanics I'd want a team to actually know. A state write is an event edit: the state
> object wraps the live session dictionary and a delta, the delta is literally the `state_delta` on the
> event that will carry your tool's result, and nothing is committed until the session service
> processes that event — so mutating a nested value in place produces no delta and breaks the day you
> move off the in-memory service. And the identity one, which I'd argue is the most important
> engineering consequence: `user_id` must never be a tool parameter, because a parameter is filled in
> by the model, and the model is reading a conversation that contains text other people wrote. That
> makes an authorisation decision a token prediction over attacker-influenceable input. Take it from
> the context, keep the ownership check in your own code, and return the same answer for 'not yours'
> as for 'doesn't exist' so the error message isn't an output channel. The failure I'd warn about is
> stashing the context in a module-level variable so a helper can reach it — safe until the function
> gains an `await`, then it writes one user's data into another user's session with a successful status
> and nothing in the logs, and it can't be reproduced in any single-user environment."

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked — honestly. `./m done 11` refuses to commit while
any box is unticked, and it cannot tell whether you were truthful. That part is yours.

The day is finished when `lookup_ticket` takes a context with no default, reads identity from it rather
than from a parameter, checks ownership in your own code, and returns the same answer for *not yours*
as for *does not exist*; when `search_kb` still takes no context and you can say why that is a decision
rather than an oversight; when a refused lookup provably writes nothing to `state_delta`; when you have
watched `crossed.py` write into the wrong person's session with two `ok` statuses; when you have made
the tool-name check, the read/write list and the `user_id` assertion into things a test enforces rather
than things you remember; when `USER_ID` in `sessions.py` has a written decision beside it; when the
`pytest-asyncio` question has an answer either way; and when `sutra/desk/agent.py` is **unchanged**.

---

## §11 Ledger & commit

Paste these **with the values you actually observed** (Principle 7), not the ones printed here.

**`docs/PROGRESS.md`** — append one row:

```text
| 11 | <date> | ADK-12, AG-06 | 16 | <hash> | ✅ |
```

**`docs/PACKAGES.md`** — **no new rows**, unless you adopted `pytest-asyncio` for §4's open question.
If you did, it is a dated row with an exact `==` pin like every other, and the reason goes in the row:
*"every tool test is async from Day 11."*

**`docs/PAPERS.md`** — no rows. Today has no paper, and the one this subject descends from,
*Toolformer* (`arXiv:2302.04761`), was taught on Day 4.

**`docs/SKILL_PROVENANCE.md`** — no rows. First entries arrive on Day 29.

**`docs/adr/`** — no new ADR is required, and there are two decisions worth recording in the commit
message: what happens to `USER_ID`, and where the test fixture lives. **If your ADK version has changed
how the context parameter is detected, or no longer trims `temp:` keys from the stored delta, stop and
re-read Principle 14 before editing anything** — both are behaviour changes in a pinned dependency, and
the plan is amended first.

**Commit message:**

```text
day 11: tool context & tool design - the parameter the model never sees - closes ADK-12, AG-06
```
