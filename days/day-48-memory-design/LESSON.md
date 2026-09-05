---
day: 48
phase: 7
phase_name: "Memory and retrieval"
title: "Memory design — what to remember, what to forget"
ids: ["AG-12", "AG-13"]
principles: [1, 2, 4, 7, 8, 9, 10, 11, 13, 15, 16, 17, 18]
kind: concept
plan_version: "v2.2.1"
parts: 19
generated: "2026-09-05"
status: written
lab_scaffolded: true
commit: ""
---

# Day 48 — Memory design: what to remember, what to forget

> **Yesterday (Day 47):** `sutra/memory/persistence.py` put a database behind the session store, so a
> conversation survives a restart.
> **Today:** the decision that machinery has been waiting for. Given everything a support conversation
> leaves behind, what is written down, in what form, and what is dropped — as a policy you can run,
> price, and be wrong about.
> **Tomorrow (Day 49):** retrieval and embeddings. A local index over the ticket archive, built on
> whatever today's policy decided was worth keeping.

---

## §1 Where we are

Every kitchen has the drawer.

It holds string, three chargers for devices nobody owns any more, a tape measure, some batteries that
may or may not be flat, six takeaway menus and a key that fits nothing. Nothing in it was put there by
mistake. Every single item went in because at that moment it seemed like a thing you might want later,
and no item has ever been taken out, because taking things out is a job and putting them in is not.

The drawer is not short of information. It is short of *decisions*, and the consequence is that when
you actually need string you empty the whole drawer onto the counter.

[Day 46](../day-46-sessions-vs-memory/LESSON.md) gave Sutra a memory service and
[Day 47](../day-47-persistent-sessions/LESSON.md) made its sessions durable. Between them they built a
drawer, and armed a trap: filing a whole conversation is one line of code, and one-line powers get used
without thinking. Today is the day Sutra decides what goes in.

**This is a design day, and design days fail by becoming opinion essays.** So the subject is not a
philosophy of memory. It is a **policy**: a table of rows, a function that applies it, and a set of
numbers that let you argue about a row. Everything in this day can be run, and most of it can be wrong
in a way you can watch.

Four things to know before you read a part.

**The two IDs are the two halves of one question.** AG-12 is what to remember: six kinds of thing a
conversation leaves behind, of which two have a lifetime of zero. AG-13 is what to forget: expiry,
supersession, and **deletion on request** — which is not a feature you prioritise but an obligation you
discharge.

**The framework does not help with the last one.** `BaseMemoryService` in `google-adk==2.7.1` has four
public methods — three that add and one that searches — and **nothing that removes anything**. That was
read out of the installed source and confirmed against the live documentation page; §8 names both. A
memory system with no delete path is a liability, so the policy owns one or nobody does.

**Summarising to remember is the trap.** Compressing a conversation loses exactly the detail a later
retrieval needed, and the loss is invisible until it hurts. Section 5 measures it: a genuinely good
summary of one ticket answers **zero of four** questions that arrive later, and the extracted memos
answer three.

**And it is priced.** Every remembered item is context spent on every later turn that retrieves it.
Section 6 runs the real tokeniser over four candidate policies and gets numbers between 1200 and 8448
tokens per customer per year — on a free tier of twenty generations a day, where tokens are rationed
rather than billed.

---

## §2 The map

Nineteen parts in six sections, and no paper part — today cites two papers taught on earlier days as
addresses. This is a two-ID day, so sections 1 and 2 are AG-12 taken in order (*what a conversation
leaves*, then *how the rules get written down*), sections 3 and 4 are AG-13's two halves (*time and
replacement*, then *privacy and erasure*), section 5 breaks it on purpose, and section 6 is where both
IDs meet in a number. The day climbs `foundation → working → production`.

