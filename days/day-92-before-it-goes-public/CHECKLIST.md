# Day 92 — checklist

**Definition of done.** `./m done 92` refuses to commit while any box is unticked. A box is ticked
when you have run the thing, not when you have read about it.

**The demo command for the whole day:**

```bash
cd days/day-92-before-it-goes-public/lab && uv run python gate.py; echo "exit: $?"
```

---

## Setup

- [ ] `days/day-92-before-it-goes-public/lab/` exists with the eleven files listed in the hub's §3.
- [ ] `git check-ignore -v days/day-92-before-it-goes-public/lab/_repo.py` prints a matching rule, and
      you can say which of this repository's three relevant ignore rules it is.
- [ ] `git diff pyproject.toml uv.lock` is empty. No package and no security tool is added today.
- [ ] Read `_repo.py` and can state its two rules — derive, never hardcode; report the location,
      never the value — and say why the second one matters for a report committed to this repository.

## Section 1 — what a review is

- [ ] Read [1.1 A review is a set of checks that can fail](parts/01-what-a-review-is/1.1-a-check-that-can-fail.md);
      ran `gate.py` and can say how many of the eight checks call a model.
- [ ] Can explain what the fault pass adds to a `PASS` line, and which check is the fault test for
      another check.
- [ ] Read [1.2 The inventory comes before the opinion](parts/01-what-a-review-is/1.2-the-inventory-comes-first.md);
      reproduced the tracked-file count with `git ls-files | wc -l`.
- [ ] Can say why `git ls-files` is the right denominator and a filesystem walk is not.
- [ ] Read [1.3 The checklist that answers itself](parts/01-what-a-review-is/1.3-the-checklist-that-answers-itself.md);
      ran `gate.py --headline`, looked for a false statement, and did not find one.
- [ ] Named the five days of this curriculum that have now produced the same shape.

## Section 2 — secrets

- [ ] Read [2.1 The scan that found nothing](parts/02-secrets/2.1-the-scan-that-found-nothing.md);
      ran the scan and the self-test and can say what each would look like if the other were failing.
- [ ] Broke the detector on purpose (`{35}` → `{135}`), saw which command told you, and put it back.
- [ ] Can say why a deleted secret still counts and which flag makes the history scan cover unmerged
      branches.
- [ ] Read [2.2 The channel no file scanner reads](parts/02-secrets/2.2-the-channel-no-file-scanner-reads.md);
      ran `metadata.py` and reproduced the finding with `git log --format='%an <%ae>' | sort -u`.
- [ ] Listed four channels a public repository publishes, and for each said whether this day scans it.
- [ ] Read [2.3 The template that drifted](parts/02-secrets/2.3-the-template-that-drifted.md);
      ran both arms and can say why *listed in `.gitignore`* is a different question from *not
      tracked*.

## Section 3 — what is not a secret

- [ ] Read [3.1 One account name, fifty-one lines](parts/03-what-is-not-a-secret/3.1-fifty-one-lines.md);
      ran both arms and can name the two principles in conflict.
- [ ] Can say why the check derives the account name instead of hardcoding it, and what would be wrong
      with a report that printed it.
- [ ] Read [3.2 The highlighter used on every line](parts/03-what-is-not-a-secret/3.2-the-highlighter.md);
      ran both arms and saw 0 against 12,286.
- [ ] Can name the two failure directions of a scanner and say which one actually kills tools.
- [ ] Read [3.3 What cannot be taken back](parts/03-what-is-not-a-secret/3.3-what-cannot-be-taken-back.md);
      sorted the five blocking findings by reversibility and found the two that move.
- [ ] Can say what you would do **first** if the scan had found a live credential — before touching
      the history.

## Section 4 — the control surface

- [ ] Read [4.1 The keys you hand over](parts/04-the-control-surface/4.1-the-keys-you-hand-over.md);
      ran both arms and can say why the missing approval gate is currently the right answer.
- [ ] Can name the event that makes that answer wrong, and the three things the check cannot see.
- [ ] Read [4.2 Thirteen taught, three shipped](parts/04-the-control-surface/4.2-thirteen-taught-three-shipped.md);
      ran it and found the three comment-only matches yourself with `grep`.
- [ ] Can state the difference between taught, mentioned and implemented, and name the two ledger rows
      that say closed over absent code.
