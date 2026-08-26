---
day: 1
phase: 1
phase_name: "Foundations"
title: "Bootstrap & the map"
ids: ["AG-01", "OPS-01", "OPS-02", "OPS-03"]
principles: [1, 2, 4, 5, 7, 9, 10, 13, 14, 15, 16, 17, 18]
kind: lab
plan_version: "v2.2.1"
parts: 14
generated: "2026-08-23"
status: complete
lab_scaffolded: false
commit: "a33938f"
---

# Day 1 — Bootstrap & the map

> **Yesterday (Day 0):** one tool owns the environment, a repository that cannot leak a key by
> accident, and `./m` with two gates.
> **Today:** you can say precisely what makes a system agentic and where Sutra's own boundary sits;
> the repository knows what it is and which document wins; three free keys live behind Day 0's guard
> rail and you have rotated one for real; and completeness becomes something this project *computes*
> rather than feels.
> **Tomorrow (Day 2):** LLM mechanics for agent builders — tokens, context, sampling — and the first
> raw `google-genai` call, using the key you set up today.

---

## §1 Where we are

Every project has a Day 1. This one starts with a scar.

Before a single day of Sutra ran, the original master plan was **lost**. Not corrupted, not
outdated — gone. It had to be rebuilt from the pieces that survived: two addenda, some ledger files,
and a standing-instructions document. The record of that reconstruction is sitting in your repository
right now as `ADR-0001`, and you did not write it.

Imagine planning a long journey, losing the notebook at the airport, and reconstructing the route
from ticket stubs and hotel confirmations. You would arrive. You would also never again keep the only
copy of anything important in one place.

That scar produced the design rule this entire project is built on:

> **The repo is the memory, not the chat.**

Anything that lives only in a conversation window can vanish when the window closes. Anything written
into the repository — day documents, ledgers, decision records — survives any tool, any crash, any
lost session. A stranger, or you in six months, or a different assistant entirely, can open this
folder and know exactly where things stand.

So today you write no agent code. Today you build the four things every later day stands on:

- **An idea, made precise.** What "agentic" actually means — the model decides what happens next,
  rather than the programmer deciding in advance — and, just as importantly, when that is the wrong
  choice. Sutra is a taxi fleet with very good brakes, and today is where you learn where the brakes
  go.
- **A memory system.** What Sutra is, which document wins when two disagree, and your first recorded
  decision.
- **A safety floor.** Three free keys that git cannot see, code that refuses to start without them,
  and a rotation you have rehearsed while it was still free to get wrong.
- **A map that computes.** Ledgers that tell you how much of the plan is genuinely done, derived from
  evidence rather than asserted from memory.

By tonight, Sutra exists as a thing rather than a folder.

---

## §2 The map

Fourteen parts in four sections — **one section per curriculum ID** — and then one paper. Read
them in order; each names its prerequisite.

### Section 1 — `AG-01`: what makes a system agentic
*The framework-independent definition, and the judgement that comes with it.*

| Part | Answers | Level |
| --- | --- | --- |
| [1.1 — Who decides the next step](parts/01-what-is-an-agent/1.1-who-decides-the-next-step.md) | Chatbot, workflow, agent — what is the actual dividing line? | `foundation` |
| [1.2 — Goal, tools, loop, stop condition](parts/01-what-is-an-agent/1.2-goal-tools-loop-stop.md) | What is an agent made of, and which part do beginners forget? | `foundation` |
| [1.3 — When an agent is the wrong answer](parts/01-what-is-an-agent/1.3-when-an-agent-is-the-wrong-answer.md) | What does autonomy cost, and when should you not buy it? | `working` |
| [1.4 — Sutra on the spectrum](parts/01-what-is-an-agent/1.4-sutra-on-the-spectrum.md) | Which parts of Sutra decide for themselves, and which never will? | `production` |

### Section 2 — `OPS-01`: the repo is the memory
*What this project is, how its documents govern each other, and how a decision gets recorded.*

