# Build scripts and page templates

Internal scripts that generate assets for the course (audio demos, SVG diagrams), plus skeletal HTML page templates. Not student-facing.

## Page templates

See [`templates/`](./templates/README.md) for HTML skeletons used as starting points for new readings, tools, and lab handouts. Each template embodies the chrome and **Today's gear** callout conventions in `meta/chrome-conventions.md`.

## `generate-audio-demos.py`

Generates the audio demo files used in the Module 2 Week 2 reading
(`module-02-audio-editing-mixing/lessons/01-reading-digital-audio.html`). The reading
references these files in its embedded audio players for the in-text
sample rate and bit depth demonstrations.

### What it produces

Output directory: `assets/audio/module-02-week-02/`

| File | Sample rate | Bit depth | Purpose |
|---|---|---|---|
| `source-44k-16bit.wav` | 44.1 kHz | 16-bit | Reference source (CD quality) |
| `sr-8k-16bit.wav` | 44.1 kHz playback, 8 kHz bandwidth | 16-bit | Telephone-quality demo (anti-alias filtered) |
| `sr-4k-16bit.wav` | 44.1 kHz playback, 4 kHz bandwidth | 16-bit | Truly lo-fi demo (anti-alias filtered) |
| `bd-8bit-44k.wav` | 44.1 kHz | 8-bit (quantized) | Audible quantization noise |
| `bd-4bit-44k.wav` | 44.1 kHz | 4-bit (quantized) | Severely degraded |
| `alias-8k-no-filter.wav` | 44.1 kHz playback, 8 kHz bandwidth | 16-bit | Aliasing demo: same bandwidth as `sr-8k-16bit` but produced via naive decimation (no anti-alias filter), so high frequencies fold back as audible artifacts |

All six files play at 44.1 kHz so they sound at the same speed in any
browser's `<audio>` element. The "sample rate" demos are bandwidth-
reduced via proper polyphase filtering to simulate what a real ADC
captures at low rate; the "aliasing" demo skips the filter to expose
the artifact that anti-alias filters exist to prevent. The "bit
depth" demos are quantized to fewer levels to expose quantization
noise.

### The source sound

