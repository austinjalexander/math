# Mathematics learning repository instructions

Follow the user's current request. Use teaching workflows for study, diagnostics, grading, and lesson authoring; use ordinary engineering workflows for repository maintenance.

## Start here

1. Read [the repository profile](docs/agents/PROFILE.md) for scope, canonical paths, sources, and computation conventions.
2. Before teaching, read `PROGRESS.md`, the target phase/module README, and relevant learner work. Use `docs/CURRICULUM.md`, `STUDY_PLAN.md`, and `RESOURCES.md` for scope and prerequisites.
3. Read [tutoring guidance](docs/agents/tutoring.md) for teaching and evidence decisions, [module structure](docs/agents/module-structure.md) for lesson authoring, and [math/code style](docs/agents/math-and-code-style.md) for mathematical material.
4. Use the relevant canonical workflow in `.agents/skills/`: `tutor-session`, `grade-solution`, `diagnose-prereqs`, `author-module`, or `external-course`. The [setup guide](docs/agents/README.md) describes local discovery and handoff.

## Evidence and scope

- Generated lessons, reference programs, notebook outputs, and course-page visits are preparation artifacts, not learner mastery.
- A module requires completed/corrected required work, a passed stated timed unaided assessment, and the learner's own dated 2–4 sentence reflection. Broad topics require their full assessed scope, not one introductory lesson.
- Record actual evidence paths, assistance, and timing. Never invent attempts, scores, elapsed time, reflections, provider progress, or account access. Readiness diagnostics do not complete prerequisite modules.
- Use the [external-course workflow](.agents/skills/external-course/SKILL.md#import-from-roam-research) for Roam imports. Keep future course progress in the repository and use `#math-repo` on the source page once its transferred checkpoints are verified in the course record and index.
- Keep answer keys separate from learner prompts. Offer staged hints by default; honor requests for full solutions and record assistance. Do not coach during an unaided assessment.
- Distinguish proof, symbolic computation, finite example checks, and numerical evidence. State domains, hypotheses, tolerances, and model assumptions.
- Use the learner's available capacity; no math-specific weekly allocation is established. Coordinate overlapping study and count reused work once.
- Preserve existing learner work and the unchanged notebook archive. Run checks relevant to the change.

## Configuration maintenance

Canonical behavior lives here, in `docs/agents/`, and in `.agents/skills/`. `.cursor/rules/` and `CLAUDE.md` are small adapters; `.claude/skills/` links to canonical local skill folders. This repository is self-contained; do not link configuration or runtime code to sibling repositories or modify global settings. Run `python3 tools/agent_config.py check` after configuration changes.
