---
day: 50
phase: 7
phase_name: "Memory and retrieval"
title: "Chunking, top-k & when RAG is the wrong tool"
ids: ["AG-14"]
principles: [1, 2, 4, 7, 10, 11, 13, 15, 16, 17, 18]
kind: lab
plan_version: "v2.2.1"
parts: 19
generated: "2026-09-05"
status: written
lab_scaffolded: true
commit: ""
---

# Day 50 — Chunking, top-k and when RAG is the wrong tool

> **Yesterday (Day 49):** retrieval arrived. `sutra/retrieval.py` turned the ticket archive into a
> hand-built vector index — term counts, tf-idf weighting, cosine similarity, nearest neighbours — and
> wired it behind `load_memory`, so the desk finally gets *ranked* results instead of everything that
> shares a word.
> **Today:** the three decisions Day 49 left unexamined. **What** you cut the documents into, **how
> many** rows you take, and — the honest half — **whether this question was ever a retrieval question at
> all.** Every number here comes from a run, and the day spends no model calls.
> **Tomorrow (Day 51):** caching. Context and response caching as the quota lifeline — which is also
> the thing that changes today's arithmetic about whether to retrieve at all.

---

## §1 Where we are

Day 46 opened Phase 7 by drawing the line between a session and a memory, priced two ways of reaching a
store, and finished on a sentence it could not act on: *the cap fixes cost but buys no correctness,
because you cannot take the top three of an unranked list.* Day 49 supplied the ranking. **Today supplies
the k** — and, on the way, discovers that the k was the smaller half of the problem.

Here is the day as a scene at the desk. An agent types *"customer bounced back to the sign-in page during
single sign-on"* and the desk returns the right ticket, at the top, with a good score. Everything on
every dashboard says this worked. And the text it returned is the half of that ticket that restates the
problem — the resolution, the sentence naming `SameSite and Secure`, was on the other side of a cut that
a chunking constant made three weeks earlier, in a script nobody has opened since.

That is the shape of every failure in this day. Nothing raises. Nothing is logged. The metric everybody
reports says ten out of ten. The day's whole method is to add a second column — *did the text you sent
actually contain the answer?* — and then to sweep every knob against it until the constants stop being
opinions.

Three subjects, and the third is the one that makes the day honest:

- **Chunking.** A ticket is not a chunk and a chunk is not a document. Where you cut is decided before
  anyone asks a question, and no ranking afterwards can hand back half a row.
- **Top-k.** k is a budget, not a preference, because retrieved rows are written into the transcript and
  re-sent on every later turn.
- **When RAG is the wrong tool.** Retrieval answers one kind of question. Twelve real desk questions go
  through the procedure at the end of this day and **two** of them are retrieval questions.

The Phase 7 gate is *"Seen anything like this before?" answered at $0*. Today the second half of that
sentence is load-bearing: **zero model calls, all day**, because chunking and k are arithmetic and the
wrong-tool question is judgement.

---

## §2 The map

Nineteen parts in six sections, no paper part. Sections 1 and 2 are chunking — the two walls, then the
measurement that finds the ground between them. Section 3 is top-k, priced and swept. Section 4 is the
similarity floor and the right to return nothing. Section 5 is the four kinds of question retrieval
cannot answer, and section 6 turns all of it into a procedure and a park. The day climbs
`foundation → working → production`.

### Section 1 — `01-the-unit-you-index`: what a chunk is and the two ways it goes wrong

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [The unit you store is the unit you find](parts/01-the-unit-you-index/1.1-the-unit-you-store-is-the-unit-you-find.md) | 57 documents, 61 rows or 187 — and why ranking cannot fix a cut | `foundation` |
| 1.2 | [The document that averages itself away](parts/01-the-unit-you-index/1.2-the-document-that-averages-itself-away.md) | 0.235 against 0.465 for the same words, cut differently | `working` |
| 1.3 | [Cut too small to mean anything](parts/01-the-unit-you-index/1.3-cut-too-small-to-mean-anything.md) | hit@3 9/10 and answered@3 5/10 — the metric that cannot see it | `working` |
| 1.4 | [The margin you pay for twice](parts/01-the-unit-you-index/1.4-the-margin-you-pay-for-twice.md) | overlap buys two answers at 160 and nothing at 280 | `working` |

