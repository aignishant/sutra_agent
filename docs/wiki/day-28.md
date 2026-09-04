# Day 28 - Progressive disclosure & skill design

IDs closed: SK-09, SK-10, SK-11 · source: `days/day-28-progressive-disclosure-design/`

## Parts

### 1.1 - Five rungs, five frequencies
`days/day-28-progressive-disclosure-design/parts/01-the-price-list/1.1-five-rungs-five-frequencies.md` · level `foundation` · ids SK-09

Progressive disclosure is not a loading order, it is five budgets paid at five different frequencies — and the whole of skill design is deciding which frequency a piece of knowledge should be paid at.

### 1.2 - Pricing your own shelf
`days/day-28-progressive-disclosure-design/parts/01-the-price-list/1.2-pricing-your-own-shelf.md` · level `working` · ids SK-09

One script prints every rung of every skill you own — card, body, references — and the whole point of running it is that the numbers are never the ones you guessed.

### 1.3 - Weight flows down the ladder — but only as far as the frequency justifies
`days/day-28-progressive-disclosure-design/parts/01-the-price-list/1.3-weight-flows-down.md` · level `working` · ids SK-09

Three questions decide which rung a piece of knowledge belongs on — how often is it needed, does it change what happens at a step, and will it grow — and the answers are read in that order, because the first one can veto the other two.

### 1.4 - Moving the example, and moving it back
`days/day-28-progressive-disclosure-design/parts/01-the-price-list/1.4-moving-the-example.md` · level `production` · ids SK-09

Moving ticket-triage's worked example into references/ saves 181 tokens per activation and costs one model round trip on most triages — so the measurement says do it and the frequency says do not, and the right answer is to make the change, look at both numbers, and revert it.

### 2.1 - A description is a row in a routing table
`days/day-28-progressive-disclosure-design/parts/02-descriptions-as-routing/2.1-a-description-is-a-routing-row.md` · level `working` · ids SK-10

With one skill a description only has to match; with twenty it has to beat the other nineteen — so past a handful of skills a description stops being a summary and becomes a routing rule, and it is graded against its neighbours rather than on its own.

### 2.2 - Coverage, orthogonality, specificity
`days/day-28-progressive-disclosure-design/parts/02-descriptions-as-routing/2.2-coverage-orthogonality-specificity.md` · level `working` · ids SK-10

A shelf is audited on three properties — every expected request matches something, no request matches two things equally, and each description says the specific thing rather than the general one — and only the first is about whether a skill exists.

### 2.3 - Measuring routing without a model
`days/day-28-progressive-disclosure-design/parts/02-descriptions-as-routing/2.3-measuring-routing-without-a-model.md` · level `working` · ids SK-10

A word-overlap scorer is not what the model does, and it is a good enough proxy for the one thing that matters — the margin between the best skill and the second — because a shelf whose descriptions collide on words collides on meaning too.

### 2.4 - The crowded shelf
`days/day-28-progressive-disclosure-design/parts/02-descriptions-as-routing/2.4-the-crowded-shelf.md` · level `production` · ids SK-10

Four vague skills added beside two good ones do not compete for the requests they describe — they narrow every margin on the shelf, taking five requests from margin 2 to margin 1 and one from 1 to 0, without a word of the good descriptions changing.

### 3.1 - Four containers, one property
`days/day-28-progressive-disclosure-design/parts/03-four-containers/3.1-four-containers-one-property.md` · level `foundation` · ids SK-11

Anything Sutra should know or do goes into exactly one of four containers — a tool, a skill, a persona line, or a reference file — and which one is decided by a property of the thing itself, not by which container you happen to be building this week.

### 3.2 - The two boundary cases
`days/day-28-progressive-disclosure-design/parts/03-four-containers/3.2-the-two-boundary-cases.md` · level `working` · ids SK-11

Two things look like skills and are not: a procedure that must run on every call, which belongs in the instruction or in a callback because a skill loads on a decision — and knowledge with no steps at all, which is data and belongs behind a tool.

### 3.3 - What a misfiling costs
`days/day-28-progressive-disclosure-design/parts/03-four-containers/3.3-what-a-misfiling-costs.md` · level `production` · ids SK-11

Each of the five common misfilings is paid in a different currency — two in tokens, one in generations, and three in wrong answers that no meter reads — so a placement argument settled on token counts alone has settled the two cheapest cases and ignored the three expensive ones.

### 4.1 - Three axes, one change
`days/day-28-progressive-disclosure-design/parts/04-the-three-axes/4.1-three-axes-one-change.md` · level `working` · ids SK-09, SK-10, SK-11

Every change to a shelf moves three numbers at once — what it costs, how well it routes, and whether each thing is in the right container — and the move that improves any one of them in isolation is usually the move that damages the other two.

### 4.2 - Refactoring the overloaded skill
`days/day-28-progressive-disclosure-design/parts/04-the-three-axes/4.2-refactoring-the-overloaded-skill.md` · level `production` · ids SK-09, SK-10, SK-11

One support-desk skill holding a procedure, a second procedure, a standing rule and two tables produces routing numbers the gate cannot distinguish from the properly separated shelf — same worst margin, same zero ties, same green exit — while costing twice the tokens and applying its standing rules only on the runs that happened to activate it.

### 4.3 - What the gate cannot check
`days/day-28-progressive-disclosure-design/parts/04-the-three-axes/4.3-what-the-gate-cannot-check.md` · level `production` · ids SK-09, SK-10, SK-11

A script can raise suspects on the placement axis — a body with two step lists, a standing rule, a table, a row of record ids — but it can never issue the verdict, because whether something is an action, a procedure, a standing value or data is a fact about the world and not about the file.

### 5.1 - When the index outgrows listing
`days/day-28-progressive-disclosure-design/parts/05-in-production/5.1-when-the-index-outgrows-listing.md` · level `production` · ids SK-09, SK-10

At around forty skills, listing every description stops working on three fronts at once — the index costs about four thousand tokens, the margins collapse to zero even when every description is individually excellent, and the audit from section 2 starts reporting good news — and the answers are structural: a hierarchy, or search instead of listing.

### 5.2 - Splitting the audience, not the index
`days/day-28-progressive-disclosure-design/parts/05-in-production/5.2-splitting-the-audience.md` · level `production` · ids SK-09, SK-10

🅿️ The third answer to a shelf that has outgrown listing is to stop giving one agent the whole of it — four agents with ten skills each pay a tenth of the index and audit forty-five pairs instead of eight hundred — and it is free only if the agents exist for a reason of their own.

