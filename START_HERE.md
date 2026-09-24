# Start Here

RomLingo is designed to be used with an agentic coding tool working directly inside this repository.

The primary recommended environments are **Codex** and **Claude Code**. Other similar coding agents can also work well when they can read repository instructions, inspect files, run shell/Python tools, edit code, and execute tests.

## Option A: Codex

Open this repository in Codex and start with:

```text
Start a new RomLingo project.
Follow AGENTS.md and guide me through setup one question at a time.
Do not start modifying the game until you have enough information and have inspected the supplied files.
```

## Option B: Claude Code

Open the repository in Claude Code. RomLingo includes `CLAUDE.md`, which points Claude Code to the shared RomLingo instructions. Start with:

```text
Start a new RomLingo project.
Use the repository instructions and guide me through setup one question at a time.
Do not start modifying the game until you have enough information and have inspected the supplied files.
```

## Other similar coding agents

RomLingo does not depend on a particular model vendor. A suitable agent should be able to:

- read `AGENTS.md` and project documentation
- inspect uploaded/local game files
- run Python and shell commands
- create and edit project files
- run tests and validators
- keep verified game-specific findings in the project directory

If an agent uses a different instruction-file convention, point it at `AGENTS.md` and `docs/setup-wizard.md`.

## What happens next

The agent should ask for the target language first and continue through the setup wizard.

You should not need to know ROM hashes, pointer formats, text encodings, or similar technical details in advance. The agent should investigate those itself.

## What you should have ready

Usually:

1. A legally obtained copy of the game you want to modify.
2. The target language you want to learn.
3. Your approximate learning level.
4. Any existing translation patch needed to make the target localization available.

Everything else can normally be decided during setup.

## Recommended first milestone

For an unfamiliar game, choose a small section such as the opening 15-30 minutes, first town, first route, or first dungeon.

The first goal is not full-game coverage. The first goal is proving that RomLingo can safely:

```text
extract -> teach -> reinsert -> render -> play -> patch
```

Once that loop works reliably, expand it.
