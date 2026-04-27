# Listening assignments — pattern and template

This folder holds one listening assignment per module. The pattern is consistent so students know what to expect: each assignment has 1–3 listening examples, a short framing paragraph, and a small set of guided questions.

## Format

All listening assignments are HTML, using the central stylesheet at [`assets/style.css`](../../assets/style.css). They share the same visual system as handouts, readings, and project prompts.

Filename: `module-XX-listening.html`.

CSS link path: `../../assets/style.css`.

## Standard structure

Every listening assignment should include:

- **Module and due date** at the top
- **Why we're listening to this** — one short paragraph framing the connection to what students are learning
- **The listening list** — 1–3 pieces with composer/artist, title, year, and a way to find them
- **Guided questions** — 3–5 questions students answer in writing
- **Length expectation** — typically half a page total; not a long essay
- **Where to submit** — Canvas (text submission) is the default

## Question design

Questions follow a consistent shape, drawn from Inés's pedagogy of listen → analyze → create:

1. **Descriptive** (1–2 questions) — what do you hear? What sounds, textures, gestures? No interpretation yet, just description.
2. **Analytical** (1–2 questions) — what techniques are being used? How is the piece structured? What technical or compositional choice is most striking?
3. **Generative** (1 question) — what would you try in your own work, based on this? How does this change how you might approach your current project?

The questions are intentionally not "did you like it" or "what does it mean." Listening responses are about training the ear, not opinion-sharing.

## Photos and historical context

When the historical or technological context matters for how students should listen (e.g., knowing that musique concrète was originally a tape practice, not a digital one), include a short framing section before the listening list. A few paragraphs of prose, interleaved with photos, is usually enough.

**Photo sourcing: Inés provides the photos.** Do not pull images from Wikimedia, Google, or other public sources independently. When a listening assignment needs photos, ask Inés for them and wait. She will also provide source URLs for attribution. Once received, store images at `assets/images/module-XX-week-YY/` and reference them locally (no hotlinking).

Compress large images before committing. Target: under 200 KB each, roughly 1200–1400 px on the long side. Use `Pillow` or `cwebp`.

**Photo display CSS** lives in the head `<style>` block of each listening file. Two layouts:

- `.photo-single` — one photo per beat, used when interleaving images through prose. Each photo gets its own `<figure>` with caption and attribution line.
- `.photo-grid` — two photos side-by-side (stacked on mobile under 640px). Use sparingly, typically for direct comparisons.

Each photo includes a `.photo-attribution` paragraph beneath the caption with proper credit (photographer or original source, license if applicable, the URL Inés provided).

## Audio and video links

**Use styled hyperlink cards (`.listen-link`), not iframe embeds.** Embeds look nice but fail in too many ways: uploaders disable embedding, third-party iframes load tracking scripts, accessibility suffers, and a single broken iframe makes the assignment unusable.

A `.listen-link` card is a single `<a>` element with three children: a circular play icon (left), a title and meta line (center), and an external-link arrow (right). Both Schaeffer and Henry on `module-02-listening.html` use this pattern — copy the markup and CSS from there.

Cards open in a new tab (`target="_blank" rel="noopener noreferrer"`) so students don't lose the assignment page when they click through to listen.

## Tone

Student-facing, warm, direct. Each assignment should make clear that there are no wrong answers as long as the student is genuinely listening and writing about what they hear.

## Submission details

Every listening assignment ends with a `.submission-card` block (style defined in `assets/style.css`) covering:

- **Where**: Canvas, under the listed assignment
- **File format**: Word (`.docx`) or PDF (`.pdf`) — no plain-text Canvas submissions
- **Filename**: `lastname-listening-NN.docx` (matching the project naming convention)
- **Length**: about half a page, 250 to 350 words
- **Formatting**: 12 pt, double-spaced, 1-inch margins, Times New Roman or Garamond, with name/course/assignment/date at top
- **Citations**: Chicago Manual of Style (notes-bibliography) or MLA Handbook, student picks one and stays consistent. Include at least one worked example for a recording citation, since that's the format students are most likely to need and least likely to have written before.

The card is the canonical form for all written assignments submitted to Canvas across the course (listening responses, midterm written component, final reflection, etc.). See `module-02-listening.html` for the markup pattern.

For project assignments where the deliverable is an audio file (not a written response), the submission flow is different: files go to NAS following the `lastname-projectNN.wav` convention. Don't use the submission card for those.

## Prose conventions

All student-facing HTML follows a shared set of prose conventions documented in [`assets/README.md`](../../assets/README.md). The most important: no em dashes (use commas, parentheses, colons, or middle dots instead).

## Grading

Listening responses are low-stakes — completion plus genuine engagement. A typical rubric: full credit if the response addresses all questions and shows real listening; partial credit if it's superficial or skips questions; no credit if not submitted.
