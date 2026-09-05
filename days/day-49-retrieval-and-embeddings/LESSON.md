---
day: 49
phase: 7
phase_name: "Memory and retrieval"
title: "Retrieval & embeddings — one honest RAG day"
ids: ["AG-33", "ADK-30"]
principles: [1, 2, 4, 7, 8, 10, 11, 13, 15, 16, 17, 18]
kind: lab
plan_version: "v2.2.1"
parts: 20
generated: "2026-09-05"
status: written
lab_scaffolded: true
commit: ""
---

# Day 49 — Retrieval & embeddings: one honest RAG day

> **Yesterday (Day 48):** memory design. `sutra/memory/policy.py` decided what is worth keeping and
> what must be forgotten, as rules a person can read rather than as branches in code.
> **Today:** the desk learns to answer *"has anything like this happened before?"* by **meaning**
> rather than by matching words. You build a vector index by hand, watch it fail the meaning test at
> a score of exactly `0.000`, reach for a local embedding model, and put the whole thing behind
> `BaseMemoryService` so Day 46's `load_memory` tool returns a **ranked** answer.
> **Tomorrow (Day 50):** chunking, top-k, and the honest half — when RAG is the wrong tool. Day 50
> extends `sutra/retrieval.py` and chooses today's two constants from evidence.

---

## §1 Where we are

Day 46 ended on a finding it could not fix, and wrote it down in one sentence:

> **The cap made the response smaller and no more correct**, because you cannot take the top three of
> a list that has no top.

The desk has a memory. It files finished conversations and it can search them. What it cannot do is
put the results in any order, because `InMemoryMemoryService` matches on a single shared word and
returns whatever it found in the order it was filed. Day 46 measured a normal-sounding question
matching **four out of four** archived tickets, and the first one — the one anything reading the list
would use — was about printing an invoice, in answer to a question about being logged out.

**Today is that correctness fix.** Not a new feature: the repair for a feature the desk already has
and currently gets wrong.

Here is the scene it has to survive. A support agent has ticket 4521 open. It says *"Auth redirect
bug: after the identity provider hands control back, our user lands at a blank sign-in screen."* She
asks the desk whether anything like it has come up before.

It has. Eighteen months ago, ticket 4188: *"Login loop on the staff portal. Session cookie written
without SameSite, so the browser dropped it. Fix KB-104."* Same fault. Same fix. Sitting in the
archive.

The two tickets share exactly one word, and that word is `the`.

So the day runs in the order Principle 4 demands. You build a vector index by hand — counting words,
weighting them by rarity, scoring by cosine — and it works well on a question written in the
archive's own vocabulary. Then you ask it the 4521 question and it scores the right answer at
**`0.000`** and puts a caching bug first at `0.270`. That zero is the whole motivation for embeddings
and it is measured, not asserted.

Then you reach for a local embedding model, put it behind the same function boundary so nothing
downstream notices, wire the result into ADK, and finish by breaking it three more ways: the answer
that was never in the archive, the index nobody rebuilt, and the query the model actually sent.

The Phase 7 gate is one question: **"Seen anything like this before?" answered at $0.** Today is the
half about whether the answer is any good.

---

## §2 The map

Twenty parts in six sections, plus two papers. Sections 1, 2 and 3 are **AG-33** — the mechanism
built by hand, the failure that motivates embeddings, and the embedding lane itself. Sections 4 and 5
are **ADK-30** — the retriever behind ADK's memory interface, and the three ways it still lies.
Section 6 is where the day is made durable. The day climbs `foundation → working → production`.

### Section 1 — `01-text-as-numbers`: building a vector index by hand (AG-33)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [The counter that takes a description](parts/01-text-as-numbers/1.1-the-counter-that-takes-a-description.md) | A lookup against a search by description, and what each fails like | `foundation` |
| 1.2 | [A ticket as a list of numbers](parts/01-text-as-numbers/1.2-a-ticket-as-a-list-of-numbers.md) | Term counts, a bag of words, and 67 zeros out of 80 | `foundation` |
| 1.3 | [Direction, not size](parts/01-text-as-numbers/1.3-direction-not-size.md) | Why cosine and not a dot product: `11.000` beats `3.000` the wrong way | `foundation` |
| 1.4 | [The word that tells you nothing](parts/01-text-as-numbers/1.4-the-word-that-tells-you-nothing.md) | tf-idf, and why `fix` and `kb` weigh exactly `0.000` here | `working` |
| 1.5 | [The work you do once](parts/01-text-as-numbers/1.5-the-work-you-do-once.md) | Index time against query time, and what goes in the file | `working` |

### Section 2 — `02-the-meaning-test`: the failure that makes embeddings necessary (AG-33)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [💥 The score that came back zero](parts/02-the-meaning-test/2.1-the-score-that-came-back-zero.md) | 4188 at `0.000`, ranked 5 of 8, and a caching bug first at `0.270` | `production` |
| 2.2 | [The repairs that fix one pair](parts/02-the-meaning-test/2.2-the-repairs-that-fix-one-pair.md) | Stopwords, stemming, synonyms: `0.000`, `0.000`, `0.523`, then `0.000` again | `production` |

