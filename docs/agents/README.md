# Tutor and authoring setup

This repository keeps one canonical set of instructions and workflows. The shared approach follows `physics`, with a math-specific profile and no cross-repository dependencies.

- [AGENTS.md](../../AGENTS.md) is the entry point; [PROFILE.md](PROFILE.md) supplies scope, current material, evidence paths, and commands.
- [Tutoring](tutoring.md), [module structure](module-structure.md), and [math/code style](math-and-code-style.md) hold common conventions.
- [.agents/skills/](../../.agents/skills/) contains `tutor-session`, `grade-solution`, `diagnose-prereqs`, `author-module`, and `external-course`.
- [.cursor/rules/](../../.cursor/rules/) contains small always-on/contextual adapters.
- [CLAUDE.md](../../CLAUDE.md) imports the shared instructions; `.claude/skills/` contains relative links to canonical local skills.

Open the repository root in your assistant. Request the relevant workflow and module naturally, or explicitly name the skill where supported. After changes, reload project guidance or start a fresh session as appropriate for the tool. Local validation checks files and links; it does not prove a running assistant has loaded them.

```sh
python3 tools/agent_config.py check
```

For ChatGPT without repository file access, use [the handoff guide](CHATGPT-START.md). The generated packet carries selected content and actual recorded progress; it does not supply unseen linked work or access to local files. Review it before sharing, since progress and logs can contain personal information.
