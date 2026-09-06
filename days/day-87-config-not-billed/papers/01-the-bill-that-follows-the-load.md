---
day: 87
paper: "doi:10.1145/1721654.1721672"
title: "The bill that follows the load"
ids: ["ADK-68"]
level: production
prerequisites: ["../parts/04-what-it-costs/4.1-priced-in-requests.md"]
prev: "../parts/05-in-production/5.2-before-you-would-actually-deploy.md"
next: "../LESSON.md"
---

# Paper 01 — The bill that follows the load

> **A view of cloud computing**
> *Communications of the ACM*, volume 53, issue 4, 2010, pages 50–58.
> `doi:10.1145/1721654.1721672`
>
> The claim this day borrows: the economic case for renting computing is not that it is cheaper per
> unit, but that **elasticity removes the need to provision for peak** — and the size of the prize is
> the ratio between peak load and average load.

## One-line answer

Paying for what you used beats paying for the worst hour of the week by exactly as much as your load
is spiky, and a week of this desk's real shape measures that at eighty-one per cent of the bill.

## The story

The wedding hall booked for the whole month.

A family has a function coming up. The hall they want is available by the day, and it is also
available on a monthly rate. The monthly rate is better value *per day* and the person quoting it
says so, repeatedly.

The function is one day. There is a mehndi the evening before and people staying two nights either
side, so call it four days of genuine use. Booking the month costs less per day and roughly seven
times as much in total, and the family very nearly does it, because the per-day number is the one
being compared.

The question that settles it is not which rate is cheaper. It is: **how many days do we actually
need it, out of how many we would be paying for?** Everything else is a distraction from that ratio.

## The idea in plain language

The paper is a survey of cloud computing written when the term was new, and its lasting contribution
is an economic argument rather than a technical one. Stripped to the claim this day uses:

**Buying capacity means buying the peak.** A machine you own has to be big enough for the busiest
moment, and it is that big during the quietest one too. The unused capacity between those is not
waste in the sense of a mistake — it is what buying-for-peak *means*.

**Renting capacity means buying the area under the curve.** If capacity can be added and removed as
load changes, the bill follows the load rather than its maximum.

**The prize is the peak-to-average ratio.** Flat load, no prize: the peak is the average and both
models cost the same. Spiky load, large prize, growing linearly with how spiky. The paper's
memorable framing is that even paying a *premium* per unit for rented capacity can win, provided the
ratio is large enough — which turns "the cloud is more expensive per hour" from an objection into an
input.

Two things the argument depends on, and they are where it fails when it fails:

- **The capacity has to actually be releasable.** Elasticity you cannot exercise is a machine with a
  different invoice.
- **The load has to be genuinely variable.** A service with steady traffic is the flat case, and for
  the flat case the paper's own argument says renting has no economic advantage.

The paper also lists obstacles it expects to matter, and one of them — **data lock-in** — is the one
part [4.2](../parts/04-what-it-costs/4.2-the-dependency-you-inherit.md) met in a requirements file.

## Why Sutra needs it

Because this day is a decision about a managed platform and the decision is economic before it is
technical. Part [4.1](../parts/04-what-it-costs/4.1-priced-in-requests.md) found the desk's two
halves in incompatible units; this paper is the argument that tells you which half to look at first
and what number decides it.

And because the desk is exactly the shape the argument is about. Fourteen slots a day with zeros at
each end, nothing at the weekend, and one bad Wednesday — that is not a flat service. Whether the
prize is worth the obstacles is a different question, and it is answerable only after the ratio is
measured.

## The mechanism

The method, written out as the thing to compute rather than paraphrased as an abstract:

**Take the load over a period, in whatever unit capacity is bought in.** Not requests — *units of
capacity per slot*, because capacity comes in whole units and a slot needing one and a bit needs two.

**Compute two totals.** The sum of what was needed, slot by slot, which is what elastic buying pays
for. And the maximum multiplied by the number of slots, which is what provisioning for peak pays for.

**The ratio between them is the argument.** Everything else in the economic case is detail.

The lab's ceiling division is where the "whole units" part lives:

```python
def units_for(requests: int) -> int:
    """How many whole units of capacity a slot's load needs."""
    return -(-requests // UNIT_CAPACITY)  # ceiling division without importing math
```

**Line by line:**

