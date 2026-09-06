---
day: 70
phase: 10
phase_name: "Safety and security"
title: "The Quota-Router plugin — requests-remaining per provider per window; route to headroom"
ids: ["OPS-12", "ADK-49"]
principles: [1, 2, 4, 7, 8, 10, 11, 13, 15, 16, 17, 18]
kind: build
plan_version: "v2.2.1"
parts: 23
generated: "2026-09-06"
status: written
lab_scaffolded: true
commit: ""
---

# Day 70 — The Quota-Router plugin

> **Yesterday (Day 69):** PII and data boundaries. Seven stores holding one customer's sentence, a
> redactor measured at 69% on free text, a delete that reported success and reached one store in
> seven, and the decision that every fixture in this repository is invented on purpose.
> **Today:** the last day of Phase 10, and the one that makes the phase's second promise true. Quota
> is this project's currency, and until now every day has spent it blindly: one model string, chosen
> once, with no idea what is left. Today the desk learns to look before it sends.
> **Tomorrow (Day 71):** computer use and the sandbox — a browser agent against a local dummy site,
> and execution isolation in practice.

---

## §1 Where we are

Addendum 02 has said since Day 0 that quota is the currency and budgets are denominated in requests
per day per provider. Day 9 wired four free providers. Day 24 counted tokens. Day 59 capped a runaway
loop. Every one of those days respected the constraint, and not one of them ever asked the question
this day is about: **how much is left, right now, on each lane, and which one should this request go
to?**

The gap matters because the answer changes between one request and the next. A model string in an
agent's constructor is chosen once, at configuration time, by somebody who cannot know what the rest
of the system will have spent by three in the afternoon. Routing is not a preference. It is
**scheduling**, and a scheduler has to see every request.

Three findings run through the day and each one is measured rather than argued.

**A ceiling is a window, not a number.** Ten a minute and 250 a day are two different questions with
two different answers, and a router that consults one is routing on half the truth — measured in
section 1, where judging on both windows keeps the scarcest lane alive to `t=380s` instead of
`t=244s`.

**The obvious way to reroute does not work.** `llm_request.model` looks like the field that selects a
provider. Rewriting it in a plugin changes what the model is *told* and not which model is *asked*,
and the run in part 3.3 sets the field to `fake/groq` and watches `gemini` answer. The router has to
answer *instead of* the agent, not redirect it.

**Your count and the provider's count are of different events.** Section 5 is three ways to arrive at
that disagreement: counting successes while the provider counts attempts, a restart that hands the
router a full allowance the provider has already spent, and two model strings sharing one pool. Part
6.1 adds the fourth — two workers, each correctly inside a ceiling of 20, and a provider that saw 26.

The day ends by naming what it built: a **client-side estimator**, not a rate limiter, and the
difference decides which of a real quota system's features you need and which would be complexity you
cannot verify.

---

## §2 The map

Six sections. Section 1 is what headroom actually is — windows, and the two that disagree. Section 2
is the choice: capability first, then availability, and when greedy is the right rule. Section 3 is
where the code has to live and what it may do at the model boundary. Section 4 is what happens when a
lane refuses. Section 5 is three routers that disagree with the provider. Section 6 is what changes
in a real deployment, and what this day deliberately did not build.

### 1 — What headroom is

*A limit is a window, and there is more than one of them.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [A ceiling is a window, not a number](parts/01-what-headroom-is/1.1-a-ceiling-is-a-window-not-a-number.md) | Limit, window, pool — and why the pool is the one people get wrong | `foundation` |
| 1.2 | [The burst every counter approved](parts/01-what-headroom-is/1.2-the-burst-every-counter-approved.md) | 💥 A fixed window permits twice the limit across its edge | `working` |
| 1.3 | [The counter that remembers when](parts/01-what-headroom-is/1.3-the-counter-that-remembers-when.md) | What a sliding window costs and what it buys | `working` |
| 1.4 | [Two windows, and the one that bites last](parts/01-what-headroom-is/1.4-two-windows-and-the-one-that-bites-last.md) | 💥 Routing on the minute empties the scarcest day first | `working` |
| 1.5 | [Twelve left means two different things](parts/01-what-headroom-is/1.5-twelve-left-means-two-different-things.md) | Remaining as a share of the ceiling, not as a count | `working` |

