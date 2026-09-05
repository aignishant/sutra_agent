---
day: 51
phase: 7
phase_name: "Memory and retrieval"
title: "Caching — context & response caching as the quota lifeline"
ids: ["ADK-31", "OPS-10"]
principles: [2, 4, 7, 8, 9, 10, 11, 13, 15, 16, 17, 18]
kind: lab
plan_version: "v2.2.1"
parts: 23
generated: "2026-09-05"
status: written
lab_scaffolded: true
commit: ""
---

# Day 51 — Caching: context and response caching as the quota lifeline

> **Yesterday (Day 50):** the three decisions Day 49 left unexamined — what you cut documents into,
> how many rows you take, and whether the question was ever a retrieval question at all. Every number
> came from a run and the day spent nothing.
> **Today:** the bill. Every request the desk sends carries 6,124 characters, of which 6,085 were
> identical last time, and the free tier allows **20 requests a day**. Two mechanisms both called
> "caching" save two different currencies, and only one of them saves the currency Sutra is rationed
> in. The day ends with an uncomfortable, measured finding about the one ADK gives us.
> **Tomorrow (Day 52):** the Phase 7 gate — memory wired into the triage flow, and *"seen anything
> like this before?"* answered at $0. Today's arithmetic is what decides whether that sentence is
> true.

---

## §1 Where we are

Phase 7 has spent six days teaching the desk to remember. Day 46 drew the line between a session and
a memory. Day 47 made sessions survive a restart. Day 48 decided what is worth keeping. Day 49 built
a ranked index over the ticket archive, and Day 50 tuned the cut, the k and the floor — and did the
whole thing for zero model calls, because chunking is a slice and ranking is a dot product.

The desk itself is not free. Every answer it gives is a generation, and the free tier this whole
curriculum runs on allows twenty of them a day.

Here is the day as a scene. There is a shop near the market that fills in government forms. The form
for a licence is four pages; three and a half of them are the same for everybody — the office address,
the eleven declarations, the list of accepted documents — and half a page is you. The man at the
counter types all four pages for every customer. He has typed the eleven declarations nine thousand
times, and nobody has ever suggested he stop, because nobody ever showed him a bill with "typing" on
it.

Sutra has that bill. Six thousand one hundred and twenty-four characters go out with every question
and thirty-nine of them are the question.

So today is about not paying twice for the same sentence. And the first thing that has to be sorted
out is that "caching" is two completely different tricks with one name. One is chopping the onions
before the lunch rush: you still cook every order, you just cook it faster. The other is making forty
plates and putting them under a cover: you do not cook at all. The first saves effort inside a job you
still do. The second saves the job. Only the second one changes the number of times you go to the
stove, and going to the stove is what Sutra is rationed on.

The day measures both, honestly, and the honest answer is not the flattering one. The cache ADK gives
us — the onions — turns out not to apply to this desk at all: our stable prefix is 1,521 tokens
against a provider floor of 4,096, which is 37% of the way there. There is a way to close that gap and
it is a retrieval architecture change wearing a caching PR's clothes. Meanwhile the cache nobody gives
us — the plates — halves the day's requests, and brings a correctness risk with it that takes five
parts to handle properly.

---

## §2 The map

Twenty-three parts in seven sections, and one paper. Section 1 separates the two caches and defines a
key. Section 2 is ADK's context cache as a mechanism. Section 3 measures Sutra against its floor and
reports what it finds. Section 4 is the ADK surface and its three numbers. Section 5 is the response
cache — the one that saves requests and the one that can be wrong. Section 6 is OPS-10: proving the
saving, logging it, and the failure none of the measurements can see. Section 7 is the production
posture and what is deliberately parked. The day climbs `foundation → working → production`.

### Section 1 — `01-two-caches-two-currencies`: what is being saved, and in what unit

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [The same sentence, paid for twice](parts/01-two-caches-two-currencies/1.1-the-same-sentence-paid-for-twice.md) | 660 + 4,952 + 512 characters, and 39 of them are new | `foundation` |
| 1.2 | [Two caches wearing one name](parts/01-two-caches-two-currencies/1.2-two-caches-wearing-one-name.md) | 99% of the characters and 0% of the requests | `foundation` |
| 1.3 | [A key is a promise about sameness](parts/01-two-caches-two-currencies/1.3-a-key-is-a-promise-about-sameness.md) | why a missing field raises the hit rate | `working` |

