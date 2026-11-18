# Repository overhaul — October 26, 2026

## Scope and model

The requested cleanup adopts the sibling `physics` repository's curriculum/study/evidence workflow for the broad scope of engineering, applied, theoretical, and abstract mathematics. The reference repository was inspected without modification. Its physics-specific career goals, degree mappings, hours, library tools, and project plans were not imported as math commitments.

Added a six-phase/30-topic blueprint, goals, prerequisite routes, an empty evidence tracker, source pins, templates, one complete proof lesson, portable tutor workflows, local adapters, a configuration/handoff tool, and a reproducible notebook environment. Phase maps are planned coverage; only the direct-proofs subtopic is currently a complete four-file lesson.

## Original material

All five notebooks moved from `notebooks/<original-name>.ipynb` to `notebooks/archive/<original-name>.ipynb` without editing their bytes. The [archive manifest](../notebooks/archive/manifest.json) records original paths, new paths, and SHA-256 hashes. The original license is retained. No original notebook is removed from the repository.

Observed issues in preserved drafts:

- `BinomialDistribution.ipynb` calls `factorial` without importing it. The current [binomial notebook](../notebooks/binomial-distribution.ipynb) supplies a separate runnable replacement.
- `Theorems.ipynb` writes the power-rule result as `na^{a-1}` instead of $na^{n-1}$ and the $x^4$ example limit as `3n^3` instead of $4a^3$.
- Linear algebra uses `np.matrix` and contains inconsistent vector-index notation. Future examples should use arrays and explicit shapes.
- Kernel metadata targets Python 3.5/Conda. Archived outputs are not evidence of execution in the new environment.

## Boundaries

No learner attempts, timed passes, reflections, provider enrollment, or prior mastery were inferred. No cross-repository symlinks, source code dependencies, global configuration changes, purchases, or schedules were introduced. The stable topic IDs allow future lessons to be added without pretending the entire roadmap already exists.

## Validation

Use `python3 tools/agent_config.py check` for required configuration, local links, topic/progress alignment, reference lesson/assessment consistency, and archive integrity. Use `python3 -m unittest discover -s tools/tests` for the export boundaries and archive-change detection. Use `uv run ruff check tools` for Python style; execute current notebooks in a fresh kernel before treating them as runnable examples. These checks validate the repository, not learner mastery.
