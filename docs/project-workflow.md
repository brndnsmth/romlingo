# New project workflow

## 1. Intake

Collect the target language, learner language, regional preference, game input, translation dependency, CEFR level, teaching intensity, desired features, first milestone, test environment, and patch-output preference.

## 2. Verify immutable inputs

Calculate hashes and record exact filenames/revisions. Never edit the originals.

## 3. Establish the target-language base

If the game already contains the localization, use it directly. If it depends on a translation patch, reproduce that dependency from the verified source and document the resulting base hash.

## 4. Reverse engineer the script path

Find text storage, encoding, compression, pointers, control codes, terminators, font data, width behavior, and text-window limits.

## 5. Build a vertical slice

Choose 5–20 representative interactions and solve the complete round trip: extract -> lesson -> encode -> rebuild -> boot -> display -> advance -> save/load where relevant.

## 6. Add hard validation

Fail builds on unsupported glyphs, overflow, invalid pointers, overlaps, or other structural conditions that can be detected automatically.

## 7. Scale carefully

Expand content only after the vertical slice is reliable. Maintain known-good builds and regression fixtures.

## 8. Release patches, not games

Create patch artifacts against the documented source revision when technically suitable, and include checksums and patching instructions.
