# Day 56 — Definition of done

`./m done 56` refuses to commit until every box is ticked. Tick a box only when you have actually run
the thing, not when you have read it.

## Before you start

- [ ] Day 55's parts and checklist are done, and you can state in one sentence the difference between
      a call that comes back and a hand-over that does not (P2).
- [ ] `python -c "from google.adk import Context; import inspect; print(inspect.signature(Context.run_node))"`
      prints a signature containing `node_input` and `run_id`. If it does not, part 3.4 is stale and
      the day is amended before it is written (P8, P14).
- [ ] `uv run python days/day-56-planning-and-replanning/lab/gate.py; echo "exit: $?"` is **red**
      before you write anything, and you have read the finding it reports.
- [ ] `lab/` scaffolded per §3 — sixteen scripts plus `lab/papers/strips/` — and `tests/test_planning.py`
      created empty.
- [ ] `git diff pyproject.toml uv.lock` is empty and stays empty. No package is added today.

## Section 1 — what a plan is

- [ ] **1.1** read · ran `shape.py` · can name the four questions data answers and prose does not ·
      reached `FrozenInstanceError` on purpose by assigning to a step's `argument` · counted the
      actions in the paragraph and compared with the three steps
- [ ] **1.2** read · ran `shape.py --validate` · saw **3 of 6 executable**, each failure a different
      field · added a seventh candidate breaking two rules and saw both reported · can say which
      reader each of the three fields is for
- [ ] **1.3** read · ran `shape.py --score` and saw **3/4, missing KB-104, with nothing executed** ·
      ran `shape.py --diff` and read `dropped` / `added` / `kept` · edited `REQUEST` to name `4702`
      and wrote down what happened to the requirement set

## Section 2 — two ways to decide

- [ ] **2.1** read · ran `cover.py --reactive` and saw **4/4** · ran
      `cover.py --reactive --shapes --budget 10` and saw the four-part arm stop at **4 steps** with
      ten available, reporting `nothing left that resembles the last observation` · found the single
      line in `_model.py` that makes the loop reactive
- [ ] **2.2** read · ran `cover.py` and saw **1 request, 3 steps, 3/4, missing KB-104** · can say why
      the planner could not reach that article · edited `REQUEST` to name `KB-104` and re-ran
- [ ] **2.3** read · ran `cover.py --shapes` · saw **both strategies at 4/6 on the four-part request
      missing different things** · can say which of them skipped something the request named · moved
      `4815` to the front of the request and wrote down whether the misses changed
- [ ] **2.4** read · ran `price.py` and saw **20 runs a day against 5** · ran `price.py --replan` and
      found the row where planning becomes **dearer** · can state why `MAX_REPLANS = 1` and not 3

## Section 3 — walking the plan

- [ ] **3.1** read · ran `walk.py` and saw **5 of 5 completed with zero decisions** · added a step
      with an action outside `ACTIONS` and saw `CONTRADICTION unknown action 'investigate'` · can say
      which step of Day 3's loop the executor deletes
- [ ] **3.2** read · ran `walk.py` and `walk.py --carry` · saw that **only the `sees` column differs**
      and both report 5 of 5 · moved `compare` to the front and watched it still report `ok` · can
      state the difference between an order and a dependency
- [ ] **3.3** read · ran `resume.py --clean`, `--start`, `--resume` · opened `run-state.json` and read
      it · ran `--resume` **twice** and saw `cursor at step 5 of 4` with **exit 0** · can name which
      of the four production fields would have made it refuse
- [ ] **3.4** read · ran `dynamic.py` and saw **five outputs for four steps, zero model calls** ·
      changed `name=f"step_{i}"` to `step-{i}` and read the `ValidationError` in full, then put it
      back · can say what `rerun_on_resume=True` obliges you to keep out of the orchestrator body

## Section 4 — when a plan dies

- [ ] **4.1** read · ran `classify.py` and saw **2 ok, 1 hiccup, 3 contradiction** · can give the one
      question that separates the two kinds · added a seventh case that is both and wrote down which
      wins
- [ ] **4.2** read · ran `classify.py --retry` · saw the hiccup clear on **attempt 2** and the three
      contradictions identical on **all three** · counted what a five-retry policy would cost against
      the free-tier daily limit
- [ ] **4.3** read · ran `silent.py --useless` · saw **3/3 succeeded and 1/3 informative, exit 0** ·
      added `limits` to `GOAL_WORDS`, re-ran, and can say whether the run got any better