### Section 1 — `01-what-a-conversation-leaves`: the taxonomy (AG-12)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [The chat nobody can leave](parts/01-what-a-conversation-leaves/1.1-the-chat-nobody-can-leave.md) | Keeping everything is a policy; 653 characters against 290 | `foundation` |
| 1.2 | [Six kinds, not one bucket](parts/01-what-a-conversation-leaves/1.2-six-kinds-not-one-bucket.md) | Seven candidates, five written down, two refused by name | `foundation` |
| 1.3 | [The transcript is exhaust](parts/01-what-a-conversation-leaves/1.3-the-transcript-is-exhaust.md) | Not promoted, and not deleted either | `working` |
| 1.4 | [A correction outranks what it corrects](parts/01-what-a-conversation-leaves/1.4-a-correction-outranks-it.md) | Why `(holder, kind, subject)` cannot express a correction | `working` |

### Section 2 — `02-policy-as-data`: rules someone else can review (AG-12)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [A rule someone else can read](parts/02-policy-as-data/2.1-a-rule-someone-else-can-read.md) | Six rows against six branches, identical verdicts | `working` |
| 2.2 | [Every verdict names its row](parts/02-policy-as-data/2.2-every-verdict-names-its-row.md) | Split, not filter: kept plus refused equals proposed | `working` |
| 2.3 | [The kind with no rule](parts/02-policy-as-data/2.3-the-kind-with-no-rule.md) | Two memos that never expire and a refusal count of zero | `working` |

### Section 3 — `03-expiry-and-supersession`: two independent ways to stop being the answer (AG-13)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [True on the day it was said](parts/03-expiry-and-supersession/3.1-true-on-the-day-it-was-said.md) | One store, four dates, only the calendar moving | `working` |
| 3.2 | [The newer fact wins](parts/03-expiry-and-supersession/3.2-the-newer-fact-wins.md) | Three unexpired answers, two of them wrong | `working` |
| 3.3 | [A verdict is not an erasure](parts/03-expiry-and-supersession/3.3-a-verdict-is-not-an-erasure.md) | Same verdicts, 1302 bytes against 828 | `production` |

### Section 4 — `04-privacy-and-erasure`: the half that is an obligation (AG-13)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [Redact before you write](parts/04-privacy-and-erasure/4.1-redact-before-you-write.md) | Identical stores, and one backup holding the raw values | `working` |
| 4.2 | [You cannot delete what you cannot address](parts/04-privacy-and-erasure/4.2-you-cannot-delete-what-you-cannot-address.md) | A string search that deletes the wrong ticket and misses the right one | `working` |
| 4.3 | [Erasure is an obligation](parts/04-privacy-and-erasure/4.3-erasure-is-an-obligation.md) | Four public methods, none of which removes anything | `production` |
| 4.4 | [The store that must not be committed](parts/04-privacy-and-erasure/4.4-the-store-that-must-not-be-committed.md) | Forever retention and an access list of everyone | `production` |

### Section 5 — `05-failure-lab`: three ways this goes wrong on purpose

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [💥 The summary that lost the sentence you needed](parts/05-failure-lab/5.1-the-summary-that-lost-the-sentence.md) | 0 of 4 against 3 of 4, for 156 characters against 290 | `production` |
| 5.2 | [💥 The price that changed last year](parts/05-failure-lab/5.2-the-price-that-changed-last-year.md) | A 380-day-old number, quoted with total confidence | `production` |
| 5.3 | [💥 The rule that deleted the evidence](parts/05-failure-lab/5.3-the-rule-that-deleted-the-evidence.md) | The policy worked exactly as written, four months too early | `production` |

### Section 6 — `06-the-price`: where both IDs meet in a number (AG-12 · AG-13)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 6.1 | [Charged again on every turn](parts/06-the-price/6.1-charged-again-on-every-turn.md) | 73 tokens per turn, 36 of which never expire | `production` |
| 6.2 | [A policy nobody priced](parts/06-the-price/6.2-a-policy-nobody-priced.md) | Four policies, 1200 to 8448 tokens per customer per year | `production` |

### The papers — both taught on earlier days

Today adds no paper part. Three parts carry §6 *The paper behind it* as an **address**:
[1.3](parts/01-what-a-conversation-leaves/1.3-the-transcript-is-exhaust.md) and
[5.1](parts/05-failure-lab/5.1-the-summary-that-lost-the-sentence.md) cite *MemGPT*
(`arXiv:2310.08560`, taught on Day 20), and
[2.3](parts/02-policy-as-data/2.3-the-kind-with-no-rule.md) cites *The protection of information in
computer systems* (`doi:10.1109/PROC.1975.9939`, taught on Day 40). A paper is taught once in the
whole curriculum.

