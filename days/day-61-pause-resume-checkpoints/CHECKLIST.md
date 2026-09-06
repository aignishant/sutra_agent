# Day 61 — Definition of done

`./m done 61` refuses to commit until every box is ticked. Tick a box only when you have actually run
the thing, not when you have read it.

## Before you start

- [ ] Day 60's parts and checklist are done, and you can say what
      `@node(rerun_on_resume=True)` changed about its four-kill experiment. Today builds directly on
      it (P2).
- [ ] `uv run python days/day-61-pause-resume-checkpoints/lab/gate.py; echo "exit: $?"` is **red**
      before you write anything — six failures, exit 1 — and you have read which part each names.
- [ ] `lab/` scaffolded per §3 — twenty-six files, four of them shared helpers — and
      `sutra/checkpoints.py` created empty.
- [ ] `git diff pyproject.toml uv.lock` is empty and stays empty. No package is added today.

## Section 1 — two ways to stop

- [ ] **1.1** read · ran `twostops.py` · saw the **identical checkpoint** from both arms with
      **8 events against 7** and **1 error event against 0** · confirmed with `grep -c exit_code`
      that the exit code appears in **neither** store · can say what a terminal status would fix
- [ ] **1.2** read · ran `pausepoint.py` · found `4 WAITING` in the seven statuses and saw the
      framework's own one-item pause condition · ran the `dir(Runner)` filter and got `[]` · can say
      why every Day 62 pattern has to be shaped as a question
- [ ] **1.3** read · ran `handle.py` · saw the four arms and then the two root shapes giving
      **`ValidationError` for a Workflow and the documented `ValueError` for a BaseAgent** · read the
      runner source slice · noticed that resuming a *finished* run did 4 stations of work

## Section 2 — inside the box

- [ ] **2.1** read · ran `drill.py` then `layers.py` · saw **6 graph checkpoints, 4 agent
      checkpoints, 5 plain events** · reached the `KeyError: 'nodes'` on purpose · can name which
      author writes which kind
- [ ] **2.2** read · ran `box.py` · saw `summarise: 3`, `dedupe: 2` and **`report` absent from the
      map** · listed the five fields omitted because they are at their defaults · can say what
      absence means
- [ ] **2.3** read · ran `notinbox.py` · saw **0, 0, 0** occurrences for three plausible locals · ran
      `locals.py` and watched the counter reach 2, die, and restart at **1** · can name the one of
      the three categories that the state object does *not* fix
- [ ] **2.4** read · ran `often.py` · saw the byte column span a factor of four while the redo column
      spans 0 to 3 candidates · reached the mid-unit checkpoint showing
      **`{'scored': ['4521'], 'results': {}}`** · can say why the byte column is the wrong one

## Section 3 — the agent's own note

- [ ] **3.1** read · ran `pen.py --root` · saw `agent_states keys = ['dedupe']` and **two `skip`
      lines** on the resume · printed `set_agent_state`'s signature and saw `-> None` · commented out
      the `yield` and watched the checkpoint disappear
- [ ] **3.2** read · ran `none.py` · saw the loader's **four-line body** and
      `AttributeError: 'NoneType' object has no attribute 'scored'` · confirmed that an empty
      pydantic model is **truthy**, unlike an empty dict · can say why `or` is accidentally correct
      and still the wrong thing to write
- [ ] **3.3** read · ran `pen.py` · saw `agent_states keys = []` on the resume and **6 checkpoints in
      the log** · read the checkpoint trail and found the `["4521"]` written *below* a
      `["4521", "4633"]` · ran the kill-and-count test and got **`resume did less work: False`**
- [ ] **3.4** read · ran `instead.py` and saw **2 of 4, exit 0** · ran `instead.py --rerun` and saw
      **4 of 4** · reached the shared-key collision · can name both halves of the repair and say what
      the half-repaired run looks like from outside
- [ ] **3.5** read · ran `endof.py` · saw the fifth dedupe event carrying
      **`end_of_agent=True agent_state=None`** · saw a finished run resumed go **15 → 25 events with
      the whole list rescored**, and **15 → 18 with nothing at all** when the flag was False · can
      state the tension between this and 3.4 in one sentence

## Section 4 — the drill

