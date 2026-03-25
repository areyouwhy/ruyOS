# ruyOS

A second brain that AI agents can read and write to.

ruyOS is an Obsidian vault with an AI skill layer. You fill it with your context — who you are, what you're working on, how you like things done — and AI agents use that context to help you. Skills handle the daily workflow: morning briefings, capturing information, triaging your inbox, reviewing priorities, and wrapping up the day.

## Quick start

### Claude Code

```bash
git clone https://github.com/areyouwhy/ruyOS.git my-vault
cd my-vault
claude
# then run: /setup-ruyos
```

### Cowork

1. Install the ruyOS plugin
2. Open a session and select a folder
3. Say "set up ruyOS"

Both paths run the same setup: scaffold the vault, install skills, and walk you through a short personalization interview.

## Skills

| Skill | What it does |
|-------|-------------|
| **start-day** | Morning briefing and daily note creation |
| **end-day** | Daily wrap-up, archive completed tasks, reflect |
| **end-session** | Checkpoint after a work block or iteration |
| **remember** | Save information to the right place in the vault |
| **inbox** | Triage captures and route them to permanent homes |
| **review** | Realign priorities against goals and focus |
| **setup-ruyos** | Bootstrap a fresh vault from scratch |
| **update-ruyos** | Pull latest updates from this repo |

## How it works

The vault has two layers:

**Context** — Your identity, goals, preferences, career, writing style, and people. AI agents read this to understand you.

**Workflow** — Daily notes, tasks, decisions, insights, and captures. AI agents read and write here as part of the daily loop.

`CLAUDE.md` is the brain file that tells any AI agent where to find and store information. Skills reference vault context instead of embedding their own copies — one update to your writing preferences benefits every skill.

## Vault structure

```
Context/           Who you are (Personal + Professional)
Workflow/          Daily notes, tasks, intelligence, captures
Projects/          Your projects
Settings/          Templates, resources, system config
.claude/skills/    AI skills
.claude/commands/  Slash commands
```

## The daily loop

1. **Start day** — Get a briefing, create today's note
2. **Work** — Claude has your context and helps throughout the day
3. **Remember** — Capture information as it comes up
4. **Inbox** — Triage captures when the pile grows
5. **End session** — Checkpoint when finishing a work block
6. **End day** — Wrap up, archive, reflect
7. **Review** — Periodic realignment (weekly or as needed)

## Updating

Run `/update-ruyos` to check for new skills, templates, or improvements. The update skill diffs your local vault against this repo and lets you choose what to apply. Your personal content is never touched.

## License

MIT
