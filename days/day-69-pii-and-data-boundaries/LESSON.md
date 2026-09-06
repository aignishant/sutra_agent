---
day: 69
phase: 10
phase_name: "Safety and security"
title: "PII & data boundaries — synthetic data only, free-tier training caveat"
ids: ["SEC-12", "SEC-13"]
principles: [1, 2, 7, 9, 10, 11, 13, 15, 16, 17, 18]
kind: build
plan_version: "v2.2.1"
parts: 22
generated: "2026-09-06"
status: written
lab_scaffolded: true
commit: ""
---

# Day 69 — PII and data boundaries

> **Yesterday (Day 68):** least privilege for tools. A permission table as data, a fence outside every
> tool, and a failure lab that broke three permission systems by running them — including a helper
> agent whose narrow toolset achieved nothing because control came back to the desk.
> **Today:** the other structural control Day 67 pointed at — not a capability the agent does not
> hold, but a **value that never entered the context**. What counts as personal data here, where the
> copies actually are, what the provider does with what you send it, and why every fixture in this
> repository is invented on purpose.
> **Tomorrow (Day 70):** the quota router, which closes Phase 10's gate — injection attempts contained,
> quota router live.

---

## §1 Where we are

Every day from 46 to 61 added a place where text is kept, and every one of them was a good idea. Day
47 made sessions survive a restart. Day 48 gave the desk a memory. Days 49 and 50 built the archive and
its index. Day 51 added a response cache because quota is the currency. Days 60 and 61 added an event
log and checkpoints so a run survives being killed.

Nobody in those days wrote a line whose purpose was to copy customer text. The count today is
**thirteen copies in seven stores, after one ordinary ticket**.

That is the shape of this day. Not a failure to be fixed, but an accumulation nobody decided on,
discovered by counting rather than by remembering — and then four questions asked of it in order. What
in that text actually names a person? Where are the copies? What does the provider do with the part
that leaves? And when somebody asks for it to be gone, what can honestly be said?

Two answers are uncomfortable and both are measured rather than asserted. The redactor this day builds
catches **100% of the structured fields and 23% of the free text**, which is a way of saying it works
perfectly on the half that was never the problem. And the delete everybody writes first succeeds,
raises nothing, and leaves the customer's address in **six of seven stores** — where the search index
will hand the whole message back, signature and all, to the next question that matches it.

The day's decision follows from a page rather than from a principle. Asked whether they may train on
what a free tier sends them, Sutra's three providers give three different answers, and **the one that
says yes is the primary**. So the rule this repository has been quietly depending on since Day 1 gets
written down: real personal data never enters it, and every fixture is invented on purpose.

---

## §2 The map

Seven sections. Section 1 asks what actually names a person, and finds the answer is not a list of
fields. Section 2 counts the copies and draws the boundary. Section 3 reads the providers' terms and
turns them into a decision. Section 4 is synthetic data as an engineering practice, and the honest
measurement of what it costs. Section 5 measures the redactor in the only way that means anything.
Section 6 is the delete that did not. Section 7 is what has to be written down, and the checks that
make it a boundary rather than a policy.

### 1 — Who a record names

*What counts as personal data here, and why a list of field names is not the answer.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [The list of fields is not the answer](parts/01-who-a-record-names/1.1-the-list-of-fields-is-not-the-answer.md) | Why "remove the personal data" is not executable until somebody says what it covers | `foundation` |
| 1.2 | [Three columns that name one person](parts/01-who-a-record-names/1.2-three-columns-that-name-one-person.md) | Quasi-identifiers: values that name nobody alone and one person together | `working` |
| 1.3 | [The box marked "anything else"](parts/01-who-a-record-names/1.3-the-box-marked-anything-else.md) | 💥 A desk keeps what matters in free text, and a redactor tested on fields is tested on the wrong half | `working` |
| 1.4 | [The number that only means something here](parts/01-who-a-record-names/1.4-the-number-that-only-means-something-here.md) | Internal keys as identifiers, and why that is what makes erasure possible at all | `working` |