| Part | Answers | Level |
| --- | --- | --- |
| [2.1 — What Sutra actually is](parts/02-repo-as-memory/2.1-what-sutra-actually-is.md) | One system, not ninety-six exercises — why, and what it does | `foundation` |
| [2.2 — The docs tree, and which document wins](parts/02-repo-as-memory/2.2-the-docs-tree-and-precedence.md) | Plan, addenda, ADRs, ledgers — what beats what, and why not just edit the plan? | `working` |
| [2.3 — The ADR that survives a cold read](parts/02-repo-as-memory/2.3-the-adr-that-survives-a-cold-read.md) | How do you record a decision so a stranger can act on it in a year? | `production` |

### Section 3 — `OPS-02`: keys that cannot leak
*Three free doors, an interface that works everywhere, code that fails loudly, and a rehearsed
incident.*

| Part | Answers | Level |
| --- | --- | --- |
| [3.1 — The three free doors](parts/03-keys-and-env/3.1-the-three-free-doors.md) | Gemini, Groq, OpenRouter — what is each one *for*? | `foundation` |
| [3.2 — `.env`, and the environment as an interface](parts/03-keys-and-env/3.2-env-and-the-environment-as-interface.md) | Why does the same code run on a laptop and in a container? | `working` |
| [3.3 — Loading keys, and failing loudly](parts/03-keys-and-env/3.3-loading-keys-failing-loudly.md) | Why check configuration at start-up rather than at first use? | `working` |
| [3.4 — The rotation drill](parts/03-keys-and-env/3.4-the-rotation-drill.md) | **Revoke a real key on purpose** — and find out what breaks | `production` |

### Section 4 — `OPS-03`: completeness you can compute
*Two kinds of ledger, a generator you write, and the shipped one you learn to read.*

| Part | Answers | Level |
| --- | --- | --- |
| [4.1 — The diary and the scoreboard](parts/04-ledgers/4.1-the-diary-and-the-scoreboard.md) | Append-only versus regenerated — and why mixing them loses the truth | `foundation` |
| [4.2 — Build the generator yourself](parts/04-ledgers/4.2-build-the-generator-yourself.md) | Three readers, one writer, forty lines — build first, compare after | `working` |
| [4.3 — Reading the shipped generator](parts/04-ledgers/4.3-reading-the-shipped-generator.md) | Same answer, five times the code — what do the extra lines buy? | `production` |

### The paper — read after the parts

*Where `AG-01` came from, and which half of it the field kept. It lives in this day's `papers/`
directory rather than in `parts/`, because it is where an idea came from and not what the day
teaches.*

| Paper | Answers | Level |
| --- | --- | --- |
| [*Intelligent agents: theory and practice*](papers/01-intelligent-agents.md) | Who decided what "agent" means — and what did they get wrong? | `production` |

**Each section climbs `foundation → working → production`.** Section 3.4 is the deliberate-failure
part the depth contract requires (§17.7): Day 0 attacked the guard rail, and today you rehearse the
response.

**The paper is read last on purpose** (plan §17.4.2). You draw the line in 1.1 and live with its
consequences all day; only then are you shown the survey paper that drew it first, and told which
half of it survived. That is Principle 4 at the scale of a day — build the thing, then read the
proposal.

---

## §3 Setup — run this

**No packages are installed today.** `dependencies` stays `[]` in `pyproject.toml` — packages arrive
on the day they are first used, and the first is `google-genai` on Day 2 (Principle 7).

```bash
# 3.1 — create three free keys in a browser. No card, for any of them.
#   Gemini      aistudio.google.com  -> Get API key   (also: read your project's rate-limit view)
#   Groq        console.groq.com     -> API Keys      (limits are per MODEL and per ORGANIZATION)
#   OpenRouter  openrouter.ai        -> Keys          (model ids MUST end in :free)

# 3.2 — confirm Day 0's guard rail is live BEFORE the secret exists
git check-ignore -v .env

# 3.2 — write .env (see part 3.2 for the full file; do not shorten it)
#   and update .env.example with the same NAMES and no values

# 3.2 — get them into this shell for the curl probes
set -a; . ./.env; set +a

# 4.2 — a scratchpad for your own generator
./m scaffold 1
```

