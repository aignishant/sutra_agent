---
day: 74
paper: "doi:10.1145/1476589.1476628"
title: "Response time in man-computer conversational transactions"
ids: ["ADK-52"]
level: production
prerequisites: ["../parts/01-the-blank-screen/1.1-the-blank-screen.md"]
prev: "../parts/05-in-production/5.2-what-a-real-streaming-system-adds.md"
next: "../LESSON.md"
---

# Response time in man-computer conversational transactions

> *Response time in man-computer conversational transactions* · `doi:10.1145/1476589.1476628` ·
> Proceedings of the December 9–11, 1968, fall joint computer conference, part I (AFIPS '68), page
> 267 · ACM Press, 1968 · <https://doi.org/10.1145/1476589.1476628>

> Record checked live on 2026-09-06 via `https://api.crossref.org/works/10.1145/1476589.1476628`.
> The title, proceedings, page and year above are copied from that record, which gives the event as
> *the December 9–11, 1968, fall joint computer conference, part I*. The record carries **no
> abstract**, so nothing in this document is a paraphrase of one, and the section below is explicit
> about which claims come from the paper as the field cites it and which are this curriculum's own
> arithmetic.

## One-line answer

The reason to build any of this day's machinery is a claim from 1968: response time does not make an
interaction better or worse by degrees — it changes **what kind of interaction it is**, at
thresholds — and the demo below shows streaming moving **3 of 4** answers back inside the
conversational band while the total time to produce them is **identical at 25.20s**.

## The story

You ask someone a question and they do not answer.

Not *no* — nothing. You watch their face. A second goes by, which is a long time when you are looking
at someone, and you start to wonder whether they heard you. Two seconds and you are deciding whether
to say it again. Four and you have started to construct an explanation: they are annoyed, they did not
understand, the line is bad.

What actually happened is that they were thinking, and at the end of it they gave you an excellent
answer. But you were not waiting for four seconds. You were *doing something else with those four
seconds*, and what you were doing was building a story about the silence.

Now compare the version where, half a second in, they say *"right —"* and nothing else. One syllable,
no information at all. You wait comfortably for as long as it takes.

## The idea in plain language

The paper's setting is 1968: terminals, time-sharing, a person at a keyboard waiting on a machine.
Its question is one that had not been asked systematically before — not *"how fast is the computer?"*
but *"how fast does the computer have to be for the person to keep working?"*

The answer the field takes from it is that there are **thresholds**, and that they matter more than
the numbers between them. Three of them are recited constantly, and they are the ones this demo uses:

| Wait | What it feels like | What the person does |
| --- | --- | --- |
| up to about 0.1s | instantaneous | nothing; the system is simply reacting |
| up to about 1s | a noticeable pause | keeps their train of thought, does not need reassuring |
| up to about 10s | a wait | attention drifts, and holding it costs them effort |
| beyond about 10s | a delay | attention goes elsewhere, and they will need to come back to it |

Three points about that table are worth making before anything else.

**It is about attention, not about speed.** A system twice as fast that stays inside the same band has
bought nothing that a person can feel. A system marginally slower that crosses a threshold has lost
something that no amount of throughput reporting will show.

**The bands are ranges, not a curve.** The paper's contribution is precisely that the relationship is
not smooth. If it were, "make it faster" would be the whole of the advice, and there would be no
design decision to make.

**And the thresholds are about the *first* sign of life, not about completion.** This is the part that
does the work for us, and it is why a day about streaming ends here. The person in the story was not
made comfortable by a faster answer. They were made comfortable by *"right —"*.

**What this document claims about the source.** The thresholds above are what the field attributes to
this paper, and they are the form in which the result is universally cited — they appear in interface
guidance and in usability textbooks with this paper as the origin. The Crossref record has no
abstract, and this document has not reproduced the paper's own tables, its experimental method, or its
exact wording. Where the numbers below are used, they are used as the field's rounded thresholds, and
the demo's `SECONDS_PER_TOKEN` is a **stated assumption** of this curriculum's own rather than
anything from 1968.

## Why Sutra needs it

Because part [1.1](../parts/01-the-blank-screen/1.1-the-blank-screen.md) made a claim it could not
prove: that streaming changes when the reader is served and not how fast the work is, and that this
matters. The lab could measure the first half — 13% of the answer needed before the screen can change,
against 100% — and had nothing to say about why 13% is better than 100%, because a scripted model
answers instantly and no wait exists to measure.

This is where that gap is filled, and it is filled by an argument rather than by a stopwatch. The
thresholds are the reason a partial event is worth all the machinery of section 2 and section 3: the
final chunk trap, the framing rules, the disconnect handling. Every one of those is a cost paid to put
one syllable on the screen early.

It also settles what to say when somebody asks whether streaming is worth the complexity. The honest
answer is not *"users like it"*. It is that the completion time is unchanged and the interaction has
moved into a different band, and that the band is the thing people respond to.

## The mechanism

The paper's idea, written as code, is a classification. Nothing more:

```python
def band(seconds: float) -> str:
    """Which band a wait of `seconds` falls into."""
    for upper, name in BANDS:
        if seconds <= upper:
            return name
    return BANDS[-1][1]
```

**Line by line:**

- `BANDS` is an ordered tuple of `(upper bound, name)` pairs, so the first pair whose bound is not
  exceeded is the answer. Ordering is the whole implementation; there is no arithmetic in this
  function at all.
- `seconds <= upper` uses the bound inclusively, which is a choice with no evidence behind it — a wait
  of exactly 1.0s is on the line, and the paper's claim is about a region rather than about a
  boundary. Putting a rounded threshold into a strict comparison gives the number a precision it does
  not have, and it is worth knowing you have done that.
- `return BANDS[-1][1]` is unreachable because the last bound is infinity, and it is there anyway: a
  function that maps a value into a set of bands should return a band for every value, including the
  ones a future edit introduces.

And the one line that turns the classification into a claim about streaming:

```python
def first_response(tokens: int) -> float:
    """How long before the reader sees anything at all."""
    return SECONDS_PER_TOKEN if STREAM else tokens * SECONDS_PER_TOKEN
```

**Line by line:**

- With streaming on, the wait is one token's worth, regardless of how long the answer is. That is the
  whole of what streaming buys, stated as an expression.
- With it off, the wait is the entire answer — `tokens * SECONDS_PER_TOKEN` — so it grows with the
  length of the reply. Longer answers are exactly where non-streaming gets worse, which is the
  opposite of what a designer would want, since longer answers are also the ones worth waiting for.
- `SECONDS_PER_TOKEN` appears on both branches, unchanged. The demo cannot be accused of making the
  streaming run faster, because the rate is shared.

## The paper in one demo

Four answers of different lengths, classified by the thresholds, with streaming on and off.

```text
lab/papers/response-time/
├── bands.py   # the thresholds, the classification, and the one switch
└── demo.py    # four answers, run through it both ways
```

`bands.py` in full below the module docstring:

```python
# The one switch. With streaming off, the first thing the reader sees is the finished answer.
STREAM = True

# Seconds per token. This is an ASSUMPTION, not a measurement: no provider was called for this demo,
# and a real rate depends on the model, the load and the network. It is held constant across both
# runs so that the comparison is about *when the reader is served*, never about speed.
SECONDS_PER_TOKEN = 0.04

# The thresholds, as the field states them: the upper bound of each band, and what it means.
BANDS: tuple[tuple[float, str], ...] = (
    (0.1, "instantaneous"),
    (1.0, "flow of thought kept"),
    (10.0, "attention held, with effort"),
    (float("inf"), "attention gone"),
)

# The band this demo treats as the goal, and the reason it can go red: the paper's argument is that
# staying inside the flow of thought is what makes an interaction feel like a conversation.
GOAL = 1.0
```

**Line by line:**

- `SECONDS_PER_TOKEN = 0.04` carries its own honesty note in the source, because a number in a demo
  gets quoted later and the comment travels with it. Nothing was measured to obtain it; it is a
  plausible rate held constant so the comparison is fair.
- `BANDS` stops at `float("inf")` so that every wait lands somewhere, including absurd ones.
- `GOAL = 1.0` is the threshold the exit code tests. Choosing the flow-of-thought bound rather than
  the instantaneous one is a judgement: a conversational assistant is not trying to feel like a button
  press, it is trying to keep the person in the conversation.
- There is no model here, no network and no agent. A demo of a paper's contribution should contain the
  contribution and nothing else, and this file could not be smaller without losing the idea.

`demo.py`'s loop is the whole of the rest:

```python
    for label, tokens in ANSWERS:
        first = first_response(tokens)
        done = completion(tokens)
        name = band(first)
        flag = "" if first <= GOAL else "   <-"
        if first > GOAL:
            missed += 1
        print(f"  {label:<26} {tokens:>6} {first:>7.2f}s {done:>7.2f}s  {name}{flag}")
```

**Line by line:**

- `first` and `done` are computed separately and printed side by side, because the argument is the
  relationship between them. A demo that printed only one of the two columns would prove nothing.
- `band(first)` classifies the **first response**, never the completion. That is the paper applied to
  streaming in one function call.
- `missed` counts turns outside the goal band and becomes the exit code. The claim is checkable rather
  than illustrated.
- `{first:>7.2f}s` prints two decimal places, which for `0.04` is exact and for the ablation's numbers
  is rounded — worth noticing, because a table of pretty numbers is where false precision enters.

With streaming on:

```bash
cd days/day-74-live-api-streaming/lab/papers/response-time
uv run python demo.py; echo "exit: $?"
```

**Line by line:**

- `cd` first: `demo.py` imports `bands` by plain name, so the working directory has to be the demo's
  own folder.
- `echo "exit: $?"` prints the exit code, because the claim *is* the exit code.

Measured on 2026-09-06:

```text
streaming: ON
4 answers, 0.04s per token in both runs

  answer                     tokens    first     done  band at first response
  a yes or no                    20    0.04s    0.80s  instantaneous
  a short explanation            60    0.04s    2.40s  instantaneous
  a walkthrough                 150    0.04s    6.00s  instantaneous
  a long answer with steps      400    0.04s   16.00s  instantaneous

  total time to finish all four   25.20s
  turns outside the goal band     0 of 4

  Every turn put something on screen inside the flow-of-thought band. The work took
  exactly as long as it did in the other run.
exit: 0
```

Now the ablation — same answers, same rate, same thresholds, and the reader waiting for the whole
thing:

```bash
uv run python demo.py --off; echo "exit: $?"
```

**Line by line:**

- `--off` sets `bands.STREAM = False`. Nothing else differs, and `SECONDS_PER_TOKEN` is untouched.

Measured on 2026-09-06:

```text
streaming: OFF (ablation)
4 answers, 0.04s per token in both runs

  answer                     tokens    first     done  band at first response
  a yes or no                    20    0.80s    0.80s  flow of thought kept
  a short explanation            60    2.40s    2.40s  attention held, with effort   <-
  a walkthrough                 150    6.00s    6.00s  attention held, with effort   <-
  a long answer with steps      400   16.00s   16.00s  attention gone   <-

  total time to finish all four   25.20s
  turns outside the goal band     3 of 4

  The same answers, produced at the same rate, took the same total time - and three of
  the four left the reader with a blank screen long enough to lose the thread. Nothing
  here is slower. The reader is simply served last instead of first.
```

| | streaming on | streaming off |
| --- | --- | --- |
| first response, longest answer | 0.04s | 16.00s |
| band, longest answer | instantaneous | attention gone |
| turns outside the goal band | **0 of 4** | 3 of 4 |
| total time to finish all four | **25.20s** | **25.20s** |
| exit code | 0 | 1 |

**Read the fourth row first.** 25.20s in both. Not similar — identical, because the same tokens were
produced at the same rate. Nothing in the streaming run is faster, and if the only thing you measured
was throughput you would conclude the change had done nothing at all.

**Then read the second row.** The long answer moves from *attention gone* to *instantaneous*, and it
does so without a single token being produced any sooner than it was before. The work is unchanged; the
serving order is not.

And notice which answers the ablation ruins. The short one is fine — 0.80s stays inside the band. It is
the walkthrough and the long answer with steps, the two most useful replies in the set, that fall out.
Non-streaming degrades exactly in proportion to how much the reader was going to get, which is a
property worth stating out loud because it is the reverse of what anyone would design on purpose.

## When it breaks

**Streaming does not rescue an answer that is simply slow to start.** The demo's first response is one
token's worth because the model begins producing immediately. A real turn can spend a long time before
its first token — retrieving documents, calling a tool, waiting on Day 72's backoff ladder — and during
all of that there is nothing to stream. The thresholds still apply and streaming has not helped, which
is why systems fill that gap with something else to look at: a status line, a tool-call indicator, a
cursor. Those are not decoration; they are the same idea applied where the model cannot supply it.

**The bands are rounded folklore by the time they reach us.** They are quoted as 0.1, 1 and 10 because
they are memorable, and any specific claim about a specific interface needs measuring rather than
citing. What survives review is the *shape* of the claim — that there are thresholds and that crossing
one changes behaviour — not the second decimal place of any of them.

**And the demo is a simulation, which limits what it can prove.** `SECONDS_PER_TOKEN` is an assumption
stated in the source; the token counts are illustrative; nothing here observed a person. What the demo
does establish is an arithmetic relationship — that first-response time under streaming is independent
of answer length while completion time is not — and that relationship is true of any rate you put in.
Substituting a measured rate would change every number in the table and none of the conclusions.

**The claim does not hold at all when nobody is reading.** Day 73's nightly job has no attention to
keep, so every threshold on this page is irrelevant to it — and a batch caller that streams is paying
for partial events nobody will look at. That is why the build brief asks for the mode to be a
parameter.

## In production

**What survived: everything, and mostly without attribution.** The thresholds are in interface
guidance, in the design of loading indicators, in the rule that a button must acknowledge a press
immediately even when the work behind it is slow, and in the existence of streaming responses at all.
Very few of the people applying them could name the paper, which is the usual fate of a result that
becomes obvious.

**What did not survive: the setting, and the units of the argument.** The paper is about a person at a
terminal in a time-sharing system, where the response time was a property of the machine and the
queue. Almost nothing about that arrangement exists now. What did not survive in a subtler way is the
assumption underneath it: that response time is something you *reduce*. A generative model's response
time is not a queueing artefact to be optimised away — the tokens genuinely take that long to produce —
so the modern application of this paper is not "make it faster" but "restructure who waits for what",
which is a different move than its authors were arguing for.

**What a professional measures because of it.** Time to first token, separately from time to
completion, as two different metrics with two different alert thresholds. Reporting only the second is
the mistake this whole day exists to prevent, and it is easy to make because the second is the one that
looks like the real number. A dashboard showing p50 and p99 completion time for a streaming endpoint is
measuring the half of the experience the user does not have.

**The review comment a senior engineer leaves:** *"Split the latency metric. Time to first token and
time to completion are different numbers with different consequences and we're only recording the
second one, which is the one the user doesn't experience. And when there's a tool call in the middle of
a turn, the stream goes quiet — put something on the wire during that, because from the reader's side a
quiet stream and a dead connection look the same. The thresholds are the old ones and they're rounded,
so don't put 1.0 in an alert as though it were measured; use it to decide what to build and measure our
own numbers to decide what to fix."*

**The interview question:** *"Why stream a response at all, if it doesn't finish any sooner?"* An honest
answer: *"Because response time isn't a smooth dial — there are thresholds where the interaction changes
character, which is the 1968 result everyone still cites. Roughly: a tenth of a second reads as
instantaneous, about a second keeps someone's train of thought, and past about ten seconds their
attention leaves. Streaming doesn't change how long the work takes — I measured a simulation where the
total was identical to two decimal places both ways — it changes which band the *first* response falls
into. Without streaming, first response scales with answer length, so the longest and most useful
answers are exactly the ones that fall out of the band; with it, first response is one token's worth
regardless. The practical consequence is that you have to measure time to first token separately from
time to completion, and that when the stream goes quiet mid-turn — a tool call, a retry — you need to
put something there, because the thresholds don't care why the screen isn't changing."*

## Check yourself

```bash
cd days/day-74-live-api-streaming/lab/papers/response-time
uv run python demo.py
uv run python demo.py --off
```

Change `SECONDS_PER_TOKEN` to a rate you have actually observed from a provider — note where you got it
and on what date — and run both again. Report which numbers changed and which conclusions did not, then
say in one sentence what that tells you about how much the demo depends on its assumption.

Then add a fifth answer of 1,000 tokens and predict, before running it, both bands. Afterwards, say
which of the two runs the new row changed and why the other one did not move at all.

**Out loud, without scrolling up:** the total time was identical in both runs, to two decimal places.
What exactly did streaming buy, and who paid for it?

---

That is the day, and the phase's first half. The nightly job runs while nobody watches; this one runs
while somebody watches every character. Tomorrow the connection goes both ways.

**Next:** [back to the hub](../LESSON.md).
