---
day: 6
phase: 1
phase_name: "Foundations"
title: "Instructions & personas — the string the framework did not take"
ids: ["ADK-03", "AG-05"]
principles: [1, 2, 4, 8, 10, 11, 12, 13, 15, 16, 17, 18]
kind: lab
plan_version: "v2.2.1"
parts: 19
generated: "2026-08-26"
status: written
lab_scaffolded: false
commit: ""
---

# Day 6 — Instructions & personas: the string the framework did not take

> **Yesterday (Day 5):** a framework took the loop. You described the agent as a configuration, pinned
> its model against ADK-73, handed the whole thing to a runner, and answered your seven seam questions
> against somebody else's code.
> **Today:** you write the one thing ADK did not take. The instruction stops being a placeholder and
> becomes a handbook with six sections, each of which you can probe. Then you learn the mechanics
> underneath it — three fields, a template engine, and a dev UI that shows you the request instead of
> only the answer.
> **Tomorrow (Day 7):** events and streaming, the 2.x event model, and two of the four framework traps.
> You will have already seen the objects in `adk web`.

---

## §1 Where we are

Yesterday you handed over seven things. Today you find out that the thing you kept decides more of the
behaviour than any of them.

Think about a bus route. The transport company provides everything: the bus, the driver, the fuel, the
depot, the schedule, the ticket machine. All of it is real engineering and none of it is yours.

Somebody, once, sat with a map and decided where the bus stops. Which corner, which market, whether it
goes past the hospital or one street behind it. That decision is not visible anywhere on the bus. You
cannot photograph it. And it is the entire difference between a route people use and a route that runs
empty, because it is the only part that knows anything about the neighbourhood.

The instruction is the list of stops. ADK gave you the runner, the session service, the event stream
and the model plumbing. It did not and could not give you the decisions about what this particular
agent refuses, what it admits it cannot see, and what it says when somebody asks for something outside
its remit. That string is the smallest artifact in the repository and the one with the most behaviour
attached, and it is usually the only one with no test, no owner and no review requirement.

Today it gets all three.

There is also a bug sitting in Sutra right now, put there by an honest carry-across on Day 5, and it is
today's failure lab. The instruction tells the agent to search a knowledge base. The agent has no
tools. What a cooperative model does with that instruction is the mechanism behind most reports of the
word "hallucination", and you are going to watch it happen and then switch it off.

---

## §2 The map

Nineteen parts in six sections, plus one paper. The day climbs `foundation → working → production`:
section 1 is the craft of writing an instruction, section 2 is how you check one, sections 3 and 4 are
the ADK mechanics underneath, section 5 is the instrument that makes any of it observable, and section
6 is the deliberate failure.

### Section 1 — `01-writing-the-handbook`: what goes in and what stays out

AG-05, the framework-independent half. What an instruction is for, the six sections it needs, and the
three things that must never be in one.

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [An instruction is a handbook, not a wish](parts/01-writing-the-handbook/1.1-handbook-not-a-wish.md) | What is the one test that decides whether a line belongs? | `foundation` |
| 1.2 | [The six sections a handbook needs](parts/01-writing-the-handbook/1.2-six-sections-of-a-handbook.md) | Six headings, six failures — which two do people skip? | `working` |
| 1.3 | [Protocol does not belong in prose](parts/01-writing-the-handbook/1.3-protocol-does-not-belong-in-prose.md) | Day 4 deleted your parser; what stops you writing it back into the prompt? | `working` |
| 1.4 | [Contradictions are randomised behaviour](parts/01-writing-the-handbook/1.4-contradictions-are-randomised-behaviour.md) | Two rules, one input — why is the result a coin toss rather than a compromise? | `production` |
| 1.5 | [Every line is a tax](parts/01-writing-the-handbook/1.5-every-line-is-a-tax.md) | Why is an untestable line not merely useless but permanent? | `production` |

### Section 2 — `02-testing-a-persona`: a persona is tested, not admired

