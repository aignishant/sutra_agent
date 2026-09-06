# Day 73 — Definition of done

`./m done 73` refuses to commit until every box is ticked. Tick a box only when you have actually run
the thing, not when you have read it. Today's measurements are mostly *states left on disk*, so most
boxes ask you to look in `lab/state/` rather than only at what the script printed.

## Before you start

- [ ] Day 72's parts and checklist are done.
- [ ] `lab/` scaffolded per §3 — six Python files, plus two under `lab/papers/idempotence/`.
- [ ] `git check-ignore -v days/day-73-ambient-agents/lab/_state.py` prints a matching rule.
- [ ] `git diff pyproject.toml uv.lock` is empty and stays empty. No package is added today.
- [ ] `uv run python days/day-73-ambient-agents/lab/gate.py; echo "exit: $?"` is **red** on all six
      checks before you write anything.
- [ ] You read `_state.py` first, and can say why two of the five eval cases are expected to fail.

## Section 1 — the agent nobody watches

- [ ] **1.1** read · you can name three things an interactive agent may do that an ambient one may not
- [ ] **1.2** read · you can say what each stage consumes and therefore why the order is forced, not
      chosen
- [ ] **1.3** read · ran `nightly.py` · recorded **rows=5**, **passed=3 total=5**, **failing=2** ·
      looked at all three files in `lab/state/` afterwards

## Section 2 — when it dies at three in the morning

- [ ] **2.1** read · ran `nightly.py --fail-at evals` · saw it **exit 1** with the index written and
      the evals not · read the `died_at` row in `lab/state/runs.jsonl`
- [ ] **2.2** read · ran `nightly.py --resume` immediately afterwards · recorded that `reindex` was
      **skipped** and the other two ran · can say why `STAGES` has to be data for that to be possible
- [ ] **2.3** read · ran `lock.py` and `lock.py --lock` · recorded **5 rows / ticket:4700 NO** against
      **6 rows / ticket:4700 yes** · can say why nothing errored in the first run
- [ ] **2.4** read · ran the stale-lock demonstration · saw the second `take_lock()` return **False**
      with the file still on disk · you picked one of the three release strategies and wrote down why
- [ ] You can state, in one sentence each, what a refusal and a wait would each mean for the *next*
      night's run

## Section 3 — the morning after

- [ ] **3.1** read · `lab/state/runs.jsonl` has both a `"ok": false` row and a `"ok": true` row · you
      can say what an empty run log means and why that is the hard case
- [ ] **3.2** read · ran `digest.py --sunny` and `digest.py` · recorded **0 failing cases named** and
      then **2**, with the same underlying facts
- [ ] **3.3** read · ran `cat lab/state/digest.md` · confirmed for yourself that it carries **no
      date** · can say how a job that stopped running entirely would look to a reader

## Section 4 — what wakes it

- [ ] **4.1** read · ran `triggers.py` · recorded that the installed ADK accepts exactly **`pubsub`**
      and **`eventarc`** · can say why the annotation had to be resolved rather than printed
- [ ] **4.2** read · you wrote the scheduler entry for your own machine (cron or Task Scheduler) and
      know where its output goes · 🅿️ you did not need to install anything

## Section 5 — in production

- [ ] **5.1** read · you priced *your* eval set: cases × requests per case, against the per-day quota
      of the provider you would run it on
- [ ] **5.2** read · you can name what an idempotency key is for, and why at-least-once delivery makes
      it non-optional rather than nice to have

## The paper — read it last

- [ ] `papers/01-idempotence.md` read **after** the parts, not before
- [ ] Ran the demo both ways from `lab/papers/idempotence/`: idempotent on records **10 against a
      truth of 10** (exit 0); `--off` records **28** (exit 1)
- [ ] Can say which of the nightly job's three stages is idempotent for the same reason the demo's
      `apply` is, and which one you would have to work at
- [ ] Noticed that the citation's title is assembled from the record's `title` **and** `subtitle`
      fields, and can say why that matters (§17.4.1 rule 5)

## Build brief

- [ ] `sutra/nightly.py` written: `STAGES` as data, `run(*, resume)`, `take_lock()`, and a
      `write_digest` that names failures
- [ ] You decided how the lock is released — including when the process is killed — and wrote the
      reason down
- [ ] You put a timestamp in the digest, which the lab deliberately does not have
- [ ] `tests/test_nightly.py` written, including the resume test and the digest-names-a-failure test
- [ ] `uv run python gate.py; echo "exit: $?"` re-run · you can say which of the six cleared

## Repo hygiene

- [ ] `./m depth 73` green — fourteen parts and one paper
- [ ] `./m trace` green, and AG-24 and ADK-51 close on this day and no others
- [ ] `./m wiki` run, so `docs/WIKI.md` and `docs/wiki/day-73.md` are not stale
- [ ] `uv run ruff format --check days/day-73-ambient-agents` clean
- [ ] `uv run ruff check days/day-73-ambient-agents/lab` clean
- [ ] `lab/state/` is left in a known condition — you either re-ran `nightly.py` clean or deleted it,
      rather than leaving a half-finished run's artefacts behind
- [ ] `docs/PROGRESS.md` row appended verbatim from §11, with the real commit hash and the `⚠️` the
      gate actually earned — no rounding up (P10)
- [ ] `docs/PAPERS.md` row for `doi:10.1145/2181796.2187821` present and dated (P7, §17.4.1)