### 2 — Where the copies are

*Thirteen copies in seven stores, after one ticket nobody handled carelessly.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [One sentence, seven places](parts/02-where-the-copies-are/2.1-one-sentence-seven-places.md) | The count, and why the map has to be runnable rather than remembered | `working` |
| 2.2 | [A boundary is a line you can name](parts/02-where-the-copies-are/2.2-a-boundary-is-a-line-you-can-name.md) | What makes a boundary a boundary rather than a diagram | `working` |
| 2.3 | [The copy nobody calls a copy](parts/02-where-the-copies-are/2.3-the-copy-nobody-calls-a-copy.md) | 💥 Derived data: six stores built for reasons unrelated to holding customer text | `working` |
| 2.4 | [The reply is personal data too](parts/02-where-the-copies-are/2.4-the-reply-is-personal-data-too.md) | The output is generated after the input filter ran, and stored by three things that do not filter | `working` |

### 3 — The line at the provider

*Three providers, three answers, and the one that says yes is the primary.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [Three providers, three answers](parts/03-the-line-at-the-provider/3.1-three-providers-three-answers.md) | Yes, no, and it-depends-on-a-setting — read from the pages, with dates | `production` |
| 3.2 | [The page that does not answer](parts/03-the-line-at-the-provider/3.2-the-page-that-does-not-answer.md) | Recording *unknown* as unknown, and why a record beats a live fetch | `working` |
| 3.3 | [What follows for Sutra](parts/03-the-line-at-the-provider/3.3-what-follows-for-sutra.md) | The decision this repository has been depending on, written down as a `refuse` | `production` |

### 4 — Invented on purpose

*Synthetic data as an engineering practice, and the measurement that keeps it honest.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [Why invent the customers](parts/04-invented-on-purpose/4.1-why-invent-the-customers.md) | Four reasons, and privacy is the least interesting of them | `foundation` |
| 4.2 | [A generator is a specification](parts/04-invented-on-purpose/4.2-a-generator-is-a-specification.md) | Writing the generator forces the belief into code where it can be diffed | `working` |
| 4.3 | [The corpus that flatters your detector](parts/04-invented-on-purpose/4.3-the-corpus-that-flatters-your-detector.md) | 💥 100% on generated data, 80% on hand-written, and no better redactor | `production` |

### 5 — Measuring the redactor

*The answer key, both columns of the score, and the class of value nothing catches.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [The answer key comes first](parts/05-measuring-the-redactor/5.1-the-answer-key-comes-first.md) | A redactor with no measured recall is a redactor nobody can tune | `working` |
| 5.2 | [Fifty per cent, and it looked fine](parts/05-measuring-the-redactor/5.2-fifty-per-cent-and-it-looked-fine.md) | 💥 50% overall is 100% on fields and 23% on free text | `production` |
| 5.3 | [The wall called a name](parts/05-measuring-the-redactor/5.3-the-wall-called-a-name.md) | 💥 A name is not a pattern, and a hash of a name is still a name — 6 of 8 recovered | `production` |

### 6 — The delete that did not

*Erasure, measured from outside the routine that claims to have done it.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 6.1 | [Deleted, and still retrievable](parts/06-the-delete-that-did-not/6.1-deleted-and-still-retrievable.md) | 💥 Six of seven stores untouched, and the index hands the message back | `production` |
| 6.2 | [The store you cannot address](parts/06-the-delete-that-did-not/6.2-the-store-you-cannot-address.md) | Three ways a store can be reached, and the two that are not deletion | `production` |
| 6.3 | [The loop over a list somebody kept](parts/06-the-delete-that-did-not/6.3-the-loop-over-a-list-somebody-kept.md) | The delete that reaches everywhere is a registry, not a cleverer delete | `production` |

### 7 — In production

