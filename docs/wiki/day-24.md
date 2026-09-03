# Day 24 - Token accounting & budgets — denominated in quota (RPM/RPD), not dollars

IDs closed: AG-11, OPS-07 · source: `days/day-24-token-accounting-and-budgets/`

## Parts

### 1.1 - A ticket id costs five tokens
`days/day-24-token-accounting-and-budgets/parts/01-what-a-request-costs/1.1-a-ticket-id-costs-five-tokens.md` · level `foundation` · ids AG-11

Asking the provider rather than guessing gives 4.55 characters per token for English prose, 2.21 for a JSON log line, and 0.80 for the string "4521" — so the four characters of a ticket id cost five tokens, and any estimate based on word count is wrong in a direction that depends on what you are sending.

### 1.2 - The conversation is charged again every turn
`days/day-24-token-accounting-and-budgets/parts/01-what-a-request-costs/1.2-charged-again-every-turn.md` · level `working` · ids AG-11

An eight-turn conversation whose full text is 151 tokens cost 786 tokens to conduct — 5.2 times its own size — because a chat model is stateless and turn eight sends turns one to eight again.

### 1.3 - The unit that gets rationed is the request
`days/day-24-token-accounting-and-budgets/parts/01-what-a-request-costs/1.3-the-unit-that-gets-rationed.md` · level `working` · ids AG-11, OPS-07

On a free tier the provider counts requests, not tokens — the quota metric it names in a refusal is generate_content_free_tier_requests with quotaValue: '20' — so a 43-token question and a 151-token one cost exactly the same, and every optimisation aimed at token count buys you nothing.

### 2.1 - Two ceilings, and only one of them clears
`days/day-24-token-accounting-and-budgets/parts/02-two-ceilings/2.1-two-ceilings-one-clears.md` · level `working` · ids OPS-07

A free tier enforces two independent limits — requests per minute, which refills as time passes, and requests per day, which does not — and a budget that models them as one number will either refuse work that would have been served or wait patiently for a ceiling that is never going to lift.

### 2.2 - Reading the ceiling off a refusal
`days/day-24-token-accounting-and-budgets/parts/02-two-ceilings/2.2-reading-the-ceiling-off-a-refusal.md` · level `working` · ids OPS-07

The daily ceiling was not taken from a documentation page — it was read out of a real refusal, whose QuotaFailure detail states quotaValue: '20' for gemini-3.7-flash — and the per-minute ceiling has not been captured that way, so it is a TODO with a command rather than a number.

### 2.3 - Denominated in quota, not dollars
`days/day-24-token-accounting-and-budgets/parts/02-two-ceilings/2.3-denominated-in-quota-not-dollars.md` · level `working` · ids OPS-07, AG-11

A budget in money assumes you can buy more, and on a free tier you cannot — so Sutra's budget is written in requests per minute and per day, per provider, and the interesting consequence is that "spend more" is not an available move, which forces every decision to be about which provider and whether at all.

### 3.1 - The ledger, with the clock as a parameter
`days/day-24-token-accounting-and-budgets/parts/03-counting-before-spending/3.1-the-ledger.md` · level `working` · ids OPS-07

The whole budget is a list of timestamps and two windows over it — and now is an argument on every method, never read from the system clock, which is what makes a ceiling that only bites after twenty-four hours testable in six milliseconds.

### 3.2 - Refusing before the call, not after
`days/day-24-token-accounting-and-budgets/parts/03-counting-before-spending/3.2-refusing-before-the-call.md` · level `working` · ids OPS-07

Twenty-five attempts against a ceiling of twenty: checking the ledger first refuses five locally and leaves the ledger reading 20 of 20, while letting the provider decide makes five real round trips and leaves the ledger reading 25 of 20 — five requests spent to be told no.

### 3.3 - Testing a ceiling that only bites at midnight
`days/day-24-token-accounting-and-budgets/parts/03-counting-before-spending/3.3-testing-a-ceiling-that-bites-at-midnight.md` · level `production` · ids OPS-07

Eight assertions cover a per-minute window, a per-day window, both of them clearing, and the ordering between them — and they run in 0.06 seconds with no key, no network and no sleeping, because every now is a number the test chose.

### 4.1 - 💥 The retry that spent the budget
`days/day-24-token-accounting-and-budgets/parts/04-failure-lab/4.1-the-retry-that-spent-the-budget.md` · level `production` · ids OPS-07

One question arriving after the day's allowance is gone costs 1 request when the policy reads the quotaId and 3 when it does not — and the three-attempt version is the same code that makes a system reliable against a per-minute ceiling, which is why the bug looks like good engineering.

### 4.2 - 💥 The counter that counted the wrong thing
`days/day-24-token-accounting-and-budgets/parts/04-failure-lab/4.2-the-counter-that-counted-the-wrong-thing.md` · level `production` · ids OPS-07

Counting answered questions instead of attempted requests made a day of twelve questions look like 11 requests used when the provider had counted 16 — so the system believed 9 remained when 4 did, and the ceiling arrived five requests before anybody expected it.

### 5.1 - Whose budget is it?
`days/day-24-token-accounting-and-budgets/parts/05-in-production/5.1-whose-budget-is-it.md` · level `production` · ids OPS-07

One project ceiling of twenty, three engineers, and one of them triaging a backlog: sharing it served 20 of 22 arrivals but refused the two light users four times, while giving each a sixth of it refused nobody except the heavy user — and served only 14. Neither is free; the question is which failure you would rather explain.

### 5.2 - Degrading, not failing
`days/day-24-token-accounting-and-budgets/parts/05-in-production/5.2-degrading-not-failing.md` · level `production` · ids OPS-07, AG-11

With the allowance gone there are three things the desk can say, and the run shows all three: a RuntimeError that helps nobody, a degraded answer from the handbook that says where it came from, and an ok answer marked source: model that came from a lookup table and is a lie.

## Papers - read after the parts

### doi:10.1109/MCOM.1986.1092946 - New directions in communications — the leaky bucket
`days/day-24-token-accounting-and-budgets/papers/01-the-leaky-bucket.md`

Buried in a broad 1986 article about what the coming broadband network should look like is a small mechanism for policing how fast a sender may send — a bucket that fills at a fixed rate and refuses anything it cannot pay for — and that mechanism, not the network architecture around it, is what every API rate limiter in use today descends from.