### Section 3 — `03-meaning-as-geometry`: the embedding lane (AG-33)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [The dish you know by taste](parts/03-meaning-as-geometry/3.1-the-dish-you-know-by-taste.md) | What an embedding is, and why the same cosine still works | `foundation` |
| 3.2 | [The model that runs in your own shop](parts/03-meaning-as-geometry/3.2-the-model-that-runs-in-your-own-shop.md) | `POST /api/embed`, 28 lines of stdlib, and `WinError 10061` | `working` |
| 3.3 | [The scale does not know what it weighs](parts/03-meaning-as-geometry/3.3-the-scale-does-not-know-what-it-weighs.md) | One function boundary, two lanes, and the index that must record which | `working` |
| 3.4 | [🅿️ The embedder we park](parts/03-meaning-as-geometry/3.4-the-embedder-we-park.md) | 5,000 rows = 50 requests = 2.5 days of a 20-per-day budget | `production` |

### Section 4 — `04-the-adk-socket`: the retriever behind `BaseMemoryService` (ADK-30)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [Two methods and a list](parts/04-the-adk-socket/4.1-two-methods-and-a-list.md) | What the interface demands, and the score field that does not exist | `working` |
| 4.2 | [The same tool, a new answer](parts/04-the-adk-socket/4.2-same-tool-new-answer.md) | One line changes; `load_memory`, the agent and the instruction do not | `working` |
| 4.3 | [The score has to be written down](parts/04-the-adk-socket/4.3-the-score-has-to-be-written-down.md) | What actually reaches the model, and why it is a Python repr | `working` |
| 4.4 | [The cap that finally means something](parts/04-the-adk-socket/4.4-the-cap-that-finally-means-something.md) | hit@1 of 6/7 against 2/7, from the same `TOP_K = 3` | `production` |

### Section 5 — `05-when-retrieval-lies`: the three failures ranking does not fix (AG-33 · ADK-30)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [💥 Nearest is not near](parts/05-when-retrieval-lies/5.1-nearest-is-not-near.md) | A refund ticket at `0.369` for a SOC 2 question, and a cutoff that cannot help | `production` |
| 5.2 | [💥 The index nobody rebuilt](parts/05-when-retrieval-lies/5.2-the-index-nobody-rebuilt.md) | `reachable: False`, no error, and weights that moved `2.079 → 1.504` | `production` |
| 5.3 | [💥 The question you actually asked](parts/05-when-retrieval-lies/5.3-the-question-you-actually-asked.md) | Five phrasings, five answers, and a greeting that ranks first | `production` |

### Section 6 — `06-in-production`: what we did not build, and what tomorrow moves (AG-33 · ADK-30)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 6.1 | [The store we did not build](parts/06-in-production/6.1-the-store-we-did-not-build.md) | 876.6 ms and 117 MB at 20,000 dense rows — the real threshold | `production` |
| 6.2 | [The seams Day 50 opens](parts/06-in-production/6.2-the-seams-day-50-opens.md) | Which lines tomorrow touches, and the gate that holds them open | `production` |

### The papers — read them **after** the parts

| Paper | What it claims | Level |
| --- | --- | --- |
| [A vector space model for automatic indexing](papers/01-vector-space-model.md) | Documents and queries are points in one term space; similarity is an angle | `production` |
| [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](papers/02-retrieval-augmented-generation.md) | A generator with an editable external memory in front of it | `production` |

`doi:10.1145/361219.361220` (1975) is what section 1 builds by hand, so it is read after building it.
`arXiv:2005.11401` (2020) is what section 4 wires into the agent. Principle 4 at the scale of a day:
hand-roll the mechanism, watch it fail, *then* read the proposal.

**Read the sections in order.** Section 2's zero is meaningless without section 1's index, and
section 4's swap is meaningless without section 3's seam.

---

## §3 Setup — run this

**No Python package is added today, and none is upgraded.** `google-adk` stays at `2.7.1`,
`google-genai` at `2.19.0`. `git diff pyproject.toml uv.lock` must be empty when you finish.
`numpy`, `scipy` and `scikit-learn` are **not** installed and must not be — every line of arithmetic
in this day is `math.sqrt` over dictionaries, and adding a dependency to avoid ten lines is an
anti-pattern this project names.