*What has to be written down, and the checks that make it fail.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 7.1 | [Answering "what do you hold?"](parts/07-in-production/7.1-answering-what-do-you-hold.md) | Disclosure and erasure must read the same registry, or they will disagree | `production` |
| 7.2 | [The boundary written down](parts/07-in-production/7.2-the-boundary-written-down.md) | A policy is what you intend; a boundary is what fails | `production` |

### The paper — read it last

*Principle 4 at the scale of a day: count your own stores first, then read about the one you do not
control.*

| # | Paper | What it answers |
| --- | --- | --- |
| 01 | [Extracting Training Data from Large Language Models](papers/01-extracting-training-data.md) | `arXiv:2012.07805` — the eighth store: a model can return training examples verbatim, and there is no key to address and no delete to perform |

---

## §3 Setup — run this

```bash
mkdir -p days/day-69-pii-and-data-boundaries/lab/papers/extracting-training-data
cd days/day-69-pii-and-data-boundaries/lab
```

Fourteen files in the lab, plus two in the paper's demo directory. No package is added today:

```bash
touch _archive.py _desk.py _redact.py _stores.py
touch freetext.py quasi.py copies.py terms.py
touch synth.py recall.py hashcheck.py deleted.py derived.py gate.py
touch papers/extracting-training-data/tinylm.py papers/extracting-training-data/demo.py
```

**What each file is for:**

- The four underscore-prefixed modules are imported, never run. `_archive.py` holds the hand-written
  ticket fixtures **and** `TRUTH`, the answer key section 5 scores against. `_stores.py` is the store
  registry — seven names, seven files — that section 6's purge and section 7's disclosure both loop
  over. `_desk.py` runs one ordinary ticket through all seven stores. `_redact.py` holds the two
  redactors, V1 and V2.
- `freetext.py` and `quasi.py` are section 1: what survives perfect field redaction, and values that
  name one person only in combination.
- `copies.py` is section 2's count and section 7's disclosure instrument.
- `terms.py` is section 3 — a **record** of a reading of three providers' pages, with dates, not a live
  fetch.
- `synth.py`, `recall.py` and `hashcheck.py` are sections 4 and 5.
- `deleted.py` and `derived.py` are section 6: the delete everybody writes first, and the one that
  loops over the registry.
- `gate.py` is today's eval.

Verify the state directory is gitignored before anything writes a file full of customer-shaped text:

```bash
git check-ignore -v days/day-69-pii-and-data-boundaries/lab/state/archive.json
```

**Why:**

- `days/*/lab/` is ignored repo-wide. Everything under `state/` is synthetic, and it is still exactly
  the shape of the thing that must never be committed — Principle 9, and the subject of this whole day.
  If this prints nothing, fix `.gitignore` before running anything.

**No package is added today.** `git diff pyproject.toml uv.lock` must be empty and stay empty.

---

## §4 Build brief

The teaching is in `parts/` and the measurements are in `lab/`. What is left is the piece that belongs
in the product, and today it is a module **and a document**.

**`sutra/data_boundary.py`** — the redactor, the store registry and the purge, promoted out of the lab.

- `TODO(me)`: `redact(text)`, built from V2 and then improved. The gate holds a **90% free-text recall
  floor** and V2 measures 69%, so this one is not a copy-and-paste — the number is the exercise.
- `TODO(me)`: `STORES` as a registry, and `purge(ref)` looping over it with a declared reach per store.
  Section 6.2's three reach kinds are the vocabulary; a store with no declared reach must stop the
  purge rather than be skipped.
- `TODO(me)`: make `purge` return a **per-store report**, because an erasure that returns `None` cannot
  be quoted as evidence — part 7.1.

**`docs/DATA_BOUNDARY.md`** — the document part 7.1 answers an access request from.

- `TODO(me)`: one row per store: what it holds, why, how long it is kept, how it is reached for
  erasure. Two of those four are not currently anywhere in this repository; part 7.2's *Check yourself*
  asks you to find out which.
- `TODO(me)`: decide whether the store table is generated from the registry or hand-written, and say
  why in the document. Day 66 part 7.2 made this argument for a threat model; the same trade applies.

