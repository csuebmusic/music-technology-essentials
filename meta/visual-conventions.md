# Visual conventions

Palette, fonts, CSS variables, SVG handling, and the per-module audio format standards.

> **Scope:** all student-facing HTML, the build scripts that generate audio assets, and any new visual elements (diagrams, screenshots, palette extensions).

## Aesthetic

Modern minimal with mechanical-retro influences. Warm cream backgrounds, warm-grey text, rust accent. Functional, technical-manual feel, but not cold. Generous whitespace; small uppercase mono headers; serif-feeling DM Sans body text; DM Mono for labels and code.

The aesthetic is consistent across every student-facing surface (readings, handouts, listening assignments, project prompts, interactive tools) so the course feels like one continuous body of work rather than a stack of unrelated documents.

## Palette

All colors live in CSS variables. **Never hardcode hex values in component CSS.** Reference variables by name; if a color doesn't exist for what you need, add it to the variable list first and use the name everywhere.

The variable definitions in `assets/style.css`:

| Variable | Hex | Purpose |
|---|---|---|
| `--bg` | `#f5f1e8` | Page background, warm cream |
| `--bg-alt` | `#ede6d6` | Slightly darker cream for callouts, audio comparison blocks, figure backgrounds |
| `--ink` | `#2a2620` | Body text, dark warm grey |
| `--ink-soft` | `#5c544a` | Secondary text, captions, sublabels |
| `--ink-faint` | `#8a8175` | Tertiary text, photo attributions |
| `--rule` | `#c9bfa8` | Borders, dividers, rules |
| `--rule-soft` | `#ddd3bd` | Subtle grid lines in diagrams |
| `--accent` | `#a85c2e` | Rust accent, used for module tags, callout titles, link borders, key highlights |
| `--accent-soft` | `#d89169` | Lighter rust for hover states, secondary accents |
| `--warn-bg` | `#f0e3d2` | Background for warning callouts |
| `--warn-ink` | `#6b3e1a` | Text for warning callouts |
| `--meter-good` | `#5c8c4e` | Level-meter green zone: signal safely below ceiling |
| `--meter-hot` | `#c08a2e` | Level-meter amber zone: signal approaching ceiling |
| `--meter-clip` | `#a83030` | Level-meter red zone: signal at or over ceiling |
| `--gr-light` | `#d9b042` | Gain-reduction gradient, light end (small reduction, yellow) |
| `--gr-heavy` | `#b5552f` | Gain-reduction gradient, heavy end (large reduction, rust) |
| `--cable-xlr` | `#3a6b7a` | XLR cable, mic-level balanced; teal-slate |
| `--cable-usb` | `#525a5e` | USB cable, digital data; neutral graphite |
| `--cable-ts` | `#a8862e` | TS cable, instrument-level unbalanced; warm ochre |
| `--cable-trs` | `#6b5e8c` | TRS cable, balanced line / stereo; muted plum |

### Meter color taxonomy

`--meter-good`, `--meter-hot`, `--meter-clip` are the canonical level-meter triplet. They follow the audio-industry green / amber / red convention but are warmed slightly to sit with the cream palette. Used in both static SVG meter diagrams (e.g. the gain-staging figure in `06-handout-mixing-in-audacity.html`) and live CSS meter widgets (e.g. the input / output / GR meters in the dynamics tool).

`--gr-light` and `--gr-heavy` are the two endpoints of the gain-reduction gradient. CSS gradient interpolation handles the middle; if a sharper transition is needed (e.g. a 3-stop gradient with a deliberate midpoint), `--meter-hot` works as the intermediate color since it sits naturally between yellow and rust.

### Cable color taxonomy

Each cable type used in the course gets a distinct desaturated hue, kept separate from `--accent` (reserved for devices) and from each other. The convention is consistent everywhere a cable appears in a diagram, so a student who learns "XLR is teal" in the Wk 6 Mon reading can recognize XLR by color in the Wk 7 Mon expansion, the Wk 8 Mon mixer diagram, and any later signal-flow visual.

