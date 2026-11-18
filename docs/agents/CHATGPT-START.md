# ChatGPT study handoff

From the repository root, export a current packet:

```sh
python3 tools/agent_config.py export --skill tutor-session --module notes/phase-1-foundations/01-statements-direct-proofs > /tmp/math-study.md
```

The packet contains shared guidance, the math profile, selected workflow, goals, curriculum/study plan/resources, current progress, and module README/notes/problems. It excludes separate solutions/answer-key files. Worked examples remain in lesson notes, so this is an instructional packet.

For a closed-book assessment, use only its learner-facing assessment file with `--assessment notes/path/to/diagnostic.md` or `--assessment assessments/path/to/diagnostic.md` and `--skill diagnose-prereqs`. Those paths are examples; the diagnostic must first be authored with a separate key. The exporter excludes module content in assessment mode. Review assessment wording and the packet before use; a filename cannot guarantee that an authored prompt contains no answers.

For an adopted outside course, use `--skill external-course --external-course external-courses/course-record.md`, optionally adding a local module. This exports a saved record, not account content.

Attach the packet and ask:

> Follow this repository's guidance. State the target and recorded evidence, then teach interactively one question at a time. Keep assistance separate from mastery. Ask for missing source/evidence content when needed. At the end propose a dated log and progress changes based only on actual work for me to save.

For an unaided assessment, ask the tutor to present the prompt and wait without hints. Report actual elapsed time and assistance, then submit completed work for grading. Supply a separate key afterward if needed. ChatGPT without local tools cannot open local links or save repository files.
