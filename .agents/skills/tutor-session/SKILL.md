---
name: tutor-session
description: Runs an interactive curriculum tutoring session with prerequisite checks, guided practice, learner reflection, and evidence-based progress. Use when the learner asks to study, continue, learn a topic, or be tutored through an existing module.
---

# Tutor a session

Read `AGENTS.md`, `docs/agents/PROFILE.md`, and `docs/agents/tutoring.md` from the repository root. Read `PROGRESS.md`, the target module README and notes, and the latest relevant log. If the learner asks for new content, use `author-module`; for a submitted attempt, use `grade-solution`.

1. **Frame (~5 min).** Name the curriculum section and module path; select one objective and agree on a session-sized outcome. Follow the profile's time budget.
2. **Prereqs (~5 min).** Ask 2–3 short questions, one at a time. Refresh one shaky prerequisite; use `diagnose-prereqs` when several are uncertain. Recent unaided evidence can satisfy this check.
3. **Teach (~15–30 min).** Introduce one concept at a time, ask the learner to derive/predict the next step, and request an explanation in their own words. Work one example collaboratively.
4. **Practice (~20–40 min).** Sample one drill, one conceptual, and one applied problem. Offer one hint at a time following the shared guidance. Check units, signs, limits, normalization, or an independent calculation. This sample does not replace required remaining problems.
5. **Reflect (~5 min).** Ask what mattered, where they nearly went wrong, and how they recovered. Save the learner's own dated 2–4 sentence reflection in the profile's log location; do not manufacture it.
6. **Record (~2 min).** Record actual attempts, assistance, remaining work, and the next task. Update a topic checkbox only when all required work, its timed unaided exit assessment, and the learner reflection are evidenced under `docs/agents/tutoring.md`. Otherwise leave it unchecked.

These times are planning targets, not claims about elapsed time. Run an unaided test separately without coaching. Honor explicit requests for worked solutions while recording assistance. Pause for the learner's input rather than delivering the whole session in a monologue.
