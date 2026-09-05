---
day: 52
phase: 7
phase_name: "Memory and retrieval"
title: "Phase gate — memory wired into the triage flow"
ids: ["AG-15"]
principles: [1, 2, 4, 7, 8, 10, 11, 13, 14, 15, 16, 17, 18]
kind: gate
plan_version: "v2.2.1"
parts: 19
generated: "2026-09-05"
status: written
lab_scaffolded: true
commit: ""
---

# Day 52 — Phase gate: memory wired into the triage flow

> **Yesterday (Day 51):** caching. Context and response caching priced as the quota lifeline, which
> is the last piece Phase 7 needed and the last one measured on a bench of its own.
> **Today:** the pieces stand in a line for the first time. A conversation closes, the policy judges
> it, redaction runs before anything is stored, the survivors join the archive in one index, and a
> real question goes in the front door. Eleven criteria, written before anybody looked, and an
> honest column for the ones that come back amber.
> **Tomorrow (Day 53):** Phase 8 opens on the graph Workflow Runtime, where four of the steps you
> measured today become nodes — and where trap number one is waiting for anybody who composes them
> the 1.x way.

---

## §1 Where we are

Six days ago this phase started with a sentence rather than a feature: *"have we seen anything like
this before?"* Everything since has been machinery for answering it. Day 46 drew the line between a
conversation and a memory. Day 47 made the conversation survive a restart. Day 48 wrote the rules
for what may be kept. Day 49 built retrieval. Day 50 chose the numbers retrieval runs on. Day 51
priced the caching that keeps it free.

Six benches, six sets of measurements, and not one line anywhere that runs them in order.

Think of a stock room at the back of a shop. The shelves are labelled, the ladder is on its hook,
the floor is swept and the temperature log has been signed every morning this month. An inspection
would find nothing to write down. And whether there is any stock on the shelves is not a question an
inspection asks, because it is not a property of the room — it is something you have to arrive
already knowing the answer to.

Today is the day somebody arrives knowing. Not *"is the machinery healthy?"* but *"is the thing we
filed on Wednesday findable on Thursday, and does the desk answer with the fix rather than with the
complaint?"* Those are questions with numbers behind them, and the numbers are the point: `0.439`
against `0.345`; `9/10` answered where the unranked path gets `0/10`; four rows in a store whose
absence would leave every dashboard green.

A gate is also the day you write down what you did **not** check. Three of this day's rows come back
amber — a framework one minor version behind, a free-tier limit that has moved behind a login, two
provider rosters that need a session — and amber is a result, not a gap in the paperwork. The gate
that turns four unrun checks into a green tick has replaced a measurement with an opinion, which is
the exact failure the whole day exists to prevent.

---

## §2 The map

Nineteen parts in seven sections. The day climbs from what a gate *is*, through the eleven criteria
in the order the phase actually runs, into three deliberate failures, and out at the boundary.

### Section 1 — the promise

*What this gate is asking, and why it is a different activity from Day 45's audit.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [The sentence the phase promised](parts/01-the-promise/1.1-the-sentence-the-phase-promised.md) | What was Phase 7 for, and what does the desk return with and without it? | `foundation` |
| 1.2 | [A gate is not an audit](parts/01-the-promise/1.2-a-gate-is-not-an-audit.md) | Why a promise checked end to end is not a component checked against rules — and why amber is a legal result | `foundation` |

### Section 2 — the run

*The two criteria about the answer a support agent is actually handed.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [G01 — the question, answered end to end](parts/02-the-run/2.1-the-question-answered-end-to-end.md) | Does the memo beat the archive, and how do you know it was the memo? | `working` |
| 2.2 | [G02 — an answer that names its source](parts/02-the-run/2.2-an-answer-that-names-its-source.md) | Why an uncited answer is exactly as fluent and cannot be checked | `working` |

### Section 3 — the write path

*Three criteria about what enters memory, in what shape, and under whose rule.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [G03 — nothing is filed unless a line files it](parts/03-the-write-path/3.1-nothing-is-filed-unless-a-line-files-it.md) | The arithmetic identity that makes an empty store detectable | `working` |
| 3.2 | [G04 — every memo names the rule that kept it](parts/03-the-write-path/3.2-every-memo-names-the-rule-that-kept-it.md) | Why a stored item without its rule cannot be reviewed or appealed | `working` |
| 3.3 | [G05 — nothing personal reached the store](parts/03-the-write-path/3.3-nothing-personal-reached-the-store.md) | Redaction on the way in, checked against the store and not the code | `working` |

