# Day 37 - Auth and enterprise — badges, questions and policy

IDs closed: MCP-13, MCP-27, MCP-30 · source: `days/day-37-auth-and-elicitation/`

## Parts

### 1.1 - The badge, the desk and the door
`days/day-37-auth-and-elicitation/parts/01-the-badge/1.1-the-badge-the-desk-and-the-door.md` · level `foundation` · ids MCP-13

An MCP server over HTTP does not check who you are; it checks a token somebody else issued — so the work splits three ways between a server that holds the tools, a separate service that holds the identities, and a client that carries the token and nothing else.

### 1.2 - The refusal that carries directions
`days/day-37-auth-and-elicitation/parts/01-the-badge/1.2-the-refusal-that-carries-directions.md` · level `working` · ids MCP-13

A protected MCP server answers an unauthenticated request with 401 and a WWW-Authenticate header naming the document that says where to go next — so the client discovers its authorization server from the refusal itself, without being configured with it in advance.

### 1.3 - A voucher for one shop
`days/day-37-auth-and-elicitation/parts/01-the-badge/1.3-a-voucher-for-one-shop.md` · level `working` · ids MCP-13

An access token names the one service it was minted for, and a server must check that the name is its own — and must never spend a token it was given somewhere else, because a token that travels is a token that has stopped meaning anything.

### 2.1 - Which desk actually answered
`days/day-37-auth-and-elicitation/parts/02-issuer-checks/2.1-which-desk-actually-answered.md` · level `working` · ids MCP-13

An authorization response that does not say which authorization server produced it can be redirected to the wrong one — so the response carries an iss parameter, and the client compares it against the issuer it recorded before it sent the user off, and stops if they differ.

### 2.2 - The comparison that must not be helpful
`days/day-37-auth-and-elicitation/parts/02-issuer-checks/2.2-the-comparison-that-must-not-be-helpful.md` · level `working` · ids MCP-13

The iss value is form-decoded once and then compared byte for byte — no case folding, no trailing-slash trimming, no default-port elision — because every tidy-up you add is one more string an attacker's issuer is allowed to be.

### 2.3 - The menu you host yourself
`days/day-37-auth-and-elicitation/parts/02-issuer-checks/2.3-the-menu-you-host-yourself.md` · level `working` · ids MCP-13

A client's identity is no longer something it registers at every authorization server it meets — its client_id is an HTTPS URL it controls, serving a small JSON document the server fetches and checks, which is why Dynamic Client Registration is now deprecated.

### 3.1 - The job that stopped and left a number
`days/day-37-auth-and-elicitation/parts/03-the-question/3.1-the-job-that-stopped-and-left-a-number.md` · level `foundation` · ids MCP-27

A server that needs a human answer mid-call cannot interrupt you — it ends the call with a result that says input required, carrying the question and an opaque slip, and you get the answer and call again as a brand new request.

### 3.2 - A form the till can print
`days/day-37-auth-and-elicitation/parts/03-the-question/3.2-a-form-the-till-can-print.md` · level `working` · ids MCP-27

The schema a server sends with a question is deliberately crippled — a flat object of primitive fields, nothing nested — so that every client, however simple its interface, can render the same question as a real form.

### 3.3 - Three answers, not two
`days/day-37-auth-and-elicitation/parts/03-the-question/3.3-three-answers-not-two.md` · level `working` · ids MCP-27

A user can accept, decline or cancel, and those are three different facts about the world — a server that folds the last two together cannot tell "no" from "not now", and will keep asking a person who has already said no.

### 3.4 - The docket you cannot write yourself
`days/day-37-auth-and-elicitation/parts/03-the-question/3.4-the-docket-you-cannot-write-yourself.md` · level `production` · ids MCP-27

requestState travels through the client, so the specification requires you to treat it as attacker-controlled input: sign it, put the principal, an expiry and a digest of the original request inside, and refuse anything that fails verification.

### 4.1 - The link you check before you click
`days/day-37-auth-and-elicitation/parts/04-out-of-band/4.1-the-link-you-check-before-you-click.md` · level `working` · ids MCP-27

When the answer must not pass through the client at all, the server sends a URL instead of a form — and the client's job shrinks to showing the full address, getting explicit consent, and opening it somewhere it cannot watch.

### 4.2 - 💥 The sheet in the corridor
`days/day-37-auth-and-elicitation/parts/04-out-of-band/4.2-the-sheet-in-the-corridor.md` · level `production` · ids MCP-27

A server MUST NOT ask for a password, an API key, a token or a payment credential through form mode — not because the form is insecure, but because the client, the model's context and every log on the retry path all see what the user types into it.

### 4.3 - 💥 The link that went to the wrong person
`days/day-37-auth-and-elicitation/parts/04-out-of-band/4.3-the-link-that-went-to-the-wrong-person.md` · level `production` · ids MCP-27

A consent URL can be forwarded, so the server MUST verify that the person who finishes the flow is the person it minted the link for — otherwise one user's account collects a token that a different user authorised.

### 5.1 - The optional extras list
`days/day-37-auth-and-elicitation/parts/05-policy/5.1-the-optional-extras-list.md` · level `foundation` · ids MCP-30

Everything beyond MCP's small core now ships as a named, versioned extension with a reverse-DNS identifier, declared by both sides on every request, disabled by default — so a capability is either in play because both parties said so, or it is not in play at all.

### 5.2 - One account instead of forty
`days/day-37-auth-and-elicitation/parts/05-policy/5.2-one-account-instead-of-forty.md` · level `working` · ids MCP-30

Enterprise-Managed Authorization moves the allow or deny decision from each employee's consent dialogue to the organisation's identity provider — the client exchanges its login for a grant the identity provider issues only if policy permits, and an unauthorised employee never receives a token at all.

### 5.3 - Policy that can name a feature
`days/day-37-auth-and-elicitation/parts/05-policy/5.3-policy-that-can-name-a-feature.md` · level `production` · ids MCP-30

Because every capability beyond the core is a named extension declared in the open on every request, an organisation can allow a server and still deny one of its features — governance gets a vocabulary finer than this whole server, yes or no.

### 6.1 - 💥 The receipt that printed the whole number
`days/day-37-auth-and-elicitation/parts/06-in-production/6.1-the-receipt-that-printed-the-whole-number.md` · level `production` · ids MCP-13

A bearer token is the credential, so the structured logger you built on Day 22 will write it out in full unless something stops it — and the three exits are the log line, the error body, and the repository.

### 6.2 - The tray the driver cannot see
`days/day-37-auth-and-elicitation/parts/06-in-production/6.2-the-tray-the-driver-cannot-see.md` · level `production` · ids MCP-13, MCP-27, MCP-30

The pinned SDK has the question — both elicitation modes, all three actions, the CIMD client id — and lacks the carriage, the iss check and the extensions framework, so this day is half runnable and you must know which half before you write a line.

### 6.3 - Seven questions before you ask anybody anything
`days/day-37-auth-and-elicitation/parts/06-in-production/6.3-seven-questions-before-you-ask-anybody-anything.md` · level `production` · ids MCP-13, MCP-27, MCP-30

Everything this day taught reduces to seven questions with a written answer, and a server that cannot answer all seven is not ready to hold a token or ask a human anything — which is why the check starts red.

## Papers - read after the parts

### doi:10.17487/RFC9207 - OAuth 2.0 Authorization Server Issuer Identification
`days/day-37-auth-and-elicitation/papers/01-issuer-identification.md`

An authorization response that does not say who sent it can be redirected to the wrong recipient, so this document adds one parameter — iss — and one obligation: the client compares it against the issuer it recorded, before the authorization code goes anywhere.

