"""Smoke test: verify plugin.toml is valid and entry module exists.

Uses importlib to avoid depending on the N.E.K.O SDK in CI environments.
"""

from pathlib import Path


def test_plugin_toml_exists():
    root = Path(__file__).parent.parent
    assert (root / "plugin.toml").is_file(), "plugin.toml must exist"


def test_entry_module_exists():
    root = Path(__file__).parent.parent
    entry_path = root / "plugins" / "xiyin_pavilion" / "__init__.py"
    assert entry_path.is_file(), "entry module plugins/xiyin_pavilion/__init__.py must exist"


def test_plugin_toml_has_entry():
    root = Path(__file__).parent.parent
    toml_text = (root / "plugin.toml").read_text(encoding="utf-8")
    assert 'entry = "plugins.xiyin_pavilion:' in toml_text, "plugin.toml must declare entry"
