# Prose conventions

Writing rules for student-facing HTML (readings, handouts, listening assignments, project prompts, interactive tools).

> **Scope:** student-facing material only. Internal docs (READMEs, TA notes, module specs, this folder) follow their own looser rhythm and these rules don't apply there.

## Why these rules exist

Student-facing material is read by beginners who may have never opened a DAW. Prose friction (fussy punctuation, jargon chains, hedges) takes attention away from the content. The rules here are about removing that friction.

## The rules

### No em dashes

Em dashes (`—`, U+2014) read as fussy or affected in beginner-facing material. Replace contextually:

- **Comma** when joining clauses or replacing parenthetical asides that flow naturally as part of the sentence
- **Parentheses** when content is genuinely a digression or aside
- **Colon** when introducing a definition, list, explanation, or directive
- **Period** when separating two complete thoughts that should stand apart
- **Middle dot (`·`, U+00B7)** for title separators in `<title>` elements and `<h1>`/`<h2>`/`<h3>` metadata-style headings (e.g. `Step 1 · Turn the knobs down`)

En dashes (`–`, U+2013) are preserved where they form correct typographic compounds, like `musique concrète–style found sounds` (combining a multi-word noun phrase with a modifier). The rule is about em dashes, not en dashes.

### No chains of negatives

Avoid sentences built from a list of "no X, no Y, no Z" or "not X, not Y" constructions. They turn an explanation into a denial.

Restate positively: name what the thing is or does rather than enumerating what it isn't.

- Instead of: "This isn't a melody, it isn't a rhythm, it isn't a chord progression."
- Use: "This is a texture: a continuous shape of sound with no distinct events."

A single negative is fine when the negation is the point. The rule is about chains.

### No bullet points when content is naturally prose

Bullets are for genuine lists: parameters, steps, items, options. Don't bullet a paragraph just because it has three points.

If the bullets read as full sentences flowing into each other, they're a paragraph; write them as one. If the bullets are short, parallel, and discrete, they're a list; keep the bullets.

### Avoid hedging filler

"It's worth noting that," "essentially," "basically," "in some sense," "kind of," "sort of." Each one softens a sentence without adding content. Cut or commit.

If a claim genuinely needs qualification, say what the qualification is. "Most of the time" is honest; "essentially" is decoration.

### Beginner-friendly first

Define every technical term the first time it appears, then use it consistently. The first mention is where the term earns its place; after that you can rely on it.

When a textbook concept and a plain-language version both exist, lead with the plain version and introduce the textbook term as the name for the thing the student now recognizes.

### Active voice over passive

"Audacity opens the file" reads more directly than "the file is opened by Audacity." Passive voice is fine when the actor genuinely doesn't matter or isn't known; otherwise prefer active.

### Short paragraphs

Walls of text intimidate beginners. Break frequently. Two or three sentences per paragraph is often enough; four is fine; six is usually too many. The visual rhythm of a page matters as much as the prose itself.

### No jargon as decoration

Use technical terms only when they earn their place. If a sentence works without a term, leave the term out. The point isn't to avoid technical language; it's to make sure each technical word is doing work.

## Quick self-check

Before publishing a student-facing HTML doc, scan for:

- Em dashes (search the source for the character `—`)
- Sequences of "no X, no Y, no Z" or "not X, not Y" sentences
- Bullet lists where each bullet is a complete sentence flowing into the next
- The words "essentially," "basically," "in some sense," "it's worth noting"
- Technical terms used before they were defined

Each one is fixable in seconds; the cumulative effect on the page is substantial.
