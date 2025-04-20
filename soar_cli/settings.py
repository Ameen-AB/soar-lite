"""
settings.py
Load and validate ~/.soar_lite/config.yml (or env overrides) into a typed object.

Usage:
    from .settings import get_settings
    settings = get_settings()
"""
from __future__ import annotations
from pathlib import Path
import os
import yaml
from typing import Any, Dict
from pydantic import BaseModel, Field, ValidationError


class DatabaseCfg(BaseModel):
    uri: str = Field(..., description="SQLAlchemy‐style DB URI (e.g. sqlite:///…)")

class SlackCfg(BaseModel):
    token: str

class JiraCfg(BaseModel):
    url: str
    user: str
    api_token: str

class ConnectorsCfg(BaseModel):
    slack: SlackCfg | None = None
    jira: JiraCfg | None = None
    # Add more built‑ins here

class Settings(BaseModel):
    database: DatabaseCfg
    connectors: ConnectorsCfg
    log_level: str = Field("INFO", description="Root log level")

    @classmethod
    def from_yaml(cls, path: Path) -> "Settings":
        with path.open("r") as fh:
            data: Dict[str, Any] = yaml.safe_load(fh)
        return cls.model_validate(data)


_SETTINGS_CACHE: Settings | None = None

def get_settings() -> Settings:
    """
    Singleton accessor with env‑var overrides, cached for reuse.
    Precedence: ENV → YAML (default)
    """
    global _SETTINGS_CACHE
    if _SETTINGS_CACHE:
        return _SETTINGS_CACHE

    cfg_path = Path.home() / ".soar_lite" / "config.yml"
    try:
        settings = Settings.from_yaml(cfg_path)
    except FileNotFoundError as exc:
        raise RuntimeError(
            f"Config not found at {cfg_path}. Run `soar init` first."
        ) from exc
    except ValidationError as exc:
        raise RuntimeError(f"Invalid configuration: {exc}") from exc

    # Environment variable overrides (e.g. SOAR_DB_URI, SOAR_LOG_LEVEL)
    if db_uri := os.getenv("SOAR_DB_URI"):
        settings.database.uri = db_uri
    if log_level := os.getenv("SOAR_LOG_LEVEL"):
        settings.log_level = log_level

    _SETTINGS_CACHE = settings
    return settings
