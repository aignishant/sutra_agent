---
day: 72
phase: 10
phase_name: "Safety and security"
title: "Backoff with honesty — retry-after, 1→2→4→8s, escalate after N; never invent a result"
ids: ["SEC-15", "OPS-13"]
principles: [1, 2, 4, 7, 8, 10, 11, 13, 15, 16, 17, 18]
kind: build
plan_version: "v2.2.1"
parts: 12
generated: "2026-09-06"
status: written
lab_scaffolded: true
commit: ""
---

# Day 72 — Backoff with honesty

> **Yesterday (Day 71):** computer use and the sandbox. A browser agent against a local fixture, a
> surface of fifteen declared actions, and a door outside every tool — plus the discovery that ADK's
> own `navigate` guard is default-closed and its opt-out is all-or-nothing.
> **Today:** Phase 10 closes on the smallest-looking subject in it. Everything in this phase has been
> about what a system does when it is attacked. This is about what it does when it is simply
> **refused** — and the failure is not the refusal, it is the sentence the code says afterwards.
> **Tomorrow (Day 73):** Phase 11 opens with ambient agents — the nightly job that re-indexes, runs
> the full evals and writes a digest.

---

## §1 Where we are

Day 70 built a router that reads a 429 and marks a lane cold. Its part 4.2 was explicit that this is
only half the answer: the router's cold-lane rule is one mechanism, the **caller's backoff ladder**
is another, and it said Day 72 owns the second. This is that day.

The ladder itself is not controversial. Wait about a second, then double: 1, 2, 4, 8. Google's own
troubleshooting guidance for `429 RESOURCE_EXHAUSTED` and `503 UNAVAILABLE` says exactly that shape,
and it is measured here rather than assumed — within a six-attempt budget the ladder **succeeds**
against a window that opens at ten seconds while retrying every second **gives up**, because doubling
reaches `t=15s` and flat retry reaches `t=5s`.

Three things beyond the ladder are what make the day worth a day.

**The server usually knows the answer.** A `retry-after` is not a hint about congestion; it is the
provider stating when its own window opens. Honouring it succeeds in **2 attempts with 1 wasted
request**; ignoring it and using the ladder instead gives up after **6 attempts and 6 wasted
requests** against the identical provider. Your ladder is a guess at a number somebody already told
you.

**Every retry loop has a line after it**, and there are exactly two things that line can do: raise,
or return something that looks like an answer. The second is not written by liars — it is a default
in an `except` branch, put there by somebody being defensive — and it is the whole of Principle 10.
The lab's two arms exit `0` for refusing correctly and `1` for answering from nowhere.

**And backoff spreads one client out in time while doing nothing to spread clients out from each
other.** Forty clients computing the same ladder from the same start arrive at **six distinct
instants**; one multiplication takes that to **123**, and leaves the first burst exactly where it was.

---

## §2 The map

Five sections. Section 1 is the ladder and why doubling. Section 2 is the number the server gave you,
which beats the ladder whenever it exists. Section 3 is the line after the loop. Section 4 is what
happens when everybody backs off at once. Section 5 is the framework's own retry plugin, and what to
watch when retries are working.

### 1 — The ladder

*Why doubling, what it buys, and where it has to stop.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [Why doubling](parts/01-the-ladder/1.1-why-doubling.md) | Doubling is a search over an unknown wait, not politeness | `foundation` |
| 1.2 | [The ladder measured](parts/01-the-ladder/1.2-the-ladder-measured.md) | The ladder succeeds where flat retry gives up, in the same budget | `working` |
| 1.3 | [The last rung](parts/01-the-ladder/1.3-the-last-rung.md) | A budget and a cap are decisions somebody has to write down | `working` |

### 2 — The number the server gave you

*A `retry-after` is a fact; your ladder is a guess at that fact.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [`retry-after` beats your ladder](parts/02-the-number-the-server-gave-you/2.1-retry-after-beats-your-ladder.md) | 2 attempts and 1 wasted request against 6 and 6 | `working` |
| 2.2 | [When it is absent](parts/02-the-number-the-server-gave-you/2.2-when-it-is-absent.md) | The ladder is the fallback, not the default | `working` |
| 2.3 | [Zero is not absent](parts/02-the-number-the-server-gave-you/2.3-zero-is-not-absent.md) | 💥 A falsy check turns "the server said nothing" into "retry now" | `production` |