A ~7.5-second sequence of 4 plucked-string-like notes (A major
arpeggio: A3, C#4, E4, A4) using a Karplus-Strong-style synthesis
algorithm. Designed to demonstrate both kinds of degradation:

- **Sharp attacks** with high-frequency content reveal sample rate
  effects (sample rate degradation rolls off the highs)
- **Long natural decays into near-silence** reveal bit depth effects
  (quantization noise becomes audible during quiet passages)

### Re-running

To regenerate any of the audio files (e.g. if the source sound
should change, or if you want to add more degradation steps):

```
python3 build/generate-audio-demos.py
```

Requires `numpy` and `scipy`. The script is self-contained and idempotent —
running it always produces the same output (the random seed used in
the Karplus-Strong noise burst is not fixed, so each run produces
slightly different timbral content, but the structural properties are
the same).

If you want the exact same output every time, add a line near the top:

```python
np.random.seed(42)
```

### Why Python and not ChucK

The synthesis itself could absolutely be done in ChucK (and would
arguably be more idiomatic for this course). The reason this is in
Python: the *degradation* steps (sample rate reduction with proper
anti-aliasing, integer quantization for bit depth reduction) are
straightforward in scipy and awkward in ChucK. Keeping the whole
pipeline in one language and one script keeps the build simple.

The students never see this code — they just hear the resulting files
embedded in the reading.

## `generate-audio-demos-week-03.py`

Generates the audio demo files used in the Module 2 Week 3 reading
(`module-02-audio-editing-mixing/lessons/04-reading-editing-envelope.html`). Twelve
files in total, supporting four pedagogical moments in the reading.

### What it produces

Output directory: `assets/audio/module-02-week-03/`

**Three contrasting envelopes** (Section 1, the envelope concept):

| File | Synthesis | Purpose |
|---|---|---|
| `env-sharp.wav` | Filtered noise burst with very fast envelope | Sharp attack, no sustain, fast release (woodblock-like) |
| `env-sustained.wav` | Sine mixture with curved 1.8 s attack + 1.5 s release | Slow swell, long sustain, gentle decay (pad-like) |
| `env-evolving.wav` | Filtered noise with slow LFO on cutoff | Continuous texture with no clear ASR boundaries |

**One source, four envelopes** (Section 3, editing changes envelope):

| File | Operation | Purpose |
|---|---|---|
| `edit-source.wav` | Karplus-Strong pluck, 3 s, A3 | Reference: complete attack-sustain-release |
| `edit-truncated.wav` | Source cut hard at 0.5 s | Demonstrates: cutting off the release |
| `edit-reversed.wav` | Source played backward | Demonstrates: attack ↔ release swap |
| `edit-fade-in.wav` | Source with 1 s linear fade-in | Demonstrates: replacing a sharp attack with a slow one |

**Edit-boundary seam** (Section 3, click pops at hard cuts):

| File | Operation | Purpose |
|---|---|---|
| `seam-hardcut.wav` | Two band-passed noise textures concatenated | Audible click at the boundary |
| `seam-crossfade.wav` | Same two textures with 200 ms crossfade | No audible click |

**Time-pitch coupling** (Section 2, tape physics):

| File | Operation | Purpose |
|---|---|---|
| `tape-source.wav` | Voice recording from `assets/audio/source/voice-tape-demo.aif`, mono 44.1k | Reference: 1× speed, ~5.7 s |
| `tape-slow.wav` | Same source via `asetrate=33075,aresample=44100` | 0.75× speed, ~7.6 s, ~5 semitones lower |
| `tape-fast.wav` | Same source via `asetrate=58800,aresample=44100` | 1.33× speed, ~4.3 s, ~5 semitones higher |

The tape demos use ffmpeg's `asetrate` filter rather than DSP-based
time-stretch or pitch-shift. `asetrate` reinterprets the file's
sample rate without changing the sample data, which is mathematically
identical to what a tape machine does at non-standard playback speed:
duration and pitch shift together, by exactly the same ratio. This
preserves the pedagogical claim of the section (time and pitch are
*physically* coupled in this regime) — the demo doesn't cheat with
modern processing.

### Re-running

```
python3 build/generate-audio-demos-week-03.py
```

Requires `numpy`, `scipy`, and `ffmpeg` (the latter for the tape
demos). The voice source must be present at
`assets/audio/source/voice-tape-demo.aif`; if it's missing, the
script prints a warning and skips the tape demos but still rebuilds
the other 9 files.

The Karplus-Strong source used in the editing demos uses a fixed
random seed (42), so output is deterministic across runs.

## `generate-audio-demos-week-05.py`

Generates the audio demo files used in the Module 2 Week 5 reading
(`module-02-audio-editing-mixing/lessons/07-reading-dynamics.html`)
and the source for the dynamics tool's embedded demo
(`module-02-audio-editing-mixing/lessons/08-tool-mixing-dynamics.html`).
Nineteen files in total, supporting the four main pedagogical moments
in the reading (dynamic range, threshold + ratio, attack + release,
limiting / loudness-wars) plus three smaller supplements (normalization
contrast, timbre A/B, dynamics-tool demo source).

### What it produces

Output directory: `assets/audio/module-02-week-05/`

- `range-wide.wav`, `range-narrow.wav` — Section 1 (dynamic range)
- `tr-source.wav`, `tr-light.wav`, `tr-medium.wav`, `tr-heavy.wav` — Section 2 (threshold + ratio)
- `ar-source.wav`, `ar-fast-attack.wav`, `ar-slow-attack.wav`,
  `ar-fast-release.wav`, `ar-slow-release.wav` — Section 3 (attack + release)
- `limit-natural.wav`, `limit-light.wav`, `limit-crushed.wav` — Section 4 (limiting / loudness wars)
- `norm-quiet.wav`, `norm-loud.wav` — Section 2 supplement (normalization contrast: same shape, different peak; pairs with the wide/narrow demo to land the "scale vs. shape" distinction)
- `timbre-scaled.wav`, `timbre-compressed.wav` — Section 2 supplement (timbre A/B at matched loudness: a scaled-only vs. compressed-then-makeup version, both peak-matched, so students can hear how compression changes the *sound* once the loudness illusion is removed)
- `dynamic-tool-demo.wav` — source audio for the dynamics tool's built-in demo button (`08-tool-mixing-dynamics.html`). The tool embeds this file as base64 inside the HTML; see `embed-tool-demo.py` below for the re-embed step.

### Implementation notes

The compressor is a feed-forward digital compressor with a one-pole
peak detector and a 2 dB soft knee. Gain is computed in the log domain
and applied as a linear multiplier. Attack and release use exponential
time constants of the form `exp(-1/(t*sr))`.

Sections 1 and 4 (dynamic-range and limiter demos) use a real
Ableton-rendered stereo loop as source material: conga slaps at
maximum velocity, shaker and clave at low velocity. The natural
dynamic range of the loop (~21 dB crest factor, ~57 dB spread between
loudest and quietest 100 ms windows) makes the compression-vs-no
demonstrations land much more clearly than any synthesized source.
The loop lives at `assets/audio/source/dynamic-loop.wav`. These two
sections use stereo-linked compression (`compress_stereo`,
`limit_stereo`): a single sidechain detector reads `max(|L|, |R|)` so
both channels are reduced equally and the stereo image stays stable.

Sections 2 and 3 use synthesized mono sources, because they need
precise level control across multiple hits (Section 2's six varied-level
hits) and precise transient timing (Section 3's percussion loop) that
are easier to guarantee from code than from a recorded source.

Makeup gain is deliberately **not** applied to the Section 2 and 3
compression demos — every demo in those sections is normalized to a
peak of -3 dBFS at write time, so the audible squashing reflects actual
compression, not the loudness illusion of automatic makeup. The
dynamic-range pair (Section 1) and the limiter trio (Section 4) are
written without normalization so students can hear the loudness-wars
effect: peak levels are matched within each comparison set, but
perceived loudness rises dramatically (and audibly) with the
compression amount.

The peak limiter has no lookahead, so fast transients can punch through
the ceiling by a couple of dB. A final hard-clip pass at the ceiling
enforces the peak exactly, so the peak meter reads identically across
files within a comparison set.

The narrow-version boost in `gen_dynamic_range` is calibrated for the
specific source loop (currently `NARROW_BOOST_DB = 18` for ~6 dB RMS
gap). If you change the source, sweep this value to recalibrate.

## `embed-tool-demo.py`

Re-embeds the dynamics tool's demo audio as base64 inside
`module-02-audio-editing-mixing/lessons/08-tool-mixing-dynamics.html`.
Run this after regenerating `dynamic-tool-demo.wav` if the embedded
copy should reflect the new audio.

### Why the tool has an embedded copy

Browsers block `fetch()` across origins under the `file://` protocol,
so fetching a sibling WAV from the tool's HTML fails when the page is
opened by double-clicking. Embedding the WAV inside the HTML sidesteps
that entirely. The trade-off is the HTML file grows from ~30 KB to
~1.4 MB, which is fine for a teaching tool loaded once per session.

The script reads the canonical WAV from
`assets/audio/module-02-week-05/dynamic-tool-demo.wav`, base64-encodes
it, and replaces the contents of the
`<script type="application/octet-stream" id="demo-audio-b64">` block
inside the tool HTML with the fresh data. No other parts of the tool
are touched.

### Re-running

```
python3 build/embed-tool-demo.py
```

Standard library only — no extra dependencies. Idempotent.

## File naming convention

Build scripts use lowercase with hyphens, matching the rest of the
repo's naming convention. Output paths and file names within
`assets/audio/` follow the same convention: `module-XX-week-YY/` for
folders, `descriptive-shortname.ext` for files.