**Read section 1 before you write a line of `RETENTION`.** Sections 2 to 4 are all machinery for
applying a taxonomy, and every one of them is useless applied to a taxonomy nobody agreed on.

---

## §3 Setup — run this

**No package is added today, and no pin is moved.** `google-adk` stays at `2.7.1`,
`google-genai` at `2.19.0`. `git diff pyproject.toml uv.lock` must be empty when you finish. Today is
stdlib plus what is already installed, by design: curation must not depend on a model's mood.

```bash
# 1 - the day's lab
cd days/day-48-memory-design
mkdir -p lab

# 2 - the shared fixtures: one conversation, one policy
touch lab/session.py lab/policy.py lab/taxonomy.py

# 3 - section 1: what a conversation leaves
touch lab/noise.py lab/exhaust.py lab/correction.py

# 4 - section 2: policy as data
touch lab/branches.py lab/verdicts.py lab/unknown_kind.py

# 5 - section 3: expiry and supersession
touch lab/expiry.py lab/supersede.py lab/sweep.py

# 6 - section 4: privacy and erasure
touch lab/redact_demo.py lab/address.py lab/erase.py lab/gitcheck.py

# 7 - section 5: the failure lab
touch lab/lossy.py lab/stale.py lab/shredded.py

# 8 - section 6 and the day's gate
touch lab/price.py lab/defend.py lab/gate.py
cd -

# 9 - the project file you are about to fill (you type every line)
mkdir -p sutra/memory
touch sutra/memory/policy.py

# 10 - the freshness check, before anything else
curl -s -o /dev/null -w "%{http_code}\n" -L https://adk.dev/sessions/memory/
```

**Step 10 is the gate.** It must print `200`. That page is the one §8 quotes, and everything section 4
says about the absent delete path is checked against it plus the installed source. If it has moved
again, read the installed `google/adk/memory/` and amend before writing code (Principle 14).

**`sutra/memory/` is yours and it is shared.** Day 46 created the package and owns `__init__.py` and
`service.py`. Day 47 added `persistence.py`. You are adding `policy.py` beside them — a third module,
not a rewrite of either.

---

## §4 Build brief

### The project code — `sutra/memory/policy.py`, and you type every line

One file. The retention rules are **data, not code branches**, so that someone who is not a programmer
can review them.

| Symbol | Shape | What it must do |
| --- | --- | --- |
| `Rule` | a frozen dataclass | One row: `kind`, `keep_for_days`, `supersede`, `authority`, `redact`, and a **required** `why` (2.1). |
| `RETENTION` | a tuple of `Rule` | The policy. Adding a kind is adding a row, never an `if` elsewhere (2.1). |
| `RULES` | a dict built from `RETENTION` | Lookup by kind. Derived, never typed twice (2.1). |
| `PII_PATTERNS` | a dict of compiled patterns | What is stripped before a write, as data (4.1). |
| `what_to_keep` | `(candidates, *, today) -> (list[Memo], list[Refusal])` | Judge, **split rather than filter**, redact before constructing (2.2). |
| `what_to_forget` | `(memos, *, today, erased_holders) -> list[Verdict]` | Erasure, then expiry, then supersession — in that order (3.1, 3.2, 4.3). |
| `survivors` | `(verdicts) -> list[Memo]` | The only memos a retrieval may return (3.3). |
| `tombstone` | `(memo) -> Memo` | The shape with no content **and no holder** (4.3). |

- **`what_to_keep` returns two lists**, and neither is optional. Kept plus refused must equal proposed
  (2.2).
- **`today` is a required keyword argument** everywhere. Nothing in this module reads the clock; if it
  did, section 3 could not ask it what it thinks on four different dates (3.1).
- **Supersession keys on `(holder, subject)`**, never on the kind. That is the whole of 1.4.
- **Erasure is checked first**, ahead of expiry, so the audit trail says the customer asked rather than
  that it timed out (4.3).
