---
day: 28
phase: 4
phase_name: "Agent Skills"
title: "Progressive disclosure & skill design"
ids: ["SK-09", "SK-10", "SK-11"]
principles: [1, 2, 4, 10, 11, 13, 15, 16, 17, 18]
kind: lab
plan_version: "v2.2.1"
parts: 16
generated: "2026-09-04"
status: written
lab_scaffolded: false
commit: ""
---

# Day 28 — Progressive disclosure & skill design

> **Yesterday (Day 27):** two real skills. Sutra's triage procedure came out of an instruction string, a
> docstring and somebody's head, and became two reviewable folders — and the instruction dropped from 294
> tokens to 157.
> **Today:** the design subject. What those two skills cost at each rung, whether their descriptions can
> be told apart, and whether every piece of them is even in the right container — three questions, three
> instruments, and one shelf that fails all three at once and gets repaired.
> **Tomorrow (Day 29):** skills Sutra did not write. Sourcing and auditing third-party packs, the
> provenance ledger, and the Agent Registry endpoint.

---

## §1 Where we are

The restaurant on the corner has a hundred and twenty things on its menu, and the owner is proud of it.

Three problems, and he would name only the first. Every item on that menu is something he has to be able
to make, so a hundred and twenty items is a fridge full of things that spoil, most of them for dishes
nobody orders twice a month. Second, there are four rice dishes whose descriptions differ by two words,
so the waiter is asked *"what is the difference between these two?"* eleven times a night and gives a
slightly different answer each time. And third — the one nobody has noticed — about fifteen of the items
are not dishes at all. They are side portions, variations of another dish, and two drinks that wandered
into the food section years ago and stayed.

Three different problems, three different fixes, and only one of them is *"write better descriptions"*.

Sutra's shelf has two skills, which is the size at which all of this is easy and none of it is urgent.
That is exactly why today is now: an instrument first run on a broken system cannot be calibrated.

Five things worth knowing before you start.

**Progressive disclosure is five budgets at five frequencies, not a loading order.** Day 26 measured
them: a fixed 479-token preamble on every request, an index when the model asks, a body carried on every
turn after activation, and a reference that costs a whole model round trip to fetch. Design happens on
the frequency column. The advice *"move detail into `references/`"* is correct on a token budget and can
be **wrong** on a request budget, and nothing tells you which you are on except measuring.

**A description stops being a summary and becomes a routing rule.** With one skill it only has to match;
with twenty it has to beat the other nineteen. So the quantity that matters is not a score, it is the
**margin** to the second-best — which means a description can get worse without a word of it changing,
and adding a skill is a change to every skill already there.

**Four containers, chosen by property.** A tool is an action, a skill is a procedure, a persona line is
a standing value, a reference is occasional detail. Two boundary cases decide themselves on frequency
rather than on shape: a procedure that must **always** run is not a skill, because a skill loads on a
decision — and knowledge with **no steps at all** is data, and data lives behind a tool.

**The three axes disagree, and one of them has no command.** Price and routing are scripts. Placement is
a person. The trap is only visible with all three: merging everything into one skill does not make the
routing check fail — it makes it **blind**, because a margin is measured against a second-best that no
longer exists. Today's specimen shelf gets the same worst margin, the same zero ties and the same green
exit as the properly separated one.

**And everything today runs on zero generations.** Set arithmetic, token counting on a separate endpoint,
and four regular expressions. The whole day's budget is in §6 and the number is nought.

---

## §2 The map

Sixteen parts in five sections, and **no paper** — see §8. The day climbs
`foundation → working → production`: section 1 prices the ladder, section 2 audits the descriptions,
section 3 decides where a thing belongs, section 4 is where all three meet and one shelf gets repaired,
and section 5 is what happens when curation stops working.

