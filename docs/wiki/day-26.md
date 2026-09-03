# Day 26 - `SkillToolset` — loading skills into ADK

IDs closed: SK-04, SK-05, ADK-24 · source: `days/day-26-loading-skills-into-adk/`

## Parts

### 1.1 - `load_skill_from_dir`: one call, and the whole folder is in memory
`days/day-26-loading-skills-into-adk/parts/01-loading-a-folder/1.1-load-skill-from-dir.md` · level `foundation` · ids SK-04

load_skill_from_dir(path) turns the folder you validated yesterday into a Python object in a single call — and it reads everything in that folder while it does so, including every reference file and the full source of every script.

### 1.2 - The `Skill` object: three fields, and what each one is for
`days/day-26-loading-skills-into-adk/parts/01-loading-a-folder/1.2-the-skill-object.md` · level `foundation` · ids SK-04

A loaded skill has exactly three fields — frontmatter, instructions and resources — and they correspond one for one to the three rungs of progressive disclosure: what is advertised, what is loaded on activation, and what is fetched only if asked for.

### 1.3 - Building a skill in code, and when that is the right call
`days/day-26-loading-skills-into-adk/parts/01-loading-a-folder/1.3-building-a-skill-in-code.md` · level `working` · ids SK-04

models.Skill(frontmatter=..., instructions=..., resources=...) builds the same object the loader builds, without a folder — which is exactly right for a test and exactly wrong for knowledge anybody is meant to review.

### 1.4 - The whole shelf in one call, all or nothing
`days/day-26-loading-skills-into-adk/parts/01-loading-a-folder/1.4-the-whole-shelf.md` · level `working` · ids SK-04

load_skills_from_dir(folder) loads every skill under a folder in one call, list_skills_in_dir loads only their cards — and the first of those two is all or nothing: one unloadable skill and you get no skills at all.

### 2.1 - The 479-token preamble you did not write
`days/day-26-loading-skills-into-adk/parts/02-the-four-tools/2.1-the-preamble-you-did-not-write.md` · level `working` · ids SK-05

Attaching a SkillToolset appends about two thousand characters of instructions to your system prompt — 479 tokens, measured — that you did not write, cannot see in your source, and pay for on every single request for the rest of the conversation.

### 2.2 - `list_skills`: the index is a tool call, not a prompt
`days/day-26-loading-skills-into-adk/parts/02-the-four-tools/2.2-the-index-is-a-tool-call.md` · level `working` · ids SK-05

In ADK 2.7.1 the list of your skills is not put into the system instruction — the model has to call a tool named list_skills to find out what is available, which makes the shelf's cost conditional rather than fixed.

### 2.3 - `load_skill`: what activation actually costs
`days/day-26-loading-skills-into-adk/parts/02-the-four-tools/2.3-what-activation-actually-costs.md` · level `working` · ids SK-05

load_skill returns the body and the entire frontmatter, so activating ticket-triage costs 334 tokens rather than the 184 the body is worth — and 118 of the difference is metadata the model has no use for.

### 2.4 - `load_skill_resource`: the third rung, and the fence around it
`days/day-26-loading-skills-into-adk/parts/02-the-four-tools/2.4-the-third-rung-and-its-fence.md` · level `working` · ids SK-05

load_skill_resource fetches one file out of a skill's own folders and refuses any path that does not begin references/, assets/ or scripts/ — and it counts failed lookups per invocation so that the second miss comes back with an order to stop.

### 2.5 - `run_skill_script`: the rung that ships switched off
`days/day-26-loading-skills-into-adk/parts/02-the-four-tools/2.5-the-rung-that-ships-switched-off.md` · level `production` · ids SK-05

The fourth tool is declared to the model, appears in every skills-enabled agent, and refuses to do anything — NO_CODE_EXECUTOR — until you deliberately attach a code executor or an environment, which is the containment story arriving with the capability instead of after it.

### 3.1 - A toolset, not a tool: wiring `SkillToolset` into an agent
`days/day-26-loading-skills-into-adk/parts/03-wiring-the-toolset/3.1-a-toolset-not-a-tool.md` · level `working` · ids ADK-24

SkillToolset goes into Agent(tools=[...]) as a single entry, and that one entry contributes four tools and rewrites your system instruction — which is why it is a toolset and not a tool.

### 3.2 - `additional_tools`: capability that appears only after activation
`days/day-26-loading-skills-into-adk/parts/03-wiring-the-toolset/3.2-tools-that-appear-after-activation.md` · level `production` · ids ADK-24

Tools passed as additional_tools are not given to the agent — they appear only after a skill has been activated and only if that skill's metadata names them under adk_additional_tools, which means the agent's tool menu grows in the middle of a conversation.

### 3.3 - Activation is a line in session state
`days/day-26-loading-skills-into-adk/parts/03-wiring-the-toolset/3.3-activation-is-a-line-in-state.md` · level `working` · ids ADK-24

load_skill writes _adk_activated_skill_<agent_name> into session state, so "this skill is active" is a durable, readable, per-agent fact — and the same session state also carries two temp: counters you did not put there.

### 4.1 - 💥 One bad folder, and the shelf came back empty
`days/day-26-loading-skills-into-adk/parts/04-failure-lab/4.1-one-bad-folder.md` · level `production` · ids SK-04

load_skills_from_dir raises on the first skill it cannot parse, so one capital letter in one frontmatter takes down every other skill and the agent that was built from them — and the exception does not name the folder.

### 4.2 - 💥 The tool that was passed in and never appeared
`days/day-26-loading-skills-into-adk/parts/04-failure-lab/4.2-the-tool-that-never-appeared.md` · level `production` · ids ADK-24

additional_tools fails silently in three different ways that look identical from outside — never activated, not declared in the skill's metadata, or the name does not match — and none of them produces an error, a warning or a log line.

### 4.3 - 💥 The manual nobody opened
`days/day-26-loading-skills-into-adk/parts/04-failure-lab/4.3-the-manual-nobody-opened.md` · level `production` · ids SK-05

The most expensive failure in this whole day produces no error, no warning and a perfectly good answer: the model never calls list_skills, so the procedure you wrote is never read, and the only evidence is a state key that is not there.

### 5.1 - What a skill really costs, in this client
`days/day-26-loading-skills-into-adk/parts/05-in-production/5.1-what-a-skill-really-costs-here.md` · level `production` · ids SK-05

A skill costs 479 tokens of fixed preamble whether or not anyone uses it, about 83 tokens in the index when somebody asks, and 334 tokens per activated skill on every turn afterwards — but on Sutra's free tier the cost that actually bites is two extra generations out of twenty.

### 5.2 - Experimental means experimental: when the page and the package disagree
`days/day-26-loading-skills-into-adk/parts/05-in-production/5.2-experimental-means-experimental.md` · level `production` · ids ADK-24

The documentation page and the installed package disagree in four places on this feature, the package disagrees with itself in a fifth, and the discipline that makes that survivable is the one Sutra already has: pin the version, name the page and the date, and believe the code.

