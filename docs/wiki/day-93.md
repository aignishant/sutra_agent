# Day 93 - Repo public — what a stranger sees

IDs closed: - · source: `days/day-93-what-a-stranger-sees/`

## Parts

### 1.1 - Public means a stranger with no context
`days/day-93-what-a-stranger-sees/parts/01-the-stranger/1.1-public-means-a-stranger.md` · level `foundation` · ids -

Making a repository public does not publish the code — the code was always there — it publishes everything you assumed, to somebody who shares none of your assumptions and will not ask.

### 1.2 - The five files before the code
`days/day-93-what-a-stranger-sees/parts/01-the-stranger/1.2-the-five-files-before-the-code.md` · level `working` · ids -

A stranger checks five files before reading a line of code — what is this, may I use it, how do I send a change back, where do I report something dangerous, and what keys will I need — and this repository answers two of them.

### 1.3 - The README that documents the design
`days/day-93-what-a-stranger-sees/parts/01-the-stranger/1.3-the-readme-that-documents-the-design.md` · level `working` · ids -

Three claims in this repository's README are checkable against the thing that enforces them, and all three have drifted — the section count is wrong three different ways, two driver commands are undocumented, and the day-folder diagram omits a directory the README's own Status paragraph announces.

### 2.1 - A README is a test you can run
`days/day-93-what-a-stranger-sees/parts/02-running-the-readme/2.1-a-readme-is-a-test.md` · level `working` · ids -

A README is a list of instructions, and instructions have an exit code — so instead of reading this one, run every command in it, which is the only form of reading that cannot quietly supply the missing step from memory.

### 2.2 - The setup block that does not work here
`days/day-93-what-a-stranger-sees/parts/02-running-the-readme/2.2-the-setup-block-that-fails.md` · level `working` · ids -

Both failures are in the three-command Setup block, and they are not the same kind of thing: one is this machine's storage layer and belongs in a precondition the README never states, the other is a single lint error in the repository and belongs in a fix.

### 2.3 - What a README owes, and what it does not
`days/day-93-what-a-stranger-sees/parts/02-running-the-readme/2.3-what-a-readme-owes.md` · level `production` · ids -

A README owes a stranger five answers — what this is, what it costs, the first command, what it will not do, and where to go next — and the commonest failure is not omitting one of them but answering a sixth question nobody asked, at length, above the five.

### 3.1 - Seventeen thousand links
`days/day-93-what-a-stranger-sees/parts/03-the-docs-pass/3.1-seventeen-thousand-links.md` · level `working` · ids -

Two thousand and eighty-one tracked markdown files hold seventeen thousand six hundred and seventy- seven relative links, fifty of which point at nothing — and the checker that finds them has to know what a code block is, or it reports eighty-four and trains everybody to ignore it.

### 3.2 - Four kinds of broken link
`days/day-93-what-a-stranger-sees/parts/03-the-docs-pass/3.2-four-kinds-of-broken-link.md` · level `working` · ids -

The fifty broken links are not fifty tasks — three need a person to edit a day document, twenty-two are a generator bug that will come back if you edit the file instead, seven are stale output a re-run repairs, and eighteen are in a frozen archive nobody should touch.

### 3.3 - The index that regenerates broken
`days/day-93-what-a-stranger-sees/parts/03-the-docs-pass/3.3-the-index-that-regenerates-broken.md` · level `production` · ids -

Twenty-two of the wiki's links are broken by one line of the generator, which copies a paragraph out of a day part and into docs/wiki/ — and a paragraph containing a relative link does not survive being moved to another directory.

### 4.1 - The scan before the door opens
`days/day-93-what-a-stranger-sees/parts/04-nothing-extra/4.1-the-scan-before-the-door-opens.md` · level `production` · ids -

Two thousand one hundred and twenty-one tracked files, six key shapes, two hits — and both hits are teaching placeholders shaped exactly like a real key, which is the result a pre-publication scan actually produces and the reason triage is a person's job rather than the scanner's.

### 4.2 - History is the part you cannot take back
`days/day-93-what-a-stranger-sees/parts/04-nothing-extra/4.2-history-is-the-part-you-cannot-take-back.md` · level `production` · ids -

Publishing a repository publishes every commit in it, so the question is never what the files contain now but what they have ever contained — and scanning all two thousand three hundred and sixty-one blobs in this repository's history finds the same two placeholders, already committed, already permanent.

### 4.3 - The ledger a stranger reads
`days/day-93-what-a-stranger-sees/parts/04-nothing-extra/4.3-the-ledger-a-stranger-reads.md` · level `working` · ids -

Ninety-four day folders exist and docs/PROGRESS.md has fifty-one rows, so forty-three days are written, checked and green with nothing recording it — and a reader cannot tell those apart from forty-three days that were never started.

### 5.1 - A demo that fails honestly
`days/day-93-what-a-stranger-sees/parts/05-the-demo/5.1-a-demo-that-fails-honestly.md` · level `production` · ids -

Fifty-two modules are promised by the day documents and five exist, because the product code is deliberately the reader's work — so the only truthful demo script is one that names what is missing and exits non-zero, and writing the version that prints success would be describing a different repository.

### 5.2 - What a real public repository adds
`days/day-93-what-a-stranger-sees/parts/05-the-demo/5.2-what-a-real-public-repo-adds.md` · level `production` · ids -

Nine things stand between this repository and a door that can safely open, and they are not equally urgent: three are the licence, the ledger and the lint, they take about an afternoon between them, and everything else on the list is easier once they are done.

## Papers - read after the parts

### doi:10.1093/comjnl/27.2.97 - The document that runs
`days/day-93-what-a-stranger-sees/papers/01-the-document-that-runs.md`

Prose and code drift apart because they are two artefacts that have to be kept in step by hand — and the paper's answer is to stop having two, so that a sentence claiming the ledger leaves nineteen units is a sentence that gets executed and can fail.

