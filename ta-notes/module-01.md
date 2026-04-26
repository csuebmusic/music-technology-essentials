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
- [ ] Print `02-session-routines.pdf` (exported from `handouts/02-session-routines.html`) and post it at every station — laminated if possible. This is the reference card students follow at the start and end of every session for the rest of the semester.
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

### Block 3 — Set up folders and connect to the NAS (20 min)

This block establishes the workflow model for the entire semester. Students will hear "two folders, the local one is where you work, the NAS is how you transport between machines" and that becomes the mental model they carry forward. It's worth slowing down and being explicit about the *why*.

**Open with the conceptual frame.** Before any clicking, draw on the whiteboard:

```
~/Documents/lastname/        <-->     /music/students/lastname/
   (local working copy)               (NAS — sync between machines)
```

Say something like: *"You'll keep two copies of your work. The local copy on whichever computer you're sitting at is where you actually do the work — it's fast and reliable. The NAS is the master copy. You download from it at the start of every session, and upload to it at the end. That way, if you sit at a different computer next time, your work is waiting on the NAS."*

This is the most important conceptual moment of Day 1. Don't rush it.

**Then: the local folder, first.**

1. Finder → click **Documents** in the sidebar
2. `Cmd + Shift + N` → name it `lastname` (lowercase) → return
3. Open it, `Cmd + Shift + N` again → name it `week-01`

Have students do this together with you on the projector. Drill the lowercase / no-spaces rule again here.

**Then: connect to the NAS.**

1. In Finder: `Cmd + K`
2. Type the NAS address: `smb://[address]`
3. Authenticate

**Important: do not save the password.** When students authenticate, the Mac will offer a checkbox to save the password to the keychain. **Tell students explicitly to leave it unchecked.** Lab machines are shared — saving credentials means the next student at that station can connect under someone else's account. Students type their password each session. The handout doesn't mention this checkbox so students aren't nudged toward it; just call it out verbally if you see anyone hovering over it.

Once students are watching, have them all do it together. **This is the moment most likely to break.** If it does:

- Common cause: typo in the server address. Have them re-check.
- Common cause: wrong username or password. Direct to where this is documented.
- Common cause: the NAS account wasn't pre-created. Have them work locally for the session — they can upload at end of class once you create the folder.

**Once everyone is connected**, have them navigate to `/music/students/[lastname]/` and confirm their folder exists. It should be empty — that's expected. They'll upload their first work to it at end of class.

**Eject the NAS.** Have students eject the NAS from Finder's sidebar. Explicitly: *"You don't need the NAS connected during the session. We'll reconnect at the end of class to upload."* This builds the habit early — no one should be working with the NAS mounted all session.

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

**Sync discipline — preview the lesson.** Briefly tell them: *"Starting Wednesday Aug 26, every session will start with you downloading your folder from the NAS, and end with you uploading it back. We'll go through the full routine at the end of class today. The most important rule: always upload before you leave. If you don't, your work is stranded on this computer, and the next time you sit at a different computer you'll be working from an older version."*

### Block 4 — Set up gear and make a recording (35 min) + Exit routine (5 min)

This is the day's main event. Students plug in their full signal chain, set their levels, and produce one successful recording, then run the exit routine to upload to the NAS for the first time. Combine what was previously two blocks — the pedagogical arc is one continuous activity ending with the upload.

The lab has different audio interfaces and MIDI keyboards across stations, all connecting through a USB hub on each desk. The Mac mini itself is mounted behind the monitor and students never see or touch it. Teach categories, not specific models.

**Time-keeping note.** Reserve the last 5 minutes for the exit routine; that leaves 35 minutes for the gear+recording portion. This is tight for what it covers. Demo each step on the projector, then circulate while students do it themselves. Don't move to the next step until most of the room is caught up.

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

