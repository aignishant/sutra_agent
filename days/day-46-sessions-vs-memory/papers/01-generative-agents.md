---
day: 46
paper: "arXiv:2304.03442"
title: "Generative Agents: Interactive Simulacra of Human Behavior"
ids: ["ADK-28"]
level: production
prerequisites: ["../parts/05-failure-lab/5.1-the-past-that-matched-on-nothing.md", "../parts/04-the-choice/4.1-pricing-both-in-tokens.md"]
prev: "../parts/06-in-production/6.2-the-two-services-we-park.md"
next: ""
---

# Generative Agents: Interactive Simulacra of Human Behavior

## One-line answer

An agent that remembers everything and an agent that remembers nothing fail in the same way, and this
paper's answer is that **retrieval must be scored on more than similarity** — recency, importance and
relevance summed together — plus a second store of conclusions the agent drew from its own
observations, kept separate from the raw record of what happened.

## The story

You hire a cook through an agency, and every week a different person comes.

Each one is perfectly good. They arrive, they ask where things are, they cook, they leave. The
trouble is the small things that took you a year to work out. The youngest child cannot eat peanuts.
The gas cylinder is nearly empty and the spare is behind the door. Thursday is a fasting day and the
food has to be ready earlier. The second burner does not light unless you hold it.

So you start leaving notes on the fridge door.

The first month this works beautifully. By the third month there are forty notes on the door, held on
with tape and magnets, overlapping. A new cook stands in front of it for a while and then reads the
top three, because forty notes is not a system. And the top three are whatever went up most recently
— *bring change for the milk*, *the tap is dripping*, *dal was too salty last time* — and the note
about the peanuts is somewhere underneath, from March, and it is the one that matters most and it is
the one nobody reads.

The problem was never the notes. It was that nothing on that door says which note to read first.

## The idea in plain language

By 2023 a language model could hold a completely convincing conversation for one exchange and had no
idea who you were on the next. The obvious fixes had both been tried and both failed.

**Remember nothing.** Every conversation starts clean. Cheap, safe, and useless for anything that
spans a day.

**Remember everything.** Put the whole history into the prompt. This fails for two reasons rather
than one, and the second is the interesting one. It does not fit — a context window is finite, and
Day 24 measured what that costs
([1.2](../../day-24-token-accounting-and-budgets/parts/01-what-a-request-costs/1.2-charged-again-every-turn.md)).
And even where it fits, it does not work: filling the window with everything buries the thing that
mattered among a thousand things that did not, which is the fridge door.

So the real question is **selection**. Given everything the agent has ever observed, which handful of
memories should be in front of the model right now?

The paper's setting was an experiment: twenty-five agents in a small simulated town, each with a
one-paragraph description, left to run. They arranged a party, made friends, ran a shop, remembered
that somebody was standing for local office. Nobody scripted any of it. That setting is what the
paper is famous for and it is not what survived; what survived is the architecture underneath.

Three ideas, and this day has been circling all three.

**A memory stream.** A single, growing, append-only list of natural-language observations, each with
a timestamp. Not a summary, not a database of facts — the record of what the agent observed, in
order. That is `add_session_to_memory` ([1.3](../parts/01-the-line/1.3-nothing-is-filed-unless-you-file-it.md)),
and *"append-only list of events"* is a fair description of what `InMemoryMemoryService` holds.

**A retrieval function that scores three things.** Not similarity alone. **Recency** — how long since
this memory was last touched. **Importance** — how much this memory mattered, rated when it was
stored. **Relevance** — how close it is to what is being asked right now. The score is the sum of the
three, and the top few are handed to the model.

**Reflection.** Periodically, the agent reads its own recent memories and asks itself what they add up
to, and writes the answer back into the same stream as a new memory — one that is marked as derived
rather than observed, and can itself be retrieved and reflected on. *"Klaus is spending a lot of time
on his research"* is not something anybody said; it is something the agent concluded from a dozen
things it saw.

The middle one is the idea this day needed. `InMemoryMemoryService` scores on **one** term, badly —
one shared word is a hit and the results are in insertion order with no score at all
([5.1](../parts/05-failure-lab/5.1-the-past-that-matched-on-nothing.md)). Everything that went wrong
in section 5 is a consequence of scoring on one term or on none.

