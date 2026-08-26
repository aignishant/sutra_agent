---
day: 2
phase: 1
phase_name: "Foundations"
title: "LLM mechanics for agent builders"
ids: ["AG-02"]
principles: [1, 2, 4, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18]
kind: lab
plan_version: "v2.2.1"
parts: 16
generated: "2026-08-24"
status: written
lab_scaffolded: false
commit: ""
---

# Day 2 — LLM mechanics for agent builders

> **Yesterday (Day 1):** the repository learned what it is — ledgers that regenerate, keys that
> cannot leak, a traceability score this project can compute, and three free doors you proved you
> could open.
> **Today:** Sutra speaks to a model for the first time, and you learn the three mechanical facts
> every agent ever built stands on — text is metered in tokens, the model forgets you between calls,
> and the last step is a weighted dice roll — each one **observed on your own screen**, not read
> about.
> **Tomorrow (Day 3):** the think→act→observe loop, hand-rolled in plain Python with no framework —
> built directly on the history list you construct today.

---

## §1 Where we are

Yesterday you built a repository that remembers things. Today you meet the thing that does not.

Imagine hiring a consultant who has read almost everything ever written. Brilliant, fast, endlessly
patient. Three things about the arrangement are unusual, and every one of them will shape the next
ninety-four days.

They charge **by the chunk of text** — for every chunk you say and every chunk they say back. They
have **total amnesia**: the moment a meeting ends they forget you existed, and walking back in ten
seconds later makes you a stranger. And before they answer, they quietly **weigh several good
phrasings and pick one**, with a little randomness you are allowed to adjust.

Every chat product you have ever used appears to remember your conversation. Given the amnesia, how?
There is a clerk outside the room who walks in before every meeting carrying the entire conversation
so far, reads it aloud, and stands back. That is the whole trick. **The memory is a filing cabinet in
the hallway, maintained by somebody else.**

Today you become that clerk. Not as a metaphor — the folder is a Python list, and you will build it,
watch the model forget without it, and watch the model remember with it.

Then two things that only appear once you look at the receipt. The first is that a modern model
**thinks before it answers**, generating reasoning tokens you pay for and never see — often more than
the visible answer. The second is what happens when you try to keep answers short by capping the
output: the reasoning eats the budget first, and you get a **successful call containing nothing at
all**. That one is section 5, and you should run it rather than read it.

One decision was made before this day was written, and it is recorded in
`docs/adr/ADR-0006-interactions-api-first.md`. Google's quickstart now leads with the **Interactions
API**, and the older `generate_content` pages have been retitled "Legacy" — so that is the surface
this project teaches. But every tutorial you will ever open uses the older one, so section 6 parks it
as awareness: you learn to *read* it without building on it.

---

## §2 The map

Sixteen parts in six sections, then three papers. The day climbs `foundation → working →
production`, ends with a deliberate failure and a parked door, and only then shows you where the
ideas came from.

### Section 1 — `01-first-contact`: from zero packages to one answered call

What a model request actually is, and everything needed to make one honestly.

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [The call that forgets you](parts/01-first-contact/1.1-the-call-that-forgets-you.md) | What *is* one model request, and why does every chat product only appear to remember? | `foundation` |
| 1.2 | [Pinning before installing](parts/01-first-contact/1.2-pinning-before-installing.md) | Why does the version go in the command, and what does `PACKAGES.md` record that `uv.lock` does not? | `working` |
| 1.3 | [Listed is not callable](parts/01-first-contact/1.3-listed-is-not-callable.md) | The docs list it, `models.list()` shows it — so why does calling it 404? | `working` |
| 1.4 | [The first interaction](parts/01-first-contact/1.4-the-first-interaction.md) | What comes back from a call, and which half does everyone throw away? | `working` |
| 1.5 | [The only door: 429 handling that listens](parts/01-first-contact/1.5-the-only-door-429.md) | Why is textbook exponential backoff *worse* than not retrying, and what must happen when you run out of tries? | `production` |

### Section 2 — `02-tokens-the-meter`: text is metered, and quota is the currency

The unit everything is counted in, and the part of the bill you cannot see.

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [What a token is](parts/02-tokens-the-meter/2.1-what-a-token-is.md) | Why is nothing counted in words, and why does a twenty-turn chat cost far more than twenty turns? | `foundation` |
| 2.2 | [Reading the receipt](parts/02-tokens-the-meter/2.2-reading-the-receipt.md) | What does `interaction.usage` actually contain, and why can it not be reconstructed later? | `working` |
| 2.3 | [The thinking tax](parts/02-tokens-the-meter/2.3-the-thinking-tax.md) | Why is the bill several times the visible text, and which setting do you change first? | `production` |

