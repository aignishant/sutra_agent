# Day 69 - PII & data boundaries — synthetic data only, free-tier training caveat

IDs closed: SEC-12, SEC-13 · source: `days/day-69-pii-and-data-boundaries/`

## Parts

### 1.1 - The list of fields is not the answer
`days/day-69-pii-and-data-boundaries/parts/01-who-a-record-names/1.1-the-list-of-fields-is-not-the-answer.md` · level `foundation` · ids SEC-12

Personal data is not a set of column names you can tick off; it is anything that gets you back to a particular person, which means the question is never "is this field on the list?" but "could somebody find them with this?"

### 1.2 - Three columns that name one person
`days/day-69-pii-and-data-boundaries/parts/01-who-a-record-names/1.2-three-columns-that-name-one-person.md` · level `working` · ids SEC-12

A table with the name, the address, the telephone number and the email all removed still names ten of its twelve accounts once you look at three ordinary columns together, because identification is a property of combinations and not of fields.

### 1.3 - The box marked \"anything else\
`days/day-69-pii-and-data-boundaries/parts/01-who-a-record-names/1.3-the-box-marked-anything-else.md` · level `working` · ids SEC-12

Two thirds of the identifiers in Sutra's archive are in prose rather than in any field, so a redactor that is perfect on the structured half of a ticket still leaves eight of fourteen tickets naming somebody.

### 1.4 - The number that only means something here
`days/day-69-pii-and-data-boundaries/parts/01-who-a-record-names/1.4-the-number-that-only-means-something-here.md` · level `working` · ids SEC-12

88-4471 is meaningless to anyone outside this system and decisive inside it, so whether a value is personal data depends on who holds the table it joins to — and you are the one holding it.

### 2.1 - One sentence, seven places
`days/day-69-pii-and-data-boundaries/parts/02-where-the-copies-are/2.1-one-sentence-seven-places.md` · level `working` · ids SEC-12

One ordinary run of the desk leaves one customer's email address in all seven of its stores, thirteen times, and not one line of code in the previous twenty days was written to copy customer data.

### 2.2 - A boundary is a line you can name
`days/day-69-pii-and-data-boundaries/parts/02-where-the-copies-are/2.2-a-boundary-is-a-line-you-can-name.md` · level `working` · ids SEC-12

A data boundary is not a feeling about what is sensitive; it is a named line with a rule attached, and until you can say where the line is and what may cross it, you have a preference rather than a control.

### 2.3 - The copy nobody calls a copy
`days/day-69-pii-and-data-boundaries/parts/02-where-the-copies-are/2.3-the-copy-nobody-calls-a-copy.md` · level `working` · ids SEC-12

An index and a cache feel like they hold structure rather than content, and both of them hold the full text — which is why a delete from the archive leaves the customer's name, telephone number and address sitting in index.json, readable with cat.

### 2.4 - The reply is personal data too
`days/day-69-pii-and-data-boundaries/parts/02-where-the-copies-are/2.4-the-reply-is-personal-data-too.md` · level `working` · ids SEC-12

The desk's own output quotes the customer back at them — "Hello Lin Zhou…" — so the generated half of every stored exchange is personal data that no redactor pointed at the input will ever see.

### 3.1 - Three providers, three answers
`days/day-69-pii-and-data-boundaries/parts/03-the-line-at-the-provider/3.1-three-providers-three-answers.md` · level `production` · ids SEC-13

Asked whether they may train on what a free tier sends them, Sutra's three providers give three different answers — yes, no, and it depends on a setting — and the one that says yes is the primary.

### 3.2 - The page that does not answer
`days/day-69-pii-and-data-boundaries/parts/03-the-line-at-the-provider/3.2-the-page-that-does-not-answer.md` · level `working` · ids SEC-13

When a provider's page does not address whether it trains on what you send it, the honest row is "read on this date, did not say" — and a row that guesses is worse than one that admits the document was silent, because a guess is indistinguishable from a fact six months later.

### 3.3 - What follows for Sutra
`days/day-69-pii-and-data-boundaries/parts/03-the-line-at-the-provider/3.3-what-follows-for-sutra.md` · level `production` · ids SEC-12, SEC-13

Sutra's primary provider trains on free-tier content, so no real personal data may enter this repository — a refusal rather than a worry, and one this curriculum has been quietly obeying since long before anybody wrote it down.

### 4.1 - Why invent the customers
`days/day-69-pii-and-data-boundaries/parts/04-invented-on-purpose/4.1-why-invent-the-customers.md` · level `foundation` · ids SEC-12

Generated data is not a weaker stand-in for real data; it is a different instrument with three powers real traffic cannot give you at any price — you can reproduce it, you can share it, and you can put the rare case in on purpose — and the privacy argument everybody reaches for first is only the fourth.