## Why Sutra needs it

Because Sutra has just built the memory stream and nothing else, and this paper is the map of what is
missing.

Section 5 measured three failures. A question about being logged out returned a ticket about printing
because there is no ranking. The right case was third in the list because there is no ranking. Five
hundred filed cases diluted a single question to 0.2% useful because there is no ranking and no cut.
All three are the same missing thing, and this paper names it precisely: a score with more than one
term in it.

And it names a term Sutra does not have and Day 49 will not add either. Embeddings give relevance.
Recency is a timestamp subtraction, nearly free. **Importance is the one that has to come from
somewhere** — the paper asks a model to rate each memory as it arrives, which costs a generation per
observation, and that cost is exactly why Day 48 exists as a separate day about what is worth
remembering.

Read it after the parts, not before. Principle 4 at the scale of a day: you have hand-built the
stream, watched an unranked retriever fail four different ways, and priced two retrieval policies in
tokens. The proposal means something now. Read first, it would have been a diagram.

## The mechanism

The paper's retrieval function, written out.

Every memory in the stream is a natural-language sentence with a creation timestamp and a
last-accessed timestamp. When the agent needs context, every memory is scored on three terms.

**Recency** is exponential decay in the hours since the memory was last *accessed*, with a decay
factor of `0.995` per hour. Note *accessed*, not *created*: a memory that keeps being retrieved stays
warm, and one that is never useful sinks.

**Importance** is a rating from one to ten, assigned **once, when the memory is created**, by asking
a language model how poignant the memory is — with the paper's own examples anchoring the scale:
brushing teeth at the low end, breaking up with a partner at the high end. It is stored with the
memory and never recomputed.

**Relevance** is the cosine similarity between an embedding of the memory and an embedding of the
query.

The three are each normalised to the range zero to one, and then summed:

> `score = α_recency · recency + α_importance · importance + α_relevance · relevance`

with all three weights set to `1` in the paper's implementation. The top-ranked memories that fit in
the context window are passed to the model.

That is the whole retrieval mechanism, and three details in it are doing real work.

**The normalisation is over the candidate set**, so the terms are comparable before they are added.
Raw cosine similarity and raw exponential decay do not live on the same scale, and summing them
without normalising would let one term silently dominate.

**Recency is on last access, not creation**, which makes the stream self-organising: retrieval is a
vote.

**Importance is assigned at write time and is a property of the memory, not of the query.** This is
the term that lets a memory nobody asked about — the peanut allergy from March — outrank three recent
notes about the milk.

Two more components sit on top of the stream.

**Reflection** runs when the summed importance of recent observations crosses a threshold — in the
paper's implementation, roughly a couple of times a day of simulated time. The agent asks a model
what the most salient questions are about its recent experience, retrieves memories for those
questions, and generates statements with citations back to the memories that produced them. Those
statements go into the same stream, so reflections can be retrieved like observations and can be
reflected on again — a tree, not a flat list.

**Planning** turns retrieved memory into a day's schedule at decreasing granularity — a broad outline
first, then hour blocks, then finer — and re-plans when something happens that contradicts the plan.

The paper's own evaluation is worth stating precisely, because it is what a careful reader asks
about. Agents were interviewed about their memory, plans and reactions, and their answers were ranked
against ablated versions of the same architecture by human raters. The ablations removed reflection,
then reflection and planning, then all three components. The full architecture was rated most
believable, and **the largest single drop came from removing memory retrieval altogether.**

## The paper in one demo

The contribution, and nothing else: a stream of observations, the three-term score, and a switch that
turns two of the terms off.

```text
days/day-46-sessions-vs-memory/lab/papers/generative-agents/
├── stream.py     nine observations with hand-assigned importance ratings
└── retrieve.py   the three-term score, the normalisation, and the ablation
```

No model, no key, no network, no embeddings. Relevance is word overlap rather than cosine similarity
— which is a weaker term than the paper's and is **the point**: if the sum still beats similarity
alone with a *worse* relevance term, the claim being tested is about the other two terms.

