# MUS 381 — Essentials of Music Technology

Course materials, teaching tools, and TA resources for MUS 381 at CSU East Bay.

This repository is the working hub for an introductory music-technology course taught by Inés Thiebaut (Department of Music, CSU East Bay). It functions as a textbook replacement: syllabus, weekly plans, readings, handouts, listening assignments, projects, and interactive browser-based tools all live here, organized by module.

## Repository structure

Everything for a given module lives in that module's folder. To prep a week of teaching, open the relevant module — readings, handouts, listening, projects, tools, spec, and TA notes are all there.

```
course-outline.md                    Full course outline, schedule, learning outcomes
module-01-fluency/                   Week 1 — computer & studio fluency
module-02-audio-editing-mixing/      Weeks 2–5 — Audacity, editing, mixing → Project 1
module-03-recording/                 Weeks 6–8 — recording & sample library → midterm
module-04-ableton/                   Weeks 9–15 — Ableton audio + MIDI → final
policies/                            Cross-cutting course policies (e.g. NAS archival)
assets/                              Shared CSS, audio, images, videos
build/                               Scripts that generate audio demos and other assets
meta/                                Internal build-time conventions (not student- or TA-facing)
```

Each module folder follows a consistent layout:

```
module-XX-name/
  README.md          The module itself: purpose, learning outcomes, session-by-session teaching notes
  lessons/           Student-facing material in session order: readings, interactive tools, lab handouts
  listening/         Listening assignments (historical + peer)
  projects/          Project prompts and project-specific notes
```

Not every module uses every subfolder — they're added as needed.

## Course at a glance

- **Term:** Fall 2026 (15 weeks, 27 class meetings)
- **Format:** Mondays = lecture, Wednesdays = lab (MB2525)
- **Modules:** 4 (Computer fluency → Audacity → Recording/sampling → Ableton)
- **Deliverables:** Project 1 (musique concrète piece), midterm (sample library + terminology exam), final project, cumulative final exam

See [`course-outline.md`](course-outline.md) for full details.

## Conventions

Build-time conventions (prose rules, document chrome, file naming, dates, visual system) live in [`meta/`](meta/). Anyone working on materials in this repo (Inés, Claude) should consult the relevant file there before drafting; the TA doesn't need to.

The two course-level patterns worth knowing without opening a convention file:

- **Student-facing materials** are HTML, sharing the stylesheet at `assets/style.css`. **Specs and TA notes** are Markdown.
- **File workflow:** Local-first with NAS as sync mechanism — students work in `~/Documents/lastname/`, download from NAS at session start, upload at end.

## License & use

Materials in this repo are developed for instructional use at CSU East Bay. Tools and handouts may be adapted for similar courses with attribution.
