---
day: 75
paper: "doi:10.2307/412243"
title: "A simplest systematics for the organization of turn-taking for conversation"
ids: ["ADK-54"]
level: production
prerequisites: ["../parts/02-talking-over/2.1-the-caller-interrupts.md"]
prev: "../parts/04-what-it-costs/4.3-what-a-real-voice-system-adds.md"
next: "../LESSON.md"
---

# A simplest systematics for the organization of turn-taking for conversation

> *A simplest systematics for the organization of turn-taking for conversation* ·
> `doi:10.2307/412243` · Language, Volume 50, Issue 4, pages 696–735, December 1974 · Cambridge
> University Press · <https://doi.org/10.2307/412243>

> Record checked live on 2026-09-06 via `https://api.crossref.org/works/10.2307/412243`. The title,
> journal, volume, issue, pages, year and publisher above are copied from that record, which carries
> **no subtitle** — unlike the last two papers in this curriculum, this title is one field. The record
> does carry an abstract, and the paragraph quoted below is from it verbatim rather than paraphrased.
> Where this document states the paper's rule set, it states it as **the field cites it**, and says so.

## One-line answer

Two people manage a conversation with no schedule, no chair and no clock, and they do it with gaps
and overlaps so short that the coordination looks like magic — and the paper's answer is that nothing
is allocated in advance at all: turns are decided **locally**, at each point where the current one
could end. Switching that off in the demo below turns a six-exchange call from **0 gaps** into **3
gaps and 2 overlaps**, on identical intentions.

## The story

Four of you are sitting round a table and the conversation is going well.

Nobody is chairing it. There is no list, no order, nobody saying *"and now Ravi"*. And yet almost
nobody talks over anybody, the silences are short enough that you would not call them silences, and
when two people do start at once one of them stops almost immediately and the other carries on. It
happens dozens of times an hour and none of you notice any of it.

Now think of the same four people in a meeting with a speaking order agreed at the start. Somebody
whose turn it is has nothing to add, so there is a pause while everyone waits for them to decline.
Somebody else thought of the important thing two turns ago and has been holding it ever since. It is
more organised and it is much worse, and the reason is not that the order was badly chosen. It is
that it was chosen at all, in advance, by somebody who could not know what anyone would want to say.

## The idea in plain language

Here is the abstract as the record carries it, quoted rather than summarised:

> *"The organization of taking turns to talk is fundamental to conversation, as well as to other
> speech-exchange systems. A model for the turn-taking organization for conversation is proposed, and
> is examined for its compatibility with a list of grossly observable facts about conversation. The
> results of the examination suggest that, at least, a model for turn-taking in conversation will be
> characterized as locally managed, party-administered, interactionally controlled, and sensitive to
> recipient design. Several general consequences of the model are explicated, and contrasts are
> sketched with turn-taking organizations for other speech-exchange systems."*

Four adjectives in the middle of that sentence are the whole result, and each one is a constraint a
voice loop either satisfies or does not:

| The paper's word | What it means | What it rules out |
| --- | --- | --- |
| locally managed | decisions are made at each transition, not for the conversation as a whole | a schedule |
| party-administered | the people talking decide, not a third thing | a coordinator |
| interactionally controlled | who speaks next depends on what just happened | a fixed rota |
| sensitive to recipient design | what is said is shaped for who is listening | a broadcast |

The mechanism the field cites for the first three is a rule set applied at each **transition-relevance
place** — a point at which the current turn could end. In the order it is usually stated:

1. If the current speaker has selected the next speaker, that party speaks.
2. Otherwise, any party may self-select, and the first to start gets the turn.
3. Otherwise, the current speaker may continue.

That is it. Three rules, applied by the parties themselves, at a point they each recognise, with no
information beyond what has just been said. And two consequences fall straight out of it, both of
which this day has already met in code.

**Overlap is produced by the rules, not by their failure.** Rule 2 lets anybody start, so when two
people want the floor they both start, and one of them stops. Part
[2.2](../parts/02-talking-over/2.2-the-event-that-says-stop.md) treated an interruption as a normal
event rather than an error for exactly this reason — and the demo below reports one overlap on its
*passing* run, because a system built on rule 2 is supposed to produce them.

**And the mechanism needs a shared idea of where a turn could end.** Rules 1 and 2 both fire at a
transition-relevance place, so the parties have to agree, moment by moment, on where those are. That
is precisely the question part
[3.2](../parts/03-what-goes-down-the-wire/3.2-who-says-the-turn-ended.md) put to a microphone: is this
pause the end of a sentence, or a breath?

