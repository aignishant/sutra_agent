# Day 50 — Definition of done

`./m done 50` refuses to commit until every box is ticked. Tick a box only when you have actually run the
thing, not when you have read it.

## Before you start

- [ ] Day 49's parts and checklist are done, and
      `python -c "import sutra.retrieval as r; print(sorted(n for n in dir(r) if not n.startswith('_')))"`
      lists `build_index` and `search`. If it does not, today cannot start (P2).
- [ ] `uv run python days/day-50-chunking-and-top-k/lab/gate.py; echo "exit: $?"` is **red** before you
      write anything, and you have read which of the six findings it reports.
- [ ] `lab/` scaffolded per §3 — eighteen files — and `tests/test_retrieval_tuning.py` created empty.
- [ ] `git diff pyproject.toml uv.lock` is empty and stays empty. No package is added today.

## Section 1 — the unit you index

- [ ] **1.1** read · ran `fragment.py --size 900` and `fragment.py` · saw **57 documents become 61 rows
      and then 187** · reached the `ValueError: overlap 300 must be smaller than size 280` on purpose ·
      can say why raising k cannot repair a bad cut
- [ ] **1.2** read · ran both arms of `dilution.py` · saw **0.235 for the whole document against 0.465 for
      its own best paragraph**, with ten of twelve pieces below 0.09 · noticed that `kb:KB-900#9` scored
      0.367 without answering the question · changed `SIZE` to `1600` and can explain which way the score
      moved
- [ ] **1.3** read · ran `fragment.py` · saw **hit@3 9/10 against answered@3 5/10** · ran
      `fragment.py --size 40` and saw answered@3 fall to **2/10** · can point at one printed row that
      would match a question about signing out and could not answer it
- [ ] **1.4** read · ran `overlap.py` and `overlap.py --size 280` · saw answered@3 go **6 → 8 for 19% more
      index** at chunk 160, and **buy nothing** at chunk 280 · ran `overlap.py --size 900` and can say why
      the whole table went flat

## Section 2 — measuring the cut

- [ ] **2.1** read · ran `gold.py` and `gold.py --leak` · can name all three columns and say what each
      makes measurable · added an eleventh gold question of your own and re-ran `sweep.py`
- [ ] **2.2** read · ran `sweep.py` and `sweep.py --overlap` · saw **hit@3 flat at 10/10** while
      **tokens at k=3 fell from 459 to 279** · can state the finding as *"chunking found the same thing
      and sent less of it"* · know that only **four** of the fifty-seven documents are longer than 900
      characters
- [ ] **2.3** read · ran `split.py` and `split.py --size 900` · saw the top hit at **0.381 from the right
      ticket with the answer NOT in it** · re-ran with `GOLD[1]` and can say which size loses that answer

## Section 3 — the k is a budget

- [ ] **3.1** read · ran `price.py` and `price.py --turns 10` · saw **8,539 tokens against 1,006** over
      six turns · changed `turns - 1` to `turns` and can say why that version overstates the cost
- [ ] **3.2** read · ran `curve.py` · saw the **knee at k=2** and **92% noise at k=20** · re-ran with
      `CHUNK_SIZE = 280` and can say which way the knee moved
- [ ] **3.3** read · ran `middle.py --k 2` and `middle.py` · saw one answer land at **rank 7, 24% into a
      4,260-character block** and another stay at rank 1 while its block grew from 55 to 731 tokens · can
      give the two separate arguments against a large k and say which survives if tokens were free

## Section 4 — the floor

- [ ] **4.1** read · ran `garbage.py` and `garbage.py --terms` · saw the printer question score **0.388 on
      `on` and `the` alone**, with `informative: []` · added a fifth `NOTHING` question and wrote down its
      top score
- [ ] **4.2** read · ran `floor.py` and `nothing.py` · saw **worst real 0.180, best impostor 0.388, gap
      −0.209** · saw floor `0.20` with two shared terms keep **9/10 long, 3/3 short, 0/4 impostors** ·
      changed `INFORMATIVE_IDF` to `3.0` and can explain what happened to the short questions