### 3 — After the last retry

*The line after the loop, and which calls may be on it at all.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [Escalate, never invent](parts/03-after-the-last-retry/3.1-escalate-never-invent.md) | 💥 A default in an `except` branch is indistinguishable from an answer | `production` |
| 3.2 | [Which calls are safe to retry](parts/03-after-the-last-retry/3.2-which-calls-are-safe-to-retry.md) | A refusal means *not done*; a timeout means *unknown* | `production` |

### 4 — Everyone at once

*Backoff spreads a client in time and does nothing about the other clients.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [The herd](parts/04-everyone-at-once/4.1-the-herd.md) | 💥 Forty clients, six distinct instants, forty requests in each | `production` |
| 4.2 | [One multiplication](parts/04-everyone-at-once/4.2-one-multiplication.md) | Jitter fixes the retries and leaves the first attempt alone | `production` |

### 5 — In production

*The framework's retry plugin, and what to watch when retrying is working.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [The plugin that asks the model](parts/05-in-production/5.1-the-plugin-that-asks-the-model.md) | 4 model calls against 1, for a refusal no rephrasing could fix | `production` |
| 5.2 | [What to alert on](parts/05-in-production/5.2-what-to-alert-on.md) | Retries hide errors, so the signal is escalations and wasted requests | `production` |

### The paper — read it last

*Principle 4 at the scale of a day: build the ladder, then read where it came from.*

| # | Paper | What it answers |
| --- | --- | --- |
| 01 | [Ethernet: distributed packet switching for local computer networks](papers/01-binary-exponential-backoff.md) | `doi:10.1145/360248.360253` — where 1→2→4→8 comes from, and the ingredient this day's ladder drops |

---

## §3 Setup — run this

```bash
mkdir -p days/day-72-backoff-with-honesty/lab/papers/binary-exponential-backoff
cd days/day-72-backoff-with-honesty/lab
touch _provider.py _fake.py
touch ladder.py retryafter.py honest.py jitter.py builtin.py gate.py
touch papers/binary-exponential-backoff/channel.py papers/binary-exponential-backoff/demo.py
```

**What each file is for:**

- `_provider.py` is the accounting and the file to read first: a `Clock` the test moves by hand, a
  `Refused` that carries what the server said, an `Unavailable` that deliberately does not, and a
  `Provider` that counts **attempts** rather than successes.
- `_fake.py` is a `BaseLlm` that counts its own calls, so section 5 can measure what a retry strategy
  spends in the currency Addendum 02 cares about.
- `ladder.py`, `retryafter.py`, `honest.py` and `jitter.py` are the four measurements, one per
  section.
- `builtin.py` runs ADK's own `ReflectAndRetryToolPlugin` against a 429.
- `gate.py` is the eval.

Verify the lab is gitignored before the first run:

```bash
git check-ignore -v days/day-72-backoff-with-honesty/lab/_provider.py
```

**Why:**

- `days/*/lab/` is ignored repo-wide (Principle 9). Nothing today writes customer-shaped text, and
  the habit is the point — every day in this phase checked the same thing.

**No package is added today.** `git diff pyproject.toml uv.lock` must be empty and stay empty.

---

## §4 Build brief

**`sutra/backoff.py`** — the retry helper every model call and tool call in the repo will route
through.

- `TODO(me)`: `with_backoff(call, *, attempts)` — an explicit attempt budget in the signature, because
  a retry loop with no budget never escalates and the gate checks for it.
- `TODO(me)`: honour `retry-after` when the refusal carries one and fall back to the ladder when it
  does not — and use `is not None` rather than a truthiness test, for the reason part 2.3 measures.
- `TODO(me)`: an `Escalated` exception carrying `attempts` and `waited`, raised when the budget runs
  out. Never a default. Part 3.1 is the argument and Principle 10 is the rule.
