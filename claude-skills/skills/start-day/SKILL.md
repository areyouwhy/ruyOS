---
name: start-day
description: "Morning briefing and daily note creator for a ruyOS vault. Use when the user says 'start my day', 'morning briefing', 'what's on my plate', 'what should I focus on', 'daily briefing', 'start-day', or anything that sounds like beginning the work day. Also trigger for open threads, carry-forward items, or yesterday's progress."
---

# Start day

Morning orientation for the vault. Read the vault, build a briefing, write it to today's daily note, and help the user set intentions.

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
   - The Log section — what actually happened (use this for the chat briefing, but don't repeat it in the daily note — it already lives in yesterday's note)
4. **Recent decisions** — Check `Workflow/Knowledge/Decisions/` for anything from the last few days.
5. **Recent session notes** — Scan `Projects/` subfolders for session notes dated yesterday or today. Note which projects had activity and any blockers or next steps.
6. **Inbox check** — List all files in `Workflow/Capture/`. Note the date of each file (from frontmatter, filename, or file modification time). Identify items added since the last daily note. Read each new item to understand what it is.

### Step 2: Build the briefing and write to daily note

Build a concise morning briefing. Present it in chat **and** persist it in today's daily note.

#### Chat briefing

Present the full briefing in chat. This is richer than what goes in the note — include:

- **Carry-forward items** — open threads from yesterday
- **Active priorities** — from Current Focus, flag misalignment if relevant
- **What happened yesterday** — 2-3 sentence summary from yesterday's Log section
- **Inbox** — new captures since last daily note, with relevance to priorities noted
- **Today's landscape** — suggest what seems natural to focus on

#### Write to daily note

Check if today's note exists in `Workflow/Log/Daily/` (format: `YYYY-MM-DD.md`).

**If it doesn't exist**, create it using the template from `Settings/Templates/Daily Note.md`.

**If it already exists**, don't overwrite existing content.

Write to the daily note under the `# Briefing` section:

- **`## From yesterday`** — bullet list of carry-forward items from yesterday's Tomorrow section and any open threads. No prose summary — that already lives in yesterday's note.
- **`## Inbox`** — if new items exist in `Workflow/Capture/` since last daily note, list them as bullets with one-line summaries. Call out any that seem relevant to today's priorities. If no new captures, write "Nothing new." Don't process or move items — that's `/inbox`'s job.

Leave `## Focus` empty — that gets filled after the user sets intentions in Step 3.

### Step 3: Set intentions

After presenting the briefing, ask the user what they want to focus on today. Frame it as a prompt:

> What do you want to focus on today?

Include the carry-forward items and landscape suggestions as starting points they can accept, adjust, or replace. If inbox items seem relevant to today's focus, mention them as candidates.

**If the user provides intentions** → write them to the `## Focus` section under `# Briefing`.

**If the user says "looks good", "go with that", or similar** → write the suggested intentions (from the landscape section) to Focus.

**If the user adds extra context** ("I also have a meeting with X", "I need to finish the docs") → incorporate it into Focus alongside the suggestions.

**If the user skips or wants to move on** → write the carry-forward items to Focus as a baseline, so the note isn't empty.

### Step 4: Confirm

Once Focus is written, confirm briefly:

> Daily note created. Focus set. Have a good one.

Show the final Focus list so the user can see what landed in the note.

## Daily note structure

The daily note has two top-level sections. Start-day owns `# Briefing`. End-session and end-day own `# Summary`.

```markdown
# Briefing
> [!info] Automatically generated by `/start-day`

## From yesterday
- [carry-forward items]

## Inbox
- [new captures or "Nothing new."]

## Focus
> [!warning] Based on input reply to `/start-day`
- [user's intentions]

# Summary
> [!info] Automatically generated by `/end-session` and `/end-day`

## Log
## Sessions (dataview)
## Decisions
## Learnings
## Tomorrow
```

## Rules

- Use wikilinks (`[[Note Name]]`) for internal references
- Preserve existing frontmatter when editing notes
- Direct, concise, no fluff
- Don't fabricate — if there's no yesterday note or no session notes, say so
- Open threads are important — carry them forward faithfully, don't silently drop items
- The `# Briefing` section is write-once — end-day and end-session never touch it
- The `# Summary` section is end-session/end-day territory — start-day never touches it
- Inbox items are surfaced for awareness only — don't move or process them (that's `/inbox`)
