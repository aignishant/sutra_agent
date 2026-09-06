# Day 87 — checklist

**Definition of done.** `./m done 87` refuses to commit while any box is unticked. A box is ticked
when you have run the thing, not when you have read about it.

**The demo command for the whole day:**

```bash
cd days/day-87-config-not-billed/lab && uv run python envleak.py; echo "exit: $?"
```

**The rule for this day:** nothing below requires a billing account. If a box asks you to spend
money, it is a bug in this checklist.

---

## Setup

- [ ] `days/day-87-config-not-billed/lab/` exists with the nine files listed in the hub's §3, plus
      `fixtures/`.
- [ ] `git check-ignore -v days/day-87-config-not-billed/lab/fixtures/.env.sample` prints a matching
      rule.
- [ ] Confirmed no fixture contains a real credential.
- [ ] `git diff pyproject.toml uv.lock` is empty. No package is added today.
- [ ] Read `_deploy.py` and can say which of its constants are read out of the installed ADK and
      which are this day's own fixtures.

## Section 1 — what you hand over

- [ ] Read [1.1 What you hand over](parts/01-what-you-hand-over/1.1-what-you-hand-over.md);
      ran `surface.py` and `surface.py --names`.
- [ ] Added a sixth row of your own to the trade table, and said what you would do if the platform
      changed its mind about it.
- [ ] Read [1.2 🅿️ Why this day is parked](parts/01-what-you-hand-over/1.2-why-this-day-is-parked.md);
      can say what the marker promises and name the two directions it goes wrong.
- [ ] Applied the hollowness test to this day and got to three things you could point at in somebody
      else's config.
- [ ] Read [1.3 Reading the deploy surface](parts/01-what-you-hand-over/1.3-reading-the-deploy-surface.md);
      read the real `--help` and found one flag not discussed that quietly decides for you.
- [ ] Added `"--nonexistent_flag"` to `QUOTED`, watched `surface.py` go red and name it, removed it.
- [ ] Can say what `--adk_version` defaults to and why that is a different problem from deprecation.

## Section 2 — the config is the artefact

- [ ] Read [2.1 The config file ADK reads](parts/02-the-config/2.1-the-config-file-adk-reads.md);
      can name the three silent ways the file is not read.
- [ ] Renamed the fixture to drop the leading dot, saw the `FileNotFoundError`, said which behaviour
      you would rather have, and renamed it back.
- [ ] Read [2.2 What the CLI adds](parts/02-the-config/2.2-what-the-cli-adds.md);
      printed `CLASS_METHODS` and sorted the thirteen into agent, session management and deprecated.
- [ ] Can say the ratio of keys authored to keys sent.
- [ ] Read [2.3 Your .env travels](parts/02-the-config/2.3-your-env-travels.md);
      ran both arms and saw four keys become two.
- [ ] Counted the keys in your own `.env` — without pasting it anywhere — and said which the deployed
      desk would actually need.
- [ ] Can explain why Principle 9 was fully satisfied and the credentials still left.

## Section 3 — checking without deploying

- [ ] Read [3.1 A config checker that can go red](parts/03-checking-locally/3.1-a-config-checker-that-fails.md);
      ran both fixtures and saw exit `1` and exit `0`.
- [ ] Deleted `SUTRA_MODEL` from the good fixture, predicted the finding, ran it, put it back.
- [ ] Added the `adk_version` check; confirmed **both** fixtures go red and can say why that is
      correct.
- [ ] Read [3.2 The zero-budget lint](parts/03-checking-locally/3.2-the-zero-budget-lint.md);
      set the model to `gemini-2.5-pro`, saw which marker caught it, put it back.
- [ ] Tried a paid model from a provider not on the marker list, watched it pass, and can say which
      of the two designs you would ship.
- [ ] Read [3.3 The parked day that billed](parts/03-checking-locally/3.3-the-parked-day-that-billed.md);
      ran all three arms and saw eleven, zero and three.
- [ ] Defeated the fixed check on purpose with a command built into a variable, then removed it.

## Section 4 — what it would cost

- [ ] Read [4.1 Priced in requests](parts/04-what-it-costs/4.1-priced-in-requests.md);
      ran both arms and can say why one exits `2`.
