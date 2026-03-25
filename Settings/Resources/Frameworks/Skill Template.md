---
title: Skill Template
tags:
  - resource
  - framework
  - skill
date:
---

# Skill template

> [!info] Purpose
> Use this template when creating new skills for Claude Code or Cowork. The key principle: skills should point to vault context, not embed their own copies.

## Template

```markdown
---
name: skill-name
description: "When to trigger this skill. Be specific about trigger phrases and use cases."
---

# Skill Name

One-sentence description of what the skill produces or automates.

## Context sources

Read these files from the vault before executing:

- Context/Professional/Writing Preferences.md
- Context/Professional/ICP.md
- [Add other relevant context files]

## What to do

1. [Step 1 — what to do first]
2. [Step 2 — what to do next]
3. [Step 3 — and so on]

## Output format

[Describe what the output should look like — length, structure, tone.]

## Rules

- Follow all rules in Context/Professional/Writing Preferences.md
- [Add skill-specific rules here]
```

## Why this pattern

- **No duplicated context.** When you update Writing Preferences once, every skill that references it gets the update.
- **Faster skill creation.** You only write the process, not the context.
- **Consistent output.** All skills pull from the same voice and style definitions.
