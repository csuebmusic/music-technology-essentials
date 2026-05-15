# Videos

Short Audacity screen recordings used as inline demos inside readings. Each clip shows a single editing operation performed on a real waveform, so students see in their own DAW exactly what the term means.

## Directory layout

```
videos/
├── module-02-week-03/    Editing vocabulary (Lecture 2)
│   ├── cut.mp4
│   ├── trim.mp4
│   ├── splice.mp4
│   ├── fades.mp4
│   ├── crossfade.mp4
│   └── reverse.mp4
└── …
```

The editing-vocabulary set has six videos. The *loop* term doesn't get a video because Audacity's looping is split between a playback-only feature and the manual copy-paste-in-succession workaround. Both are covered in the prose definition with a forward pointer to Module 4 (Ableton), where looping is a first-class compositional tool.

## Recording specs

For consistency across the editing-vocabulary set, each clip should:

- **Use the same source audio.** A single voice recording (or other sound with a clear envelope) used across all clips in the set. Reinforces the "one source, transformed by edits" framing of the module.
- **Be silent.** No audio track. Record video only, or strip the audio in post. Browsers block autoplay-with-sound by default, and silent clips don't make surprise noise when students scroll past.
- **Be short.** 5 to 12 seconds. Long enough to show source → operation → result. Short enough that students don't lose patience.
- **Capture the Audacity track view, not the whole desktop.** The waveform region with at least the timeline, transport, and Edit menu visible. Avoid showing the whole macOS window with menus and the dock.
- **Show the cursor.** Students need to see where you click. Hiding it makes the operation look magical.
- **Hold the source for ~1 second** before doing anything, so students see the starting state.
- **Hold the result for ~1 second** after the operation, so they see what changed.

## Encoding

Recordings come in as `.mov` (QuickTime). Re-encode to `.mp4` (H.264) before placing in this folder:

```bash
ffmpeg -i input.mov \
  -vf "scale=1280:-2,fps=30" \
  -c:v libx264 -crf 23 -preset slow \
  -movflags +faststart \
  -an \
  output.mp4
```

Notes on the flags:
- `scale=1280:-2` resizes to 1280px wide preserving aspect ratio, with height rounded to an even number (required by H.264)
- `fps=30` drops 60fps screen recordings to 30 — invisible quality loss for screen content, halves the file size
- `crf 23` is a good quality/size sweet spot for screen recordings; lower (18-20) for higher quality, higher (26-28) for smaller files
- `preset slow` spends more CPU during encoding for better compression
- `+faststart` moves the MP4 metadata to the front so the video can start playing before fully loaded
- `-an` strips any audio track

For typical Audacity screen recordings at 1518×1160 source, this lands files at 200–400 KB per clip.

## Embedding

In the reading HTML, each clip embeds inside the `.vocab` definition list as a `<figure class="vocab-video">` containing a `<video>` plus a row of speed-control buttons (0.5×, 1×, 2×). The buttons are wired up by a small script at the bottom of the reading. See `module-02-audio-editing-mixing/lessons/04-reading-editing-envelope.html` for the canonical pattern.
