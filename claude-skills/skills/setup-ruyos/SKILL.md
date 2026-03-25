---
name: setup-ruyos
description: "Bootstrap a fresh ruyOS vault. Use when the user says 'set up ruyOS', 'install ruyOS', 'create my vault', 'initialize ruyOS', 'setup', or when this is the first time running in an empty or near-empty directory. Also trigger if the user cloned the ruyOS repo and wants to personalize it."
---

# Setup ruyOS

Bootstrap a working ruyOS vault from scratch, or verify and repair an existing installation.

## What to do

### Step 1: Detect vault state

Check the current working directory for signs of an existing vault:

- Does `CLAUDE.md` exist?
- Does `.ruyos-version` exist?
- Does the folder structure exist (Context/, Workflow/, Projects/, Settings/)?

**If fresh (no CLAUDE.md):** Run full setup (steps 2-6).
**If existing but incomplete:** Run repair — create missing folders and files without overwriting existing content.
**If fully set up:** Tell the user the vault is already configured. Offer to run the personalization interview or a health check.

### Step 2: Scaffold the vault

Create the full folder structure. Skip any folders/files that already exist.

```
Context/Personal/
Context/Professional/
Workflow/Capture/
Workflow/Daily/
Workflow/Intelligence/Decisions/
Workflow/Intelligence/Insights/
Workflow/Intelligence/Meetings/
Workflow/Intelligence/Research/
Workflow/Tasks/
Projects/
Settings/System/
Settings/Resources/Examples/
Settings/Resources/Frameworks/
Settings/Resources/Prompts/
Settings/Resources/Snippets/
Settings/Templates/
.claude/skills/
.claude/commands/
```

### Step 3: Write system files

Create these files if they don't exist (never overwrite):

- `CLAUDE.md` — The brain file with routing tables and living rules
- `.ruyos-version` — Version tracking file
- `Workflow/Home.md` — Vault landing page
- `Settings/System/AI Setup.md` — How ruyOS works
- `Settings/Resources/Resources.md` — Resource index
- `Workflow/Intelligence/Intelligence.md` — Intelligence index
- `Workflow/Intelligence/Decisions/Decisions.md` — Decision log
- All templates in `Settings/Templates/`
- All starter files in `Context/` (empty with frontmatter)
- All task files (`Active.md`, `Backlog.md`, `Done.md`)

Use the contents from `scaffold.json` as the source for generated files. For system files that ship in the repo (CLAUDE.md, templates, etc.), copy them from their locations in the repo.

**Important:** In the repo, skills and commands live in `claude-skills/` (not `.claude/`). This is intentional — `.claude/` would be auto-detected by Claude Code when browsing the repo. During setup, copy `claude-skills/skills/` → `.claude/skills/` and `claude-skills/commands/` → `.claude/commands/`.

### Step 4: Install dependencies

Check for and install required packages:

```bash
# Python packages (for document skills)
pip install --break-system-packages openpyxl pandas python-pptx

# Verify key tools
which pandoc || echo "Note: pandoc not found — some document features may be limited"
which node || echo "Note: node not found — some document features may be limited"
```

Report any missing dependencies but don't fail — the vault works without them, some document skills just won't be available.

### Step 5: Personalization interview

Switch to conversation mode. Explain what's about to happen:

"Your vault is set up. Now let's fill in some context so I can be useful to you from day one. I'll ask a few questions — skip any you'd rather fill in later."

Ask these questions one at a time, waiting for each answer:

1. **"What's your name and what do you do?"**
   → Write to `Context/Personal/About Me.md` (name, role, nutshell)
   → Write to `Context/Professional/Work & Career.md` (current role)

2. **"What are you focused on right now — the main thing on your plate?"**
   → Write to `Context/Personal/Current Focus.md`

3. **"Any bigger goals you're working toward this year?"**
   → Write to `Context/Personal/Goals.md` (This Year section)

4. **"How do you like your writing — formal, casual, direct, something else?"**
   → Write to `Context/Professional/Writing Preferences.md` (Voice/Tone sections)

5. **"Anyone I should know about — colleagues, partners, collaborators you mention often?"**
   → Write to `Context/Personal/People.md`

Each answer writes directly to the vault. If the user says "skip" or similar, move to the next question.

### Step 6: Health check

Verify the vault is functional:

1. CLAUDE.md exists and contains routing tables
2. All required folders exist
3. All starter files have valid frontmatter
4. `.ruyos-version` exists
5. Skills are present in `.claude/skills/`
6. At least one Context file has user content (from the interview)

Report results. If everything passes, suggest: "Want to try starting your day? Say 'start my day' to test the loop."

## Rules

- Never overwrite existing files — check first, create only if missing
- The interview is optional — power users may skip it entirely
- Keep the interview conversational, not form-like
- Works in both Claude Code and Cowork — don't assume either environment
- If the vault is a cloned repo, the scaffold files are already there — just verify and personalize