### Section 2 — `02-the-context-cache`: the mechanism ADK gives you

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [What ADK is willing to cache](parts/02-the-context-cache/2.1-what-adk-is-willing-to-cache.md) | the last unbroken run of user messages, and `contents[:0]` on turn one | `working` |
| 2.2 | [What a hit does to the request](parts/02-the-context-cache/2.2-what-a-hit-does-to-the-request.md) | 6,124 characters become 39, and `tools` becomes `None` | `working` |
| 2.3 | [The fingerprint is the key](parts/02-the-context-cache/2.3-the-fingerprint-is-the-key.md) | a trailing space moves it; reversing the tool list does not | `working` |
| 2.4 | [The three ways a cache dies](parts/02-the-context-cache/2.4-the-three-ways-a-cache-dies.md) | 18 deaths from reuse, 0 from the TTL everyone tunes | `working` |

### Section 3 — `03-the-floor-we-never-reach`: measuring Sutra against the limit

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [Two floors and a first-turn rule](parts/03-the-floor-we-never-reach/3.1-two-floors-and-a-first-turn-rule.md) | three gates, three log lines, three different owners | `working` |
| 3.2 | [💥 Thirty-seven per cent of the way to a cache](parts/03-the-floor-we-never-reach/3.2-thirty-seven-per-cent-of-the-way-to-a-cache.md) | 1,521 of 4,096, and the three wrong ways to close it | `production` |
| 3.3 | [What would have to change](parts/03-the-floor-we-never-reach/3.3-what-would-have-to-change.md) | the archive pasted in: 4,700 tokens, `CACHEABLE`, and four costs | `production` |

### Section 4 — `04-the-adk-config`: the surface, the metadata and the knobs

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [Where the config goes](parts/04-the-adk-config/4.1-where-the-config-goes.md) | `App`, not `LlmAgent` — trap #1 in miniature | `working` |
| 4.2 | [What the metadata says, and what it does not](parts/04-the-adk-config/4.2-what-the-metadata-says.md) | three states, not two, and where the docs page differs | `working` |
| 4.3 | [Choosing the three numbers](parts/04-the-adk-config/4.3-choosing-the-three-numbers.md) | the crossover is at 90, because 90 × 20 s is the TTL | `production` |

### Section 5 — `05-the-response-cache`: the one that saves requests, and can be wrong

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [The traffic decides the hit rate](parts/05-the-response-cache/5.1-the-traffic-decides-the-hit-rate.md) | 10 distinct questions in 60 asks, so the ceiling is 83% | `working` |
| 5.2 | [Scoping the key](parts/05-the-response-cache/5.2-scoping-the-key.md) | the tenant costs 25 points and is mandatory; the agent costs 21 and buys nothing | `working` |
| 5.3 | [💥 The key that dropped the field](parts/05-the-response-cache/5.3-the-key-that-dropped-the-field.md) | 78 → 83 → 85 → 87%, and 0 → 0 → 1 → 3 wrong | `production` |
| 5.4 | [💥 The answer that was right when it was stored](parts/05-the-response-cache/5.4-the-answer-that-was-right-when-it-was-stored.md) | 17 served, 5 wrong, no error anywhere | `production` |
| 5.5 | [A TTL is a bet](parts/05-the-response-cache/5.5-a-ttl-is-a-bet.md) | the free lunch ends at 3600 seconds | `production` |

### Section 6 — `06-proving-the-saving`: OPS-10, the report and the alarms

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 6.1 | [The saving, in the unit of the bill](parts/06-proving-the-saving/6.1-the-saving-in-the-unit-of-the-bill.md) | 6.0 days of free tier against 3.3 | `production` |
| 6.2 | [The log line and four alarms](parts/06-proving-the-saving/6.2-the-log-line-and-four-alarms.md) | five fields, and the one that is always left out | `production` |
| 6.3 | [💥 The stampede on a cold key](parts/06-proving-the-saving/6.3-the-stampede-on-a-cold-key.md) | 6 calls for one answer — 30% of the day, in nine seconds | `production` |