### Section 2 — `02-measuring-the-cut`: the answer key, the sweep, and what the sweep hides

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [The answer key you write before you tune](parts/02-measuring-the-cut/2.1-the-answer-key-you-write-before-you-tune.md) | three columns, not two, and four questions with no answer | `working` |
| 2.2 | [One table, seven chunk sizes](parts/02-measuring-the-cut/2.2-one-table-seven-chunk-sizes.md) | 459 tokens to 279 for the same 10/10 — `CHUNK_SIZE = 900` | `production` |
| 2.3 | [💥 The cut that kept the ticket and lost the fix](parts/02-measuring-the-cut/2.3-the-cut-that-kept-the-ticket-and-lost-the-fix.md) | right document, wrong half, score 0.381, every metric green | `production` |

### Section 3 — `03-the-k-is-a-budget`: what k costs and what it buys

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [k is a budget, not a preference](parts/03-the-k-is-a-budget/3.1-k-is-a-budget-not-a-preference.md) | 8,539 tokens against 1,006 over one conversation | `working` |
| 3.2 | [Where the curve goes flat](parts/03-the-k-is-a-budget/3.2-where-the-curve-goes-flat.md) | the knee is at 2; k=20 is 92% noise — `TOP_K = 2` | `production` |
| 3.3 | [💥 Twenty rows, and nothing new in nineteen](parts/03-the-k-is-a-budget/3.3-twenty-rows-and-nothing-new-in-nineteen.md) | the answer at rank 7, a quarter into the block | `production` |

### Section 4 — `04-the-floor`: the right to return nothing

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [💥 Cosine never says it does not know](parts/04-the-floor/4.1-cosine-never-says-it-does-not-know.md) | a printer question scoring 0.388 on `on` and `the` | `production` |
| 4.2 | [There is no floor that separates them](parts/04-the-floor/4.2-there-is-no-floor-that-separates-them.md) | the gap is −0.209, so one condition is not enough | `production` |
| 4.3 | [Nothing is an answer](parts/04-the-floor/4.3-nothing-is-an-answer.md) | the sentence the desk says, and the one it may not | `production` |

### Section 5 — `05-the-wrong-tool`: four questions retrieval cannot answer

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [When the answer is a rule](parts/05-the-wrong-tool/5.1-when-the-answer-is-a-rule.md) | a refund policy answered with a rate-limit ticket at 0.266 | `working` |
| 5.2 | [When the answer must be true now](parts/05-the-wrong-tool/5.2-when-the-answer-must-be-true-now.md) | 0 of 61 rows carry a date | `working` |
| 5.3 | [When the answer has to be counted](parts/05-the-wrong-tool/5.3-when-the-answer-has-to-be-counted.md) | the answer is 12 of 52; retrieval returns 3 and no number | `working` |
| 5.4 | [When the whole archive fits in the prompt](parts/05-the-wrong-tool/5.4-when-the-whole-archive-fits-in-the-prompt.md) | 2,795 tokens — 31x, inside the judgement band | `production` |

### Section 6 — `06-in-production`: the procedure, and what is deliberately not built

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 6.1 | [The five questions, in order](parts/06-in-production/6.1-the-five-questions-in-order.md) | 12 questions, 2 of them retrieval, and an ablation that flips 2 | `production` |
| 6.2 | [🅿️ Rerankers, hybrid search and a vector database](parts/06-in-production/6.2-rerankers-hybrid-search-and-a-vector-database.md) | what each buys, and the number that would change the answer | `production` |

**No paper part today.** *Lost in the Middle* (`arXiv:2307.03172`) is cited as an address by 3.3 and 5.4
and is taught on Day 19. Day 49 teaches the retrieval-augmented generation paper; today builds on the
mechanism rather than on the proposal.

**Read the sections in order.** Section 2 cannot be read without section 1's two failures, and section 6
is a summary of section 5 in a usable shape rather than a replacement for it.

---

## §3 Setup — run this

**No package is added today and no pin moves.** `google-adk` stays at `2.7.1`, `google-genai` at
`2.19.0`. Everything in this day is the Python standard library and arithmetic. `git diff pyproject.toml
uv.lock` must be empty when you finish.

