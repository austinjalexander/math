---
name: external-course
description: Track outside mathematics courses, map them to local objectives, and record evidence and resume points. Use for course intake, progress updates, resuming an outside course, or importing Roam Research study bookmarks and tagging transferred course pages with #math-repo.
---

# Integrate an external mathematics course

Read `AGENTS.md`, `docs/agents/PROFILE.md`, `EXTERNAL_COURSES.md`, and any existing provider record. For planning, also read local objectives, progress evidence, and available capacity.

Create a record from `templates/external-course-template.md` only when a course is adopted or needs tracking. Record the source URL/edition, integration role, inspected scope, access limits, exact resume point, and known evidence. Keep candidate resources separate from adopted courses. Verify public source material before assigning section/page/exercise numbers; do not infer enrollment, restricted-content access, or completion from a public page.

Map specific sections to stable curriculum IDs and authored local modules. Mark outline-only mappings provisional. Choose one main exercise track per objective; reading, video, and code positions can be recorded independently without doubling assignments.

Keep general mathematics course records and future resume points here. Attach an MIT Open Learning Library delivery to the matching course record while retaining each edition's activity labels, access limits, and resume points. Use a separate record for a distinct course. Physics and quantum applications can reference the math record and track their own application work.

For updates, record actual activity/date, report source, assistance, evidence paths, and stopping point. Keep provider completion and local mastery distinct. Use `grade-solution` for submitted work and `tutor-session` for guided study. Check topic gates only under the shared evidence policy.

At a learner request or topic transition, inspect the return queue and suggest one relevant session-sized task within available capacity. Do not invent review dates or schedules. Update the course record/index when evidence changes; never advance provider progress just to inspect a lesson. Export with `tools/agent_config.py export --skill external-course --external-course external-courses/<record>.md` when useful.

## Import from Roam Research

1. Use the Roam connection available in the session. Identify the graph and read its guidelines once before the first graph read or write. Follow the user's named pages or schedule links. When the connection is unavailable, use user-provided exports or excerpts when available and report any pending Roam tagging.
2. Read the relevant course branches through their `#last` blocks. Check the surrounding notes and provider links to match each marker to its edition, lesson, and activity. Keep distinct readings, videos, problem attempts, and code positions. A bare link belongs with resource bookmarks. Preserve an inaccessible provider link with its Roam evidence and note the verification limit.
3. Match by provider, edition, and existing Roam source before creating a course record. Update the existing record when there is a match. Keep conflicting or undated markers with their context and avoid choosing a latest position without evidence. Record the import date separately from study dates. Link the source page and relevant blocks. Verify the record, its links, and its entry in `EXTERNAL_COURSES.md` before tagging.
4. For an authorized transfer, check the intended parent for an existing `#math-repo` marker. If absent, add one top-level block on a dedicated course page or one child under the resource block on a mixed page. Use a verified remote file link where available. For a local-only record, link the repository root and include the repository-relative file and section. Preserve the original notes and bookmarks. Verify the tag and destination under the intended parent. If a write result is ambiguous, re-read the parent before considering a retry and follow the connector's retry rules. Report any pending imports or tags so a later run can resume without creating duplicates.
