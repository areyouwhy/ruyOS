---
name: end-day
description: "Daily wrap-up for a ruyOS vault. Use when the user says 'end my day', 'wrap up', 'daily wrap-up', 'end-day', 'close out the day', 'what did I do today', or anything that sounds like wrapping up a work day. Also trigger for logging decisions, archiving completed tasks, or summarizing today's work."
---

# End day

Daily wrap-up for the vault. Review what happened, log decisions, archive tasks, and close out the day.

## Vault detection

Before doing anything, check if the current workspace is a ruyOS vault:

1. Look for `CLAUDE.md` at the workspace root containing the word "ruyOS"
2. Look for the `Workflow/` folder

**If BOTH exist** → this is a ruyOS vault. Proceed with "Vault mode" below.
**If EITHER is missing** → this is not the vault. Use "Roaming mode" below.

---

## Roaming mode (no vault detected)

You're running outside the ruyOS vault. Capture the day's wrap-up to auto-memory so it can be synced next time the user opens the vault.

### Step 1: Review the day

Review the conversation for everything that happened — accomplishments, decisions, insights, new tasks, things learned.

### Step 2: Save to auto-memory

Write a memory file to the auto-memory directory:

- **Filename**: `ruyos-endday-YYYY-MM-DD.md`
- **Frontmatter**:
  ```yaml
  ---
  name: ruyos-endday-YYYY-MM-DD
  description: "ruyOS end-of-day wrap-up — [brief context]"
  type: project
  ---
  ```
- **Body** — structured as:
  ```markdown
  ## End of day: YYYY-MM-DD
  **Source**: [which Cowork project this was captured from]

  ### Accomplished
  - [what got done today]

  ### Decisions
  - [decisions made, with context/why]

  ### Carry forward
  - [unfinished items for tomorrow]

  ### Tasks completed
  - [tasks that should move to Done.md]

  ### New tasks
  - [tasks that emerged today]

  ### Learnings
  - [writing rules, insights, preferences discovered]
  ```

### Step 3: Tell the user

> Saved end-of-day wrap-up to memory. Next time you open your vault and run `/start-day`, I'll sync everything — daily note, tasks, decisions, and learnings — into the vault.

Done.

---

## Vault mode (vault detected)

### Context sources

Read these files from the vault before executing:

- Workflow/Log/Daily/ (today's daily note)
- Workflow/Tasks/Active.md
- Workflow/Knowledge/Decisions/Decisions.md
- Context/Professional/Writing Preferences.md (for any new rules learned)

### Step 1: Gather context

1. **Today's daily note** — Read `Workflow/Log/Daily/YYYY-MM-DD.md` (today's date).
2. **Active tasks** — Read `Workflow/Tasks/Active.md` to see what was on the list.
3. **Conversation review** — Review this conversation for any decisions, insights, or rules learned during the session.

### Step 2: Write to daily note under `# Summary`

Write to the sections under `# Summary` in today's daily note:

- **`## Log`** — Write or finalize the narrative summary of the day. If end-session already wrote partial log entries, build on them — add any remaining work from the current session and write a cohesive day summary. Write in prose, not bullets.
- **`## Decisions`** — List all significant decisions made today as bullet points. Merge with any decisions already logged by end-session.
- **`## Learnings`** — List insights, tools discovered, rules learned as bullet points with links.
- **`## Tomorrow`** — Flag anything unfinished that should carry forward. Be specific enough that tomorrow's start-day can act on these.

Do NOT touch anything under `# Briefing` — that's start-day's territory.

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

### Step 6: Update open-threads frontmatter

Update the `open-threads` array in today's daily note frontmatter with the items written to `## Tomorrow`. This makes them machine-readable for start-day to pick up.

### Step 7: CLAUDE.md health check

Scan for routing gaps by comparing the vault's actual state against CLAUDE.md:

1. **New files without routes** — List any files created today (check daily note log, new project folders, new context files) that aren't covered by the Knowledge Routing or Save Routing tables in CLAUDE.md. For example, if a new project folder `Projects/Unity Game/` was created today but the routing table still only has the generic `Projects/<project-name>/` entry, that's fine. But if a new top-level category was added (e.g., `Workflow/Knowledge/Patterns/`), the routing table needs updating.

2. **Dead routes** — Check if any paths referenced in CLAUDE.md's routing tables point to files that no longer exist (deleted or renamed during the day).

3. **New living rules** — If any writing rules, communication preferences, or general conventions were established today, check they're reflected in the Living Rules section of CLAUDE.md.

If gaps are found:
- Update CLAUDE.md directly — add new routes, remove dead ones, add new rules.
- Mention the updates briefly in the day summary: "Updated CLAUDE.md: added route for X, removed stale route for Y."

If everything is clean, skip silently.

### Step 8: Day summary

Finish with a quick summary for the user:
- What got done
- What carries forward
- Any decisions logged
- CLAUDE.md updates (if any)

## Daily note structure

The daily note has two top-level sections. Start-day owns `# Briefing`. End-session and end-day own `# Summary`.

```
# Briefing          ← start-day (don't touch)
  ## From yesterday
  ## Inbox
  ## Focus
# Summary           ← end-session / end-day write here
  ## Log             ← narrative prose
  ## Sessions        ← dataview (auto)
  ## Decisions       ← bullet list
  ## Learnings       ← bullet list with links
  ## Tomorrow        ← end-day only
```

## Rules

- Use wikilinks (`[[Note Name]]`) for internal references
- Preserve existing frontmatter when editing notes
- Direct, concise, no fluff
- Don't fabricate — only log what actually happened
- When moving tasks to Done, preserve the task text exactly
- Do NOT touch anything under `# Briefing` (that's start-day)
- Write the Log as narrative prose — tell the story of the day
- The `## Tomorrow` section is end-day exclusive — end-session never writes here