### 2 — Choosing a lane

*Capability, then availability — and the condition under which greedy is correct.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [Headroom is not a preference](parts/02-choosing-a-lane/2.1-headroom-is-not-a-preference.md) | Routing is scheduling, so it cannot live in an agent's configuration | `foundation` |
| 2.2 | [The lane that cannot do the job](parts/02-choosing-a-lane/2.2-the-lane-that-cannot-do-the-job.md) | Capability filtering runs before headroom is ever consulted | `working` |
| 2.3 | [With perfect information, greedy is fine](parts/02-choosing-a-lane/2.3-with-perfect-information-greedy-is-fine.md) | When the simplest rule is also the right one | `working` |
| 2.4 | [Everyone read the same board](parts/02-choosing-a-lane/2.4-everyone-read-the-same-board.md) | 💥 A shared view, a herd, and what randomisation is actually for | `production` |

### 3 — The plugin

*Where the router's code has to live, and what it is allowed to do at the model boundary.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [Where a router has to stand](parts/03-the-plugin/3.1-where-a-router-has-to-stand.md) | Plugin hooks are global, agent callbacks are local — adk.dev's own words | `foundation` |
| 3.2 | [Observe, block, answer instead](parts/03-the-plugin/3.2-observe-block-answer-instead.md) | Three return values, and why a router needs the third | `working` |
| 3.3 | [The field that does not reroute](parts/03-the-plugin/3.3-the-field-that-does-not-reroute.md) | 💥 The field is set to `fake/groq` and `gemini` answers | `production` |
| 3.4 | [Answering instead of the agent](parts/03-the-plugin/3.4-answering-instead-of-the-agent.md) | 24 tickets, with and without the router, in a real Runner | `production` |

### 4 — When a lane says no

*A 429 is an instruction with a time in it.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [Reading the refusal](parts/04-when-a-lane-says-no/4.1-reading-the-refusal.md) | Why `retry-after` is worth more than every counter you keep | `working` |
| 4.2 | [A cold lane, not a broken one](parts/04-when-a-lane-says-no/4.2-a-cold-lane-not-a-broken-one.md) | 💥 Hammering serves the same 10 and costs 29 extra refusals | `production` |
| 4.3 | [Every lane dry](parts/04-when-a-lane-says-no/4.3-every-lane-dry.md) | Refusing with a number, so the caller can act on it | `production` |
| 4.4 | [The part that will do](parts/04-when-a-lane-says-no/4.4-the-part-that-will-do.md) | 💥 Silent degradation, and the difference a declaration makes | `production` |

### 5 — Failure lab

*Three routers that look correct and disagree with the provider.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [The tally that counts only sales](parts/05-failure-lab/5.1-the-tally-that-counts-only-sales.md) | 💥 The router believed 20, the provider counted 60 | `production` |
| 5.2 | [The counter that starts full](parts/05-failure-lab/5.2-the-counter-that-starts-full.md) | 💥 A restart hands back an allowance already spent | `production` |
| 5.3 | [Two cards, one household](parts/05-failure-lab/5.3-two-cards-one-household.md) | 💥 Two model strings, one pool, and an imaginary second meter | `production` |

### 6 — In production

*What changes when there are two of everything, and what this day did not build.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 6.1 | [One till, two cashiers](parts/06-in-production/6.1-one-till-two-cashiers.md) | 💥 13 and 13 inside a ceiling of 20, and a provider that saw 26 | `production` |
| 6.2 | [The gauge shows what is left](parts/06-in-production/6.2-the-gauge-shows-what-is-left.md) | Remaining per window, and the disagreement worth alerting on | `production` |
| 6.3 | [What a real quota system adds](parts/06-in-production/6.3-what-a-real-quota-system-adds.md) | Estimator versus enforcer, and four things deliberately parked | `production` |

