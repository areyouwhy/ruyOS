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

Read `.ruyos-version` in the vault root. The version is a date in `YYYY.MM.DD` format (e.g. `2026.03.25`). If it doesn't exist, tell the user this vault may not have been set up with setup-ruyos and suggest running setup first.

### Step 2: Fetch latest version

Pull or fetch the latest from the ruyOS GitHub repo:

```bash
# Clone the latest to a temp directory for comparison
git clone https://github.com/areyouwhy/ruyOS.git /tmp/ruyos-latest
```

Read the `.ruyos-version` from the latest source. Display both versions to the user, then **always proceed to Step 3 to diff the actual files** — even if the versions match. The version is a label, not a gate. Real changes are detected by comparing file contents, not version strings. Only skip the diff if the user explicitly says "never mind" or cancels.

### Step 3: Diff using manifests

The fast path. Instead of reading every file, compare two small JSON files:

1. **Local manifest** — Read `<vault>/.ruyos-manifest.json` (written at install/update time)
2. **Repo manifest** — Read `/tmp/ruyos-latest/.ruyos-manifest.json` (from the cloned repo)

Compare every entry by hash. Categorize into:

**New files** — In repo manifest but not in local manifest. These need to be created. For `content_file` and `obsidian` sources, copy from the repo (remember: `claude-skills/skills/` in repo → `.claude/skills/` in vault). For `generated_file` sources, render from `scaffold.json` definitions.

**Changed files** — In both manifests but hashes differ. The repo version is newer. Apply based on `merge_strategy`:
- `replace` → overwrite with repo version
- `merge` → append new content (e.g. CLAUDE.md routing entries)
- `skip_if_modified` → check if user modified the file (hash their current file against the local manifest hash — if they match, safe to replace; if they differ, user customized it, skip)
- `never_touch` → skip entirely
- `skip_if_exists` → skip (file exists)

**Removed files** — In local manifest but not in repo manifest. Flag as deprecated for the user to decide.

**Unchanged** — Hashes match. Skip entirely.

Also check `scaffold.json` → `folders` for any new folders that need to be created.

If `.ruyos-manifest.json` is missing from the vault (pre-manifest install), fall back to reading files directly and comparing against the repo. After the update, write the manifest so future updates are fast.

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
| **Generated files** (hub pages, etc.) | Per scaffold.json | `replace` = always update, `never_touch` = skip, `skip_if_modified` = check first |
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

### Step 7: Re-brand updated skills and commands

After applying changes, re-stamp the vault name prefix on any new or updated skills and commands. This ensures new skills added by the update are immediately identifiable in autocomplete.

**Read the vault name** from `<vault>/.ruyos-config.json` → `vault_name` field. If the config file doesn't exist (pre-branding install), ask the user what their vault is called, then create the config file.

**Brand skills:** For every `SKILL.md` in `<vault>/.claude/skills/*/` that was added or updated in this run, find the `description:` line in the frontmatter and prepend `[<vault-name>]` to the description string — but only if it's not already branded.

```bash
VAULT_NAME=$(python3 -c "import json; print(json.load(open('<vault>/.ruyos-config.json'))['vault_name'])")

for skill in <vault>/.claude/skills/*/SKILL.md; do
  if ! grep -q "description: \"\\[$VAULT_NAME\\]" "$skill"; then
    sed -i "s/description: \"/description: \"[$VAULT_NAME] /" "$skill"
  fi
done
```

**Brand commands:** For every `.md` file in `<vault>/.claude/commands/` that was added or updated, prepend `[<vault-name>]` to the first line — but only if not already branded.

```bash
for cmd in <vault>/.claude/commands/*.md; do
  if ! head -1 "$cmd" | grep -q "^\[$VAULT_NAME\]"; then
    sed -i "1s/^/[$VAULT_NAME] /" "$cmd"
  fi
done
```

This keeps all ruyOS commands consistently branded even as new skills are added in updates.

### Step 8: Update version and manifest

Write the new version to `.ruyos-version` and copy the repo's `.ruyos-manifest.json` to the vault, replacing the old one. This ensures the next update can diff efficiently against what was just installed.

### Step 9: CLAUDE.md health check

After applying updates, verify the brain file is in sync with the vault's current state:

1. **New routes needed** — If the update added new folders, files, or structural changes (e.g., a new `Workflow/Knowledge/Patterns/` folder), check that CLAUDE.md's Knowledge Routing and Save Routing tables have entries pointing to them. Add any missing routes.

2. **Dead routes** — If the update removed or renamed files/folders, check that CLAUDE.md doesn't still point to the old paths. Fix any stale routes.

3. **New conventions** — If the update introduced new tags, frontmatter fields, or structural conventions, add them to the Conventions section of CLAUDE.md.

4. **Skill Integration section** — Verify the Skill Integration section still accurately describes how skills should reference vault context.

Update CLAUDE.md directly for any gaps found. This ensures the navigation layer stays accurate after every update, not just at end-of-day.

### Step 10: Report

Summarize what was applied:
- Items added
- Items updated
- Items skipped
- New version number
- CLAUDE.md updates (if any)

If new skills were added, briefly describe what each one does.

## Rules

- Never touch user-owned content (Context/, Workflow/ data, Projects/)
- Always show the plan before applying — no silent changes
- Preserve user modifications to templates
- When merging CLAUDE.md, append don't replace
- If something goes wrong mid-update, report what was applied and what wasn't
- Works in both Claude Code and Cowork