- [ ] **4.1** read · ran `drill.py` twice and got **15 events, 10 checkpoints, 0 model requests**
      both times · saw the second start into one store raise **`AlreadyExistsError`** · can say why
      19 ≠ 15 is not a regression
- [ ] **4.2** read · ran `kill.py` · saw **exit code 9, stderr 0 bytes** and the five-record trail ·
      ran the `sys.exit` / `os._exit` comparison and watched `finally` run in one and not the other ·
      can say why only one of them tests durability
- [ ] **4.3** read · ran `kill.py` then `pickup.py` · saw `summarise` skipped, `report` run for the
      first time, all three nodes end at **status 3**, and the log go **7 → 19** · noticed the
      dedupe list was rescored · resumed with a bogus id and saw the store grow **19 → 21** anyway
- [ ] **4.4** read · ran `storage.py` · saw `is_resumable: True` beside
      **`SessionNotFoundError: Session not found: S1`** · ran the single-process version and watched
      it pass · can name the two separate decisions and which one `is_resumable` is

## Section 5 — the failure lab

- [ ] **5.1** read · ran `drift.py` · saw `BaseAgentState` **`extra='forbid'`** raise
      `extra_forbidden` naming `cursor`, and `NodeState` **`extra='ignore'`** accept the same drift
      silently · ran the added-field case and saw `attempts=0` appear from nowhere · can fill in all
      three rows of the caught/not-caught table
- [ ] **5.2** read · ran `ghost.py` · saw **both stored `agent_state` values are `null`** and the
      resume return **`Progress(done=[])`** · read the runtime source comment that invents it ·
      can say what it does to the `is None` guard
- [ ] **5.3** read · ran `polite.py` · saw **identical checkpoints**, the destroyed run resume to
      exit 0 and the raised run fail · saw the **control** — one error event deleted, same store,
      resumes cleanly · can say why "stop raising" is the wrong conclusion

## Section 6 — in production

- [ ] **6.1** read · ran `stamp.py` · saw a v1 checkpoint **parse without complaint** and then be
      refused by the version check · ran the un-bumped case and watched the guard pass on data that
      means something else · can say precisely what a stamp does and does not detect
- [ ] **6.2** read · ran `leaks.py` · saw the ticket text **4 times** in a store that exists only
      because of checkpointing · ran the deletion case and saw **0 rows in the archive, 4
      occurrences in the log** · can recite the four questions and name the one that removes work

## The build

- [ ] `sutra/checkpoints.py` written, with a comment at the top saying **where the progress lives**
      and why (3.3, 3.4).
- [ ] The session-state key is namespaced by station name (3.4).
- [ ] `rerun_on_resume` is set, with a comment saying it is a correctness setting and naming what it
      costs on a duplicate resume (3.4, 3.5).
- [ ] `schema_version` is stamped and compared with `!=`, not `<` (6.1).
- [ ] The four questions were applied to every field, and at least one value is stored as an id
      rather than as content (6.2).
- [ ] `uv run python days/day-61-pause-resume-checkpoints/lab/gate.py` is **green**, 6/6, exit 0.

## The tests

- [ ] `tests/test_checkpoints.py` exists and has the **kill-and-count** test: start, kill, resume in
      a separate process, assert the second attempt does *less* work than the first (3.3).
- [ ] **Break it, watch it go red, fix it:** remove `rerun_on_resume` from the node and watch the
      kill-and-count test fail. Put it back.
- [ ] **Break it, watch it go red, fix it:** delete the `end_of_agent=True` call and watch `gate.py`
      check five go red. Put it back.
- [ ] `uv run python -m pytest tests/test_checkpoints.py -q` passes.
- [ ] `uv run ruff check .` and `uv run ruff format --check .` are clean on everything you wrote.

## The ledger

- [ ] The `docs/PROGRESS.md` row from §11 is pasted, with the real commit hash.
- [ ] Confirmed there is **no** `PACKAGES.md`, `PAPERS.md` or `SKILL_PROVENANCE.md` row to add today,
      and you know why for each.
- [ ] Request budget confirmed **zero** — no provider was called by any script.
- [ ] `uv run python scripts/depth_check.py 61` passes.
- [ ] Committed as `day 61: pause/resume and checkpoints in ADK — closes ADK-44, ADK-45`.
