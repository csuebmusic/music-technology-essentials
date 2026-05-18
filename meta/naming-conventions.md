# Naming conventions

File and folder naming across the repo.

> **Scope:** the whole repo, including student-facing material on the NAS. Naming consistency matters because file paths show up in handouts, in NAS instructions, and on the projector.

## The base rule

Lowercase. Hyphens, not spaces. No special characters (no `&`, `!`, `@`, `#`, `$`, `%`, `(`, `)`, quotes, apostrophes).

This is the same convention taught to students on Day 1 (see Module 1's first-day handout). The repo follows the rule students follow.

## Placeholder syntax used in this file

When a pattern uses `XX`, `YY`, or `NN`, those are placeholders for a zero-padded two-digit number that gets substituted at use-time. Examples:

- `module-XX-shortname/` → `module-01-fluency/`, `module-02-audio-editing-mixing/`
- `module-XX-week-YY/` → `module-02-week-03/`
- `project-NN-shortname.html` → `project-01-musique-concrete.html`
- `lastname-projectNN.wav` → `lastname-project01.wav`

Note: `XX` and `NN` are interchangeable as "zero-padded number" placeholders; the letter choice in this file just helps disambiguate when multiple numbers appear in one pattern (e.g. `module-XX-week-YY/` makes it clear which number is the module and which is the week). They're not meaningful tokens to the filesystem.

`[bracketed-words]` are placeholders for arbitrary user-supplied content (a last name, a descriptive shortname, etc.) and are not zero-padded numbers.

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
/music/students/[lastname]/sample-library/            Per-student sample library (Module 3 onward)
/music/shared/sample-banks/project-01/                Project 1 sample bank
/music/shared/mus-381-fall-2026/                      Per-semester shared resources
/music/shared/mus-381-fall-2026/project-NN-pieces/    Class listening folders for each project
/music/shared/module-XX/[purpose]/                    Module-specific shared assets (e.g. orientation samples)
```

The `mus-381-fall-YYYY/` prefix is the only place a semester date appears in a path. Every other path is semester-stable.

## Sample library files

Starting in Module 3 Wk 6, every student builds and maintains a personal sample library on the NAS at `students/[lastname]/sample-library/`. Filenames inside the library follow a category-descriptor-variant pattern:

```
[category]-[descriptor]-[variant].wav
```

- **category** — the high-level kind of sound; matches the folder it lives in. Examples: `paper`, `metal`, `water`, `voice`, `field`.
- **descriptor** — what the sound is, in a word or two. Examples: `crumble`, `rip`, `clang`, `drip`, `hum`.
- **variant** — what distinguishes this take from sibling takes of the same descriptor. Examples: `slow`, `fast`, `close`, `far`, `dry`, `wet`.

Lowercase, hyphens between words, no spaces, no special characters. Same base rule as everywhere in the repo.

Worked examples:

```
sample-library/
  paper/
    paper-crumble-slow.wav            Module 3 Wk 6 starter library
    paper-crumble-fast.wav
    paper-rip-slow.wav
    paper-rip-fast.wav
  metal/
    metal-pan-strike-soft.wav         Hypothetical Wk 7 additions
    metal-pan-strike-hard.wav
    metal-wire-scrape-slow.wav
```

The variant slot is optional when there's only one take of a descriptor (`metal-fork-drop.wav` is fine if there's no sibling); add it when sibling variants exist. If a student records a third or fourth variant of a descriptor and the slow/fast axis runs out, use a noun-shaped variant instead (`paper-crumble-slow.wav`, `paper-crumble-fast.wav`, `paper-crumble-corner.wav`, `paper-crumble-edge.wav`). The rule isn't a fixed taxonomy; it's a discipline of meaningful distinctions.

The category is also the folder. `paper-crumble-slow.wav` lives in `paper/`. The redundancy is intentional: the file is identifiable on its own (without the folder context) and the folder is browsable on its own (without renaming files when reorganizing).

All samples in the library are mono, 44.1 kHz, 16-bit WAV, prepped through the denoise / trim / normalize pipeline (see the Module 3 Wk 6 lab handout).

## Student submission filenames

The filenames students use when submitting work follow the same lowercase-hyphen rule, with last name first:

```
lastname-projectNN.wav                  Audio deliverables (e.g. lastname-project01.wav)
lastname-projectNN-vN.wav               Versioned working copies (lastname-project01-v3.wav)
lastname-listening-NN.docx              Historical listening writeups (NN = module number)
lastname-peer-listening-NN.docx         Peer listening writeups (NN = project number being responded to)
lastname-orientation.wav                Module 1 / 2 orientation deliverables
lastname-hello.m4a                      Module 1 Day 1 recording
```

Project numbers are zero-padded and global (`project01`, `project02`), matching the chrome and project-file conventions. Version numbers are not padded (`v1`, `v2`, `v10`).

### Hyphen rule for project references

The token `project01` in filenames does **not** take an internal hyphen, but the same project referenced as a folder name does:

- Filename: `lastname-project01.wav`
- Folder name: `project-01/`, `project-01-pieces/`, `sample-banks/project-01/`

Treat the filename's hyphen as the separator between last name and project token; inside the project token, no further hyphen. In folder names, the hyphen reads as a visual break between the word `project` and the number, since folder names tend to be longer and read better with the hyphen.

This means `~/Documents/lastname/project-01/lastname-project01.wav` is the canonical full path for a student's Project 1 working file: hyphenated folder, unhyphenated filename.

### Listening filename NN meaning

The `NN` in listening filenames is overloaded across the two assignment types:

- **Historical listening (one per module):** `NN` = module number (`lastname-listening-02.docx` is the Module 2 historical listening writeup, `lastname-listening-03.docx` will be Module 3, and so on).
- **Peer listening (tied to a specific project):** `NN` = the project number being responded to (`lastname-peer-listening-01.docx` is the peer listening on Project 1 pieces, the Module 3 midterm peer-listening becomes `lastname-peer-listening-02.docx` if the midterm sample library counts as Project 2 in the global numbering).

The two assignments are different enough (one is per-module, one is per-project) that giving them different placeholder meanings reads more clearly than forcing both onto the same axis.
