# Day 67 — Definition of done

`./m done 67` refuses to commit until every box is ticked. Tick a box only when you have actually run
the thing, not when you have read it. Several boxes ask you to record **two** numbers, because this is
the day whose whole argument is that one number is not a measurement.

## Before you start

- [ ] Day 66's parts and checklist are done, and `lab/threat-model.md` exists. Today implements the
      row that reads *hostile text reaching the prompt — provenance marking and guardrails, Day 67*.
- [ ] `lab/` scaffolded per §3 — twenty-one files, plus two under `lab/papers/camel/`.
- [ ] `git check-ignore -v days/day-67-guardrail-callbacks/lab/_poison.py` prints a matching rule.
      The corpus is synthetic hostile text and none of it reaches git (P9).
- [ ] `git diff pyproject.toml uv.lock` is empty and stays empty. No package is added today.
- [ ] `uv run python days/day-67-guardrail-callbacks/lab/gate.py; echo "exit: $?"` is **red** on all
      six checks before you write anything.

## Section 1 — the ladder

- [ ] **1.1** read · ran `score.py` · can say why no single check stops injection, and what question
      replaces *which guardrail works*
- [ ] **1.2** read · ran `ladder.py` · recorded the model calls saved — **seven instead of fourteen**
      over the same fourteen tickets — and can say what cheap-first trades away
- [ ] **1.3** read · can state the difference between a **filter** and a **boundary** in one sentence,
      and name which kind every rung of today's ladder is

## Section 2 — where a check stands

- [ ] **2.1** read · ran `surface.py` and `toolcall.py` · can name all **eight** callback positions
      and say what each one can see
- [ ] **2.2** read · ran `returns.py` · saw the three verdicts and confirmed **`block` is the only one
      with `model calls=0`**
- [ ] **2.3** read · ran `ladder.py` · can say what the runtime does with a list of callbacks and what
      "stops at the first truthy result" means for a rung that returns `{}`
- [ ] **2.4** read · ran `names.py` and reached the real `TypeError` · can quote the adk.dev sentence
      about keyword parameter names, and say why a type checker does not catch this
- [ ] **2.5** read · ran `failopen.py` · saw a refusal **overwritten** by a later callback and the
      tool run anyway · can say which one character of the return value decides it

## Section 3 — what comes in

- [ ] **3.1** read · ran `provenance.py` · recorded **1,463 of 1,591 characters — 92%** — written
      outside the system, and can name the spans they came from
- [ ] **3.2** read · can say why provenance marking stops no attack by itself and what it makes
      possible
- [ ] **3.3** read · ran `spotlight.py` · saw the data close the fence, and counted **2 opens, 2
      closes** on the run that was still an attack · can name the two distinct failure modes
- [ ] **3.4** read · ran `bypass.py` · can say why NFKC normalisation does not catch a Cyrillic `е`
      and what check does
- [ ] **3.5** read · can state the rule about retrieved text and the system instruction, and say why
      it is checkable by a test when nothing else in section 3 is

## Section 4 — what goes out

- [ ] **4.1** read · ran `toolcall.py` · can say why an output check that reads prose is checking the
      harmless half
- [ ] **4.2** read · ran `outbound.py` · can name the channels a URL allowlist does **not** close
- [ ] **4.3** read · ran `rewrite.py` and `rewrite.py --log` · found the log line that is a
      truthful-looking record of text that was never received · can state the rule: a guardrail may
      change text and may not change it quietly
- [ ] **4.4** read · ran `swallow.py` and saw the desk say **"I could not find any prior tickets"**
      while the archive was unreachable · ran `swallow.py --raise` and reached the real
      `ConnectionError: archive unreachable: connection refused on 127.0.0.1:5432` · can name the
      master plan §5.1 trap number and the principle

## Section 5 — measure it

- [ ] **5.1** read · ran `score.py`, `score.py --rows` and `score.py --hostile` · recorded **6/6
      caught and 1/8 falsely flagged** · did the base-rate arithmetic for 10,000 tickets with 10
      hostile and wrote down both resulting numbers
- [ ] **5.2** read · ran `falsepos.py` · can quote what `ticket:4601` actually asked and which phrase
      refused them · noted **0 model calls**, and can say why that makes the mistake sustainable
- [ ] **5.3** read · ran `falsepos.py --tighten` · recorded **6/6 → 6/6** and **1 → 3** · can name the
      two new casualties and the single list entry that refused them both
- [ ] **5.4** read · ran `bypass.py` and `bypass.py --split` · recorded **2 of 5** and **0 of 3** ·
      can say why checking the assembled context does not catch the split payload

## Section 6 — in production

- [ ] **6.1** read · ran `selfinject.py` and `selfinject.py --nested` · saw the identical instruction
      graded **UNSAFE** and **SAFE** · can say where a model judge belongs on the ladder and why the
      regress does not terminate
- [ ] **6.2** read · ran `failmode.py` and reached the real `KeyError: 'delete_ticket'` · ran
      `failmode.py --closed` and saw the refusal carry the exception · can say why the measured
      fail-closed behaviour is a finding rather than a reassurance
- [ ] **6.3** read · ran `gate.py` · can state what the ladder is worth and what it is not worth, with
      a number in each, and name the two days that own the controls that close a channel

## The paper — read it last

- [ ] `papers/01-defeating-prompt-injections-by-design.md` read **after** the parts, not before
- [ ] Ran the demo both ways from `lab/papers/camel/`: `demo.py` **exits 0** with
      `REFUSED: recipient came from ['ticket:9002']`, `demo.py --off` **exits 1** with the data gone
- [ ] Can say what is identical between the two runs — the model was injected and obeyed in both —
      and what that licenses you to conclude that a detection rate cannot
- [ ] Broke the propagation on purpose per the paper's *Check yourself*, and can name which of the
      four stated limits that demonstrated

## Build brief

- [ ] `sutra/guardrails.py` written, exporting `inspect_text`, `block_disallowed_send` with parameters
      named `(tool, args, tool_context)`, and a truthy `REFUSAL`
- [ ] The fail mode is decided **per tool** and the reason is written in the module docstring, not in
      a commit message
- [ ] `tests/test_guardrails.py` written, including the two-column test with thresholds you chose and
      can defend

## The eval

- [ ] `uv run python gate.py; echo "exit: $?"` run before and after the build brief, and you can say
      which findings cleared and which did not
- [ ] At least one check driven red **on purpose** and back to green, and you can say which behaviour
      the red proved was real (P11)

## Repo hygiene

- [ ] `./m depth 67` green — twenty-four parts and one paper
- [ ] `./m trace` green, and SEC-08 and SEC-09 close on this day and no others
- [ ] `./m wiki` run, so `docs/WIKI.md` and `docs/wiki/day-67.md` are not stale
- [ ] `uv run ruff format --check days/day-67-guardrail-callbacks` clean — Python inside fences is
      formatted like Python anywhere else
- [ ] `docs/PROGRESS.md` row appended verbatim from §11, with the real commit hash and the `⚠️` the
      gate actually earned — no rounding up (P10)
- [ ] `docs/PAPERS.md` row for `arXiv:2503.18813` present and dated, with the record checked live
      rather than recalled (P7, §17.4.1)
