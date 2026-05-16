# Meta

Internal build-time conventions for this repo. Codifies the decisions that keep the course materials visually, structurally, and editorially consistent as they're written.

> **For Inés and Claude only.** The TA does not need to read anything in this folder. Conventions here are scaffolding for building the course, not part of teaching it.

## What's here

- [`prose-conventions.md`](./prose-conventions.md) — writing rules for student-facing HTML: em dashes, chains of negatives, bullet discipline, hedging, beginner-first phrasing
- [`chrome-conventions.md`](./chrome-conventions.md) — document chrome: header / footer roles, title-block tags, lecture / project / handout numbering, subtitles, intro paragraphs
- [`naming-conventions.md`](./naming-conventions.md) — file and folder names: lowercase-hyphen rules, zero-padding, module / lesson / asset paths
- [`date-conventions.md`](./date-conventions.md) — where calendar dates live, where week references go, and the content-vs-schedule test
- [`visual-conventions.md`](./visual-conventions.md) — palette, fonts, CSS variables, SVG inlining rule, per-module audio format standards

## How to use this folder while building

Before drafting anything student-facing, scan the relevant convention file. The files are short and topic-focused so the relevant one is fast to find.

- Drafting a reading or handout → `prose-conventions.md`, `chrome-conventions.md`, `visual-conventions.md`
- Adding new lessons or assets → `naming-conventions.md`
- Writing TA notes or module READMEs → `chrome-conventions.md` (for the H1 line), `date-conventions.md`
- Anything that involves a date → `date-conventions.md`

## Scope notes

Most conventions in this folder apply only to **student-facing material** (the HTML in `module-XX-name/lessons/`, `listening/`, and `projects/`). Internal docs (READMEs, TA notes, module specs, this folder) are written for Inés and the TA and follow their own looser rhythm. Each convention file flags its scope at the top.

The point of the scope distinction is that student-facing material is read by beginners and stylistic friction matters; internal docs are read by people who already know the material and stylistic friction would just make the docs stiffer without making them clearer.
