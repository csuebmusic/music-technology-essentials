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
- [Session 7 — Wed Wk 5 (Sep 16): Project 1 final work session + submission](#session-7--wed-wk-5-sep-16-project-1-final-work-session--submission)
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

The reading for today is [`course/readings/module-02-week-03-editing-envelope.html`](../course/readings/module-02-week-03-editing-envelope.html). It includes 9 audio demos: three contrasting envelope shapes (sharp, sustained, evolving), one source transformed by four edits (truncate, reverse, fade-in), and a hard-cut vs. crossfade comparison demonstrating click pops at edit boundaries. Read it before class. The audio demos are central to how the concepts land, so listen on headphones if you've never gone through them.

### Pre-class checklist

- Read the Mon Wk 3 reading and listen to all 9 audio demos
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
- **Process expectations.** Start early. Save versions. Take breaks. Ask for feedback during lab time.
- **Submission:** Wed Sep 16, two weeks from today. End of class, files uploaded to NAS (private working folder + class listening folder). No live presentation — listening happens asynchronously after, with a short peer-listening response due Mon Sep 21.
- **Rubric.** Five dimensions, 20 points each, 100 total. Late submissions are handled per the syllabus's late policy.

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

## Session 6 — Mon Wk 5 (Sep 14): Dynamics + mixing tool Part 2

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

Wed Wk 5 (Sep 16) is the final work session and submission deadline. Walk through what to expect:
- Class is a final work session — no new content, just time to finish
- Files due to NAS by **end of class**, not start
- Two locations: their private working folder (`lastname/project-01/`) and the class listening folder (`/music/shared/mus-381-fall-2026/project-01-pieces/`). Both must have the final WAV.
- A short peer-listening response is due Mon Sep 21 (about classmates' pieces in the listening folder), separate assignment

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

## Session 7 — Wed Wk 5 (Sep 16): Project 1 final work session + submission

**100 min · Lab-style · MB2525**

This is the closing session of Module 2. There is no live presentation. Class time is dedicated to finishing pieces and uploading them to NAS by end of class. Listening to each other's pieces happens asynchronously in the days after, with a short peer-listening response due Mon Sep 21.

Why no presentations? Math: 25 students × 3-5 minutes each is longer than class time, and asynchronous listening gives students more careful, repeatable encounters with each other's work. The trade-off is the live "press play" moment, which some pedagogies value highly. We'll partly recover the cohort feeling on Mon Sep 21 with a brief discussion of what students heard.

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

Mention the peer-listening response due Mon Sep 21. They've gotten an assignment ahead of time so they can plan to listen during the week.

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

Late submissions are handled per the syllabus's late policy. Pieces not in the class listening folder by end of class on Wed Sep 16 are late.

### After class

- Confirm every student has a file in the class listening folder. Note the missing ones.
- For students whose files are only in their private working folder, message them — they need to add to the class folder for the submission to be complete (or you can copy on their behalf, instructor's call).
- Begin grading. Plan to return scores within a week.
- The class listening folder is now populated. Listening happens between today and Mon Sep 21, when the peer-listening response is due.

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