```bash
# 1 - the day's lab
cd days/day-50-chunking-and-top-k
mkdir -p lab

# 2 - the two shared modules everything imports
touch lab/_archive.py lab/_index.py

# 3 - section 1: the unit you index
touch lab/fragment.py lab/dilution.py lab/overlap.py

# 4 - section 2: measuring the cut
touch lab/gold.py lab/sweep.py lab/split.py lab/ranks.py

# 5 - section 3: the k
touch lab/price.py lab/curve.py lab/middle.py

# 6 - section 4: the floor
touch lab/garbage.py lab/floor.py lab/nothing.py

# 7 - sections 5 and 6: the wrong tool, and the procedure
touch lab/wrongtool.py lab/decide.py

# 8 - the day's gate
touch lab/gate.py
cd -

# 9 - the test file you fill in today (you type every line)
touch tests/test_retrieval_tuning.py

# 10 - confirm Day 49's module is there to extend
python -c "import sutra.retrieval as r; print(sorted(n for n in dir(r) if not n.startswith('_')))"
```

**Step 10 is the one that matters.** Today **extends** `sutra/retrieval.py`; it does not rewrite it.
`build_index`, `search`, `cosine` and `tokenize` are Day 49's and must still be there when you finish —
`lab/gate.py` checks exactly that. If step 10 fails, Day 49 is not done and today cannot start.

`lab/_index.py` is the lab's own copy of Day 49's arithmetic plus the two new knobs, so that every table
in this day is reproducible from a fresh checkout without the project module being finished. That
duplication is deliberate and it is confined to `lab/`.

---

## §4 Build brief

### The project code — `sutra/retrieval.py`, extended, and you type every line

Four new constants and four new functions. Day 49's functions are **not touched**.

| Symbol | Shape | What it must do |
| --- | --- | --- |
| `CHUNK_SIZE` | `int` | The cut, in characters, with a comment naming the sweep it came from (2.2) |
| `CHUNK_OVERLAP` | `int` | The shared margin, with the run that says whether it earns its keep (1.4) |
| `TOP_K` | `int` | The rows returned, with the curve it was read off (3.2) |
| `SIM_FLOOR` | `float` | The score below which a row is dropped, and the answer it costs (4.2) |
| `MIN_SHARED_TERMS` | `int` | Informative words a row must share with the question (4.2) |
| `chunk_document` | `(str, int, int) -> list[str]` | Cut one document; raise when the overlap is not smaller than the size (1.1) |
| `chunked_rows` | `(dict[str, str]) -> dict[str, str]` | The archive as rows, with `#n` refs (1.1) |
| `parent_ref` | `(str) -> str` | `ticket:4610#3` -> `ticket:4610` (1.1) |
| `retrieve` | `(Index, str, int) -> list[tuple[float, str]]` | `search` plus both conditions; **returns `[]` when nothing survives** (4.3) |

- **Every constant carries a comment naming the run it came from**, with the date. `lab/gate.py` fails
  the day on a bare number, and that check is the ritual half of Principle 7 pointed at a tuning
  parameter.
- **`retrieve` wraps `search`; it does not replace it.** Day 49's ranking is untouched and the two
  conditions are applied on top of it, so the two concerns stay separable and either can be measured
  alone.
- **An empty list is a normal return value**, not an exception and not `None`
  ([4.3](parts/04-the-floor/4.3-nothing-is-an-answer.md)).

**`TODO(me)` markers left for you:**

- **2.2** — choose `CHUNK_SIZE` and write the sweep row it came from in the comment beside it. Then say,
  in the same comment, **how many documents in the archive are actually longer than it** — because on
  this corpus that number is four, and the next person needs to know that the constant barely bites.
- **1.4** — choose `CHUNK_OVERLAP`. The measurement says zero at this size. Write down the chunk size at
  which you would turn it on, and the number in the sweep that would tell you.
- **3.2** — choose `TOP_K`, and then decide the harder thing: `sutra/memory/service.py` already holds a
  `TOP_K` from Day 46. **Decide which module owns the number**, make the other import it, and write down
  why that one is the owner. Two constants with the same name and different values is a bug waiting for
  a quiet week.
- **4.2** — choose `SIM_FLOOR` and `MIN_SHARED_TERMS` off the sweep, and write **the cost** in the
  comment: which gold question you are choosing to lose, and why losing it is better than the impostor
  you are choosing to reject.
- **4.3** — write the sentence the desk says when `retrieve` returns nothing. It goes in the agent's
  instruction, not in `retrieval.py`. Then write down the sentence it must **never** say, and why.
- **5.2** — decide whether to write each document's date and status into its chunk text at index time.
  Measure what it costs in tokens per row before deciding, and say what it would let the desk do that it
  currently cannot.
