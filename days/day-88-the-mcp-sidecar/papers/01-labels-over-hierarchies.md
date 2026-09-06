---
day: 88
paper: "doi:10.1145/2890784"
title: "Labels over hierarchies"
ids: ["ADK-69"]
level: production
prerequisites: ["../parts/01-what-the-cluster-is-told/1.2-the-pod-is-the-unit.md"]
prev: "../parts/05-what-did-not-run/5.2-the-first-night-in-a-new-house.md"
next: "../LESSON.md"
---

# Paper 01 — Labels over hierarchies

> **Borg, Omega, and Kubernetes**
> *Communications of the ACM*, volume 59, issue 5, 2016, pages 50–57.
> `doi:10.1145/2890784`
>
> The claim this day borrows: containers should be grouped into a Pod as the unit of scheduling and
> of shared fate, and workloads should be organised by **labels** — a flat, open set of key/value
> pairs, selected on at query time — rather than by a place in a fixed hierarchy.

## One-line answer

Ten years of running containers at scale produced two design choices that are now everywhere: the
Pod, which exists because cooperating processes need shared fate and one network namespace, and the
label, which exists because any hierarchy you choose privileges one question and makes every other
one an enumeration.

## The story

The school library, shelved by subject.

It is a good system and it took somebody a term to set up. History here, biology there, poetry in the
corner. A child who wants a book about volcanoes goes to one shelf and finds four, and the whole
thing works exactly as intended.

Then the inspector asks for every book published before a certain year, because the older ones are to
be checked for damage. There is no shelf for that. The answer is on every shelf, a few books at a
time, and finding them means walking the entire room and opening each cover.

Nothing is wrong with the library. The shelving answers the question it was built around perfectly,
and it answers no other question at all — and the year of publication was printed inside every book
the whole time, just not written anywhere you could sort by.

## The idea in plain language

The paper is a retrospective: three generations of cluster management, what each got right, and what
the third one — Kubernetes — kept from the first two on purpose. Two of its design conclusions are
the ones this day is built on.

**The Pod.** Real workloads are not one process. There is a server and a log shipper, a server and a
proxy, an agent and its MCP server. Those cooperating processes need to be on the same machine, to
start and stop together, and to talk to each other cheaply. The paper's argument is that the unit of
scheduling therefore should not be the container but a **group** of them with shared fate and a
shared network identity. That is the Pod, and part
[1.2](../parts/01-what-the-cluster-is-told/1.2-the-pod-is-the-unit.md) is its four consequences.

**Labels rather than hierarchy.** This is the deeper one. A workload has many attributes: which
application, which component, which environment, which team, which release. A hierarchy makes you
pick an order — team, then component, then environment — and every workload gets exactly one place.
That order is a bet on which question you will ask most, made before you know.

Labels refuse the bet. A workload carries an unordered set of key/value pairs, none privileged, and
selection happens at query time by naming the pairs you care about. *Every canary in production* is a
selector. In a tree it is a walk.

The paper also draws the consequence that makes the whole system work: **objects find each other by
label selector rather than by pointer.** A Deployment does not remember which Pods it made; it
selects the Pods carrying its labels, right now. A Service does not hold a list of endpoints; it
selects. That indirection is why you can take a Pod out of a Deployment's control by editing its
labels, and it is what part
[2.2](../parts/02-the-sidecar-decision/2.2-the-address-is-the-boundary.md)'s exposure check reads to
answer *"who can reach the archive server"* — because the answer is a question about selectors, not
about names.

## Why Sutra needs it

Because both design choices are load-bearing in this day's manifest. The sidecar decision is only
expressible because the Pod exists as a unit; the exposure argument is only checkable because
Services select by label.

And because Phase 14 adds more agents. The moment there is a second agent, the questions Sutra's
operators ask stop lining up with any single tree — *every component that touches the archive*,
*everything on the canary release*, *everything the desk team owns* — and the label model is the
reason those are one selector each rather than three different walks.

## The mechanism

The paper's argument written out as the property that matters, rather than paraphrased from the
abstract: **a hierarchy answers exactly the questions that align with its chosen axis, and turns
every other question into an enumeration of subtrees.** Labels have no axis, so every attribute is
equally selectable, and the cost is paid elsewhere — in discipline, because nothing enforces that two
teams use `component` to mean the same thing.

That trade is the honest version, and the paper does not hide it. A tree gives you uniqueness and a
guaranteed place for everything; labels give you flexibility and a naming problem.

## The paper in one demo

A small end-to-end project implementing the claim and nothing else. Twelve workloads, described
twice — once as labels, once as one path in one tree — and four questions asked of both.

```text
days/day-88-the-mcp-sidecar/lab/papers/pods-and-labels/
├── workloads.yaml  # twelve workloads, each with labels and one path
└── select.py       # label selection; --off selects by prefix; --grow adds one service
```