### The paper — read it last

*Principle 4 at the scale of a day: build the router, find the condition where its rule stops being
right, then read the result about that condition.*

| # | Paper | What it answers |
| --- | --- | --- |
| 01 | [The power of two choices in randomized load balancing](papers/01-the-power-of-two-choices.md) | `doi:10.1109/71.963420` — what a *little* information buys, and why Sutra does not need it until the router is replicated |

---

## §3 Setup — run this

```bash
mkdir -p days/day-70-the-quota-router/lab/papers/two-choices
cd days/day-70-the-quota-router/lab
```

Sixteen files in the lab, plus two in the paper's demo directory. No package is added today:

```bash
touch _lane.py _router.py _fake.py
touch windows.py twowindows.py headroom.py stale.py
touch hooks.py modelfield.py desk.py
touch cold.py dry.py failopen.py pool.py budget.py gate.py
touch papers/two-choices/balance.py papers/two-choices/demo.py
```

**What each file is for:**

- The three underscore-prefixed modules are imported, never run. `_lane.py` is the accounting —
  `Clock`, `Refused`, `Fixed`, `Sliding`, `Lane` and `fleet()` — and it is the file to read first,
  because every number this day prints comes from it. `_router.py` is the choice. `_fake.py` is a
  `BaseLlm` subclass so the plugin runs inside the real ADK runtime at zero cost.
- `windows.py`, `twowindows.py`, `headroom.py` and `stale.py` are sections 1 and 2.
- `hooks.py`, `modelfield.py` and `desk.py` are section 3 — what a plugin may do, what does not work,
  and the whole thing end to end.
- `cold.py` and `dry.py` are section 4; `failopen.py` and `pool.py` are section 5.
- `budget.py` proves the day spends nothing, and `gate.py` is the eval.

Verify the lab is gitignored before running anything:

```bash
git check-ignore -v days/day-70-the-quota-router/lab/_lane.py
```

**Why:**

- `days/*/lab/` is ignored repo-wide, so this should print the matching rule. Nothing today writes
  customer-shaped text, but the habit is the point — Principle 9, and every earlier day in this phase
  checked the same thing.

**No package is added today.** `git diff pyproject.toml uv.lock` must be empty and stay empty.

---

## §4 Build brief

The teaching is in `parts/` and the measurements are in `lab/`. What is left is the product piece.

**`sutra/routing.py`** — the quota router, as a plugin.

- `TODO(me)`: a `QuotaRouter(BasePlugin)` whose `before_model_callback` picks a lane and returns an
  `LlmResponse`. A plugin on the `Runner`, not an agent callback — part 3.1 is the argument and
  adk.dev's own sentence about global versus local hooks is the evidence.
- `TODO(me)`: `headroom()` consulting **both** windows and returning a share of the ceiling rather
  than a count. Parts 1.4 and 1.5 are why; `gate.py` checks it.
- `TODO(me)`: count on **attempt**, not on success. Part 5.1 is the measurement, and it is one line's
  difference — which side of the `try` the decrement sits on.
- `TODO(me)`: mark a refused lane cold from its `retry-after` and stop sending until it elapses; raise
  rather than degrade when nothing can serve the request. Parts 4.2 and 4.3.
- `TODO(me)`: open the module docstring with the sentence part 6.3 asks for — *this is a client-side
  estimator, not an enforcer* — and the four parked items with the condition that would change each.

**`tests/test_routing.py`**

- `TODO(me)`: a test that the router picks by share of ceiling rather than by raw remaining, using two
  lanes whose raw counts and shares disagree. Part 1.5 supplies the case.
- `TODO(me)`: a test that a non-quota failure still decrements the counter. This is the one test that
  would have caught part 5.1, and it is the one nobody writes.
- `TODO(me)`: a test that an exhausted fleet **raises** and that the exception carries `soonest`. Part
  4.3 is why the number matters more than the exception.

Do not copy the lab scripts into `sutra/`. `_fake.py` and the simulated lanes are this day's
instrument; the product piece is the plugin.