- **5.3** — write the one-sentence description of the retrieval tool that says what it **cannot** do.
  Day 4's [1.3](../day-04-tools-by-hand/parts/01-the-schema/1.3-the-description-is-the-prompt.md): the
  description is the prompt.
- **6.1** — add three questions of your own to `decide.py`, answered honestly, and reconcile any
  disagreement between your `expect` and the routing.
- **6.2** — write the two trigger numbers as an ADR: the mean answer rank above which you add a reranker,
  and the row count above which you move to a real store.

### The tests — `tests/test_retrieval_tuning.py`, and you type every line

Five test functions, named as sentences, all offline and all fast:

| Test | What it pins |
| --- | --- |
| `test_chunk_document_respects_size_and_overlap` | windows are at most `size`, and neighbours share exactly `overlap` |
| `test_chunk_document_refuses_an_overlap_it_cannot_advance_past` | `pytest.raises(ValueError)` on `overlap >= size` (1.1) |
| `test_a_chunk_ref_resolves_to_its_parent_document` | `parent_ref("ticket:4610#3") == "ticket:4610"` |
| `test_retrieve_returns_nothing_for_a_question_with_no_informative_overlap` | the printer question comes back empty (4.1, 4.3) |
| `test_retrieve_still_finds_a_known_answer` | the guard against a rule so strict it refuses everything |

The last one is the important one and it is the one people leave out. A refusal rule with no positive
test passes perfectly when it refuses every question in the archive.

### The lab — sixteen scripts, all of which run, none of which call a model

| File | What it does | Taught in |
| --- | --- | --- |
| `lab/_archive.py` | 57 documents, a ten-question gold set with three columns, four unanswerable questions | all |
| `lab/_index.py` | Day 49's arithmetic plus `chunk`, `split_docs`, `parent`, the two metrics | all |
| `lab/fragment.py` | the same ticket at 80 and at 900 characters, and both metrics | 1.1, 1.3 |
| `lab/dilution.py` | the incident review whole, then in twelve pieces, scored | 1.2 |
| `lab/overlap.py` | five overlaps at one chunk size, with the index growth | 1.4 |
| `lab/gold.py` | the answer key, and how many words each question shares with its target | 2.1 |
| `lab/sweep.py` | seven chunk sizes, two arms, four columns | 2.2 |
| `lab/split.py` | one question, three sizes: right document, wrong half | 2.3 |
| `lab/ranks.py` | the rank of every gold target at five chunk sizes | 2.2 |
| `lab/price.py` | k against a conversation, not against a request | 3.1 |
| `lab/curve.py` | eight values of k, with useful rows and noise | 3.2 |
| `lab/middle.py` | where the answer lands inside the block at k=2 and k=20 | 3.3 |
| `lab/garbage.py` | four unanswerable questions, and what matched | 4.1 |
| `lab/floor.py` | two distributions and the gap between them | 4.2 |
| `lab/nothing.py` | fifteen settings of the two-condition rule, and the sentence | 4.2, 4.3 |
| `lab/wrongtool.py` | four arms: `rule`, `current`, `count`, `fits` | 5.1–5.4 |
| `lab/decide.py` | twelve questions through the five checks, with an exit code | 6.1 |
| `lab/gate.py` | the day's definition of done, as six findings | §5 |

---

## §5 The eval that must be able to fail

Three checks with exit codes, and every one of them runs on zero model calls.

**The gate** is the day's definition of done, and it is red until the module is written:

```bash
uv run python days/day-50-chunking-and-top-k/lab/gate.py; echo "exit: $?"
```

Measured on 2026-09-05, before anything was written: `1-6: sutra.retrieval is not importable: No module
named 'sutra'`, `findings: 1`, `exit: 1`. When it prints `findings: 0` and `exit: 0`, six statements are
true: the five constants exist, the four functions exist, **every constant carries a comment naming its
measurement**, Day 49's `build_index` and `search` are still there, an unanswerable question comes back
empty, and the overlap is smaller than the size. Then break exactly one on purpose — delete the comment
after `TOP_K` — and watch finding 3 appear.

**The routing procedure**, which fails when the priorities change rather than when the code breaks:

```bash
cd days/day-50-chunking-and-top-k/lab
uv run python decide.py; echo "exit: $?"
uv run python decide.py --skip-rule; echo "exit: $?"
cd -
```

