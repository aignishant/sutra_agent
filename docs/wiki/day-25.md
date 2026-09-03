# Day 25 - Skills: the open spec — `SKILL.md` anatomy

IDs closed: SK-01, SK-02, SK-03 · source: `days/day-25-skills-the-open-spec/`

## Parts

### 1.1 - A skill is a folder, not a program
`days/day-25-skills-the-open-spec/parts/01-what-a-skill-is/1.1-a-skill-is-a-folder.md` · level `foundation` · ids SK-01

A skill is a directory whose only required member is a file called SKILL.md with two required frontmatter fields — name and description — and everything else, including whether there is any code at all, is optional.

### 1.2 - A folder against a tool
`days/day-25-skills-the-open-spec/parts/01-what-a-skill-is/1.2-a-folder-against-a-tool.md` · level `working` · ids SK-01

A tool is a capability the model may invoke and a skill is a procedure telling it when and in what order — which is why a tool's description is one sentence about a function and a skill's ticket-triage body is 292 tokens of steps, edge cases and a linked table.

### 1.3 - An open spec, and what \"open\" buys
`days/day-25-skills-the-open-spec/parts/01-what-a-skill-is/1.3-an-open-spec.md` · level `working` · ids SK-01

The format is published at agentskills.io/specification with a reference implementation on PyPI, and what that buys is portability in both directions: a skill written for one client works in another, and Sutra can validate a skill without running any client at all.

### 2.1 - Two required fields and nothing else
`days/day-25-skills-the-open-spec/parts/02-the-frontmatter/2.1-two-required-fields.md` · level `foundation` · ids SK-02

The whole required frontmatter is name and description; the format's other four fields — license, compatibility, metadata and allowed-tools — are optional, and a skill with only the two costs 20 tokens at startup against 64 for one carrying all of them.

### 2.2 - `name`: five rules and a directory
`days/day-25-skills-the-open-spec/parts/02-the-frontmatter/2.2-the-name-field.md` · level `working` · ids SK-02

name has five constraints — 1 to 64 characters, lowercase alphanumerics and hyphens only, no leading or trailing hyphen, no consecutive hyphens, and it must match the parent directory name — and the last one is the only rule in the whole format that reaches outside the file.

### 2.3 - `description`: the field the agent actually reads
`days/day-25-skills-the-open-spec/parts/02-the-frontmatter/2.3-the-description-field.md` · level `working` · ids SK-02

description is the only part of a skill the model sees before choosing it, so it has to say what the skill does and when to use it — and measured against five realistic requests, a description written that way overlapped on 7 words where "Helps with tickets." overlapped on 1.

### 2.4 - The four optional fields
`days/day-25-skills-the-open-spec/parts/02-the-frontmatter/2.4-the-optional-fields.md` · level `working` · ids SK-02

license says who may reuse it, compatibility says what it needs, metadata is a free-form map for everything the spec did not define — including the version the format lacks — and allowed-tools is marked experimental, which means a skill that depends on it may behave differently in every client.

### 3.1 - The body is loaded whole
`days/day-25-skills-the-open-spec/parts/03-the-body-and-the-folders/3.1-the-body-is-loaded-whole.md` · level `working` · ids SK-03

Once a skill is activated its entire SKILL.md body enters the context — all 292 tokens of ticket-triage, not the paragraph that was relevant — which is why the spec recommends keeping the file under 500 lines and moving detail into references/.

### 3.2 - `scripts/`, `references/`, `assets/`
`days/day-25-skills-the-open-spec/parts/03-the-body-and-the-folders/3.2-scripts-references-assets.md` · level `working` · ids SK-03

Three conventional subdirectories — code to run, documents to read on demand, and static resources — none of them required, all of them loaded only when the body's links are followed, which is what keeps a skill's activation cost at 292 tokens instead of everything it knows.

### 3.3 - Progressive disclosure: three levels, three budgets
`days/day-25-skills-the-open-spec/parts/03-the-body-and-the-folders/3.3-progressive-disclosure.md` · level `working` · ids SK-03

A skill enters the model's context in three stages with three budgets — metadata (~100 tokens, always), instructions (under ~5,000, on activation) and resources (whatever they cost, when a link is followed) — and ticket-triage measured 64 and 292, a 4.6× ratio that is the whole economics of the format.

### 4.1 - 💥 The skill that never triggered
`days/day-25-skills-the-open-spec/parts/04-failure-lab/4.1-the-skill-that-never-triggered.md` · level `production` · ids SK-02, SK-03

Helps with tickets. is a valid skill description — the validator says Valid skill — and across five realistic requests it overlapped on one word, and that one match was the vaguest request in the set: a folder that is correct, cheap, permanently loaded, and never chosen.

### 4.2 - 💥 The name that did not match
`days/day-25-skills-the-open-spec/parts/04-failure-lab/4.2-the-name-that-did-not-match.md` · level `production` · ids SK-02

One badly-typed name produced three validation failures at once — lowercase, consecutive hyphens, and the directory mismatch — and the value of this failure is precisely that it is loud, immediate and enumerated, which is what [4.1](4.1-the-skill-that-never-triggered.md)'s failure is not.

### 5.1 - Validating before you ship
`days/day-25-skills-the-open-spec/parts/05-in-production/5.1-validating-before-you-ship.md` · level `production` · ids SK-03

agentskills validate exits 1 with a named list of failures and 0 on a valid skill, which is everything a gate needs — and the command is agentskills, not the skills-ref the specification page names, which is what running it rather than trusting it discovered.

### 5.2 - What a skill costs at startup
`days/day-25-skills-the-open-spec/parts/05-in-production/5.2-what-a-skill-costs.md` · level `production` · ids SK-03

Three skills cost 115 tokens of permanent context between them, so a library of two hundred at the same size would cost about 7,600 tokens on every request — paid whether any of them is used, which is the real ceiling on how many skills a system can carry.

