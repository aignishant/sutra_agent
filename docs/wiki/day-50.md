# Day 50 - Chunking, top-k & when RAG is the wrong tool

IDs closed: AG-14 · source: `days/day-50-chunking-and-top-k/`

## Parts

### 1.1 - The unit you store is the unit you find
`days/day-50-chunking-and-top-k/parts/01-the-unit-you-index/1.1-the-unit-you-store-is-the-unit-you-find.md` · level `foundation` · ids AG-14

Retrieval can only ever hand back the pieces you decided to store, so the size of a stored piece — its chunk — is chosen before anybody asks a question, and no amount of clever ranking afterwards can hand back half of one.

### 1.2 - The document that averages itself away
`days/day-50-chunking-and-top-k/parts/01-the-unit-you-index/1.2-the-document-that-averages-itself-away.md` · level `working` · ids AG-14

One vector is one average, so a long document scores against a question with the meaning of its whole self and not with the meaning of its best paragraph — measured here, the incident review scores 0.235 where its own answer-bearing paragraph scores 0.465.

### 1.3 - Cut too small to mean anything
`days/day-50-chunking-and-top-k/parts/01-the-unit-you-index/1.3-cut-too-small-to-mean-anything.md` · level `working` · ids AG-14

Below a certain size a row stops being about anything, and the measurement shows it precisely: cutting the archive at eighty characters keeps the right document in the top three for nine questions out of ten while the text that comes back contains the answer for only five.

### 1.4 - The margin you pay for twice
`days/day-50-chunking-and-top-k/parts/01-the-unit-you-index/1.4-the-margin-you-pay-for-twice.md` · level `working` · ids AG-14

Overlap stores the text near every cut twice so that an idea straddling a boundary still exists whole somewhere, and it is a purchase with a price tag: at a chunk size of one hundred and sixty characters, an overlap of forty took answered@3 from 6 out of 10 to 8 out of 10 and made the index 19% larger.

### 2.1 - The answer key you write before you tune
`days/day-50-chunking-and-top-k/parts/02-measuring-the-cut/2.1-the-answer-key-you-write-before-you-tune.md` · level `working` · ids AG-14

You cannot tune a retriever without an answer key, and the key needs three columns — the question, the document that answers it, and the words that are the answer — because the difference between the second and the third column is where every chunking bug lives.

### 2.2 - One table, seven chunk sizes
`days/day-50-chunking-and-top-k/parts/02-measuring-the-cut/2.2-one-table-seven-chunk-sizes.md` · level `production` · ids AG-14

Swept across seven settings on the same archive and the same key, chunking bought Sutra no extra recall at all and cut the retrieved context from 459 tokens to 279 for the same ten answers out of ten — so the size that ships is 900 characters, and it ships because a table said so and not because it sounded reasonable.

### 2.3 - 💥 The cut that kept the ticket and lost the fix
`days/day-50-chunking-and-top-k/parts/02-measuring-the-cut/2.3-the-cut-that-kept-the-ticket-and-lost-the-fix.md` · level `production` · ids AG-14

At a chunk size of four hundred characters the top result for "customer bounced back to the sign-in page during single sign-on" is the correct ticket, scoring 0.381, and it does not contain the resolution — the cut fell between the sentence naming the cause and the sentence describing the effect, and every metric that counts documents reports this retrieval as a success.

### 3.1 - k is a budget, not a preference
`days/day-50-chunking-and-top-k/parts/03-the-k-is-a-budget/3.1-k-is-a-budget-not-a-preference.md` · level `working` · ids AG-14

k is the number of rows retrieval pastes into the prompt, and because a tool result is written into the transcript and re-sent on every later turn, one lookup at k=20 costs 8,539 tokens over a six-turn conversation where the same lookup at k=2 costs 1,006 — so k is a line in a budget and not a matter of taste.

### 3.2 - Where the curve goes flat
`days/day-50-chunking-and-top-k/parts/03-the-k-is-a-budget/3.2-where-the-curve-goes-flat.md` · level `production` · ids AG-14

On Sutra's archive the answer rate reaches its maximum at k = 2 and never improves again, so every row above two is pure cost — at k = 20 the retrieval is 92% noise and answers exactly the same ten questions out of ten that two rows answered.

### 3.3 - 💥 Twenty rows, and nothing new in nineteen
`days/day-50-chunking-and-top-k/parts/03-the-k-is-a-budget/3.3-twenty-rows-and-nothing-new-in-nineteen.md` · level `production` · ids AG-14

