# RomLingo Setup Wizard

Use this document when starting a new game-specific RomLingo project.

The interaction should feel like a guided setup wizard. Ask one question, or one small group of closely related questions, at a time. Do not dump the whole questionnaire on the user.

## 1. Target language

Ask directly rather than limiting the user to a predefined family or list:

```text
What language do you want to learn?

Example: Spanish
```

Accept any target language. Spanish is used in this documentation as the primary example, not as a restriction.

Store as `language.target_language`.

## 2. Learner/explanation language

Ask what language translations and explanations should use.

Default to English only when the user has not specified another preference.

Store as `language.learner_language`.

## 3. Regional variety

Ask only when it meaningfully affects teaching.

For Spanish, for example:

```text
Which variety should lessons emphasize?

[1] Mexican / Latin American Spanish
[2] Spain Spanish
[3] Preserve the game's localization and explain important differences
[4] Other
```

The normal default is to preserve the game's localization and explain useful regional differences rather than rewriting the game.

Store as `language.target_variant`.

## 4. Source game

Ask the user to provide the legally obtained source game.

After receiving it, investigate rather than asking the user to identify:

- file format/platform
- file size
- CRC32
- MD5
- SHA-1/SHA-256
- header state when relevant
- likely region/revision
- built-in language options
- useful public technical information when research is available

Treat the source file as immutable.

## 5. Translation base

Ask:

```text
Is the target language already present in this version?

[1] Yes
[2] No - I have a translation patch
[3] No - I have an already translated version
[4] I'm not sure
```

If a fan translation is supplied, record its project/source and license or distribution requirements when discoverable.

Keep the patch chain reproducible.

## 6. Learner level

Ask:

```text
What is your current level?

[0] Absolute beginner
[1] A1 - Beginner
[2] A2 - Elementary
[3] B1 - Intermediate
[4] B2 - Upper intermediate
[5] C1+ - Advanced
[6] Custom
```

Store as `learning.learner_level`.

## 7. Teaching intensity

Ask:

```text
How heavily should the game teach?

[1] Light
    Occasional translation and vocabulary help.

[2] Balanced
    Frequent useful explanations without stopping constantly.

[3] Heavy
    Detailed teaching of important dialogue and recurring grammar.

[4] Immersion
    Minimal learner-language translation.

[5] Custom
```

Store as `learning.lesson_density`.

## 8. Learning features

Offer sensible defaults rather than requiring individual answers to everything.

Recommended defaults:

```text
[X] Translation
[X] Vocabulary
[X] Grammar
[X] Sentence breakdown
[X] Important expressions
[X] Verb/form explanations
[X] Regional usage notes
[X] Memory aids when useful
[X] Occasional quizzes
[X] Concept review
[X] Spaced repetition when technically feasible
```

Optional:

```text
[ ] Pronunciation
[ ] Phonetic spelling
[ ] IPA
[ ] Literal translation
[ ] Cultural notes
[ ] Etymology
[ ] Word-family notes
[ ] Cognate notes
[ ] False-friend warnings
```

Do not put every enabled feature in every lesson.

## 9. First milestone

Ask how much the first development pass should cover:

```text
[1] Opening / first 15-30 minutes
[2] First major area
[3] First chapter / dungeon
[4] Several hours
[5] Entire game
[6] Custom milestone
```

For an unfamiliar game, recommend a small vertical slice even if the eventual goal is the entire game.

## 10. Target environment

Ask only when useful for testing or implementation:

```text
[ ] Original hardware / flash cart
[ ] RetroArch
[ ] Steam Deck
[ ] MiSTer
[ ] Analogue Pocket
[ ] mGBA
[ ] Dolphin
[ ] DuckStation
[ ] Other
[ ] No preference
```

## 11. Patch output

Ask only after the platform and modification strategy are understood enough to know which formats are realistic.

Possible formats include BPS, IPS, UPS, xdelta/VCDIFF, and PPF.

Do not promise an unsuitable format simply because it was requested.

## 12. Summarize and persist

Before substantial implementation, show a concise summary and create the project directory/configuration.

Example:

```text
Project: Example Game - Spanish Learning
Platform: GBA
Target language: Spanish
Variant: Preserve localization; explain Mexican differences
Explanation language: English
Learner level: A2
Teaching intensity: Heavy
First milestone: Opening through first town
Target environment: RetroArch / Steam Deck
```

Then create `projects/<slug>/` from the template and begin technical analysis.
