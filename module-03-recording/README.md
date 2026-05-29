# Module 03 — Recording, Sample Prep & Library Building

**Weeks 6–9 · 8 sessions (800 minutes total)**

> **Status:** Roadmap in place. Session blocks are stubs to be filled in between sessions as the module is built out. The spec at the top is the load-bearing part for now.

---

## Module purpose

Module 2 taught students to manipulate sound that was handed to them. Module 3 teaches them to make their own. By the end of four weeks they should be able to plug in a microphone, capture a clean recording, prepare the file for use, and organize it into a usable library.

The deliverable is the library itself, the curated and organized collection of sounds students will draw from for the rest of the semester (and beyond). The midterm is two parts: the library submission, and a terminology exam covering Modules 1 through 3.

The arc of the module: trace the basic flow from mic to DAW → record into Audacity → widen the flow (other signal types, other mics, signal modifiers) → see how a mixer routes multiple flows at once (the Toft ATB in detail) → put the mixer through the live-sound scenario in lab → visit the studio in person, with the studio-recording walkthrough to work through on their own time → submit the library.

Two principles thread through the module:

1. **Signal flow is a sequence of decisions.** Sound becomes signal becomes recording becomes sample becomes library. At every stage, something is chosen: which mic, which signal type, which cable, which input, which interface, which prep step, which destination folder. Students should be able to look at any setup (a stage, a studio, a phone propped against a doorframe) and name the flow from acoustic source to stored file. The basic recording chain is the most common version of this flow; the Wk 7 expansion (instrument and line signals, DI boxes, preamps) and the Wk 8–9 mixer sessions (the console, the live-sound scenario, and the studio visit with its self-guided recording walkthrough) widen the frame.
2. **A sample is not a recording.** A recording is what comes out of the mic; a sample is what goes into the library. Turning one into the other is its own discipline, and it spans both the tracking stage and the prep stage. While recording: leave headroom (peaks around -12 to -6 dBFS) so there are decisions left to make. After recording: denoise, trim, normalize, name, and file. Neither step is optional; both are what make a usable library possible.

By the end of Wk 9, students should have a working library of their own recordings, prepped to a consistent standard, organized in a documented folder structure, ready to use as raw material in Module 4 (Ableton).

---

## Learning outcomes

By the end of this module, students should be able to:

1. Describe signal flow from acoustic source to stored file, naming the components at each stage
2. Name the components of the basic recording chain (dynamic mic, mic-level signal, XLR cable, audio interface) as the most common version of that flow
3. Distinguish dynamic, condenser, and (briefly) ribbon microphones, and know when to reach for each
4. Distinguish mic-level, instrument-level, and line-level signals, and match each to the correct input on an interface
5. Identify XLR, TS, and TRS cables and know what each carries
6. Set up a recording session in Audacity from cold: select input, set gain, monitor, record with headroom
7. Prepare a recorded sample for use: denoise, trim, normalize to a consistent standard
8. Organize a sample library with a documented folder structure, consistent naming, and a README
9. Record audio on a phone (iPhone or Android) at a quality suitable for adding to the library
10. Describe how a mixer routes multiple signal flows at once, and what auxes and busses do in live-sound vs. studio-recording contexts
11. Pass a cumulative terminology exam covering vocabulary from Modules 1 through 3

---

## Key concepts introduced

