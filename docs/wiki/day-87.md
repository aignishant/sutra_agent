# Day 87 - Agent Engine — the config written, not billed

IDs closed: ADK-68 · source: `days/day-87-config-not-billed/`

## Parts

### 1.1 - What you hand over when you hand it over
`days/day-87-config-not-billed/parts/01-what-you-hand-over/1.1-what-you-hand-over.md` · level `foundation` · ids ADK-68

A managed platform is a trade rather than a service: you stop operating a thing and you start depending on one, and the whole of this day is about looking hard at the second half of that sentence before signing, because the first half is the half everybody reads.

### 1.2 - 🅿️ Why this day is parked
`days/day-87-config-not-billed/parts/01-what-you-hand-over/1.2-why-this-day-is-parked.md` · level `foundation` · ids ADK-68

🅿️ means the configuration gets written, reviewed and checked and the deploy command never gets typed — not because deploying is hard, but because the command is the only part of this that costs money and the only part that teaches nothing.

### 1.3 - Reading the deploy surface
`days/day-87-config-not-billed/parts/01-what-you-hand-over/1.3-reading-the-deploy-surface.md` · level `working` · ids ADK-68

adk deploy agent_engine --help is twenty-five options long, nine of them deprecated, and reading it properly answers three questions no tutorial will: which flags are load-bearing, which are already on their way out, and which quietly decide something you would want to decide yourself.

### 2.1 - The config file ADK actually reads
`days/day-87-config-not-billed/parts/02-the-config/2.1-the-config-file-adk-reads.md` · level `working` · ids ADK-68

.agent_engine_config.json, sitting beside the agent, is the artefact this whole day is about: a plain JSON file that ADK loads before it does anything, that flags then override, and that is therefore the one place a deployment decision can be written down, reviewed and disagreed with before it costs anything.

### 2.2 - What the CLI adds that you did not write
`days/day-87-config-not-billed/parts/02-the-config/2.2-what-the-cli-adds.md` · level `working` · ids ADK-68

The config you wrote is a starting point: before it is sent, ADK adds the source packages, an image spec, a framework name, a generated Dockerfile and thirteen published methods — five of which are deprecated the moment they arrive, including the one that runs the agent — so the resource you get is described by a document you have only partly authored.

### 2.3 - Your .env travels
`days/day-87-config-not-billed/parts/02-the-config/2.3-your-env-travels.md` · level `production` · ids ADK-68

The deploy path reads your .env with dotenv_values, which returns every key in it, and assigns the whole dictionary to the config that is uploaded — so the one file this repository has kept out of git since Day 0 is the file that goes to the platform in its entirety, including the database password nobody remembered was in it.

### 3.1 - A config checker that can go red
`days/day-87-config-not-billed/parts/03-checking-locally/3.1-a-config-checker-that-fails.md` · level `working` · ids ADK-68

The config file has no schema and the platform will accept whatever you send it, so the only thing standing between a bad deployment and a good one is a checker you write yourself — and it is worth writing precisely because it runs where the config is written rather than where it is applied.

### 3.2 - The zero-budget lint
`days/day-87-config-not-billed/parts/03-checking-locally/3.2-the-zero-budget-lint.md` · level `working` · ids ADK-68

Two of the four config checks exist only because this repository has a spending rule, and encoding a policy as a lint is what turns "we only use free models" from a thing everybody remembers into a thing the build refuses to break.

### 3.3 - The parked day that quietly required a credit card
`days/day-87-config-not-billed/parts/03-checking-locally/3.3-the-parked-day-that-billed.md` · level `production` · ids ADK-68

A day can claim it needs no billing account and contain a script that does, so the claim needs a check — and the first version of that check flagged eleven things, every one of them a mention in this day's own documentation, which is precisely how a policy check gets switched off.

### 4.1 - Priced in requests, not money
`days/day-87-config-not-billed/parts/04-what-it-costs/4.1-priced-in-requests.md` · level `working` · ids ADK-68

The desk's model traffic is countable and already twelve times the observed free-tier allowance, while the platform's charge is a resource that bills by existing — a unit with no free-tier equivalent — so the honest report has two halves and only one of them fits in this repository's ledger.

### 4.2 - The dependency you inherit
`days/day-87-config-not-billed/parts/04-what-it-costs/4.2-the-dependency-you-inherit.md` · level `production` · ids ADK-68

Deploying to the managed platform adds google-cloud-aiplatform[adk,agent_engines] to your requirements and freezes the ADK version at whatever is installed on the machine that typed the command — two dependencies you did not choose, one of which is decided by a laptop.

### 5.1 - The failure path nobody tests
`days/day-87-config-not-billed/parts/05-in-production/5.1-the-failure-path-nobody-tests.md` · level `production` · ids ADK-68

ADK creates the resource first, configures it second, and deletes it if the second step throws — a correct design with one gap: a deploy that is interrupted between those two calls leaves a created, unconfigured, billing resource that nothing will ever tidy up.

### 5.2 - What you would need before actually deploying
`days/day-87-config-not-billed/parts/05-in-production/5.2-before-you-would-actually-deploy.md` · level `production` · ids ADK-68

Nine things stand between the config this day validated and a deployment somebody could defend, and the useful property of the list is that eight of them are free — the single item that costs money is the command itself, which is why it is the one this curriculum leaves unrun.

## Papers - read after the parts

### doi:10.1145/1721654.1721672 - The bill that follows the load
`days/day-87-config-not-billed/papers/01-the-bill-that-follows-the-load.md`

Paying for what you used beats paying for the worst hour of the week by exactly as much as your load is spiky, and a week of this desk's real shape measures that at eighty-one per cent of the bill.

