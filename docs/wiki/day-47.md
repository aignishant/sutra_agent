# Day 47 - Persistent sessions — database-backed

IDs closed: ADK-29 · source: `days/day-47-persistent-sessions/`

## Parts

### 1.1 - The book that survives the shutter
`days/day-47-persistent-sessions/parts/01-what-restart-costs/1.1-the-book-under-the-shutter.md` · level `foundation` · ids ADK-29

A session service decides where a conversation is kept, and the only difference between one that survives a restart and one that does not is whether that place is a file on disk or a dictionary in one process's memory.

### 1.2 - A session is four tables
`days/day-47-persistent-sessions/parts/01-what-restart-costs/1.2-a-session-is-four-tables.md` · level `foundation` · ids ADK-29

Once a session is on disk it is an ordinary SQLite database with four tables — app_states, user_states, sessions and events — that any tool can read without ADK in the room.

### 1.3 - Three scopes, three tables
`days/day-47-persistent-sessions/parts/01-what-restart-costs/1.3-three-scopes-three-tables.md` · level `working` · ids ADK-29

The four state prefixes Day 17 taught are not a naming convention: on disk they are three different tables and one deliberate absence, and temp: is absent because absence is what it means.

### 2.1 - The class that is not exported
`days/day-47-persistent-sessions/parts/02-reaching-the-service/2.1-the-class-that-is-not-exported.md` · level `working` · ids ADK-29

SqliteSessionService exists in google-adk==2.7.1, is what the ADK itself uses for local session storage, and is absent from google.adk.sessions.__all__ — so the import every reader tries first raises, and the supported way in is a URI, not a class name.

### 2.2 - The driver you do not have
`days/day-47-persistent-sessions/parts/02-reaching-the-service/2.2-the-driver-you-do-not-have.md` · level `working` · ids ADK-29

DatabaseSessionService is exported, documented and unusable in this repository, because it needs SQLAlchemy and SQLAlchemy is an optional extra that google-adk==2.7.1 does not pull in — which is why this day installs nothing and uses the SQLite service instead.

### 2.3 - The URL that names a file
`days/day-47-persistent-sessions/parts/02-reaching-the-service/2.3-the-url-that-names-a-file.md` · level `working` · ids ADK-29

db_path accepts a plain path or a sqlite: URL, and one slash decides whether the rest is relative to the process's working directory or absolute — so the same string can name two different files and neither of them raises.

### 2.4 - Handing the runner a store
`days/day-47-persistent-sessions/parts/02-reaching-the-service/2.4-handing-the-runner-a-store.md` · level `working` · ids ADK-29

The session service is a constructor argument to the Runner, not a property of the agent, so making a conversation durable is one line at one place — and adk web already made that choice for you, which is why the CLI and your own code disagree about whether sessions survive.

### 2.5 - 🅿️ The lounge you cannot enter
`days/day-47-persistent-sessions/parts/02-reaching-the-service/2.5-the-lounge-you-cannot-enter.md` · level `production` · ids ADK-29

VertexAiSessionService stores sessions in a managed Google Cloud service and is parked for this curriculum, because it needs a billing account — but you should be able to say precisely what it does, what it gives you that a file does not, and what it takes away.

### 3.1 - The ticket torn in two
`days/day-47-persistent-sessions/parts/03-writes-that-survive/3.1-the-ticket-torn-in-two.md` · level `working` · ids ADK-29

One append_event is not one row: it inserts the event, patches the session's state and moves the session's update_time, and the reason it is safe is that all of it happens inside a single transaction that either lands whole or leaves nothing behind.

### 3.2 - What a restart still loses
`days/day-47-persistent-sessions/parts/03-writes-that-survive/3.2-what-a-restart-still-loses.md` · level `production` · ids ADK-29

A durable store saves every event that was committed, and a turn is several events of which only the final one is committed — so a process killed mid-answer leaves a question in the transcript with nothing after it, and no record that anything was in flight.

### 3.3 - 💥 The pragma nobody set
`days/day-47-persistent-sessions/parts/03-writes-that-survive/3.3-the-pragma-nobody-set.md` · level `production` · ids ADK-29

