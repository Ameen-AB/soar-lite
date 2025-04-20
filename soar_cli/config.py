import shutil
from pathlib import Path
import typer

CONFIG_STUB = Path(__file__).parent.parent / "config" / "config.yml"
PLAYBOOK_STUB = Path(__file__).parent.parent / "playbooks" / "example_playbook.yml"

def get_config_dir() -> Path:
    """
    Returns the path to the user's soar-lite config dir, e.g. ~/.soar_lite
    """
    return Path.home() / ".soar_lite"

def bootstrap_config():
    cfg_dir = get_config_dir()
    playbook_dir = cfg_dir / "playbooks"

    # Create directories
    cfg_dir.mkdir(parents=True, exist_ok=True)
    playbook_dir.mkdir(parents=True, exist_ok=True)

    # Copy config.yml if not exists
    dest_cfg = cfg_dir / "config.yml"
    if not dest_cfg.exists():
        shutil.copy2(CONFIG_STUB, dest_cfg)
        typer.echo(f"Created {dest_cfg}")
    else:
        typer.echo(f"Config already exists at {dest_cfg}")

    # Copy example playbook
    dest_pb = playbook_dir / "example_playbook.yml"
    if not dest_pb.exists():
        shutil.copy2(PLAYBOOK_STUB, dest_pb)
        typer.echo(f"Copied example playbook to {dest_pb}")
    else:
        typer.echo(f"Playbook already exists at {dest_pb}")
