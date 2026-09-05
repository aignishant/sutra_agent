# Day 49 - Retrieval & embeddings — one honest RAG day

IDs closed: AG-33, ADK-30 · source: `days/day-49-retrieval-and-embeddings/`

## Parts

### 1.1 - The counter that takes a description
`days/day-49-retrieval-and-embeddings/parts/01-text-as-numbers/1.1-the-counter-that-takes-a-description.md` · level `foundation` · ids AG-33

Retrieval is finding things by describing them instead of naming them, and the only way a computer can do that is to turn every description into numbers and then measure how far apart the numbers are.

### 1.2 - A ticket as a list of numbers
`days/day-49-retrieval-and-embeddings/parts/01-text-as-numbers/1.2-a-ticket-as-a-list-of-numbers.md` · level `foundation` · ids AG-33

Counting how often each word appears turns any piece of text into a list of numbers over a fixed list of words, and that list is already a vector — no model, no training, no library.

### 1.3 - Direction, not size
`days/day-49-retrieval-and-embeddings/parts/01-text-as-numbers/1.3-direction-not-size.md` · level `foundation` · ids AG-33

Score two documents by the angle between their vectors rather than by how big the overlap is, or the longest complaint wins every time regardless of what it is about.

### 1.4 - The word that tells you nothing
`days/day-49-retrieval-and-embeddings/parts/01-text-as-numbers/1.4-the-word-that-tells-you-nothing.md` · level `working` · ids AG-33

A word that appears in every document cannot tell any two of them apart, so weight each word by how rare it is and the common words fall out of the score by themselves — no hand-written stopword list required.

### 1.5 - The work you do once
`days/day-49-retrieval-and-embeddings/parts/01-text-as-numbers/1.5-the-work-you-do-once.md` · level `working` · ids AG-33

An index is the vectors computed once, ahead of time, and written to a file, so that answering a question is arithmetic over numbers you already have instead of re-reading every document.

### 2.1 - 💥 The score that came back zero
`days/day-49-retrieval-and-embeddings/parts/02-the-meaning-test/2.1-the-score-that-came-back-zero.md` · level `production` · ids AG-33

Ticket 4521 and ticket 4188 are the same fault, and the index you just built scores them at 0.000 — not low, not weak, exactly zero — while it puts a ticket about a stale browser cache at the top with 0.270.

### 2.2 - The repairs that fix one pair
`days/day-49-retrieval-and-embeddings/parts/02-the-meaning-test/2.2-the-repairs-that-fix-one-pair.md` · level `production` · ids AG-33

Stopword lists, stemming and a hand-written synonym map are the three repairs everybody tries after [2.1](2.1-the-score-that-came-back-zero.md); the first two move the score by exactly nothing, the third takes it to 0.523 and rank 1, and the very next sentence a support agent types is back to 0.000.

### 3.1 - The dish you know by taste
`days/day-49-retrieval-and-embeddings/parts/03-meaning-as-geometry/3.1-the-dish-you-know-by-taste.md` · level `foundation` · ids AG-33

An embedding is a list of numbers produced by a model that was trained to put texts used in similar ways close together, so two sentences with no shared words can still have a high cosine — which is the one thing counting words can never do.

### 3.2 - The model that runs in your own shop
`days/day-49-retrieval-and-embeddings/parts/03-meaning-as-geometry/3.2-the-model-that-runs-in-your-own-shop.md` · level `working` · ids AG-33

POST http://localhost:11434/api/embed with a model name and a list of texts returns one vector per text, at zero quota and zero cost, from a model running on your own machine — twenty-eight lines of standard-library Python and no new package.

### 3.3 - The scale does not know what it weighs
`days/day-49-retrieval-and-embeddings/parts/03-meaning-as-geometry/3.3-the-scale-does-not-know-what-it-weighs.md` · level `working` · ids AG-33

Put the vectoriser behind one function that takes a list of texts and returns a list of vectors, and the ranking, the cap and the memory service never learn which lane produced the numbers — which is why swapping tf-idf for an embedding model is one line and not a rewrite.

### 3.4 - 🅿️ The embedder we park
`days/day-49-retrieval-and-embeddings/parts/03-meaning-as-geometry/3.4-the-embedder-we-park.md` · level `production` · ids AG-33

The Gemini embedding API exists, works, and is probably better than the local model — and indexing a five-thousand-row archive through it costs fifty batched requests against a free tier of about twenty a day, so Sutra names it, prices it, and spends zero requests on it today.