### Section 7 — `07-in-production`: the posture, and what is deliberately not built

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 7.1 | [What must never enter a key](parts/07-in-production/7.1-what-must-never-enter-a-key.md) | the key is published; and a hit is 400× faster than a miss | `production` |
| 7.2 | [🅿️ Eviction, shared stores and semantic caching](parts/07-in-production/7.2-eviction-shared-stores-and-semantic-caching.md) | three triggers with numbers in them | `production` |

### The paper — read it **after** the parts

| # | Paper | Why it is here |
| --- | --- | --- |
| 01 | [Evaluation techniques for storage hierarchies](papers/01-storage-hierarchies.md) · `doi:10.1147/sj.92.0078` · 1970 | one pass over the reference stream gives the hit rate at **every** cache size — the result behind part 5.1's claim that the traffic, not the cache, decides |

**Read it last, and that is Principle 4 at the scale of a day.** Section 5 measures a hit rate by
replaying traffic; the paper then explains why the number was never a property of the cache. A reader
who meets the paper first has nothing to hang it on.

**Read the sections in order.** Section 3 is unreadable without section 2's mechanism, and section 6's
alarms are a list of arbitrary thresholds unless sections 4 and 5 have already produced the failures
they detect.

---

## §3 Setup — run this

**No package is added today and no pin moves.** `google-adk` stays at `2.7.1`, `google-genai` at
`2.19.0`. Everything today is the standard library plus ADK objects that are constructed and inspected
rather than called. `git diff pyproject.toml uv.lock` must be empty when you finish.

```bash
# 1 - the day's lab
cd days/day-51-caching-the-quota-lifeline
mkdir -p lab lab/papers/storage-hierarchies

# 2 - the two shared fixtures everything imports
touch lab/_desk.py lab/_log.py

# 3 - sections 2 and 3: the context cache and the floor
touch lab/prefix.py lab/cacheable.py lab/shrink.py lab/fingerprint.py
touch lab/floors.py lab/lifecycle.py

# 4 - section 5: the response cache
touch lab/hitrate.py lab/collide.py lab/ttl.py lab/stale.py

# 5 - section 6: proving the saving
touch lab/savings.py lab/ops.py lab/stampede.py

# 6 - the day's gate
touch lab/gate.py

# 7 - the paper demo
touch lab/papers/storage-hierarchies/trace.py
touch lab/papers/storage-hierarchies/stack.py
cd -

# 8 - the module you write today, and its tests (you type every line)
touch sutra/cache.py tests/test_cache.py

# 9 - confirm the ADK surface this day depends on actually exists
python -c "from google.adk.apps.app import App; print('context_cache_config' in App.model_fields)"
python -c "from google.adk.agents.context_cache_config import ContextCacheConfig as C; print({k: v.default for k, v in C.model_fields.items()})"
```

**Steps 8 and 9 are the ones that matter.** Step 8 creates the two files the build brief fills in; step
9 is Principle 8 as a command — it prints `True` and then the three real defaults, and if either line
raises, the ADK version in this environment is not the one this day was written against and the day
should stop rather than adapt.

`lab/_desk.py` writes out the desk's request in full — the Day 6 instruction, the three tool
declarations from Days 4 and 39, and Day 50's two retrieved rows — rather than importing them, so
every table in this day is reproducible from a fresh checkout with only `google-adk` installed. That
duplication is deliberate and confined to `lab/`.

---

## §4 Build brief

### The project code — `sutra/cache.py`, and you type every line

A new module. Nothing from Days 46–50 is touched.

| Symbol | Shape | What it must do |
| --- | --- | --- |
| `CACHE_TTL_SECONDS` | `int` | the expiry, with a comment naming the sweep it came from (5.5) |
| `CACHE_INTERVALS` | `int` | how many invocations one context cache may serve (4.3) |
| `CACHE_MIN_TOKENS` | `int` | your own floor, set to the provider's, with its source named (3.1) |
| `cache_key` | `(str, str, str) -> str` | readable tenant and class, hashed question (7.1) |
| `ResponseCache` | class | `get`, `put`, `get_with_age`; a miss past the TTL, never a stale serve |
| `context_cache_config` | `() -> ContextCacheConfig` | the three constants, assembled, for the `App` |

