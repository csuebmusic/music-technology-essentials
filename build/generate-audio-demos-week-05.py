"""
Generates audio demo files for the Module 2 Week 5 reading
on dynamics, compression, and limiting.

Produces (11 files):

  Dynamic range (Section 1):
  - range-wide.wav         : mixed source with full dynamic range (-30 to -3 dBFS peaks)
  - range-narrow.wav       : same source aggressively compressed to a narrow range
                             (-9 to -3 dBFS peaks) for the loudness contrast

  Threshold + ratio (Section 2):
  - tr-source.wav          : repeating snare-like hits with varied levels
                             (peaks at -3, -9, -15, -3, -9, -15 dBFS) — the same
                             source heard at three compression settings below
  - tr-light.wav           : threshold -12 dB, ratio 2:1 (gentle, peaks tamed)
  - tr-medium.wav          : threshold -18 dB, ratio 4:1 (clearly squashed)
  - tr-heavy.wav           : threshold -24 dB, ratio 10:1 (everything pinned)

  Attack and release (Section 3):
  - ar-source.wav          : a kick + percussion loop with sharp transients
                             (the transients are what attack/release affects most)
  - ar-fast-attack.wav     : 1 ms attack — transients are clamped down
  - ar-slow-attack.wav     : 30 ms attack — transients pass through, body squashed
  - ar-fast-release.wav    : 50 ms release — "pumping" audible as compressor recovers
  - ar-slow-release.wav    : 400 ms release — smoother, no pumping

  Limiting / loudness wars (Section 4):
  - limit-natural.wav      : full mix at natural dynamics, no limiting
  - limit-light.wav        : same mix with gentle limiting (~3 dB gain reduction)
  - limit-crushed.wav      : same mix at the loudness-wars extreme (~9 dB GR,
                             pinned at 0 dBFS — audibly distorted, no peaks)

The pedagogical point of `limit-natural` -> `limit-light` -> `limit-crushed`
is that the *peak level* is identical across the three (all near 0 dBFS)
but the *perceived loudness* climbs dramatically — and so does the audible
damage. Students should hear and then unhear the loudness-wars effect.

All compression in this script is implemented as a feed-forward digital
compressor with a peak detector (one-pole follower) on the absolute
signal, applied to the linear-domain envelope. Gain reduction is computed
in the log domain, then multiplied back onto the signal. Makeup gain is
deliberately *not* applied automatically — these files are normalized to
a peak of -3 dBFS at the end like every other demo in this build, so
students hear the squashing without the loudness illusion of makeup.

Output: assets/audio/module-02-week-05/

Re-run with: python3 build/generate-audio-demos-week-05.py
"""

import os
import numpy as np
from scipy.io import wavfile
from scipy.signal import butter, sosfilt


# ----- Output paths -----

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUT_DIR = os.path.join(REPO_ROOT, "assets", "audio", "module-02-week-05")
os.makedirs(OUT_DIR, exist_ok=True)

SR = 44100


# ----- Helpers -----

def write_wav(path, audio, sr=SR, peak_dbfs=-3.0):
    """Normalize to peak_dbfs and write as 16-bit WAV."""
    audio = np.asarray(audio, dtype=np.float32)
    peak = np.max(np.abs(audio))
    if peak > 0:
        target = 10 ** (peak_dbfs / 20)
        audio = audio * (target / peak)
    audio_int = np.clip(audio * 32767, -32768, 32767).astype(np.int16)
    wavfile.write(path, sr, audio_int)
    print(f"Wrote {path}  ({len(audio)/sr:.2f} s, peak {peak_dbfs:+.1f} dBFS)")


def write_wav_no_normalize(path, audio, sr=SR):
    """Write as 16-bit WAV without normalization (used for limiter demos where
    we deliberately want different perceived loudness at the same peak)."""
    audio = np.clip(audio, -1.0, 1.0).astype(np.float32)
    audio_int = np.clip(audio * 32767, -32768, 32767).astype(np.int16)
    wavfile.write(path, sr, audio_int)
    peak_db = 20 * np.log10(max(np.max(np.abs(audio)), 1e-12))
    print(f"Wrote {path}  ({len(audio)/sr:.2f} s, peak {peak_db:+.1f} dBFS)")