```bash
# 1 - the day's lab
cd days/day-49-retrieval-and-embeddings
mkdir -p lab lab/papers/vector-space-model lab/papers/retrieval-augmented-generation

# 2 - the two shared helpers every script imports
touch lab/_archive.py lab/_script.py

# 3 - section 1: building the index by hand
touch lab/counts.py lab/angle.py lab/weights.py lab/index.py

# 4 - section 2: the meaning test
touch lab/meaning.py lab/patches.py

# 5 - section 3: the embedding lane
touch lab/space.py lab/embed.py lab/lanes.py lab/priced.py

# 6 - section 4: the ADK socket
touch lab/surface.py lab/service.py lab/wired.py lab/entrytext.py lab/capped.py

# 7 - section 5: the failure lab
touch lab/nearest.py lab/stale.py lab/words.py

# 8 - section 6 and the gate
touch lab/stores.py lab/gate.py

# 9 - the two paper demos
touch lab/papers/vector-space-model/corpus.py lab/papers/vector-space-model/vsm.py
touch lab/papers/retrieval-augmented-generation/parametric.py
touch lab/papers/retrieval-augmented-generation/rag.py
cd -

# 10 - the project module you are about to fill (you type every line)
touch sutra/retrieval.py

# 11 - the index file is DERIVED, so it must never be committed
grep -n "archive_index" .gitignore || echo "not ignored yet - see the build brief"

# 12 - the local embedder (optional today; the day runs without it)
ollama --version
ollama pull nomic-embed-text
ollama list
```

**Steps 10, 11 and 12 are the three that matter.**

`sutra/retrieval.py` is a **new module created today**, beside `sutra/memory/` rather than inside it:
memory is *what the desk kept* and retrieval is *how it is found*, and Day 50 extends this file
directly.

Step 11 is [Day 0](../day-00-toolchain-skeleton-driver/LESSON.md)'s discipline applied to a new kind
of file. `.gitignore` today covers `*.db` and `*.sqlite3`; the index is **JSON**, so it is **not**
covered, and the build brief asks you to add the line before the file exists. Day 48's
[4.4](../day-48-memory-design/parts/04-privacy-and-erasure/4.4-the-store-that-must-not-be-committed.md)
is the part that explains why `git check-ignore` is the right question to ask.

Step 12 is optional. **This day was written on a machine with no Ollama**, and every transcript in it
was produced without one — including the connection error in
[3.2](parts/03-meaning-as-geometry/3.2-the-model-that-runs-in-your-own-shop.md). Two blocks in the
day are marked `TODO(me)` and are yours to produce once the daemon is running.

---

## §4 Build brief

### The project code — `sutra/retrieval.py`, and you type every line

One module. The table below is the contract
[6.2](parts/06-in-production/6.2-the-seams-day-50-opens.md) explains and `lab/gate.py` enforces.

| Symbol | Shape | What it must do |
| --- | --- | --- |
| `tokenize` | `(str) -> list[str]` | Split on `\w+`, lowercase — **the same tokenizer ADK's memory service uses** (1.2) |
| `counts` | `(str) -> dict[str, float]` | A sparse term-count vector (1.2) |
| `cosine` | `(dict, dict) -> float` | Direction, not size; guard the empty vector (1.3) |
| `idf`, `tfidf` | over the collection | Weight by rarity; a word in every row weighs `0.0` (1.4) |
| `embed` | `(list[str]) -> list[list[float]]` | The local model, batched, with `429` handled (3.2) |
| `tfidf_vectoriser`, `embedding_vectoriser` | builders returning a `Vectorise` | The seam; the lane is the caller's decision (3.3) |
| `build_index` | `(rows, *, vectorise) -> dict` | Vectorise **pre-cut** rows. **It never splits anything** (1.5, 6.2) |
| `search` | `(query, index, *, k, floor) -> list` | Sort, **then** cut, then apply the floor (1.5, 5.1) |
| `TOP_K` | `int` | The cap, with the evidence in the comment (4.4) |
| `SIMILARITY_FLOOR` | `float` | Below this, *nothing found* — the honest miss (5.1) |
| `SutraRetrievalMemoryService` | `BaseMemoryService` subclass | A thin adapter: translate in, translate out, no scoring logic (4.1, 4.2) |
| `build_memory_service` | `() -> BaseMemoryService` | The one place construction happens; **no arguments** (4.2) |

- **The service filters by `(app_name, user_id)` before it ranks.** The lab's version deletes both
  arguments and says so; the real one must not. Day 46's
  [5.3](../day-46-sessions-vs-memory/parts/05-failure-lab/5.3-another-customers-memory.md) is what
  skipping this costs.
- **The score is written into the entry text**, and also into `custom_metadata` for programs
  ([4.3](parts/04-the-adk-socket/4.3-the-score-has-to-be-written-down.md)).
- **The index file is derived and gitignored.** Add the line to `.gitignore` **before** the file
  exists, then prove it with `git check-ignore -v <path>`.
- `lab/gate.py` checks six of these structurally and behaviourally, and is **red as shipped**.

**`TODO(me)` markers left for you:**

- **1.5, 5.2** — decide **where the index file lives and when it is rebuilt**. Write down what
  triggers a rebuild, and add `built_at` and a source row count to the file so staleness is
  measurable rather than invisible.
