---
name: start-day
description: "Morning briefing and daily note creator for a ruyOS vault. Use when the user says 'start my day', 'morning briefing', 'what's on my plate', 'what should I focus on', 'daily briefing', 'start-day', or anything that sounds like beginning the work day. Also trigger for open threads, carry-forward items, or yesterday's progress."
---

# Start day

Morning orientation for the vault. Read the vault, build a briefing, and create today's daily note.

## Vault detection

Before doing anything, check if the current workspace is a ruyOS vault:

1. Look for `CLAUDE.md` at the workspace root containing the word "ruyOS"
2. Look for the `Workflow/` folder

**If BOTH exist** → this is a ruyOS vault. Proceed normally below.
**If EITHER is missing** → tell the user:

> Start day needs direct access to the vault — it reads your tasks, focus, goals, and creates your daily note. Please open your ruyOS vault folder in Cowork and run `/start-day` from there.

Then stop.

---

## Context sources

Read these files from the vault before executing:

- Context/Personal/Current Focus.md
- Workflow/Tasks/Active.md
- Context/Personal/Goals.md (skim for "This Year" section)

## What to do

Follow these steps in order. Read everything before writing anything.

### Step 0: Sync roaming memories

Before doing anything else, check Cowork's auto-memory directory for files matching the pattern `ruyos-*.md` (e.g., `ruyos-session-*`, `ruyos-endday-*`, `ruyos-remember-*`).

If roaming memories exist:

1. **Read each one** and parse its structured content.
2. **Route each item** to the correct vault location:
   - **Session blocks** → append to today's daily note (or create it first)
   - **Decisions** → append to `Workflow/Knowledge/Decisions/Decisions.md`
   - **Tasks completed** → move from `Workflow/Tasks/Active.md` to `Workflow/Tasks/Done.md`
   - **New tasks** → add to `Workflow/Tasks/Active.md`
   - **Learnings/insights** → route to `Workflow/Knowledge/Insights/` or `Context/Professional/Writing Preferences.md` as appropriate
   - **Remember items** → use the `Category` and `Intended destination` fields to route to the correct file
   - **Carry-forward items** → include in today's daily note Focus section
3. **Delete the processed memory files** from auto-memory after successfully syncing.
4. **Tell the user** what was synced: "Synced X items from other sessions" with a brief list.

If no roaming memories exist, skip this step silently.

### Step 1: Gather context

1. **Current Focus** — Read `Context/Personal/Current Focus.md`. This is the living priority list.
2. **Active tasks** — Read `Workflow/Tasks/Active.md`. What's on the to-do list?
3. **Yesterday's daily note** — Find the most recent file in `Workflow/Log/Daily/` by date in filename (`YYYY-MM-DD.md`). Pay attention to:
   - The Tomorrow section — carry-forward items
   - The Log section — what actually happened
4. **Recent decisions** — Check `Workflow/Knowledge/Decisions/` for anything from the last few days.
5. **Recent session notes** — Scan `Projects/` subfolders for session notes dated yesterday or today. Note which projects had activity and any blockers or next steps.

### Step 2: Build the briefing

Present a concise morning briefing. Keep it scannable — orientation, not a report.

**Carry-forward items** — Open threads from yesterday's daily note. Things flagged as unfinished, with enough context to act on.

**Active priorities** — From Current Focus. Flag if yesterday's work seems misaligned with stated priorities (not necessarily bad, just worth noting).

**What happened yesterday** — 2-3 sentence summary from the daily note's Log section. Distilled, not copy-pasted.

**Today's landscape** — Based on open threads and priorities, suggest what seems most natural to focus on. Frame as observation, not instruction — the user decides their own priorities.

### Step 3: Create today's daily note

Check if today's note exists in `Workflow/Log/Daily/` (format: `YYYY-MM-DD.md`).

**If it doesn't exist**, create it using the template from `Settings/Templates/Daily Note.md`. Populate the Focus section by carrying forward unresolved items from yesterday.

**If it already exists**, don't overwrite. Check if Focus is empty — if so, populate from yesterday's carry-forward. If it has content, leave it.

### Step 4: Suggest intentions (optional)

If the Focus section of today's daily note is empty, suggest 2-4 concrete, actionable intentions based on the briefing. Write them directly into the note. Frame as starting points — the user will adjust.

## Rules

- Use wikilinks (`[[Note Name]]`) for internal references
- Preserve existing frontmatter when editing notes
- Direct, concise, no fluff
- Don't fabricate — if there's no yesterday note or no session notes, say so
- Open threads are important — carry them forward faithfully, don't silently drop items