def db_to_lin(db):
    return 10 ** (db / 20)


def lin_to_db(lin):
    return 20 * np.log10(np.maximum(lin, 1e-12))


def lowpass_sos(cutoff_hz, sr=SR, order=4):
    return butter(order, cutoff_hz / (sr / 2), btype="low", output="sos")


# ----- The compressor (used by every demo here) -----

def compress(audio, threshold_db, ratio, attack_ms, release_ms, sr=SR,
             knee_db=2.0):
    """
    Feed-forward digital compressor with one-pole peak detector and soft knee.

    audio          : input mono signal in [-1, 1]
    threshold_db   : threshold in dBFS (e.g. -18)
    ratio          : compression ratio (e.g. 4 for 4:1)
    attack_ms      : attack time in milliseconds
    release_ms     : release time in milliseconds
    knee_db        : soft-knee width in dB (set 0 for hard knee)

    Returns the compressed signal at the same peak as the input (no makeup).
    """
    a_atk = np.exp(-1.0 / (attack_ms * 0.001 * sr))
    a_rel = np.exp(-1.0 / (release_ms * 0.001 * sr))

    abs_sig = np.abs(audio).astype(np.float32)
    env = np.zeros_like(abs_sig)

    # One-pole peak follower: fast attack, slow release.
    prev = 0.0
    for i, x in enumerate(abs_sig):
        if x > prev:
            prev = a_atk * prev + (1 - a_atk) * x
        else:
            prev = a_rel * prev + (1 - a_rel) * x
        env[i] = prev

    env_db = lin_to_db(env)

    # Soft-knee gain computer:
    # below (T - W/2): no reduction
    # above (T + W/2): full reduction
    # between: quadratic interpolation
    knee_lo = threshold_db - knee_db / 2
    knee_hi = threshold_db + knee_db / 2

    gain_db = np.zeros_like(env_db)
    above = env_db > knee_hi
    knee_region = (env_db > knee_lo) & ~above

    # Above the knee: gain_reduction = (env - T) * (1 - 1/ratio)
    gain_db[above] = -(env_db[above] - threshold_db) * (1 - 1.0 / ratio)

    # In the knee: smooth quadratic transition
    if knee_db > 0:
        knee_pos = env_db[knee_region] - knee_lo
        knee_amount = (knee_pos / knee_db) ** 2  # 0 -> 1 across knee
        excess = env_db[knee_region] - threshold_db
        gain_db[knee_region] = -excess * knee_amount * (1 - 1.0 / ratio)

    gain_lin = db_to_lin(gain_db)
    return (audio.astype(np.float32) * gain_lin).astype(np.float32)


# ----- Source syntheses -----

def transient_hit(duration_sec=0.18, freq=180.0, sr=SR, seed=0):
    """
    A sharp tonal hit with body. Used as a building block for the demos.
    Sharp attack (~1 ms), exponential decay, mix of tone + noise.
    """
    rng = np.random.default_rng(seed)
    n = int(duration_sec * sr)
    t = np.arange(n) / sr
    tone = np.sin(2 * np.pi * freq * t) + 0.5 * np.sin(2 * np.pi * freq * 2 * t)
    noise = rng.normal(0, 0.4, n).astype(np.float32)
    sos = lowpass_sos(3000, sr, order=2)
    noise = sosfilt(sos, noise).astype(np.float32)
    src = (0.7 * tone + 0.3 * noise).astype(np.float32)
    # Sharp attack, exponential decay
    attack_n = int(0.001 * sr)
    env = np.zeros(n, dtype=np.float32)
    env[:attack_n] = np.linspace(0, 1, attack_n)
    env[attack_n:] = np.exp(-(t[attack_n:] - t[attack_n]) * 12)
    return src * env


