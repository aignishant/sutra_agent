# Day 08 - Sessions, runs & in-memory services — the conversation gets an address

IDs closed: ADK-06, ADK-07 · source: `days/day-08-sessions-and-services/`

## Parts

### 1.1 - A conversation with an address
`days/day-08-sessions-and-services/parts/01-the-session/1.1-a-conversation-with-an-address.md` · level `foundation` · ids ADK-06

A session is one conversation, held as an ordered list of events plus a small dictionary of stored values, and the thing that makes it useful is that it has an address you can come back to.

### 1.2 - Three parts to one key
`days/day-08-sessions-and-services/parts/01-the-session/1.2-three-parts-to-one-key.md` · level `working` · ids ADK-06

A session is found by app_name + user_id + session_id together, so getting any one of the three wrong returns None rather than an error — and the day you find this out is usually the day you have been debugging the wrong thing for an hour.

### 1.3 - The register and the key board
`days/day-08-sessions-and-services/parts/01-the-session/1.3-the-register-and-the-key-board.md` · level `working` · ids ADK-06

events is the history — everything that happened, in order, never edited — and state is what is true now, a small dictionary rebuilt from that history, and confusing the two is how people end up storing a conversation in a dictionary or a fact in a transcript.

### 1.4 - Minted, or chosen
`days/day-08-sessions-and-services/parts/01-the-session/1.4-minted-or-chosen.md` · level `working` · ids ADK-06

Leave session_id off and the service mints a unique one; pass your own and you take responsibility for it being unique — which is occasionally exactly what you want and is otherwise an AlreadyExistsError waiting for a busy afternoon.

### 2.1 - One dish from one recipe
`days/day-08-sessions-and-services/parts/02-the-run/2.1-one-dish-from-one-recipe.md` · level `foundation` · ids ADK-06

A run — ADK also calls it an invocation — is everything that happens between one user message and the agent being finished with it, however many model calls, tool calls and events that takes, and every event in it shares one invocation_id.

### 2.2 - The complaint book
`days/day-08-sessions-and-services/parts/02-the-run/2.2-the-complaint-book.md` · level `working` · ids ADK-06

The runner writes the user's message into the session before your agent runs, and does not hand it to your loop — so a session always has one more event than your loop counted, and a run that crashed instantly still leaves a record that somebody asked something.

### 2.3 - A journey and a pass
`days/day-08-sessions-and-services/parts/02-the-run/2.3-a-journey-and-a-pass.md` · level `production` · ids ADK-06

A session outlives every run inside it and only ever grows, so the two questions that decide whether an agent stays affordable are what ends a session and how much of it you actually load — and ADK gives you GetSessionConfig for the second and nothing at all for the first.

### 3.1 - The tap and the pipe
`days/day-08-sessions-and-services/parts/03-the-services/3.1-the-tap-and-the-pipe.md` · level `foundation` · ids ADK-07

A service in ADK is an interface — a list of methods with no opinion about where the data goes — and every "in-memory" thing you have used today is one implementation of one, which is what lets Day 86 swap a dictionary for a database without your agent noticing.

### 3.2 - Three drawers deep
`days/day-08-sessions-and-services/parts/03-the-services/3.2-three-drawers-deep.md` · level `working` · ids ADK-07

InMemorySessionService is three nested dictionaries keyed by app, then user, then session id — it hands you a copy when you read, and it looks the session up by its address when you write, which is why writing to a session it has never heard of produces a log warning and nothing else.

### 3.3 - Ctrl+F is not understanding
`days/day-08-sessions-and-services/parts/03-the-services/3.3-ctrl-f-is-not-understanding.md` · level `working` · ids ADK-07

InMemoryMemoryService finds a past conversation by matching words, not meaning — its own docstring says so — which makes it a perfectly good way to learn the shape of a memory service and a completely inadequate way to answer "has anything like this happened before?"

### 3.4 - The cloakroom, and the one you were not given
`days/day-08-sessions-and-services/parts/03-the-services/3.4-the-cloakroom-and-the-one-you-were-not-given.md` · level `working` · ids ADK-07

InMemoryArtifactService is the place files live between turns — versioned, addressed like a session and namespaced by user: when they should outlive one — and the credential service is the fourth one ADK has and does not give you by default, which is a decision rather than an oversight.

### 3.5 - The furnished flat
`days/day-08-sessions-and-services/parts/03-the-services/3.5-the-furnished-flat.md` · level `production` · ids ADK-07

InMemoryRunner fills in three services and an app name so you can run an agent in one line — which is exactly right for a test and exactly wrong for anything that has to be found again, because the app name it chooses is "InMemoryRunner" and you did not choose it.

### 4.1 - The tab you did not save
`days/day-08-sessions-and-services/parts/04-what-in-memory-means/4.1-the-tab-you-did-not-save.md` · level `production` · ids ADK-07

"In memory" means in this process, so every session, artifact and memory entry disappears the moment the process ends — and a process ends far more often than beginners expect, including on every deploy.

### 4.2 - Two counters, two notebooks
`days/day-08-sessions-and-services/parts/04-what-in-memory-means/4.2-two-counters-two-notebooks.md` · level `production` · ids ADK-07

Two processes of the same program have two separate in-memory stores, so a user served by one is a stranger to the other — and unlike losing a session on restart, this failure is intermittent, which makes it much harder to see.

### 4.3 - 🅿️ The shop that bought a computer
`days/day-08-sessions-and-services/parts/04-what-in-memory-means/4.3-the-shop-that-bought-a-computer.md` · level `production` · ids ADK-07

The three persistent session services — a file, a database, a cloud service — all satisfy the same interface, so the swap is one line; what is not one line is everything the interface never promised, which is locking, latency, migrations and a whole new class of error.

### 5.1 - 💥 The name called in the waiting room
`days/day-08-sessions-and-services/parts/05-failure-lab/5.1-the-name-called-in-the-waiting-room.md` · level `production` · ids ADK-06, ADK-07

Today's deliberate failure is one bug — an address that does not match — wearing three different faces: an exception, a None, and a log line nobody reads, and the three are worth producing on purpose because you will only recognise the last two if you have seen them.

