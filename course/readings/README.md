# Readings

The textbook layer of MUS 381. One reading per Monday lecture, written for students to read on their own and for the TA to project and lecture *through* during class.

These exist because no commercial textbook covers what this course covers in the way it needs to be covered. Rather than asking students to buy a book that won't quite fit, the course builds its own reference material — concept by concept, in the language and order this course uses.

## Format

All readings are HTML, using the central stylesheet at [`assets/style.css`](../../assets/style.css). They share the same visual system as handouts, projects, and listening assignments.

Filename: `module-XX-week-YY-shortname.html` (e.g. `module-02-week-02-digital-audio.html`).

CSS link path: `../../assets/style.css`.

## Standard structure

Every reading should include:

- **Title and framing** — what this reading covers, why it matters, what the student will be able to do after
- **Body content** — the actual concepts, written for beginners, with technical terms introduced gently and used consistently
- **Visuals where they help** — diagrams, waveform graphics, screenshots, photos. Audio concepts especially benefit from visualization.
- **Inline listening references** — when a piece is relevant to the concept being explained, mention it at the right moment. The full listening assignment lives separately.
- **Vocabulary section** — key terms with plain-language definitions, gathered at the end
- **For further exploration** — optional pointers for students who want to go deeper

## Length

Aim for ~10–15 minutes of focused student reading per file. The TA spends 90 minutes elaborating on this in lecture, so the reading is the spine, not the whole lecture.

## How students use them

- **Before lecture:** optional preview
- **During lecture:** the TA projects it; students follow along
- **After lecture:** primary reference; what they re-read when working on assignments

## How the TA uses them

- The reading is the canonical content. The TA doesn't have to invent a curriculum — it's already here.
- The TA's job in lecture is to *lecture through* the reading: pause for questions, add personal insights, demonstrate examples on the projector, play the listening pieces, draw on the whiteboard, react to the room.
- Companion TA notes (in `ta-notes/module-XX.md`) provide pacing, suggested moments to pause, demo cues.

## Authoring

Use existing readings as templates. The header, title block, and footer follow the cross-document chrome convention documented in [`assets/README.md`](../../assets/README.md#document-chrome-convention). The reading-specific shape:

```html
<header class="handout-header">
  <span class="course">MUS 381 · Essentials of Music Technology</span>
  <span class="meta">Module XX · Lecture N</span>
</header>

<div class="title-block">
  <div class="module-tag">Module XX · [thematic label for the module]</div>
  <h1>[Title of this reading]</h1>
  <div class="subtitle">[One sentence describing what's in this reading.]</div>
</div>

<p class="lede">[One paragraph, lede-sized, framing what's ahead and why it matters.]</p>
```

And at the bottom:

```html
<footer class="handout-footer">
  <span>MUS 381 · CSU East Bay</span>
  <span>Module XX · Lecture N</span>
</footer>
```

Notes on the precedent:

- The **lecture number** in the header and footer is the lecture's position within its module, counting only Monday lectures (Mondays are lecture; Wednesdays are lab). Module 02 has three Monday lectures over weeks 2-5 (Mon Wk 4 is Labor Day), so they're Lectures 1, 2, 3. Lecture numbering is more durable than dates: the schedule shifts every semester, but lecture order within a module doesn't.
- The **module tag** is the module's thematic label (what the module is *about*), not a position label. Both readings within a module share the same module tag.
- The **subtitle** is a one-sentence description of the reading's content. Don't put dates here.
- The **lede paragraph** is one paragraph at lede size. If you need more than one paragraph of framing, merge them; if you need a follow-up that isn't part of the framing, put it after the first `<hr>` so it visually separates from the lede.

Other structural elements:

- `<h2>` for major sections, `<h3>` for subsections
- `<div class="callout">` for asides; `.callout.warn` for cautions
- `<code>`, `<kbd>`, etc. as in handouts

Visuals can be inline SVG (built in the warm palette) or referenced images. Photos of historical figures or gear come from CC-licensed sources (Wikimedia, etc.) with attribution.

## Tone

Beginner-friendly but substantive. The goal is "the textbook chapter that doesn't exist commercially" — accurate, well-paced, with personality. Define every technical term the first time it appears and use it consistently. Connect concepts to musical and creative outcomes wherever possible.

## Prose conventions

All student-facing HTML follows a shared set of prose conventions documented in [`assets/README.md`](../../assets/README.md). The most important: no em dashes (use commas, parentheses, colons, or middle dots instead).
