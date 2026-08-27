---
day: 9
phase: 2
phase_name: "Models & tools"
title: "Same agent, four free providers — the string that changes everything"
ids: ["ADK-08", "ADK-09"]
principles: [1, 2, 4, 6, 7, 8, 10, 11, 13, 14, 15, 16, 17, 18]
kind: lab
plan_version: "v2.2.1"
parts: 16
generated: "2026-08-27"
status: written
lab_scaffolded: false
commit: ""
---

# Day 9 — Same agent, four free providers: the string that changes everything

> **Yesterday (Day 8):** the conversation got an address. Sessions, runs, the four services
> underneath, and the honest accounting of what "in memory" costs you.
> **Today:** Phase 2 opens. One agent, one handbook, one question — and four different models
> answering it. Gemini natively, Groq and OpenRouter through a translation layer, and one running on
> your own machine with no key and no quota at all. Then the first honest benchmark table of this
> project, and a paper about doing the choosing properly.
> **Tomorrow (Day 10):** function tools in ADK — Day 4's hand-rolled tool calling, handed to
> `FunctionTool`.

---

## §1 Where we are

Think about how electricity reaches a house that has stopped trusting the grid.

There is the mains. Cheap when it is there, and not always there. There is an inverter with a battery,
which runs the fans and the lights but will not run the geyser. There is a diesel generator that will
run anything and costs money every minute it is on. And on the roof, increasingly, there are panels
that produce nothing at night and produce more than you need at two in the afternoon.

Four sources, and here is the thing worth noticing: **the sockets do not change.** The fan does not
know which one it is on. Nobody rewires anything when the mains goes. Somewhere there is a box that
handles the switching, and that box is the whole of the engineering.

But nobody in that house treats the four as interchangeable. Everybody knows the inverter will not
take the geyser. Everybody knows the generator is for emergencies because of what it costs. Somebody
has thought about what happens when the mains goes at 8pm and the battery is already low, and that
thinking is what makes the house comfortable rather than merely wired.

Today you get the four sources and you build the box. The socket is the `model=` argument you have
been passing since Day 5, and it turns out to be a switch. What is behind it can be Google's own
service, an inference company running open-weight models on custom chips, an aggregator in front of
dozens of vendors, or a file on your disk — and the agent, the handbook and the runner do not change
at all.

The part that takes real care is not the wiring. It is knowing what each source will not do. One
lane gives you twenty requests a day and no published limits. One gives you a thousand and tells you
your remaining balance on every single response. One gives you fifty and tells you nothing until it
refuses. And one never refuses, never charges, never leaves the room, and is smaller than the others
in a way that will quietly change your agent's answers.

By the end of the day that is a table with dates on it, and by Day 70 it is a router.

---

## §2 The map

Sixteen parts in seven sections, plus one paper. The day climbs `foundation → working →
production`: section 1 is what the model string really is, section 2 is the translation layer and the
two hosted lanes, section 3 is the local lane, section 4 measures all four honestly, section 5 is
choosing between them, section 6 is what you will never use, and section 7 is a failure that costs
money instead of raising.

### Section 1 — `01-one-model-field`: ADK-09, the string is a switch

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [A name is a lookup](parts/01-one-model-field/1.1-a-name-is-a-lookup.md) | Why does `gemini-9.9-turbo` resolve and a real Llama name not? | `foundation` |
| 1.2 | [The spare tyre you never checked](parts/01-one-model-field/1.2-the-spare-tyre-you-never-checked.md) | Four things stay green with a broken model string — which four, and why is each right? | `working` |

### Section 2 — `02-the-translator`: ADK-09, one adapter and two hosted lanes

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [One charger, many sockets](parts/02-the-translator/2.1-one-charger-many-sockets.md) | What does an adapter translate, and what can it fundamentally not fix? | `foundation` |
| 2.2 | [The toolkit you did not need](parts/02-the-translator/2.2-the-toolkit-you-did-not-need.md) | ADK's error recommends an extra with seventeen packages in it. Take the other suggestion | `working` |
| 2.3 | [The express counter](parts/02-the-translator/2.3-the-express-counter.md) | Which of Groq's two free limits will Sutra hit first, and how would you know before being refused? | `working` |
| 2.4 | [The wholesale market](parts/02-the-translator/2.4-the-wholesale-market.md) | Five characters decide whether a model is free — and the free list moved in fifteen days | `working` |

