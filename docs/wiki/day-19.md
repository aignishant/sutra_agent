# Day 19 - Context engineering I — what earns a place in the window

IDs closed: AG-08, AG-09 · source: `days/day-19-context-engineering-selection/`

## Parts

### 1.1 - Room is not free
`days/day-19-context-engineering-selection/parts/01-the-binder/1.1-room-is-not-free.md` · level `foundation` · ids AG-08

A context window is a budget you spend on every call, not a container you fill once — so the question that matters is never "will it fit?" but "what does the model need to answer this step?".

### 1.2 - Three costs in one scene
`days/day-19-context-engineering-selection/parts/01-the-binder/1.2-three-costs-in-one-scene.md` · level `working` · ids AG-08

Every token you add is billed on every call, delays the first word of the answer, and competes for the model's attention — and only the first of those three has a number you can look up.

### 1.3 - The organ that grows by itself
`days/day-19-context-engineering-selection/parts/01-the-binder/1.3-the-organ-that-grows-by-itself.md` · level `working` · ids AG-08

Every part of a request is a size you chose, except one: the conversation history grows on its own, gets re-sent in full on every call, and by turn ten costs twenty-one times what turn one cost — measured.

### 2.1 - Opening the envelope
`days/day-19-context-engineering-selection/parts/02-anatomy/2.1-opening-the-envelope.md` · level `working` · ids AG-09

You can read the exact request your agent sends without any provider by putting a recording model in its place — and the first thing the recording shows is that the tool declarations are three and a half times the size of the instruction you spent an afternoon writing.

### 2.2 - Six organs and who packed them
`days/day-19-context-engineering-selection/parts/02-anatomy/2.2-six-organs-and-who-packed-them.md` · level `working` · ids AG-09

A request has six recognisable parts, and the useful question about each is not what is it but who put it there — because that tells you which dial you are allowed to turn.

### 2.3 - The menu costs more than the handbook
`days/day-19-context-engineering-selection/parts/02-anatomy/2.3-the-menu-costs-more-than-the-handbook.md` · level `working` · ids AG-09

Each tool on an agent's list costs a few hundred characters of declaration on every call — six small tools measured at 1,855 characters, against an instruction of 145 — and it costs the model a decision as well.

### 2.4 - A subscription, not a purchase
`days/day-19-context-engineering-selection/parts/02-anatomy/2.4-a-subscription-not-a-purchase.md` · level `working` · ids AG-09

The system instruction is sent again on every single call, unchanged, for the life of the agent — so every sentence in it is a standing charge, and the test for whether a sentence belongs there is whether it would be true on a call you have not thought of yet.

### 3.1 - A rule for each organ
`days/day-19-context-engineering-selection/parts/03-selection/3.1-a-rule-for-each-organ.md` · level `working` · ids AG-09

Six organs, six different selection rules — and the reason there is not one rule is that each organ has a different owner, a different growth behaviour and a different way of going wrong.

### 3.2 - Facts, not blobs
`days/day-19-context-engineering-selection/parts/03-selection/3.2-facts-not-blobs.md` · level `working` · ids AG-09

Send the finding, not the evidence: a sixty-line log distilled to its two interesting lines is twenty-seven times smaller, and the model answers the question either way — but only one of those versions still fits in a conversation.

### 3.3 - Position is not presence
`days/day-19-context-engineering-selection/parts/03-selection/3.3-position-is-not-presence.md` · level `production` · ids AG-09

A fact in the window is not a fact the model will use: where it sits changes how reliably it is found, and its position is not something you chose — it drifts as the conversation grows, from the end, through the middle, towards the beginning.

### 4.1 - A scale for prompts
`days/day-19-context-engineering-selection/parts/04-measuring/4.1-a-scale-for-prompts.md` · level `working` · ids AG-08

Characters are free to measure and good enough for ratios; tokens are what the provider counts and cost one API call that generates nothing — so Sutra weighs in characters continuously and converts to tokens when a number has to be exact.

### 4.2 - Curated against kitchen sink
`days/day-19-context-engineering-selection/parts/04-measuring/4.2-curated-against-kitchen-sink.md` · level `production` · ids AG-08

The same question, packed two ways: 45 tokens against 6,220 — and the expensive version contains no fact the cheap one lacks, which is what makes the comparison an argument rather than a trade-off.

### 5.1 - 💥 In state, and not in the window
`days/day-19-context-engineering-selection/parts/05-failure-lab/5.1-in-state-and-not-in-the-window.md` · level `production` · ids AG-09

A fact written to session state is in your code's memory and not in the model's: unless a placeholder names it or a tool returns it, it is absent from the request — measured, with no error and no warning anywhere.

### 6.1 - Testing what goes in the window
`days/day-19-context-engineering-selection/parts/06-in-production/6.1-testing-what-goes-in-the-window.md` · level `production` · ids AG-08, AG-09

Prompts are testable: a recording model plus a scale gives you seven assertions about size, growth and presence that run in a second with no key — and writing them exposed two of them as too weak, which is the part worth copying.

### 6.2 - A budget per organ
`days/day-19-context-engineering-selection/parts/06-in-production/6.2-a-budget-per-organ.md` · level `production` · ids AG-08

One total tells you something is wrong and nothing about whose it is: a limit per organ turns prompt growth into a failing test that names the owner, and it is the shape Day 24 will fill with quota.

### 6.3 - The heaviest organ
`days/day-19-context-engineering-selection/parts/06-in-production/6.3-the-heaviest-organ.md` · level `production` · ids AG-08

Five organs are fixed by decisions you can make today; the sixth grows on its own and cannot be fixed by choosing better — which is why tomorrow is a whole day about replacing what happened with a shorter true account of it.

## Papers - read after the parts

### arXiv:2307.03172 - Lost in the Middle: How Language Models Use Long Contexts
`days/day-19-context-engineering-selection/papers/01-lost-in-the-middle.md`

It measured what happens when the position of the relevant information inside a long context is moved, and found performance highest at the beginning and the end and significantly degraded in the middle — even for models built for long contexts.