**Verified live on 2026-08-23** (Principle 8 — looked up, not remembered):

| Provider | What the page says today |
| --- | --- |
| Gemini | Free-tier numbers are **not published**; they are per *project* and read from your AI Studio dashboard. Documented stable Flash-class ids: `gemini-3.7-flash`, `gemini-3.6-flash`, `gemini-3.5-flash`, `gemini-2.5-flash`. Flash-Lite: `gemini-3.5-flash-lite`, `gemini-3.1-flash-lite`, `gemini-2.5-flash-lite`. |
| Groq | 30 RPM; RPD and TPM **vary per model**; limits are **per organization**. 429 carries `retry-after` plus `x-ratelimit-remaining-requests` / `-tokens`. |
| OpenRouter | 20 RPM; **50 RPD** on the free floor, 1000 RPD once ≥$10 of credit has ever been purchased. |

**No model is pinned today** — Day 1 makes no model call. Day 5 pins one explicitly (ADK-73), after
looking up the free list on that day.

---

## §4 Build brief

| File | Written in | What it is |
| --- | --- | --- |
| `.env` | [3.2](parts/03-keys-and-env/3.2-env-and-the-environment-as-interface.md) | Three real keys + `GOOGLE_GENAI_USE_VERTEXAI=FALSE`. **Never committed.** |
| `.env.example` | [3.2](parts/03-keys-and-env/3.2-env-and-the-environment-as-interface.md) | The same names, no values. **Always committed.** |
| `sutra/config.py` | [3.3](parts/03-keys-and-env/3.3-loading-keys-failing-loudly.md) | Sutra's first product code: `load_env`, `require`, `describe`, `ConfigError` |
| `docs/adr/ADR-0005-provider-roles.md` | [2.3](parts/02-repo-as-memory/2.3-the-adr-that-survives-a-cold-read.md) | One named role per provider — the hypothesis Day 9 tests |
| `days/day-01-bootstrap-and-map/lab/trace_mine.py` | [4.2](parts/04-ledgers/4.2-build-the-generator-yourself.md) | Your own traceability generator. Scratchpad; gitignored. |
| `tests/test_config.py` | §5 below | The first test in this repository |
| `docs/PROGRESS.md` row | [4.1](parts/04-ledgers/4.1-the-diary-and-the-scoreboard.md) | Day 1's diary entry, appended |

**`TODO(me)` — the reps this day leaves you:**

- `TODO(me)` Write `sutra/config.py` yourself from part 3.3. Do not paste it in one go — the
  `setdefault` line and the `describe()` function each exist for a reason you should be able to
  state.
- `TODO(me)` Fill in ADR-0005's **Context** table with the limits *you* observed today, not the ones
  in part 3.1. Then put a real number in *What would make us change our minds*.
- `TODO(me)` Type `trace_mine.py` rather than copying it, and get the same `closed/total` as the
  shipped script.
- `TODO(me)` Write `tests/test_config.py`. The hub gives you the first test; **the second and third
  are yours** — see below.
- `TODO(me)` Do the rotation drill for real (part 3.4). Write down how long it took and how many
  places the key had to reach.
- `TODO(me)` Cold-read ADR-0005 **tomorrow**, sign the last line, and change its status to
  `accepted`. Not today — the gap is the point.

---

## §5 The eval that must be able to fail

The first real test in this repository. `pytest` arrived as a dev dependency on Day 0; this is the
day it stops reporting `no tests ran`.

