---
day: 24
phase: 3
phase_name: "State, context & discipline"
title: "Token accounting & budgets — denominated in quota (RPM/RPD), not dollars"
ids: ["OPS-07", "AG-11"]
principles: [1, 2, 7, 8, 10, 11, 14, 15, 16, 17, 18]
kind: lab
plan_version: "v2.2.1"
parts: 13
generated: "2026-09-04"
status: written
lab_scaffolded: false
commit: ""
---

# Day 24 — Token accounting & budgets: denominated in quota, not dollars

> **Yesterday (Day 23):** pytest arrived and the deterministic half of Sutra got a harness — and
> [23.1.1](../day-23-testing-tools-and-callbacks/parts/01-where-the-line-falls/1.1-the-nondeterminism-excuse.md)
> named the next thing that would bite: *"a function that reads a clock is not deterministic, and
> Day 24's quota window is exactly such a function."*
> **Today:** the budget that window belongs to. What a request actually costs, the two ceilings a free
> tier enforces, a ledger that refuses before it spends, and the last part of Phase 3's gate — *budgets
> enforced*.
> **Tomorrow (Day 25):** Phase 4 opens with Agent Skills and the `SKILL.md` spec.

---

## §1 Where we are

The office printer has a code you type before it will print anything, and the code belongs to your
department.

Nobody explained the system when you joined. You found out about it on the afternoon it said
`quota exceeded` in the middle of a fifty-page bundle for a client meeting, and the person who could
reset it was on leave. It turned out that somebody in the next room had printed a project's worth of
drawings that morning, out of the same monthly allowance, and there had been no way for either of you
to know.

Three things about that afternoon are worth noticing. The allowance was not money — you could not
solve it by paying. It was shared, and nobody had divided it. And the moment you found out about it was
the moment you could least afford to.

That is precisely where Sutra is this morning. Twenty generate requests per day, per model, per
project, and **nothing anywhere in the codebase knows that number**.

Four things worth knowing before you start.

**The scarce thing is not what you think it is.** Measured against the provider's own tokenizer,
English prose costs 4.55 characters per token, a JSON log line 2.21, and the string `"4521"` — four
characters — costs **five tokens**. All of which is interesting and none of which is what you are
rationed on: the refusal names its metric as `generate_content_free_tier_requests`, with
`quotaValue: '20'`. **Requests.** A one-word question and a fifteen-thousand-token document cost the
same.

**And the conversation is charged again every turn.** An eight-turn conversation whose full text is
**151 tokens** cost **786** to conduct — 5.2× — because a chat model is stateless. In the currency that
matters, that is **eight of the day's twenty requests for one conversation**: two and a half
conversations a day, per model.

**There are two ceilings and only one of them clears.** Per-minute refills as requests age out;
per-day does not. Both arrive as `429 RESOURCE_EXHAUSTED`, and retrying the second one costs **3
requests instead of 1** to learn the same fact — which Day 21 measured for real at twenty-eight
requests across a quarter of an hour.

**And checking before you spend is not the same as handling the refusal.** Twenty-five attempts against
a ceiling of twenty: check first and the ledger reads `20 of 20`; let the provider decide and it reads
**`25 of 20`** — five requests spent to be told no.

---

## §2 The map

Thirteen parts in five sections, and **one paper**. The day climbs
`foundation → working → production`: section 1 measures what a request costs, section 2 is the
provider's side of the contract, section 3 builds the ledger, section 4 is the failure lab and
section 5 is what changes when there is more than one consumer.

**Read the paper last.** *New directions in communications* (`doi:10.1109/MCOM.1986.1092946`) is the
1986 report the leaky bucket comes from, and its descendant — the token bucket — is what
[3.1](parts/03-counting-before-spending/3.1-the-ledger.md)'s list of timestamps becomes when it has to
be O(1) and atomic. Principle 4 at the scale of a day: build the limiter by hand, then read the
proposal.

### Section 1 — `01-what-a-request-costs`: token economics (AG-11)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [A ticket id costs five tokens](parts/01-what-a-request-costs/1.1-a-ticket-id-costs-five-tokens.md) | 4.55, 2.21 and 0.80 characters per token | `foundation` |
| 1.2 | [The conversation is charged again every turn](parts/01-what-a-request-costs/1.2-charged-again-every-turn.md) | 151 tokens of text, 786 charged | `working` |
| 1.3 | [The unit that gets rationed is the request](parts/01-what-a-request-costs/1.3-the-unit-that-gets-rationed.md) | Why trimming prompts buys nothing here | `working` |

