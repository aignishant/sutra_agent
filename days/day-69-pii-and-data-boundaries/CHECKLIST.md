# Day 69 — Definition of done

`./m done 69` refuses to commit until every box is ticked. Tick a box only when you have actually run
the thing, not when you have read it. Several boxes ask you to record **two** numbers rather than one,
because this day's whole argument is that an aggregate hides the finding.

## Before you start

- [ ] Day 68's parts and checklist are done. Today builds the other structural control: not a
      capability the agent lacks, but a value that never entered the context.
- [ ] `lab/` scaffolded per §3 — fourteen files, plus two under `lab/papers/extracting-training-data/`.
- [ ] `git check-ignore -v days/day-69-pii-and-data-boundaries/lab/state/archive.json` prints a
      matching rule. Everything under `state/` is synthetic and is still exactly the shape of the thing
      that must never be committed (P9).
- [ ] `git diff pyproject.toml uv.lock` is empty and stays empty. No package is added today.
- [ ] `uv run python days/day-69-pii-and-data-boundaries/lab/gate.py; echo "exit: $?"` is **red**
      before you write anything, and you have read all four findings rather than counted them.

## Section 1 — who a record names

- [ ] **1.1** read · ran `freetext.py` · can say why "remove the personal data" is not executable
      until somebody says what it covers
- [ ] **1.2** read · ran `quasi.py` · can give an example of three values that name nobody
      individually and one person together
- [ ] **1.3** read · ran `freetext.py --show` · read the bodies that still name somebody after every
      structured field was redacted perfectly
- [ ] **1.4** read · ran `recall.py` · can name the four internal keys the desk uses and say why they
      are identifiers in their own right *and* what makes erasure possible

## Section 2 — where the copies are

- [ ] **2.1** read · ran `copies.py` · recorded **7 of 7 stores** and **13 copies** after one ordinary
      run · can name which day added each store and why
- [ ] **2.2** read · can say what makes a boundary a boundary rather than a diagram
- [ ] **2.3** read · ran `copies.py --files` · looked at the seven files on disk · can define
      **derived data** in one sentence
- [ ] **2.4** read · can say why the reply is personal data, and name the three stores that keep it
      without applying any filter

## Section 3 — the line at the provider

- [ ] **3.1** read · ran `terms.py` · recorded the three answers — **YES**, **NO**, **DEPENDS** — and
      which provider gives which
- [ ] **3.2** read · ran `terms.py --quotes` and `terms.py --recheck` · can say what an `n/a` row
      means and why silence must not be read as either permission or prohibition
- [ ] **3.3** read · can state Sutra's decision in the accept/mitigate/refuse vocabulary from Day 66
      part 7.3, and say why it is a `refuse` rather than a `mitigate`
- [ ] **You re-verified at least one provider row yourself**, on your own date, using the commands
      `--recheck` prints. This day's date is not yours (P7)

## Section 4 — invented on purpose

- [ ] **4.1** read · ran `synth.py` and `synth.py --seed 7` · can name the four reasons for synthetic
      data and say which one is the least interesting
- [ ] **4.2** read · can say what the generator makes inspectable that a sample of real traffic does
      not, and name one shape it does **not** emit
- [ ] **4.3** read · ran `synth.py --score` · recorded **600/600 (100%)** generated against
      **16/20 (80%)** hand-written · can say why the generated corpus is easier rather than wrong

## Section 5 — measuring the redactor

- [ ] **5.1** read · read `TRUTH` in `_archive.py` · can name the three things each entry records and
      say why the third makes 5.2's split possible
- [ ] **5.2** read · ran `recall.py`, `recall.py --misses` and `recall.py --v2` · recorded V1 as
      **50% overall = 100% field / 23% free** and V2 as **80% = 100% / 69%** · noticed that every
      single miss is in free text
- [ ] **5.3** read · ran `hashcheck.py` and `hashcheck.py --salted` · recorded **6 of 8 recovered**
      both times · can say why the salt did not help and what a salt *is* for · can state the test
      that distinguishes pseudonymisation from anonymisation

## Section 6 — the delete that did not

- [ ] **6.1** read · ran `deleted.py` and `deleted.py --retrieve` · recorded **6 of 7 stores** still
      holding the address and **11 copies remaining** · saw the index return the whole message,
      signature and phone number included, to an unrelated query
- [ ] **6.2** read · ran `derived.py --how` · can name the three reach kinds and the residual of each ·
      can say why the log line is redacted rather than deleted
- [ ] **6.3** read · ran `derived.py` · recorded **copies remaining 0** · can explain why the `log`
      row shows `after 0` even though the line was not deleted

## Section 7 — in production

- [ ] **7.1** read · ran `copies.py --needle "Lin Zhou"` and compared it with the default needle · can
      say why disclosure and erasure must read the same registry
- [ ] **7.2** read · ran `gate.py` · named the two checks that pass silently · broke the fixture-safety
      check on purpose with a non-reserved domain and recorded the exact finding, then put it back

## The paper — read it last

- [ ] `papers/01-extracting-training-data.md` read **after** the parts, not before
- [ ] Ran the demo both ways from `lab/papers/extracting-training-data/`: with the paper's filter the
      canary is **rank 1 of 2735** and `extracted: YES`; with `--no-zlib` it falls to **rank 39** with
      **61 candidates tied** and `extracted: no`
- [ ] Can say what is identical between the two runs and therefore what the ablation demonstrates —
      the ranking signal, not the generation
- [ ] Can say honestly what a small locally-trained model does and does not tell you about the risk
      for a large one
- [ ] Can say why the demo's ranking sorts ties alphabetically, and what the ablation would
      prove without a deterministic tiebreak — with 61 candidates level at the top score, a
      canary surfacing at rank 1 by luck would prove nothing

## Build brief

- [ ] `sutra/data_boundary.py` written: `redact`, `STORES`, `purge` with a declared reach per store and
      a per-store report
- [ ] `docs/DATA_BOUNDARY.md` written: one row per store — what, why, how long, how it is reached ·
      you found the two of those four facts that were not previously anywhere in the repository
- [ ] `tests/test_data_boundary.py` written, including the drift test over `lab/state/` and a recall
      assertion against a **held-out** fixture set
- [ ] `uv run python gate.py; echo "exit: $?"` re-run · you can say which findings cleared and, if the
      90% recall floor is still red, what verdict you are giving it (met, lowered with a reason, or
      accepted with the condition written down)

## Repo hygiene

- [ ] `./m depth 69` green — twenty-two parts and one paper
- [ ] `./m trace` green, and SEC-12 and SEC-13 close on this day and no others
- [ ] `./m wiki` run, so `docs/WIKI.md` and `docs/wiki/day-69.md` are not stale
- [ ] `uv run ruff format --check days/day-69-pii-and-data-boundaries` clean — Python inside fences is
      formatted like Python anywhere else
- [ ] `git status` shows nothing under `lab/state/` staged or untracked-and-about-to-be-added
- [ ] `docs/PROGRESS.md` row appended verbatim from §11, with the real commit hash and the `⚠️` the
      gate actually earned — no rounding up (P10)
- [ ] `docs/PAPERS.md` row for `arXiv:2012.07805` present and dated, with the record checked live
      rather than recalled (P7, §17.4.1)