- `-(-a // b)` is integer ceiling division: floor-divide the negation and negate back. It avoids
  importing `math` and it avoids floating point, which matters because a slot needing exactly
  `UNIT_CAPACITY` must be one unit and not two.
- The function is the reason a flat-looking week still has granularity. A slot with a single request
  costs a whole unit, so elasticity's win is never quite the full ratio.
- `UNIT_CAPACITY` is twenty, which is the one allowance this repository has actually observed. Using
  a measured number rather than a round one keeps the demo's arithmetic honest even though the
  scenario is a fixture.

## The paper in one demo

A small end-to-end project implementing the paper's claim and nothing else: one week of load, one
unit of capacity, two ways of buying it.

```text
days/day-87-config-not-billed/lab/papers/elasticity/
├── load.py    # one deterministic week: a weekday shape, a quiet weekend, one bad Wednesday
└── demo.py    # both buying models over that week; --off removes elasticity
```

The week is generated once and shared by both arms, because two arms given different weeks are
comparing weather rather than models:

```python
def week() -> dict[str, tuple[int, ...]]:
    """Requests per slot, per day. Wednesday carries the incident."""
    profile: dict[str, tuple[int, ...]] = {}
    for day in DAYS:
        shape = WEEKEND if day in ("Sat", "Sun") else WEEKDAY
        multiplier = 3 if day == "Wed" else 1
        profile[day] = tuple(slot * TURNS_PER_TICKET * multiplier for slot in shape)
    return profile
```

**Line by line:**

- No randomness anywhere. The paper's claim is arithmetic, so a demo of it that varies run to run
  would be adding noise to a proof.
- `WEEKEND` is a different shape rather than a scaled one — a quiet day is not a busy day divided,
  it is a day where most slots are empty, and that distinction is what produces the ratio.
- `multiplier = 3 if day == "Wed"` is the incident: a billing run goes wrong and the queue triples.
  One bad day in seven is what makes a peak, and peaks are the whole subject.
- Returning a dictionary keyed by day means the report can print per-day rows, which is what makes
  the waste legible rather than a single number.

And the two buying models are one line apart:

```python
    held = needed if elastic else [peak] * len(needed)
```

**Line by line:**

- `needed` is capacity that follows load. `[peak] * len(needed)` is the same peak held for every slot
  of the week, including the ones with no traffic at all.
- One expression, one flag. The ablation is not a different program; it is the same program with the
  paper's idea removed, which is what makes the comparison mean something.

Run it:

```bash
cd days/day-87-config-not-billed/lab/papers/elasticity
uv run python demo.py; echo "exit: $?"
```

**Line by line:**

- No flag: elasticity on, which is the paper's proposal.

Measured on 2026-09-07:

```text
one week, 98 slots, one unit serves 20 requests per slot
buying: capacity follows the load

  day     requests  peak units  units held
  Mon          246           3          19
  Tue          246           3          19
  Wed          738           7          42
  Thu          246           3          19
  Fri          246           3          19
  Sat           21           1           6
  Sun           21           1           6

  peak slot needs 7 unit(s); the average slot needs 0.90
  peak-to-average ratio: 7.8x  <- the paper says this is the whole prize

  unit-slots actually used:  130
  unit-slots paid for:       130
  waste:                     0  (0% of the bill)

  paying for what was used costs less than paying for the worst slot of the week
exit: 0
```

Now the ablation — the same week, capacity provisioned for the peak:

```bash
uv run python demo.py --off; echo "exit: $?"
```

**Line by line:**

- `--off` removes elasticity and changes nothing else. Same week, same unit size, same arithmetic.

Measured on 2026-09-07:

```text
buying: provisioned for the peak

  day     requests  peak units  units held
  Mon          246           3          98
  Tue          246           3          98
  Wed          738           7          98
  Thu          246           3          98
  Fri          246           3          98
  Sat           21           1          98
  Sun           21           1          98

  peak slot needs 7 unit(s); the average slot needs 0.90
  peak-to-average ratio: 7.8x  <- the paper says this is the whole prize

  unit-slots actually used:  130
  unit-slots paid for:       686
  waste:                     556  (81% of the bill)

  every quiet slot, every night and the whole weekend are charged at Wednesday's rate
exit: 1
```

**One hundred and thirty unit-slots used, six hundred and eighty-six paid for. Eighty-one per cent
waste.** The `units held` column is the finding: it is `98` on Sunday, a day with twenty-one requests
in it, because Wednesday happened.

