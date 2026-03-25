---
name: end-day
description: "Daily wrap-up for a ruyOS vault. Use when the user says 'end my day', 'wrap up', 'daily wrap-up', 'end-day', 'close out the day', 'what did I do today', or anything that sounds like wrapping up a work day. Also trigger for logging decisions, archiving completed tasks, or summarizing today's work."
---

# End day

Daily wrap-up for the vault. Review what happened, log decisions, archive tasks, and close out the day.

## Context sources

Read these files from the vault before executing:

- Workflow/Log/Daily/ (today's daily note)
- Workflow/Tasks/Active.md
- Workflow/Knowledge/Decisions/Decisions.md
- Context/Professional/Writing Preferences.md (for any new rules learned)

## What to do

### Step 1: Gather context

1. **Today's daily note** — Read `Workflow/Log/Daily/YYYY-MM-DD.md` (today's date).
2. **Active tasks** — Read `Workflow/Tasks/Active.md` to see what was on the list.
3. **Conversation review** — Review this conversation for any decisions, insights, or rules learned during the session.

### Step 2: Update today's daily note

Update the daily note with:

- **Log section** — Summary of what was accomplished today. Keep it factual and concise.
- **Tomorrow section** — Flag anything unfinished that should carry forward.
- **Decisions section** — List any significant decisions made.

If the daily note doesn't exist yet, create it using the template from `Settings/Templates/Daily Note.md`.

### Step 3: Log decisions

For any significant decisions made today, add them to `Workflow/Knowledge/Decisions/Decisions.md` with:

- Date
- What was decided
- Context / why
- Alternatives considered (if any)

### Step 4: Update tasks

- **Move completed tasks** from `Workflow/Tasks/Active.md` to `Workflow/Tasks/Done.md` under the current month heading.
- **Add new tasks** that came up today to `Workflow/Tasks/Active.md`.

### Step 5: Capture learnings

- **Writing rules or preferences** learned today → append to `Context/Professional/Writing Preferences.md` in the Living Rules section.
- **Insights** → save to `Workflow/Knowledge/Insights/` if significant.

### Step 6: Day summary

Finish with a quick summary for the user:
- What got done
- What carries forward
- Any decisions logged

## Rules

- Use wikilinks (`[[Note Name]]`) for internal references
- Preserve existing frontmatter when editing notes
- Direct, concise, no fluff
- Don't fabricate — only log what actually happened
- When moving tasks to Done, preserve the task text exactly
