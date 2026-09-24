# RomLingo architecture

RomLingo separates four concerns that are easy to accidentally mix together:

1. **Source-game engineering** — extracting, encoding, relocating, and safely rebuilding script data.
2. **Language analysis** — understanding the actual localized line and its linguistic features.
3. **Lesson design** — selecting what is pedagogically useful at the learner's configured level.
4. **Presentation constraints** — fitting the resulting lesson into the game's real font, textbox, script, and memory limits.

A mature game adapter should make the pipeline reproducible from a verified clean source:

```text
verified source
    v
localized base / translation dependency
    v
script extraction
    v
structured dialogue
    v
lesson generation + human/agent review
    v
layout validation
    v
encoding + allocation + repointing
    v
rebuilt development image
    v
playtest / regression checks
    v
distributable patch
```

Generic tools should not encode assumptions from a single game. Put game-specific logic beneath `projects/<project>/` until it is proven reusable.