The other half of AG-05. A probe, the three that gate any change, and the bridge to Phase 12.

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [A line you cannot probe](parts/02-testing-a-persona/2.1-a-line-you-cannot-probe.md) | Three conditions a probe must meet — which one do most attempts fail? | `working` |
| 2.2 | [The three probes every persona owes](parts/02-testing-a-persona/2.2-the-three-probes.md) | Scope, honesty, happy path — which failure does nobody find out about? | `working` |
| 2.3 | [When probes become an evalset](parts/02-testing-a-persona/2.3-when-probes-become-an-evalset.md) | Why judge by hand first, when the automatic version is obviously better? | `production` |

### Section 3 — `03-the-instruction-fields`: ADK-03, the mechanics

Where your string actually goes, and the three other fields that can change the answer.

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [Where your instruction lands](parts/03-the-instruction-fields/3.1-where-your-instruction-lands.md) | What are the three things that happen to your string before the model sees it? | `working` |
| 3.2 | [Two fields, two readers](parts/03-the-instruction-fields/3.2-two-fields-two-readers.md) | One failure is visible and one is silence — which is which? | `working` |
| 3.3 | [The static instruction that moves yours](parts/03-the-instruction-fields/3.3-the-static-instruction-that-moves-yours.md) | A field added for caching demotes your handbook — how, and why does nothing warn you? | `production` |
| 3.4 | [The deprecated global instruction](parts/03-the-instruction-fields/3.4-the-deprecated-global-instruction.md) | Set it on the wrong agent and it does nothing, silently — which agent is the right one? | `production` |

### Section 4 — `04-state-templating`: the handbook is a form

The instruction is not a constant. Curly braces are live, and the question mark is a design decision.

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [The instruction is a template, not a string](parts/04-state-templating/4.1-the-instruction-is-a-template.md) | What decides whether `{something}` is a blank or ordinary text? | `working` |
| 4.2 | [Hard and soft contracts](parts/04-state-templating/4.2-hard-and-soft-contracts.md) | Why is "make everything optional" the wrong lesson from an outage? | `production` |
| 4.3 | [A callable turns templating off](parts/04-state-templating/4.3-a-callable-turns-templating-off.md) | One refactor removes a feature and its safety check at once — which one? | `production` |

### Section 5 — `05-the-dev-ui`: ADK-03, the glass engine