The setup is the whole argument, so the data file carries both descriptions of each workload:

```yaml
  - name: triage-api-prod-canary
    path: /team-desk/triage/prod/frontend
    labels: {app: sutra, component: triage, env: prod, tier: frontend, release: canary, team: desk}
```

The tree is `/<team>/<component>/<env>/<tier>` — a perfectly sensible hierarchy, chosen once, by
somebody who did not yet know which questions would be asked. Note that `release` is not a level in
it at all. That is not a trick: a tree has finitely many levels and a workload has arbitrarily many
attributes, so some attribute is always left out.

Selection by label is a subset test:

```python
def by_labels(workloads: list[dict], selector: dict[str, str]) -> set[str]:
    """A label selector: every workload whose labels are a superset of the selector."""
    return {w["name"] for w in workloads if selector.items() <= w["labels"].items()}
```

**Line by line:**

- `selector.items() <= w["labels"].items()` is a subset test on dictionary items, which is exactly
  Kubernetes' equality-based selector semantics: every key in the selector must be present with that
  value, and extra labels on the workload are irrelevant.
- A `set` of names is returned rather than a list, because the comparison in the ablation is set
  equality — *does this prefix name exactly these workloads* — and ordering would make that comparison
  wrong for uninteresting reasons.
- No hierarchy is consulted. That is the point: the label model does not know the tree exists.

And the ablation's criterion is rigorous rather than rhetorical:

```python
def hierarchy_answer(workloads: list[dict], wanted: set[str]) -> str | None:
    """The single prefix that names exactly `wanted`, if the tree has one."""
    for prefix in prefixes(workloads):
        if by_prefix(workloads, prefix) == wanted:
            return prefix
    return None
```

**Line by line:**

- Every prefix the tree can name is tried — `prefixes()` returns every ancestor of every workload —
  so a "no" here means the tree genuinely cannot express the question, not that the demo failed to
  look.
- The test is `== wanted`, exact set equality. A prefix that returns a superset or a subset is not an
  answer; it is a different question with a plausible-looking result, and part of the demo's third
  arm is what that costs.
- Returning the prefix rather than a boolean lets the report name it, so a reader can check the claim
  by eye.

Run it:

```bash
cd days/day-88-the-mcp-sidecar/lab/papers/pods-and-labels
uv run python select.py; echo "exit: $?"
```

**Line by line:**

- No flag: the label model, which is the paper's proposal.

Measured on 2026-09-07:

```text
12 workloads, described as labels and as one path each
selecting by: labels

  everything the desk team owns
    -l team=desk                    -> 8 workloads
  every triage workload, whoever owns it
    -l component=triage             -> 5 workloads
  everything running in production
    -l env=prod                     -> 8 workloads
  every canary in production
    -l env=prod,release=canary      -> 3 workloads

  4 of 4 questions answerable

  every question is one selector, because no attribute is privileged over another
exit: 0
```

Now the ablation — the same twelve workloads, the same four questions, selected by place in the tree:

```bash
uv run python select.py --off; echo "exit: $?"
```

**Line by line:**

- `--off` turns off the paper's contribution and nothing else. The workloads, the questions and the
  expected answers are identical.

Measured on 2026-09-07:

```text
selecting by: a place in the tree (the ablation)

  everything the desk team owns
    /team-desk                       -> 8 workloads
  every triage workload, whoever owns it
    /team-desk/triage                -> 5 workloads
  everything running in production
    no single prefix names these     -> 8 workloads, scattered
       they live under: ['/team-archive/archive/prod/backend', '/team-archive/archive/prod/frontend', '/team-desk/triage/prod/backend', '/team-desk/triage/prod/frontend', '/team-desk/voice/prod/frontend']
  every canary in production
    no single prefix names these     -> 3 workloads, scattered
       they live under: ['/team-archive/archive/prod/backend', '/team-desk/triage/prod/frontend', '/team-desk/voice/prod/frontend']

  2 of 4 questions answerable
    - everything running in production
    - every canary in production

  the tree answers the question it was shaped around and enumerates the rest
  a label is a fact about a workload; a path is a fact about one filing decision
exit: 1
```

**Two of four, not zero of four.** The tree is not useless: it answers *"everything the desk team
owns"* perfectly, because team is its first level. That is the honest result, and a demo that made
the hierarchy fail everything would have been arguing against a strawman.

And then the third arm, which is the finding worth more than either:

```bash
uv run python select.py --grow; echo "exit: $?"
```

**Line by line:**

- `--grow` adds exactly one workload — a triage service started by the *other* team — and re-asks
  the question the tree got right.

Measured on 2026-09-07:

```text
12 workloads, and then a second team starts its own triage service
the tree answered 'every triage workload' with the prefix /team-desk/triage

  before  -l component=triage -> 5   /team-desk/triage -> 5
  after   -l component=triage -> 6   /team-desk/triage -> 5

  the prefix now misses: ['triage-api-archive']
  it did not start failing. It started returning a smaller answer, with no error.

  the tree was right until somebody filed a thing somewhere reasonable
```

**The tree's second answer was correct by coincidence.** `/team-desk/triage` returned all five triage
workloads only because no other team happened to own one. The moment one does, the prefix returns
five out of six — and there is no error, no warning and no way to tell from the output that the
answer shrank relative to the truth. The label selector returned six without being changed.

That is the paper's argument at its sharpest: the failure of a hierarchy is not that it says *no*.
It is that it keeps saying *yes*, about a smaller set, forever.

## When it breaks

The label model has a real cost and the paper is not coy about it.

**Nothing enforces meaning.** `component: api` is a string. Two teams will independently choose it,
and within one namespace a selector matching it matches both — which is part
[5.2](../parts/05-what-did-not-run/5.2-the-first-night-in-a-new-house.md)'s step 3, arriving as a
production hazard. A tree gives uniqueness for free; labels require a convention and a person to
maintain it.

**A wrong selector fails silently in the worst direction.** A Service whose selector matches nothing
is a valid object with no endpoints — it accepts connections and refuses them. A Deployment whose
`matchLabels` does not match its own template creates Pods forever, each one immediately unmanaged.
Both are configurations, not errors, and both are consequences of the same indirection that makes
labels powerful.

**Where the claim does not hold.** For genuinely hierarchical things — a namespace inside a cluster,
a directory inside a filesystem — a tree is the right structure and labels would be a worse fit.
Kubernetes uses both: namespaces are a hierarchy, and everything inside one is labelled. The paper's
claim is about *workload organisation*, not about naming in general, and reading it as "trees are
bad" is the common overreach.

## In production

**What survived.** Almost all of it, and beyond Kubernetes. The Pod is now the assumed unit for
co-located cooperating containers, and the sidecar pattern this whole day is about is a direct
descendant of it. Label selection is everywhere: it is how Services find Pods, how Deployments find
ReplicaSets, how monitoring finds targets, and how every `kubectl get -l` a person has ever typed
works. The declarative, API-driven, reconcile-toward-desired-state model that part
[1.1](../parts/01-what-the-cluster-is-told/1.1-adjectives-not-verbs.md) opens with is from the same
lineage.

**What did not.** The paper's lessons-learned section warns about things the field then went and did
anyway. Its caution about the one-IP-per-Pod model's cost was real and the model shipped regardless,
because the alternative — containers sharing a host's port space — was worse. And its scepticism
about running stateful workloads on a cluster manager designed for stateless ones is a warning
practice has steadily ignored: StatefulSets, operators and cluster-hosted databases are now ordinary,
which is not a refutation of the paper so much as the field deciding to pay the cost the paper named.

**What it means for Sutra, concretely.** Every label in this day's manifests is a query somebody will
run later. `app: sutra` answers *what is ours*; `component: mcp` is what part
[2.2](../parts/02-the-sidecar-decision/2.2-the-address-is-the-boundary.md)'s exposure check keys on;
`env: local` is what will separate this from anything deployed elsewhere. The one that is missing is
`release`, and part [3.3](../parts/03-what-the-manifest-must-say/3.3-the-usual.md)'s pinned tag is
the reason it has not been needed yet.

**The review comment a senior engineer leaves:** *"Write down what our label keys mean, in the repo,
before the second service exists. `component` will be chosen by somebody else for something else and
we will find out through a Service that selects two applications."*

**The interview question:** *"Why does Kubernetes use labels instead of a naming hierarchy?"* The
answer that shows experience gives the reason — no attribute is privileged, so any question is one
selector — and then the cost, which is that nothing enforces what a label key means, so a wrong
selector produces a plausible answer rather than an error.

## Check yourself

```bash
cd days/day-88-the-mcp-sidecar/lab/papers/pods-and-labels
uv run python select.py; echo "exit: $?"
uv run python select.py --off; echo "exit: $?"
uv run python select.py --grow; echo "exit: $?"
```

Three arms. Say why `--off` answers two of four rather than none, and why that makes the demo
stronger rather than weaker.

Now add a level to the tree: change every `path` in `workloads.yaml` so that `release` comes right
after `team`. Predict which of the four questions the hierarchy can then answer, and which one it has
just lost. Then put it back.

**Out loud, without scrolling up:** the `--grow` arm's finding in one sentence, and what it implies
about trusting a query that has been right for a year.

**Next:** back to the hub — [`LESSON.md`](../LESSON.md).
