import typer

app = typer.Typer(help="SOAR‑Lite CLI")

@app.command()
def init():
    """
    Initialize configuration and example playbooks.
    """
    typer.echo("Initializing SOAR‑Lite…")
    # TODO: bootstrap config directory & example YAML

@app.command()
def run(playbook: str):
    """
    Execute a playbook immediately.
    """
    typer.echo(f"Running playbook: {playbook}")
    # TODO: load & execute


if __name__ == "__main__":
    app()