- **Every constant carries a comment naming the run it came from**, with the date. `lab/gate.py`
  finding 3 fails the day on a bare number — the same discipline Day 50 applied to `CHUNK_SIZE`.
- **`ResponseCache.get` takes `now` as an argument** rather than calling the clock itself. A cache that
  reads the wall clock internally cannot be tested for expiry without sleeping, and Principle 17's
  cousin applies to tests: nothing in this repo waits for a duration to prove a point.
- **`cache_key` hashes the question and keeps the tenant readable.** Both halves are load-bearing and
  7.1 says why.

**`TODO(me)` markers left for you:**

- **4.3** — choose `CACHE_INTERVALS` and write the `lifecycle.py` run it came from in the comment.
  Then say, in the same comment, **which of the two limits is actually binding at that value** and what
  turn rate would flip it.
- **5.5** — choose `CACHE_TTL_SECONDS` off the sweep, and write **the cost** in the comment: the number
  of wrong answers your choice accepts on this traffic, or the word `zero` if you stopped at 3600.
- **5.2** — decide whether the agent id belongs in `cache_key`. Write the one-sentence promise that
  leaving it out makes, and check it against `_log.py`'s answer key.
- **7.1** — decide the `question_class` values Sutra will actually use. Two or three, not ten, and each
  one has to be a class whose TTL you would set differently.
- **3.2** — write the comment above `CACHE_MIN_TOKENS` that records **the measurement, the date and the
  trigger condition** under which context caching would start working for the desk. `prefix.py` gives
  you the number; 3.3 gives you the trigger.
- **3.3** — write the ADR for the pasted-archive question. Both columns: what it buys (a cacheable
  prefix at 4,700 tokens) and the four things Day 50 says it costs. End with a corpus size that would
  change the answer.
- **6.3** — decide whether the desk needs single-flight yet. It is single-process today. Write down
  what would make it necessary and what the wait deadline would be.
- **7.2** — write the three trigger conditions from 7.2 as three sentences with numbers in them.

### The tests — `tests/test_cache.py`, and you type every line

Six test functions, named as sentences, all offline and all instant:

| Test | What it pins |
| --- | --- |
| `test_cache_key_separates_two_tenants` | `acme` and `borex` never share an entry (5.2, gate finding 4) |
| `test_cache_key_does_not_contain_the_question_text` | the question is hashed, not embedded (7.1) |
| `test_cache_key_ignores_case_and_trailing_punctuation` | the 5 points that `normalised` buys over `exact` |
| `test_get_returns_none_past_the_ttl` | an expired entry is a miss, not a fast answer (5.4) |
| `test_get_with_age_reports_the_age_it_served` | the log can carry `age_s` (6.2, gate finding 7) |
| `test_context_cache_config_min_tokens_clears_the_provider_floor` | `min_tokens >= 4096` (3.1, gate finding 6) |

The second one is the test people leave out, and it is the only thing standing between a support
agent's typing and every log line the system will ever write.

### The lab — sixteen scripts and a two-file paper demo, none of which call a model

| File | What it does | Taught in |
| --- | --- | --- |
| `lab/_desk.py` | the desk's real request: instruction, three tools, two retrieved rows, five turns | all |
| `lab/_log.py` | 60 asks with an answer key, 12 tenant-specific asks, and two trap pairs | 5.x, 6.x |
| `lab/prefix.py` | the prefix against the floor, at k=2, k=20 and whole-archive | 1.1, 3.2, 3.3 |
| `lab/cacheable.py` | four conversation shapes and where ADK puts the boundary | 2.1 |
| `lab/shrink.py` | the request before and after the substitution | 1.1, 2.2 |
| `lab/fingerprint.py` | seven edits, and which move the hash | 1.3, 2.3 |
| `lab/floors.py` | the three refusals, with ADK's own log lines | 3.1, 3.2 |
| `lab/lifecycle.py` | 200 turns, three death causes, the bookkeeping count | 2.4, 4.3 |
| `lab/hitrate.py` | four key recipes over one day of traffic | 5.1, 5.2, 7.2 |
| `lab/collide.py` | two lossy keys and one dropped scope, with a `wrong` column | 5.2, 5.3 |
| `lab/ttl.py` | eight TTLs, hits against stale answers | 5.5 |
| `lab/stale.py` | the actual text served across a policy change | 5.4 |
| `lab/savings.py` | both caches, both units, against the free tier | 1.2, 6.1 |
| `lab/ops.py` | the structured log line and four alarms | 5.3, 6.2 |
| `lab/stampede.py` | eight arrivals on one cold key, two arms | 6.3 |
| `lab/gate.py` | the day's definition of done, as seven findings | §5 |
| `lab/papers/storage-hierarchies/trace.py` | 60 references, in order | paper 01 |
| `lab/papers/storage-hierarchies/stack.py` | one pass against twelve, with the ablation switch | paper 01 |