**Bring up monitoring.** Have students put headphones on (slider already up — see above), then turn up the headphone knob to about noon (12 o'clock, knob pointing straight up), then the main knob to about noon. They probably won't hear anything yet because gain is still at zero. That's fine.

**The mix knob (only some interfaces).** Roughly half of the lab interfaces have an additional knob labeled "Mix" or "Direct/USB" — it controls the headphone balance between the live input signal and what the computer is sending back. The other half handle this internally and don't expose it to the user.

Before you teach the gain step, point this out:

> "Some of you have an extra knob labeled Mix or Direct-USB. If you do, set it to about 60% toward the direct/input side and 40% toward the computer side — about 11 o'clock if direct is on the left. This means you'll hear mostly yourself live, plus a little of any playback the computer sends. If your interface doesn't have this knob, don't worry — it handles this for you. We'll come back to this concept in Module 3."

Walk to the stations that have it and confirm they've set it correctly. This is a tiny piece of "your gear may differ" diversity — embrace it as a teaching moment rather than something to apologize for.

**Set the gain — this is the moment.** Have students talk into the mic at normal volume (suggest "count to twenty" or "say what you had for breakfast"). While talking, slowly turn up the gain knob. They watch the QuickTime level meter. Stop when the meter is regularly moving but not pinning the right edge.

This is the first time most students will see input level visually represented. Worth pausing here briefly:

> "What you just did is called *gain staging* — setting the input level so the signal is strong enough to be useful, but not so strong that it distorts. It's one of the most important skills in recording, and we'll come back to it properly in Module 3. For today, the rule is: meter moving = good, meter pinned all the way to the right = too hot, turn down."

Don't go deeper than that on Day 1. The temptation will be to teach digital headroom, dBFS, the relationship between input gain and noise floor — save it. Day 1 is the introduction; Module 3 is the proper treatment.

**Record + save.** Hit record, say name + one word, stop, listen back. Save as `lastname-hello.m4a` to `~/Documents/lastname/week-01/` (local). The NAS upload happens during the exit routine.

**Common confusions during this block:**

- *"I can't hear anything in the headphones."* — Check in this order: (1) headphone slider on cable all the way up; (2) headphone knob on interface above zero; (3) audio interface set as system output in Audio MIDI Setup; (4) main/output knob above zero; (5) for stations with a mix knob, that it isn't pinned all the way to one side.
- *"I hear myself but no playback."* (only for stations with mix knob) — Mix knob is too far toward direct. Move toward the computer/USB side.
- *"I hear playback but not myself."* (only for stations with mix knob) — Mix knob is too far toward computer. Move toward the direct/input side.
- *"My meter isn't moving when I talk."* — Gain knob is at zero, or wrong input is selected in QuickTime, or mic XLR cable not seated properly.
- *"My meter is pinning red the whole time."* — Gain too high. Turn it down until peaks just stop hitting the right edge.
- *"My recording sounds quiet."* — Gain was too low when recording. Have them re-record with the gain higher.
- *"My recording sounds distorted/crunchy."* — Gain was too high (clipping). Re-record with the gain lower.
- *"I forgot to pick the audio interface in QuickTime."* — They recorded through the Mac mini's nonexistent built-in mic and got nothing, or got something through the wrong source. Have them re-record.
- *"I can't find the NAS in the save dialog."* — The NAS appears in the sidebar of save dialogs the same way it does in Finder. Show them the sidebar.

**Fallback if gear is genuinely broken.** If a station has a hardware problem you can't fix in 5 minutes, have the student record through QuickTime's built-in option (which on a Mac mini may mean the monitor's mic, or no mic at all). The point is they leave having saved locally and uploaded to the NAS. Fix the gear after class. Day 1 success = file uploaded to the NAS during the exit routine.

**Before students leave**, open the NAS folder on the projector and scroll through to confirm every student's file is there. This is a small ritual but makes the work feel real.

If a student's file isn't there in their local folder:
- Don't single them out publicly. Quietly help them after class or in office hours.
- Most often the issue is they saved to Desktop or Downloads. Walk them through Recents in Finder to find the file, then drag it into `~/Documents/lastname/week-01/`.

**Teach the exit routine — last 5 minutes of class.** Before dismissing, walk students through the end-of-session routine on the projector. They have a printed copy at every station (Handout 02 — Session Routines) and a version in the Day 1 handout, but verbal reinforcement on Day 1 sets the habit. This is the moment students upload their work to the NAS for the first time.

Walk them through:

1. Save the recording in QuickTime if they haven't already (`Cmd + S`)
2. Connect to the NAS again: `Cmd + K`, address, sign in (no keychain save)
3. Open two Finder windows side by side: one on `~/Documents/lastname/`, one on the NAS at `/music/students/lastname/`
4. Drag the *contents* of the local `lastname/` folder (today: just `week-01/` with the hello file inside) onto the NAS `lastname/` folder. Or simply drag the entire local `lastname/` folder onto `/music/students/` and choose **Replace** if asked.
5. Confirm the upload: the NAS folder should now show today's modification date and contain `week-01/[lastname]-hello.m4a`
6. Eject the NAS from Finder's sidebar
7. Sign out of any browser accounts (Canvas, Google, etc.); quit the browser
8. Quit all apps with `Cmd + Q`
9. Knobs to zero, headphones away, chair in

Tell them this is a 2-minute routine they'll do every session for the rest of the semester, and that **starting Wednesday Aug 26, every session also begins with downloading from the NAS** (the start-of-session half of Handout 02).

**Verify uploads on the projector.** Once everyone is done, open `/music/students/` on the projector and scroll through. Confirm every student's folder is there with their hello file inside. This is the same "small ritual" as before, but now it confirms upload happened, not just save.

**Common Day-1 confusions during the upload:**

- *Move vs copy.* When dragging from local to NAS, macOS may try to *move* (delete the local copy). Students should hold `Option` while dragging to force a copy, or use `Cmd + C` / `Cmd + V` (which always copies). Demo this explicitly. Losing the local copy isn't a disaster on Day 1, but it sets a bad habit.
- *Replace prompt confusion.* If macOS asks whether to replace the existing folder, the answer today is **Replace** — the local version is the latest. (Going forward, students should be checking modification dates before replacing, but on Day 1 there's no ambiguity.)
- *Two Finder windows.* Some students will be confused about how to have two windows open. Show them `Cmd + N` to make a new Finder window. Demo dragging between them.

---

## Things students will ask

- *"Do I need a Mac at home?"* — No. The lab has everything they need. The NAS keeps your work synced between lab machines.
- *"Can I use my own headphones?"* — Yes. The lab provides them but personal headphones are fine.
- *"What if my audio interface isn't working?"* — Try: unplug from the hub, replug into a different hub port, check Audio MIDI Setup. If still broken, switch stations and report it.
- *"Can I take my files home on a USB drive?"* — Yes — copy from your local `~/Documents/lastname/` folder. The NAS stays in the lab. (Note: home Macs may not handle some lab software the same way, so working at home is at your own risk.)
- *"What if I forget to upload at the end?"* — Your work is stranded on that machine. The next time you're at that exact same station, it'll still be in `~/Documents/lastname/`, but if you're at a different station, you'll be working from an older version. Always upload.
- *"What if I forget to download at the start?"* — You'll be working from an older version. Sync regularly: download at start, upload at end. If you realize mid-session, save what you've done, then go check the NAS to see what you should have started with.
- *"Do I need to buy a textbook?"* — No. Course materials are in the GitHub repo and on Canvas.

---

## Common confusions to watch for

- **"I saved it but I can't find it."** — They saved to Desktop or Downloads instead of `~/Documents/lastname/`. Walk them through Recents in Finder to find the file, then drag it.
- **"My screenshot didn't work."** — They held the wrong key combination. `Cmd + Shift + 4` to drag a region. The screenshot lands on Desktop.
- **"Audio MIDI Setup is empty."** — The interface isn't seated properly. Replug.
- **"I can't hear anything in the headphones."** — Check four things in this order: (1) the in-line slider on the headphone cable is all the way up, (2) the headphone knob on the interface is above zero, (3) the audio interface is selected as system output in Audio MIDI Setup, (4) the main/output knob is above zero.
- **"My meter isn't moving when I talk."** — Gain knob still at zero, wrong input selected in QuickTime, or XLR cable not seated.
- **"My recording sounds distorted."** — Gain was too high during recording. Re-record with the gain lower.
- **"I don't know my last name's spelling on the NAS."** — Send them to the projector list of folders and have them find theirs.
- **"The NAS folder doesn't have my name."** — Account creation gap. Have them work locally for the session; create the folder after class and have them upload at the next session.
- **"Local and NAS folders look different."** — Sync issue. Whichever has the newer modification date is the trusted version. Copy that one over the older one. If they can't tell which is newer, ask the TA before deleting anything.

---

## Pacing fallbacks

The day's clock is genuinely tight: Welcome 10 + Mac/Finder 30 + Folders/NAS 20 + Gear/recording 35 + Exit routine 5 = 100 min. That assumes Block 4 holds at 35 min for the gear and recording portion, with the last 5 min of class reserved for the exit routine. If gear setup or gain staging runs long, the exit routine is non-negotiable — cut something inside Block 4 instead.

If you're behind:

- Cut Block 2 short. Mac fundamentals continue informally throughout the semester. As long as students can find Finder and save a file, the rest can be picked up.
- Block 4 (gear + recording) is the heart of the day. Don't shortcut the order-of-operations (knobs to zero, slider up, plug in, monitor up, gain last). That sequence is the lesson.
- If absolutely necessary, accept a less-than-perfect gain setting and let students just get a recording. Module 3 will treat this properly.
- **Never skip the exit routine.** If everything else has run long, dismiss students one-by-one only after they've uploaded to the NAS. The whole semester's workflow depends on this habit forming on Day 1.

If you're ahead:

- Have students record a second clip and save it as `lastname-hello-v2.m4a`. Reinforces the versioning convention.
- Have them try adjusting the gain too low (recording too quiet) and too high (clipping) to hear the difference. Sets up Module 3.
- Open Audacity (which will be a focus next week) just to see the icon in Applications.

---

## After class

- [ ] Open the NAS at `/music/students/`. Confirm every student has a `lastname/week-01/[lastname]-hello.m4a` uploaded. Note any missing students for follow-up — these are students who didn't run the exit routine, which is the sync discipline we're trying to build from Day 1.
- [ ] Note any technical issues (broken stations, NAS hiccups, gear that didn't work) in a running log so they get fixed before Monday.
- [ ] If the NAS had problems, debrief with Inés about what happened and what to fix.
- [ ] Email any students whose files are missing — don't shame, just make sure they know how to do it before Monday.

---

## What to assess

Nothing in Module 1 is graded. The deliverable (`lastname-hello.m4a` uploaded to the NAS) is a check that everyone made it through Day 1 and ran the exit routine. The only thing to "assess" is whether each student's file is in the right place on the NAS — that's binary, no rubric needed.

If a student is missing the file by Monday's class, that's an early signal they may need extra support, particularly with the sync workflow. Reach out individually.