- **Nothing is logged inside this module.** It returns everything it knows; the caller decides (2.2).

**`TODO(me)` markers left for you:**

- **1.2** — write the six rows of `RETENTION` for Sutra's desk, and decide whether six is the right
  number. For each row you add beyond the six, say which existing row it wants a *different retention
  rule* from; if there is no such row, it is not a new kind.
- **1.4** — decide Sutra's `authority` numbers, and write down what would have to be true for a
  `correction` to lose to something. Then say what breaks if you compare authority before date.
- **2.1** — fill in the `why` on every row, and make each one name the thing it is sized against. A
  `why` that says "standard retention" is a description, not a reason.
- **2.3** — decide what Sutra does with a refused unlisted kind beyond returning it: a log line, a
  counter, a quarantine, or nothing. Then write the alert threshold on the refusal rate, and say what
  a hundred percent refusal rate would mean.
- **3.1** — choose `keep_for_days` for every row, and beside each number write the event it is sized
  against. Two of them should be `None`; say why those two and not others.
- **3.3** — write the sweep. Decide whether it is a scheduled job or runs on write, whether it is
  resumable, and what it records about what it removed.
- **4.1** — tighten `PII_PATTERNS["EMAIL"]` so it stops eating the sentence's full stop, then write the
  test that pins it. Then decide which pattern classes Sutra is *not* covering and write that list
  down, because an uncovered class is not a bug you find later, it is a claim you never made.
- **4.2** — decide what `holder` is for Sutra: an account id, a contact id, or something else. Then
  answer the two-holder case — a memo about a transfer between accounts — by refusing it or by making
  the field a list. Both are defensible; not choosing is not.
- **4.3** — write the erasure path Sutra actually calls, given that `BaseMemoryService` has none. Then
  list every store a holder appears in — memory, sessions, logs, backups, Day 49's index — and say what
  reaches each one.
- **4.4** — add the memory store's path to `.gitignore` **before** the code that writes it lands, and
  decide whether `lab/gitcheck.py` belongs in `./m check`. Do not fix it with `*.json`.
- **6.1** — decide whether Sutra stores the token count on each memo at write time, and what that buys
  the retrieval path.
- **6.2** — produce the two-column table for Sutra's own policy: tokens per customer per year, beside
  what each candidate policy can still answer. Then choose, and write the number you would defend in a
  review.

### The lab — twenty scripts, none of which spends a generation

| File | What it does | Taught in |
| --- | --- | --- |
| `lab/session.py` | one synthetic support ticket, ten turns, no real customer | fixture |
| `lab/policy.py` | the rules as rows, and the two functions that apply them | 2.1, 2.2 |
| `lab/taxonomy.py` | the seven things that conversation left behind, classified | 1.2 |
| `lab/noise.py` | 653 characters against 290, for the same three useful entries | 1.1 |
| `lab/exhaust.py` | 698 characters of transcript, 294 of memos | 1.3 |
| `lab/correction.py` | two live billing addresses against one | 1.4 |
| `lab/branches.py` | six branches and six rows, identical verdicts | 2.1 |
| `lab/verdicts.py` | every verdict with the row that made it | 2.2 |
| `lab/unknown_kind.py` | two permanent memos nobody reviewed | 2.3 |
| `lab/expiry.py` | one store, four dates | 3.1 |
| `lab/supersede.py` | three unexpired answers to one question | 3.2 |
| `lab/sweep.py` | 1302 bytes against 828, and a substring that survives | 3.3 |
| `lab/redact_demo.py` | two clean stores and one dirty backup | 4.1 |
| `lab/address.py` | the deletion that hits the wrong ticket | 4.2 |
| `lab/erase.py` | tombstones, and ADK's four public memory methods | 4.3 |
| `lab/gitcheck.py` | is it ignored, is it clean — as an exit code | 4.4 |
| `lab/lossy.py` | 0 of 4 against 3 of 4 | 5.1 |
| `lab/stale.py` | a 380-day-old price, quoted | 5.2 |
| `lab/shredded.py` | a decision expired four months before the dispute | 5.3 |
| `lab/price.py` | the real tokeniser over the store, per kind | 6.1 |
| `lab/defend.py` | four policies, priced side by side | 6.2 |
| `lab/gate.py` | the day's seven assertions, as an exit code | §5 |

