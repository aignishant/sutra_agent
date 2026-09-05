# Day 46 - Sessions versus memory — `MemoryService` semantics

IDs closed: ADK-27, ADK-28 · source: `days/day-46-sessions-vs-memory/`

## Parts

### 1.1 - The conversation that ends
`days/day-46-sessions-vs-memory/parts/01-the-line/1.1-the-conversation-that-ends.md` · level `foundation` · ids ADK-27

A session is one conversation and it has an end; memory is whatever you deliberately carry out of it so a different conversation, on a different day, can find it.

### 1.2 - Putting it somewhere, and finding it again
`days/day-46-sessions-vs-memory/parts/01-the-line/1.2-putting-versus-finding.md` · level `foundation` · ids ADK-27

Session state is a place you put a value under a name you chose, so reading it back either returns that value or fails loudly; memory is a place you put something and later have to find it by describing it, and a description can match the wrong thing, several things, or nothing at all.

### 1.3 - Nothing is filed unless somebody files it
`days/day-46-sessions-vs-memory/parts/01-the-line/1.3-nothing-is-filed-unless-you-file-it.md` · level `foundation` · ids ADK-27

Sessions accumulate whether you want them to or not; memory accumulates nothing at all until a line of your code calls add_session_to_memory, and a system with a memory service and no such line behaves exactly like a system with no memory at all.

### 2.1 - Two promises, and two polite refusals
`days/day-46-sessions-vs-memory/parts/02-the-interface/2.1-two-promises-and-two-refusals.md` · level `working` · ids ADK-27

BaseMemoryService makes exactly two things compulsory — add_session_to_memory and search_memory — and offers two more, add_events_to_memory and add_memory, which any implementation may decline with a NotImplementedError that tells you what to call instead.

### 2.2 - The silence that lets you change the brain
`days/day-46-sessions-vs-memory/parts/02-the-interface/2.2-the-silence-that-lets-you-swap.md` · level `working` · ids ADK-27

BaseMemoryService never says how matching works, and that omission is the most valuable thing about it: the same calling code runs unchanged over a service that compares words and one that compares meanings, and the quality of what comes back changes completely.

### 2.3 - What comes back is not a session
`days/day-46-sessions-vs-memory/parts/02-the-interface/2.3-what-comes-back-is-not-a-session.md` · level `working` · ids ADK-27

A search returns MemoryEntry objects — some content, and optionally who said it, when, an id and some metadata — and it deliberately does not return the session those words came from, so the ticket number, the state and the rest of the conversation are all gone unless they happened to be in the text.

### 2.4 - The bucket is a person, not a conversation
`days/day-46-sessions-vs-memory/parts/02-the-interface/2.4-the-bucket-is-a-person.md` · level `working` · ids ADK-27

Every memory is filed under the pair (app_name, user_id) and can be found only by a search using that same pair — so the single most consequential decision in this whole day is who you decide the user is.

### 3.1 - The service rides the runner, not the agent
`days/day-46-sessions-vs-memory/parts/03-three-wires/3.1-the-service-rides-the-runner.md` · level `working` · ids ADK-28

memory_service= is an argument to Runner, not to Agent — so the agent stays portable and the deployment decides which store stands behind it, and an agent carrying a memory tool with no service on its runner raises ValueError: Memory service is not available. from inside the framework.

### 3.2 - The line where it crosses
`days/day-46-sessions-vs-memory/parts/03-three-wires/3.2-the-line-where-it-crosses.md` · level `working` · ids ADK-28

add_session_to_memory is the single line where a conversation becomes something a later conversation can find, it may be called more than once on the same session, and inside a run the same act is await callback_context.add_session_to_memory().

### 3.3 - The tool the model may call
`days/day-46-sessions-vs-memory/parts/03-three-wires/3.3-the-tool-the-model-may-call.md` · level `working` · ids ADK-28

load_memory is an ordinary tool the model decides to call, with a query it writes itself — so nothing is retrieved unless the model asks, the ask is visible in the event stream, and the tool quietly adds a paragraph to your system instruction on every request whether it is used or not.

### 3.4 - The past pushed in before the turn
`days/day-46-sessions-vs-memory/parts/03-three-wires/3.4-the-past-pushed-in-before-the-turn.md` · level `working` · ids ADK-28