### Section 2 — `02-two-ceilings`: what the provider actually enforces (OPS-07)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [Two ceilings, and only one of them clears](parts/02-two-ceilings/2.1-two-ceilings-one-clears.md) | One status code, two opposite responses | `working` |
| 2.2 | [Reading the ceiling off a refusal](parts/02-two-ceilings/2.2-reading-the-ceiling-off-a-refusal.md) | `quotaValue: '20'`, and one honest `TODO` | `working` |
| 2.3 | [Denominated in quota, not dollars](parts/02-two-ceilings/2.3-denominated-in-quota-not-dollars.md) | What "spend more" being unavailable buys you | `working` |

### Section 3 — `03-counting-before-spending`: the ledger (OPS-07)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [The ledger, with the clock as a parameter](parts/03-counting-before-spending/3.1-the-ledger.md) | Thirty lines, and no `import time` | `working` |
| 3.2 | [Refusing before the call, not after](parts/03-counting-before-spending/3.2-refusing-before-the-call.md) | `20 of 20` against `25 of 20` | `working` |
| 3.3 | [Testing a ceiling that only bites at midnight](parts/03-counting-before-spending/3.3-testing-a-ceiling-that-bites-at-midnight.md) | A daily reset, verified in 0.06s | `production` |

### Section 4 — `04-failure-lab`: the deliberate failures

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [💥 The retry that spent the budget](parts/04-failure-lab/4.1-the-retry-that-spent-the-budget.md) | 1 request against 3, same outcome | `production` |
| 4.2 | [💥 The counter that counted the wrong thing](parts/04-failure-lab/4.2-the-counter-that-counted-the-wrong-thing.md) | Believing 9 remain when 4 do | `production` |

### Section 5 — `05-in-production`: more than one consumer

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [Whose budget is it?](parts/05-in-production/5.1-whose-budget-is-it.md) | 20 served and two people angry, or 14 and nobody | `production` |
| 5.2 | [Degrading, not failing](parts/05-in-production/5.2-degrading-not-failing.md) | Three exits, and the one that lies twice | `production` |

### The paper — read after the parts

| # | Paper | What it answers | Level |
| --- | --- | --- | --- |
| 01 | [New directions in communications — the leaky bucket](papers/01-the-leaky-bucket.md) | `doi:10.1109/MCOM.1986.1092946` — 5 served against 10, at the boundary | `production` |

---

## §3 Setup — run this

**No new packages today.** `google-genai` supplies `count_tokens`, and everything else is the standard
library — `collections.deque` and `dataclasses`. `docs/PAPERS.md` gains one row (§11).

```bash
# 1 - the day folder's lab, and the paper's demo folder
cd days/day-24-token-accounting-and-budgets
mkdir -p lab/papers/token-bucket
cd lab

# 2 - the two measurement scripts (these need a key, and cost 0 generations)
touch count_the_cost.py history_costs_again.py

# 3 - the ledger and its tests
touch quota.py test_quota_demo.py

# 4 - the demonstrations, each with an ablation switch
touch refuse_before_spending.py retry_spent_the_budget.py counted_the_wrong_thing.py
touch budget_per_what.py degrade_dont_fail.py

# 5 - the paper's two-file demo
touch papers/token-bucket/bucket.py papers/token-bucket/run.py
cd -

# 6 - what changes under sutra/ and tests/ today
ls sutra/                    # quota.py is new; plugins.py gains the budget check
ls tests/                    # test_quota.py is the eval
```

**Two scripts need `GOOGLE_API_KEY` and neither of them generates anything.** `count_the_cost.py` and
`history_costs_again.py` call `count_tokens`, which is a **different endpoint** from
`generate_content` and sits on its own quota. Verified on 2026-09-04, on a key whose daily generation
allowance was already exhausted: counting still worked while generating was refused with a `429`. That
is what lets a day about spending requests cost none.

**Every other script simulates the provider**, deliberately. The refusals they raise are shortened forms
of the real `429` body captured on 2026-09-04
([2.2](parts/02-two-ceilings/2.2-reading-the-ceiling-off-a-refusal.md)), not invented strings — because
a day about not wasting requests should not waste twenty-five of them proving a point about
arithmetic.

**Run `count_the_cost.py` first.** Five samples, five numbers, and the last one — a four-character
ticket id costing five tokens — is the one that resets your intuition for the rest of the day.

---

## §4 Build brief

**`sutra/quota.py`** — new:

| Symbol | What it is | Taught in |
| --- | --- | --- |
| `Ceiling` | frozen: `name`, `rpm`, `rpd` — no token field, no currency field | 1.3, 2.3 |
| `Ledger` | a `deque` of timestamps, one per provider-and-model pair | 3.1 |
| `used(now)` | both counts, so the two ceilings never collapse into one | 2.1 |
| `refusal(now)` | the sentence, or `None` — day ceiling checked **first** | 2.1, 3.2 |
| `spend(now)` | called for **every attempt**, including the failed ones | 4.2 |
| `ceiling_from(exc)` | the `quotaId` and `quotaValue` out of a real `429` body | 2.2 |

Three things in that table are the design. `Ceiling` is **frozen** because a limit is a fact about the
provider and not runtime state. `refusal` returns **a string or `None`** rather than a boolean, so one
value carries the decision and the reason. And **`now` is an argument everywhere** — there is no
`import time` in the module, which is what makes
[3.3](parts/03-counting-before-spending/3.3-testing-a-ceiling-that-bites-at-midnight.md) possible.

**`sutra/plugins.py`** — extended so that `before_model_callback` asks the ledger and refuses locally
before a request goes out, and `spend` is recorded at the point the call leaves. It sits **beside**
Day 22's `Flight` recorder and Day 21's `Policy`, not merged into either.

**`tests/test_quota.py`** — new. Eight cases, no key; see §5.

**`TODO(me)` markers left for you:**

- **2.2** — **capture the per-minute ceiling.** `rpm=5` in the lab is a placeholder, not a measured
  fact, and the exact command is in the part. Record the real number and the date in
  `docs/PACKAGES.md`, then replace it. This is the highest-value item in the list.
- **1.1** — add two samples of your own to `count_the_cost.py`: one line from a log you have written,
  and one of your own identifiers. Write down the characters-per-token you expect first.
- **1.2** — add four turns to the conversation and check whether the multiplier moved the way (n+1)/2
  predicts. Then decide Sutra's compaction threshold from *that* number rather than from Day 20's
  character estimate.
- **2.3** — write your own provider table and mark every cell **measured** or **estimated**. Count how
  many are measured. That count is the honest state of your budget.
- **3.1** — decide where the ledger's state lives across a restart. In memory it forgets the day's
  spending while the provider does not. A file, a sqlite row and "accept the gap" are all defensible;
  write down which and why.
- **3.1, 3.2** — close the check-then-spend race: one atomic `take(now)` that returns a permit or a
  refusal, instead of two calls. Then say what still breaks with two processes.
- **3.3** — add the boundary cases: exactly `MINUTE`, one before, one after. Decide whether the
  behaviour you find is the one you want.
- **4.1** — set `MAX_ATTEMPTS` from the daily allowance rather than from taste, and show the
  arithmetic. Day 21 asked for this; today you have the ledger to do it with.
- **4.2** — wrap the model client so the increment happens in **one** place, beside the call, and grep
  the repository to prove there is no second increment anywhere.
- **5.1** — choose Sutra's unit of fairness (user, workload class, feature) and say which of the two
  failures you are buying. Then implement a floor plus a shared surplus, and see whether the totals
  meet in the middle.
- **5.2** — list every desk function as *needs the model*, *nice to have it*, or *does not need it*.
  The third column is your degradation path. Then turn the raw refusal string into a customer-facing
  sentence, using Day 21's `public_message`.
- **The paper** — move `ARRIVALS` away from the window boundary and run both arms again. The fixed
  window now behaves; say why that is the reason this bug survives testing.

---

## §5 The eval that must be able to fail

Eight cases over the ledger, **no key, no network and no sleeping** — every `now` is a number the test
chose. All are shown with their walkthrough in
[3.3](parts/03-counting-before-spending/3.3-testing-a-ceiling-that-bites-at-midnight.md).

They assert that an empty ledger refuses nothing, that the per-minute ceiling refuses the sixth request
and then **clears**, that the per-day ceiling refuses and does **not** clear after a minute but does
after a day, that the day refusal is reported ahead of the minute refusal when both are breached, that
the refusal names the provider, and that **every attempt is counted including the failed ones**.

**How to watch it go RED before it goes green:**

```bash
uv run python -m pytest tests/test_quota.py -q -m "not live"   # RED: no sutra/quota.py yet
# ... write the symbols from §4 ...
uv run python -m pytest tests/test_quota.py -q -m "not live"   # green
```

Then break it on purpose. Measured in the lab on 2026-09-04:

| Break this | Which cases go red | What it is telling you |
| --- | --- | --- |
| delete the per-day branch from `refusal()` | **two of eight** | the wrong ceiling gives a recoverable-sounding refusal (2.1) |
| swap the two `if`s so the minute check runs first | one of eight | *"retry in 52s"* for something that will not clear |
| prune the deque to `MINUTE` instead of `DAY` | the two daily cases | one list, two windows, and only the outer may forget (3.1) |
| increment on success instead of on attempt | the last case | five phantom requests out of sixteen (4.2) |