`misrouted: 0 of 12` and `exit: 0` in the first arm. `misrouted: 2 of 12` and `exit: 1` in the second, and
both misroutes go to retrieval — which is the day's thesis reduced to an exit code.

**The test suite**, offline and green:

```bash
uv run python -m pytest tests/test_retrieval_tuning.py -q -m "not live"
```

Red as shipped, because `tests/test_retrieval_tuning.py` is empty until you write it.

**And every measurement in the day, re-runnable:**

```bash
cd days/day-50-chunking-and-top-k/lab
uv run python fragment.py; uv run python fragment.py --size 900
uv run python dilution.py --whole; uv run python dilution.py
uv run python overlap.py; uv run python overlap.py --size 280
uv run python gold.py; uv run python gold.py --leak
uv run python sweep.py; uv run python sweep.py --overlap
uv run python split.py; uv run python split.py --size 900
uv run python ranks.py
uv run python price.py; uv run python price.py --turns 10
uv run python curve.py
uv run python middle.py --k 2; uv run python middle.py
uv run python garbage.py; uv run python garbage.py --terms
uv run python floor.py
uv run python nothing.py; uv run python nothing.py --say
uv run python wrongtool.py rule; uv run python wrongtool.py current
uv run python wrongtool.py count; uv run python wrongtool.py fits
cd -
```

`floor.py` **reports a negative gap on purpose**: `the gap : -0.209`. That is the finding, not a broken
lab.

---

## §6 Request budget

**Free-tier Gemini**, 20 generate requests per day per model (`gemini-3.7-flash`, roster re-verified
2026-09-04).

| What | Generations |
| --- | --- |
| every part in every section | **0** |
| all eighteen lab scripts, every flag | **0** |
| `sutra/retrieval.py`, the gate and the five tests | **0** |
| **Total planned** | **0 of 20** |

**Zero, and today the zero is the argument rather than the economy.** Chunking is a slice. Ranking is a
dot product over dictionaries. A gold set is a list somebody wrote. Every table in this day is arithmetic
over 12,716 characters of synthetic text, and the fact that a whole day of retrieval tuning costs nothing
is the reason the tuning can be repeated on every change instead of once, at launch, by whoever had quota
left.

The one thing worth spending quota on, once, is handing a model the k=20 block from
[3.3](parts/03-the-k-is-a-budget/3.3-twenty-rows-and-nothing-new-in-nineteen.md) and the k=2 block and
comparing the two answers. It costs two generations and it will show you the effect this day measured the
inputs to. It is **not** required, and no number in this day depends on it.

**Cost: $0.**

---

## §7 Traps

- **Chunk size is decided at index time and no k fixes it.** Ranking chooses between rows and cannot
  build one (1.1).
- **If the row count does not grow when the chunk size falls, you are not chunking.** Every document is
  shorter than the window and the constant does nothing (1.1).
- **A character splitter cuts words in half.** `inves` and `tigation` are two rows and neither is a word
  (1.3).
- **One vector is one average.** The incident review scores 0.235 where its own best paragraph scores
  0.465 (1.2).
- **Small chunks match better and answer worse.** At 80 characters, hit@3 is 9/10 and answered@3 is 5/10;
  at 40 characters, answered@3 is 2/10 (1.3).
- **Overlap is a repair, not a default.** At chunk 160 it takes answered@3 from 6 to 8 for 19% more index;
  at chunk 280 it buys nothing and at 160 of overlap it stores 60% more text than the archive contains
  (1.4).
- **A two-column gold set cannot see chunking bugs.** hit@k was flat at 10/10 across six of seven chunk
  sizes while answered@3 went from 10 to 5 (2.1, 2.2).
- **Ten questions means one question is ten percentage points.** Read every table in this day for its
  shape, never for a one-row difference (2.1).
- **The half of a document that answers your question is the half that least resembles it.** A question is
  a description of the symptom, so the symptom chunk wins (2.3).
- **A retrieved chunk is written into the transcript and re-sent on every later turn.** k=20 costs 8,539
  tokens over six turns against 1,006 at k=2 (3.1).
- **Recall plateaus far earlier than anybody sets k.** The knee is at 2; at 20 the retrieval is 92% noise
  (3.2).
- **Raising k does not move the answer up, it builds a middle for the answer to sit in.** One gold answer
  lands at rank 7, a quarter into a 4,260-character block (3.3).