---

## §5 The eval that must be able to fail

Three checks with exit codes, and every one of them runs on zero model calls.

**The gate** is the day's definition of done, and it is red until `sutra/cache.py` is written:

```bash
uv run python days/day-51-caching-the-quota-lifeline/lab/gate.py; echo "exit: $?"
```

Measured on 2026-09-05, before anything was written: `1-7: sutra.cache is not importable: No module
named 'sutra'`, `findings: 1`, `exit: 1`. When it prints `findings: 0` and `exit: 0`, seven statements
are true: the three constants exist, the two functions exist, every constant carries a comment naming
its measurement, `cache_key` separates two tenants, `ResponseCache` keeps a fresh entry and refuses an
expired one, `min_tokens` clears the provider floor, and `get_with_age` exists so the log can carry
`age_s`. Then break exactly one on purpose — delete the tenant argument from `cache_key` — and watch
finding 4 appear.

**The ablation on the paper demo**, which is an eval in the Principle 11 sense because it can go red:

```bash
cd days/day-51-caching-the-quota-lifeline/lab/papers/storage-hierarchies
diff <(uv run python stack.py | tail -12) <(uv run python stack.py --ablate | tail -12); echo "exit: $?"
cd -
```

Measured on 2026-09-05: no output and `exit: 0`. The paper's one-pass method and twelve separate LRU
simulations produce the same curve, row for row, from 1 pass and 351 stack reads against 12 passes and
3,226. If that `diff` ever prints, the demo is wrong and the paper part is teaching something false.

**The test suite**, offline and green:

```bash
uv run python -m pytest tests/test_cache.py -q -m "not live"
```

Red as shipped, because `tests/test_cache.py` is empty until you write it.

**And every measurement in the day, re-runnable:**

```bash
cd days/day-51-caching-the-quota-lifeline/lab
uv run python prefix.py; uv run python prefix.py --k 20; uv run python prefix.py --archive
uv run python cacheable.py; uv run python cacheable.py --tool
uv run python shrink.py
uv run python fingerprint.py; uv run python fingerprint.py --tools
uv run python floors.py; uv run python floors.py --min 8000
uv run python lifecycle.py; uv run python lifecycle.py --intervals 100
uv run python lifecycle.py --intervals 1; uv run python lifecycle.py --drift 1
uv run python hitrate.py; uv run python hitrate.py --ttl 1800
uv run python collide.py --show
uv run python ttl.py; uv run python ttl.py --revalidate
uv run python stale.py; uv run python stale.py --ttl 1800; uv run python stale.py --revalidate
uv run python savings.py; uv run python savings.py --archive; uv run python savings.py --ttl 21600
uv run python ops.py; uv run python ops.py --break-key
uv run python stampede.py; uv run python stampede.py --fill 20; uv run python stampede.py --agents 12
cd -
```

`floors.py --live` is **not** in that list. It is the only thing in this day that opens a socket, it
is behind a flag for that reason, and its output is left as a `TODO(me)` in part 3.1 rather than
invented.

---

## §6 Request budget

**Free-tier Gemini**, 20 generate requests per day per model (`gemini-3.7-flash`, `docs/PACKAGES.md`
row dated 2026-08-25).

| What | Generations |
| --- | --- |
| every part in every section, and the paper | **0** |
| all sixteen lab scripts, every flag except `--live` | **0** |
| the paper demo, both arms | **0** |
| `sutra/cache.py`, the gate and the six tests | **0** |
| `floors.py --live`, optional, once | **1 cache create, 0 generations** |
| **Total planned** | **0 of 20** |

