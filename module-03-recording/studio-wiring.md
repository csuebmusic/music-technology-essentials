# MB2508 Patchbay Wiring Spec

**Internal / TA-facing.** Not student-facing. The student-facing version of the patchbay (what it does, the default routing, how to patch during a session) lives in `lessons/08-handout-studio.html`.

This document is the wiring authority for the Switchcraft StudioPatch 9625 patchbay in MB2508. It's the single source of truth for which signal lands on which DB25, which TT column carries what, and what's normalled. If the studio is rewired, this file gets updated first; the handout gets updated to match.

---

## Hardware overview

- **Patchbay:** Switchcraft StudioPatch 9625 (96 TT patch points on the front, organized into 48 columns × 2 rows; 12 DB25 sockets on the rear, 6 INPUT + 6 OUTPUT).
- **Top TT (front) = source.** Wired internally to a rear DB25 INPUT pin. The signal arrives from gear and appears at this jack.
- **Bottom TT (front) = destination.** Wired internally to a rear DB25 OUTPUT pin. The signal leaves this jack and travels to gear.
- **Each column** carries one source signal (top) plus one destination signal (bottom). The two are connected internally by the column's normal switch (full, half, or non).

## Cables connecting the patchbay to the rest of the studio

| Cable type | Quantity | Connects |
|---|---|---|
| Switchcraft DB25MM10TRS (2× DB25-M to 8× 1/4" TRS-M insert snake, 10 ft) | 4 | Toft inserts → patchbay DB25s 1-4 and 1-4 OUTPUT pairs |
| Switchcraft DB25M10XLRF (DB25-M to 8× XLR-F, 10 ft) | 1 | Effects gear outputs (SSL, M2000) → patchbay DB25 INPUT 5 |
| Switchcraft DB25M10XLRM (DB25-M to 8× XLR-M, 10 ft) | 1 | Patchbay DB25 OUTPUT 5 → effects gear inputs (SSL, M2000) |
| Switchcraft DB25M10TRS (DB25-M to 8× 1/4" TRS-M, 10 ft) | 2 | Toft aux masters → patchbay DB25 INPUT 6; patchbay DB25 OUTPUT 6 → Toft stereo effects returns |

Total: 8 cables.

## DB25 allocation

The 12 patchbay DB25s are numbered 1-6 for INPUT (top row of the patchbay rear) and 1-6 for OUTPUT (bottom row). Each carries 8 channels.

### INPUT DB25 1 → patchbay columns 1-8 (top TT row)

Carries the SEND legs of Toft channel inserts 1-8.

| Column | Top TT (source) | Cable |
|---|---|---|
| 1 | Toft channel 1 INSERT SEND | DB25MM10TRS #1 |
| 2 | Toft channel 2 INSERT SEND | DB25MM10TRS #1 |
| 3 | Toft channel 3 INSERT SEND | DB25MM10TRS #1 |
| 4 | Toft channel 4 INSERT SEND | DB25MM10TRS #1 |
| 5 | Toft channel 5 INSERT SEND | DB25MM10TRS #1 |
| 6 | Toft channel 6 INSERT SEND | DB25MM10TRS #1 |
| 7 | Toft channel 7 INSERT SEND | DB25MM10TRS #1 |
| 8 | Toft channel 8 INSERT SEND | DB25MM10TRS #1 |

### OUTPUT DB25 1 → patchbay columns 1-8 (bottom TT row)

Carries the RETURN legs of Toft channel inserts 1-8.

| Column | Bottom TT (destination) | Cable |
|---|---|---|
| 1 | Toft channel 1 INSERT RETURN | DB25MM10TRS #1 |
| 2 | Toft channel 2 INSERT RETURN | DB25MM10TRS #1 |
| 3 | Toft channel 3 INSERT RETURN | DB25MM10TRS #1 |
| 4 | Toft channel 4 INSERT RETURN | DB25MM10TRS #1 |
| 5 | Toft channel 5 INSERT RETURN | DB25MM10TRS #1 |
| 6 | Toft channel 6 INSERT RETURN | DB25MM10TRS #1 |
| 7 | Toft channel 7 INSERT RETURN | DB25MM10TRS #1 |
| 8 | Toft channel 8 INSERT RETURN | DB25MM10TRS #1 |

**Normal:** half-normal for columns 1-8. At rest, SEND flows directly to RETURN (insert loop closed, no processing). Plug into the bottom (RETURN) jack alone to break the normal and force the signal through external processing.

### INPUT DB25 2 + OUTPUT DB25 2 → columns 9-16

Same pattern as columns 1-8 for Toft channels 9-16: each column carries SEND on top and RETURN on bottom, half-normalled.

| Column | Top TT (source) | Bottom TT (destination) |
|---|---|---|
| 9 | Toft channel 9 INSERT SEND | Toft channel 9 INSERT RETURN |
| 10 | Toft channel 10 INSERT SEND | Toft channel 10 INSERT RETURN |
| 11 | Toft channel 11 INSERT SEND | Toft channel 11 INSERT RETURN |
| 12 | Toft channel 12 INSERT SEND | Toft channel 12 INSERT RETURN |
| 13 | Toft channel 13 INSERT SEND | Toft channel 13 INSERT RETURN |
| 14 | Toft channel 14 INSERT SEND | Toft channel 14 INSERT RETURN |
| 15 | Toft channel 15 INSERT SEND | Toft channel 15 INSERT RETURN |
| 16 | Toft channel 16 INSERT SEND | Toft channel 16 INSERT RETURN |

Cable: DB25MM10TRS #2.

### INPUT DB25 3 + OUTPUT DB25 3 → columns 17-24

Subgroup inserts 1-8.

| Column | Top TT (source) | Bottom TT (destination) |
|---|---|---|
| 17 | Toft subgroup 1 INSERT SEND | Toft subgroup 1 INSERT RETURN |
| 18 | Toft subgroup 2 INSERT SEND | Toft subgroup 2 INSERT RETURN |
| 19 | Toft subgroup 3 INSERT SEND | Toft subgroup 3 INSERT RETURN |
| 20 | Toft subgroup 4 INSERT SEND | Toft subgroup 4 INSERT RETURN |
| 21 | Toft subgroup 5 INSERT SEND | Toft subgroup 5 INSERT RETURN |
| 22 | Toft subgroup 6 INSERT SEND | Toft subgroup 6 INSERT RETURN |
| 23 | Toft subgroup 7 INSERT SEND | Toft subgroup 7 INSERT RETURN |
| 24 | Toft subgroup 8 INSERT SEND | Toft subgroup 8 INSERT RETURN |

Cable: DB25MM10TRS #3. Normal: half-normal.

### INPUT DB25 4 + OUTPUT DB25 4 → columns 25-32

Master inserts and 6 spare columns.

| Column | Top TT (source) | Bottom TT (destination) |
|---|---|---|
| 25 | Toft master INSERT L SEND | Toft master INSERT L RETURN |
| 26 | Toft master INSERT R SEND | Toft master INSERT R RETURN |
| 27 | (spare) | (spare) |
| 28 | (spare) | (spare) |
| 29 | (spare) | (spare) |
| 30 | (spare) | (spare) |
| 31 | (spare) | (spare) |
| 32 | (spare) | (spare) |

Cable: DB25MM10TRS #4. Normal: half-normal for columns 25-26 (the active master insert columns); set unused columns to non-normal so dust caps don't cause unintended routing if someone plugs in by accident.

### INPUT DB25 5 → columns 33-40 (top TT row only, effects gear outputs)

| Column | Top TT (source) | Cable |
|---|---|---|
| 33 | SSL G L OUT | DB25M10XLRF #1 (XLR-F plug to SSL L OUT jack) |
| 34 | SSL G R OUT | DB25M10XLRF #1 (XLR-F plug to SSL R OUT jack) |
| 35 | M2000 L OUT | DB25M10XLRF #1 (XLR-F plug to M2000 L OUT jack) |
| 36 | M2000 R OUT | DB25M10XLRF #1 (XLR-F plug to M2000 R OUT jack) |
| 37 | (spare) | |
| 38 | (spare) | |
| 39 | (spare) | |
| 40 | (spare) | |

### OUTPUT DB25 5 → columns 33-40 (bottom TT row only, effects gear inputs)

| Column | Bottom TT (destination) | Cable |
|---|---|---|
| 33 | SSL G L IN | DB25M10XLRM #1 (XLR-M plug to SSL L IN jack) |
| 34 | SSL G R IN | DB25M10XLRM #1 (XLR-M plug to SSL R IN jack) |
| 35 | M2000 IN (mono) | DB25M10XLRM #1 (XLR-M plug to M2000 IN jack) |
| 36 | (spare) | |
| 37 | (spare) | |
| 38 | (spare) | |
| 39 | (spare) | |
| 40 | (spare) | |

**Normal for columns 33-40:** non-normal (the SSL's input and output are on the same column number, so a full or half normal would create a feedback loop). Effects gear sits in the bay awaiting front-panel patching.

### INPUT DB25 6 → columns 41-48 (top TT row only, Toft aux masters)

| Column | Top TT (source) | Cable |
|---|---|---|
| 41 | Toft Aux Master 1 | DB25M10TRS #1 (TRS plug to Toft Aux Master 1) |
| 42 | Toft Aux Master 2 | DB25M10TRS #1 (TRS plug to Toft Aux Master 2) |
| 43 | Toft Aux Master 3 | DB25M10TRS #1 (TRS plug to Toft Aux Master 3) |
| 44 | Toft Aux Master 4 | DB25M10TRS #1 (TRS plug to Toft Aux Master 4) |
| 45 | Toft Aux Master 5 | DB25M10TRS #1 (TRS plug to Toft Aux Master 5) |
| 46 | Toft Aux Master 6 | DB25M10TRS #1 (TRS plug to Toft Aux Master 6) |
| 47 | (spare) | |
| 48 | (spare) | |

### OUTPUT DB25 6 → columns 41-48 (bottom TT row only, Toft stereo effects returns)

| Column | Bottom TT (destination) | Cable |
|---|---|---|
| 41 | (spare) | |
| 42 | (spare) | |
| 43 | (spare) | |
| 44 | (spare) | |
| 45 | (spare) | |
| 46 | (spare) | |
| 47 | Toft Stereo Effects Return 1 | DB25M10TRS #2 (TRS plug to Toft ER1 jack, carries L+R stereo) |
| 48 | Toft Stereo Effects Return 2 | DB25M10TRS #2 (TRS plug to Toft ER2 jack, carries L+R stereo) |

**Normal for columns 41-48:** non-normal (aux masters and effects returns aren't naturally paired with each other).

---

## Permanent TT cables on the front of the bay

These cables route the studio's two default outboard processors. They live on the front of the bay permanently and only come off when the engineer wants to use the SSL or M2000 for something other than the default.

### SSL G on master INSERT (4 TT cables)

| TT cable | From (top TT, source) | To (bottom TT, destination) |
|---|---|---|
| 1 | Column 25 top (Master INS L SEND) | Column 33 bottom (SSL L IN) |
| 2 | Column 33 top (SSL L OUT) | Column 25 bottom (Master INS L RETURN) |
| 3 | Column 26 top (Master INS R SEND) | Column 34 bottom (SSL R IN) |
| 4 | Column 34 top (SSL R OUT) | Column 26 bottom (Master INS R RETURN) |

### M2000 on Aux 3 → Stereo Effects Returns (3 TT cables)

| TT cable | From (top TT, source) | To (bottom TT, destination) |
|---|---|---|
| 5 | Column 43 top (Aux Master 3) | Column 35 bottom (M2000 IN) |
| 6 | Column 35 top (M2000 L OUT) | Column 47 bottom (Stereo Effects Return 1) |
| 7 | Column 36 top (M2000 R OUT) | Column 48 bottom (Stereo Effects Return 2) |

**Total: 7 permanent TT cables on the front of the bay.**

---

## What this configuration achieves

- All 26 Toft inserts are reachable from the front of the bay. The half-normal setting keeps the insert loop closed when no cable is plugged, so the console behaves normally; plugging into the bottom (RETURN) jack of any channel breaks the loop and forces external processing.
- The SSL is permanently in the master mix INSERT path by default. To bypass it, the engineer pulls the 4 TT cables that route the SSL.
- The M2000 is permanently available as a parallel reverb on Aux 3. Any channel can send to Aux 3 and hear reverb come back in the master mix.
- The aux masters and stereo effects returns are exposed on the bay for ad-hoc patching (e.g., routing aux 1 to a different destination, or sending a stereo source into the Toft via an effects return).
- 6 spare columns total (4 inserts + 8 outboard slots + 2 aux/return slots) for future expansion.

## Open questions / future revisions

- **Spare DB25 INPUT slots on cable #4** (columns 27-32, 6 unused insert columns): if more outboard gear arrives, those slots can be repurposed by re-pinning the cable or replacing it with a different breakout.
- **Direct outs:** the Toft channel direct outs are not on this patchbay yet. If we want them accessible, we'd need another DB25 INPUT + cable from the Toft to the bay.
- **HDX I/O is not on this patchbay.** The HDX submaster routing is hardwired Toft ↔ HDX without going through the patchbay. If we ever want the HDX channels patchable (e.g., to substitute an external A/D converter), this would be a future expansion.