**The first row is the one to sit with.** The message on the failing assertion is
`gemini-3.7-flash: 20/5 per minute - 52s` — a refusal that is *technically true* and completely
misleading, telling the caller to wait fifty-two seconds for a ceiling that will still be there
tomorrow morning. That is what a wrong ceiling looks like from the outside, and only an assertion on
the **words** of the refusal catches it.

**What this suite does not catch, and the parts say so:** all eight cases call the ledger directly, so
they pass in a system where nothing ever consults it before sending. The integration test that closes
that gap runs one invocation and asserts the ledger moved — and it is Day 31's business, exactly as
[23.4.3](../day-23-testing-tools-and-callbacks/parts/04-testing-hooks/4.3-testing-that-a-hook-returns-none.md)
warned.

---

## §6 Request budget

**Free-tier Gemini**, 20 generate requests per day per model (`gemini-3.7-flash`, roster re-verified
2026-09-04).

| What | Generations |
| --- | --- |
| `count_the_cost.py` — five `count_tokens` calls | **0** |
| `history_costs_again.py` — nine `count_tokens` calls | **0** |
| the ledger's eight tests | **0** |
| five demonstration scripts, ten arms between them | **0** |
| the paper's demo, both arms | **0** |
| **Total required** | **0 of 20** |

**Zero, on the day about spending.** That is not a coincidence and it is not a dodge: `count_tokens` is
a separate endpoint on a separate quota, and everything that needed a *refusal* used the real body
captured on 2026-09-04 rather than provoking a new one.

**One number in this day is not measured and the parts say so loudly.** The per-day ceiling — 20 — came
off a live refusal. The per-minute ceiling did not; `rpm=5` is a placeholder chosen so the tests have
two ceilings to tell apart. Writing a plausible number there would have been exactly the failure
Principle 7 exists to prevent, so
[2.2](parts/02-two-ceilings/2.2-reading-the-ceiling-off-a-refusal.md) carries a `TODO` with the exact
command instead. Capturing it costs real requests, and it is the first item in the build brief.

**Cost: $0.**

---

## §7 Traps

- **A word count cannot estimate a token count.** Prose is 4.55 characters per token, a log line 2.21,
  and `"4521"` is 0.80 — fewer than one character per token (1.1).
- **`count_tokens` does not enforce the model's input limit.** It cheerfully counted 800,002 tokens on
  2026-09-04. Counting tells you the size, not whether the request is sendable (1.2).
- **Optimising prompt length buys nothing on a per-request tier.** Cut the prompt in half and you can
  still answer exactly twenty questions (1.3).
- **A refused request is not a refund.** The provider counted the attempt, so a `429` costs one of the
  twenty (1.3, 3.2).
- **Both ceilings arrive as `429 RESOURCE_EXHAUSTED`.** The only reliable discriminator is `quotaId` —
  `...PerMinute...` against `...PerDay...` (2.1, 2.2).
- **`retryDelay` on the daily ceiling is a backoff hint, not a window reset.** Day 21 obeyed it
  twenty-eight times across a quarter of an hour and was refused every time (2.1, `ADR-0007`).
- **`quotaValue` arrives as a string.** `"20" == 20` is `False`, forever, and produces a check that
  never fires (2.2).
- **Check the day ceiling before the minute ceiling.** Both breached, minute reported first, and the
  caller is told to wait fifty-two seconds for something that will not clear (2.1, 3.3).
- **Prune the deque to `DAY`, never to the window asked for.** One list, two windows, and pruning to
  the minute destroys the daily count (3.1).
- **A mutable class attribute makes every provider's ledger the same ledger.** The dataclass field
  version raises; a plain `class Ledger: spent = deque()` does not (3.1).
- **Increment on attempt, not on success.** Counting successes lost five requests out of sixteen and
  the local check then waves through requests the provider will refuse (4.2).
- **The local check is an optimisation, not an authority.** The quota is per **project**: a notebook, a
  staging deployment and a demo are all spending it too (3.2, 5.1).

---

## §8 Verify before you code

Fetched, run or read on **2026-09-04**, the day this was written:

- `client.models.count_tokens(model="gemini-3.7-flash", ...)` — run live against five samples and a
  nine-step conversation. Every number in section 1 is its output. Confirmed to work **while
  `generate_content` was refusing with a `429`**, which is the fact section 1 rests on.
- `client.models.list()` — 55 models visible, `gemini-3.7-flash` still among them, so Day 9's pin
  holds. This is Addendum 02's "look up the provider's current free list" carried out rather than
  assumed.
