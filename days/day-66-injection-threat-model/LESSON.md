---
day: 66
phase: 10
phase_name: "Safety and security"
title: "Threat model — prompt injection & the lethal trifecta"
ids: ["SEC-06", "SEC-07"]
principles: [1, 2, 7, 9, 10, 11, 13, 15, 16, 17, 18]
kind: build
plan_version: "v2.2.1"
parts: 22
generated: "2026-09-06"
status: written
lab_scaffolded: true
commit: ""
---

# Day 66 — Threat model: prompt injection and the lethal trifecta

> **Yesterday (Day 65):** Phase 9 closed with a drill rather than a review — four kills at four
> moments, a cold-eyes audit of the wreckage, and seven criteria that each ended in an exit code.
> **Today:** Phase 10 opens by turning the archive Days 49 and 50 built into what it actually is —
> an attack surface. Six doors into the desk's context, five ways out, the trifecta traced along the
> path instead of per stage, and a threat model written down as a file the next four days implement
> against.
> **Tomorrow (Day 67):** defense in depth — input and output guardrail callbacks, a ladder of checks
> with honest numbers in both columns, and the day's closing argument that a check which works by
> reading text can always be argued with.

---

## §1 Where we are

Phase 7 gave the desk a memory and an archive. Phase 8 gave it a graph that plans, delegates and
criticises. Phase 9 made it survive being killed. Every one of those was a capability, and every one
of them widened the same thing without ever saying so out loud: **the amount of text written by
strangers that ends up in the model's context.**

Measured on the desk's own prompt today, 73.4% of the characters going to the model were written by
somebody outside the system. That is not a bug in the design. It is the design working: a support
desk that will not read what customers write is not a support desk, and a retrieval index that finds
relevant documents will find relevant hostile documents by exactly the same mechanism.

Think about a parcel arriving at a building where the guard has standing orders. The orders are on a
card he was given on his first day. The parcel has a note taped to it. Both are writing, both are in
front of him, and the only thing that distinguishes them is a habit about which one to believe —
because nothing in the paper itself says which is which. Section 1 is about why that habit is all a
language model has, and why the fix that solved SQL injection cannot be copied across.

Today produces a document. Not a feeling that the system is risky, and not a list of things somebody
ought to look at: a generated file, `lab/threat-model.md`, with an asset list, an entry-point list, a
trifecta table, a channel list and eight decisions, each carrying one of three verdicts. Days 67 to
70 are implementations of four of those rows.

The day's most interesting measurement is in section 4, and it comes out **twice, differently**.
Asked stage by stage, the triage graph from Day 58 looks clean — zero of five stages hold all three
legs of the lethal trifecta. Asked along the path, the trifecta is complete at `review`. The
difference is not a subtlety; it is the whole finding, and the reassuring first answer is the one a
normal design review produces.

---

## §2 The map

Seven sections. Section 1 is why the problem exists at all and why the database's fix does not
transfer. Section 2 is the taxonomy of arrival — where a stranger's words get in, counted on this
desk. Section 3 is the delay: injections that are written now and act later, and payloads split
across two documents. Section 4 is the lethal trifecta and the measurement that inverts when you ask
it correctly. Section 5 is what an injection actually asks for, in five kinds. Section 6 counts every
way a byte can leave. Section 7 turns all of it into the artefact and its verdicts.

### 1 — One stream

*Why a model cannot tell your instructions from a stranger's, and why the database's fix does not
transfer.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [The note taped to the parcel](parts/01-one-stream/1.1-the-note-taped-to-the-parcel.md) | Instructions and data arrive as one flat stream, measured at 73.4% stranger-written | `foundation` |
| 1.2 | [The fix the database got](parts/01-one-stream/1.2-the-fix-the-database-got.md) | Why parameterised queries solved SQL injection and cannot be copied across | `foundation` |
| 1.3 | [The sentence you did not write](parts/01-one-stream/1.3-the-sentence-you-did-not-write.md) | A definition that says nothing about how the sentence is phrased | `foundation` |

### 2 — How it arrives

