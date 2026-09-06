# Day 90 — checklist

**Definition of done.** `./m done 90` refuses to commit while any box is unticked. A box is ticked
when you have run the thing, not when you have read about it.

**The demo command for the whole day:**

```bash
cd days/day-90-identity-and-registry/lab && uv run python revoke.py --signature-only; echo "exit: $?"
```

---

## Setup

- [ ] `days/day-90-identity-and-registry/lab/` exists with the eleven files listed in the hub's §3.
- [ ] `git check-ignore -v days/day-90-identity-and-registry/lab/_ids.py` prints a matching rule.
- [ ] `git diff pyproject.toml uv.lock` is empty. No package is added today.
- [ ] Read `_ids.py` and can say why every key is generated from a fixed seed.
- [ ] Can say which fields of `Card` a signature covers and which it does not.

## Section 1 — what an identity is

- [ ] Read [1.1 A name is not an identity](parts/01-what-an-identity-is/1.1-a-name-is-not-an-identity.md);
      printed both fingerprints and can say what two cards bearing the same name have in common.
- [ ] Found the field you could add to `Card` that a signature would not cover.
- [ ] Read [1.2 The three questions](parts/01-what-an-identity-is/1.2-the-three-questions.md);
      ran both `registry.py` arms and can say which question failed in the refusal.
- [ ] Can name all three questions, the artefact that answers each, and what each does **not** settle.
- [ ] Read [1.3 What ADK puts in the card](parts/01-what-an-identity-is/1.3-the-sticker-anyone-can-print.md);
      ran both arms and can say why the missing `signatures` field is invisible in a dump.
- [ ] Listed the fourteen `AgentCard` fields yourself and named the six ADK left out.

## Section 2 — the registry

- [ ] Read [2.1 The registry is a file](parts/02-the-registry/2.1-the-list-behind-the-counter.md);
      can name the four columns and the failure each prevents.
- [ ] Can say why a withdrawn peer is marked rather than deleted.
- [ ] Read [2.2 Trust on first use](parts/02-the-registry/2.2-the-milkmans-substitute.md);
      ran all three arms and can say which one pinned zero keys and why.
- [ ] Reordered `contacts` so the impostor arrives first, predicted all three arms, and put it back.
- [ ] Read [2.3 Two shops, one name](parts/02-the-registry/2.3-two-shops-one-name.md);
      ran both arms and can name the capability the lookalike had that the real peer did not.
- [ ] Changed `[-1]` to `[0]`, saw the exit code flip, and can say why that is not a fix.

## Section 3 — keys change

- [ ] Read [3.1 Rotation](parts/03-keys-change/3.1-the-cheques-already-written.md);
      ran both arms and can state the two rules and which one `--no-history` breaks.
- [ ] Can say what `previous_keys` is missing and why it matters after a compromise.
- [ ] Read [3.2 The signature that stays valid for ever](parts/03-keys-change/3.2-the-card-of-someone-who-left.md);
      ran both arms and can say which two checks pass for a withdrawn peer.
- [ ] Deleted the `billing-bot` entry instead of marking it, ran both arms, and can say why the
      resulting refusal is correct with the wrong reason. Then put it back.

## Section 4 — verified is not authorised

- [ ] Read [4.1 Verified is not authorised](parts/04-verified-is-not-authorised/4.1-the-man-the-office-sent.md);
      ran both arms and noticed that `in grant` reads `False` in the run that allowed the call.
- [ ] Can give the reason identity is checked once and authorisation every time, without saying
      "security".
- [ ] Read [4.2 One identity for many callers](parts/04-verified-is-not-authorised/4.2-the-shared-login.md);
      can name the three ways one key comes to cover several callers.
- [ ] Picked the row in the four-line grant history where you would have pushed back, and said what you
      would have asked for instead.

## Section 5 — in production

- [ ] Read [5.1 What a registry costs](parts/05-in-production/5.1-what-a-registry-costs.md);
      ran the timing command and got a figure in the same order as 103.5 microseconds.
