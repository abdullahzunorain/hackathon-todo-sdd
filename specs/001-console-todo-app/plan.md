# Implementation Plan: Console Todo App

**Branch**: `001-console-todo-app` | **Date**: 2026-03-13 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-console-todo-app/spec.md`

## Summary

Build an in-memory Python console Todo application supporting five CRUD operations (Add, View, Update, Delete, Mark Complete) via a CLI interface. The app uses Typer for command parsing and Rich for formatted table output. All data is stored in-memory (Python dict) with no persistence. The architecture follows clean separation: models (dataclass), services (business logic), and CLI (interface layer).

## Technical Context

**Language/Version**: Python 3.13+ managed by UV
**Primary Dependencies**: Typer (CLI framework), Rich (terminal formatting)
**Storage**: In-memory Python dict (no persistence)
**Testing**: pytest with pytest-cov (>80% coverage target)
**Target Platform**: Linux (WSL 2 Ubuntu) terminal
**Project Type**: Single project
**Performance Goals**: Instant CLI response (<1s for all operations)
**Constraints**: No external services, no file I/O, single-user, single-process
**Scale/Scope**: Single-user CLI, ~5 commands, ~200-400 lines of source code

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Status | Evidence |
|-----------|--------|----------|
| I. Spec-Driven Development | PASS | Feature follows SDD lifecycle: constitution → spec → plan → tasks → implement. All code will be generated via Claude Code from validated spec. |
| II. Incremental Evolution | PASS | Phase I builds the foundation (models, services) that Phase II will extend. Task model designed for reuse. |
| III. Test-First Development | PASS | pytest with >80% coverage target. Red-Green-Refactor cycle will be followed. Tasks will include test-writing before implementation. |
| IV. Clean Architecture | PASS | Three-layer separation: models (data), services (logic), cli (interface). Each layer independently testable. Dependencies flow inward: cli → services → models. |
| V. Cloud-Native Ready | PASS | Stateless design (in-memory). Configuration via environment variables possible. Structured output to stdout. Graceful error handling. |
| VI. Security by Default | PASS | No secrets needed for Phase I. Input validation at CLI boundary (task IDs). No external I/O. |

**Gate result**: ALL PASS — proceed to Phase 0.

## Project Structure

### Documentation (this feature)

```text
specs/001-console-todo-app/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── contracts/           # Phase 1 output (CLI contract)
│   └── cli-commands.md
├── checklists/
│   └── requirements.md
└── tasks.md             # Phase 2 output (/sp.tasks command)
```

### Source Code (repository root)

```text
src/
└── todo_app/
    ├── __init__.py
    ├── main.py          # Typer CLI entry point + app commands
    ├── models.py        # Task dataclass
    ├── services.py      # TodoService (CRUD business logic)
    └── display.py       # Rich table formatting helpers

tests/
├── __init__.py
├── test_models.py       # Task dataclass unit tests
├── test_services.py     # TodoService unit tests
└── test_cli.py          # CLI integration tests (Typer CliRunner)

pyproject.toml           # UV project config with dependencies
```

**Structure Decision**: Single project layout. This is a standalone CLI app with no frontend/backend split. The `src/todo_app/` package structure supports future import by Phase II's backend service layer.

## Complexity Tracking

> No violations detected. All principles satisfied with minimal complexity.