- **Cosine similarity always returns something.** A question whose only known words are `on` and `the`
  scored 0.388 — higher than nine of the ten real answers (4.1).
- **There is no similarity floor that separates real answers from nonsense on this archive.** The worst
  real answer is 0.180 and the best impostor is 0.388: the gap is negative (4.2).
- **A second condition beats a stricter first one.** Floor 0.20 with two shared informative terms keeps
  9/10 long answers, 3/3 short ones and rejects 4/4 impostors; demanding three terms rejects all three
  short questions (4.2).
- **A similarity floor is not portable.** Scores depend on the whole index, so re-chunking or swapping the
  retriever invalidates the number (1.2, 4.2).
- **"I found nothing" and "there is no past case" are different claims**, and only the first is one the
  retriever can make (4.3).
- **An empty list rendered as a blank prompt section is worse than saying nothing**, because the model
  will explain the blank itself (4.3).
- **An archive holds what happened, never what is allowed.** A refund policy question returns a rate-limit
  ticket at 0.266, above the floor and past the shared-terms rule (5.1).
- **Zero of 61 rows carry a date**, so a question containing "right now" has nothing to match, and
  rebuilding the index more often does not fix it (5.2).
- **Ranking discards everything outside the top k, so it cannot count.** The true answer was 12 of 52 and
  retrieval returned 3 rows and no number — and with distinctive words in the question, a model will
  report the value of `TOP_K` as the count (5.3).
- **The whole archive is 2,795 tokens.** At 31x a retrieval, this corpus is inside the band where "just
  paste it" is a real alternative (5.4).
- **The order of the five checks carries as much as the checks.** Drop the first and two of twelve
  questions silently become retrieval (6.1).

---

## §8 Verify before you code

Read or fetched on **2026-09-05**, the day this was written.

**Nothing new was installed and no API surface is new**, so today's verification is arithmetic
provenance rather than documentation:

- **`CHARS_PER_TOKEN = 4.55`** is not re-derived today. It was measured against the provider's own
  tokenizer on Day 24, part
  [1.1](../day-24-token-accounting-and-budgets/parts/01-what-a-request-costs/1.1-a-ticket-id-costs-five-tokens.md),
  and it is quoted with that citation in `lab/_index.py`. Counting tokens for real is a network call and
  this day makes none.
- **The free-tier ceiling of 20 requests per day** for `gemini-3.7-flash` was read off a live 429 on Day 2
  and recorded in `docs/PACKAGES.md`. It is quoted in `lab/price.py` and not re-checked, because nothing
  today spends a request.
- **`arXiv:2307.03172`, *Lost in the Middle: How Language Models Use Long Contexts*, 2023** — verified on
  2026-09-03, row already in `docs/PAPERS.md`, taught on Day 19 at
  [`papers/01-lost-in-the-middle.md`](../day-19-context-engineering-selection/papers/01-lost-in-the-middle.md).
  Cited as an address by parts 3.3 and 5.4; not re-taught.
- **`arXiv:2005.11401`, *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*, 2020** — row
  already in `docs/PAPERS.md`, taught by Day 49. Today builds on the mechanism rather than the proposal,
  which is Principle 4 at the scale of a phase.

**Two commands, run today, that establish what this day may assume:**

```bash
python -c "import sutra.retrieval as r; print(sorted(n for n in dir(r) if not n.startswith('_')))"
uv run python days/day-50-chunking-and-top-k/lab/gate.py; echo "exit: $?"
```

The first says whether Day 49's module is there to extend. The second, run before any of today's code
existed, printed `1-6: sutra.retrieval is not importable: No module named 'sutra'` and `exit: 1` — which
is the correct starting state and is the reason `lab/_index.py` carries its own copy of the arithmetic.

**What no documentation says**, and what therefore had to be measured: every constant this day ships.
There is no page anywhere that will tell you the right chunk size, the right k or the right similarity
floor for your archive, and any page that appears to is describing somebody else's corpus. That is the
whole reason section 2 exists.

---

## §9 Say it in an interview

*"Day 49 gave the desk a ranked retriever. Day 50 was the day I found out that the ranking was the easy
part, and it started by adding one column to my evaluation. The usual retrieval metric is hit@k — is the
right document in the top k — and I added answered@k, which checks whether the text I actually sent
contained the answer. Those two columns disagree constantly, and every real finding I had came out of the
gap between them.*

