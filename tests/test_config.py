import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("validate_config", ROOT / "tools" / "validate_config.py")
MOD = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MOD)


def test_example_config_is_valid():
    data = json.loads((ROOT / "project_config.example.json").read_text(encoding="utf-8"))
    assert MOD.validate(data) == []


def test_missing_language_is_rejected():
    data = {
        "project_name": "x",
        "game": {"title": "x", "platform": "gba"},
        "language": {"learner_language": "English"},
        "learning": {"learner_level": "A2", "lesson_density": "balanced"},
    }
    errors = MOD.validate(data)
    assert any("target_language" in error for error in errors)
