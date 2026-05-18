# Page templates

Skeletal HTML files that embody the conventions in this folder. Copy one of these as the starting point for a new page.

| Template | Used for | Today's gear callout |
|---|---|---|
| `reading.html` | Mon-lecture readings | audio interface, headphones |
| `tool.html` | Interactive in-class tools | audio interface, headphones |
| `handout-module-02.html` | Wed-lab handouts in Module 2 | audio interface, headphones |
| `handout-module-03.html` | Wed-lab handouts in Module 3 | audio interface, headphones, dynamic mic (with stand and XLR cable) |
| `handout-module-04.html` | Wed-lab handouts in Module 4 | audio interface, headphones, MIDI keyboard |

Each template includes the right module-tag, header/footer chrome, title block, lede slot, **Today's gear** callout matching the file type's gear tier, and (for handouts) an `End of session` skeleton that points at the routines card.

## What to fill in

Bracketed placeholders mark every slot that needs editing:

- `[Reading title]` / `[Lab title]` / `[Tool title]` — the page's H1, also drop into the `<title>` and (for headers/footers) any title-tied chrome
- `Module XX · Lecture N` / `Module XX · Lab N` / `Module XX · Tool N` — the role chrome in the header and footer right spans, plus the module tag in the title block. Replace `XX` with the zero-padded module number and `N` with the within-module count
- `[Module thematic label]` — the module's shared thematic label (e.g. `Digital audio, editing & mixing` for Module 02). One-line label shared by every document in that module
- `[One-sentence subtitle, no dates]` — the title-block subtitle
- `[One-paragraph lede ...]` — the lede paragraph, exactly one paragraph at lede size

## What not to change

The **Today's gear** callout is the same text every time within its file-type variant. If a session's gear differs from the template's variant (e.g. a Module 2 handout that for some reason needs a mic), don't edit the callout inline — first update `meta/chrome-conventions.md` to define a new variant, then update the template here.

The `End of session` closing paragraph that points back to the routines card is also reusable across handouts; tweak its wording only when the session genuinely changes the unplug sequence (e.g. a Module 4 handout might need to call out the MIDI keyboard's USB instead of the mic's XLR).

## When to skip the Today's gear callout

Per `meta/chrome-conventions.md`:

- The Session Routines card itself (`module-01-fluency/lessons/02-handout-session-routines.html`)
- The Day 1 reading (`module-01-fluency/lessons/01-reading-first-day-setup.html`), which teaches the take-out cycle from scratch
- Listening pages and project prompts, which students consult at home and across sessions; the day's lab handout owns the gear context, not these
