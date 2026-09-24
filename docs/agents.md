# Using RomLingo with coding agents

RomLingo is built primarily around **Codex** and **Claude Code**, but the workflow is intentionally portable to other similar repository-aware coding agents.

## Canonical instructions

`AGENTS.md` is the shared source of truth for RomLingo behavior. Keep it concise and stable. Detailed procedures belong in `docs/`, while verified game-specific reverse-engineering facts belong under `projects/<slug>/`.

## Codex

Use the repository-root `AGENTS.md` and any project-scoped `AGENTS.md` files as the main operating instructions. Start new projects through `docs/setup-wizard.md`.

## Claude Code

The root `CLAUDE.md` is intentionally small. It directs Claude Code to read and follow the canonical RomLingo instructions rather than duplicating the full rule set. Game-project templates include the same lightweight adapter pattern.

## Other similar agents

An agent can use RomLingo effectively if it can:

- read repository documentation and instruction files
- inspect local binary files
- run Python and shell commands
- create/edit files
- execute tests and validators
- preserve project-specific knowledge across work sessions

If the tool uses another instruction-file convention, configure or prompt it to read `AGENTS.md`, then follow `docs/setup-wizard.md` for a new project.

## Design rule

Do not fork the methodology by maintaining separate full instruction sets for every agent. Agent-specific files should be adapters only. The shared RomLingo workflow and safety rules belong in `AGENTS.md` and `docs/`.
