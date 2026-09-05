# Day 39 - Database tools — Toolbox versus hand-written

IDs closed: MCP-15, ADK-25, ADK-78 · source: `days/day-39-database-tools/`

## Parts

### 1.1 - The numbers on the back of a bill
`days/day-39-database-tools/parts/01-the-archive/1.1-the-numbers-on-the-back-of-a-bill.md` · level `foundation` · ids MCP-15

Sutra's ticket archive has been a Python dictionary since Day 3, and a dictionary stops being an archive the moment somebody else needs to write to it, the moment it outgrows one screen, and the moment losing the process means losing the data.

### 1.2 - One file, one engine
`days/day-39-database-tools/parts/01-the-archive/1.2-one-file-one-engine.md` · level `foundation` · ids MCP-15

SQLite is a complete SQL engine that ships inside Python's standard library and stores an entire database in one ordinary file, so Sutra gets a real query language, real constraints and real transactions without installing anything, running a server, or opening a billing account.

### 1.3 - A door, not a hallway
`days/day-39-database-tools/parts/01-the-archive/1.3-a-door-not-a-hallway.md` · level `working` · ids MCP-15

A database tool should expose one intent with typed arguments — search_tickets(term, limit) — and never a general "run this SQL" hallway, because the tool's signature is the only part of the arrangement a prompt cannot argue with.

### 2.1 - 💥 The argument that became syntax
`days/day-39-database-tools/parts/02-the-five-brakes/2.1-the-argument-that-became-syntax.md` · level `working` · ids MCP-15

If a tool argument is pasted into a SQL string, the caller is no longer supplying a value — it is supplying part of the statement — and the first thing that buys an attacker is not a deleted table but a silently wrong answer that walks straight past your filters.

### 2.2 - The connection that cannot write
`days/day-39-database-tools/parts/02-the-five-brakes/2.2-the-connection-that-cannot-write.md` · level `working` · ids MCP-15

Opening the archive with file:...?mode=ro makes every write impossible at the engine level, which means the refusal comes from the database rather than from your code, your prompt or anybody's good intentions.

### 2.3 - The statements you allow
`days/day-39-database-tools/parts/02-the-five-brakes/2.3-the-statements-you-allow.md` · level `working` · ids MCP-15

SQLite lets you install a callback the engine consults while compiling every statement, so you can name the small set of operations a read tool is allowed to perform and have everything else — including reads of files you never mentioned — refused before a single row is touched.

### 2.4 - A ceiling the caller cannot raise
`days/day-39-database-tools/parts/02-the-five-brakes/2.4-a-ceiling-the-caller-cannot-raise.md` · level `working` · ids MCP-15

The row limit must be applied in the SQL the server owns and clamped in the server's own code, so that a caller asking for a thousand rows gets your maximum and a correct answer rather than an argument about it.

### 2.5 - The query that never ends
`days/day-39-database-tools/parts/02-the-five-brakes/2.5-the-query-that-never-ends.md` · level `working` · ids MCP-15

A row limit caps the answer and not the work, so a statement that has to look at a billion combinations before returning five rows needs a separate brake — a budget the engine checks as it runs, which aborts the statement rather than waiting for it.

### 2.6 - Which brakes actually held
`days/day-39-database-tools/parts/02-the-five-brakes/2.6-which-brakes-actually-held.md` · level `production` · ids MCP-15

Each of the five brakes was handed the attack it exists to stop, and all five held — while the thing most teams reach for first, the sentence "this tool is read-only" in the description, stopped nothing at all.

### 3.1 - What the model is told
`days/day-39-database-tools/parts/03-the-adk-side/3.1-what-the-model-is-told.md` · level `working` · ids ADK-25

ADK builds the tool declaration from your function's name, signature and docstring, so the docstring is not documentation about the tool — it is the tool, as far as the model is concerned, and a table it does not describe is a table the model will guess about.

### 3.2 - A database server through McpToolset
`days/day-39-database-tools/parts/03-the-adk-side/3.2-a-database-server-through-mcptoolset.md` · level `working` · ids ADK-25

