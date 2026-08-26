# 01 · Local-first: Docker, Docker Compose, and Kubernetes on your laptop

> **This is the zero-risk tier.** Nothing in this file ever touches a cloud account, a credit
> card, or a bill. It is also exactly what Sutra's own curriculum does on
> [day_086.md](../days/day_086.md) (Docker Compose) and [day_088.md](../days/day_088.md)
> (`kind` Kubernetes) — this file generalizes the same techniques for any project, with every
> manifest field explained, so you can apply it beyond Sutra.

---

## 1 · Docker and Docker Compose — the one-machine version

Install **Docker Desktop** on Windows (includes Docker Engine, the CLI, and Compose v2):

```powershell
winget install -e --id Docker.DockerDesktop
docker version
docker compose version
```

A minimal, generic Compose file for "a container with an HTTP API":

```yaml
# docker-compose.yml — one service, explained line by line below.
services:
  app:
    build: .                          # build from the Dockerfile in this directory
    image: myagent:dev                # tag the built image so `docker run` can reuse it
    env_file: [.env]                  # secrets/config injected at run time, never baked in
    ports: ["127.0.0.1:8080:8080"]    # host:container — 127.0.0.1 = not reachable from outside this machine
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8080/healthz"]
      interval: 30s
      timeout: 3s
      retries: 3
    restart: unless-stopped            # restart on crash or reboot; not on manual `docker compose down`
```

| Line | Why it matters |
| --- | --- |
| `build: .` | rebuilds from your Dockerfile every time you run `up --build`; drop this and use `image:` alone once you're pulling a pre-built image |
| `env_file: [.env]` | the security-relevant line — see Day 86 §3: anything baked in with `COPY .env .` inside the image is there forever, even if deleted in a later layer |
| `127.0.0.1:8080:8080` | binds only to loopback; without the `127.0.0.1:` prefix, Docker publishes to **all** network interfaces by default, which matters the moment your laptop is on a shared Wi-Fi |
| `healthcheck` | Docker restarts nothing on a failed healthcheck by itself, but `docker ps` shows `(unhealthy)`, which is what you want to notice before a demo, not during one |
| `restart: unless-stopped` | survives a laptop reboot; `docker compose down` (an explicit stop) is still respected |

```powershell
docker compose up --build      # build + start, logs attached
docker compose down            # stop and remove containers (data in a bind-mounted ./data survives)
```

For the full Sutra-specific version — two services, a sidecar, a statefulness audit, and proof
that no secret leaked into the image — see [day_086.md](../days/day_086.md) directly; it is
more detailed than a generic template needs to be.

## 2 · Kubernetes on your laptop: `kind` vs `k3d` vs `minikube`

All three run a **real** Kubernetes API — same objects, same `kubectl`, same manifests you'd
use against GKE/AKS/EKS. They differ in how the cluster itself is implemented:

| | `kind` | `k3d` | `minikube` |
| --- | --- | --- | --- |
| What it runs | Upstream Kubernetes, each node = a Docker container | **k3s** (a lightweight, CNCF-certified Kubernetes distribution), each node = a Docker container | A single VM or container running full Kubernetes |
| Startup speed | Fast | Fastest (k3s is intentionally small) | Slower (heavier default footprint) |
| Built-in local registry | No (manual `kind load`) | **Yes** (`k3d registry create`) — closer to a "real" pull-based workflow | No |
| Multi-node clusters | Yes, easily | Yes, easily | Yes, since v1.10+, more setup |
| Who maintains it | Kubernetes project itself (`kubernetes-sigs`) | Rancher/SUSE community | Kubernetes project (`kubernetes/minikube`) |
| Pick this when | You want the reference implementation the K8s project tests itself with — best for learning the "real" behavior | You want less friction (built-in registry, fastest loop) and don't mind a slightly different Kubernetes distribution underneath | You want a GUI dashboard (`minikube dashboard`) or are following a tutorial written for it |

Sutra's Day 88 uses `kind`. This file's manifests work unchanged on any of the three.

