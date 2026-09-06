# Day 93 — checklist

**Definition of done.** `./m done 93` refuses to commit while any box is unticked. A box is ticked
when you have run the thing, not when you have read about it.

**The demo command for the whole day:**

```bash
cd days/day-93-what-a-stranger-sees/lab && uv run python gate.py; echo "exit: $?"
```

---

## Setup

- [ ] `days/day-93-what-a-stranger-sees/lab/` exists with the thirteen files listed in the hub's §3.
- [ ] `git check-ignore -v days/day-93-what-a-stranger-sees/lab/_repo.py` prints a matching rule, and
      you can say why that matters for a day whose checks count *tracked* files.
- [ ] `git diff pyproject.toml uv.lock` is empty. No package is added today.
- [ ] Read `_repo.py` and can say why every function reads the live tree instead of a saved snapshot.
- [ ] Confirmed nothing in this day wrote to the repository root — `LICENSE` and `SECURITY.md`
      candidates are in `lab/candidates/`, deliberately.

## Section 1 — the stranger

- [ ] Read [1.1 Public means a stranger](parts/01-the-stranger/1.1-public-means-a-stranger.md);
      ran `gate.py` and can say how many of the seven checks run the agent.
- [ ] Can say why a stranger's silence is a worse signal than a colleague's complaint.
- [ ] Read [1.2 The five files](parts/01-the-stranger/1.2-the-five-files-before-the-code.md);
      ran both arms and can say what a public repository with no `LICENSE` grants a reader.
- [ ] Read `candidates/LICENSE.candidate` and `candidates/SECURITY.candidate.md` and formed a view on
      whether each is right for this repository.
- [ ] Read [1.3 The README that documents the design](parts/01-the-stranger/1.3-the-readme-that-documents-the-design.md);
      ran both arms and can name all three numbers in the section-count finding.
- [ ] Found the sentence in `README.md` that describes `papers/` **correctly**, and can say which of
      the two contradicting sentences was written later.

## Section 2 — running the README

- [ ] Read [2.1 A README is a test](parts/02-running-the-readme/2.1-a-readme-is-a-test.md);
      ran `runnable.py` and `--list` and can name the five commands neither arm checks.
- [ ] Can say what the tell was that the first version of that check was wrong rather than the repo.
- [ ] Read [2.2 The setup block](parts/02-running-the-readme/2.2-the-setup-block-that-fails.md);
      can say which of the two failures reproduces on a fresh clone elsewhere, and how you would
      find out without owning that machine.
- [ ] Wrote the precondition sentence the README is missing — one sentence, no apology.
- [ ] Read [2.3 What a README owes](parts/02-running-the-readme/2.3-what-a-readme-owes.md);
      wrote the five answers from memory before opening the README, and compared.
- [ ] Measured what fraction of the README a reader passes before the first command.

## Section 3 — the docs pass

- [ ] Read [3.1 Seventeen thousand links](parts/03-the-docs-pass/3.1-seventeen-thousand-links.md);
      ran both arms and can say why the naive report is worse than useless rather than merely noisy.
- [ ] Opened one of the three broken links under `days/` and named the class of mistake.
- [ ] Read [3.2 Four kinds of broken link](parts/03-the-docs-pass/3.2-four-kinds-of-broken-link.md);
      ran both arms and can say what happens if you fix the twenty-two by editing the files.
- [ ] Worked out where a fifth `OWNERS` rule for `skills/` must sit, and why one position is wrong.
- [ ] Read [3.3 The index that regenerates broken](parts/03-the-docs-pass/3.3-the-index-that-regenerates-broken.md);
      ran the `sed` and the basename check and saw twenty-two of twenty-two.
- [ ] Wrote the exact string `[2.3](2.3-two-runs-at-once.md)` would have to become in `docs/wiki/`.

## Section 4 — nothing that should not be there

- [ ] Read [4.1 The scan before the door opens](parts/04-nothing-extra/4.1-the-scan-before-the-door-opens.md);
      ran `secrets.py`, opened both hit files, and decided real or placeholder from the file rather
      than the string.
- [ ] Can name three kinds of secret this scan cannot find, and what would have to change for each.
- [ ] Understood why `--loud` exists and did **not** run it on a repository you care about.
- [ ] Read [4.2 History is the part you cannot take back](parts/04-nothing-extra/4.2-history-is-the-part-you-cannot-take-back.md);
      ran `--history` and can say what you would do in the first sixty seconds if it had found three.
