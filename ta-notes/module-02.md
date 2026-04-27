# TA Notes — Module 2 (Weeks 2–5, Aug 24 – Sep 16)

This module is the foundation of the course. Students learn what digital audio is, how to manipulate it, and how to shape a balanced mix — and they make their first piece. By the end of Wk 5 they should be able to take a folder of source sounds and produce a deliberately edited, mixed, 2-minute piece. That is not a small jump from Day 1.

The module spans seven sessions. They are not interchangeable. The Mondays are lecture-style (concept introduction, listening, discussion); the Wednesdays are lab-style (hands-on, tools, project work). Students need both rhythms — the Monday sessions give them vocabulary and ear training, the Wednesday sessions give them craft. If you find yourself drifting toward the lab pattern on a Monday, pull back: students who only do the lab work without the conceptual frame produce technically functional but creatively shallow pieces.

Project 1 launches Wed Wk 3 and is presented Wed Wk 5. Two and a half weeks. The clock is tight on purpose — students who have a month tend to use the first three weeks avoiding the work.

This file is the operational runbook for all seven sessions. Module spec (the "what") is in [`course/modules/module-02.md`](../course/modules/module-02.md); this file is the "how."

---

## Contents

- [Module-wide concerns](#module-wide-concerns)
- [Session 1 — Mon Wk 2 (Aug 24): Digital audio fundamentals](#session-1--mon-wk-2-aug-24-digital-audio-fundamentals)
- [Session 2 — Wed Wk 2 (Aug 26): Digital audio explorer + Audacity orientation](#session-2--wed-wk-2-aug-26-digital-audio-explorer--audacity-orientation)
- [Session 3 — Mon Wk 3 (Aug 31): Editing concepts + envelope listening](#session-3--mon-wk-3-aug-31-editing-concepts--envelope-listening)
- [Session 4 — Wed Wk 3 (Sep 2): Editing techniques + Project 1 begins](#session-4--wed-wk-3-sep-2-editing-techniques--project-1-begins)
- [Session 5 — Wed Wk 4 (Sep 9): Mixing tool Part 1 + Project 1 work](#session-5--wed-wk-4-sep-9-mixing-tool-part-1--project-1-work)
- [Session 6 — Mon Wk 5 (Sep 14): Dynamics + mixing tool Part 2](#session-6--mon-wk-5-sep-14-dynamics--mixing-tool-part-2)
- [Session 7 — Wed Wk 5 (Sep 16): Project 1 presentations](#session-7--wed-wk-5-sep-16-project-1-presentations)
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

## Session 1 — Mon Wk 2 (Aug 24): Digital audio fundamentals

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
- Due Mon Wk 5 (Sep 14), about 3 weeks from now
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

## Session 2 — Wed Wk 2 (Aug 26): Digital audio explorer + Audacity orientation

**100 min · Lab-style · MB2525**

### Goal

Students hear the conceptual material from Monday made tactile via the digital audio explorer tool, then orient to Audacity: open, navigate, basic transport, basic selection, save a project. Leave with hands on the software and a feeling of "I can move around in this."

> **Note on the interactive tool:** the digital audio explorer tool is not yet built. This block-by-block plan describes what it should support. Update this section once the tool exists, with specific things to point at within it.

### Pre-class checklist

- Walk the room: gear setup baseline (see Module-wide concerns)
- Verify Audacity opens cleanly on every machine (test on at least 3 stations)
- Pull up the digital audio explorer tool on the instructor station
- Have the lab handout for today open and ready (TBD: lab handout file)

### Block 1 — Recap and tool intro (15 min)

Quick verbal recap of Monday's concepts. Ask 2-3 students to explain in their own words: "What's sample rate?" "What's bit depth?" Let them get it slightly wrong; correct gently. The retrieval practice matters more than precision.

Introduce the digital audio explorer: "This is a small interactive tool that lets you change sample rate and bit depth on a sound and immediately hear what happens. It's the audio examples from Monday's reading, but you control them."

Demo the tool on the projector for 5-7 minutes. Show the controls. Play one or two examples.

### Block 2 — Tool exploration (30 min)

Students work in pairs (one Mac mini per pair). Each pair has 25 minutes to explore the tool and answer 3-4 simple prompts on the lab handout (TBD when tool is built — example prompts: "What sample rate makes the high hat disappear? What bit depth makes the quiet decay disappear?").

Walk the room. Listen for genuine engagement vs. clicking-through-without-listening. The tool's value is in the *listening*, not in clicking buttons. If a pair is moving too fast, sit down with them: "What did you actually hear when you switched?"

### Block 3 — Audacity orientation (45 min)

Time to hands-on Audacity. Have students close the tool and open Audacity.

Walk through the following on the projector, with students following along on their machines. Don't move on until everyone is at each step.

1. **Window layout.** Tracks panel on the left, transport at the top, time ruler. Audacity is intentionally simple visually.
2. **Project sample rate.** Bottom-left corner. Set to 44.1 kHz. "This is our Module 2 standard."
3. **Importing audio.** File → Import → Audio. Have everyone import a sound from `/music/shared/sample-banks/project1/` (the bank should be ready by today). One sound. Any sound.
4. **Transport: play, stop, loop.** Spacebar plays from the cursor. Shift-spacebar plays in a loop. Practice: "Loop the first second of your sound. Now loop the last second."
5. **Selection with click and drag.** Click at one point, drag to another. The selection highlights. "Whatever's selected is what gets affected by the next thing you do."
6. **Selection refinement.** Use the time ruler. Hold Shift and click to extend a selection. Press Z to "snap to zero crossings" — this prevents click-pops at edit boundaries (introduce the concept; we'll use it more on Mon Wk 3).
7. **Cut, copy, paste.** Standard keyboard shortcuts work. Cut a 2-second selection out of your sound, paste it back in at a different time location. Listen. "What just happened?"
8. **Saving the project.** File → Save Project. Save as `~/Documents/lastname/audacity-orientation.aup3`. Discuss the difference between saving a project (`.aup3`, editable) and exporting audio (a WAV/MP3 file, the finished product).
9. **Exiting cleanly.** Close Audacity. Upload the project file to NAS following the Session Routines card.

### Block 4 — Wrap and preview (10 min)

Quick close: "Next Monday we go deeper into editing. Wednesday after that, you start Project 1." Mention that the listening assignment is also due Mon Wk 5.

### Common confusions

- **Cursor vs. selection.** Cursor is a single point in time; selection is a range. Many students try to "cut a section" with just the cursor placed. Demonstrate both, in contrast.
- **Project file vs. audio file.** `.aup3` is the working document; you can't open it on someone else's computer without the linked data. Audio files (WAV/MP3) are the universal format. Reinforce: "Save the project to keep working; export to share."
- **Where the file went.** If a student saved to the wrong location, it's still there — show them how to find it. This usually means they hit Save without paying attention to the location field.

### Pacing fallbacks

- **If running long:** Cut Block 4 to 5 minutes; the close can be brief. Don't cut the saving/exiting step in Block 3 — students need that habit established.
- **If running short:** In Block 3, give them a small free-explore at the end: "Spend 5 minutes trying anything you want with this sound. Cut it up. Reverse it. Slow it down. We'll share what you found."

### After class

- Walk the room before locking up. Make sure all machines are logged out, headphone sliders down (default position for next session), interface mix knobs reset.
- Verify NAS uploads happened (spot-check 3-4 student folders).

---

## Session 3 — Mon Wk 3 (Aug 31): Editing concepts + envelope listening

**100 min · Lecture-style · MB2525**

### Goal

Students leave with the conceptual vocabulary for *editing* (cuts, fades, time placement, looping, reversing, time-stretch, pitch-shift) and for *envelope* (attack, sustain, release). The envelope vocabulary in particular will be load-bearing for the rest of the course — Module 4's synthesis section depends on it.

> **Note on the reading:** the Mon Wk 3 reading on editing concepts and envelope is not yet written. This plan describes what it should cover and how to teach with it; update once the reading exists.

### Pre-class checklist

- Read the Mon Wk 3 reading (when it exists)
- Pull up the listening assignment — students have had it since Monday but most won't have started; nudge them today
- Pull up Audacity on the instructor machine; you'll do a few short demos
- Have a few sample sounds queued — ideally with contrasting envelopes (a sharp percussion hit, a sustained string drone, a complex evolving sound)

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

Demo: play three contrasting sounds from the sample bank. After each, ask the class: "Describe the envelope. Sharp attack, long sustain, no release? Slow attack, long sustain, gradual release?"

Then play the listening assignment Schaeffer or Henry pieces (or a short excerpt) and ask: "What envelopes are you hearing? Are most of these sounds sharp or smooth at the attack?"

This vocabulary lets students *describe* what they want from a sound, which is the prerequisite to *finding* the right sound for a project.

#### Block 3 — Editing concepts (45 min)

Walk through the vocabulary of editing. For each, demonstrate briefly in Audacity on the projector.

- **Cut.** Removes a selection; the timeline closes the gap.
- **Trim.** Removes everything *outside* a selection; keeps only the selected region.
- **Splice / arrange.** Cut a chunk and paste it elsewhere in the timeline. The fundamental musique concrète technique.
- **Fade in / fade out.** Smooth volume ramp at the boundary of an edit. Prevents clicks. Always use them, even just 5-10 ms worth.
- **Crossfade.** Where two pieces of audio overlap, one fading out as the other fades in. Smooth transitions between regions.
- **Loop.** Repeating a section. Either as a working aid (looping while listening) or a compositional tool (a tape-loop pattern).
- **Reverse.** Flips a section in time. The musique concrète tradition leaned hard on this. Demonstrate: a piano note played forward sounds attacking; played backward, it sounds swelling.
- **Time-stretch.** Make a sound longer or shorter without changing its pitch (or, in older techniques, with the pitch changing as a side effect).
- **Pitch-shift.** Move a sound up or down in pitch without changing its duration (or, again, with duration shifting as a side effect).

Connect this back to the listening: "Schaeffer didn't have software. He did all of this with razor blades and tape. The principle of *editing as a creative move* is the same; the tools are radically different."

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

## Session 4 — Wed Wk 3 (Sep 2): Editing techniques + Project 1 begins

**100 min · Lab-style · MB2525**

This is the pivot session of the module. By the end of class, students should have *started* Project 1: opened the sample bank, listened to enough sounds to pick a few, and made one experimental edit. If they leave without that, they're behind.

### Goal

(1) Students learn hands-on the editing techniques covered conceptually Monday: cuts, fades, splicing, time-stretch, pitch-shift, reversing. (2) Students officially begin Project 1.

### Pre-class checklist

- Walk the room (gear baseline)
- Verify the sample bank is mounted and accessible from every station: `/music/shared/sample-banks/project1/`
- Verify Audacity opens cleanly on every machine
- Pull up the Project 1 prompt ([`course/projects/project-01-musique-concrete.html`](../course/projects/project-01-musique-concrete.html)) on the instructor station
- Have the lab handout for today open (TBD)

### Block-by-block

#### Block 1 — Walkthrough of editing techniques (35 min)

Hands-on, follow-along. Each student loads one sound from the sample bank and tries each technique in turn on the projector's instruction. Don't rush.

- **Cut and rearrange.** Cut a one-second chunk. Paste it somewhere else in the timeline. Listen to the result. *Required habit:* before pasting, check where the cursor is. Pasting at the wrong location is the #1 frustration source.
- **Fades.** Effect → Fade In / Fade Out. Or use the envelope tool (small triangle handles at edit boundaries). Apply a 50ms fade at every edit boundary you make. Listen to a clip with and without fades — point out the click.
- **Crossfade.** Effect → Crossfade Tracks (requires two tracks). This is more advanced; demonstrate but don't require mastery today.
- **Reverse.** Effect → Reverse. Reverse a sound. Listen. "What's different? Which envelope changed?" (The release becomes the attack.)
- **Time-stretch.** Effect → Change Tempo (preserves pitch) or Effect → Change Speed (changes pitch with tempo). Try both. Discuss why you'd want one vs. the other.
- **Pitch-shift.** Effect → Change Pitch. Try shifting up an octave, down an octave. Note that extreme shifts produce artifacts.

Demonstrate the **save-version habit** at this point: "Save your project as `editing-practice-v1.aup3`. Now do something destructive — apply a heavy effect. Save as `-v2.aup3`. You can always go back to v1." This habit will save students multiple times during Project 1.

#### Block 2 — Project 1 launch (20 min)

Pull up the Project 1 prompt on the projector. Walk through it section by section:

- **Read the prompt aloud.** Yes, all of it. They'll skim if you don't.
- **Constraints.** 2 minutes max (90 seconds min). Sample bank only. WAV 44.1/16-bit. Filename `lastname-project01.wav`.
- **What demonstrating skills means.** Go through the five bullets. These are the rubric items; students should hear them now and remember them.
- **Process expectations.** Start early. Save versions. Listen on different headphones. Take breaks.
- **Presentation:** Wed Sep 16, two weeks from today. Each student plays their piece + one sentence intro.
- **Rubric.** Five dimensions, 20 points each, 100 total. Late penalty: 10 points/day.

End with: "You'll start working on it today. The rest of class is your time."

#### Block 3 — Open work time (40 min)

Students start Project 1. The minimum threshold for "I started" is: opened the sample bank, auditioned at least 5 sounds with intention, picked at least 2-3 to save into their project folder, made at least one experimental edit.

Walk the room. The most useful thing you can do is *ask questions*, not provide answers:
- "What sounds are catching your ear?"
- "What contrast do you want in the piece?"
- "Have you tried that backward?"

If a student is stuck on "I don't know what I want to make," that's normal. Suggest they pick one sound that interests them and play with it for 10 minutes — the work clarifies as they make it. Don't let them sit frozen; small movement beats no movement.

#### Block 4 — Wrap (5 min)

Quick close: "Save your work, upload to NAS, log out. Next Wednesday we add mixing concepts. Continue working between now and then — at least one more session, even just an hour at home if you can install Audacity."

Mention that Audacity is free and they can install it on a personal computer if they want; the working session model expects them to use lab time, but extra time on a personal machine is fine and encouraged.

### Common confusions

- **"How do I know if my piece is any good?"** It's too early — they're an hour in. Reframe: "Right now you're collecting material and trying things. You'll know it's working when something you made surprises you."
- **"I'm overwhelmed by the sample bank."** Genuine reaction; the bank has 40-80 sounds. Suggest: pick 3 sounds you find interesting, ignore the rest for now. You can come back.
- **"Do I have to use the bank?"** Yes. The constraint is part of the assignment — it forces creative work with given material rather than open-ended sound-collection.
- **"Can I record my own sounds?"** Not for Project 1 (that's Module 3). For Project 1, sample bank only.

### Pacing fallbacks

- **If running long:** Cut Block 1 to the essential moves (cut, fade, reverse). Time-stretch and pitch-shift can be discovered during work time.
- **If running short:** Pull up a sample piece (one of the Schaeffer or Henry pieces) and analyze a 30-second segment together: "What edits do you hear? What techniques?"

### After class

- Verify NAS uploads (every student should have at least an `editing-practice-vN.aup3` and the start of a `project-01/` folder)
- Walk the room: gear reset, headphone sliders down, machines logged out
- Note any students who didn't engage — plan to check in next session

---

## Session 5 — Wed Wk 4 (Sep 9): Mixing tool Part 1 + Project 1 work

**100 min · Lab-style · MB2525**

(No Mon Wk 4 session — Labor Day, Sep 7. Students have had a full week to work on Project 1 since Wk 3 Wed.)

### Goal

Students learn the first half of mixing concepts — levels, EQ basics, stereo placement — via the mixing tool Part 1, then apply them to Project 1 in progress.

> **Note on the interactive tool:** the mixing tool Part 1 is not yet built. This plan describes what it should support; update once the tool exists.

### Pre-class checklist

- Walk the room
- Pull up the mixing tool Part 1 on the instructor station
- Take a quick mental inventory: who's where on Project 1? You should have a sense from last week and any work students did between sessions.

### Block-by-block

#### Block 1 — Quick check-in (10 min)

Open: "Show of hands — who's spent at least an hour on Project 1 since last Wednesday?" If most hands are up, great. If most aren't, name it: "You need to be working on this between sessions. Two more sessions before presentations."

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

Quick close. "Mon Wk 5 we add the last mixing concept — dynamics. Then Wed Wk 5 is presentations. Plan your work accordingly."

### Common confusions

- **"How do I add EQ in Audacity?"** Effect → Filter Curve EQ (or Graphic EQ). Demonstrate once; students will look up the rest.
- **"My piece is too quiet / too loud."** Levels question. Show them the gain controls and the master output. Aim for peaks at -6 dBFS, never clipping the master.
- **"It sounds different on these headphones than on my own."** Real and important. Headphone variation is one reason mixing is hard. Suggest A/B-ing on a second pair before final submission.

### Pacing fallbacks

- **If running long:** Cut Block 4 work time to 25 minutes. Students will have time on their own and Mon Wk 5.
- **If running short:** Sit with individual students whose Project 1 is on track and listen with them, giving feedback. Personal mentoring time is high-value when you have it.

---

## Session 6 — Mon Wk 5 (Sep 14): Dynamics + mixing tool Part 2

**100 min · Lecture-style turning into lab · MB2525**

This is the last new content of the module. After today, Wed Wk 5 is purely presentations.

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

This is the last session before presentations. Anyone whose piece isn't substantially complete needs to make a plan. Sit with them: "What's the gap? What do you need to do tonight and tomorrow?"

#### Block 5 — Presentation logistics (5 min)

Wed Wk 5 (Sep 16) is presentations. Walk through what to expect:
- We'll go in alphabetical order
- Each student plays their piece (don't talk during the playback)
- Before pressing play, share *one sentence* about the piece (the prompt has examples)
- After all pieces, brief discussion period
- Final files due to NAS by start of class

Mention the rubric one more time — five dimensions, students should self-assess against it as they finish their work.

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

## Session 7 — Wed Wk 5 (Sep 16): Project 1 presentations

**100 min · Presentation format · MB2525**

This is the high-stakes session of the module. For students, it's the first time they share original work in this course. The room dynamic matters as much as the technical execution.

### Goal

Every student presents their Project 1. Pieces are submitted to NAS. The class hears each other's work, builds a sense of the cohort's range, and starts to understand what the medium does.

### Pre-class checklist

- **Verify all final pieces are uploaded to NAS** to `lastname/project-01/lastname-project01.wav`. Spot-check at least 5-6 folders. If a file is missing, message that student before class — there's still time to upload, but they need to know.
- Have a backup playback method ready: if a student's NAS upload didn't go through, have them play from their local machine. *Don't* spend more than 60 seconds troubleshooting during their slot — pivot to local playback fast.
- Speakers in MB2525 are essential today. Verify they work. Set the volume to a comfortable listening level (loud enough to hear detail; not so loud it's punishing).
- Have the alphabetical presentation order written down. Decide in advance.
- Know the rubric. You'll be using it.

### Block-by-block

#### Block 1 — Open and frame (5 min)

Open warmly: "Today everyone shares the piece they've been working on for two and a half weeks. This is the first time most of you have made and shared something in this medium. That takes nerve."

Set ground rules:
- Listen carefully when each piece plays — no phones, no whispering
- Applause after each piece
- We'll do brief reflection together after all pieces
- The pieces don't have to be "finished" or "polished" to count — a 90-second sketch played sincerely is a real submission

Introduce the order: alphabetical by last name. "When I call your name, walk up, share your one sentence, press play, sit down."

#### Block 2 — Presentations (75 min)

For 25 students at ~3 minutes each (1 minute setup + 2 minute piece): 75 minutes. Tight but workable. If presentations run shorter (some pieces will be 90 seconds), you have buffer.

For each student:
1. Call their name
2. They walk to the instructor machine, find their file on the NAS
3. They turn to the class and say their sentence ("I built this around X" or similar)
4. They press play
5. The class listens
6. After the piece ends, applause
7. *Optional, brief* reaction from you — one observation, not an evaluation. Examples: "I noticed how the sharp metallic sounds came back at the end" or "Beautiful use of silence." Save evaluation for the rubric, not the room.

If a student's NAS file isn't there: pivot fast. "Open Finder, navigate to your local Documents folder, find your file, drag it to Audacity. We'll play from your local copy." Time it tightly — 60 seconds max. If they can't find it on local either, move to the next student and circle back at the end.

#### Block 3 — Group reflection (15 min)

After all pieces have played, open the room:

- "What did you notice across the pieces? Common moves? Differences?"
- "Anyone surprised by something they heard in someone else's work?"
- "What did you learn making yours that you wish you'd known earlier?"

This isn't evaluation — it's the cohort processing the experience together. Students often hear things in classmates' pieces that they want to try in their own future work; that's the productive outcome.

#### Block 4 — Close and bridge to Module 3 (5 min)

Close: "You did something hard. You took a constraint, applied techniques, and made something. That's the work of a music technologist. Project 1 is graded against the rubric and you'll see scores in a few days."

Bridge to Module 3: "Next Monday we move into recording. Project 1 was made entirely from sounds someone else recorded for you. Module 3, you become the person who records the sounds. Bring curiosity."

### Common situations

**A student's piece is incomplete (e.g., 30 seconds long, clearly unfinished).** Play what they have. Treat it the same as any other piece — applause, optional one-sentence observation. Grading happens against the rubric in private; the room is not a judgment space. Late penalty applies per the rubric (10 points/day), but you don't announce that publicly.

**A student is absent on presentation day.** Their piece is still due to the NAS by start of class. Play it without them present (note their absence to follow up about why). Late submission policy applies.

**A piece causes an emotional reaction (a piece that's deeply somber, a piece that's deeply funny, etc.).** Honor the reaction. If laughter is appropriate, let people laugh. If a piece lands with weight, give a beat of silence before applause. Follow the room.

**A piece has technical issues during playback (it sounds wrong, distorted, doesn't play correctly).** First troubleshoot for 30 seconds: check the file, check the playback chain. If it sounds the same wrong way it did when they exported it, that's their submission — play it as-is. If the file is corrupted or the upload was bad, ask them to retry from local; if that fails, move on and circle back.

### Grading

Use the rubric in [`course/projects/project-01-musique-concrete.html`](../course/projects/project-01-musique-concrete.html). Five dimensions, 20 points each. Grade pieces individually, after class — don't rush in the moment.

Late submissions: 10 points/day. Pieces not submitted by the start of class on Wed Sep 16 are late.

### After class

- Confirm all final WAV files are on NAS in the right place
- Begin grading
- Plan to return scores within a week — feedback now is much more useful than feedback at the end of the semester

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

### What gets logged

After Module 2 ends, write a short retrospective (1 page, in this file or a separate retrospective doc) covering:
- What went well
- What didn't
- What you'd change for next year
- Pacing notes — where time was tight, where time was loose
- Student questions that surprised you

This becomes the basis for revising both the module plan and these TA notes for the next time the course runs.
