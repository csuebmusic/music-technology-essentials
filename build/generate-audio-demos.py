"""
Generates audio demo files for the Module 2 Week 2 digital audio reading.

Produces:
  - source-44k-16bit.wav     : reference source at CD quality
  - sr-8k-16bit.wav          : 8 kHz sample rate (telephone quality), 16-bit
  - sr-4k-16bit.wav          : 4 kHz sample rate (truly lo-fi), 16-bit
  - bd-8bit-44k.wav          : 8-bit, 44.1 kHz (audible quantization noise)
  - bd-4bit-44k.wav          : 4-bit, 44.1 kHz (severely degraded)

The source is a 4-note plucked-string sequence (Karplus-Strong-like),
designed to have:
  - sharp attacks (high frequency content for sample rate demo)
  - long decays into near-silence (reveals quantization noise at low bit depth)
  - some musical interest

Output: assets/audio/module-02-week-02/

Re-run with: python3 build/generate-audio-demos.py
"""

import os
import numpy as np
from scipy.io import wavfile
from scipy.signal import resample_poly

# ----- Output paths -----

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUT_DIR = os.path.join(REPO_ROOT, "assets", "audio", "module-02-week-02")
os.makedirs(OUT_DIR, exist_ok=True)


# ----- Source synthesis -----

SR = 44100  # source sample rate

def karplus_strong_pluck(freq, duration_sec, sr=SR, decay=0.997, brightness=0.5):
    """
    Karplus-Strong plucked string: sharp attack, natural decay.
    `decay` is the per-sample feedback coefficient (closer to 1 = longer sustain).
    `brightness` mixes in some white noise for bite (0 = pure tone, 1 = noisy).
    """
    period = int(sr / freq)
    # Initialize with noise burst (the "pluck")
    buffer = np.random.uniform(-1, 1, period).astype(np.float32)
    # Smooth slightly by tone control
    buffer = (1 - brightness) * (np.convolve(buffer, [0.5, 0.5], mode="same")) + brightness * buffer

    n_samples = int(duration_sec * sr)
    output = np.zeros(n_samples, dtype=np.float32)
    for i in range(n_samples):
        output[i] = buffer[i % period]
        # Update buffer: average current and next (low-pass), apply decay
        next_idx = (i + 1) % period
        buffer[i % period] = decay * 0.5 * (buffer[i % period] + buffer[next_idx])
    return output


def build_source():
    """
    Build a ~3 second pluck sequence: 4 notes in quick succession, with the
    last one held into a brief decay tail.

    Total duration is deliberately short. At low bit depths, quiet samples
    round down to zero — the natural Karplus-Strong decay floors out into
    pure silence around 2.3 seconds at 4-bit. A longer file would have
    several seconds of dead air at low bit depths, which sounds broken
    rather than pedagogically illuminating. By keeping the file to ~3
    seconds, we give the 4-bit version time to demonstrate its loud
    quantization noise, then trail naturally into a short silence at the
    end. The 16-bit and 8-bit versions still demonstrate full decay within
    the same window.
    """
    sr = SR
    sequence = np.zeros(int(3.0 * sr), dtype=np.float32)

    # Notes: A3, C#4, E4, A4 (an A major arpeggio): bright but resolved.
    # Tightly spaced so all 4 attacks land in the first second.
    notes = [
        (220.00, 0.0),    # A3 at 0.0s
        (277.18, 0.25),   # C#4 at 0.25s
        (329.63, 0.5),    # E4 at 0.5s
        (440.00, 0.75),   # A4 at 0.75s, held longest
    ]

    for freq, start_sec in notes:
        # Each note rings for ~2.5 seconds; decay overlaps with later notes
        pluck = karplus_strong_pluck(freq, duration_sec=2.5, decay=0.998, brightness=0.4)
        start_idx = int(start_sec * sr)
        end_idx = start_idx + len(pluck)
        if end_idx > len(sequence):
            pluck = pluck[: len(sequence) - start_idx]
            end_idx = len(sequence)
        sequence[start_idx:end_idx] += pluck

    # Normalize to about -3 dBFS so we have a touch of headroom but plenty of signal
    peak = np.max(np.abs(sequence))
    if peak > 0:
        sequence = sequence * (0.707 / peak)  # -3 dBFS

    return sequence


# ----- Format conversions -----

def to_int16(audio_float):
    """
    Convert -1..1 float32 to int16. Includes defensive clipping at slightly
    less than full scale (0.999) so that if any upstream processing pushes
    samples to exactly ±1.0, the int16 conversion doesn't quantize awkwardly
    at the boundary.
    """
    clipped = np.clip(audio_float, -0.999, 0.999)
    return (clipped * 32767).astype(np.int16)