### Section 1 — `01-the-price-list`: five rungs, five frequencies (SK-09)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [Five rungs, five frequencies](parts/01-the-price-list/1.1-five-rungs-five-frequencies.md) | Which rung multiplies, and which one costs a round trip | `foundation` |
| 1.2 | [Pricing your own shelf](parts/01-the-price-list/1.2-pricing-your-own-shelf.md) | 93, 109, 375, 654, 142 — and the index total | `working` |
| 1.3 | [Weight flows down the ladder](parts/01-the-price-list/1.3-weight-flows-down.md) | Three questions, in an order, and size is the last | `working` |
| 1.4 | [Moving the example, and moving it back](parts/01-the-price-list/1.4-moving-the-example.md) | 28 per cent of a body, 1 per cent of a conversation | `production` |

### Section 2 — `02-descriptions-as-routing`: the shelf is a routing table (SK-10)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [A description is a row in a routing table](parts/02-descriptions-as-routing/2.1-a-description-is-a-routing-row.md) | Margin, not score | `working` |
| 2.2 | [Coverage, orthogonality, specificity](parts/02-descriptions-as-routing/2.2-coverage-orthogonality-specificity.md) | Three properties, three different fixes | `working` |
| 2.3 | [Measuring routing without a model](parts/02-descriptions-as-routing/2.3-measuring-routing-without-a-model.md) | A deterministic proxy and what it cannot see | `working` |
| 2.4 | [💥 The crowded shelf](parts/02-descriptions-as-routing/2.4-the-crowded-shelf.md) | Four decoys, no score changed, every margin down | `production` |

### Section 3 — `03-four-containers`: where a thing belongs (SK-11)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [Four containers, one property](parts/03-four-containers/3.1-four-containers-one-property.md) | Two questions that land on exactly one home | `foundation` |
| 3.2 | [The two boundary cases](parts/03-four-containers/3.2-the-two-boundary-cases.md) | "Always" and "no steps" beat the shape | `working` |
| 3.3 | [What a misfiling costs](parts/03-four-containers/3.3-what-a-misfiling-costs.md) | Three currencies, and only two have a meter | `production` |

### Section 4 — `04-the-three-axes`: where SK-09, SK-10 and SK-11 meet

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [Three axes, one change](parts/04-the-three-axes/4.1-three-axes-one-change.md) | Why a single-axis gate rewards the worst shelf | `working` |
| 4.2 | [💥 Refactoring the overloaded skill](parts/04-the-three-axes/4.2-refactoring-the-overloaded-skill.md) | Four containers in one file, before and after | `production` |
| 4.3 | [What the gate cannot check](parts/04-the-three-axes/4.3-what-the-gate-cannot-check.md) | Suspects, never verdicts | `production` |

### Section 5 — `05-in-production`: when curation stops working

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [When the index outgrows listing](parts/05-in-production/5.1-when-the-index-outgrows-listing.md) | ~4,212 tokens, margin 0, and an audit that lies | `production` |
| 5.2 | [🅿️ Splitting the audience, not the index](parts/05-in-production/5.2-splitting-the-audience.md) | The third answer, and when it is a bad idea | `production` |

**No paper today.** This is a craft day, like Day 27: its material is Sutra's own two skills, the five
rungs Day 26 measured, and arithmetic over both. The one research paper it leans on — *RouteLLM: Learning
to Route LLMs with Preference Data*, `arXiv:2406.18665` — was taught on Day 9 and is cited as an address
from [2.1](parts/02-descriptions-as-routing/2.1-a-description-is-a-routing-row.md). A paper is taught
once in this curriculum.

**Two deliberate failures**, both at `production` level:
[2.4](parts/02-descriptions-as-routing/2.4-the-crowded-shelf.md) crowds the shelf with four plausible
decoys and watches every margin fall, and
[4.2](parts/04-the-three-axes/4.2-refactoring-the-overloaded-skill.md) builds one skill holding four
containers and finds that the routing check cannot tell it apart from the correct shelf.

---

## §3 Setup — run this

**No package is added today.** Nothing is installed and no model string changes;
`git diff pyproject.toml uv.lock` must be empty when you finish.

