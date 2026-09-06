# Day 70 - The Quota-Router plugin — requests-remaining per provider per window; route to headroom

IDs closed: OPS-12, ADK-49 · source: `days/day-70-the-quota-router/`

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

A router that compares lanes on their minute window alone spends the scarcest daily allowance in the fleet first: routing 300 reasoning calls by minute headroom empties OpenRouter's whole day by t=244s and drops 78 requests, while the same run judged on both windows drops 75.

### 1.5 - Twelve left means two different things
`days/day-70-the-quota-router/parts/01-what-headroom-is/1.5-twelve-left-means-two-different-things.md` · level `working` · ids OPS-12

Comparing lanes by requests remaining is comparing numbers that are not in the same unit; comparing each lane's remaining share of its own ceiling serves 233 of 300 calls against 222, and keeps the scarce lane alive to t=380s instead of t=244s.

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

### 3.1 - Where a router has to stand
`days/day-70-the-quota-router/parts/03-the-plugin/3.1-where-a-router-has-to-stand.md` · level `foundation` · ids OPS-12, ADK-49

A scheduler can only schedule what it can see, so the router cannot live in an agent's configuration — chosen once, before any request exists — and cannot live in one agent's own callback, which is local to that agent: it has to be a plugin registered on the Runner, which is the one place in ADK that sees every model call a run makes.

### 3.2 - Observe, block, answer instead
`days/day-70-the-quota-router/parts/03-the-plugin/3.2-observe-block-answer-instead.md` · level `working` · ids OPS-12, ADK-49

before_model_callback has exactly three outcomes — return None and the call happens, edit the request and the edited version goes, return an LlmResponse and the model call never happens — and a router is built entirely on the third, because answering instead is how the plugin gets to choose which lane did the work.

### 3.3 - The field that does not reroute
`days/day-70-the-quota-router/parts/03-the-plugin/3.3-the-field-that-does-not-reroute.md` · level `production` · ids OPS-12, ADK-49

llm_request.model looks like the field that picks the provider, so rewriting it in a plugin looks like a two-line router — and it is not one: the model object was bound to the agent before the request existed, the field is data that object receives, and changing it changes what the model is told rather than which model is asked.

### 3.4 - Answering instead of the agent
`days/day-70-the-quota-router/parts/03-the-plugin/3.4-answering-instead-of-the-agent.md` · level `production` · ids OPS-12, ADK-49

Twenty-four tickets through a real InMemoryRunner, with one BasePlugin registered on it, spread across four lanes as {'gemini': 4, 'groq': 9, 'openrouter': 11, 'ollama': 0} and the agent's own model running zero times — while the same twenty-four tickets with the plugin removed all go to one lane whose ceiling is ten a minute.

### 4.1 - Reading the refusal
`days/day-70-the-quota-router/parts/04-when-a-lane-says-no/4.1-reading-the-refusal.md` · level `working` · ids OPS-12

A 429 is not an error, it is an instruction with a time in it, and the retry-after it carries is worth more than every counter the router keeps — because it is the provider's own statement about its own window, and the counters are only the router's estimate of it.

### 4.2 - A cold lane, not a broken one
`days/day-70-the-quota-router/parts/04-when-a-lane-says-no/4.2-a-cold-lane-not-a-broken-one.md` · level `production` · ids OPS-12

A refused lane is a lane with a time on it, so the router marks it cold, stops sending, and probes back when the time elapses — and the proof is that honouring the refusal serves 10 requests and ignoring it serves 10, so the twenty-nine extra attempts bought nothing at all.

### 4.3 - Every lane dry
`days/day-70-the-quota-router/parts/04-when-a-lane-says-no/4.3-every-lane-dry.md` · level `production` · ids OPS-12

When no lane can serve the request the router raises — and it raises with a number, soonest headroom in 60s, which is the field that turns an exception into an instruction the caller can act on instead of a sentence it can only log.

### 4.4 - The part that will do
`days/day-70-the-quota-router/parts/04-when-a-lane-says-no/4.4-the-part-that-will-do.md` · level `production` · ids OPS-12

Degrading to a lane that cannot do the job is worse than refusing, and the reason is not the quality of the answer — it is the silence: the caller receives an answer and no error at all, and nothing anywhere records that it came from a lane that cannot reason.

### 5.1 - The tally that counts only sales
`days/day-70-the-quota-router/parts/05-failure-lab/5.1-the-tally-that-counts-only-sales.md` · level `production` · ids OPS-12

A router that decrements its headroom inside the success branch is counting a different event from the one the provider counts, and the measurement is brutal: sixty requests reach a limit of thirty, thirty of them come back refused, and the router's own tally says it has used twenty.

### 5.2 - The counter that starts full
`days/day-70-the-quota-router/parts/05-failure-lab/5.2-the-counter-that-starts-full.md` · level `production` · ids OPS-12

The router's headroom lives in the process and the provider's window does not, so a restart twenty seconds into a minute hands the router thirty units of headroom when the provider has ten, and the router spends the difference confidently.

### 5.3 - Two cards, one household
`days/day-70-the-quota-router/parts/05-failure-lab/5.3-two-cards-one-household.md` · level `production` · ids OPS-12

A free tier meters per project, organization or account and not per model string, so pointing the classifier at one model and the drafter at another does not buy a second allowance — and a router keyed on the model name sends twenty requests into a limit of ten, holds nothing back, and believes both of its meters.

### 6.1 - One till, two cashiers
`days/day-70-the-quota-router/parts/06-in-production/6.1-one-till-two-cashiers.md` · level `production` · ids OPS-12

Run the router in two workers and each one stays comfortably inside the limit it can see — 13 and 13 against a ceiling of 20 — while the provider counts the sum and refuses the last six, because the allowance is shared and the counters are not.

### 6.2 - The gauge shows what is left
`days/day-70-the-quota-router/parts/06-in-production/6.2-the-gauge-shows-what-is-left.md` · level `production` · ids OPS-12

Every counter in this day measures requests sent, and the number worth putting on a wall is the one nobody computes: what remains, per lane, per window, as a percentage — because 12 left and 42 left on the same lane are 60% of a minute that refills and 84% of a day that does not.

### 6.3 - What a real quota system adds
`days/day-70-the-quota-router/parts/06-in-production/6.3-what-a-real-quota-system-adds.md` · level `production` · ids OPS-12

The router this day builds is a client-side estimator, and everything a real quota system has that it does not — token buckets, admission control, priority, fairness between callers, a shared authoritative counter — exists because the thing being protected changes from your own allowance to somebody else's service.

## Papers - read after the parts

### doi:10.1109/71.963420 - The power of two choices in randomized load balancing
`days/day-70-the-quota-router/papers/01-the-power-of-two-choices.md`

Spreading work over several servers had two settled options — choose blindly and watch one server end up badly overloaded, or ask every server how loaded it is and pay more for the asking than the work is worth — and this is the document that established that asking two buys almost everything asking all of them would have bought, while asking three buys almost nothing more.

