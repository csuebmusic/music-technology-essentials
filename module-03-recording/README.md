# Module 03 — Recording, Sample Prep & Library Building

**Weeks 6–8 · 6 sessions (600 minutes total)**

> **Status:** Roadmap in place. Session blocks are stubs to be filled in between sessions as the module is built out. The spec at the top is the load-bearing part for now.

---

## Module purpose

Module 2 taught students to manipulate sound that was handed to them. Module 3 teaches them to make their own. By the end of three weeks they should be able to plug in a microphone, capture a clean recording, prepare the file for use, and organize it into a usable library.

The deliverable is the library itself, the curated and organized collection of sounds students will draw from for the rest of the semester (and beyond). The midterm is two parts: the library submission, and a terminology exam covering Modules 1 through 3.

The arc of the module: understand the recording chain → record into Audacity → expand the chain (other signal types, other mics, signal modifiers) → understand the live-vs-studio context (mixers, auxes, busses) → submit the library.

Three principles thread through the module:

1. **Record with headroom.** Module 2 promised this in the Mon Wk 2 reading; Module 3 is where it gets delivered. Peaks around -12 to -6 dBFS while recording, room to commit later in editing.
2. **The recording chain is a sequence of decisions.** Mic, signal type, cable, interface. Each link is a choice, and each one has consequences. Students should be able to look at a setup and name the chain.
3. **A sample is not a recording.** A recording is what comes out of the mic; a sample is what goes into the library. The difference is the prep step (denoise, trim, normalize), and the prep step is non-negotiable.

By the end of Wk 8, students should have a working library of their own recordings, prepped to a consistent standard, organized in a documented folder structure, ready to use as raw material in Module 4 (Ableton).

---

## Learning outcomes

By the end of this module, students should be able to:

1. Name the components of the basic recording chain (mic, signal, cable, interface) and describe what each one does
2. Distinguish dynamic, condenser, and (briefly) ribbon microphones, and know when to reach for each
3. Distinguish mic-level, instrument-level, and line-level signals, and match each to the correct input on an interface
4. Identify XLR, TS, and TRS cables and know what each carries
5. Set up a recording session in Audacity from cold: select input, set gain, monitor, record with headroom
6. Prepare a recorded sample for use: denoise, trim, normalize to a consistent standard
7. Organize a sample library with a documented folder structure, consistent naming, and a README
8. Record audio on a phone (iPhone or Android) at a quality suitable for adding to the library
9. Describe the difference between a live-sound mixer and a recording session: what auxes and busses do in each context
10. Pass a cumulative terminology exam covering vocabulary from Modules 1 through 3

---

## Key concepts introduced