- [ ] Changed `TURNS_PER_TICKET` to 5, saw the ratio move and the platform row not, put it back.
- [ ] Read [4.2 The dependency you inherit](parts/04-what-it-costs/4.2-the-dependency-you-inherit.md);
      printed `AGENT_ENGINE_REQUIREMENT` and read `--adk_version`'s two defaults.
- [ ] Can name the two things a deploy attaches that appear in no diff, and which one a line fixes.

## Section 5 — in production

- [ ] Read [5.1 The failure path nobody tests](parts/05-in-production/5.1-the-failure-path-nobody-tests.md);
      read `--agent_engine_id`'s default and said how many resources three iterations would create.
- [ ] Wrote the three-step sequence from memory and marked the window.
- [ ] Read [5.2 Before you would actually deploy](parts/05-in-production/5.2-before-you-would-actually-deploy.md);
      mapped `gate.py`'s six checks onto the nine items and named the two that could not have one.
- [ ] Re-sorted the nine items by what decays and found the one that moves a long way.

## The paper — after the parts

- [ ] Read [papers/01 The bill that follows the load](papers/01-the-bill-that-follows-the-load.md).
- [ ] Ran `demo.py` and `demo.py --off` in `lab/papers/elasticity/` and saw 130 against 686.
- [ ] Set every `multiplier` to 1, predicted the waste, ran it, and worked out why it is sixty-four
      per cent and not zero. Put it back.
- [ ] Can say the peak-to-average ratio, why the measured saving is lower than it, and which of the
      paper's obstacles this day met in a requirements file.

## The build brief

- [ ] `sutra/deploy.py` written — `config()`, `validate()`, `env_allowlist()`, `estimate()`,
      `parked()`, `plan()`.
- [ ] `config()` pins `adk_version` explicitly.
- [ ] `plan()` prints the assembled config **and** the command, and runs nothing.
- [ ] `plan()` includes `--agent_engine_id` from the config.
- [ ] `estimate()` returns a distinct code for the half with no free-tier unit.
- [ ] `parked()` run over the whole repository; findings counted, and the rule narrowed rather than
      suppressed if any were false.
- [ ] `tests/test_deploy.py` written — bad fixture fails, good fixture passes, missing `adk_version`
      refused, allowlist drops the password, and `plan()` asserted to start no process.
- [ ] **Decide how the credential arrives** once it is out of the config file. Needs another person.
- [ ] **Decide what the thirteen published methods may be called by.** Needs another person.
- [ ] **The Flash-Lite allowance measurement**, now open for a sixth day: one controlled burn, a
      count, a dated `docs/PACKAGES.md` row. Six lists are blocked on it.

## The evals, including ones that go red on demand

- [ ] `uv run python gate.py` runs and reports 0 of 6 — `sutra/deploy.py` is the build brief.
- [ ] `surface.py` exits `0`; `--names` exits `0`.
- [ ] `validate.py` exits `1`; `--fixed` exits `0`.
- [ ] `envleak.py` exits `1`; `--curated` exits `0`.
- [ ] `parked.py` exits `0`; `--sloppy` exits `1`; `--grep` exits `1`.
- [ ] `cost.py` exits `2`; `--model` exits `0`.
- [ ] `papers/elasticity/demo.py` exits `0`; `--off` exits `1`.
- [ ] **Break it and watch it go red:** added a `.sh` fixture with a bare `gcloud` line, confirmed
      `parked.py --sloppy` names it, then removed it.

## The request budget

- [ ] Confirmed **zero** provider requests and **zero** billed calls were made today.
- [ ] Confirmed no `gcloud`, no Vertex call, no `adk deploy` was executed.
- [ ] Can name the single thing this day left unrun, and say exactly what running it would create.

## Ledger & commit

- [ ] `./m depth 87` green.
- [ ] `./m trace` regenerated; day 87 closes exactly `ADK-68`.
- [ ] `./m wiki` regenerated.
- [ ] `docs/PROGRESS.md` row appended, verbatim from the hub's §11, with the real commit hash and the
      `⚠️` gate mark.
- [ ] `docs/PAPERS.md` — the `doi:10.1145/1721654.1721672` row added.
- [ ] Committed with the message in the hub's §11.
