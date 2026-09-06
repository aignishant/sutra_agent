# Day 52 - Phase gate — memory wired into the triage flow

IDs closed: AG-15 · source: `days/day-52-memory-in-triage-flow/`

## Parts

### 1.1 - The sentence the phase promised
`days/day-52-memory-in-triage-flow/parts/01-the-promise/1.1-the-sentence-the-phase-promised.md` · level `foundation` · ids AG-15

Phase 7 exists to make one sentence answerable — "have we seen anything like this before?" — and a phase gate is the day you stop discussing whether the sentence is answerable and find out.

### 1.2 - A gate is not an audit
`days/day-52-memory-in-triage-flow/parts/01-the-promise/1.2-a-gate-is-not-an-audit.md` · level `foundation` · ids AG-15

An audit checks a component against a list of rules; a gate checks whether a promise made to a person is kept end to end — and the difference decides what you check, in what order, and what you are allowed to call green.

### 2.1 - G01 — the question, answered end to end
`days/day-52-memory-in-triage-flow/parts/02-the-run/2.1-the-question-answered-end-to-end.md` · level `working` · ids AG-15

G01: asked a question whose answer exists only in a memo filed this week, the desk returns that memo above every archive row — measured at 0.439 against 0.345, where the same question without the memo returns the original complaint and stops.

### 2.2 - G02 — an answer that names its source
`days/day-52-memory-in-triage-flow/parts/02-the-run/2.2-an-answer-that-names-its-source.md` · level `working` · ids AG-15

G02: every answer carries the reference of the row it came from and that reference resolves to a row that exists — because an answer without a citation is exactly as fluent as one with it, and cannot be checked, corrected or defended.

### 3.1 - G03 — nothing is filed unless a line files it
`days/day-52-memory-in-triage-flow/parts/03-the-write-path/3.1-nothing-is-filed-unless-a-line-files-it.md` · level `working` · ids AG-15

G03: memory fills only where a line of code fills it, and the counts must reconcile — six candidates proposed, five kept, one refused, four live — because a store nobody writes to is indistinguishable from a store that does not exist.

### 3.2 - G04 — every memo names the rule that kept it
`days/day-52-memory-in-triage-flow/parts/03-the-write-path/3.2-every-memo-names-the-rule-that-kept-it.md` · level `working` · ids AG-15

G04: every stored memo carries the retention rule that admitted it and every rule carries a reason — because a store where things are simply present cannot be reviewed, appealed or cleaned up, and the reason is the field that rots first.

### 3.3 - G05 — nothing personal reached the store
`days/day-52-memory-in-triage-flow/parts/03-the-write-path/3.3-nothing-personal-reached-the-store.md` · level `working` · ids AG-15

G05: no personal detail is in the store, checked by running the patterns against the stored rows rather than against the code that was supposed to strip them — and the same conversations redacted on the way out instead leave two rows still matching.

### 4.1 - G06 — the ranked path is the one that ships
`days/day-52-memory-in-triage-flow/parts/04-the-read-path/4.1-the-ranked-path-is-the-one-that-ships.md` · level `working` · ids AG-15

G06: three read paths over the same index and the same answer key give 0/10, 10/10 and 9/10 answered — and only the third one, which loses a real answer, rejects all four questions the archive cannot answer.

### 4.2 - G07 — every constant names its run
`days/day-52-memory-in-triage-flow/parts/04-the-read-path/4.2-every-constant-names-its-run.md` · level `production` · ids AG-15

G07: every tuned number carries a comment naming the run it came from and no two modules own the same number — a check that deleting two comment lines takes from zero findings to one, and that this project's own TOP_K fails on the second half.

### 4.3 - G08 — nothing, said out loud
`days/day-52-memory-in-triage-flow/parts/04-the-read-path/4.3-nothing-said-out-loud.md` · level `working` · ids AG-15

G08: all four questions the archive cannot answer come back with a sentence saying the search found nothing — a sentence that makes a claim about the search and never about the world, because those are different claims and only one of them is true.

### 5.1 - G09 — counted during the run, not after
`days/day-52-memory-in-triage-flow/parts/05-the-zero-claim/5.1-counted-during-the-run-not-after.md` · level `production` · ids AG-15

G09: the phase's request budget is a number a counter produced while the desk was running — fourteen questions, fourteen model requests, zero requests to any provider — and not a number somebody typed into a document afterwards.

### 5.2 - G10 — the lane we did not buy
`days/day-52-memory-in-triage-flow/parts/05-the-zero-claim/5.2-the-lane-we-did-not-buy.md` · level `production` · ids AG-15

G10: building and searching this memory spent zero provider requests, and the hosted alternative is priced from a measured tier rather than dismissed — fifteen requests against a free tier of about twenty a day, for one run of fourteen questions.

### 5.3 - G11 — what a cache can and cannot reach
`days/day-52-memory-in-triage-flow/parts/05-the-zero-claim/5.3-what-a-cache-can-and-cannot-reach.md` · level `production` · ids AG-15

G11: the desk's one request splits 41% fixed and 59% variable at the shipped k, and the variable half is the retrieved rows — so retrieval, which is what made the desk useful, is also what put most of the request permanently out of a cache's reach.

### 6.1 - 💥 The store that was never filled
`days/day-52-memory-in-triage-flow/parts/06-failure-lab/6.1-the-store-that-was-never-filled.md` · level `production` · ids AG-15

An empty memory produces a healthy-looking desk: rows returned, a score of 0.415, a citation that resolves, no errors and no warnings — and the only check that separates it from a working one is naming a case in advance and asking whether it can be found.

### 6.2 - 💥 The memo that could not be found
`days/day-52-memory-in-triage-flow/parts/06-failure-lab/6.2-the-memo-that-could-not-be-found.md` · level `production` · ids AG-15

A memo filed, judged, admitted and live in the store was unreachable because the index was built one memo earlier — and the desk returned the same top answer either way, so the only observable difference was a score moving from 0.314 to 0.285.

### 6.3 - 💥 Green because nothing existed
`days/day-52-memory-in-triage-flow/parts/06-failure-lab/6.3-green-because-nothing-existed.md` · level `production` · ids AG-15

Two implementations of the same five checks over the same repository print PHASE 7 GREEN and PHASE 7 NOT GREEN — and the one that says green is the one that treats a module it cannot import as nothing to check rather than as the finding it is.

### 7.1 - The freshness re-check
`days/day-52-memory-in-triage-flow/parts/07-the-phase-boundary/7.1-the-freshness-recheck.md` · level `production` · ids AG-15

Four things outside this repository get re-read at every phase boundary; on 2026-09-05 two came back green, one came back amber because the numbers moved behind a login, and the offline half found a real Principle 7 violation — mcp==1.29.1 is pinned in pyproject.toml with no row in docs/PACKAGES.md.

### 7.2 - Six conditions, and the one that is amber
`days/day-52-memory-in-triage-flow/parts/07-the-phase-boundary/7.2-six-conditions-and-the-one-that-is-amber.md` · level `production` · ids AG-15

Plan section 15 lists six conditions for a green phase; on 2026-09-05 two hold, three do not, one is in progress, and the honest verdict for Phase 7 is not green — which is a result, not a failure.

### 7.3 - What Phase 8 inherits
`days/day-52-memory-in-triage-flow/parts/07-the-phase-boundary/7.3-what-phase-eight-inherits.md` · level `production` · ids AG-15

Four of the six steps behind one answer already exist and none of them calls a model — but only two of the four are shaped like a node, because the other two reach for a module-level dictionary instead of taking it as an argument.

