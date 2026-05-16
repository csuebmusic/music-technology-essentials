"""
Generates audio demo files for the Module 2 Week 5 reading
on dynamics, compression, and limiting.

Produces (13 files):

  Dynamic range (Section 1) — STEREO, from real source loop:
  - range-wide.wav         : conga/shaker/clave loop with natural dynamic
                             range, peak -3 dBFS
  - range-narrow.wav       : same source aggressively compressed and pushed
                             into a limiter, peak -3 dBFS, RMS ~6 dB
                             higher than wide

  Threshold + ratio (Section 2) — MONO, synthesized:
  - tr-source.wav          : repeating snare-like hits with varied levels
                             (peaks at -3, -9, -15, -3, -9, -15 dBFS)
  - tr-light.wav           : threshold -12 dB, ratio 2:1 (gentle)
  - tr-medium.wav          : threshold -18 dB, ratio 4:1 (clearly squashed)
  - tr-heavy.wav           : threshold -24 dB, ratio 10:1 (everything pinned)

  Attack and release (Section 3) — MONO, synthesized:
  - ar-source.wav          : kick + percussion loop with sharp transients
  - ar-fast-attack.wav     : 1 ms attack — transients clamped down
  - ar-slow-attack.wav     : 30 ms attack — transients pass through
  - ar-fast-release.wav    : 50 ms release — "pumping" audible
  - ar-slow-release.wav    : 400 ms release — smoother

  Limiting / loudness wars (Section 4) — STEREO, from real source loop:
  - limit-natural.wav      : full mix at natural dynamics, peak -3 dBFS
  - limit-light.wav        : +6 dB into limiter at -3 dBFS, ~3 dB louder RMS
  - limit-crushed.wav      : +12 dB into limiter at -0.3 dBFS, ~7 dB louder RMS

Sections 1 and 4 use a real Ableton-rendered loop (conga slaps at
maximum velocity + shaker + clave at low velocity) as source material;
the loop's natural dynamic range (~21 dB crest factor) is much wider
than anything practical to synthesize, which makes the compression
demonstrations land much more clearly. Sections 2 and 3 use synthesized
sources because they need precise level control across multiple hits
(Section 2) and precise transient timing (Section 3) that's easier to
guarantee from code.

All compression in this script is implemented as a feed-forward digital
compressor with a peak detector (one-pole follower) on the absolute
signal, applied to the linear-domain envelope. Gain reduction is computed
in the log domain, then multiplied back onto the signal. The stereo
variants (compress_stereo, limit_stereo) use linked sidechain detection
(single envelope from max(|L|, |R|), applied equally to both channels)
so the stereo image stays stable. Makeup gain is deliberately *not*
applied automatically — the compression demos in Sections 2 and 3 are
normalized to peak -3 dBFS, so students hear the squashing without the
loudness illusion of automatic makeup. The dynamic-range and limiter
demos (Sections 1 and 4) are deliberately NOT normalized post-processing
because their lesson is the loudness change at matched peaks.

The peak limiter in this build has no lookahead, so fast transients can
punch through the ceiling by a couple of dB. A final hard-clip pass at
the ceiling enforces the peak exactly. In a real production limiter
you'd want true lookahead and inter-sample-peak detection; for a
teaching demo where the peak meter must read identically across files
in a comparison set, a final clip is the right tradeoff.

Source loop expected at: assets/audio/source/dynamic-loop.wav
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
SOURCE_LOOP = os.path.join(REPO_ROOT, "assets", "audio", "source", "dynamic-loop.wav")
os.makedirs(OUT_DIR, exist_ok=True)

# Calibration constant for the narrow version of the dynamic-range demo.
# How much gain to push the compressed source through the limiter, so that
# the narrow version has ~6 dB higher RMS than the wide version (both at
# the same -3 dBFS peak). This value is calibrated specifically for
# dynamic-loop.wav (conga slaps + shaker + clave, ~21 dB crest factor);
# if you change the source, sweep this value to recalibrate.
NARROW_BOOST_DB = 18

SR = 44100


# ----- Helpers -----

def write_wav(path, audio, sr=SR, peak_dbfs=-3.0):
    """Normalize to peak_dbfs and write as 16-bit WAV. Supports mono (1-D
    array) or stereo (2-D array of shape (n, 2))."""
    audio = np.asarray(audio, dtype=np.float32)
    peak = float(np.max(np.abs(audio)))
    if peak > 0:
        target = 10 ** (peak_dbfs / 20)
        audio = audio * (target / peak)
    audio_int = np.clip(audio * 32767, -32768, 32767).astype(np.int16)
    wavfile.write(path, sr, audio_int)
    nframes = audio.shape[0] if audio.ndim == 2 else len(audio)
    chans = "stereo" if audio.ndim == 2 else "mono"
    print(f"Wrote {path}  ({nframes/sr:.2f} s, {chans}, peak {peak_dbfs:+.1f} dBFS)")


def write_wav_no_normalize(path, audio, sr=SR):
    """Write as 16-bit WAV without normalization. Supports mono or stereo."""
    audio = np.asarray(audio, dtype=np.float32)
    audio = np.clip(audio, -1.0, 1.0)
    audio_int = np.clip(audio * 32767, -32768, 32767).astype(np.int16)
    wavfile.write(path, sr, audio_int)
    peak_db = 20 * np.log10(max(float(np.max(np.abs(audio))), 1e-12))
    nframes = audio.shape[0] if audio.ndim == 2 else len(audio)
    chans = "stereo" if audio.ndim == 2 else "mono"
    print(f"Wrote {path}  ({nframes/sr:.2f} s, {chans}, peak {peak_db:+.1f} dBFS)")


def load_source_wav(path):
    """Read a 16-bit WAV from disk and return a (n,) mono or (n, 2) stereo
    float32 array in [-1, 1]. Raises FileNotFoundError if the path is missing."""
    if not os.path.isfile(path):
        raise FileNotFoundError(
            f"Source WAV not found: {path}\n"
            f"Expected the conga/shaker/clave loop at this path. "
            f"See the head of this script for setup notes."
        )
    sr, data = wavfile.read(path)
    if sr != SR:
        raise ValueError(f"Source sample rate {sr} != expected {SR}")
    return data.astype(np.float32) / 32768.0


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


def compress_stereo(audio, threshold_db, ratio, attack_ms, release_ms, sr=SR,
                    knee_db=2.0):
    """
    Stereo-linked feed-forward compressor. The sidechain detector reads the
    MAXIMUM of |left| and |right| sample-by-sample, so both channels are
    reduced by the same amount and the stereo image stays stable. (If you
    compressed each channel independently, a loud transient on one side
    would shift the apparent stereo position.)

    audio  : (n, 2) float32 array in [-1, 1]
    Returns the compressed signal at the same peak as the input (no makeup).
    """
    if audio.ndim != 2 or audio.shape[1] != 2:
        raise ValueError("compress_stereo expects shape (n, 2)")

    a_atk = np.exp(-1.0 / (attack_ms * 0.001 * sr))
    a_rel = np.exp(-1.0 / (release_ms * 0.001 * sr))

    # Build the linked detection signal: max of |L|, |R| at each sample.
    detector = np.maximum(np.abs(audio[:, 0]), np.abs(audio[:, 1])).astype(np.float32)

    env = np.zeros_like(detector)
    prev = 0.0
    for i, x in enumerate(detector):
        if x > prev:
            prev = a_atk * prev + (1 - a_atk) * x
        else:
            prev = a_rel * prev + (1 - a_rel) * x
        env[i] = prev

    env_db = lin_to_db(env)

    knee_lo = threshold_db - knee_db / 2
    knee_hi = threshold_db + knee_db / 2

    gain_db = np.zeros_like(env_db)
    above = env_db > knee_hi
    knee_region = (env_db > knee_lo) & ~above
    gain_db[above] = -(env_db[above] - threshold_db) * (1 - 1.0 / ratio)
    if knee_db > 0:
        knee_pos = env_db[knee_region] - knee_lo
        knee_amount = (knee_pos / knee_db) ** 2
        excess = env_db[knee_region] - threshold_db
        gain_db[knee_region] = -excess * knee_amount * (1 - 1.0 / ratio)

    gain_lin = db_to_lin(gain_db).reshape(-1, 1)  # broadcast across channels
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


def limit_stereo(audio, ceiling_db=-0.3, attack_ms=2.0, release_ms=80.0, sr=SR):
    """Stereo-linked limiter (same idea as compress_stereo but at limiter
    settings). Used for the dynamic-range and limiter demos when working
    from a real stereo source."""
    return compress_stereo(audio, threshold_db=ceiling_db, ratio=20.0,
                           attack_ms=attack_ms, release_ms=release_ms,
                           sr=sr, knee_db=0.5)


# ----- Generators -----

def gen_dynamic_range():
    """range-wide.wav (full dynamic range) and range-narrow.wav (squashed).

    Critical: these two files must be at the same PEAK level but DIFFERENT
    perceived loudness — same as the limiter trio. The narrow version
    should sound *louder on average* despite hitting the same ceiling.

    The source is a stereo Ableton-rendered loop of conga slaps (high
    velocity, near peak), shaker, and clave (low velocity, deep below
    peak). The natural dynamic range of the source is wide: roughly 21 dB
    of crest factor, with a ~57 dB spread between the loudest and
    quietest 100ms windows. This makes the compression-vs-no-compression
    contrast much more obvious than a synthesized source could.

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

    Both files are stereo, processed with linked stereo compression
    (single sidechain reading max(|L|, |R|), gain applied equally to both
    channels) so the stereo image stays stable under heavy compression.
    """
    src = load_source_wav(SOURCE_LOOP)  # shape (n, 2)

    # Wide: scale to peak -3 dBFS, no further processing. Natural dynamics
    # intact.
    wide = src.copy()
    peak = float(np.max(np.abs(wide)))
    if peak > 0:
        wide = wide / peak * db_to_lin(-3)
    write_wav_no_normalize(os.path.join(OUT_DIR, "range-wide.wav"), wide)

    # Narrow: aggressive compression, then push the result into a limiter
    # at -3 dBFS, then enforce the ceiling with a hard clip. The
    # compression squashes the dynamic range; the boost pulls the average
    # level toward the ceiling; the limiter handles the bulk of the
    # transients musically; the final clip catches anything the limiter
    # doesn't catch in time. Peak: exactly -3 dBFS. Average: ~6 dB higher
    # than wide. The boost amount is calibrated for this specific source
    # to land near +6 dB RMS gap; if you change the source, re-sweep.
    narrow = compress_stereo(src, threshold_db=-24, ratio=8,
                             attack_ms=3, release_ms=80)
    narrow = narrow * db_to_lin(NARROW_BOOST_DB)
    narrow = limit_stereo(narrow, ceiling_db=-3.0, attack_ms=1, release_ms=50)
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
    NOT normalized to the same peak. They sit at the SAME peak (-3 dBFS
    for natural and light, -0.3 dBFS for crushed) and the perceived
    loudness differs across them. Students should hear the loudness climb
    (and the cost) when comparing them.

    Same stereo source as gen_dynamic_range. Stereo-linked limiting +
    final hard-clip pass to keep peaks exact, same approach as the
    dynamic-range demo.
    """
    src = load_source_wav(SOURCE_LOOP)  # shape (n, 2)

    # Natural: scale to peak -3 dBFS, write directly.
    natural = src.copy()
    peak = float(np.max(np.abs(natural)))
    if peak > 0:
        natural = natural / peak * db_to_lin(-3)
    write_wav_no_normalize(os.path.join(OUT_DIR, "limit-natural.wav"), natural)

    # Light limiting: push the source +6 dB into a limiter at -3 dBFS,
    # final clip to enforce. Perceived loudness up noticeably; peaks the
    # same as natural.
    ceiling_3 = db_to_lin(-3.0)
    light_in  = src * db_to_lin(6)
    light_out = limit_stereo(light_in, ceiling_db=-3.0, attack_ms=2, release_ms=80)
    light_out = np.clip(light_out, -ceiling_3, ceiling_3)
    write_wav_no_normalize(os.path.join(OUT_DIR, "limit-light.wav"), light_out)

    # Crushed: push +12 dB into a limiter at -0.3 dBFS with a very fast
    # attack. The classic loudness-war sound: squashed transients, no
    # dynamic life, audibly distorted.
    ceiling_03 = db_to_lin(-0.3)
    crushed_in  = src * db_to_lin(12)
    crushed_out = limit_stereo(crushed_in, ceiling_db=-0.3, attack_ms=0.5, release_ms=30)
    crushed_out = np.clip(crushed_out, -ceiling_03, ceiling_03)
    write_wav_no_normalize(os.path.join(OUT_DIR, "limit-crushed.wav"), crushed_out)