```python
# days/day-46-sessions-vs-memory/lab/papers/generative-agents/stream.py
@dataclass(frozen=True)
class Observation:
    """One thing the desk saw, in the order it saw it."""

    hours_ago: float
    importance: int  # 1 = utterly mundane, 10 = a core memory
    text: str


STREAM: list[Observation] = [
    Observation(1.0, 1, "Agent opened the ticket queue."),
    Observation(2.0, 2, "Customer on 4610 says the page is slow this morning."),
    Observation(3.0, 3, "Agent filtered the queue by priority."),
    Observation(30.0, 9, "Root cause on 4521: session cookie missing SameSite; logged out."),
    Observation(31.0, 2, "Agent replied to 4521 with the standard holding message."),
    Observation(50.0, 8, "KB-104 published: set SameSite and Secure on the session cookie."),
    Observation(52.0, 1, "Agent went to lunch."),
    Observation(120.0, 7, "Northwind reported the same logout loop last month; fixed by KB-104."),
    Observation(121.0, 2, "Agent archived the March tickets."),
]

QUERY = "the customer keeps getting logged out"
```

**Line by line:**

- `frozen=True` makes an observation immutable, which matches the paper: the stream is append-only,
  and an importance rating is assigned once at creation and never recomputed.
- `hours_ago` stands in for the paper's timestamp arithmetic. The paper decays on hours since **last
  access**; this demo has no access history, so it decays on age. That is a simplification and it is
  named here rather than hidden — it makes recency slightly less powerful than the paper's version,
  which again biases against the result being demonstrated.
- `importance` is an `int` from one to ten, **written by hand**. The paper obtains it by asking a
  language model to rate poignancy. Doing that here would cost nine generations and would make the
  demo unreproducible; hand-assigning it costs nothing and isolates the claim, which is about what
  the score does with importance, not about where importance comes from. What it does *not* do is
  dodge the real question — see *When it breaks*.
- The nine observations are built to hold one specific trap. The **most useful** memory for this query
  is `KB-104 published: set SameSite and Secure on the session cookie` — importance 8 — and it shares
  **no word** with the query. It is invisible to any similarity-only retriever, and that is exactly
  what the ablation will show.
- The routine noise — opening the queue, filtering it, lunch, archiving — is recent and low
  importance, and it exists so that recency alone is not a winning strategy either.

```python
# days/day-46-sessions-vs-memory/lab/papers/generative-agents/retrieve.py
DECAY = 0.995  # the paper's exponential decay factor, applied per hour since last access
TOP_K = 4
STOP = {"the", "a", "an", "is", "was", "on", "to", "of", "and", "in", "this", "it"}


def relevance(observation: Observation, query: str) -> float:
    """Overlap between the query and the memory, as a fraction of the query's words."""
    query_words = words(query)
    return len(query_words & words(observation.text)) / len(query_words)


def recency(observation: Observation) -> float:
    """Exponential decay in the hours since the memory was last touched."""
    return DECAY**observation.hours_ago


def importance(observation: Observation) -> float:
    """The hand-assigned poignancy rating, on the paper's 1-10 scale."""
    return observation.importance / 10.0
```

**Line by line:**

- `DECAY = 0.995` is the paper's stated decay factor, per hour. It is gentle on purpose: a memory
  from five days ago still scores about a third of a memory from now, so recency shades the ranking
  rather than dictating it.
- `STOP` exists because the relevance term here is word overlap, and without it every memory would
  share `the` with the query — the exact failure
  [5.1](../parts/05-failure-lab/5.1-the-past-that-matched-on-nothing.md) measured on
  `InMemoryMemoryService`. Removing stopwords is what makes this a *weak* relevance term rather than
  a *useless* one, and the comparison needs the similarity-only arm to be a fair opponent.
- `relevance` divides by the number of **query** words, not by the union, so it answers *"how much of
  what was asked does this memory cover"*. A long memory is not penalised for being long, which is
  the right shape for a memory store where entries vary wildly in length.
- `recency` is `DECAY ** hours_ago` — a float raised to a float. This is the paper's exponential
  decay written directly; there is no library and no half-life conversion, because writing it any
  other way would obscure the one line that is the paper's.
- `importance` divides by ten only to put the one-to-ten scale into the zero-to-one range before
  normalisation. The rating itself is untouched.
- Each of the three is a **pure function of one observation** (plus the query, for relevance). That
  is what makes the ablation a one-line change rather than a second implementation.