### Section 4 — the read path

*Three criteria about what comes back, how it was ranked, and what happens when nothing does.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [G06 — the ranked path is the one that ships](parts/04-the-read-path/4.1-the-ranked-path-is-the-one-that-ships.md) | Three read paths, one table, and the real answer the floor costs | `working` |
| 4.2 | [G07 — every constant names its run](parts/04-the-read-path/4.2-every-constant-names-its-run.md) | Why a tuned number without its measurement is a thermostat set to 22 | `production` |
| 4.3 | [G08 — nothing, said out loud](parts/04-the-read-path/4.3-nothing-said-out-loud.md) | The sentence a miss produces, and the sentence it must never be | `working` |

### Section 5 — the zero claim

*Three criteria that turn "answered at $0" from a slogan into arithmetic.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [G09 — counted during the run, not after](parts/05-the-zero-claim/5.1-counted-during-the-run-not-after.md) | Provider requests against model requests, both counted rather than asserted | `production` |
| 5.2 | [G10 — the lane we did not buy](parts/05-the-zero-claim/5.2-the-lane-we-did-not-buy.md) | What the hosted embedding lane would cost, priced without spending a request | `production` |
| 5.3 | [G11 — what a cache can and cannot reach](parts/05-the-zero-claim/5.3-what-a-cache-can-and-cannot-reach.md) | Why retrieval grew the half of the request no cache can touch | `production` |

### Section 6 — the failure lab

*Three failures reached on purpose, each of which produces no error at all.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 6.1 | [💥 The store that was never filled](parts/06-failure-lab/6.1-the-store-that-was-never-filled.md) | Why every health signal is identical on an empty memory | `production` |
| 6.2 | [💥 The memo that could not be found](parts/06-failure-lab/6.2-the-memo-that-could-not-be-found.md) | A live memo, unreachable, with the same top answer either way | `production` |
| 6.3 | [💥 Green because nothing existed](parts/06-failure-lab/6.3-green-because-nothing-existed.md) | Three lines between a gate and a green badge | `production` |

### Section 7 — the phase boundary

*The rituals plan section 15 requires, and the handover to Phase 8.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 7.1 | [The freshness re-check](parts/07-the-phase-boundary/7.1-the-freshness-recheck.md) | The four external things re-read, what came back, and the pin with no ledger row | `production` |
| 7.2 | [Six conditions, and the one that is amber](parts/07-the-phase-boundary/7.2-six-conditions-and-the-one-that-is-amber.md) | Plan section 15's six rules, checked, with the honest verdict | `production` |
| 7.3 | [What Phase 8 inherits](parts/07-the-phase-boundary/7.3-what-phase-eight-inherits.md) | Which of the four steps can become a node, and which two cannot | `production` |

> This day carries no `papers/` directory: it teaches no paper of its own. The four it leans on were
> taught on Days 46, 47 and 49, and [7.3](parts/07-the-phase-boundary/7.3-what-phase-eight-inherits.md)
> ends by listing them for re-reading now that the whole phase runs end to end.

---

## §3 Setup — run this

No package is added today. The whole day is standard library plus what Days 46 to 51 already
installed, and `git diff pyproject.toml uv.lock` must stay empty.

```bash
mkdir -p days/day-52-memory-in-triage-flow/lab
cd days/day-52-memory-in-triage-flow/lab

# the two fixtures, copied from Day 50 so today's numbers are comparable with yesterday's
cp ../../day-50-chunking-and-top-k/lab/_archive.py .
cp ../../day-50-chunking-and-top-k/lab/_index.py .

# this week's closed conversations, and the phase wired end to end
touch _conversations.py _phase7.py

# one script per criterion, plus the three failure-lab runs and the three boundary runs
touch endtoend.py cite.py
touch filed.py ruled.py redacted.py
touch ranked.py constants.py saidnothing.py
touch budget.py indexcost.py cacheprefix.py
touch emptystore.py staleindex.py greenonnothing.py
touch freshness.py ids.py handover.py

# the gate itself
touch gate.py
```

Then, from the repository root, prove the gate is red before you write anything:

```bash
uv run python days/day-52-memory-in-triage-flow/lab/gate.py; echo "exit: $?"
```

Verified on 2026-09-05: `google-adk==2.7.1`, `google-genai==2.19.0`, `mcp==1.29.1`, Python 3.12.
None of them is imported by anything in this day's lab.

---

## §4 Build brief

