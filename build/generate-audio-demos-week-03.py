"""
Generates audio demo files for the Module 2 Week 3 reading
on editing concepts and envelope.

Produces (12 files):

  Three contrasting envelopes (Section 1):
  - env-sharp.wav       : sharp attack, no sustain, fast release (woodblock-like)
  - env-sustained.wav   : slow attack, long sustain, gentle release (pad-like)
  - env-evolving.wav    : continuous filtered noise (wind/water-like)

  One source, four envelopes (Section 3):
  - edit-source.wav     : Karplus-Strong pluck, ~3 s, complete envelope
  - edit-truncated.wav  : same source cut hard at 0.5 s
  - edit-reversed.wav   : same source played backward
  - edit-fade-in.wav    : same source with a 1 s fade-in applied

  Edit boundary demo (Section 3):
  - seam-hardcut.wav    : two pad sounds joined with no fade (audible click)
  - seam-crossfade.wav  : same two sounds joined with a 200 ms crossfade

  Time-pitch coupling demo (Section 2, before time-stretch / pitch-shift):
  - tape-source.wav     : 440 Hz sine, 1.5 s (the source / 1x reference)
  - tape-slow.wav       : 220 Hz sine, 3.0 s (half-speed: longer + lower)
  - tape-fast.wav       : 880 Hz sine, 0.75 s (double-speed: shorter + higher)

Output: assets/audio/module-02-week-03/

Re-run with: python3 build/generate-audio-demos-week-03.py
"""

import os
import numpy as np
from scipy.io import wavfile
from scipy.signal import butter, sosfilt

# ----- Output paths -----

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUT_DIR = os.path.join(REPO_ROOT, "assets", "audio", "module-02-week-03")
os.makedirs(OUT_DIR, exist_ok=True)

SR = 44100


# ----- Helpers -----

def write_wav(path, audio, sr=SR, bit_depth=16, peak_dbfs=-3.0):
    """Normalize to peak_dbfs and write as 16-bit WAV."""
    audio = np.asarray(audio, dtype=np.float32)
    peak = np.max(np.abs(audio))
    if peak > 0:
        target = 10 ** (peak_dbfs / 20)
        audio = audio * (target / peak)
    if bit_depth == 16:
        audio_int = np.clip(audio * 32767, -32768, 32767).astype(np.int16)
    else:
        raise NotImplementedError("Only 16-bit supported here")
    wavfile.write(path, sr, audio_int)
    print(f"Wrote {path} ({len(audio)/sr:.2f} s)")


def apply_envelope(audio, attack_s, sustain_s, release_s, sr=SR):
    """
    Apply a piecewise linear ASR envelope to audio.
    Total duration = attack + sustain + release.
    The audio array should be at least that long; trailing samples are zeroed.
    """
    n_a = int(attack_s * sr)
    n_s = int(sustain_s * sr)
    n_r = int(release_s * sr)
    total = n_a + n_s + n_r
    env = np.concatenate([
        np.linspace(0, 1, n_a, dtype=np.float32),
        np.ones(n_s, dtype=np.float32),
        np.linspace(1, 0, n_r, dtype=np.float32),
    ])
    out = np.zeros(max(total, len(audio)), dtype=np.float32)
    out[:total] = audio[:total] * env
    return out[:total]


def apply_curved_envelope(audio, attack_s, sustain_s, release_s, curve=2.5, sr=SR):
    """
    Apply an ASR envelope with curved (power-law) attack and release.
    `curve > 1` produces an ease-in attack (slow start, faster finish) and
    a mirrored ease-out release. This sounds more like a natural swell than
    a linear ramp — the attack feels gradual rather than metronomic, and
    the release fades organically rather than sliding linearly to silence.
    """
    n_a = int(attack_s * sr)
    n_s = int(sustain_s * sr)
    n_r = int(release_s * sr)
    total = n_a + n_s + n_r

    attack = np.linspace(0, 1, n_a, dtype=np.float32) ** curve
    sustain = np.ones(n_s, dtype=np.float32)
    release = (np.linspace(1, 0, n_r, dtype=np.float32)) ** curve

    env = np.concatenate([attack, sustain, release])
    out = np.zeros(max(total, len(audio)), dtype=np.float32)
    out[:total] = audio[:total] * env
    return out[:total]


def lowpass_sos(cutoff_hz, sr=SR, order=4):
    return butter(order, cutoff_hz / (sr / 2), btype="low", output="sos")


# ----- Source syntheses -----

def karplus_strong_pluck(freq, duration_sec, sr=SR, decay=0.997, brightness=0.5, seed=42):
    """
    Karplus-Strong plucked string. Sharp attack, natural decay. Same algorithm
    as the Wk 2 demos for consistency.
    """
    rng = np.random.default_rng(seed)
    period = int(sr / freq)
    buffer = rng.uniform(-1, 1, period).astype(np.float32)
    buffer = (1 - brightness) * np.convolve(buffer, [0.5, 0.5], mode="same") + brightness * buffer
    n_samples = int(duration_sec * sr)
    output = np.zeros(n_samples, dtype=np.float32)
    for i in range(n_samples):
        output[i] = buffer[i % period]
        next_idx = (i + 1) % period
        buffer[i % period] = decay * 0.5 * (buffer[i % period] + buffer[next_idx])
    return output


