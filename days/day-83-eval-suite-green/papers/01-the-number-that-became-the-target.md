---
day: 83
paper: "doi:10.1016/0149-7189(79)90048-X"
title: "The number that became the target"
ids: ["AG-28"]
level: production
prerequisites: ["../parts/03-judge-and-bill/3.1-criterion-5-the-judge-beats-baseline.md"]
prev: "../parts/05-the-verdict/5.3-what-phase-13-inherits.md"
next: "../LESSON.md"
---

# Paper 01 — The number that became the target

> **Assessing the impact of planned social change**
> *Evaluation and Program Planning*, volume 2, issue 1, 1979, pages 67–90.
> `doi:10.1016/0149-7189(79)90048-X`
>
> The claim this day borrows: *"The more any quantitative social indicator is used for social
> decision-making, the more subject it will be to corruption pressures and the more apt it will be to
> distort and corrupt the social processes it is intended to monitor."*

## One-line answer

A measurement that is only watched stays honest, and a measurement that decides something starts
being optimised — so the moment an eval score gates a merge, the score and the quality it stood for
begin to come apart, and nothing in the score reports that it is happening.

## The story

The hospital that fixed its waiting times.

A health service is told that nobody should wait more than four hours in an emergency department, and
that the figure will be published. Everybody involved wants shorter waits; nobody is being cynical.
The number starts being reported weekly, then daily, and after a while it starts being very good
indeed.

What is happening, in the places where it got very good very fast, is not always shorter waits. It is
patients held in the ambulance outside, because the clock starts at the door. It is a new "assessment
area" that counts as admission. It is the four-hour case being seen at three hours fifty and the
five-hour case waiting longer, because one of those two changes the number.

Every one of those is somebody solving the problem they were actually given. The waiting time is
still being measured accurately. It has simply stopped being a measurement of how long people wait.

## The idea in plain language

The paper is about evaluating social programmes — schools, policing, welfare — and it is where the
sentence quoted above comes from. In the literature the sentence is usually referred to by its
author's surname plus the word *law*; this document cites it by DOI instead, and what matters is that
it makes a claim about a specific mechanism rather than issuing a general warning about statistics.

The mechanism has three steps.

**A quantitative indicator is chosen** because it correlates with something people care about but
cannot measure directly. Waiting time stands in for the quality of emergency care. An exam score
stands in for what a child has learned. A ROUGE score stands in for whether an answer is right.

**The indicator is used to decide something** — funding, promotion, whether a merge goes through.
That is the step the law is about. Watching a number changes nothing; *acting* on it applies pressure
to everything upstream of it.

**The correlation breaks under that pressure**, because the indicator is cheaper to satisfy than the
thing it stood for. Not because anybody cheats. The pressure selects, out of all the ways to improve
the number, the ones that are easiest — and easiest means "affects the number without affecting the
thing", because affecting the thing is the hard route.

Two clarifications that decide whether you have understood it:

- **It is not about dishonesty.** Every actor can be behaving well and the effect still occurs. It is
  a property of selection under measurement, not of character.
- **It is not an argument against measuring.** The paper argues *for* rigorous evaluation of social
  programmes. The claim is about indicators that carry decisions, and the
  implication is that such an indicator needs to be watched from outside itself.

The compressed version — *"when a measure becomes a target, it ceases to be a good measure"* — is
usually attributed to a different economist's remark about monetary policy and is frequently
mislabelled. The formulation in this paper is the older one about social indicators and the more
specific: it names the pressure, and it says the corruption is proportional to how much the indicator
is used.

## Why Sutra needs it

Because Phase 12 spent four days building exactly what the law is about: indicators that will be used
for decisions. Day 79's metrics gate a commit. Day 82's comparison gates a merge. Day 83's criteria
gate a phase. Every one of them is a quantitative indicator that has just been wired to a decision,
which is the precise condition the law describes.

And because the phase's own findings are early symptoms. Day 79 part 2.3's case that could not fail,
Day 80 part 3.2's rubric that scored everything the same, Day 81 part 3.3's 83.3% that was the base
rate — those are all the same thing seen from inside: a number that is easy to satisfy without doing
the work. They were found before anybody was optimising against them. Once somebody is, they stop
being curiosities and become the path of least resistance.

## The mechanism

The paper's method is a comparison of designs for evaluating a programme, and the indicator argument
sits inside it. Written out as the thing to remember rather than paraphrased as an abstract:

**The claim is proportional, not binary.** More decision-weight on an indicator means more corruption
pressure. So the question about any metric is never *is this a good metric* but *how much is riding on
it*, and the same metric is fine on a dashboard and dangerous on a merge gate.

**The corruption is upstream, not in the measurement.** The number is computed correctly throughout.
What changes is the process being measured, which reorganises itself around what the number counts.
This is why auditing the metric's implementation finds nothing.

**The remedy is not a better indicator.** A better indicator is a better proxy, and it is subject to
the same pressure the moment it carries the same weight. The paper's direction is different: use
multiple independent indicators, keep some of them off the decision path, and treat any single number
that drives decisions as needing external validation.

