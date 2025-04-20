# SOAR‑Lite Orchestrator CLI

A command-line-first security orchestration and automation engine designed for rapid, scriptable workflows.

## 🚀 Features
- **Simplicity & Portability:** Single binary or pip-installable package with minimal dependencies.
- **Code-First Playbooks:** Define workflows in YAML, manage them as code.
- **Extensibility:** Connector SDK to integrate with CRMs, ticketing systems, cloud APIs.
- **Immutable Audit Trail:** Every action logged immutably using SQLite.

## 📦 Tech Stack
- CLI framework: Typer
- Packaging: Poetry
- Storage: SQLite (via SQLModel)
- Scheduling: APScheduler
- Logging: Structlog

## 🛠️ Project Structure

```text
soar-lite/
├── soar_cli/              # Main CLI application
│   ├── commands/          # CLI commands
│   ├── connectors/        # Integrations with external services
│   ├── sdk/               # Developer SDK for writing connectors
│   ├── engine.py          # Core engine (playbook execution logic)
│   ├── models.py          # Data models
│   └── storage.py         # Persistence (SQLite operations)
├── playbooks/             # Example and user playbooks
├── config/                # Configuration files
├── tests/                 # Test cases
├── docs/                  # Project documentation
├── README.md              # Project overview
└── pyproject.toml         # Poetry configuration
```

## ⚙️ Getting Started

```bash
# Install dependencies
poetry install

# Run the CLI
poetry run python -m soar_cli
```

(more to come…)

## 📄 License

MIT License
