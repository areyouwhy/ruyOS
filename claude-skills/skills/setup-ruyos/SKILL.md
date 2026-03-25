---
name: setup-ruyos
description: "Bootstrap a fresh ruyOS vault. Use when the user says 'set up ruyOS', 'install ruyOS', 'create my vault', 'initialize ruyOS', 'setup', or when this is the first time running in an empty or near-empty directory. Also trigger if the user cloned the ruyOS repo and wants to personalize it."
---

# Setup ruyOS

Bootstrap a working ruyOS vault in a dedicated folder, separate from the repo.

## Important: repo vs. vault

The ruyOS repo (where this skill lives) is NOT the vault. The repo contains the source files — skills, templates, scaffold definition. The vault is a separate folder where the user's personal content lives. Never scaffold Context/, Workflow/, Projects/ inside the repo itself.

## What to do

### Step 1: Detect context

Determine where you're running:

- **Current directory has `scaffold.json`?** → You're in the ruyOS repo. The vault needs to be created elsewhere.
- **Current directory has `CLAUDE.md` with routing tables and `Context/` folder?** → You're already inside a vault. Offer repair or re-personalization.
- **Current directory is empty or unrelated?** → Treat as a fresh vault location.

### Step 2: Ask where to create the vault

If running from the repo (scaffold.json exists), ask the user two things:

1. **"What do you want to name your vault?"**
   Default: `ruyos`
   This becomes the folder name.

2. **"Where should I create it?"**
   Default: `~/Documents/<vault-name>`
   On macOS: `~/Documents/<vault-name>`
   On Windows: `~/Documents/<vault-name>`
   The user can provide any path.

Confirm the full path before proceeding: "I'll create your vault at `~/Documents/ruyos`. Sound good?"

If the folder already exists and contains vault files, offer repair instead of overwriting.

### Step 3: Locate the repo source

The setup skill needs the repo to copy files from. Determine the repo path:

- If running from the repo directory: use current directory
- If running from elsewhere: check if the repo was cloned nearby, or clone it:
  ```bash
  git clone https://github.com/areyouwhy/ruyOS.git /tmp/ruyos-repo
  ```

Store the repo path for use in later steps.

### Step 4: Scaffold the vault

Create the full folder structure at the vault path. Read the `folders` array from `scaffold.json` in the repo:

```
<vault-path>/Context/Personal/
<vault-path>/Context/Professional/
<vault-path>/Workflow/Capture/
<vault-path>/Workflow/Daily/
<vault-path>/Workflow/Intelligence/Decisions/
<vault-path>/Workflow/Intelligence/Insights/
<vault-path>/Workflow/Intelligence/Meetings/
<vault-path>/Workflow/Intelligence/Research/
<vault-path>/Workflow/Tasks/
<vault-path>/Projects/
<vault-path>/Settings/System/
<vault-path>/Settings/Resources/Examples/
<vault-path>/Settings/Resources/Frameworks/
<vault-path>/Settings/Resources/Prompts/
<vault-path>/Settings/Resources/Snippets/
<vault-path>/Settings/Templates/
<vault-path>/.claude/skills/
<vault-path>/.claude/commands/
```

### Step 5: Copy system files from repo

Copy these files from the repo to the vault (never overwrite existing):

- `CLAUDE.md` → `<vault-path>/CLAUDE.md`
- `.ruyos-version` → `<vault-path>/.ruyos-version`
- `Settings/Templates/*` → `<vault-path>/Settings/Templates/`
- `Settings/System/AI Setup.md` → `<vault-path>/Settings/System/`
- `Settings/Resources/Resources.md` → `<vault-path>/Settings/Resources/`
- `Settings/Resources/Frameworks/Skill Template.md` → `<vault-path>/Settings/Resources/Frameworks/`

**Skills and commands:** In the repo these live in `claude-skills/` (not `.claude/`). Copy them to the vault's `.claude/`:

```bash
cp -r <repo-path>/claude-skills/skills/* <vault-path>/.claude/skills/
cp -r <repo-path>/claude-skills/commands/* <vault-path>/.claude/commands/
```

**Obsidian config and plugins:** Copy the `.obsidian/` directory from the repo to the vault. This includes app settings, core/community plugin lists, and bundled plugins (calendar, dataview, templater, color-folders-files):

```bash
cp -r <repo-path>/.obsidian <vault-path>/.obsidian
```

This gives users a working Obsidian setup out of the box — daily notes configured, templates pointed at the right folder, and community plugins ready to enable.

### Step 6: Generate starter files

Read `scaffold.json` → `generated_files.files` array. For each entry, create the file at `<vault-path>/<path>` using the frontmatter, heading, and body defined in the manifest. Skip any file that already exists.

Format for each generated file:

```markdown
---
title: <frontmatter.title>
tags:
  - <each tag>
date: <today's date>
---

# <heading>

<body>
```

### Step 7: Install dependencies

Check for and install required packages:

```bash
# Python packages (for document skills)
pip install --break-system-packages openpyxl pandas python-pptx

# Verify key tools
which pandoc || echo "Note: pandoc not found — some document features may be limited"
which node || echo "Note: node not found — some document features may be limited"
```

Report any missing dependencies but don't fail — the vault works without them, some document skills just won't be available.

### Step 8: Personalization interview

Switch to conversation mode. Explain what's about to happen:

"Your vault is set up at `<vault-path>`. Now let's fill in some context so I can be useful to you from day one. I'll ask a few questions — skip any you'd rather fill in later."

Ask these questions one at a time, waiting for each answer:

1. **"What's your name and what do you do?"**
   → Write to `<vault-path>/Context/Personal/About Me.md` (name, role, nutshell)
   → Write to `<vault-path>/Context/Professional/Work & Career.md` (current role)

2. **"What are you focused on right now — the main thing on your plate?"**
   → Write to `<vault-path>/Context/Personal/Current Focus.md`

3. **"Any bigger goals you're working toward this year?"**
   → Write to `<vault-path>/Context/Personal/Goals.md` (This Year section)

4. **"How do you like your writing — formal, casual, direct, something else?"**
   → Write to `<vault-path>/Context/Professional/Writing Preferences.md` (Voice/Tone sections)

5. **"Anyone I should know about — colleagues, partners, collaborators you mention often?"**
   → Write to `<vault-path>/Context/Personal/People.md`

Each answer writes directly to the vault. If the user says "skip" or similar, move to the next question.

### Step 9: Health check

Verify the vault is functional:

1. `<vault-path>/CLAUDE.md` exists and contains routing tables
2. All required folders exist
3. All starter files have valid frontmatter
4. `.ruyos-version` exists and contains a date in `YYYY.MM.DD` format
5. Skills are present in `<vault-path>/.claude/skills/`
6. At least one Context file has user content (from the interview)

Report results and the vault path.

If everything passes, suggest: "Your vault is ready at `<vault-path>`. Open it in Obsidian or point Claude Code at it. Try 'start my day' to test the loop."

## Rules

- NEVER scaffold inside the repo — always create the vault in a separate location
- Never overwrite existing files — check first, create only if missing
- The interview is optional — power users may skip it entirely
- Keep the interview conversational, not form-like
- Works in both Claude Code and Cowork — don't assume either environment
- Always confirm the vault path before creating anything
