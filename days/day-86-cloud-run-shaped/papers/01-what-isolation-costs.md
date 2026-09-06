---
day: 86
paper: "doi:10.1109/ISPASS.2015.7095802"
title: "What isolation costs"
ids: ["ADK-66"]
level: production
prerequisites: ["../parts/01-what-a-container-promises/1.1-an-image-is-a-recipe.md"]
prev: "../parts/05-the-word-stateless/5.3-what-a-real-deployment-adds.md"
next: "../LESSON.md"
---

# Paper 01 — What isolation costs

> **An updated performance comparison of virtual machines and Linux containers**
> 2015 IEEE International Symposium on Performance Analysis of Systems and Software (ISPASS),
> 2015, pages 171–172. `doi:10.1109/ISPASS.2015.7095802`
>
> The claim this day borrows: containers match or exceed virtual-machine performance in nearly
> every case, and both are close to untouched hardware on processor and memory — so what
> isolation costs is paid on input and output, not on computation.

## One-line answer

Isolation used to be a thing you bought and paid for in performance, and this paper is the
measurement that showed the price had fallen to almost nothing for computation while remaining
real for anything that crosses the boundary — which is why the unit of deployment became an image
rather than a machine.

## The story

The two ways to give a tenant their own place.

One way is to build a separate house: own walls, own foundations, own water tank, own everything.
Nobody can hear anybody, nothing is shared, and it costs what a house costs — and it takes as
long to put up as a house takes.

The other is to partition an existing floor: solid walls between units, separate doors, separate
meters, but one building, one foundation, one water supply. Each tenant has a place of their own
in every way that matters to them, and a new unit is ready in days rather than months.

For a long time the second option had a reputation: thin walls, you can hear the neighbours,
things leak between units. The question that decided which one people built was not architectural
taste. It was whether the partitioned version had actually got good enough — and somebody had to
measure it rather than assert it.

## The idea in plain language

By 2015 there were two ways to run somebody else's code on your machine with a boundary around it.

**A virtual machine** simulates hardware. The guest has its own kernel, its own device drivers,
its own idea of a disk. Isolation is strong because the boundary is low down, and everything the
guest does to a device passes through a layer that translates it.

**A container** shares the host's kernel. The boundary is a set of kernel features — namespaces,
which control what a process can see, and control groups, which limit what it can use. There is
no simulated hardware, so there is nothing to translate.

The intuition of the time was that the second must be faster and weaker, and that the first must
be slower and safer, and that the interesting question was where you wanted to sit on that trade.
The paper's contribution was to *measure* it across a spread of workloads — processor, memory,
storage, network — rather than argue about it.

The result, in the two sentences that matter:

- **On processor and memory, both are within noise of running directly on the hardware.** The
  overhead people were budgeting for was not there.
- **On input and output, the differences are real**, and they concentrate where work crosses the
  boundary — disk operations, network round trips — rather than scaling with how much computation
  is done inside it.

The consequence was not "use containers because they are faster". It was that **isolation stopped
being a performance decision**, which meant it could become a packaging decision. Once a boundary
costs nothing to compute inside, you can put a boundary around every service, and once you do
that the image becomes the natural unit of deployment. Everything in this day rests on that
having been settled.

## Why Sutra needs it

Because part [1.1](../parts/01-what-a-container-promises/1.1-an-image-is-a-recipe.md) asserted
that the value of a container is reproducibility rather than isolation, and that assertion only
holds because isolation is cheap. If a boundary cost thirty percent, the image would be a thing
you used sparingly and the packaging benefit would not be worth it.

And because the paper's shape predicts where this system will actually pay. Sutra's desk is not
computation-heavy; it waits on model calls and reads small files. Its cost is crossings — network
round trips, a file read per readiness probe, a call to a separate MCP process. Those are exactly
the axis the paper says is not free, which is a more useful thing to know than a total.

## The mechanism

The method, written out as the thing to reproduce rather than as an abstract:

**Hold everything constant except the isolation layer.** Same hardware, same workload, same
inputs; vary only whether the work runs directly, inside a container, or inside a virtual
machine. That sounds obvious and is the hard part — a comparison where the guest also has a
different filesystem, or a different amount of memory, measures the difference in those.

**Use workloads that separate the axes.** A processor benchmark and a memory benchmark say
whether the boundary costs anything to *compute* behind. A storage benchmark and a network
benchmark say what it costs to *cross*. Reporting a single blended number would have hidden the
finding, because the finding is that the two axes behave differently.

**Report the overhead relative to the unvirtualised baseline**, so the numbers answer "what does
this cost me" rather than "which of these two is faster".

The part that carried across to practice is the second point. The useful question about any
isolation boundary is not *how much overhead* but *what does it charge for* — and the answer is
almost always crossings.

