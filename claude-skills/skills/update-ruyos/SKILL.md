---
name: update-ruyos
description: "Update a ruyOS vault to the latest version. Use when the user says 'update ruyOS', 'check for updates', 'get latest ruyOS', 'upgrade ruyOS', 'sync ruyOS', or anything that sounds like they want to pull the latest skills, templates, or structure from the ruyOS repo."
---

# Update ruyOS

Pull the latest version from the ruyOS GitHub repo, compare with the local vault, and apply changes safely.

## Context sources

- `.ruyos-version` — Current installed version
- `CLAUDE.md` — Current brain file

## What to do

### Step 1: Check current version

Read `.ruyos-version` in the vault root. If it doesn't exist, tell the user this vault may not have been set up with setup-ruyos and suggest running setup first.

### Step 2: Fetch latest version

Pull or fetch the latest from the ruyOS GitHub repo:

```bash
# Clone the latest to a temp directory for comparison
git clone https://github.com/areyouwhy/ruyOS.git /tmp/ruyos-latest
```

Read the `.ruyos-version` from the latest source. Compare with local.

If versions match, tell the user they're up to date and stop (unless they say "force update" or "check anyway").

### Step 3: Diff and categorize changes

Compare the local vault against the latest repo. Categorize every difference:

**New skills** — Skills in the repo's `claude-skills/skills/` that don't exist in the local `.claude/skills/`.

**Updated skills** — Skills that exist in both but have different content. Compare SKILL.md files. Note: the repo stores skills in `claude-skills/skills/` but they install to `.claude/skills/` locally.

**New templates** — Templates in `Settings/Templates/` that don't exist locally.

**Updated templates** — Templates that exist locally but differ from repo. Check if the user has modified them (compare against the version they were installed from, if possible).

**Structural changes** — New folders, new system files (like new routing entries in CLAUDE.md).

**Updated system files** — Changes to AI Setup.md, Resources.md, Intelligence.md, or other system-owned files.

**Obsidian config** — Compare `.obsidian/` between repo and local vault. The repo's `.obsidian/` includes app settings and bundled plugins (calendar, dataview, templater, color-folders-files). Strategy: `skip_if_exists` — only copy files that don't exist locally. Never overwrite user's Obsidian customizations (themes, workspace, hotkeys, etc.).

**Deprecations** — Skills or files in the local vault that no longer exist in the repo.

### Step 4: Present the update plan

Show the user a clear summary:

```
## ruyOS update — v[current] → v[latest]

### New
- [list of new skills, templates, files]

### Updated
- [list of changed skills, templates, system files]

### Deprecated
- [list of removed items, if any]

### Unchanged
- [count] files unchanged
```

For each updated item, briefly note what changed.

### Step 5: Let the user choose

Never force changes. Ask the user what to apply:

- "Apply all" — Apply everything
- "Apply new only" — Only add new items, don't update existing
- Selective — "Apply #1 and #3, skip #2"
- "Skip" — Don't apply anything

### Step 6: Apply changes with merge strategy

Apply selected changes using these rules:

| File type | Strategy | Why |
|-----------|----------|-----|
| **Skills** (`.claude/skills/`) | Replace | System-owned, always take latest |
| **Commands** (`.claude/commands/`) | Replace | System-owned |
| **CLAUDE.md routing entries** | Merge | Append new entries, preserve existing + user additions |
| **CLAUDE.md living rules** | Merge | Append new rules, preserve user-added rules |
| **Templates** (`Settings/Templates/`) | Replace if unmodified, skip if modified | Respect user customizations |
| **System files** (AI Setup.md, etc.) | Replace | System-owned |
| **Obsidian config** (`.obsidian/`) | Skip if exists | Respect user customizations; only add missing files/plugins |
| **Context files** (`Context/`) | Never touch | User-owned content |
| **Workflow files** (tasks, daily notes, etc.) | Never touch | User-owned content |
| **Project files** | Never touch | User-owned content |

When merging CLAUDE.md:
1. Read the current file
2. Read the latest file
3. Identify new routing entries (rows in tables that don't exist locally)
4. Append new entries to the appropriate tables
5. Preserve all existing content, including user-added living rules

### Step 7: Update version

Write the new version to `.ruyos-version`.

### Step 8: Report

Summarize what was applied:
- Items added
- Items updated
- Items skipped
- New version number

If new skills were added, briefly describe what each one does.

## Rules

- Never touch user-owned content (Context/, Workflow/ data, Projects/)
- Always show the plan before applying — no silent changes
- Preserve user modifications to templates
- When merging CLAUDE.md, append don't replace
- If something goes wrong mid-update, report what was applied and what wasn't
- Works in both Claude Code and Cowork