**Verified 2026-08-21:** `kind`'s latest release is **v0.32.0** (released 2026-06-02), defaulting
to Kubernetes **v1.36.1** — `kindest/node:v1.36.1@sha256:3489c7674813ba5d8b1a9977baea8a6e553784dab7b84759d1014dbd78f7ebd5`
(source: `github.com/kubernetes-sigs/kind/releases`). ⚠️ **Note for anyone running Day 88:**
that pre-generated doc (dated 2026-08-20) states "default node image Kubernetes v1.32.0" for
`kind` v0.32.0 — this appears to conflate `kind`'s own version number with a Kubernetes version;
historically the two numbers are unrelated (`kind` v0.26.0 was the release that defaulted to
Kubernetes v1.32.0). Re-run Day 88 §4 Step 1's freshness check and use whatever `kind version`
actually prints on the day you run it, per Principle 14 — don't carry either number forward
without checking.

### Install (Windows)

```powershell
winget install -e --id Kubernetes.kind
winget install -e --id Kubernetes.kubectl
# k3d has no winget package as of this writing — install via the official script under WSL,
# or download the Windows binary directly from github.com/k3d-io/k3d/releases.
# minikube:
winget install -e --id Kubernetes.minikube
```

### Create a cluster

```powershell
# kind
kind create cluster --name demo
kubectl cluster-info --context kind-demo

# k3d (if installed)
k3d cluster create demo

# minikube
minikube start --driver=docker
```

### Load a locally built image (the #1 first-day trap, all three tools)

The cluster's nodes are themselves containers (or a VM) with their *own* image store, separate
from your Docker Desktop's. A locally built image is invisible to the cluster until you load it:

```powershell
docker build -t myagent:dev .
kind load docker-image myagent:dev --name demo        # kind
k3d image import myagent:dev -c demo                   # k3d
minikube image load myagent:dev                        # minikube
```

Skip this step and the pod sits in `ErrImagePull`/`ImagePullBackOff` — Kubernetes tried to pull
`myagent:dev` from a public registry (where it doesn't exist), because nothing told it the image
was already sitting right there on the host.

## 3 · The generic manifest set, explained field by field

**ConfigMap** — non-secret configuration, safe to commit:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  PORT: "8080"
  LOG_LEVEL: "info"
```

**Secret** — created imperatively from your shell environment so the value never touches a file:

```powershell
kubectl create secret generic app-secrets `
  --from-literal=API_KEY=$env:API_KEY
```

⚠️ A Kubernetes `Secret` is **base64-encoded, not encrypted** — anyone who can `kubectl get
secret -o jsonpath` with sufficient RBAC permissions reads it in one command. It is better than
a key in git (not in your history, not in an image layer) and worse than a real secrets
manager. Say that distinction correctly; it is a common interview question.

**Deployment** — the desired-state document for your pods:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app
spec:
  replicas: 1                        # see the note below before ever raising this
  selector:
    matchLabels: {app: app}          # must match template.metadata.labels exactly
  template:
    metadata:
      labels: {app: app}
    spec:
      containers:
        - name: app
          image: myagent:dev
          imagePullPolicy: Never      # loaded by hand (§2) — fail loudly, don't silently pull
          ports: [{containerPort: 8080}]
          envFrom:
            - configMapRef: {name: app-config}
            - secretRef: {name: app-secrets}
          resources:
            requests: {memory: "256Mi", cpu: "100m"}   # what the scheduler reserves
            limits:   {memory: "512Mi", cpu: "500m"}   # the hard ceiling before throttling/OOM-kill
          readinessProbe:             # "should traffic reach this pod right now?"
            httpGet: {path: /readyz, port: 8080}
            initialDelaySeconds: 5
            periodSeconds: 10
          livenessProbe:              # "is this process wedged and needs a restart?"
            httpGet: {path: /healthz, port: 8080}
            initialDelaySeconds: 20
            periodSeconds: 30
```

| Field | What it does | Common mistake |
| --- | --- | --- |
| `replicas: 1` | how many identical pods should exist | raising this for any process holding local state (a SQLite file, an in-memory quota counter) silently duplicates that state — Sutra's Day 86/88 measured this directly: double-spent quota, invisible approvals, a duplicated write |
| `selector` / `template.metadata.labels` | how the Deployment finds "its" pods | these two label sets must match exactly, or the Deployment reports 0/1 ready forever with no obvious error |
| `imagePullPolicy: Never` | never attempt a registry pull | the "loud failure" choice for local clusters — `Always` (the usual production default) is the most common reason a `kind`/`k3d`/`minikube` pod sits in `ErrImagePull` |
| `requests` vs `limits` | requests = what the scheduler guarantees when placing the pod; limits = the ceiling enforced at runtime | setting only `limits` (no `requests`) makes scheduling non-deterministic; setting `requests` too low for a real Python + model-client process is the most common cause of an unexplained OOM-kill |
| `readinessProbe` vs `livenessProbe` | readiness controls whether the **Service** sends traffic here; liveness controls whether Kubernetes **restarts** the container | pointing both at the same trivial "always 200" endpoint means a wedged dependency (e.g., no API key) never gets detected — it needs its own semantics, as Day 85/88 designed with `/readyz` vs `/healthz` |

**Service** — a stable address for the pods, plus (optionally) how to reach them from outside:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: app
spec:
  selector: {app: app}     # routes to any pod with this label — this is the only link to the Deployment
  ports:
    - port: 80              # the Service's own port
      targetPort: 8080       # the container's port
  type: ClusterIP           # default: reachable only inside the cluster
```

| `type` | Reachable from | Use it when |
| --- | --- | --- |
| `ClusterIP` (default) | inside the cluster only | you'll use `kubectl port-forward` to reach it — the right choice for a local cluster with no authentication in front of it (exactly Day 88's reasoning) |
| `NodePort` | `<any-node-IP>:<30000-32767>` | you want a fixed port without port-forwarding, still local-only in practice |
| `LoadBalancer` | a real external IP, on a **cloud** cluster | has nothing to provision on `kind`/`k3d`/`minikube` by default — don't use this locally |

