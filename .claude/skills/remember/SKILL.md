---
name: remember
description: "Save something to a ruyOS vault. Use when the user says 'remember this', 'save this', 'log this', 'note this down', 'store this', or anything that sounds like they want to persist information to their second brain. Also trigger for 'add a rule', 'new task', 'log a decision', or any request to capture information for later."
---

# Remember

Save something to the vault. Determine where the information belongs using the save routing table, then store it in the right place.

## Save routing

Use this table to decide where to save:

| If you learn... | Save it to |
|-----------------|-----------|
| A writing rule or preference | `Context/Professional/Writing Preferences.md` → Living Rules section |
| A decision with rationale | `Workflow/Intelligence/Decisions/` → new note or append to Decisions.md |
| Meeting notes or transcript | `Workflow/Intelligence/Meetings/` → `YYYY-MM-DD <meeting-name>.md` |
| A research finding or insight | `Workflow/Intelligence/Research/` or `Workflow/Intelligence/Insights/` |
| A new task or to-do | `Workflow/Tasks/Active.md` |
| A completed task | Move from `Workflow/Tasks/Active.md` to `Workflow/Tasks/Done.md` |
| A useful prompt | `Settings/Resources/Prompts/` |
| A good output example | `Settings/Resources/Examples/` |
| A reusable code snippet | `Settings/Resources/Snippets/` |
| A project update | The project's index note in `Projects/` |
| A priority shift | `Context/Personal/Current Focus.md` |
| Something about a person | `Context/Personal/People.md` |
| An unstructured dump or quick capture | `Workflow/Capture/` |

## What to do

1. **Determine what's being saved** — Read the user's input and categorize it using the routing table above.
2. **Find the target file** — Navigate to the correct location in the vault.
3. **Save appropriately:**
   - If it's a **new note**, create it with proper frontmatter (`title`, `tags`, `date`).
   - If it's **appending to an existing file**, read the file first, preserve the existing structure, and add to the right section.
4. **Confirm** — Tell the user what was saved and where.

## Rules

- Use wikilinks (`[[Note Name]]`) for internal references
- Always preserve existing frontmatter when editing notes
- When unsure where something goes, put it in `Workflow/Capture/`
- Use the vault's tag conventions: `context`, `me`, `project`, `work`, `ai`, `intelligence`, `resource`, `task`, `daily`
- Keep saves clean and structured — don't dump raw text, format it to match the target file's style
