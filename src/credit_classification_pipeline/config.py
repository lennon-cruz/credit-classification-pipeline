from pathlib import Path
from typing import Any
import yaml

# Resolve project root relative to this file
PROJECT_ROOT = Path(__file__).resolve().parents[2]
CONFIG_DIR = PROJECT_ROOT / "configs"

def load_config(config_file: str = "data.yaml") -> dict[str, Any]:
    """Loads and returns a YAML configuration file from the configs directory."""
    target_path = CONFIG_DIR / config_file
    if not target_path.exists():
        raise FileNotFoundError(f"Configuration file not found: {target_path}")

    with open(target_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def get_absolute_path(relative_path: str) -> Path:
    """Utility to turn any relative string path into an absolute Path from project root."""
    return PROJECT_ROOT / relative_path