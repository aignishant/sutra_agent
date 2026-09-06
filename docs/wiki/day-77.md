# Day 77 - The standup agent — a voice client over the queue state

IDs closed: ADK-57, AG-25 · source: `days/day-77-the-standup-agent/`

## Parts

### 1.1 - A report with one chance
`days/day-77-the-standup-agent/parts/01-a-report-somebody-hears/1.1-a-report-with-one-chance.md` · level `foundation` · ids ADK-57, AG-25

A written report is finished by its reader — they choose where to start, go back over a line, skip the part that is not theirs and stop when they have what they came for — while a spoken report arrives in one order, at one speed, once, so every convenience the page hands out for free has to be supplied by the author instead, and the first and biggest of them is deciding what comes first.

### 1.2 - The three tools, called for real
`days/day-77-the-standup-agent/parts/01-a-report-somebody-hears/1.2-the-three-tools.md` · level `working` · ids ADK-57, AG-25

The standup agent is the first thing in this curriculum to call three tools in one turn — the runtime answering each one and pushing the result back through the open connection before the next call is emitted — and it worked the first time it was run, which is worth saying plainly, because the ease of the plumbing is exactly what makes it tempting to think the agent is finished when the tools work.

### 1.3 - What the listener actually got
`days/day-77-the-standup-agent/parts/01-a-report-somebody-hears/1.3-what-the-listener-got.md` · level `production` · ids ADK-57, AG-25

Both standups called all three tools, read the queue correctly and said only true things — and when the listener spoke after two sentences, attention-first had delivered 3 of 3 sentences that needed a person while queue order had delivered 0 of 2.

### 2.1 - One function, one order
`days/day-77-the-standup-agent/parts/02-the-order-is-the-product/2.1-one-function-one-order.md` · level `working` · ids ADK-57, AG-25

The order a standup is said in is one decision, so it belongs in one function — lines(queue, night), returning the sentences in the order they will be spoken — and because that function returns data instead of printing text, the order becomes something a test can read.

### 2.2 - Carry the flag, do not search for it
`days/day-77-the-standup-agent/parts/02-the-order-is-the-product/2.2-carry-the-flag.md` · level `production` · ids ADK-57, AG-25

The first version of this lab worked out which sentences mattered by searching them for the phrase "needs you" — and the good standup says "Two tickets need you", so the search missed it and the measurement reported 53 words before the first important sentence when the answer was 0, ranking the ablation as the better of the two.

### 2.3 - Words before it matters
`days/day-77-the-standup-agent/parts/02-the-order-is-the-product/2.3-words-before-it-matters.md` · level `working` · ids ADK-57, AG-25

The two orderings contain exactly the same facts, and the number that separates them is words before the first sentence that needs a person: 0 against 25 — not length, position.

### 3.1 - Nothing needs you is a report
`days/day-77-the-standup-agent/parts/03-the-quiet-morning/3.1-nothing-needs-you.md` · level `production` · ids ADK-57, AG-25

From the listener's side, a standup that says nothing and a standup that has stopped running are the same event, so "nothing needs you" has to be a sentence somebody deliberately wrote — an assertion that the check was made and came back clean — and never the absence of sentences.

### 3.2 - Saying what you do not know
`days/day-77-the-standup-agent/parts/03-the-quiet-morning/3.2-saying-what-you-do-not-know.md` · level `production` · ids ADK-57, AG-25

Last night's job died before it wrote the digest, so one of the three things this standup reports on does not exist — and the dangerous version of that is not a wrong sentence, it is no sentence, because a section quietly left out of a spoken report is heard as nothing to report: omitting the digest does not omit anything, it asserts a good night.

### 4.1 - What a standup costs
`days/day-77-the-standup-agent/parts/04-in-production/4.1-what-a-standup-costs.md` · level `production` · ids ADK-57, AG-25

A standup is spent from a person's attention long before it is spent from anybody's quota, and the two budgets behave nothing alike: quota is per morning, shared across the whole product and written down; attention is per listener, renews slowly, is spent whether or not the report turned out to be worth hearing — and nothing anywhere records it.

### 4.2 - Who it is for
`days/day-77-the-standup-agent/parts/04-in-production/4.2-who-it-is-for.md` · level `production` · ids ADK-57, AG-25

"Needs a person" is not a property of a ticket — it is a property of a ticket and a listener, so the same twelve tickets make three different correct standups for three different people, and the ordering rule this whole day has been arguing for only means something once you have said who is listening.

### 4.3 - What a real one adds
`days/day-77-the-standup-agent/parts/04-in-production/4.3-what-a-real-one-adds.md` · level `production` · ids ADK-57, AG-25

The lab's standup is a correct one-way announcement, and the distance between that and a report a team would actually rely on is not vague "polish" — it is a specific, enumerable list of nine things, and almost all of it is about two subjects the lab does not contain a single line of: what changed since yesterday and how old the state is, and dialogue — the fact that a standup is the opening of a conversation rather than a broadcast.

## Papers - read after the parts

### doi:10.1037/h0043158 - The magical number seven, plus or minus two: Some limits on our capacity for processing information.
`days/day-77-the-standup-agent/papers/01-chunking.md`

A listener cannot hold a long list, and the useful part of that is not the limit — it is what the limit is measured in. It is not information and not words; it is units, and how much information you put inside each unit is up to you. Twelve ticket references are twelve units and nobody keeps them; "two needing you, then four sign-in, four billing, four export" is 4 units carrying the same twelve tickets.