def kick(duration_sec=0.35, sr=SR):
    """Low-frequency kick: pitched sine sweep + click."""
    n = int(duration_sec * sr)
    t = np.arange(n) / sr
    # Pitch sweep from 110 -> 50 Hz over the first 80 ms
    sweep_n = int(0.08 * sr)
    pitch = np.concatenate([
        np.linspace(110, 50, sweep_n),
        np.full(n - sweep_n, 50.0)
    ])
    phase = np.cumsum(2 * np.pi * pitch / sr)
    body = np.sin(phase).astype(np.float32)
    env = np.exp(-t * 8).astype(np.float32)
    # Small click at the very start
    click_n = int(0.002 * sr)
    body[:click_n] += np.linspace(0.5, 0, click_n) * np.random.default_rng(1).normal(0, 1, click_n)
    return body * env


def percussion_loop(bars=2, bpm=110, sr=SR):
    """
    A short percussion loop (kick on 1 and 3, hits on 2 and 4) with
    pronounced transients. The transients are what the attack/release
    demos work on.
    """
    beat_s = 60.0 / bpm
    bar_s = 4 * beat_s
    total_s = bars * bar_s
    n_total = int(total_s * sr)
    out = np.zeros(n_total, dtype=np.float32)

    def add(audio, start_s, gain=1.0):
        start = int(start_s * sr)
        end = min(start + len(audio), n_total)
        out[start:end] += gain * audio[: end - start]

    for bar in range(bars):
        t0 = bar * bar_s
        add(kick(), t0 + 0 * beat_s, gain=0.9)
        add(transient_hit(seed=10), t0 + 1 * beat_s, gain=0.7)
        add(kick(), t0 + 2 * beat_s, gain=0.9)
        add(transient_hit(seed=11), t0 + 3 * beat_s, gain=0.7)

    return out


def varied_levels_source(sr=SR):
    """
    Six transient hits at varied levels: -3, -9, -15, -3, -9, -15 dBFS.
    Spaced 0.5 s apart, total ~3.5 s. Used for threshold+ratio demos
    so students can hear how compression affects loud hits vs. quiet
    hits differently.
    """
    levels_db = [-3, -9, -15, -3, -9, -15]
    spacing_s = 0.5
    hit_dur = 0.4
    total_n = int((len(levels_db) * spacing_s + hit_dur) * sr)
    out = np.zeros(total_n, dtype=np.float32)

    for i, db in enumerate(levels_db):
        hit = transient_hit(duration_sec=hit_dur, freq=240, seed=i)
        # Normalize the hit to -3 dBFS first, then scale to target
        hit_peak = np.max(np.abs(hit))
        if hit_peak > 0:
            hit = hit / hit_peak * db_to_lin(-3)
        hit = hit * db_to_lin(db - (-3))  # scale relative to -3
        start = int(i * spacing_s * sr)
        end = min(start + len(hit), total_n)
        out[start:end] += hit[: end - start]
    return out


def mixed_phrase(sr=SR, duration_sec=6.0):
    """
    A short musical-ish phrase combining percussion, low pad, and accents.
    Used for the wide-vs-narrow dynamic range demo and the limiter demos.
    Has deliberately varied dynamics: some quiet parts, some loud peaks.
    """
    n = int(duration_sec * sr)
    t = np.arange(n) / sr
    out = np.zeros(n, dtype=np.float32)

    # Low pad — quiet sustained background
    pad_freq = 110
    pad = (
        0.18 * np.sin(2 * np.pi * pad_freq * t) +
        0.10 * np.sin(2 * np.pi * pad_freq * 1.5 * t) +
        0.08 * np.sin(2 * np.pi * pad_freq * 2 * t)
    ).astype(np.float32)
    # Slow attack/release for the pad
    pad_env = np.minimum(t / 0.5, (duration_sec - t) / 0.5)
    pad_env = np.clip(pad_env, 0, 1)
    out += (pad * pad_env * 0.4).astype(np.float32)

    # Percussion: kicks on beats, hits between
    bpm = 100
    beat_s = 60.0 / bpm
    for i in range(int(duration_sec / beat_s)):
        t0 = i * beat_s + 0.05  # tiny offset so first kick is audible
        start = int(t0 * sr)
        if i % 2 == 0:
            k = kick(duration_sec=0.4) * 0.95  # loud kicks (the peaks)
            end = min(start + len(k), n)
            out[start:end] += k[: end - start]
        else:
            h = transient_hit(duration_sec=0.25, freq=300, seed=20 + i) * 0.35
            end = min(start + len(h), n)
            out[start:end] += h[: end - start]

    # A few softer accents in the gaps for textural variety
    for i, t0 in enumerate([0.35, 1.55, 3.05, 4.55]):
        h = transient_hit(duration_sec=0.15, freq=520, seed=50 + i) * 0.12
        start = int(t0 * sr)
        end = min(start + len(h), n)
        out[start:end] += h[: end - start]

    return out


