---
day: 17
phase: 3
phase_name: "State, context & discipline"
title: "Session state — prefixes, scopes and lifetimes"
ids: ["ADK-19", "ADK-20"]
principles: [1, 2, 4, 6, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18]
kind: lab
plan_version: "v2.2.1"
parts: 18
generated: "2026-09-03"
status: written
lab_scaffolded: false
commit: ""
---

# Day 17 — Session state: prefixes, scopes and lifetimes

> **Yesterday (Day 16):** built-in tools with brakes — two capabilities switched on rather than
> written, and the containment story for each. That closed Phase 2.
> **Today:** Phase 3 opens with the store those capabilities have been quietly using. `session.state`
> is Sutra's working memory: a small form stapled to the conversation, with **four different
> lifetimes** chosen by the first word of a key's name, and exactly three ways to write it safely.
> **Tomorrow (Day 18):** artifacts — the other store, for the things that are too big to be facts.

---

## §1 Where we are

Moving day, and the labels on the boxes.

You are not carrying much: some boxes, a bag, and a suitcase that has been in and out of three flats.
What decides how the day goes is not the lifting. It is what somebody wrote on the side of each box in
marker pen.

**Kitchen** goes in the kitchen and gets unpacked this week. **Bedroom — open first** has the kettle,
the bedding and the phone charger, and it is the one you carry in yourself. **Storage** goes straight
to the cupboard under the stairs and will be opened in two years or never. And the flattened cardboard
and the bubble wrap go out with the recycling on Thursday, because they were for the journey and the
journey is over.

Nobody looks inside a box to decide where it goes. They read the label. The label is not a description
of the contents — it is a decision about where the box lives and when it gets thrown out, made by
whoever held the pen, and it is very hard to change afterwards.

That is today. Sutra gets a place to keep structured facts — a severity, a ticket number, an engineer's
preference — and every key you write carries its lifetime in its name. Sections 1 and 2 are what state
is and how long each kind lives. Section 3 is the three ways to write it and why they all end the same
way. Section 4 is state reaching back into the prompt. Section 5 is the schema 2.x lets you declare and
what it does not check. Section 6 is the write everybody tries that silently does nothing, and
section 7 is what you keep, what you test, and what the history can tell you afterwards.

Four things worth knowing before you start.

**The transcript is a story; state is a form.** One is for the model to read, the other is for your
code. Putting a decision in prose costs a model call and a chance of being wrong every time somebody
needs it back.

**The prefix is the lifetime, and it is enforced.** `severity` dies with the conversation.
`user:severity` follows the engineer into every conversation they ever open. Nothing warns you; the
name *is* the behaviour.

**Every real write goes through an event.** That is what makes state changes ordered, attributed and
replayable. It is also why the obvious `session.state["k"] = v` does nothing at all.

**And three separate things in this day fail silently, in a background thread.** A schema violation, an
`output_schema` mismatch and a missing `{placeholder}` all produce the same symptom: a turn that
finishes with no answer and no exception you can catch. Meeting all three today is why Day 21 exists.

---

## §2 The map

Eighteen parts in seven sections, and **no paper**: session state is an SDK surface rather than an idea
from the literature, and the depth contract is explicit that a day does not manufacture a citation it
does not have (§17.4.2). The day climbs `foundation → working → production`.

### Section 1 — `01-form-not-story`: what state is

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [The transcript is not a database](parts/01-form-not-story/1.1-the-transcript-is-not-a-database.md) | Two stores, two readers, and which question each answers | `foundation` |
| 1.2 | [What may live in state](parts/01-form-not-story/1.2-what-may-live-in-state.md) | Seven values accepted, five that survive being written down | `working` |
| 1.3 | [The pad and the rail](parts/01-form-not-story/1.3-the-pad-and-the-rail.md) | The two dictionaries inside `State`, and the one that travels | `working` |

### Section 2 — `02-four-lifetimes`: the scopes

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [The prefix is the lifetime](parts/02-four-lifetimes/2.1-the-prefix-is-the-lifetime.md) | Five vantage points on one write, and four different answers | `foundation` |
| 2.2 | [An invocation is not a session](parts/02-four-lifetimes/2.2-an-invocation-is-not-a-session.md) | `temp_visible: True`, then `False`, one turn later | `working` |
| 2.3 | [Where `user:` and `app:` live](parts/02-four-lifetimes/2.3-where-user-and-app-live.md) | Why deleting the session deletes none of them | `working` |
| 2.4 | [Why `temp:` exists](parts/02-four-lifetimes/2.4-why-temp-exists.md) | 57,530 bytes kept, or 2 bytes shredded | `production` |

