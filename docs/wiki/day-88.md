# Day 88 - Kubernetes on the laptop — the MCP sidecar

IDs closed: ADK-69, OPS-18 · source: `days/day-88-the-mcp-sidecar/`

## Parts

### 1.1 - Adjectives, not verbs
`days/day-88-the-mcp-sidecar/parts/01-what-the-cluster-is-told/1.1-adjectives-not-verbs.md` · level `foundation` · ids ADK-69

Every deployment tool up to now took an instruction and carried it out once; a cluster takes a description of what should be true and spends the rest of its life closing the gap — so you stop writing what to do and start writing what should be the case.

### 1.2 - The Pod is the unit, not the container
`days/day-88-the-mcp-sidecar/parts/01-what-the-cluster-is-told/1.2-the-pod-is-the-unit.md` · level `foundation` · ids ADK-69

A cluster does not schedule containers, it schedules Pods — a group of containers that share one network namespace, one lifecycle and one machine — and every interesting decision today follows from the fact that containers in one Pod reach each other on localhost while containers in two Pods do not.

### 1.3 - The document is the artifact
`days/day-88-the-mcp-sidecar/parts/01-what-the-cluster-is-told/1.3-the-document-is-the-artifact.md` · level `working` · ids OPS-18

The thing you ship to a cluster is a YAML file, which means the deployment can be read, reviewed and checked before anything runs — and on a machine with no cluster at all, that file is still the whole deliverable rather than a description of one.

### 2.1 - One Pod or two
`days/day-88-the-mcp-sidecar/parts/02-the-sidecar-decision/2.1-one-pod-or-two.md` · level `working` · ids ADK-69

The agent and its MCP server can go in one Pod or in two, and the manifest does not merely record that choice — it determines the address, the failure mode, the scaling ratio and the upgrade unit, all four of which fall out of the single fact that one Pod means one network namespace.

### 2.2 - The address is the boundary
`days/day-88-the-mcp-sidecar/parts/02-the-sidecar-decision/2.2-the-address-is-the-boundary.md` · level `production` · ids ADK-69, OPS-18

A thing with no address cannot be called by anything that does not already share its network namespace, so putting the MCP server in the agent's Pod enforces the data boundary by topology rather than by policy — and the same fact, read the other way, means the agent has unauthenticated access to it and always will.

### 2.3 - What the sidecar costs
`days/day-88-the-mcp-sidecar/parts/02-the-sidecar-decision/2.3-what-the-sidecar-costs.md` · level `working` · ids ADK-69

A sidecar cannot be scaled, restarted, upgraded or reached independently of the container it rides with, and every one of those is the same fact — shared lifecycle — which is worth paying for exactly while the two things genuinely have one lifecycle, and is a trap the moment they do not.

### 3.1 - Checking what the cluster would read
`days/day-88-the-mcp-sidecar/parts/03-what-the-manifest-must-say/3.1-checking-what-the-cluster-would-read.md` · level `working` · ids OPS-18

Nine properties decide whether this manifest is worth applying, every one of them is a thing a careful reviewer could check by reading, and turning them into a script is what makes them true every time rather than on the days somebody was paying attention.

### 3.2 - The PIN on the back of the card
`days/day-88-the-mcp-sidecar/parts/03-what-the-manifest-must-say/3.2-the-pin-on-the-back-of-the-card.md` · level `working` · ids OPS-18

A manifest is a file that gets committed, reviewed, pasted into chat and — in this repository's case — published, so a credential written into it as a literal has been handed to everybody who will ever read the deployment, and the fix is one field name.

### 3.3 - \"The usual\
`days/day-88-the-mcp-sidecar/parts/03-what-the-manifest-must-say/3.3-the-usual.md` · level `working` · ids OPS-18

latest is not a version, it is a subscription to whatever is newest, so a manifest that names it describes a different system on Tuesday than it did on Monday — and the companion field, imagePullPolicy, decides whether a mistake about images fails loudly or is quietly papered over with something from the internet.

### 3.4 - The whistle and the limit
`days/day-88-the-mcp-sidecar/parts/03-what-the-manifest-must-say/3.4-the-whistle-and-the-limit.md` · level `working` · ids ADK-69, OPS-18

Three fields decide whether a Pod is a controlled thing or a hopeful one: a probe so the cluster can tell working from present, a limit so one container cannot take the machine down with it, and a non-root user so a container that is compromised did not also inherit the node.

### 4.1 - The clinic was not open yet
`days/day-88-the-mcp-sidecar/parts/04-the-order-nobody-promised/4.1-the-clinic-was-not-open-yet.md` · level `production` · ids ADK-69

💥 Two containers in one Pod start at the same time, so an agent that dials its MCP server on boot dials a process that exists and is not yet listening — and the error it gets back depends on a timeout it chose, which means the same failure arrives wearing two different names and only one of them points at the truth.

### 4.2 - Redial
`days/day-88-the-mcp-sidecar/parts/04-the-order-nobody-promised/4.2-redial.md` · level `working` · ids ADK-69

The caller's half of the fix is a bounded retry with backoff around the first connection, which turns a startup race from a fatal error into six-tenths of a second nobody notices — and it works whether or not the platform underneath ever promises anything about ordering.

### 4.3 - What Kubernetes actually promises
`days/day-88-the-mcp-sidecar/parts/04-the-order-nobody-promised/4.3-what-kubernetes-actually-promises.md` · level `production` · ids ADK-69

Kubernetes will start a sidecar before the app container and wait for it — but only if the sidecar is declared as an initContainers entry with restartPolicy: Always, and "wait for it" means a process is running unless you also give it a startupProbe, which is the difference between the guarantee people think they have and the one they do.

### 5.1 - Taught on dry land
`days/day-88-the-mcp-sidecar/parts/05-what-did-not-run/5.1-taught-on-dry-land.md` · level `production` · ids OPS-18

There is no kubectl, no kind, no k3d and no docker on this machine, so nine manifest properties, one topology derivation and one startup race were measured for real and every command that needs a cluster is written down unrun — which makes the Phase 13 gate's second clause the one finding this day cannot close.

### 5.2 - The first night in a new house
`days/day-88-the-mcp-sidecar/parts/05-what-did-not-run/5.2-the-first-night-in-a-new-house.md` · level `production` · ids ADK-69, OPS-18

The manifests describe a Pod that would run; the distance between that and a deployment a team can operate is nine things, and the first two are a namespace and a rollback path, both of which are five minutes and neither of which is interesting until the night you need them.

## Papers - read after the parts

### doi:10.1145/2890784 - Labels over hierarchies
`days/day-88-the-mcp-sidecar/papers/01-labels-over-hierarchies.md`

Ten years of running containers at scale produced two design choices that are now everywhere: the Pod, which exists because cooperating processes need shared fate and one network namespace, and the label, which exists because any hierarchy you choose privileges one question and makes every other one an enumeration.