def woodblock(duration_sec=0.4, sr=SR, seed=1):
    """
    Sharp percussive hit: filtered noise burst with very short envelope.
    Fast attack (~3 ms), no sustain, exponential decay.
    """
    rng = np.random.default_rng(seed)
    n = int(duration_sec * sr)
    noise = rng.normal(0, 0.5, n).astype(np.float32)
    # Bandpass-flavored filter for "wooden" tone: lowpass then a touch of
    # resonance via a simple comb-like structure. We'll use a single pole
    # lowpass at 2 kHz plus an exponential decay envelope.
    sos = lowpass_sos(2500, sr, order=2)
    filt = sosfilt(sos, noise).astype(np.float32)
    # Sharp exponential envelope: 3 ms attack, then exp decay.
    t = np.arange(n) / sr
    attack_n = int(0.003 * sr)
    env = np.zeros(n, dtype=np.float32)
    env[:attack_n] = np.linspace(0, 1, attack_n)
    env[attack_n:] = np.exp(-(t[attack_n:] - t[attack_n]) * 35)  # fast decay
    return filt * env


def slow_pad(duration_sec=5.5, freq=220.0, sr=SR):
    """
    Slow-attack sustained tone with a sine mixture and a curved ASR
    envelope. Total duration is split as 1.8 s attack + 2.0 s sustain
    + 1.5 s release = 5.3 s.

    The curved envelope (power=2.5) gives a clearly gradual swell at the
    start and a clearly gentle fade at the end — more exaggerated than the
    linear ramps used in the first draft, which felt more metronomic than
    organic. The pedagogical point is to contrast strongly with the
    woodblock (sharp attack, no sustain) and the evolving texture (no
    clear stages).
    """
    n = int(duration_sec * sr)
    t = np.arange(n) / sr
    # Mix sine + slight detuned sine (gives a fuller sound than pure sine)
    osc = (
        0.5 * np.sin(2 * np.pi * freq * t) +
        0.3 * np.sin(2 * np.pi * freq * 1.005 * t) +
        0.2 * np.sin(2 * np.pi * freq * 2 * t)  # one octave above
    ).astype(np.float32)
    # Gentle slow vibrato in amplitude for organic feel
    lfo = 1.0 + 0.04 * np.sin(2 * np.pi * 0.6 * t)
    osc = osc * lfo.astype(np.float32)
    # Apply curved ASR envelope: longer attack and release than the linear
    # version, with a power-law curve for a more natural swell.
    return apply_curved_envelope(osc, attack_s=1.8, sustain_s=2.0, release_s=1.5, curve=2.5, sr=sr)


def evolving_texture(duration_sec=4.5, sr=SR, seed=7):
    """
    Continuous filtered noise that evolves over time. The filter cutoff is
    modulated by a slow LFO, creating timbral motion within the texture.
    No clear ASR boundaries; the sound exists for its full duration.
    """
    rng = np.random.default_rng(seed)
    n = int(duration_sec * sr)
    noise = rng.normal(0, 0.4, n).astype(np.float32)
    # Slow filter modulation: cutoff sweeps between ~600 Hz and ~3500 Hz
    # over a ~6 s cycle. We approximate by processing in short blocks with
    # different filter cutoffs.
    block_size = 1024
    output = np.zeros(n, dtype=np.float32)
    n_blocks = n // block_size
    t_block = np.arange(n_blocks) * block_size / sr
    cutoffs = 600 + 1450 * (1 + np.sin(2 * np.pi * 0.16 * t_block))  # 600 .. 3500
    for i, cutoff in enumerate(cutoffs):
        start = i * block_size
        end = min(start + block_size, n)
        sos = lowpass_sos(cutoff, sr, order=4)
        output[start:end] = sosfilt(sos, noise[start:end]).astype(np.float32)
    # Gentle overall envelope so the start and end aren't abrupt
    fade_n = int(0.2 * sr)
    output[:fade_n] *= np.linspace(0, 1, fade_n)
    output[-fade_n:] *= np.linspace(1, 0, fade_n)
    return output


def sine_tone(freq, duration_sec, sr=SR, fade_s=0.005):
    """
    Pure sine tone with very short fade-in/fade-out (default 5 ms each)
    to prevent click pops at the start and end. Used for the tape-coupling
    demo where the visual is a clean sine and the audible result must be
    just-the-pitch with no envelope artifacts.
    """
    n = int(duration_sec * sr)
    t = np.arange(n) / sr
    out = np.sin(2 * np.pi * freq * t).astype(np.float32)
    fade_n = int(fade_s * sr)
    if fade_n > 0 and 2 * fade_n < n:
        out[:fade_n] *= np.linspace(0, 1, fade_n)
        out[-fade_n:] *= np.linspace(1, 0, fade_n)
    return out


# ----- Editing operations -----

def truncate(audio, duration_s, sr=SR):
    n = int(duration_s * sr)
    return audio[:n].copy()


def reverse(audio):
    return audio[::-1].copy()


