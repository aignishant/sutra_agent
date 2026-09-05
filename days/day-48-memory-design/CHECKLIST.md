# Day 48 — Definition of done

`./m done 48` refuses to commit until every box is ticked. Tick a box only when you have actually run
the thing, not when you have read it.

## Before you start

- [ ] **The freshness gate.**
      `curl -s -o /dev/null -w "%{http_code}\n" -L https://adk.dev/sessions/memory/` prints `200`. If
      it does not, read `.venv/Lib/site-packages/google/adk/memory/` and amend before writing code
      (Principle 14).
- [ ] `uv run python -c "from google.adk.memory import BaseMemoryService as B; print([m for m in dir(B) if not m.startswith('_')])"`
      still prints four methods and **none of them removes anything**. If a delete method has appeared,
      section 4.3 is amended before the code is.
- [ ] Day 46's parts and checklist are done, and `sutra/memory/service.py` exists.
- [ ] Day 47's parts and checklist are done, and `sutra/memory/persistence.py` exists.
- [ ] `lab/` scaffolded per §3 — twenty-two files, and `sutra/memory/policy.py` created empty.

## Section 1 — what a conversation leaves (AG-12)

- [ ] **1.1** read · ran both arms of `noise.py` · saw **653 characters against 290 for the same three
      useful entries** · changed `QUESTION` to a single word with no stopwords and can say why the
      curated store's advantage got *smaller*
- [ ] **1.2** read · ran `taxonomy.py` · saw **7 proposed, 5 written down** · relabelled the `guess` as
      a `customer_fact`, watched the count go to six with no warning, and can say what would catch it
      in review
- [ ] **1.3** read · ran `exhaust.py` · saw **698 characters against 294** · added four pleasantries to
      `TURNS` and watched the kept row stay still · can state all three halves of the transcript rule:
      not promoted, not deleted, retention owned by the session store
- [ ] **1.4** read · ran both arms of `correction.py` · saw **two live billing addresses against one** ·
      changed the `correction` row's `authority` to `1` and watched the correction lose · can explain
      why `(holder, kind, subject)` cannot express a correction

## Section 2 — policy as data (AG-12)

- [ ] **2.1** read · ran `branches.py` · saw six branches and six rows produce **identical verdicts** ·
      tried to construct a `Rule` with no `why` and read the `TypeError`
- [ ] **2.2** read · ran `verdicts.py` · saw **5 kept, 2 refused, 7 proposed** and every line naming its
      rule · added a `kind="promise"` candidate and found which `refused.append` branch produced it
- [ ] **2.3** read · ran both arms of `unknown_kind.py` · saw **two memos that never expire and a
      refusal count of zero** · added a `sentiment` row with `keep_for_days=0`, watched the two arms
      converge, and can say what that convergence proves about any test written against either

## Section 3 — expiry and supersession (AG-13)

- [ ] **3.1** read · ran `expiry.py` · saw **one store, four dates, only the calendar moving** · changed
      `decision` to `120` days and watched a second memo drop out · can say why the expiry date is
      resolved at write time
- [ ] **3.2** read · ran both arms of `supersede.py` · saw **three unexpired answers, two of them
      wrong** · renamed one memo's `subject` and watched supersession silently stop working
- [ ] **3.3** read · ran both arms of `sweep.py` · saw **identical verdicts, 1302 bytes against 828**,
      and the `4800` substring present in one and absent in the other · can name three things that read
      a store without going through the policy

## Section 4 — privacy and erasure (AG-13)

- [ ] **4.1** read · ran both arms of `redact_demo.py` · saw **two identical clean stores and one dirty
      backup** · added a postal address to `RAW`, ran the safe arm, and can say what the
      `reached disk unredacted: none` line is actually measuring
- [ ] **4.2** read · ran both arms of `address.py` · saw the string search **match the wrong ticket and
      miss the right one** · can state the difference between the person a memo is about, the person who
      typed it, and the session it came from
- [ ] **4.3** read · ran `erase.py` · saw **four public methods and none that removes anything** · moved
      the erasure branch below the expiry check, ran a memo that is both, and can say what that changes
      about what you could prove a year later
- [ ] **4.4** read · ran both arms of `gitcheck.py` · saw **exit 1** and the finding that
      `sutra/data/memory.json` is not ignored · added the path to `.gitignore`, watched it go green,
      then changed `STORE` by one character and saw what the green run had actually proved
- [ ] **`.gitignore` updated before any store file was written**, and not with `*.json`

## Section 5 — the failure lab

- [ ] **5.1** read · ran both arms of `lossy.py` · saw **0 of 4 against 3 of 4** · can explain why the
      memos arm scores three and not four, and why that is the honest result rather than a bug
- [ ] **5.2** read · ran both arms of `stale.py` · saw a **380-day-old price quoted with total
      confidence** · can say why the broken arm produces the better-sounding reply, and why supersession
      cannot fix it
- [ ] **5.3** read · ran both arms of `shredded.py` · saw **`expired on 2026-10-05`**, four months
      before the dispute · moved `DISPUTE` four years out and watched the good rule fail too · can name
      the two costs of a retention rule and say which one has a number

## Section 6 — the price (AG-12 · AG-13)

- [ ] **6.1** read · ran both arms of `price.py` · saw **73 tokens per turn, 876 per conversation, 36
      that never expire** · compared the `quote` row across the two arms (**12 against 7**) and can say
      why a number tokenises worse than prose
- [ ] **6.2** read · ran both arms of `defend.py` · saw **1200 / 2976 / 4848 / 8448 tokens per customer
      per year** · changed the `guess` row to 365 days, re-ran `lossy.py --memos`, and can say what that
      pair of runs proves in both directions

## The build

- [ ] `sutra/memory/policy.py` written, every line typed, and it does **not** re-create
      `sutra/memory/__init__.py` (Day 46) or `persistence.py` (Day 47)
- [ ] `RETENTION` is a tuple of rows, every row has a non-empty `why` that **names the event it is
      sized against**
- [ ] `what_to_keep` returns two lists, and you asserted that kept plus refused equals proposed
- [ ] `today` is a required keyword argument everywhere; nothing in the module reads the clock
- [ ] Supersession keys on `(holder, subject)`, and erasure is checked **before** expiry
- [ ] `tombstone` drops the holder as well as the text
- [ ] Every `TODO(me)` in §4 answered in writing, including the two-holder case (4.2) and the list of
      pattern classes you are **not** covering (4.1)

## Gates

- [ ] `uv run python days/day-48-memory-design/lab/gate.py` prints `findings: 0` and exits `0`
- [ ] You broke exactly one on purpose — `correction` authority `3` → `1` — saw
      `a correction did not supersede the same-day fact it corrects`, `exit: 1`, and put it back
- [ ] `uv run ruff check .` and `uv run ruff format --check .` clean
- [ ] `uv run python -m pytest -q -m "not live"` green
- [ ] `./m depth 48` green
- [ ] `git diff pyproject.toml uv.lock` is empty — no package added, no pin moved
- [ ] **Zero generations spent.** `price.py` and `defend.py` used `count_tokens`, which is separate
      quota from `generate_content`
- [ ] Commit made; no `.env` in the commit; no memory store file in the commit
- [ ] `docs/PROGRESS.md` row appended with the real hash
