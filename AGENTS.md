# RomLingo Agent Instructions

    +----------------------------------------------------------+
    |                         ROMLINGO                         |
    |             PLAY THE GAME. LEARN THE LANGUAGE.          |
    +----------------------------------------------------------+

## Mission

Build language-learning patches around the **actual localized text** of legally obtained games while preserving the original game experience as much as practical.

RomLingo is agent-driven and designed primarily for Codex and Claude Code, while remaining usable with other similar repository-aware coding agents. The helper scripts support the work; they are not a universal one-click ROM patcher.

`AGENTS.md` is the canonical shared instruction set. Agent-specific entry files such as `CLAUDE.md` should stay thin and point back here instead of duplicating these rules.

## Before doing substantial work

If no game-specific project is configured, follow `docs/setup-wizard.md` and guide the user through setup **one question or one small related group at a time**.

Do not ask the user for technical facts that can be inferred from supplied files.

If a project already exists, read its `projects/<project>/AGENTS.md` and project configuration before making game-specific changes.

## Sources of truth

Use the relevant documentation only when the task needs it:

- `docs/setup-wizard.md` - onboarding and project configuration
- `docs/agents.md` - Codex, Claude Code, and other agent usage
- `docs/agent-playbook.md` - detailed development and teaching rules
- `docs/architecture.md` - repository/tooling architecture
- `docs/project-workflow.md` - project lifecycle and vertical-slice process
- `docs/lesson-format.md` - structured lesson data and presentation rules
- `docs/patching.md` - patch creation/distribution guidance

Do not load every document for every small edit.

## Non-negotiable rules

1. **The target localization is authoritative.** Extract and teach the text actually present in the target game. Do not assume another language's script is equivalent.
2. **Never modify source game files in place.** Treat files under `input/` as immutable.
3. **Do not commit commercial game images, BIOS files, or patched commercial game images.**
4. **Preserve existing fan-translation attribution and licensing requirements.**
5. **Start with a vertical slice.** Solve 5-20 representative interactions before attempting broad coverage.
6. **No silent text truncation.** Overflow, invalid pointers, missing glyphs, or structural script errors should fail validation.
7. **Prefer actual rendered/pixel width** over character count when the game uses a variable-width font.
8. **Keep lessons concise.** Fewer polished, correct lessons are better than broad low-quality coverage.
9. **Preserve character voice.** Prefer a distinct lesson message after authentic dialogue rather than rewriting NPCs into teachers.
10. **Test after changes.** Run relevant automated checks and preserve known-good builds.

## Agent workflow

For a new project:

```text
GUIDED SETUP
  -> identify/verify source files
  -> analyze the game
  -> document text/script/font constraints
  -> extract a representative vertical slice
  -> create structured lessons
  -> validate layout/encoding/control codes
  -> insert into a working copy
  -> boot/playtest
  -> generate a distributable patch
  -> expand coverage only after the slice is stable
```

## Project-specific knowledge

Store discoveries under `projects/<slug>/` rather than bloating this root file.

A mature project should contain or generate:

```text
projects/<slug>/
├── AGENTS.md
├── project_config.json
├── docs/
├── data/
├── tools/
├── tests/
└── README.md
```

Use the nested project `AGENTS.md` for verified game-specific facts such as encoding, pointer rules, control codes, font metrics, text-bank layout, expansion strategy, and required test commands.

## Tooling style

Prefer reproducible scripts over manual hex edits once a technique is understood.

General-purpose helpers belong in `tools/`. Game-specific extraction/insertion logic belongs under the relevant project until it is clearly reusable.

Do not pretend an unknown ROM format is supported. Investigate, document evidence, prototype safely, and build an adapter.

## Language support

RomLingo is language-agnostic. Do not assume that the target language:

- uses a particular alphabet or writing system
- uses spaces between words
- uses subject-verb-object word order
- has grammatical gender or cases
- conjugates verbs in a Spanish-like way
- can be represented by the game's existing font or encoding
- has the same punctuation, shaping, line-breaking, or text-direction needs as the learner language

Spanish is the primary documentation example only. Analyze the target language and the target game's localization independently for every project.

## Language-learning behavior

Adapt explanations to the configured learner level and the actual linguistic features of the target language. Teach only concepts that are relevant to the language and useful in context.

Do not force every lesson feature into every interaction. Reuse concepts naturally and reduce explanation as familiarity grows.

## Completion standard

Before declaring a milestone complete, verify as applicable:

- source hashes/configuration are recorded
- game boots
- normal dialogue still works
- lesson pages advance correctly
- special characters and variables render correctly
- no known lesson overflow/truncation remains
- relevant automated tests pass
- patch output applies to the documented source revision
- release files do not contain the commercial source game