- **Signal flow:** the path sound takes from acoustic source to stored file. Mic → signal → cable → input → interface → DAW is the most common version of it, but every recording setup has one (a phone recording has a shorter flow; a live show with a mixer has a wider one). Students should be able to point at any setup and trace the flow.
- **The basic recording chain:** dynamic mic → mic-level signal → XLR cable → audio interface → DAW. The default flow at every lab station, and the first one students learn to name.
- **Transducer types:** dynamic mics (moving-coil, what's at every station; rugged, no power needed, common); condenser mics (more sensitive, more detail, need phantom power); ribbon mics (mentioned for completeness, not used in the lab).
- **Polar patterns:** at a beginner level. Cardioid is what students will mostly meet at the lab. Omni and figure-8 introduced for vocabulary.
- **Signal types:** mic level (small, needs preamp), instrument level (medium, from a guitar or bass pickup), line level (large, from a synth or interface output). Each one wants a different input.
- **Cables:** XLR (balanced, three-conductor, carries mic-level and line-level signals; what's at every station for the dynamic mic). TS (unbalanced, two-conductor, carries instrument-level signals; what plugs into a guitar). TRS (three-conductor, carries balanced line-level or stereo, depending on context).
- **Signal modifiers:** the DI box (instrument level → mic level, balanced) and the hardware preamp (mic level → line level, with character). Where they sit in the flow and why.
- **Recording with headroom:** peaks around -12 to -6 dBFS while tracking. The reason: leaving room to make decisions in editing, not committing to a level you can't undo.
- **The sample prep pipeline:** a three-step standardization process applied to every raw recording before it enters the library. (1) Denoise using a captured silence sample; (2) trim silence at start and end; (3) peak-normalize to a consistent ceiling. The pipeline turns a recording into a sample.
- **Library organization:** folder structure, naming conventions, an internal README. The library is a usable resource, not a pile of files. Students who can find a sound in their library will use their library; students who can't, won't.
- **The mixer (introduction):** the place where many signal flows converge, split, and route to different destinations. Channel strips, faders, auxes, busses. Students don't need to operate one yet; they need to understand what it is and why it's the shape it is.
- **Auxes and busses:** routing tools that work the same way on the mixer; what's different is what they feed. In a live context, auxes feed monitor wedges so performers can hear themselves. In a studio, the same auxes feed headphone mixes for performers being recorded. The mechanism is the same; the destination is different.

---

## Deliverable: Midterm

Two parts, both due Wed Wk 9.

### Sample library

A submitted folder of the student's own recorded sounds, prepped through the standardization pipeline and organized into a documented structure on the NAS.

Full prompt and rubric: [`projects/project-02-sample-library.html`](https://csuebmusic.github.io/music-technology-essentials/module-03-recording/projects/project-02-sample-library.html) *(to be written)*

**Scope (working target, revisit when drafting the prompt):** ~15–25 prepped sounds, organized in a documented folder structure with a student-written README, all files at 44.1 kHz / 16-bit WAV, all named per convention.

**Timeline:**
- Wk 6 Wed: students record their first 4 sounds in lab (paper crumble x2 speeds, paper rip x2 speeds), prep them, and submit them as a starter library
- Wk 7 onward: students record additional sounds in lab and on their phones outside class
- Wk 8: Mon mixer lecture and Wed mixer-in-practice lab (live sound). Students continue adding sounds to the library between sessions.
- Wk 9 Mon: studio visit (MB2508), a walk around the studio; handout 08 (the studio-recording walkthrough) goes home to try on their own time; midterm review packet handed out
- Wk 9 Wed: final library submission and terminology exam

### Terminology exam

A cumulative in-class exam covering Modules 1 through 3 vocabulary and concepts. ~30 minutes, in-class on Wed Wk 9 after library submission is verified.

Full exam and answer key: [`projects/terminology-exam.md`](./projects/terminology-exam.md) *(to be written, TA-facing only)*

---

## Listening assignment

**Module 3 historical listening:** Field recording and acousmatic tradition. Composers and sound artists who treat recording itself as the compositional act. Chris Watson, Hildegard Westerkamp, Francisco López as starting points; the choice of three pieces and the framing are to be finalized when the assignment is drafted.

Full listening assignment with guided questions: [`listening/historical.html`](https://csuebmusic.github.io/music-technology-essentials/module-03-recording/listening/historical.html) *(to be written)*

**Due:** Mon Wk 9, before class.

**Peer listening:** Module 3 also includes a peer-listening assignment, where students browse and listen to each other's sample libraries after midterm submission and respond briefly. The format differs from Module 2's peer listening: students are listening to *libraries* (collections of curated sounds) rather than *finished pieces*, so the prompts orient toward what's in the libraries and what the listener would do with it.

Peer listening assignment: [`listening/peer-midterm.html`](https://csuebmusic.github.io/music-technology-essentials/module-03-recording/listening/peer-midterm.html) *(to be written)*

**Due:** Mon Wk 10, before class.

---

## Session overview

| Wk | Day | Focus |
|---|---|---|
| 6 | Mon | Session 1 · Lecture: The basic recording chain. Dynamic mic, mic-level signal, XLR cable, audio interface. End-to-end ADC flow with the most common components. |
| 6 | Wed | Session 2 · Lab: Recording into Audacity (Lab 1). Project setup, four paper recordings (crumble slow/fast, rip slow/fast), three-step sample prep pipeline (denoise / trim / normalize), library folder set up, naming convention established. Phone-recording reference card distributed. |
| 7 | Mon | Session 3 · Lecture: Widening the flow. Instrument-level and line-level signals. TS and TRS cables. Condenser mics and other transducer types. Signal modifiers: DI boxes and hardware preamps. |
| 7 | Wed | Session 4 · Lab: Phone recording → Audacity (Lab 2). Importing phone recordings into Audacity, prepping them through the same pipeline. Worktime on the library. |
| 8 | Mon | Session 5 · Lecture: The mixer. The Toft ATB walked top to bottom: channel strip, in-line architecture, submasters, master section. |
| 8 | Wed | Session 6 · Lab 3: The mixer in practice — live sound. The Sound Below walked through one live-show scenario (FOH mix + stage monitor mixes on the same desk), followed by the You-try widget where students generate a random band lineup and work the routing themselves. Handout 07. |
| 9 | Mon | Session 7 · Lab 4: Studio visit to MB2508. A walk around the studio: the live room, the control room, the Toft and the side-rack gear in person. Handout 08, the self-guided studio-recording walkthrough (one vocal mic to a laptop recording), goes home to try on their own time. Midterm review packet (handout 09) handed out. |
| 9 | Wed | Session 8 · **Midterm: library submission + terminology exam.** Review handout 09 covers the vocabulary on the exam. |

Block-by-block facilitation, demo scripts, common confusions, and pacing fallbacks for each session will be filled in below as the module is built out.

---

## Pre-module preparation (Inés / TA)

*To be expanded.*

- **Paper supplies:** scrap paper (not too thick, not too thin) at every station for Wed Wk 6 recordings. Quantity: enough for each student to have 4 sheets, plus extras
- **Recording gear in the lab's gear storage and inventoried:** dynamic mic, mic stand, XLR cable, audio interface, headphones, one set per workstation. Quick visual check that nothing is missing before the start of Wk 6.
- **Phone-to-Mac transfer method for Wed Wk 7:** to be finalized with IT before Wk 7. The lab Macs may be on a different network segment than the campus Wi-Fi student phones connect to, which rules out methods that depend on device-to-device discovery on the local network. Once IT confirms what's possible, Step 1 of `lessons/05-handout-phone-to-audacity.html` gets filled in
- **Sample library template ready:** a folder structure students will mirror, ideally available as a downloadable starter on the NAS
- **Lecture demo materials:** physical examples of XLR, TS, TRS cables (Wk 6 Mon and Wk 7 Mon); a condenser mic and a DI box to hold up in the Wk 7 Mon lecture
- **MB2508 booked for Mon Wk 9:** the studio visit (Session 7) needs the room reserved a few weeks ahead. The session is a walk around the studio, so the console doesn't have to be powered; if you do power it on to show signal moving, confirm the Toft is in a known-good state and do a quick signal-path check the morning of.
- **Handout 09 (midterm review) printed in advance:** Session 7 hands it out for take-home study, so the document needs to exist before that Monday. It is the next thing to build for this module. A few extra copies for students who lose theirs between Monday and Wednesday.

---

## Module-wide concerns

*To be expanded as sessions are designed.*

### Recurring confusions to expect across the module

*Stub. Likely candidates from Module 2 carry-over and from the recording-specific content:*

- Levels still confusing: the in-line slider, the mix knob, the gain trim, and the Audacity input level are four different things; students need help disambiguating
- "My recording is too quiet" → almost always gain-trim too low (or in-line slider too low, or mix knob set wrong, in that order)
- "My recording is too loud / clipping" → gain-trim too high; reinforce the -12 to -6 dBFS target
- "I can't hear myself while recording" → monitor mix knob on interface set to USB-only instead of a blend
- "My file disappeared" → carry-over from Module 2; the local-first / NAS-as-sync workflow needs to be reinforced because the library is starting to accumulate real value
- *(More to be added as we work through the sessions.)*

### Gear setup baseline (every Wednesday)

Same as Module 2, plus a check that the dynamic mic at every station is the same model (so the lab handouts can refer to a specific mic by name rather than "your dynamic mic").

### Pacing across the module

The pacing pressure point in this module is **Wed Wk 6**: students need to leave with their first four samples recorded, prepped, and in a named folder. If they leave without having gone through the full prep pipeline at least once, the rest of the module loses its scaffold. Plan Wed Wk 6 with the full pipeline as the deliverable, not just the recordings.

The other pacing risk is **Wed Wk 7**: phone recordings + worktime. It's the only session in the module that's primarily unstructured. Students who haven't been recording on their own time will use this session to start, which is fine; students who have been recording will use it for prep and organization, which is also fine; but a student who shows up with nothing and works on nothing is the failure mode to watch for.

### When to escalate to Inés

Same as Module 2.

---

## Session 1 · Mon Wk 6: The basic recording chain

**100 min · Lecture-style · MB2525**

### Roadmap

Names the umbrella concept (signal flow: the path from acoustic source to stored file) and then drills into the basic recording chain as the most common version of it: **dynamic mic → mic-level signal → XLR cable → audio interface**. Each stage of the chain gets a section.

This is the spine reading of the module. Everything else (the Wed Wk 6 lab, the Wk 7 Mon expansion, the Wk 8 Mon mixer lecture) builds on it. Students should walk out able to draw the four-box diagram on a napkin.

### Reading

[`lessons/01-reading-recording-chain.html`](https://csuebmusic.github.io/music-technology-essentials/module-03-recording/lessons/01-reading-recording-chain.html) *(to be written)*

### Connection to Module 1

Module 1 introduced the lab interface and showed students how to plug things in. This lecture re-frames what they already touched as a **signal flow with named stages**, not just a list of objects. The vocabulary lands now because they have hands-on context from Module 2.

### Open questions for when we draft

- Filename: `01-reading-recording-chain.html` (what the reading is mostly about) or `01-reading-signal-flow.html` (what the reading opens with as umbrella)? Probably the former, with the umbrella concept landed in the subtitle and opening section.
- How much polar-pattern detail goes in this reading? (Probably just cardioid mentioned by name, with a single diagram. The fuller polar-pattern treatment can land in the Wk 7 reading or in a separate diagram.)
- Inline SVG diagram of the flow itself (four boxes, labeled connections, with the umbrella name above and the chain-specific labels below) is the visual anchor for the reading. Worth building before the prose.

### Block-by-block

*To be filled in.*

---

## Session 2 · Wed Wk 6: Recording into Audacity (Lab 1)

**100 min · Lab-style · MB2525**

### Roadmap

Students go through the full record-and-prep pipeline end-to-end, using paper as the source material.

**Recording task:** four sounds, recorded into a single Audacity project.

1. Paper crumble, slow
2. Paper crumble, fast
3. Paper rip, slow
4. Paper rip, fast

**Critical detail:** the project opens with a dedicated **noise-profile clip** (10 seconds of room tone, recorded once at the start of the session) before any of the four sounds. The noise profile is what the denoise step uses; capturing it as its own clip is cleaner than tucking silence at the start of every recording, and easier to teach. The four sound clips each carry a one-second silence buffer at start and end, but those are for clean trimming, not for noise capture. Reinforce the noise-profile-first pattern *before* recording starts, not after.

**After recording:** students set up their sample library folder, with the Audacity project living inside it. The folder is the future home of every sample they record this semester.

**Three-step sample prep pipeline:** applied to each of the four sounds, after the noise profile has been captured once from the dedicated noise-profile clip.

1. **Denoise.** Select the sound clip in its entirety, then `Effect → Noise Removal and Repair → Noise Reduction…`, leave the three sliders at their defaults (12 / 6.00 / 3), click OK. (The noise profile itself is captured once at the top of the session by selecting the noise-profile clip and clicking Get Noise Profile.)
2. **Trim and fade.** Delete the silence at the start and end of the clip. Apply a 50-ms Fade In at the new start and a 50-ms Fade Out at the new end to avoid click pops at the trim boundaries.
3. **Normalize.** `Effect → Volume and Compression → Normalize…`, peak target -1.0 dBFS, Remove DC offset checked.

**Export:** each prepped sample exported as a mono WAV from the project (select the clip, then `File → Export Audio…` with Export Range set to **Current selection**). Saved into `sample-library/paper/` following the naming convention.

**Naming convention for samples** (canonical, mirrors the lab handout):

```
[category]-[descriptor]-[variant].wav
```

Examples: `paper-crumble-slow.wav`, `paper-rip-fast.wav`. Lowercase, hyphens, no spaces, no special characters (matches the repo-wide rule).

**Library folder structure** (canonical):

```
~/Documents/lastname/sample-library/
  paper/
    paper-crumble-slow.wav
    paper-crumble-fast.wav
    paper-rip-slow.wav
    paper-rip-fast.wav
  audacity-projects/
    sample-library.aup3
  README.txt            <- student writes; what's in the library, how it's organized
```

The library lives at `~/Documents/lastname/sample-library/` on the local machine and at `students/lastname/sample-library/` on the NAS. The Wk 6 lab handout includes a README template students fill in by hand; the template names the organization and lists the samples.

End-of-session: upload library folder to NAS following the standard session-end routine.

### Handout

[`lessons/02-handout-recording-into-audacity.html`](https://csuebmusic.github.io/music-technology-essentials/module-03-recording/lessons/02-handout-recording-into-audacity.html) — Lab 1

Ten numbered steps from cold start to NAS upload: configure Audacity for mono recording, set gain on the interface against the -12 to -6 dBFS target, set monitor blend, test recording, capture the noise-profile clip, record the four paper sounds, set up the sample-library folder, run the prep pipeline on each clip, export each as a WAV, write the library README, NAS upload. Includes an inline SVG diagram of the headroom target band and five Audacity screenshots at the moments students are most likely to drift.

### Phone-recording reference card

A separate parallel handout, distributed at the end of this session for students to use **outside class**: how to record audio on a phone using a dedicated field-recording app, one for each platform. iPhone students use **Lossless Field Recorder** by edson engineering (free); Android students use **Field Recorder** by Pfitzinger Voice Design ($5.95 on Google Play). Both export 48 kHz / 24-bit WAV; both expose actual controls (mic selection, pickup pattern, sample rate) instead of applying automatic "make it sound good" processing. The card walks through setup on each platform, recording technique (airplane mode, set the phone down, distance, level meter, wind), and a "what records well" starter list. The card stops at the point where students have made a recording they're happy with; getting recordings off the phone, into Audacity, and through the prep pipeline is the work of Wed Wk 7's Lab 2.

Filename: `lessons/03-handout-recording-on-phone.html`. The card isn't module-tied; students keep using it every week onward as they add phone-recorded sounds to their library.

### Pre-class checklist

- Walk the room: gear setup baseline (see Module-wide concerns above) plus the recording-specific extras.
- In the lab's gear storage, confirm every set is present and intact: dynamic mic, mic stand, XLR cable, audio interface, headphones. Students will pull these out per the Session Routines card; the TA's job is to confirm nothing is missing before the room fills.
- Scrap paper at every station: 4 sheets per student plus 2-3 extras for the test-recording step in Step 2 of the handout. Standard 8.5×11 printer paper works well (not cardstock, not tissue).
- Confirm Audacity has the **Noise Removal and Repair** menu accessible (`Effect → Noise Removal and Repair → Noise Reduction…`). Standard in Audacity 3.x; verify on 3 stations during walk-through.
- Test-record on the instructor station: confirm the level meter goes live when clicked, the gain knob produces visible meter response, the headphones produce live monitoring (set the monitor blend toward Inputs first).
- Open the Wed Wk 6 lab handout on the projector and on each student station's desktop browser.
- Phone-recording reference cards stacked at the front of the room. Hand out at end of session.
- Session Routines reference card posted and visible at every station (same as every Wednesday).

### Block-by-block

The session runs 100 min. Pacing target:

| Block | Time | Handout steps | Focus |
|---|---|---|---|
| 1. Setup and gain | 20 min | Steps 1–2 | Audacity recording config, set gain to -12 to -6 dBFS |
| 2. Monitor and test | 10 min | Steps 3–4 | Hear yourself, confirm chain end-to-end |
| 3. Noise profile and recording | 20 min | Steps 5–6 | Room tone clip, four paper sounds |
| 4. Library folder and prep | 30 min | Steps 7–8 | Folder structure, prep pipeline four times |
| 5. Export and NAS upload | 15 min | Steps 9–10 | Mono WAV export, README, end-of-session NAS upload |
| 6. Wrap and phone card | 5 min | — | Hand out phone reference card, preview Mon Wk 7 |

The 100-min budget assumes students arrive on time and complete the start-of-session routine before Block 1 starts. Today's routine is the first session where the mic and XLR cable enter the gear list, so it runs a bit longer than usual; allow 8–10 minutes rather than the usual 5. Demo the mic-and-XLR setup on the instructor station at the front of the class as students arrive so the lab handout's Before-you-start callout gets a visual reinforcement. The 4-stage chain diagram from Monday's reading is the mental model: students should be able to point at their own setup and name each piece.

**Block 1 · Setup and gain (20 min, Steps 1–2).** Walk through Step 1 on the projector with students mirroring on their stations. The Audio Setup dropdown is the new territory: students saw it labeled in Wk 2's interface tour as marker 5, but they didn't open it then. Today they open it and configure four things (Host, Playback Device, Recording Device, Recording Channels). The Recording Channels → **1 (Mono)** setting is the easiest to miss; if a student records to a stereo track with a mono input, the mic shows up on the left channel and silence on the right. Audible only if you balance hard, but the file is wrong.

Then the mono track. `Tracks → Add New → Mono Track`. Quick.

Step 2 (set gain) is where most of the block's time goes. Demonstrate the live-monitoring behavior on the projector: **click the recording level meter** to enter monitoring mode (the meter changes appearance once active), speak into the mic, watch the peaks. Reinforce the target band against the diagram in the handout: peaks of the *loudest sound you're about to make* should land at -12 to -6 dBFS. Then have students do the calibration with a test crumble or quick test rip using scrap paper from the extras pile (not their four sheets).

The single most common error in this block: students set gain by speech-volume rather than by paper-sound volume. Speech into a dynamic mic at 15-20 cm reads quieter than a close-miked paper rip. They'll set gain too high. Demo the test-crumble approach explicitly.

**Block 2 · Monitor and test (10 min, Steps 3–4).** Most students will already be hearing themselves from Block 1 because the gain step requires monitoring. Step 3 just confirms and adjusts the blend; on PreSonus stations, turn the Mixer knob about three-quarters toward Inputs; on Behringer stations, press the Direct Monitor button. Step 4 is a single test recording. The "delete the test clip, add a fresh mono track" step at the end of Step 4 matters: the project should start with a clean empty track for the noise-profile clip in Block 3, not with a residual test recording.

Quick block. Move through it.

**Block 3 · Noise profile and recording (20 min, Steps 5–6).** The noise-profile clip is the most easily skipped step in the whole session. Walk the room during the 10-second capture: every student should be standing still, hands off the mic and the table, mouth closed. If anyone is moving or breathing audibly, their noise profile will be contaminated and the denoise step in Block 4 will produce strange artifacts. Stop the clock if needed; have a student who moved redo it.

Then the four recordings. The handout instructs: hold paper 15-20 cm from the mic, click Record, wait one full second of silence, make the sound, wait one full second more, click Stop. Watch for students who skip the silence buffer and start the sound immediately on Record. The silence is for clean trimming in Block 4, not for noise capture; if they skip it, they risk clipping off the start of the sound during trim.

The four sounds are short — slow rip is ~7 sec, fast rip is one motion. The block's twenty minutes is mostly for the four record-listen-decide-keep-or-redo cycles, not for the recordings themselves. Encourage students to redo any take that didn't capture what they wanted; they have plenty of paper.

By end of Block 3, every student should have five clips on one mono track: noise-profile clip, paper-crumble-slow, paper-crumble-fast, paper-rip-slow, paper-rip-fast. Have them save the Audacity project (Cmd+S) before moving on.

**Block 4 · Library folder and prep (30 min, Steps 7–8).** The longest block. Two distinct phases.

*Phase 1: Folder setup (5 min).* Step 7 in the handout. Students create `~/Documents/lastname/sample-library/` with subfolders `paper/` and `audacity-projects/`. Move the .aup3 file into `audacity-projects/`. The callout in the handout flags that Audacity may lose track of the file after the move; close and re-open the project from the new location. Walk the room and verify the folder structure looks right at every station before any student starts Step 8.

*Phase 2: Prep pipeline (25 min).* Step 8. This is procedure-dense and students will rush. Demonstrate the full pipeline on the instructor station with one sound clip from start to finish before students try it themselves:

1. **Capture the noise profile (once).** Select inside the noise-profile clip → Effect → Noise Removal and Repair → Noise Reduction… → **Get Noise Profile** button. Dialog closes. Audacity now has the profile in memory.
2. **For paper-crumble-slow (the second clip on the track):** Click inside it, Cmd+A to select the full clip (or click-and-drag if Cmd+A grabs the whole track). Open Noise Reduction again, OK at defaults (12 / 6.00 / 3). Then trim the silence buffer at start and end with Delete. Then select 50 ms at the new start, Effect → Fading → Fade In; repeat at the new end with Fade Out. Then Cmd+A on the trimmed clip, Effect → Volume and Compression → Normalize…, peak -1.0 dB, OK.

Then students repeat for the other three sounds. By the end of the block: four clips, all denoised, trimmed, faded, and normalized to -1 dBFS.

Common errors in this block, in rough frequency order:

- Clicking **Get Noise Profile** on each sound clip rather than once on the noise-profile clip. The dialog closes silently and the student thinks denoise has been applied; in fact only the noise profile was updated to whatever clip they had selected. Watch for the second-time-through pattern: if a student opens Noise Reduction on a sound clip and clicks Get Noise Profile instead of OK, intervene.
- Selecting only part of a sound clip for denoise (e.g., just the loud middle). The unselected silence at the edges remains noisy; later trim doesn't help because the noise is mixed into the body of the file.
- Skipping the fades. Audible click pop at the start or end of the file. Easy to miss visually; remind the room when most students are at the trim step.
- Trimming too aggressively, cutting off the natural decay of the sound. The handout says "to just before the sound starts" and "after the sound ends"; let the natural ring or scrape decay into silence rather than chopping it.

**Block 5 · Export and NAS upload (15 min, Steps 9–10).** Export first. Demo the first export on the instructor station: select the clip, File → Export Audio…, fill in the dialog with **special attention to Export Range → Current selection** (the most common error: leaving it at Entire Project, which produces one big file with all four sounds in it). Walk the room during the first export by each student; catch the Export Range error early so the remaining three exports go right.

Filename and folder pattern: `sample-library/paper/paper-crumble-slow.wav` for the first sound, mirroring for the other three.

Then README. Open TextEdit. **Format → Make Plain Text** is the easily-missed step; if a student skips it, they save an .rtf file with smart quotes and styled text. The plain-text move converts the document before they paste the template in. Walk the room during this step.

Then end-of-session NAS upload (same routine as every Wednesday). Drag `sample-library/` from local to `students/lastname/` on the NAS. **Watch the drag direction:** students sometimes drag the parent `lastname/` folder onto the NAS, ending up with `students/lastname/lastname/sample-library/`. Verify a few uploads by opening `students/lastname/sample-library/paper/` on the NAS and counting four WAVs.

**Block 6 · Wrap and phone card (5 min).** Quick close. Hand out the phone-recording reference card on the way out the door. Frame: "From this week on, you can grow your library on your own time using your phone. The card walks through the iPhone and Android setup. Next session we'll talk about other signal types — instrument level, line level, condenser mics, DI boxes — and what cables go with them."

Reminder to do the end-of-session routine on the card before leaving the station: log out, eject NAS, headphones placed on the holder.

### Common confusions

- **Recording device not set.** Student clicks Record, sees no waveform appear. The Audio Setup dropdown was skipped or the wrong device was selected. Most common in Block 1; verify by checking Audio Setup → Recording Device on the affected station.
- **Mono mic recorded to a stereo track.** Recording Channels was left at 2 (Stereo) in Audio Setup. The mic ends up on the left channel; right is silent. The waveform looks half-empty (only the top channel filled). Fix: set Recording Channels → 1 (Mono), delete the stereo track, add a fresh mono track, re-record.
- **Live meter shows nothing.** Student is setting gain without clicking the meter to enable monitoring. Reach over and click the recording level meter at the top of the window; it changes appearance once active.
- **Monitor blend pointed at Playback.** Student can't hear themselves while recording; or they hear themselves with a noticeable delay (round-trip through the computer). On PreSonus, the Mixer knob is pointed toward Playback; turn toward Inputs. On Behringer, the Direct Monitor button isn't pressed in; press it.
- **Noise-profile clip captured with movement.** During the 10-second capture, the student breathed audibly, shifted weight, or touched the cable. The profile carries non-noise content. The denoise step will then "subtract" things that aren't actually constant background, producing artifacts (a whispery underwater quality). Recapture the noise-profile clip.
- **Get Noise Profile vs. Apply Noise Reduction.** Audacity's two-phase dialog confuses many students. Phase 1 captures the profile and closes the dialog without changing anything (audibly silent moment, students think it's broken). Phase 2 applies the reduction. Demo both phases explicitly on the projector; expect to repeat the distinction at individual stations.
- **No silence buffer in the recordings.** Student started the sound on Record instead of waiting a second first. The trim step in Block 4 risks clipping off the start of the sound itself. Mitigate by trimming gently from the visible silence into the start of the waveform, leaving 10-20 ms of pre-sound rather than cutting hard.
- **Click pops at trim points.** Student skipped the 50-ms fade. Listen to a sample of theirs on headphones; if you hear a click at the start or end, walk them back to the fade step.
- **Export Range left at Entire Project.** One WAV file with all four sounds in it instead of four separate WAVs. Catch on the first export; the remaining three should be fine once the dialog defaults to Current selection.
- **TextEdit saved README as .rtf.** Format → Make Plain Text was skipped. The README has styled text and smart quotes. Fix: open the file in TextEdit, Format → Make Plain Text, re-save (overwriting). Or delete and start fresh from the template in the handout.
- **NAS upload contains an extra nesting level.** Student dragged `lastname/` instead of `sample-library/`, ending up with `students/lastname/lastname/sample-library/` on the NAS. Verify by clicking into the upload destination; fix by moving the inner folder up one level.

### Pacing fallbacks

- **Running long in Block 1 (gain setup).** Most likely cause: students struggling with the monitoring-mode click. Demo it once more on the projector with the whole room watching; have neighbors verify each other got the meter live before moving on.
- **Running long in Block 4 (prep pipeline).** The most cuttable thing is the fourth pass through the pipeline: students can apply the pipeline to three sounds in class and the fourth at home, since the project file goes home on the NAS anyway. Keep at least three full passes in class so they have the rhythm.
- **Running short.** Add a fifth recording: students invent an interesting paper sound (e.g., paper sliding against itself, paper folded sharply, paper crinkled in slow motion). They name it themselves following the convention. This makes the naming convention a real decision rather than a recipe.
- **One station's interface fails partway through.** Pair the student with a working-station neighbor; they share the interface for the recording portion and split the prep work between two stations. Note the failed interface for end-of-session diagnosis.

### Paper supplies

Standard 8.5×11 printer paper. About 5 sheets per student (4 for recordings, 1+ for test-crumble during gain setup). Ream of 500 covers many semesters. Avoid cardstock (the crackle is harsh and unrepresentative) and tissue paper (tears too quietly to register clearly through a dynamic mic).

### Critical reminders for the TA

- **Noise-profile clip first.** Before students record any of the four paper sounds, they need a 10-second clip of pure room tone at the top of the project. Walk the room during Step 5 of the handout (the noise-profile capture); a student who skips this won't be able to denoise. The clip should look almost flat in the waveform display, with no audible content.
- **Headroom target: -12 to -6 dBFS peaks.** Don't let students push to -3 or above "to be loud."
- **Don't normalize as a substitute for tracking levels right.** Normalize is for standardizing across already-good recordings, not for rescuing too-quiet ones.
- **The library folder structure is the load-bearing artifact of this session.** If students leave with four good samples but no organized folder, they leave without the actual skill. Make sure the folder is set up and the README started before they go.

### After class

- Walk the room before locking up: all machines logged out, NAS ejected, headphones placed on holders, headphone sliders down to default, interface monitor blend reset to a neutral starting position (center for PreSonus, Direct Monitor unpressed for Behringer), gain knobs back to a sane starting position (around 9-10 o'clock).
- Spot-check 3-4 student folders on the NAS at `students/lastname/sample-library/`: confirm the four WAVs are in `paper/`, the README.txt is at the root, the .aup3 is in `audacity-projects/`.
- Listen to one or two samples per spot-checked folder on headphones: confirm peaks at or near -1 dBFS, no click pops at the start or end, clean denoise without underwater artifacts.
- Note recurring quality issues (e.g. "three of the four students I spot-checked had click pops") for a brief recap moment at the start of Mon Wk 7's lecture.
- Note any interface or mic failures for repair before next session.

---

## Session 3 · Mon Wk 7: Widening the flow

**100 min · Lecture-style · MB2525**

### Roadmap

Builds on Session 1. The basic flow used a dynamic mic, mic-level signal, XLR cable, and the standard interface input. Now we widen the frame to the other signal types, cables, mics, and modifiers students will meet outside that default setup.

**Other signal types:**
- **Instrument level** — what comes out of a guitar or bass pickup. Higher than mic level, lower than line level. Wants a dedicated instrument input (the "Hi-Z" input on most interfaces) or a DI box.
- **Line level** — what comes out of a synth, a mixer, an interface's outputs. The highest level of the three. Wants a line input.

**Other cables:**
- **TS (tip-sleeve)** — two-conductor, unbalanced. Carries instrument-level signals. The guitar cable.
- **TRS (tip-ring-sleeve)** — three-conductor. Can carry balanced line-level (one signal) or unbalanced stereo (two signals). Context-dependent.
- **(XLR already covered in Session 1.)**

**Other mics:**
- **Condenser** — more sensitive, captures more detail, needs phantom power. The studio mic. Different sonic character from a dynamic.
- **Ribbon** — briefly mentioned; warm, fragile, less common in beginner work.
- A note on polar patterns at the working level: omni, cardioid, figure-8. What each means for what the mic picks up.

**Signal modifiers:**
- **DI box** — takes an instrument-level unbalanced signal and outputs a mic-level balanced signal. Lets you plug a guitar into a mic input. Live sound and studio use.
- **Hardware preamp** — takes mic-level and outputs line-level, often with character (color, saturation, warmth). The "1073 sound" or "API sound" some students will hear about later.

### Reading

[`lessons/NN-reading-signals-and-modifiers.html`](https://csuebmusic.github.io/music-technology-essentials/module-03-recording/lessons/) *(to be written; filename to be assigned after Lab 1 handout is named)*

### Open questions for when we draft

- This reading is wide. Open question: one reading or split into two (signals + cables as one; mics + modifiers as another).
- How much condenser-mic detail? Likely: what makes them different, when you'd reach for one, phantom power as a thing to know. Not: large-vs-small diaphragm distinctions, frequency-response curves, etc.

### Block-by-block

*To be filled in.*

---

## Session 4 · Wed Wk 7: Phone recordings into Audacity + worktime (Lab 2)

**100 min · Lab-style · MB2525**

### Roadmap

Two halves.

**First half: getting phone recordings into Audacity and through the prep pipeline.**

- Transferring files from phone to computer: method TBD pending IT confirmation on what's possible between the lab Macs and the campus Wi-Fi student phones connect to. Step 1 of the lab handout is currently a placeholder; it gets filled in once the method is settled
- File format: both apps produce 48 kHz / 24-bit WAV. Audacity opens them directly with no conversion step. This is the payoff of using dedicated field-recording apps instead of the phone's default voice recorder
- Importing into Audacity (drag-and-drop, or File → Import → Audio)
- **Resampling** to the project's 44.1 kHz / 16-bit standard. This is the teaching moment of the lab: sample rate conversion is a routine operation in recording, why we care about matching project rate, what changes (or doesn't) when you resample. Use Tracks → Resample (or the equivalent in the student's Audacity version) to bring the imported clip down to 44.1 kHz
- Running the same three-step prep pipeline (denoise, trim, normalize) on the resampled clip
- Exporting as 44.1 kHz / 16-bit WAV to the library

**Second half: worktime on the library.**

Students record more sounds (in the lab or out in the building hallways, courtyards) and prep them. The TA is available to troubleshoot.

This is the one mostly-unstructured session of the module. Use the room: circulate, ask questions, catch students who are stuck.

### Handout

[`lessons/05-handout-phone-to-audacity.html`](https://csuebmusic.github.io/music-technology-essentials/module-03-recording/lessons/05-handout-phone-to-audacity.html) — Lab 2

Eight steps from phone-side transfer through library upload: get the recording off the phone (transfer method TBD pending IT, currently a placeholder in the handout), pull the library down from the NAS, import, resample 48 kHz → 44.1 kHz, run the prep pipeline (with a noise profile captured from the phone recording itself), export to a student-chosen category folder, README update, worktime, NAS upload. References Lab 1 for the prep-pipeline detail rather than re-walking it.

### Block-by-block

*To be filled in.*

---

## Session 5 · Mon Wk 8: The mixer

**100 min · Lecture-style · MB2525**

### Roadmap

Introduces the mixer as the place where many signal flows converge. Up to now students have thought about one flow at a time (one mic, one signal, one input, one recording). A mixer is what handles many flows at once and gives the engineer routing, processing, and combining tools they couldn't pull off with a single audio interface.

The lecture walks the actual console in the studio (a Toft Audio Designs ATB) top to bottom, in five sections:

1. **The mixer as the place where flows meet.** Conceptual frame: what a mixer is for, how it sits in the chain between mics and audio interface, the analog-vs-digital distinction (a digital mixer like an X32 or SQ can replace the interface; an analog console like the Toft cannot).
2. **The channel strip.** Walked control by control: input gain, phase reverse, 80 Hz HPF, four-band EQ, six aux sends, monitor section, pan/solo/mute, routing buttons to L-R and to subgroup pairs, the channel fader and unity gain. Callouts connect each control back to material from Lectures 1 and 2 (phase to the XLR balanced-cable trick; the EQ to Audacity's Filter Curve EQ; the aux sends to the river-with-taps metaphor; TRS as a third-way wiring on the insert jack).
3. **In-line architecture.** Every strip carries two paths (channel and monitor), both active at the same time. The processing-vs-monitoring distinction lands here, plus the I/P REV button that swaps them at mixdown.
4. **The submaster section.** Eight subgroup strips, what they do, how channels get routed to them, the stereo effects returns.
5. **The master section.** Aux masters, talkback, monitor switching, 2-track returns, the master stereo fader.

The lecture explicitly does *not* walk the live-sound or studio-session scenarios; those are the work of Wednesday's lab (Session 6, live sound) and the studio-recording walkthrough in handout 08, which students work through on their own time after the Wk 9 studio visit. The Monday lecture is "what the console is"; the live-sound lab and the take-home studio walkthrough are "what the console does."

### Reading

[`lessons/06-reading-the-mixer.html`](https://csuebmusic.github.io/music-technology-essentials/module-03-recording/lessons/06-reading-the-mixer.html)

Five sections plus vocabulary and a "for further exploration" pointer: (1) the mixer as the place where many flows meet (with the analog-vs-digital paragraph); (2) the channel strip walked top to bottom on the Toft ATB with seven embedded callouts (phase, EQ, aux sends with river-and-taps SVG, routing/pan worked example, TRS-as-insert-loop, aux-vs-insert with canonical effect categories, processing-vs-monitoring); (3) the in-line architecture and the I/P REV button; (4) the submaster section (subgroups, monitor returns, stereo effects returns); (5) the master section (aux masters, talkback, monitor switching, 2-track returns, master fader). Closes with vocabulary and a "for further exploration" pointer to the Tape Op review of the ATB Series Console, the Sound on Sound review of the ATB24, and the Shure Audio Systems Guide for Music Educators.

The reading uses five photos: a top-down shot of the studio's actual 16-channel ATB (sourced from Retro Gear Shop) as the chapter-opening overview; an annotated front-panel photo of a single input strip with every control labeled (Aux Masters, EQ bands, monitor section, fader); an annotated front-panel photo of the entire group/master section showing all eight submaster strips alongside the master strip (used twice in the reading: section 4 focuses on the submaster strips, section 5 focuses on the master strip); the rear-panel input section showing LINE / MON / INSERT / DIR. O/P + XLR per channel (from the Toft manual); the rear-panel output section showing subgroup outputs, monitor returns, effects returns, aux masters, master output (from the Toft manual). Annotated front-panel photos sourced separately; rear-panel photos credited to Toft Audio Designs / PMI Audio Group; the overview credited to Retro Gear Shop.

### Resolved decisions

- **Detail on the channel strip:** the reading covers what's on the front panel of the Toft input strip in beginner-friendly prose (input gain, phase, 80 Hz filter, four-band EQ, six aux sends, monitor section, solo/mute, pan, routing buttons, fader). Doesn't get into per-band EQ tuning or different EQ topologies.
- **Photos vs schematic diagrams:** photos chosen. The Toft manual's own flow diagrams are too dense for beginners; five photos ground the explanations in the actual console. Conceptual flow is carried by prose, callouts (including the river-and-taps SVG for aux sends), and section structure, rather than by a master schematic.
- **Lecture/lab split:** the console walkthrough (what it is) is Monday's lecture; what it does is split between Wednesday's live-sound lab and the take-home studio walkthrough. Wednesday covers the live-sound scenario in MB2525 with The Sound Below as the running example, then opens into the You-try widget where students generate a new band and route it themselves. The following Monday is a walk around the actual studio in MB2508; the studio-recording walkthrough itself is handout 08, which students work through on their own time.
- **The fictional band:** named (The Sound Below), instrumented, and used as the running example for Wednesday's live-sound lab. The Monday lecture and its reading stay band-agnostic so the console walkthrough doesn't depend on a setup students haven't met yet.

### Block-by-block

*To be filled in.*

---

## Session 6 · Wed Wk 8: The mixer in practice — live sound (Lab 3)

**100 min · Lab-style · MB2525**

### Roadmap

Hands-on session that takes the console students just met in Monday's reading and puts it through one fully worked scenario. The session has two halves: a walked scenario (with the lecturer demonstrating routing decisions on the projected console image at the front of the room) and an interactive widget where students generate a random band and route it themselves.

**The fictional band: The Sound Below.** A five-piece, introduced in this lab handout as the running example for the live-sound walkthrough. Instrumentation chosen to exercise every signal type and mic introduced in Lectures 1 and 2, plus the canonical DI-dry-plus-amp-wet bass treatment and the standard kick-snare-overheads drum miking from Huber (Modern Recording Techniques, 2018), plus a stage keyboardist with a laptop running alongside (the only line-level signals in the band):
- **Vocals:** dynamic mic, mic-level signal, XLR
- **Electric guitar:** amp mic'd with a dynamic, mic-level, XLR
- **Bass guitar:** recorded two ways simultaneously, DI dry (XLR out of the DI box) + amp wet (dynamic mic on the bass amp's speaker, XLR). The DI box's thru jack passes the instrument signal on to the amp.
- **Drums:** four mics, kick (dynamic) + snare (dynamic) + two overhead condensers (left and right, both needing phantom power), four XLRs
- **Keys + laptop:** four line-level signals (stage keyboard L+R, laptop L+R), brought to mic-level via a four-channel DI box at the keyboardist's station

Twelve signals into the console total. With sixteen input channels on our console, the band fills three-quarters of the desk.

**Scenario 1: Live sound (walked).** The band is playing a small venue. The mixer's job is to take everything happening on stage and send it two places: (1) the front-of-house speakers the audience hears (via the L-R master mix at MASTER O/P), (2) the stage monitors each performer hears (via the aux sends, pre-fader, with each aux carrying a different blend for a different performer). The handout walks the channel chart, the FOH routing (three patches: direct-to-master, drums-to-subgroup-1-2, keys-and-laptop-to-subgroup-3-4), and the stage monitor mixes (five auxes, one per performer).

**Scenario 2: You try! (interactive widget).** The same console, the student doing the patching. A "Generate a band" button pulls a random lineup from a pool of six bands, each chosen to expose one routing concept past what The Sound Below covered (when not to use subgroups, stereo line sources on a subgroup pair, double-mic'd kick, multiple stereo subgroups for a jazz quartet, all-line-level electronic duo, sit-in performer with mute-via-subgroup). For each lineup the widget presents three reveal-on-click questions: build the channel chart (blank fillable table renders first; the reveal shows a suggested chart plus notes on phantom power and LINE-button decisions); plan the FOH mix (the reveal shows recipe-style patches with specific button presses, pans, and submaster moves, plus a trade-off callout); plan the stage monitor mixes (the reveal opens with how many auxes are needed, runs the universal pre-fader stage-monitor recipe as numbered steps, then shows the per-aux blend table for this band).

**The synthesis.** Auxes are routing tools; subgroups are routing tools; the master is a routing tool. They look the same on the desk regardless of context; what differs is what's plugged into them and where their output goes. The studio half of that synthesis, the same auxes feeding performer headphone cues instead of stage monitors, lives in handout 08, which students work through on their own time after seeing the studio in person on the Wk 9 visit.

### Handout

[`lessons/07-handout-the-mixer-in-practice.html`](https://csuebmusic.github.io/music-technology-essentials/module-03-recording/lessons/07-handout-the-mixer-in-practice.html) — Lab 3

Walks the live-sound scenario in full detail, then opens the You-try widget. Today's gear is minimal (this is a desk-and-projector session, not a recording session). Students follow the walkthroughs as the lecturer demonstrates the routing decisions on the projected console image, then work the widget at their stations.

### Block-by-block

*To be filled in.*

---

## Session 7 · Mon Wk 9: Studio visit to MB2508 — a walk around the studio (Lab 4)

**100 min · Lab-style · MB2508 (studio)**

### Roadmap

The session moves to MB2508, where the actual Toft ATB lives, so students see a working studio in person before the module closes. There's only time for a walk around the room and to hand out the midterm materials, so this is a guided tour, not a hands-on recording session. Students see the two rooms (the live room where performers play, the control room where the engineer sits), the Toft on its console desk, the side-rack gear that feeds it (the two preamps, the SSL bus compressor, the Behringer, the HDX interface, the Rane headphone amp), and the wall of feed-throughs that connects the rooms.

The detailed studio-recording walkthrough is not done in class. It lives in handout 08, which students take home and work through on their own time when the studio is free. The handout is self-contained: it documents the gear room by room and walks one vocal mic from the live room to a finished recording, so a student can follow it at the desk without an instructor present. The reason it exists is exactly this, so they can try the whole chain themselves rather than watch it once.

**Studio visit structure (working draft):**
- Walk students to MB2508 at the start of class. (~5 min)
- Tour the two rooms and the wall panel between them: what's in the live room (mics, the preamp and headphone racks), what's in the control room (the Toft, the side rack, the monitors), and how a signal crosses from one room to the other. (~20 min)
- At the Toft, identify the input strips, submasters, master section, and master fader in person; point out the front-of-channel controls (phase, HPF, EQ, aux sends, monitor section, pan, routing buttons, fader) and the rear-panel jacks on a real input section (LINE, MON, INSERT, DIR. O/P, MIC). (~25 min)
- Walk the side-rack gear, naming what each piece does in the chain: the two preamps, the SSL compressor, the Behringer, the HDX interface running Pro Tools, the Rane headphone amp. Point students to handout 08 for the full detail on each. (~20 min)
- Optional, if time and setup allow: power the console on and pass one signal through a single channel strip to the monitors, just to show sound moving. If the studio isn't set up, the tour stays observational. (~15 min)
- Hand out handout 08 (the studio-recording walkthrough, to try on their own time) and the midterm review packet (handout 09, for take-home study before Wednesday's exam). (~10 min)

### Handout

[`lessons/08-handout-studio.html`](https://csuebmusic.github.io/music-technology-essentials/module-03-recording/lessons/08-handout-studio.html) — Lab 4

A self-guided studio guide and walkthrough, written so a student can follow it at the desk on their own time. It documents the studio gear room by room (the live-room rack, the control-room console and side rack, and a full signal-flow map of every jack on the Toft), then walks one vocal mic end to end: from a mic in the live room, onto the Toft, into the singer's headphone cue, through a reverb on the Behringer FX processor and parallel compression on the SSL, and out to a 48 kHz / 16-bit recording on a laptop via the Behringer. Closes with a comping section (Logic Pro and Ableton Live). Not walked in class; handed out at the studio visit for students to work through when the studio is free.

### Midterm review packet

[`lessons/09-handout-midterm-review.html`](https://csuebmusic.github.io/music-technology-essentials/module-03-recording/lessons/09-handout-midterm-review.html) *(to be written)*

Distributed at the end of Session 7 for take-home study. Synthesizes Module 3 vocabulary and concepts in one place. Maps every term back to the lesson where it was introduced so students can re-read the specific section if a term is unfamiliar. Closes with a "what to bring to the exam" reminder (just yourself; closed-book, no devices) and a note that the library submission happens before the exam, so students should arrive with the library uploaded and verified-ready.

### Block-by-block

*To be filled in.*

---

## Session 8 · Wed Wk 9: Midterm — library submission + terminology exam

**100 min · Mixed format · MB2525**

### Roadmap

Students walked out of Session 7 with the midterm review packet (handout 09) for take-home study; today is when they prove the work. Two parts.

**Part 1 (first ~30 minutes): library submission.**

Students upload their final library to the NAS following the submission card on the midterm prompt. The TA verifies each upload before moving on:
- Folder is at the correct location
- Folder structure matches the convention
- README is present and filled in
- All files are 44.1 kHz / 16-bit WAV
- Filenames follow the convention
- Minimum sound count met

**Part 2 (remaining ~60–70 minutes): terminology exam.**

Cumulative in-class exam covering Modules 1 through 3 vocabulary and concepts. Closed-book, no devices.

### Exam scope (working draft)

To be expanded into the actual exam document [`projects/terminology-exam.md`](./projects/terminology-exam.md) *(TA-facing, with answer key)*.

Vocabulary and concepts on the exam should include:
- Sample rate, bit depth, dynamic range (Module 2)
- Envelope: attack, sustain, release (Module 2)
- Edit techniques: cuts, fades, time-stretch, pitch-shift, reverse (Module 2)
- Levels: dBFS, headroom, clipping, peak vs. RMS (Module 2)
- EQ, compression, limiting (Module 2)
- Stereo placement: pan, mono vs. stereo (Module 2)
- Signal flow: tracing the path from acoustic source to stored file (Module 3)
- The basic recording chain: mic, signal, cable, interface (Module 3)
- Transducer types: dynamic, condenser, ribbon (Module 3)
- Polar patterns: omni, cardioid, figure-8 (Module 3)
- Signal types: mic, instrument, line (Module 3)
- Cables: XLR, TS, TRS (Module 3)
- Signal modifiers: DI, preamp (Module 3)
- Mixer: channel strip, aux, bus, monitor send (Module 3)
- File workflow: local-first, NAS-as-sync (Module 1, reinforced throughout)

### Block-by-block

*To be filled in.*

---

## End-of-module assessment

*To be expanded.*

### What success looks like

Students at the end of Module 3 should be able to:

1. Trace the signal flow at any setup they meet, from acoustic source to stored file
2. Set up a recording session from cold and capture a clean recording
3. Move a phone recording through the prep pipeline into their library
4. Navigate their own library and find a sound by category or by name
5. Distinguish signal types, cables, and transducer types
6. Describe what auxes and busses do in two different contexts
7. Pass the cumulative terminology exam

### Across-the-cohort signs of trouble

*To be filled in as the module is taught. Likely candidates:*

- Libraries with no README or with a one-line README → the organization lesson didn't land; reinforce in Module 4 with an explicit "find a sound from your library" exercise
- Libraries where every file peaks at 0 dBFS → normalization is being applied as a "make it loud" step rather than a standardization; the "scale not shape" framing from Module 2 needs another pass
- Libraries where files have noticeable click pops at the cuts → trim step is being done sloppily, fades aren't being added at trim points; reinforce the fade habit explicitly
- Students who can't trace signal flow on the terminology exam → the Wk 6 Mon reading didn't stick; rethink whether the flow diagram is doing enough

### Forward promises to deliver in later modules

*Stub. To be filled in as readings are drafted.*

- The peer-listening discussion on Mon Wk 10 (start of Module 4) opens with a discussion of the sample libraries students just submitted. Plan that into Module 4's first session.
- Sample libraries built in this module become the source material for Module 4 audio work (Wks 10–11 in Ableton). The "your library" framing should appear in the Module 4 README.
- The ADSR forward-promise from Module 2 (Mon Wk 3 reading) is still outstanding for Module 4 synthesis content.

### What gets logged

After Module 3 ends, write a short retrospective covering what went well, what didn't, pacing notes, and questions that surprised you.

---

## What follows

Module 4 (Wks 10–14) moves into Ableton. Audio work first, MIDI and synthesis second. The sample libraries built in this module are the bridge: students will load their own libraries into Ableton in Wk 10 and start making pieces from their own recorded material.