- **3.2** — run `uv run python days/day-49-retrieval-and-embeddings/lab/embed.py` on a machine with
  Ollama and **record the dimension it prints** plus the digest from `ollama list` in
  `docs/PACKAGES.md`. The model page does not state the dimension; your run does.
- **3.3** — run `uv run python lanes.py --embeddings` and paste the output. Then say whether 4188
  climbed, and whether **any** score came back as exactly `0.000`.
- **3.3, 5.2** — decide what the index file records about the lane that built it: vectoriser name,
  model name, tag, dimension. Then write the check that refuses to search when they do not match.
- **3.4** — open `https://ai.google.dev/gemini-api/docs/rate-limits`, find the free-tier embedding
  limit, and add the row to `docs/PACKAGES.md`. Until then the only defensible number is the twenty
  per day this project measured.
- **4.2** — write the **desk instruction** that tells the model past cases exist, what a good query
  looks like for this archive, and that a weak match is not evidence. ADK's appended paragraph is
  generic (5.3 quotes it in full).
- **4.4, 5.1** — choose `TOP_K` and `SIMILARITY_FLOOR`, and write in the comment beside each what you
  sized it against. Then decide what the desk **says** when everything is below the floor — the exact
  sentence, not "return nothing".
- **5.1** — decide the two signals the desk emits about every search: the top score, and the gap
  between the first and second result. Then decide the threshold at which the gap is an alert.
- **5.3** — log the query on every search, then add five queries from your own runs to the judgement
  set in `lab/capped.py`, including one that is only a greeting.
- **6.1** — decide the archive size at which you would move to a real store, and name which one.
  Write the date and the measurement behind the decision.
- **6.2** — promote `lab/gate.py`'s six rules into `tests/test_retrieval.py`, one test function each,
  named as sentences, with a comment naming the ADK version they were observed against.

### The lab — twenty-two scripts, all of which run, none of which call a model

| File | What it does | Taught in |
| --- | --- | --- |
| `lab/_archive.py` | eight closed tickets, one incoming ticket, and the five arithmetic functions | all |
| `lab/_script.py` | `ScriptedModel`, a `BaseLlm` that reads from a script instead of a provider | 4.2, 4.3 |
| `lab/counts.py` | one ticket, its tokens, its vector, and its 67 zeros | 1.2 |
| `lab/angle.py` | two complaints and two tickets, scored by cosine and by dot product | 1.3 |
| `lab/weights.py` | the idf table, and the three words that weigh exactly zero | 1.4 |
| `lab/index.py` | build the file, read it back, rank a query; weighted and not | 1.5 |
| `lab/meaning.py` | the whole archive scored against ticket 4521 | 2.1 |
| `lab/patches.py` | stopwords, stemming and synonyms, applied cumulatively | 2.2 |
| `lab/space.py` | hand-placed vectors, to show the shape a good embedding would have | 3.1 |
| `lab/embed.py` | the Ollama client: one POST, `429` handled, no invented vector | 3.2 |
| `lab/lanes.py` | the same ranking code over two vectorisers | 3.3 |
| `lab/priced.py` | what the hosted embedder would cost, in requests | 3.4 |
| `lab/surface.py` | what `BaseMemoryService` demands, read off the installed class | 4.1 |
| `lab/service.py` | the subclass, and the same query against ADK's shipped service | 4.2 |
| `lab/wired.py` | a `Runner`, `load_memory`, and one line swapped | 4.2 |
| `lab/entrytext.py` | what the model is actually sent when the tool returns | 4.3 |
| `lab/capped.py` | seven questions, hit@1 and hit@3, both services | 4.4 |
| `lab/nearest.py` | three questions the archive cannot answer, and a cutoff | 5.1 |
| `lab/stale.py` | a ticket closed after the index was built | 5.2 |
| `lab/words.py` | five phrasings of one question | 5.3 |
| `lab/stores.py` | scan time and memory at 8, 1,000 and 20,000 rows, sparse and dense | 6.1 |
| `lab/gate.py` | six rules about `sutra/retrieval.py`, as an exit code | 6.2, §5 |

`lab/papers/vector-space-model/` and `lab/papers/retrieval-augmented-generation/` hold the two paper
demos and are **given complete** in the paper parts. They are teaching material, not reps: type them,
run both arms of each, and compare your output with the transcripts.

---

## §5 The eval that must be able to fail

Four checks and eleven ablations, all on zero model calls.

**The gate** is the day's definition of done, and it is red until you have written the module:

```bash
uv run python days/day-49-retrieval-and-embeddings/lab/gate.py; echo "exit: $?"
```