### Section 3 — `03-context-and-memory`: the desk, and who sweeps it

Where "memory" actually lives, and the decision about who owns it.

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [The desk that gets wiped](parts/03-context-and-memory/3.1-the-desk-that-gets-wiped.md) | What is a context window, and why is a bigger one not simply better? | `foundation` |
| 3.2 | [History is a list you own](parts/03-context-and-memory/3.2-history-is-a-list-you-own.md) | How do you make an amnesiac remember, and why do the role labels matter? | `working` |
| 3.3 | [The server will remember for you](parts/03-context-and-memory/3.3-the-server-will-remember.md) | The provider offers to hold your conversation — what exactly do you give up by accepting? | `production` |

### Section 4 — `04-sampling-the-dial`: how one token gets picked

Why the same prompt gives different answers, and which dial fixes which problem.

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [The probability list nobody shows you](parts/04-sampling-the-dial/4.1-the-probability-list.md) | If the model outputs scores rather than words, who picks the word? | `foundation` |
| 4.2 | [Turning the dial](parts/04-sampling-the-dial/4.2-turning-the-dial.md) | Temperature, `top_p`, `top_k` — different mechanisms or different amounts of the same thing? | `working` |
| 4.3 | [Stability is not reproducibility](parts/04-sampling-the-dial/4.3-stability-is-not-reproducibility.md) | Temperature is 0 — so why did the test that passed for weeks just fail? | `production` |

### Section 5 — `05-the-failure-lab`: the deliberate failure

Today's failure, run on purpose (plan §17.7).

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [💥 The cap that ate the answer](parts/05-the-failure-lab/5.1-the-cap-that-ate-the-answer.md) | Why does a small `max_output_tokens` return a *successful* call with nothing in it? | `production` |

### Section 6 — `06-the-legacy-door`: 🅿️ parked, for reading not building

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 6.1 | [🅿️ `generate_content`, the legacy door](parts/06-the-legacy-door/6.1-generate-content-parked.md) | Every tutorial uses the other surface — how do you read them, and what connects this to Day 5? | `production` |

### The papers — read after the parts

*Three of today's ideas are not this project's inventions, and each traces to one document. They
live in this day's `papers/` directory rather than in `parts/`, because where an idea came from is a
different errand from what the day teaches. Read them **last**: "what survived and what did not"
only means something once you have built the thing.*

| Paper | What it answers | Level |
| --- | --- | --- |
| [*Neural Machine Translation of Rare Words with Subword Units*](papers/01-subword-units.md) | Why is your bill counted in fragments instead of words? | `production` |
| [*Chain-of-Thought Prompting Elicits Reasoning in Large Language Models*](papers/02-chain-of-thought-prompting.md) | Why does the model reason before answering — and bill you for it? | `production` |
| [*The Curious Case of Neural Text Degeneration*](papers/03-neural-text-degeneration.md) | Why does `top_p` exist, and why is it not just another temperature? | `production` |

---

## §3 Setup — run this

Look the version up **before** you install it (Principle 7). This document observed `google-genai`
**2.19.0** on **2026-08-24**; use what your own lookup prints.

```bash
# 1 — look it up live
curl -s https://pypi.org/pypi/google-genai/json \
  | python -c "import sys,json; d=json.load(sys.stdin); print(d['info']['version'], d['info']['requires_python'])"

# 2 — pin exactly what you just read
uv add google-genai==2.19.0

# 3 — verify what actually landed
uv pip show google-genai | head -3
uv run python -c "import google.genai; print('import ok')"

# 4 — a scratchpad for your own experiments
mkdir -p days/day-02-llm-mechanics/lab
```

Nothing else is installed today. No HTTP library, no retry library, no `python-dotenv` — the `.env`
loader is the one **you wrote on Day 1**, and the retry logic you write yourself in part 1.5.

Then open your AI Studio rate-limit view and **write your own RPM and RPD down**. There is no public
table to copy: the rate-limits page directs you to your project's own numbers, and Day 24's budgets
are built on them.

---

## §4 Build brief

One new module. Every `TODO(me)` stays unsolved — this project does not do your reps.

**`sutra/mechanics.py`** — importable with **no side effects**, demos run only via
`uv run python -m sutra.mechanics <name>`:

| Symbol | What it does | Taught in |
| --- | --- | --- |
| `MODEL` | The explicit model pin — never a floating alias | 1.3 |
| `_retry_wait(error, attempt)` | The server's stated delay, else exponential fallback | 1.5 |
| `ask(client, prompt, *, config, store)` | **The only door.** Every model call in Sutra goes through it | 1.5 |
| `demo_ask` | One prompt, one answer, and the receipt | 1.4 |
| `demo_tokens` | Estimate first, then measure | 2.2 |
| `demo_thinking` | The same question at two thinking levels | 2.3 |
| `demo_memory` | Amnesia, then the cure — **carries a `TODO(me)`** | 3.2 |
| `demo_server_state` | The arrangement Sutra declines | 3.3 |
| `demo_sampling` | Two temperatures, three runs each | 4.2 |
| `demo_capped` | 💥 the failure lab | 5.1 |
| `main()` | Dispatch by name; exit non-zero on bad usage | 1.4 |

**`tests/test_mechanics.py`** — offline only. Not one model call; see §5.

**`TODO(me)` markers left for you:**

- **3.2** — add the model's own turn to the `history` list. The exact shape is not printed for you;
  read it off a real object with the lookup command in that part.
- **§5** — the fourth test, described below.

---

## §5 The eval that must be able to fail

`_retry_wait` is a **pure function**: an error and an attempt number in, a float out. No network, no
sleeping, no quota. That is exactly what makes the day's most important logic testable for free.

```python
# tests/test_mechanics.py
import pytest
from google.genai import errors
from google.genai._gaos.lib import compat_errors

from sutra.mechanics import _retry_wait


class FakeError(Exception):
    """Stands in for an APIError carrying a server-stated delay."""

    def __init__(self, body: str) -> None:
        self.body = body

    def __str__(self) -> str:
        return self.body


def test_prefers_the_server_stated_delay() -> None:
    assert _retry_wait(FakeError("{'retryDelay': '47s'}"), 0) == 48.0


def test_falls_back_to_exponential_when_silent() -> None:
    assert _retry_wait(FakeError("no delay in this body"), 2) == 4.0


def test_decimal_delays_are_parsed() -> None:
    assert _retry_wait(FakeError("{'retryDelay': '36.5s'}"), 0) == 37.5


def test_reads_the_interactions_surfaces_own_phrasing() -> None:
    """The spelling your own key actually sends (ADR-0007)."""
    body = "Please retry in 52.320368558s."
    assert _retry_wait(FakeError(body), 0) == 53.320368558


def test_the_interactions_error_hierarchy_is_where_we_think() -> None:
    """Pins the private import `ask` depends on, so an SDK move fails here first."""
    assert compat_errors.RateLimitError.status_code == 429
    assert not issubclass(compat_errors.RateLimitError, errors.APIError)


# TODO(me): a sixth test. `ask` must RAISE on a non-429 error rather than
# returning anything at all (Principle 10, and 1.x->2.x trap #4). Write it
# with a fake client whose .interactions.create raises a 401 --- and assert it
# was called ONCE, because a 401 will be just as invalid next time.
```

**How to watch it go RED before it goes green:**

```bash
uv run python -m pytest tests/test_mechanics.py -q     # RED: no sutra/mechanics.py yet
# ... write sutra/mechanics.py from parts 1.4 and 1.5 ...
uv run python -m pytest tests/test_mechanics.py -q     # green
```

Then break it on purpose: delete the `+ 1.0` margin from `_retry_wait` and watch the first test fail
with `48.0 != 47.0`. Put it back. **A test you have never seen fail is a test you do not know
works.**

---

## §6 Request budget

**The first day that spends quota.** Every call is free-tier Gemini; no other provider is touched.

| Demo | Model calls |
| --- | --- |
| `ask` | 1 |
| `tokens` | 1 |
| `thinking` | 2 |
| `memory` | 3 |
| `server` | 2 |
| `sampling` | 6 |
| `capped` | 2 |
| Model reachability probe (1.3) | 1 |
| **Total** | **~18** |

`models.list()` is **metadata, not inference** — it costs no token quota, and knowing that
distinction is a checklist box.

**Your limits are not in this document.** Free-tier numbers are shown per project in AI Studio, not
in a public table, and they are **per project rather than per key** — a second key doubles nothing.
Requests-per-day quotas reset at midnight Pacific.

**Run the demos one at a time.** `sampling` alone is six calls and will trip a per-minute ceiling on
a tight free tier — which is worth seeing once, because you get to watch part 1.5's wrapper read the
server's stated delay and wait it out honestly.

**Cost: $0.** Principle 15 — quota is the currency, denominated in RPM/RPD, not dollars.

---

## §7 Traps

- **The 429 trap.** Textbook 1→2→4-second backoff is *worse* than not retrying against a per-minute
  limit — all three retries land inside the window that is already closed. Read the delay from the
  body: `Please retry in 52.3s` on this surface, `retryDelay: '47s'` on the legacy one. (1.5)
