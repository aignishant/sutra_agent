# Day 9 — CHECKLIST

**IDs closed:** ADK-08, ADK-09
**Principles served:** 1, 2, 4, 6, 7, 8, 10, 11, 13, 14, 15, 16, 17, 18
**Parts:** 16 across 7 sections, plus 1 paper

> `./m done 9` refuses to commit while any box below is unticked. It cannot tell whether you were
> honest — that part is yours.

## Demo command

```bash
uv run python days/day-09-four-free-providers/lab/resolve.py
cat days/day-09-four-free-providers/lab/BENCHMARK.md
cd days/day-09-four-free-providers/lab/papers/routellm && uv run python run.py && cd -
./m check && uv run python scripts/trace.py && git log --oneline -1
```

Expected: three provider strings resolving to `LiteLlm`; your own four-row benchmark table with your
own numbers and dates; `strong-model calls: 10/10` then `5/10`; then `OK all green`, then
`traceability: 18/199 closed, 0 problem(s)`, then one commit reading
`day 09: same agent, four free providers - the string that changes everything - closes ADK-08, ADK-09`.

---

## Before the install

- [ ] `./m check` is green and `scripts/trace.py` shows Day 8's count before you change anything
- [ ] Ran `lab/resolve.py` **before** installing anything, and kept the output (1.1)
- [ ] Can say why `gemini-9.9-turbo` resolves and `llama-3.3-70b-versatile` does not (1.1)
- [ ] Ran `lab/deferred.py` and can name the four things that stay green with a broken model string
      (1.2)
- [ ] `sutra/desk/models.py` written with `check()` before you touch a provider (1.2)

## ADK-09 — the translator (section 2)

- [ ] Looked the `litellm` version up on PyPI **before** typing it, and recorded `requires_python`
      (2.2)
- [ ] `uv add "litellm==<observed>"` — exact pin, runtime dependency, and `uv.lock` diff looked at
      (2.2)
- [ ] Ran `lab/resolve.py` again and can name **which three lines changed and why one did not** (2.2)
- [ ] Can list three things `google-adk[extensions]` installs that have nothing to do with models
      (2.2)
- [ ] Can say what an exact pin buys you that `>=` does not, using the March 2026 security note (2.2)
- [ ] Ran `lab/providers.py` and saw why `openrouter/` resolves without being an ADK pattern (2.2)
- [ ] Ran `lab/two_forms.py` and can say why both forms end at the same class (2.1)
- [ ] Ran `lab/groq_lane.py` — Sutra's handbook answered by a model Google did not make (2.3)
- [ ] Ran `lab/groq_headers.py` and pasted the headers into your notes (2.3)
- [ ] Worked out which of Groq's two limits Sutra's real tickets hit first, and wrote it down (2.3,
      `TODO(me)`)
- [ ] Ran `lab/free_list.py` and used **your** list, not this document's (2.4)
- [ ] Counted how many of the seventeen models listed here still exist on your day (2.4)
- [ ] Ran `lab/openrouter_lane.py` with a `:free` model, through `guard()` (2.4)
- [ ] Can say how Groq and OpenRouter differ in *when* they report remaining quota (2.4, 4.3)

## ADK-08 — the local lane (section 3)

- [ ] `ollama --version` and `curl http://localhost:11434/api/tags` both answered — or the reason
      written down (3.1)
- [ ] Chose a model, ran `ollama show`, and confirmed **tools** is in its capabilities (3.1)
- [ ] Recorded the model name, its size and the date in your notes (3.1, `TODO(me)`)
- [ ] Ran `lab/local_lane.py` with the reachability guard doing its job (3.1)
- [ ] Can name four things this lane does not need and two it costs you (3.1)
- [ ] Ran `lab/ollama_prefixes.py` and saw three strings resolve three ways (3.2)
- [ ] Turned on `litellm._turn_on_debug()` and compared the two `curl` commands side by side (3.2)
- [ ] Can give the two symptoms ADK attributes to `ollama/`, and which layer each sends you to debug
      by mistake (3.2)
- [ ] Ran `lab/portability.py` on every lane you can reach, one lane at a time (3.3)
- [ ] Wrote a verdict beside each of the twelve answers: pass, fail, or **hedged near-miss** (3.3,
      `TODO(me)`)
- [ ] Named the probe that survived every lane and the one that did not (3.3, `TODO(me)`)
- [ ] Can say why "the handbook passed its probes" is a claim about two things (3.3)

## The benchmark (section 4)

- [ ] Ran `lab/bench.py` once per reachable lane, in one sitting (4.1)
- [ ] Discarded the warm-up and can say how much slower it was (4.1)
- [ ] Recorded the answer length beside every timing (4.1)
- [ ] Can name three things that vary between two calls and have nothing to do with the provider
      (4.1)
- [ ] `lab/BENCHMARK.md` written, with a **conditions header** — date, rough time, machine, method,
      sample size (4.2)
