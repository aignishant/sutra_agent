# Day 92 - Hardening pass — the review before it goes public

IDs closed: SEC-16 · source: `days/day-92-before-it-goes-public/`

## Parts

### 1.1 - A review is a set of checks that can fail
`days/day-92-before-it-goes-public/parts/01-what-a-review-is/1.1-a-check-that-can-fail.md` · level `foundation` · ids SEC-16

A security review is not a document you produce and it is not a list of questions you answer; it is a set of commands that run against the repository as it actually is, each of which can come back red — and this one comes back with three passing and five blocking.

### 1.2 - The inventory comes before the opinion
`days/day-92-before-it-goes-public/parts/01-what-a-review-is/1.2-the-inventory-comes-first.md` · level `foundation` · ids SEC-16

You cannot review what you have not counted, and the counting is the slow honest part: two thousand one hundred and twenty-one tracked files, sixty-nine commits, one hundred and thirteen installed packages, sixteen named controls — every later finding in this day is a subset of one of those four numbers.

### 1.3 - The checklist that answers itself
`days/day-92-before-it-goes-public/parts/01-what-a-review-is/1.3-the-checklist-that-answers-itself.md` · level `working` · ids SEC-16

Three of this day's checks have an arm that runs the same code, reads a narrower thing, prints only true sentences, and exits 0 — and the composite of those three is a security review that reports 0 errors over a repository with five blocking findings in it.

### 2.1 - The scan that found nothing
`days/day-92-before-it-goes-public/parts/02-secrets/2.1-the-scan-that-found-nothing.md` · level `working` · ids SEC-16

Two thousand one hundred and twenty-one tracked files and sixty-nine commits contain zero live credentials, the two shaped hits are lesson fixtures that announce themselves, and the result is worth reporting only because a self-test proves the detector would have caught one.

### 2.2 - The channel no file scanner reads
`days/day-92-before-it-goes-public/parts/02-secrets/2.2-the-channel-no-file-scanner-reads.md` · level `production` · ids SEC-16

Not one address belonging to a real person is in any of two thousand one hundred and twenty-one tracked files — and the same repository publishes one on every single one of its sixty-nine commits, because the author identity lives in the commit and no scanner that reads files will ever open it.

### 2.3 - The template that drifted
`days/day-92-before-it-goes-public/parts/02-secrets/2.3-the-template-that-drifted.md` · level `working` · ids SEC-16

.env holds five keys and the committed .env.example describes four, so the file a new contributor copies is missing GEMINI_API_KEY — a small finding, found only because the check compares two files instead of asking whether an example exists.

### 3.1 - One account name, fifty-one lines
`days/day-92-before-it-goes-public/parts/03-what-is-not-a-secret/3.1-fifty-one-lines.md` · level `production` · ids SEC-16

This machine's account name appears fifty-one times across twenty-six tracked files in fifteen day folders, every occurrence arrived inside a real pasted traceback, and pasting the traceback verbatim is what Principle 10 requires — so two of this repository's own principles are in direct conflict and the review is where that gets noticed.

### 3.2 - The highlighter used on every line
`days/day-92-before-it-goes-public/parts/03-what-is-not-a-secret/3.2-the-highlighter.md` · level `working` · ids SEC-16

The same scanner, the same repository, one looser pattern: zero real hits becomes twelve thousand two hundred and eighty-six lines to read by hand — and a report nobody finishes reading has exactly the value of a report nobody ran.

### 3.3 - What cannot be taken back
`days/day-92-before-it-goes-public/parts/03-what-is-not-a-secret/3.3-what-cannot-be-taken-back.md` · level `production` · ids SEC-16

Publishing is the one operation in this repository with no undo: fifty-one account-name lines can be scrubbed today with a find-and-replace and sixty-nine commits of author metadata cannot be changed at all without rewriting every hash — so the ordering of this day and Day 93 is the entire mitigation.

### 4.1 - The keys you hand over
`days/day-92-before-it-goes-public/parts/04-the-control-surface/4.1-the-keys-you-hand-over.md` · level `working` · ids SEC-16

The desk declares two tools, both read an in-memory dictionary, neither can change anything, and no approval step exists anywhere in sutra/ — which is a pass, and a pass that expires the moment somebody adds a third tool.

### 4.2 - Thirteen taught, three shipped
`days/day-92-before-it-goes-public/parts/04-the-control-surface/4.2-thirteen-taught-three-shipped.md` · level `production` · ids SEC-16

The plan names sixteen security controls; six of them have their vocabulary somewhere in sutra/, three survive when comments and docstrings are stripped, and two of the three the ledger reports as closed are not in the product at all.

### 4.3 - Six chosen, one hundred and thirteen installed
`days/day-92-before-it-goes-public/parts/04-the-control-surface/4.3-six-chosen-one-hundred-and-thirteen-installed.md` · level `production` · ids SEC-16

pyproject.toml names six dependencies and the environment contains one hundred and thirteen distributions — a factor of nineteen — and every one of the other hundred and seven imports at exactly the same privilege as the code that chose it, with no row in docs/PACKAGES.md recording a decision about any of them.

### 5.1 - The verdict, and what blocks Day 93
`days/day-92-before-it-goes-public/parts/05-the-verdict/5.1-the-verdict.md` · level `production` · ids SEC-16

Three pass and five block: no credential is in this repository or its history, and what stands between it and publication is one person's account name in fifty-one lines, an identity on every commit, a stale template, thirteen controls that were taught and never shipped, and a hundred and seven packages nobody chose.

### 5.2 - What a real hardening pass adds
`days/day-92-before-it-goes-public/parts/05-the-verdict/5.2-what-a-real-hardening-pass-adds.md` · level `production` · ids SEC-16

Eight checks that read files, git and installed metadata is a genuine review and it is the cheap half; the distance between it and one a team can rely on is nine items, two of which must happen before Day 93 and the rest of which are worthless unless the checks run on every commit.

## Papers - read after the parts

### doi:10.1145/168588.168615 - How systems actually fail
`days/day-92-before-it-goes-public/papers/01-how-systems-actually-fail.md`

The controls in this repository were all written against an attacker, and every failure it has actually recorded was the system reporting success incorrectly or information leaving by a channel nobody had drawn — zero of eleven anticipated, which is the paper's claim reproduced on the repository that quotes it.