| Variable | Cable | Carries | Where it first appears |
|---|---|---|---|
| `--cable-xlr` | XLR | Mic-level (or line-level), balanced, three-conductor | Module 3 Wk 6 Mon reading (basic recording chain) |
| `--cable-usb` | USB | Digital data | Module 3 Wk 6 Mon reading (interface to computer) |
| `--cable-ts` | TS | Instrument-level, unbalanced, two-conductor | Module 3 Wk 7 Mon reading (widening the flow) |
| `--cable-trs` | TRS | Balanced line / unbalanced stereo, three-conductor | Module 3 Wk 7 Mon reading |

If a new cable type is needed later (optical, MIDI, etc.), add a `--cable-*` variable here first, then use the name everywhere.

## Typography

| Variable | Stack | Purpose |
|---|---|---|
| `--serif` | `'DM Sans', -apple-system, system-ui, sans-serif` | Body text (despite the variable name, DM Sans is a humanist sans, not a serif) |
| `--mono` | `'DM Mono', 'SF Mono', Menlo, monospace` | Headers, labels, captions, code, key combos |

Fonts are loaded from Google Fonts via the `@import` at the top of `style.css`. The course wordmark, the document-chrome header / footer, and all label-style elements use `--mono`; everything else uses `--serif`.

## SVG diagrams

Diagrams are **written inline** in the HTML. CSS variables only resolve when the SVG is embedded directly; loading SVG via `<img src="...">` strips the variable resolution and breaks the palette.

For diagrams generated by build scripts (e.g. the wide-vs-narrow waveform in Module 2 Week 5), the script writes the SVG to `assets/images/module-XX-week-YY/` as the source of truth, and the reading **inlines that SVG content directly** by pasting it into the page. The image on disk exists for regeneration and review; the version that ships in the HTML is the inlined copy.

SVG conventions:

- Always include `role="img"` and `aria-label` for accessibility
- Use `var(--ink)`, `var(--accent)`, etc., for stroke and fill colors, never hex
- Use `DM Mono, monospace` for any text inside the SVG (this is the convention; the variable doesn't resolve inside SVG `font-family` attributes in some browsers, so the literal stack is fine)
- `viewBox` rather than fixed width/height so diagrams scale

### Signal-flow diagrams

Signal-flow diagrams show how audio moves through equipment: from a source, through cables and devices, to a destination. They appear throughout Module 3 (basic recording chain, widened flow, mixer routing) and need to read consistently across readings.

The visual hierarchy distinguishes **devices** from **cables**:

- **Devices** (mic, audio interface, computer, mixer, etc.) are drawn as rounded rectangles outlined in `--accent`, filled with `--bg-alt`. Equal size where possible. They're the nodes of the flow.
- **Cables** (XLR, USB, TS, TRS) are drawn as smaller, lower-weight labeled segments connecting two devices. Stroked in the cable's color from the `--cable-*` family. Each cable gets a small inline label (e.g. "XLR", "USB") in DM Mono, positioned above or below the segment, colored to match the cable.
- **Direction** is shown with an arrowhead at the receiving-device end of each cable segment, in the cable's color.

The device-cable-device-cable-device chain reads visually as anchor-line-anchor-line-anchor, with color doing the work of distinguishing cable types at a glance.

A separate inline label above the whole diagram, in `--accent` DM Mono caps with letter-spacing, names what the diagram is (`BASIC RECORDING CHAIN`, `SIGNAL FLOW`, etc.). Beneath each device, an `--ink-soft` DM Mono caption names what category of signal is leaving that device (`acoustic`, `analog electrical`, `digital`).

The canonical example is the chain diagram in `module-03-recording/lessons/01-reading-recording-chain.html`, section 1.

## Images and screenshots

Screenshots of software (Audacity, etc.) and photographs are loaded as `<img>` with `loading="lazy"`. They sit inside `<figure>` blocks with a `<figcaption>` styled in DM Mono uppercase.

Photo attributions, when present, go inside the figure as a small italic line under the figcaption (see Module 2 listening for examples). The attribution uses `--ink-faint` and the `.photo-attribution` class.

When a figure needs numbered annotations, the HTML pattern is the same regardless of source: a `<figure class="annotated">` (or `figure.screenshot` for software screenshots specifically) containing the image, a brief `<figcaption>`, and an `.annotation-key` block below the image listing the numbered items.

For screenshots that the course produces in-house (e.g. an Audacity capture taken from a lab machine), the markers drawn directly onto the PNG follow a fixed style: orange filled circles with white numbers, placed on the region they identify, no leader lines. The canonical example is `audacity-interface-empty.png` in `assets/images/module-02-week-02/`. If the screenshot is ever re-captured, the new version needs fresh annotations drawn on in the same style.

For figures that come from outside sources (e.g. a third-party cross-section diagram of a microphone, a manufacturer-produced schematic), the markers on the image stay in whatever style the source uses; only the `.annotation-key` block beneath is rewritten in the course voice. A canonical example is `dynamic-microphone-cross-section.png` in `assets/images/module-03-week-06/`.

## Callout and pause blocks

Two block types interrupt the main prose flow with framed content. They look different on purpose because they do different jobs.

**`.callout`** — a small framed aside for operational notes: lab heads-ups, "don't yank the cable," brief reminders. Tight padding, left border in `--accent`. A `.callout-label` in DM Mono caps names the kind of interruption (e.g. `LAB NOTE`, `WEDNESDAY: DON'T YANK THE CABLE`). Short. Doesn't take more than a few sentences.

**`.pause`** — a longer aside that interrupts the main flow to explain a deeper principle. Dashed border on all sides, more generous padding, full background tint. A `.pause-label` in DM Mono caps reads `PAUSE`. Inside, an `<h4>` titles what's being explained, followed by paragraphs, optionally a figure. Used when the prose has just made a claim that depends on a principle worth taking a moment to ground (e.g. the balanced-cable cancellation depends on how waveforms sum, so a pause box explains phase summation before the prose moves on).

The visual cue:
- Callout = "heads-up, then keep reading"
- Pause = "stop, learn this, then resume"

The canonical pause example is the phase-summation explainer in `module-03-recording/lessons/01-reading-recording-chain.html`, section 4.

## Per-module audio format standards

Each module has a default audio format that students use throughout. The standard is introduced in the module's first reading and reinforced consistently in handouts and project prompts.

| Module | Sample rate | Bit depth | DAW | Notes |
|---|---|---|---|---|
| 1 | n/a | n/a | QuickTime | Day 1 hello recording uses whatever default QuickTime sets |
| 2 | 44.1 kHz | 16-bit | Audacity | CD standard, matches the destructive-editing pedagogy and Schaeffer historical context |
| 3 | 44.1 kHz | 16-bit | Audacity | Continues Module 2 standard so sample-library files are compatible |
| 4 | 48 kHz | 32-bit float | Ableton | Ableton's native working format; the shift is taught explicitly |

The Module 2 → Module 4 standards shift is a pedagogical moment, not a footnote. Module 4 readings should introduce 48/32f explicitly and explain why Ableton wants it.

Build scripts respect the per-module standard: anything that writes to `assets/audio/module-02-*` outputs 44.1/16, anything that writes to `assets/audio/module-04-*` outputs 48/32f.

## Page width and structure

Student-facing HTML pages are constrained to `max-width: 720px` (see `body` in `style.css`). This is the readable-prose width and shouldn't be widened for any reason short of an interactive tool that needs more horizontal room. If a tool needs more width, scope the override to the tool block; don't widen the body.

Header lives in `<header class="handout-header">` at the top. Title block lives in `<div class="title-block">` immediately after. The lede paragraph is `<p class="lede">` immediately after the title block. Footer is `<footer class="handout-footer">` at the bottom. The first horizontal rule `<hr>` after the lede separates intro from body content.

This structural skeleton is consistent across every student-facing document; deviating without reason breaks the visual rhythm of the course.