```bash
# 1 - the day's lab
cd days/day-28-progressive-disclosure-design
mkdir -p lab

# 2 - section 1: the price list
touch lab/price_the_shelf.py

# 3 - section 2: descriptions as routing (route.py first - everything imports it)
touch lab/route.py lab/audit_the_shelf.py lab/routing_gate.py lab/crowd.py

# 4 - section 3: the four containers
touch lab/containers.py lab/boundary_cases.py lab/misfile_cost.py

# 5 - section 4: where the three axes meet
touch lab/overloaded.py lab/refactor.py lab/suspects.py

# 6 - section 5: the shelf that outgrew listing
touch lab/forty_skills.py
cd -

# 7 - confirm the shelf and the dispatch table today's scripts will read
uv run python -c "from sutra.loop import TOOLS, KB; print(sorted(TOOLS), len(KB), 'kb articles')"
uv run python -c "
import pathlib
from google.adk.skills import load_skills_from_dir
for s in sorted(load_skills_from_dir(pathlib.Path('skills')), key=lambda s: s.name):
    print(s.name, sorted(s.resources.list_references()))
"
```

**Step 7 is the gate and it is not ceremony.** On 2026-09-04 the first command printed
`['lookup_ticket', 'search_kb'] 2 kb articles` and the second printed `kb-answer-style []` and
`ticket-triage ['severity-rubric.md']`. Every number in this day is measured against that shelf, so if
yours differs, your numbers will differ and that is fine — what must not happen is reading today's
figures and assuming they are yours.

**Write `route.py` before anything in section 2 or later.** Five of the twelve lab files import it, and
its stopword list decides what every margin in the day means
([2.3](parts/02-descriptions-as-routing/2.3-measuring-routing-without-a-model.md)).

**Nothing moves into `sutra/` today, and that is deliberate.** Day 27 wrote `sutra/desk/skills.py` and
trimmed `sutra/desk/agent.py`; today measures and argues about what is already there. The one change the
day proposes to project code —
[5.2](parts/05-in-production/5.2-splitting-the-audience.md)'s `shelf` parameter on `build_desk` — is
parked, not built, and appears in §4 as a decision to write down rather than a line to type.

**Two things do touch `skills/`, and both are temporary.**
[1.4](parts/01-the-price-list/1.4-moving-the-example.md) moves `ticket-triage`'s worked example into
`references/worked-example.md`, measures, and moves it back — deleting the orphan file afterwards.
[2.3](parts/02-descriptions-as-routing/2.3-measuring-routing-without-a-model.md) and §5 add a sentence to
a description to make the gate go red, and take it out again. `git status` must be clean of both by the
end.

---

## §4 Build brief

**Twelve lab files, in dependency order.** `route.py` first; `overloaded.py` before `refactor.py` and
`suspects.py`; everything else is independent.

| File | What it does | Taught in |
| --- | --- | --- |
| `lab/price_the_shelf.py` | every rung of every skill, with the model's own tokeniser | 1.2 |
| `lab/route.py` | the scorer: `words`, `card`, `rank`, `report`, and `REQUESTS` | 2.3 |
| `lab/audit_the_shelf.py` | coverage, shared filler, specificity | 2.2 |
| `lab/routing_gate.py` | the worst margin, with an exit code | 2.3 |
| `lab/crowd.py` | four decoys beside the two real skills | 2.4 |
| `lab/containers.py` | what Sutra keeps in each of the four containers | 3.1 |
| `lab/boundary_cases.py` | deliveries per day per container, and the live store | 3.2 |
| `lab/misfile_cost.py` | the two priced misfilings, and the three that refuse a number | 3.3 |
| `lab/overloaded.py` | the specimen: one skill holding four containers. Definitions only | 4.2 |
| `lab/refactor.py` | the specimen against the real shelf, same requests | 4.2 |
| `lab/suspects.py` | four container smells, phrased as questions | 4.3 |
| `lab/forty_skills.py` | forty well-scoped skills, and what breaks | 5.1 |

