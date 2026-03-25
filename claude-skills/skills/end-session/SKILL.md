---
name: end-session
description: "Session checkpoint for a ruyOS vault. Use when the user says 'end session', 'close this iteration', 'session wrap-up', 'checkpoint', 'save progress', 'wrap up this session', or anything that sounds like finishing a work block without ending the full day. Different from end-day — this is lighter, for closing an iteration or switching contexts mid-day."
---

# End session

Checkpoint after a work block or iteration. Lighter than end-day — this captures what happened in the current session without doing full daily wrap-up.

## Context sources

Read these files before executing:

- Workflow/Log/Daily/ (today's daily note, if it exists)
- Workflow/Tasks/Active.md

## What to do

### Step 1: Review the session

Look at the current conversation to understand what was worked on:

- What was accomplished?
- Were any decisions made?
- Are there open items or blockers?
- Which project(s) were touched?

### Step 2: Update task statuses

In `Workflow/Tasks/Active.md`:

- Add progress notes to tasks that were worked on but not completed
- Do NOT move tasks to Done.md — that's end-day's job
- Add any new tasks that emerged during the session

### Step 3: Log decisions

For any decisions made during the session, append to `Workflow/Knowledge/Decisions/Decisions.md` with:

- Date
- What was decided
- Context / why

### Step 4: Write session block in daily note

If today's daily note exists (`Workflow/Log/Daily/YYYY-MM-DD.md`), append a session block to the Log section:

```markdown
### Session: [context/project name]
- What was accomplished
- Key decisions made
- Open items carrying forward
```

If the daily note doesn't exist, create it from `Settings/Templates/Daily Note.md` and then add the session block.

### Step 5: Update project notes (if applicable)

If the session was focused on a specific project, check if a session note or update to the project index is appropriate. For significant sessions, create a session note in the project folder using `Settings/Templates/Session Note.md`.

### Step 6: Quick summary

Tell the user:
- What was logged
- What carries forward
- Keep it brief — 3-5 lines max

## Rules

- This is a save-point, not a closing ceremony — keep it light
- Do NOT archive tasks to Done.md (that's end-day)
- Do NOT write "Tomorrow" items (that's end-day)
- Do NOT do the full daily note wrap-up (that's end-day)
- Use wikilinks (`[[Note Name]]`) for internal references
- Preserve existing frontmatter and content when editing notes
- Don't fabricate — only log what actually happened in this session
