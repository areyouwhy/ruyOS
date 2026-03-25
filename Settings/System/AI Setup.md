---
title: AI Setup
tags:
  - ai
  - system
date:
---

# AI setup

How ruyOS works as an AI-powered second brain.

## Philosophy

The vault is the single source of truth. AI agents (Claude via Cowork, Claude Code, or any other provider) read and write to this vault. The CLAUDE.md file at the root is the navigation layer that tells any AI agent how to find and store information.

## Key components

- **CLAUDE.md** — Brain file with knowledge routing and save routing tables
- **Context/Personal/** — Identity, goals, preferences, people
- **Context/Professional/** — Work, strategy, brand, writing style, ICP, tech stack
- **Workflow/Intelligence/** — Accumulated knowledge from meetings, decisions, research
- **Settings/Resources/** — Reusable prompts, frameworks, examples
- **Workflow/Tasks/** — AI-readable task tracking

## Skills

ruyOS ships with workflow skills in `.claude/skills/`:

| Skill | What it does |
|-------|-------------|
| **start-day** | Morning briefing and daily note creation |
| **end-day** | Daily wrap-up, archive, and reflection |
| **end-session** | Checkpoint after a work block or iteration |
| **remember** | Save information to the right vault location |
| **inbox** | Triage items in Workflow/Capture/ to permanent homes |
| **review** | Realign priorities against goals and focus |
| **setup-ruyos** | Bootstrap a fresh vault |
| **update-ruyos** | Pull latest updates from the ruyOS repo |

Skills reference vault context instead of embedding copies. One update to a context file benefits every skill.

## Tips

- Every new Cowork/Claude Code session should point to this vault folder
- When the AI learns a rule or preference, tell it to save it to the right place
- If navigation breaks, update CLAUDE.md — it's the bridge
- Put unsorted captures in Workflow/Capture/ and process later
