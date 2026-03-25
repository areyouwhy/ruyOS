---
name: inbox
description: "Triage and process items in the ruyOS capture inbox. Use when the user says 'process my inbox', 'triage captures', 'what's in capture', 'inbox', 'process captures', 'clean up captures', or anything that sounds like they want to sort through unsorted items. Also trigger when Workflow/Capture/ has unprocessed files."
---

# Inbox

Process everything in `Workflow/Capture/` and route each item to its permanent home in the vault.

## Vault detection

Before doing anything, check if the current workspace is a ruyOS vault:

1. Look for `CLAUDE.md` at the workspace root containing the word "ruyOS"
2. Look for the `Workflow/` folder

**If BOTH exist** → this is a ruyOS vault. Proceed normally below.
**If EITHER is missing** → tell the user:

> Inbox triage needs direct access to the vault. Please open your ruyOS vault folder in Cowork and run `/inbox` from there.

Then stop. Do not attempt to process inbox from outside the vault.

---

## Context sources

Read these files before executing:

- CLAUDE.md (for the save routing table)
- Workflow/Tasks/Active.md (to avoid duplicating existing tasks)
- Context/Personal/Current Focus.md (to understand priority context)

## What to do

### Step 1: Scan the inbox

List all files in `Workflow/Capture/`. If empty, tell the user there's nothing to process and stop.

For each file, read its contents and determine what it is.

### Step 2: Categorize each item

For each capture, determine its type using the save routing table from CLAUDE.md:

| Type | Destination |
|------|------------|
| Task or to-do | `Workflow/Tasks/Active.md` |
| Decision with rationale | `Workflow/Knowledge/Decisions/` |
| Meeting notes | `Workflow/Log/Meetings/` |
| Research finding or insight | `Workflow/Knowledge/Insights/` or `Research/` |
| Writing rule or preference | `Context/Professional/Writing Preferences.md` |
| Person info | `Context/Personal/People.md` |
| Project update | `Projects/<project>/` index note |
| Prompt | `Settings/Resources/Prompts/` |
| Code snippet | `Settings/Resources/Snippets/` |
| Example output | `Settings/Resources/Examples/` |
| Priority shift | `Context/Personal/Current Focus.md` |

### Step 3: Present the triage plan

Show the user a summary of all captures with proposed destinations. Format:

```
## Inbox triage — X items

1. **[capture title/summary]** → [destination]
   Brief: [one-line description of what this is]

2. **[capture title/summary]** → [destination]
   Brief: [one-line description]
```

Wait for the user to confirm, redirect, or skip items. The user may say "looks good" (process all), redirect specific items ("move #3 to Backlog instead"), or skip items ("skip #2 for now").

### Step 4: Handle complex items

Some captures may need extra handling:

- **Splitting**: If a capture contains multiple distinct things, propose splitting it ("This looks like a task and a decision — want me to split it?")
- **Enrichment**: If a capture is too vague to route ("meeting went well" with no details), ask the user for more context before filing
- **Duplicates**: If a capture matches an existing task or decision, flag it ("This looks similar to an existing task in Active.md — merge or keep separate?")

### Step 5: Process confirmed items

For each confirmed item:

1. Read the destination file
2. Add the content in the right format, matching the file's existing structure
3. Delete the processed capture file from `Workflow/Capture/`

For skipped items, leave them in `Workflow/Capture/`.

### Step 6: Report

Summarize what was processed:
- How many items processed
- Where each one went
- How many skipped/remaining

## Rules

- Never auto-process without showing the user the plan first
- Preserve existing structure when appending to files
- Use wikilinks (`[[Note Name]]`) for internal references
- Match the formatting style of the destination file
- When in doubt about categorization, ask — don't guess
- Delete capture files only after successfully saving to destination