## The paper in one demo

A small project implementing the paper's method and nothing else. Two files, one workload, one
boundary, and a switch that removes it.

```text
days/day-86-cloud-run-shaped/lab/papers/isolation/
├── boundary.py   # the workload, and the far side of the boundary
└── demo.py       # measures the crossing cost and prices two workloads; --off removes it
```

**The limitation, stated plainly.** The paper's axis is virtual machine against container. This
machine has neither a hypervisor nor a container runtime — `docker --version` reports
`command not found` — so the demo uses the only isolation boundary available to it: an operating
system process. That is a narrower boundary than either of the paper's, and a process boundary is
cheaper to cross than a network hop between containers. What carries over is the *shape*: a
boundary that is free per unit of work and charged per crossing. What does not carry over is any
particular number.

The workload is deliberately dull, because the point is what surrounds it:

```python
def checksum(rounds: int) -> int:
    """A unit of pure CPU work: no allocation to speak of, no I/O, no syscalls."""
    total = 0
    for i in range(rounds):
        total = (total * 31 + i) & 0xFFFFFFFF
    return total
```

**Line by line:**

- Integer arithmetic in a loop, and nothing else. No allocation, no file access, no system calls —
  if the boundary charged for computation, this is where it would show.
- `& 0xFFFFFFFF` keeps the number bounded so Python does not drift into arbitrary-precision
  arithmetic partway through, which would make later iterations slower than earlier ones and turn
  the workload into a measurement of integer size.
- Deterministic, so the same rounds always cost the same work.

The first version of this demo timed each workload end to end and compared totals. That produced a
compute overhead that swung between **-22.8% and +10.9%** across runs on this laptop — a result
whose *sign* changed, because the effect being measured was smaller than the machine's noise. So
the two ingredients are measured separately, each where it is stable:

```python
def crossing_cost() -> float:
    """Seconds for one round trip across the boundary, averaged over many of them."""
    parent, child = mp.Pipe()
    process = mp.Process(target=worker, args=(child,))
    process.start()
    try:
        parent.send(1)  # one warm-up crossing, so start-up is not in the average
        parent.recv()
        start = time.perf_counter()
        for _ in range(CROSSING_SAMPLES):
            parent.send(1)
            parent.recv()
        elapsed = time.perf_counter() - start
    finally:
        parent.send(None)
        process.join(timeout=10)
        if process.is_alive():
            process.terminate()
    return elapsed / CROSSING_SAMPLES
```

**Line by line:**

- Twenty thousand round trips, averaged. One crossing takes tens of microseconds, which is
  unmeasurable against a clock with millisecond noise; twenty thousand of them takes most of a
  second, which is not.
- The warm-up crossing before the timer starts, so process creation and the first import are
  outside the average. Without it the first sample carries the whole start-up cost and the mean is
  wrong in a way that flatters nothing in particular.
- `send` then `recv` — a **round trip**, not a one-way send. A one-way measurement would time how
  fast this process can write into a pipe, which is not what a boundary crossing costs.
- The `finally` shuts the worker down and escalates to `terminate()` if it does not go, so a
  failed run does not leave a process behind.
- Returns a per-crossing figure, which is the number that can then be multiplied by a workload's
  crossing count.

Then the two workloads are priced from those two stable measurements rather than timed:

```python
    for name, crossings in workloads.items():
        cost = crossings * per_crossing
        overhead = cost / work * 100
```

**Line by line:**

- `crossings * per_crossing` is the model: a boundary charges per crossing and nothing else. That
  is the paper's claim expressed as arithmetic, and the demo's job is to show the two workloads
  land in different places under it.
- Dividing by `work` expresses the cost as a percentage of the useful work, which is what makes
  the two rows comparable — both do exactly the same total computation.
- No timing of the isolated run at all. That is the honest consequence of the noise measured
  earlier: a number this laptop cannot measure reliably is not reported as if it could.

Run it:

```bash
cd days/day-86-cloud-run-shaped/lab/papers/isolation
uv run python demo.py; echo "exit: $?"
```

**Line by line:**

- No flag: the boundary is in place, which is the paper's treatment condition.

Measured on 2026-09-07:

```text
workload total: 8,000,000 rounds either way
boundary: a separate process
  work in this process, best of 5: 731 ms
  one crossing, mean of 20,000:      29.3 us

  workload               crossings  boundary cost   overhead
  bulk    (1 job)                1          0.0ms      0.00%
  chatty  (4,000 jobs)       4,000        117.1ms     16.02%

  the boundary costs 0.00% on compute and 16.0% on chatter
  isolation is nearly free per unit of work and is paid for per crossing
exit: 0
```

**Identical total work, and 0.00% against 16.0%.** The only difference between the two rows is how
many times the same eight million rounds were split up.

