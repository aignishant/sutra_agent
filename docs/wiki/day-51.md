# Day 51 - Caching — context & response caching as the quota lifeline

IDs closed: ADK-31, OPS-10 · source: `days/day-51-caching-the-quota-lifeline/`

## Parts

### 1.1 - The same sentence, paid for twice
`days/day-51-caching-the-quota-lifeline/parts/01-two-caches-two-currencies/1.1-the-same-sentence-paid-for-twice.md` · level `foundation` · ids ADK-31, OPS-10

Every request the desk sends carries 6,124 characters of instruction, tool schemas and history that were byte-for-byte identical last time, and caching is the practice of not paying for those characters again.

### 1.2 - Two caches wearing one name
`days/day-51-caching-the-quota-lifeline/parts/01-two-caches-two-currencies/1.2-two-caches-wearing-one-name.md` · level `foundation` · ids ADK-31, OPS-10

"Caching" names two different mechanisms that save two different currencies — a context cache saves characters inside a request you still send, and a response cache saves the request entirely — and confusing them is why teams report a saving their quota page does not show.

### 1.3 - A key is a promise about sameness
`days/day-51-caching-the-quota-lifeline/parts/01-two-caches-two-currencies/1.3-a-key-is-a-promise-about-sameness.md` · level `working` · ids ADK-31, OPS-10

A cache key is not an identifier for a stored thing; it is a claim that any two lookups producing the same key deserve the same answer, and every serious caching bug is that claim turning out to be false.

### 2.1 - What ADK is willing to cache
`days/day-51-caching-the-quota-lifeline/parts/02-the-context-cache/2.1-what-adk-is-willing-to-cache.md` · level `working` · ids ADK-31

ADK caches everything in the conversation before the last unbroken run of user messages, which means the cacheable prefix ends wherever the newest question begins — and on the very first turn that boundary is at zero, so there is nothing to cache at all.

### 2.2 - What a hit does to the request
`days/day-51-caching-the-quota-lifeline/parts/02-the-context-cache/2.2-what-a-hit-does-to-the-request.md` · level `working` · ids ADK-31

A context-cache hit is not a discount applied to your bill — ADK physically deletes the system instruction, the tools and the cached contents from the outgoing request and puts a single resource name in their place, so the desk's request goes from 6,124 characters to 39.

### 2.3 - The fingerprint is the key
`days/day-51-caching-the-quota-lifeline/parts/02-the-context-cache/2.3-the-fingerprint-is-the-key.md` · level `working` · ids ADK-31

ADK decides whether a cached prefix still applies by hashing the model, the system instruction, the tools, the tool config and the first N contents into sixteen hex characters — so one trailing space in the instruction abandons the cache, while reversing the whole tool list does not.

### 2.4 - The three ways a cache dies
`days/day-51-caching-the-quota-lifeline/parts/02-the-context-cache/2.4-the-three-ways-a-cache-dies.md` · level `working` · ids ADK-31, OPS-10

ADK abandons a cache for exactly three reasons — the TTL passed, the reuse count passed cache_intervals, or the fingerprint moved — and whichever limit is tightest is the only one you are actually tuning, which is why the desk's default settings die 18 times from reuse and 0 times from expiry.

### 3.1 - Two floors and a first-turn rule
`days/day-51-caching-the-quota-lifeline/parts/03-the-floor-we-never-reach/3.1-two-floors-and-a-first-turn-rule.md` · level `working` · ids ADK-31

Before a context cache can be created, three gates must open in order — a previous token count must exist, the prefix must clear your min_tokens, and it must clear Gemini's own floor of 4,096 tokens on a gemini-3 model — and each refusal writes a different log line that says exactly which one bit.

### 3.2 - 💥 Thirty-seven per cent of the way to a cache
`days/day-51-caching-the-quota-lifeline/parts/03-the-floor-we-never-reach/3.2-thirty-seven-per-cent-of-the-way-to-a-cache.md` · level `production` · ids ADK-31, OPS-10

Sutra's desk cannot use ADK's context caching at all — its cacheable prefix is 1,521 estimated tokens against a 4,096-token floor, which is 37.1% of the way there — and the correct engineering response is to write that number down rather than to configure around it.

### 3.3 - What would have to change
`days/day-51-caching-the-quota-lifeline/parts/03-the-floor-we-never-reach/3.3-what-would-have-to-change.md` · level `production` · ids ADK-31

There is exactly one change to Sutra that clears the 4,096-token floor honestly — putting the whole 12,716-character ticket archive in the instruction, which takes the prefix to 4,700 tokens — and it is the same architecture Day 50 identified as a real alternative to retrieval, which turns "enable caching" into a design question rather than a configuration one.

### 4.1 - Where the config goes
`days/day-51-caching-the-quota-lifeline/parts/04-the-adk-config/4.1-where-the-config-goes.md` · level `working` · ids ADK-31

Context caching is configured once on the App, not on each agent — App(context_cache_config= ContextCacheConfig(...)) — and that placement is the 2.x composition model showing through: cross-cutting behaviour is attached to the thing that runs the graph, never to the nodes inside it.

### 4.2 - What the metadata says, and what it does not
`days/day-51-caching-the-quota-lifeline/parts/04-the-adk-config/4.2-what-the-metadata-says.md` · level `working` · ids ADK-31, OPS-10

