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
| Reading | `Module XX · Lecture N` |
| Listening assignment | `Module XX · Listening` |
| Peer listening assignment | `Module XX · Peer listening` |
| Project prompt | `Module XX · Project N` |
| Module-tied handout | `Module XX · Handout N` |
| Module-agnostic handout | `Lab · Reference card` |
| Interactive tool | `Module XX · Tool N` |

### Numbering rules

- **Lecture numbers** count only Monday lectures within a module: Mon Wk 2 is Lecture 1, Mon Wk 3 is Lecture 2, etc.
- **Project numbers** count globally across the semester: Project 1 (Module 2), Project 2 (Module 3 midterm), and so on.
- **Handout numbers** count globally across the semester. Handout 1 is the first day setup; Handout 2 is session routines; subsequent handouts continue counting regardless of which module they fall in. The header still tags them with their module if they're module-specific.
- **Tool numbers** count within the module: the Module 2 digital-audio explorer is Tool 1, the Module 2 dynamics tool is Tool 2.

### Title block

The title block's module tag (`<div class="module-tag">`) carries the module's *thematic* label (e.g. `Module 02 · Digital audio, editing & mixing`), shared across all documents in a module.

The title block's subtitle is a one-sentence description of the document's content. **Subtitles do not contain dates.** Schedules shift each semester; positional labels and content descriptions don't.

### Intro paragraph

The intro paragraph (the first `<p>` after the title block) is **exactly one paragraph at lede size** (`<p class="lede">`).

If the intro feels like it wants to be two paragraphs, either merge them into one (sometimes a sentence reorder is enough) or push the second one past the first `<hr>` so it visually belongs to the body, not the intro. Two paragraphs at different sizes back-to-back makes the page look like the second one was an afterthought.

## Markdown files (internal)

Markdown docs (module specs, TA notes, this folder) use the H1 to identify themselves:

| Document type | H1 line |
|---|---|
| Module spec / TA notes (merged) | `# Module XX — [Module title]` |
| Operational doc (NAS policy, sample bank prep, this folder's files) | `# [Document title]` (no module reference) |

If a metadata line is useful immediately under the H1, put it as bold text and keep it dateless. For example: `**Weeks 2–5** (7 sessions)`. Calendar date ranges belong in `course-outline.md`, not here.

## Why the chrome stays consistent

Students see roughly thirty documents across the semester. Consistent chrome means they can navigate any one of them within a few seconds: the header tells them what document it is, the title block tells them what module it belongs to, the subtitle tells them what it covers. Reinventing that vocabulary per document would cost the reader attention they should spend on the content.