### Section 3 — `03-local`: ADK-08, the model on your own machine

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [Cooking at home](parts/03-local/3.1-cooking-at-home.md) | Four things this lane does not need, and the two it costs you | `working` |
| 3.2 | [Two switches that look the same](parts/03-local/3.2-two-switches-that-look-the-same.md) | `ollama/` drops your conversation and loops on tools — and neither symptom points at the prefix | `working` |
| 3.3 | [The learner driver](parts/03-local/3.3-the-learner-driver.md) | "The handbook passed its probes" is a claim about two things. Which two? | `production` |

### Section 4 — `04-the-benchmark`: measuring four lanes without lying

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [Two routes to work](parts/04-the-benchmark/4.1-two-routes-to-work.md) | What claim do three samples entitle you to make, and what claim do they not? | `working` |
| 4.2 | [The mileage on the sticker](parts/04-the-benchmark/4.2-the-mileage-on-the-sticker.md) | Six columns, two of which you can fill in without spending a request | `production` |
| 4.3 | [Three shops, three closing times](parts/04-the-benchmark/4.3-three-shops-three-closing-times.md) | Four different jobs hide behind "handle the 429" | `production` |

### Section 5 — `05-routing`: ADK-09, choosing per request

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [Which queue do you join?](parts/05-routing/5.1-which-queue-do-you-join.md) | The documented `RoutedLlm` does not exist in Python — so what does routing look like today? | `production` |
| 5.2 | [🅿️ The dispatcher at the taxi stand](parts/05-routing/5.2-the-dispatcher-at-the-taxi-stand.md) | Four things Day 70's router needs, and why the floor has to be a lane you have probed | `production` |

### Section 6 — `06-parked`: the lanes you will never use

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 6.1 | [🅿️ The spec sheet you can read](parts/06-parked/6.1-the-spec-sheet-you-can-read.md) | Two lines away and permanently out of scope — what are you entitled to claim? | `production` |

### Section 7 — `07-failure-lab`: the deliberate failure

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 7.1 | [💥 The free trial that charges](parts/07-failure-lab/7.1-the-free-trial-that-charges.md) | Six layers accept a billable string. Which one objects, and in what currency? | `production` |

### Papers — read **after** the parts

Principle 4 at the scale of a day: hand-roll a router out of a length check and a regular expression,
*then* read what the field learned about doing it properly.

| # | Paper | What it settles |
| --- | --- | --- |
| 01 | [RouteLLM: Learning to Route LLMs with Preference Data](papers/01-routellm.md) — `arXiv:2406.18665` | Routing is a **prediction about a comparison**, not a judgement about difficulty — and the threshold becomes an operational dial |

---

## §3 Setup — run this

**One new package today**, and you look the version up before you pin it (Principle 7). Everything
else is keys you have had since Day 1 and a program you may need to install.

```bash
# 1 - confirm where you are starting from
./m check

# 2 - see the registry fail on three correct strings, BEFORE the install (1.1)
mkdir -p days/day-09-four-free-providers/lab/papers/routellm
cd days/day-09-four-free-providers/lab
touch resolve.py deferred.py two_forms.py providers.py
touch groq_lane.py groq_headers.py free_list.py openrouter_lane.py
touch local_lane.py ollama_prefixes.py portability.py
touch bench.py BENCHMARK.md refusals.py route.py quota_sketch.py
touch parked_lanes.py billable.py free_lint.py
touch papers/routellm/router.py papers/routellm/run.py
cd -
uv run python days/day-09-four-free-providers/lab/resolve.py

# 3 - look the version up, then pin it (2.2)
curl -s https://pypi.org/pypi/litellm/json | python -c "import sys,json; d=json.load(sys.stdin)['info']; print(d['version'], d['requires_python'])"
uv add "litellm==1.98.0"          # <- use YOUR observed version, not this one

# 4 - the same script again. three lines changed.
uv run python days/day-09-four-free-providers/lab/resolve.py

# 5 - the two keys you have never used
uv run python -c "from sutra.config import load_env, describe; load_env(); print(describe('GROQ_API_KEY')); print(describe('OPENROUTER_API_KEY'))"

# 6 - the local lane, if your machine can take it (3.1)
ollama --version
curl -s http://localhost:11434/api/tags
ollama list

# 7 - the one new module under sutra/ and the one new test file
touch sutra/desk/models.py
touch tests/test_models.py
```