- `TODO(me)`: jitter, and decide the range. The lab uses `0.5 + random()`; full jitter over the whole
  interval is the more common recommendation. Pick one and say why in the docstring.
- `TODO(me)`: decide which exception types are retryable at all. Part 3.2 is why `Refused` and
  `Unavailable` cannot share a policy.

**`tests/test_backoff.py`**

- `TODO(me)`: a test that an exhausted budget **raises** rather than returning anything. That single
  test is the difference between this module and the failure in part 3.1.
- `TODO(me)`: a test that a refusal carrying `retry_after=0.0` is honoured as zero rather than treated
  as absent — part 2.3's bug, as a test that can go red.
- `TODO(me)`: a test that `Escalated` carries what was tried, because the gate checks the fields and
  an error with no evidence cannot be acted on.

---

## §5 The eval that must be able to fail

```bash
cd days/day-72-backoff-with-honesty/lab
uv run python gate.py; echo "exit: $?"
```

Six checks against `sutra/backoff.py`, all red today because the module is the build brief. A check
that cannot run counts as a **failure** rather than as skipped (Principle 11).

The red-alarm test is `honest.py`, and it is unusual in this repository because its two arms encode
the verdict in the exit code:

```bash
uv run python honest.py; echo "exit: $?"
uv run python honest.py --invent; echo "exit: $?"
```

The first exits `0` — refusing correctly is success. The second exits `1` — a plausible answer from
nowhere is the failure. If those ever agree, Principle 10 has stopped being enforced anywhere in this
repository. Three more ablations exist and are exercised in their parts: `ladder.py --flat`,
`retryafter.py --ladder` and `jitter.py --jitter`.

---

## §6 Request budget

**Zero provider requests, to every provider.**

| Provider | Requests today | Against |
| --- | --- | --- |
| Google AI Studio (Gemini) | 0 | free tier |
| Groq | 0 | 30 RPM / 250 RPD, observed 2026-09-05 |
| OpenRouter `:free` | 0 | free tier |
| Ollama (local) | 0 | n/a |

Every wait in this day is `Clock.sleep`, which adds to a number instead of sleeping — the only way to
watch a sixteen-second ladder without waiting sixteen seconds, and the only way for two runs to agree
on a slow machine and a fast one. `_fake.py`'s model is a real `BaseLlm` subclass so that section 5's
plugin measurement runs inside the real runtime; it contacts nothing.

The numbers the day **reports** are real costs — part 5.1's four model calls are four requests the
desk would have spent against a provider — because a retry policy priced in imaginary units cannot be
compared with another one.

---

## §7 Traps

1. **Retrying at a fixed interval.** Within the same attempt budget it reaches a fraction as far
   through time, and gives up on a window the ladder would have caught — part 1.2.
2. **Doubling without a cap.** The tenth rung is over eight minutes, which is a delay nobody meant to
   schedule — part 1.3.
3. **Retrying with no attempt budget.** A loop that never exhausts never escalates, so the failure
   never reaches a person — parts 1.3 and 3.1.
4. **Ignoring `retry-after`.** The server told you when its window opens; the ladder is your guess at
   that same number — part 2.1.
5. **`refusal.retry_after or default`.** A falsy check turns a stated `0` into "the server said
   nothing", which is the same shape as Day 67's empty-dict refusal — part 2.3.
6. **A default in the `except` branch.** Nothing downstream can tell it from an answer, and nothing in
   the log says the provider was never reached — part 3.1, Principle 10.
7. **Retrying a non-idempotent call after a timeout.** A refusal means the request was not performed;
   a timeout means you do not know — part 3.2.
8. **Assuming backoff spreads clients out.** They all compute the same ladder from the same start, so
   forty clients arrive together six times — part 4.1.
9. **Adding jitter and thinking the herd is solved.** Jitter delays a retry and nothing delays the
   first attempt — part 4.2.
10. **Reaching for the framework's retry plugin on a 429.** It hands the error to the model to reflect
    on, which spends model calls rephrasing something that was never wrong — part 5.1.
