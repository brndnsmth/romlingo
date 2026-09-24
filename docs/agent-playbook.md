# RomLingo Agent Playbook

This document expands on the short root `AGENTS.md`. Read the sections relevant to the current task rather than treating this as mandatory context for every edit.

## 1. Product goal

The game remains the main experience. Educational content should explain language encountered during normal play rather than replace the game with textbook dialogue.

The framework should remain language-agnostic. Language-specific behavior belongs in profiles, configuration, lesson rules, dictionaries, and game adapters rather than being hardcoded into the general pipeline.

Do not assume a target language uses a particular alphabet, whitespace model, word order, morphology, punctuation system, text direction, or rendering behavior. Spanish is used as the primary documentation example only.

## 2. Localization is authoritative

Localization often changes jokes, idioms, sentence structure, register, terminology, references, and characterization.

Therefore:

- extract the actual target-language text
- use other-language scripts only as secondary context
- build the lesson from the localized line the player really sees

Regional variation should usually become a teaching opportunity rather than a reason to rewrite professional localization.

## 3. Analyze before mass editing

For each new game, determine as much as practical about:

- platform/format/revision
- text encoding
- script storage
- compression
- pointer representation
- control codes
- font/glyph coverage
- fixed-width versus variable-width rendering
- textbox dimensions and visible line count
- text buffers
- free space and/or expansion options
- safe repointing strategy

Record verified discoveries in the project's own documentation and nested `AGENTS.md`.

## 4. Reproducibility

Prefer scripts over manual binary edits once a technique is understood.

A typical project-specific pipeline may eventually look like:

```text
source
  -> verify
  -> apply translation dependency if required
  -> extract text/script data
  -> generate/select lesson data
  -> validate glyphs/layout/control codes
  -> encode/repoint/insert
  -> build
  -> run automated checks
  -> playtest
  -> create patch
```

Keep original files immutable and preserve known-good builds.

## 5. Structured data first

Do not write generated educational prose directly into unknown binary locations as a first step.

Prefer structured extracted dialogue such as:

```json
{
  "id": "npc_city_001",
  "location": "City",
  "speaker": "NPC",
  "original": "¿Has estado alguna vez aquí?",
  "address": "0x123456",
  "control_codes": [],
  "window_lines": 2
}
```

and separate lesson data such as:

```json
{
  "dialogue_id": "npc_city_001",
  "translation": "Have you ever been here?",
  "vocabulary": [
    {"target": "alguna vez", "meaning": "ever"}
  ],
  "grammar": {
    "pattern": "has + participle",
    "explanation": "This forms the present perfect."
  }
}
```

Review and validate content before encoding it into the game.

## 6. Teaching priorities

Prioritize concepts that are frequent, reusable, important to comprehension, useful in conversation, or likely to recur naturally.

Lower priority includes obscure one-off terms unless they are necessary for the current scene.

Beginner lessons should be concrete and short. Intermediate lessons should emphasize reusable patterns. Advanced lessons should reduce basic translation and focus more on idiom, register, nuance, and natural phrasing.

## 7. Language-specific pedagogy

Determine teaching priorities from the actual target language instead of from a language-family template. Relevant features may include morphology, syntax, particles, agreement, tense/aspect, cases, classifiers, writing-system knowledge, pronunciation, register, compounds, idioms, or other language-specific structures.

Do not teach a category merely because it appears in another RomLingo project. The lesson system should reflect the language the player is actually learning.

### Spanish documentation example

For Spanish, useful concepts may include:

- grammatical gender and agreement
- articles and contractions
- verb conjugation
- ser vs. estar
- preterite vs. imperfect
- object pronouns
- subjunctive when level-appropriate
- formal/informal address
- regional vocabulary and register
- idioms and common expressions

These are examples of how a language profile can guide lesson selection. They are not part of the core RomLingo architecture.

## 8. Writing-system and rendering assumptions

