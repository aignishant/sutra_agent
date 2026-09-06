# Day 85 - The API surface — api_server, FastAPI endpoints

IDs closed: ADK-64, ADK-65 · source: `days/day-85-the-api-surface/`

## Parts

### 1.1 - A desk with a street address
`days/day-85-the-api-surface/parts/01-the-routing-table/1.1-a-desk-with-a-street-address.md` · level `foundation` · ids ADK-64

adk api_server turns the agent you have been running from a terminal into twenty-seven HTTP routes, and the moment it does, the desk stops being a program you run and becomes a service other people can call — which changes almost nothing about the agent and everything about what can go wrong.

### 1.2 - What the paths say about the design
`days/day-85-the-api-surface/parts/01-the-routing-table/1.2-what-the-paths-say-about-the-design.md` · level `foundation` · ids ADK-64

Almost every route is shaped /apps/{app_name}/users/{user_id}/sessions/{session_id}/..., which says three true things about how ADK organises state — and one dangerous thing, which is that the caller's identity is a segment of the URL they type themselves.

### 1.3 - Two ways to start it, and one is safer
`days/day-85-the-api-surface/parts/01-the-routing-table/1.3-two-ways-to-start-it.md` · level `working` · ids ADK-64, ADK-65

adk api_server and get_fast_api_app build the same twenty-seven routes, and the command passes two arguments the factory defaults to nothing — so the supported way to start the server has a protection on that the embeddable way silently does not.

### 2.1 - A client with no socket
`days/day-85-the-api-surface/parts/02-exercising-it-free/2.1-a-client-with-no-socket.md` · level `working` · ids ADK-65

httpx.ASGITransport(app=app) calls the application object the way a web server would — through every middleware, every dependency and every exception handler — without binding a port, so an HTTP test is as cheap and as deterministic as a function call and still exercises the real HTTP path.

### 2.2 - Which endpoints cost nothing
`days/day-85-the-api-surface/parts/02-exercising-it-free/2.2-which-endpoints-cost-nothing.md` · level `working` · ids ADK-65

Twenty-four of the twenty-seven routes answer from the process's own state and cost nothing to call; three hand the turn to an agent and spend provider quota — and the three refuse a bad session id before they spend anything, which is the difference between a typo and a bill.

### 2.3 - The endpoint that sends a stream
`days/day-85-the-api-surface/parts/02-exercising-it-free/2.3-the-endpoint-that-sends-a-stream.md` · level `working` · ids ADK-65

/run_sse declares application/json in the generated schema and actually sends text/event-stream, so a client built from the document will wait for one object that never arrives — and /run_live is a WebSocket, which is not in the document at all.

### 3.1 - One field, two types
`days/day-85-the-api-surface/parts/03-when-it-refuses/3.1-one-field-two-types.md` · level `working` · ids ADK-65

Every refusal from this server has a field called detail, and on a 404 it is a string while on a 422 it is a list — so a client that read one refusal and wrote a handler gets AttributeError: 'list' object has no attribute 'lower' the first time somebody sends a bad body.

### 3.2 - The 404 that reads out the disk
`days/day-85-the-api-surface/parts/03-when-it-refuses/3.2-the-404-that-reads-out-the-disk.md` · level `production` · ids ADK-65

Ask this server for an app that does not exist and the refusal comes back with the absolute filesystem path it looked in, account name included — a hundred and sixty-five characters where about twenty-six were needed, on a route that requires no credential.

### 3.3 - An error with a handle on it
`days/day-85-the-api-surface/parts/03-when-it-refuses/3.3-an-error-with-a-handle-on-it.md` · level `working` · ids ADK-65

Both of section 3's findings have the same fix: decide the error body deliberately, give every kind of refusal a stable identifier a client can branch on, and put the prose in a field that is allowed to change — which is a standard, not an invention.

### 4.1 - The caller says who they are
`days/day-85-the-api-surface/parts/04-blast-radius/4.1-the-caller-says-who-they-are.md` · level `production` · ids ADK-65

mallory listed, read and deleted alice's session by typing alice into the URL — three requests, three 200s, no credential — because {user_id} is a path parameter, and the library's own help text says so before you start.

### 4.2 - Which pages may call it
`days/day-85-the-api-surface/parts/04-blast-radius/4.2-which-pages-may-call-it.md` · level `working` · ids ADK-65

With no allow_origins the browser refuses a page on another origin with a 403 before your code sees it; set it to [""] for convenience and any web page anybody visits can drive every route on this server, which part 4.1 established needs no credential.

### 4.3 - The guard in the box
`days/day-85-the-api-surface/parts/04-blast-radius/4.3-the-guard-in-the-box.md` · level `production` · ids ADK-64

ADK ships a guard that rejects a request addressed to a host this server is not, which is what stops a web page from reaching your loopback API — and it is off unless you pass bind_host, which the command does and an embedder must remember to.

### 5.1 - Health is not readiness
`days/day-85-the-api-surface/parts/05-in-production/5.1-health-is-not-readiness.md` · level `production` · ids ADK-64

GET /health returns {"status":"ok"} from a two-line function that checks nothing, which is exactly right for is this process alive and useless for may I send it traffic — and the second question is the one a load balancer is actually asking.

### 5.2 - What a real API surface adds
`days/day-85-the-api-surface/parts/05-in-production/5.2-what-a-real-api-surface-adds.md` · level `production` · ids ADK-64, ADK-65

The factory gives you twenty-seven working routes and none of the eight things that make a service safe to expose — and two of the eight are single lines that this day has already measured the cost of omitting.

## Papers - read after the parts

### doi:10.17487/RFC9457 - An error a client can act on
`days/day-85-the-api-surface/papers/01-an-error-a-client-can-act-on.md`

HTTP has a rich vocabulary for what went wrong at the protocol level and nothing at all for what went wrong in your application, so every API invented its own error body — and this document is the field's agreement to stop, in one page of normative text.