11. **Alerting on the error rate.** A system that retries successfully reports no errors at all; watch
    escalations and wasted requests — part 5.2.

---

## §8 Verify before you code

Fetched on 2026-09-06:

| What | Where | What it said |
| --- | --- | --- |
| Backoff guidance for 429/503 | <https://ai.google.dev/gemini-api/docs/troubleshooting> | the recommended shape for `RESOURCE_EXHAUSTED` and `UNAVAILABLE` — checked on the day it is used, and part 1.1 records what the page actually said rather than what this table remembers |
| `ReflectAndRetryToolPlugin` | installed `google-adk==2.7.1` | constructor is `(name, max_retries=3, throw_exception_if_retry_exceeded=True, tracking_scope=TrackingScope.INVOCATION)`; its own docstring describes it as self-healing recovery that hands the error back to the model — part 5.1 quotes it and measures it |
| Error hook signatures | installed `google-adk==2.7.1` | `on_model_error_callback(*, callback_context, llm_request, error)` and `on_tool_error_callback(*, tool, tool_args, tool_context, error)` — keyword-only, as Day 67 part 2.4 found for every callback |
| `doi:10.1145/360248.360253` record | <https://api.crossref.org/works/10.1145/360248.360253> | the record splits the title: `title: ["Ethernet"]` plus `subtitle: ["distributed packet switching for local computer networks"]`. The paper document assembles both and says so (§17.4.1 rule 5) |

**No ADK symbol is used outside section 5.** Sections 1 to 4 are arithmetic over a simulated provider
and a hand-moved clock, deliberately, so the day's core measurements do not depend on a framework
version at all.

---

## §9 Say it in an interview

*"Retry policy sounds like a solved problem and the interesting part is the line after the loop. We
built the usual ladder — one second, then double — and measured it, which was worth doing: within the
same six-attempt budget, doubling reached fifteen seconds and succeeded where retrying every second
reached five and gave up. But the ladder is a guess at a number the server usually tells you.
Honouring `retry-after` took the same scenario from six attempts and six wasted requests down to two
attempts and one. The subtle bug there is a falsy check — `retry_after or default` treats a stated
zero as 'the server said nothing', and zero and absent are different facts. Then the part that
actually matters: every retry loop ends, and the code on the next line either raises or returns
something. We had a default in an except branch returning 'no incidents reported', which is
indistinguishable downstream from a real answer and appears in no log as a failure. And backoff
doesn't do what people think about crowds — it spreads one client out in time and does nothing to
spread clients apart, because they all compute the same ladder from the same start. Forty clients hit
six distinct instants; jitter took that to a hundred and twenty-three, and left the first burst
exactly where it was, which needs a different fix."*

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked, and you have run the commands rather than read
them. `./m done 72` refuses to commit until they are.

The day is finished when you can say what your code does on the line after the retry loop without
opening the file — and when you can explain why a system that retries well reports no errors and is
therefore harder to monitor, not easier.

---

## §11 Ledger & commit

**`docs/PROGRESS.md`** — append this row:

```text
| 72 | 2026-09-06 | SEC-15, OPS-13 | 12 | <hash> | ⚠️ |
```

The gate column is `⚠️` and means it. `./m depth 72` is green over the twelve parts and the paper.
`lab/gate.py` is **red** on all six checks by design — `sutra/backoff.py` is the build brief. This is
the last day of Phase 10; the phase's gate was *injection attempts contained; quota router live*, and
both halves land when the Day 70 and Day 72 build briefs are written. The repository-wide `⚠️`
carried since Day 15 is unchanged.

**`docs/PACKAGES.md`** — no new rows. No package is added today.

**`docs/PAPERS.md`** — one row, checked live today:

```text
| Ethernet: distributed packet switching for local computer networks | doi:10.1145/360248.360253 | 1976 | 2026-09-06 | 72 | `days/day-72-backoff-with-honesty/papers/01-binary-exponential-backoff.md` |
```

**`docs/SKILL_PROVENANCE.md`** — no new rows.

**Commit:**

```text
day 72: backoff with honesty - retry-after, the ladder, and the line after the loop - closes SEC-15, OPS-13
```
