---
day: 76
paper: "doi:10.1002/j.1538-7305.1975.tb02840.x"
title: "An Algorithm for Determining the Endpoints of Isolated Utterances"
ids: ["ADK-56"]
level: production
prerequisites: ["../parts/03-deciding-when-they-stopped/3.1-the-knobs.md"]
prev: "../parts/04-in-production/4.2-what-a-real-one-adds.md"
next: "../LESSON.md"
---

# An Algorithm for Determining the Endpoints of Isolated Utterances

> *An Algorithm for Determining the Endpoints of Isolated Utterances* ·
> `doi:10.1002/j.1538-7305.1975.tb02840.x` · Bell System Technical Journal, Volume 54, Issue 2,
> pages 297–315, February 1975 · <https://doi.org/10.1002/j.1538-7305.1975.tb02840.x>

> Record checked live on 2026-09-06 via
> `https://api.crossref.org/works/10.1002/j.1538-7305.1975.tb02840.x`. The title, journal, volume,
> issue, pages and year above are copied from that record, which lists the publisher as IEEE — the
> Bell System Technical Journal's archive is distributed by them. **The record carries no abstract**,
> and this document has not read the full text. What it states about the method is the form in which
> the field carries it, and the section below says so in its own words rather than letting a
> confident paragraph imply a quotation.

## One-line answer

Finding where a word starts sounds like a question about loudness, and it is not: the first sound of
"safe" or "four" is **quieter than the room**. The method that fixed this uses energy to find a
confident interior and then a second, completely different measurement — how often the signal changes
sign — to walk outwards to the real edges. Switching that second pass off in the demo below clips
**8 frames** off a 24-frame word, four at each end.

## The story

You record a voice note to send to somebody, and you start talking as you press the button.

When you play it back it begins mid-word. Not by much — the app started recording the moment it heard
you, and what it heard was the vowel. The "s" you actually started with is not there. You listen to
it twice and it sounds like you began with a strange abrupt noise, and you re-record it, this time
pausing awkwardly before you speak.

Everybody has learned that pause. It is a habit people have developed to work around a piece of
software deciding, reasonably and wrongly, that the quiet part at the front of your sentence was not
you.

## The idea in plain language

Part [3.1](../parts/03-deciding-when-they-stopped/3.1-the-knobs.md) listed the settings a modern
system exposes for this: sensitivities at each edge, a silence duration, and a **prefix padding**
measured in milliseconds — audio kept from *before* the detected start. That last one is a
particularly clear admission. It exists because the detected start is known to be late.

Here is why it is late.

Speech is made of two quite different kinds of sound. **Voiced** sounds — vowels, and consonants like
"m" and "b" — are produced with the vocal cords vibrating, and they are loud and regular. **Unvoiced**
sounds — "s", "f", "sh", "th" — are produced by pushing air through a narrow gap, and they are noise:
quiet, hissy, and with no regular pattern at all.

An energy threshold has to sit above the room. An unvoiced sound can sit **below** the room. So a word
that begins or ends with one has an edge the energy measurement cannot see, and the beginnings and
endings of English words are full of them.

What those quiet sounds do have is a very high **zero-crossing rate**: the number of times the signal
crosses zero — changes sign — in a short window. A vowel is a slow wave and crosses rarely. Hiss
crosses constantly. So the two kinds of sound differ sharply on a measurement that has nothing to do
with volume, and that is the opening the method goes through.

**The method, as the field states it**, is two passes:

1. Find a confident interior from the energy. A high threshold marks what is unarguably speech; a
   lower threshold is then used to walk outwards while the signal is still plausibly speech, which
   catches the quiet tail of a vowel.
2. From those endpoints, search a **bounded** distance further out, extending across any frame whose
   zero-crossing rate is above a threshold. Those frames are noise-like — which, next to a word, means
   they are part of it.

The bound on the second search is not a detail. Without it, a noisy microphone extends the word across
the entire recording, because room noise is also noise-like.

## Why Sutra needs it

