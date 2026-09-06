# Day 88 — checklist

**Definition of done.** `./m done 88` refuses to commit while any box is unticked. A box is ticked
when you have run the thing, not when you have read about it.

**The demo command for the whole day:**

```bash
cd days/day-88-the-mcp-sidecar/lab && uv run python race.py; echo "exit: $?"
```

---

## Setup

- [ ] `days/day-88-the-mcp-sidecar/lab/` exists with the eleven files listed in the hub's §3.
- [ ] `git check-ignore -v days/day-88-the-mcp-sidecar/lab/_manifests.py` prints a matching rule.
- [ ] `git diff pyproject.toml uv.lock` is empty. No package is added today.
- [ ] Read `k8s/deployment.yaml` end to end and can name the three lines that make `sutra-mcp` a
      sidecar with a real ordering guarantee.
- [ ] Confirmed `serve.py` carries a hard `DEADLINE_SECONDS`, so an interrupted run cannot leave a
      process holding port 8931.
- [ ] Ran `command -v kubectl kind docker` and know which of this day's claims your machine can check.

## Section 1 — what the cluster is told

- [ ] Read [1.1 Adjectives, not verbs](parts/01-what-the-cluster-is-told/1.1-adjectives-not-verbs.md);
      can say what changes about a bug when it moves from a script into a declarative document.
- [ ] Found every adjective and every noun in `k8s/deployment.yaml`, and confirmed there are no verbs.
- [ ] Read [1.2 The Pod is the unit](parts/01-what-the-cluster-is-told/1.2-the-pod-is-the-unit.md);
      can name the four things containers in one Pod share and which one this day turns on.
- [ ] Said what would happen if the sidecar's port were changed from `8000` to `8080`, and at which
      exact call it would surface.
- [ ] Read [1.3 The document is the artifact](parts/01-what-the-cluster-is-told/1.3-the-document-is-the-artifact.md);
      can name the three layers of manifest checking and which needs a cluster.
- [ ] Introduced the `startUpProbe` typo, ran `check.py`, read the message, and put it back.

## Section 2 — the sidecar decision

- [ ] Read [2.1 One Pod or two](parts/02-the-sidecar-decision/2.1-one-pod-or-two.md);
      ran both `address.py` arms and can say what exit `1` is claiming.
- [ ] Deleted the `Service` from `deployment-split.yaml`, re-ran `--split`, and said what the agent
      would experience at runtime. Then put it back.
- [ ] Read [2.2 The address is the boundary](parts/02-the-sidecar-decision/2.2-the-address-is-the-boundary.md);
      wrote the NetworkPolicy that would answer the split topology's finding.
- [ ] Can name one thing the sidecar makes **worse** for security, and the two earlier days whose
      controls still have to do that job.
- [ ] Read [2.3 What the sidecar costs](parts/02-the-sidecar-decision/2.3-what-the-sidecar-costs.md);
      wrote the three-line expiry comment using conditions somebody could actually observe.

## Section 3 — what the manifest must say

- [ ] Read [3.1 Checking what the cluster would read](parts/03-what-the-manifest-must-say/3.1-checking-what-the-cluster-would-read.md);
      ran both arms and saw `9 of 9` against `1 of 9`.
- [ ] Can say why the `?` line is not counted as a pass, and name the two earlier days that found the
      same shape.
- [ ] Deleted `restartPolicy: Always`, predicted both property changes, ran it, saw `7 of 9 ... 1 had
      nothing to check`, and put the line back.
- [ ] Read [3.2 The PIN on the back of the card](parts/03-what-the-manifest-must-say/3.2-the-pin-on-the-back-of-the-card.md);
      can state two things people get wrong about Kubernetes Secrets.
- [ ] Renamed `GOOGLE_API_KEY` to `GOOGLE_CREDENTIAL` in the naive manifest, watched the check pass a
      plaintext credential, and said why a longer word list is the wrong fix. Then put it back.
- [ ] Read [3.3 "The usual"](parts/03-what-the-manifest-must-say/3.3-the-usual.md);
      can say why `latest` has no rollback and why `Never` is safer on a registry-less cluster.
- [ ] Found the gap in the pin check: wrote a maximally pinned reference that still fails it.
- [ ] Read [3.4 The whistle and the limit](parts/03-what-the-manifest-must-say/3.4-the-whistle-and-the-limit.md);
      explained all four probe presences and both absences in the manifest.
- [ ] Worked out, in seconds, how long the cluster waits for the archive server before giving up.

## Section 4 — the order nobody promised

- [ ] Read [4.1 The clinic was not open yet](parts/04-the-order-nobody-promised/4.1-the-clinic-was-not-open-yet.md);
      ran both failing arms and saw `ConnectionRefusedError` against `TimeoutError`.