The session service sets one pragma on every connection and it is not journal_mode or busy_timeout — four workers on one file still all succeed, because the driver's default five-second wait absorbs the queueing, and the moment anything holds the file longer than that the service fails at construction with database is locked.

### 4.1 - Refused, not overwritten
`days/day-47-persistent-sessions/parts/04-two-workers/4.1-refused-not-overwritten.md` · level `production` · ids ADK-29

Two workers holding the same session do not lock each other out and do not overwrite each other: the store stamps every session with an update_time, refuses any append whose in-memory copy is older, and raises StaleSessionError at the loser.

### 4.2 - 💥 The read that raises nothing
`days/day-47-persistent-sessions/parts/04-two-workers/4.2-the-read-that-raises-nothing.md` · level `production` · ids ADK-29

The store guards writes and not reads, so a worker that loaded a session, did some work, and then made a decision from the copy in its hand gets no error at all — just last week's answer with this morning's confidence.

### 4.3 - Losing the race on purpose
`days/day-47-persistent-sessions/parts/04-two-workers/4.3-losing-the-race-on-purpose.md` · level `production` · ids ADK-29

A refused write is only recoverable if the retry re-reads first: retrying the same session object sends the same stale timestamp, is refused identically every time, and spends the whole attempt budget proving something you already knew.

### 5.1 - The store the code cannot read
`days/day-47-persistent-sessions/parts/05-shape-and-size/5.1-the-store-the-code-cannot-read.md` · level `working` · ids ADK-29

A durable store is a promise you make to your future self, and the ADK's own schema has already changed once: a file written by an older version makes the constructor raise, and the migration the error names needs a package this repository deliberately does not have.

### 5.2 - 💥 The migration that passed
`days/day-47-persistent-sessions/parts/05-shape-and-size/5.2-the-migration-that-passed.md` · level `production` · ids ADK-29

A migration that checks row counts checks the one thing that cannot go wrong: a thousand conversations came across as a thousand empty rows, every count matched, and the script reported success.

### 5.3 - The session that never ended
`days/day-47-persistent-sessions/parts/05-shape-and-size/5.3-the-session-that-never-ended.md` · level `production` · ids ADK-29

get_session reads and deserialises every event in the conversation, so the cost of one turn grows with everything that has ever been said in it — and the fix is a limit pushed into the SQL, not a slice taken afterwards.

### 6.1 - Delete the session, keep the customer
`days/day-47-persistent-sessions/parts/06-forgetting-on-purpose/6.1-delete-the-session-keep-the-customer.md` · level `production` · ids ADK-29

delete_session removes one conversation and, through a cascade, its turns — and it does not touch the customer's user: state, because user state is defined as outliving conversations, so a loop that deletes every session a person had leaves the person behind.

### 6.2 - 💥 A store in a public repository
`days/day-47-persistent-sessions/parts/06-forgetting-on-purpose/6.2-a-store-in-a-public-repo.md` · level `production` · ids ADK-29

The file this day taught you to create is a plain-text archive of everything customers typed, it appears in your working tree the first time you run anything, and the only thing standing between it and a public repository is two lines in .gitignore that you should verify by asking git rather than by reading them.

### 7.1 - The backup nobody restored
`days/day-47-persistent-sessions/parts/07-in-production/7.1-the-backup-nobody-restored.md` · level `production` · ids ADK-29

Copying the file is not a backup of a live SQLite store — the recent turns are in a side file the copy leaves behind — and the only way to know is to restore it and read a conversation out, which is the step every backup routine skips.

## Papers - read after the parts

### doi:10.1145/289.291 - Principles of transaction-oriented database recovery
`days/day-47-persistent-sessions/papers/01-transaction-oriented-recovery.md`

This is the paper that turned "did the write go through?" from an argument into a question with a defined answer: it named the transaction as the unit of work, gave that unit four properties — atomicity, consistency, isolation, durability — and set out the logging and recovery methods that make the properties true after a crash.