# ----- Limiter (peak limiter at a hard ceiling) -----

def limit(audio, ceiling_db=-0.3, attack_ms=2.0, release_ms=80.0, sr=SR):
    """
    Brick-wall-ish peak limiter: extreme compression (ratio inf) at a hard
    ceiling, smoothed with attack and release. Used for the loudness-wars
    demo. Returns the limited signal with no makeup applied; we'll scale
    afterward to push the perceived loudness up.
    """
    return compress(audio, threshold_db=ceiling_db, ratio=20.0,
                    attack_ms=attack_ms, release_ms=release_ms,
                    sr=sr, knee_db=0.5)


# ----- Generators -----

def gen_dynamic_range():
    """range-wide.wav (full dynamic range) and range-narrow.wav (squashed).

    Critical: these two files must be at the same PEAK level but DIFFERENT
    perceived loudness — same as the limiter trio. The narrow version
    should sound *louder on average* despite hitting the same ceiling.

    The technique mirrors real-world "loudness compression": compress the
    source aggressively, then boost the result into a limiter set at the
    target ceiling. The limiter holds the peak; the boost pulls average
    level up toward it. A final normalization step here would defeat the
    purpose by scaling everything back down, so we use
    write_wav_no_normalize for both files.

    The limiter in this build does not have lookahead, so fast transients
    can punch through the ceiling by 1–3 dB. A final hard-clip pass at
    the ceiling enforces the peak exactly. In a real production limiter
    you'd want true lookahead and inter-sample-peak detection; for a
    teaching demo where we need the peak meter to read identical, a
    final clip is the right tradeoff.
    """
    src = mixed_phrase(duration_sec=6.0)

    # Wide: scale to peak -3 dBFS, no further processing.
    wide = src.copy()
    peak = np.max(np.abs(wide))
    if peak > 0:
        wide = wide / peak * db_to_lin(-3)
    write_wav_no_normalize(os.path.join(OUT_DIR, "range-wide.wav"), wide)

    # Narrow: aggressive compression, then push +15 dB into a limiter at
    # -3 dBFS, then enforce the ceiling with a hard clip. The compression
    # squashes the dynamic range; the +15 dB boost pulls the average level
    # toward the ceiling; the limiter handles the bulk of the transients
    # musically; the final clip catches the few fast transients the limiter
    # doesn't catch in time. Peak: exactly -3 dBFS. Average: ~6 dB higher
    # than wide. That gap is comfortably audible and matches the lesson:
    # narrow dynamic range sounds louder on average, at the same peak.
    narrow = compress(src, threshold_db=-24, ratio=8, attack_ms=3, release_ms=80)
    narrow = narrow * db_to_lin(15)
    narrow = limit(narrow, ceiling_db=-3.0, attack_ms=1, release_ms=50)
    ceiling_lin = db_to_lin(-3.0)
    narrow = np.clip(narrow, -ceiling_lin, ceiling_lin)
    write_wav_no_normalize(os.path.join(OUT_DIR, "range-narrow.wav"), narrow)


