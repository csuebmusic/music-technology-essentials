# Handouts

Student-facing reference materials for use during lab sessions. Lab-specific in nature: things students follow along with at their station, or refer back to during a session.

## Format

All handouts are HTML and share the central stylesheet at [`assets/style.css`](../assets/style.css). The aesthetic is modern minimal with a mechanical-retro tilt: DM Sans for body, DM Mono for accents, warm low-saturation palette, generous whitespace.

This same stylesheet is used by readings, listening assignments, and project prompts — every student-facing document in the course shares one visual system.

## Files

- `01-first-day-setup.html` — Module 1, Wed Aug 19 (first day of class)
- `02-session-routines.html` — Start-of-session and end-of-session reference card, used every session

## Distribution

Handouts are pre-loaded onto each lab machine in `/Users/Shared/Downloads/` for the relevant week, and also linked in Canvas. Students can open them in any browser.

## Authoring

When writing new handouts, use `01-first-day-setup.html` as a template. Maintain the same structural elements:

- `<header class="handout-header">` with course and meta
- `<div class="title-block">` with module tag, title, subtitle
- `<p class="lede">` for opening paragraph
- `<h2>` for major sections, `<h3>` for subsections
- `<ol class="steps">` for numbered procedural steps (renders with monospace numbered chips)
- `<table class="shortcut-table">` for keyboard shortcuts and similar
- `<div class="callout">` for asides; `.callout.warn` for problem-troubleshooting; `.callout.tip` for friendly tips
- `<kbd>` for keys, `<code>` for file names, paths, and code

CSS link path: `../assets/style.css`

## Tone

Beginner-friendly. Explicit micro-steps. No assumed knowledge. Warm without being saccharine. Define every term the first time it appears.

## Prose conventions

All student-facing HTML follows a shared set of prose conventions documented in [`assets/README.md`](../assets/README.md). The most important: no em dashes (use commas, parentheses, colons, or middle dots instead).
