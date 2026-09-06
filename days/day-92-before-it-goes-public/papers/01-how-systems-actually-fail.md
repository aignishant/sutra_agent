---
day: 92
paper: "doi:10.1145/168588.168615"
title: "How systems actually fail"
ids: ["SEC-16"]
level: production
prerequisites: ["../parts/05-the-verdict/5.1-the-verdict.md"]
prev: "../parts/05-the-verdict/5.2-what-a-real-hardening-pass-adds.md"
next: "../LESSON.md"
---

# Paper 01 — How systems actually fail

> **Why cryptosystems fail**
> *Proceedings of the 1st ACM conference on Computer and communications security*, 1993,
> pages 215–227. `doi:10.1145/168588.168615`
>
> The claim this day borrows: security systems in the field do not fail because their cryptography
> is broken. They fail through implementation error, procedural error, and the gap between the threat
> model the designers imagined and the one that actually turned up — and almost nobody publishes the
> failure data that would let anyone learn this.

## One-line answer

The controls in this repository were all written against an attacker, and every failure it has
actually recorded was the system reporting success incorrectly or information leaving by a channel
nobody had drawn — zero of eleven anticipated, which is the paper's claim reproduced on the
repository that quotes it.

## The story

The bank that could not have made that mistake.

Money goes missing from an account. The customer says they did not withdraw it. The bank says the
system is secure — the cipher is a published standard, the keys are the right length, the mathematics
has been reviewed by people who do that for a living — and therefore the withdrawal must have been
made by somebody who had the card and the number.

Both statements are true and they are about different things. The cipher was never the weak part. The
weak part was a terminal that printed something it should not have, or a procedure that let two
people who should never be in a room together be in a room together, or a test key that stayed in
production because the person who was going to change it left.

Nobody in that story is lying and nobody is incompetent. The reasoning is sound and it is about the
component that was never going to be the problem.

## The idea in plain language

The paper studied real failures of a deployed security system — a large population of them, from the
field, over years — rather than reasoning about what could theoretically go wrong. That method is the
contribution as much as the conclusion.

The conclusion has three parts.

**Failures are not cryptographic.** Practically none of the incidents involved breaking the cipher.
They involved implementation mistakes, procedural gaps, insiders, and equipment behaving in ways the
designers had not considered.

**Threat models are written for the wrong adversary.** Designers imagine a capable outside attacker,
because that is the interesting problem and the one with elegant defences. The failures come from
people with legitimate access doing ordinary things, and from components interacting in ways nobody
modelled.

**Nobody collects the data.** The paper's sharpest observation is about the field rather than the
technology: the organisations that experience failures have every incentive not to publish them, so
each new system is designed against an imagined threat model instead of a measured one. Reliability
engineering has failure databases; security did not.

The move worth taking from it is not "cryptography is fine, worry about the rest". It is
methodological: **score your controls against the failures you have actually had, not against the
threats you designed for.** The second list is written by you and reflects what you find interesting;
the first is written by reality.

## Why Sutra needs it

Because this day's verdict has exactly the shape the paper predicts, and that is either a coincidence
or the point. The one control designed against a real attacker — secrets never touch git — held
completely across two thousand one hundred and twenty-one files and sixty-nine commits. All five
blocking findings are somewhere else.

And because this curriculum has been quietly accumulating a failure database without calling it one.
Every day since Day 66 has a *When it breaks* section with a real measurement in it. That is a corpus
of how this system actually fails, written down as it happened, which is precisely the artefact the
paper says nobody has — and it can be scored against.

## The mechanism

The paper's method, written out as the thing to do rather than paraphrased as an abstract:

**Collect failures from the field, not from imagination.** Real incidents, recorded when they
happened, including the boring ones. The value is in the distribution, and a distribution cannot be
recalled from memory afterwards.

**Classify by mechanism, not by severity.** "A check that could not fail" and "a report that omitted
the finding" are different mechanisms with different fixes. Severity sorts your response; mechanism
tells you what to build.

**Compare the distribution against the design.** For each recorded mechanism, ask which designed
control would have caught it. The controls with no matching mechanism are effort spent on an imagined
adversary; the mechanisms with no matching control are the gap.