**`tests/test_data_boundary.py`**

- `TODO(me)`: a test that walks `lab/state/` and fails if a file present has no row in `STORES`. That
  is the drift check, and it is the one thing that keeps the registry honest.
- `TODO(me)`: a test that asserts free-text recall against a **held-out** fixture set the redactor's
  author does not edit — part 4.3 is why the same corpus will not do.

Do not copy the lab scripts into `sutra/`. `_desk.py` and `terms.py` are instruments for this day.

---

## §5 The eval that must be able to fail

```bash
cd days/day-69-pii-and-data-boundaries/lab
uv run python gate.py; echo "exit: $?"
```

Six findings, four of them **red** today. Three are the build brief — the module, the document and the
test. The fourth is a measurement, and it is the interesting one: the redactor's free-text recall is
**69% (9/13) against a 90% floor**, which is a target with a name against it rather than a description
of what the code already does.

The gate's own docstring carries the design choice worth copying: a check that **cannot run** reports
as a **failure** rather than as skipped, because a skipping check goes green on a repository where
somebody deleted the module.

Two checks pass silently and they are the day's actual achievements — a purge really does empty every
registered store, and every fixture value comes from a range reserved for fiction (RFC 2606 domains,
Ofcom drama numbers). Part 7.2's *Check yourself* has you break the second one on purpose.

---

## §6 Request budget

**Zero provider requests, to every provider.**

| Provider | Requests today | Against |
| --- | --- | --- |
| Google AI Studio (Gemini) | 0 | free tier |
| Groq | 0 | 30 RPM / 250 RPD, observed 2026-09-05 |
| OpenRouter `:free` | 0 | free tier |
| Ollama (local) | 0 | n/a |

Nothing in this lab imports `google.adk`, calls a model or opens a socket. `terms.py` is a record of a
reading rather than a fetch, for the reason part 3.2 argues, and its `--recheck` flag prints the
commands for you to run rather than running them.

The paper's demo trains a small local model on a synthetic corpus and queries it thousands of times,
which is exactly the sort of thing that would be unaffordable against a provider and costs nothing on
your own machine — Principle 15 doing real work rather than being a constraint.

---

## §7 Traps

1. **Answering "what is personal data?" from a list of field names.** The desk keeps what matters in
   the box a human typed into, and a redactor tested on the fields is tested on the wrong half —
   parts 1.1 and 1.3.
2. **Treating a value that names nobody as safe.** Three columns that each name nobody can name one
   person together — part 1.2.
3. **Assuming the stores are the ones with "store" in the name.** Six of the seven were built for
   reasons unrelated to holding customer text — part 2.3.
4. **Forgetting the reply.** It is generated *after* the input filter has run and stored by three
   things that apply no filter at all — part 2.4.
5. **Guessing a provider's terms.** The answer is a page and a date, and where the page does not
   answer, the honest record says so — parts 3.1 and 3.2.
6. **Scoring a detector on data you generated from the same beliefs.** 100% generated against 80%
   hand-written, and not a better redactor — part 4.3.
7. **Reporting an aggregate recall.** 50% overall is 100% on fields and 23% on free text, and only one
   of those three numbers is a finding — part 5.2.
8. **Calling a hash anonymous.** 6 of 8 addresses recovered from their hashes, and salting changed
   nothing against a guessable candidate set — part 5.3.
9. **Deleting from the archive and reporting success.** Six of seven stores untouched, eleven copies
   remaining, and the index still returns the whole message — part 6.1.
10. **Treating every store the same way.** One has to be scanned because it is not addressable, and one
    must survive because it is the record that the event happened — part 6.2.
11. **Letting disclosure and erasure read different lists.** That is how a system tells somebody it
    holds nothing and then fails to delete it — part 7.1.

---

## §8 Verify before you code

Fetched on 2026-09-06:

| What | Where | What it said |
| --- | --- | --- |
| Gemini free-tier terms | <https://ai.google.dev/gemini-api/terms> and <https://ai.google.dev/gemini-api/docs/pricing> | unpaid usage **may be used to improve the products** — the row that makes SEC-13 a decision rather than a caveat |
| Groq terms | <https://console.groq.com/docs/legal/services-agreement> and <https://groq.com/privacy-policy/> | **no** training on customer content in the services agreement; the privacy policy does not address it, recorded as `n/a` rather than inferred |
| OpenRouter privacy and logging | <https://openrouter.ai/docs/features/privacy-and-logging> | **depends on a setting**, so the row is about your account rather than about the provider |
| `arXiv:2012.07805` record | <https://arxiv.org/abs/2012.07805> | title *Extracting Training Data from Large Language Models*, v1 14 December 2020 — copied into `docs/PAPERS.md` and the paper document, never from memory (§17.4.1 rule 5) |

**No ADK symbol is used today.** Nothing in `lab/` imports `google.adk`: the whole day is file counting,
string matching and arithmetic, so every measurement can be re-derived by anyone who checks out the
repo without a provider account.

Re-verify the provider rows on the day you use them — `uv run python terms.py --recheck` prints the
commands. A row about a legal document is attributable to a document **and a date**, and this day's
date is not yours.

---

## §9 Say it in an interview

*"We treated privacy as a counting problem before treating it as a policy problem. One ordinary
support ticket put the customer's email address in seven stores and thirteen copies — the archive, a
session, a memory store, a search index, a response cache, an event log and a checkpoint — and six of
those were built for reasons that had nothing to do with holding customer data. Then we measured the
redactor properly: fifty per cent overall, which sounds like half done, and split by where the value
was sitting it was a hundred per cent on structured fields and twenty-three on free text, so it worked
perfectly on the half that was never the problem. Names are the wall — a name has no pattern to match,
and hashing one doesn't help, we recovered six of eight addresses from their hashes and salting changed
nothing. The delete was the sharpest finding: deleting the ticket from the archive succeeded, raised
nothing, and left the data in six of seven stores, with the index still returning the whole message
including the signature to an unrelated later query. The fix wasn't a cleverer delete, it was a
registry of stores that code loops over, with a declared way of reaching each — including a cache that
isn't addressable by customer at all and a log that has to survive, where the operation is redacting
the excerpt rather than deleting the line. And the reason all our fixtures are synthetic is a page
rather than a principle: our primary provider's free tier says it may train on what we send it."*

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked, and you have run the commands rather than read
them. `./m done 69` refuses to commit until they are.

The day is finished when you can name all seven stores and say, for each, how you would reach a
customer's rows in it — and when you can state the redactor's recall in the only form that means
anything, which is two numbers rather than one.

---

## §11 Ledger & commit

**`docs/PROGRESS.md`** — append this row:

```text
| 69 | 2026-09-06 | SEC-12, SEC-13 | 22 | <hash> | ⚠️ |
```

The gate column is `⚠️` and means it. `./m depth 69` is green over the twenty-two parts and the paper.
`lab/gate.py` is **red** on four of its six findings: three are the build brief, and the fourth is the
redactor at 69% free-text recall against the 90% floor this day set. That fourth one is left red
deliberately — part 7.2 argues why lowering the floor to what the code does would measure nothing. The
repository-wide `⚠️` carried since Day 15 is unchanged: `tests/test_persona.py` still fails ruff
`I001`, and it is the learner's own file, which no generated day may edit.

**`docs/PACKAGES.md`** — no new rows. No package is added today.

**`docs/PAPERS.md`** — one row, checked live today:

```text
| Extracting Training Data from Large Language Models | arXiv:2012.07805 | 2020 | 2026-09-06 | 69 | `days/day-69-pii-and-data-boundaries/papers/01-extracting-training-data.md` |
```

**`docs/SKILL_PROVENANCE.md`** — no new rows. No third-party skill is used today.

**Commit:**

```text
day 69: PII and data boundaries - synthetic data only, free-tier training caveat - closes SEC-12, SEC-13
```