## Why Sutra needs it

Because this day built a turn-taking system without ever calling it one, and it is worth seeing that
the design decisions were not arbitrary.

The lab's connection checks for an interruption **between chunks** — part 2.1 explained that as "there
is no way to un-say half a word". The paper's name for that is a transition-relevance place. The lab
lets the caller speak at any moment and the model yield when they do — the paper calls that
party-administered. And part 3.2's turn markers are an attempt to make transition points explicit
because a machine cannot reliably find them the way a person can.

There is also a warning in it, and it is the reason this paper is worth a document rather than a
citation. A voice assistant is **not** a party in the paper's sense. It has no rights to the floor,
only obligations: it must yield instantly and always, and it never self-selects. That is a deliberate
and probably correct design, and it means the elegant symmetry the paper describes does not apply to
the system you are building — which is worth knowing before you reach for the paper as a blueprint.

## The mechanism

The paper's rule set, written as code, is one function:

```python
    def local(self, moment: Moment, rng: random.Random) -> None:
        """The paper's rules, applied at one transition point."""
        if moment.selects is not None:
            self.speaker = moment.selects
        elif moment.wants:
            # Self-selection. More than one starter is an overlap, and it resolves immediately -
            # which is what the paper's "first starter gets the turn" amounts to in practice.
            if len(moment.wants) > 1:
                self.overlaps += 1
            self.speaker = rng.choice(moment.wants)
        # else: nobody was selected and nobody wanted the floor, so the current speaker continues.
        self.turns.append(self.speaker)
```

**Line by line:**

- The three branches are the three rules, in order, and the order is the mechanism: rule 1 beats rule
  2 beats rule 3. Reordering them produces a different and worse system, which is a good way to see
  that the ordering is a claim rather than an implementation detail.
- `moment.selects is not None` is rule 1 — the current speaker named somebody. Note it is `is not
  None` rather than a truthy test, for the reason Day 72 part 2.3 measured: a legitimate value and an
  absent one must not collapse into the same branch.
- `if len(moment.wants) > 1: self.overlaps += 1` counts an overlap **and then carries on**. Overlap is
  recorded, not prevented, because rule 2 does not prevent it — it resolves it.
- `rng.choice(moment.wants)` stands in for "the first to start". Which of two simultaneous starters
  wins is not something the rules determine, and modelling it as a coin toss is honest about that.
- The missing `else` is rule 3, and the comment is there because an absent branch is invisible: when
  nobody is selected and nobody wants the floor, `self.speaker` is simply left alone and the current
  speaker continues. That is a rule expressed by not writing anything, which is worth pointing at.

And the arrangement the paper contrasts itself with:

```python
    def scheduled(self, moment: Moment) -> None:
        """The contrast: the floor passes to the next party on the rota, whatever anybody wants."""
        nxt = self.parties[(self.parties.index(self.speaker) + 1) % len(self.parties)]
        # Somebody was chosen and did not want the floor: that is silence where a turn should be.
        if nxt not in moment.wants and moment.selects != nxt:
            self.gaps += 1
        # Somebody wanted the floor, was not given it, and speaks anyway.
        for party in moment.wants:
            if party != nxt:
                self.overlaps += 1
        self.speaker = nxt
        self.turns.append(self.speaker)
```

**Line by line:**

- `(index + 1) % len(self.parties)` is the entire allocation policy: next, in order, always. It reads
  the rota and nothing else — not who was selected, not who wants to speak.
- The gap test asks whether the party being handed the floor actually wanted it. Handing the floor to
  somebody with nothing to say is silence, and it is the characteristic cost of allocating in advance.
- The overlap loop counts everybody who wanted the floor and did not get it, on the assumption that
  they speak anyway. That is an assumption of the model rather than a finding, and it is the least
  defensible line in the file — a perfectly disciplined party would stay quiet, and the cost would
  show up as an unsaid thing instead, which is harder to count and arguably worse.

## The paper in one demo

Two files. One short call, run under the rules and under a rota.

```text
lab/papers/turn-taking/
├── floor.py   # the three rules, the rota, and the one switch
└── demo.py    # six transition points, run both ways
```

The conversation, which is identical in both runs:

```python
CALL = [
    Moment(selects="desk", wants=()),  # the caller asks the desk a direct question
    Moment(selects=None, wants=("desk",)),  # the desk keeps going, and wants to
    Moment(selects=None, wants=("caller", "desk")),  # both start at once
    Moment(selects="caller", wants=()),  # the desk hands back explicitly
    Moment(selects=None, wants=()),  # a pause; nobody has anything to add
    Moment(selects="desk", wants=()),  # the caller asks one more thing
]
```