```python
# days/day-46-sessions-vs-memory/lab/papers/generative-agents/retrieve.py (continued)
def normalise(values: list[float]) -> list[float]:
    """Min-max to [0, 1], as the paper does before summing the three terms."""
    low, high = min(values), max(values)
    span = high - low
    return [1.0 if span == 0 else (v - low) / span for v in values]


def rank(stream: list[Observation], query: str, *, relevance_only: bool) -> list[tuple]:
    relevances = normalise([relevance(o, query) for o in stream])
    recencies = normalise([recency(o) for o in stream])
    importances = normalise([importance(o) for o in stream])
    rows = []
    triples = zip(relevances, recencies, importances, strict=True)
    for observation, (rel, rec, imp) in zip(stream, triples, strict=True):
        score = rel if relevance_only else rel + rec + imp
        rows.append((score, rel, rec, imp, observation))
    return sorted(rows, key=lambda row: -row[0])
```

**Line by line:**

- `normalise` is min-max over the candidate set, which is the paper's stated step and is not optional.
  Cosine similarity lives in roughly zero to one; `0.995 ** 120` is about `0.55`; a poignancy rating
  over ten is between `0.1` and `1.0`. Summing those raw would weight the three terms by accident.
- `1.0 if span == 0` handles the degenerate case where every memory scores the same on a term — which
  happens for relevance the moment a query shares no words with anything. Without it this is a
  division by zero, and it is the single most likely crash in the file.
- `score = rel if relevance_only else rel + rec + imp` is the **ablation switch**, and it is one
  expression. The three weights are all `1`, as in the paper's implementation, so the sum is the
  paper's formula with nothing tuned.
- The rows keep all three component scores alongside the total, so the transcript shows *why* each
  memory ranked where it did. A ranking you cannot decompose is a ranking you cannot argue with —
  which is the same complaint section 5 made about `InMemoryMemoryService` returning no score at all.
- `zip(..., strict=True)` raises if the three normalised lists and the stream ever fall out of step,
  rather than silently truncating to the shortest. Silent truncation here would misattribute scores
  to the wrong memories and the output would still look plausible.
- `sorted(rows, key=lambda row: -row[0])` sorts descending by score. **This line is the paper.**
  Everything `InMemoryMemoryService` cannot do is in the fact that there is a number to sort on.

Run both arms:

```bash
cd days/day-46-sessions-vs-memory/lab/papers/generative-agents
uv run python retrieve.py
uv run python retrieve.py --relevance
```

**Line by line:**

- The first arm is the paper: relevance plus recency plus importance.
- `--relevance` is the ablation — similarity alone, which is what an ordinary vector search does and
  what most people mean by "the agent remembers".
- **Zero model calls in both arms.** There is no model, no key and no network anywhere in either
  file.

Measured on 2026-09-05, the full score:

```text
query: 'the customer keeps getting logged out'
score: relevance + recency + importance

     score   rel   rec   imp  memory
 ->   2.70  1.00  0.70  1.00  Root cause on 4521: session cookie missing SameSite; logged out.
 ->   1.61  0.50  0.99  0.12  Customer on 4610 says the page is slow this morning.
 ->   1.39  0.00  0.52  0.88  KB-104 published: set SameSite and Secure on the session cookie.
 ->   1.23  0.00  0.98  0.25  Agent filtered the queue by priority.
      1.00  0.00  1.00  0.00  Agent opened the ticket queue.
      0.82  0.00  0.69  0.12  Agent replied to 4521 with the standard holding message.
      0.76  0.00  0.01  0.75  Northwind reported the same logout loop last month; fixed by KB-10
      0.50  0.00  0.50  0.00  Agent went to lunch.
      0.12  0.00  0.00  0.12  Agent archived the March tickets.

    the top 4 are what the agent would be handed.
```

And the ablation, relevance alone:

```text
query: 'the customer keeps getting logged out'
score: relevance only

     score   rel   rec   imp  memory
 ->   1.00  1.00  0.70  1.00  Root cause on 4521: session cookie missing SameSite; logged out.
 ->   0.50  0.50  0.99  0.12  Customer on 4610 says the page is slow this morning.
 ->   0.00  0.00  1.00  0.00  Agent opened the ticket queue.
 ->   0.00  0.00  0.98  0.25  Agent filtered the queue by priority.
      0.00  0.00  0.69  0.12  Agent replied to 4521 with the standard holding message.
      0.00  0.00  0.52  0.88  KB-104 published: set SameSite and Secure on the session cookie.
      0.00  0.00  0.50  0.00  Agent went to lunch.
      0.00  0.00  0.01  0.75  Northwind reported the same logout loop last month; fixed by KB-10
      0.00  0.00  0.00  0.12  Agent archived the March tickets.

    the top 4 are what the agent would be handed.
```

**Look at where KB-104 lands.** Under the full score it is third, and in the four memories handed to
the agent. Under similarity alone it is **sixth**, below *"Agent opened the ticket queue"* and *"Agent
went to lunch"* — because it shares no word with the query and its score is therefore `0.00`, exactly
like every other irrelevant row. The article that actually fixes the customer's problem is ranked
below lunch.

And read the ablation's ranking properly, because it is worse than a demotion. Seven of the nine rows
score `0.00`. They are **tied**, so their order is whatever the sort was handed, which is insertion
order — the same arbitrary ordering
[5.1](../parts/05-failure-lab/5.1-the-past-that-matched-on-nothing.md) found in
`InMemoryMemoryService`. A similarity-only retriever does not merely rank the useful memory low; past
the first couple of hits it stops ranking at all.

The full score is not perfect either, and the transcript says so: rank four is *"Agent filtered the
queue by priority"*, pure noise, carried in on recency alone. That is the honest reading. The three
terms move the memory that matters into the window and they do not keep the rubbish out, which is why
importance has to come from somewhere better than a rating on routine events — and why the paper adds
reflection on top rather than stopping here.

## When it breaks

**Importance is the weakest link, and it costs a generation per memory.** The paper rates every
observation by asking a model. For a simulated town that is affordable. For a support desk filing
every event of every ticket it is a model call on the write path, forever, and on Sutra's budget —
twenty free requests a day — it is not affordable at all
([4.1](../parts/04-the-choice/4.1-pricing-both-in-tokens.md)). The demo above dodges this by writing
the ratings by hand, which is honest for a demo and is not a system. Any real use has to answer *where
does importance come from*, and the cheap answers are all bad: message length is not importance,
recency is already a term, and "the user pressed the star" is a feature nobody uses.

**One rating, forever.** Importance is assigned at creation from a single observation with no context
around it. A note about a routine deployment is mundane on Tuesday and the most important memory in
the store on Wednesday when it turns out to have caused the outage, and nothing in this architecture
revisits it.

**Reflection compounds its own mistakes.** Reflections are written back into the same stream and can
be retrieved and reflected on again. That is the mechanism's strength and it has no correction path:
a wrong conclusion becomes a memory, gets retrieved, supports another conclusion, and there is no
step anywhere that checks a derived statement against the observations underneath it. The citations
back to source memories make an audit *possible*; nothing performs one.

**The evaluation is not the one an engineer wants.** Believability, rated by human raters, over
interview answers about a simulated town. That is a reasonable measure for the question the paper was
asking. It is not precision at k on a retrieval benchmark, and it does not tell you whether this
scoring function beats a well-tuned vector search on a support archive. Nobody should quote this
paper as evidence that three-term scoring outperforms similarity on their own data. Quote it as
evidence that scoring on similarity alone is a choice, not a default.

**The weights are all `1` and were not tuned.** Whether recency should weigh as much as relevance is
entirely domain-specific — a support desk probably wants relevance to dominate, a personal assistant
probably wants recency to. The paper gives you the shape of the function, not the constants.

**And the whole thing assumes memories are sentences.** The stream is natural language throughout,
which is why a model can rate, retrieve and reflect on it. A store of structured records does not fit
this architecture without first being written out as prose, and that conversion is lossy in both
directions.

## In production

**What survived.** Three things, and they are now so ordinary that people build them without knowing
where they came from.

*Retrieval scored on more than similarity.* Recency as an explicit term, and some notion of
importance or priority alongside it, is standard in production memory systems now. Anybody who has
added a time-decay factor to a vector search has re-derived the first half of this paper.