Because this day spent section 3 turning knobs whose names only make sense once you know this. A
setting called `prefix_padding_ms` is a blunt version of the second pass: rather than finding the real
edge, keep a fixed amount of whatever came before it and hope. A setting called
`start_of_speech_sensitivity` is the first pass's threshold, exposed. The 1975 method is what those
settings are approximating, and knowing that changes what you do when a caller complains that the
system keeps clipping the first word off their sentences.

And because it is the sharpest available example of a lesson this curriculum keeps arriving at from
other directions: **when one measurement cannot separate two things, the answer is usually a second
measurement of a different kind, not a better threshold on the first.** Day 70's router could not tell
a cold lane from a busy one by counting alone; Day 72 could not tell a refusal from a timeout by
status code alone. Tuning an energy threshold harder will never find an "s".

## The mechanism

The first pass, from `lab/papers/endpoints/detect.py`:

```python
def energy_endpoints(frames: list[Frame]) -> tuple[int, int]:
    """First pass: the confident interior, from the energy alone."""
    loud = [i for i, f in enumerate(frames) if f.energy >= ITU]
    if not loud:
        return (0, 0)
    start, end = loud[0], loud[-1]
    # Walk out while the energy is still above the lower threshold: the tail of a vowel is quieter
    # than its middle and is unarguably still the word.
    while start > 0 and frames[start - 1].energy >= ITL:
        start -= 1
    while end < len(frames) - 1 and frames[end + 1].energy >= ITL:
        end += 1
    return start, end
```

**Line by line:**

- `f.energy >= ITU` is the upper threshold: frames that are unarguably speech. Taking the first and
  last of them gives an interior that is certainly inside the word, which is a deliberately
  conservative starting point.
- The two `while` loops walk outwards on the **lower** threshold, `ITL`. Two thresholds rather than
  one is the first idea in the method: a high bar to decide *that* there is a word, and a low bar to
  decide *how far it extends*.
- `if not loud: return (0, 0)` is the no-speech case. Returning an empty span rather than raising is
  right here — silence is a normal input, not an error.
- Nothing in this function mentions zero crossings. Everything it can do, it does with loudness, and
  everything it cannot do is what the second pass is for.

The second pass is the paper's contribution:

```python
def refine(frames: list[Frame], start: int, end: int) -> tuple[int, int]:
    """Second pass: extend outward across frames that are noise-like rather than loud."""
    left = start
    for i in range(start - 1, max(-1, start - 1 - SEARCH), -1):
        if frames[i].crossings >= IZCT:
            left = i
    right = end
    for i in range(end + 1, min(len(frames), end + 1 + SEARCH)):
        if frames[i].crossings >= IZCT:
            right = i
    return left, right
```

**Line by line:**

- The left loop counts **downwards** from just before the interior, and the right loop counts upwards
  from just after it. Each assignment overwrites the last, so the final value is the furthest
  qualifying frame in that direction.
- `frames[i].crossings >= IZCT` is the whole test, and it says nothing about volume. A frame that is
  quieter than the room can still qualify, which is precisely the case an energy threshold cannot
  reach.
- `max(-1, start - 1 - SEARCH)` and `min(len(frames), end + 1 + SEARCH)` bound the search in both
  directions. `SEARCH` is the guard against walking out across a noisy room, and it is also a limit on
  how much of a long fricative can be recovered — a real trade rather than a safety belt.
- The frames between a qualifying frame and the interior are included whether or not they qualify,
  because the result is a *span*. A method that only kept qualifying frames would return holes, and a
  word with a hole in it is not a word.

## The paper in one demo

One synthetic utterance, with the second pass on and off.

```text
lab/papers/endpoints/
├── detect.py   # the two passes, the thresholds, and the one switch
└── demo.py     # a word that begins and ends with a quiet sound, run both ways
```

The frames, from `demo.py`:

```python
# The fricative's energy sits BELOW the lower energy threshold - that is the whole difficulty. What
# separates it from room noise is not how loud it is but how often the signal changes sign.
SILENCE = [Frame(energy=3, crossings=12)] * 8
FRICATIVE = [Frame(energy=5, crossings=60)] * 4
VOICED = [Frame(energy=90, crossings=15)] * 16
FRAMES = SILENCE + FRICATIVE + VOICED + FRICATIVE + SILENCE
```