def reduce_bit_depth(audio_float, target_bits, headroom_db=-3.0):
    """
    Reduce bit depth by quantizing to fewer levels. Returns float32 audio
    with quantization grid imposed; we'll save as 16-bit so it can be
    played in browsers, but the quantization is what makes it sound
    degraded.

    `headroom_db` lowers the signal before quantization to prevent the
    rounding from pushing values past full scale. At low bit depths this
    matters a lot: 4-bit has step size of 1/8, which means a peak sample
    can round upward by up to 1/16 of full scale. Without headroom,
    samples already near 0 dBFS will be pushed past it and clip when
    converted to int16. Real-world bit depth reduction (in DAWs, mastering
    chains) always leaves headroom before quantization for this reason.
    """
    # Apply headroom: scale down by `headroom_db` worth of attenuation
    headroom_linear = 10 ** (headroom_db / 20.0)
    audio_attenuated = audio_float * headroom_linear

    # Quantize to (target_bits) bits, then map back to full-scale float
    levels = 2 ** target_bits
    half_levels = levels // 2
    quantized = np.round(audio_attenuated * (half_levels - 1)) / (half_levels - 1)

    return quantized.astype(np.float32)


def downsample(audio_float, source_sr, target_sr):
    """
    Downsample using polyphase filtering. This is the right way: a low-pass
    filter is applied to prevent aliasing before decimation. Real ADCs do this.
    Returns audio at target_sr.
    """
    # Use resample_poly with up=target, down=source (in lowest terms)
    from math import gcd
    g = gcd(source_sr, target_sr)
    up = target_sr // g
    down = source_sr // g
    return resample_poly(audio_float, up, down)


def downsample_then_back(audio_float, source_sr, intermediate_sr):
    """
    Simulate "this would have sounded like at lower sample rate" by
    downsampling then upsampling back to source_sr. Result has the
    bandwidth of intermediate_sr but plays at source_sr (which is what
    every browser's HTML5 audio expects).
    """
    downsampled = downsample(audio_float, source_sr, intermediate_sr)
    upsampled = downsample(downsampled, intermediate_sr, source_sr)
    # Pad/trim to match original length
    if len(upsampled) < len(audio_float):
        upsampled = np.pad(upsampled, (0, len(audio_float) - len(upsampled)))
    else:
        upsampled = upsampled[: len(audio_float)]
    return upsampled


def downsample_naive_then_back(audio_float, source_sr, intermediate_sr):
    """
    Demonstration of aliasing: downsample WITHOUT an anti-alias filter,
    then upsample back. Result contains audible aliasing artifacts —
    high-frequency content above the intermediate Nyquist folds back as
    false lower frequencies. This is what would happen if you skipped
    the filter that real ADCs always include.

    We do this by simple decimation (taking every Nth sample) rather
    than scipy's polyphase resampler, which includes proper filtering.
    Then we upsample back via zero-order hold (sample-and-hold) so the
    result plays at source_sr without smoothing the artifact away.
    """
    # Naive decimation: take every Nth sample, no filter
    decimation = source_sr // intermediate_sr
    decimated = audio_float[::decimation]

    # Naive upsampling via zero-order hold: each sample held for `decimation` samples
    upsampled = np.repeat(decimated, decimation)

    # Match original length
    if len(upsampled) < len(audio_float):
        upsampled = np.pad(upsampled, (0, len(audio_float) - len(upsampled)))
    else:
        upsampled = upsampled[: len(audio_float)]
    return upsampled


# ----- Build everything -----

def main():
    print("Generating source audio...")
    source = build_source()
    duration_sec = len(source) / SR
    print(f"  Source: {duration_sec:.2f} seconds at {SR} Hz")

    # 1. Source: 44.1k / 16-bit reference
    out_path = os.path.join(OUT_DIR, "source-44k-16bit.wav")
    wavfile.write(out_path, SR, to_int16(source))
    print(f"  → {out_path}")

    # 2. Sample rate demos: keep 16-bit, vary sample rate
    # We downsample then upsample back to 44.1k so browsers play them at the same speed
    for target_sr, label in [(8000, "8k"), (4000, "4k")]:
        degraded = downsample_then_back(source, SR, target_sr)
        out_path = os.path.join(OUT_DIR, f"sr-{label}-16bit.wav")
        wavfile.write(out_path, SR, to_int16(degraded))
        print(f"  → {out_path}")

    # 3. Bit depth demos: keep 44.1k, vary bit depth
    for target_bits, label in [(8, "8bit"), (4, "4bit")]:
        degraded = reduce_bit_depth(source, target_bits)
        out_path = os.path.join(OUT_DIR, f"bd-{label}-44k.wav")
        wavfile.write(out_path, SR, to_int16(degraded))
        print(f"  → {out_path}")

    # 4. Aliasing demo: same source, downsampled to 8k WITHOUT anti-alias
    # filtering. The resulting file has audible aliasing where high-frequency
    # content folds back into the audible range as false lower frequencies.
    # This is the artifact every digital audio system is designed to prevent.
    aliased = downsample_naive_then_back(source, SR, 8000)
    out_path = os.path.join(OUT_DIR, "alias-8k-no-filter.wav")
    wavfile.write(out_path, SR, to_int16(aliased))
    print(f"  → {out_path}")

    print("\nDone. Files in assets/audio/module-02-week-02/")


if __name__ == "__main__":
    main()
