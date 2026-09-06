# Day 72 - Backoff with honesty — retry-after, 1→2→4→8s, escalate after N; never invent a result

IDs closed: SEC-15, OPS-13 · source: `days/day-72-backoff-with-honesty/`

## Parts

### 1.1 - Why doubling
`days/day-72-backoff-with-honesty/parts/01-the-ladder/1.1-why-doubling.md` · level `foundation` · ids SEC-15, OPS-13

Doubling the wait between attempts is not politeness towards a busy server — it is a search for an instant you cannot see, where each rung probes twice as far into the future as the one before it, so a handful of attempts covers a long stretch of time while still answering quickly if the window opens soon.

### 1.2 - The ladder measured
`days/day-72-backoff-with-honesty/parts/01-the-ladder/1.2-the-ladder-measured.md` · level `working` · ids SEC-15, OPS-13

Given the same six attempts, the ladder succeeds where retrying every second gives up — not because doubling is gentler, but because it reaches t=15s while flat retry reaches t=5s, and the window opened at ten.

### 1.3 - The last rung
`days/day-72-backoff-with-honesty/parts/01-the-ladder/1.3-the-last-rung.md` · level `working` · ids SEC-15, OPS-13

A ladder needs two limits that nothing computes for you — how many attempts and how long a single wait may get — because uncapped doubling reaches over eight minutes by the tenth rung, and an uncapped attempt count never escalates at all.

### 2.1 - retry-after beats your ladder
`days/day-72-backoff-with-honesty/parts/02-the-number-the-server-gave-you/2.1-retry-after-beats-your-ladder.md` · level `working` · ids SEC-15, OPS-13

Against the identical provider, honouring the server's own number finishes in 2 attempts with 1 wasted request, while ignoring it and running the ladder instead gives up after 6 attempts and 6 wasted requests — because your ladder is a guess at a number the server already told you.

### 2.2 - When it is absent
`days/day-72-backoff-with-honesty/parts/02-the-number-the-server-gave-you/2.2-when-it-is-absent.md` · level `working` · ids SEC-15, OPS-13

Not every refusal carries the number, and when it does not the ladder is all you have — the same provider, the same window at t=37s, and without the header the client gives up after 6 attempts and 6 wasted requests, exactly as if it had ignored one.

### 2.3 - Zero is not absent
`days/day-72-backoff-with-honesty/parts/02-the-number-the-server-gave-you/2.3-zero-is-not-absent.md` · level `production` · ids SEC-15, OPS-13

retry_after=0.0 means come back now and retry_after=None means the server said nothing, and one character decides whether your code can tell them apart: refusal.retry_after or ladder_wait(1) turns a stated zero into a one-second wait, while is not None keeps it at zero.

### 3.1 - Escalate, never invent
`days/day-72-backoff-with-honesty/parts/03-after-the-last-retry/3.1-escalate-never-invent.md` · level `production` · ids SEC-15, OPS-13

Every retry loop has a line after it, and there are exactly two things that line can do — raise, or return something shaped like an answer — and only the first is allowed: honest.py exits 0 when it refuses to answer and 1 when it hands back 'no incidents reported' from a default nobody measured.

### 3.2 - Which calls are safe to retry
`days/day-72-backoff-with-honesty/parts/03-after-the-last-retry/3.2-which-calls-are-safe-to-retry.md` · level `production` · ids SEC-15, OPS-13

A refusal and a timeout are not two flavours of the same failure: a 429 means the request was never performed, so retrying it is free, while a timeout means you do not know, and the same retry loop that credits a card once after a refusal credits it twice after a lost acknowledgement.

### 4.1 - The herd
`days/day-72-backoff-with-honesty/parts/04-everyone-at-once/4.1-the-herd.md` · level `production` · ids SEC-15, OPS-13

Backoff spreads one client out in time and does nothing to spread clients out from each other: forty clients running the identical ladder from the identical start land at 6 distinct instants, with all forty arriving together at each one.

### 4.2 - One multiplication
`days/day-72-backoff-with-honesty/parts/04-everyone-at-once/4.2-one-multiplication.md` · level `production` · ids SEC-15, OPS-13

Multiplying each wait by a random factor takes the fleet from 6 distinct instants to 123 and the biggest retry burst from 40 requests to 7 — and leaves the first burst at 40 in both runs, because jitter delays a retry and nothing delays a first attempt.

### 5.1 - The plugin that asks the model
`days/day-72-backoff-with-honesty/parts/05-in-production/5.1-the-plugin-that-asks-the-model.md` · level `production` · ids SEC-15, OPS-13

ADK ships a retry plugin, ReflectAndRetryToolPlugin, and it is a well-made mechanism pointed at a different failure than this day's: it hands a tool's error back to the model so the model can call the tool differently, which is exactly right when the call was wrong and exactly wrong for a 429, where the call was fine and the window was shut — 4 model calls against 1, for a refusal no rephrasing could fix.

### 5.2 - What to alert on
`days/day-72-backoff-with-honesty/parts/05-in-production/5.2-what-to-alert-on.md` · level `production` · ids SEC-15, OPS-13

A retry that works reports no error at all, so the error rate is the one number guaranteed to stay flat while the system degrades — the signals are the escalation rate and the wasted-request count, and this day's own successful run wasted 4 requests to produce one answer.

## Papers - read after the parts

### doi:10.1145/360248.360253 - Ethernet: distributed packet switching for local computer networks
`days/day-72-backoff-with-honesty/papers/01-binary-exponential-backoff.md`

The idea this day is built on is not "wait longer each time" — it is draw the wait at random from a range that doubles after each collision, and the randomness is not an improvement somebody added later: switching the widening off in the demo below takes sixteen senders from 16 of 16 delivered on 95 attempts to 0 of 16 on 4,269 attempts.

