# Day 27 - Authoring Sutra's first skills

IDs closed: SK-06, SK-07, SK-08 · source: `days/day-27-authoring-first-skills/`

## Parts

### 1.1 - Where the procedure lives now, and why that is a problem
`days/day-27-authoring-first-skills/parts/01-extraction/1.1-where-the-procedure-lives-now.md` · level `foundation` · ids SK-06

Sutra's triage procedure exists, it works, and it is written down nowhere: it is spread across an instruction string, a tool docstring, a test, and the head of the person who has been running the loop by hand since Day 3.

### 1.2 - One job, four words: choosing a skill's scope
`days/day-27-authoring-first-skills/parts/01-extraction/1.2-one-job-four-words.md` · level `working` · ids SK-06

A skill's scope is decided by whether you can name it in four words or fewer without using "and" — and Sutra's inventory turns out to be two skills, not one, because triaging a ticket and writing the reply are different jobs done at different moments.

### 1.3 - The six-question pass, and where each answer lands
`days/day-27-authoring-first-skills/parts/01-extraction/1.3-the-six-question-pass.md` · level `working` · ids SK-06

Six questions — scope, trigger, steps, example, edges, overflow — turn a procedure in your head into a skill folder, and each answer has exactly one destination, so nothing ends up in two places.

### 1.4 - Steps a competent stranger can follow
`days/day-27-authoring-first-skills/parts/01-extraction/1.4-steps-for-a-competent-stranger.md` · level `working` · ids SK-06

Question 3 of the pass produces numbered, imperative steps in the order they happen — each one a single action, each one naming its tool in backticks, and each one carrying its own failure branch rather than deferring it to a section at the bottom.

### 1.5 - One worked example, and why one is enough
`days/day-27-authoring-first-skills/parts/01-extraction/1.5-one-worked-example.md` · level `working` · ids SK-06

Question 4 produces exactly one worked case — real input, the calls in order, the real output — because a single concrete trace teaches the shape of a good answer in a way seven steps cannot, and a second example teaches almost nothing extra for twice the tokens.

### 1.6 - Edge cases are scar tissue
`days/day-27-authoring-first-skills/parts/01-extraction/1.6-edges-are-scar-tissue.md` · level `working` · ids SK-06

Question 5 asks where you have actually been burned, and the answer is one line per burn — which means an edge case you cannot trace back to something that really happened is a guess, and guesses in a procedure are worse than gaps.

### 1.7 - What goes behind a link, and what a fetch really costs
`days/day-27-authoring-first-skills/parts/01-extraction/1.7-what-goes-behind-a-link.md` · level `working` · ids SK-06

Question 6 sends true but long material into references/ — and the rule for the split is not size, it is how often it is needed, because on Sutra's tier a reference fetch costs a whole model round trip and not merely a hundred and forty tokens.

### 2.1 - One fact, one home: shrinking the instruction
`days/day-27-authoring-first-skills/parts/02-what-leaves-the-prompt/2.1-one-fact-one-home.md` · level `working` · ids SK-06

Extraction has a second half nobody does: once a rule is in the skill, it comes out of the instruction — and Sutra's shrinks from 294 tokens to 157, including the deletion of one sentence that has been false for twenty days.

### 2.2 - What never leaves code
`days/day-27-authoring-first-skills/parts/02-what-leaves-the-prompt/2.2-what-never-leaves-code.md` · level `production` · ids SK-06

A skill body is a request, not a rule: the model may not read it, may not follow it, and cannot be made to — so anything that must hold belongs in a callback or a tool, and the test is "what happens on the run where this skill never fires?"

### 3.1 - A skill that names a tool has written a contract
`days/day-27-authoring-first-skills/parts/03-procedure-and-capability/3.1-a-named-tool-is-a-contract.md` · level `working` · ids SK-07

The moment a body says "call lookup_ticket", the skill has declared a requirement — and nothing in the format, the loader or the runtime checks that the requirement is met, so the check has to be yours.

### 3.2 - Honouring the contract: the tools arrive with the procedure
`days/day-27-authoring-first-skills/parts/03-procedure-and-capability/3.2-honouring-the-contract.md` · level `working` · ids SK-07

SkillToolset(skills=..., additional_tools=[lookup_ticket, search_kb]) is where the requirement is met — and because ADK resolves those tools out of the activated skill's metadata, the desk agent goes from four tools to six the moment the triage procedure is loaded, and not before.

### 3.3 - Two skills, one toolset, no overlap
`days/day-27-authoring-first-skills/parts/03-procedure-and-capability/3.3-two-skills-one-toolset.md` · level `working` · ids SK-07

Both skills go on one shelf and one toolset, they can both be active in the same conversation, and the thing that keeps them from competing is that their descriptions share four content words out of forty-seven — which is a number you check rather than a property you hope for.

### 4.1 - Draft, run, read, sharpen: skills are tested prose
`days/day-27-authoring-first-skills/parts/04-the-authoring-loop/4.1-draft-run-read-sharpen.md` · level `working` · ids SK-08

A skill is not finished when it is written; it is finished when a run of it has been watched — and the step everybody skips is the third one, reading what actually happened rather than reading the answer.

### 4.2 - Which rung did it climb: turning a transcript into a verdict
`days/day-27-authoring-first-skills/parts/04-the-authoring-loop/4.2-which-rung-did-it-climb.md` · level `production` · ids SK-08

The list of tool calls a run made, in order, is enough to say which rung the model stopped at — so the diagnosis can be a twenty-line function rather than a judgement, and that function is testable without a model.

### 4.3 - Sharpening without a model: the preflight
`days/day-27-authoring-first-skills/parts/04-the-authoring-loop/4.3-sharpening-without-a-model.md` · level `working` · ids SK-08

Four checks — required tools, dead links, unused references, and the house shape — run in under a second with no key and no quota, and they catch the mistakes that would otherwise be discovered by spending a request to find out.

### 5.1 - 💥 The drill at a locked gate
`days/day-27-authoring-first-skills/parts/05-failure-lab/5.1-the-drill-at-a-locked-gate.md` · level `production` · ids SK-07

Ship the procedure without the tools it names and everything looks correct — the skill loads, the model activates it, the steps are read — and then step 1 is impossible, at which point the model does something, and the something is not in your control.

### 5.2 - 💥 Two notices on one door
`days/day-27-authoring-first-skills/parts/05-failure-lab/5.2-two-notices-on-one-door.md` · level `production` · ids SK-06

Skip the deletion half of extraction and the handbook and the skill end up describing the same field with two different words — priority in one, severity in the other — and the model receives both, in the same request, with no way to know which is current.

### 6.1 - Reviewing a skill like code
`days/day-27-authoring-first-skills/parts/06-in-production/6.1-reviewing-a-skill-like-code.md` · level `production` · ids SK-08

A skill review has three readers with three different jobs — the machine checks structure, an engineer checks the couplings, and the person who owns the procedure checks whether it is right — and a review where one person does all three is a review where the third job does not happen.

### 6.2 - Versioning a procedure, and the answer you cannot explain
`days/day-27-authoring-first-skills/parts/06-in-production/6.2-versioning-a-procedure.md` · level `production` · ids SK-08

metadata.version is a string ADK never reads, the activation register records only skill names, and the consequence is that an answer given last Tuesday cannot be explained today unless you log the version yourself.

