# NAS file retention and archival policy — MUS 381

**Status:** Draft, pending IT approval.
**Owner:** Inés Thiebaut (course PI and lab manager).
**Last updated:** April 2026.

## Purpose

To define what happens to MUS 381 student working files on the lab NAS over time: when they stay, when they move to archive, and when they're deleted. The policy balances three things: students' right to access and retrieve their own work, operational hygiene of the active workspace, and reasonable bounds on long-term storage.

## Scope

This policy applies to:

- Student working folders on the MUS 381 NAS share (`/music/students/<lastname>/`)
- Project deliverables and final exports stored on the NAS
- The shared sample bank and any TA/instructor working files for MUS 381

This policy does **not** apply to:

- Grade records, course rosters, or other registrar-managed data
- Student-owned files stored on personal devices or personal cloud accounts
- Files stored elsewhere on CSUEB systems outside the MUS 381 NAS share

## Storage tiers

Files exist in one of three states:

1. **Active** — read-write, on the primary NAS share. Accessible during normal lab sessions.
2. **Archive** — read-only, on a slower storage tier. Accessible by request to the instructor or TA. Not visible from the lab workstations.
3. **Deleted** — permanently removed. Cannot be recovered.

## Lifecycle

The default flow for any student's MUS 381 working folder:

### Stage 1: End of semester (December for fall, May for spring)

No action. Files remain in the active tier. This handles students who continue into Sound Design or other downstream courses, students who repeat MUS 381 in a later term, and the common case of returning to past work over winter or summer break.

### Stage 2: End of academic year (late May or early June)

Students who took MUS 381 during the prior academic year and are not continuing with related coursework receive a notification (see "Notification" below) that their working files will be moved to archive on a stated date, typically four weeks out. After the deadline, the files move from active to archive. The active workspace is reclaimed.

"Not continuing" means: not enrolled in MUS 381 again, not enrolled in Sound Design or another course that uses the lab NAS, and not in a graduate program with continued lab access. The instructor confirms the list before notifications go out.

### Stage 3: Departure from CSUEB (graduation, transfer, withdrawal)

When a student leaves the institution, their archived files are retained for one additional academic year, then permanently deleted. This gives departed students a reasonable window to retrieve material they may have missed at the year-end archive transition.

## Notification

Students are notified twice during the lifecycle:

- **At enrollment in MUS 381**, the syllabus and Day 1 orientation include a brief mention of the file retention policy and a pointer to this document.
- **Before any move from active to archive**, students receive an email from the instructor or TA at least four weeks before the transition date. The notice includes the date, instructions for downloading their files, and a contact path for questions or requests for extension.

No notification is sent before deletion (Stage 3). The institution's general data retention policies cover that case, and the year-end notification has already given the student fair warning that files are not held indefinitely.

## Responsibilities

**Instructor (course PI):**

- Owns this policy.
- Confirms the "not continuing" student list each spring.
- Sends or supervises the year-end notification email.
- Handles requests for extension or restoration from archive.
- Updates this policy as the course evolves.

**Teaching assistant:**

- Executes the annual archive transition following the runbook (separate document).
- Drafts and sends the notification email under the instructor's name.
- Maintains the archive directory listing for retrieval requests.

**IT:**

- Provides and maintains the storage tiers (active and archive).
- Performs the technical transition between tiers when requested by the instructor or TA.
- Performs the final deletion at the end of the post-departure retention window.

## Student rights

Students may, at any time before final deletion:

- Download their own files from the active or archive tier (active anytime; archive by request).
- Request an extension on the year-end transition if they need more time, are returning from leave, or have an ongoing project that would benefit from continued access.
- Request that their files be deleted earlier than the default lifecycle would dictate.

Requests should be sent to the instructor by email.

## Exceptions

The default lifecycle can be extended in cases including but not limited to:

- A student takes a leave of absence and intends to return.
- A student's MUS 381 work is part of an ongoing research project, performance, or portfolio.
- A student is using their final project as part of a graduate school or job application.
- The instructor or another faculty member identifies pedagogical or archival value in retaining a piece of student work as a reference example (with the student's written permission).

Extensions are granted in one-year increments. The instructor reviews active extensions annually.

## Open questions

These are intentionally unresolved pending IT specification of the storage solution:

- The exact mechanism for the active-to-archive transition (filesystem move, snapshot, separate share). Affects how the TA's runbook is written.
- Whether archive is on the same physical NAS or on separate institutional storage.
- Cost implications of long-term archive retention vs. earlier deletion.

This policy is intended to be technology-agnostic — it describes the *what* and *when*, not the *how*. The runbook will fill in the mechanics once IT confirms the storage architecture.