- [ ] Changed `STARTUP_SECONDS` to one, ran `race.py`, explained the surprising result, and put it
      back to five.
- [ ] Read [4.2 Redial](parts/04-the-order-nobody-promised/4.2-redial.md);
      ran `--gate`, saw `attempt 7`, and can say what the loop cost beyond the unavoidable wait.
- [ ] Set `GATE_DEADLINE_SECONDS` to `1.0`, predicted the exit code and the exception, ran it, and put
      it back.
- [ ] Read [4.3 What Kubernetes actually promises](parts/04-the-order-nobody-promised/4.3-what-kubernetes-actually-promises.md);
      can quote the condition under which the kubelet marks a sidecar *started* with no startup probe.
- [ ] Can say what `restartPolicy: Always` being absent would do, and why the Pod state is `Init:0/1`.

## Section 5 — what did not run

- [ ] Read [5.1 Taught on dry land](parts/05-what-did-not-run/5.1-taught-on-dry-land.md);
      ran `gate.py` and saw 0 of 6.
- [ ] Read the eight unrun commands and picked the one whose absence costs this day the most —
      and it was not the first row.
- [ ] Can state what this day verified and the exact phrase that must travel with the claim.
- [ ] Read [5.2 The first night in a new house](parts/05-what-did-not-run/5.2-the-first-night-in-a-new-house.md);
      mapped the six-step sequence onto the nine items and found the step no item prevents.
- [ ] Can name the three items that take about twenty minutes, and the one that is a code change.

## The paper — after the parts

- [ ] Read [papers/01 Labels over hierarchies](papers/01-labels-over-hierarchies.md).
- [ ] Ran `select.py`, `--off` and `--grow` and saw 4 of 4, 2 of 4, and an answer that shrank silently.
- [ ] Can say why `--off` answering two of four makes the demo stronger rather than weaker.
- [ ] Moved `release` into the tree path, predicted which question the hierarchy gains and which it
      loses, and put it back.
- [ ] Can state the `--grow` finding in one sentence and what it implies about a query that has been
      right for a year.

## The build brief

- [ ] `deploy/k8s/deployment.yaml` written, carrying all nine properties and the three-part sidecar
      declaration.
- [ ] A `Namespace` object plus `namespace: sutra` on every other object.
- [ ] `deploy/k8s/README.md` carries the cold start in order — `kind create cluster`, `kind load
      docker-image`, `kubectl apply` — plus the rollback line and the Secret command with its rotation
      caveat.
- [ ] The Secret is created by a committed command from `.env`; no Secret object is committed.
- [ ] `sutra/` — the MCP client's startup connection has a bounded retry with a deadline, and logs the
      attempt count.
- [ ] `sutra/` — `/readyz` means the MCP session is established and the tools are listed.
- [ ] `tests/test_deploy.py` — the nine properties, the naive-manifest-must-fail test, the
      `n/a`-is-not-a-pass test, and the digest-reference extension to the pin check.
- [ ] **Installed `kind` (or `k3d`) and `kubectl`**, and recorded the versions actually printed in
      `docs/PACKAGES.md` with the date.
- [ ] **Ran the cold start once from the README on a clean machine.** That is the whole of OPS-18.
- [ ] **Reproduced both Pod-level failures deliberately:** `ErrImageNeverPull` by skipping the image
      load, and `Init:0/1` by removing `restartPolicy: Always`.

## The evals, including ones that go red on demand

- [ ] `uv run python gate.py` runs and reports 0 of 6 — `deploy/k8s/` is the build brief.
- [ ] `check.py` exits `0`; `--naive` exits `1`.
- [ ] `address.py` exits `0`; `--split` exits `1`.
- [ ] `race.py` exits `1`; `--impatient` exits `1`; `--gate` exits `0`.
- [ ] `papers/pods-and-labels/select.py` exits `0`; `--off` exits `1`; `--grow` exits `1`.
- [ ] **Break it and watch it go red:** added a tenth check to `check.py` that returns `None`
      unconditionally, confirmed it reports `ok` and proves nothing, and removed it again.
- [ ] No stray process is holding port 8931 after the runs.

## The request budget

- [ ] Confirmed **zero** provider requests were made today, to every provider.
- [ ] Confirmed **zero** cluster commands were run, and that no `kubectl` output appears anywhere in
      this day's documents.
- [ ] Can list what was measured for real and what was written down unrun.

## Ledger & commit

- [ ] `./m depth 88` green.
- [ ] `./m trace` regenerated; day 88 closes exactly `ADK-69`, `OPS-18`.
- [ ] `./m wiki` regenerated.
- [ ] `docs/PROGRESS.md` row appended, verbatim from the hub's §11, with the real commit hash and the
      `⚠️` gate mark.
- [ ] `docs/PAPERS.md` — the `doi:10.1145/2890784` row added.
- [ ] Committed with the message in the hub's §11.