Measured on 2026-09-05, before anything was written: `rule 1-6: sutra.retrieval is not importable: No
module named 'sutra.retrieval'`, `findings: 1`, `exit: 1`. When it prints `findings: 0` and `exit: 0`,
six statements are true — the four public names exist, `cosine` is a cosine, `TOP_K` is a named
integer, `SIMILARITY_FLOOR` is a named float, the service is a real `BaseMemoryService` with the right
signature, and **what comes back is sorted best first with a score on every entry**. Then break
exactly one on purpose — replace `TOP_K` with the literal `3` at its use site — and watch rule 3
appear.

**The day's thesis, as an ablation**, and both arms must be run:

```bash
cd days/day-49-retrieval-and-embeddings/lab
uv run python meaning.py
uv run python meaning.py --counts
cd -
```

The same archive, the same incoming ticket, weighted and unweighted. `4188 scored 0.000 and ranked 5
of 8`, with a caching ticket first at `0.270`. That is the day in two runs.

**The measurement that closes Day 46:**

```bash
cd days/day-49-retrieval-and-embeddings/lab
uv run python capped.py
uv run python capped.py --keyword
cd -
```

`right answer first: 6/7` against `2/7`; `right answer in the top 3: 7/7` against `4/7`. Same cap,
same archive, same seven questions.

**The two paper ablations**, both arms of each:

```bash
cd days/day-49-retrieval-and-embeddings/lab/papers/vector-space-model
uv run python vsm.py
uv run python vsm.py --no-idf
cd ../retrieval-augmented-generation
uv run python rag.py
uv run python rag.py --no-retrieval
cd -
```

Weighted, one card scores above the `0.2` cutoff and it is the right one; unweighted, four do and
three are wrong. With retrieval, `4/4` answers cite a ticket; without, `0/4`, and one of the four is a
confident policy statement the archive contradicts.

**And the rest, each of which has a named break in its own part:**

```bash
cd days/day-49-retrieval-and-embeddings/lab
uv run python counts.py
uv run python angle.py; uv run python angle.py --dot
uv run python weights.py
uv run python index.py; uv run python index.py --counts
uv run python patches.py
uv run python space.py
uv run python embed.py
uv run python lanes.py; uv run python lanes.py --embeddings
uv run python priced.py
uv run python surface.py
uv run python service.py; uv run python service.py --keyword
uv run python wired.py; uv run python wired.py --keyword; uv run python wired.py --incoming
uv run python entrytext.py
uv run python nearest.py; uv run python nearest.py --threshold
uv run python stale.py; uv run python stale.py --rebuild
uv run python words.py
uv run python stores.py
cd -
```

`embed.py` and `lanes.py --embeddings` **fail on purpose** on a machine without Ollama, with
`urllib.error.URLError: <urlopen error [WinError 10061] No connection could be made because the target
machine actively refused it>`. That is the finding, not a broken lab: the embedding lane raises rather
than silently falling back.

---

## §6 Request budget

**Free-tier Gemini**, 20 generate requests per day per model (`gemini-3.7-flash`, quota read off a
live 429 on Day 2 and recorded in `docs/PACKAGES.md`).

| What | Generations |
| --- | --- |
| every part in every section | **0** |
| all twenty-two lab scripts, every flag | **0** |
| both paper demos, both arms of each | **0** |
| `sutra/retrieval.py`, the gate and the six rules | **0** |
| **Total planned** | **0 of 20** |

**Zero, and today it is the argument rather than the economy.**
[3.4](parts/03-meaning-as-geometry/3.4-the-embedder-we-park.md) is the part that explains why: this
is the first mechanism in the curriculum whose cost scales with the size of *your data* rather than
with how many questions you ask, and a five-thousand-row archive through the hosted embedder is fifty
batched requests — two and a half days of the whole budget for one rebuild. The local embedder is
zero requests at any archive size, which is why the plan chose it.

**Ollama requests: local only**, to `http://localhost:11434`. No rate limit, no key, no network.
**Gemini embedding API requests: 0** — named, priced and 🅿️ parked in
[3.4](parts/03-meaning-as-geometry/3.4-the-embedder-we-park.md).

Every model call path in `lab/embed.py` handles HTTP `429` with `retry-after` and backoff even though
a local daemon will never send one, because the same function is the one you would point at a hosted
endpoint.

**Cost: $0.**

---

## §7 Traps

- **A cosine over two documents that share no words is `0.000`, not "low".** The dot product runs over
  the intersection and the intersection is empty. No threshold, no larger `k` and no better ranking
  recovers it (2.1).
- **Weighting makes a stopword list redundant, and a stopword list makes weighting look useful.**
  `the`, `fix` and `kb` all weigh exactly `0.0` in this archive, and removing them changed the failing
  score by nothing at all (1.4, 2.2).
- **A rank of 1 at a score of `0.000` is a tie broken by ticket id.** Seven of eight tied, and the
  report said rank 1. Always print the tie count or the score (2.2, 5.3).
- **The dot product ranks by how much somebody typed.** A long complaint's *wrong* match scored
  `11.000` against a short complaint's *right* match at `3.000` (1.3).
