# Day 91 — checklist

**Definition of done.** `./m done 91` refuses to commit while any box is unticked. A box is ticked
when you have run the thing, not when you have read about it.

**The demo command for the whole day:**

```bash
cd days/day-91-slack-shaped-intake/lab && uv run python vector.py; echo "exit: $?"
```

---

## Setup

- [ ] `days/day-91-slack-shaped-intake/lab/` exists with the fifteen files listed in the hub's §3.
- [ ] `git check-ignore -v days/day-91-slack-shaped-intake/lab/_events.py` prints a matching rule,
      and you can say which rule it is and why it is not the one part 4.2 asks about.
- [ ] `git diff pyproject.toml uv.lock` is empty. No package is added today, and there is no vendor
      SDK anywhere in this day.
- [ ] Read `_events.py` and can say which values came from the vendor's documentation and which were
      written for this lab.

## Section 1 — what an integration is

- [ ] Read [1.1 Somebody else's shape](parts/01-what-an-integration-is/1.1-somebody-elses-shape.md);
      ran the paper demo and can state the four-against-one result.
- [ ] Added `raw: dict` to `Message`, used it in `route`, re-ran the demo, and can say what the
      vendor-name count did and what it failed to tell you. Then put it back.
- [ ] Read [1.2 The ways in](parts/01-what-an-integration-is/1.2-the-ways-in.md);
      ranked the ten rows by what each can see and compared that with how easy each is to enable.
- [ ] Can name the row with the widest data surface and say roughly what it would cost to switch on.
- [ ] Read [1.3 A survey that can go red](parts/01-what-an-integration-is/1.3-a-survey-that-can-go-red.md);
      ran both arms and can say which rows are genuinely checked and which rest on discipline.
- [ ] Pointed the MCP row at `sutra_mcp/server.py`, saw it go red, and decided whether that was a
      true finding. Then put it back.

## Section 2 — verifying it

- [ ] Read [2.1 What a vendor sends](parts/02-verifying-it/2.1-what-a-vendor-sends.md);
      ran both arms and can say why the unsigned arm exiting `0` is correct.
- [ ] Moved the `url_verification` branch above the signature check, ran both arms, saw what changed,
      and can name what that endpoint would now do for a stranger. Then put it back.
- [ ] Read [2.2 The string that gets signed](parts/02-verifying-it/2.2-the-string-that-gets-signed.md);
      confirmed the fourteen-byte arithmetic by hand.
- [ ] Can say why `base_string` works in `bytes` end to end, and what breaks if it does not.
- [ ] Read [2.3 Checked against the vendor](parts/02-verifying-it/2.3-checked-against-the-vendor.md);
      ran `vector.py` and saw sixty-four of sixty-four.
- [ ] Ran `vector.py --tamper` and can say why fifty-six differing characters is unsurprising.
- [ ] Read [2.4 The bytes that arrived](parts/02-verifying-it/2.4-the-bytes-that-arrived.md);
      ran both arms and can list everything `401 bad signature` implies that is untrue there.
- [ ] Changed `ON_THE_WIRE` to default `json.dumps` separators, saw `--reparse` pass, and can say
      what that proves about the test you would have written. Then put it back.

## Section 3 — three ways it goes wrong

- [ ] Read [3.1 The signature that never expires](parts/03-three-ways-it-goes-wrong/3.1-the-signature-that-never-expires.md);
      ran both arms and saw two copies of one refund reach the desk.
- [ ] Can say why the timestamp check runs before the signature check.
- [ ] Read [3.2 The comparison you cannot benchmark](parts/03-three-ways-it-goes-wrong/3.2-the-comparison-you-cannot-benchmark.md);
      ran each arm three times and wrote down the six spreads.
- [ ] Can state the argument for `hmac.compare_digest` that does not depend on any measurement.
- [ ] Read [3.3 Signed is not safe](parts/03-three-ways-it-goes-wrong/3.3-signed-is-not-safe.md);
      ran both arms and can say what the `valid` column proves without using the word "safe".
- [ ] Wrote a message that gets past `looks_hostile` and still asks for something it should not.

## Section 4 — blast radius

- [ ] Read [4.1 What a forged request reaches](parts/04-blast-radius/4.1-what-a-forged-request-reaches.md);
      wrote the five-row blast-radius table for the version where the payload reaches the desk.
- [ ] Decided the chat runner's toolset, with a one-clause justification for each exclusion.
- [ ] Read [4.2 The secret itself](parts/04-blast-radius/4.2-the-secret-itself.md);
      ran `git check-ignore -v ../../../.env` and the `SIGNING_SECRET` grep.
- [ ] Can say what a reviewer would need in order to tell this fixture from a real committed secret,
      and whether any tool could do it.

## Section 5 — in production

- [ ] Read [5.1 Which one to build first](parts/05-in-production/5.1-which-one-to-build-first.md);
      ordered the two account-blocked rows by demand and can say how you would find out rather than
      guess.
- [ ] Tried to write the one sentence justifying the ticketing row without inventing a person.
- [ ] Read [5.2 What a real integration layer adds](parts/05-in-production/5.2-what-a-real-integration-layer-adds.md);
      mapped the gate's six checks onto the nine items and found the two the gate does not check.
- [ ] Walked the seven-step sequence and found the step no item covers.

## The paper — after the parts

- [ ] Read [papers/01 The module that owns the vendor](papers/01-the-module-that-owns-the-vendor.md).
- [ ] Ran `demo.py` and `demo.py --off` in `lab/papers/modules/` and saw four against one.
- [ ] Repaired `adapt` in `hidden.py` for the new payload, then `steps.py`, and counted the edits.
- [ ] Found the decision in this day's lab that is hidden nowhere, and said what module it would get.
- [ ] Can answer out loud: what is the criterion for a module, and which step of the method does
      everybody skip?

## The build brief

- [ ] `sutra/intake.py` written — `secret()`, `raw_body()`, `fresh()`, `verify()`, the event-type
      allowlist, the body-size limit, and `accept()`.
- [ ] `secret()` indexes the environment and has **no default**.
- [ ] The handler takes `Request`, not a Pydantic model, with a comment saying why.
- [ ] `fresh()` is two-sided, runs before the signature check, and returns `400` rather than `401`.
- [ ] The handler acknowledges before doing any work, and the work is keyed on the vendor's
      `event_id`.
- [ ] `sutra/adapters/slack.py` written — the only module that mentions a vendor field name.
- [ ] `tests/test_intake.py` written — the vendor's vector, the re-serialisation test, the window
      test, the duplicate-`event_id` test, and the grep test.
- [ ] **Decide the chat runner's toolset** — the one item that needs somebody else's agreement.
- [ ] 🅿️ **The live workspace**, parked: needs an account and a public HTTPS URL, not budget.

## The evals, including ones that go red on demand

- [ ] `uv run python gate.py` runs and reports 0 of 6 — `sutra/intake.py` is the build brief.
- [ ] `vector.py` exits `0`; `--tamper` exits `1`.
- [ ] `intake.py` exits `0`; `--unsigned` exits `0` — and you can say why both are correct.
- [ ] `raw.py` exits `0`; `--reparse` exits `1`.
- [ ] `replay.py` exits `0`; `--no-window` exits `1`.
- [ ] `timing.py` exits `0`; `--naive` exits `1`.
- [ ] `trusted.py` exits `0`; `--signed-is-safe` exits `1`.
- [ ] `survey.py` exits `0`; `--optimistic` exits `1`.
- [ ] `papers/modules/demo.py` exits `0`; `--off` exits `1`.
- [ ] **Break it and watch it go red:** changed the delimiter in `base_string` from `:` to `|`,
      confirmed `vector.py` goes red, and put it back.

## The request budget

- [ ] Confirmed **zero** provider requests were made today, and zero network requests of any kind.
- [ ] Can say what `httpx.ASGITransport` exercises and what it cannot, and which part of this
      integration is therefore still unconfirmed.
- [ ] Can name the four surfaces marked 🅿️ requires budget and the two marked 🅿️ requires an account.

## Ledger & commit

- [ ] `./m depth 91` green.
- [ ] `./m trace` regenerated; day 91 closes exactly `AG-30`, `ADK-72`.
- [ ] `./m wiki` regenerated.
- [ ] `docs/PROGRESS.md` row appended, verbatim from the hub's §11, with the real commit hash.
- [ ] `docs/PAPERS.md` — the `doi:10.1145/361598.361623` row added.
- [ ] Committed with the message in the hub's §11.
