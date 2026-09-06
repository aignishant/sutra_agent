# Day 86 — checklist

**Definition of done.** `./m done 86` refuses to commit while any box is unticked. A box is ticked
when you have run the thing, not when you have read about it.

**The demo command for the whole day:**

```bash
cd days/day-86-cloud-run-shaped/lab && uv run python replicas.py; echo "exit: $?"
```

---

## Setup

- [ ] `days/day-86-cloud-run-shaped/lab/` exists with the thirteen files listed in the hub's §3.
- [ ] `uv run python -c "import fastapi, uvicorn, httpx, yaml; print('all four present')"` prints.
- [ ] `git diff pyproject.toml uv.lock` is empty. No package is added today.
- [ ] `git check-ignore -v days/day-86-cloud-run-shaped/lab/_app.py` prints a matching rule, and you
      can say why that matters before running `context.py`.
- [ ] Read `_app.py` and can name the three things in it that every finding in sections 4 and 5
      comes out of.
- [ ] Confirmed for yourself that `docker` is absent, so you know which of this day's claims are
      measured and which are written down unrun.

## Section 1 — what a container promises

- [ ] Read [1.1 An image is a recipe](parts/01-what-a-container-promises/1.1-an-image-is-a-recipe.md);
      listed the desk's unwritten assumptions before reading the table.
- [ ] Can say why `--frozen`, `--no-dev` and `--no-install-project` are each on the `uv sync` line.
- [ ] Read [1.2 A layer is written once](parts/01-what-a-container-promises/1.2-a-layer-is-written-once.md);
      can answer whether a file deleted in a later layer is in the image and in the container.
- [ ] Reordered `Dockerfile` so the source is copied first, ran `image.py`, and put it back.
- [ ] Read [1.3 The platform chooses the port](parts/01-what-a-container-promises/1.3-the-platform-chooses-the-port.md);
      can say why `0.0.0.0` is a warning sign on a laptop and correct in a container.
- [ ] Can say what uvicorn would do with the literal string `$PORT` in the list-form `CMD`.

## Section 2 — the image contract

- [ ] Read [2.1 Writing the Dockerfile](parts/02-the-image-contract/2.1-writing-the-dockerfile.md);
      can say why `useradd` and `chown` share one `RUN`, and why `USER` is placed where it is.
- [ ] Can say why the `HEALTHCHECK` uses `python -c` rather than `curl`.
- [ ] Read [2.2 Eight properties](parts/02-the-image-contract/2.2-eight-properties-checked.md);
      ran both arms and saw 8 of 8 against 2 of 8.
- [ ] Can state what `8 of 8` proves and what a reader wrongly takes it to prove.
- [ ] Read [2.3 The build context](parts/02-the-image-contract/2.3-the-build-context-nobody-looked-at.md);
      ran both arms and saw 414,219,769 bytes against 2,207,035.
- [ ] Named the second file the ablation reports besides `.env`, and what is in it that matters.
- [ ] Commented out the `.git` line in `.dockerignore`, predicted both counts, ran it, put it back.

## Section 3 — configuration from outside

- [ ] Read [3.1 An app that refuses to start](parts/03-config-from-outside/3.1-an-app-that-refuses-to-start.md);
      ran both arms and saw `ConfigError: missing required environment: SUTRA_API_KEY`.
- [ ] Can say why an empty string counts as missing, and why every missing name is collected before
      raising.
- [ ] Read [3.2 Three ways a secret gets in](parts/03-config-from-outside/3.2-three-ways-a-secret-gets-in.md);
      can explain why a build argument is the drawer rather than the neighbour.
- [ ] Found the fourth route a secret can take that the part does not list in its table.
- [ ] Read [3.3 compose.yaml is the shape](parts/03-config-from-outside/3.3-compose-is-the-shape.md);
      found the two places the file expresses a privilege boundary, one of which is an absence.
- [ ] Can say the one thing `depends_on` guarantees and the one thing it is believed to.

## Section 4 — health checks

- [ ] Read [4.1 Alive and able to work](parts/04-health-checks/4.1-alive-and-able-to-work.md);
      can give the consequence of each probe rather than its definition.
- [ ] Can say what goes wrong when a dependency check is put in the liveness probe.
- [ ] Read [4.2 The check that only watched the process](parts/04-health-checks/4.2-the-check-that-only-watched-the-process.md);
      ran both arms and saw `200 ok` beside `503 quota_ledger_missing`.
- [ ] Named the flag on each of days 79, 81, 82 and 86 that produces the finding-hiding arm.

## Section 5 — the word "stateless"