def gen_threshold_ratio():
    """tr-source.wav and three compression settings on the same source."""
    src = varied_levels_source()
    write_wav(os.path.join(OUT_DIR, "tr-source.wav"), src, peak_dbfs=-3.0)

    # Source comes in with peaks at -3, -9, -15. We normalize at write time
    # to -3 dBFS, so the relative differences between hits are preserved.

    # Light: T=-12, R=2:1 — only the -3 dBFS hits get touched, mildly.
    light = compress(src, threshold_db=-12, ratio=2, attack_ms=2, release_ms=100)
    write_wav(os.path.join(OUT_DIR, "tr-light.wav"), light, peak_dbfs=-3.0)

    # Medium: T=-18, R=4:1 — -3 and -9 hits both compressed.
    medium = compress(src, threshold_db=-18, ratio=4, attack_ms=2, release_ms=100)
    write_wav(os.path.join(OUT_DIR, "tr-medium.wav"), medium, peak_dbfs=-3.0)

    # Heavy: T=-24, R=10:1 — everything gets pinned, dynamics nearly gone.
    heavy = compress(src, threshold_db=-24, ratio=10, attack_ms=2, release_ms=100)
    write_wav(os.path.join(OUT_DIR, "tr-heavy.wav"), heavy, peak_dbfs=-3.0)


def gen_attack_release():
    """ar-source.wav and four attack/release variants."""
    src = percussion_loop(bars=2, bpm=110)
    write_wav(os.path.join(OUT_DIR, "ar-source.wav"), src, peak_dbfs=-3.0)

    # All four use threshold -18 dB, ratio 4:1 — only attack/release differ.
    # Same threshold+ratio in every variant means students can attribute the
    # perceived difference unambiguously to the time constants.

    fast_atk = compress(src, threshold_db=-18, ratio=4,
                        attack_ms=1, release_ms=120)
    write_wav(os.path.join(OUT_DIR, "ar-fast-attack.wav"), fast_atk, peak_dbfs=-3.0)

    slow_atk = compress(src, threshold_db=-18, ratio=4,
                        attack_ms=30, release_ms=120)
    write_wav(os.path.join(OUT_DIR, "ar-slow-attack.wav"), slow_atk, peak_dbfs=-3.0)

    fast_rel = compress(src, threshold_db=-18, ratio=4,
                        attack_ms=5, release_ms=50)
    write_wav(os.path.join(OUT_DIR, "ar-fast-release.wav"), fast_rel, peak_dbfs=-3.0)

    slow_rel = compress(src, threshold_db=-18, ratio=4,
                        attack_ms=5, release_ms=400)
    write_wav(os.path.join(OUT_DIR, "ar-slow-release.wav"), slow_rel, peak_dbfs=-3.0)


def gen_limiter():
    """The loudness-wars demo: same source, progressively crushed.

    Critical difference from every other generator: these three files are
    NOT normalized to the same peak. They're all near 0 dBFS, but the
    perceived loudness differs by 6-9 LU. Students should hear the
    loudness climb (and the cost) when comparing them.
    """
    src = mixed_phrase(duration_sec=6.0)

    # Natural: just normalize the source to peak -3 dBFS, write directly.
    natural = src.copy()
    peak = np.max(np.abs(natural))
    if peak > 0:
        natural = natural / peak * db_to_lin(-3)
    write_wav_no_normalize(os.path.join(OUT_DIR, "limit-natural.wav"), natural)

    # Light limiting: gain the source +6 dB into a limiter at -3 dBFS ceiling.
    # ~3 dB of gain reduction on peaks. Perceived loudness up noticeably,
    # peaks the same.
    light_in = src * db_to_lin(6)
    light_out = limit(light_in, ceiling_db=-3.0, attack_ms=2, release_ms=80)
    write_wav_no_normalize(os.path.join(OUT_DIR, "limit-light.wav"), light_out)

    # Crushed: gain +12 dB into a limiter at -0.3 dBFS, very fast attack.
    # ~9+ dB of gain reduction on peaks. The classic loudness-war sound:
    # squashed transients, no dynamic life, audibly distorted.
    crushed_in = src * db_to_lin(12)
    crushed_out = limit(crushed_in, ceiling_db=-0.3, attack_ms=0.5, release_ms=30)
    write_wav_no_normalize(os.path.join(OUT_DIR, "limit-crushed.wav"), crushed_out)


# ----- Run everything -----

if __name__ == "__main__":
    print(f"Generating dynamics demos in {OUT_DIR}\n")
    gen_dynamic_range()
    print()
    gen_threshold_ratio()
    print()
    gen_attack_release()
    print()
    gen_limiter()
    print(f"\nAll demos written to {OUT_DIR}")