- [ ] **4.3** read · ran `nothing.py --say` · can give both sentences — the one the retriever may say and
      the one it may not — and say what the difference is a difference *about*

## Section 5 — the wrong tool

- [ ] **5.1** read · ran `wrongtool.py rule` · saw a refund policy question answered with **ticket:4612 at
      0.266**, above `SIM_FLOOR` and past the shared-terms rule · wrote two more rule questions and
      recorded their top scores
- [ ] **5.2** read · ran `wrongtool.py current` · saw **0 of 61 rows carry a date** and the top hit be the
      31-character tail chunk `'rm now survives the round trip.'` · can state the difference between a
      stale index and an index with no concept of time
- [ ] **5.3** read · ran `wrongtool.py count` · saw the true answer be **12 of 52** against three returned
      rows, two of which are not about signing in · added `"redirect"` to `SIGN_IN_WORDS` and can say why
      that movement argues for stating the rule in code
- [ ] **5.4** read · ran `wrongtool.py fits` · saw **2,795 tokens, 31x, eleven windows over** · can give
      two reasons why "the corpus fits" is not the end of the argument

## Section 6 — in production

- [ ] **6.1** read · ran `decide.py` (`misrouted: 0 of 12`, `exit: 0`) and `decide.py --skip-rule`
      (`misrouted: 2 of 12`, `exit: 1`) · noticed that **only two of twelve questions are retrieval
      questions** · added a thirteenth question of your own and reconciled the disagreement
- [ ] **6.2** read · can say what a reranker does that a retriever cannot, name both halves of hybrid
      search and which one Sutra already has, and give the reason teams usually move to a vector database
      that is not speed

## The build

- [ ] `sutra/retrieval.py` carries `CHUNK_SIZE`, `CHUNK_OVERLAP`, `TOP_K`, `SIM_FLOOR` and
      `MIN_SHARED_TERMS`, and **every one of them has a comment naming the run and the date it came from**
- [ ] `sutra/retrieval.py` carries `chunk_document`, `chunked_rows`, `parent_ref` and `retrieve`
- [ ] Day 49's `build_index`, `search`, `cosine` and `tokenize` are **untouched** — `git diff` on that
      file shows additions only
- [ ] `retrieve` returns an **empty list** for the printer question, and it is a `list`, not `None` and
      not an exception
- [ ] You decided which module owns `TOP_K` — `sutra/retrieval.py` or `sutra/memory/service.py` — made
      the other one import it, and wrote down why
- [ ] `tests/test_retrieval_tuning.py` holds all five tests from §4, including
      `test_retrieve_still_finds_a_known_answer`

## The gates

- [ ] `uv run python days/day-50-chunking-and-top-k/lab/gate.py; echo "exit: $?"` prints `findings: 0` and
      `exit: 0`
- [ ] You broke exactly one finding on purpose — deleted the comment beside `TOP_K` — saw finding 3
      appear, and put it back
- [ ] `uv run python days/day-50-chunking-and-top-k/lab/decide.py; echo "exit: $?"` prints `exit: 0`
- [ ] `uv run python -m pytest tests/test_retrieval_tuning.py -q -m "not live"` is green, with no network
- [ ] `./m depth 50` is green
- [ ] `./m check` is green
- [ ] `git diff pyproject.toml uv.lock` is empty

## The ledger

- [ ] `docs/PROGRESS.md` has the day 50 row from §11, with the real commit hash
- [ ] `docs/PACKAGES.md`, `docs/PAPERS.md` and `docs/SKILL_PROVENANCE.md` are unchanged — today adds no
      rows to any of them
- [ ] Commit made with the message from §11; no `.env` in the diff
- [ ] **Zero model calls were spent.** If you spent any, write down how many and on what.
