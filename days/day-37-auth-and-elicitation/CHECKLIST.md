# Day 37 — CHECKLIST

**IDs closed:** MCP-13, MCP-27, MCP-30
**Principles served:** 1, 2, 4, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18
**Parts:** 19 across 6 sections, plus 1 paper

> `./m done 37` refuses to commit while any box below is unticked. It cannot tell whether you were
> honest — that part is yours.

## Demo command

```bash
curl -s https://modelcontextprotocol.io/specification/versioning | grep -o "specification/2026-07-28" | head -1
python days/day-37-auth-and-elicitation/lab/badge.py
python days/day-37-auth-and-elicitation/lab/challenge.py
python days/day-37-auth-and-elicitation/lab/audience.py
python days/day-37-auth-and-elicitation/lab/iss_check.py; echo "exit: $?"
python days/day-37-auth-and-elicitation/lab/compare.py
python days/day-37-auth-and-elicitation/lab/cimd.py
python days/day-37-auth-and-elicitation/lab/elicit_form.py
python days/day-37-auth-and-elicitation/lab/actions.py; echo "exit: $?"
python days/day-37-auth-and-elicitation/lab/request_state.py; echo "exit: $?"
python days/day-37-auth-and-elicitation/lab/url_mode.py; echo "exit: $?"
python days/day-37-auth-and-elicitation/lab/credential_guard.py; echo "exit: $?"
SAME_USER=1 python days/day-37-auth-and-elicitation/lab/same_user.py
SAME_USER=0 python days/day-37-auth-and-elicitation/lab/same_user.py
python days/day-37-auth-and-elicitation/lab/extensions.py
python days/day-37-auth-and-elicitation/lab/policy.py; echo "exit: $?"
python days/day-37-auth-and-elicitation/lab/leak.py; echo "exit: $?"
.venv/Scripts/python.exe days/day-37-auth-and-elicitation/lab/sdk_surface.py; echo "exit: $?"
python days/day-37-auth-and-elicitation/lab/review.py; echo "exit: $?"
cd days/day-37-auth-and-elicitation/lab/papers/issuer-identification
ISS_CHECK=1 python client.py
ISS_CHECK=0 python client.py
cd -
./m depth 37 && ./m check && ./m trace && git log --oneline -1
```

Expected: `specification/2026-07-28`; then the four roles and the four things they must not hold;
then a 401 and a 403 challenge and `hops the client needs to find the desk: 1`; then three rejections
including the one for a token minted for the vendor API; then five `iss` verdicts and
`exit: 0`; then **4** issuer strings the helpful comparison accepts and the strict one does not; then
`findings: 0` for the honest CIMD document and `findings: 1` for the forged echo; then the whole
`input_required` JSON and `flat schema findings : []`; then `user answers the naive server cannot
tell apart: 1`; then four refusals and `forged slips this server would have honoured: 0`; then five
inspected links and `URLs fetched by this host before consent: 0`; then two REFUSE verdicts and
`forbidden requests this guard let through: 0`; then `vault: {}` against
`vault: {'u-1': 'vendor-token-granted-by-u-2'}`; then one live extension out of four and
`extensions active by default: 0`; then five policy decisions and
`employees who had to read an authorization dialog: 0`; then the redacted log line and
`places the token escaped to: 0`; then `mechanisms taught today that this SDK cannot speak: 4` with
`exit: 4`; then `unanswered questions: 7` with `exit: 7`; then
**`token requests sent : 0`** against **`token requests sent : 1`** with
`attacker holds an honest authorization code: True ['honest-code-4521']`. Then
`OK day 37 19 parts + 1 papers`, `OK all green`, a traceability line with `0 problem(s)`, and one
commit.

## Setup

- [ ] `./m brief 37` read, and the three IDs confirmed as MCP-13, MCP-27, MCP-30
- [ ] **The specification freshness gate was run first** and
      `modelcontextprotocol.io/specification/versioning` still names **2026-07-28** as current — if it
      had moved, you stopped and amended (Principle 14)
- [ ] **No `uv add` and no `uv sync --upgrade` was run** — `git diff pyproject.toml uv.lock` is empty,
      and the `mcp` pin is still `1.29.1` despite part 6.2
- [ ] `sutra_mcp/auth.py` and `sutra/mcp/auth.py` created by you, line by line, from §4
- [ ] No token, key or signing secret appears as a literal anywhere you wrote today (Principle 9)

## Section 1 — `01-the-badge`

- [ ] **1.1** read · ran `badge.py` · named the four OAuth roles and which one `sutra_mcp` plays ·
      **added a fifth `FORBIDDEN` row for a gateway** and wrote down what it must not hold
- [ ] **1.2** read · ran `challenge.py` · said out loud what a client does differently on 401 and on
      403 · **decided what Sutra's client does with a 401 that carries no `WWW-Authenticate`**
- [ ] **1.3** read · ran `audience.py` · **commented out the two `aud` lines, watched exactly one
      verdict flip and nothing else complain, and put them back** · decided whether a token whose
      `aud` omits the `/mcp` path may be used

## Section 2 — `02-issuer-checks`

- [ ] **2.1** read · ran `iss_check.py` and got `exit: 0` · **tested the `advertised` flag first,
      watched a row flip, and put it back** · can state the four-row table from memory
