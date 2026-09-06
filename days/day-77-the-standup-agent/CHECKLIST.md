# Day 77 — Definition of done

`./m done 77` refuses to commit until every box is ticked. Tick a box only when you have actually run
the thing, not when you have read it. Today's two measurements are pairs on identical facts, so most
boxes ask for both numbers — and the point of every pair is that the losing arm is **correct**.

## Before you start

- [ ] Day 76's parts and checklist are done.
- [ ] `lab/` scaffolded per §3 — five Python files, plus two under `lab/papers/chunking/`.
- [ ] `git check-ignore -v days/day-77-the-standup-agent/lab/_state.py` prints a matching rule.
- [ ] `git diff pyproject.toml uv.lock` is empty and stays empty. No package is added today.
- [ ] `uv run python days/day-77-the-standup-agent/lab/gate.py; echo "exit: $?"` is **red** on all six
      checks before you write anything.
- [ ] You read `_state.py` first, and can say why `needs_person` is a field on the ticket rather than
      something worked out from `days_open`.

## Section 1 — a report somebody hears

- [ ] **1.1** read · you can name three things a reader of a written report can do that a listener
      cannot
- [ ] **1.2** read · ran `live.py` · recorded the three tool names in the order the runtime returned
      them
- [ ] **1.3** read · ran `live.py` and `live.py --flat` · recorded **3 of 3** sentences needing a
      person delivered against **0 of 2** · confirmed for yourself that both runs called all three
      tools and said only true things

## Section 2 — the order is the product

- [ ] **2.1** read · you can state the `lines(queue, night)` contract from memory, including what the
      second element of each pair is
- [ ] **2.2** read · you can say what went wrong when importance was recovered from the text, and why
      the wrong number looked plausible
- [ ] **2.3** read · ran `standup.py` and `standup.py --flat` · recorded **0 words against 25** before
      the first sentence needing a person, and **5 sentences against 14** in total

## Section 3 — the quiet morning

- [ ] **3.1** read · you decided what your standup says on a morning when nothing needs anybody, and
      wrote the sentence down
- [ ] **3.2** read · you can say what last night's job failed to produce, and what a standup that
      omits it accidentally claims

## Section 4 — in production

- [ ] **4.1** read · you can say which budget a standup is spent from first, and why the token count
      is the second question
- [ ] **4.2** read · you named three people who would want three different standups from this same
      queue, and what each would cut
- [ ] **4.3** read · you cut the list to the three you would build first, with a sentence each

## The paper — read it last

- [ ] `papers/01-chunking.md` read **after** the parts, not before
- [ ] Ran the demo both ways from `lab/papers/chunking/`: chunked gives **4 units** for twelve
      tickets (exit 0); `--off` gives **12** against a budget of 5 (exit 1)
- [ ] You can say what a "unit" is, and why recoding twelve tickets into four units loses nothing
- [ ] You noticed that the Crossref record has an empty `published-print` field and **no abstract**,
      and can say how the paper document handles that

## Build brief

- [ ] `sutra/standup.py` written: `lines(queue, night)` returning `(text, attention)` pairs, attention
      first, and something to say on a quiet morning
- [ ] The attention flag is carried from the data, not recovered from the text
- [ ] You decided what the standup says about state it could not read, and wrote down why
- [ ] You wrote down who this standup is for
- [ ] `tests/test_standup.py` written, including the test that the flag survives a rewording
- [ ] `uv run python gate.py; echo "exit: $?"` re-run · you can say which of the six cleared

## Repo hygiene

- [ ] `./m depth 77` green — eleven parts and one paper
- [ ] `./m trace` green, and ADK-57 and AG-25 close on this day and no others
- [ ] `./m wiki` run, so `docs/WIKI.md` and `docs/wiki/day-77.md` are not stale
- [ ] `uv run ruff format --check days/day-77-the-standup-agent` clean
- [ ] `uv run ruff check days/day-77-the-standup-agent/lab` clean
- [ ] `docs/PROGRESS.md` row appended verbatim from §11, with the real commit hash and the `⚠️` the
      gate actually earned — no rounding up (P10)
- [ ] `docs/PAPERS.md` row for `doi:10.1037/h0043158` present and dated (P7, §17.4.1)
