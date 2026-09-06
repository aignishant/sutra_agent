# Day 86 - Containerize — Cloud-Run-shaped, locally

IDs closed: ADK-66, OPS-17, ADK-67 · source: `days/day-86-cloud-run-shaped/`

## Parts

### 1.1 - An image is a recipe a stranger can follow
`days/day-86-cloud-run-shaped/parts/01-what-a-container-promises/1.1-an-image-is-a-recipe.md` · level `foundation` · ids ADK-66

Everything the desk needs to run is currently an unwritten assumption about one laptop — a particular Python, a particular lockfile, a file called .env in a particular folder — and an image is that list written down so completely that a machine which has never seen the project can reproduce it.

### 1.2 - A layer is written once and kept forever
`days/day-86-cloud-run-shaped/parts/01-what-a-container-promises/1.2-a-layer-is-written-once.md` · level `foundation` · ids ADK-66

Each instruction in a Dockerfile produces a layer that is stored, addressed by its contents and never edited — which is why the ordering of instructions decides how fast a rebuild is, and why deleting a file in a later instruction does not remove it from the image.

### 1.3 - The platform chooses the port and the address
`days/day-86-cloud-run-shaped/parts/01-what-a-container-promises/1.3-the-platform-chooses-the-port.md` · level `foundation` · ids ADK-66

A container does not pick where it listens: the platform hands it a port in an environment variable and expects it to bind every interface — so --port $PORT and --host 0.0.0.0 are not style choices, and the second one is the exact opposite of what is correct on a laptop.

### 2.1 - Writing the Dockerfile
`days/day-86-cloud-run-shaped/parts/02-the-image-contract/2.1-writing-the-dockerfile.md` · level `working` · ids ADK-66

The file is twenty lines and every one of them is a decision somebody will otherwise have to remember — so it is written in the order things change, from the base image that changes yearly to the source that changes hourly, with the user dropped from root exactly once.

### 2.2 - Eight properties, checked without a daemon
`days/day-86-cloud-run-shaped/parts/02-the-image-contract/2.2-eight-properties-checked.md` · level `working` · ids ADK-66, OPS-17

Eight of the things a deployable image has to get right are visible in the text of the Dockerfile and the compose file, so they can be checked on a machine with no container runtime at all — and a Dockerfile written quickly gets one of the eight.

### 2.3 - The build context nobody looked at
`days/day-86-cloud-run-shaped/parts/02-the-image-contract/2.3-the-build-context-nobody-looked-at.md` · level `production` · ids ADK-67, OPS-17

💥 Without a .dockerignore the build would send 414,219,769 bytes across 22,020 files to be packaged, including this repository's real .env and .git/config; with one it sends 40 files and 2,207,035 bytes — and the difference is not a build-time optimisation, it is whether a live key ends up in an immutable layer.

### 3.1 - An app that refuses to start
`days/day-86-cloud-run-shaped/parts/03-config-from-outside/3.1-an-app-that-refuses-to-start.md` · level `working` · ids ADK-67

Configuration that is missing should stop the process at import, naming the setting, rather than producing a working-looking service that fails on the first request that needs it — and the difference is measurable: a complete environment exits 0 and an incomplete one exits 1 with ConfigError: missing required environment: SUTRA_API_KEY.

### 3.2 - Three ways a secret gets in, one of them acceptable
`days/day-86-cloud-run-shaped/parts/03-config-from-outside/3.2-three-ways-a-secret-gets-in.md` · level `working` · ids ADK-67

A key can be baked into a layer, passed as a build argument, or injected at run time; the first two put it in an artefact that gets copied, and only the third keeps it in the part of the system that is never rebuilt and never pushed.

### 3.3 - compose.yaml is the shape, not the tool
`days/day-86-cloud-run-shaped/parts/03-config-from-outside/3.3-compose-is-the-shape.md` · level `working` · ids OPS-17

The compose file is not a way to run containers on a laptop; it is the first written statement that Sutra is a system of processes rather than a program — two services with different lifecycles and different privileges, one shared volume, and one number that is a confession.

### 4.1 - Alive and able to work are different questions
`days/day-86-cloud-run-shaped/parts/04-health-checks/4.1-alive-and-able-to-work.md` · level `working` · ids OPS-17

Is the process running and can the process do its job have different answers, different consequences and different endpoints — /healthz decides whether to restart a container and /readyz decides whether to send it traffic, and pointing both at the same code throws away the distinction.

### 4.2 - The health check that only watched the process
`days/day-86-cloud-run-shaped/parts/04-health-checks/4.2-the-check-that-only-watched-the-process.md` · level `production` · ids OPS-17

💥 The dependency is deleted, the service can do no work at all, and /healthz answers 200 ok — so a run that asks only the liveness endpoint reports a healthy service and exits 0, while the readiness endpoint two lines away is saying 503 quota_ledger_missing.

### 5.1 - The statefulness audit
`days/day-86-cloud-run-shaped/parts/05-the-word-stateless/5.1-the-statefulness-audit.md` · level `working` · ids ADK-66, OPS-17

A container is a process that will be replaced without notice, so the only useful question about this system's state is which parts survive replacement — and the answer, measured by killing it and starting it again, is one of two: the ledger file comes back and the session store does not.

### 5.2 - Two replicas, and only one failure is about replication
`days/day-86-cloud-run-shaped/parts/05-the-word-stateless/5.2-two-replicas-one-failure.md` · level `production` · ids ADK-66, OPS-17

💥 Scale to two and two things break — a session created on one replica returns 404 on the other, and twenty units of spend leave a shared ledger recording six — but only the first is caused by the second replica, and finding that out is what the ablation is for.

### 5.3 - What a real deployment adds
`days/day-86-cloud-run-shaped/parts/05-the-word-stateless/5.3-what-a-real-deployment-adds.md` · level `production` · ids OPS-17

The lab wrote a correct image and proved two real defects without ever building anything, and the distance between that and a deployment is nine items — the first three of which are free, one of which is an installation, and two of which are the reason the replica count is one.

## Papers - read after the parts

### doi:10.1109/ISPASS.2015.7095802 - What isolation costs
`days/day-86-cloud-run-shaped/papers/01-what-isolation-costs.md`

Isolation used to be a thing you bought and paid for in performance, and this paper is the measurement that showed the price had fallen to almost nothing for computation while remaining real for anything that crosses the boundary — which is why the unit of deployment became an image rather than a machine.