**Two documents, not code**, and they are the part that survives the day:

- `skills/README.md` gains the **four-container table** with Sutra's own files in the fourth column
  ([3.1](parts/03-four-containers/3.1-four-containers-one-property.md)) and the **weight-flows-down rule**
  as a paragraph ([1.3](parts/01-the-price-list/1.3-weight-flows-down.md)).
- The **three-line reading** — price, routing, placement — written down for Sutra's shelf as it stands
  today, so the next change has a baseline to be compared against
  ([4.1](parts/04-the-three-axes/4.1-three-axes-one-change.md)).

**`TODO(me)` markers left for you:**

- **1.1** — redo the five-turn table for a conversation that activates **both** skills, and for one that
  activates nothing at all.
- **1.2** — print each reference individually instead of summing them, and write your guess for all six
  numbers before you run it.
- **1.3** — apply the three questions to each of `kb-answer-style`'s sections and write the verdict and
  the reason for each.
- **1.4** — do the move, re-price, run the preflight so you see the orphan finding **once**, then revert
  and delete the file.
- **2.1** — print your own index and underline the word that decides each of the six requests.
- **2.2** — add two more negative requests and confirm both score zero.
- **2.3** — add `ticket` to `STOP`, count how many margins move at once, and decide whether it should
  stay.
- **2.4** — delete three of the four decoys and find out how much damage the last one does on its own;
  then rewrite one decoy into a real job.
- **3.1** — route the five items at the bottom of the part, saying the **property** out loud for each.
- **3.2** — grep both skill bodies for `never`, `must` and `always`, assign a tier to every hit, and say
  what a callback version of one of them would have to check.
- **3.3** — re-run with `CONVERSATIONS = 12` and `TRIAGES = 10` and say which finding flips; then write
  the three unpriced rows for your own system, answering *who finds out and how*.
- **4.1** — predict all three lines for one change you want to make, **before** making it, and see which
  one you got wrong.
- **4.2** — shorten `DESCRIPTION` to the one-sentence merge and confirm the coverage failure.
- **4.3** — point `review()` at `skills/`, answer every suspect it raises in one line, and decide where
  those answers should live.
- **5.1** — cut `SUBJECTS` down and find the shelf size at which the worst margin first reaches zero, and
  the size at which the shared-filler set first empties. They are not the same number.
- **5.2** — partition the forty subjects into four shelves by **what a person would ask**, then decide
  whether `build_desk` should gain a `shelf` parameter today and write the reason either way.

---

## §5 The eval that must be able to fail

The day's gate is the routing gate, and it is red or green with an exit code.

```bash
cd days/day-28-progressive-disclosure-design/lab
uv run python routing_gate.py; echo "exit: $?"
cd -
```

Measured on 2026-09-04 against Sutra's two skills:

```text
margin  1  draft a reply to the customer on this ticket
margin  2  how urgent is this ticket
margin  2  what priority should this ticket get
margin  2  triage this ticket for me
margin  2  can you take a look at this ticket
margin  4  how do we word an answer that cites a KB article

worst margin: 1 (threshold 1)
exit: 0
```

Now break it, with one sentence. Append `Use when a reply is needed.` to `ticket-triage`'s `description`
in `skills/ticket-triage/SKILL.md` and run it again:

```text
margin  0  draft a reply to the customer on this ticket
margin  2  how urgent is this ticket
margin  2  what priority should this ticket get
margin  2  triage this ticket for me
margin  2  can you take a look at this ticket
margin  4  how do we word an answer that cites a KB article

worst margin: 0 (threshold 1)
exit: 1
```

**One sentence, added to the skill that was not even involved**, and the reply-drafting request is now a
tie between two skills that both score two. Nothing about `kb-answer-style` changed. Take the sentence
out again and confirm the gate returns to `exit: 0`.

Three more checks that can go red, none of them costing a generation:

