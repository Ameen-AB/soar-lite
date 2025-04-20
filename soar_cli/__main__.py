import typer
from .config import bootstrap_config
from .settings import get_settings
from .logging import configure_logging

app = typer.Typer(help="SOAR‑Lite CLI")

@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    """
    Pre‑flight: load settings & configure logging once.
    """
    try:
        settings = get_settings()
    except RuntimeError as err:
        # Allow `soar init` to run without existing config
        if ctx.invoked_subcommand != "init":
            typer.secho(str(err), fg=typer.colors.RED, err=True)
            raise typer.Exit(code=1)
        settings = None

    if settings:
        configure_logging(settings)
        ctx.obj = {"settings": settings}  # attach to Typer context


@app.command()
def init():
    """
    Initialize configuration and example playbooks.
    """
    typer.echo("Initializing SOAR‑Lite…")
    bootstrap_config()

@app.command()
def run(
    ctx: typer.Context,
    playbook: str = typer.Argument(..., help="Playbook YAML file"),
):
    """
    Execute a playbook immediately.
    """
    from structlog import get_logger
    log = get_logger()

    settings = ctx.obj["settings"]
    log.info("run.start", playbook=playbook)
    # TODO: actual engine call
    typer.echo(f"Would run: {playbook} with DB {settings.database.uri}")


if __name__ == "__main__":
    app()