### Section 3 — `03-three-safe-writes`: how state actually changes

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [Writing from inside a tool](parts/03-three-safe-writes/3.1-writing-from-inside-a-tool.md) | An assignment, and the event that carries it | `working` |
| 3.2 | [The carbon copy](parts/03-three-safe-writes/3.2-the-carbon-copy.md) | `output_key`, and what lands when there is a schema | `working` |
| 3.3 | [Writing from outside a run](parts/03-three-safe-writes/3.3-writing-from-outside-a-run.md) | Intake, a nightly job, and a correction with an author | `working` |

### Section 4 — `04-state-in-the-prompt`: state reaching the model

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [State steers the next turn](parts/04-state-in-the-prompt/4.1-state-steers-the-next-turn.md) | The instruction the model actually received | `working` |
| 4.2 | [The brace that raises](parts/04-state-in-the-prompt/4.2-the-brace-that-raises.md) | Seven templates, seven rules, and one cliff | `production` |

### Section 5 — `05-a-schema-for-state`: declaring the keys

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [Declaring the boxes](parts/05-a-schema-for-state/5.1-declaring-the-boxes.md) | `state_schema`, and where the check actually happens | `working` |
| 5.2 | [What the schema does not do](parts/05-a-schema-for-state/5.2-what-the-schema-does-not-do.md) | An `int` field holding `'4521'`, and three unchecked prefixes | `production` |

### Section 6 — `06-failure-lab`: the deliberate failure

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 6.1 | [💥 The write that was never written](parts/06-failure-lab/6.1-the-write-that-was-never-written.md) | The same key, one line apart, with opposite answers | `production` |

### Section 7 — `07-in-production`: what you test, keep and can prove

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 7.1 | [Testing state without a model](parts/07-in-production/7.1-testing-state-without-a-model.md) | Six assertions, no key, and a test that asserts a failure | `production` |
| 7.2 | [What belongs in state](parts/07-in-production/7.2-what-belongs-in-state.md) | Four stores, four tests, and the keys nobody owns | `production` |
| 7.3 | [State as a trace](parts/07-in-production/7.3-state-as-a-trace.md) | Who set it, when, and what it was before | `production` |

---

## §3 Setup — run this

**No new packages today.** `google-adk` 2.7.1 carries all of it, and everything else is the standard
library.

```bash
# 1 - confirm where you are starting from
./m check

# 2 - today's lab
mkdir -p days/day-17-state-scopes-and-lifetimes/lab
cd days/day-17-state-scopes-and-lifetimes/lab

# yesterday's scripted model - copy it, do not import across day folders
cp ../../day-16-built-in-tools-with-brakes/lab/scripted.py .

# section 1
touch what_state_is.py what_fits.py pad.py
# section 2
touch scopes.py one_invocation.py where_user_lives.py the_cost_of_keeping.py
# section 3
touch in_a_tool.py carbon_copy.py from_outside.py
# section 4
touch steers.py braces.py
# section 5
touch declared.py schema_holes.py
# section 6
touch lost_write.py
# section 7
touch who_changed_it.py
cd -

# 3 - what changes under sutra/ and tests/ today
ls sutra/                    # state.py is new, at the package root
ls tests/                    # test_state.py is the eval; scripted.py is already there from day 15
```

**Every lab script runs from inside `lab/`**, because four of them import `scripted` by bare name:

```bash
cd days/day-17-state-scopes-and-lifetimes/lab && uv run python scopes.py
```

**Run `scopes.py` first.** It is five lines of output and it contains the whole of section 2; every
later part in that section explains one of those five lines.

**Then run `lost_write.py` before you write any code of your own.** It is section 6, it takes one
command, and it is the failure you would otherwise ship: two lines of output showing the same key
present and absent at the same moment.

**`sutra/state.py` is new and lives at the package root**, beside `builtin_tools.py`. That placement is
today's argument as a file path: the keys, their scopes and the one tool that writes them are facts
about the whole application, not about one agent.

---

## §4 Build brief

**`sutra/state.py`** — new, at the package root:

| Symbol | What it is | Taught in |
| --- | --- | --- |
| `SEVERITY`, `TICKET_ID`, `LAST_TRIAGE` | session-scoped key names, as constants a reviewer can grep | 1.3, 2.1 |
| `REPLY_STYLE` | the `user:`-scoped key that follows an engineer | 2.3 |
| `REFUND_WINDOW` | the `app:`-scoped key everybody shares | 2.3 |
| `RAW_SEARCH` | the `temp:`-scoped key handed between tools | 2.4 |
| `DeskState` | the pydantic model declaring the unprefixed keys | 5.1 |
| `record_triage` | the only writer of `severity` and `ticket_id` | 3.1, 7.2 |
| the module docstring | the scope rules and the three prohibitions | 7.2 |

Two things in that table are the whole design. Every key is a **named constant with its scope in a
comment**, because the prefix is the lifetime and a reviewer has to be able to see it
([2.1](parts/02-four-lifetimes/2.1-the-prefix-is-the-lifetime.md)). And `record_triage` calls
`int(ticket_id)` itself, because `DeskState` declaring `ticket_id: int` **validates without converting**
and would happily store the string
([5.2](parts/05-a-schema-for-state/5.2-what-the-schema-does-not-do.md)).

**`tests/test_state.py`** — new. Six assertions and one deliberate skip; see §5.

**Nothing under `sutra/desk/` has to change today**, and one of the `TODO(me)` items below is whether
it should. Confirm with `git diff` before you commit.

**`days/day-17-state-scopes-and-lifetimes/lab/`** — fourteen scripts plus the copied double. **All of
them cost zero requests.**

**`TODO(me)` markers left for you:**

- **4.2, 7.2** — decide whether the desk's instruction gains `{severity?}` and `{user:reply_style?}`
  today or in Phase 8. If it does, write the instruction so that it still reads correctly when both are
  blank, which is every conversation's first turn. Write down the sentence you chose.
- **2.1** — Sutra will eventually want an engineer's preferred reply style. Decide who writes
  `user:reply_style`: the engineer through a command, the desk inferring it, or an admin path. Note the
  failure each choice accepts.
- **7.2** — add a size budget. Pick a number of bytes a session's state may not exceed, write the
  assertion, and say what you would do when it fires.
- **5.1** — `DeskState` currently declares three keys. Decide whether the desk agent actually sets
  `state_schema=DeskState`, given that one undeclared key fails the **whole step**
  ([5.1](parts/05-a-schema-for-state/5.1-declaring-the-boxes.md)). Both answers are defensible; write
  down which failure you prefer.
- **2.4** — name one value in Sutra's future that should be `temp:` and one that must not be, and put
  both in the module docstring as examples.
- **7.3** — write the second history helper: given an `invocation_id`, every state change made during
  that one turn. Four lines, and it is the query Day 84 will want.

---

## §5 The eval that must be able to fail

One new file, **six assertions and one deliberate skip**, no key and no network. The whole file with
its walkthrough is [7.1](parts/07-in-production/7.1-testing-state-without-a-model.md).

Today is the opposite of yesterday. Yesterday nothing could be faked, because the capability lived in
the platform; today almost everything can be asserted, because state is a data structure whose rules
are enforced by code that needs no model. The one claim that cannot be made in this file is Phase 3's
own gate — *state survives restarts* — because an in-memory service cannot survive one. That test is
skipped, with a `TODO(me)` naming Day 47.

**How to watch it go RED before it goes green:**

```bash
uv run python -m pytest tests/test_state.py -q -m "not live"   # RED: no sutra/state.py yet
# ... write the module from §4 ...
uv run python -m pytest tests/test_state.py -q -m "not live"   # 6 passed, 1 skipped
```

Then break each thing on purpose. These were **measured**, each applied on its own to a green suite:

| Break this | Which test goes red | What it is telling you |
| --- | --- | --- |
| `REPLY_STYLE = "reply_style"` (drop `user:`) | the prefixes test | the prefix *is* the lifetime (2.1) |
| `RAW_SEARCH = "raw_search"` (drop `temp:`) | the trimming test | the intermediate is now kept for ever (2.4) |
| `state[TICKET_ID] = str(ticket_id)` | the `record_triage` test | the schema validates, it does not convert (5.2) |

**And one test asserts that something does not work.** `test_a_direct_write_is_lost` performs
[6.1](parts/06-failure-lab/6.1-the-write-that-was-never-written.md)'s forbidden write and asserts the
value is gone. If a future ADK ever makes that write stick, this test goes red and tells you the day's
advice has changed — which is exactly what a test of a documented anti-pattern is for.