- [ ] Can name the two maintenance tasks that have no trigger, and wrote the `./m check` line for each.
- [ ] Read [5.2 What a real identity layer adds](parts/05-in-production/5.2-what-a-real-identity-layer-adds.md);
      mapped the six-step composite onto the nine items and found the step none of them catches.
- [ ] Read [5.3 The registry as a single point of trust](parts/05-in-production/5.3-the-one-road-into-town.md);
      added a row with your own fingerprint and `move_money`, saw nothing refuse it, and removed it.

## The paper — after the parts

- [ ] Read [papers/01 Speaks for](papers/01-speaks-for.md).
- [ ] Ran `demo.py` and `demo.py --off` in `lab/papers/speaksfor/` and saw 6 of 6 against 3 of 6.
- [ ] Identified the two rows the ablation gets right for the wrong reason.
- [ ] Added a second `audit-reader → audit-worker-1` statement, predicted the fifth request, and checked.
- [ ] Can state the speaks-for relation in one sentence and say why scope can only narrow along a chain.

## The build brief

- [ ] `sutra/identity.py` written — `resolve`, `verify_card`, `pinned`, `rotate`, `revoked`, `allowed`.
- [ ] `resolve` returns a **reason**, not a boolean, and compares the key before verifying the signature.
- [ ] Full public keys are compared; the fingerprint appears only in log messages.
- [ ] `verify_card` handles **more than one** signature, and the decision when signers disagree is in a
      comment.
- [ ] The pin store survives a restart.
- [ ] Retired keys carry a `valid_until`, and `previous_keys` is never consulted for a live contact.
- [ ] A refused revoked peer is logged at warning level with its id.
- [ ] `allowed` is called per request, and its default is refusal.
- [ ] `sutra/registry.py` written — every row carries `confirmed_on`, and `./m check` fails on a stale
      one.
- [ ] Decided and wrote down what happens when the registry cannot be read at all.
- [ ] `tests/test_identity.py` written — the wrong-key test, the revoked test, the rotation pair, the
      outside-the-grant test, and the no-lookup-by-name test.
- [ ] **Wrote down who may change the registry**, and made a registry change its own pull request.

## The evals, including ones that go red on demand

- [ ] `uv run python gate.py` runs and reports 0 of 6 — `sutra/identity.py` is the build brief.
- [ ] `card.py` exits `1`; `--signed` exits `0`.
- [ ] `registry.py` exits `0`; `--unknown` exits `1`.
- [ ] `tofu.py` exits `0`; `--no-pin` exits `1`; `--registry` exits `0`.
- [ ] `rotate.py` exits `0`; `--no-history` exits `1`.
- [ ] `revoke.py` exits `0`; `--signature-only` exits `1`.
- [ ] `confusion.py` exits `0`; `--by-name` exits `1`.
- [ ] `authz.py` exits `0`; `--verified-is-authorised` exits `1`.
- [ ] `papers/speaksfor/demo.py` exits `0`; `--off` exits `1`.
- [ ] **Break it and watch it go red:** changed `REGISTRY`'s `public_key` for the refund desk to the
      impostor's fingerprint, ran `registry.py`, and confirmed the refusal names both keys. Then put it
      back.
- [ ] Confirmed that **not one** of the six red arms contains a failed signature.

## The request budget

- [ ] Confirmed **zero** provider requests were made today, to every provider.
- [ ] Can say why `card.py` constructs a real `LlmAgent` and still costs nothing.

## Ledger & commit

- [ ] `./m depth 90` green.
- [ ] `./m trace` regenerated; day 90 closes exactly `AG-29`, `ADK-71`.
- [ ] `./m wiki` regenerated.
- [ ] `docs/PROGRESS.md` row appended, verbatim from the hub's §11, with the real commit hash.
- [ ] `docs/PAPERS.md` — the `doi:10.1145/121132.121160` row added.
- [ ] Committed with the message in the hub's §11.