```bash
cd days/day-28-progressive-disclosure-design/lab
uv run python crowd.py       # expect ties 0, then ties 1
uv run python refactor.py    # expect ties 0 twice, worst margin 1 both times
uv run python suspects.py    # expect suspects: 4
cd -
```

`crowd.py` is the failure lab: four decoys, no score changed, five margins down and one request flipped
to a skill whose body says *"Do the obvious thing."* `refactor.py` is the trap: the two tables it prints
have the **same** worst margin and the same tie count, which is the finding rather than a disappointment.
`suspects.py` names the four misplaced sections of a five-section body — and has deliberately **no exit
code**, because a placement suspect is a question for a person
([4.3](parts/04-the-three-axes/4.3-what-the-gate-cannot-check.md)).

---

## §6 Request budget

**Free-tier Gemini**, 20 generate requests per day per model (`gemini-3.7-flash`, roster re-verified
2026-09-04).

| What | Generations |
| --- | --- |
| `price_the_shelf.py` — `count_tokens`, a separate endpoint | **0** |
| every script in sections 2, 3, 4 and 5 | **0** |
| the routing gate, green and red | **0** |
| **Total planned** | **0 of 20** |

**Nought, and it is worth saying why rather than treating it as luck.** Every question today is either
arithmetic over numbers Day 26 and Day 27 already measured, or set arithmetic over strings. The one thing
that touches the network — `count_tokens` — runs on the endpoint Day 24 verified keeps working while
`generate_content` is refusing
([24.2.1](../day-24-token-accounting-and-budgets/parts/02-two-ceilings/2.1-two-ceilings-one-clears.md)).

`price_the_shelf.py` still needs `GOOGLE_API_KEY` in `.env`, and it deliberately does not fall back to a
character estimate when the key is missing: a measurement that quietly prints a guess is worse than one
that stops.

**Cost: $0.** If you want to spend quota today, spend it on Day 27's `ask_the_desk.py` after making a
description change, and watch whether the routing you predicted from the proxy is the routing you get.
That is the one question the whole of section 2 cannot answer.

---

## §7 Traps

- **Counting one request instead of one conversation.** An activated body is carried on every turn after
  activation, so a per-request figure under-reports rung 2 by however many turns follow (1.1).
- **Optimising rung 0.** The 479-token preamble is the biggest single number and it cannot be changed
  (1.1).
- **Designing against the spec's 5,000-token body limit.** Sutra's largest body is 654. The recommendation
  is a ceiling, not a budget (1.1).
- **Measuring the description instead of the card.** The index is XML, and the tags are about forty
  tokens per skill. The error is silent, because the number that comes out is plausible (1.2).
- **Moving something because it is large.** Frequency moves things; size is only why you noticed. A small,
  static, occasionally-needed section costs **more** behind a link, because a fetch is a round trip
  (1.3, 3.3).
- **Weight flowing up.** Content pushed into a description to "help it get found" is paid on every
  listing and dilutes the triggers that were doing the routing (1.3).
- **A description reviewed on its own.** It is graded against its neighbours, and adding a skill is a
  change to every skill already there (2.1).
- **A shelf where everything matches something.** That is not good coverage, it is mush. Keep a request
  that should match nothing (2.2).
- **A threshold set aspirationally.** A gate that is red from the day it is written is deleted within a
  fortnight. Set it at today's worst margin and ratchet (2.3).
- **A stopword list that swallows a trigger.** Adding `ticket` to `STOP` changes every margin at once. It
  may be right; it must not be an accident (2.3).
- **A general-purpose fallback skill.** It never wins and it takes a point from everybody who does. If a
  fallback is genuinely wanted, it belongs in the instruction (2.4).
- **An action described in prose instead of given as a tool.** The model writes a plausible record. The
  most expensive misfiling available, and it produces the most confident output (3.1, 3.3).
- **A standing rule in a skill body.** Measured: delivered on 8 requests of 20, and on which 8 depends on
  what the model decided (3.2).