### 4.2 - A generator is a specification
`days/day-69-pii-and-data-boundaries/parts/04-invented-on-purpose/4.2-a-generator-is-a-specification.md` · level `working` · ids SEC-12

Writing the generator forces you to put every shape you believe your data contains into code, which turns a belief you cannot argue with into a file you can read, diff and disagree with — and turns the shapes you never thought of into a visible absence instead of an invisible assumption.

### 4.3 - The corpus that flatters your detector
`days/day-69-pii-and-data-boundaries/parts/04-invented-on-purpose/4.3-the-corpus-that-flatters-your-detector.md` · level `production` · ids SEC-12

A generator emits the shapes its author thought of and a redactor matches the shapes its author thought of, so when the same person wrote both, the score measures the person: 100% on two hundred generated tickets against 80% on the fourteen hand-written ones, and the twenty-point gap is not a better redactor.

### 5.1 - The answer key comes first
`days/day-69-pii-and-data-boundaries/parts/05-measuring-the-redactor/5.1-the-answer-key-comes-first.md` · level `working` · ids SEC-12

A redactor with no measured recall is a redactor nobody can tune, so the first thing this section builds is not the redactor — it is the answer key: twenty rows, written by hand before any pattern exists, each saying what identifier is really in the archive, what kind it is, and where it was sitting.

### 5.2 - Fifty per cent, and it looked fine
`days/day-69-pii-and-data-boundaries/parts/05-measuring-the-redactor/5.2-fifty-per-cent-and-it-looked-fine.md` · level `production` · ids SEC-12

V1 catches 10 of 20 identifiers, which reads as half a job done and something to keep chipping away at — until the same run is split by where each value was sitting, and it is 7 of 7 in the structured field and 3 of 13 in free text: a redactor that is perfect on the half that was never the problem.

### 5.3 - The wall called a name
`days/day-69-pii-and-data-boundaries/parts/05-measuring-the-redactor/5.3-the-wall-called-a-name.md` · level `production` · ids SEC-12

A name is not a pattern and a hash of a name is still a name: a redactor cannot match a name because names have no shape, and hashing one does not stop it naming somebody — 6 of 8 addresses in this archive come back from their hashes, and the salted column comes back exactly the same 6 of 8.

### 6.1 - Deleted, and still retrievable
`days/day-69-pii-and-data-boundaries/parts/06-the-delete-that-did-not/6.1-deleted-and-still-retrievable.md` · level `production` · ids SEC-12

Deleting the ticket from the archive succeeds, raises nothing, and leaves the customer's address in 6 of 7 stores — and the search index will hand the whole message back, signature and all, to the next question that matches it.

### 6.2 - The store you cannot address
`days/day-69-pii-and-data-boundaries/parts/06-the-delete-that-did-not/6.2-the-store-you-cannot-address.md` · level `production` · ids SEC-12

Five of the seven stores can be reached by key, one has to be scanned because its key is a hash of the prompt and cannot be asked what do you hold about this person, and one — the log — must survive, so erasing it means removing the personal part and keeping the line that proves the event happened.

### 6.3 - The loop over a list somebody kept
`days/day-69-pii-and-data-boundaries/parts/06-the-delete-that-did-not/6.3-the-loop-over-a-list-somebody-kept.md` · level `production` · ids SEC-12

The delete that reaches everywhere is not a cleverer delete — it is a loop over a registry, and the measured result is copies remaining 0 across all seven stores, with the whole difference from part 6.1 being that the list of stores is data the code iterates rather than a list a person remembers.

### 7.1 - Answering \"what do you hold?\
`days/day-69-pii-and-data-boundaries/parts/07-in-production/7.1-answering-what-do-you-hold.md` · level `production` · ids SEC-12

The question a person is entitled to ask is what do you hold about me, and the desk can only answer it from the same registry the purge loops over — 7 of 7 stores, 13 copies after a single ordinary run, each with the day and the reason it was written.

### 7.2 - The boundary written down
`days/day-69-pii-and-data-boundaries/parts/07-in-production/7.2-the-boundary-written-down.md` · level `production` · ids SEC-12, SEC-13

A data boundary that exists only as a shared understanding is not a boundary — today's gate turns it into six checks that can go red, four of which are red right now, including a redactor whose free-text recall is 69% against a 90% floor and a check that every fixture value comes from a range reserved for fiction.

## Papers - read after the parts

### arXiv:2012.07805 - Extracting Training Data from Large Language Models
`days/day-69-pii-and-data-boundaries/papers/01-extracting-training-data.md`

Before this document the working assumption was that a model learns statistics about its training data rather than the data itself — which made sending text to a model feel categorically different from storing it — and this paper's contribution was to show that the assumption is wrong in a specific, demonstrable way: individual training examples can be recovered word for word, by somebody who only gets to ask the model questions.