*Separating raw observations from derived conclusions.* The reflection idea — that what an agent
concluded is a different kind of thing from what it observed, stored alongside it and marked as
such — is the design behind every "extract facts from the conversation" memory product, including
`VertexAiMemoryBankService`, which stores model-extracted memories rather than transcripts
([6.2](../parts/06-in-production/6.2-the-two-services-we-park.md)).

*Memory as an explicit, inspectable store.* Before this, "memory" mostly meant whatever was still in
the context window. Afterwards, memory is a thing with a schema, a write path, a retrieval function
and a place you can go and look. Every part of this day rests on that shift, and
`add_session_to_memory` / `search_memory` is that shift expressed as two methods.

**What did not.** Also three things, and being honest about them is what makes the first list
credible.

*The simulation.* Twenty-five agents in a town is not a product, and the wave of "agent society"
projects that followed the paper mostly produced demonstrations rather than systems. What people
needed was the retrieval architecture; what they copied first was the town.

*Reflecting on everything.* Rating every observation and reflecting on schedule is a model call per
memory plus periodic batches, and at production volumes that is the dominant cost of the whole
system. Real deployments reflect rarely, on a filtered subset, or asynchronously and off the critical
path — and many skip importance ratings entirely and use a cheap proxy, which is a real loss and is
usually the right trade.

*The evaluation setting.* Believability ratings by human judges over interviews did not become how
anyone measures a memory system. What did become standard is much more boring: retrieval precision on
labelled queries, and end-task accuracy with the memory ablated — which is exactly the shape of the
two-arm comparison in the demo above.

**What a professional writes instead of the teaching version.** They keep the three-term score and
replace every term with something cheaper. Relevance from an embedding index. Recency from a
timestamp. Importance from something free — the type of the event, whether a human marked the ticket,
whether the memory has been retrieved before and led to a resolution — with a model-based rating
reserved for the small fraction of memories where it changes the answer. And they log the three
component scores with every retrieval, exactly as the demo prints them, because a ranking you cannot
decompose is a ranking nobody can debug.

**The review comment a senior engineer leaves:** *"The scoring function is fine, but every weight is
`1` and there is no comment saying why. Put the three weights in one place with the workload they
were tuned against, and log the components alongside the total — when somebody reports that the agent
surfaced the wrong past case, the only thing that will tell us anything is which term won."*

**The interview question:** *"What did Generative Agents actually contribute?"* An honest answer:
*"Everyone remembers the simulated town, and the town is the part that did not survive. The
contribution is the memory architecture: an append-only stream of natural-language observations, and
a retrieval function that scores each one on three normalised terms — recency as exponential decay
since last access, importance as a poignancy rating assigned when the memory was written, and
relevance as embedding similarity to the query — summed, then top-k. Plus reflection: the agent
periodically reads its own recent memories, writes down what they add up to, and stores that
conclusion back in the same stream marked as derived. I built the retrieval half with no model at all
— nine observations, hand-assigned importances, word overlap for relevance — and the ablation is
convincing: with similarity alone, the knowledge-base article that actually fixes the problem ranks
sixth, below 'agent went to lunch', because it shares no words with the question. With all three
terms it is third and inside the window. What I would push back on is the importance term: the paper
gets it from a model call per memory, which is not affordable at volume, and nobody has a good cheap
substitute. And the paper's evaluation is believability ratings on a simulation, so it is evidence
that similarity-only retrieval is a choice rather than proof that this exact function wins on your
data."*

## Check yourself

```bash
cd days/day-46-sessions-vs-memory/lab/papers/generative-agents
uv run python retrieve.py
uv run python retrieve.py --relevance
```

Now set the importance of `KB-104 published: ...` to `1` and re-run the full-score arm. Watch where it
lands, then say in one sentence who — or what — would have to assign that rating in a real system, and
what it would cost per filed ticket.

Then change `DECAY` from `0.995` to `0.5` and re-run. The ranking collapses onto whatever happened
most recently. Say which of the three terms you would weight highest for a support desk, and why that
is different from the answer for a personal assistant.

**Out loud, without scrolling up:** name the three terms in the retrieval score, say which one Sutra
has no way to compute, and say what reflection stores that an observation does not.