Every event carries a cache_metadata in one of exactly two states — active, with a cache name and an expiry, or fingerprint-only, with neither — and the second state is the one worth reading, because it is how ADK tells you "I measured your prefix and declined" rather than "caching is off".

### 4.3 - Choosing the three numbers
`days/day-51-caching-the-quota-lifeline/parts/04-the-adk-config/4.3-choosing-the-three-numbers.md` · level `production` · ids ADK-31, OPS-10

cache_intervals, ttl_seconds and min_tokens are chosen by running the traffic against them and reading which one kills the caches, not by picking round numbers — and on the desk's traffic the default cache_intervals=10 is the only one of the three that does anything at all.

### 5.1 - The traffic decides the hit rate
`days/day-51-caching-the-quota-lifeline/parts/05-the-response-cache/5.1-the-traffic-decides-the-hit-rate.md` · level `working` · ids OPS-10

A cache's hit rate is a property of the stream of requests it sees, not of the cache — the desk's 60-ask day contains only 10 distinct questions, so the hit rate stops improving at 83% no matter how large the store gets.

### 5.2 - Scoping the key
`days/day-51-caching-the-quota-lifeline/parts/05-the-response-cache/5.2-scoping-the-key.md` · level `working` · ids OPS-10

Adding a scope to the key — the customer account, the agent, the locale — always costs hit rate, and the only question worth asking is whether the answer genuinely differs across that scope: the tenant costs the desk 25 percentage points and is mandatory, the agent costs a further 21 and buys nothing.

### 5.3 - 💥 The key that dropped the field
`days/day-51-caching-the-quota-lifeline/parts/05-the-response-cache/5.3-the-key-that-dropped-the-field.md` · level `production` · ids OPS-10

A key that throws away information raises the hit rate and starts serving wrong answers at the same time — dropping digits takes the desk from 83% to 85% with one wrong answer, keeping only the first three words takes it to 87% with three — so a rising hit-rate graph is not evidence that anything is working.

### 5.4 - 💥 The answer that was right when it was stored
`days/day-51-caching-the-quota-lifeline/parts/05-the-response-cache/5.4-the-answer-that-was-right-when-it-was-stored.md` · level `production` · ids OPS-10

With entries that never expire, the desk serves 17 cached answers about two topics and five of them are wrong — not because the cache broke, but because the refund policy changed and the stored answer did not, and nothing in the system is capable of noticing.

### 5.5 - A TTL is a bet on how long the world stays still
`days/day-51-caching-the-quota-lifeline/parts/05-the-response-cache/5.5-a-ttl-is-a-bet.md` · level `production` · ids OPS-10

Sweeping the TTL from 60 to 21600 seconds moves the desk from 0 hits and 60 calls to 50 hits and 10 calls, and the stale answers appear at 7200 — so the honest way to choose is to read both columns and say out loud which wrong answers you are buying.

### 6.1 - The saving, in the unit of the bill
`days/day-51-caching-the-quota-lifeline/parts/06-proving-the-saving/6.1-the-saving-in-the-unit-of-the-bill.md` · level `production` · ids OPS-10

A caching report has to be denominated in whatever the provider actually rations — for Sutra that is requests per day, so the honest sentence is "6,085 of 6,124 characters and zero of 120 requests from the context cache; 54 of 120 requests from the response cache", and any single-number version of it is misleading.

### 6.2 - The log line and four alarms
`days/day-51-caching-the-quota-lifeline/parts/06-proving-the-saving/6.2-the-log-line-and-four-alarms.md` · level `production` · ids OPS-10

Five fields on every cache lookup — decision, key_recipe, age_s, saved_calls, reason — make four alarms computable, and age_s is the one everybody omits and the only one that can see a stale answer.

### 6.3 - 💥 The stampede on a cold key
`days/day-51-caching-the-quota-lifeline/parts/06-proving-the-saving/6.3-the-stampede-on-a-cold-key.md` · level `production` · ids OPS-10

An entry is written when the answer comes back, not when the question is asked, so six agents asking one new question inside that gap produce six model calls for one answer — 30% of the desk's daily free tier spent on a single question, which one claim-the-key lock reduces to 5%.

### 7.1 - What must never enter a key
`days/day-51-caching-the-quota-lifeline/parts/07-in-production/7.1-what-must-never-enter-a-key.md` · level `production` · ids OPS-10

A cache key is written to logs, to metrics labels and to a shared store, so it is a published string — customer text and credentials must be hashed out of it, the tenant must stay in it in readable form, and the timing of a hit leaks whether a question has been asked before.

### 7.2 - 🅿️ Eviction, shared stores and semantic caching
`days/day-51-caching-the-quota-lifeline/parts/07-in-production/7.2-eviction-shared-stores-and-semantic-caching.md` · level `production` · ids OPS-10

Three things a real deployment adds to today's cache — an eviction policy, a store shared across processes, and similarity matching on the key — are deliberately not built here, and each has one number that would tell you when to build it.

## Papers - read after the parts

### doi:10.1147/sj.92.0078 - Evaluation techniques for storage hierarchies
`days/day-51-caching-the-quota-lifeline/papers/01-storage-hierarchies.md`

For a replacement policy with the inclusion property — what a cache of size C holds is always a subset of what a cache of size C+1 holds, and least-recently-used has it — the hit rate at every cache size can be read off a single pass over the reference stream, because the answer was always a property of the stream and not of the cache.

