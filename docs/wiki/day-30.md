# Day 30 - Skill testing & versioning

IDs closed: SK-17, SK-18, SK-19 · source: `days/day-30-skill-testing-and-versioning/`

## Parts

### 1.1 - Prose with consequences
`days/day-30-skill-testing-and-versioning/parts/01-testing-prose/1.1-prose-with-consequences.md` · level `foundation` · ids SK-17

A skill is a Markdown file that changes what your program does, so it needs the same protection every other file that changes what your program does already has — a test that runs on every commit and can go red.

### 1.2 - Shape and sense
`days/day-30-skill-testing-and-versioning/parts/01-testing-prose/1.2-shape-and-sense.md` · level `foundation` · ids SK-17

A test over a skill can check its shape — the fields are there, within limits, pointing at files that exist — and cannot check its sense, so the job of today's suite is to be excellent at shape and to say out loud, in code, that it never touched sense.

### 1.3 - The rules worth a test
`days/day-30-skill-testing-and-versioning/parts/01-testing-prose/1.3-the-rules-worth-a-test.md` · level `working` · ids SK-17

A rule earns a place in the suite when breaking it changes behaviour, a machine can decide it without argument, and nothing else in the toolchain already catches it — which leaves Sutra with six rules, three from the open specification and three from the house.

### 2.1 - A finding is a return value
`days/day-30-skill-testing-and-versioning/parts/02-checks-as-functions/2.1-a-finding-is-a-return-value.md` · level `working` · ids SK-17

Every check in tools/skill_checks.py takes a skill and returns a list of Finding — it never prints, never exits and never raises because a skill is bad — because the same function has to serve a test that asserts on it today and a command-line linter that turns it into an exit code tomorrow.

### 2.2 - Let the loader be the oracle
`days/day-30-skill-testing-and-versioning/parts/02-checks-as-functions/2.2-let-the-loader-be-the-oracle.md` · level `working` · ids SK-17

Do not re-implement the specification's rules — call the loader your agent will use at runtime, catch what it raises, and turn the exception into a finding, because then your check and your runtime can never disagree about whether a skill is valid.

### 2.3 - One bad folder must not stop the shelf
`days/day-30-skill-testing-and-versioning/parts/02-checks-as-functions/2.3-one-bad-folder-must-not-stop-the-shelf.md` · level `working` · ids SK-17

load_skills_from_dir raises on the first broken folder and tells you nothing about the rest, so the checker walks the shelf itself and loads each folder separately — one bad skill becomes one row, not a dead run.

### 2.4 - Pointers that go nowhere
`days/day-30-skill-testing-and-versioning/parts/02-checks-as-functions/2.4-pointers-that-go-nowhere.md` · level `working` · ids SK-17

A skill body that names references/severity-rubric.md is making a promise about a file, nothing in ADK checks that the promise holds, and a broken promise costs you a worse answer with no error — so the checker extracts every resource path the body mentions and asks the filesystem.

### 3.1 - Enumerate the shelf, never a list
`days/day-30-skill-testing-and-versioning/parts/03-the-suite/3.1-enumerate-never-list.md` · level `working` · ids SK-17

The test must ask the filesystem what is on the shelf every time it runs, because any list of skills written into the test is a copy of the truth that stops being true the first time somebody adds a skill — and it stops being true silently, while the suite stays green.

### 3.2 - A failure must name the file
`days/day-30-skill-testing-and-versioning/parts/03-the-suite/3.2-a-failure-must-name-the-file.md` · level `working` · ids SK-17

A red test over a whole shelf has to print the folder, the rule and the offending text, because the person reading the failure is usually not the person who caused it and has no idea which of forty files to open.

### 3.3 - The test for the checker
`days/day-30-skill-testing-and-versioning/parts/03-the-suite/3.3-the-test-for-the-checker.md` · level `working` · ids SK-17

A green shelf lane cannot tell you whether your shelf is clean or whether your checks do nothing, so every rule needs a second test that hands it something broken and demands the finding — otherwise the suite is measuring your skills' silence, not your checks' vigilance.

