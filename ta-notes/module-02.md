# TA Notes — Module 02

This module is the foundation of the course. Students learn what digital audio is, how to manipulate it, and how to shape a balanced mix — and they make their first piece. By the end of Wk 5 they should be able to take a folder of source sounds and produce a deliberately edited, mixed, 2-minute piece. That is not a small jump from Day 1.

The module spans seven sessions. They are not interchangeable. The Mondays are lecture-style (concept introduction, listening, discussion); the Wednesdays are lab-style (hands-on, tools, project work). Students need both rhythms — the Monday sessions give them vocabulary and ear training, the Wednesday sessions give them craft. If you find yourself drifting toward the lab pattern on a Monday, pull back: students who only do the lab work without the conceptual frame produce technically functional but creatively shallow pieces.

Project 1 launches Wed Wk 3 and is due Wed Wk 5. Two and a half weeks. The clock is tight on purpose — students who have a month tend to use the first three weeks avoiding the work.

This file is the operational runbook for all seven sessions. Module spec (the "what") is in [`course/modules/module-02.md`](../course/modules/module-02.md); this file is the "how."

---

## Contents

- [Module-wide concerns](#module-wide-concerns)
- [Session 1 — Mon Wk 2: Digital audio fundamentals](#session-1--mon-wk-2-digital-audio-fundamentals)
- [Session 2 — Wed Wk 2: Digital audio explorer + Audacity orientation](#session-2--wed-wk-2-digital-audio-explorer--audacity-orientation)
- [Session 3 — Mon Wk 3: Editing concepts + envelope listening](#session-3--mon-wk-3-editing-concepts--envelope-listening)
- [Session 4 — Wed Wk 3: Editing techniques + Project 1 begins](#session-4--wed-wk-3-editing-techniques--project-1-begins)
- [Session 5 — Wed Wk 4: Mixing tool Part 1 + Project 1 work](#session-5--wed-wk-4-mixing-tool-part-1--project-1-work)
- [Session 6 — Mon Wk 5: Dynamics + mixing tool Part 2](#session-6--mon-wk-5-dynamics--mixing-tool-part-2)
- [Session 7 — Wed Wk 5: Project 1 final work session + submission](#session-7--wed-wk-5-project-1-final-work-session--submission)
- [End-of-module assessment](#end-of-module-assessment)

---

## Module-wide concerns

### Recurring confusions to expect across the module

- **"Why does my recording sound thin/loud/quiet?"** Almost always a level-staging issue, an interface direct-monitor mix knob set wrong, or headphones with the in-line slider not all the way up. Train yourself to ask three questions in this order: (1) Is the in-line slider on the headphones up? (2) Is the interface mix knob set correctly (60% direct / 40% USB by default)? (3) Are the levels in Audacity reasonable (peaks around -12 to -6 dBFS, never clipping)?
- **"My file disappeared."** Almost always means they saved to the wrong location, or saved as a project file (`.aup3`) when they meant to export as WAV, or didn't upload to NAS at session end. Walk them through the local-first / NAS-as-sync workflow again. The Session Routines card (Handout 02) is at every station for this reason — point at it.
- **"Audacity crashed."** It will. Audacity's autosave is good but not perfect. Reinforce the version-saving habit (`-v1.aup3`, `-v2.aup3`) early. If a student lost work, the right response is sympathy and a process correction, not panic.
- **"Why doesn't my edit sound smooth?"** Usually missing fades. The single most useful Audacity habit is to add a small fade-in/fade-out (5-50 ms) on every edit boundary. Click pops at edit points are the audible signature of someone new to editing.
- **"How do I [thing I've never done]?"** Resist the urge to do it for them. Sit next to them, ask where they are, ask what they've tried. The goal is for them to learn the move, not for you to demonstrate competence.

### Gear setup baseline (every Wednesday)

Before students arrive, walk the room and verify at every station:
- Mac mini powered on, monitor working
- USB hub connected
- Audio interface plugged in, USB connected, power LED on
- Headphones plugged into the interface, in-line slider checked (it tends to drift down)
- Mic in stand, plugged in (XLR), phantom power off unless using a condenser
- MIDI keyboard plugged in (used in Module 4, but leave it set up consistently)

The interface mix knob (where present) should be at 60% direct / 40% USB by default. Reset it before each session — students will have moved it.

If anything is missing or broken, log it immediately in the lab gear tracker and use the spare. Don't try to teach with broken gear; it derails the session.

### The Audacity setup ritual

Every student opens Audacity for every Module 2 session. The same opening sequence applies:

1. Open Audacity (already in the dock on lab machines)
2. Set project sample rate to 44.1 kHz (bottom-left of window) — this is the Module 2 standard
3. Set project to record from the audio interface (top toolbar dropdown, should default correctly but verify)
4. Open last session's project file from `~/Documents/lastname/` (after the first session)

Demonstrate this once on Wed Wk 2 and reinforce it Mon Wk 3 and Wed Wk 3. By Wk 4, it should be automatic. If a student is fumbling with this in Wk 5, they've been disengaging — check in.

### Reading the room: when to slow down

Signs that you're moving too fast and need to pause:
- Multiple students asking the same clarifying question within five minutes
- Students staring at their screens without clicking
- A student who was engaged earlier has gone quiet and is on their phone
- The room has lost the "tap-tap-tap" of mouse clicks and gone silent

When this happens, the right move is almost never to plow through. Stop, ask "what's working / what's not?" Wait. Listen. Adjust. Five minutes of recalibration saves 20 minutes of confusion.

### Pacing across the module

The pacing pressure point in this module is **Wed Wk 3** — Project 1 begins. If students leave that session having opened the sample bank, listened to a few sounds, and made one experimental edit, they're on track. If they leave having only heard a lecture about Audacity and not touched anything creative, you're behind. Plan your Wed Wk 3 with that as the deliverable.

The other pacing risk is **Mon Wk 5** — last new content, students may be deep in Project 1 and treating it as optional. It isn't. The dynamics content lands in their final mix.

### When to escalate to Inés

- A student is significantly behind and looks like they may not finish Project 1
- Equipment issues you can't resolve in the moment
- Anything involving a student in apparent distress (academic, emotional, otherwise)
- Anything you're uncertain about, full stop. Better to ask.

---

## Session 1 — Mon Wk 2: Digital audio fundamentals

**100 min · Lecture-style · MB2525**

### Goal

Students leave with conceptual fluency on what digital audio actually is: sample rate, bit depth, file formats. They've heard real audio examples that make the numbers audible (sample rate degradation, bit depth degradation, the consequence of removing the anti-aliasing filter). They've also been introduced to the listening assignment and the historical context for Project 1.

### Pre-class checklist

- The reading for today, [`course/readings/module-02-week-02-digital-audio.html`](../course/readings/module-02-week-02-digital-audio.html), is the spine of the lecture. **Read it before class.** If you've internalized it, you can teach it conversationally; if not, you'll end up reading slides.
- Pull up the reading on the projector before students arrive. Have the audio comparison blocks ready to play (sample rate, bit depth, anti-alias filter on/off).
- Make sure speakers in MB2525 are working and at a reasonable volume. The audio examples need to be heard clearly by the room — earbuds won't do.
- The listening assignment ([`course/listening/module-02-listening.html`](../course/listening/module-02-listening.html)) is due Mon Wk 5. You'll introduce it at the end of class. Have it pulled up.

### What students walk in knowing

From Module 1 (Wk 1 Wed, six days ago):
- They've recorded a short audio file with a microphone and saved it
- They know `~/Documents/lastname/` and the NAS workflow
- They know the basic gear in the room (interface, mic, headphones)

What they do **not** know:
- Anything formal about digital audio
- Vocabulary like sample rate, bit depth, Nyquist, aliasing
- File formats (most know "MP3" exists; few have heard of WAV)
- Anything about musique concrète or Schaeffer/Henry

Treat this as zero-prior-knowledge. The reading does the heavy lifting; your job in class is to walk through it with them, play the audio examples loudly, and stop for questions.

### Block-by-block

#### Block 1 — Setup and welcome (5 min)

Open: "Welcome back. Today is the first real conceptual lecture of the course. We're going to learn what digital audio actually is. Some of this will be familiar from physics or general knowledge, some will be brand new. By the end you'll be able to explain to someone why CDs are 44.1 kHz instead of just any random number."

Have them open the reading on their machines so they can follow along and read the captions on the diagrams. The reading is also their study reference — they'll come back to it.

#### Block 2 — Sound, sampling, sample rate (40 min)

Walk through Sections 1-3 of the reading. Don't read it aloud verbatim — narrate around the diagrams and play the audio examples.

Key beats:
- **Sound is continuous, digital is discrete.** This is the central tension. Use the sine wave diagram in the reading. "We need to take a smooth, continuous wave and turn it into a list of numbers. How?"
- **Sampling.** Use the sampling diagram — the dots ON the wave. "We measure the value of the wave at evenly spaced moments in time."
- **Sample rate.** "How often do we measure? Forty-four thousand one hundred times per second on a CD. Why that specific number?"
- **Nyquist.** This is the conceptual peak of the section. The reading explains it with the math; in class, explain it as: "To reproduce a wave, you need at least two samples per cycle — one for the up, one for the down. So the highest frequency you can capture is half your sample rate. CDs target 22 kHz max because human hearing tops out around 20 kHz, and they wanted some headroom."
- **Play the sample rate audio comparison.** Source / 8k / 4k. After playing each, ask: "What did you hear go away?" Look for "the high frequencies" or "the cymbals" or "the sparkle." If a student says "it sounds muffled," that's correct vocabulary — feed it back.

Take questions before moving on. Common confusion: students conflate "sample rate" with "bit rate" (which is an MP3 thing they've heard of). Disambiguate: "bit rate is a property of compressed files; sample rate is a property of the audio itself."

#### Block 3 — Bit depth, aliasing, file formats (40 min)

Walk through Sections 4-6 of the reading.

Key beats:
- **Bit depth = how precisely we measure each sample.** Use the bit depth diagram (the staircase). "Sample rate is how often, bit depth is how precise."
- **Dynamic range follows from bit depth.** ~6 dB per bit. 16-bit = ~96 dB of usable range. The bar chart in Section 5 makes this visceral — point at the orchestra column and say "an orchestra at full volume to a whisper-quiet pianissimo is about 80 dB of range. 16-bit fits that. 4-bit doesn't."
- **Play the bit depth audio comparison.** Source / 8-bit / 4-bit. The 4-bit example goes silent in its tail because the decay falls below the noise floor — point this out.
- **Aliasing.** This is the trickiest concept in the reading. The wagon-wheel analogy in the reading is the clearest framing. "If you sample too slowly, high frequencies don't disappear cleanly — they show up as fake low frequencies." Play the aliasing audio comparison: source / 8k properly filtered / 8k unfiltered. The unfiltered version sounds "wrong" in a specific way, and that wrongness is aliasing.
- **File formats.** WAV (uncompressed, what we use), AIFF (similar, Mac native), MP3 (lossy compression, smaller files, throws information away), FLAC (lossless compression, smaller files but mathematically identical). For Module 2 we work in WAV at 44.1 kHz / 16-bit. That's the assignment standard; later modules will introduce 48 kHz / 32-bit float for Ableton.

#### Block 4 — Listening assignment + close (15 min)

Pull up the listening assignment ([`course/listening/module-02-listening.html`](../course/listening/module-02-listening.html)) on the projector. Walk through it briefly:

- Three pieces: Schaeffer (1948), Henry (1963), and one contemporary piece they choose
- Read the "Before you listen" history section *with them* — at least the first paragraph, to establish that these were tape compositions, not digital
- Show the YouTube link cards: clicking opens a new tab with the piece
- Show the four questions
- Show the submission card: Word or PDF, ~250-350 words, formatting, Chicago or MLA
- Due Mon Wk 5, about 3 weeks from now
- This connects directly to Project 1 — they'll be making something in this tradition

Close with a small bridge to Wednesday: "On Wednesday we'll start working in Audacity. Bring your headphones."

### Common questions

**"Why 44.1 specifically?"** Answer: rooted in early CD/video standards involving NTSC video frame rates. The reading covers it. Don't go deeper than the reading does — it's a curiosity, not a load-bearing concept.

**"Why would anyone use lower sample rates?"** Smaller files, less CPU, certain aesthetic uses (lo-fi). Module 4 will touch on intentional sample-rate manipulation as an effect.

**"Is 32-bit float just better?"** It's better for *working* (more headroom, no clipping), not necessarily for *delivering*. CDs and most distribution still use 16-bit. We'll use 32-bit float in Module 4's Ableton work because Ableton's mixer benefits from it.

**"What's the difference between 16-bit and 24-bit if both sound 'good enough' to me?"** 24-bit gives you more headroom for editing without losing resolution. For final delivery, 16-bit is usually fine. For working files, 24-bit is the professional standard.

### Pacing fallbacks

- **If running long:** Cut the file formats discussion to a 2-minute mention. The reading covers it; students can absorb on their own.
- **If running short:** Open up to discussion: "What surprised you in the reading? What's still confusing?" These conversations build community and surface confusions you can address.

### After class

- Verify all students have the reading open / accessible (it's on the public site, but check)
- Quick mental note: who looked engaged, who looked lost. If anyone seemed lost, plan to check in Wednesday.

---

## Session 2 — Wed Wk 2: Digital audio explorer + Audacity orientation

**100 min · Lab-style · MB2525**

### Goal

Two halves:

- **Part 1 (Digital Audio Explorer):** students hear *how complex sounds are built from sines*. The tool walks them from one sine, to summed sines, to the harmonic series, to timbre. By the end they should understand that "real sound is the sum of sines" is literal and physical, not a metaphor, and they should have hands-on intuition for fundamental, partial, and timbre.
- **Part 2 (Audacity orientation):** students open Audacity for the first time, set the project format to course standard (44.1 kHz / 16-bit), import a sample, make a basic selection-cut-fade, save the project, export a WAV, and complete the NAS round-trip. Leave with hands on the software and the workflow.

### Materials

- **Lab Part 1:** [`course/tools/module-02-week-02-digital-audio-explorer.html`](../course/tools/module-02-week-02-digital-audio-explorer.html)
- **Lab Part 2:** [`handouts/03-audacity-orientation.html`](../handouts/03-audacity-orientation.html)

### Pre-class checklist

- Walk the room: gear setup baseline (see Module-wide concerns)
- Verify Audacity opens cleanly on every machine (test on at least 3 stations); confirm project sample rate defaults to 44100 Hz, 16-bit format
- Confirm `orientation-sample.wav` is on the NAS at `shared/module-02/orientation/`. **If it's not there, the lab can't run.** This is a short field recording of a struck bell (~15 s), with sharp attack and long decay — see "Asset prep" below for what's expected.
- Open the explorer tool on the instructor station and confirm sound plays from the projector
- Open the orientation handout (Handout 03) on the instructor station and on each student station's desktop browser
- Confirm Handout 02 (Session Routines) is laminated and visible at every station

### Block 1 — Recap (10 min)

Quick verbal recap of Monday's reading. Ask 2–3 students to explain, in their own words: "What's sample rate?" "What's bit depth?" "Why 44.1 kHz?" Let them get it slightly wrong; correct gently. The retrieval matters more than precision.

Then bridge: "Today's lab has two halves. First we're going to take the *idea* of a sine wave from yesterday's reading and pull on it: how do we get from a sine — which sounds artificial — to the kind of sound a flute or a clarinet makes? After that, we'll open Audacity for the first time."

### Block 2 — Digital Audio Explorer (35 min)

Project the explorer on the room display. Walk students through it section by section, pausing for hands-on at each step. Pace: 8–10 minutes per section, mostly student exploration with brief framing.

**Section 1 (Sine maker, 5 min).** "This is what one sine sounds like." Demo: play, move the frequency slider through the range, then the amplitude slider. Then: "Move only the frequency. Pitch changes, loudness doesn't. Move only the amplitude. The opposite. These are independent dimensions even though they live in the same sound." Each student tries.

**Section 2 (Sine summer, 8 min).** Frame: "Real sounds aren't sines. So how do we get from sines to real sounds? The answer is: you add them up." Have each student turn up partial 1 only (verifies they're back to a sine), then partial 2 at a random freq. "What do you hear?" The answer should be: two pitches, or beating if they're close, or just chaos. Let them play. Make sure at least one student hears the beating phenomenon and ask them to describe it. Don't define beating formally yet — it'll come up again in Module 4.

**Section 3 (Harmonic series, 12 min).** This is the heart of the lab. Frame: "We just discovered that random sums of sines don't sound like notes. So why does a flute sound like one note even though it contains many sines? Watch what happens when the sines line up at integer ratios." Have everyone start from all amps at zero, fundamental at 220. Bring up partial 1 (the fundamental). Then partial 2. "What pitch are you hearing now?" Most will say "the same one, just richer." That's the right answer. Add 3, 4, 5, 6 one at a time. The pitch stays put, the timbre fattens. The conceptual punchline: *the ear fuses harmonically related partials into one perceived note*. This is the moment they should leave the section with.

**Section 4 (Timbre, 8 min).** "Same harmonic series, different amplitude balance, different sound." Demo the suggested experiments: silence the fundamental and notice the pitch can stay; silence the even partials and listen for the clarinet-like hollowness; etc. Then give 3 minutes for free exploration: "Can you make a sound that resembles an instrument you know?"

Walk the room throughout. Listen for genuine engagement vs. clicking-without-listening. The tool's value is in the *listening*, not in clicking sliders. If a pair is moving too fast, sit down: "What did you actually hear when you turned that one up?"

### Block 3 — Audacity orientation (45 min)

Switch to the Audacity handout (Handout 03). Have students close the explorer and open the handout in a browser. Walk through the seven steps on the projector with students following along on their machines. **Don't move on until everyone is at each step.** This is one of those sessions where pacing to the slowest student is the right thing.

The handout is detailed enough that students could in principle do it on their own. Your job in class is (a) catching the moments where someone misses a step and falls behind, (b) demonstrating each move on the projector so they have a model to mirror, (c) reinforcing the *workflow logic* (NAS-to-local at the start, work locally, local-to-NAS at the end) that the handout encodes.

Suggested pacing within Block 3:

- **Step 1 (NAS pull, 6 min)** — first contact with the NAS workflow as a real action, not just a card on the wall. Watch for students who try to open `orientation-sample.wav` directly from the NAS rather than copying it locally first.
- **Step 2 (Open Audacity, set format, 4 min)** — quick.
- **Step 3 (Interface tour, 5 min)** — point at the named regions on the projector. The annotated screenshot in the handout is a reference; students don't need to memorize it today.
- **Step 4 (Import + play, 5 min)** — should be quick. Watch for students who try double-clicking the WAV in Finder instead of using File → Import.
- **Step 5 (Selection, cut, fade, 12 min)** — the heart of Part 2. Demonstrate each move on the projector. Pause after the cut so they can play and *hear* the abrupt ending before doing the fade. The fade transforms the sound from "broken edit" to "deliberate edit" — that contrast is the lesson.
- **Step 6 (Save + export, 8 min)** — the project-vs-export distinction trips students up. Reinforce: "Save the project to keep working tomorrow. Export the WAV to have something you can submit or share."
- **Step 7 (NAS upload, 5 min)** — closes the loop on the workflow that opened the session.

### Block 4 — Wrap and preview (10 min)

Quick close: "On Monday we go deeper into editing — the full vocabulary, plus envelope. Then on Wednesday Project 1 begins. The Module 2 listening (Schaeffer + Henry) is due at the start of Mon Wk 5; start it this weekend if you can."

### Common confusions

- **The explorer's pitch experience.** Some students will *hear* the harmonic series fusing into one note before others. If a student says "I hear separate notes" when partials 1+2 are on, ask them to bring up partials 3 and 4 too and listen again — the fusion strengthens with more partials. If they still hear separate notes, that's fine; it's a perceptual skill that develops with listening practice.
- **Cursor vs. selection in Audacity.** Cursor is a single point in time; selection is a range. Many students try to "cut a section" with just the cursor placed. Demonstrate both, in contrast.
- **Project file vs. audio file.** `.aup3` is the working document; you can't open it without Audacity, and links to the source data must be intact. Audio files (WAV/MP3) are universal. The handout calls this out, but expect to repeat it in person.
- **NAS-direct editing.** Students will sometimes try to open `orientation-sample.wav` directly from the mounted NAS. Catch this early: always copy to local first.

### Pacing fallbacks

- **If running long in Part 1:** trim Section 4 (Timbre) free-exploration time. The first three sections carry the main pedagogical weight; Section 4 can be a 4-minute demo + brief student touch.
- **If running long in Part 2:** the most cuttable step is Step 7 (NAS upload). It can be done after class with a 30-second reminder ("Don't leave without uploading. The card on your station has the steps.") But better to keep it in if at all possible — first-day NAS upload is the workflow-formation moment.
- **If running short:** in Part 1 Section 4, give 5–7 minutes of timbre free-exploration ("Try to make a sound that's like a brass instrument, then a woodwind, then something inhuman"). In Part 2 Step 5, give them an extra try-this: "Now reverse the bell. What does the envelope look like?"

### Asset prep — orientation-sample.wav

The Audacity orientation handout assumes a specific sample on the NAS at `shared/module-02/orientation/orientation-sample.wav`:

- **Source:** a single struck bell, gong, glass, or similar percussive object with a long decay
- **Length:** 12–18 seconds
- **Format:** WAV, 44.1 kHz, 16-bit, mono or stereo
- **Pedagogical fit:** clear sharp attack near the start, almost no sustain, long gradual release. The bell is what students cut into and fade in Step 5; its envelope is what visually demonstrates the attack–release shape from the Wk 2 reading.

Inés to record or source. If unavailable, any single sound with a clear attack + long decay works (bowed string note that fades, struck rim, plucked piano string).

### Asset prep — Audacity screenshots for Handout 03

Handout 03 references five screenshots that need capturing on a lab Mac and saved to `assets/images/handouts/`. The handout's `alt` text describes what each screenshot should show:

| Filename | Content |
|---|---|
| `audacity-settings.png` | Audacity Audio Settings window with project sample rate 44100 Hz, default sample format 16-bit PCM |
| `audacity-interface-empty.png` | Empty Audacity main window with numbered annotations 1–9 identifying menu bar, transport, tools, level meters, host/device/rate, timeline, track area, selection toolbar |
| `audacity-imported.png` | Main window with `orientation-sample.wav` imported, showing the bell waveform (sharp attack + long decay) |
| `audacity-selection.png` | Same window with a region selected from mid-decay to end of file |
| `audacity-fade-out.png` | Same window after cut + fade-out, showing the new shorter ending tapering to zero |

The annotation numbers on `audacity-interface-empty.png` should be drawn on top of the screenshot in red or rust; the handout's annotation key reads them in order. Recommended approach: capture the raw screenshot, then annotate with a tool like Skitch or Preview's markup. Keep annotation numbers consistent with the handout's order.

Until the screenshots are captured, the figures render with their `alt` text visible in placeholder boxes — students can still follow the handout, but the boxes look unfinished. Capture before the first time the lab runs.

### After class

- Walk the room before locking up. Make sure all machines are logged out, headphone sliders down (default position for next session), interface mix knobs reset.
- Verify NAS uploads happened (spot-check 3-4 student folders for `lastname-orientation.aup3` and `lastname-orientation.wav`).
- Note any common confusions for the after-Module retrospective.

---

## Session 3 — Mon Wk 3: Editing concepts + envelope listening

**100 min · Lecture-style · MB2525**

### Goal

Students leave with the conceptual vocabulary for *editing* (cuts, fades, time placement, looping, reversing, time-stretch, pitch-shift) and for *envelope* (attack, sustain, release). The envelope vocabulary in particular will be load-bearing for the rest of the course — Module 4's synthesis section depends on it.

The reading for today is [`course/readings/module-02-week-03-editing-envelope.html`](../course/readings/module-02-week-03-editing-envelope.html). It includes 12 audio demos: three contrasting envelope shapes (sharp, sustained, evolving); one source transformed by four edits (truncate, reverse, fade-in); a hard-cut vs. crossfade comparison demonstrating click pops at edit boundaries; and a voice recording at three speeds (source, slow, fast) demonstrating the tape-style time-pitch coupling. Read it before class. The audio demos are central to how the concepts land, so listen on headphones if you've never gone through them.

### Pre-class checklist

- Read the Mon Wk 3 reading and listen to all 12 audio demos
- Pull up the listening assignment — students have had it since Monday but most won't have started; nudge them today
- Pull up Audacity on the instructor machine; you'll do a few short demos
- Have a few sample sounds queued — ideally with contrasting envelopes (a sharp percussion hit, a sustained string drone, a complex evolving sound). The reading's audio demos are good fallbacks if your sample bank doesn't have variety yet.

### Block-by-block

#### Block 1 — Recap and frame (10 min)

Quick recap of Wed Wk 2: students opened Audacity, made a basic edit, saved a project. Today we step back from the tool and talk about *what edits do to sound*.

Open: "We're going to spend today on two related ideas — *what an edit is*, and *what a sound's envelope is*. These are the two vocabularies you need to talk about Project 1."

#### Block 2 — Envelope (30 min)

Define envelope: "Every sound has a shape over time — how it starts, how it sustains, how it ends. We call that the envelope, and it's one of the things our ears use to identify what a sound is."

Three components:
- **Attack** — how a sound begins. Sharp (a snare drum hit) or gradual (a bowed violin note).
- **Sustain** — what happens during the sound. Steady (an organ note) or evolving (a vocal "ahhh" that wavers).
- **Release** — how the sound ends. Abrupt (a percussion clap, no tail) or gradual (a piano note decaying after the key is released).

(Some teachers use ADSR — Attack, Decay, Sustain, Release — distinguishing the initial peak from the steady-state. For Module 2 we keep it to three; Module 4 will introduce the four-stage version with synthesis.)

Open the reading on the projector and play the three contrasting envelope demos (sharp / sustained / evolving). After each, ask the class: "Describe the envelope. Sharp attack, long sustain, no release? Slow attack, long sustain, gradual release?"

**Then open the envelope explorer in the reading and demonstrate live.** This is the centerpiece of the block. The tool has three sliders (attack, sustain, release) and a play button; the source is a fixed sine tone, only the envelope changes. Drag the sliders to walk through:

- "Watch what happens when I make the attack tiny." Drag attack to its minimum, sustain to zero, release short. Press play. The result is percussive — sounds nothing like a sustained note even though the source is a sine.
- "Now I'll stretch the attack way out." Drag attack to ~1500 ms. Press play. Same source, but it swells in. Completely different character.
- "What if I take the sustain out entirely?" Drag sustain to zero, attack and release to medium. Press play. The peak of the envelope only exists for an instant.
- "Now a balanced shape — clear attack, clear body, clear ending." Drag to roughly 200/800/600. Press play.

The pedagogical point: the same source sound becomes radically different sounds based only on its envelope. This is what students will be doing to their source recordings in Project 1, even when they're not thinking about it explicitly.

Then play the listening assignment Schaeffer or Henry pieces (or a short excerpt) and ask: "What envelopes are you hearing? Are most of these sounds sharp or smooth at the attack?"

This vocabulary lets students *describe* what they want from a sound, which is the prerequisite to *finding* the right sound for a project.

#### Block 3 — Editing concepts (45 min)

The reading structures these as: six fairly intuitive moves, then a pause to introduce time-pitch coupling, then time-stretch / pitch-shift as the modern decoupled operations, then reverse last. Use that same arc on the projector.

**The six intuitive moves (15 min).** Walk through and demonstrate briefly in Audacity:

- **Cut.** Removes a selection; the timeline closes the gap.
- **Trim.** Removes everything *outside* a selection; keeps only the selected region.
- **Splice / arrange.** Cut a chunk and paste it elsewhere in the timeline. The fundamental musique concrète technique.
- **Fade in / fade out.** Smooth volume ramp at the boundary of an edit. Prevents clicks. Always use them, even just 5-10 ms worth.
- **Crossfade.** Where two pieces of audio overlap, one fading out as the other fades in. Smooth transitions between regions.
- **Loop.** Repeating a section. Either as a working aid (looping while listening) or a compositional tool (a tape-loop pattern).

These should feel obvious to students. The "you cut a thing, you put a thing next to another thing" intuition is fine — that's what the reading sets up. Don't overteach them.

**The pause: time-pitch coupling (15 min).** This is the conceptual hinge. Open the reading on the projector and show the three-sine SVG diagram (source / slow / fast). Talk through what's visible: same waveform, three speeds. The slowed version's cycles are wider; the sped-up version's cycles are narrower. That's why pitch changes — pitch is determined by how often the cycles repeat per second.

Then play the three audio demos in the reading (`tape-source.wav`, `tape-slow.wav`, `tape-fast.wav`). The audio is a voice recording, not a sine — the diagram uses a sine because cycles are visible at a glance, but the audio uses a voice because the perceptual coupling is more obvious on real material. Note the speed factors: the audio uses 0.75× and 1.33× rather than the 0.5× / 2× shown in the diagram. The principle is identical, but a 2× slow of the full recording would run over 11 seconds, which is too long for an A/B comparison; 1.33× keeps it under 8 seconds. Students will hear the same words at three speeds: the source, a slowed-down version (about 5 semitones lower, lower-pitched and noticeably stretched), and a sped-up version (about 5 semitones higher, brighter and faster). Ask the room: "What's different between the source and the slow version?" Get them to articulate both: it's longer *and* it's lower. Same for fast: shorter *and* higher. The point landing is that these aren't two separate effects; they're the same effect viewed two ways.

A brief historical note lands well here: "Schaeffer worked entirely in this world. Every tape recording until about 1990 worked this way. If you wanted longer, you went lower. If you wanted higher, you went shorter. There was no choice."

**Time-stretch and pitch-shift as the decoupling (10 min).** Now that students know what's *physically* coupled, the modern operations make sense:

- **Time-stretch.** Make a sound longer or shorter *without* changing its pitch. Software analyzes the recording and rebuilds it at the new duration. Demonstrate in Audacity: Effect → Change Tempo (this is Audacity's pitch-preserving time-stretch). Compare to Effect → Change Speed (which is Audacity's tape-style coupled change). The two effects are different operations that look superficially similar — students will mix them up. Be explicit: "Change Tempo keeps pitch. Change Speed changes both, like tape."
- **Pitch-shift.** Move a sound up or down in pitch *without* changing its duration. Effect → Change Pitch. Demo a few semitones up and down. Note that extreme settings produce artifacts — interesting in their own right, but worth knowing they exist.

**Reverse (5 min).** Save reverse for last. It's a different kind of operation: it's about *direction*, not duration or pitch. Effect → Reverse. Demonstrate: a piano note played forward sounds attacking; played backward, it sounds swelling. Connect back to envelope: "Remember from the envelope vocabulary — the attack is how a sound begins, the release is how it ends. Reverse swaps them."

Close Block 3: "Schaeffer didn't have software. He did all of this with razor blades and tape — except for time-stretch and pitch-shift, which he literally couldn't do because the physics were locked together. The principle of editing as a creative move is the same; the tools are radically different."

#### Block 4 — Envelope-listening exercise (10 min)

Quick group exercise. Play 3-4 sounds from the sample bank, one at a time. After each, students describe the envelope in writing — one line per sound. ("Sharp attack, no sustain, no release. Sound: a wood block.")

This is practice for the kind of careful listening that Project 1 demands.

#### Block 5 — Close + listening reminder (5 min)

Remind students: listening assignment due in 2 weeks. Recommend they start this week — three pieces is a real listening time investment.

Wednesday: editing techniques and Project 1 begins.

### Common confusions

- **Attack vs. transient.** They're related but not synonymous. The attack is the *time-shape* of how the sound starts; the transient is the *sharp acoustic event* that often defines the attack. For Module 2, "attack" is enough — distinguish later if it comes up.
- **Editing as cutting vs. arranging.** Some students think of editing as just removing bad parts (the recording-engineer connotation). For musique concrète and Project 1, editing is *also* arranging, repeating, layering, transforming. Reframe explicitly: "We're not just cleaning up; we're making."

### Pacing fallbacks

- **If running long:** Cut Block 4's exercise. The vocabulary is what matters; the practice will happen Wednesday.
- **If running short:** Add a deeper listening to a Henry or Schaeffer excerpt. Ask students to identify three distinct edit moves.

---

## Session 4 — Wed Wk 3: Editing techniques + Project 1 begins

**100 min · Lab-style · MB2525**

This is the pivot session of the module. By the end of class, students should have *started* Project 1: copied the sample bank locally, created a saved Audacity project, and placed at least three sounds in it. If they leave without that, they're behind.

### Goal

Two halves:

- **Editing techniques walkthrough (~60 min):** every technique from the Mon Wk 3 reading, mapped to its location in Audacity, with a hands-on exercise on a real Project 1 sample. Nine techniques in the reading's order: cut, trim, splice, fades, crossfade, loop, reverse, time-stretch, pitch-shift.
- **Project 1 begins (~30 min):** open the prompt, browse the bank, pick three sounds, place them in the saved project, save. Students leave with a real Project 1 starting point, not a blank screen.

### Materials

- **Lab handout:** [`handouts/04-editing-techniques.html`](../handouts/04-editing-techniques.html) — covers the full session including setup, all nine techniques with menu paths and exercises, the Project 1 starter, and the end-of-session NAS routine. The handout is the script; this TA-notes block is for pacing, common confusions, and judgment calls.
- **Project 1 prompt:** [`course/projects/project-01-musique-concrete.html`](../course/projects/project-01-musique-concrete.html) — open on the projector during the Project-1-begins block.
- **Sample bank** at NAS `shared/sample-banks/project1/` — must be ready by class start. See [`ta-notes/sample-bank-project-01.md`](sample-bank-project-01.md).

### Pre-class checklist

- Walk the room (gear baseline)
- **Verify the sample bank is ready and complete on the NAS** at `shared/sample-banks/project1/`. The handout assumes the canonical category folders (`attack-sharp`, `attack-soft`, `sustain-long`, `sustain-short`, `texture-continuous`, `voice-and-language`, `found-objects`, `natural-environment`, `mechanical-electronic`). If the bank is missing or has different folder names, **the handout's exercises won't work**. Confirm before class.
- Verify Audacity opens cleanly on every machine; verify project format defaults are 44.1 kHz / 16-bit
- Open the Project 1 prompt on the instructor station
- Have Handout 04 open in a browser at every student station's desktop

### Block-by-block

#### Block 1 — Setup, zoom, zero crossings (15 min)

Walk students through the handout's "Setup" and "Before the techniques" sections together on the projector. Three parts:

- NAS connect, then **copy the entire sample bank** (~40-80 sounds) from `shared/sample-banks/project1/` into the student's local `~/Documents/lastname/project-01/sources/`. The local copy is what they'll work from for the rest of the module. The first time this copy runs it'll take a minute or two depending on bank size.
- Open Audacity, save an empty project as `lastname-project01.aup3` in `~/Documents/lastname/project-01/`. This is *the* Project 1 file students will keep returning to.
- Walk through the zoom and zero-crossings prelude. Show the Cmd+E (zoom to selection) and Cmd+F (fit to width) pair on the projector. Then make a selection in a sample, press Z, and point out how the edges shift slightly to land on zero crossings. The handout has a "Try it" mini-exercise; students do it on their own machines once they've seen it on the projector. Total prelude time: about 5 min, included in this 15 min block.

Students who get behind here will fall behind on every technique exercise after, since each one assumes a working local copy of the bank and the zoom/zero-crossings habit. Don't move to Block 2 until everyone has the bank copied, the project saved, and has tried Z on a selection at least once.

#### Block 2 — The ten techniques (60 min)

This is the heart of the session. Each technique in the handout has the same shape: one-line recap, where to click in Audacity, hands-on exercise on a sample, "listen for" note. The handout is detailed enough that students could do this on their own; your job is (a) demonstrating each move on the projector so they have a model to mirror, (b) catching when someone's stuck on a UI gotcha (Trim hidden under Remove Special, Reverse hidden under Special, etc.), (c) keeping pace.

Suggested per-technique pacing (~6 min each on average, with the time/pitch trio sharing exercise momentum):

| # | Technique | Pace target | Note |
|---|---|---|---|
| 1 | Cut | 4 min | Fast; students did this in Wed Wk 2. Reinforce the Z-then-cut habit from Block 1 |
| 2 | Trim | 5 min | Flag the "hidden under Remove Special" gotcha explicitly |
| 3 | Splice | 8 min | The longest, since it's import-three-sounds + arrange |
| 4 | Fade in/out | 6 min | The first Effect-menu use; orient to how Effect submenus work |
| 5 | Crossfade | 7 min | Demoing on the projector helps; the drag-onto-same-track move trips students up |
| 6 | Loop | 6 min | Two paths (transport-loop vs. paste-in-succession) |
| 7 | Reverse | 4 min | Fast; the listening payoff is dramatic |
| 8 | Change Speed | 5 min | The coupled tape-physics version. Most intuitive starting point of the time/pitch trio |
| 9 | Time-stretch | 4 min | Direct A/B with the same sound from #8: same -50%, but pitch holds. Decoupling is audible |
| 10 | Pitch-shift | 4 min | Completes the trio. Together #8-#10 make the "couple vs. decouple" idea concrete |

Total: ~53 min. The remaining 7 min absorb individual help and inevitable "my Audacity opened in a weird state" moments.

**Things to call out as you go:**

- **The Effect menu's submenus.** First time students open Effect, they see categories (Fading, Pitch and Tempo, Special, etc.), not individual effects. Show this on the projector at technique 4 (Fades) so they understand the menu structure before they need it again.
- **The time/pitch trio (techniques 8-10).** This is the lab's biggest pedagogical payoff. The handout sequences them to make the coupling/decoupling concrete: Change Speed first (couples both, like tape), then Change Tempo (time only, pitch holds), then Change Pitch (pitch only, time holds). Encourage students to use the *same* source sound for all three and compare directly. The "wait, the pitch didn't drop?" moment when they hear technique 9 after technique 8 is the lesson landing.
- **Save habits.** Encourage students to keep their technique experiments in a separate scratch project, not in `lastname-project01.aup3`. The Project 1 file should be reserved for actual project work. The handout suggests this; reinforce it.

#### Block 3 — Project 1 begins (~30 min)

Pull up the Project 1 prompt on the projector. Walk through key sections (read constraints aloud, point at the rubric, confirm the Wed Wk 5 deadline). About 5 min of framing.

Then it's open work time. Students follow the handout's "Project 1 begins" section:

1. Open the prompt themselves and read it
2. Spend ~10 min browsing the bank's category folders, listening to sounds
3. Pick three sounds (the handout offers a heuristic: short percussive, long continuous, recognizable specific thing)
4. Open `lastname-project01.aup3`, import the three sounds (one per track), place them in time
5. Save

The bar for "I started Project 1" is clear: three sounds in their `.aup3`, saved. If a student has that by the end of class, they're on track. If not, they're behind and should be checked in with.

Walk the room. The most useful thing you can do is *ask questions*, not provide answers:

- "What sounds are catching your ear?"
- "What contrast do you want in the piece?"
- "Have you tried that backward?"

If a student is stuck on "I don't know what I want to make," that's normal. Suggest the handout's heuristic (short percussive + long continuous + specific thing) and let them pick from there. Don't let them sit frozen.

#### End of session — NAS upload (last 5 min)

Final 5 minutes: students follow the handout's end-of-session routine. Save the project (`Cmd+S`), copy `lastname-project01.aup3` (NOT the sources folder, which is already on NAS) to `students/lastname/project-01/` on the NAS, eject NAS, log out.

### Common confusions

- **"How do I know if my piece is any good?"** It's too early. Reframe: "Right now you're collecting material and trying things. You'll know it's working when something you made surprises you."
- **"I'm overwhelmed by the sample bank."** Genuine reaction. Suggest the handout's three-bucket heuristic. Browsing 6-8 sounds out of 40-80 is plenty for today.
- **"Do I have to use the bank?"** Yes. The constraint is part of the assignment.
- **"Can I record my own sounds?"** Not for Project 1 (that's Module 3). For Project 1, bank only.
- **Trim looks missing.** Hidden under Remove Special. Flag verbally when you reach technique 2.
- **Reverse looks missing.** Hidden under Effect → Special. Flag when you reach technique 7.
- **The sample bank is huge / scrolling Finder is slow.** Once it's copied locally, browsing is much faster than over the network. If a student is browsing the NAS share directly (because they skipped the copy step), they'll experience friction. Catch this and have them complete Block 1 properly.

### Pacing fallbacks

The session is tight. 100 min for a setup + zoom prelude + ten techniques + Project 1 starter + NAS upload runs slightly over on paper. Like Wed Wk 2, students who don't finish in class can finish technique exercises at home: the handout is self-contained and the bank is on their local machine. What MUST happen in class:

1. The bank must get copied locally (Block 1)
2. The zoom and zero-crossings habit must get a projector demo (Block 1's prelude). Without this, every cut they make for the next two weeks will produce click pops they don't know how to fix
3. Crossfade and the time/pitch trio (techniques 5 and 8-10) must be demonstrated on the projector (these are the trickiest moves; students who skip them in class often skip them entirely in their pieces)
4. Students must leave with `lastname-project01.aup3` containing three sounds, saved to NAS

If running long: skip the in-audio loop variant in technique 6 (the playback-loop demo is enough). Skip the +100 percent variant in technique 8 and the +7 semitone variant in technique 10 (the -50%/-12 demos are enough).

If running short (rare): give more time to free Project 1 sketching. More browsing time always helps.

### After class

- Verify NAS uploads. Every student should have `students/lastname/project-01/lastname-project01.aup3` on the NAS by end of class. Spot-check 3-4 student folders.
- Walk the room: gear reset, headphone sliders down, machines logged out
- Note any students whose project file shows zero or one tracks at the end of class. They didn't finish Project 1 setup; check in with them at Wed Wk 4.

---

## Session 5 — Wed Wk 4: Mixing tool Part 1 + Project 1 work

**100 min · Lab-style · MB2525**

(No Mon Wk 4 session — Labor Day. Students have had a full week to work on Project 1 since Wk 3 Wed.)

### Goal

Students learn the first half of mixing concepts — levels, EQ basics, stereo placement — via the mixing tool Part 1, then apply them to Project 1 in progress.

> **Note on the interactive tool:** the mixing tool Part 1 is not yet built. This plan describes what it should support; update once the tool exists.

### Pre-class checklist

- Walk the room
- Pull up the mixing tool Part 1 on the instructor station
- Take a quick mental inventory: who's where on Project 1? You should have a sense from last week and any work students did between sessions.

### Block-by-block

#### Block 1 — Quick check-in (10 min)

Open: "Show of hands — who's spent at least an hour on Project 1 since last Wednesday?" If most hands are up, great. If most aren't, name it: "You need to be working on this between sessions. Two more sessions before submission."

Quick survey: "What's the hardest thing about it so far?" Listen. Common answers: "I don't know what to make," "my edits sound choppy," "I don't know when to stop." All normal. Acknowledge.

#### Block 2 — Mixing concepts intro (15 min)

Frame mixing: "You've been making editing decisions. Mixing is a different category — it's about how all the elements fit together. Three concepts today: levels, EQ, and stereo placement. Each is something you balance across the elements of your piece."

- **Levels.** How loud is each element relative to others? Aim for peaks around -12 to -6 dBFS, never let anything clip. The "main" element of a moment should be louder than the supporting elements.
- **EQ.** Different sounds occupy different frequency ranges. If two sounds compete in the same range, neither sounds clear. EQ lets you sculpt frequency content — cutting unwanted parts, occasionally boosting wanted parts.
- **Stereo placement.** Stereo is wider than mono. Placing different elements at different points across the stereo field gives the piece space to breathe.

#### Block 3 — Mixing tool Part 1 (30 min)

Demonstrate the tool on the projector. Then students work in pairs with the tool for 20 minutes, with 3-4 prompts on the lab handout (TBD when tool is built).

The tool should let students adjust levels, EQ, and stereo placement on a small mix and hear the consequences in real time. The point is to make abstract concepts ("EQ shapes frequency content") into immediate audible experiences ("when I cut this 200 Hz from the bass, the kick comes through clearer").

#### Block 4 — Apply to Project 1 (40 min)

Students return to their Project 1 in progress and apply mixing concepts. For students who haven't gotten to a stage where mixing applies (still in pure-editing mode), this is also project work time.

Walk the room. Listen on their headphones to short excerpts — you can give specific feedback now that there's actual material. Common things to point out:
- "Your loudest moment is too loud relative to your quietest. Bring the loud ones down."
- "These two elements are fighting in the same frequency range. Try EQing one of them."
- "Everything is dead-center in the stereo field. Pan something."

#### Block 5 — Wrap (5 min)

Quick close. "Mon Wk 5 we add the last mixing concept — dynamics. Then Wed Wk 5 is your final work session and submission. Plan your work accordingly."

### Common confusions

- **"How do I add EQ in Audacity?"** Effect → Filter Curve EQ (or Graphic EQ). Demonstrate once; students will look up the rest.
- **"My piece is too quiet / too loud."** Levels question. Show them the gain controls and the master output. Aim for peaks at -6 dBFS, never clipping the master.
- **"It sounds different on these headphones than on my own."** Real and important. Headphone variation is one reason mixing is hard. Suggest A/B-ing on a second pair before final submission.

### Pacing fallbacks

- **If running long:** Cut Block 4 work time to 25 minutes. Students will have time on their own and Mon Wk 5.
- **If running short:** Sit with individual students whose Project 1 is on track and listen with them, giving feedback. Personal mentoring time is high-value when you have it.

---

## Session 6 — Mon Wk 5: Dynamics + mixing tool Part 2

**100 min · Lecture-style turning into lab · MB2525**

This is the last new content of the module. After today, Wed Wk 5 is the final work session and submission deadline.

> **Notes:** Listening assignment is **due today**, before class. Spot-check Canvas before class to know who submitted. The mixing tool Part 2 is not yet built; update this plan once it is.

### Goal

Students learn what dynamics processing is (compression, limiting), why and when to use it, and apply Part 2 of the mixing tool. By end of class, they should have a draft of Project 1 that's mixed (not just edited) and approaching final.

### Pre-class checklist

- Confirm listening assignment submissions on Canvas (note who's missing — you'll follow up)
- Pull up the mixing tool Part 2 on the instructor station
- Project 1 prompt visible on instructor machine for reference

### Block-by-block

#### Block 1 — Listening recap (15 min)

Most students will have listened. Some will have written. A discussion-style recap is high-value: it lets students hear each other's responses and sharpens everyone's listening.

Pick 2-3 questions from the listening assignment to discuss as a group:
- "What technique stood out to you in Schaeffer or Henry?"
- "How does a piece made entirely from edits cohere as music?"
- "What did you choose for piece 3, and why?"

Don't grade in the moment — just listen, ask follow-ups, let students hear each other.

#### Block 2 — Dynamics concepts (25 min)

Define:
- **Dynamic range** — the difference between the quietest and loudest parts of a piece. A piece with wide dynamic range has subtle details and big peaks; a piece with narrow dynamic range is roughly the same loudness throughout.
- **Compression** — a tool that reduces dynamic range by attenuating loud parts (or, equivalently, raising quiet parts). Used to "even out" a mix or to add perceived loudness.
- **Limiting** — extreme compression at the loudest peaks. Used to set a maximum ceiling and prevent clipping while pushing overall loudness up.

Demonstrate in Audacity: Effect → Compressor. Apply to a sound that has wide dynamics. Listen before and after.

The pedagogical message: dynamics processing is *powerful and overused*. A little goes a long way. The goal is balance, not maximum loudness. The "loudness wars" of pop music are a cautionary tale, not an aspiration.

#### Block 3 — Mixing tool Part 2 (25 min)

Demo the tool, then students work in pairs for 15 minutes with prompts (TBD).

#### Block 4 — Project 1 work (30 min)

Students apply dynamics (and any earlier mixing concepts) to their pieces. Walk the room.

This is the last session before submission. Anyone whose piece isn't substantially complete needs to make a plan. Sit with them: "What's the gap? What do you need to do tonight, tomorrow, and during Wednesday's work session?"

#### Block 5 — Submission logistics (5 min)

Wed Wk 5 is the final work session and submission deadline. Walk through what to expect:
- Class is a final work session — no new content, just time to finish
- Files due to NAS by **end of class**, not start
- Two locations: their private working folder (`lastname/project-01/`) and the class listening folder (`/music/shared/mus-381-fall-2026/project-01-pieces/`). Both must have the final WAV.
- A short peer-listening response is due Mon Wk 6 (about classmates' pieces in the listening folder), separate assignment

Mention the rubric one more time — five dimensions, students should self-assess against it as they finish their work.

The shift from "presentations" to "submission + asynchronous listening" is intentional: the math doesn't work for 25 students at 3-5 minutes each, and asynchronous listening gives students more thoughtful encounters with each other's pieces. Don't apologize for the change; frame it as the design.

### Common confusions

- **"My piece sounds quieter than [other student's]."** Probably a levels issue. Show them how to use a limiter to push overall level without clipping.
- **"Should I use compression?"** Mostly: less than you think. If it sounds good without, leave it. If a sound has wide dynamic range that's getting in the way of the mix, light compression can help.
- **"Am I done?"** Open question, ask them. "Listen to the whole thing front-to-back without making changes. Is anything still bothering you?" If yes, work on that. If no, you're done.

### Pacing fallbacks

- **If running long:** Cut Block 4 work time. Students will have until Wednesday.
- **If running short:** Listen to a few student pieces in progress on speakers (with permission). Live feedback. This is risky but high-value when it works — only do it if students are comfortable.

### After class

- Note who submitted the listening assignment, who's late, who's absent. Follow up before Wednesday.

---

## Session 7 — Wed Wk 5: Project 1 final work session + submission

**100 min · Lab-style · MB2525**

This is the closing session of Module 2. There is no live presentation. Class time is dedicated to finishing pieces and uploading them to NAS by end of class. Listening to each other's pieces happens asynchronously in the days after, with a short peer-listening response due Mon Wk 6.

Why no presentations? Math: 25 students × 3-5 minutes each is longer than class time, and asynchronous listening gives students more careful, repeatable encounters with each other's work. The trade-off is the live "press play" moment, which some pedagogies value highly. We'll partly recover the cohort feeling on Mon Wk 6 with a brief discussion of what students heard.

### Goal

Every student finishes Project 1 and uploads to both NAS folders by end of class. The class listening folder fills up. Students leave with a piece in the world.

### Pre-class checklist

- **Verify the class listening folder exists and is writable by students.** Path: `/music/shared/mus-381-fall-2026/project-01-pieces/`. Permissions: students can write (drop their final WAV in), but cannot delete or modify others' files. Test this before class — drop a placeholder file in, then have one student try to add one and try to modify someone else's. If permissions aren't right, escalate to IT before students start uploading.
- **Spot-check working folders** for 5-6 students. They should have at least a `lastname-project01-vN.aup3` project file by now, and ideally an in-progress export. If a student's working folder is empty or has only one early version, flag them to check in with first thing.
- Walk the room (gear baseline).
- Have the project prompt ([`course/projects/project-01-musique-concrete.html`](../course/projects/project-01-musique-concrete.html)) open on the instructor machine. Specifically the Submission section.

### Block-by-block

#### Block 1 — Open and frame (5 min)

Open: "Today is your final work session for Project 1. By end of class, your final WAV is uploaded to two places. After today, you'll listen to each other's pieces in the class listening folder, and a short response is due Monday."

Walk through the submission card from the prompt on the projector. Be explicit about both folders:
1. Your private working folder: `lastname/project-01/lastname-project01.wav`
2. The class listening folder: `/music/shared/mus-381-fall-2026/project-01-pieces/lastname-project01.wav`

"Drag a copy of your final file to the class folder. Don't move it — copy. Your working folder still gets a copy too."

Mention the peer-listening response due Mon Wk 6. They've gotten an assignment ahead of time so they can plan to listen during the week.

#### Block 2 — Final work time (80 min)

Students work. Walk the room. This is the most one-on-one time you'll have with the cohort all module — use it.

Triage what students need:

- **Students nearly done:** check their export. WAV at 44.1/16-bit? Right filename? Right length (90 seconds to 2 minutes)? Listen to the last 30 seconds with them — endings often reveal whether the piece is actually finished. If yes, walk them through the upload to the class folder.
- **Students mid-mix:** sit with them, listen for 30-60 seconds on their headphones, give one specific suggestion. Don't try to fix everything; pick the highest-leverage thing.
- **Students still editing:** check whether they're going to make the deadline. If their piece is 30 seconds and they have an hour left, that's a real problem — talk through what's achievable in the time. It's better to submit a 90-second piece they're proud of than a 2-minute piece that runs out of steam.
- **Students who are stuck or panicking:** sit. Listen. Ask what's hard. Sometimes the unblock is small ("I don't know how to fade out the end") and sometimes it's bigger ("I hate everything I made"). Either way, the response is calm presence and small concrete next steps.

About 30 minutes before the end of class, give a verbal time check: "30 minutes left. If you haven't started exporting yet, start now."

About 10 minutes before the end: "10 minutes. Final export, name check, upload to both folders."

About 2 minutes before: "Make sure your file is in both folders before you leave. If you're stuck on upload, flag me now."

#### Block 3 — Confirm uploads + bridge to Module 3 (15 min)

Walk the room while students are wrapping up. Verify visually that files are landing in the class folder — refresh the folder on the instructor machine and watch files appear.

Quick close to the room:

"You did something hard. You took a constraint and a folder of sounds and made a piece. The first piece is the hardest. Listen to each other's work this week — Monday we'll talk briefly about what you heard, and your peer-listening response is due then.

Module 3 starts Monday. We move from manipulating someone else's sounds to recording your own. Bring curiosity."

### Common situations

**A student's piece isn't done.** Their submission is what's in the class folder at end of class. If they upload a 60-second draft, that's their submission. The late policy in the syllabus applies if they upload after class ends. Don't allow informal extensions during class — be consistent. Real extensions go through the instructor in advance.

**A student didn't upload to the class folder, only their working folder.** Catch this before they leave. The class folder is part of the submission — the rubric explicitly mentions both folders. Walk them through the copy.

**A student is absent.** Their submission is whatever's in the class folder by end of class. If nothing's there by end of class, the late policy in the syllabus applies. Note absences for instructor follow-up.

**A piece has technical issues (silent, distorted, wrong format).** Help diagnose for ~5 minutes. Common causes: exported as MP3 instead of WAV (fix in Audacity export settings), exported at wrong sample rate (export again), file is silent because tracks were muted before export (unmute, re-export). If you can't fix in 5 minutes, the student submits what they have and follows up with the instructor.

**The class listening folder doesn't accept uploads (permissions issue).** Students upload only to their private working folder. After class, you (or the instructor) batch-copy files into the class folder. Document the issue for IT. Don't let students stand there waiting.

### Grading

Use the rubric in [`course/projects/project-01-musique-concrete.html`](../course/projects/project-01-musique-concrete.html). Five dimensions, 20 points each. Grade after class — listen to each piece on good headphones in a quiet space, not in the chaos of submission day.

Late submissions are handled per the syllabus's late policy. Pieces not in the class listening folder by end of class on Wed Wk 5 are late.

### After class

- Confirm every student has a file in the class listening folder. Note the missing ones.
- For students whose files are only in their private working folder, message them — they need to add to the class folder for the submission to be complete (or you can copy on their behalf, instructor's call).
- Begin grading. Plan to return scores within a week.
- The class listening folder is now populated. Listening happens between today and Mon Wk 6, when the peer-listening response is due.

---

## End-of-module assessment

### What success looks like

Students at the end of Module 2 should be able to:

1. Explain digital audio fundamentals at a conversational level (sample rate, bit depth, file formats)
2. Describe a sound's envelope and use the vocabulary fluently
3. Navigate Audacity confidently — open, transport, select, edit, export
4. Apply core editing techniques (cuts, fades, splicing, reverse, time-stretch, pitch-shift)
5. Make basic mixing decisions (levels, EQ, stereo placement, dynamics)
6. Produce a 2-minute piece from sourced material that demonstrates the above
7. Discuss their work and others' in the historical and aesthetic context of musique concrète

### Across-the-cohort signs of trouble

If many students show the same pattern, it points back to the module rather than the student:

- **Pieces are 2 minutes of one texture with no change** → editing concepts (Mon Wk 3) didn't land. Add more class time analyzing structure in Module 3.
- **Pieces clip or are wildly uneven in level** → mixing levels (Wed Wk 4) didn't land. Reinforce in Module 3 recording sessions.
- **Pieces have audible click pops at edit boundaries** → fade habit (Wed Wk 3) didn't stick. Make fades part of every Module 3 demo.
- **Students can't describe their own pieces** → vocabulary (envelope, edit techniques) didn't transfer. Add description exercises to Module 3 listening.

### Forward promises to deliver in later modules

Module 02 readings make several "we'll come back to this" promises. Track them so they don't go stale:

- **Mon Wk 2 reading, section 5 (SNR / dynamic range):** "That principle (record with headroom, commit later) is one of the most important practices in audio. We'll return to it in Module 3." — Module 3 covers recording, so the mic-gain / input-level discussion is the place to deliver this. Make sure recording-with-margin shows up explicitly in the Module 3 recording session.
- **Mon Wk 2 reading, section 7 (warning callout):** points students forward to "the tape-physics situation we'll see in Week 3." — delivered by Mon Wk 3 reading's time-pitch coupling section. (Already in place.)
- **Mon Wk 3 reading (synthesis vocab note + Reverse vocab):** "Module 4 will introduce ADSR when we get into synthesis with Ableton." — Module 4 spec needs to introduce ADSR explicitly when synthesis comes online.
- **Mon Wk 3 reading (Loop entry):** "Looping is far more central in DAWs built around it; we'll come back to it in Module 4 with Ableton." — Module 4 needs to handle looping as a first-class concept once we move into Ableton.

When drafting Module 3 and Module 4 specs, scan this list and make sure each promise is covered. If a promise stops being relevant, edit the original reading rather than leave a dangling pointer.

### What gets logged

After Module 2 ends, write a short retrospective (1 page, in this file or a separate retrospective doc) covering:
- What went well
- What didn't
- What you'd change for next year
- Pacing notes — where time was tight, where time was loose
- Student questions that surprised you

This becomes the basis for revising both the module plan and these TA notes for the next time the course runs.
