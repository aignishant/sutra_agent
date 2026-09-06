# Day 75 — Definition of done

`./m done 75` refuses to commit until every box is ticked. Tick a box only when you have actually run
the thing, not when you have read it. Every script today carries its own deadline, so a run that
reports reaching the deadline has told you something — record it rather than re-running until it
looks better.

## Before you start

- [ ] Day 74's parts and checklist are done.
- [ ] `lab/` scaffolded per §3 — six Python files, plus two under `lab/papers/turn-taking/`.
- [ ] `git check-ignore -v days/day-75-the-bidi-voice-loop/lab/_live.py` prints a matching rule.
- [ ] `git diff pyproject.toml uv.lock` is empty and stays empty. No package is added today.
- [ ] `uv run python days/day-75-the-bidi-voice-loop/lab/gate.py; echo "exit: $?"` is **red** on all
      six checks before you write anything.
- [ ] You read `_live.py` first, and can name the five methods a live connection has to implement.

## Section 1 — the open line

- [ ] **1.1** read · you can say what a caller can do on an open line that they cannot do in a
      request, and what that costs the program
- [ ] **1.2** read · you found `BaseLlm.connect`'s return type in the installed package **yourself**
      and recorded the ADK version you found it in (P8)
- [ ] **1.3** read · ran `session.py`, `session.py --queue-only` and `session.py --hang` · recorded
      **exit 0** against **exit 1 at the 2.0s deadline** twice · can say what each of the two closes
      actually does

## Section 2 — talking over

- [ ] **2.1** read · you can say why an interruption is a normal event rather than an error, and name
      one thing a request/response system never has to handle because of it
- [ ] **2.2** read · ran `barge_in.py` and `barge_in.py --ignore` · recorded **3 of 6 chunks with an
      `interrupted` event** against **6 of 6 and 12 in total with none**
- [ ] **2.3** read · you listed the three things a client has to do when the event arrives, and can
      say which of them is a decision rather than code

## Section 3 — what goes down the wire

- [ ] **3.1** read · ran `audio.py` and `audio.py --text` · recorded **64,000 bytes against 20** ·
      noticed that `RATE` is a stated assumption and can say which figures depend on it
- [ ] **3.2** read · ran `vad.py` and `vad.py --no-markers` · recorded the five things the connection
      received in order, and the three · can say why two of the five are not sound

## Section 4 — what it costs, and what a real one adds

- [ ] **4.1** read · you can say what capacity means for a service holding connections open, and why
      it is not requests per second
- [ ] **4.2** read · you can name what a session with no deadline leaks, and say what your deadline
      would be and why
- [ ] **4.3** read · you cut the list to the three you would build first, with a sentence each

## The paper — read it last

- [ ] `papers/01-turn-taking.md` read **after** the parts, not before
- [ ] Ran the demo both ways from `lab/papers/turn-taking/`: local management gives **0 gaps** (exit
      0) and the central rota gives **3 gaps and 2 overlaps** (exit 1)
- [ ] You can state the three rules in order, and say which of them produced the one overlap in the
      passing run
- [ ] You can say what "locally managed" means for a voice loop you would actually build

## Build brief

- [ ] `sutra/voice.py` written: `call(...)` that closes both the queue and the stream, handles
      `interrupted`, and has a deadline
- [ ] You decided what your client does on an interruption and wrote the reason down
- [ ] You decided whether the client sends turn markers, and why
- [ ] You decided what the transcript contains after an interrupted turn
- [ ] `tests/test_voice.py` written, including the completes-within-a-deadline test
- [ ] `uv run python gate.py; echo "exit: $?"` re-run · you can say which of the six cleared

## Repo hygiene

- [ ] `./m depth 75` green — eleven parts and one paper
- [ ] `./m trace` green, and ADK-54 and ADK-55 close on this day and no others
- [ ] `./m wiki` run, so `docs/WIKI.md` and `docs/wiki/day-75.md` are not stale
- [ ] `uv run ruff format --check days/day-75-the-bidi-voice-loop` clean
- [ ] `uv run ruff check days/day-75-the-bidi-voice-loop/lab` clean
- [ ] `docs/PROGRESS.md` row appended verbatim from §11, with the real commit hash and the `⚠️` the
      gate actually earned — no rounding up (P10)
- [ ] `docs/PAPERS.md` row for `doi:10.2307/412243` present and dated (P7, §17.4.1)
