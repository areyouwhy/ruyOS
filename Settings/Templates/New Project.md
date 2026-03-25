---
title: "{{ project_name }}"
tags:
  - project
status: planning
date: "{{ date }}"
last-updated: "{{ date }}"
directory: "{{ directory_name }}"
context-dependencies: []
---

# {{ project_name }}

## Vision

What is this project and why does it exist?

## Goals

-

## Status

Current state of the project.

## Log

- {{ date }}: Project created

## Session notes

```dataview
TABLE date AS "Date", title AS "Summary"
FROM "Projects/{{ project_name }}"
WHERE contains(tags, "session")
SORT date DESC
```

## See also

-