---

## §6 Request budget

**Free-tier Gemini**, 20 requests per day (`docs/PACKAGES.md`, 2026-08-25).

| What | Model calls |
| --- | --- |
| all fourteen lab scripts, all seven sections | **0** |
| the failure lab | **0** |
| the whole test suite | **0** |
| **Total required** | **0 of 20** |

Zero, and the reason is worth stating because it is not the same reason as Day 15's. State is not a
model feature at all: it is a data structure the runtime keeps beside the conversation, and every rule
this day teaches — the four lifetimes, the trimming, the delta, the schema, the templating — can be
observed with a scripted model or with no model whatever. Four of the scripts drive a real `Runner`,
because *"a tool's write becomes an event"* is a claim about a run; they drive it against Day 13's
scripted double.

**Optional, and worth one request if you have quota:** put `{user:reply_style?}` in the desk's real
instruction, set the key, and send one triage to `gemini-3.7-flash`. The thing to watch is whether the
answer's *shape* changes — which is a fact about the model reading your filled-in instruction, and the
one thing a scripted model cannot tell you.

**Cost: $0.**

---

## §7 Traps

- **The transcript is not a database.** A decision left in prose costs a model call and a chance of
  being wrong every time something needs it back. (1.1)
- **State accepts anything and persists only some of it.** A `datetime` or a custom object is stored
  happily today and raises `TypeError: Object of type datetime is not JSON serializable` the day
  persistence arrives. (1.2)
- **`to_dict()` returns a copy.** Editing it changes nothing, silently. (1.3)
- **`setdefault` writes.** A call that looks like a read puts an entry in the delta and therefore in the
  history. (1.3)
- **The prefix is the lifetime, not a label.** `reply_style` and `user:reply_style` are different keys
  with different lives, and nothing warns you when you pick the wrong one. (2.1)
- **`temp:` is scoped to the invocation, not the session.** The next tool in the same turn can read it;
  the next turn cannot. (2.2)
- **`user:` and `app:` are not stored on the session.** Deleting a session deletes neither, which
  matters the first time somebody asks you to forget a user. (2.3)
- **Ordinary state is carried by every later turn.** Twelve turns with one modest intermediate each
  measured 57,530 bytes; the same twelve with `temp:` measured 2. (2.4)
- **A tool's `tool_context` must be annotated.** A parameter named `tool_context` with no
  `: ToolContext` annotation becomes an argument the model is asked to supply. (3.1)
- **Write state after the work that can fail.** A delta whose event never gets emitted is a write that
  never happened. (3.1)
- **`output_key` writes only on a final response with text parts**, so a turn ending in a tool result
  leaves the key untouched. (3.2)
- **An `output_schema` mismatch does not raise to your code.** The key is simply absent and the
  traceback goes to the logs. (3.2)
- **`append_event` ignores a `partial=True` event entirely** — no delta applied, nothing appended. (3.3)
- **A stale session object is a bug waiting for Day 47.** Persistent services raise `StaleSessionError`;
  the in-memory one does not notice. (3.3, 6.1)
- **`{key}` for a missing key raises `KeyError` inside the runtime**, and the exception never reaches
  your loop: the turn simply produces no answer. Use `{key?}` or seed the key. (4.2)
- **A value of `None` templates as an empty string**, and a dictionary templates as its `repr`. (4.1, 4.2)
- **Braces that are not valid state names are left alone**, which is why JSON in an instruction usually
  survives — until a key inside it happens to be an identifier. (4.2)
- **`state_schema` is checked when the event is tracked, not at the assignment.** Your tool cannot catch
  it, and the failing step commits **nothing**, including its valid keys. (5.1)
- **Prefixed keys bypass the schema completely**, so the longest-lived keys are the unchecked ones. (5.2)
- **The schema validates types without converting them.** A declared `int` field will hold `'4521'`.
  (5.2)
- **`session.state["k"] = v` on a fetched session is discarded**, with no event, no error and no record
  that anything was attempted. This is the day's failure lab. (6.1)
- **A test that writes and reads the same session object proves nothing.** Assert through the service.
  (7.1)
- **Secrets never go in state**, and bytes go to artifacts rather than to a key. (7.2)

---

## §8 Verify before you code

Fetched on **2026-09-03**, the day this was written:

- **`adk.dev/sessions/state/`** — confirmed the four-prefix table and what each scope means; that
  values must be **serializable** (strings, numbers, booleans, simple lists and dictionaries, *"avoid
  complex objects, functions, connections"*); the three recommended update methods (`output_key`,
  context objects, `EventActions` + `append_event`); `{key}` templating in instructions with
  `InstructionProvider` as the escape hatch for literal braces; and the anti-pattern in its own words:
  *"Avoid direct modification … outside managed contexts. This bypasses event history, breaks
  persistence, and risks data loss."*
- **The installed `google-adk` 2.7.1**, in `.venv/Lib/site-packages/google/adk/` —
  `sessions/state.py` (the `State` class, its value/delta pair, `StateSchemaError` and the rule that
  keys containing `:` bypass validation), `sessions/base_session_service.py` (`_apply_temp_state`,
  `_trim_temp_delta_state`, `_update_session_state`, the `partial` short-circuit and the documented
  `StaleSessionError`), `sessions/_session_util.py` (`extract_state_delta` splitting by prefix and
  stripping it), `sessions/in_memory_session_service.py` (the three separate stores and `_merge_state`),
  `agents/llm_agent.py` (`output_key` handling), `workflow/_base_node.py` (`state_schema` and its
  inheritance by child nodes) and `utils/instructions_utils.py` (the substitution rules, `{key?}`, and
  `_is_valid_state_name`). **Every behavioural claim in this day was run on this machine against this
  version**, not read.

If your `google-adk` is not 2.7.1, run `scopes.py`, `declared.py` and `braces.py` before trusting a
number in this day — and if any of them disagrees, that is a Principle 14 moment: amend first, then
write.

---

## §9 Say it in an interview

"Our agent kept forgetting things between turns, and the fix was not memory in the fancy sense — it was
using session state properly. Three things bit us. First, the prefix on a key is its lifetime, and it
is enforced: no prefix means the conversation, `user:` means that person for ever, and `temp:` is one
turn and is never persisted. We had a preference written without the prefix, so it worked in the
conversation we tested and nowhere else. Second, writes have to go through an event. Assigning to a
session you fetched edits a copy — no exception, no log line, nothing in the history, and the value is
gone next time anybody asks the service. We lost an afternoon to that, and now we have a test that
performs the bad write and asserts it does not stick. Third, and this is the one I would warn anybody
about: three separate mechanisms in that framework fail into a background thread. A state schema
violation, a structured-output mismatch and a missing placeholder in an instruction all produce the
same symptom — a turn that finishes with no answer and nothing raised where you can catch it. The
upside of doing it properly is the thing I did not expect: because every change rides in an event with
an author and a timestamp, the session history is an audit log. When somebody asks why a ticket was
escalated, it is a loop over the events, not an afternoon of reading transcripts."

---

## §10 Done when

See [`CHECKLIST.md`](CHECKLIST.md). Every box ticked, `./m depth 17` green, `./m check` printing
`OK all green`, and — the part no script can check — you can answer the *out loud* question at the end
of each of the eighteen parts without scrolling up.

Not when a number of sittings has passed. When you can name a key's lifetime from its name alone, and
say what happens to a write that produces no event.

---

## §11 Ledger & commit

Paste these **with the values you actually observed** (Principle 7), not the ones printed here.

**`docs/PROGRESS.md`** — append one row:

```text
| 17 | <date> | ADK-19, ADK-20 | 18 | <hash> | ✅ |
```

**`docs/PACKAGES.md`** — **no new rows.** Nothing was installed today; `google-adk` 2.7.1 and its
dependencies carry the whole day.

**`docs/PAPERS.md`** — **no new rows.** Today has no paper: session state is an SDK surface, not an idea
from the literature, and §17.4.2 is explicit that a day does not manufacture a citation it does not
have. The next paper arrives on Day 19, with context engineering.

**`docs/SKILL_PROVENANCE.md`** — no rows. First entries arrive on Day 29.

**`docs/adr/`** — no new ADR is required, and one decision belongs in the commit message: whether the
desk agent sets `state_schema=DeskState` (§4's `TODO(me)`), given that one undeclared key fails the
whole step. **If your ADK version applies the schema at the assignment instead of at the event, or
stops trimming `temp:` keys, stop and re-read Principle 14 before editing anything** — that is a
behaviour change in a pinned dependency, and the plan is amended first.

**Commit message:**

```text
day 17: session state - prefixes, scopes and lifetimes - closes ADK-19, ADK-20
```
