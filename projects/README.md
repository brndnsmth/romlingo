# Game projects

Game-specific adapters, configuration, documentation, and data should live here.

Suggested layout:

```text
projects/
+-- example-game-spanish/
    +-- project_config.json
    +-- README.md
    +-- adapter/
    +-- docs/
    +-- data/
    +-- tests/
```

Keep reusable tooling in the top-level `tools/` or a future reusable Python package instead of duplicating it across projects.

## Project-scoped agent instructions

Each game project should maintain a concise `AGENTS.md` containing verified game-specific facts and required test commands. Codex, Claude Code, and other similar agents should use these project-scoped instructions so they do not need to rediscover or load unrelated game details. A project may also include a tiny agent-specific adapter file when useful, but `AGENTS.md` should remain the canonical game-specific source of truth.