def gen_normalization():
    """norm-quiet.wav and norm-loud.wav for Section 2.

    Same conga/shaker/clave loop as Section 1, scaled to two different
    peak levels. The pedagogical point is the OPPOSITE of Section 1: in
    Section 1 the two files have identical peaks and different shapes
    (compression); here the two files have identical shapes and
    different peaks (normalization is just a scaler).

    Quiet version: peak -18 dBFS. Simulates a conservative tracking
    decision — the kind of recording you might make when you don't yet
    know how loud your loudest moment will be.

    Loud version: same source, normalized to -1 dBFS. This is the exact
    operation Audacity's Effect > Volume and Compression > Normalize
    performs: find the peak, compute the scaler that lands it at the
    target, multiply every sample. No time-varying gain, no compression,
    no decision-making about what's loud and what's quiet. The whole
    signal moves by the same amount in dB. The shape is preserved.
    """
    src = load_source_wav(SOURCE_LOOP)  # shape (n, 2)

    # First, peak-normalize the source to a known starting point (-3 dBFS)
    # so the demo doesn't depend on whatever level the source happens to
    # be tracked at. From that known starting point, scale down to peak
    # -18 dBFS for the "quiet" demo. Both subsequent files derive from
    # this scaled starting signal, which guarantees the only difference
    # between them is a single multiplier.
    src_peak = float(np.max(np.abs(src)))
    src_at_minus3 = src / src_peak * db_to_lin(-3) if src_peak > 0 else src

    # Quiet: scale -3 dBFS source down 15 dB more, lands at peak -18 dBFS.
    # That's the "I set my input gain conservatively while tracking" level.
    quiet = src_at_minus3 * db_to_lin(-15)
    write_wav_no_normalize(os.path.join(OUT_DIR, "norm-quiet.wav"), quiet)

    # Loud (normalized): take the quiet version, find its peak, scale to -1 dBFS.
    # This is verbatim what Audacity's Normalize effect does.
    quiet_peak = float(np.max(np.abs(quiet)))
    loud = quiet / quiet_peak * db_to_lin(-1)
    write_wav_no_normalize(os.path.join(OUT_DIR, "norm-loud.wav"), loud)


