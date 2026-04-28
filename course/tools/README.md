# Tools

Interactive, browser-based teaching tools for MUS 381. Each tool is a self-contained HTML file that runs in any modern browser without installation, login, or backend.

These exist to make abstract audio concepts physical: instead of *describing* what summing sines does, students hear it; instead of *defining* timbre, they reshape it with sliders and listen.

## Format

All tools are HTML files using the central stylesheet at [`assets/style.css`](../../assets/style.css). They share the same visual system as readings, handouts, projects, and listening assignments — warm cream background, DM Sans body, DM Mono accents, rust accent color.

Filename: `module-XX-week-YY-shortname.html` to mirror the reading naming convention so the parallel is obvious. (e.g. `module-02-week-02-digital-audio.html` is the Mon Wk 2 reading; `module-02-week-02-digital-audio-explorer.html` is the matching Wed Wk 2 lab tool.)

CSS link path: `../../assets/style.css`.

## Standard structure

Every tool should include:

- **Title block** with module tag, h1, subtitle
- **Lede** — what the tool covers and a hearing-safety reminder if it produces sound
- **TOC** — if the tool has multiple sections, a small jump-nav at the top
- **The interactive content itself** — broken into sections separated by `<hr>`, each with framing prose, the tool, and a "what to listen for" / "try this" prompt
- **What you've heard / Takeaways** — short summary of the conceptual points
- **Vocabulary** — terms introduced by the tool, with plain-language definitions

## Implementation conventions

- **Self-contained.** Inline CSS for tool-specific styles, inline JavaScript for behavior. No external dependencies beyond the shared stylesheet.
- **Web Audio API** for audio synthesis. Lazy-initialize the AudioContext on first user interaction (browsers require this).
- **Conservative gain.** Sine tones at high frequencies are loud and fatiguing. Default master gain around 0.18 of full scale. Multi-oscillator tools should normalize so adding partials doesn't pile up loud.
- **Live visual feedback.** When a tool produces sound, it should also show a live waveform or other visualization. Students need to see the relationship between the controls they're moving and the sound they're hearing.
- **Hearing-safety reminder** in the lede whenever the tool produces sound. "Keep your headphones at a moderate volume."

## How students use them

- **In the Wednesday lab**, the TA walks through each section, lets students explore for a few minutes, then prompts the next step
- **After class**, the tool is the reference — students return to it when working on their own pieces or studying for exams

## How the TA uses them

- The tool is the lab's structure. Walk students through it section by section, pausing for the explore-then-discuss rhythm
- Companion TA notes (in `ta-notes/module-XX.md`) provide pacing, suggested moments to pause, things to demonstrate

## Tools currently in this folder

- `module-02-week-02-digital-audio-explorer.html` — Wed Wk 2 lab Part 1: sine maker, sine summer, harmonic series, timbre.

## Coming soon

- Wed Wk 4: Mixing tool Part 1 (levels, EQ, stereo placement)
- Mon Wk 5: Mixing tool Part 2 (dynamics)
