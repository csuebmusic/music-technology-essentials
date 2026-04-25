# Handouts

Student-facing course materials for MUS 381.

## Format

All handouts are HTML, sharing a single stylesheet (`handout.css`) for visual consistency. The aesthetic is modern minimal with a mechanical-retro tilt: DM Sans for body, DM Mono for accents, warm low-saturation palette, generous whitespace.

## Files

- `handout.css` — shared stylesheet for all handouts
- `01-first-day-setup.html` — Module 1, Wed Aug 19 (first day of class)

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

## Tone

Beginner-friendly. Explicit micro-steps. No assumed knowledge. Warm without being saccharine. Define every term the first time it appears.
