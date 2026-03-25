---
name: review
description: "Priority review and realignment for a ruyOS vault. Use when the user says 'review priorities', 'realign', 'weekly review', 'am I on track', 'what should I focus on', 'priority check', 'review my goals', or anything that sounds like checking alignment between current work and stated goals. Also trigger for 'what am I missing', 'should I reprioritize', or periodic reflection."
---

# Review

Analyze alignment between current work, stated priorities, and goals. Surface observations and facilitate realignment.

## Vault detection

Before doing anything, check if the current workspace is a ruyOS vault:

1. Look for `CLAUDE.md` at the workspace root containing the word "ruyOS"
2. Look for the `Workflow/` folder

**If BOTH exist** → this is a ruyOS vault. Proceed normally below.
**If EITHER is missing** → tell the user:

> Priority review needs direct access to the vault — it reads your tasks, goals, focus, and daily notes. Please open your ruyOS vault folder in Cowork and run `/review` from there.

Then stop. Do not attempt to review from outside the vault.

---

## Context sources

Read ALL of these before starting:

- Context/Personal/Current Focus.md
- Context/Personal/Goals.md
- Workflow/Tasks/Active.md
- Workflow/Tasks/Backlog.md
- Recent daily notes (last 5-7 files in `Workflow/Log/Daily/`, sorted by date)
- Recent decisions (`Workflow/Knowledge/Decisions/`)

## What to do

### Step 1: Build the full picture

Read every context source listed above. Take note of:

- What the user says their focus is (Current Focus.md)
- What their goals are (Goals.md)
- What they're actually working on (Active tasks, recent daily notes)
- What decisions they've been making (Decisions/)
- What's been sitting untouched (stale tasks, backlog items)

### Step 2: Analyze alignment

Look for these patterns:

**Focus drift** — Are active tasks and recent daily note logs aligned with what Current Focus says? If the user declared "primary focus: launch product" but spent the week on admin tasks, surface that.

**Orphaned goals** — Are there goals in Goals.md with no supporting tasks in Active or Backlog? These are aspirations with no action.

**Task staleness** — Are there tasks in Active.md that haven't shown up in any daily note log for 7+ days? They may need to be moved to Backlog or killed.

**Backlog opportunities** — Are there Backlog items that now align with current focus and should be promoted to Active?

**Decision patterns** — Do recent decisions support or contradict stated priorities?

**Overcommitment** — Are there too many active tasks relative to what's being completed? Signs: growing Active list, few items moving to Done.

### Step 3: Present findings

Share observations as honest, non-judgmental insights. Frame as "here's what I see" — the user decides what to do about it.

Structure:

**Alignment check** — Where current work matches stated focus and goals. Acknowledge what's working.

**Drift or gaps** — Where things seem misaligned. Be specific: "Your focus says X, but the last 5 daily notes show mostly Y work."

**Stale items** — Tasks or goals that aren't getting attention. Ask whether they should stay, be backlogged, or be dropped.

**Opportunities** — Backlog items worth promoting, or connections between goals and available tasks.

### Step 4: Facilitate decisions

Ask the user what they want to adjust. Common actions:

- Update Current Focus.md with new priorities
- Move tasks between Active and Backlog
- Remove tasks that are no longer relevant
- Add new tasks to support orphaned goals
- Acknowledge intentional drift ("yes, I shifted focus on purpose")

### Step 5: Apply changes

After the user decides:

1. Update `Context/Personal/Current Focus.md` with agreed changes
2. Move tasks between `Active.md` and `Backlog.md` as decided
3. Remove or archive tasks that were killed
4. Log the review itself as a decision in `Workflow/Knowledge/Decisions/` if significant priority shifts were made

### Step 6: Summary

Close with a brief summary of what changed and the updated priority landscape.

## Rules

- Observations, not instructions — the user decides priorities
- Be honest about drift, but not judgmental — drift is often intentional
- Always acknowledge what IS working before surfacing gaps
- Use specific evidence from the vault, not vague assessments
- Use wikilinks (`[[Note Name]]`) for internal references
- Preserve existing frontmatter when editing notes
