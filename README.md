# math

A self-study home for **engineering mathematics, applied mathematics, theoretical mathematics, and abstract mathematics**. Build fluency in calculation, modeling, proof, and computation, then connect those skills through independent work.

This repository follows the learning approach used in the sibling `physics` repository: a curriculum, a prerequisite-aware study plan, evidence-based progress, reusable lesson templates, and portable tutor guidance. Mathematics has its own broad scope; physics and quantum computing are application partners.

## Start here

1. Read [the goals](GOALS.md) and [curriculum](docs/CURRICULUM.md).
2. Use [the study plan](STUDY_PLAN.md) to choose a route and check prerequisites against [recorded progress](PROGRESS.md).
3. Start with a diagnostic if readiness is unknown. The first authored lesson is [statements and direct proofs](notes/phase-1-foundations/01-statements-direct-proofs/README.md); most of the curriculum is a coverage plan awaiting lessons.
4. Study notes, attempt required problems, correct them, and take a timed unaided exit assessment. Record your own reflection before checking a progress item.

## Learning paths

- [Foundations and reasoning](notes/phase-1-foundations/README.md): algebra, functions, logic/proof, discrete mathematics, and computing.
- [Calculus and linear algebra](notes/phase-2-calculus-linear-algebra/README.md): differential/integral/multivariable/vector calculus and linear algebra.
- [Engineering and applied mathematics](notes/phase-3-engineering-applied/README.md): differential equations, transforms, PDEs, numerical methods, optimization, and control.
- [Analysis, probability, and statistics](notes/phase-4-analysis-probability/README.md): real/complex analysis, probability, inference, measure, and stochastic processes.
- [Abstract structures](notes/phase-5-abstract-structures/README.md): proof-based linear algebra, groups, rings/fields, topology, and number theory.
- [Advanced connections](notes/phase-6-advanced-connections/README.md): geometry, functional analysis, dynamics, algorithms/information, and independent projects.

Phases organize subjects; their prerequisites determine the learning order. Abstract mathematics can begin before the applied path is finished.

## Repository layout

```text
GOALS.md                 mathematical goals and scope
STUDY_PLAN.md            prerequisite routes and session planning
PROGRESS.md              learner evidence and completion gates
docs/CURRICULUM.md       topic blueprint with stable identifiers
RESOURCES.md             source pins and selection policy
EXTERNAL_COURSES.md      outside-course index and return queue
external-courses/        provider records, created when a course is adopted
notes/                  phase maps and authored lesson modules
notebooks/              current computational work and preserved archive
projects/               project index and acceptance workflow
templates/              notes, problems, learner logs, courses, projects
AGENTS.md               shared assistant instructions
docs/agents/            repository profile and teaching conventions
.agents/skills/         canonical tutoring and authoring workflows
.cursor/rules/          small contextual adapters
CLAUDE.md               shared-instruction import
.claude/skills/         relative links to canonical workflows
tools/                  configuration checks and study-packet export
```

## Computation

Use Python 3.12+ and [uv](https://docs.astral.sh/uv/). This is a notebook environment, with no Python package named `math` that could shadow the standard library.

```sh
uv sync --locked
uv run jupyter lab
python3 tools/agent_config.py check
uv run ruff check tools
```

The [current binomial notebook](notebooks/binomial-distribution.ipynb) provides an exact PMF calculation, seeded simulation, and independent numerical checks. It is a reference example; running it records no learner mastery.

## Existing material and related repositories

All five original notebooks are preserved byte-for-byte in [the archive](notebooks/archive/README.md), including original filenames and outputs. They contain old kernel metadata and known mathematical/code defects; the [migration record](docs/MIGRATION.md) lists them. Active lessons should use reviewed material.

Keep mathematical derivations here and link application-specific experiments from `physics` or `quantum` when useful. Each repository owns its instructions, environments, and learner records. There are no cross-repository runtime or configuration dependencies.

[Agent setup](docs/agents/README.md) explains the shared tutor workflows and ChatGPT handoff. [MIT OCW Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/) is the initial proof/discrete reference; the other inspected source pins are in [RESOURCES.md](RESOURCES.md).

## License

[MIT](LICENSE). External resources remain under their own licenses; links do not relicense their content.