- [ ] **2.2** read · ran `compare.py` and saw **4** extra strings accepted · removed one tidy-up at a
      time and watched the count fall · wrote the sentence you would use to argue against the hardest
      one
- [ ] **2.3** read · ran `cimd.py` · **broke the echo check to compare hostnames only, confirmed the
      forgery passed, and put it back** · **decided the exact HTTPS URL where Sutra's metadata
      document will be hosted**, path component included

## Section 3 — `03-the-question`

- [ ] **3.1** read · ran `elicit_form.py` · wrote the retry request out by hand, with a **different**
      JSON-RPC id and the `requestState` echoed · added a second `inputRequests` entry and its answer
- [ ] **3.2** read · ran `flat` against an array of objects and read the finding · **rewrote the
      duplicates question legally as a multi-select** and wrote down what the user loses
- [ ] **3.3** read · ran `actions.py` · added an `accept` with no `content` and predicted both servers
      before running · **decided how long a `decline` lasts for Sutra**
- [ ] **3.4** read · ran `request_state.py` and got `exit: 0` · **moved the decode above the
      signature check, confirmed everything still passed, and put it back** · replaced
      `compare_digest` with `==`, saw identical output, and wrote why no test can tell · chose the TTL

## Section 4 — `04-out-of-band`

- [ ] **4.1** read · ran `url_mode.py` and got `exit: 0` · **removed the leading dot from
      `"." + TRUSTED_HOST` and found the hostname that now passes** · named three of the seven client
      rules out loud
- [ ] **4.2** read · ran `credential_guard.py` and got `exit: 0` · **added the `q` field with the OTP
      message, watched it pass, and wrote what does catch it** · can state the four kinds of
      information that must never go through form mode
- [ ] **4.3** read · **ran both arms** and put the two vault lines side by side · added the
      query-string version of the subject and confirmed the check passes for anybody · said where the
      identity must come from

## Section 5 — `05-policy`

- [ ] **5.1** read · ran `extensions.py` · added `io.modelcontextprotocol/ui` to the client set and
      noted that it goes live despite the settings disagreeing · said whose job the reconciliation is
- [ ] **5.2** read · ran `policy.py` and got `exit: 0` · added an `Ask` from an unknown group and
      predicted the verdict first · **can explain what an ID-JAG is and where policy is evaluated**
- [ ] **5.3** read · added a denied extension nothing requests, noted that nothing changed, and wrote
      what that says about testing a denylist · decided what Sutra's audit log records
- [ ] 🅿️ **boundaries honest:** you know that EMA and third-party OAuth were read, not built, and why

## Section 6 — `06-in-production`

- [ ] **6.1** read · ran `leak.py` and got `exit: 0` · **made `redact` return its input, watched the
      exit code reach 1, and put it back** · confirmed `.env` is not tracked
- [ ] **6.2** read · ran `sdk_surface.py` on the venv python and saw **4 absent** · **grepped for the
      bare `iss`, watched the count drop to 3 for the wrong reason, and put it back** · **did not
      change the pin**
- [ ] **6.3** read · ran `review.py` and got `exit: 7` · **filled all seven and watched it reach 0** ·
      blanked `REVIEWED_BY` alone and saw `exit: 1` · added the eighth question

## The paper

- [ ] `papers/01-issuer-identification.md` read **after** the parts, not before
- [ ] Both arms of the demo run, and **your own** output compared with the transcript in the part
- [ ] The two `token requests sent` numbers recorded: **0** against **1**
- [ ] `advertises_iss = False` tried on the evil server, and you can say which table row that
      exercises and whether the protected arm still stops
- [ ] Said out loud what survived — the check is a MUST in MCP — and what did not: the assumption
      that multi-issuer clients are unusual
- [ ] Noticed that the pinned SDK still does not perform the check, four years on, and can say why
      defences whose absence is invisible propagate slowly

## The eval

- [ ] `review.py` printed `unanswered questions: 7` and `exit: 7` before you filled anything in
- [ ] `sdk_surface.py` printed `4` against the pinned SDK, and you understand that this is a Phase 5
      finding and not a Phase 5 fix
- [ ] The paper demo was run **both ways** and the two token-request counts recorded
- [ ] `same_user.py` was run **both ways** and the two vault lines recorded
- [ ] At least four of the named breaks were performed on purpose and reverted

## The budget

- [ ] Total generations spent: **0 of 20**
- [ ] No `GOOGLE_API_KEY` was needed by anything in this day
- [ ] The only network traffic was one HTTPS GET to the specification site, plus two servers on
      `127.0.0.1`
- [ ] No identity provider, no cloud IAM, no billing account — cost **$0**

## The ledger

- [ ] `docs/PROGRESS.md` row pasted from §11, with the real date and hash
- [ ] `docs/PACKAGES.md` — **no new row**; the SDK-gap finding lives in §8 and part 6.2
- [ ] `docs/PAPERS.md` — **no new row**; all four DOIs already have theirs
- [ ] `docs/SKILL_PROVENANCE.md` — **no new row**
- [ ] `./m depth 37` green · `./m check` green · `./m trace` prints `0 problem(s)`
- [ ] `git status` shows no `.env`; commit message is the one in §11
