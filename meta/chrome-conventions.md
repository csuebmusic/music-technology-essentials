# Chrome conventions

How every document in the repo identifies itself: header / footer roles, title-block module tags, numbering, subtitles, intro paragraphs.

> **Scope:** all documents. The patterns differ between HTML (student-facing) and Markdown (internal), but every document is covered.

## The pattern

`Module XX · Role` — module-tagged context first, role within the module second. Modules are zero-padded (`Module 01`, `Module 02`); roles are not (`Lecture 1`, `Project 1`, `Handout 1`).

For documents that aren't tied to a single module (e.g. a lab reference card used all semester), the leading word is the context type (`Lab`), followed by the document's role.

## HTML files (student-facing)

The header `<span class="meta">` and the matching footer span both contain the role line for the document. They identify the document without dating it.

| Document type | Header / footer right span |
|---|---|
| Reading (Monday lecture) | `Module XX · Lecture N` |
| Reading (supplement to a lecture) | `Module XX · Lecture N (supplement)` |
| Lab handout (paired with a specific lab session) | `Module XX · Lab N` |
| Generic module-tied handout | `Module XX · Handout N` |
| Interactive tool | `Module XX · Tool N` |
| Listening assignment | `Module XX · Listening` |
| Peer listening assignment | `Module XX · Peer listening` |
| Project prompt | `Module XX · Project N` |
| Module-agnostic handout (used all semester) | `Lab · Reference card` |

### Numbering rules

All within-module counts reset at the module boundary. Most numbers are within-module; project numbers are the exception (global, since projects build on each other across the semester).

- **Lecture numbers** count Monday lectures within a module. Mon Wk 2 in Module 2 is Lecture 1, Mon Wk 3 is Lecture 2, etc.
- **Supplement readings** carry the parent lecture's number with `(supplement)` appended. Example: `Lecture 3 (supplement)` for a reading that backs up Lecture 3.
- **Lab numbers** count Wednesday lab sessions within a module. Module 2 has three lab sessions and three Lab-numbered handouts (Lab 1 → Lab 2 → Lab 3). Used when a module has multiple labs and the number serves as session-navigation help.
- **Handout numbers** count handouts within a module when the document is module-tied but not paired with a single lab session. Used when a module has multiple module-wide handouts and the number serves as a within-module disambiguator. No document currently uses this pattern; the slot is reserved for future module-tied handouts that aren't paired with a specific Wednesday lab. (Module 1's `Your First Day` document was previously chromed `Handout 1` and has since been reclassified as `Lecture 1`, since the Mon Wk 1 session is a lecture-style reading even though it's also operationally guided.)
- **Tool numbers** count interactive tools within a module. Module 2's digital audio explorer is Tool 1; its dynamics tool is Tool 2.
- **Project numbers** count globally across the semester. Project 1 (Module 2), Project 2 (Module 3 midterm), etc.

### When to choose Lab N vs Handout N for a module-tied handout

If the module has multiple labs (Wednesday sessions) and the handout is the principal document for a specific one of them, use `Lab N`, where N is which lab in the module. This matches Module 2's pattern and helps the TA and students quickly navigate to "the handout for Wednesday two."

If the handout isn't tied to a specific lab session (e.g. a "general orientation" handout used across multiple weeks of the module), use `Handout N`, where N counts handouts within the module.

The distinction is about whether the number provides session-navigation value. If yes → Lab. If no → Handout.

### Title block

The title block's module tag (`<div class="module-tag">`) carries the module's *thematic* label (e.g. `Module 02 · Digital audio, editing & mixing`), shared across all documents in a module.

The title block's subtitle is a one-sentence description of the document's content. **Subtitles do not contain dates.** Schedules shift each semester; positional labels and content descriptions don't.

### Intro paragraph

The intro paragraph (the first `<p>` after the title block) is **exactly one paragraph at lede size** (`<p class="lede">`).

If the intro feels like it wants to be two paragraphs, either merge them into one (sometimes a sentence reorder is enough) or push the second one past the first `<hr>` so it visually belongs to the body, not the intro. Two paragraphs at different sizes back-to-back makes the page look like the second one was an afterthought.

### Today's gear callout

Every student-facing HTML document that students use during a lab session opens with a **Today's gear** callout, placed immediately after the lede paragraph and before the first `<h2>` or `<hr>`. The callout names what students need to take from the lab's gear storage for today's session.

This callout exists because the gear list used to drift inside the body prose of every handout. Centralizing it at the top of each file gives it one place per session, easy to update, easy to skip past once internalized.

Three gear tiers, mapped across file type and module:

| File type | Gear list |
|---|---|
| Reading (Mon lecture) | audio interface, headphones |
| Interactive tool | audio interface, headphones |
| Module 2 lab handout | audio interface, headphones |
| Module 3 lab handout | audio interface, headphones, dynamic mic (with stand and XLR cable) |
| Module 4 lab handout | audio interface, headphones, MIDI keyboard |

The Module 3 recording-lab variant uses the inline "(with stand and XLR cable)" parenthetical rather than listing the stand and cable as separate items, since the mic-stand-cable triplet is a unit (you can't use any one of them without the other two).

The callout markup is always the same:

```html
<div class="callout">
  <div class="callout-label">Today's gear</div>
  <p>Take from the lab's gear storage: <strong>[gear list]</strong>. Plug in and run through the start-of-session steps on the laminated <strong>Session Routines</strong> card before continuing here.</p>
</div>
```

Files that don't get the callout:
- The Session Routines card itself (it's the card the callout references)
- The Day 1 reading (`01-reading-first-day-setup.html`), since it teaches the take-out cycle from scratch with its own walkthrough
- Listening pages and project prompts (consulted at home, across sessions; gear context is the day's lab handout, not these files)

Once the callout is present, the body prose should not redundantly list the gear. A lab handout's "Before you start" callout can carry pedagogical context (first-time framing, what's new about today's session), but should not re-list interface/headphones/mic. Templates for new pages live in `meta/templates/`.

## Markdown files (internal)

Markdown docs (module specs, TA notes, this folder) use the H1 to identify themselves:

| Document type | H1 line |
|---|---|
| Module spec / TA notes (merged) | `# Module XX — [Module title]` |
| Operational doc (NAS policy, sample bank prep, this folder's files) | `# [Document title]` (no module reference) |

If a metadata line is useful immediately under the H1, put it as bold text and keep it dateless. For example: `**Weeks 2–5** (7 sessions)`. Calendar date ranges belong in `course-outline.md`, not here.

## Why the chrome stays consistent

Students see roughly thirty documents across the semester. Consistent chrome means they can navigate any one of them within a few seconds: the header tells them what document it is, the title block tells them what module it belongs to, the subtitle tells them what it covers. Reinventing that vocabulary per document would cost the reader attention they should spend on the content.