- [ ] Read [4.3 Six chosen, one hundred and thirteen installed](parts/04-the-control-surface/4.3-six-chosen-one-hundred-and-thirteen-installed.md);
      picked three unfamiliar packages from the sample and found out what pulled them in.
- [ ] Can say what `docs/PACKAGES.md` actually records, and why a lockfile is not protection against a
      pinned version being bad.

## Section 5 — the verdict

- [ ] Read [5.1 The verdict, and what blocks Day 93](parts/05-the-verdict/5.1-the-verdict.md);
      sorted the five blocking findings into identity, drift and scope before checking.
- [ ] Wrote the one-sentence verdict yourself and it does not contain the word "secure".
- [ ] Can name the control that held completely, and the four things this review did **not** look at.
- [ ] Read [5.2 What a real hardening pass adds](parts/05-the-verdict/5.2-what-a-real-hardening-pass-adds.md);
      re-sorted the nine items by what decays and found the two that expire tomorrow.
- [ ] Can say what this day's lab is currently an instance of, and why that is the most urgent item.

## The paper — after the parts

- [ ] Read [papers/01 How systems actually fail](papers/01-how-systems-actually-fail.md).
- [ ] Ran `demo.py` and `demo.py --off` in `lab/papers/threat-model/` and saw 0 of 11 against
      10 of 10 defended.
- [ ] Added a twelfth incident from a day you have read, with its day number and its mechanism, and
      said whether any designed threat would have caught it.
- [ ] Can name the one condition under which the paper's claim does not apply, and the bias in this
      repository's own eleven-incident corpus.

## The build brief

- [ ] `sutra/audit.py` written — the checks as data, `derive_account()`, `mask()`, the fault pass.
- [ ] Every reporting path takes the masked form, enforced by the type rather than by care.
- [ ] Near-miss fixtures added: strings that nearly match a credential and must **not** fire.
- [ ] `surface.py`'s reach analysis extended one level, with the stopping point stated explicitly.
- [ ] `tests/test_audit.py` written — the detector test, the `BLIND` test, the never-emits-the-account
      test, and the `.env`-is-untracked assertion.
- [ ] **The eight checks are in `./m check`** — they currently live in a directory git does not track.
- [ ] **The author-identity question is decided** before Day 93. A `git config` line and a morning
      now; not available afterwards.
- [ ] **The fifty-one lines are scrubbed** and one sentence added to the day-format contract saying
      transcripts are verbatim except for the home directory.
- [ ] **`GEMINI_API_KEY` is in `.env.example`.**

## The evals, including ones that go red on demand

- [ ] `uv run python gate.py` exits `1` with 3 pass and 5 blocking.
- [ ] The fault pass shows `secrets.py --naive` and `surface.py --with-write` both going red, and
      nothing reported as `BLIND`.
- [ ] `secrets.py` exits `0`; `--naive` exits `1`; `--selftest` exits `0`.
- [ ] `metadata.py` exits `1`; `--files-only` exits `0`.
- [ ] `identity.py` exits `1`; `--preview` exits `0`.
- [ ] `template.py` exits `1`; `--values` exits `1`.
- [ ] `surface.py` exits `0`; `--with-write` exits `1`.
- [ ] `controls.py` exits `1`; `--taught` exits `0`.
- [ ] `deps.py` exits `1`; `--direct-only` exits `0`.
- [ ] `gate.py --headline` exits `0` — and you can say what that costs.
- [ ] `uv run python papers/threat-model/demo.py` exits `0`; `--off` exits `1`.
- [ ] **Break it and watch it go red:** added a ninth check that returns `0` unconditionally,
      confirmed the gate reports it as `BLIND`, and removed it again.

## The request budget

- [ ] Confirmed **zero** provider requests were made today, to every provider.
- [ ] Can say why a security review needs no model, and name the one thing this day could not do
      because no security tooling is installed.

## Ledger & commit

- [ ] `./m depth 92` green.
- [ ] `./m trace` regenerated; day 92 closes exactly `SEC-16`.
- [ ] `./m wiki` regenerated.
- [ ] `docs/PROGRESS.md` row appended, verbatim from the hub's §11, with the real commit hash and the
      `⚠️` gate mark.
- [ ] `docs/PAPERS.md` — the `doi:10.1145/168588.168615` row added.
- [ ] Committed with the message in the hub's §11.
