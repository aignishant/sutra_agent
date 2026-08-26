---
day: 5
phase: 1
phase_name: "Foundations"
title: "First ADK agent — the runner takes the loop"
ids: ["ADK-01", "ADK-02", "ADK-73"]
principles: [1, 2, 4, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
kind: lab
plan_version: "v2.2.1"
parts: 16
generated: "2026-08-25"
status: written
lab_scaffolded: false
commit: ""
---

# Day 5 — First ADK agent: the runner takes the loop

> **Yesterday (Day 4):** you replaced a hand-written text protocol with the provider's own function
> calling, deleted your parser, and then spent two sections being precise about what a schema does *not*
> buy — a validated argument is not a correct one, and no schema knows who is asking.
> **Today:** a framework takes the loop. You install `google-adk`, describe the agent as a
> configuration, pin its model explicitly, hand the whole thing to a runner, and then answer — against
> somebody else's code — the seven questions you wrote before you installed anything.
> **Tomorrow (Day 6):** instructions and personas, and the `adk web` dev UI you park today.
> Reach it as `adk web sutra/desk` — §7's last trap is why.

---

## §1 Where we are

You have built the same agent twice, and today somebody else's code runs it.

Think about a kitchen that used to make its own stock. Every morning, somebody stood there skimming a
pot for two hours. Then the restaurant started buying it in — better stock, from a supplier who does
nothing else, cheaper than the morning it replaced. Nothing is lost. The food improves.

Until the supplier changes something, the sauces start breaking, and nobody in that kitchen has made
stock in a year.

The restaurant that survives is not the one that refused to buy it in. It is the one where somebody
still makes it occasionally, and where the person who signed the contract could tell you exactly which
morning's work they were handing over.

That is today. You are handing over seven things you wrote yourself, and the only question that matters
about the framework taking them is **which of your intervention points it hands back** — the place a
human approves an action, the place you count what a run costs, the place you edit a conversation that
has grown too long. You wrote the loop, so you can write that list. Most people evaluating a framework
cannot.

There is also a trap in here with a curriculum number on it, and it is the quietest one this project
will meet for weeks: an agent that does not say which model it uses will be given one, and that
one changes when the framework does.

---

## §2 The map

Sixteen parts, seven sections. The day climbs `foundation → working → production`, spends a whole
section comparing what you built against what you adopted, and ends with a deliberate failure and a
parked pair of tools.

### Section 1 — `01-installing-adk`: the framework arrives

What a framework takes, what version you pinned, and the layout it expects.

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [What a framework takes from you](parts/01-installing-adk/1.1-what-a-framework-takes.md) | What does it add (nothing) and what does it take (the inside of seven things)? | `foundation` |
| 1.2 | [Pinning the framework](parts/01-installing-adk/1.2-pinning-the-framework.md) | The plan says 2.6.3 and PyPI says otherwise — is that a contradiction? | `working` |
| 1.3 | [The layout ADK expects](parts/01-installing-adk/1.3-the-layout-adk-expects.md) | Four conventions Sutra adopts and one it refuses — which, and why? | `working` |

### Section 2 — `02-the-agent-object`: an agent is a description

What an `LlmAgent` actually is, and which of its fields have runtime behaviour attached.

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [An agent is a configuration](parts/02-the-agent-object/2.1-an-agent-is-a-configuration.md) | What does constructing one cost, and where did your `history` list go? | `foundation` |
| 2.2 | [Name and description are not decoration](parts/02-the-agent-object/2.2-name-and-description.md) | One is an address and one is an advertisement — which fails silently? | `working` |
| 2.3 | [The instruction is your system prompt](parts/02-the-agent-object/2.3-the-instruction-is-your-system-prompt.md) | It moves across unchanged — so what exactly did you lose? | `working` |

### Section 3 — `03-the-model-pin`: ADK-73, and the two ways to not choose

The day's named trap, and the two neighbouring ways to end up on a model you did not pick.

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [The default that moved under you](parts/03-the-model-pin/3.1-the-default-that-moved.md) | Why does an agent with no `model=` make your evals uninterpretable? | `production` |
| 3.2 | [A floating alias is not a pin](parts/03-the-model-pin/3.2-a-floating-alias-is-not-a-pin.md) | Why is `-latest` *worse* than specifying nothing at all? | `production` |
| 3.3 | [Two doors to Gemini](parts/03-the-model-pin/3.3-two-doors-to-gemini.md) | One environment variable decides whether you are billed — and `.env` cannot enforce it | `production` |

### Section 4 — `04-the-runner`: handing over the loop

The object that replaces `run_loop`, the service that replaces `history`, and the habit that replaces
copying from tutorials.

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [The runner is your run_loop](parts/04-the-runner/4.1-the-runner-is-your-run-loop.md) | What three things does a runner need, and why does it yield events? | `working` |
| 4.2 | [Sessions and the transcript](parts/04-the-runner/4.2-sessions-and-the-transcript.md) | Who holds the conversation now, and what may you still do to it? | `working` |
| 4.3 | [Read the signature, not the tutorial](parts/04-the-runner/4.3-read-the-signature-not-the-tutorial.md) | Two questions `inspect` answers that decide how you call anything | `working` |

### Section 5 — `05-the-comparison`: the Principle 4 cash-in

Build first, compare after. This is the "after".

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [The seam list, checked](parts/05-the-comparison/5.1-the-seam-list-checked.md) | Seven questions, seven answers or dates — which row is decisive? | `production` |
| 5.2 | [What you handed over](parts/05-the-comparison/5.2-what-you-handed-over.md) | Three protocols in three days — what survived all of them? | `production` |

### Section 6 — `06-failure-lab`: the deliberate failure

Today's failure, run on a day you chose (plan §17.7).

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 6.1 | [💥 The agent with no model](parts/06-failure-lab/6.1-the-agent-with-no-model.md) | You ran the unpinned agent and both answers were fine — why is that the finding? | `production` |

### Section 7 — `07-the-dev-ui`: 🅿️ parked, for reading not building

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 7.1 | [🅿️ `adk run` and `adk web`](parts/07-the-dev-ui/7.1-adk-run-and-adk-web.md) | Two commands run today's agent with no code — so why did you write `run_once.py`, and why does one of the two refuse? | `production` |

---

## §3 Setup — the framework arrives today

Look the version up **before** you install it (Principle 7). This document observed `google-adk`
**2.7.1** on **2026-08-25** — uploaded 2026-08-17, requires Python `>=3.10`. Plan §5's baseline is
2.6.3 and §5 itself says to re-verify on install day; part 1.2 is about why that is not a
contradiction.

```bash
# 1 - look it up live
curl -s https://pypi.org/pypi/google-adk/json | python -c "
import sys, json; d = json.load(sys.stdin); i = d['info']
print(i['version'], i['requires_python'], d['releases'][i['version']][0]['upload_time'])"

# 2 - pin exactly what you just read
uv add google-adk==2.7.1

# 3 - three sources must agree
uv pip show google-adk | head -3
uv run python -c "import google.adk; print(google.adk.__version__)"

# 4 - the agent folder, by ADK's convention (part 1.3)
mkdir -p sutra/desk
touch sutra/desk/__init__.py sutra/desk/agent.py sutra/desk/run_once.py sutra/desk/multi_turn.py
touch tests/test_desk.py

# 5 - a scratchpad, and the seam list you write BEFORE reading any ADK docs (part 1.1)
mkdir -p days/day-05-first-adk-agent/lab
touch days/day-05-first-adk-agent/lab/seams.md

# 6 - the gate, before you write anything
./m check
```

**One line in `.env`, and no second `.env` anywhere** (parts 1.3 and 3.3):

```text
GOOGLE_GENAI_USE_VERTEXAI=FALSE
```

Then `git check-ignore -v .env sutra/desk/.env` — the first must report a rule, the second must print
nothing, because that file must not exist.

**Step 5 is not optional and its order matters.** Write the seven seam questions from part 1.1 into
`lab/seams.md` before you read ADK's documentation. A list written afterwards is a list shaped by what
you found.

---

## §4 Build brief

Two modules under a new package, one function added to Day 1's config, and a test file. **Nothing in
`sutra/loop.py` or `sutra/agent.py` changes today** — Days 3 and 4 stay as written, as the fallback lane
(Day 9) and as the comparison part 5.2 rests on.

**`sutra/desk/agent.py`** — the agent, discovered by convention:

| Symbol | What it does | Taught in |
| --- | --- | --- |
| `INSTRUCTION` | Day 4's `SYSTEM`, moved **verbatim** | 2.3 |
| `root_agent` | `LlmAgent` with `name`, `model`, `description`, `instruction` | 1.3, 2.1, 2.2 |

**`sutra/desk/run_once.py`** — one question through the runner, so the runner is visible:

| Symbol | What it does | Taught in |
| --- | --- | --- |
| `APP_NAME`, `USER_ID` | the session address, minus the session id | 4.2 |
| `ask_with(agent, question)` | build a runner + session, consume events, return the final text | 4.1, 6.1 |
| `ask_once(question)` | `ask_with(root_agent, ...)` | 4.1 |
| `main()` | `load_env` → `require_free_tier` → `asyncio.run` | 3.3, 4.1 |

**`sutra/desk/multi_turn.py`** — the memory demo, through the framework (4.2).

**`sutra/config.py`** — one new function: `require_free_tier()` (3.3).

**`tests/test_desk.py`** — offline only. See §5.

**`days/day-05-first-adk-agent/lab/`** — `seams.md` (1.1, 5.1) and `unpinned.py` (6.1). **Experiments
live here, never in `sutra/`.**

**`TODO(me)` markers left for you:**

- **4.1** — the exact keywords for `Runner(...)`, `run_async(...)` and `create_session(...)`. This
  document could **not** verify them against a live adk.dev page, so it prints the `inspect` command
  instead of guessing. Part 4.3 is why that is the right answer rather than a gap.
- **§5** — the fourth test, described below.
- **6.1** — record the substituted model string and your ADK version in `lab/seams.md`.

---

## §5 The eval that must be able to fail

Three structural tests you can write today for **zero tokens**, plus one you write yourself. Structural
assertions about an agent are cheap because constructing one costs nothing (2.1), and they hold whatever
the model does.

```python
# tests/test_desk.py
import pathlib

from sutra.desk.agent import root_agent


def test_the_agent_pins_its_model() -> None:
    """ADK-73: an agent without an explicit model silently follows ADK's default."""
    assert root_agent.model, "no model pinned - ADK's default would apply"
    assert not root_agent.model.endswith(("-latest", "-preview", "-exp")), (
        f"{root_agent.model!r} is a pointer, not a model id (ADK-73, Addendum 02)"
    )


def test_no_agent_in_sutra_is_unpinned() -> None:
    """The failure lab lives in lab/; sutra/ never constructs an unpinned agent."""
    for path in pathlib.Path("sutra").rglob("*.py"):
        source = path.read_text(encoding="utf-8")
        if "LlmAgent(" in source:
            assert "model=" in source, f"{path} constructs an agent without model="


def test_the_tools_know_nothing_about_the_framework() -> None:
    """Sutra's tools are plain functions. Days 3, 4 and 5 all agree on this."""
    source = pathlib.Path("sutra/loop.py").read_text(encoding="utf-8")
    assert "google.adk" not in source, "framework types have leaked into the tool layer"
    assert "google.genai" not in source, "SDK types have leaked into the tool layer"


# TODO(me): a fourth test. `require_free_tier()` must RAISE when
# GOOGLE_GENAI_USE_VERTEXAI is set to anything but FALSE, and must be quiet when
# it is absent. Use monkeypatch.setenv / delenv - no network, no key, and it is
# the only guard standing between this project and a billing account.
```

**How to watch it go RED before it goes green:**

```bash
uv run python -m pytest tests/test_desk.py -q     # RED: no sutra/desk/agent.py yet
# ... write sutra/desk/agent.py from parts 1.3 -> 2.3 ...
uv run python -m pytest tests/test_desk.py -q     # green
```

Then break each one and watch it fail:

- Remove `model=` from `root_agent` and watch the first test go red — that is ADK-73, caught offline.
- Change it to `gemini-flash-latest` and watch the *second* assertion of the same test fire. Note that
  a truthiness check alone would have passed it (3.2).
- Add `from google.adk.agents import LlmAgent` to the top of `sutra/loop.py` and watch the third go red.
  **Nothing else in the project would have told you** that the boundary had moved (5.2).

---

## §6 Request budget

**Free-tier Gemini only**, through the AI Studio door — and part 3.3 is the check that keeps it that
way.

| What | Model calls |
| --- | --- |
| proving the pin is callable (3.2) | 1 |
| 4.1 check yourself | 1 |
| the multi-turn memory demo (4.2) | 3 |
| 💥 the failure lab: pinned vs unpinned (6.1) | ~4 |
| 6.1's deliberate 404 | 1 |
| three ways to run the same agent (7.1) | ~2 |
| `adk web sutra/desk`, a couple of messages | ~2 |
| **Total** | **~14** |

**Less than either of the last two days**, and the reason is worth noticing: almost everything today is
structural — signatures, constructed objects, source assertions — and none of it costs a token. Sections
1, 2, 3 and 5 are almost entirely free.

`models.list()` (3.2) is **metadata, not inference**, and costs no token quota.

**Your limits are not in this document.** Free-tier numbers are per project, in AI Studio, and RPD
resets at midnight Pacific.

**Cost: $0** — and today is the day that becomes a check rather than an intention (3.3).

---

## §7 Traps

- **ADK-73 — the default model.** An agent with no `model=` uses ADK's own default, which changed in a
  minor release. Your eval scores move with nothing in `git log` to explain it. **Every agent pins its
  model explicitly.** (3.1, 6.1)
- **A floating alias is worse than no model at all.** `gemini-flash-latest` is a pointer, and it
  **passes code review** because it looks like a decision. ADK's own examples use one. (3.2)
- **`GOOGLE_GENAI_USE_VERTEXAI` can be set outside your repository**, and Day 1's loader lets a real
  environment variable beat `.env` — correctly. Writing `FALSE` in `.env` is intent, not enforcement.
  Assert it. (3.3)
- **No second `.env`.** ADK suggests one per agent folder; Sutra keeps one, at the root. Two files
  holding one secret is two paths to protect. `git check-ignore -v` before you believe anything. (1.3)
- **`root_agent`, `agent.py`, `__init__.py`** — the convention is a contract. A differently-named
  variable is invisible however correct it is. (1.3)
- **1.x → 2.x trap #1.** Workflow-agent classes were replaced by the graph Workflow Runtime; a 1.x
  import raises `ImportError`. That is the **kind** version. (1.2)
- **1.x → 2.x traps #2 and #3.** Event field names changed, and custom agents **yield** rather than
  append. Both produce code that imports cleanly and behaves differently. Never copy event handling from
  a 1.x tutorial; print the signature. (4.3, and Day 7 in earnest)
- **`create_session` is awaited and `run_async` is an async generator.** Get either wrong and you get
  `coroutine was never awaited` or `'async_generator' object is not iterable`. `inspect` answers both
  before you write the loop. (4.1, 4.3)
- **`InMemorySessionService` dies with the process.** Multi-turn works inside one run and not across
  two `run_once` invocations. That is what the name says. (4.2)
- **`USER_ID = "local"` is a constant**, and would be a cross-user leak behind an HTTP handler. Note it
  now; Day 8 fixes it. (4.2)
- **Import-time work.** The convention forces `load_env()` and `require_free_tier()` to run at import, so
  importing `sutra.desk.agent` is not free — and anything that imports it inherits its requirements.
  (1.3, 3.3)
- **The agent is shared; the session is per-conversation.** Never attach per-conversation state to an
  agent object. (2.1)
- **💥 `adk run sutra/desk` refuses in this repository, and nothing you wrote is wrong.** `adk run`
  splits the path into a parent folder and a name, and ADK treats **any folder containing a file called
  `agent.py`** as an agent — so Day 4's `sutra/agent.py` makes `sutra/` itself the agent and `desk`
  unreachable: `Agent not found: 'desk'. In single agent mode, only 'sutra' is accessible.` Use
  `adk web sutra/desk`, which takes the same path without splitting it. **Adopting a convention rewrites
  the meaning of files you already have.** (7.1, and the `google-adk` row in `docs/PACKAGES.md`)
- **Bare `adk web` offers `docs`, `legacy` and `tests` as agents**, because with no path every
  subdirectory of the root is a candidate. Discovery answers "what could be an agent?"; only a
  manifest answers "what is one?" Always pass the folder. (7.1, 1.3)

---

## §8 Verify before you code

Every page below was fetched on **2026-08-25** while this day was written. Principle 8: re-fetch on the
day you use them — this list is evidence, not a substitute.

| Source | What it settled |
| --- | --- |
| `pypi.org/pypi/google-adk/json` | **2.7.1**, uploaded 2026-08-17, requires Python `>=3.10`. Plan §5's baseline of 2.6.3 has moved, exactly as §5 said to check for |
| `adk.dev/agents/llm-agents/` | `from google.adk.agents import LlmAgent`; `Agent` is an alias; parameters `name` (required), `model` (required), `description`, `instruction`, `tools`, `output_key`, `output_schema`, `input_schema`, `generate_content_config`, `include_contents`, `planner`. **"If you do not specify a model … it falls back to ADK's built-in default model"**, plus `LlmAgent.set_default_model(...)` — this is ADK-73 |
| `adk.dev/get-started/python/` | The folder convention: a folder with `agent.py` defining `root_agent`, `__init__.py`, and a `.env`; `adk run <folder>` and `adk web --port 8000`; install via `pip install google-adk` |
| `adk.dev/agents/models/google-gemini/` | Model given as a string or an object; the examples use the **floating alias** `gemini-flash-latest`; `use_interactions_api=True` exists as an opt-in and does not mix custom function tools with built-in tools |
| `adk.dev/sessions/session/` | `from google.adk.sessions import InMemorySessionService, Session`; `create_session` is **awaited**, takes `app_name`, `user_id` and optional `state`, and returns a session carrying `id`, `state`, `events`, `last_update_time`; `delete_session(app_name, user_id, session_id)` |
| `adk.dev/runtime/` and `/runtime/event-loop/` | The Runner ↔ execution-logic event loop: the agent **yields** events, the runner processes and forwards them (1.x → 2.x trap #3). **No verbatim `Runner` constructor or `run_async` code was obtainable from these pages**, which is why part 4.1 carries a `TODO(me)` with an `inspect` command instead of a guess (Principle 8) |

**The one thing this day could not verify from a page**, and therefore does not assert:

```bash
uv run python -c "
import inspect
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
print(inspect.signature(Runner.__init__))
print(inspect.signature(Runner.run_async))
print(inspect.signature(InMemorySessionService.create_session))
"
```

Run it, and if the keywords disagree with part 4.1's code, **your signature wins** and you fix the code.
That is Principle 8 working rather than failing.

---

## §9 Say it in an interview

> "I built the loop by hand twice before I touched a framework, and the payoff arrived on the day I
> adopted one. Before installing anything I wrote down seven places my own loop had a seam — where the
> step limit was, where I counted tokens, where I could read or edit the conversation, the one line that
> executes a tool, where I'd redact a result before storing it, where the model call happens, and where
> the trace comes from. Then evaluating the framework was answering those seven questions rather than
> comparing ergonomics, and the honest output was two answers and five dates. The one that decides
> everything is whether there's a hook between the model proposing a tool call and my code running it,
> because every safety requirement attaches there. The other thing I'd mention is a trap that cost
> somebody else weeks: the framework has a built-in default model, and it changed in a minor release —
> so agents that don't specify a model silently swap underneath you and your eval scores move with
> nothing in git to attribute it to. I pin the model on every agent and record it with every run, and I
> treat a `-latest` style tag as unpinned, because that one passes code review while a missing model at
> least looks like an omission."

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked — honestly. `./m done 5` refuses to commit while
any box is unticked, and it cannot tell whether you were truthful. That part is yours.

The day is finished when `uv run adk web sutra/desk` answers a question — and when you have typed
`uv run adk run sutra/desk`, read its refusal, and can name the file that causes it (7.1); when
`run_once.py` answers the same question through a runner you wrote; when the multi-turn demo remembers within a session and forgets across
two; when `lab/seams.md` has seven rows each carrying an answer or a day number; when you have watched
an unpinned agent produce a perfectly good answer from a model you did not choose; and when
`sutra/loop.py` and `sutra/agent.py` are **unchanged**.

---

## §11 Ledger & commit

Paste these **with the values you actually observed** (Principle 7), not the ones printed here.

**`docs/PROGRESS.md`** — append one row:

```text
| 5 | <date> | ADK-01, ADK-02, ADK-73 | 16 | <hash> | ✅ |
```

**`docs/PACKAGES.md`** — append one row:

```text
| google-adk | 2.7.1 | <date> | 5 | The agent framework. Plan §5's baseline was 2.6.3 (observed 2026-08-12); §5 instructs re-verification on install day and this is it - a dated observation superseding a dated observation, not a Principle 14 amendment. Uploaded 2026-08-17, requires Python >=3.10. |
```

**`docs/SKILL_PROVENANCE.md`** — no rows. First entries arrive on Day 29.

**`docs/adr/`** — no new ADR. The version difference is what plan §5 already prescribes (part 1.2), and
today makes no decision the plan has not already made. **If your own lookup finds a major version rather
than a patch, stop and re-read Principle 14 before writing any code.**

**Commit message:**

```text
day 05: first ADK agent - the runner takes the loop - closes ADK-01, ADK-02, ADK-73
```