**Run step 2 before step 3.** The before-and-after on `resolve.py` is the clearest thing in the day
and it is gone once the package is installed.

**`describe()` in step 5** is Day 1's function, which reports presence and length and never a value.
Two keys that have been sitting in `.env` for eight days are about to do their first work.

**One file under `sutra/` is new** — `models.py` — and nothing else changes.
`sutra/desk/agent.py` keeps its Gemini pin and its handbook: **today's four lanes are all
experiments**, and the decision to move Sutra's own agent belongs to Day 70.

---

## §4 Build brief

**`sutra/desk/models.py`** — new, and small:

| Symbol | What it does | Taught in |
| --- | --- | --- |
| `DESK_MODEL` | one home for the model string | 1.2 |
| `check(model)` | resolve it at startup, not at the first request | 1.2 |
| `BillableModelError` | its own exception type, so the message names the mistake | 7.1 |
| `free_only(model)` | refuse an `openrouter/` string with no `:free` suffix | 7.1 |

**`days/day-09-four-free-providers/lab/`** — nineteen scripts and one table. Ten of them cost
**zero requests**.

**`lab/BENCHMARK.md`** — the day's real deliverable (4.2). Six columns, a header stating the
conditions, and a `not run:` with a reason in any cell you could not fill.

**`lab/papers/routellm/`** — the paper demo, two files, given complete in the paper part. The routing
arm is deterministic and free; the live arm is twenty Groq requests.

**`tests/test_models.py`** — the structural suite. See §5.

**`TODO(me)` markers left for you:**

- **2.3** — from your Groq headers, work out which of the two limits Sutra's real ticket sizes hit
  first. Day 70 needs the answer.
- **3.1** — choose your local model and record its name, size and whether `ollama show` lists
  **tools**. If you cannot run this lane at all, write the reason down and mark the benchmark row
  `not run:`.
- **3.3** — twelve probe answers, four lanes, three verdicts each: pass, fail, or hedged near-miss.
  Then say which probe survived every lane and which did not.
- **4.2** — fill in `BENCHMARK.md`. Every number is yours; none of them is in this document.
- **5.2** — the sketch sends every classification to the **slowest** lane. Fix the ordering so a
  classification goes to the fast hosted lane while it has headroom.
- **7.1** — the lint flags `lab/billable.py`, correctly. Decide between an explicit allowance with a
  written reason and rewriting the file so the string is assembled. Both are defensible; pick one and
  say why.

---

## §5 The eval that must be able to fail

Every assertion below is free. That is not a coincidence: today's most expensive mistake — a billable
model string — is entirely catchable before any call, which is
[7.1](parts/07-failure-lab/7.1-the-free-trial-that-charges.md)'s whole point.

```python
# tests/test_models.py
import pytest
from google.adk.models import LLMRegistry

from sutra.desk.models import DESK_MODEL, BillableModelError, check, free_only


def test_the_pinned_model_resolves() -> None:
    """1.2: a model string that cannot select a class should stop us at startup."""
    assert check(DESK_MODEL) == DESK_MODEL


def test_a_billable_openrouter_string_is_refused() -> None:
    """7.1: the Day 31 lint, twenty-two days early."""
    with pytest.raises(BillableModelError):
        free_only("openrouter/z-ai/glm-5.2")


def test_a_free_openrouter_string_is_allowed() -> None:
    """7.1: the check must not be so eager that it blocks the correct string."""
    assert free_only("openrouter/z-ai/glm-5.2:free").endswith(":free")


def test_other_providers_are_not_asked_for_a_free_suffix() -> None:
    """7.1: the rule is provider-specific. Groq and Gemini have no such suffix."""
    for model in ("gemini-3.7-flash", "groq/llama-3.3-70b-versatile"):
        assert free_only(model) == model


def test_a_provider_string_without_a_provider_never_resolves() -> None:
    """1.1: the prefix is not decoration - a bare model name is not a model string."""
    with pytest.raises(ValueError):
        LLMRegistry.resolve("llama-3.3-70b-versatile")


# TODO(me): the sixth test - free_only must refuse a billable string built by
# concatenation at runtime, which no text lint can see (7.1).
```