- **`idf` weights belong to the collection, not the document.** Adding one ticket moved `app` from
  `2.079` to `1.504` and invalidated every stored vector containing it (1.4, 5.2).
- **Small archives make idf noisy and the noise looks like signal.** One query ranked the right ticket
  second, and its entire score came from the preposition `on` (1.4, 4.4).
- **The tokenizer splits on hyphens.** `KB-104` is `kb` + `104`, and `sign-in` is `sign` + `in`. Both
  sides of the comparison must use the same function (1.2).
- **`/api/embeddings` is the retired Ollama endpoint** and takes `prompt` rather than `input`. The
  current one is **`/api/embed`**, and `https://docs.ollama.com/api/embeddings` returns HTTP 404
  (3.2).
- **`WinError 10061` — *actively refused* — is not a timeout.** Something answered instantly and said
  no, so the address is right and the daemon is absent (3.2).
- **Searching a sparse index with a dense query does not error.** The key intersection is empty and
  every document ties at `0.000`, which looks exactly like an archive with nothing relevant in it
  (3.3).
- **`search_memory`'s arguments are keyword-only and the method is `async`.** A synchronous override
  raises `TypeError: object SearchMemoryResponse can't be used in 'await' expression`, which names the
  return value rather than the method (4.1).
- **`SearchMemoryResponse` has one field and `MemoryEntry` has no score.** The similarity has to be
  written into the text; there is no box for it (4.1, 4.3).
- **What reaches the model is `{'result': LoadMemoryResponse(...)}` — a Python repr**, complete with
  `id=None` and `timestamp=None` on every entry, re-sent on every later turn. The tool's own docstring
  says it *"only uses text part from the memory"* (4.3).
- **Cut after you sort, never before.** Reversing those two lines produces three arbitrary results
  with scores attached, which is worse than Day 46's version (4.2, 4.4).
- **`memory_service=` belongs on `Runner`, not on `Agent`** — `ValueError: Memory service is not
  available.` (Day 46, 3.1).
- **Top-k always returns k.** A question about a subject the archive has never contained returned a
  refund ticket at `0.369`, higher than the second-best result on a question it answers perfectly
  (5.1).
- **A similarity threshold cannot separate right from nearest.** In one run a wrong answer scored
  `0.369` and a right answer scored `0.100`. Use the **gap** between first and second as well as the
  level (5.1).
- **A stale index is worse than a missing one.** Missing raises `FileNotFoundError` and gets fixed
  within the hour; stale returns confident answers from last quarter, and the staleness window sits
  over exactly the newest documents, which are the ones people ask about (1.5, 5.2).
- **The model writes the query.** Five phrasings of one question gave five different answers, and a
  bare greeting ranked the right ticket first at a score of `0.000` (5.3).
- **876 ms of blocking CPU inside an `async` method stops the whole event loop.** Twenty thousand
  dense rows in pure Python is nearly a second per search and 117 MB resident (6.1).

---

## §8 Verify before you code

Fetched or read on **2026-09-05**, the day this was written.

**The ADK documentation:**

- `https://adk.dev/sessions/memory/` — fetched and read. It calls `BaseMemoryService` *"the interface
  for managing this searchable, long-term knowledge store"*; `search_memory` *"lets an agent (typically
  via a `Tool`) query the knowledge store and retrieve relevant snippets or context based on a search
  query"*; `add_session_to_memory` *"takes a completed `Session` and adds relevant information to the
  long-term knowledge store"*; `InMemoryMemoryService` *"performs basic keyword matching for
  searches"*; and `VertexAiRagMemoryService` *"stores conversations in Knowledge Engine and retrieves
  them by vector similarity"*. It does **not** discuss writing a custom memory service, so everything
  in section 4 came from the installed source.
- `https://adk.dev/docs/sessions/memory/` returned **HTTP 404**. The live paths carry no `/docs`
  segment, as Days 33, 40, 44 and 46 all found.

**The Ollama documentation:**

- `https://ollama.com/search?q=embed` — fetched. `nomic-embed-text` is listed, alongside
  `embeddinggemma` (300M), `qwen3-embedding` (0.6B/4B/8B), `mxbai-embed-large` (335M), `all-minilm`
  (22M/33M), `snowflake-arctic-embed`, `snowflake-arctic-embed2` (568M), `granite-embedding` and
  `bge-large` (335M).
- `https://ollama.com/library/nomic-embed-text` — fetched. Tags `latest`, `v1.5` and
  `137m-v1.5-fp16`; **"2K context window"**; pull command `ollama pull nomic-embed-text`. **The
  embedding dimension is not stated on the page**, so this day does not claim one — 3.2 leaves it as a
  `TODO(verify: ...)` to be read off the learner's own run.
- `https://docs.ollama.com/capabilities/embeddings` — fetched. Documents `/api/embed` with the request
  body `{"model": ..., "input": ...}` and an `embeddings` field in the response, and states that *"The
  `/api/embed` endpoint returns L2-normalized (unit-length) vectors."*