McpToolset is the ADK object that turns "a database MCP server" into tools an agent can use, and building one starts no process and opens no connection — it is a launch spec plus a filter, which means the decision about what a database server may expose is inspectable before anything runs.

### 4.1 - 🅿️ The server you did not write
`days/day-39-database-tools/parts/04-toolbox-parked/4.1-the-server-you-did-not-write.md` · level `working` · ids ADK-25

MCP Toolbox for Databases is a single binary that turns a database into an MCP server from a YAML file, in two modes — a prebuilt recipe that hands you execute_sql, or a config where you declare each tool's statement yourself — and Sutra parks it because every required step in this curriculum must run with no installed server and no account.

### 4.2 - Who writes the SQL
`days/day-39-database-tools/parts/04-toolbox-parked/4.2-who-writes-the-sql.md` · level `production` · ids ADK-25, MCP-15

The real question is not "generated tools or hand-written tools" but who authors the statement and when — a statement written by you and reviewed in a diff, or a statement written by a model at request time — and every difference that matters follows from that one.

### 4.3 - 🅿️ The extras map
`days/day-39-database-tools/parts/04-toolbox-parked/4.3-the-extras-map.md` · level `production` · ids ADK-78

ADK ships twenty-three optional dependency bundles called extras, each one a doorway to a capability the framework has grown, and the professional skill is being able to place every one of them on a map without having installed any of them.

### 5.1 - 💥 Forty thousand rows
`days/day-39-database-tools/parts/05-failure-lab/5.1-forty-thousand-rows.md` · level `production` · ids MCP-15

A correct, safe, injection-proof, read-only query with no LIMIT returned a result 173% the size of the model's entire input window, which means the tool worked perfectly and the request could not be sent.

### 5.2 - 💥 The label that stayed
`days/day-39-database-tools/parts/05-failure-lab/5.2-the-label-that-stayed.md` · level `production` · ids MCP-15, ADK-25

A tool's description is an interface, so renaming a column is an interface change — and because nothing in the toolchain compares the description against the schema, the tool keeps promising a column that no longer exists until a query fails at runtime.

### 5.3 - 💥 The write with no undo
`days/day-39-database-tools/parts/05-failure-lab/5.3-the-write-with-no-undo.md` · level `production` · ids MCP-15

A write tool that is correct, parameterised and read-only-proof can still be uncallable-back: one wrong argument closed 203 tickets when 200 were wanted, and nothing in the system could say which three were the mistake.

### 6.1 - The connection you do not hold
`days/day-39-database-tools/parts/06-in-production/6.1-the-connection-you-do-not-hold.md` · level `production` · ids MCP-15

A database tool opens its connection inside the call and closes it before returning, because a connection kept between calls is state living in one process — and on SQLite a read connection with an open transaction blocks every writer with database is locked.

### 6.2 - When SQLite is not the database
`days/day-39-database-tools/parts/06-in-production/6.2-when-sqlite-is-not-the-database.md` · level `production` · ids MCP-15, ADK-25

Moving the archive to a server database changes the connection helper and three of the five brakes, and leaves every SELECT untouched — which is the whole practical payoff of having written declarative queries against named relations instead of code that knows where the data sits.

### 6.3 - The audit that reads your file
`days/day-39-database-tools/parts/06-in-production/6.3-the-audit-that-reads-your-file.md` · level `production` · ids MCP-15

The day's eval opens sutra_mcp/db_tools.py, looks for each of the five brakes by its source shape, and parses the file to prove no statement is built by string formatting — so it is red until you write the tools and stays red for every brake you leave out.

## Papers - read after the parts

### doi:10.1145/362384.362685 - A Relational Model of Data for Large Shared Data Banks
`days/day-39-database-tools/papers/01-relational-model.md`

It argued that a program should ask questions about named relations with named attributes, never about how the data is physically arranged — so that the storage can be reorganised underneath a working program without breaking it.