### 4.1 - Two methods and a list
`days/day-49-retrieval-and-embeddings/parts/04-the-adk-socket/4.1-two-methods-and-a-list.md` · level `working` · ids ADK-30

BaseMemoryService demands exactly two methods and gives you back a response object with one field — a plain list of MemoryEntry with no score, no rank and no distance anywhere — so a retrieval-backed implementation has to carry its own scores in a shape ADK does not provide.

### 4.2 - The same tool, a new answer
`days/day-49-retrieval-and-embeddings/parts/04-the-adk-socket/4.2-same-tool-new-answer.md` · level `working` · ids ADK-30

Subclass BaseMemoryService, rank inside search_memory, pass the object to Runner(memory_service=...), and Day 46's load_memory tool — the same agent, the same instruction, not one line changed — starts returning three scored results instead of eight unranked ones.

### 4.3 - The score has to be written down
`days/day-49-retrieval-and-embeddings/parts/04-the-adk-socket/4.3-the-score-has-to-be-written-down.md` · level `working` · ids ADK-30

MemoryEntry has no score field, so the similarity has to be written into the text — and the reason the text and not custom_metadata is that what reaches the model is {'result': LoadMemoryResponse(...)}, the Python repr of a pydantic object, complete with id=None and timestamp=None.

### 4.4 - The cap that finally means something
`days/day-49-retrieval-and-embeddings/parts/04-the-adk-socket/4.4-the-cap-that-finally-means-something.md` · level `production` · ids ADK-30

The same TOP_K = 3 that Day 46 called a cost control and not a precision control puts the right answer first 6 times out of 7 over a ranked list and 2 times out of 7 over an unranked one — the cap did not change, the thing underneath it did.

### 5.1 - 💥 Nearest is not near
`days/day-49-retrieval-and-embeddings/parts/05-when-retrieval-lies/5.1-nearest-is-not-near.md` · level `production` · ids AG-33

Asked about SOC 2 evidence — a subject the archive has never covered once — the retriever returned a refund ticket at 0.369, higher than any score it gave the question it could genuinely answer's second and third results, and a 0.20 cutoff did not remove it.

### 5.2 - 💥 The index nobody rebuilt
`days/day-49-retrieval-and-embeddings/parts/05-when-retrieval-lies/5.2-the-index-nobody-rebuilt.md` · level `production` · ids AG-33

A ticket closed after the index was written is unreachable — is 4602 reachable at all? False — with no error, no warning and no empty result, and adding that one row also moved the weight of app from 2.079 to 1.504, which changes the score of every other row in the archive.

### 5.3 - 💥 The question you actually asked
`days/day-49-retrieval-and-embeddings/parts/05-when-retrieval-lies/5.3-the-question-you-actually-asked.md` · level `production` · ids ADK-30

Five ways of asking for the same ticket give five different results — 0.456, 0.372 and three 0.000s — and under load_memory the wording is chosen by the model, not by you, so the retrieval quality you measured is not the retrieval quality you ship.

### 6.1 - The store we did not build
`days/day-49-retrieval-and-embeddings/parts/06-in-production/6.1-the-store-we-did-not-build.md` · level `production` · ids AG-33

A linear scan is 0.1 ms at eight rows and 876.6 ms at twenty thousand dense vectors, holding 117 MB in memory — which is where a hand-written index stops being an engineering choice and a real vector store starts being one.

### 6.2 - The seams Day 50 opens
`days/day-49-retrieval-and-embeddings/parts/06-in-production/6.2-the-seams-day-50-opens.md` · level `production` · ids ADK-30

sutra/retrieval.py is written so that tomorrow's changes — chunking, and choosing TOP_K and SIMILARITY_FLOOR from evidence — touch what produces the rows and two constants, and nothing else; the gate in lab/gate.py is what holds those seams open.

## Papers - read after the parts

### doi:10.1145/361219.361220 - A vector space model for automatic indexing
`days/day-49-retrieval-and-embeddings/papers/01-vector-space-model.md`

Represent every document and every query as a vector over the same set of terms, and retrieval stops being a test of whether words match and becomes a measurement of how far apart two things are — which is what makes ranking, partial matches and a cutoff possible at all.

### arXiv:2005.11401 - Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks
`days/day-49-retrieval-and-embeddings/papers/02-retrieval-augmented-generation.md`

Put a retriever in front of a generator, so that the model answers from documents fetched at question time rather than only from what was frozen into its weights — which makes the knowledge replaceable, inspectable and citable without retraining anything.

