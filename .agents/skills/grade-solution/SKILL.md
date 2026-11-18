---
name: grade-solution
description: Grades a learner's mathematical or computational solution with a verdict, earliest faulty step, concept gap, next action, and sanity check. Use when the learner submits an attempt, derivation, proof, code result, or asks whether their answer is correct.
---

# Grade an attempted solution

Read `AGENTS.md`, `docs/agents/PROFILE.md`, `docs/agents/tutoring.md`, and the relevant problem/notes. Use a separate answer key to verify after the learner's attempt. For a numerical result, inspect model assumptions and conventions, not just the final number.

Return these five pieces:

1. **Verdict:** Correct (sound reasoning); Correct-but-brittle (right result with an unjustified step); Incomplete (missing work); or Wrong (incorrect result or real misconception).
2. **First faulty step:** identify the earliest wrong, missing, or brittle line. For correct work say none.
3. **Root cause:** explain the underlying idea; distinguish a local arithmetic slip from a conceptual gap without guessing what the learner thinks.
4. **Next action:** one specific hint, step to redo, linked notes section, changed-number retest, or next problem. For correct work, ask one transfer/limiting-case question.
5. **Sanity check:** units, signs, limiting behavior, normalization, substitution, or an independent numerical check.

Be precise and patient. Match rigor to the learner's phase. Prefer a useful hint to a full solution; provide a worked answer if explicitly requested and label the work assisted. A graded single problem does not satisfy an entire module gate. Record assistance and apply the shared mastery requirements before editing any completion checkbox.