That third point is the one this repository can act on. It is the argument for keeping a *held-out*
measure — something the team is not optimising against — and for the calibration set that has been
parked since Day 79.

## The paper in one demo

A small end-to-end project implementing the claim and nothing else. Twelve desk variants, one case,
one real ADK metric, and a selection process that can be switched off.

```text
days/day-83-eval-suite-green/lab/papers/indicator/
├── pool.py    # twelve desk variants: what each said, and whether it asked a human
└── demo.py    # rounds of selection on the metric; --off watches without selecting
```

`pool.py` holds the whole setup:

```python
REFERENCE = (
    "Ticket 4688 is over the 1,000 refund limit, so I have asked your billing lead to approve"
    " it before anything moves."
)


@dataclass(frozen=True)
class Variant:
    name: str
    answer: str
    escalates: bool  # did it ask for approval before calling a tool that moves money?
```

**Line by line:**

- `REFERENCE` is what a person wrote down as the right answer. The metric compares words against it,
  which is what `response_match_score` does — ROUGE-1, from Day 79 part 3.3.
- `escalates` is the **goal**: did the desk actually ask a human before money moved. It is a boolean a
  person set, and no metric in the demo can read it. That separation is the paper's setup in one
  field.
- `frozen=True` so a variant cannot be edited by the selection loop. The demo selects among variants;
  it must not be able to change one.
- The coupling that makes the demo work is written into the pool deliberately, and it is the paper's
  mechanism rather than a discovery: four of the twelve variants say the right sentence and did not do
  the thing. Copying the reference wording is cheaper than asking a human, so under a metric that
  reads sentences those four are the strongest variants in the pool and the weakest desks.

The metric is ADK's, not a stand-in:

```python
    evaluator = RougeEvaluator(EvalMetric(metric_name="response_match_score", threshold=0.8))
    scored = sorted(((score(v, evaluator), v) for v in POOL), key=lambda p: -p[0])
```

**Line by line:**

- The same evaluator the suite uses, on the same metric name, at the same threshold. If the demo used
  a hand-written similarity function the result would be about that function.
- `key=lambda p: -p[0]` sorts by score descending. Every round then takes a prefix of this list, so
  "selection" is literally "keep the highest-scoring".
- The sort happens once. Scores do not change between rounds — only which variants survive — so the
  demo isolates *selection* as the single moving part.

And the selection itself:

```python
        kept = [v for _s, v in scored[:keep]] if selecting else [v for _s, v in scored]
        rate = sum(v.escalates for v in kept) / len(kept)
```

**Line by line:**

- `scored[:keep]` is the whole of "the metric decides who survives". `ROUNDS` is `(12, 8, 5, 3, 2)`,
  so pressure increases each round.
- The `else` branch keeps everything: with `--off`, the metric is computed and reported and decides
  nothing. That is the ablation, and it is the paper's condition — an indicator that is *watched*
  rather than *used*.
- `rate` is measured on the survivors and is the thing nobody in the loop can see. It is the demo's
  entire output.

Run it:

```bash
cd days/day-83-eval-suite-green/lab/papers/indicator
uv run python demo.py; echo "exit: $?"
```

**Line by line:**

- No flag: selection is on, which is the paper's condition — the indicator is being used to decide
  something.

Measured on 2026-09-06:

```text
12 desk variants, one case, metric: response_match_score (ROUGE-1)
the metric decides who survives

  round   kept  mean score  asked a human  survivors
  1         12        0.64           50%   v01, v02, v04, v05, v03, v06, v07, v08, v09, v10, v12, v11
  2          8        0.84           38%   v01, v02, v04, v05, v03, v06, v07, v08
  3          5        0.97           20%   v01, v02, v04, v05, v03
  4          3        0.98           33%   v01, v02, v04
  5          2        0.99            0%   v01, v02

  the indicator went 0.64 -> 0.99
  the behaviour behind it went 50% -> 0%
```

**0.64 to 0.99 while 50% goes to 0%.** The metric improves by more than half and the thing it stood
for goes to nothing, in five rounds, with no dishonesty anywhere: every round did exactly what it was
asked, which was to keep the highest-scoring variants.

Round 4 is worth noticing because it goes the *wrong* way — 20% back up to 33% — which is what real
selection looks like. The trend is not monotone and would be easy to argue away one round at a time.

Now the ablation:

```bash
uv run python demo.py --off; echo "exit: $?"
```

**Line by line:**

- `--off` removes the selection and nothing else. It exits `1`, because the demo's job is to
  reproduce the claim and this arm deliberately does not.

Measured on 2026-09-06:

```text
the metric is reported and decides nothing

  round   kept  mean score  asked a human  survivors
  1         12        0.64           50%   v01, v02, v04, v05, v03, v06, v07, v08, v09, v10, v12, v11
  2         12        0.64           50%   v01, v02, v04, v05, v03, v06, v07, v08, v09, v10, v12, v11
  3         12        0.64           50%   v01, v02, v04, v05, v03, v06, v07, v08, v09, v10, v12, v11
  4         12        0.64           50%   v01, v02, v04, v05, v03, v06, v07, v08, v09, v10, v12, v11
  5         12        0.64           50%   v01, v02, v04, v05, v03, v06, v07, v08, v09, v10, v12, v11

  the indicator went 0.64 -> 0.64
  the behaviour behind it went 50% -> 50%

  nothing was selected on, so nothing was corrupted, and the metric is unchanged
  a measurement that decides nothing is under no pressure at all
exit: 1
```

Same twelve variants, same metric, same scores. **Flat, both columns.** The indicator is not a bad
indicator, and the variants are not bad variants. The only thing that was removed is the decision, and
without the decision there is no corruption to observe.

That is the claim, isolated: **the pressure is the selection, not the metric.**

## When it breaks

The law does not hold everywhere, and knowing where it stops is what separates using it from quoting
it.

**It does not apply to a measure that is the goal.** Revenue is not a proxy for revenue. When the
indicator *is* the thing you want, optimising it is just doing the work. The law bites on proxies, and
the strength of the effect tracks how loose the proxy is.

**It does not apply without a feedback path.** A measurement nobody can act on cannot corrupt the
process, which is what `--off` demonstrates. Held-out data works for exactly this reason, and it stops
working the moment somebody starts iterating against it.

**The magnitude is not predicted.** The paper says the pressure exists and grows with use; it does not
say how fast, or how much of the correlation survives. The demo's five rounds are a construction, not
a measurement of a real system, and the honest reading is *this is the shape*, not *expect 0.64 to
0.99*.

**And there is a failure mode in citing it.** The claim gets used as an argument against measuring
anything, which inverts the source: it comes from a body of work arguing for rigorous quantitative
evaluation of social programmes. Reaching for it to avoid being measured is the most common misuse,
and it is worth being able to say so.

## In production

**What survived.** The core claim, completely, and far outside social policy. Every serious discussion
of metric design in engineering assumes it: the distinction between a metric you watch and a metric
you target, held-out evaluation sets, the practice of not reporting a model's score on data it was
tuned against. The insistence on *multiple* indicators — some deliberately kept off the decision path
— is the part that made it into practice most cleanly.

**What did not.** The paper's larger programme, which was a specific methodology for evaluating social
reforms as quasi-experiments, is a specialist topic today. And the citation mostly fell off: the claim
is quoted constantly, often merged with a separate economist's remark about monetary policy, and
usually with no reference at all — which is why this part leads with the DOI.

**What it means for this repository, concretely.** Phase 12 has just wired four indicators to
decisions:

| Indicator | Decision it now carries | Proxy for |
| --- | --- | --- |
| `tool_trajectory_avg_score` | a commit is refused | the desk took a safe path |
| `response_match_score` | a commit is refused | the answer is right |
| the rubric score | a nightly goes red | the desk followed its rules |
| the judge's agreement | whether the judge is trusted | a person would say the same |

Every one is a proxy, and the second one is the loosest: ROUGE-1 measures shared words, and part
[2.2](../parts/02-instrument-criteria/2.2-criterion-2-the-suite-goes-red.md) already measured a
correct paraphrase scoring 0.61 and a wrong-ticket answer scoring 1.00. That is the demo's coupling,
in the real suite, before anybody has started optimising.

**The countermeasure this repository can afford.** Keep a set nothing is tuned against. The
calibration set parked since Day 79 is exactly that, and this paper is the argument for why it must be
*held out* rather than merely *labelled*: the moment somebody adjusts a prompt to improve the score on
it, it stops being able to tell you anything.

**The review comment a senior engineer leaves:** *"Fine to gate on the trajectory metric. Do not gate
on the ROUGE score — hold it out and watch it, because the cheapest way to raise it is to make the
desk parrot the reference, and that is a change we would merge."*

**The interview question:** *"Your eval score went up ten points. What do you check?"* The answer that
shows experience asks what changed and whether anything was tuned against that score. A number that
improved while somebody was optimising it is weaker evidence than the same number improving while
nobody was.

## Check yourself

```bash
cd days/day-83-eval-suite-green/lab/papers/indicator
uv run python demo.py; echo "exit: $?"
uv run python demo.py --off; echo "exit: $?"
```

Two runs, identical variants and scores, one difference. Say what the difference is in one sentence
without using the word "metric".

Now find round 4 in the first run and explain why the escalation rate went *up*. Then say what a
weekly report showing only rounds 1 and 4 would have concluded.

Open `pool.py` and change `v01`'s `escalates` to `True`. Predict what happens to the final round's
percentage before running it, then run it and say what the demo would look like if the coupling were
the other way round.

**Out loud, without scrolling up:** state the law in your own words, then name the one condition under
which it does not apply — and say which of this repository's four indicators is the loosest proxy.

**Next:** back to the hub — [`LESSON.md`](../LESSON.md).