**How to watch each one go RED before it goes green:**

```bash
uv run python -m pytest tests/test_models.py -q -m "not live"   # RED: sutra/desk/models.py is empty
# ... write the four symbols from parts 1.2 and 7.1 ...
uv run python -m pytest tests/test_models.py -q -m "not live"   # green
```

Then break each one on purpose:

- Change `DESK_MODEL` to `"llama-3.3-70b-versatile"` — a **real** model name with no provider — and
  watch the first test go red. That is 1.1's finding as an assertion.
- Delete the `startswith("openrouter/")` guard in `free_only` and watch
  `test_other_providers_are_not_asked_for_a_free_suffix` go red. An over-eager check is a check
  somebody will delete.
- Change `raise` to a `warnings.warn` in `free_only` and watch the second test go red. Then read the
  failure and decide whether you would have caught a warning in a log.
- Change `DESK_MODEL` to `"gemini-9.9-turbo"` — an invented model — and watch **every test pass**.
  That is 1.1's other finding, and the sixth test is not the one that catches it either. Write down
  what would.

---

## §6 Request budget

Four providers, four different currencies. This is the first day whose budget has to be planned per
lane rather than as one number.

| What | Gemini (20/day) | Groq (1000/day) | OpenRouter (50/day) | Ollama |
| --- | --- | --- | --- | --- |
| all of section 1 · 2.1 · 2.2 · `free_list.py` · 5.1 · 5.2 · 6.1 · 7.1 | 0 | 0 | 0 | 0 |
| 2.3 — `groq_lane.py` + `groq_headers.py` | — | 2 | — | — |
| 2.4 — `openrouter_lane.py` | — | — | 1 | — |
| 3.1 / 3.2 — the local lane | — | — | — | free |
| 3.3 — three probes per lane | 3 | 3 | 3 | free |
| 4.1 / 4.2 — warm-up + 3 timed, per lane | 4 | 4 | 4 | free |
| 4.3 — `refusals.py` | — | 1 | 1 | — |
| the paper demo, routing arm | 0 | 0 | 0 | 0 |
| the paper demo, `--live` arm | — | 20 | — | — |
| **Total** | **7 of 20** | **30 of 1000** | **9 of 50** | **0** |

**Read the Gemini column first.** Seven of twenty, and four of those are the benchmark. If you have
already spent quota today, do the Gemini rows tomorrow — everything else in the day is unaffected,
which is itself the argument the day is making.

**Ten of the nineteen lab scripts cost nothing**, including the whole of the failure lab and the
paper's routing arm. Run those first: `resolve.py` before and after the install, `deferred.py`,
`billable.py`, `free_lint.py`, `quota_sketch.py` and the paper demo will take you through most of the
day's ideas without touching a key.

**Cost: $0.** And that sentence is doing more work today than on any previous day — see
[7.1](parts/07-failure-lab/7.1-the-free-trial-that-charges.md).

---

## §7 Traps

- **The model string is a key into a registry, not a name that gets passed on.** `gemini-9.9-turbo`
  resolves because the pattern is `gemini-.*`; a correct Groq model name with no `groq/` prefix does
  not resolve at all. **Resolution is not validation.** (1.1)
- **Nothing checks the model string until something needs the model.** Imports, unit tests and
  `./m check` are all green with a broken one, because none of them makes a call. (1.2)
- **ADK's error recommends `google-adk[extensions]`**, which brings seventeen packages including two
  other agent frameworks, a Kubernetes client and a Docker client. Its own documentation says
  `pip install "litellm>=1.84"`. Take the second suggestion. (2.2)