Raising k from two to twenty answers the same ten questions out of ten, costs eight and a half times as much over a conversation, and pushes the answer-bearing row away from the front of the block — for one question it lands at rank 7, a quarter of the way into the context, which is the region the model reads least reliably.

### 4.1 - 💥 Cosine never says it does not know
`days/day-50-chunking-and-top-k/parts/04-the-floor/4.1-cosine-never-says-it-does-not-know.md` · level `production` · ids AG-14

Asked "the office printer jams on thick paper" — a question about which the archive contains nothing whatsoever — retrieval returns three confident rows, the best of them scoring 0.388, which is higher than the score of the row that carries the correct answer for nine of the ten real questions.

### 4.2 - There is no floor that separates them
`days/day-50-chunking-and-top-k/parts/04-the-floor/4.2-there-is-no-floor-that-separates-them.md` · level `production` · ids AG-14

The worst real answer scores 0.180 and the best piece of nonsense scores 0.388, so the two distributions overlap and no similarity floor exists that keeps every real answer and rejects every impostor — the working rule needs a second condition, and SIM_FLOOR = 0.20 with MIN_SHARED_TERMS = 2 keeps nine of ten real answers, all three short questions, and lets none of the four impostors through.

### 4.3 - Nothing is an answer
`days/day-50-chunking-and-top-k/parts/04-the-floor/4.3-nothing-is-an-answer.md` · level `production` · ids AG-14

An empty result is a legitimate, useful and under-used outcome, and it has to be said rather than returned as silence: "I searched the archive and found nothing close enough to be useful — nobody has written this one up yet" is a sentence the desk needs, and it is not the same sentence as "there is no past case".

### 5.1 - When the answer is a rule
`days/day-50-chunking-and-top-k/parts/05-the-wrong-tool/5.1-when-the-answer-is-a-rule.md` · level `working` · ids AG-14

An archive records what happened, never what is allowed, so a question about policy has no correct answer anywhere in it — asked "how long does a customer have to ask for a refund", retrieval returns a ticket about API rate limits at 0.266 and clears the floor, because the question was never a similarity search.

### 5.2 - When the answer must be true now
`days/day-50-chunking-and-top-k/parts/05-the-wrong-tool/5.2-when-the-answer-must-be-true-now.md` · level `working` · ids AG-14

Zero of the sixty-one rows in the index carry anything resembling a date, so a question containing the words "right now" has nothing to match against — asked "is the export service slow right now", retrieval answers from a resolved ticket about a form, at 0.256, with total confidence and no notion of when anything happened.

### 5.3 - When the answer has to be counted
`days/day-50-chunking-and-top-k/parts/05-the-wrong-tool/5.3-when-the-answer-has-to-be-counted.md` · level `working` · ids AG-14

Ranking visits every row and returns the nearest few; counting has to visit every row and keep all of them, so "how many tickets are about signing in" has no answer in a top-k result at all — the true answer is 12 of 52, and retrieval returns three tickets and no number.

### 5.4 - When the whole archive fits in the prompt
`days/day-50-chunking-and-top-k/parts/05-the-wrong-tool/5.4-when-the-whole-archive-fits-in-the-prompt.md` · level `production` · ids AG-14

Sutra's entire archive is 2,795 tokens — a 32,000-token window holds it eleven times over — so retrieval here is not saving room, it is adding a way to miss, and the honest question is not "how do we retrieve better" but "at what archive size does retrieval start earning its place?"

### 6.1 - The five questions, in order
`days/day-50-chunking-and-top-k/parts/06-in-production/6.1-the-five-questions-in-order.md` · level `production` · ids AG-14

Five yes-or-no questions asked in a fixed order route any desk question to the tool that can actually answer it, and the order is the design: run them on twelve real questions and all twelve route correctly, drop the first question and two of them silently become retrieval.

### 6.2 - 🅿️ Rerankers, hybrid search and a vector database
`days/day-50-chunking-and-top-k/parts/06-in-production/6.2-rerankers-hybrid-search-and-a-vector-database.md` · level `production` · ids AG-14

Three pieces of production retrieval infrastructure are named, priced and deliberately not built: a reranker buys precision at the top of the list, hybrid search buys recall on words a vector misses, and a vector database buys scale — and Sutra needs none of them at sixty-one rows, which is the only honest reason to skip anything.