---

## §5 The eval that must be able to fail

Three checks with exit codes, plus eleven ablations, all on zero generations.

**The gate** is the day's definition of done, and it is red until you have written the module:

```bash
uv run python days/day-48-memory-design/lab/gate.py; echo "exit: $?"
```

Measured on 2026-09-05, before anything was written:
`- sutra.memory.policy is not importable: ModuleNotFoundError: No module named 'sutra.memory'`,
`findings: 1`, `exit: 1`.

When it prints `findings: 0` and `exit: 0`, seven statements are true: `RETENTION` is a table of rows,
every row has a non-empty `why`, an unlisted kind is refused, an expired memo reports expired, a
same-day correction supersedes the fact it corrects, an erasure request erases, and no email address
survives into a stored memo.

Then **break exactly one on purpose.** Change the `correction` row's `authority` from `3` to `1` and
run it again:

```text
- a correction did not supersede the same-day fact it corrects
findings: 1
exit: 1
```

One number, in a table, and the eval goes red. That is what the day is for.

**The git check** is red today for a real reason:

```bash
cd days/day-48-memory-design/lab
uv run python gitcheck.py; echo "exit: $?"
uv run python gitcheck.py --raw; echo "exit: $?"
cd -
```

`findings: 1` and `exit: 1` against `findings: 2` and `exit: 1`. The first finding is that
`sutra/data/memory.json` is not ignored by this repository, which is true as it stands and is a
`TODO(me)` in §4.

**The eleven ablations**, each with a named break in its own part:

```bash
cd days/day-48-memory-design/lab
uv run python noise.py;         uv run python noise.py --policy
uv run python correction.py --by-kind; uv run python correction.py
uv run python unknown_kind.py;  uv run python unknown_kind.py --permissive
uv run python supersede.py;     uv run python supersede.py --no-supersede
uv run python sweep.py;         uv run python sweep.py --sweep
uv run python redact_demo.py;   uv run python redact_demo.py --after
uv run python address.py;       uv run python address.py --keyed
uv run python lossy.py;         uv run python lossy.py --memos
uv run python stale.py;         uv run python stale.py --expiring
uv run python shredded.py;      uv run python shredded.py --tidy
uv run python price.py;         uv run python price.py --offline
cd -
```

And the five with no arms, which are measurements rather than experiments:

```bash
cd days/day-48-memory-design/lab
uv run python session.py; uv run python policy.py; uv run python taxonomy.py
uv run python exhaust.py; uv run python branches.py; uv run python verdicts.py
uv run python expiry.py;  uv run python erase.py;   uv run python defend.py
cd -
```

`lossy.py --memos` scores **3 of 4 and not 4**, on purpose. The question it misses is the one redaction
removed, and understanding why that is the honest result rather than a bug is the point of 5.1.

---

## §6 Request budget

**Free-tier Gemini**, 20 generate requests per day per model (`gemini-3.7-flash`, roster re-verified
2026-09-04).

| What | Generations |
| --- | --- |
| every part in every section | **0** |
| all twenty lab scripts, every flag | **0** |
| `price.py` and `defend.py`, live tokeniser | **0** (`count_tokens` is a separate endpoint) |
| `sutra/memory/policy.py` and the gate | **0** |
| **Total planned** | **0 of 20** |

**Zero, and it is the thesis rather than an economy.** The entire argument of this day is that curation
must not depend on a model's mood: a retention rule is a row, a verdict is a comparison, an expiry is
arithmetic on a date, and a deletion is a query on a field. None of that needs a generation, and a
policy that did would be a policy you could not test.

The two scripts that talk to the provider call **`count_tokens`**, which sits on separate quota from
`generate_content` — the technique Day 24's
[3.1](../day-24-token-accounting-and-budgets/parts/03-counting-before-spending/3.1-the-ledger.md)
established. Both also run with `--offline`, so the day is complete for a reader with no key at all.