- [ ] Every cell you could not fill says `not run: <reason>`, and none is blank (4.2)
- [ ] The quality column is a **sentence** naming the weakest probe, not a number (4.2)
- [ ] Ran `lab/refusals.py` and read the `headroom reported:` line for each lane that has a key (4.3)
- [ ] Did **not** provoke a 429 on Gemini to reproduce a result Day 2 already recorded (4.3)
- [ ] Can name the four different jobs hiding behind "handle the 429" (4.3)

## ADK-09 — routing (section 5)

- [ ] Ran `lab/route.py` and worked out why one row prints `str` before reading the explanation (5.1)
- [ ] Ran the `RoutedLlm` check and saw an empty list (5.1)
- [ ] Can say what you would have lost by writing Python from that documentation page (5.1)
- [ ] `choose()` returns the **reason** as well as the model — checked in your own code (5.1)
- [ ] Ran `lab/quota_sketch.py` and argued with the middle row (5.2)
- [ ] Fixed the ordering so a classification goes to the fast hosted lane while it has headroom (5.2,
      `TODO(me)`)
- [ ] Can name the four things a Quota-Router needs and say why the floor must be a probed lane (5.2)

## 🅿️ Parked (section 6)

- [ ] Ran `lab/parked_lanes.py` and saw two non-existent models resolve anyway (6.1)
- [ ] Read `.env.example` and confirmed it names four keys, all free (6.1)
- [ ] Can say precisely what you are and are not entitled to claim about the paid models (6.1)

## 💥 The failure lab (section 7)

- [ ] Ran `lab/billable.py` and watched six layers accept a billable string (7.1)
- [ ] `free_only()` and `BillableModelError` written, and used **inline** at construction (7.1)
- [ ] Ran `lab/free_lint.py` and saw it go red on your own teaching file — correctly (7.1)
- [ ] Appended a billable string to `sutra/desk/models.py`, watched the count go to two, reverted,
      watched it return to one (7.1)
- [ ] Decided what to do about the deliberate example: an allowance with a written reason, or
      assembling the string. Wrote down which and why (7.1, `TODO(me)`)
- [ ] Ran the `grep` version and can say what it catches that the Python lint does not (7.1)
- [ ] Can name the two places the check has to live, and what each catches that the other cannot
      (7.1)

## The paper — read **after** the parts

- [ ] Read [`papers/01-routellm.md`](papers/01-routellm.md) only after finishing section 7
- [ ] Ran the demo's routing arm and reproduced `10/10` then `5/10` (papers/01)
- [ ] Walked α across the whole range and reproduced the staircase (papers/01)
- [ ] Ran the `--live` arm and judged, by hand, whether the five demoted answers were worse
      (papers/01, `TODO(me)`)
- [ ] Can state the routing rule in one sentence, including what α does (papers/01)
- [ ] Can name the number in the paper that its abstract does not mention (papers/01)
- [ ] Can say which half of the paper is in shipped systems and which half was replaced (papers/01)

## Tests — each one red, then green

- [ ] `tests/test_models.py` written and passing (§5)
- [ ] Changed `DESK_MODEL` to a real model name with no provider prefix, watched the first test go
      red, put it back
- [ ] Deleted the `startswith("openrouter/")` guard, watched the fourth test go red, put it back
- [ ] Changed `raise` to a warning in `free_only`, watched the second test go red, put it back
- [ ] Changed `DESK_MODEL` to `gemini-9.9-turbo`, watched **every test pass**, and wrote down what
      would have caught it
- [ ] Wrote the sixth test: a billable string built by concatenation (`TODO(me)`)
- [ ] `uv run python -m pytest -q -m "not live"` green across the whole suite

## The request budget

- [ ] Spent **7 or fewer** Gemini requests, and know which parts they went to (§6)
- [ ] Ran all ten zero-cost scripts before any that costs quota
- [ ] `GOOGLE_GENAI_USE_VERTEXAI=FALSE` still set, and `require_free_tier()` still runs at import
- [ ] No paid model string committed anywhere — `lab/free_lint.py` and the `grep` both checked

## Ledger & commit

- [ ] `docs/PROGRESS.md` row appended, with the real date, the real hash, 16 parts and 1 paper
- [ ] `docs/PACKAGES.md` — the `litellm` row with **your** version and date, plus a row per model
      string you used, each with its observed limits and the date you checked them
- [ ] `docs/PAPERS.md` — both rows confirmed, and both identifiers opened at least once
- [ ] Read the `CHANGELOG_PLAN.md` note in the hub's §11 and can say why today needed no amendment
- [ ] `./m check` green: ruff, format, pytest, depth, trace
- [ ] `uv run python scripts/trace.py` shows ADK-08 and ADK-09 closed and no problems
- [ ] `sutra/desk/agent.py` is **unchanged** — still Gemini, still Day 6's handbook. Checked with
      `git diff --stat`, not assumed
- [ ] One commit, message exactly as in the hub's §11
