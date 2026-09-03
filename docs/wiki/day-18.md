# Day 18 - Artifacts — files that survive turns

IDs closed: ADK-21 · source: `days/day-18-artifacts-that-survive/`

## Parts

### 1.1 - The thing state cannot hold
`days/day-18-artifacts-that-survive/parts/01-not-a-state-key/1.1-the-thing-state-cannot-hold.md` · level `foundation` · ids ADK-21

An artifact is a named, versioned blob of bytes kept beside the conversation — a screenshot, an attached log, a generated report — because state is for small serializable facts and bytes are neither small nor facts.

### 1.2 - A Part, not a file
`days/day-18-artifacts-that-survive/parts/01-not-a-state-key/1.2-a-part-not-a-file.md` · level `working` · ids ADK-21

An artifact is a types.Part carrying inline_data — bytes plus a MIME type — which is the same class the model's own content is made of, and the MIME type is optional in the code and required in practice.

### 1.3 - A separate wire
`days/day-18-artifacts-that-survive/parts/01-not-a-state-key/1.3-a-separate-wire.md` · level `working` · ids ADK-21

Artifacts come from their own service, wired onto the runner beside the session service — and if you do not wire one, saving raises ValueError: Artifact service is not initialized. at the moment a tool tries.

### 2.1 - Every save is a new version
`days/day-18-artifacts-that-survive/parts/02-versions/2.1-every-save-is-a-new-version.md` · level `working` · ids ADK-21

Saving the same filename again does not replace anything: it appends version 1 beside version 0 and returns the new number, so an artifact is a list of versions under a name rather than a file you can overwrite.

### 2.2 - What a version knows about itself
`days/day-18-artifacts-that-survive/parts/02-versions/2.2-what-a-version-knows.md` · level `working` · ids ADK-21

Each version carries a record beside its bytes — the number, a canonical URI, a creation time, the MIME type and any custom metadata you pass at save time — which is what turns a pile of versions into something you can explain.

### 2.3 - Nothing is overwritten
`days/day-18-artifacts-that-survive/parts/02-versions/2.3-nothing-is-overwritten.md` · level `production` · ids ADK-21

A store that never replaces anything only grows: twenty saves of one modest note hold twenty copies, delete_artifact removes every version at once rather than the newest, and a save after a delete starts again at version 0.

### 3.1 - The user: filename
`days/day-18-artifacts-that-survive/parts/03-two-scopes/3.1-the-user-filename.md` · level `working` · ids ADK-21

Artifacts have two scopes and the filename chooses between them: a plain name belongs to one conversation, and a name beginning user: belongs to the person for the life of the application — exactly the trick Day 17's state keys use, applied to files.

### 3.2 - Where it actually lives
`days/day-18-artifacts-that-survive/parts/03-two-scopes/3.2-where-it-actually-lives.md` · level `production` · ids ADK-21

FileArtifactService writes a directory tree you can read with ls — app, user, then either a session or nothing, then the filename, then a numbered version folder holding the bytes and a metadata.json — and the filename you pass becomes part of that path, which is why it is validated.

### 4.1 - Saving from a tool
`days/day-18-artifacts-that-survive/parts/04-in-the-run/4.1-saving-from-a-tool.md` · level `working` · ids ADK-21

await tool_context.save_artifact(filename, part) writes the file, returns its version, and records {filename: version} on the event as an artifact delta — the same mechanism as Day 17's state delta, so one step can update both stores and the history knows about both.

### 4.2 - Reading it back
`days/day-18-artifacts-that-survive/parts/04-in-the-run/4.2-reading-it-back.md` · level `working` · ids ADK-21

await tool_context.load_artifact(filename) returns a Part or None, and the tempting shortcut — {artifact.name} in an instruction — puts the repr of the whole Part object into your prompt rather than the file's text.

### 4.3 - What the model cannot see
`days/day-18-artifacts-that-survive/parts/04-in-the-run/4.3-what-the-model-cannot-see.md` · level `production` · ids ADK-21

Saving an artifact does not put it in the model's context: ADK's load_artifacts tool advertises the filenames on every request and inserts the contents only after the model asks for them, into that one request and no further.

### 5.1 - 💥 The artifact with no service
`days/day-18-artifacts-that-survive/parts/05-failure-lab/5.1-the-artifact-with-no-service.md` · level `production` · ids ADK-21

A runner with no artifact_service turns every save into a ValueError raised inside the runtime, which never reaches your loop — so the turn produces no answer, no exception and no file, and the only evidence is a traceback in a background thread.

### 6.1 - Testing artifacts without a model
`days/day-18-artifacts-that-survive/parts/06-in-production/6.1-testing-artifacts-without-a-model.md` · level `production` · ids ADK-21

Seven assertions, no key and no network — versioning, the two scopes, the None cases, delete semantics, the tool's two deltas, the derived filename, and durability across a fresh service — which is the one place Phase 3's gate can actually be proved today.

### 6.2 - What belongs in an artifact
`days/day-18-artifacts-that-survive/parts/06-in-production/6.2-what-belongs-in-an-artifact.md` · level `production` · ids ADK-21

Artifacts are for bytes somebody would want back: a file a person uploaded, a document Sutra produced, an output worth keeping — not scratch data, not secrets, and not anything whose only reader is the next line of your own code.

### 6.3 - Surviving a restart
`days/day-18-artifacts-that-survive/parts/06-in-production/6.3-surviving-a-restart.md` · level `production` · ids ADK-21

FileArtifactService(root_dir=...) makes artifacts outlive the process — a second service object on the same directory reads what the first one wrote — which is the first half of Phase 3's gate proved rather than promised, at zero cost.

