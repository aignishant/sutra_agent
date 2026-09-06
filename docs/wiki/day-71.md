# Day 71 - Computer use & the sandbox — browser agent vs a local dummy site; execution isolation in practice

IDs closed: AG-31, ADK-50, SEC-14 · source: `days/day-71-computer-use-and-the-sandbox/`

## Parts

### 1.1 - The page with no JSON
`days/day-71-computer-use-and-the-sandbox/parts/01-no-api/1.1-the-page-with-no-json.md` · level `foundation` · ids AG-31

Most of the world publishes for people and not for programs, so an agent that can only call functions is blind to it — and computer use closes that gap in the most literal way there is: the model is shown the screen and allowed to move the pointer, exactly like a person, which makes it the last thing you should reach for and sometimes the only thing left.

### 1.2 - Pixels and a URL
`days/day-71-computer-use-and-the-sandbox/parts/01-no-api/1.2-pixels-and-a-url.md` · level `foundation` · ids AG-31

current_state() hands the model two things — a screenshot and a URL — and nothing else: no HTML, no text, no accessibility tree, so every fact the model has about the page is one it recovered from an image, and on this day's status page that image is 28 165 bytes of PNG.

### 1.3 - Fifteen doors, one used
`days/day-71-computer-use-and-the-sandbox/parts/01-no-api/1.3-fifteen-doors-one-used.md` · level `working` · ids AG-31

The surface you have to sandbox is what the runtime declares, not what your script happens to call: this day's agent uses exactly one action, and the runtime offers the model fifteen — a number read off the real request rather than counted in your head.

### 2.1 - See, decide, act
`days/day-71-computer-use-and-the-sandbox/parts/02-driving-it/2.1-see-decide-act.md` · level `foundation` · ids AG-31, ADK-50

Computer use is the loop you already hand-rolled on Day 3, with exactly one substitution: the observation that comes back after each action is a screenshot rather than a line of text — look at the screen, choose one action, take it, look again.

### 2.2 - The coordinates are not your pixels
`days/day-71-computer-use-and-the-sandbox/parts/02-driving-it/2.2-the-coordinates-are-not-your-pixels.md` · level `working` · ids AG-31, ADK-50

The model always works in a fixed 1000 by 1000 space and ADK silently rescales every x and y to your real window before your computer ever sees them — so the numbers in your trace are not the numbers the model emitted, and a sandbox rule written about pixels has to say which pixels.

### 2.3 - A site you own
`days/day-71-computer-use-and-the-sandbox/parts/02-driving-it/2.3-a-site-you-own.md` · level `working` · ids AG-31, ADK-50

The page this agent drives is served from lab/site/ on a port on your own machine for three separate reasons — it cannot change under you, driving somebody else's site is not yours to do, and the blast radius is a port you control — and only the first of the three is the one people think of.

### 3.1 - The check outside every tool
`days/day-71-computer-use-and-the-sandbox/parts/03-the-door/3.1-the-check-outside-every-tool.md` · level `working` · ids SEC-14, ADK-50

The sandbox is one plugin registered on the Runner, not a check written inside a browser action — because [1.3](../01-no-api/1.3-fifteen-doors-one-used.md) counted fifteen actions handed to the model, and a check inside one of them guards one of them.

### 3.2 - The guard ADK already shipped
`days/day-71-computer-use-and-the-sandbox/parts/03-the-door/3.2-the-guard-adk-already-shipped.md` · level `production` · ids SEC-14, ADK-50

Before your plugin sees anything, ComputerUseToolset has already wrapped navigate in a check that refuses any URL whose host is not publicly routable — and that check is on by default, because an agent that can be talked into navigating can be talked into fetching your cloud metadata endpoint or an admin panel on localhost.

### 3.3 - All or nothing
`days/day-71-computer-use-and-the-sandbox/parts/03-the-door/3.3-all-or-nothing.md` · level `production` · ids SEC-14, ADK-50

allow_private_network_access is a boolean, so switching it off to reach your own fixture on 127.0.0.1:8771 also opens the cloud metadata endpoint and every admin panel on localhost — a flag with the right default and the wrong shape, which is why your own door has to supply the precision the framework's cannot.

### 3.4 - What a refusal leaves behind
`days/day-71-computer-use-and-the-sandbox/parts/03-the-door/3.4-what-a-refusal-leaves-behind.md` · level `production` · ids SEC-14, ADK-50

A sandbox that stops something and leaves no record of it has told nobody — so a refusal is an event with a reason, written into the same trace as the actions that were allowed, beside them and in order.

### 4.1 - The action nobody enumerated
`days/day-71-computer-use-and-the-sandbox/parts/04-in-production/4.1-the-action-nobody-enumerated.md` · level `production` · ids SEC-14

A rule that switches on action names is only ever as complete as the list of action names, and that list belongs to the framework rather than to you — so the door does not merely have gaps today, it acquires new ones on a day you did not write any code.

### 4.2 - Isolation you can buy
`days/day-71-computer-use-and-the-sandbox/parts/04-in-production/4.2-isolation-you-can-buy.md` · level `production` · ids SEC-14

The door in section 3 decides what the agent is allowed to ask for, and that is a different thing from containing what the browser then does — the second one is not a better rule, it is a wall the running process cannot reach around, and it is bought at a layer underneath your code rather than written into it.

### 4.3 - What this is worth
`days/day-71-computer-use-and-the-sandbox/parts/04-in-production/4.3-what-this-is-worth.md` · level `production` · ids AG-31, SEC-14

Computer use buys you one thing that nothing else buys — a system with no interface for machines becomes reachable — and it charges for it in pictures, in fragility and in a fifteen-action surface you now have to police, so the rule that falls out of the day is: reach for it only when there is no API, no feed and no MCP server, and say out loud which of those you checked.

## Papers - read after the parts

### doi:10.1109/SP.2009.25 - Native Client: A Sandbox for Portable, Untrusted x86 Native Code
`days/day-71-computer-use-and-the-sandbox/papers/01-native-client.md`

Running code somebody else wrote had two settled answers — trust it and run it, or refuse it and run nothing — and this is the document that established a third: check it against a small set of structural rules before it runs, refuse anything that does not fit, and put the trust in the checker rather than in the code.