def fade_in(audio, fade_s, sr=SR):
    n = int(fade_s * sr)
    out = audio.copy().astype(np.float32)
    n = min(n, len(out))
    out[:n] *= np.linspace(0, 1, n)
    return out


def hard_cut_join(audio_a, audio_b):
    """Concatenate two sounds with no fade — produces an audible click
    if waveform values don't match at the seam."""
    return np.concatenate([audio_a, audio_b]).astype(np.float32)


def crossfade_join(audio_a, audio_b, fade_s=0.2, sr=SR):
    """Join two sounds with a linear crossfade overlap."""
    n_fade = int(fade_s * sr)
    n_fade = min(n_fade, len(audio_a), len(audio_b))
    a = audio_a.astype(np.float32).copy()
    b = audio_b.astype(np.float32).copy()
    fade_out = np.linspace(1, 0, n_fade)
    fade_in_curve = np.linspace(0, 1, n_fade)
    a[-n_fade:] *= fade_out
    b[:n_fade] *= fade_in_curve
    out = np.zeros(len(a) + len(b) - n_fade, dtype=np.float32)
    out[:len(a)] += a
    out[len(a) - n_fade:] += b
    return out


# ----- Build all demos -----

def build():
    # Section 1: three contrasting envelopes
    write_wav(os.path.join(OUT_DIR, "env-sharp.wav"), woodblock(0.4))
    write_wav(os.path.join(OUT_DIR, "env-sustained.wav"), slow_pad(5.5, freq=220))
    write_wav(os.path.join(OUT_DIR, "env-evolving.wav"), evolving_texture(4.5))

    # Section 3: one source, four envelopes
    source = karplus_strong_pluck(freq=220.0, duration_sec=3.0, decay=0.997, brightness=0.4)
    write_wav(os.path.join(OUT_DIR, "edit-source.wav"), source)
    write_wav(os.path.join(OUT_DIR, "edit-truncated.wav"), truncate(source, 0.5))
    write_wav(os.path.join(OUT_DIR, "edit-reversed.wav"), reverse(source))
    write_wav(os.path.join(OUT_DIR, "edit-fade-in.wav"), fade_in(source, fade_s=1.0))

    # Edit boundary: two distinct sustained textures. We want the hard cut
    # to actually produce an audible discontinuity at the boundary.
    #
    # Pure synthesized tones tend to land at or near zero-crossings at clean
    # time intervals, which mutes the click. Filtered noise has guaranteed
    # non-zero values at any sample, so the boundary is reliably abrupt —
    # and it's also more representative of the kind of source material
    # students will actually work with in Project 1 (real-world recordings,
    # not pure tones).
    duration_s = 1.5
    n = int(duration_s * SR)
    rng_a = np.random.default_rng(11)
    rng_b = np.random.default_rng(22)

    # Texture A: noise filtered to a darker, lower-mid band (formant-ish around 400-800 Hz)
    noise_a = rng_a.normal(0, 0.7, n).astype(np.float32)
    sos_a = butter(4, [350 / (SR / 2), 900 / (SR / 2)], btype="band", output="sos")
    pad_a = sosfilt(sos_a, noise_a).astype(np.float32)

    # Texture B: noise filtered to a brighter, higher-mid band (1500-3000 Hz)
    noise_b = rng_b.normal(0, 0.7, n).astype(np.float32)
    sos_b = butter(4, [1500 / (SR / 2), 3000 / (SR / 2)], btype="band", output="sos")
    pad_b = sosfilt(sos_b, noise_b).astype(np.float32)

    # Apply small attack/release to the OUTSIDE of the joined sound only,
    # so the start and end aren't clicky. The seam is what we want to compare.
    fade_outer = int(0.05 * SR)
    pad_a[:fade_outer] *= np.linspace(0, 1, fade_outer)
    pad_b[-fade_outer:] *= np.linspace(1, 0, fade_outer)

    # Hard cut: just concatenate. Seam at the boundary.
    write_wav(os.path.join(OUT_DIR, "seam-hardcut.wav"), hard_cut_join(pad_a, pad_b))
    # Crossfade: 200 ms overlap.
    write_wav(os.path.join(OUT_DIR, "seam-crossfade.wav"), crossfade_join(pad_a, pad_b, fade_s=0.2))

    # Section 2: time-pitch coupling demo (the physical tape relationship).
    # Three sines: source, half-speed (lower + longer), double-speed (higher + shorter).
    # The visual in the reading shows a single waveform stretched / compressed; these
    # audio files give the audible counterpart. Peak gain reduced to -6 dBFS because
    # pure sines are fatiguing.
    write_wav(os.path.join(OUT_DIR, "tape-source.wav"), sine_tone(440.0, 1.5), peak_dbfs=-6.0)
    write_wav(os.path.join(OUT_DIR, "tape-slow.wav"),   sine_tone(220.0, 3.0), peak_dbfs=-6.0)
    write_wav(os.path.join(OUT_DIR, "tape-fast.wav"),   sine_tone(880.0, 0.75), peak_dbfs=-6.0)


if __name__ == "__main__":
    build()
    print("Done.")
