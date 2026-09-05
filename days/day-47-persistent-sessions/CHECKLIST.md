# Day 47 — Definition of done

`./m done 47` refuses to commit until every box is ticked. Tick a box only when you have actually run
the thing, not when you have read it.

## Before you start

- [ ] **The freshness gate.**
      `uv run python -c "import google.adk, aiosqlite, importlib.util as u; print(google.adk.__version__, 'sqlalchemy:', u.find_spec('sqlalchemy') is not None)"`
      prints `2.7.1` and `sqlalchemy: False`. If either has moved, run `lab/reach.py` and
      `lab/oldschema.py` and re-open section 2's decisions before writing code (Principle 14).
- [ ] Day 46's parts and checklist are done, and `sutra/memory/` exists with `__init__.py` and
      `service.py` in it. **You are adding a module, not creating the package.**
- [ ] You have re-read Day 43's
      [4.1](../day-43-stateless-by-default/parts/04-where-state-goes/4.1-down-out-or-nowhere.md) —
      *down, out or nowhere* — because today is the "down" it promised.
- [ ] `lab/` scaffolded per §3 — nineteen scripts and `lab/papers/transaction-oriented-recovery/`.

## Section 1 — what a restart costs (ADK-29)

- [ ] **1.1** read · ran both arms of `amnesia.py` · saw **2 turns against `None`** · deleted
      `desk.sqlite3`, ran the first arm again, and can say why deleting the file is a different loss
      from restarting the process even though the reader sees the same `None`
- [ ] **1.2** read · ran `tables.py` · named the four tables and the one that grows without bound ·
      saw **2 events survive a `DELETE FROM sessions`** run without the pragma · can say why
      `event_data` is one JSON column and what that costs
- [ ] **1.3** read · ran `scopes.py` · **`failures: 0`**, with `temp:token_estimate` in no table ·
      removed the `temp:` prefix, watched one check go red, and said out loud what you had just
      decided about that value's retention

## Section 2 — reaching the service (ADK-29)

- [ ] **2.1** read · ran `reach.py` · **`changed: 0`** across the three routes · read route 1's
      `ImportError` in full, including the path of the `__init__.py` it looked in · ran
      `uv run adk web --help` and found `--session_service_uri`
- [ ] **2.2** read · ran `driver.py` · saw `sqlalchemy installed : False`, the ImportError naming
      `google-adk[db]`, and **`sqlite+aiosqlite:///...` resolving to `None`** · confirmed
      `grep -n "sqlalchemy\|google-adk\[" pyproject.toml` matches nothing
- [ ] **2.3** read · ran `urls.py` from **two different directories** · saw the same seven strings
      resolve to different files · can say which row is identical in both and why
- [ ] **2.4** read · ran `gate.py` **before** writing the module and saw it red · found where
      `adk web sutra/desk` puts its own sessions · can say which object takes the session service and
      which string must never change once a store has sessions in it
- [ ] **2.5** read · ran the two `inspect.signature` / `create_session` probes · saw the `gcp` extra
      named on the **first call**, not on the import · can name two things the managed store gives
      and two it takes away, without using the word "scalable"

## Section 3 — writes that survive (ADK-29)

- [ ] **3.1** read · ran `writes.py` · saw **three changes and no growth in file size** ·
      `update_time == event timestamp: True` · can say which of the three a reader would see if the
      process died between the `UPDATE` and the `INSERT`
- [ ] **3.2** read · ran both arms of `restart.py` · **3 partials sent, 1 event stored** against 2 ·
      moved `os._exit(9)` before the first `append_event` and said what the customer saw in that
      version · can say what `flush()` does on this service
- [ ] **3.3** read · ran all three arms of `locked.py` · **100 of 100 stored with 0 errors**, WAL
      changing nothing, and **4 of 4 workers dead at construction** · read the traceback in full and
      found `_is_migration_needed` in it · set `HOLD_SECONDS` to `3.0`, watched the blocked arm go
      green, and can name the number you just discovered and where it is set

## Section 4 — two workers (ADK-29)

- [ ] **4.1** read · ran both arms of `stale.py` · **2 tried, 1 stored** against 2 and 2 · changed
      `except StaleSessionError` to `except ValueError`, saw identical behaviour, and can say why
      that is a problem in code you did not write
- [ ] **4.2** read · ran both arms of `staleread.py` · **`exceptions : 0` in both** · added an
      `append_event` from B after the decision in the default arm and checked whether it was refused ·
      can name one value in Sutra that must be re-read before it is acted on