# ----- Diagram generator: wide-vs-narrow waveform comparison -----

DIAGRAM_DIR = os.path.join(REPO_ROOT, "assets", "images", "module-02-week-05")


def _peak_envelope_for_display(audio, n_columns):
    """Reduce a long audio signal to (min, max) pairs per output column.
    Mixes stereo to mono for display. Returns two arrays of length n_columns:
    one for min values, one for max values, each in [-1, 1]."""
    if audio.ndim == 2:
        mono = audio.astype(np.float32).mean(axis=1)
    else:
        mono = audio.astype(np.float32)
    n = len(mono)
    mins = np.zeros(n_columns, dtype=np.float32)
    maxs = np.zeros(n_columns, dtype=np.float32)
    for col in range(n_columns):
        i0 = int(col * n / n_columns)
        i1 = int((col + 1) * n / n_columns)
        if i1 > i0:
            chunk = mono[i0:i1]
            mins[col] = float(np.min(chunk))
            maxs[col] = float(np.max(chunk))
    return mins, maxs


def gen_wide_vs_narrow_diagram():
    """Render an SVG that shows the wide and narrow waveforms stacked, both
    with the same -3 dBFS ceiling drawn. The point of the figure is the
    visual contrast: both touch the same ceiling, but narrow fills much
    more of the space underneath. The reading embeds this image right
    after the audio comparison in Section 1 to explain why narrow
    sounds louder despite identical peaks.

    Reads the WAVs that gen_dynamic_range just produced. Must run after
    gen_dynamic_range.
    """
    os.makedirs(DIAGRAM_DIR, exist_ok=True)

    sr_w, wide   = wavfile.read(os.path.join(OUT_DIR, "range-wide.wav"))
    sr_n, narrow = wavfile.read(os.path.join(OUT_DIR, "range-narrow.wav"))
    wide_f   = wide.astype(np.float32) / 32768.0
    narrow_f = narrow.astype(np.float32) / 32768.0

    # SVG layout. Two waveform panels stacked. Each panel has its own
    # local mid-line and a -3 dBFS ceiling drawn at the same vertical
    # offset from its mid-line. The same ceiling distance in both panels
    # is the visual punchline.
    W = 720
    H = 360
    pad_l = 80
    pad_r = 24
    pad_t = 18
    pad_b = 32
    plot_w = W - pad_l - pad_r
    panel_h = (H - pad_t - pad_b) // 2 - 14  # leave a gap between panels
    panel_gap = 28

    panel1_top = pad_t
    panel2_top = pad_t + panel_h + panel_gap

    n_cols = plot_w  # one column per pixel of plot width

    mins_w, maxs_w = _peak_envelope_for_display(wide_f, n_cols)
    mins_n, maxs_n = _peak_envelope_for_display(narrow_f, n_cols)

    # The waveform's vertical scale: amplitude 1.0 reaches the panel's
    # half-height, so a sample at peak (-3 dBFS = 0.708) reaches 70.8% of
    # the half-height. The "ceiling" line lives at amplitude 0.708 above
    # and below the centerline of each panel.
    ceiling_lin = 10 ** (-3.0 / 20)  # ~0.708
    half = panel_h / 2

    def amp_to_y(panel_top, amp):
        """amp in [-1, 1] -> y inside the panel, where 0 = centerline."""
        return panel_top + half - amp * half

    def build_waveform_path(panel_top, mins, maxs):
        # Filled outline: top edge along maxs, bottom edge along mins (reversed)
        parts = []
        # Top edge (max values)
        for col, v in enumerate(maxs):
            x = pad_l + col
            y = amp_to_y(panel_top, v)
            parts.append(f"{'M' if col == 0 else 'L'} {x:.2f} {y:.2f}")
        # Bottom edge (min values, drawn right-to-left)
        for col in range(n_cols - 1, -1, -1):
            x = pad_l + col
            y = amp_to_y(panel_top, mins[col])
            parts.append(f"L {x:.2f} {y:.2f}")
        parts.append("Z")
        return " ".join(parts)

    path_w = build_waveform_path(panel1_top, mins_w, maxs_w)
    path_n = build_waveform_path(panel2_top, mins_n, maxs_n)

    # Ceiling lines (at -3 dBFS, above and below centerline of each panel)
    def ceiling_pair(panel_top):
        cy_above = amp_to_y(panel_top, +ceiling_lin)
        cy_below = amp_to_y(panel_top, -ceiling_lin)
        return cy_above, cy_below

    c1_up, c1_dn = ceiling_pair(panel1_top)
    c2_up, c2_dn = ceiling_pair(panel2_top)

    # Center lines for visual reference
    cx1 = panel1_top + half
    cx2 = panel2_top + half

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}"
     role="img" aria-label="Waveform comparison: wide-dynamic-range version above, narrow-compressed version below, both with the same -3 dBFS peak ceiling marked">
  <rect width="{W}" height="{H}" fill="var(--bg-alt)"/>

  <!-- Panel labels -->
  <text x="{pad_l - 12}" y="{panel1_top + half + 4}" text-anchor="end"
        font-family="DM Mono, monospace" font-size="11" fill="var(--ink)">wide</text>
  <text x="{pad_l - 12}" y="{panel2_top + half + 4}" text-anchor="end"
        font-family="DM Mono, monospace" font-size="11" fill="var(--ink)">narrow</text>

  <!-- Ceiling lines at -3 dBFS, drawn in panel 1 -->
  <line x1="{pad_l}" y1="{c1_up:.2f}" x2="{pad_l + plot_w}" y2="{c1_up:.2f}"
        stroke="var(--accent)" stroke-width="0.8" stroke-dasharray="4,4" opacity="0.7"/>
  <line x1="{pad_l}" y1="{c1_dn:.2f}" x2="{pad_l + plot_w}" y2="{c1_dn:.2f}"
        stroke="var(--accent)" stroke-width="0.8" stroke-dasharray="4,4" opacity="0.7"/>

  <!-- Ceiling lines at -3 dBFS, drawn in panel 2 (SAME vertical offset from center as panel 1) -->
  <line x1="{pad_l}" y1="{c2_up:.2f}" x2="{pad_l + plot_w}" y2="{c2_up:.2f}"
        stroke="var(--accent)" stroke-width="0.8" stroke-dasharray="4,4" opacity="0.7"/>
  <line x1="{pad_l}" y1="{c2_dn:.2f}" x2="{pad_l + plot_w}" y2="{c2_dn:.2f}"
        stroke="var(--accent)" stroke-width="0.8" stroke-dasharray="4,4" opacity="0.7"/>

  <!-- Center reference lines (thin, subtle) -->
  <line x1="{pad_l}" y1="{cx1:.2f}" x2="{pad_l + plot_w}" y2="{cx1:.2f}"
        stroke="var(--ink-soft)" stroke-width="0.4" opacity="0.4"/>
  <line x1="{pad_l}" y1="{cx2:.2f}" x2="{pad_l + plot_w}" y2="{cx2:.2f}"
        stroke="var(--ink-soft)" stroke-width="0.4" opacity="0.4"/>

  <!-- Waveform fills -->
  <path d="{path_w}" fill="var(--ink)" opacity="0.78"/>
  <path d="{path_n}" fill="var(--ink)" opacity="0.78"/>

  <!-- Ceiling annotation: place INSIDE the plot area, just above the ceiling line, right-aligned -->
  <text x="{pad_l + plot_w - 6}" y="{c1_up - 4:.2f}"
        font-family="DM Mono, monospace" font-size="10" fill="var(--accent)" text-anchor="end">−3 dBFS ceiling</text>
  <text x="{pad_l + plot_w - 6}" y="{c2_up - 4:.2f}"
        font-family="DM Mono, monospace" font-size="10" fill="var(--accent)" text-anchor="end">−3 dBFS ceiling</text>

  <!-- Time axis (single label centered under bottom panel) -->
  <text x="{pad_l + plot_w / 2:.2f}" y="{H - 8}"
        font-family="DM Mono, monospace" font-size="10" fill="var(--ink-soft)" text-anchor="middle">6 seconds →</text>