- [ ] Can say why `git filter-repo` is not the first action after a key is pushed.
- [ ] Read [4.3 The ledger a stranger reads](parts/04-nothing-extra/4.3-the-ledger-a-stranger-reads.md);
      ran both arms and `./m brief 94`, and can say which number is true and which is the truth.
- [ ] Worked out what a backfilled row for day 83 must contain, and found the field `git log` alone
      cannot supply.

## Section 5 — the demo, and the list

- [ ] Read [5.1 A demo that fails honestly](parts/05-the-demo/5.1-a-demo-that-fails-honestly.md);
      ran both arms and can say which line of `--pretend` is false.
- [ ] Found the day whose build brief owns the first `MISSING` stage.
- [ ] Can say whether fifty-two promised against five present is a defect, and which README sentence
      decides it.
- [ ] Read [5.2 What a real public repository adds](parts/05-the-demo/5.2-what-a-real-public-repo-adds.md);
      mapped each failing check onto the nine items and found the check that maps to more than one
      and the item that maps to none.
- [ ] Re-sorted the nine by what stops being fixable, and found the two that move.

## The paper — after the parts

- [ ] Read [papers/01 The document that runs](papers/01-the-document-that-runs.md).
- [ ] Ran `demo.py` and `demo.py --off` in `lab/papers/literate/` and saw a one-digit drift caught
      and missed.
- [ ] Ran the weaver against the clean `doc.md` and saw ten of ten.
- [ ] Added a fourth prose-only claim to `doc.md`, re-ran, and can say why the count did not move.
- [ ] Can name the half of the paper that shipped and the half that did not, and which README claims
      could be woven.

## The build brief

- [ ] `scripts/public_check.py` written — the seven checks as data, runnable from `./m`.
- [ ] Wired into `./m check`, so a broken link, a missing `LICENSE` or a secret-shaped string fails
      the build.
- [ ] The secret scanner has an allowlist, each entry carrying a reason and who looked.
- [ ] The link check excludes `legacy/` **in code, with a comment saying why** — not by leaving
      eighteen permanent failures.
- [ ] `scripts/wiki.py` rewrites relative links when copying a part's answer into `docs/wiki/`,
      handling both sibling-style and parent-relative forms.
- [ ] `tests/test_public_check.py` written — the fenced-block test, the never-print-a-value test, and
      the missing-ledger-row test.
- [ ] **Add `LICENSE`** — decaying, and the README's licence sentence already points at it.
- [ ] **Backfill `docs/PROGRESS.md`** from `git log` — forty-three rows, harder every week.
- [ ] **Fix the one lint error** so `./m check` matches what the README promises it prints.
- [ ] **Add `SECURITY.md` and `CONTRIBUTING.md`**, and the machine precondition sentence in Setup.

## The evals, including ones that go red on demand

- [ ] `uv run python gate.py` exits `1` with zero of seven passing.
- [ ] The gate's comfortable-arm block shows `firstfiles`, `readme_contract`, `ledger` and `demo` all
      **going green**, and you can say why each sentence they print is still true.
- [ ] `firstfiles.py` exits `1`; `--readme-only` exits `0`.
- [ ] `readme_contract.py` exits `1`; `--prose` exits `0`.
- [ ] `links.py` exits `1`; `--naive` exits `1` and reports thirty-four more.
- [ ] `owners.py` exits `1`; `--one-pile` exits `1`.
- [ ] `secrets.py` exits `1`; `--history` exits `1` with the same two.
- [ ] `ledger.py` exits `1`; `--count` exits `0`.
- [ ] `demo.py` exits `1`; `--pretend` exits `0`.
- [ ] `runnable.py` exits `1`; `--list` exits `0`.
- [ ] `papers/literate/demo.py` exits `0`; `--off` exits `1`.
- [ ] **Break it and watch it go red:** added a file named `LICENSE` in the repository root,
      confirmed `firstfiles.py` reports three of five, then removed it again.

## The request budget

- [ ] Confirmed **zero** provider requests were made today, to every provider.
- [ ] Can say why this day is free by nature rather than by compromise, and name the five README
      commands no check here covers and why each is declined.

## Ledger & commit

- [ ] `./m depth 93` green, with `ids: []` accepted.
- [ ] `./m trace` regenerated; day 93 closes no IDs, which is what plan §14 assigns it.
- [ ] `./m wiki` regenerated.
- [ ] `docs/PROGRESS.md` row appended, verbatim from the hub's §11, with the real commit hash, the
      `—` IDs column and the `⚠️` gate mark.
- [ ] `docs/PAPERS.md` — the `doi:10.1093/comjnl/27.2.97` row added.
- [ ] Committed with the message in the hub's §11.