**Line by line:**

- `FRICATIVE` has energy `5` against `SILENCE`'s `3`. Barely louder than the room and **below** the
  lower energy threshold of `8`, which is what makes it invisible to the first pass. This is the one
  number in the file that matters.
- Its `crossings` is `60` against silence's `12` and the vowel's `15`. On loudness the fricative
  resembles the silence; on zero crossings it resembles nothing else in the recording.
- `VOICED` is loud and slow-crossing, which is what a vowel is.
- The word is the fricative, the vowel and the fricative — a shape like "safes" or "faces". It was
  chosen because it is ordinary. An adversarial example would prove less.

Both passes:

```bash
cd days/day-76-vad-and-non-blocking-tools/lab/papers/endpoints
uv run python demo.py; echo "exit: $?"
```

**Line by line:**

- `cd` first: `demo.py` imports `detect` by plain name, so the working directory has to be the demo's
  own folder.
- `echo "exit: $?"` prints the exit code, because the claim is the exit code — the endpoints are
  exactly right, or they are not.

Measured on 2026-09-06:

```text
zero-crossing pass: ON
40 frames; the word occupies frames 8 to 31

  detected start     8   (true 8)
  detected end       31   (true 31)
  frames clipped     0

  frame: ............################............
  found:         ^^^^^^^^^^^^^^^^^^^^^^^^        
  truth:         ^^^^^^^^^^^^^^^^^^^^^^^^        

  Both edges found. The loud middle came from the energy pass; the quiet fricatives
  at each end were too quiet for it and were recovered by their zero-crossing rate.
exit: 0
```

Now with the second pass removed:

```bash
uv run python demo.py --off; echo "exit: $?"
```

**Line by line:**

- `--off` sets `detect.ZERO_CROSSINGS = False`. The frames, the thresholds and the energy pass are
  untouched.

Measured on 2026-09-06:

```text
zero-crossing pass: OFF (ablation)
40 frames; the word occupies frames 8 to 31

  detected start     12   (true 8)
  detected end       27   (true 31)
  frames clipped     8

  frame: ............################............
  found:             ^^^^^^^^^^^^^^^^            
  truth:         ^^^^^^^^^^^^^^^^^^^^^^^^        

  The loud middle was found and the quiet edges were not. Nothing errored: an energy
  threshold did exactly what an energy threshold does, and the first sound of the word
  is below it. On a live microphone this is the caller being cut off mid-word.
```

| | both passes | energy only |
| --- | --- | --- |
| detected start | **8** | 12 |
| detected end | **31** | 27 |
| frames clipped | **0** | 8 |
| exit code | 0 | 1 |

The three-line diagram is the argument better than the numbers are. The `frame:` row shows what an
energy threshold can see — sixteen loud frames and nothing else, with the fricatives rendered as dots
exactly like the silence. The `found:` and `truth:` rows in the ablation are visibly different
lengths, four frames short at each end.

**And nothing failed.** The energy threshold did exactly what an energy threshold does. The word was
found. The middle is correct. What is missing is the part of the word that was never loud, and there
is no error condition for that — which is why the fix had to be a second measurement rather than a
better threshold.

## When it breaks

**Zero-crossing rate is a good discriminator in a quiet room and a poor one in a noisy street.** The
whole method rests on speech-onset noise being distinguishable from background noise, and plenty of
background noise is also noise-like. The bounded search is the acknowledgement of this: it limits how
far a wrong answer can run, and it does not prevent one.

**The paper's setting is "isolated utterances" — it is in the title.** One word, with silence either
side, spoken deliberately at a machine. Continuous conversational speech, two people, a bad line and a
television in the background is a much harder problem, and this method is a component of a solution to
it rather than a solution.

**This demo is frames of made-up numbers, not sound.** No audio was processed. What it demonstrates is
that the *decision procedure* recovers edges the energy pass cannot, given frames with the properties
speech is known to have. That is a real demonstration of the method's logic and it is not evidence
about any recording.

**And the honest limit on this whole document:** the record carries no abstract, and the full text was
not read. The two-pass structure, the two energy thresholds and the bounded zero-crossing search are
the form in which the method is universally described, and the constant names in `detect.py` follow
that convention. A reader who needs the exact thresholds, window lengths or the paper's own evaluation
must read the paper.