</svg>
"""

    out_path = os.path.join(DIAGRAM_DIR, "wide-vs-narrow.svg")
    with open(out_path, "w") as f:
        f.write(svg)
    print(f"Wrote {out_path}  ({W}x{H} SVG)")


def gen_normalization_diagram():
    """Render an SVG showing quiet and normalized waveforms stacked at the
    SAME vertical scale, so students see two things:

    1. Different peak levels (quiet sits well below the -1 dBFS ceiling;
       loud touches it). Both ceilings drawn at -1 dBFS for reference.
    2. Identical SHAPE — the loud waveform is a scaled-up copy of the
       quiet one. The pattern of slaps, the gaps, the relative heights
       of every event: identical.

    This diagram is the visual counterpoint to wide-vs-narrow.svg:
    where that one shows two waveforms with matched peaks but
    different shapes (compression reshapes), this one shows two
    waveforms with matched shapes but different peaks (normalization
    just scales).

    Reads the WAVs that gen_normalization just produced; must run
    after it.
    """
    os.makedirs(DIAGRAM_DIR, exist_ok=True)

    sr_q, quiet = wavfile.read(os.path.join(OUT_DIR, "norm-quiet.wav"))
    sr_l, loud  = wavfile.read(os.path.join(OUT_DIR, "norm-loud.wav"))
    quiet_f = quiet.astype(np.float32) / 32768.0
    loud_f  = loud.astype(np.float32) / 32768.0

    W = 720
    H = 360
    pad_l = 80
    pad_r = 24
    pad_t = 18
    pad_b = 32
    plot_w = W - pad_l - pad_r
    panel_h = (H - pad_t - pad_b) // 2 - 14
    panel_gap = 28

    panel1_top = pad_t
    panel2_top = pad_t + panel_h + panel_gap
    n_cols = plot_w

    mins_q, maxs_q = _peak_envelope_for_display(quiet_f, n_cols)
    mins_l, maxs_l = _peak_envelope_for_display(loud_f,  n_cols)

    # Both panels use the SAME vertical scale: amplitude 1.0 reaches the
    # panel's half-height. This is critical for the demonstration. If we
    # auto-scaled each panel to fill its space, the two waveforms would
    # look identical and the "different peaks" message would be lost.
    ceiling_lin = 10 ** (-1.0 / 20)  # -1 dBFS = 0.891, the normalization target
    half = panel_h / 2

    def amp_to_y(panel_top, amp):
        return panel_top + half - amp * half

    def build_waveform_path(panel_top, mins, maxs):
        parts = []
        for col, v in enumerate(maxs):
            x = pad_l + col
            y = amp_to_y(panel_top, v)
            parts.append(f"{'M' if col == 0 else 'L'} {x:.2f} {y:.2f}")
        for col in range(n_cols - 1, -1, -1):
            x = pad_l + col
            y = amp_to_y(panel_top, mins[col])
            parts.append(f"L {x:.2f} {y:.2f}")
        parts.append("Z")
        return " ".join(parts)

    path_q = build_waveform_path(panel1_top, mins_q, maxs_q)
    path_l = build_waveform_path(panel2_top, mins_l, maxs_l)

    def ceiling_pair(panel_top):
        cy_above = amp_to_y(panel_top, +ceiling_lin)
        cy_below = amp_to_y(panel_top, -ceiling_lin)
        return cy_above, cy_below

    c1_up, c1_dn = ceiling_pair(panel1_top)
    c2_up, c2_dn = ceiling_pair(panel2_top)

    cx1 = panel1_top + half
    cx2 = panel2_top + half

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}"
     role="img" aria-label="Waveform comparison: quiet recording above, same recording normalized below. Same shape, different scale. Both panels show the -1 dBFS ceiling for reference; quiet sits well below it, normalized touches it.">
  <rect width="{W}" height="{H}" fill="var(--bg-alt)"/>

  <!-- Panel labels -->
  <text x="{pad_l - 12}" y="{panel1_top + half + 4}" text-anchor="end"
        font-family="DM Mono, monospace" font-size="11" fill="var(--ink)">quiet</text>
  <text x="{pad_l - 12}" y="{panel2_top + half + 4}" text-anchor="end"
        font-family="DM Mono, monospace" font-size="11" fill="var(--ink)">normalized</text>

  <!-- Ceiling lines at -1 dBFS. Only draw the upper one in each panel; the
       lower one is symmetric and redundant; cleaner visual. -->
  <line x1="{pad_l}" y1="{c1_up:.2f}" x2="{pad_l + plot_w}" y2="{c1_up:.2f}"
        stroke="var(--accent)" stroke-width="0.8" stroke-dasharray="4,4" opacity="0.7"/>

  <line x1="{pad_l}" y1="{c2_up:.2f}" x2="{pad_l + plot_w}" y2="{c2_up:.2f}"
        stroke="var(--accent)" stroke-width="0.8" stroke-dasharray="4,4" opacity="0.7"/>

  <!-- Center reference lines -->
  <line x1="{pad_l}" y1="{cx1:.2f}" x2="{pad_l + plot_w}" y2="{cx1:.2f}"
        stroke="var(--ink-soft)" stroke-width="0.4" opacity="0.4"/>
  <line x1="{pad_l}" y1="{cx2:.2f}" x2="{pad_l + plot_w}" y2="{cx2:.2f}"
        stroke="var(--ink-soft)" stroke-width="0.4" opacity="0.4"/>

  <!-- Waveform fills -->
  <path d="{path_q}" fill="var(--ink)" opacity="0.78"/>
  <path d="{path_l}" fill="var(--ink)" opacity="0.78"/>

  <!-- Ceiling annotation -->
  <text x="{pad_l + plot_w - 6}" y="{c1_up - 4:.2f}"
        font-family="DM Mono, monospace" font-size="10" fill="var(--accent)" text-anchor="end">−1 dBFS ceiling</text>
  <text x="{pad_l + plot_w - 6}" y="{c2_up - 4:.2f}"
        font-family="DM Mono, monospace" font-size="10" fill="var(--accent)" text-anchor="end">−1 dBFS ceiling</text>

  <!-- Time axis -->
  <text x="{pad_l + plot_w / 2:.2f}" y="{H - 8}"
        font-family="DM Mono, monospace" font-size="10" fill="var(--ink-soft)" text-anchor="middle">6 seconds →</text>
</svg>
"""

    out_path = os.path.join(DIAGRAM_DIR, "norm-quiet-vs-loud.svg")
    with open(out_path, "w") as f:
        f.write(svg)
    print(f"Wrote {out_path}  ({W}x{H} SVG)")


# ----- Run everything -----

if __name__ == "__main__":
    print(f"Generating dynamics demos in {OUT_DIR}\n")
    gen_dynamic_range()
    print()
    gen_normalization()
    print()
    gen_threshold_ratio()
    print()
    gen_attack_release()
    print()
    gen_limiter()
    print()
    gen_wide_vs_narrow_diagram()
    gen_normalization_diagram()
    print(f"\nAll demos written to {OUT_DIR}")
    print(f"Diagrams written to {DIAGRAM_DIR}")
