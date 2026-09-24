# RomLingo - Claude Code Instructions

RomLingo's canonical shared instructions live in `AGENTS.md`.

Before substantial work:

1. Read `AGENTS.md`.
2. If no game project is configured, follow `docs/setup-wizard.md` and guide the user through setup one question or one small related group at a time.
3. If working inside an existing game project, read that project's `AGENTS.md`, `project_config.json`, and relevant documentation before making game-specific changes.
4. Treat `input/` source game files as immutable.
5. Start unfamiliar games with a small vertical slice before expanding coverage.
6. Run relevant validation/tests after changes.

Do not duplicate the full RomLingo rules here. `AGENTS.md` remains the source of truth so Codex, Claude Code, and other compatible coding agents can share the same workflow.