## In production

**What survived: the shape, completely, and usually without the name.** Every voice-activity detector
in use has an energy stage, and essentially all of them have at least one additional feature that is
not energy — zero crossings in the simplest, spectral measures or a small trained model in the rest.
The specific thresholds are long gone; the idea that loudness alone cannot find the edge of speech is
permanent.

**What did not survive: the isolated utterance.** The paper's setting — a single word, deliberately
spoken, with silence either side — was the practical setting of speech recognition in 1975 and has not
been anyone's setting for a long time. Modern detection runs continuously on conversational speech and
has to cope with overlap, which Day 75's turn-taking paper is about, and with the caller's own
loudspeaker, which part
[4.2](../parts/04-in-production/4.2-what-a-real-one-adds.md) named as echo.

**What replaced it, and what stayed the same.** The two hand-set thresholds are now, in most systems, a
small model trained on a lot of speech — a strictly better estimator of the same quantity. What did
**not** change is the trade: any detector still has to decide, at each moment, whether quiet means
finished or thinking, and a model that decides it more accurately still decides it. Part
[3.2](../parts/03-deciding-when-they-stopped/3.2-sensitivity-is-a-trade.md)'s dial is not an artefact
of a simple algorithm; it is the problem.

**What a professional takes from this into a voice product.** That "it cuts off the start of what I
say" is a known, old, structural problem with a name, and that the settings exposed for it —
sensitivity, prefix padding — are approximations of a method rather than arbitrary numbers. Also that
prefix padding is the cheap version: it keeps a fixed amount of audio before the detected start
because finding the true start is harder, and the amount is a guess about how long an unvoiced onset
lasts.

**The review comment a senior engineer leaves:** *"When people say it's clipping their first word,
don't reach for the sensitivity first — that trades one complaint for another. Prefix padding is the
setting that exists for exactly this, and it's cheap. And log which setting was in force per session,
because we're going to be told 'it cut me off' by people whose real problem is the blocking tool from
part 1.3, and those two need to be distinguishable from the outside."*

**The interview question:** *"Why is detecting the start of speech hard?"* An honest answer: *"Because
loudness doesn't work at the edges. Speech has voiced sounds — vowels — that are loud and regular, and
unvoiced ones like 's' and 'f' that are essentially hiss, and the unvoiced ones can be quieter than
the room. So any energy threshold that ignores background noise also ignores the start of a word
beginning with an 's'. The classic fix is from 1975: use energy to find a confident interior, then
extend outwards using zero-crossing rate — how often the signal changes sign — which is high for
noise-like sounds and low for vowels. It's a second measurement of a different kind rather than a
better threshold on the first, and that's the transferable part. Modern systems replace the hand-set
thresholds with a trained model, but the underlying trade doesn't go away: something still has to
decide whether a pause is the end of a sentence, and that's a judgement, not a measurement. The
setting called 'prefix padding' in modern APIs is the blunt version — keep some audio from before the
detected start, because the detected start is known to be late."*

## Check yourself

```bash
cd days/day-76-vad-and-non-blocking-tools/lab/papers/endpoints
uv run python demo.py
uv run python demo.py --off
```

Raise `FRICATIVE`'s energy from `5` to `10` and run the ablation again. Predict first what happens and
why, then say which of the two thresholds in `detect.py` you have just moved the fricative across, and
what that tells you about how carefully the demo's numbers were chosen.

Then set `SEARCH` to a very large number and give the silence a high `crossings` value. Report what the
detected span becomes, and write one sentence explaining why the bound exists.

**Out loud, without scrolling up:** the energy pass found the loud middle and missed both edges, and
nothing errored. What second measurement recovers them, and why does it work where loudness does not?

---

That is the day. A tool call the caller can hear, a line that goes dead on one word inside it, three
answers to *when* a result should come back, and a panel of settings for deciding that somebody has
stopped speaking — all of which are approximations of a problem that was named, and half-solved, in
1975.

**Next:** [back to the hub](../LESSON.md).
