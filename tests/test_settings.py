from pathlib import Path
import os
import yaml
from soar_cli.settings import Settings, get_settings, _SETTINGS_CACHE

def test_from_yaml(tmp_path: Path):
    cfg = {
        "database": {"uri": "sqlite:///tmp.db"},
        "connectors": {"slack": {"token": "x"}}
    }
    cfg_fp = tmp_path / "config.yml"
    cfg_fp.write_text(yaml.safe_dump(cfg))

    settings = Settings.from_yaml(cfg_fp)
    assert settings.database.uri.endswith("tmp.db")
    assert settings.connectors.slack.token == "x"

def test_env_override(monkeypatch, tmp_path: Path):
    cfg = {"database": {"uri": "sqlite:///orig.db"}, "connectors": {}}
    cfg_fp = tmp_path / "config.yml"
    cfg_fp.write_text(yaml.safe_dump(cfg))

    monkeypatch.setenv("SOAR_DB_URI", "sqlite:///override.db")
    monkeypatch.setenv("SOAR_LOG_LEVEL", "DEBUG")
    monkeypatch.setenv("HOME", str(tmp_path))  # trick get_settings path

    _SETTINGS_CACHE = None  # reset cache
    settings = get_settings()
    assert settings.database.uri.endswith("override.db")
    assert settings.log_level == "DEBUG"