- `https://docs.ollama.com/api/embeddings` returned **HTTP 404**.

**The Gemini embedding documentation:**

- `https://ai.google.dev/gemini-api/docs/embeddings` — fetched. Current models are
  **`gemini-embedding-2`** (latest, multimodal, 8,192 token limit) and **`gemini-embedding-001`**
  (text only, 2,048). The call is
  `client.models.embed_content(model="gemini-embedding-2", contents=...)` on the `google-genai` client
  this project already pins. **Free-tier limits for embeddings are not on the page**; it links to a
  separate rate-limits page, which is 3.4's `TODO(verify: ...)`.

**The installed ADK — the authoritative surface, read rather than guessed** (`google-adk==2.7.1`):

- `.venv/Lib/site-packages/google/adk/memory/base_memory_service.py` — two `@abstractmethod`s,
  `add_session_to_memory(session)` and `search_memory(*, app_name, user_id, query)`, both `async` and
  the second keyword-only; two concrete methods whose bodies `raise NotImplementedError`; and
  `SearchMemoryResponse` with the single field `memories: list[MemoryEntry]` (4.1).
- `.venv/Lib/site-packages/google/adk/memory/memory_entry.py` — `MemoryEntry` declares exactly
  `content`, `custom_metadata`, `id`, `author`, `timestamp`. **No score, no rank, no distance** (4.1,
  4.3).
- `.venv/Lib/site-packages/google/adk/memory/in_memory_memory_service.py` — re-verified against Day
  46's reading: matching is `any(query_word in words_in_event for query_word in words_in_query)` over
  `set(word.lower() for word in re.findall(r'\w+', text, re.UNICODE))`, and results are appended in
  iteration order with **no sort anywhere in the file** (1.2, 4.2, 4.4).
- `.venv/Lib/site-packages/google/adk/tools/load_memory_tool.py` — the four-line `load_memory` body,
  the `LoadMemoryResponse` type, the docstring note *"NOTE: Currently this tool only uses text part
  from the memory."*, and the generic paragraph appended to the system instruction, quoted in full in
  5.3 (4.2, 4.3, 5.3).

**Four live commands, re-run today:**

```bash
python -c "import google.adk; print(google.adk.__version__)"
python -c "import google.adk.memory as m; print(m.__all__)"
python -c "from google.adk.memory import BaseMemoryService as B; print(sorted(B.__abstractmethods__))"
python -c "import numpy" ; echo "expect ModuleNotFoundError - this day adds no package"
```

---

## §9 Say it in an interview

*"Day 46 gave the desk a memory and left me with a finding I could not fix: the search returned an
unranked list, so capping it at three picked three arbitrary rows. A cap is a cost control, not a
precision control. Day 49 was the correctness fix, and I built the retriever by hand before reaching
for anything — term counts, tf-idf weighting, cosine similarity, an index written to a file. About
sixty lines of standard library, no numpy.*

*It worked on the query I wrote for it and then it failed the test that matters. A ticket came in
saying 'auth redirect bug, the user lands at a blank sign-in screen', and the archive contained the
same fault from eighteen months earlier described as 'login loop, session cookie without SameSite'.
The only word the two share is 'the', and 'the' is in all eight tickets so its idf is exactly zero. The
cosine came back as 0.000 and the system ranked a caching bug first at 0.270, because that ticket
happened to share the word 'blank'. That zero is the whole argument for embeddings and I would rather
quote it than assert it.*

*Before switching I tried the three repairs everybody tries, because the argument is only convincing
if the alternative gets a fair run. Stopwords moved the score by nothing — proper weighting had already
zeroed those words. Stemming did nothing, because 'auth' and 'login' are not two forms of one word.
Six hand-written synonym entries took it from 0.000 to 0.523 and rank one, which is better than a
general model would have done on that pair. Then I wrote two more sentences describing the same bug
and both went back to 0.000, and one of them returned a completely unrelated ticket at 0.302. A
synonym map can only fix the phrasings somebody already thought of.*

*The ADK half is that I put the retriever behind `BaseMemoryService` rather than calling it from the
agent. Two abstract methods, and a response object with a single list of entries — no score field, no
rank, no distance — so a ranked retriever has to write its own score into the entry text. I checked
what actually reaches the model and it is a Python repr of the pydantic response, with `id=None` and
`timestamp=None` on every result, re-sent on every later turn, and the tool's own docstring says it
only uses the text part. The payoff is that the agent, the instruction and the `load_memory` tool did
not change at all; one line changed, the object passed to the runner. On seven queries with known
answers, hit@1 went from 2 out of 7 to 6 out of 7 and hit@3 from 4 out of 7 to 7 out of 7 — the same
cap of three, applied to a sorted list instead of an unsorted one. The detail I liked is that on an
easy query both services returned the identical three tickets in the identical order, which is why
nobody notices the difference in testing.*