- **A live store pasted into a body.** Sutra's KB would fit, and it still does not go there. The cost is
  staleness, and staleness has no reading (3.2, 3.3).
- **Judging a change on the axis its author measured.** Price, routing and placement disagree, and the
  merge that improves nothing improves the number people look at (4.1).
- **The routing gate on a one-skill shelf.** It does not report perfect routing. It raises
  `IndexError: list index out of range`, because there is no second-best to subtract (4.1).
- **A suspect list turned into a gate.** It fires on `ticket-triage`'s worked example, correctly, and the
  cheapest way to make it green is to delete the real tool output (4.3).
- **Believing an audit after the shelf outgrew it.** At 42 skills the shared-filler intersection is empty
  and specificity has gone up — on the worst shelf in the day (5.1).
- **Creating agents to shrink an index.** You have taken on session boundaries and transfer logic to save
  two thousand tokens, and moved the routing problem up a level (5.2).

---

## §8 Verify before you code

Run, read or fetched on **2026-09-04**, the day this was written:

- **`https://adk.dev/skills/`** — fetched. Confirms `from google.adk.skills import load_skill_from_dir`,
  `from google.adk.skills import models`, `models.Skill`, `models.Frontmatter`, `models.Resources` and
  `skill_toolset.SkillToolset`. It does **not** document `load_skills_from_dir`,
  `prompt.format_skills_as_xml`, `Resources.list_references` or `Resources.get_reference`, so those were
  verified a second way, below.
- **The installed `google-adk==2.7.1`**, read directly: `google/adk/skills/__init__.py` exports
  `load_skills_from_dir`; `models.py` defines `Skill.name` and `Skill.description` as properties over the
  frontmatter and `Resources.get_reference` / `Resources.list_references`; `prompt.py` defines
  `format_skills_as_xml`, which HTML-escapes each name and description into `<available_skills>`. Day 26
  verified this surface; today only uses it.
- **The 1024-character description limit**, reproduced against the same package —
  `models.Frontmatter(name="kb-dump", description="x" * 1104)` raises the `ValidationError` quoted in
  [3.1](parts/03-four-containers/3.1-four-containers-one-property.md).
- **`sutra/loop.py`**, read and run — `TOOLS` prints `['lookup_ticket', 'search_kb']`, `KB` holds two
  articles, and `search_kb("logout")` returns KB-104. Every container example in section 3 names a symbol
  that exists in that file rather than one from memory.
- **The five rungs**, from Day 26's measurements against `gemini-3.7-flash`: preamble 479, index envelope
  12, cards 93 and 109, bodies 654 and 375, rubric 142. Every arithmetic block in sections 1, 3 and 4 is
  built on those and says so; nothing today re-measures them.
- **Day 24's 429 body**, cited rather than reproduced —
  [24.2.2](../day-24-token-accounting-and-budgets/parts/02-two-ceilings/2.2-reading-the-ceiling-off-a-refusal.md)
  carries the full text with `limit: 20` in it.
- `https://arxiv.org/abs/2406.18665` — cited, not re-taught. The dated row is in `docs/PAPERS.md` from
  Day 9.

**No new ADK surface is used today**, and no model is called. The two things that could have been
invented — a symbol and a token count — were checked against the installed package and against Day 26's
measurements respectively, and the numbers that could not be checked that way are printed as `~` or as
`not in tokens`.

---

## §9 Say it in an interview

"We had two skills and no idea what they cost, so we built a scale. Progressive disclosure gets talked
about as a loading order, and it is really five budgets paid at five different frequencies — a fixed
preamble on every request, an index when the model asks, a body that is carried on every turn after
activation, and a reference file that costs a whole model round trip to fetch. The body's multiplication
across turns is the biggest lever, and on a rate-limited tier the reference fetch is the most expensive
rung per byte. So the design question is never 'is this big?' — it is 'how often should this be paid
for?'

