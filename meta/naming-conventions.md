# Naming conventions

File and folder naming across the repo.

> **Scope:** the whole repo, including student-facing material on the NAS. Naming consistency matters because file paths show up in handouts, in NAS instructions, and on the projector.

## The base rule

Lowercase. Hyphens, not spaces. No special characters (no `&`, `!`, `@`, `#`, `$`, `%`, `(`, `)`, quotes, apostrophes).

This is the same convention taught to students on Day 1 (see Module 1's first-day handout). The repo follows the rule students follow.

## Folder structure

### Top level

```
README.md
course-outline.md
module-01-fluency/
module-02-audio-editing-mixing/
module-03-recording/
module-04-ableton/
policies/
assets/
build/
meta/
```

Module folders are `module-XX-shortname/` where XX is zero-padded (`01`, `02`, etc.) and shortname is a few hyphenated words capturing the module's content. The shortname is meant to make the folder readable in `cd` and `ls` output; it's not load-bearing for any reference.

### Per-module

```
module-XX-name/
  README.md          The module: purpose, learning outcomes, session-by-session teaching notes
  lessons/           Student-facing material in encounter order: readings, interactive tools, lab handouts
  listening/         Listening assignments (historical + peer where applicable)
  projects/          Project prompts and project-specific TA notes
```

Not every module uses every subfolder; they're added as needed.

## Lesson files

Lesson files inside `module-XX-name/lessons/` are numbered by encounter order within the module, with the document type in the filename:

```
01-reading-digital-audio.html
02-tool-digital-audio-explorer.html
03-handout-audacity-orientation.html
04-reading-editing-envelope.html
05-handout-editing-techniques.html
06-handout-mixing-in-audacity.html
07-reading-dynamics.html
08-tool-mixing-dynamics.html
09-reading-audacity-dynamics.html
```

The number is a sort key, not a global ID; it resets at the start of each module. The type word (`reading`, `tool`, `handout`) lets the TA glance at the folder and see the shape of the module without opening anything.

## Listening files

Listening files inside `module-XX-name/listening/` use descriptive shortnames:

```
historical.html
peer-project-01.html
```

The peer-listening filename includes the project number it pairs with (so Module 3 will have `peer-midterm.html` or similar, not `peer-project-02.html` if the midterm isn't formally a "Project 2").

## Project files

Project files inside `module-XX-name/projects/` use `project-NN-shortname.html` for the prompt and `project-NN-shortname-notes.md` for the TA/prep notes:

```
project-01-musique-concrete.html
project-01-sample-bank-notes.md
```

Project numbers are zero-padded and global (Project 1, Project 2 = midterm, Project 3 = final, etc.) — this matches the chrome convention.

## Assets

### Images

```
assets/images/module-XX-week-YY/[descriptive-shortname].[ext]
```

Week numbers are zero-padded. Examples: `module-02-week-02/audacity-settings.png`, `module-02-week-05/wide-vs-narrow.svg`.

Some images sit in week-keyed folders even though they're conceptually module-wide (e.g. Audacity screenshots used across multiple weeks). The week is the week the image was *first generated for*, not a constraint on where it can be used.

### Audio

```
assets/audio/module-XX-week-YY/[descriptive-shortname].wav   <- build-script output
assets/audio/source/[descriptive-shortname].[ext]            <- inputs to build scripts
```

Examples: `module-02-week-02/sr-8k-16bit.wav`, `module-02-week-05/range-wide.wav`, `source/voice-tape-demo.aif`.

The `source/` folder holds real recordings used as inputs to build scripts. Files there are commit-tracked but not regenerable: losing them means losing material.

### Videos

```
assets/videos/module-XX-week-YY/[descriptive-shortname].[ext]
```

Short Audacity screen recordings inlined in readings. Specs in `assets/videos/README.md`.

## Build scripts

```
build/generate-[purpose].py
build/generate-[purpose]-week-YY.py
```

The week suffix is used when there's a script per week of generated assets (e.g. `generate-audio-demos-week-03.py`). For single-purpose scripts that produce one set of assets, the week suffix is dropped (e.g. `generate-audio-demos.py`).

## NAS paths (referenced in handouts)

The lab NAS uses the same convention for the same reason. Paths that appear in student-facing materials:

```
/music/students/[lastname]/                           Student private folders
/music/students/[lastname]/project-NN/                Per-project working folders
/music/shared/sample-banks/project1/                  Project 1 sample bank
/music/shared/mus-381-fall-2026/                      Per-semester shared resources
/music/shared/mus-381-fall-2026/project-NN-pieces/    Class listening folders for each project
/music/shared/module-XX/[purpose]/                    Module-specific shared assets (e.g. orientation samples)
```

The `mus-381-fall-YYYY/` prefix is the only place a semester date appears in a path. Every other path is semester-stable.

## Student submission filenames

The filenames students use when submitting work follow the same lowercase-hyphen rule, with last name first:

```
lastname-projectNN.wav                  Audio deliverables (e.g. lastname-project01.wav)
lastname-projectNN-vN.wav               Versioned working copies (lastname-project01-v3.wav)
lastname-listening-NN.docx              Listening response writeups
lastname-peer-listening-NN.docx         Peer listening writeups
lastname-orientation.wav                Module 1 / 2 orientation deliverables
lastname-hello.m4a                      Module 1 Day 1 recording
```

Project numbers are zero-padded and global (`project01`, `project02`), matching the chrome and project-file conventions. Version numbers are not padded (`v1`, `v2`, `v10`).