**Zero, and today the zero is pointed.** A day whose entire subject is the cost of model calls would be
absurd if it spent them, and it does not have to: a cache decision is arithmetic over a request object
and a traffic log, and both of those are on disk. Every table here is reproducible offline, which is
what makes it safe to re-run the whole day after any change to the instruction or the tool schemas —
and after Day 53 starts adding nodes, that will matter.

The one thing worth spending on, once, is `floors.py --live`, which creates a real context cache and
tells you whether ADK's four-characters-a-token estimate agreed with the real tokenizer. It costs one
cache create and **no generations**, and nothing in this day depends on the answer.

**Cost: $0.**

---

## §7 Traps

- **"Caching" is two mechanisms with one name.** One saves tokens inside a request you still send; one
  skips the request. Only the second moves a requests-per-day quota (1.2).
- **A 99% saving in the wrong unit is a green dashboard on a service that still runs out.** Report the
  saving in the unit the limit is written in, or report both in one sentence (6.1).
- **The cacheable prefix stops where the current question starts.** On a cold first turn it is
  `contents[:0]`, so context caching never helps the first question of a session (2.1, 3.1).
- **Anything per-request placed in the system instruction moves the fingerprint every request.** Day
  49 put the retrieved rows there. 200 turns, 200 caches, 399 extra API calls (2.1, 2.3).
- **Reordering the tool list is free; adding a trailing space is not.** ADK canonicalises tools before
  hashing and does not touch the instruction (2.3).
- **After a cache hit, `request.config.tools` is `None`, not `[]`.** Code that iterates it raises
  `TypeError` on the second question and not the first (2.2).
- **Only the tightest of `ttl_seconds` and `cache_intervals` does anything.** The desk's defaults die 18
  times from reuse and 0 times from expiry; the crossover is at 90 (2.4, 4.3).
- **`ContextCacheConfig` goes on the `App`, never on an `LlmAgent`** — 1.x → 2.x **trap #1**, and it
  fails loudly with `Extra inputs are not permitted` (4.1).
- **`cache_metadata` has three states, not two.** `None` means unconfigured; fingerprint-only means
  configured and declined; only `cache_name` being set means a cache is in use. There is no `is_active`
  in the Python API despite the docs page (4.2).
- **Sutra's prefix is 1,521 tokens against a 4,096 floor.** Lowering your own `min_tokens` does not
  touch the provider's, and padding the prompt spends 10,000 characters to save 6,000 (3.2).
- **A cache's hit rate has a ceiling set by the traffic.** 10 distinct questions in 60 asks means 83%,
  and no configuration goes above it (5.1).
- **A hit rate above the ceiling is a defect report, not a triumph.** Above 83% on this traffic means a
  key collision (5.1, 5.3).
- **A worse key produces a higher hit rate.** Dropping digits: 85% and one wrong. First three words:
  87% and three wrong. Dropping the tenant: 92% with 73% of hits wrong (5.3).
- **A scope's cost is paid on every question**, because the key is computed before you know the answer
  and cannot tell which questions are account-sensitive (5.2).
- **A stale hit is faster than the correct behaviour and produces no error.** 17 served, 5 wrong, at a
  TTL of 21600 (5.4).
- **The TTL cannot be tuned from the hit rate**, which is monotonic in it. The free lunch on this
  traffic ends at 3600 seconds (5.5).
- **A TTL shorter than the gap between repeats is an off switch.** At 60 seconds the desk gets zero
  hits; the closest repeat is 240 seconds apart (5.5).
- **`age_s` is the only detector of a stale answer.** Without it a four-second-old hit and a
  six-clock-hour-old hit are the same log line (6.2).
- **The entry is written when the answer returns, not when the question is asked.** Eight agents on one
  cold key with an eight-second fill spend six requests — 30% of the day (6.3).
- **`hash()` is salted per process.** A key built from it never hits across replicas or restarts. Use
  `hashlib` (7.1).
- **The cache key is published** — logs, metric labels, the store — so customer text goes in hashed and
  the tenant stays readable (7.1).
- **A hit is hundreds of times faster than a miss**, which tells the caller whether a question has been
  asked before. The tenant scope closes it (7.1).