- **The recording chain:** mic → signal → cable → interface → DAW. Each link is a discrete component with a job. Students should be able to point at any link and name what it does.
- **Transducer types:** dynamic mics (moving-coil, what's at every station; rugged, no power needed, common); condenser mics (more sensitive, more detail, need phantom power); ribbon mics (mentioned for completeness, not used in the lab).
- **Polar patterns:** at a beginner level. Cardioid is what students will mostly meet at the lab. Omni and figure-8 introduced for vocabulary.
- **Signal types:** mic level (small, needs preamp), instrument level (medium, from a guitar or bass pickup), line level (large, from a synth or interface output). Each one wants a different input.
- **Cables:** XLR (balanced, three-conductor, carries mic-level and line-level signals; what's at every station for the dynamic mic). TS (unbalanced, two-conductor, carries instrument-level signals; what plugs into a guitar). TRS (three-conductor, carries balanced line-level or stereo, depending on context).
- **Signal modifiers:** the DI box (instrument level → mic level, balanced) and the hardware preamp (mic level → line level, with character). Where they sit in the chain and why.
- **Recording with headroom:** peaks around -12 to -6 dBFS while tracking. The reason: leaving room to make decisions in editing, not committing to a level you can't undo. This delivers on the Module 2 promise (Mon Wk 2 reading, §5).
- **The sample prep pipeline:** a three-step standardization process applied to every raw recording before it enters the library. (1) Denoise using a captured silence sample; (2) trim silence at start and end; (3) peak-normalize to a consistent ceiling. The pipeline turns a recording into a sample. This delivers on the Module 2 promise (Mon Wk 5 reading, §2): "scale, not shape."
- **Library organization:** folder structure, naming conventions, an internal README. The library is a usable resource, not a pile of files. Students who can find a sound in their library will use their library; students who can't, won't.
- **The mixer (introduction):** the central routing surface in both live sound and studio recording. Channel strips, faders, auxes, busses. Students don't need to operate one yet; they need to understand what it is and why it's the shape it is.
- **Auxes and busses:** what they route in a live context (monitor sends to performers' floor wedges) vs. a studio context (headphone mixes for performers being recorded). The same mechanism, two different uses.

---

## Deliverable: Midterm

Two parts, both due Wed Wk 8.

### Sample library

A submitted folder of the student's own recorded sounds, prepped through the standardization pipeline and organized into a documented structure on the NAS.

Full prompt and rubric: [`projects/project-02-sample-library.html`](https://csuebmusic.github.io/music-technology-essentials/module-03-recording/projects/project-02-sample-library.html) *(to be written)*

**Scope (working target, revisit when drafting the prompt):** ~15–25 prepped sounds, organized in a documented folder structure with a student-written README, all files at 44.1 kHz / 16-bit WAV, all named per convention.

**Timeline:**
- Wk 6 Wed: students record their first 4 sounds in lab (paper crumble x2 speeds, paper rip x2 speeds), prep them, and submit them as a starter library
- Wk 7 onward: students record additional sounds in lab and on their phones outside class
- Wk 8 Wed: final library submission

### Terminology exam

A cumulative in-class exam covering Modules 1 through 3 vocabulary and concepts. ~30 minutes, in-class on Wed Wk 8 after library submission is verified.

Full exam and answer key: [`projects/terminology-exam.md`](./projects/terminology-exam.md) *(to be written, TA-facing only)*

---

## Listening assignment

**Module 3 historical listening:** Field recording and acousmatic tradition. Composers and sound artists who treat recording itself as the compositional act. Chris Watson, Hildegard Westerkamp, Francisco López as starting points; the choice of three pieces and the framing are to be finalized when the assignment is drafted.

Full listening assignment with guided questions: [`listening/historical.html`](https://csuebmusic.github.io/music-technology-essentials/module-03-recording/listening/historical.html) *(to be written)*

**Due:** Mon Wk 8, before class. (Pacing rationale: gives students the field-recording listening vocabulary before the mixer / live-vs-studio session, and before the midterm.)

**Peer listening:** Module 3 also includes a peer-listening assignment, where students browse and listen to each other's sample libraries after midterm submission and respond briefly. The format differs from Module 2's peer listening: students are listening to *libraries* (collections of curated sounds) rather than *finished pieces*, so the prompts orient toward what's in the libraries and what the listener would do with it.

Peer listening assignment: [`listening/peer-midterm.html`](https://csuebmusic.github.io/music-technology-essentials/module-03-recording/listening/peer-midterm.html) *(to be written)*

**Due:** Mon Wk 9, before class.

---

## Session overview

| Wk | Day | Focus |
|---|---|---|
| 6 | Mon | Session 1 · Lecture: The basic recording chain. Dynamic mic, mic-level signal, XLR cable, audio interface. End-to-end ADC flow with the most common components. |
| 6 | Wed | Session 2 · Lab: Recording into Audacity (Lab 1). Project setup, four paper recordings (crumble slow/fast, rip slow/fast), three-step sample prep pipeline (denoise / trim / normalize), library folder set up, naming convention established. Phone-recording reference card distributed. |
| 7 | Mon | Session 3 · Lecture: Expanding the chain. Instrument-level and line-level signals. TS and TRS cables. Condenser mics and other transducer types. Signal modifiers: DI boxes and hardware preamps. |
| 7 | Wed | Session 4 · Lab: Phone recording → Audacity (Lab 2). Importing phone recordings into Audacity, prepping them through the same pipeline. Worktime on the library. |
| 8 | Mon | Session 5 · Lecture: The mixer. Live sound vs. recording session walkthrough using a fictional band as the running example. Auxes, busses, monitor sends, headphone mixes. |
| 8 | Wed | Session 6 · **Midterm: library submission + terminology exam.** |

Block-by-block facilitation, demo scripts, common confusions, and pacing fallbacks for each session will be filled in below as the module is built out.

---

## Pre-module preparation (Inés / TA)

*To be expanded.*

- **Paper supplies:** scrap paper (not too thick, not too thin) at every station for Wed Wk 6 recordings. Quantity: enough for each student to have 4 sheets, plus extras
- **Every station's recording chain verified:** dynamic mic in stand, XLR connected, interface gain trim at a sane starting position, headphones connected with in-line slider checked
- **Sample library template ready:** a folder structure students will mirror, ideally available as a downloadable starter on the NAS
- **Lecture demo materials:** physical examples of XLR, TS, TRS cables (Wk 6 Mon and Wk 7 Mon); a condenser mic and a DI box to hold up in the Wk 7 Mon lecture
- **Fictional band sketch (Wk 8 Mon):** 4–5 piece band, defined instruments and stage positions, so the live-vs-studio walkthrough is concrete. Worth writing out in advance so the lecture doesn't drift

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

The basic ADC flow with the most common components a student will encounter: **dynamic mic → mic-level signal → XLR cable → audio interface**. Each link in the chain gets a section.

This is the spine reading of the module. Everything else (the Wed Wk 6 lab, the Wk 7 Mon expansion, the Wk 8 Mon mixer lecture) builds on it. Students should walk out able to draw the four-box diagram on a napkin.

### Reading

[`lessons/01-reading-recording-chain.html`](https://csuebmusic.github.io/music-technology-essentials/module-03-recording/lessons/01-reading-recording-chain.html) *(to be written)*

### Connection to Module 1

Module 1 introduced the lab interface and showed students how to plug things in. This lecture re-frames what they already touched as a **chain of decisions**, not just a list of objects. The vocabulary lands now because they have hands-on context from Module 2.

### Open questions for when we draft

- How much polar-pattern detail goes in this reading? (Probably just cardioid mentioned by name, with a single diagram. The fuller polar-pattern treatment can land in the Wk 7 reading or in a separate diagram.)
- Inline SVG diagram of the chain itself (four boxes, labeled connections) is the visual anchor for the reading. Worth building before the prose.

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

**Critical detail:** each recording must include a small amount of **silence at the start** before the sound begins. The silence is what the denoise step uses as its noise profile. If they don't record the silence, they can't denoise properly. Reinforce this *before* they start recording, not after.

**After recording:** students set up their sample library folder, with the Audacity project living inside it. The folder is the future home of every sample they record this semester.

**Three-step sample prep pipeline:** applied to each of the four sounds.

1. **Denoise.** Select the initial silence in the file to capture a noise profile, then apply Noise Reduction (Effect → Noise Reduction → Get Noise Profile → re-select the whole clip → Effect → Noise Reduction → OK with default values).
2. **Trim.** Cut silence at the start and end of the sound. The silence-at-start was for denoising; once denoise is done, it goes.
3. **Normalize.** Apply Audacity's Normalize effect with peak target at -1 dBFS. This is the "scale, not shape" move from the Module 2 dynamics reading.

**Export:** each prepped sample exported as a WAV from the project (File → Export → Export as WAV), saved into the library folder following the naming convention established in this session.

**Naming convention for samples:** to be finalized in [`meta/naming-conventions.md`](../meta/naming-conventions.md) before this session. Working proposal:

```
[category]-[descriptor]-[variant].wav
```

Examples: `paper-crumble-slow.wav`, `paper-rip-fast.wav`. Lowercase, hyphens, no spaces, no special characters (matches the repo-wide rule).

**Library folder structure for the session:** also to be finalized. Working proposal:

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

End-of-session: upload library folder to NAS following the standard session-end routine.

### Handout

[`lessons/02-handout-recording-into-audacity.html`](https://csuebmusic.github.io/music-technology-essentials/module-03-recording/lessons/02-handout-recording-into-audacity.html) *(to be written; this is Lab 1)*

The handout walks students through: opening Audacity, setting input to the audio interface, setting gain trim, monitor blend, doing a test recording, listening back, recording the four sounds, the prep pipeline, exporting, organizing into the library folder.

### Phone-recording reference card

A separate parallel handout, distributed at the end of this session for students to use **outside class**: how to record audio on iPhone (Voice Memos) and Android (default Voice Recorder or recommended alternative). Holding the phone, distance from source, wind/handling noise, file format and how to get the file off the phone.

Filename to be decided: likely `lessons/03-handout-recording-on-phone.html`. Whether this is `Handout N` or `Reference card` in the chrome depends on whether we treat it as Module-3-specific or as a semester-long reference. Bias toward `Module 03 · Handout N` since the framing is "we just did interface recording in lab; here's the parallel for outside class."

### Block-by-block

*To be filled in.*

### Critical reminders for the TA

- **Verify every station has silence-before-sound habits before recording.** This is the most easily-missed step and it makes or breaks the denoise.
- **Headroom target: -12 to -6 dBFS peaks.** Don't let students push to -3 or above "to be loud."
- **Don't normalize as a substitute for tracking levels right.** Normalize is for standardizing across already-good recordings, not for rescuing too-quiet ones. The Module 2 dynamics reading already framed this; the lab reinforces it.
- **The library folder structure is the load-bearing artifact of this session.** If students leave with four good samples but no organized folder, they leave without the actual skill. Make sure the folder is set up and the README started before they go.

---

## Session 3 · Mon Wk 7: Expanding the chain

**100 min · Lecture-style · MB2525**

### Roadmap

Builds on Session 1. The basic chain was mic-level → XLR → interface. Now we open up the other links.

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

- This reading is wide. Worth deciding whether it's one reading or split into two (signals + cables as one; mics + modifiers as another). My instinct is one reading with clear section breaks, since the framing is "all the other things you might meet in the chain."
- How much condenser-mic detail? Likely: what makes them different, when you'd reach for one, phantom power as a thing to know. Not: large-vs-small diaphragm distinctions, frequency-response curves, etc.

### Block-by-block

*To be filled in.*

---

## Session 4 · Wed Wk 7: Phone recordings into Audacity + worktime (Lab 2)

**100 min · Lab-style · MB2525**

### Roadmap

Two halves.

**First half: getting phone recordings into Audacity and through the prep pipeline.**

- Transferring files from phone to computer (AirDrop for iPhone; USB or Files app for Android; alternatives like a quick cloud upload)
- File formats from phones: iPhone Voice Memos produce M4A; Android default depends on app. Both need to be imported into Audacity.
- Importing into Audacity (File → Import → Audio, or drag-and-drop)
- Running the same three-step prep pipeline (denoise, trim, normalize) on the phone recording
- Exporting as 44.1 kHz / 16-bit WAV to the library

**Second half: worktime on the library.**

Students record more sounds (in the lab or out in the building hallways, courtyards) and prep them. The TA is available to troubleshoot.

This is the one mostly-unstructured session of the module. Use the room: circulate, ask questions, catch students who are stuck.

### Handout

[`lessons/NN-handout-phone-to-audacity.html`](https://csuebmusic.github.io/music-technology-essentials/module-03-recording/lessons/) *(to be written; this is Lab 2)*

Walks through the phone → computer → Audacity → prep → library flow, with screenshots of the relevant moments.

### Block-by-block

*To be filled in.*

---

## Session 5 · Mon Wk 8: The mixer · live vs. studio

**100 min · Lecture-style · MB2525**

### Roadmap

Introduces the mixer as the central routing surface in audio work. The pedagogical move: walk through **the same fictional band in two scenarios** (live performance and studio session) to surface what's the same and what's different.

**The fictional band:** to be sketched. Working assumption: 4–5 piece. Vocals, guitar, bass, drums, maybe keys. Each instrument has known mic-and-signal requirements that connect back to Wk 6 Mon and Wk 7 Mon.

**Scenario 1: Live sound.**

The band is playing a small venue. The mixer's job is to take everything happening on stage and send it two places: (1) the front-of-house speakers the audience hears, (2) the monitor wedges or in-ears each performer hears.

Concepts that land here:
- **Channel strips** — one per input. Gain, EQ, fader.
- **The main mix** — what comes out the front-of-house speakers.
- **Aux sends** — separate mixes that go to a different destination. In live sound, auxes feed monitor wedges (each performer wants to hear a different mix).

**Scenario 2: Studio recording session.**

The same band, now in a studio. The mixer's job changes. Front-of-house speakers don't exist; the audience is the recording. The performers wear headphones, and each performer's headphone mix is what they need to play to.

Concepts that land here:
- The same channel strips, the same EQ, the same faders
- **Auxes** now feed **headphone mixes** instead of monitor wedges. The mechanism is the same; the destination is different.
- **Busses** — groups of channels routed together (e.g. all drum mics summed to a "drums" bus before going to the mix). Useful both live and in studio, but easier to introduce in the studio context.
- **Recording sends** — the mix going to the DAW for capture.

**The synthesis:** auxes and busses are routing tools. They look the same on the mixer; what's different is what's plugged into them. Once a student understands that, the apparent complexity collapses.

### Reading

[`lessons/NN-reading-the-mixer.html`](https://csuebmusic.github.io/music-technology-essentials/module-03-recording/lessons/) *(to be written)*

### Open questions for when we draft

- How much detail on the channel strip itself? (Probably: gain, EQ briefly, fader, pan, aux sends, mute/solo. Not: per-band EQ tuning, parametric vs. graphic, etc.)
- Should the reading include actual photos of mixers, or schematic diagrams, or both? Schematic diagrams probably read more clearly for beginners; a single photo of a real mixer at the start grounds the abstraction.
- The fictional band needs a name and a defined instrumentation before this is drafted. Worth doing as a one-pager (the band, who's in it, what they play, what mics/signals each one uses) so the reading and the lecture both pull from the same source.

### Block-by-block

*To be filled in.*

---

## Session 6 · Wed Wk 8: Midterm — library submission + terminology exam

**100 min · Mixed format · MB2525**

### Roadmap

Two parts.

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
- The recording chain: mic, signal, cable, interface (Module 3)
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

1. Set up a recording session from cold and capture a clean recording
2. Move a phone recording through the prep pipeline into their library
3. Navigate their own library and find a sound by category or by name
4. Explain the recording chain at a conversational level
5. Distinguish signal types and cables
6. Describe what auxes and busses do in two different contexts
7. Pass the cumulative terminology exam

### Across-the-cohort signs of trouble

*To be filled in as the module is taught. Likely candidates:*

- Libraries with no README or with a one-line README → the organization lesson didn't land; reinforce in Module 4 with an explicit "find a sound from your library" exercise
- Libraries where every file peaks at 0 dBFS → normalization is being applied as a "make it loud" step rather than a standardization; the "scale not shape" framing from Module 2 needs another pass
- Libraries where files have noticeable click pops at the cuts → trim step is being done sloppily, fades aren't being added at trim points; reinforce the fade habit explicitly
- Students who can't name the chain on the terminology exam → the chain reading from Wk 6 Mon didn't stick; rethink whether the diagram in the reading is doing enough

### Forward promises to deliver in later modules

*Stub. To be filled in as readings are drafted.*

- The peer-listening discussion on Mon Wk 9 (start of Module 4) opens with a discussion of the sample libraries students just submitted. Plan that into Module 4's first session.
- Sample libraries built in this module become the source material for Module 4 audio work (Wks 9–11 in Ableton). The "your library" framing should appear in the Module 4 README.
- The ADSR forward-promise from Module 2 (Mon Wk 3 reading) is still outstanding for Module 4 synthesis content.

### What gets logged

After Module 3 ends, write a short retrospective covering what went well, what didn't, pacing notes, and questions that surprised you.

---

## What follows

Module 4 (Wks 9–14) moves into Ableton. Audio work first, MIDI and synthesis second. The sample libraries built in this module are the bridge: students will load their own libraries into Ableton in Wk 9 and start making pieces from their own recorded material.