- **The error hierarchy trap — the one that cost this day an amendment.** `interactions.create`
  raises from `google.genai._gaos.lib.compat_errors`, **not** `google.genai.errors`, and the two are
  unrelated: `issubclass(compat_errors.RateLimitError, errors.APIError)` is `False`. A door written
  as `except errors.APIError` catches nothing and every 429 escapes unretried. The status attribute
  is `.status_code`, not `.code`. See `docs/adr/ADR-0007-interactions-error-hierarchy.md`. (1.5)
- **1.x → 2.x trap #4 — don't swallow exceptions.** ADK 1.x habit was catching model errors and
  returning them as strings. 2.x surfaces them through the runtime so callbacks and plugins can act.
  `ask` re-raises rather than returning a placeholder — and today's `TODO(me)` test enforces it. (1.5)
- **`store` defaults to `True`.** The straightforward call persists your conversation on Google's
  servers — free tier retains one day. Sutra sets `store=False` and opts in deliberately. (1.4, 3.3)
- **Listed ≠ callable.** Docs, pricing and `models.list()` describe the vendor's catalogue, not your
  key's permissions. Only a live call proves access. `gemini-2.5-flash` shuts down **2026-10-16**.
  (1.3)
- **Never a floating alias.** ADK's own docs use `gemini-flash-latest`. That is a moving target that
  invalidates evals and quota arithmetic with no commit in your history. Pin explicitly. (1.3)
- **`output_text` can be `None` on a *successful* call.** Guard every `.strip()`, and read the
  finish reason rather than substituting an empty string. (1.4, 5.1)
