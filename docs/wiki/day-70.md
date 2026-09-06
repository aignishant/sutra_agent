# Day 70 - day-70-the-quota-router

IDs closed: OPS-12 · source: `days/day-70-the-quota-router/`

## Parts

### 1.1 - A ceiling is a window, not a number
`days/day-70-the-quota-router/parts/01-what-headroom-is/1.1-a-ceiling-is-a-window-not-a-number.md` · level `foundation` · ids OPS-12

"Ten requests per minute" is not a quantity you own, it is a shape: a limit paired with a span of time, and every question about whether you may send now is really a question about which span you are asking over.

### 1.2 - The burst every counter approved
`days/day-70-the-quota-router/parts/01-what-headroom-is/1.2-the-burst-every-counter-approved.md` · level `working` · ids OPS-12

The obvious per-minute counter — an integer and the time the current minute started — allows twenty requests through a limit of ten, and refuses none of them, because it enforces a rule about calendar minutes rather than about any sixty seconds.

### 1.3 - The counter that remembers when
`days/day-70-the-quota-router/parts/01-what-headroom-is/1.3-the-counter-that-remembers-when.md` · level `working` · ids OPS-12

Storing the time of each request instead of a running total turns the boundary burst from twenty requests into ten, because a limiter that knows when things happened can answer questions about any span rather than only about the span it happens to be in.

### 1.4 - Two windows, and the one that bites last
`days/day-70-the-quota-router/parts/01-what-headroom-is/1.4-two-windows-and-the-one-that-bites-last.md` · level `working` · ids OPS-12

A router that compares lanes on their minute window alone spends the scarcest daily allowance in the fleet first: routing 300 reasoning calls by minute headroom empties OpenRouter's whole day in 4.1 minutes and drops 78 requests, while the same run judged on both windows drops 75.

### 1.5 - Twelve left means two different things
`days/day-70-the-quota-router/parts/01-what-headroom-is/1.5-twelve-left-means-two-different-things.md` · level `working` · ids OPS-12

Comparing lanes by requests remaining is comparing numbers that are not in the same unit; comparing each lane's remaining share of its own ceiling serves 233 of 300 calls against 222, and keeps the scarce lane alive for 6.3 minutes instead of 4.1.

### 2.1 - Headroom is not a preference
`days/day-70-the-quota-router/parts/02-choosing-a-lane/2.1-headroom-is-not-a-preference.md` · level `foundation` · ids OPS-12

Routing is a scheduling decision over a resource that runs out and refills on a clock, not a choice about which model you like best — and the moment you write it as a preference you have built something that cannot survive its own busiest hour.

### 2.2 - The lane that cannot do the job
`days/day-70-the-quota-router/parts/02-choosing-a-lane/2.2-the-lane-that-cannot-do-the-job.md` · level `working` · ids OPS-12

A quota router is not a load balancer, because its servers are not interchangeable: the same fleet offers four lanes for classification and only two for reasoning, so capability filters the set before headroom ranks it.

### 2.3 - With perfect information, greedy is fine
`days/day-70-the-quota-router/parts/02-choosing-a-lane/2.3-with-perfect-information-greedy-is-fine.md` · level `working` · ids OPS-12

Measured over 270 requests by a single decider with live counters, the crude "first capable lane" policy serves 258 and the clever headroom-sampling one serves 251 — so the sophistication this day is building buys nothing at all until the information stops being perfect.

### 2.4 - Everyone read the same board
`days/day-70-the-quota-router/parts/02-choosing-a-lane/2.4-everyone-read-the-same-board.md` · level `production` · ids OPS-12

When fourteen workers decide from one snapshot, sampling two lanes and keeping the emptier spills zero requests while taking the single best lane spills one and the crude policies spill two and three — and outside a narrow band of load, none of it matters.