```python
# tests/test_config.py
import os

import pytest

from sutra.config import ConfigError, describe, load_env, require


def test_require_raises_when_missing():
    """A missing variable must fail loudly, naming itself."""
    os.environ.pop("SUTRA_TEST_ABSENT", None)
    with pytest.raises(ConfigError, match="SUTRA_TEST_ABSENT"):
        require("SUTRA_TEST_ABSENT")


def test_describe_never_leaks_the_value():
    """describe() reports presence and length, never the secret itself."""
    os.environ["SUTRA_TEST_SECRET"] = "hunter2-not-a-real-key"
    out = describe("SUTRA_TEST_SECRET")
    assert "hunter2" not in out
    assert "22 chars" in out


def test_load_env_does_not_overwrite_the_real_environment(tmp_path):
    """A real environment variable always wins over .env. TODO(me): why?"""
    os.environ["SUTRA_TEST_WINS"] = "from-the-real-environment"
    env = tmp_path / ".env"
    env.write_text("SUTRA_TEST_WINS=from-the-file\n", encoding="utf-8")
    load_env(env)
    assert os.environ["SUTRA_TEST_WINS"] == "from-the-real-environment"
```

**Make it go RED first**, which is the only way to know a test can fail:

```bash
uv run python -m pytest tests/test_config.py -q     # RED: sutra/config.py does not exist yet
# ... write sutra/config.py from part 3.3 ...
uv run python -m pytest tests/test_config.py -q     # GREEN: 3 passed
```

Then break it on purpose: change `setdefault` to `os.environ[key] = value` in `load_env` and watch
the third test fail. **That is the production hazard from part 3.3, caught by a test** — put it back.

`TODO(me)` Add a fourth test: `require` must reject a variable set to whitespace. If it passes
without you changing `config.py`, work out why.

---

## §6 Request budget

| Provider | Calls today | Notes |
| --- | --- | --- |
| Gemini | **0** | The key is created and verified; no `generateContent` call is made. Day 2 makes the first. |
| Groq | **~3** | `GET /openai/v1/models` — the rotation drill's before/after probes. **Not** model inference. |
| OpenRouter | **~1** | `GET /api/v1/models` — public, no key required. |
| Ollama | **0** | — |
| **Model inference calls** | **0** | **Cost: $0.** |

The handful of requests above are **metadata endpoints**, not inference. They do not consume the
model quotas in §3's table, which is worth noticing: *"how many requests did that cost?"* and
*"how much quota did that cost?"* are different questions, and Day 24 (OPS-07, AG-11) is where the
distinction becomes a budget.

---

## §7 Traps

- **Creating `.env` before checking the ignore rule.** Run `git check-ignore -v .env` **first**. If
  it prints nothing, stop — Day 0's rule is missing and you are one `git add -A` from the incident.
- **An unquoted heredoc eating your key.** `cat > .env <<EOF` without quotes expands `$` — a key
  containing `$X` is silently truncated, and the resulting 400 blames the provider. Use `<<'EOF'`
  ([3.2](parts/03-keys-and-env/3.2-env-and-the-environment-as-interface.md)).
- **Quoting values in `.env`.** `GOOGLE_API_KEY="AIza..."` sends the quotes as part of the key.
- **A file is not an environment.** The key is in `.env` and `$GOOGLE_API_KEY` is empty until
  something loads it. The most common five minutes lost tomorrow.
- **Sourcing in a subshell.** `bash -c '. ./.env'` sets variables in a child that then exits. Use
  `. ./.env` in the current shell.
- **`setdefault` surprising you after rotation.** A shell that already exported the old key keeps
  it — the loader deliberately will not overwrite. `unset`, or open a fresh shell
  ([3.4](parts/03-keys-and-env/3.4-the-rotation-drill.md)).
- **The missing `:free` suffix.** `deepseek/deepseek-r1` is a paid model; `deepseek/deepseek-r1:free`
  is not. No warning, no error — this is the one trap today that costs money. Linted from Day 31.
- **`>` instead of `>>` on a ledger.** One character between appending a row and destroying the
  file. Recover with `git checkout docs/PROGRESS.md`.
