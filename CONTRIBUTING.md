# Contributing to RomLingo

RomLingo benefits most from reusable contributions that help multiple game projects.

## Useful contribution areas

- script/text extractors and encoders
- font and glyph analysis
- variable-width text measurement
- pointer/repointing helpers
- compression/decompression adapters
- patch-generation integrations
- language profiles and lesson rules
- game-specific adapters
- automated validation and tests
- reverse-engineering documentation

## Ground rules

1. Do not commit commercial ROMs, ISOs, BIOS files, or patched commercial game images.
2. Keep user-supplied source files under ignored local directories such as `input/`.
3. Prefer reproducible scripts over undocumented manual hex edits.
4. Preserve the original localization unless a project's explicit goal requires changing it.
5. Keep linguistic content reviewable separately from binary/script modifications when practical.
6. Add tests or fixtures for reusable tooling.
7. Document game-specific assumptions, addresses, pointer formats, encodings, and known limitations.

## Game-specific work

Create a directory under `projects/` for project-specific code and notes rather than hardcoding one game's assumptions into generic framework helpers.

## Linguistic quality

A lesson should be accurate, concise, appropriate to the configured learner level, and based on the target localization actually present in the game.

When in doubt, prefer fewer high-quality lessons over broad but unreliable coverage.