- **Three version floors disagree** — the error says `>=1.75.5`, the extra says `>=1.84`, the docs say
  `>=1.84`. Look it up rather than trusting the first number you are shown. (2.2)
- **Groq's two rate-limit headers are on different windows.** `x-ratelimit-limit-requests` is per
  **day**, `x-ratelimit-limit-tokens` is per **minute**, and they look symmetrical. The one you hit
  first depends on prompt size, not call count. (2.3)
- **`openrouter/` strings must end in `:free`.** Same model, five characters shorter, billed. Nothing
  in the framework objects. (2.4, 7.1)
- **The free roster moves.** `deepseek/deepseek-r1:free`, named first in this project's own addendum
  on 2026-08-12, was gone by 2026-08-27 — and the free count went from about twenty-five to
  seventeen. List before you pin, every time. (2.4)
- **OpenRouter sends no rate-limit headers on success**, only on the 429. Groq sends them always.
  That difference decides whether a lane can be routed to proactively. (2.4, 4.3)
- **`ollama_chat/`, not `ollama/`.** ADK's docs attribute *"infinite tool call loops and ignoring
  previous context"* to the second, and neither symptom points at a model string. (3.2)
- **`ollama/gemma3*` resolves to `Gemma3Ollama`**, a different class with function-calling
  workarounds. `gemma4` does not. (3.2)
- **A prompt is qualified against a model, not in the abstract.** The handbook passed its probes on
  Gemini; that is a claim about the handbook *and* Gemini. Re-probe per lane. (3.3)
- **One call is not a measurement.** Discard the first — a cold start can be an order of magnitude
  out — record the answer length so you are not ranking verbosity, and put the sample size in the
  cell. (4.1, 4.2)
- **A retry-after hint tells you how long to wait, not which limit you hit.** Day 2 obeyed one
  twenty-eight times over fifteen minutes; the exhausted limit was daily. Cap the attempts. (4.3)
- **`RoutedLlm` is documented and does not exist in Python.** The page is correct about the
  TypeScript runtime. Check the installed package before writing code from a page. (5.1)
- **A router must return the reason as well as the model**, and both must be logged. A routing bug
  does not error — the answers just come from somewhere else. (5.1, 5.2)
- **A router's floor must be a lane that cannot run out and has been probed.** A paid fallback is not
  a floor, and an unprobed one fires exactly when things are already bad. (5.2, 6.1)
- **`anthropic/` and `openai/` resolve on your machine right now**, for model names that do not
  exist. The only thing between that and a bill is a key you do not have. (6.1, 7.1)

---

## §8 Verify before you code

Every source below was checked on the date given, while this day was written. Principle 8: re-check
on the day you use them. This table is evidence, not a substitute — and today more of it has a
shelf life than on any previous day.

