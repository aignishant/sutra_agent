# Day 49 — Definition of done

`./m done 49` refuses to commit until every box is ticked. Tick a box only when you have actually run
the thing, not when you have read it.

## Before you start

- [ ] Day 48's parts and checklist are done. `sutra/memory/` holds `__init__.py`, `service.py`,
      `persistence.py` and `policy.py`.
- [ ] You have re-read Day 46's
      [5.1](../day-46-sessions-vs-memory/parts/05-failure-lab/5.1-the-past-that-matched-on-nothing.md)
      and can quote the sentence today exists to answer: *"the cap made the response smaller and no
      more correct, because you cannot take the top three of a list that has no top."*
- [ ] `python -c "import google.adk; print(google.adk.__version__)"` prints `2.7.1`.
- [ ] `python -c "from google.adk.memory import BaseMemoryService as B; print(sorted(B.__abstractmethods__))"`
      prints `['add_session_to_memory', 'search_memory']`. If it does not, stop and read the installed
      package before writing anything (Principle 8).
- [ ] `python -c "import numpy"` raises `ModuleNotFoundError`. **It must stay that way** — no package
      is added today.
- [ ] `lab/` scaffolded per §3 — twenty-two scripts plus the two `lab/papers/` folders.
- [ ] `sutra/retrieval.py` created and empty.

## Section 1 — building the index by hand (AG-33)

- [ ] **1.1** read · ran the overlap command · saw that ticket 4521 and ticket 4188 share **exactly
      one word** · can say what a description-based answer can never tell you that a name-based
      answer always can
- [ ] **1.2** read · ran `counts.py` · saw **14 tokens, 13 axes, 67 zeros out of 80** · confirmed
      that `'the cookie dropped the browser'` and `'the browser dropped the cookie'` produce identical
      vectors · can say what a bag of words throws away
- [ ] **1.3** read · ran both arms of `angle.py` · saw the dot product put **`11.000` (wrong) above
      `3.000` (right)** and cosine reverse it to `0.330` against `0.433` · duplicated `LONG` and
      watched the dot product double while the cosine did not move
- [ ] **1.4** read · ran `weights.py` · saw **`fix`, `kb` and `the` at exactly `0.000`** · can say why
      `fix` and `kb` are zero and why no stopword list would have caught them
- [ ] **1.5** read · ran both arms of `index.py` · opened `archive_index.json` and found the
      `"weights"` key and one row's `"vector"` · saw **5.2 KB weighted against 1.8 KB** · deleted the
      file and read the `FileNotFoundError` · **wrote down when the index gets rebuilt**

## Section 2 — the meaning test (AG-33)

- [ ] **2.1** read · ran both arms of `meaning.py` · saw **`4188 scored 0.000 and ranked 5 of 8`** and
      **`top hit was 4467 at 0.270`** · can say why the score is exactly zero rather than merely low
- [ ] **2.2** read · ran `patches.py` · saw the four rows — `0.000`, `0.000`, `0.000`, **`0.523`** —
      and the two follow-up phrasings **back at `0.000`** · deleted the `"redirect": ["loop"]` line and
      watched the working arm stop working · can say what a rank of 1 at a score of 0.000 means

## Section 3 — meaning as geometry (AG-33)

- [ ] **3.1** read · ran `space.py` · saw **`0.987` between two texts sharing no words** · can say the
      one thing you must never claim about an embedding's individual numbers
- [ ] **3.2** read · ran `embed.py` · **either** pasted the real output and **recorded the dimension
      and the `ollama list` digest in `docs/PACKAGES.md`**, **or** read the
      `URLError: <urlopen error [WinError 10061] ...>` in full and can say why *actively refused* is
      not a timeout
- [ ] **3.3** read · ran both arms of `lanes.py` · confirmed the embedding arm **raises** rather than
      falling back silently · found the single line that would have to change to add a third lane ·
      **decided what the index file records about the lane that built it**
- [ ] **3.4** read · ran `priced.py` · saw **5,000 rows = 50 batched requests = 2.5 days of a 20/day
      budget** · set `BATCH` to `1` and re-read the table · **opened the Gemini rate-limits page and
      recorded the free-tier embedding limit, or left the `TODO(verify: ...)` with the exact URL**

## Section 4 — the ADK socket (ADK-30)

- [ ] **4.1** read · ran `surface.py` · read the
      `TypeError: Can't instantiate abstract class Nothing ...` in full · read both inherited
      `NotImplementedError` messages in `base_memory_service.py` · can name the five `MemoryEntry`
      fields and say which one is the score (none)