Treat the writing system as a project-specific engineering constraint. Investigate:

- character repertoire and encoding
- glyph availability and font capacity
- line-breaking rules
- whether spaces reliably mark word boundaries
- punctuation behavior
- text direction and shaping requirements when relevant
- whether learner-language annotations need characters the original game never renders

Do not simplify or transliterate the target language merely to avoid engineering work unless the project explicitly chooses that teaching design and documents the tradeoff.

## 9. Translation fading and review

For lower-level learners, early interactions can include fuller translation and explanation. Later encounters can use shorter reminders, recall prompts, or no explanation for familiar concepts.

Do not fade assistance merely because a fixed number of dialogue lines passed. Base it on concept familiarity when the game/project can track that information.

Use quizzes sparingly. Gameplay remains primary.

## 10. Textbox limits are hard constraints

A lesson that does not fit is broken.

Never silently truncate educational text.

Validate:

- rendered width
- visible lines
- page breaks
- control codes
- buffer limits
- variable expansion
- font coverage

Prefer pixel/glyph-width validation when a variable-width font is used.

Break long lessons across clean pages instead of squeezing them into unreadable layouts.

## 11. Control codes and variables

Treat newlines, page breaks, pauses, waits, portraits, colors, speaker changes, text-speed commands, player-name variables, item variables, branches, and unknown control bytes as structured script data rather than normal text.

Unknown control bytes should remain preserved until understood.

## 12. Fonts

Verify every character needed by the target localization and learner-language lesson text.

The required character set depends on both the target language and the learner-language annotations. Inventory the actual characters needed for the project rather than assuming a preselected character subset.

For the Spanish examples in this repository, that commonly includes accented vowels, ñ, ü, ¿, and ¡. Other projects may require entirely different glyph inventories or renderer behavior.

Do not strip meaningful orthography merely because a reduced character set would be easier unless there is a documented technical reason and the project explicitly accepts that compromise.

## 13. Vertical slices

A first slice should intentionally cover varied script cases, not simply the first N strings.

Good coverage includes:

- short text
- long text
- multi-page text
- variables
- control codes
- environmental interactions
- special characters
- at least one representative lesson
- at least one review/quiz if the design uses them

Do not scale until this slice reliably builds and plays.

## 14. Environmental language

Useful learning material can come from NPCs, signs, bookshelves, TVs, computers, posters, shops, items, menus, tutorials, battle messages, and maps.

Environmental actions often create especially strong context for vocabulary.

## 15. Preserve character voice

Prefer:

```text
original character dialogue
  -> dialogue ends
  -> visually/structurally distinct language note
```

rather than rewriting every NPC to sound like a tutor.

## 16. Lesson review checklist

Before insertion, ask:

- Does the translation match the actual localization?
- Is the linguistic explanation accurate?
- Is the regional note accurate and relevant?
- Is it suitable for the learner level?
- Is the concept useful?
- Was it already explained recently?
- Can it be shorter?
- Does it fit safely?

## 17. Testing

Automate checks where practical. A mature pipeline may validate:

- source revision/hash
- encoding
- glyph availability
- text/page width
- pointer targets
- bank boundaries
- script structure
- output size
- patch creation/application

Then playtest relevant paths. At minimum verify booting, save/load, dialogue progression, variables, special characters, page breaks, map transitions, menus, and any affected battle or scripted sequences.

## 18. Regression discipline

When a formatting or pointer change breaks something that previously worked, compare against the last known-good build and make the smallest reliable correction.

A theoretically cleaner implementation is not an improvement if it renders or behaves worse.

## 19. Release discipline

Use prerelease versioning honestly. Do not call a largely untested patch `1.0`.

Release patch data and original educational/tooling material, not the commercial source game.

Document the exact required source revision/hash and any translation dependency.

## 20. Quality principle

When forced to choose between more lesson coverage and fewer polished/correct lessons, choose the latter.
