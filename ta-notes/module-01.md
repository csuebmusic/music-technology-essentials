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
- [ ] Place `01-first-day-setup.pdf` (exported from `handouts/01-first-day-setup.md`) into `/Users/Shared/Downloads/` on every lab machine
- [ ] Walk through the entire session yourself end-to-end on a lab machine the day before, as if you were a student. Time yourself. This will surface every broken thing.
- [ ] Have a backup plan if the NAS is down: students save locally to `~/Desktop/lastname/week-01/` and you'll move files later. **Do not cancel the session over a network issue.**

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

### Block 1 — Welcome (15 min)

- Introduce yourself briefly. Say you're a grad student in [program], working with Inés.
- Don't read the syllabus aloud — just tell them where to find it (Canvas) and what's on it (4 modules, one project per module, a midterm and a final).
- The most important thing to communicate: **"You don't need to know any of this already. That's why we're here."**
- Tell them about the NAS in plain words: *"Everyone in this room is going to be working with big audio files all semester. The lab has a shared file server — we call it the NAS — and that's where your work lives. By the end of today you'll have your own folder on it."*

**Do not** spend this block on classroom rules or grading policies. Those go on Canvas. Day 1 is for hands-on energy.

### Block 2 — Mac & Finder (35 min)

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

### Block 4 — Plug in gear (15 min)

The lab has different audio interfaces and MIDI keyboards across stations. Don't try to teach a single model — teach the categories.

**Hold up an audio interface.** Say what it does in one sentence: *"This converts analog audio (sound from a microphone, or sound to your headphones) into digital audio that the computer can work with, and back."* Show where headphones plug in. Show where mics will plug in (you don't need to plug a mic in today).

**Hold up a MIDI keyboard.** Say what it does: *"This sends note information to the computer. It doesn't make sound on its own — it's a controller. The sound comes from software."*

**Have students plug in:**

1. Audio interface → computer (USB)
2. Headphones → audio interface
3. MIDI keyboard → computer (USB)

**Open Audio MIDI Setup.** `Cmd + Space`, type "Audio MIDI Setup." It opens. Students should see their audio interface listed in the left panel. If they don't:

- Common cause: USB cable not seated properly. Have them unplug and re-plug.
- Common cause: wrong USB port (a few stations have flaky ports). Try another.
- Common cause: interface needs power switch (rare on USB-bus-powered units, common on larger ones).

**Set the interface as system input/output.** In Audio MIDI Setup, right-click the interface → "Use this device for sound input" and "Use this device for sound output." This step is easy to forget and causes confusion in Block 5.

### Block 5 — Hello world (15 min)

The point: every student leaves having saved a file in the right place. This is the win moment.

1. Open QuickTime Player.
2. File → New Audio Recording.
3. Click the small dropdown next to the record button and select the audio interface.
4. Record themselves saying their name and one word about why they're in the class.
5. Stop, File → Save, name the file `lastname-hello.m4a`, save to `lastname/week-01/` on the NAS.

**Common confusion:** Students forget to pick their audio interface in QuickTime's dropdown and end up recording from the built-in mic. The recording will still work, but it won't go through the interface they just plugged in. If you're being strict about teaching signal flow, have them re-record. If time is short, accept it — the point is the file lands in the right place.

**Common confusion:** Students try to save the file before the NAS folder shows up in the save dialog. Show them how to navigate to the NAS in any save dialog (it's in the Finder sidebar, which appears in save dialogs too).

**Before students leave**, open the NAS folder on the projector and scroll through to confirm every student's file is there. This is a small ritual but it makes the work feel real.

If a student's file isn't there:

- Don't single them out publicly. Quietly help them after class or in office hours.
- Most often the issue is they saved locally instead of to the NAS. Have them drag the file into the NAS folder.

---

## Things students will ask

- *"Do I need a Mac at home?"* — No. The lab has everything they need. If they want to work outside the lab, an external SSD is enough.
- *"Can I use my own headphones?"* — Yes. The lab provides them but personal headphones are fine.
- *"What if my audio interface isn't working?"* — Try: unplug/replug, try another USB port, check Audio MIDI Setup. If still broken, switch stations and report it.
- *"Can I take my files home on a USB drive?"* — Yes, but the NAS is the source of truth for graded work. Always work from the NAS in class.
- *"Do I need to buy a textbook?"* — No. Course materials are in the GitHub repo and on Canvas.

---

## Common confusions to watch for

- **"I saved it but I can't find it."** — They saved to a default location like Desktop or Documents instead of the NAS. Walk them through Recents in Finder to find the file, then drag it.
- **"My screenshot didn't work."** — They held the wrong key combination. `Cmd + Shift + 4` to drag a region. The screenshot lands on Desktop.
- **"Audio MIDI Setup is empty."** — The interface isn't seated properly. Replug.
- **"I can't hear anything in the headphones."** — Either the interface isn't selected as system output, or the headphone volume on the interface itself is at zero. Check both.
- **"I don't know my last name's spelling on the NAS."** — Send them to the projector list of folders and have them find theirs.
- **"The NAS folder doesn't have my name."** — Account creation gap. Have them save locally for now; you'll add the folder after class.

---

## Pacing fallbacks

If you're behind:

- Cut Block 2 short. Mac fundamentals continue informally throughout the semester. As long as students can find Finder and save a file, the rest can be picked up.
- The non-negotiable blocks are 3 (NAS), 4 (gear), and 5 (hello world). If you have to drop something, drop the screenshots exercise.

If you're ahead:

- Have students record a second clip and save it as `lastname-hello-v2.m4a`. Reinforces the versioning convention.
- Or have them open Audacity (which will be a focus next week) just to see the icon in Applications.

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