*Every door into the desk's context, and who can write through each one.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [Typed at the counter](parts/02-how-it-arrives/2.1-typed-at-the-counter.md) | Direct injection, and why it is the least dangerous kind | `foundation` |
| 2.2 | [Arriving in somebody else's post](parts/02-how-it-arrives/2.2-arriving-in-somebody-elses-post.md) | Indirect injection: the attacker never speaks to your system | `working` |
| 2.3 | [The recipe folder in the staff kitchen](parts/02-how-it-arrives/2.3-the-recipe-folder-in-the-staff-kitchen.md) | Six doors, four feeding the index, and the insider one that works best | `working` |
| 2.4 | [The camera that recorded everything](parts/02-how-it-arrives/2.4-the-camera-that-recorded-everything.md) | 💥 The honest experiment: not *would it obey*, but *would anything stop it* | `working` |

### 3 — The slow fuse

*Injections that are written now and act later, and payloads that are harmless one row at a time.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [Written Monday, read Thursday](parts/03-the-slow-fuse/3.1-written-monday-read-thursday.md) | An injection that survives into memory stops being an event and becomes a rule | `production` |
| 3.2 | [The half that is harmless alone](parts/03-the-slow-fuse/3.2-the-half-that-is-harmless-alone.md) | 💥 A payload split across two documents that a per-document check cannot see | `production` |

### 4 — Three legs

*The lethal trifecta, and the measurement that inverts depending on the unit you ask in.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [The three things that must not meet](parts/04-three-legs/4.1-the-three-things-that-must-not-meet.md) | Private data, untrusted content, a way out — and why any two is survivable | `foundation` |
| 4.2 | [Nobody here holds all three](parts/04-three-legs/4.2-nobody-here-holds-all-three.md) | 💥 A clean result — zero of five stages — produced by asking in the wrong unit | `working` |
| 4.3 | [The line that passes it along](parts/04-three-legs/4.3-the-line-that-passes-it-along.md) | The same question asked along the path: the trifecta closes at `review` | `production` |
| 4.4 | [Closing the tap nearest the outlet](parts/04-three-legs/4.4-closing-the-tap-nearest-the-outlet.md) | Two sensible interventions, one of which changes nothing | `production` |

### 5 — What it asks for

*Five harms, each needing a different leg and noticed by a different person.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [The stocktake](parts/05-what-it-asks-for/5.1-the-stocktake.md) | Exfiltrate, escalate, mislead, destroy, spend — and who notices each | `foundation` |
| 5.2 | [The meter somebody else is feeding](parts/05-what-it-asks-for/5.2-the-meter-somebody-else-is-feeding.md) | One sentence buys twenty requests against a twenty-request day | `production` |

### 6 — The way out

*Five channels, four of which do not look like network calls.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 6.1 | [The address inside the picture](parts/06-the-way-out/6.1-the-address-inside-the-picture.md) | 💥 The channel that needs no tool, and the blocklist measured failing both ways | `working` |
| 6.2 | [Read back for confirmation](parts/06-the-way-out/6.2-read-back-for-confirmation.md) | The reply itself is a channel, and it is the one nobody counts | `working` |
| 6.3 | [The note inside the back cover](parts/06-the-way-out/6.3-the-note-inside-the-back-cover.md) | Writing to memory is outward: the planted row comes back at 0.491 | `production` |
| 6.4 | [The receipt that printed too much](parts/06-the-way-out/6.4-the-receipt-that-printed-too-much.md) | The error message, and why no tool allowlist touches it | `production` |

### 7 — Writing it down

*The artefact, how it stays true, and the three verdicts that make it a decision.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 7.1 | [What is worth taking](parts/07-writing-it-down/7.1-what-is-worth-taking.md) | Assets and entry points in plain words, and why aggregation is its own asset | `foundation` |
| 7.2 | [The document that writes itself](parts/07-writing-it-down/7.2-the-document-that-writes-itself.md) | 💥 Generated from the declarations, and the gate that catches drift | `working` |
| 7.3 | [Accept, mitigate, refuse](parts/07-writing-it-down/7.3-accept-mitigate-refuse.md) | What each verdict obliges you to write down | `production` |

### The paper — read it last

*Principle 4 at the scale of a day: build the mechanism by hand, then read the proposal.*

| # | Paper | What it answers |
| --- | --- | --- |
| 01 | [Not what you've signed up for: … Indirect Prompt Injection](papers/01-indirect-prompt-injection.md) | `arXiv:2302.12173` — the document that moved the field from *what a user types* to *what the application fetches* |

Two further papers are cited by parts today and were taught on earlier days: *Reflections on trusting
trust* (`doi:10.1145/358198.358210`) in 1.3, and *The protection of information in computer systems*
(`doi:10.1109/PROC.1975.9939`) in 4.4.

---

## §3 Setup — run this

```bash
mkdir -p days/day-66-injection-threat-model/lab/papers/indirect-prompt-injection
cd days/day-66-injection-threat-model/lab
```

Sixteen files in the lab, plus two in the paper's demo directory. None of them is a package install:

```bash
touch _archive.py _desk.py _index.py _poison.py
touch prompt.py obey.py doors.py reaches.py delayed.py split.py blocklist.py
touch legs.py gate.py channels.py spend.py model.py
touch papers/indirect-prompt-injection/corpus.py papers/indirect-prompt-injection/demo.py
```

**What each file is for:**

- The four underscore-prefixed modules are imported, never run: `_archive.py` is the fifty-eight
  documents Days 49 and 50 indexed, `_desk.py` is the desk's prompt assembly, `_index.py` is Day 49's
  tf-idf arithmetic restated so today's numbers reproduce without a network call, and `_poison.py` is
  the corpus — twelve hostile variants of one instruction and five ordinary tickets.
- `prompt.py`, `obey.py`, `doors.py` and `reaches.py` are section 1 and 2's measurements: what the
  prompt is made of, what the desk would do about it, where the doors are, and which one reaches.
- `delayed.py` and `split.py` are section 3 — the fuse and the two halves.
- `legs.py` is section 4 and is the file the whole day turns on: it declares the graph's wiring and
  answers the trifecta question in both units.
- `blocklist.py`, `channels.py` and `spend.py` are sections 5 and 6.
- `model.py` generates `threat-model.md` and `gate.py` checks it. Those two are the deliverable.

Verify the lab is gitignored before anything writes customer-shaped text into it:

```bash
git check-ignore -v days/day-66-injection-threat-model/lab/threat-model.md
```

**Why:**

- Everything in `lab/` is scratch, and today's scratch contains synthetic values shaped like account
  records. If this prints nothing, stop and fix `.gitignore` before running anything — Principle 9.
  The generated artefact is meant to be read locally; the version that goes in the repo is the one
  the build brief asks you to write under `sutra/`.

**No package is added today.** `git diff pyproject.toml uv.lock` must be empty and stay empty.

---

## §4 Build brief

The teaching is in `parts/` and the measurements are in `lab/`. What is left for you is the piece
that belongs in the product rather than in the lab.

**`sutra/threat_model.py`** — the threat model as data the rest of the codebase can assert against.

- `TODO(me)`: a `Channel` dataclass and a `CHANNELS` tuple naming every way out, including the four
  that are not network calls. `gate.py`'s `check_project_module()` fails until every channel name in
  `lab/channels.py` appears in this module, which is the crudest possible version of "the code knows
  what the document says".
- `TODO(me)`: a `Decision` dataclass carrying `verdict`, `about` and `because`, with `verdict`
  constrained to the three words. A fourth verdict is how a threat model stops being a decision.
- `TODO(me)`: `accepted_under(decision) -> str` — the condition an `accept` row is valid under, which
  part 7.3 argues is the field everybody omits. Decide whether an `accept` row with an empty
  condition should be a type error or a test failure, and say why in the docstring.

**`tests/test_threat_model.py`**

- `TODO(me)`: a test that every `mitigate` decision names an owner, mirroring `gate.py`'s check but
  against the product module.
- `TODO(me)`: a test that the channel list in `sutra/threat_model.py` and the one in the generated
  artefact do not disagree. Decide which of the two is the source of truth before you write it — that
  decision is the actual exercise.

Do not copy the lab scripts into `sutra/`. They are this day's instrument; the product piece is the
declaration that Days 67 to 70 import.

---

## §5 The eval that must be able to fail

```bash
cd days/day-66-injection-threat-model/lab
uv run python model.py --write
uv run python gate.py; echo "exit: $?"
```

Five checks, and it is **red** today for two reasons the day names rather than hides: the trifecta
closes at `review` (section 4's finding, which is a finding and not a bug in the gate), and
`sutra/threat_model.py` is the build brief you have not written yet.

The check that can be made to go red **on demand** — the point of Principle 11 — is the mitigation
ownership check, and section 7.3 runs the ablation: rewrite every `mitigate` row's reason so it names
no day, and watch four mitigations be reported by name. Two more ablations exist and are exercised in
their parts: `legs.py --isolate` and `legs.py --cut outward` in section 4, and the second corpus in
`blocklist.py --benign --wider` in section 6.

---

## §6 Request budget

**Zero provider requests, to every provider.**

| Provider | Requests today | Against |
| --- | --- | --- |
| Google AI Studio (Gemini) | 0 | free tier |
| Groq | 0 | 30 RPM / 250 RPD, observed 2026-09-05 |
| OpenRouter `:free` | 0 | free tier |
| Ollama (local) | 0 | n/a |

Every measurement today is arithmetic over declared wiring, string matching over a fixed corpus, or
Day 49's tf-idf restated locally. Nothing calls a model and nothing opens a socket, which is why the
whole day can be re-run as often as you like.

The numbers the day **reports** are still real costs — part 5.2's twenty extra requests are requests
the desk would spend against a provider — because a threat model priced in imaginary units is not a
threat model. Nothing today spends them.

---

## §7 Traps

1. **Asking the trifecta question per component.** Five stages, none holding all three legs, and a
   pipeline that holds it anyway. The legs travel with the text, not with the box — section 4.2 gets
   the reassuring answer and 4.3 gets the true one.
2. **Reading "outward" as "to the internet".** Four of the five channels are not network calls, and
   the one everybody removes is the only one a tool registry knows about — section 6.
3. **Reporting a filter with one column.** The wider blocklist catches 10 of 12 hostile variants and
   refuses 4 of 5 honest customers, including a customer reporting a phishing mail, blocked for
   quoting it — section 6.1.
4. **Treating an injection as a phrasing.** The corpus is twelve spellings of one instruction; the
   instruction never changes. A defence built on vocabulary is a guess about surface form — sections
   1.3 and 6.1.
5. **Forgetting that the desk writes into its own context.** `save_memory` is an entry point and an
   exit, and the two are different rows in the threat model — sections 3.1 and 6.3.
6. **Hand-editing the generated artefact.** It says not to on line three. The next regeneration
   deletes the edit and nobody finds out which parts were somebody's — section 7.2.
7. **A `mitigate` row that names nobody.** This is how a threat model rots under deadline pressure,
   and it is the one check here that can be driven red in one command — section 7.3.
8. **Writing the threat model against a nation-state.** A plan nobody can afford is a plan nobody
   executes. The attacker in the artefact has a free account, one article and a week, and every
   measurement in this day was produced by that attacker.

---

## §8 Verify before you code

Fetched on 2026-09-06:

| What | Where | What it said |
| --- | --- | --- |
| `arXiv:2302.12173` record | <https://arxiv.org/abs/2302.12173> | title and identifier confirmed; v1 23 Feb 2023, v2 5 May 2023 — copied into `docs/PAPERS.md` and the paper document, never from memory (§17.4.1 rule 5) |
| `google-adk` latest | <https://pypi.org/pypi/google-adk/json> | `2.8.0`; this repo pins `2.7.1`, carried forward as the Day 65 freshness finding rather than upgraded mid-phase (Principle 14) |

**No ADK symbol is used today, and that is deliberate.** Nothing in `lab/` imports `google.adk`: the
whole day is arithmetic over declared wiring plus string matching, so the analysis does not depend on
a framework version and can be re-derived by anyone who checks out the repo. Day 67 is where the
callback surface is verified against adk.dev and used.

---

## §9 Say it in an interview

*"We opened our security phase by threat modelling an agent rather than an API, and the useful part
was choosing the unit. Asked per stage, our triage pipeline looked clean — no single stage held
private data, untrusted content and a way out at the same time. Asked along the path, the trifecta
was complete by the review stage, because the text carries the exposure forward even though the
capabilities stay put. Same wiring, opposite answer, and the reassuring one is what a normal design
review produces. Then we counted the ways out and found five, four of which do not look like network
calls: a markdown image in a reply whose URL is fetched by whoever renders it, the reply itself
going back to whoever opened the ticket, a memory row that comes back to a later question, and an
error message quoting the argument it choked on. Removing the fetch tool closed exactly one of the
five. We also measured the defence everyone reaches for first: a phrase blocklist caught three of
twelve spellings of one instruction, and widening it got to ten of twelve while refusing four of five
ordinary customers — including someone reporting a phishing mail, blocked for quoting it. So the
document we produced is generated from the same declarations the analysis runs on, and every risk in
it carries one of three verdicts, with a check that fails when a mitigation names nobody."*

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked, and you have run the commands rather than read
them. `./m done 66` refuses to commit until they are.

The day is finished when you can say, without looking, which stage the trifecta closes at and why the
per-stage answer differed — and when you can name the four channels that survive removing
`fetch_url`, and say for each one what it would cost to close it.

---

## §11 Ledger & commit

**`docs/PROGRESS.md`** — append this row:

```text
| 66 | 2026-09-06 | SEC-06, SEC-07 | 22 | <hash> | ⚠️ |
```

The gate column is `⚠️` and means it. `./m depth 66` is green over the twenty-two parts and the paper.
`lab/gate.py` is **red** by design: the trifecta finding from section 4 stands unresolved until Day
68 removes the capability, and `sutra/threat_model.py` is the build brief. The repository-wide `⚠️`
carried since Day 15 is unchanged — `tests/test_persona.py` still fails ruff `I001`, and it is the
learner's own file, which no generated day may edit.

**`docs/PACKAGES.md`** — no new rows. No package is added today.

**`docs/PAPERS.md`** — one row, already present, checked live today:

```text
| Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection | arXiv:2302.12173 | 2023 | 2026-09-06 | 66 | `days/day-66-injection-threat-model/papers/01-indirect-prompt-injection.md` |
```

**`docs/SKILL_PROVENANCE.md`** — no new rows. No third-party skill is used today.

**Commit:**

```text
day 66: threat model - prompt injection and the lethal trifecta - closes SEC-06, SEC-07
```