The one thing worth spending quota on is not in this day: an **extractor** that reads a closed
conversation and proposes candidates. One generation per closed ticket, and the policy still judges the
output. That is Day 49's neighbourhood.

**Cost: $0.**

---

## §7 Traps

- **"We did not write a retention policy" and "our retention policy is keep everything" are the same
  sentence.** The second one is just the one nobody reviewed (1.1).
- **ADK's `InMemoryMemoryService` matches on *any* shared word**, with no stopword list, no scoring and
  no cutoff. A query containing `the` matches almost everything you have stored (1.1).
- **`add_session_to_memory` files every event with content.** No filter, no kind, no expiry. It is one
  line and it is a copy, not an extraction (1.3).
- **Storage strips the hedging.** "Might be a proxy issue, not sure" goes in and comes back three
  months later as a finding with a ticket number attached (1.2).
- **A correction and the fact it corrects are different kinds**, so keying supersession on
  `(holder, kind, subject)` means a correction can never win. Both stay live (1.4).
- **Two memos recorded on the same day tie**, and a tie means both survive. The correction and the fact
  it corrects are almost always from the same conversation (1.4).
- **Comparing `authority` before `recorded_on` pins the store to old corrections forever.** Date first
  (1.4, 3.2).
- **`if not rule.keep_for_days` refuses every permanent memo**, because `None` is falsy too. Test
  `== 0` and `is None` separately (2.2).
- **A filter throws away the item and the reason in the same instant.** Split, and check that kept plus
  refused equals proposed (2.2).
- **A default-keep policy gives the one category nobody reviewed the most permissive treatment in the
  system** — no expiry and no redaction, because both come from the row it does not have (2.3).
- **A refusing default without an alert on the refusal rate is data loss with good intentions** (2.3).
- **Storing the rule instead of the resolved expiry date** means changing the policy retroactively
  re-dates every memo already written (3.1).
- **A far-future sentinel instead of `None`** is a real date to every query that touches it (3.1).
- **`None < date` raises `TypeError` inside the loop**, taking every other verdict with it (3.1).
- **Expiry cannot fix a superseded fact and supersession cannot fix a stale one.** Three plan facts
  over two years are all unexpired and two are wrong (3.2).
- **`best[key]` raises `KeyError` for a `decision`**, because a non-superseding kind was never added.
  The `supersede` check must come first and short-circuit (3.2).
- **Subject-name drift silently disables supersession.** `billing_email` and `billing_address` are two
  buckets, and both go live (3.2).
- **A verdict is not a deletion.** Between the decision and the sweep, backups, replicas, analytics
  exports and debugging scripts all still see the row (3.3).
- **Redacting after the write leaves both stores identical and the backup dirty** — so the test passes
  and the raw values are on disk (4.1).
- **Logging the before-and-after of a redaction is a copy of the thing you removed**, in a store with a
  longer retention (4.1).
- **The email pattern eats the sentence's full stop.** `[\w.]+` is greedy; this day's own output shows
  it (4.1).
- **Deleting by searching text for an account id hits the ticket that *mentions* it and misses the one
  that is *about* it** — customers do not say their account numbers out loud (4.2).
- **`BaseMemoryService` has no delete, remove or forget method.** Not a deprecated one. None (4.3).
- **A tombstone that still names the holder is a queryable list of everyone who asked to be forgotten**
  (4.3).
- **Checking expiry before erasure** makes the audit trail say a record timed out when a customer
  actually asked (4.3).
- **`.gitignore` covers `*.db` and `*.sqlite3` and the memory store is JSON.** Git keeps everything,
  git is distributed, and this repository goes public in Phase 14 (4.4).
- **A summary is optimised for a general question and retrievals are specific.** A good summary of the
  billing ticket does not contain the billing address (5.1).
- **Keeping the summary *as well as* the memos** puts a prose account and five facts in one store with
  no rule for which wins when they disagree (5.1).
- **A stale memo gets more likely to be retrieved over time, not less.** Relevance scoring loves an
  exact subject match and nothing in the score knows about age (5.2).