### The project code — the five modules Phase 7 asked for, and you type every line

Today writes no new module. It is the day the five that Days 46 to 50 specified have to exist
together, and `lab/gate.py` is the list:

| Module | Symbols the gate looks for | Asked for by |
| --- | --- | --- |
| `sutra/memory/service.py` | `build_memory_service`, `MEMORY_TOOLS`, `TOP_K` | Day 46 |
| `sutra/memory/persistence.py` | `SESSION_DB`, `session_service`, `purge_user` | Day 47 |
| `sutra/memory/policy.py` | `RETENTION`, `RULES`, `PII_PATTERNS`, `what_to_keep`, `what_to_forget`, `survivors` | Day 48 |
| `sutra/retrieval.py` | `build_index`, `search`, `chunk_document`, `chunked_rows`, `parent_ref`, `retrieve` | Days 49, 50 |
| `sutra/retrieval.py` | `CHUNK_SIZE`, `CHUNK_OVERLAP`, `TOP_K`, `SIM_FLOOR`, `MIN_SHARED_TERMS` | Day 50 |

**`TODO(me)` markers left for you:**

- **4.2** — decide **which module owns `TOP_K`**. Day 46 puts one in `sutra/memory/service.py`, sized
  against a token budget; Day 50 puts one in `sutra/retrieval.py`, read off an answer-rate curve.
  Make one import the other, and write the one-sentence reason in the comment beside the owner.
  Until you do, `gate.py` reports two modules disagreeing about one number.
- **7.3** — make the write path node-shaped before Day 58 wraps it. `what_to_keep` and
  `what_to_forget` both reach module-level `RULES`; add it as a keyword argument with a default so
  no call site changes, and say in a comment what the default has to be for that to hold.
- **3.3** — write down the PII classes this project does **not** cover. The two patterns handle email
  and phone. Account numbers, postcodes, national identifiers and names are not covered, and an
  uncovered class is a claim you never made rather than a bug you find later.
- **5.3** — write the desk's standing instruction, in full. The shape is fixed by
  [5.3](parts/05-the-zero-claim/5.3-what-a-cache-can-and-cannot-reach.md) — one constant, in front,
  ending with the sentence that hands over to the retrieved rows — and the wording is yours.
- **6.1** — design the **canary memo**: a synthetic memo the system files itself, under a holder that
  is not a customer, with a retention rule that can never expire it and a subject nothing can
  supersede. Then decide where the reachability check runs and how often.
- **6.2** — add the two fields to the index file: the newest source timestamp it saw, and the row
  count at build time. Both must come from the data, never from `datetime.now()`. Then decide what
  the search does when the store is newer than the index — refuse, or warn.
- **7.1** — write the missing `docs/PACKAGES.md` row for `mcp==1.29.1` (the snippet is in §11), then
  decide whether the pin-versus-ledger check belongs in `./m check`.
- **7.1** — re-verify the Gemini free-tier embedding limit. The public rate-limits page no longer
  publishes per-model numbers; open the AI Studio rate-limit page while signed in, record what it
  says with the date, and correct
  [5.2](parts/05-the-zero-claim/5.2-the-lane-we-did-not-buy.md)'s arithmetic if it has moved.
- **7.2** — run `./m check` and record its result. This day cannot tick plan section 15 rule 3 for
  you; a known-red lint elsewhere in the repository is named in §7 and it is yours to clear.

### The tests — `tests/test_memory_flow.py`, and you type every line

`gate.py` reports `G11: tests/test_memory_flow.py does not exist` until this file does. Five test
functions, named as sentences, all offline and all fast:

| Test | What it pins |
| --- | --- |
| `test_a_filed_memo_is_reachable_by_ref` | 6.1's canary check, as a test |
| `test_proposed_equals_kept_plus_refused` | 3.1's identity |
| `test_no_stored_row_matches_a_pii_pattern` | 3.3, run against the store |
| `test_an_unanswerable_question_returns_no_rows` | 4.3, and it must assert `== []`, not falsiness |
| `test_the_shipped_read_path_rejects_every_impostor` | 4.1's third column |

---

## §5 The eval that must be able to fail

`lab/gate.py`. Eleven criteria, zero model calls, zero network requests, and an exit code.

```bash
uv run python days/day-52-memory-in-triage-flow/lab/gate.py; echo "exit: $?"
```

It is **red as shipped**, and this is what it says on 2026-09-05:

```text
G01: sutra.memory.service (Day 46) is not importable: No module named 'sutra.memory'
G01: sutra.memory.persistence (Day 47) is not importable: No module named 'sutra.memory'
G01: sutra.memory.policy (Day 48) is not importable: No module named 'sutra.memory'
G01: sutra.retrieval (Days 49 and 50) is not importable: No module named 'sutra.retrieval'
G10: mcp is pinned in pyproject.toml with no row in PACKAGES.md
G11: tests/test_memory_flow.py does not exist
findings: 6
exit: 1
```

Four findings are the modules you have not written yet. The fifth is a real Principle 7 violation the
gate found on its first run. The sixth is the test file above.

**Break it on purpose once:** open `lab/greenonnothing.py`, run it without `--strict`, and watch the
same repository report `PHASE 7 GREEN` with exit `0`. Three lines separate the two implementations,
and [6.3](parts/06-failure-lab/6.3-green-because-nothing-existed.md) is what those three lines are.

---

## §6 Request budget

**Zero requests to any provider.** Not "nearly zero" — zero, counted during a run rather than
asserted afterwards.

| Provider | RPM used | RPD used |
| --- | --- | --- |
| Gemini free tier | 0 | 0 |
| Groq free tier | 0 | 0 |
| OpenRouter `:free` | 0 | 0 |
| Ollama local | 0 | 0 |

Counted by `lab/budget.py` over the full fourteen-question pass: fourteen retrieval calls, zero
network requests, fourteen model requests — all fourteen served by `CountingModel`, a dozen lines of
string formatting that never opens a socket. In production those fourteen become fourteen real calls
against a free tier; the number is printed as itself rather than rounded to zero, because
[5.1](parts/05-the-zero-claim/5.1-counted-during-the-run-not-after.md) is about not doing that.

The **network** requests this day makes are documentation lookups, listed in §8. They cost no model
quota and they are the plan's section 15 rule 5 ritual, not part of the desk.

---

## §7 Traps

1. **Checking the reference instead of the product.** `gate.py` imports `sutra`; the parts import
   `_phase7`. One word in one import line makes every criterion pass today, on a repository where
   `sutra/memory/` does not exist. If the gate goes green before you have written anything, this is
   why.
2. **Treating a missing target as a skip.** `except Exception: continue` turns eleven criteria into
   zero and prints a green verdict.
   [6.3](parts/06-failure-lab/6.3-green-because-nothing-existed.md) runs both versions side by side.
3. **Deleting amber.** Three of §8's rows are honestly unchecked. A tick from memory and a tick from
   a visit are indistinguishable a month later, so every row here carries a date and a result.
4. **Asserting a threshold that is a property of today's archive.** `answered@k 9/10`, `SIM_FLOOR
   0.20` and the `0.439` gap were all measured on sixty-five rows. Write criteria that *report* those
   numbers; do not assert them, or the gate goes red on the day somebody files a memo.
5. **The `mcp` pin is blocked upstream, not merely stale.** `mcp` is at `2.1.1` on PyPI and
   `google-adk` 2.8.0 declares `mcp<2,>=1.24`. Do not bump it. Write the missing ledger row instead.
6. **`./m check` is not green in this repository**, and it is not this day's doing:
   `tests/test_persona.py` fails ruff `I001` (unsorted import block), a file that last changed on Day
   15. It is the learner's own code, which a generated day may not edit. The fix is
   `uv run ruff check --fix tests/test_persona.py`, and plan section 15 rule 3 cannot be ticked until
   it is run.
7. **Two modules owning one `TOP_K`.** Day 46's and Day 50's, with different values and different
   evidence. Nothing today reconciles them; §4's first `TODO(me)` is where you do.
8. **A stale canary is worse than no canary.** If the reachability check in
   [6.1](parts/06-failure-lab/6.1-the-store-that-was-never-filled.md) names a real customer memo, it
   goes red the day that memo is superseded, twice, and then it gets deleted. Use a synthetic one.

---

## §8 Verify before you code

Every URL below was fetched on **2026-09-05**, and the result is recorded rather than assumed.

| What | URL | Result |
| --- | --- | --- |
| ADK memory service, `BaseMemoryService`, `add_session_to_memory` | `https://adk.dev/sessions/memory/` | `200`; documents all three. Verified locally too: `python -c "from google.adk.memory import BaseMemoryService; print(sorted(m for m in dir(BaseMemoryService) if not m.startswith('_')))"` lists `add_events_to_memory, add_memory, add_session_to_memory, search_memory` on `google-adk==2.7.1`, and `Runner.__init__` takes `memory_service` |
| The URL Day 46's hub cites | `https://adk.dev/docs/sessions/memory/` | **`404`** — the docs moved. A link written in a day eleven days ago no longer resolves |
| Framework releases | `https://pypi.org/pypi/google-adk/json` | latest `2.8.0`; pinned `2.7.1`. **Amber** — Principle 14 says read the notes and amend before adopting, and that is Day 53's first act |
| MCP specification revision | `https://modelcontextprotocol.io/specification/` and `/2026-07-28` | revision links end at `2026-07-28`, which returns `200`. **Green** — unchanged, so Addendum 01 Part 2 does not fire. `2026-08-30` also appears on the page and returns `404` as a revision path |
| Gemini free-tier limits | `https://ai.google.dev/gemini-api/docs/rate-limits` | `200`, last updated `2026-09-02`. Documents RPM/TPM/RPD, per project not per key, RPD resetting at midnight Pacific, and `429 RESOURCE_EXHAUSTED`. **Per-model numbers have moved**: *"For details on those rate limits, see the AI Studio Rate Limit page."* **Amber** — that page needs a session |
| `mcp` on PyPI, and what the framework allows | `https://pypi.org/pypi/mcp/json`, `https://pypi.org/pypi/google-adk/json` | `mcp` latest `2.1.1`; `google-adk` declares `mcp<2,>=1.24`. The `1.29.1` pin is **blocked upstream** |
| Groq and OpenRouter free rosters | `https://console.groq.com/settings/limits`, `https://openrouter.ai/models?q=:free` | **Amber, not checked** — both render behind a session |

