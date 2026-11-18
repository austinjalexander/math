# Mathematics repository profile

All paths below are relative to this repository root.

## Scope and sources

This is a broad learning home for engineering, applied, theoretical, and abstract mathematics. Read `GOALS.md` for intent, `docs/CURRICULUM.md` for 30 stable topic IDs, `STUDY_PLAN.md` for routes, `PROGRESS.md` for actual evidence, and `RESOURCES.md` for inspected source pins. Phase numbers organize content; topic prerequisites control study order.

The sibling `physics` repository is the organizational reference and a source of application questions. No physics-specific degree goal, career plan, study budget, or learner completion has been adopted here. Each repository owns its files. Link actual overlapping work when useful and assess its scope before reusing evidence.

## Current material and evidence

Reference module: `notes/phase-1-foundations/01-statements-direct-proofs/`

This module covers only the first part of **1c**, not all logic, sets, functions/relations, induction, or proof methods. Other topic entries are coverage plans awaiting lessons and rubrics. Do not present a phase README as a complete course.

The original five notebooks are in `notebooks/archive/`, unchanged and checksum-verified. `docs/MIGRATION.md` lists known defects. Use `notebooks/binomial-distribution.ipynb` for the current binomial reference example; neither old nor new code establishes learner mastery.

No starting level, preferred route, textbook ownership, or weekly allocation is recorded. Inspect learner evidence before diagnosing or assigning work. Keep plans and actual activity distinct.

## Teaching and logs

Keep dated attempts, assistance, assessment reports, and learner reflections in the module's `learner-work.md`, using `templates/learner-log-template.md`. Link supporting files from the log and `PROGRESS.md`. Ask for a learner-authored reflection; do not write it on their behalf. Record reported timing as reported, unknown timing as unknown.

Use the [external-course workflow](../../.agents/skills/external-course/SKILL.md) to track outside courses. [EXTERNAL_COURSES.md](../../EXTERNAL_COURSES.md) indexes course records and historical checkpoints imported from Roam Research. Resource candidates are not enrollment or assigned homework. Select and verify the actual edition/section before assigning pages or problem numbers. There is no imported book-library integration.

## Computation and checks

Use `pyproject.toml` and the committed `uv.lock`; `uv sync --locked` creates a local environment. There is no importable package named `math` and no dependency on the sibling `physics` or `quantum` package. Prefer NumPy arrays to `np.matrix`; distinguish `@` from elementwise multiplication and `.T` from conjugate transpose.

Record shapes, domains, seeds, model assumptions, error tolerances, and physical units where relevant. Use SymPy/exact arithmetic for exact claims, and independent analytical cases or trusted numerical routines for numerical checks. Keep large cell outputs out of commits.

Commands:

```sh
python3 tools/agent_config.py check
python3 -m unittest discover -s tools/tests
uv run ruff check tools
uv run jupyter lab
```

For a ChatGPT study packet:

```sh
python3 tools/agent_config.py export --skill tutor-session --module notes/phase-1-foundations/01-statements-direct-proofs > /tmp/math-study.md
```

The exporter includes README/notes/problems, guidance, and recorded context, but excludes separate answer keys. Use an assessment-only export for closed-book work. Linked evidence is not automatically included.
