import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("validate_text", ROOT / "tools" / "validate_text.py")
MOD = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MOD)


def test_width_overflow_detected():
    errors = MOD.validate_pages(
        "WWWW",
        max_width_px=24,
        max_lines_per_page=2,
        glyph_widths={"W": 8},
        default_width=8,
    )
    assert errors


def test_valid_text_passes():
    errors = MOD.validate_pages(
        "Hi\nOK",
        max_width_px=32,
        max_lines_per_page=2,
        glyph_widths={},
        default_width=8,
    )
    assert errors == []