- **Editing a generated ledger.** `TRACEABILITY.md`, `TRACKER.md` and `CURRICULUM_INDEX.md` are
  rewritten by `./m check`. Your edit will vanish; fix the source instead.

**No 1.x → 2.x ADK trap applies today** — no ADK code is written. The first is Day 5 (explicit model
pinning, ADK-73); the event-model trap is Day 7. But note that
[3.3](parts/03-keys-and-env/3.3-loading-keys-failing-loudly.md)'s "raise, don't swallow" is the same instinct as
trap #4 (*don't swallow exceptions*), which lands properly on Day 21.

---

## §8 Verify before you code

Fetched live on **2026-08-23** while writing this day. Re-check on yours — Principle 7 says look it
up, never remember it.

| What | Where | Why today |
| --- | --- | --- |
| Gemini rate limits | `ai.google.dev/gemini-api/docs/rate-limits` | Confirms the numbers are **per project**, not published — read your own dashboard |
| Gemini model ids | `ai.google.dev/gemini-api/docs/models` | The stable Flash-class roster, for Day 2 and Day 5 |
| Groq rate limits | `console.groq.com/docs/rate-limits` | 30 RPM, per-model RPD/TPM, per-organization, and the 429 headers |
| OpenRouter limits | `openrouter.ai/docs/api-reference/limits` | 20 RPM / 50 RPD free floor, and the `:free` suffix rule |
| `.gitignore` syntax | `git-scm.com/docs/gitignore` | The `!` negation that rescues `.env.example` |

**Not checked today, deliberately:** anything on `adk.dev`. Day 1 writes no ADK code, and Principle 8
says the page is checked *on the day the symbol is used* — Day 5 is the first.

---

## §9 Say it in an interview

> "The first thing I settled was what 'agentic' actually means in our system, because the word gets
> used for three different things. An agent is where the model decides what happens next, rather
> than the programmer deciding in advance — and that buys you the ability to handle inputs you
> didn't anticipate, at the cost of predictability, testability and a bounded call count. So I drew
> the boundary per stage rather than for the whole system: intake and the classifier are fixed, the
> Researcher is genuinely agentic with read-only tools and a call cap, the Writer–Critic loop caps
> at three rounds, and nothing reaches a customer without a human. Then I made the operational side
> match: three free providers with one named role each so a rate limit on one doesn't stop the desk,
> keys read from the environment with a start-up check that refuses to run rather than failing forty
> minutes in, and traceability that's *computed* from the plan, the day documents and the progress
> ledger — so 'is this done' is a derivation from evidence rather than a feeling. I also revoked a
> live key on purpose on day one, to find out what breaks before it mattered."

---

## §10 Done when

Not when you have read all fourteen parts. **When every box in [`CHECKLIST.md`](CHECKLIST.md) is
honestly ticked and `./m check` is green.**

There is no time estimate in this day and there never will be (Principle 17). Day 1 might take you
one evening or four; both are the day done properly.

```bash
./m done 1
```

---

## §11 Ledger & commit

Paste these before running `./m done 1`. **Use the values you actually observed**, not the ones
printed here (Principle 7).

**`docs/PROGRESS.md`** — append one row:

```text
| 1 | 2026-08-23 | AG-01, OPS-01, OPS-02, OPS-03 | 14 | <hash> | ✅ |
```

**`docs/PACKAGES.md`** — **no rows today.** Day 1 installs nothing; `dependencies` stays `[]`. The
first row is Day 2's `google-genai`. *(Recording that a day added nothing is itself worth knowing —
it is why the ledger has no gaps.)*

**`docs/SKILL_PROVENANCE.md`** — no rows. First entries arrive on Day 29 (SK-12..SK-16).

**`docs/adr/ADR-0005-provider-roles.md`** — created today with `Status: proposed`. Change it to
`accepted` **tomorrow**, after the cold read.

**Commit message:**

```text
day 01: bootstrap & the map — closes AG-01, OPS-01, OPS-02, OPS-03
```