And the ratio predicted it. Peak-to-average is 7.8, and 686/130 is 5.3 — lower than the ratio because
of the whole-unit granularity that `units_for` introduces, which is exactly the direction the paper's
own caveats point.

## When it breaks

The claim is conditional and the conditions are where it stops.

**Flat load.** If the peak is the average, both columns are identical and elasticity buys nothing.
The paper says this plainly and it is routinely quoted as though it did not.

**Capacity that cannot be released.** A resource billed by existence — part
[4.1](../parts/04-what-it-costs/4.1-priced-in-requests.md)'s second half — is the provisioned-for-peak
model wearing a rented label. The word "cloud" on an invoice does not make a bill elastic; the
ability to release capacity does.

**Granularity.** Capacity comes in whole units and in minimum durations. A load that spikes for
moments against a platform that bills in longer blocks recovers much less of the theoretical prize
than the ratio suggests. The demo's `units_for` is a small version of this and real platforms have a
larger one.

**The obstacles the paper listed.** It named several, and they did not fare equally. Data transfer
costs and unpredictable performance were substantially addressed by the industry. Data lock-in was
not — and part [4.2](../parts/04-what-it-costs/4.2-the-dependency-you-inherit.md) found a small,
current, entirely ordinary instance of it: a dependency and a version pin that attach themselves to a
project through a deploy command and appear in no diff.

## In production

**What survived.** The economic argument, completely and without much modification. Provisioning for
peak is now the unusual choice rather than the default, autoscaling is a standard expectation, and
"pay for what you use" is the assumed billing model for new infrastructure. The peak-to-average ratio
as *the* number that decides is still the right first question, and it is still the question most
teams have not computed.

**What did not.** The paper's framing of the alternative was owning machines, and that comparison has
largely stopped being the live one — the argument today is between two rented models, per-request and
always-on, which is part [4.1](../parts/04-what-it-costs/4.1-priced-in-requests.md)'s two units. The
paper's optimism about lock-in becoming a solved problem through standardisation did not hold; if
anything the direction reversed, as managed services grew richer and therefore harder to leave. And
its list of obstacles was written for infrastructure, so it has nothing to say about the thing that
actually constrains this repository — a per-day request allowance on a free tier, which is neither
elastic nor purchasable.

**What it means here, concretely.** The desk's load is 7.8 times spikier at peak than on average,
which puts it firmly in the region where the paper's argument applies and elasticity is worth real
money. And the platform this day examined charges in the one unit that does not flex. Those two
sentences together are the actual finding of this day's economics: **the desk has exactly the load
shape that makes elasticity valuable, and the managed option on the table is not elastic in the
dimension that would capture it.**

**The review comment a senior engineer leaves:** *"Compute the peak-to-average before we argue about
platforms. If it is under two, this whole conversation is about convenience and we should say so."*

**The interview question:** *"When is the cloud cheaper?"* The answer that shows experience does not
compare unit prices. It asks for the peak-to-average ratio and the minimum billing granularity, and
observes that a higher per-unit price can still win — which is the paper's actual claim and the part
that is almost always dropped.

## Check yourself

```bash
cd days/day-87-config-not-billed/lab/papers/elasticity
uv run python demo.py; echo "exit: $?"
uv run python demo.py --off; echo "exit: $?"
```

Two arms, one week, one line of difference. Say what `units held` means in each, and why Sunday's
number is the most damning cell in the second table.

Now remove the incident: set `multiplier` to `1` for every day in `load.py`, so Wednesday is an
ordinary day, and run the `--off` arm again. Predict the waste percentage first. It falls from
eighty-one per cent to sixty-four, not to zero — and working out why *before* you read the next
paragraph is the exercise.

The reason is that taking out Wednesday did not flatten the load. The within-day shape is still two
empty slots at each end and a peak in the middle, and the weekend is still nearly empty, so the peak
is still several times the average. **Spikiness is not one thing.** A service can be smoothed at the
weekly scale and violently spiky at the hourly one, and it is the finest scale at which you must
provision that sets the bill. Put the multiplier back, then say what a genuinely flat week would have
to look like.

**Out loud, without scrolling up:** what is the peak-to-average ratio of this desk, why is the
measured saving lower than that ratio, and which of the paper's named obstacles did this day meet in
a requirements file?

**Next:** back to the hub — [`LESSON.md`](../LESSON.md).
