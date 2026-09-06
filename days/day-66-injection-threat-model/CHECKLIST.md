# Day 66 — Definition of done

`./m done 66` refuses to commit until every box is ticked. Tick a box only when you have actually run
the thing, not when you have read it. Several boxes ask you to record a number, because today's whole
argument is that a threat model made of feelings is not a threat model.

## Before you start

- [ ] Day 65's parts and checklist are done, and Phase 9's gate verdict is written into
      `docs/PROGRESS.md` — including its reds. Today opens a new phase on top of that record.
- [ ] `lab/` scaffolded per §3 — sixteen files, plus two under
      `lab/papers/indirect-prompt-injection/`.
- [ ] `git check-ignore -v days/day-66-injection-threat-model/lab/threat-model.md` prints a matching
      rule. Everything today writes is synthetic and shaped like customer data; none of it reaches
      git (P9).
- [ ] `git diff pyproject.toml uv.lock` is empty and stays empty. No package is added today.
- [ ] `uv run python days/day-66-injection-threat-model/lab/gate.py; echo "exit: $?"` is **red**
      before you write anything, and you have read the findings rather than counted them.

## Section 1 — one stream

- [ ] **1.1** read · ran `prompt.py` · saw the measured share of the prompt written by strangers —
      **73.4%** — and can say which spans those characters came from
- [ ] **1.2** read · can state, in one sentence each, what a parameterised query gives the database
      and why there is no equivalent second input for a model
- [ ] **1.3** read · can define prompt injection without referring to how the sentence is phrased ·
      can say why row three of the table is the uncomfortable one

## Section 2 — how it arrives

- [ ] **2.1** read · ran `obey.py` · can say why direct injection is the case the threat model can
      largely accept, and what that acceptance depends on
- [ ] **2.2** read · can explain why the attacker in an indirect injection needs no account, no
      session and no knowledge that you exist
- [ ] **2.3** read · ran `doors.py` · counted **six** doors and **four** feeding the index · can name
      the door that reaches the prompt most reliably and say why it is the insider one
- [ ] **2.4** read · ran `obey.py` against the poisoned archive · recorded the measured result —
      **one private value out, zero warnings** — and can say why *"would a model obey this?"* is the
      wrong question to have asked

## Section 3 — the slow fuse

- [ ] **3.1** read · ran `delayed.py` · saw the row written on one ticket retrieved for a different
      question · can say what changes when an injection becomes a standing rule
- [ ] **3.2** read · ran `split.py` · saw both halves pass individually · can say why checking the
      assembled context does not help either

## Section 4 — three legs

- [ ] **4.1** read · can name the three legs and say why `save_memory` is classified `OUTWARD`
- [ ] **4.2** read · ran `legs.py` · recorded the per-stage answer — **zero of five stages hold all
      three** — and can say why that answer is produced by asking in the wrong unit
- [ ] **4.3** read · read the *second* table from the same run · recorded the stage the trifecta
      closes at — **`review`** — and can explain the one `|` that is the entire difference from 4.2
- [ ] **4.4** read · ran `legs.py --cut outward` and `legs.py --isolate <stage>` · saw one of them
      close the trifecta everywhere and the other change **nothing** · can say why

## Section 5 — what it asks for

- [ ] **5.1** read · ran `model.py --write` and read the decisions section · can name the five harms
      and say which two survive removing the outward leg
- [ ] **5.2** read · ran `spend.py` · recorded **20 extra requests** and **5 displaced tickets** from
      one sentence · ran `spend.py --cap 6` and recorded **8** and **2** · can say why a cap is a
      price rather than a door, and what it costs an honest hard ticket

## Section 6 — the way out

- [ ] **6.1** read · ran `channels.py` and `channels.py --closed` · recorded **5 of 5** and **4 of 5**
      · ran all four `blocklist.py` variants and recorded **3/12**, **10/12**, **2/5** and **4/5** ·
      can name the honest customer who is refused for quoting a phishing mail
- [ ] **6.2** read · can say why the reply is a channel that produces no unusual event, and name the
      two structural controls that narrow it and the day that owns each
- [ ] **6.3** read · ran the retrieval demonstration · recorded the planted row's score — **0.491,
      top of three** — for a question unrelated to the ticket it was written on · can state the
      difference between this part's memory row and 3.1's
- [ ] **6.4** read · ran the error demonstration and read the real `ValueError` line · can say why a
      tool allowlist does not touch this channel

## Section 7 — writing it down

- [ ] **7.1** read · ran `model.py` and read the first two tables · can say why *the archive as a
      whole* is a separate asset from *customer text*, and name the entry point whose writer cannot
      be named
- [ ] **7.2** read · ran the in-memory drift demonstration and saw the Ways-out table lose a row
      without any file being edited · ran the stale-artefact demonstration and saw
      **`entry points absent from the artefact: ['ticket attachment']`**
- [ ] **7.3** read · ran the ownership ablation and saw **four** mitigations reported by name · wrote
      the trigger condition for both `accept` rows in your own words

## The paper — read it last

- [ ] `papers/01-indirect-prompt-injection.md` read **after** the parts, not before
- [ ] Ran the demo both ways from `lab/papers/indirect-prompt-injection/`: `demo.py` **exits 1** with
      `ATTACKER-CONTROLLED`, `demo.py --no-retrieval` **exits 0** with the identical page inert
- [ ] Can say what the ablation licenses you to conclude, and what it does not — the reader is a
      deterministic stand-in, so it shows the sentence *arrived somewhere it could act*, not that a
      particular model obeys

## The artefact and the eval

- [ ] `uv run python model.py --write` run, and `lab/threat-model.md` read end to end — assets, entry
      points, the trifecta table, the ways out, the eight decisions, the attacker
- [ ] `uv run python gate.py; echo "exit: $?"` run · **red**, with exactly the two expected findings:
      the trifecta closing at `review`, and `sutra/threat_model.py` not yet written
- [ ] At least one check driven red **on purpose** and back to green, and you can say which behaviour
      the red proved was real (P11)

## Build brief

- [ ] `sutra/threat_model.py` written, with `CHANNELS`, `Decision`, and `accepted_under`
- [ ] `tests/test_threat_model.py` written, and both `TODO(me)` tests present
- [ ] You decided which of the two channel lists is the source of truth, and wrote the reason down in
      the module docstring rather than in a commit message

## Repo hygiene

- [ ] `./m depth 66` green — twenty-two parts and one paper
- [ ] `./m trace` green, and SEC-06 and SEC-07 close on this day and no others
- [ ] `./m wiki` run, so `docs/WIKI.md` and `docs/wiki/day-66.md` are not stale
- [ ] `uv run ruff format --check days/day-66-injection-threat-model` clean — Python inside fences is
      formatted like Python anywhere else
- [ ] `docs/PROGRESS.md` row appended verbatim from §11, with the real commit hash and the `⚠️` the
      gate actually earned — no rounding up (P10)
- [ ] `docs/PAPERS.md` row for `arXiv:2302.12173` present and dated, with the record checked live
      rather than recalled (P7, §17.4.1)