*What I would not claim is that this made retrieval good. Three failures survive everything I built.
Top-k always returns k, so a question about SOC 2 compliance — which that archive has never contained
— came back with a refund ticket at 0.369, higher than the second-best result on a question the archive
answers perfectly, and a threshold cannot separate those because a wrong answer scored 0.369 and a
right one scored 0.100. A ticket closed after the index was written is unreachable with no error at
all, and adding it also moved the idf weight of a word from 2.079 to 1.504, which quietly invalidates
every stored vector containing it. And the query is written by the model: I asked for the same ticket
five ways and got five answers, including a bare greeting that ranked the right ticket first at a
score of zero.*

*On the choice of embedder: I costed it rather than guessing. Indexing scales with the size of your
data, not with traffic, so a five-thousand-row archive batched a hundred at a time is fifty requests
against a free tier of about twenty a day — two and a half days of the entire budget for one rebuild,
on the same key the agent uses. Local was zero requests at any size and keeps the ticket archive on
the machine. And I measured where the hand-rolled version stops being reasonable: a sparse scan over
twenty thousand rows is 64 milliseconds, which is fine, but the same rows as dense 768-dimension
vectors is 876 milliseconds and 117 MB, inside an async method on the event loop. Adopting embeddings
moves you an order of magnitude closer to needing a real vector store, and that belongs in the decision
next to the quality gain."*

---

## §10 Done when

See [`CHECKLIST.md`](CHECKLIST.md). Every box is ticked because you ran the thing, not because you
read about it. `./m done 49` refuses to commit until they are.

---

## §11 Ledger & commit

**`docs/PROGRESS.md` — append this row** (fill in the hash after committing):

```markdown
| 49 | 2026-09-05 | AG-33, ADK-30 | 20 (+2 papers) | <hash> | ⚠️ |
```

**`docs/PACKAGES.md` — one row, and it is a model pin rather than a package.** No Python package is
added and no pin is moved; `google-adk` stays at `2.7.1` and `google-genai` at `2.19.0`. Addendum 02
requires the model and the date, so:

```markdown
| nomic-embed-text (ollama model) | tags `latest`, `v1.5`, `137m-v1.5-fp16`; TODO(`ollama list` — record the digest and TODO(`uv run python days/day-49-retrieval-and-embeddings/lab/embed.py` — record the dimension)) | 2026-09-05 | 49 | Local embedding model for the archive index. Verified present on `https://ollama.com/search?q=embed` and `https://ollama.com/library/nomic-embed-text` on 2026-09-05; that page states a **2K context window** and gives `ollama pull nomic-embed-text`, and does **not** state the vector dimension. Endpoint `POST http://localhost:11434/api/embed`, verified against `https://docs.ollama.com/capabilities/embeddings` on 2026-09-05, which also states the endpoint *"returns L2-normalized (unit-length) vectors"*; `https://docs.ollama.com/api/embeddings` returns HTTP 404. Chosen over the Gemini embedding API because index cost scales with corpus size: 5,000 rows batched by 100 is 50 requests against a free tier of ~20/day (part 3.4). **$0, no rate limit, offline.** Not installed on the writing machine — two transcripts in the day are `TODO(me)`. |
| gemini-embedding-2 / gemini-embedding-001 (NOT adopted) | n/a — documented alternative | 2026-09-05 | 49 | Current Gemini embedding models per `https://ai.google.dev/gemini-api/docs/embeddings`, fetched 2026-09-05: `gemini-embedding-2` (multimodal, 8,192 token limit) and `gemini-embedding-001` (text only, 2,048). Called with `client.models.embed_content(...)` on the already-pinned `google-genai==2.19.0`, so no package would be added. 🅿️ **Parked**: free-tier embedding limits are not published on the docs page — TODO(open `https://ai.google.dev/gemini-api/docs/rate-limits` and record the free-tier embedding RPM/RPD) — and against the measured 20/day generate budget one index rebuild would consume the whole day's quota on the same key the agent uses. Reconsider when there is a billing account or a separate key. |
```

**`docs/PAPERS.md` — no new rows today.** *A vector space model for automatic indexing*
(`doi:10.1145/361219.361220`, 1975) and *Retrieval-Augmented Generation for Knowledge-Intensive NLP
Tasks* (`arXiv:2005.11401`, 2020) were verified on 2026-09-05 and their rows already exist, naming
this day and `days/day-49-retrieval-and-embeddings/papers/01-vector-space-model.md` and
`.../papers/02-retrieval-augmented-generation.md`. *Efficient Estimation of Word Representations in
Vector Space* (`arXiv:1301.3781`, 2013) is named in prose in `papers/01-vector-space-model.md` and is
not taught; its row already records that.

**`docs/SKILL_PROVENANCE.md` — no new rows today.**

**Git commit message:**

```
day 49: retrieval & embeddings — one honest RAG day — closes AG-33, ADK-30
```