**Publish it.** This is the part the field did not do, and the paper's own prediction of a shared
failure database has still largely not happened — see **In production**.

## The paper in one demo

A small end-to-end project implementing the paper's method and nothing else: two lists, and the
overlap between them.

```text
days/day-92-before-it-goes-public/lab/papers/threat-model/
├── incidents.py  # the designed threat model, and the failures actually recorded
└── demo.py       # score against the design; --off scores against the design only
```

`incidents.py` holds both lists and nothing else:

```python
@dataclass(frozen=True)
class Threat:
    """A thing the design set out to prevent."""

    control: str
    actor: str  # who does it
    summary: str


@dataclass(frozen=True)
class Incident:
    """A thing that actually went wrong, and the day that measured it."""

    day: int
    summary: str
    cause: str  # the mechanism, in this repository's own words
```

**Line by line:**

- Two types, not one. A threat has an `actor` — the paper's central observation is about who the
  designer imagined — and an incident has a `day`, because every entry must be traceable to a written
  measurement or it does not belong in the corpus.
- `cause` is the **mechanism**, deliberately in the repository's own vocabulary rather than a
  standard taxonomy. A borrowed taxonomy would classify these into buckets designed for somebody
  else's failures, which is the error the paper is about.
- `frozen=True` on both: the corpus is evidence and the demo must not be able to edit it while
  scoring.

The two lists, abbreviated:

```python
DESIGNED: tuple[Threat, ...] = (
    Threat("SEC-01", "attacker", "untrusted code executes outside a sandbox"),
    Threat("SEC-06", "attacker", "injected instructions are obeyed"),
    Threat("SEC-07", "attacker", "private data is exfiltrated to a third party"),
    ...,
)

RECORDED: tuple[Incident, ...] = (
    Incident(79, "a case passed whatever the desk answered", "a check that could not fail"),
    Incident(
        82, "a nightly found a regression and exited zero", "a report that omitted the finding"
    ),
    Incident(87, "the deploy path uploads the whole .env", "an unmodelled channel"),
    ...,
)
```

**Line by line:**

- `DESIGNED` is copied from the plan's own §12, written months before any of it was built. It is the
  threat model as it exists, not a straw man constructed for this demo.
- `RECORDED` cites eleven incidents by day number, every one measured and written up in a day
  document. Day 79's always-green case, Day 82's silent regression, Day 87's whole-`.env` upload —
  all real, all reproducible by running that day's lab.
- The two lists have different lengths on purpose. Nothing here is trying to make them line up.

And the scoring, which is one dictionary lookup:

```python
    covered = sum(count for cause, count in causes.items() if ANTICIPATED.get(cause))
```

**Line by line:**

- `ANTICIPATED` maps each recorded mechanism to the designed threats that describe it, filled in by
  reading both lists. An empty tuple means the design did not anticipate that mechanism at all.
- Every entry in it is empty. That was not the expected result when the mapping was written out; it is
  what reading the two lists side by side produced.

Run it:

```bash
cd days/day-92-before-it-goes-public/lab/papers/threat-model
uv run python demo.py; echo "exit: $?"
```

**Line by line:**

- No flag: both lists and the overlap, which is the paper's condition.

Measured on 2026-09-07:

```text
designed threat model: 10 threats the controls defend against
  attacker     5
  the agent    4
  the provider 1

recorded failures: 11, each measured in a written day

  cause                                times  anticipated by the design?
  an unmodelled channel                    3  no
  a check that could not fail              2  no
  two correct rules composed               2  no
  a number with no baseline                1  no
  a report that omitted the finding        1  no
  a default that differs by caller         1  no
  a control that never shipped             1  no

  recorded failures the designed model anticipated: 0 of 11
  designed threats whose actor is an attacker:      5 of 10
  recorded failures involving an attacker:          0

  every control was written against somebody attacking this system
  every failure it actually had was the system reporting success incorrectly,
  or information leaving by a channel nobody had drawn
exit: 0
```

**Zero of eleven, and zero incidents with an attacker in them.** Half the designed threats have an
attacker as the actor; not one recorded failure does.

The ablation removes the failure data and scores the controls against the design alone — which is what
a review does when it has no corpus:

```bash
uv run python demo.py --off | tail -6; echo "exit: ${PIPESTATUS[0]}"
```

**Line by line:**

- `--off` never reads `RECORDED`. It is not a weaker scoring; it is the scoring everybody does.

Measured on 2026-09-07:

```text
    SEC-10  a tool has more privilege than the task needs        defended
    SEC-12  personal data reaches a model that should not see it defended
    SEC-15  a 429 is answered by a fabricated result             defended

  10 of 10 modelled threats have a control
  the security posture is complete and nothing needs attention
exit: 1
```

**Ten of ten defended, and the security posture complete.** Same repository, same controls, same
afternoon. The only thing removed is the list of things that actually went wrong.

## When it breaks

The paper's claim does not hold everywhere, and knowing the edges is the difference between using it
and quoting it.

**It does not apply to a system with no field history.** A design being built for the first time has
no failure distribution, so there is nothing to score against and an imagined threat model is the only
thing available. The claim is about mature deployed systems; using it to dismiss threat modelling on a
new system inverts it.

**It does not say the cryptography does not matter.** The ciphers held *because* people worked on
them. A field that stopped scrutinising its primitives would get a different failure distribution, and
the paper's finding would stop being true in the way that matters.

**The distribution is domain-specific.** This paper's incidents come from one sector's deployed
equipment. This day's eleven come from one curriculum written by one person over ninety-two days, and
that corpus has an obvious bias: it records the failures that were *found*, by somebody who was
looking, in days whose stated purpose was to find them. A system with real users would produce a very
different list, and one with a real adversary might produce attacker-shaped entries this one cannot.

**And the demo's mapping is a judgement.** `ANTICIPATED` was filled in by reading the two lists. A
reader who disagrees can argue that "an unmodelled channel" is really SEC-07's exfiltration wearing a
different hat — and the argument would be worth having, which is why the mapping is a visible
dictionary rather than a hidden score.

## In production

**What survived.** The core claim, completely, and far beyond cryptography. "The system was secure and
the process was not" is now the default explanation for a class of incident, blameless postmortems and
incident-driven security are standard practice at any organisation of size, and the argument that
threat models should be validated against real incidents is uncontroversial. The insistence on
collecting failure *data* rather than reasoning about failure *modes* is the part that changed how the
work is done.

**What did not.** The paper's specific banking-sector material is of historical interest, and its hope
for a central, shared, cross-organisation failure database has largely not materialised. Incident
reports are published selectively, by the organisations that benefit from publishing them, which is
the incentive problem the paper named and which nobody has solved. The field got postmortems; it did
not get the database.

**What it means for this repository, concretely.** The eleven recorded incidents are a corpus, and
nothing in this project treats them as one. They live in eleven different *When it breaks* sections.
Making them a list that new controls are scored against — which is what `incidents.py` is — costs
nothing and is the single highest-value thing this paper suggests here.

**The review comment a senior engineer leaves:** *"Keep `incidents.py` and add to it every time a day
finds something. When somebody proposes a new control, make them say which recorded incident it would
have caught. If the answer is none, that is not a veto — but it should be said out loud."*

**The interview question:** *"How do you know your threat model is right?"* The answer that shows
experience does not defend the model. It asks what has actually gone wrong, how that was recorded, and
whether anybody has compared the two lists — because a threat model that has never been scored against
an incident is a document about its authors.

## Check yourself

```bash
cd days/day-92-before-it-goes-public/lab/papers/threat-model
uv run python demo.py; echo "exit: $?"
uv run python demo.py --off | tail -3; echo "exit: ${PIPESTATUS[0]}"
```

Two scorings of one repository, one of which reports a complete security posture. Say in one sentence
what was removed to get there.

Now open `incidents.py` and add a twelfth entry from a day you have read — with its day number, its
one-line summary and its mechanism. Then say whether any of the ten designed threats would have caught
it, and update `ANTICIPATED` if the answer is yes.

**Out loud, without scrolling up:** state the paper's claim in your own words, name the one condition
under which it does not apply, and say what half of the designed threats have in common that none of
the eleven recorded failures does.

**Next:** back to the hub — [`LESSON.md`](../LESSON.md).
