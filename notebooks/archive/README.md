# Original notebook archive

The five original notebooks are preserved unchanged, including old Python 3.5/Conda kernel metadata, filenames, and outputs. [The SHA-256 manifest](manifest.json) records every old/new path. Run `python3 tools/agent_config.py check` from the repository root to verify preservation.

- [Definitions](Definitions.ipynb): calculus definitions; connects to **2a**.
- [Theorems](Theorems.ipynb): calculus rule drafts; connects to **2a**. Contains incorrect power-rule expressions; see [migration notes](../../docs/MIGRATION.md).
- [Linear algebra](LinearAlgebra.ipynb): array/matrix notation drafts; connects to **2d**. Uses legacy `np.matrix` and inconsistent vector indexing notation.
- [Probability distributions](ProbablityDistributions.ipynb): short PMF/joint-distribution notes; connects to **4c**. Original misspelled filename retained for provenance.
- [Binomial distribution](BinomialDistribution.ipynb): PMF/plot draft; connects to **4c**. Calls `factorial` without an import and cannot run as written in a fresh kernel.

These are historical study artifacts, not assessed mastery or vetted reference lessons. Use [the current notebook index](../README.md) for active work. Archive revisions should preserve originals; place reviewed replacements outside this folder.