*Chunking first. I swept seven chunk sizes over the same archive and the same gold set, and hit@3 was flat
at ten out of ten across six of them. Chunking bought me no recall at all. What it bought was cost: the
retrieved context for one question went from four hundred and fifty-nine tokens to two hundred and
seventy-nine, thirty-nine per cent, with answered@3 still perfect. Below four hundred characters
answered@3 collapsed to six and then five while hit@3 stayed at ten, because small chunks match sharply
and are too small to answer from. The failure I would actually talk about is the boundary one: at four
hundred characters, my top hit for a sign-in question was the correct ticket, scoring 0.381, and it did
not contain the fix — the cut had fallen between the symptom and the resolution, and the question a
support agent types is a description of the symptom, so the symptom half wins every time. Raising k does
not fix that, because the resolution half is genuinely dissimilar to the question. The fix is at the cut.*

*Then top-k. I priced it over a conversation rather than over a request, because retrieved rows are
written into the transcript and re-sent every turn. At k equals two, one lookup cost about a thousand
tokens over six turns; at k equals twenty it cost eight and a half thousand. And it bought nothing — the
answer rate reached ten out of ten at k equals two and never moved, so at twenty, ninety-two per cent of
what I was sending came from documents the answer key does not name. It also pushed the answer into the
middle: one question's answer-bearing row was at rank seven, starting a quarter of the way into a
four-thousand-character block, which is the region Lost in the Middle measured as the least reliably
used. A ranked list with a bad k is still a bad answer.*

*The part I am most pleased with is the floor. Cosine similarity always returns something — I asked my
archive about an office printer, which it knows nothing about, and got a top score of 0.388, higher than
nine of my ten real answers, because the only two words of the question the index had ever seen were 'on'
and 'the'. So I tried to set a similarity threshold and found I could not: the worst real answer scored
0.180 and the best impostor scored 0.388, so the gap was negative and no single number separates them.
What worked was a second condition rather than a stricter first one — how many of the question's
informative words actually appear in the matched row, which is information the score throws away. A floor
of 0.20 with at least two shared terms keeps nine of ten real answers, keeps the short two-word questions
a real agent types, and rejects all four impostors. It loses one real answer on purpose, and that trade is
written in the comment beside the constant.*

*And the half of the day I would lead with is when not to use retrieval at all. I ran twelve real desk
questions through five checks in a fixed order — is the answer a rule someone decided, must it be true
right now, does it need every record visited, does the whole corpus fit in the prompt, and only then, does
the archive plausibly hold a similar case. Two of the twelve were retrieval questions. Two more had no
answer and got an honest refusal. The order matters: I ablated the first check and two questions silently
became retrieval, and I had already measured what that looks like — a refund policy question returning a
ticket about API rate limits at a score that clears my floor. The one that surprised me most was the size
check. My whole archive is two thousand seven hundred and ninety-five tokens. It fits eleven times over
in a thirty-two-thousand-token window, and one retrieval is ninety-one tokens, so retrieval is buying me a
factor of thirty-one in exchange for four documented ways to miss. That is a judgement call, not an
obvious win, and I would rather say so than pretend the architecture was inevitable.*

*The whole day cost zero model calls, which is the other thing I would mention. Chunking is a slice and
ranking is a dot product, so the tuning can be re-run on every change instead of once at launch."*

---

## §10 Done when

See [`CHECKLIST.md`](CHECKLIST.md). Every box is ticked because you ran the thing, not because you read
about it. `./m done 50` refuses to commit until they are.

---

## §11 Ledger & commit

**`docs/PROGRESS.md` — append this row** (fill in the hash after committing):

```markdown
| 50 | 2026-09-05 | AG-14 | 19 | <hash> | ⚠️ |
```

**`docs/PACKAGES.md` — no new rows today.** No package is added, no pin moves, and nothing is installed.
The whole day is the standard library.

**`docs/PAPERS.md` — no new rows today.** *Lost in the Middle: How Language Models Use Long Contexts*
(`arXiv:2307.03172`, 2023) already has its row, verified 2026-09-03, naming Day 19 and
`days/day-19-context-engineering-selection/papers/01-lost-in-the-middle.md`. Today cites it as an address
from parts 3.3 and 5.4 and teaches no paper of its own.

**`docs/SKILL_PROVENANCE.md` — no new rows today.**

**Git commit message:**

```
day 50: chunking, top-k and when RAG is the wrong tool — closes AG-14
```