---

## §8 Verify before you code

Read or fetched on **2026-09-05**, the day this was written.

- **`adk.dev/context/caching/`** — the ADK-31 page. Fetched today. It gives `ContextCacheConfig`'s four
  fields and their defaults, the `App`-level placement, the two cache states, the note that Gemini
  "applies its own minimum cacheable size, which varies by model", and the behaviour on a create
  timeout ("the request proceeds uncached"). **It does not give the minimum as a number**, and its
  reported-fields list is the Kotlin surface — there is no `isActive` in Python. Part 4.2 tables the
  difference.
- **The installed package, `google-adk==2.7.1`** — every symbol this day uses was introspected rather
  than remembered:

```bash
python -c "from google.adk.apps.app import App; print(sorted(App.model_fields))"
python -c "from google.adk.agents.context_cache_config import ContextCacheConfig as C; print({k: v.default for k, v in C.model_fields.items()})"
python -c "from google.adk.models.cache_metadata import CacheMetadata as M; print(sorted(M.model_fields))"
python -c "from google.adk.models.gemini_context_cache_manager import GeminiContextCacheManager as G; print([n for n in dir(G) if not n.startswith('__')])"
```

  Those four commands produced the field lists, the defaults `cache_intervals=10 / ttl_seconds=1800 /
  min_tokens=0 / create_http_options=None`, the six `CacheMetadata` fields, and the manager's methods.
  The two floors — 2,048 for `gemini-2.5-*` and 4,096 for `gemini-3*` — were read from
  `_minimum_cache_tokens` in that module's source, because they are not published anywhere else.
- **`doi:10.1147/sj.92.0078`, *Evaluation techniques for storage hierarchies*, IBM Systems Journal
  1970, 9(2), 78–117** — the record was opened today via the DOI's CrossRef registration and the title
  copied from it. Row added to `docs/PAPERS.md`. **The identifier this day was first drafted against,
  `doi:10.1147/sj.51.0078`, does not resolve** — it returns HTTP 404 — and was corrected before a word
  was written. That is §17.4.1 rule 5 doing its job: a plausible identifier attached to the right title
  would have sat here for years.
- **The free-tier ceiling of 20 requests per day** for `gemini-3.7-flash` was read off a live 429 on
  Day 2 and recorded in `docs/PACKAGES.md`. It is quoted by `savings.py` and `stampede.py` and is not
  re-checked, because nothing today spends a request.
- **`CHARS_PER_TOKEN = 4.55`** is not re-derived today. It was measured against the provider's own
  tokenizer on Day 24, part
  [1.1](../day-24-token-accounting-and-budgets/parts/01-what-a-request-costs/1.1-a-ticket-id-costs-five-tokens.md),
  and part 3.2 uses it only to show that ADK's four-characters-a-token estimate is the optimistic one.

**What no documentation says**, and what therefore had to be measured: everything in sections 3, 5 and
6. No page will tell you your own prefix size, your own hit-rate ceiling, which of your two cache
limits is binding, or what a TTL costs you in wrong answers. Those are properties of Sutra's request
and Sutra's traffic, and the whole lab exists because they cannot be looked up.

---

## §9 Say it in an interview

*"Day 51 was the day I found out that the caching feature my framework gave me didn't apply to my
agent, and that saying so was the actual deliverable.*

*I started by measuring what a request weighs, which almost nobody does. Six thousand one hundred and
twenty-four characters per request, of which four thousand nine hundred and fifty-two were the JSON
schemas for three tools and six hundred and sixty were the system instruction. The new question was
thirty-nine characters. So ninety-two per cent of every request was a byte-for-byte repeat, charged for
every turn, because a conversation re-sends its whole history.*

*Then the thing that reframed the day: 'caching' is two mechanisms with one name and they save
different currencies. Context caching stores the stable prefix on the provider's side and sends a
handle instead — it cut my request from 6,124 characters to 39, ninety-nine per cent, and it saved
exactly zero requests, because you still make the call. My free tier was metered in requests per day,
twenty of them. So the impressive number was in the wrong unit, and I now refuse to report a caching
saving without naming the unit in the same sentence.*