**Ingress** — HTTP routing by hostname/path, only meaningful once an Ingress controller is
installed (`kind`/`k3d`/`minikube` all have a documented way to add one — the official ingress-nginx
project is the common choice for all three):

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: app
  annotations: {nginx.ingress.class: "nginx"}
spec:
  rules:
    - host: app.local.test
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service: {name: app, port: {number: 80}}
```

**HorizontalPodAutoscaler** — scales `replicas` based on observed load (requires the metrics
server, which `minikube addons enable metrics-server` installs; `kind`/`k3d` need it added
manually):

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: app
spec:
  scaleTargetRef: {apiVersion: apps/v1, kind: Deployment, name: app}
  minReplicas: 1
  maxReplicas: 3
  metrics:
    - type: Resource
      resource: {name: cpu, target: {type: Utilization, averageUtilization: 70}}
```

⚠️ Don't reach for this on a stateful, single-instance-only agent (see the `replicas` warning
above) until whatever local state it has moved to something shared (Postgres, not SQLite).

## 4 · Apply, verify, expose

```powershell
kubectl apply -f configmap.yaml -f deployment.yaml -f service.yaml
kubectl get pods -w                          # watch until Running; Ctrl-C
kubectl get pods                              # confirm READY 1/1, RESTARTS 0
kubectl port-forward svc/app 8080:80          # forward to your own laptop only
curl.exe http://127.0.0.1:8080/readyz
```

## 5 · Showing it to someone else, briefly, without deploying anywhere

`kubectl port-forward` and `docker compose`'s port publishing are both **loopback-only by
design** in the templates above — on purpose, since neither has authentication in front of it.
To let a specific other person see a live demo temporarily, use a free tunnel instead of
opening the firewall:

```powershell
# ngrok — free tier: one online tunnel, a random https URL, torn down when you Ctrl-C
ngrok http 8080

# Cloudflare Tunnel — free, no account strictly required for a quick "trycloudflare.com" URL
cloudflared tunnel --url http://localhost:8080
```

Both are covered in more depth, with their real limits, in
[06_other_free_platforms.md](06_other_free_platforms.md) §Tunnels. Close the tunnel the moment
the demo ends — it is the only "public URL" step in this entire file, and it should exist for
minutes, not days.

## 6 · Cleanup

```powershell
kind delete cluster --name demo
# k3d cluster delete demo
# minikube delete
docker compose down
docker system prune           # reclaims disk from unused images/layers — safe, asks before deleting
```

None of this ever cost anything, so cleanup here is about laptop disk space, not a bill — but
the habit is the same one §00 asks you to build for the paid providers.