- **The broken arm produces the better-sounding reply.** "The Business plan is 4800 a year" beats "let
  me check" in every demo and every satisfaction score (5.2).
- **Every retention rule has two costs and only one has a number.** Keeping costs a little,
  continuously, on a bill. Forgetting costs nothing until it costs everything (5.3).
- **A `keep_for_days` copied from the row above it** might be right, and nobody can tell, because the
  `why` says "standard retention" (5.3).
- **A memo is carried, not stored.** The prompt is resent every turn, so retention is priced per turn
  and multiplied by conversation length (6.1).
- **Character estimates are fine for a total and wrong for a row.** `4800` tokenises worse than prose
  (6.1).
- **A cost table with no answered-questions column argues for the policy that can answer nothing**
  (6.2).

---

## §8 Verify before you code

Fetched or read on **2026-09-05**, the day this was written.

**The ADK documentation:**

- `https://adk.dev/sessions/memory/` — fetched and read, **HTTP 200**. It documents `BaseMemoryService`
  with exactly four methods — `add_session_to_memory`, `search_memory`, `add_memory`,
  `add_events_to_memory` — and **no delete, erase, forget or removal method** for any implementation.
  It contains no mention of retention, TTL, expiry or deletion; the only retention-adjacent sentence is
  *"None, data is lost on restart"* about `InMemoryMemoryService`, which is about process lifetime
  rather than a deletion mechanism. This is the page 4.3 is built on.
- `https://adk.dev/docs/sessions/memory/` returned **HTTP 404**. The `/docs/` prefix that older
  material uses has moved; the live path has no prefix. Days 44 and 45 recorded the same shift for the
  tools pages, and `https://adk.dev/tools-custom/built-in-tools/` also 404s today while
  `https://adk.dev/tools/`, `https://adk.dev/sessions/state/` and `https://adk.dev/sessions/session/`
  all return 200.

**The installed SDK — the authoritative surface, read rather than guessed** (`google-adk==2.7.1`):

- `.venv/Lib/site-packages/google/adk/memory/base_memory_service.py` — `BaseMemoryService` declares
  `add_session_to_memory` (abstract), `search_memory` (abstract), `add_events_to_memory` and
  `add_memory`. The last two raise `NotImplementedError` with the messages *"This memory service does
  not support adding event deltas."* and *"This memory service does not support direct memory
  writes."*. **There is no removal method of any kind.** `add_memory`'s docstring notes that
  `custom_metadata` is the place for *"service-specific fields (e.g., TTL) that may later become
  first-class API parameters"* — which is the only retention hook the interface offers, and it is
  implementation-defined (4.3).
- `.venv/Lib/site-packages/google/adk/memory/in_memory_memory_service.py` — `add_session_to_memory`
  stores `[event for event in session.events if event.content and event.content.parts]` keyed on
  `(app_name, user_id)` then session id: every event with content, no filter (1.3, 4.2).
  `_extract_words_lower` is `set(word.lower() for word in re.findall(r'\w+', text, re.UNICODE))`, and
  the match test is `if any(query_word in words_in_event for query_word in words_in_query)` — **any**
  shared word, no scoring (1.1). The class docstring says *"for prototyping purpose only"* and *"Uses
  keyword matching instead of semantic search."*. It overrides nothing that removes anything.
- `.venv/Lib/site-packages/google/adk/memory/memory_entry.py` — `MemoryEntry` carries `content`,
  `custom_metadata`, `id`, `author` and `timestamp`, with `timestamp` documented as *"forwarded to
  LLM. Preferred format is ISO 8601"*. There is no holder field distinct from the filing user, which is
  4.2's whole problem.
- `.venv/Lib/site-packages/google/adk/memory/__init__.py` — `__all__` is `BaseMemoryService`,
  `InMemoryMemoryService`, `VertexAiMemoryBankService`, `VertexAiRagMemoryService`. The two
  Vertex-prefixed services need a billing account and are therefore 🅿️ **parked** under Addendum 02.