The tool Day 5 parked. What it shows you, how to read a turn, and what it exposes.

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [The glass engine — `adk web`](parts/05-the-dev-ui/5.1-the-glass-engine.md) | Which panels show you something you could not see yesterday? | `working` |
| 5.2 | [Reading a turn's anatomy](parts/05-the-dev-ui/5.2-reading-a-turns-anatomy.md) | Three questions, in a fixed order — why does the first one come first? | `working` |
| 5.3 | [An unauthenticated server on your machine](parts/05-the-dev-ui/5.3-an-unauthenticated-server.md) | What is the only thing containing it, and what one flag removes it? | `production` |

### Section 6 — `06-failure-lab`: the deliberate failure

Today's failure is live in Sutra right now, and it has an off switch (plan §17.7).

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 6.1 | [💥 The handbook that promised equipment](parts/06-failure-lab/6.1-the-handbook-that-promised-equipment.md) | Why is "hallucination" the wrong word for what you are about to watch? | `production` |

### Papers — read **after** the parts

Principle 4 at the scale of a day: write the handbook by hand, watch a model follow one too well, and
only then read the proposal that made any of it possible.

| # | Paper | What it settles |
| --- | --- | --- |
| 01 | [Training language models to follow instructions with human feedback](papers/01-instructgpt.md) — `arXiv:2203.02155` | Instruction following is a **trained behaviour, not a property of scale** — and the cooperativeness that makes your handbook work is the same one that fills a gap when it is wrong |

---

## §3 Setup — run this

**No new packages today.** Day 5's `google-adk` 2.7.1 carries the whole day, and nothing here installs
anything. If your `uv pip show google-adk` disagrees with 2.7.1, that is a fact worth writing down
before you start — several parts paste output observed on that exact version.

```bash
# 1 - confirm where you are starting from
uv run python -m pytest -q -m "not live"
uv run python scripts/trace.py

# 2 - the lab scratchpad for today
mkdir -p days/day-06-instructions-and-personas/lab/papers/instructgpt
touch days/day-06-instructions-and-personas/lab/{show_instruction.py,collision.py,weigh.py}
touch days/day-06-instructions-and-personas/lab/{probes.py,run_probes.py,two_readers.py}
touch days/day-06-instructions-and-personas/lab/{static_instruction.py,global_instruction.py}
touch days/day-06-instructions-and-personas/lab/{templating.py,contracts.py,provider.py}
touch days/day-06-instructions-and-personas/lab/promised_equipment.py

# 3 - the one new test file
touch tests/test_persona.py

# 4 - the gate, before you change anything
./m check
```

**Write `lab/show_instruction.py` first, before anything else.** It is part 1.1's script, it is used by
eight of the nineteen parts, and it costs nothing to run. Everything today is easier once you can see
what the model is actually given.

**`sutra/desk/agent.py` is the only file under `sutra/` you touch today**, and only its `INSTRUCTION`
and `description`. No new modules, no new dependencies, no changes to `sutra/loop.py` or
`sutra/agent.py`.

---

## §4 Build brief

**`sutra/desk/agent.py`** — the handbook replaces the placeholder:

| Symbol | What changes | Taught in |
| --- | --- | --- |
| `INSTRUCTION` | four carried-over sentences → six named sections | 1.2, and 6.1 for why the old one was a bug |
| `description` | one line → the four questions, third person, including what it is **not** for | 3.2 |
| `root_agent` | unchanged apart from those two fields | — |

**`tests/test_persona.py`** — the zero-token structural suite (2.3), plus one `live`-marked behavioural
case. See §5.

**`days/day-06-instructions-and-personas/lab/`** — eleven small scripts, each given whole in the part
that needs it. They are experiments and they stay in `lab/`; nothing under `sutra/` imports any of
them, and `lab/show_instruction.py` in particular borrows a private ADK name that no product code may
touch (3.1).

**`lab/papers/instructgpt/`** — the paper demo, two files, given complete in the paper part. Pure
standard library, no model call.

**`TODO(me)` markers left for you:**

- **2.3** — the fourth structural test: assert the Tone section states its length budget **numerically**.
  Watch it go red by rewriting the budget as "keep it brief", then make it green again.
- **6.1** — paste **both** arms of the failure lab's output, verbatim, from your own run. This document
  deliberately prints neither; a fabricated transcript inside a part about fabrication would be the
  exact failure it teaches.
- **1.4** — decide, and write down, whether Sutra's tone budget needs a precedence clause for data-loss
  tickets. There is a right answer for Sutra and this document does not give it to you.
- **5.2** — the two-request state experiment: add `{focus?}`, look at the rendered instruction in the
  event, set `focus` in the State panel, look again. Then remove it or keep it **as a decision**.

---

## §5 The eval that must be able to fail

Three structural tests you can write for **zero tokens**, plus the `TODO(me)` fourth, plus one
behavioural case quarantined behind the `live` marker. Structural assertions about a prompt are cheap
because reading a string costs nothing, and they catch the exact regression that caused today's failure
lab.

```python
# tests/test_persona.py
import re

from sutra.desk.agent import INSTRUCTION

REQUIRED_SECTIONS = ["Role", "Scope", "Refusal", "Honesty", "Tone", "Example"]


def test_the_handbook_has_all_six_sections() -> None:
    """1.2: six sections, each closing a named failure. Order is asserted too."""
    found = re.findall(r"^# (.+)$", INSTRUCTION, re.M)
    assert found == REQUIRED_SECTIONS, f"sections are {found}"


def test_the_handbook_promises_no_equipment_the_agent_lacks() -> None:
    """6.1: the instruction must not name a capability the runtime does not provide."""
    from sutra.desk.agent import root_agent

    if not root_agent.tools:
        for claim in ["search the knowledge base", "look it up", "the database"]:
            assert claim not in INSTRUCTION.lower(), f"instruction promises {claim!r}"


def test_no_template_variable_is_unguarded() -> None:
    """4.2: a bare {var} is a hard contract, and nothing today can satisfy one."""
    for var in re.findall(r"{([a-zA-Z_][a-zA-Z0-9_]*)}", INSTRUCTION):
        raise AssertionError(f"{{{var}}} has no '?' and no state to fill it")


# TODO(me): the fourth test - assert the Tone section states its budget numerically.
```

**How to watch each one go RED before it goes green:**

```bash
uv run python -m pytest tests/test_persona.py -q -m "not live"   # RED: handbook not written yet
# ... write the six sections from part 1.2 ...
uv run python -m pytest tests/test_persona.py -q -m "not live"   # green
```

Then break each one on purpose:

- Rename `# Refusal` to `# Boundaries` and watch the first test go red naming what it found (2.3).
- Put `search the knowledge base` back into `INSTRUCTION` and watch the second go red — **the same
  failure the lab spends two requests demonstrating, caught for zero** (6.1).
- Add `{product}` to the Scope section and watch the third go red. Then remove the `?`-less form,
  run `lab/show_instruction.py`, and watch the `KeyError` arrive before any network call (4.1).

---

## §6 Request budget

**Free-tier Gemini only**, 20 requests per day (`docs/PACKAGES.md`, 2026-08-25). This day is unusually
lopsided: almost all of the teaching is free, and the paid part is concentrated in four places.

| What | Model calls |
| --- | --- |
| sections 1.1–1.3, 1.5 · all of section 3 · all of section 4 · 5.3 · the paper demo | **0** |
| 1.4 — the contradiction run, same question three times | 3 |
| 2.2 — the three probes, one at a time | 3 |
| 2.2 — re-running the one that failed, after an edit | ~1 |
| 2.3 — the `live`-marked behavioural test | 1 |
| 5.1 — one message in `adk web` | 1 |
| 5.2 — the state experiment, before and after | 2 |
| 6.1 — the failure lab, both arms | 2 |
| **Total** | **~13** |

**Run the free things first.** That is not frugality, it is sequencing: `lab/show_instruction.py`,
`weigh.py`, `templating.py` and the structural tests all answer "is the handbook what I think it is?",
and a probe sent against a handbook you have not verified is a wasted request.

**If you run out**, the day does not stop. Sections 3 and 4 are entirely free, the paper demo needs no
key at all, and reading events in `adk web` works fine on turns you have already spent. The two parts
that genuinely need quota are 2.2 and 6.1 — do those first tomorrow.

`count_tokens` in `lab/weigh.py` is **metadata, not inference**, and costs no request quota (1.5).

**Cost: $0.**

---

## §7 Traps

- **The instruction promises equipment the agent does not have.** Live in Sutra right now: the string
  says "search the knowledge base" and there is no `tools=` on the agent. A cooperative model closes
  the gap by describing a search it did not run. **This is a specification bug, not a model defect.**
  (6.1, 1.1)
- **"Be accurate and do not guess" does not fix it.** The original string already forbids inventing
  facts, twice. Stating the **absence** is what works: *"You have no ticket database, no knowledge base
  and no search."* (6.1, 1.2)
- **A refusal without a script is a refusal the model writes itself**, differently every time. Forbid
  and supply, never forbid alone. (1.2)
- **An example that disagrees with a rule silently deletes the rule.** Demonstration outranks
  description, and the two sit in different sections so review never sees them together. (1.2)
- **Curly braces in the instruction are live.** `{product}` is a hard template contract and raises
  `KeyError: 'Context variable not found: ...'` at the **first live turn** — not at import, not at
  startup. And doubling the braces does **not** escape them: `{{product}}` substitutes exactly like
  `{product}`. (4.1, 4.2)
- **A JSON example in your prompt usually survives, and that is luck.** `{"priority": "high"}` is left
  alone because it is not a valid identifier; `{priority}` is not. Two quotation marks separate the two
  behaviours. (4.1, 1.3)
- **Passing a callable to `instruction` turns state substitution off entirely** — and turns off the
  `KeyError` that used to protect you. Wrapping a working template in a function to add one conditional
  removes a feature and its safety net in a diff about something else. Call `inject_session_state`
  yourself. (4.3)
- **`static_instruction` is not additive.** Setting it moves your `instruction` out of the system slot
  and re-sends it as a `role="user"` message. It is a behaviour change dressed as a performance change,
  and **setting it alone does not enable caching** — its own docstring says so. (3.3)
- **`global_instruction` is read only from the root agent.** On any other agent it is silently ignored:
  no error, no warning, nothing in the rendered request. It is also deprecated in favour of
  `GlobalInstructionPlugin`, with no `DeprecationWarning` emitted. (3.4)
- **`system_instruction` is appended to, not assigned.** More than one thing can write into it, so
  assert on the **rendered** request rather than on your `INSTRUCTION` constant. (3.1, 3.4)
- **`description` failure is silence.** A badly written one means your agent is never routed to — no
  error, no log line, just work going elsewhere. Write it in third person and include what the agent is
  **not** for. (3.2)
- **`adk web` endpoints are unauthenticated.** The only containment is the default host `127.0.0.1`,
  and `--host 0.0.0.0` removes it. The State panel is a prompt-editing interface for anyone who can
  reach the port. (5.3)
- **`--reload` and `--reload_agents` are different flags.** The first reloads the server; the second is
  what picks up agent changes. Assuming the first covers the second is why your handbook edit "did not
  land". (5.1)
- **`adk web` writes `.adk/session.db` into the agent folder** by default. Real conversations, on disk,
  in a repository that goes public in Phase 14. Day 0's `.gitignore` covers it — verify with
  `git check-ignore -v` rather than assuming. (5.3)
- **The dev UI makes requests feel free.** One message, then go and read its events. Reading costs
  nothing. (5.1)
- **A flaky eval is not noise.** It is either a contradiction in the prompt or an assertion that has
  stopped meaning what it meant. Adding a retry deletes the measurement. (1.4, 2.3)

---

## §8 Verify before you code

Every source below was checked on **2026-08-26** while this day was written. Principle 8: re-check on
the day you use them. This table is evidence, not a substitute.

| Source | What it settled |
| --- | --- |
| `adk.dev/agents/llm-agents/` | `instruction` is "a string (or a function returning a string)"; template syntax `{var}`, `{var?}`, `{artifact.var}`; `description` is "primarily used by *other* LLM agents to determine if they should route a task to this agent"; `global_instruction` is **deprecated** in favour of `GlobalInstructionPlugin`; guidance to "Be Clear and Specific", "Use Markdown", "Provide Examples (Few-Shot)", "Guide Tool Use". **`static_instruction` is not mentioned on this page at all** — everything 3.3 says about it comes from the installed package |
| `adk.dev/runtime/web-interface/` | `adk web`, `http://localhost:8000`, `--port` / `--host` / `--reload`; panels for chat, sessions, state ("View and modify session state during development"), event history; "ADK Web is **not meant for use in production deployments**" |
| `arxiv.org/abs/2203.02155` | Title copied from the record for `docs/PAPERS.md`; the 1.3B-preferred-over-175B result and the "minimal performance regressions" clause quoted in the paper part |
| the installed `google-adk` 2.7.1 | `LlmAgent.instruction` type; `static_instruction`'s docstring and its effect on `instruction`; `global_instruction`'s root-only rule; `inject_session_state`'s identifier rule and its two exceptions; `adk web --help`'s unauthenticated-endpoints notice and `--port` default of 8000 |

**Three claims in this day that no page states**, and that were established by running code rather than
by reading. Re-run them; if your version disagrees, **your terminal wins** and you fix the document:

```bash
uv run python days/day-06-instructions-and-personas/lab/static_instruction.py   # 3.3
uv run python days/day-06-instructions-and-personas/lab/global_instruction.py   # 3.4
uv run python days/day-06-instructions-and-personas/lab/provider.py             # 4.3
```

That is Principle 8 working rather than failing: a field that can relocate your system prompt is real
whether or not a page mentions it, and the way you find out is to print the request.

---

## §9 Say it in an interview

> "The system prompt is the artifact with the most behaviour attached and usually the least process
> around it, so I treat it like code. I write it in six named sections — role, scope, refusal script,
> honesty, tone, one example — and the rule for keeping any line is that I can name the message that
> would answer differently without it. If I can't, it goes, because a line with no probe can never
> safely be deleted, which is why prompt files only ever grow. The two sections people underrate are
> the refusal script and the honesty section: a refusal without a script means the model composes its
> own, differently every time, and the honesty section has to state what the agent *cannot* see rather
> than just telling it to be truthful. That second one is the fix for most of what gets reported as
> hallucination — I had a case where the prompt told the agent to search a knowledge base and there was
> no search tool wired up, so the most cooperative thing available to it was to describe having
> searched. Nobody wrote 'make things up'; somebody wrote a handbook for a better-equipped agent. On
> the framework side, the thing I'd want a team to know is that the instruction isn't a string, it's a
> template rendered against session state before every call, and there are three other fields that can
> change what the model receives — so I assert on the rendered request rather than on the constant in
> my file, and I check it locally before I spend a single call arguing with the model's behaviour."

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked — honestly. `./m done 6` refuses to commit while
any box is unticked, and it cannot tell whether you were truthful. That part is yours.

The day is finished when `sutra/desk/agent.py` carries a six-section handbook that names no capability
the agent lacks; when you have sent all three probes one at a time and written down a verdict for each,
including at least one honest "hedged near-miss"; when you have watched the failure lab's two arms
differ and can say which clause caused it; when `tests/test_persona.py` has gone red and green for each
of its assertions; when you have rendered the instruction locally and read the same instruction inside
a real event in `adk web`; when you can say what `static_instruction`, `global_instruction` and a
callable each do to the request, having run all three; and when `sutra/loop.py`, `sutra/agent.py` and
`sutra/desk/run_once.py` are **unchanged**.

---

## §11 Ledger & commit

Paste these **with the values you actually observed** (Principle 7), not the ones printed here.

**`docs/PROGRESS.md`** — append one row:

```text
| 6 | <date> | ADK-03, AG-05 | 19 (+1 paper) | <hash> | ✅ |
```

**`docs/PACKAGES.md`** — **no new rows.** Nothing was installed today and no new model string was
introduced; Day 5's `google-adk` 2.7.1 and the `gemini-3.7-flash` pin carry the whole day. If your own
lookup finds a different `google-adk`, that is a row — a dated observation superseding a dated
observation.

**`docs/PAPERS.md`** — one row, already added when this day was written. Confirm the identifier
resolves before you trust it:

```text
| Training language models to follow instructions with human feedback | arXiv:2203.02155 | 2022 | 2026-08-26 | 6 | `days/day-06-instructions-and-personas/papers/01-instructgpt.md` |
```

**`docs/SKILL_PROVENANCE.md`** — no rows. First entries arrive on Day 29.

**`docs/adr/`** — no new ADR. Today adopts nothing the plan has not already prescribed, and refuses two
things (`global_instruction`, `static_instruction`) on grounds the parts state in full. **If your ADK
version has removed `global_instruction` entirely rather than deprecating it, stop and re-read
Principle 14 before editing anything** — that is an ecosystem change, and the plan is amended first.

**Commit message:**

```text
day 06: instructions & personas - the string the framework did not take - closes ADK-03, AG-05
```
