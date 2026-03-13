# Quickstart: Console Todo App

**Feature**: 001-console-todo-app | **Date**: 2026-03-13

## Prerequisites

- Python 3.13+ (installed via UV)
- UV package manager

## Setup

```bash
cd "/mnt/c/Users/MY PC/Desktop/II"

# Initialize project (if not done)
uv init --python 3.13 --name todo-app

# Install dependencies
uv add typer rich
uv add --dev pytest pytest-cov

# Verify installation
uv run python --version
```

## Run the App

```bash
# Add a task
uv run python -m todo_app add "Buy groceries" --description "Milk, eggs, bread"

# View all tasks
uv run python -m todo_app list

# Mark task as complete
uv run python -m todo_app complete 1

# Update a task
uv run python -m todo_app update 1 --title "Buy organic groceries"

# Delete a task
uv run python -m todo_app delete 1

# Get help
uv run python -m todo_app --help
uv run python -m todo_app add --help
```

## Run Tests

```bash
# Run all tests
uv run pytest -v

# Run with coverage report
uv run pytest -v --cov=src/todo_app --cov-report=term-missing

# Run specific test file
uv run pytest tests/test_services.py -v

# Run specific test
uv run pytest tests/test_services.py::test_add_task -v
```

## Project Structure

```
src/todo_app/
├── __init__.py      # Package init
├── __main__.py      # Entry point for `python -m todo_app`
├── main.py          # Typer app and CLI commands
├── models.py        # Task dataclass
├── services.py      # TodoService business logic
└── display.py       # Rich table formatting

tests/
├── __init__.py
├── test_models.py   # Task dataclass tests
├── test_services.py # TodoService tests
└── test_cli.py      # CLI integration tests
```

## Validation Checklist

- [ ] `uv run python -m todo_app add "Test task"` creates task with ID 1
- [ ] `uv run python -m todo_app list` shows the task in a formatted table
- [ ] `uv run python -m todo_app complete 1` toggles task status
- [ ] `uv run python -m todo_app update 1 --title "Updated"` changes the title
- [ ] `uv run python -m todo_app delete 1` removes the task
- [ ] `uv run python -m todo_app list` shows "no tasks found" after deletion
- [ ] `uv run python -m todo_app complete 99` shows error message
- [ ] `uv run pytest -v --cov=src/todo_app` shows >80% coverage