The thing that surprised me was an optimisation we rejected. Moving a worked example out of a skill body
into a reference file cut the body by twenty-eight per cent, which sounds decisive. But the fetched
content comes back into the context and rides along for the rest of the conversation, so over five turns
the net saving was about one per cent — and the fetch is a whole round trip, five per cent of our daily
request budget. We made the change, measured it, reverted it, and left both numbers in the repository so
the next person does not have to.

Descriptions turned out to be a routing table rather than documentation. With one skill it only has to
match; with twenty it has to beat the other nineteen, so what matters is the margin to the second-best,
not the score. A description gets worse without changing, just because somebody added a neighbour. We
measure it with a deterministic word-overlap proxy against a fixed list of real requests — it is not what
the model does, no synonyms, no stemming, but it is good at the thing that matters, which is detecting
collisions, and it is free and reproducible where a live routing test is neither. We proved it on
ourselves: four plausible, well-meant, general-purpose skills added to a shelf of two changed no score at
all, dropped every margin by one, and flipped one request to a skill whose entire body says 'do the
obvious thing'.

The part I would push in a design review is that there are three axes, not one. Price, routing, and
whether each thing is even in the right container — an action, a procedure, a standing value or data.
Only the first two have a command. And they disagree: we built a specimen skill holding a triage
procedure, a reply procedure, a standing rule, a rubric and a copy of the knowledge base, and our routing
check could not tell it apart from the properly separated shelf. Same worst margin, same zero ties, same
green exit. Splitting it halved the token cost and fixed the real problem, which was that the standing
rules only applied on the runs where the model happened to load the skill.

And I know where it stops working. At forty skills the index is about four thousand tokens on every
conversation that asks, forty-one of forty-two of our cards contained the word 'ticket', and — the one
that caught us — the audit itself degraded, because we had measured shared filler as a set intersection
and one card with a different vocabulary empties it. The fix at that point is structural: search instead
of listing, or a hierarchy, and on a rate-limited tier search wins because a hierarchy costs an extra
round trip per request."

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked and `./m depth 28` is green. Defined by
understanding and green checks, never by elapsed time — a part is finished when you could explain it to
someone else without the page open.

**Phase 4's gate** is skills authored, loaded and audited, with `./m check` green including the skills
lint and the `:free` lint. Today closes the design half and hands Day 31 two more checks with exit
codes — `routing_gate.py` and Day 27's `preflight.py` — plus one report that must deliberately **not**
become a gate ([4.3](parts/04-the-three-axes/4.3-what-the-gate-cannot-check.md)). Sourcing and auditing
is Day 29, testing and versioning is Day 30, and [5.2](parts/05-in-production/5.2-splitting-the-audience.md)
has already left Phase 8 a decision to make on its first day: whether the second agent gets its own
shelf.

---

## §11 Ledger & commit

**`docs/PROGRESS.md`** — append:

```text
| 28 | <date> | SK-09, SK-10, SK-11 | 16 | <hash> | ✅ |
```

**`docs/PACKAGES.md`** — **no new rows.** Nothing was installed and no model string changed;
`google-adk` stays at 2.7.1 and `gemini-3.7-flash` stays pinned as recorded on 2026-08-26.

**`docs/PAPERS.md`** — **no new rows.** Today teaches no paper. `arXiv:2406.18665` is cited from
[2.1](parts/02-descriptions-as-routing/2.1-a-description-is-a-routing-row.md) and already has its dated
row from Day 9.

**`docs/SKILL_PROVENANCE.md`** — **no new rows.** No skill was added or removed; the two first-party rows
from Day 27 are unchanged. The decoys in
[2.4](parts/02-descriptions-as-routing/2.4-the-crowded-shelf.md) and the specimen in
[4.2](parts/04-the-three-axes/4.2-refactoring-the-overloaded-skill.md) are built in code precisely so
that this ledger does not gain a row for something nobody should ship.

**The commit:**

```text
day 28: progressive disclosure and skill design - closes SK-09, SK-10, SK-11
```