| Source | Checked | What it settled |
| --- | --- | --- |
| `adk.dev/agents/models/litellm/` | 2026-08-26 | `pip install "litellm>=1.84"` with **no extra**; `from google.adk.models.lite_llm import LiteLlm`; provider keys read from the environment; ADK handles Claude thinking blocks across turns; and the security note that *"unauthorized code was identified in LiteLLM versions 1.82.7 and 1.82.8 (March 2026)"* |
| `adk.dev/agents/models/ollama/` | 2026-08-26 | `ollama_chat` over `ollama`, because the latter *"can result in unexpected behaviors such as infinite tool call loops and ignoring previous context"*; `OLLAMA_API_BASE`; `ollama show` for tool support; `litellm._turn_on_debug()` |
| `adk.dev/agents/models/routing/` | 2026-08-26 | `RoutedLlm`, `LlmRouter`, the fallback-with-error-context design — **and that every example is TypeScript** |
| `console.groq.com/docs/models` | 2026-08-26 | the production language models, and that preview models *"may be discontinued at short notice"* |
| `console.groq.com/docs/rate-limits` | 2026-08-26 | free plan, other open models: **30 RPM · 1,000 RPD · 8,000 TPM**; the `x-ratelimit-*` headers and that `limit-requests` is *always* RPD while `limit-tokens` is *always* TPM |
| `openrouter.ai/api/v1/models` | 2026-08-27 | **416 models, 17 ending in `:free`**, and `deepseek/deepseek-r1:free` absent — against Addendum 02's 2026-08-12 baseline of "~25 more" |
| `openrouter.ai/docs/api-reference/limits` | 2026-08-27 | **20 RPM · 50 RPD** with no credits purchased; 1,000 RPD needs a $10 purchase; *"successful inference responses do not include `X-RateLimit-*` headers"* |
| `ai.google.dev/gemini-api/docs/rate-limits` | 2026-08-26 | that Google publishes **no** free-tier numbers — limits are shown in AI Studio only, which is why Day 2's 20 RPD came off a live 429 |
| `pypi.org/pypi/litellm/json` | 2026-08-26 | `1.98.0`, `requires_python <3.15,>=3.10` |
| `arxiv.org/abs/2406.18665` and its HTML v4 | 2026-08-26 | the title copied from the record for `docs/PAPERS.md`; the abstract's *"over 2 times"* and transfer-learning claims; `R^α(q)`, the four router methods, the 80k Arena battles, the ~$700 judge-labelling cost, and PGR / CPT / APGR |
| the installed `google-adk` 2.7.1 | 2026-08-26 | the registry's pattern table · `LiteLlm(BaseLlm)` · that `openrouter/` is **not** an ADK pattern and resolves through the library's own provider list · `ollama/gemma3.*` → `Gemma3Ollama` · that **no** `RoutedLlm` exists · that `agent.model` stays a `str` until `canonical_model` is read |

**Six claims in this day that no page states**, established by running code. Re-run them; if your
version disagrees, **your terminal wins** and you fix the document:

```bash
uv run python days/day-09-four-free-providers/lab/resolve.py        # 1.1 - before and after the install
uv run python days/day-09-four-free-providers/lab/deferred.py       # 1.2 - the deferred failure
uv run python days/day-09-four-free-providers/lab/ollama_prefixes.py # 3.2 - three prefixes, three classes
uv run python days/day-09-four-free-providers/lab/route.py          # 5.1 - the field is a str on one lane
uv run python days/day-09-four-free-providers/lab/billable.py       # 7.1 - six layers, no objection
uv run python -c "from google.adk import models; print([n for n in dir(models) if 'Rout' in n])"
```

The last one is the Principle 8 check in its purest form: **an empty list is the finding.**

---

## §9 Say it in an interview

> "The thing that surprised me building on free tiers is how little of the work is the models. One
> agent, one prompt, four providers, and the code difference is a string — the framework resolves it
> against a registry of patterns and picks a native class or a translation layer. So the engineering
> is entirely in knowing what each lane will not do. Two of mine had daily allowances that differed by
> a factor of fifty, which settles where a per-ticket classifier runs before anyone discusses quality.
> One reported remaining requests and remaining tokens on every response, so it could be routed to
> proactively; the others only tell you when they refuse, which means you can only route away from
> them reactively — and that difference is the core of the router's design rather than a detail. The
> two things I'd want a team to internalise are both about silence. A prompt is qualified against a
> model, not in the abstract, so switching providers is a behaviour change that no test catches —
> I re-run the same persona probes on every lane and log which lane answered each request, because a
> fallback that answers slightly worse isn't an error and you'll never find it afterwards. And on the
> aggregator, the free variant of a model is the same identifier with a suffix, so five characters
> shorter is the paid one: the registry resolves it, the agent builds, the client sends it, the
> provider answers well, and the only thing that objects is an invoice. That's a lint, in two places,
> because a string built from config is invisible to a text search."

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked — honestly. `./m done 9` refuses to commit while
any box is unticked, and it cannot tell whether you were truthful. That part is yours.

