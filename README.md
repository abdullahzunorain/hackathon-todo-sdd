# Todo App — Phase I: In-Memory Console Application

An in-memory Python console Todo app built with **Typer** and **Rich** as Phase I of the Hackathon II — The Evolution of Todo.

## Features

- **Add** tasks with title and optional description
- **View** all tasks in a formatted table
- **Update** task title and/or description
- **Delete** tasks permanently
- **Mark Complete** / toggle back to pending

## Setup

```bash
# Requires Python 3.13+ and UV
uv sync

# Verify installation
uv run python -m todo_app --version
```

## Usage

```bash
# Add a task
uv run python -m todo_app add "Buy groceries" --description "Milk, eggs, bread"

# View all tasks
uv run python -m todo_app list

# Mark task as complete (toggles)
uv run python -m todo_app complete 1

# Update a task
uv run python -m todo_app update 1 --title "Buy organic groceries"

# Delete a task
uv run python -m todo_app delete 1

# Help
uv run python -m todo_app --help
```

## Testing

```bash
# Run all tests
uv run pytest -v

# Run with coverage
uv run pytest -v --cov=src/todo_app --cov-report=term-missing
```

## Project Structure

```
src/todo_app/
├── __init__.py      # Package init + version
├── __main__.py      # Entry point (python -m todo_app)
├── main.py          # Typer CLI commands
├── models.py        # Task dataclass
├── services.py      # TodoService business logic
└── display.py       # Rich table formatting

tests/
├── test_models.py   # Task model unit tests
├── test_services.py # Service layer unit tests
└── test_cli.py      # CLI integration tests
```

## Architecture

- **Models**: Task dataclass with id, title, description, completed, timestamps
- **Services**: TodoService wraps in-memory dict with CRUD operations
- **CLI**: Typer commands call service methods, Rich formats output
- **Storage**: In-memory only — data resets on exit (by design for Phase I)