- [ ] **4.4** read · ran `silent.py --stale` · saw **0 contradictions, 0 replans, 1 reply to a closed
      ticket** · found the word `closed` in step 2's own returned text · can name the two production
      mechanisms that close the staleness window

## Section 5 — the second edition

- [ ] **5.1** read · ran `patch.py` · saw **patch 2/3 against rewrite 3/3** · can say what a patch can
      never do · built the variant where the dead step is redundant and saw the patch win
- [ ] **5.2** read · ran `patch.py --sunk` · saw **4 steps / 0 repeats against 5 steps / 1 repeat** ·
      added a `reply` before the failing step, re-ran both arms, and printed `world.sent` for each
- [ ] **5.3** read · ran `brake.py` and `brake.py --max 0`, both **exit 1** · can name the three things
      the escalation sentence carries · ran `brake.py --max 3` and looked the request count up in
      part 2.4's table
- [ ] **5.4** read · ran `brake.py --oscillate` · saw **12 editions with no error anywhere**, then 2
      with the brake · can explain why each edition is individually correct · raised the cap to 40 and
      wrote down what that costs in free-tier days

## Section 6 — in production

- [ ] **6.1** read · ran `notgoal.py` (**exit 0**) and `notgoal.py --check` (**exit 1,
      `found in evidence: nothing`**) · can name the four mechanisms from this day that do **not** fire
      · changed the plan to look up `4610` and re-ran
- [ ] **6.2** read · ran `review.py` and `review.py --trace` · can name the three questions the card
      answers and which field says whether a step *should* happen · added a `close_ticket` step and
      found the line of the card that is now wrong
- [ ] **6.3** read · ran `irreversible.py` and `--ordered` · saw the reply go out on **0 evidence**
      then on **2**, with the actions unchanged · added `compare` to `IRREVERSIBLE` and re-ran · can
      give the case where *put it last* is not available
- [ ] **6.4** read · ran `cover.py --shapes` and `price.py --replan` for your own two numbers · can
      name the trigger condition for hierarchy and say why plan repair is worth having anyway

## The paper — read after the parts

- [ ] **01 STRIPS** read · ran `demo.py` (**consistent, exit 0**) and `demo.py --no-delete`
      (**INCONSISTENT, exit 1**) · saw that both plans are **four steps and eight states explored**
      and only the **order** differs · added the `reopen(4633)` operator and wrote down what the
      no-delete arm does with it · can say which half of the paper survived and which the field
      replaced

## The build

- [ ] `sutra/planning.py` carries `Step`, `Plan`, `MAX_REPLANS`, `plan`, `execute`, `classify`,
      `replan` and `answered`
- [ ] `MAX_REPLANS` has a comment naming **the run and the date** it came from, not a bare number
- [ ] The module names its irreversible actions in one set, and `execute` orders them last
- [ ] `execute` can report `UNANSWERED` — a run where every step succeeded and the goal was not
      reached is not a success (P10)
- [ ] `classify` returns different kinds for `429 Too Many Requests` and `no ticket with id '9999'`
- [ ] You decided the **3.2 question** — whether `Step` gets an `id` and a `needs` list — and wrote
      down the decision and the reason, having seen four parts of this day fail for want of it
- [ ] `tests/test_planning.py` holds all six tests from §4, including
      `test_a_run_where_every_step_succeeded_can_still_be_unanswered`

## The gates

- [ ] `uv run python days/day-56-planning-and-replanning/lab/gate.py; echo "exit: $?"` prints
      `findings: 0` and `exit: 0`
- [ ] You broke exactly one finding on purpose — deleted the date from the comment beside
      `MAX_REPLANS` — saw finding 2 appear, and put it back
- [ ] `uv run python -m pytest tests/test_planning.py -q -m "not live"` is green, with no network
- [ ] `./m depth 56` is green
- [ ] `./m check` is green
- [ ] `git diff pyproject.toml uv.lock` is empty

## The ledger

- [ ] `docs/PROGRESS.md` has the day 56 row from §11, with the real commit hash
- [ ] `docs/PAPERS.md` has the STRIPS row, dated **2026-09-05**, naming
      `days/day-56-planning-and-replanning/papers/01-strips.md`
- [ ] `docs/PACKAGES.md` and `docs/SKILL_PROVENANCE.md` are unchanged — today adds no rows to either
- [ ] The **6.4 ADR** is written: the median plan length above which you add hierarchy, and the
      edition count above which planning stops being cheaper than reacting
- [ ] Commit made with the message from §11; no `.env` in the diff
- [ ] **Zero model calls were spent.** If you spent any, write down how many and on what.
