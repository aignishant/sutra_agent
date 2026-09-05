# Day 48 - Memory design — what to remember, what to forget

IDs closed: AG-12, AG-13 · source: `days/day-48-memory-design/`

## Parts

### 1.1 - The chat nobody can leave
`days/day-48-memory-design/parts/01-what-a-conversation-leaves/1.1-the-chat-nobody-can-leave.md` · level `foundation` · ids AG-12

Keeping everything is not the absence of a memory policy, it is a memory policy, and it is the one policy nobody wrote down or agreed to.

### 1.2 - Six kinds, not one bucket
`days/day-48-memory-design/parts/01-what-a-conversation-leaves/1.2-six-kinds-not-one-bucket.md` · level `foundation` · ids AG-12

"What should the agent remember?" has no useful answer until you split the question by kind, because a fact, a decision, a correction and a guess want four different lifetimes and only one of them wants none.

### 1.3 - The transcript is exhaust
`days/day-48-memory-design/parts/01-what-a-conversation-leaves/1.3-the-transcript-is-exhaust.md` · level `working` · ids AG-12

The raw turns of a conversation are what produced the memory, not the memory itself, and the right place for them is the session store you already have rather than the memory store you are about to fill.

### 1.4 - A correction outranks what it corrects
`days/day-48-memory-design/parts/01-what-a-conversation-leaves/1.4-a-correction-outranks-it.md` · level `working` · ids AG-12

When a customer says "actually, no", they have not added a second fact — they have replaced the first one, and a store that treats both as equally live will sometimes answer with the version the customer already told you was wrong.

### 2.1 - A rule someone else can read
`days/day-48-memory-design/parts/02-policy-as-data/2.1-a-rule-someone-else-can-read.md` · level `working` · ids AG-12

Write the retention rules as rows of data rather than as branches of code, because the person who carries the risk of a bad rule is not the person who can read Python.

### 2.2 - Every verdict names its row
`days/day-48-memory-design/parts/02-policy-as-data/2.2-every-verdict-names-its-row.md` · level `working` · ids AG-12

A decision to keep or drop something must come back carrying the rule that made it, because a verdict without a citation cannot be checked, appealed or improved.

### 2.3 - The kind with no rule
`days/day-48-memory-design/parts/02-policy-as-data/2.3-the-kind-with-no-rule.md` · level `working` · ids AG-12

The most important row in a retention policy is the one that is not there: what happens to something nobody wrote a rule for, and the only safe answer is that it is refused.

### 3.1 - True on the day it was said
`days/day-48-memory-design/parts/03-expiry-and-supersession/3.1-true-on-the-day-it-was-said.md` · level `working` · ids AG-13

Some memories go off, and the only way a store can know is if the date they stop being trustworthy was written on them when they went in.

### 3.2 - The newer fact wins
`days/day-48-memory-design/parts/03-expiry-and-supersession/3.2-the-newer-fact-wins.md` · level `working` · ids AG-13

A fact can be perfectly fresh and still wrong, because something newer about the same subject replaced it — and unlike expiry, nothing about the memo itself will ever tell you.

### 3.3 - A verdict is not an erasure
`days/day-48-memory-design/parts/03-expiry-and-supersession/3.3-a-verdict-is-not-an-erasure.md` · level `production` · ids AG-13

Deciding that a memo should be forgotten and actually removing it are two different events, and everything that reads the store between them still sees the memo.

### 4.1 - Redact before you write
`days/day-48-memory-design/parts/04-privacy-and-erasure/4.1-redact-before-you-write.md` · level `working` · ids AG-13

Personal data that never reaches storage cannot leak, cannot be backed up, cannot be exported and cannot be asked for — so the redaction happens on the way in, not on the way out.

### 4.2 - You cannot delete what you cannot address
`days/day-48-memory-design/parts/04-privacy-and-erasure/4.2-you-cannot-delete-what-you-cannot-address.md` · level `working` · ids AG-13

Deleting one person's data is only possible if every stored item says whose it is, so the field that looks like bookkeeping is the field the whole obligation rests on.

### 4.3 - Erasure is an obligation
`days/day-48-memory-design/parts/04-privacy-and-erasure/4.3-erasure-is-an-obligation.md` · level `production` · ids AG-13

A memory system with no delete path is a liability rather than a feature gap, and the framework Sutra uses does not give you one — so the policy owns it or nobody does.

### 4.4 - The store that must not be committed
`days/day-48-memory-design/parts/04-privacy-and-erasure/4.4-the-store-that-must-not-be-committed.md` · level `production` · ids AG-13

Every retention rule in this policy is undone the moment the store is committed to git, because git keeps everything forever and this repository goes public.

### 5.1 - 💥 The summary that lost the sentence you needed
`days/day-48-memory-design/parts/05-failure-lab/5.1-the-summary-that-lost-the-sentence.md` · level `production` · ids AG-12

Compressing a conversation into a summary throws away exactly the detail a later question needed, and the loss is invisible at the moment it happens because a good summary looks complete.

### 5.2 - 💥 The price that changed last year
`days/day-48-memory-design/parts/05-failure-lab/5.2-the-price-that-changed-last-year.md` · level `production` · ids AG-13

A memo with no expiry date does not go quiet when it stops being true — it keeps answering, with the same confidence it had on the day it was written.

### 5.3 - 💥 The rule that deleted the evidence
`days/day-48-memory-design/parts/05-failure-lab/5.3-the-rule-that-deleted-the-evidence.md` · level `production` · ids AG-13

Forgetting is a feature right up to the moment somebody disputes what you did, and a retention number chosen for tidiness rather than for a reason will eventually delete the only record of a decision.

### 6.1 - Charged again on every turn
`days/day-48-memory-design/parts/06-the-price/6.1-charged-again-on-every-turn.md` · level `production` · ids AG-12, AG-13

A remembered fact is not paid for once when you store it — it is paid for again on every turn that retrieves it, so retention is priced per turn and not per row.

### 6.2 - A policy nobody priced
`days/day-48-memory-design/parts/06-the-price/6.2-a-policy-nobody-priced.md` · level `production` · ids AG-12, AG-13

Put the three candidate retention policies in one table with a number beside each, and the argument stops being about who is more confident.

