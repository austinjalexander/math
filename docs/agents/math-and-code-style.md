# Mathematical writing and computation

## Definitions and proofs

Use `$...$` for inline math and `$$...$$` for display equations, with blank lines around display math. Specify domains, quantifiers, assumptions, and symbol meanings. State whether $\mathbb N$ includes zero when it matters. Distinguish an implication from its converse, and existence from uniqueness.

A proof must cover arbitrary permitted inputs. Use explicit witnesses for existence, both directions for an equivalence, and justified steps for transformations. A counterexample refutes a universal claim; finitely many successful examples do not establish one. State theorem hypotheses at the point of use. Mark exploratory conjectures and unproved claims.

For calculations, show reproducible algebra and check domain restrictions, signs, limits, dimensions, or substitution. For applied work, distinguish the mathematical model from the system it represents and identify approximation assumptions.

## Code and notebooks

Use Python 3.12+ and the local `uv` environment. Use NumPy arrays with explicit shapes; matrix products use `@`. For complex vectors, use conjugate transpose where appropriate. Do not create a top-level module or package named `math`.

Separate symbolic/exact equality from floating-point closeness. State absolute/relative tolerances, conditioning concerns, seeds, sample counts, and convergence checks. Validate a method against an analytical case or independent routine when meaningful. Simulation supports numerical claims, not universal proof or experimental measurement.

Keep current notebook outputs small or cleared. Save intentional figures beside the analysis. Do not rewrite archived notebook contents as part of formatting or output cleanup. Use repository-relative links in Markdown; use the profile's actual commands and avoid imports from sibling repositories.