---

## §5 The eval that must be able to fail

```bash
cd days/day-70-the-quota-router/lab
uv run python gate.py; echo "exit: $?"
```

Six checks against `sutra/routing.py`, and today every one of them is red because the module is the
build brief. Each check prints what it actually found rather than only pass or fail — a check that
says `False` and nothing else is a check nobody can debug (Principle 10).

The red-alarm test — the one that can be driven red **on demand** once the module exists — is the
`--naked` arm of the end-to-end run:

```bash
uv run python desk.py
uv run python desk.py --naked
```

The first spreads 24 tickets across the fleet. The second sends all 24 to the agent's own lane against
a ceiling of ten a minute, with nothing consulting it. If those two ever agree, the router has stopped
routing. Three more ablations exist and are exercised in their parts: `cold.py --hammer`,
`dry.py --degrade`, `failopen.py --strict` and `pool.py --pooled`.

---

## §6 Request budget

**Zero provider requests, to every provider.**

| Provider | Requests today | Against |
| --- | --- | --- |
| Google AI Studio (Gemini) | 0 | free tier |
| Groq | 0 | 30 RPM / 250 RPD, observed 2026-09-05 |
| OpenRouter `:free` | 0 | free tier |
| Ollama (local) | 0 | n/a |

A day about quota that quietly spent some would be teaching one thing and doing another, so this one
is checkable rather than promised:

```bash
uv run python budget.py
```

Every lane in the lab is `_lane.Lane` — a counter with a clock whose windows, refusals and
`retry-after` values behave the way the real ones do. `_fake.py`'s models are **real `BaseLlm`
subclasses**, so the ADK runtime treats them as models in every respect and section 3's plugin
measurements mean something; none of them is a provider, nothing imports an HTTP client, and no key is
read from the environment.

The limits the day **reports** are the real free-tier figures from Addendum 02 — 10/min and 250/day
for Gemini, 30/min and 1000/day for Groq, 20/min and 50/day for OpenRouter — because a router tuned
against invented ceilings would be tuned against nothing.

---

## §7 Traps

1. **Treating a limit as a number.** It is a window, and there is more than one of them — part 1.1.
2. **A fixed window.** It approves a burst of twice the limit across its edge, and both your counter
   and the provider's are telling the truth about different windows — part 1.2.
3. **Routing on the minute alone.** It empties the scarcest daily allowance first, which is the one
   that does not refill — part 1.4.
4. **Comparing lanes by requests remaining.** Different ceilings make those numbers incommensurable;
   compare shares — part 1.5.
5. **Putting the router in the agent's configuration or an agent callback.** A scheduler that cannot
   see every request is not a scheduler — parts 2.1 and 3.1.
6. **Rewriting `llm_request.model`.** It changes what the model is told, not which model is asked, and
   it passes every unit test you would think to write — part 3.3.
7. **Retrying a 429 immediately.** The minute window was never going to open sooner for being asked
   more often; the same 10 are served and 29 extra refusals are counted against you — part 4.2.
8. **Degrading silently.** An answer from a lane that cannot do the job, with nothing recording it,
   is the failure — not the outage, the silence about it — part 4.4.
9. **Counting successes.** The provider counts attempts, and the gap was 40 requests in a 60-request
   run — part 5.1.
10. **Keeping headroom in process memory.** A restart resets it (part 5.2) and a second worker doubles
    it (part 6.1), and both are the same root cause.
11. **Keying the counter on the model string.** Free tiers meter per project, organization or account,
    so the second meter is imaginary — part 5.3.
12. **Alerting on requests sent.** The operational number is what remains, per window, and the alert
    that catches every bug above is the *disagreement* between your gauge and a 429 — part 6.2.

---

## §8 Verify before you code

Fetched on 2026-09-06:

| What | Where | What it said |
| --- | --- | --- |
| Plugin hook scope | <https://adk.dev/plugins/> | verbatim: *"Plugin hooks are global. You register a Plugin once on the `Runner`, and its hooks apply universally to every Agent, Model, and Tool it manages. In contrast, Agent Callbacks are local, configured individually on a specific agent instance."* — the sentence part 3.1 is built on |
| `before_model_callback` return contract | <https://adk.dev/callbacks/types-of-callbacks/> | returning an `LlmResponse` means the call to the LLM is **skipped** and the value is used as if it came from the model — the hook the whole router stands on (part 3.2) |
| `doi:10.1109/71.963420` record | <https://api.crossref.org/works/10.1109/71.963420> | title *The power of two choices in randomized load balancing*, IEEE TPDS 12(10), 1094–1104, 2001. The Crossref record carries **no abstract**, so the paper document quotes no constants and no theorem statement, and says so (§17.4.1 rule 5) |
| `google-adk` latest | <https://pypi.org/pypi/google-adk/json> | `2.8.0`; this repo pins `2.7.1`, carried forward as the Day 65 freshness finding rather than upgraded mid-phase (Principle 14) |

Two behaviours were **measured** against the installed `2.7.1` rather than read, and each part shows
the command: that rewriting `llm_request.model` does not change which model object answers (part 3.3),
and that a plugin returning an `LlmResponse` intercepts the call while one returning `None` does not
(part 3.2).

---

## §9 Say it in an interview

*"We were on free tiers across four providers and every agent had one model string chosen at
configuration time, so nothing in the system knew what was left. The reframe that helped was that
routing is scheduling, not preference — a scheduler has to see every request, so the code went into a
runner-level plugin rather than an agent callback, which is the only place in ADK that sees them all.
Three things surprised me. Rewriting the request's model field doesn't reroute anything: it changes
what the model is told, not which model object answers, and it passes every test you'd think to write
— the router has to answer instead of the agent. Comparing lanes by requests remaining is wrong,
because different ceilings make those numbers incommensurable; comparing each lane's share of its own
ceiling kept the scarcest lane alive half as long again. And our count and the provider's count are of
different events — we counted successes, they counted attempts, and in a sixty-request run the gap
was forty, so thirty requests were refused while our router said it was fine. The one I'd flag first
on any new system is that the counter lives in the process and the allowance doesn't: a restart hands
you a full allowance you've already spent, and two workers each stay inside a ceiling of twenty while
the provider sees twenty-six. And I'd be clear about what we built — a client-side estimator, not a
rate limiter. The single best change is reading the provider's own remaining-quota headers where they
send them, and treating your counter as a prediction whose error you can measure."*

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked, and you have run the commands rather than read
them. `./m done 70` refuses to commit until they are.

The day is finished when you can look at any two lanes and say which one the router will pick and why,
without running it — and when you can name the four ways your counter and the provider's can disagree,
and which single change fixes three of them.

---

## §11 Ledger & commit

**`docs/PROGRESS.md`** — append this row:

```text
| 70 | 2026-09-06 | OPS-12, ADK-49 | 23 | <hash> | ⚠️ |
```

The gate column is `⚠️` and means it. `./m depth 70` is green over the twenty-three parts and the
paper. `lab/gate.py` is **red** on all six checks by design — `sutra/routing.py` is the build brief.
Phase 10's gate — *injection attempts contained; quota router live* — is green on its first half and
becomes green on the second when that module lands. The repository-wide `⚠️` carried since Day 15 is
unchanged: `tests/test_persona.py` still fails ruff `I001`, and it is the learner's own file, which no
generated day may edit.

**`docs/PACKAGES.md`** — no new rows. No package is added today.

**`docs/PAPERS.md`** — one row, checked live today:

```text
| The power of two choices in randomized load balancing | doi:10.1109/71.963420 | 2001 | 2026-09-06 | 70 | `days/day-70-the-quota-router/papers/01-the-power-of-two-choices.md` |
```

**`docs/SKILL_PROVENANCE.md`** — no new rows. No third-party skill is used today.

**Commit:**

```text
day 70: the quota-router plugin - route to headroom per provider per window - closes OPS-12, ADK-49
```