- [ ] **4.2** read · ran `wired.py`, `--keyword` and `--incoming` · saw the easy query return **the
      identical three tickets in the identical order from both services** · saw the hard query return
      **3 ranked against 8 unranked** · reordered `ARCHIVE` and watched the keyword arm's "right"
      answer move
- [ ] **4.3** read · ran `entrytext.py` · saw that what reaches the model is
      **`{'result': LoadMemoryResponse(...)}` as a Python repr**, with `id=None` and `timestamp=None`
      on every entry · read `LoadMemoryTool`'s docstring note in the installed source · can say why
      the score goes in the text anyway
- [ ] **4.4** read · ran both arms of `capped.py` · saw **hit@1 `6/7` against `2/7`** and hit@3
      **`7/7` against `4/7`** · noticed that four keyword queries returned the same first three
      tickets · can say which of the ranked arm's seven hits should not be trusted, and why

## Section 5 — when retrieval lies (AG-33 · ADK-30)

- [ ] **5.1** read · ran both arms of `nearest.py` · saw a **refund ticket at `0.369`** for a SOC 2
      question · saw that a `0.20` cutoff left **all three** unanswerable questions with results ·
      raised it to `0.40` and watched the answerable question lose its answer too · **decided what the
      desk says when everything is below the floor**
- [ ] **5.2** read · ran both arms of `stale.py` · saw **`is 4602 reachable at all? False`** with no
      error, and `0.597` after the rebuild · saw `app` move from **`2.079` to `1.504`** · can say why a
      missing index is a better failure than a stale one
- [ ] **5.3** read · ran `words.py` · saw **five phrasings, five results**, two of them `0.000` with
      seven ties · read ADK's generic memory instruction in `load_memory_tool.py` · **wrote the desk
      instruction** that says what a good query looks like for this archive

## Section 6 — in production (AG-33 · ADK-30)

- [ ] **6.1** read · ran `stores.py` · saw **64.3 ms sparse against 876.6 ms dense at 20,000 rows**,
      and **117 MB** held · halved `width` and watched both halve · **decided the archive size at which
      you would move to a real store, and named which one**
- [ ] **6.2** read · ran `gate.py` and saw it **red** · read all six rules before writing the module ·
      can name the two things Day 50 changes and the exact lines each touches

## The papers — read them after the parts

- [ ] **`papers/01-vector-space-model.md`** read · ran both arms of `vsm.py` · saw
      **`weight of 'brake': 0.000`**, one card above the cutoff weighted against **four (three wrong)**
      unweighted, and the gap `0.481` against `0.299` · changed `QUERY` to `"brake pedal soft"` and ran
      both arms again · can say the one assumption the field spent fifty years working around
- [ ] **`papers/02-retrieval-augmented-generation.md`** read · ran both arms of `rag.py` · saw
      **`4/4` answers citing a source against `0/4`**, and the stale *"Refunds above 60 days are not
      possible"* that the archive contradicts · added a fifth question the archive cannot answer and
      read what the retrieval arm produced · can define parametric and non-parametric memory in one
      sentence each

## The build

- [ ] `sutra/retrieval.py` written, **every line typed by you**, with all twelve public symbols from
      §4's table
- [ ] `build_index` takes pre-cut rows and its docstring says it never splits anything
- [ ] `search` **sorts, then cuts, then applies the floor** — in that order
- [ ] `SutraRetrievalMemoryService.search_memory` **filters by `(app_name, user_id)` before it ranks**
- [ ] `TOP_K` and `SIMILARITY_FLOOR` are named module constants, each with the evidence for its value
      in the comment beside it
- [ ] the index path is in `.gitignore` **before** the file exists, proved with
      `git check-ignore -v <path>`
- [ ] `uv run python days/day-49-retrieval-and-embeddings/lab/gate.py` prints `findings: 0` and
      `exit: 0`
- [ ] you broke exactly one rule on purpose — replaced `TOP_K` with a literal — **watched the gate go
      red**, and put it back

## Gates

- [ ] `./m depth 49` green
- [ ] `.venv/Scripts/ruff.exe format --check days/day-49-retrieval-and-embeddings/` clean
- [ ] `./m check` green (or the failure is named and understood, and is not yours)
- [ ] `git diff pyproject.toml uv.lock` is **empty** — no package added, no pin moved
- [ ] `docs/PROGRESS.md`, `docs/PACKAGES.md` rows appended per §11
- [ ] committed with the message in §11; no `.env`, no `archive_index.json`