- A live `429` body, captured whole, carrying `quotaMetric`,
  `quotaId: 'GenerateRequestsPerDayPerProjectPerModel-FreeTier'`,
  `quotaDimensions: {'model': 'gemini-3.7-flash', 'location': 'global'}`, `quotaValue: '20'` and
  `retryDelay: '26s'`. Every number in section 2 comes from it.
- A live `404` from `count_tokens` against a model that does not exist, for
  [1.1](parts/01-what-a-request-costs/1.1-a-ticket-id-costs-five-tokens.md)'s *When it breaks* — real
  text, not a paraphrase.
- `count_tokens` against 5.6 million characters, which returned `800002` rather than an error — the
  measured basis for the trap above.
- Python's own behaviour, checked by running it: that a `deque` default in a dataclass field raises
  `ValueError: mutable default ... use default_factory`, and that a plain class attribute does not.
- `https://api.crossref.org/works/10.1109/MCOM.1986.1092946` — the paper's exact title, journal,
  volume, issue, pages and year, from the machine-readable record rather than from memory
  (§17.4.1 rule 5).

**No adk.dev page was needed today.** The day's subject is the provider's quota and the standard
library; the one ADK-adjacent claim — that the budget check belongs in `before_model_callback` — reuses
the hook signatures verified on Day 21 and Day 23 against the installed package.

---

## §9 Say it in an interview

"We were on a free tier — twenty model requests a day — and nothing in the codebase knew that number.
The first thing I did was find out what was actually being metered, because that decides everything
else. It wasn't tokens. The refusal names its own quota metric, and it said *requests*, per day, per
project, per model, limit twenty. So all the obvious optimisations — shorter prompts, tighter
instructions — were worth exactly nothing, and the only levers were fewer calls, a different provider,
or later.

The measurement that changed how I thought about it was the conversation one. Eight turns, 151 tokens
of actual text, 786 tokens charged, because a chat model is stateless and every turn re-sends the whole
transcript. In request terms that's eight of the twenty for one conversation — two and a half
conversations a day.

Two things I'd tell anyone building this. First, there are two ceilings and they arrive as the same
HTTP 429: a per-minute one that refills on its own and a per-day one that doesn't. You have to read the
quota id in the body to tell them apart, because retrying the daily one costs three requests instead of
one and returns the same sentence each time. And the `retryDelay` field in that body is a backoff hint,
not a window reset — we had requests obeying it for a quarter of an hour and being refused every time.

Second, count attempts, not successes. We simulated a normal day — twelve questions, three of them
retried, one filtered — and a success-counting ledger said eleven requests used when the provider had
counted sixteen. It believed nine remained when four did, so the local budget check was waving through
requests that were about to be refused, and each of those refusals cost a request too.

The thing I'm proudest of is what we didn't write down. The daily ceiling came off a real refusal so
it's a fact. The per-minute one we never captured, so it's still a TODO with the exact command in it
rather than a plausible number in a constant — because a made-up limit that's too high spends real
requests discovering it."

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked and `./m depth 24` is green. Defined by
understanding and green checks, never by elapsed time — a part is finished when you could explain it to
someone else without the page open.

**This is the last day of Phase 3.** Its gate is *state survives restarts; budgets enforced*, and the
second half of that sentence is what today built — with one honest gap, named in the build brief: the
ledger does not yet survive a restart itself.

---

## §11 Ledger & commit

**`docs/PROGRESS.md`** — append:

```text
| 24 | <date> | OPS-07, AG-11 | 13 (+1 paper) | <hash> | ✅ |
```

**`docs/PACKAGES.md`** — no new package rows. One **quota** row is expected once
[2.2](parts/02-two-ceilings/2.2-reading-the-ceiling-off-a-refusal.md)'s `TODO` is done:

```text
| gemini-3.7-flash (quota) | RPM = TODO(capture a per-minute 429; see day 24 part 2.2) | <date> | 24 | Per-day is already recorded above at 20, read off a live refusal on 2026-08-25 and re-confirmed 2026-09-04. |
```

**`docs/PAPERS.md`** — append:

```text
| New directions in communications (or which way to the information age?) | doi:10.1109/MCOM.1986.1092946 | 1986 | 2026-09-04 | 24 | `days/day-24-token-accounting-and-budgets/papers/01-the-leaky-bucket.md` |
```

**`docs/SKILL_PROVENANCE.md`** — no new rows. No skills were sourced today.

**The commit:**

```text
day 24: token accounting and budgets - denominated in quota, not dollars - closes OPS-07, AG-11
```