- [ ] Read [5.1 The statefulness audit](parts/05-the-word-stateless/5.1-the-statefulness-audit.md);
      ran it and identified the line that proves the process was really replaced.
- [ ] Can define "stateless" in one sentence without the word "data", and name the piece of Sutra
      that fails the definition.
- [ ] Read [5.2 Two replicas](parts/05-the-word-stateless/5.2-two-replicas-one-failure.md);
      ran both arms and saw the session failure vanish while the lost updates did not.
- [ ] Can say why a mutex fixes the single-replica measurement and not the problem.
- [ ] Set `SUTRA_RMW_DELAY` to `0`, ran the two-replica arm several times, and can say what the
      delay is actually doing.
- [ ] Read [5.3 What a real deployment adds](parts/05-the-word-stateless/5.3-what-a-real-deployment-adds.md);
      re-sorted the nine items by what is already costing something today.
- [ ] Can name the everyday operation that makes the replica count two without anybody scaling.

## The paper — after the parts

- [ ] Read [papers/01 What isolation costs](papers/01-what-isolation-costs.md).
- [ ] Ran `demo.py` and `demo.py --off` in `lab/papers/isolation/` and saw 0.00% against 16.0%,
      then both at zero.
- [ ] Can explain why the bulk row reads `0.00%` in **both** runs and why that is not a bug.
- [ ] Changed `CHATTY_JOBS` to 400, predicted the chatty overhead, and checked.
- [ ] Can state both halves of the paper's finding, and which half applies to a service that mostly
      waits on a network.

## The build brief

- [ ] `sutra/deploy.py` written — `image_report()`, `context_report()`, `required_env()`,
      `readiness()`, `state_inventory()`, `replica_limit()`.
- [ ] `context_report()` **redacts values** when it names a baked secret. CI logs are a place a key
      can appear.
- [ ] `readiness()` returns a reason, with separate reasons for missing and unparseable.
- [ ] `replica_limit()` derives its answer from `state_inventory()` rather than returning a
      hard-coded `1`.
- [ ] `tests/test_deploy.py` written — the `GOOGLE_API_KEY` pattern test, the `.env` exclusion test,
      the every-missing-name test, and the 503-with-a-reason test.
- [ ] **The ledger increment made atomic.** This is a live defect, measured losing fifteen of twenty
      updates with one replica — not a deployment task, and not fixed with a lock.
- [ ] **The session store moved out of the process**, pointed at Day 47's persistent sessions.
- [ ] **A container runtime installed and the image built once**, then run and probed. Expect it to
      fail on `sutra.api:app`, which is Day 85's build brief.
- [ ] `healthcheck:` added to the compose api service, pointed at `/readyz` — four lines, free.
- [ ] Base image pinned by digest, using the command in the `Dockerfile`'s `TODO(me)`.

## The evals, including ones that go red on demand

- [ ] `uv run python gate.py` runs and reports 0 of 6 — `sutra/deploy.py` is the build brief.
- [ ] `uv run python config.py` exits `0`; `--half` exits `1`.
- [ ] `uv run python image.py` exits `0`; `--sloppy` exits `1`.
- [ ] `uv run python context.py` exits `0`; `--no-ignore` exits `1`.
- [ ] `uv run python health.py` exits `0`; `--liveness-only` exits `1`.
- [ ] `uv run python audit.py` exits `1`, and the reason is a design fact rather than a bug.
- [ ] `uv run python replicas.py` exits `0`; `--single` exits `1`.
- [ ] `uv run python papers/isolation/demo.py` exits `0`; `--off` exits `1`.
- [ ] No uvicorn subprocess is left running after any of the above.
- [ ] **Break it and watch it go red:** removed the `USER desk` line from `Dockerfile`, ran
      `image.py`, confirmed it drops to 7 of 8, and put it back.

## The request budget

- [ ] Confirmed **zero** provider requests were made today, to every provider.
- [ ] Can list the six commands in the hub's §6 that were **not** run, and say what each would
      catch.
- [ ] Can say why the two-replica finding did not need a container runtime.

## Ledger & commit

- [ ] `./m depth 86` green.
- [ ] `./m trace` regenerated; day 86 closes exactly `ADK-66`, `ADK-67`, `OPS-17`.
- [ ] `./m wiki` regenerated.
- [ ] `docs/PROGRESS.md` row appended, verbatim from the hub's §11, with the real commit hash and
      the `⚠️` gate mark.
- [ ] `docs/PAPERS.md` — the `doi:10.1109/ISPASS.2015.7095802` row added.
- [ ] Committed with the message in the hub's §11.