Now the ablation — the same two workloads with no boundary at all:

```bash
uv run python demo.py --off; echo "exit: $?"
```

**Line by line:**

- `--off` removes the boundary and changes nothing else. It exits `1`, because the demo's job is
  to reproduce the claim and this arm deliberately cannot.

Measured on 2026-09-07:

```text
boundary: none (the ablation)
  work in this process, best of 5: 705 ms
  crossings: none, so there is nothing to average

  workload               crossings  boundary cost   overhead
  bulk    (1 job)                1          0.0ms      0.00%
  chatty  (4,000 jobs)       4,000          0.0ms      0.00%

  no boundary was crossed, so both workloads cost the same as no isolation
  an isolation cost cannot be observed by a run that has no isolation in it
exit: 1
```

Both rows collapse to zero. The workloads are unchanged, the split is unchanged, and the effect
disappears entirely — which is what an ablation is for: it shows the measured difference came from
the boundary and not from the shape of the workload.

## When it breaks

**The claim does not hold where the boundary is not thin.** The paper measures containers sharing
a kernel. A boundary that involves a network hop, an encryption layer, or a hypervisor mediating
each device access charges much more per crossing, and the "nearly free" half of the finding
stops being true.

**It does not hold for input and output at all**, and the paper says so — this is the half that
gets dropped in citation. "Containers are basically free" is what people remember; the measured
statement is "free on processor and memory, and not on storage and network". A service whose work
is mostly waiting on a disk or a socket is exactly the case the paper excludes from its
reassurance.

**And the specific numbers are gone.** The measurements are from 2015 hardware, 2015 kernels and
a 2015 container runtime. Every layer has changed, several of them substantially. Quoting a
percentage from this paper today is quoting an artefact of a machine nobody has.

**The demo's own limits**, stated because the alternative is implying more than was shown: the
boundary is a process, not a container; the workload is Python, whose interpreter overhead is
large enough to make the compute row generous; and the crossing cost is a local pipe, which is
the cheapest crossing there is. The demo reproduces the paper's *shape* on a much narrower axis.
It is not a replication.

## In production

**What survived.** The conclusion, completely, and so thoroughly that it stopped being cited: that
containers are the default unit of deployment is now an assumption rather than a claim, and the
reason it is safe to assume is this class of measurement. Every design in this day — one image per
service, a boundary around each process, two services rather than one — is affordable only because
that question was settled.

The methodological half survived too, in the form of a habit: when comparing isolation options,
separate the axes and report against an unvirtualised baseline. That is what makes a result
usable rather than a league table.

**What did not.** The numbers, entirely. And the framing: in 2015 the paper was arguing against a
live belief that containers were a performance compromise, and that belief is gone, so the
argument reads as obvious. The genuinely current question is a different one — how *strong* the
isolation is, given a shared kernel — and this paper does not address it. Day 71's sandbox
argument is where that thread is picked up.

**What it means for this repository, concretely.** Sutra's costs are crossings, not computation:

| Crossing | How often | Cheap? |
| --- | --- | --- |
| api to the MCP process | per tool call | a local hop, small |
| api to a model provider | per model call | a network round trip; this is the real cost |
| readiness probe reading the ledger | per probe, per replica, for ever | a file read; small and constant |
| two replicas contending on the ledger | per spend | not a cost — a correctness bug (part 5.2) |

The last row is the one the paper's frame does not cover and this day found anyway: a crossing
that is cheap and *wrong*.

**The review comment a senior engineer leaves:** *"Fine to split the MCP server into its own
container — the boundary is nearly free. Just count the crossings per request first, because that
is what we will actually pay, and if a tool call becomes three hops we will feel it."*

**The interview question:** *"Why containers rather than virtual machines?"* The answer that shows
experience does not say "lighter" and stop. It says the performance argument was settled — the
overhead is negligible on compute and real on I/O — so the decision is now about packaging speed
and isolation strength, and then notes that a shared kernel is a weaker boundary, which is a
separate trade from the performance one.

## Check yourself

```bash
cd days/day-86-cloud-run-shaped/lab/papers/isolation
uv run python demo.py; echo "exit: $?"
uv run python demo.py --off; echo "exit: $?"
```

Same work, same split, one difference. Say what the ablation removes, and why the bulk row reads
`0.00%` in *both* runs — that is not a bug and explaining it is the exercise.

Now change `CHATTY_JOBS` to 400 and predict the chatty overhead before running it. The
relationship is not subtle, and being able to state it is the whole of the paper's finding.

**Out loud, without scrolling up:** half of this paper's result is quoted constantly and half is
usually dropped. State both halves, and say which one applies to a service that mostly waits on a
network.

**Next:** back to the hub — [`LESSON.md`](../LESSON.md).
