# Module 1 — Computer & Studio Fluency

**Week 1 — Wednesday Aug 19, 2026** (single session, 3:00–4:40 PM, MB2525)

---

## Module purpose

Most students arrive without Mac experience or studio fluency. Before any music-technology content can land, students need to be able to:

- Navigate the Mac desktop and Finder
- Save and retrieve files using a clear naming convention
- Connect to the lab NAS and find their personal folder
- Plug in headphones, an audio interface, and a MIDI keyboard
- Verify their setup in Audio MIDI Setup

This module is short but foundational. Everything downstream depends on it.

---

## Learning outcomes

By the end of this single session, students should be able to:

1. Locate, open, and navigate Finder; understand file paths, folders, and basic keyboard shortcuts
2. Set up a local working folder at `~/Documents/lastname/` and connect to the lab NAS
3. Save files using the course naming convention
4. Identify each piece of gear at their station (USB hub, audio interface, mic, MIDI keyboard, headphones) and connect them correctly
5. Set the three knobs on an audio interface (gain, main, headphone) in the correct order, starting from zero
6. Use a software level meter to set mic gain at a usable level
7. Record a short audio clip through the full signal chain and save it to their local folder
8. Run through the end-of-session routine: upload local folder to NAS, eject NAS, sign out of browser accounts, quit apps, leave the station clean
9. Articulate the local-first / NAS-as-sync workflow that the course will use all semester

---

## Session plan (Wed Aug 19, 100 minutes)

### Block 1 — Welcome & framing (3:00–3:10)

- Instructor introduction
- Quick overview of the course: what we'll do, when projects are due, how the semester is shaped
- The room: shared Music/Art lab, MB2525, what lives where
- The vibe: hands-on, project-based, no prior experience expected
- Where to find everything: Canvas (announcements, grades), GitHub repo (course materials, handouts), NAS (working files)

### Block 2 — Mac & Finder fundamentals (3:10–3:40)

Task-based, not lecture. TA demos each step on the projector, then students do it.

- Opening Finder; understanding the menu bar, Dock, Desktop
- Folders, files, and paths
- Essential keyboard shortcuts: `Cmd+C`, `Cmd+V`, `Cmd+X`, `Cmd+Z`, `Cmd+S`, `Cmd+Shift+N` (new folder), `Cmd+Space` (Spotlight)
- Taking a screenshot: `Cmd+Shift+4` (region)
- The "don't save to Desktop" rule (Desktop is wiped periodically)
- Show/hide file extensions (Finder → Settings → Advanced — turn extensions ON)

**Practical exercise:** Each student opens the local handout (`/Users/Shared/Downloads/01-first-day-setup.pdf` — pre-loaded by the TA), makes a throwaway folder on the Desktop, takes a screenshot, renames it (previewing the naming convention), drags it into the folder, and deletes the folder.

### Block 3 — Set up folders and connect to the NAS (3:40–4:00)

This is where the **workflow model** of the course is established. Students learn that they work locally and use the NAS to sync between sessions. Establishing this on Day 1 sets a precedent for the rest of the semester.

- Two-folder model: `~/Documents/lastname/` (local working copy) and `nas:/music/students/lastname/` (master / sync location)
- The pattern: download from NAS at start of session, work locally, upload to NAS at end
- Folder convention: `lastname/` at the top level, then per-week or per-project subfolders
- File naming convention: `lastname-projectname-version.ext` — lowercase, hyphens, no spaces, no special characters

**Practical exercise:**
1. Each student creates `~/Documents/lastname/week-01/` locally
2. Connects to the NAS (`Cmd+K`, `smb://[address]`, log in — do NOT save credentials to keychain)
3. Confirms their personal folder exists at `/music/students/lastname/`
4. Ejects the NAS — they'll reconnect at the end of the session to upload

### Block 4 — Set up gear and make a recording (4:00–4:40)

This is the day's main event. Students plug in their full signal chain (mic, audio interface, headphones, MIDI keyboard), set their levels, and produce one successful recording. The recording gets saved to their *local* folder during the session; uploading to the NAS happens as part of the exit routine.

The pedagogical arc is the full signal chain in miniature: physical sound → mic → cable → interface → gain → software → file. Students will return to every link in this chain across the semester. Day 1 is the first time they touch all of it.

**Order of operations (matters — don't shortcut):**

1. **All three interface knobs to zero** (gain, main/output, headphone) — protects ears and gear before anything is plugged in
2. **Plug in:** audio interface USB → hub; mic XLR → interface; MIDI keyboard USB → hub; headphones → interface headphone jack
3. **Headphone in-line slider all the way up** (the in-line slider on the headphone cable — common cause of confusion later)
4. **Verify in Audio MIDI Setup**, set as system input/output, *quit* the app (not close — Day 1 chance to teach close vs quit)
5. **Open QuickTime → File → New Audio Recording**, select interface from dropdown
6. **Bring up monitoring**: headphone knob to noon, then main knob to noon
7. **If the interface has a Mix / Direct-USB knob**, set it to ~60% direct / 40% USB (about 11 o'clock if direct is on the left). Roughly half of lab interfaces have this; the rest skip this step.
8. **Set the gain** by talking into the mic and watching QuickTime's level meter — target is meter moving regularly but not pinning the right edge
9. **Record** name + one word, **listen back**, **save** as `lastname-hello.m4a` to `~/Documents/lastname/week-01/` (local)

**Light touch on gain staging.** This is a foundational concept in the course, but Day 1 isn't where it gets the full treatment. For today, students should leave knowing:
- The three knobs exist and what each does in one sentence
- The order to turn them up (gain last)
- The visual meter is the goal — moving but not pinned
- We'll return to gain staging properly in Module 3

**Fallback if gear is broken:** If a student's mic, interface, or hub isn't working and can't be quickly fixed, they record using QuickTime's built-in mic (no interface) and save the file as normal to the local folder. The TA fixes the gear after class. Day 1 success = file in the local folder, then uploaded to NAS during exit routine.

**Last 5 minutes — exit routine.** TA walks through Handout 02 (Session Routines) on the projector. Students reconnect to the NAS, upload their `lastname/` folder for the first time, eject, and complete the rest of the routine. Once everyone has uploaded, the TA opens the NAS on the projector and scrolls through to confirm every student's folder is there with their hello file inside.

---

## Deliverable

A `lastname/` folder uploaded to the NAS at `/music/students/[lastname]/`, containing `week-01/[lastname]-hello.m4a`. The local copy at `~/Documents/lastname/` should also exist. Not graded — confirmation everyone made it through Day 1 with the workflow established.

---

## Listening assignment (assigned end of session)

None for Week 1. Module 1 is a setup module. The first listening assignment lands at the start of Module 2.

---

## What to bring to Wednesday Aug 26 (Week 2)

- Headphones (lab provides, but students may bring their own if they prefer)
- Notebook or note-taking tool of choice
- Curiosity

---

## Notes for the TA

See [`ta-notes/module-01.md`](../../ta-notes/module-01.md) for detailed teaching notes, common student confusions, and pacing guidance.