### 4.1 - One valid skill, one changed field
`days/day-30-skill-testing-and-versioning/parts/04-skills-built-in-code/4.1-a-skill-without-a-folder.md` · level `working` · ids SK-18

The checker lane needs a skill that is valid in every way except the one being tested, so the suite gets a single builder — a_skill(...) — that returns a good Skill in memory and lets a test change exactly one field, which makes every failure attributable to that field and nothing else.

### 4.2 - The model is the spec
`days/day-30-skill-testing-and-versioning/parts/04-skills-built-in-code/4.2-the-model-is-the-spec.md` · level `working` · ids SK-18

Frontmatter refuses to hold an invalid name or an empty description at construction time, so the specification's rules are testable as pytest.raises cases against the model itself — and a rule you cannot even build an object to break is a rule you do not need to re-implement.

### 4.3 - What memory cannot test
`days/day-30-skill-testing-and-versioning/parts/04-skills-built-in-code/4.3-what-memory-cannot-test.md` · level `production` · ids SK-18

A Skill built in memory has no folder, so every rule that is about the folder — the name matching the directory, a pointer resolving to a file, a digest over what is on disk — is untestable that way, and those rules keep their evidence on the real shelf.

### 5.1 - A name for the text that ran
`days/day-30-skill-testing-and-versioning/parts/05-versioning/5.1-a-name-for-the-text-that-ran.md` · level `foundation` · ids SK-19

A skill version is not a release number and buys you no compatibility — it is a name for one exact version of the text, so that an audit, a log line and a bug report can all say which one, and the check that enforces it is short because the field is inert everywhere else.

### 5.2 - The bump rule
`days/day-30-skill-testing-and-versioning/parts/05-versioning/5.2-the-bump-rule.md` · level `working` · ids SK-19

The size of the bump is not a description of how much text changed — it is a declaration of which checks have to be re-run, so a patch obliges nothing, a minor obliges the routing gate, and a major obliges a full re-read as though the skill had arrived from a stranger.

### 5.3 - The change the version missed
`days/day-30-skill-testing-and-versioning/parts/05-versioning/5.3-the-change-the-version-missed.md` · level `production` · ids SK-19

The version lives in SKILL.md and the skill is a whole folder, so editing only a reference file changes what the agent reads while the version sits still — and the fix is a short hash of the folder, recorded next to the version, so any content change forces the frontmatter to move.

### 6.1 - 💥 The drill in the other building
`days/day-30-skill-testing-and-versioning/parts/06-in-production/6.1-the-drill-in-the-other-building.md` · level `production` · ids SK-17

A suite whose input list is a copy of the shelf keeps passing while the real shelf breaks, and this part builds that suite on purpose, runs it beside the honest one, and watches the wrong one report success on a shelf with a skill that will not load.

### 6.2 - Writing down what green means
`days/day-30-skill-testing-and-versioning/parts/06-in-production/6.2-writing-down-what-green-means.md` · level `production` · ids SK-17, SK-18

A suite's boundary has to live inside the suite, as a test that passes on purpose and says why, because a docstring is read once by the person who wrote it and a test runs in front of everyone forever.

### 6.3 - Fix the skill, never the check
`days/day-30-skill-testing-and-versioning/parts/06-in-production/6.3-when-the-suite-goes-red.md` · level `production` · ids SK-17, SK-19

When the suite goes red the decision is always the same and always made in the same order — read the rule tag, fix the skill, and only then ask whether the rule itself was wrong — because a check bent to accommodate the thing it was checking has stopped being a check.

## Papers - read after the parts

### doi:10.1109/C-M.1978.218136 - Hints on Test Data Selection: Help for the Practicing Programmer
`days/day-30-skill-testing-and-versioning/papers/01-hints-on-test-data-selection.md`

You can measure how good a test suite is by deliberately introducing small errors into the program and counting how many the suite notices — because a suite that cannot tell a broken program from the real one is not testing that program, however much of it the suite runs.

