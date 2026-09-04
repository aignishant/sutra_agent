# Day 40 — definition of done

`./m done 40` refuses to commit until every box below is ticked. A box is ticked when you have run the
thing, not when you believe it would work.

## Read

- [ ] All twenty parts, in order, sections 1 through 6.
- [ ] The paper, [`papers/01-protection-of-information.md`](papers/01-protection-of-information.md),
      **after** the parts.
- [ ] You can state the difference between a deny-list and an allowlist in one sentence, without using
      the word "security".

## The lab — you ran these and read the output

- [ ] `lab/postures.py` — you saw the two postures produce identical output on the reviewed server and
      differ on Tuesday's, and the exit code was 1.
- [ ] `lab/listing.py` against both server versions — you read the injected sentence in `check_status`'s
      description with your own eyes, with no model involved.
- [ ] `lab/resolve.py` for all five postures — `none`, `allow`, `empty`, `string`, `tuple` — and you can
      say why `empty` and `tuple` disagree.
- [ ] `lab/filter_semantics.py` — you saw rows one and three come back identical.
- [ ] `lab/predicate.py` — one rule, two contexts, two answers, and `False` for a name it has never seen.
- [ ] `lab/reserved.py` — you saw the framework's warning line and the tool disappear.
- [ ] `lab/pin.py` against both server versions — clean, then `rewritten check_status`, exit 1.
- [ ] `lab/cache.py` — three listings became one, and you can say what that bought and what it cost.
- [ ] `lab/one_door.py` — red before `sutra/mcp/filtering.py` exists, green after.
- [ ] `lab/late.py` — 36 characters against 103, and you can say what the 67 are.
- [ ] `lab/anchors.py` — the pattern naming two tools admitted four.
- [ ] `lab/shadow.py` — four names, two distinct, then four distinct with prefixes.
- [ ] The paper demo, **both arms**, with both exit codes read.

## The build

- [ ] `sutra/mcp/filtering.py` exists, in the package Day 33 created, and is the **only** file under
      `sutra/` that constructs an `McpToolset`.
- [ ] It exposes `allowlist(server_key) -> list[str]` and `deny(names, policy) -> list[str]`, and
      `deny` runs on the output of `allowlist` and never on the server's full offering.
- [ ] The filter is applied at **toolset construction**, not at dispatch.
- [ ] An unknown server key raises rather than returning a default.
- [ ] An empty allowlist raises, with the server key in the message.
- [ ] Whatever reaches `tool_filter` is a `list`, converted explicitly, never a tuple or a set.
- [ ] `REGISTRY` has at least one real entry with `allow`, `pinned` and `reviewed_on` filled in, and
      you wrote down whether `sutra_mcp` itself belongs there.
- [ ] `lab/one_door.py` exits 0.

## The `TODO(me)` decisions — written down, not solved for you

- [ ] 2.1 — what `filtering.py` asserts about the value it hands to `tool_filter`.
- [ ] 2.2 — whether Sutra needs the predicate form yet, and the condition that will trigger it.
- [ ] 2.3 — Sutra's own copy of the reserved names, and what happens when a server advertises one.
- [ ] 3.1 — who receives a new tool, a missing tool and a changed tool, and which of the three is an
      incident.
- [ ] 3.2 — the schema half of the pin, and the severity split between read tools and write tools.
- [ ] 3.3 — a `ttl_seconds` per server, with a reason beside each number, and they are not all the same.
- [ ] 4.1 — where `one_door.py`'s successor lives, and what it does about test code.
- [ ] 4.3 — what else belongs in `NEVER`, and the overlap check between `allow` and `deny`.
- [ ] 5.1 — the startup assertion that resolved tools equal policy names, and where it lives.
- [ ] 6.2 — a one-page threat model for one integration, with at least one row saying
      *"nothing — accepted risk"*.
- [ ] 6.4 — the eight intake questions as a pull-request template, and who reviews question 2.

## You can explain, out loud, without notes

- [ ] Why a deny-list and an allowlist produce the same output on the day they are written.
- [ ] Where in the request lifecycle ADK's filter runs, and what that means the filter does *not*
      protect.
- [ ] Why `tool_filter=[]` admits everything and `tool_filter=("a",)` admits nothing.
- [ ] Why an allowlist cannot catch a rug pull, and what does.
- [ ] What the reserved tool names protect and what they do not.
- [ ] Three attacks the filter does not stop, and which of them have no mitigation today.
- [ ] What fail-safe defaults claims, and why the paper argues for it on grounds of detectability.

## Gates

- [ ] `git diff pyproject.toml uv.lock` is empty — nothing was installed or upgraded.
- [ ] `./m depth 40` is green.
- [ ] `./m check` is green.
- [ ] `docs/PROGRESS.md` has the day 40 row from the hub's §11, with the real date and commit hash.
- [ ] `.env` is not staged. Nothing secret is in the day folder.
