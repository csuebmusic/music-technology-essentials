# Date conventions

Where calendar dates appear in the repo, and how everything else refers to time.

> **Scope:** the whole repo, every document type.

## The rule

Calendar dates (`Aug 24`, `Sep 16`, etc.) appear **only** in `course-outline.md`.

Re-running this course in a future semester should require editing only that file (and Canvas, externally). Every other reference to time uses a stable positional label that doesn't change between semesters.

## Why

Dates change every semester. If they appear in many places, they have to be updated in many places, and they will inevitably drift. Lecture numbers, project numbers, week numbers, and module thematic labels are all stable across semesters; calendar dates aren't.

## Week references

For everything except `course-outline.md`, use week references:

- **`Day Wk N`** for a specific session: `Mon Wk 2`, `Wed Wk 5`. This is the default and matches the existing TA-notes phrasing.
- **`Wk N`** when day-of-week doesn't matter: `By Wk 3`, `Starting Wk 2`.
- Add role-words ("the lab session," "lecture day") only when the *role* is what's being emphasized, not when position alone identifies the session.

### Examples

- "Project 1 is due Wed Wk 5." (was: "Wed Sep 16")
- "We'll discuss the pieces at the start of class on Mon Wk 6." (was: "Mon Sep 21")
- "Bank uploaded by Wk 3 Wed." (was: "Wed Sep 2")
- "(no Mon Wk 4 session, Labor Day)" (was: "Sep 7, Labor Day")

## Exceptions: when a date is content, not schedule

Some dates describe historical facts or external metadata and don't change between semesters. These stay:

- **Historical citations and bibliography:** `Schaeffer (1948)`, `Hosken (2nd ed., 2015)`, `June 1981` magazine reference. Historical facts.
- **Doc-revision metadata:** `**Last updated:** April 2026` at the top of operational docs. Helps the reader know how stale the doc is.
- **Year labels in timeline diagrams:** `1948`, `~2000`, `today (2026)`. Historical landmarks in a diagram about the history of recording.
- **File path embeds:** `mus-381-fall-2026/`. The semester is part of the path on the NAS.
- **Filename illustrations:** `Screenshot 2026-08-19 at 3.21.45 PM.png`. Demonstrating the macOS default screenshot format.

## The content-vs-schedule test

If you're unsure whether a date is schedule (move it) or content (keep it), the test is: **would this number need to change next semester?**

- Yes → it's schedule, replace it with a week reference.
- No → it's content, keep it.
