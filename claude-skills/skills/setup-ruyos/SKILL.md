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
<vault-path>/Workflow/Log/Daily/
<vault-path>/Workflow/Log/Meetings/
<vault-path>/Workflow/Knowledge/Decisions/
<vault-path>/Workflow/Knowledge/Insights/
<vault-path>/Workflow/Knowledge/Research/
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

**Manifest:** Copy `.ruyos-manifest.json` from the repo to the vault root. This file contains SHA-256 hashes of every installed file. The update skill uses it to detect changes without reading every file.

```bash
cp <repo-path>/.ruyos-manifest.json <vault-path>/.ruyos-manifest.json
```

### Step 5b: Brand skills and commands with vault name

**THIS STEP IS MANDATORY.** After copying skills and commands, stamp the vault name as a `[prefix]` so the user can identify their commands in autocomplete and skill lists. Without this, ruyOS commands are indistinguishable from other sources.

**Save the vault name to config:** Create `<vault-path>/.ruyos-config.json`:

```json
{
  "vault_name": "<vault-name>"
}
```

**Then run this Python script** to brand ALL skills and commands. Use Python, not sed — sed behaves differently on macOS vs Linux.

```python
import json, glob, os

VAULT = "<vault-path>"
VAULT_NAME = "<vault-name>"  # from Step 2

# Save config
with open(os.path.join(VAULT, ".ruyos-config.json"), "w") as f:
    json.dump({"vault_name": VAULT_NAME}, f, indent=2)

prefix = f"[{VAULT_NAME}] "

# Brand skill descriptions in YAML frontmatter
for skill in glob.glob(os.path.join(VAULT, ".claude/skills/*/SKILL.md")):
    with open(skill, "r") as f:
        content = f.read()
    # Remove any existing branding first (handles re-runs and name changes)
    import re
    content = re.sub(r'(description:\s*")\[.*?\]\s*', r'\1', content)
    # Add the prefix
    content = re.sub(r'(description:\s*")', rf'\1{re.escape(prefix)}', content)
    with open(skill, "w") as f:
        f.write(content)

# Brand command descriptions (first line of each .md file)
for cmd in glob.glob(os.path.join(VAULT, ".claude/commands/*.md")):
    with open(cmd, "r") as f:
        lines = f.readlines()
    if not lines:
        continue
    # Remove any existing branding from first line
    first = re.sub(r'^\[.*?\]\s*', '', lines[0])
    lines[0] = prefix + first
    with open(cmd, "w") as f:
        f.writelines(lines)

print(f"Branded {len(glob.glob(os.path.join(VAULT, '.claude/skills/*/SKILL.md')))} skills and {len(glob.glob(os.path.join(VAULT, '.claude/commands/*.md')))} commands with [{VAULT_NAME}]")
```

**What this looks like in practice:**

```
# Skills — visible in Cowork skill list and Claude Code
description: "[The Monster] Morning briefing and daily note creator..."

# Commands — visible in Claude Code autocomplete
[The Monster] Start my day. Run the start-day skill...
```

Searching the vault name in autocomplete finds all your commands instantly.

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

### Step 7: Install Obsidian and dependencies

#### Obsidian

Check if Obsidian is installed. If not, install it automatically (ask permission first).

**macOS:**
```bash
# Check if installed
if [ ! -d "/Applications/Obsidian.app" ]; then
    echo "Obsidian not found. Installing..."
    # Download latest universal DMG
    curl -L -o /tmp/Obsidian.dmg "https://github.com/obsidianmd/obsidian-releases/releases/latest/download/Obsidian-universal.dmg"
    hdiutil attach /tmp/Obsidian.dmg -quiet
    cp -r "/Volumes/Obsidian/Obsidian.app" /Applications/
    hdiutil detach "/Volumes/Obsidian" -quiet
    rm /tmp/Obsidian.dmg
    echo "Obsidian installed to /Applications"
fi
```

**Linux:**
```bash
# Check if installed
if ! command -v obsidian &>/dev/null; then
    echo "Obsidian not found. Installing via snap..."
    sudo snap install obsidian --classic
fi
```

**Windows (WSL/PowerShell):**
```powershell
# Download installer
Invoke-WebRequest -Uri "https://github.com/obsidianmd/obsidian-releases/releases/latest/download/Obsidian.exe" -OutFile "$env:TEMP\Obsidian.exe"
Start-Process "$env:TEMP\Obsidian.exe" -Wait
```

If auto-install fails or the user declines, provide the download link: https://obsidian.md/download and continue with the rest of setup. Obsidian is not required to complete setup — the vault works without it, the user can install it later.

#### Other dependencies

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

If everything passes:

1. **Open the vault in Obsidian automatically** (if Obsidian is installed):
   ```bash
   # macOS
   open "obsidian://open?path=<vault-path>"
   # Linux
   xdg-open "obsidian://open?path=<vault-path>"
   ```

2. If Obsidian prompts about "Trust author and enable plugins", tell the user to click **Trust** — the bundled plugins (calendar, dataview, templater, color-folders-files) are safe and needed for the full experience.

3. Tell the user: "Your vault is ready at `<vault-path>`. I've opened it in Obsidian. Try 'start my day' to test the loop."

## Rules

- NEVER scaffold inside the repo — always create the vault in a separate location
- Never overwrite existing files — check first, create only if missing
- The interview is optional — power users may skip it entirely
- Keep the interview conversational, not form-like
- Works in both Claude Code and Cowork — don't assume either environment
- Always confirm the vault path before creating anything
