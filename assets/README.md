# Assets

Shared resources used across student-facing materials in the course.

## Files

- `style.css` — central stylesheet for all student-facing HTML documents (handouts, readings, listening assignments, project prompts)

## Why one stylesheet

Every document a student sees in this course shares the same visual system: warm palette (cream background, dark warm grey text, rust accent), DM Sans for body text, DM Mono for headers and accents, generous whitespace, technical-manual feel. This is achieved by every HTML document linking to `assets/style.css`.

## Reference path

Documents in subfolders link to the stylesheet via a relative path:

- From `handouts/` → `../assets/style.css`
- From `course/readings/` → `../../assets/style.css`
- From `course/projects/` → `../../assets/style.css`
- From `course/listening/` → `../../assets/style.css`

## Future contents

This folder may also hold:

- Shared images (logos, decorative SVGs, course wordmark)
- Reusable diagram components
- Web fonts (currently loaded from Google Fonts CDN; could be self-hosted here later)