preload_memory searches the store with the user's raw message and injects the results into the request before every turn, so nothing depends on the model deciding to look — and nothing appears in the transcript, nothing is logged that you will see, and a search that raises is swallowed.

### 4.1 - Pricing both, in tokens
`days/day-46-sessions-vs-memory/parts/04-the-choice/4.1-pricing-both-in-tokens.md` · level `production` · ids ADK-28

Measured over one ten-turn conversation, preload_memory costs 1,898 tokens and ten model requests where load_memory costs 3,130 tokens and eleven requests for a single lookup, and 7,927 tokens and fifteen requests for five — because a tool result is written into the transcript and re-sent on every later turn, while a preloaded block is transient.

### 4.2 - Sutra's memory policy
`days/day-46-sessions-vs-memory/parts/04-the-choice/4.2-sutras-memory-policy.md` · level `production` · ids ADK-28

Sutra chooses load_memory even though [4.1](4.1-pricing-both-in-tokens.md) measured it as the more expensive option, because a retrieval you cannot see is a retrieval you cannot debug — and the policy is written as five checks with an exit code so that the code cannot drift away from it in silence.

### 5.1 - 💥 The past that matched on nothing
`days/day-46-sessions-vs-memory/parts/05-failure-lab/5.1-the-past-that-matched-on-nothing.md` · level `production` · ids ADK-28

A query written the way people actually write questions matched all four filed tickets, the first of them was the wrong one, and an agent reading memories[0] told the customer to apply KB-201 when the right article was KB-104 — with no error, no warning and no way to tell from the result that anything had gone wrong.

### 5.2 - 💥 The store that was never a store
`days/day-46-sessions-vs-memory/parts/05-failure-lab/5.2-the-store-that-was-never-a-store.md` · level `production` · ids ADK-28

InMemoryMemoryService keeps everything in one Python dictionary on one object inside one process, so the afternoon where five filed cases returned ten memories becomes a Monday where the same search returns zero — with no error, no warning and no log line, because nothing failed.

### 5.3 - 💥 Another customer's memory
`days/day-46-sessions-vs-memory/parts/05-failure-lab/5.3-another-customers-memory.md` · level `production` · ids ADK-28

Filing every case under the support agent's id puts two companies' tickets in one bucket, so a search on Blue Peak's ticket returns Northwind's billing address first — correctly filed, correctly retrieved, by code with no bug in it except one string.

### 5.4 - 💥 The store that outgrew its value
`days/day-46-sessions-vs-memory/parts/05-failure-lab/5.4-the-store-that-outgrew-its-value.md` · level `production` · ids ADK-28

Filing more cases makes the desk worse, not better: at five hundred filed cases one question matches all five hundred, injects 48,175 characters — 10,588 tokens — and the chance that the case you needed is the one being read is 0.2%, while a cap of three holds the same store at 102 tokens forever.

### 6.1 - Eight things that must stay true
`days/day-46-sessions-vs-memory/parts/06-in-production/6.1-eight-things-that-must-stay-true.md` · level `production` · ids ADK-27, ADK-28

Everything this day taught about MemoryService is behaviour you observed rather than behaviour anybody promised you, so it goes into a script of eight assertions that runs in six thousandths of a second with no key, no network and no model — and that will go red on the upgrade that changes any of it.

### 6.2 - 🅿️ The two services we park
`days/day-46-sessions-vs-memory/parts/06-in-production/6.2-the-two-services-we-park.md` · level `production` · ids ADK-27

VertexAiMemoryBankService and VertexAiRagMemoryService are the two implementations a real deployment would actually use, they need a Google Cloud billing account, and on this machine they refuse at construction with ImportError: The 'google-cloud-aiplatform' package is required — so Sutra reads their constructor signatures, writes down what each one would buy, and builds neither.

## Papers - read after the parts

### arXiv:2304.03442 - Generative Agents: Interactive Simulacra of Human Behavior
`days/day-46-sessions-vs-memory/papers/01-generative-agents.md`

An agent that remembers everything and an agent that remembers nothing fail in the same way, and this paper's answer is that retrieval must be scored on more than similarity — recency, importance and relevance summed together — plus a second store of conclusions the agent drew from its own observations, kept separate from the raw record of what happened.