**Line by line:**

- Each `Moment` is one transition-relevance place, described by what the parties *want* rather than by
  what happens. That separation is what lets the same call be run under two different allocation
  policies: the intentions are fixed, and only the rules change.
- The third moment is rule 2 with two starters, which is the overlap the passing run reports.
- The fifth is rule 3: nobody selected, nobody wanting, so whoever is talking carries on. Under a rota
  it is a silence, and that is the clearest single row in the comparison.
- `selects` and `wants` are deliberately not symmetric — one names a party, the other is a set —
  because rules 1 and 2 are different kinds of thing. Rule 1 is an instruction; rule 2 is a
  free-for-all with a tie-break.

With the paper's rules:

```bash
cd days/day-75-the-bidi-voice-loop/lab/papers/turn-taking
uv run python demo.py; echo "exit: $?"
```

**Line by line:**

- `cd` first: `demo.py` imports `floor` by plain name, so the working directory has to be the demo's
  own folder.
- `echo "exit: $?"` prints the exit code, because the claim is the exit code — and the claim being
  tested is about gaps, not about overlaps.

Measured on 2026-09-06:

```text
turn allocation: local, by the parties
6 transition points, identical in both runs

  turns taken       6
  gaps              0
  overlaps          1

  who spoke: ['desk', 'desk', 'caller', 'caller', 'caller', 'desk']

  No silences. Nobody was ever handed the floor with nothing to say, because
  nothing was allocated in advance - every turn was settled at the moment it had
  to be, by the two people who were there.

  The 1 overlap is the rules working rather than failing: two
  parties self-selected at the same moment, and a moment later one of them had
  the floor.
exit: 0
```

Now the rota — same call, same intentions, allocation decided in advance:

```bash
uv run python demo.py --off; echo "exit: $?"
```

**Line by line:**

- `--off` sets `floor.LOCAL = False`, which swaps the rule set for the rota and changes nothing else.

Measured on 2026-09-06:

```text
turn allocation: central rota (ablation)
6 transition points, identical in both runs

  turns taken       6
  gaps              3
  overlaps          2

  who spoke: ['desk', 'caller', 'desk', 'caller', 'desk', 'caller']

  3 silences, where the rota gave the floor to somebody with
  nothing to say, and 2 collisions, where somebody who did
  have something spoke anyway. The rota is not badly designed. It is designed in
  advance, which is the one thing a conversation will not let you do.
```

| | the paper's rules | a central rota |
| --- | --- | --- |
| turns taken | 6 | 6 |
| gaps | **0** | 3 |
| overlaps | 1 | 2 |
| exit code | 0 | 1 |

**The turn count is the same in both.** Six transition points, six turns; the rota is not doing less
work or serving fewer people. What it produces is three silences and an extra collision, and it
produces them from the same intentions, which is the point of holding everything else fixed.

Look at the `who spoke` rows together, because they carry the argument better than the counts do. The
rota's is `['desk', 'caller', 'desk', 'caller', 'desk', 'caller']` — perfectly regular, obviously
fair, and clearly not a conversation. The rules produce `['desk', 'desk', 'caller', 'caller',
'caller', 'desk']`, where somebody sometimes speaks twice running and sometimes three times, and that
irregularity is not a defect. It is what following what people actually want looks like.

## When it breaks

**Not everything is a conversation, and the paper says so.** Its abstract ends by sketching contrasts
with "other speech-exchange systems", and that is a real limit rather than a caveat: meetings,
interviews, ceremonies and courtrooms genuinely do pre-allocate turns, and they are not badly designed
for doing so. A voice system with a fixed script — asking three questions in order — is one of those,
and the rota this demo mocks is the right design for it. What the paper's model is about is
*conversation*, and building an assistant you can interrupt is a claim that you are building one.

**A machine is not a party.** The rules are symmetric, and a voice assistant is not: it yields
absolutely, self-selects never, and cannot decline the floor. That asymmetry is deliberate — nobody
wants an assistant that talks over them because it self-selected — but it means the paper describes a
system with one more degree of freedom than the one you are building. Rule 2, the interesting one,
barely applies when only one party is ever allowed to start.

