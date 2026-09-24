# Patch and release guidance

RomLingo should distribute patches and original project material rather than commercial game images.

## Possible patch formats

- **BPS** — useful general-purpose binary patch format.
- **IPS** — simple and widely supported but has format limitations; verify suitability first.
- **UPS** — another ROM-oriented patch option.
- **xdelta/VCDIFF** — often useful for larger binaries/disc-based projects.
- **PPF** — may be appropriate for some disc-image workflows.

A game adapter should record exactly which source revision/hash is expected.

## Recommended release bundle

```text
release/
+-- README.md
+-- PATCHING.md
+-- CHANGELOG.md
+-- checksums.txt
+-- patches/
    +-- <project>.<patch-format>
```

Do not ship the source or patched commercial game image.
