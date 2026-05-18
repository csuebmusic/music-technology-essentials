# Asset recipes

Per-asset specifications: what each shared asset is, what it sounds like or looks like, how to recreate or substitute it. Internal build-time information.

> **Scope:** internal. The TA does not need any of this during the semester. The TA only needs to know an asset exists at its expected path. If something is missing, escalate to Inés; recipes here are for whoever rebuilds or substitutes the asset, which means Inés or a future maintainer of the course infrastructure.

The pattern: each module's section lists the prep-time assets needed for that module's lessons. For each asset: the path where it lives, what it is, and the recipe (length, format, what it sounds like / shows, pedagogical fit, substitution notes).

This file complements the build-script docs in [`../build/README.md`](../build/README.md). Build scripts cover assets that are programmatically generated (audio demos for digital-audio readings, diagrams that need scripted layout). This file covers assets that are produced by hand: recorded audio, photographed gear, captured screenshots, anything where the recipe is human-readable rather than scripted.

---

## Module 02 — Audio editing & mixing

### Wed Wk 2 lab handout · `orientation-sample.wav`

**Path on NAS:** `shared/module-02/orientation/orientation-sample.wav`

**Used in:** Lab 1 (`module-02-audio-editing-mixing/lessons/03-handout-audacity-orientation.html`)

**What it is:** a stereo bell-like resonance or sustained ringing texture, ~16 seconds, that gradually decays to silence across its full length.

**Format:** WAV, 44.1 kHz, 16-bit, stereo.

**Pedagogical fit:** the audible envelope shape (slow decay across the full clip) is what makes the lab work. Students cut into the decay around the 7-second mark and apply a fade to what remains; the visible taper across both stereo channels makes the editing moves easy to see on the waveform, and the audible fade-then-silence is what tells them the edit succeeded.

**Substitution:** Inés has the canonical file. If a substitute is ever needed: any stereo sustained sound with an audible decay (~10–18 s) works. Candidates: a long bowed note that fades, a struck rim recorded in stereo, a sampler-generated bell-like timbre. Avoid sounds with a hard ending (the lab's Step 5 depends on the decay being there for the fade to land on).

---

### Wed Wk 2 lab handout · Audacity screenshots

**Folder:** `assets/images/module-02-week-02/`

**Used in:** Lab 1 (`module-02-audio-editing-mixing/lessons/03-handout-audacity-orientation.html`)

**Status:** captured (Inés's Mac, May 2026). If re-capture is needed, the table below documents what each screenshot shows.

| Filename | Content |
|---|---|
| `audacity-settings.png` | Preferences → Audio Settings: Quality section showing Project Sample Rate 44100 Hz, Default Sample Rate 44100 Hz, Default Sample Format 16-bit |
| `audacity-interface-empty.png` | Empty Audacity main window with eight numbered orange markers placed directly on the regions identified in Step 3's annotation key (menu bar, transport, tools, level meters, Audio Setup, ruler, track area, selection toolbar) |
| `audacity-imported.png` | Main window with `orientation-sample.wav` imported as a stereo track, showing the ringing-decay waveform across both channels |
| `audacity-selection.png` | Same window with a region selected from roughly 7s to the end of the file (visible blue highlighted region in the waveform and timeline) |
| `audacity-fade-out.png` | Same window after the cut + fade-out: file now ends around 7.5s, last ~2.5s shows the visible fade taper |
| `audacity-export-prompt.png` | The "How would you like to export?" interstitial dialog with two options (Share to audio.com / On your computer) and the "Don't show again" checkbox |
| `audacity-export.png` | Export Audio dialog: filename `thiebaut-orientation.wav`, format WAV (Microsoft), Stereo, 44100 Hz, Signed 16-bit PCM, Entire Project |

**About the annotations on `audacity-interface-empty.png`:** the eight numbered markers are baked into the PNG itself (orange filled circles with white numbers, placed directly on the regions they identify). The handout's annotation key below the figure provides the legend. If the screenshot is ever re-captured, the new version will need fresh annotations drawn on; the numbering should match the order in the handout's Step 3 key.

Note that the empty Audacity window does not display the project sample rate anywhere visible. In Audacity 3.6 the project rate lives inside the Audio Setup dropdown, not in the main window's status bar. The annotation key reflects this; marker 5 (Audio Setup) describes the dropdown as the home for host, device, channel, and project-rate settings.

---

## Module 03 — Recording, sample prep & library building

### Wed Wk 6 lab handout · Audacity screenshots

**Folder:** `assets/images/module-03-week-06/`

**Used in:** Lab 1 (`module-03-recording/lessons/02-handout-recording-into-audacity.html`)

**Status:** to be captured from a lab Mac with the standard Audacity 3.x install, over the summer.

| Filename | Content |
|---|---|
| `audacity-audio-setup.png` | Audio Setup dropdown with the interface selected as Recording Device and Playback Device, and 1 (Mono) selected for Recording Channels |
| `audacity-meter-target.png` | Recording level meter in live monitoring mode, with peaks visibly landing in the -12 to -6 dBFS target band |
| `audacity-five-clips.png` | One mono track holding five clips in sequence: flat noise-profile clip first, then the four paper-sound clips of varying duration and amplitude |
| `audacity-noise-reduction-profile.png` | The Noise Reduction dialog in its Step 1 state, with the Get Noise Profile button at the top |
| `audacity-noise-reduction-apply.png` | The Noise Reduction dialog in its Step 2 state, with three sliders set to defaults (12 / 6.00 / 3) and OK at the bottom |

Filenames in the handout are already correct; the images just need to exist at those paths. Until then, browsers show broken-image icons but the prose and SVG diagram carry the lab on their own.
