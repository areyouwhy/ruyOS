# CLAUDE.md — ruyOS Brain File

This file is the navigation layer for any AI agent working with this vault. Read this first to understand where to find information and where to save new information.

## What This Is

**ruyOS** is a second brain — an Obsidian vault that serves as the single source of truth for identity, career, work, projects, preferences, decisions, and accumulated knowledge. Any AI agent (Cowork, Claude Code, etc.) that has access to this folder can read and write to it.

## Vault Structure

| Folder | What lives here |
|--------|----------------|
| **Context/** | Everything about you — split into Personal and Professional |
| **Context/Personal/** | Identity, goals, preferences, people, hobbies |
| **Context/Professional/** | Work, career, strategy, brand, writing style, ICP, tech stack |
| **Workflow/** | Everything that flows: logs, tasks, knowledge, captures |
| **Workflow/Log/Daily/** | Daily notes in `YYYY-MM-DD.md` format |
| **Workflow/Log/Meetings/** | Meeting transcripts and notes |
| **Workflow/Tasks/** | Task tracking: active, backlog, done |
| **Workflow/Knowledge/** | Decisions, research findings, insights |
| **Workflow/Capture/** | Quick captures — anything unsorted lands here first |
| **Projects/** | Personal projects — each has an index note + session notes |
| **Settings/** | Vault infrastructure |
| **Settings/Resources/** | Reusable assets: prompts, frameworks, examples, snippets |
| **Settings/Templates/** | Note templates for daily notes, meetings, projects, sessions |
| **Settings/System/** | AI Setup, Computer specs — how ruyOS itself works |

Key root file: this file (AI navigation). Home is at `Workflow/Home.md`.

## Knowledge Routing — Where to Find Things

When you need context to answer a question or complete a task, use this table:

| If you need to know about... | Read this |
|------------------------------|-----------|
| Who the vault owner is | `Context/Personal/About Me.md` |
| Current priorities | `Context/Personal/Current Focus.md` |
| Life goals (short & long term) | `Context/Personal/Goals.md` |
| How the owner likes things done | `Context/Personal/Preferences.md` |
| Key people | `Context/Personal/People.md` |
| Hobbies and interests | `Context/Personal/Interests & Hobbies.md` |
| Career history & skills | `Context/Professional/Work & Career.md` |
| Current job / employer | `Context/Professional/Work.md` |
| Personal strategy & positioning | `Context/Professional/Strategy.md` |
| Brand colors, fonts, voice | `Context/Professional/Brand.md` |
| Writing tone, rules, style | `Context/Professional/Writing Preferences.md` |
| Target audience / reader | `Context/Professional/ICP.md` |
| Audience pain points | `Context/Professional/Pain Points.md` |
| Languages, frameworks, tools | `Context/Professional/Tech Stack.md` |
| Communication style by channel | `Context/Professional/Communication Style.md` |
| A specific project | `Projects/<project-name>/<project-name>.md` |
| What to work on today | `Workflow/Tasks/Active.md` |
| What happened today/recently | `Workflow/Log/Daily/` |
| What happened in a meeting | `Workflow/Log/Meetings/` |
| Past decisions and rationale | `Workflow/Knowledge/Decisions/` |
| Research & competitive intel | `Workflow/Knowledge/Research/` |
| Reusable prompts | `Settings/Resources/Prompts/` |
| Good output examples | `Settings/Resources/Examples/` |
| Hardware & software setup | `Settings/System/Computer Overview.md` |
| How ruyOS works | `Settings/System/AI Setup.md` |
| Note templates | `Settings/Templates/` |

## Save Routing — Where to Store New Information

When you learn something new during a conversation, save it to the right place:

| If you learn... | Save it to |
|-----------------|-----------|
| A writing rule or preference (e.g. "never use em dashes") | `Context/Professional/Writing Preferences.md` → Rules section |
| A decision with rationale | `Workflow/Knowledge/Decisions/` → new note or append to existing |
| Meeting notes or transcript | `Workflow/Log/Meetings/` → `YYYY-MM-DD <meeting-name>.md` |
| A research finding or insight | `Workflow/Knowledge/Research/` or `Workflow/Knowledge/Insights/` |
| A new task or to-do | `Workflow/Tasks/Active.md` |
| A completed task | Move from `Workflow/Tasks/Active.md` to `Workflow/Tasks/Done.md` |
| A useful prompt | `Settings/Resources/Prompts/` |
| A good output example | `Settings/Resources/Examples/` |
| A reusable code snippet | `Settings/Resources/Snippets/` |
| A project update | The project's index note in `Projects/` |
| A priority shift | `Context/Personal/Current Focus.md` |
| Something about a person | `Context/Personal/People.md` |
| An unstructured dump or quick capture | `Workflow/Capture/` |

## Living Rules

Rules that accumulate over time. AI agents must follow these when producing output.

### Writing
- Active voice preferred
- No filler words (just, simply, basically, actually)
- Clear over clever — say what you mean
- Sentence case for headings
- American English spelling

### Communication
- Direct and clear, but knows when nuance is needed
- Adapts to context — different with colleagues, partner, family, friends

### General
- When unsure where to save something, put it in `Workflow/Capture/`
- Always preserve existing frontmatter when editing notes
- Use `[[wikilinks]]` for internal links, markdown links for external URLs

## Conventions

- **Frontmatter**: YAML with `title`, `tags`, `date`, `last-updated`, `status`
- **Wikilinks** (`[[Note Name]]`) for internal linking
- **Daily notes**: `YYYY-MM-DD.md` format in `Workflow/Log/Daily/`
- **Project structure**: Each project is a folder under `Projects/` with an index note
- **Tags**: `context`, `me`, `project`, `work`, `ai`, `knowledge`, `log`, `resource`, `task`, `daily`
- **Callouts**: Obsidian-flavored (`> [!info]`, `> [!warning]`, `> [!tip]`)

## Skill Integration

Skills should reference vault context instead of embedding their own copies. Pattern:

```markdown
## Context Sources
Read these files from the vault before executing:
- Context/Professional/Writing Preferences.md
- Context/Professional/ICP.md
- Context/Professional/Communication Style.md
- Settings/Resources/Examples/<relevant examples>
```

This way, one update to a context file benefits every skill that uses it.
