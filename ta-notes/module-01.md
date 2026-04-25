# TA Notes — Module 1 (Week 1, Wed Aug 19)

This is the first day of class. The single biggest thing you can do is establish that the lab is a low-stakes, supportive place to learn. Most students arrive nervous about technology. If they leave feeling like *they* did something — saved a file, plugged in gear, made a recording — they'll come back Monday ready to learn. If they leave feeling lost, the rest of the semester is harder.

Plan to circulate constantly. Do not lecture for more than 5 minutes at a stretch. Demo, then have them do it. Be willing to repeat instructions twice; some students will need to see something three times before it lands.

---

## Before class — preparation checklist

Do all of this **at least one day in advance** of Aug 19, ideally two:

- [ ] Confirm the NAS is running and reachable from every lab machine
- [ ] Confirm every student has a NAS account and a `lastname/` folder pre-created
- [ ] Get the list of student last names from the registrar; pre-create folders matching exactly (lowercase, hyphenate any spaces)
- [ ] Write the NAS server address on the whiteboard before class starts
- [ ] Place `01-first-day-setup.pdf` (exported from `handouts/01-first-day-setup.html`) into `/Users/Shared/Downloads/` on every lab machine
- [ ] Walk through every station: confirm USB hub works, audio interface is recognized, mic and XLR cable are at the station, MIDI keyboard is at the station, headphones are at the station with the in-line slider all the way up
- [ ] Test-record at one station end-to-end (mic → interface → QuickTime → NAS) to confirm the full chain works
- [ ] Walk through the entire session yourself end-to-end on a lab machine the day before, as if you were a student. Time yourself. This will surface every broken thing.
- [ ] Have a backup plan if the NAS is down: students save locally to a temp folder you'll move later. **Do not cancel the session over a network issue.**
- [ ] Have at least one spare hub, one spare XLR cable, and one spare set of headphones available in case something fails during class

---

## What students walk in knowing

Assume:

- Most have **never used a Mac** in any meaningful way
- Most have **never connected to a file server**
- Most do not know what an **audio interface** is
- Most have **not seen a MIDI keyboard** before
- Some have used GarageBand or Audacity casually; very few have used a real DAW
- A small number will be quite advanced relative to the rest — they'll be bored if you go too slow, but they're useful as peer helpers

The right pacing: **slow enough that the slowest student keeps up, with side-tasks for the fast students.** When a fast student finishes early, ask them to help a neighbor. This is your secret weapon.

---

## Block-by-block notes

### Block 1 — Welcome (10 min)

- Introduce yourself briefly. Say you're a grad student in [program], working with Inés.
- Don't read the syllabus aloud — just tell them where to find it (Canvas) and what's on it (4 modules, one project per module, a midterm and a final).
- The most important thing to communicate: **"You don't need to know any of this already. That's why we're here."**
- Tell them about the NAS in plain words: *"Everyone in this room is going to be working with big audio files all semester. The lab has a shared file server — we call it the NAS — and that's where your work lives. By the end of today you'll have your own folder on it."*

**Do not** spend this block on classroom rules or grading policies. Those go on Canvas. Day 1 is for hands-on energy.

### Block 2 — Mac & Finder (30 min)

This is the longest single block. Pace it carefully.

**Demo on the projector first, then have students do each step.** Don't try to teach all the shortcuts at once — introduce them as they come up:

- "Open Finder." (Some students don't know what Finder is. Show the smiley-face icon.)
- "Take a screenshot." (`Cmd+Shift+4`, drag a region.)
- "Now find that screenshot." (It goes to Desktop by default — this is where many students freeze. Walk them through opening Desktop in Finder.)
- "Make a new folder called `test`." (Right-click → New Folder, OR `Cmd+Shift+N`.)
- "Drag the screenshot into the folder."
- "Now delete the folder." (Drag to Trash, or `Cmd+Delete`.)

That whole sequence in five minutes teaches: Finder, screenshots, Desktop location, folder creation, drag-and-drop, deletion.

**Show file extensions.** This matters more than students realize. Walk them through Finder → Settings → Advanced → "Show all filename extensions." Some students will have the toggle already on; some won't. Make sure everyone leaves with extensions visible.

**Common confusion:** Students don't understand that "Documents," "Desktop," and "Downloads" are folders just like any other folder. Show them the same locations from inside Finder's sidebar — it's the same thing as the Desktop they see behind their windows.

**Practical exercise — local handout:** Have students find `01-first-day-setup.pdf` in `/Users/Shared/Downloads/` and open it. This proves they can navigate Finder. (You pre-loaded this earlier.)

### Block 3 — NAS connection (20 min)

This is the make-or-break block. Plan it carefully.

**Demo first on the projector.**

1. In Finder: `Cmd + K`
2. Type the NAS address: `smb://[address]`
3. Authenticate
4. The NAS appears in Finder's sidebar
5. Navigate to `/music/students/`
6. Find your last name folder

Once students are watching, have them all do it together at the same time. **This is the moment most likely to break.** If it does:

- Common cause: typo in the server address. Have them re-check.
- Common cause: wrong username or password. Direct to where this is documented.
- Common cause: the NAS account wasn't pre-created. Apologize, have them save locally, fix it after class.

**Once everyone is connected**, walk them through:

- Their `lastname/` folder is the only place they'll save work for this class
- Inside it, they make subfolders per week or per project
- Have everyone create `lastname/week-01/` right now

**File naming convention.** Write the convention on the whiteboard:

```
lastname-projectname-version.ext
```

Examples (use your name and Inés's so it doesn't feel arbitrary):

```
thiebaut-hello.m4a
smith-soundpiece-v1.wav
```

Drill the rules: lowercase, hyphens, no spaces, no special characters. **Tell them why:** different operating systems and different software treat capitalization, spaces, and special characters inconsistently. A file named `My Project (final!).wav` will eventually break something.

### Block 4 — Set up gear and make a recording (40 min)

This is the day's main event. Students plug in their full signal chain, set their levels, and produce one successful recording. Combine what was previously two blocks — the pedagogical arc is one continuous activity.

The lab has different audio interfaces and MIDI keyboards across stations, all connecting through a USB hub on each desk. The Mac mini itself is mounted behind the monitor and students never see or touch it. Teach categories, not specific models.

**Time-keeping note.** This block runs 40 minutes, which is tight for what it covers. Demo each step on the projector, then circulate while students do it themselves. Don't move to the next step until most of the room is caught up.

#### Step-by-step facilitation

**Show the gear.** Hold up each piece and say what it does in one sentence:

- *USB hub:* "Everything plugs into this. It's already connected to the computer behind your monitor. Don't unplug the hub itself."
- *Audio interface:* "This converts analog audio (sound from a microphone, or sound to your headphones) into digital audio that the computer can work with, and back."
- *Microphone:* "This is a tabletop mic. It plugs into the audio interface using an XLR cable — the thick three-pin one."
- *MIDI keyboard:* "This sends note information to the computer. It doesn't make sound on its own — it's a controller. The sound comes from software."

**Knobs to zero first.** Before anything else, have students turn all three interface knobs (gain, main, headphone) all the way down. *Say why:* "If something is set wrong, you can get a sudden loud sound when you plug in. Starting at zero protects your ears and the gear. This is something you'll do for the rest of your life if you keep working with audio."

**Plug everything in (in this order):**

1. Audio interface → USB hub
2. Mic → audio interface front-panel input (XLR)
3. MIDI keyboard → USB hub
4. Headphones → headphone jack on the audio interface

**The headphone slider gotcha.** The lab headphones have an in-line volume slider on the cable. Have students slide it all the way up *before* putting headphones on. This is a real Day 1 trap — students think the gear is broken when actually the slider is at zero. Calling it out early saves 10 minutes of confusion.

**Audio MIDI Setup.** `Cmd + Space`, type "Audio MIDI Setup." It opens. Students should see their audio interface listed.

If they don't:
- Common cause: USB cable not seated properly. Replug into the same hub port.
- Common cause: a flaky port on the hub. Try a different port on the same hub.
- Common cause: interface needs power switch (rare on USB-bus-powered units, common on larger ones).
- If a whole hub appears dead (multiple devices not recognized), have the student switch stations and flag the hub for replacement.

Right-click the interface → "Use this device for sound input" and "Use this device for sound output." This step is easy to forget and causes confusion later.

**Open QuickTime → New Audio Recording.** Walk students through opening QuickTime, choosing File → New Audio Recording, clicking the dropdown arrow next to the record button, and selecting their audio interface as the source.

**Bring up monitoring.** Have students put headphones on (slider already up — see above), then turn up the headphone knob to ~25% (about a quarter turn), then the main knob to ~25%. They probably won't hear anything yet because gain is still at zero. That's fine.

**Set the gain — this is the moment.** Have students talk into the mic at normal volume (suggest "count to twenty" or "say what you had for breakfast"). While talking, slowly turn up the gain knob. They watch the QuickTime level meter. Stop when the meter is regularly moving but not pinning the right edge.

This is the first time most students will see input level visually represented. Worth pausing here briefly:

> "What you just did is called *gain staging* — setting the input level so the signal is strong enough to be useful, but not so strong that it distorts. It's one of the most important skills in recording, and we'll come back to it properly in Module 3. For today, the rule is: meter moving = good, meter pinned all the way to the right = too hot, turn down."

Don't go deeper than that on Day 1. The temptation will be to teach digital headroom, dBFS, the relationship between input gain and noise floor — save it. Day 1 is the introduction; Module 3 is the proper treatment.

**Record + save.** Hit record, say name + one word, stop, listen back. Save as `lastname-hello.m4a` to NAS at `lastname/week-01/`.

**Common confusions during this block:**

- *"I can't hear anything in the headphones."* — Check in this order: (1) headphone slider on cable all the way up; (2) headphone knob on interface above zero; (3) audio interface set as system output in Audio MIDI Setup; (4) main/output knob above zero.
- *"My meter isn't moving when I talk."* — Gain knob is at zero, or wrong input is selected in QuickTime, or mic XLR cable not seated properly.
- *"My meter is pinning red the whole time."* — Gain too high. Turn it down until peaks just stop hitting the right edge.
- *"My recording sounds quiet."* — Gain was too low when recording. Have them re-record with the gain higher.
- *"My recording sounds distorted/crunchy."* — Gain was too high (clipping). Re-record with the gain lower.
- *"I forgot to pick the audio interface in QuickTime."* — They recorded through the Mac mini's nonexistent built-in mic and got nothing, or got something through the wrong source. Have them re-record.
- *"I can't find the NAS in the save dialog."* — The NAS appears in the sidebar of save dialogs the same way it does in Finder. Show them the sidebar.

**Fallback if gear is genuinely broken.** If a station has a hardware problem you can't fix in 5 minutes, have the student record through QuickTime's built-in option (which on a Mac mini may mean the monitor's mic, or no mic at all). The point is they leave with a file on the NAS. Fix the gear after class. Day 1 success = file in the right place.

**Before students leave**, open the NAS folder on the projector and scroll through to confirm every student's file is there. This is a small ritual but makes the work feel real.

If a student's file isn't there:
- Don't single them out publicly. Quietly help them after class or in office hours.
- Most often the issue is they saved locally instead of to the NAS. Have them drag the file into the NAS folder.

---

## Things students will ask

- *"Do I need a Mac at home?"* — No. The lab has everything they need. If they want to work outside the lab, an external SSD is enough.
- *"Can I use my own headphones?"* — Yes. The lab provides them but personal headphones are fine.
- *"What if my audio interface isn't working?"* — Try: unplug from the hub, replug into a different hub port, check Audio MIDI Setup. If still broken, switch stations and report it.
- *"Can I take my files home on a USB drive?"* — Yes, but the NAS is the source of truth for graded work. Always work from the NAS in class.
- *"Do I need to buy a textbook?"* — No. Course materials are in the GitHub repo and on Canvas.

---

## Common confusions to watch for

- **"I saved it but I can't find it."** — They saved to a default location like Desktop or Documents instead of the NAS. Walk them through Recents in Finder to find the file, then drag it.
- **"My screenshot didn't work."** — They held the wrong key combination. `Cmd + Shift + 4` to drag a region. The screenshot lands on Desktop.
- **"Audio MIDI Setup is empty."** — The interface isn't seated properly. Replug.
- **"I can't hear anything in the headphones."** — Check four things in this order: (1) the in-line slider on the headphone cable is all the way up, (2) the headphone knob on the interface is above zero, (3) the audio interface is selected as system output in Audio MIDI Setup, (4) the main/output knob is above zero.
- **"My meter isn't moving when I talk."** — Gain knob still at zero, wrong input selected in QuickTime, or XLR cable not seated.
- **"My recording sounds distorted."** — Gain was too high during recording. Re-record with the gain lower.
- **"I don't know my last name's spelling on the NAS."** — Send them to the projector list of folders and have them find theirs.
- **"The NAS folder doesn't have my name."** — Account creation gap. Have them save locally for now; you'll add the folder after class.

---

## Pacing fallbacks

If you're behind:

- Cut Block 2 short. Mac fundamentals continue informally throughout the semester. As long as students can find Finder and save a file, the rest can be picked up.
- Block 4 (gear + recording) is the heart of the day. Don't shortcut the order-of-operations (knobs to zero, slider up, plug in, monitor up, gain last). That sequence is the lesson.
- If absolutely necessary, accept a less-than-perfect gain setting and let students just get a recording. Module 3 will treat this properly.

If you're ahead:

- Have students record a second clip and save it as `lastname-hello-v2.m4a`. Reinforces the versioning convention.
- Have them try adjusting the gain too low (recording too quiet) and too high (clipping) to hear the difference. Sets up Module 3.
- Open Audacity (which will be a focus next week) just to see the icon in Applications.

---

## After class

- [ ] Open the NAS folder. Confirm every student has a `lastname-hello.m4a` in `lastname/week-01/`. Note any missing students for follow-up.
- [ ] Note any technical issues (broken stations, NAS hiccups, gear that didn't work) in a running log so they get fixed before Monday.
- [ ] If the NAS had problems, debrief with Inés about what happened and what to fix.
- [ ] Email any students whose files are missing — don't shame, just make sure they know how to do it before Monday.

---

## What to assess

Nothing in Module 1 is graded. The deliverable (`lastname-hello.m4a`) is a check that everyone made it through Day 1. The only thing to "assess" is whether each student has the file in the right place — that's binary, no rubric needed.

If a student is missing the file by Monday's class, that's an early signal they may need extra support. Reach out individually.