*Then the uncomfortable finding. Context caching has a provider-side minimum — four thousand and
ninety-six tokens on a gemini-3 model, which isn't in the docs, it's a constant in the framework's
source. My cacheable prefix was one thousand five hundred and twenty-one. Thirty-seven per cent of the
way there. There were three ways to make that go away and all three were worse than the fact: lowering
my own minimum doesn't touch the provider's, padding the prompt spends ten thousand characters to save
six thousand and changes what the model reads, and reporting it as done leaves a lie in the repo for
whoever reads it next. The only honest way over the floor was to stop retrieving and paste my whole
archive into the instruction, which measures at four thousand seven hundred tokens and is cacheable —
but that's a retrieval architecture change, and it costs me citations and the ability to say 'I found
no past case'. So I wrote the number and a re-check trigger into the config comment and moved on.*

*The half that actually saved anything was a response cache, which no framework writes for you because
only you know when two questions are the same question. That's where the real lessons were. First, the
hit rate is a property of the traffic — sixty asks, ten distinct questions, so the ceiling is
eighty-three per cent and I hit it with a five-line normalisation. Second, and this is the one I'd lead
with: a worse cache key produces a higher hit rate. Dropping digits from the question took me to
eighty-five per cent with one wrong answer; keeping the first three words took me to eighty-seven with
three; dropping the customer account took me to ninety-two per cent with seventy-three per cent of hits
serving another company's answer. Every one of those looked like an improvement on the only graph
anybody watches. The defence is arithmetic: anything above the distinct-key ceiling is a collision, not
a win.*

*Third, staleness. With entries that never expired, I served seventeen answers on two topics and five
of them were wrong, because a refund policy changed and the stored answer didn't. No error, no warning,
and faster than being correct. I swept the TTL and found the shape: going from eighteen hundred seconds
to thirty-six hundred saved eleven model calls and cost nothing; going from thirty-six hundred to
twenty-one thousand six hundred saved another twenty-three and cost five wrong answers. So there's a
point where the free lunch ends and after it you're making a trade you have to defend.*

*And the one that only shows up with traffic: the entry is written when the answer comes back, not when
the question is asked. Eight agents asking one new question in nine seconds, with an eight-second model
call, produced six calls for one answer — thirty per cent of my daily quota on one question, all six of
them honest, correctly-logged cache misses that no hit-rate metric would ever flag.*

*The bottom line I'd give a manager: one working day at the desk went from six days of free-tier quota
to three and a third. Caching halved the overrun. It didn't fix it, and I'd rather say that than
present a percentage."*

---

## §10 Done when

See [`CHECKLIST.md`](CHECKLIST.md). Every box is ticked because you ran the thing, not because you read
about it. `./m done 51` refuses to commit until they are.

---

## §11 Ledger & commit

**`docs/PROGRESS.md` — append this row** (fill in the hash after committing):

```markdown
| 51 | 2026-09-05 | ADK-31, OPS-10 | 23 (+1 paper) | <hash> | ⚠️ |
```

**`docs/PACKAGES.md` — no new rows today.** No package is added, no pin moves, and nothing is
installed. `google-adk` stays at `2.7.1` and the `gemini-3.7-flash` row dated 2026-08-25 is quoted,
not re-verified, because nothing today spends a generation.

**`docs/PAPERS.md` — one new row, added today:**

```markdown
| Evaluation techniques for storage hierarchies | doi:10.1147/sj.92.0078 | 1970 | 2026-09-05 | 51 | `days/day-51-caching-the-quota-lifeline/papers/01-storage-hierarchies.md` |
```

> **Correction worth recording.** This day was drafted against `doi:10.1147/sj.51.0078`, which does
> not resolve — `https://doi.org/10.1147/sj.51.0078` returns HTTP 404. The correct identifier is
> `doi:10.1147/sj.92.0078` (volume 9, issue 2, page 78), confirmed against the DOI's CrossRef
> registration on 2026-09-05, which also supplied the title, the year and the page range copied above.
> §17.4.1 rule 5 exists for exactly this: the wrong identifier was plausible, attached to the right
> title, and would have been believed.

**`docs/SKILL_PROVENANCE.md` — no new rows today.**

**Git commit message:**

```
day 51: caching — context and response caching as the quota lifeline — closes ADK-31, OPS-10
```