- `.venv/Lib/site-packages/google/adk/tools/load_memory_tool.py` — `load_memory(query, tool_context)`
  calls `tool_context.search_memory(query)` and returns a `LoadMemoryResponse`. It is a read path only.

**Two live commands, re-run today:**

```bash
curl -s -o /dev/null -w "%{http_code}\n" -L https://adk.dev/sessions/memory/
uv run python -c "from google.adk.memory import BaseMemoryService as B; print([m for m in dir(B) if not m.startswith('_')])"
```

The second prints
`['add_events_to_memory', 'add_memory', 'add_session_to_memory', 'search_memory']`. If a future
version adds a removal method, section 4.3 is amended before the code is (Principle 14).

**Nothing was pinned or installed today**, so `docs/PACKAGES.md` gets no row. The model string
`gemini-3.7-flash` and its ~20 requests per day are Day 2's finding, already in the ledger.

---

## §9 Say it in an interview

*"The memory-design day is the one where I stopped asking what the agent should remember and started
asking when each thing stops being true, because that is the only version of the question a policy can
act on. It came out as six kinds, and the useful part was that two of them have a lifetime of zero:
raw transcripts stay in the session store and never get promoted, and guesses never get written at
all — because storage strips the hedging, and 'might be a proxy issue, not sure' comes back three
months later as a finding with a ticket number attached.*

*The rules went in a table rather than in branches, with a required reason column. I would defend that
specifically for retention rather than as a general principle. How long we keep a record of what a
customer was told is a question about disputes and obligations, and the person who should answer it
does not read Python. I wrote both versions and they produce identical verdicts, so it is not about
correctness — it is that a comment is not a value and nobody is ever forced to fill one in.*

*Two things surprised me. The first was that supersession is the mechanism everyone keys wrong. If you
key it on holder, kind and subject, a correction can never supersede the fact it corrects, because
they are different kinds — so a customer says 'actually, no' mid-conversation and you end up with two
live billing addresses and a model picking one. It needs to key on holder and subject only, with an
authority number to break the same-day tie, and the ordering has to be date first or a correction from
last year beats a genuine change from this morning.*

*The second was that the framework has no delete. I read the memory interface we use — four public
methods, three that add and one that searches, and nothing that removes anything — and the
documentation page confirms it. So erasure on request is something the policy owns or nobody does, and
it is not a feature you prioritise against other features, it is an obligation. Ours checks erasure
first, ahead of expiry, because the audit trail needs to say the customer asked rather than that it
timed out, and what is left behind is a tombstone with the kind and the date and no holder — a
tombstone that names the person is a queryable list of everyone who asked to be forgotten.*

*And I priced it, because a design day that produces only opinions cannot be reviewed. Using the
token-counting endpoint, which is separate quota from generation, four candidate policies came out
between 1200 and 8448 tokens per customer per year. The one that catches people out is the cheap one:
an aggressive privacy-first policy costs a quarter of the others and can answer none of the questions
the desk actually gets asked. So I would never show that cost table without the column beside it saying
what each policy can still answer — the cost column on its own argues for the worst product."*

---

## §10 Done when

See [`CHECKLIST.md`](CHECKLIST.md). Every box is ticked because you ran the thing, not because you read
about it. `./m done 48` refuses to commit until they are.

---

## §11 Ledger & commit

**`docs/PROGRESS.md` — append this row** (fill in the hash after committing):

```markdown
| 48 | 2026-09-05 | AG-12, AG-13 | 19 | <hash> | ⚠️ |
```

**`docs/PACKAGES.md` — no new rows today.** No package is added and no pin is moved. The model string
`gemini-3.7-flash` already has its row from Day 2.

**`docs/PAPERS.md` — no new rows today.** Today teaches no paper. *MemGPT* (`arXiv:2310.08560`) and
*The protection of information in computer systems* (`doi:10.1109/PROC.1975.9939`) already have rows
naming Day 20 and Day 40 respectively, and this day cites both as addresses only.

**`docs/SKILL_PROVENANCE.md` — no new rows today.**

**Git commit message:**

```
day 48: memory design — what to remember, what to forget — closes AG-12, AG-13
```