**And this demo is a simulation of a rule set, not evidence about people.** The gaps and overlaps come
from a hand-written list of intentions, and both figures move if the list changes. Nothing here
measured a conversation. What it does establish, and it is worth having, is that the difference
between the two policies is produced by the *policies* — the intentions were byte-identical in both
runs — rather than by the example being unkind to the rota.

**One line in the code is the weakest claim in the file.** The rota's overlap count assumes that
somebody who wanted the floor and was not given it speaks anyway. A more disciplined party would wait,
and the cost would move from an overlap to an unsaid thing. That is a modelling choice, it is called
out in the walkthrough above, and a reader who disagrees with it should change it and re-run — the
gap count, which is what the exit code tests, does not depend on it at all.

## In production

**What survived, in linguistics: nearly all of it.** The paper founded a field. Its vocabulary — turn,
transition-relevance place, overlap, repair, self-selection — is the working language of conversation
analysis, and its central claim, that turn allocation is local rather than pre-planned, is not
seriously disputed.

**What survived, in technology: the design, mostly without the citation.** Every voice interface that
can be interrupted is built on the assumption that the floor is negotiated moment by moment. So is
every endpointing decision, every barge-in implementation, and the entire industry practice of
treating an interruption as a normal event rather than an error. Very few of the people building those
could name the paper, which is the usual fate of a result that becomes obvious.

**What did not survive is the symmetry**, and it is worth being precise about how it was dropped
rather than saying the field ignored it. Human turn-taking gives every party the same rights and
obligations. Voice systems give the machine obligations only — always yield, never self-select, never
hold the floor against a person — and this is not an oversight. It is a safety and courtesy decision
that most people would defend. But it means the mechanism deployed in products is a **deliberately
crippled version** of the one the paper describes, and knowing which half was removed is the
difference between applying a result and cargo-culting it.

**What a professional takes from it into a design review.** Three questions, none of which are obvious
without the paper. Where are the transition-relevance places in my system, and does the client agree
with the server about them? What happens when both parties start at once — is it handled, or is it an
error? And is this a conversation or a form, because a form should pre-allocate and a conversation
should not, and building one while believing you are building the other is where voice interfaces go
wrong.

**The review comment a senior engineer leaves:** *"Two things to write down before this is a design.
Where do we think a turn can end — is that the client's decision, the model's, or both, and what
happens when they disagree? And what do we do when the caller and the assistant start at the same
moment: the assistant should always lose, and I want that stated somewhere rather than emerging from
whichever code path runs first. Also be clear which of our flows are conversations and which are
forms. The three-question intake is a form; pre-allocating turns there is correct and interrupting it
is the thing we should be preventing."*

**The interview question:** *"How should a voice assistant decide when to speak?"* An honest answer:
*"There's a 1974 paper on human turn-taking that's the reference point, and its result is that nothing
is allocated in advance — turns are decided locally, at each point where the current one could end, by
the parties themselves. Three rules: if the speaker selected someone, they go; otherwise anyone can
start and the first one wins; otherwise the current speaker continues. Two things follow that matter
for building this. Overlap is produced by the rules rather than by their failure, so an interruption
is a normal event and not an error — which changes how you write the handler. And the rules need both
sides to agree on where a turn could end, which is the endpointing problem: is this pause a sentence
ending or someone thinking. The honest caveat is that a machine isn't a party in the paper's sense. We
give it obligations and no rights — always yield, never self-select — so what we deploy is a
deliberately asymmetric version of the model, and that's a good decision rather than an accident. I
ran a simulation of both policies: the same six exchanges produced no silences under local management
and three under a fixed rota, which is a small thing but it's the whole argument for why the machine
shouldn't be working from a plan."*

## Check yourself

```bash
cd days/day-75-the-bidi-voice-loop/lab/papers/turn-taking
uv run python demo.py
uv run python demo.py --off
```

Add a seventh `Moment` in which the caller selects the desk *and* the desk already wants the floor.
Predict, before running it, which rule fires and whether the overlap count moves. Then say why rule 1
being first rather than second matters for that case.

Then take one flow from something you have built — an assistant, a form, a chat interface — and decide
whether it is a conversation or a form in this paper's sense. Write one sentence saying which, and one
saying what would go wrong if you built it as the other.

**Out loud, without scrolling up:** the passing run reported an overlap. Why is that not a failure,
and which of the three rules produced it?

---

That is the day, and Phase 11's second half. The nightly job ran while nobody was watching; this one
runs while somebody is talking, and can be talked over. Tomorrow the phase closes on both of them, in
free quota.

**Next:** [back to the hub](../LESSON.md).
