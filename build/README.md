# Build scripts

Internal scripts that generate assets for the course. Not student-facing.

## `generate-audio-demos.py`

Generates the audio demo files used in the Module 2 Week 2 reading
(`course/readings/module-02-week-02-digital-audio.html`). The reading
references these files in its embedded audio players for the in-text
sample rate and bit depth demonstrations.

### What it produces

Output directory: `assets/audio/module-02-week-02/`

| File | Sample rate | Bit depth | Purpose |
|---|---|---|---|
| `source-44k-16bit.wav` | 44.1 kHz | 16-bit | Reference source (CD quality) |
| `sr-8k-16bit.wav` | 44.1 kHz playback, 8 kHz bandwidth | 16-bit | Telephone-quality demo |
| `sr-4k-16bit.wav` | 44.1 kHz playback, 4 kHz bandwidth | 16-bit | Truly lo-fi demo |
| `bd-8bit-44k.wav` | 44.1 kHz | 8-bit (quantized) | Audible quantization noise |
| `bd-4bit-44k.wav` | 44.1 kHz | 4-bit (quantized) | Severely degraded |

All five files play at 44.1 kHz so they sound at the same speed in any
browser's `<audio>` element. The "sample rate" demos are bandwidth-
reduced to simulate what a low-sample-rate system would have captured;
the "bit depth" demos are quantized to fewer levels to expose
quantization noise.

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

## File naming convention

Build scripts use lowercase with hyphens, matching the rest of the
repo's naming convention. Output paths and file names within
`assets/audio/` follow the same convention: `module-XX-week-YY/` for
folders, `descriptive-shortname.ext` for files.