---

## §9 Say it in an interview

"Phase seven of that project was memory and retrieval, and the last day of it was a gate rather than
a feature. I wrote eleven criteria before looking at anything, then ran the whole thing end to end.
The headline was one question asked twice: with the week's memos in the index the desk returned the
resolution memo at 0.439 above the original complaint at 0.345, and with the memos removed it
returned the complaint at 0.415 and nothing else — so the answer went from the symptom to the cause,
and I can point at both runs. The number I was most pleased to have measured is the ugly one: three
read paths on the same answer key give zero out of ten, ten out of ten, and nine out of ten answered,
and only the nine rejects all four questions the archive has no business answering. So I ship the
path that loses a real answer, on purpose, and I can say why. The gate also found something nobody
was looking for — a package pinned in `pyproject.toml` for seven days with no row in the package
ledger — which is the argument for writing the rules before you open the files. And three rows came
back amber: the framework is one minor behind, and the provider's free-tier numbers have moved behind
a login since we recorded them. Amber is a result. The version of that report where those are ticks
is the version I would not trust."

---

## §10 Done when

See [`CHECKLIST.md`](CHECKLIST.md). Every box is ticked because you ran the thing, not because you
read about it — and `./m done 52` refuses to commit until they are.

Phase 7 is green when plan section 15's six conditions hold, and
[7.2](parts/07-the-phase-boundary/7.2-six-conditions-and-the-one-that-is-amber.md) is where they are
checked one by one. Today's honest verdict is **not green**, for reasons that are written down rather
than glossed.

---

## §11 Ledger & commit

**`docs/PROGRESS.md`** — append this row:

```text
| 52 | 2026-09-05 | AG-15 | 19 | <hash> | ⚠️ |
```

The gate column is `⚠️` and it means it. `./m depth 52`, `./m trace` and `./m wiki --check` are
green; `./m check` is red on `tests/test_persona.py` failing ruff `I001`, which predates this day
(see §7, trap 6). It becomes `✅` when `uv run ruff check --fix tests/test_persona.py` has been run
and `./m check` passes.

**`docs/PACKAGES.md`** — the row this day's freshness check found missing. Fill in the two fields
you can only know by looking, then append it:

```text
| mcp | 1.29.1 | <the date you verify it> | 32 | The MCP SDK `sutra_mcp` is built on. Pinned since Phase 5; the row was never written, and Day 52's freshness check found the gap. `google-adk` 2.8.0 declares `mcp<2,>=1.24`, so 2.x is blocked upstream. Observed with `uv pip show mcp`. |
```

**`docs/PAPERS.md`** — no rows. This day teaches no paper; it cites four already in the ledger.

**`docs/SKILL_PROVENANCE.md`** — no rows.

**Commit:**

```text
day 52: phase gate — memory wired into the triage flow — closes AG-15
```