- **`max_output_tokens` caps thinking *plus* output** on Gemini 3 — contrary to the documentation,
  per [python-genai#2062](https://github.com/googleapis/python-genai/issues/2062). A small cap returns
  a successful call with nothing in it. (5.1)
- **Two names for the same field.** `total_thought_tokens` on Interactions,
  `thoughts_token_count` on the legacy surface. Copying between tutorials produces an
  `AttributeError`. (2.2, 6.1)
- **`load_env()` before `genai.Client()`.** The client reads the key at construction; a loader called
  afterwards is called too late. (1.3)
- **`python -m sutra.mechanics`, never `python sutra/mechanics.py`.** The second gives
  `ModuleNotFoundError: No module named 'sutra'`. (1.4)

---

## §8 Verify before you code

Every page below was fetched on **2026-08-24** while this day was written. Principle 8: re-fetch on
the day you use them — this list is evidence, not a substitute.

| Source | What it settled |
| --- | --- |
| `pypi.org/pypi/google-genai/json` | **2.19.0**, uploaded 2026-08-19, requires Python `>=3.10` |
| `pypi.org/pypi/google-adk/json` | **2.7.1**, uploaded 2026-08-17 — the plan's §5 baseline of 2.6.3 has moved. Day 5 re-verifies |
| `ai.google.dev/gemini-api/docs/quickstart` | The current sample is `client.interactions.create(...)` → `interaction.output_text`; usage via `interaction.usage` |
| `ai.google.dev/gemini-api/docs/models` | Flash roster now lists `gemini-3.7-flash`, `gemini-3.6-flash` above `gemini-3.5-flash` |
| `ai.google.dev/gemini-api/docs/interactions` | Runs on the free tier; `store=True` is the default; retention **1 day free / 55 paid**; `previous_interaction_id` continues a conversation |
| `ai.google.dev/gemini-api/docs/rate-limits` | No public free-tier table — limits are in AI Studio, **per project not per key**; RPD resets midnight Pacific |
| `ai.google.dev/gemini-api/docs/thinking` | Thinking **on by default** on Flash; controlled by `thinking_level`, and **the levels are per-model** — `gemini-3.7-flash` takes `low`/`medium`/`high`, default `medium`; `minimal` is offered by `gemini-3.6-flash` and `gemini-3.5-flash-lite`, and 400s here (re-checked 2026-08-25); usage field `total_thought_tokens` |
| `googleapis.github.io/python-genai` | `models.generate_content` still documented in full, **no deprecation notice**; `interactions.create` documented alongside it |
| [`python-genai#2062`](https://github.com/googleapis/python-genai/issues/2062) | `max_output_tokens` caps thinking **+** output combined on Gemini 3 — contrary to the docs. This is part 5.1 |
| `adk.dev/agents/models/google-gemini/` | ADK 2.x reaches this surface via `Gemini(model=..., use_interactions_api=True)`; ADK docs use the alias `gemini-flash-latest` |

**Read off the installed package and one live response on 2026-08-25**, when the lab was built — the
day this file was written, these were claims; here they became observations (Principle 8, and the
reason for `ADR-0007`):

| Source | What it settled |
| --- | --- |
| `.venv/…/google/genai/_gaos/lib/compat_errors.py` | Interactions raises `GeminiNextGenAPIClientError → APIError → APIStatusError → RateLimitError(429)`. **Not** a subclass of `google.genai.errors.APIError`; the status attribute is `.status_code` |
| A live 429 from `gemini-3.7-flash` | The body says `Please retry in 52.320368558s.` with **no** `retryDelay` field, and states this key's own limit: **20** on `generate_content_free_tier_requests` |
| `.venv/…/_gaos/types/interactions/{userinputstep,modeloutputstep,textcontent}.py` | A history turn is `{"type": "user_input" \| "model_output", "content": [{"type": "text", "text": …}]}` — the shape part 3.2's `TODO(me)` sends you to find |
| `.venv/…/_gaos/types/interactions/generationconfig.py` | `temperature` and `top_p` are **not** typed fields in 2.19.0, but `GenerationConfig` is `extra: "allow"`, so both still reach the wire |
| `client.models.list()` on this key | `gemini-3.7-flash` is listed **and** callable — the live call in 1.3, not the listing, is what proved it |

**No ADK symbol is used today** — ADK is not installed until Day 5, and packages arrive on the day
they are used. The ADK rows above are forward references for part 6.1, verified rather than
remembered.

---

## §9 Say it in an interview

> "The first thing I actually built against an LLM wasn't an agent — it was a wrapper around one
> call, because I wanted to understand what I was paying for. Three things surprised me. The model is
> genuinely amnesiac: I told it my favourite colour, asked in the next call, and it had no idea — the
> 'memory' in every chat product is the application re-sending the transcript, which is also why a
> twenty-turn conversation costs far more than twenty times one turn. Second, the receipt didn't
> match the visible text: on a thinking model I was billed a few hundred reasoning tokens for a
> twelve-token answer, so any cost estimate built from prompt-plus-answer length is wrong in a
> direction that always surprises you. Third — and this is the one I'd tell anyone starting — I
> capped `max_output_tokens` at sixteen to keep answers short and got successful calls with nothing
> in them. The reasoning had spent the entire budget before a single visible word. A token cap is a
> guillotine, not a brevity instruction. I also learned to read the server's own `retryDelay` instead
> of using textbook 1-2-4-second backoff, because against a per-minute limit those three retries all
> land inside the window that's already closed and just quadruple the load."

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked — honestly. `./m done 2` refuses to commit
while any box is unticked, and it cannot tell whether you were truthful. That part is yours.

The day is finished when you can **explain every number your own terminal printed**: the four fields
on the receipt, why call 2 of the memory demo did not know the colour, why the capped run returned
`None`, and what your free-tier RPM actually is.

---

## §11 Ledger & commit

Paste these **with the values you actually observed** (Principle 7), not the ones printed here.

**`docs/PROGRESS.md`** — append one row:

```text
| 2 | 2026-08-24 | AG-02 | 16 | <hash> | ✅ |
```

**`docs/PACKAGES.md`** — append two rows:

```text
| google-genai | 2.19.0 | 2026-08-24 | 2 | Raw Gemini SDK — Sutra's first model calls. Looked up on PyPI before pinning (uploaded 2026-08-19, requires Python >=3.10). ADK arrives Day 5. |
| gemini-3.7-flash (model) | free tier; limit 20 on generate_content_free_tier_requests (read off a live 429, not a table) | 2026-08-24 | 2 | Primary brain. Repinned from gemini-3.5-flash per CHANGELOG_PLAN.md 2026-08-24; the model Google's own current quickstart uses. Verified callable by live call, not by listing. |
```

**`docs/SKILL_PROVENANCE.md`** — no rows. First entries arrive on Day 29.

**`docs/adr/ADR-0006-interactions-api-first.md`** — written **before** this day, per Principle 14.
Cold-read and sign it tomorrow, not today.

**`docs/adr/ADR-0007-interactions-error-hierarchy.md`** — written **during** this day, because
building the lab disproved something the day claimed: `ask` caught an error class this surface never
raises. Principle 14 says amend first, then code, and that is the order it happened in — the ADR and
the `CHANGELOG_PLAN.md` entry dated 2026-08-25 came before the corrected `sutra/mechanics.py`. Cold-read
this one tomorrow too.

**Commit message:**

```text
day 02: LLM mechanics for agent builders — closes AG-02
```