- [ ] **4.3** read · ran both arms of `recover.py` · **16 attempts and 1 line** against **11 attempts
      and 6** · set `WORKERS` to `2`, watched the blind arm go green, and can say why a passing test
      is not evidence here · can name the three steps of a correct retry and the one people leave out

## Section 5 — shape and size (ADK-29)

- [ ] **5.1** read · ran `oldschema.py` · **`changed: 0`**, with the service refusing the old file and
      the named migration unavailable · added an `event_data TEXT` column to `OLD_SCHEMA`, watched the
      service construct happily, and said which of the two failures you would rather have
- [ ] **5.2** read · ran both arms of `dropped.py` · **`row-count check : PASS` in both**, with
      `readable after : 0` against `1000` · changed the `''` to `NULL`, watched it fail loudly, and
      said what that tells you about `NOT NULL` on a column that can be empty
- [ ] **5.3** read · ran both arms of `grow.py` · **4.4ms at one turn and 54.2ms at four hundred**,
      against a flat ~6ms with `num_recent_events=20` · set `RECENT` to `1`, read what came back, and
      listed what would have to be in `user:` state for that window to be usable

## Section 6 — forgetting on purpose (ADK-29)

- [ ] **6.1** read · ran both arms of `forget.py` · **`user_states` 1 → 1** in the API-only arm and
      1 → 0 in the purge arm, with **`other customers intact: True` in both** · dropped `app_name`
      from the purge `WHERE` clause, watched it still exit `0`, and said what it had done to a second
      application sharing that file
- [ ] **6.2** read · ran both arms of `leak.py` · **`safe` against `a store of customer words is
      trackable`** · ran `git check-ignore -v data/sessions.sqlite3` and can say which rule matched
      and why it is a different one from the lab file's · can say why adding a `.gitignore` line after
      the first commit fixes nothing

## Section 7 — in production (ADK-29)

- [ ] **7.1** read · ran both arms of `backup.py` · **0 of 200 turns restored** from the copy against
      **200 of 200** from `VACUUM INTO`, with a 36 864-byte store and a 2.3 MB write-ahead log ·
      removed the reader's two lines, watched the copy arm go green, and said what that teaches about
      testing a backup on an idle system

## The paper

- [ ] Read [`papers/01-transaction-oriented-recovery.md`](papers/01-transaction-oriented-recovery.md)
      **after** the parts
- [ ] Ran both arms of the demo: **`turn_count 2 / events 2 / consistent`** against
      **`turn_count 2 / events 3 / TORN`**, with a rollback journal of **8 720 bytes** present in the
      first arm and absent in the second
- [ ] Changed `os._exit(9)` to `sys.exit(9)`, watched the ablation pass, and worked out which of the
      paper's mechanisms the interpreter performed for you
- [ ] **Said out loud** what this paper claimed in one sentence, its three failure classes and which
      one a log cannot survive, and which of the four letters is a promise you make rather than one
      you are given

## The project code

- [ ] `sutra/memory/persistence.py` written, with `SESSION_DB`, `session_service()` and
      `purge_user()`
- [ ] The unexported `SqliteSessionService` import appears in **exactly one file in the project**,
      with the ADK version and the date beside it
- [ ] `SESSION_DB` is absolute, its parent is created before the service is constructed, and
      `git check-ignore -q` on it exits `0`
- [ ] `purge_user` runs inside one `BEGIN IMMEDIATE ... COMMIT`, removes the `user_states` row, does
      **not** touch `app_states`, and returns a count
- [ ] The store choice is logged once at start-up, at INFO, naming the class and the resolved path
- [ ] `uv run python days/day-47-persistent-sessions/lab/gate.py` prints `findings: 0` and `exit: 0`
- [ ] You ran the gate **before** writing the module and saw it red
- [ ] You broke exactly one assertion on purpose — deleted the `user_states` statement from
      `purge_user` — and watched `purge_user left 1 rows behind` appear

## The whole day

- [ ] Every `TODO(me)` in §4 has been **read**, and the ones you answered are written down somewhere
      that is not this checklist
- [ ] `./m depth 47` is green
- [ ] `.venv/Scripts/ruff.exe format --check days/day-47-persistent-sessions/` passes
- [ ] `uv run python -m pytest -q -m "not live"` — you know which tests are red and why
- [ ] **`git diff --stat pyproject.toml uv.lock` prints nothing.** No package was added and no pin was
      moved.
- [ ] **`git status` shows no `.sqlite3` file anywhere** (Principle 9), and no `.env`
- [ ] `docs/PROGRESS.md` row appended verbatim from §11
- [ ] Commit made with the message in §11