The day is finished when you have run `resolve.py` before and after the install and can say which
three lines changed and why one did not; when `litellm` is pinned exactly with a dated row in
`docs/PACKAGES.md` and you can say why you declined the extra; when the same handbook has answered
the same question on every lane your machine can reach; when you have read Groq's rate-limit headers
and know which of its two limits Sutra hits first; when you have listed OpenRouter's free models
yourself rather than copying this document's list; when you can say what `ollama_chat/` does that
`ollama/` does not; when twelve probe answers have verdicts written beside them; when
`lab/BENCHMARK.md` has a conditions header and no invented number in it; when you have watched six
layers accept a billable model string and made the lint go red; when `tests/test_models.py` has gone
red and green for each assertion; when you have read the paper and run its demo's routing arm; and
when `sutra/desk/agent.py` is **unchanged**.

---

## §11 Ledger & commit

Paste these **with the values you actually observed** (Principle 7), not the ones printed here.

**`docs/PROGRESS.md`** — append one row:

```text
| 9 | <date> | ADK-08, ADK-09 | 16 (+1 paper) | <hash> | ✅ |
```

**`docs/PACKAGES.md`** — **one row for the package, and two model rows**, all with your own dates:

```text
| litellm | <version> | <date> | 9 | The translation layer for Groq, OpenRouter and Ollama. Installed directly rather than via `google-adk[extensions]`, which pulls seventeen packages including langgraph, crewai, kubernetes and docker to deliver this one; ADK's own docs say `pip install "litellm>=1.84"`. Looked up on PyPI before pinning. **Exact pin, deliberately:** unauthorized code was published in 1.82.7 and 1.82.8 (adk.dev security note, March 2026), and an exact pin plus this row makes "were we ever on an affected version" a lookup. |
| groq/llama-3.3-70b-versatile (model) | free tier; **30 RPM · 1000 RPD · 8000 TPM** ("other open models") | <date> | 9 | The speed lane (Addendum 02). Production list, not preview - preview models "may be discontinued at short notice". Limits read from console.groq.com/docs/rate-limits. |
| openrouter/<the model you chose>:free (model) | free tier; **20 RPM · 50 RPD** without purchased credits | <date> | 9 | The breadth lane (Addendum 02). Chosen from `lab/free_list.py` on the day, not from a document: the free roster held 17 models on 2026-08-27, against "~25 more" in Addendum 02 on 2026-08-12, and `deepseek/deepseek-r1:free` - the model that addendum named first - was gone. |
```

Add a fourth row for your Ollama model if you ran that lane, with its size and whether `ollama show`
listed **tools**.

```bash
curl -s https://pypi.org/pypi/litellm/json | python -c "import sys,json; d=json.load(sys.stdin)['info']; print(d['version'], d['requires_python'])"
uv run python days/day-09-four-free-providers/lab/free_list.py
```

If either lookup fails, the row says `TODO(<that exact command>)` and **not a guess**.

**`docs/PAPERS.md`** — two rows, already added when this day was written. Confirm both identifiers
resolve before you trust them:

```text
| RouteLLM: Learning to Route LLMs with Preference Data | arXiv:2406.18665 | 2024 | 2026-08-26 | 9 | `days/day-09-four-free-providers/papers/01-routellm.md` |
| FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance | arXiv:2305.05176 | 2023 | 2026-08-26 | 9 | *(not taught — named in `papers/01-routellm.md` as the cascade the router is contrasted with)* |
```

**`docs/SKILL_PROVENANCE.md`** — no rows. First entries arrive on Day 29.

**`docs/CHANGELOG_PLAN.md`** — **read this before you skip it.** Addendum 02 §3 lists
`deepseek/deepseek-r1:free` among OpenRouter's free workhorses as of 2026-08-12, and it is no longer
free. That is a Principle 14 situation: reality moved and the plan says so. It does not need an
amendment — the addendum already carries the standing lookup rule that covers it, and §3 is
explicitly a *baseline* — but **if a model this project has actually pinned loses its free tier, stop
and amend before writing code.** Today nothing pinned has, and that sentence is worth writing into
your notes so the next roster change finds you ready.

**`docs/adr/`** — no new ADR. The decision to install `litellm` directly rather than through
`google-adk[extensions]` is recorded in the `PACKAGES.md` row above, which is where a dependency
decision belongs.

**Commit message:**

```text
day 09: same agent, four free providers - the string that changes everything - closes ADK-08, ADK-09
```
