# Research: Console Todo App

**Feature**: 001-console-todo-app | **Date**: 2026-03-13

## Research Tasks

### R1: CLI Framework Selection

**Decision**: Typer
**Rationale**: Typer provides type-hint-based command definitions, automatic help generation, and built-in parameter validation. It integrates naturally with Rich for formatted output. Minimal boilerplate compared to argparse or click (Typer is built on click internally).
**Alternatives considered**:
- **argparse** (stdlib): More verbose, no type-hint integration, manual help formatting. Rejected for developer experience.
- **click**: Lower-level than Typer, requires more decorators. Typer wraps click with a better DX.
- **fire**: Auto-generates CLI from functions/classes but less control over help text and validation.

### R2: Output Formatting

**Decision**: Rich library with Table component
**Rationale**: Rich provides beautiful terminal tables with alignment, borders, and color support. The `Table` class handles column width, truncation, and styling out of the box. Pairs naturally with Typer (same creator).
**Alternatives considered**:
- **tabulate**: Simpler but no color/styling support. Rejected for UX quality.
- **prettytable**: Similar to tabulate, less actively maintained.
- **Manual formatting**: Too brittle for aligned columns with variable-width content.

### R3: Data Model Approach

**Decision**: Python dataclass with field defaults
**Rationale**: Dataclasses provide clean, immutable-friendly data structures with automatic `__init__`, `__repr__`, and `__eq__`. No external dependency needed. The `field(default_factory=...)` pattern handles timestamps cleanly. Supports future extension to SQLModel in Phase II (SQLModel models can mirror dataclass structure).
**Alternatives considered**:
- **Pydantic BaseModel**: More powerful validation but overkill for Phase I's in-memory model. Would add an unnecessary dependency.
- **NamedTuple**: Immutable by default, which complicates status toggling. No default values in older Python.
- **Plain dict**: No type safety, no IDE support, error-prone.

### R4: In-Memory Storage Pattern

**Decision**: Python dict keyed by integer ID, wrapped in a TodoService class
**Rationale**: Dict provides O(1) lookup by ID. Wrapping in a service class provides clean separation of storage logic from CLI interface. The service maintains a `_next_id` counter for auto-increment. This pattern maps directly to a repository/service pattern in Phase II.
**Alternatives considered**:
- **List**: O(n) lookup by ID, deletion leaves gaps or requires re-indexing.
- **OrderedDict**: Unnecessary — regular dict preserves insertion order in Python 3.7+.
- **SQLite in-memory**: Over-engineered for Phase I requirements.

### R5: Testing Strategy

**Decision**: pytest + pytest-cov with Typer's CliRunner for integration tests
**Rationale**: pytest is the standard Python testing framework. Typer provides `CliRunner` (inherited from click) for testing CLI commands without subprocess overhead. Three test layers: unit tests for models, unit tests for services, integration tests for CLI commands.
**Alternatives considered**:
- **unittest**: More verbose, less ergonomic fixtures, fewer plugins.
- **subprocess testing**: Slower, harder to capture output, unnecessary when CliRunner available.

### R6: Package Structure for Phase II Compatibility

**Decision**: `src/todo_app/` package with `__main__.py` entry point
**Rationale**: The `src/` layout is the modern Python standard (PEP 517/518). Using a package under `src/` ensures proper import isolation during testing and allows Phase II to import models/services directly. The `__main__.py` allows `python -m todo_app` execution.
**Alternatives considered**:
- **Flat structure** (files at root): No import isolation, conflicts with test imports.
- **`app/` directory**: Non-standard, less recognizable.

## Resolved Clarifications

No NEEDS CLARIFICATION items were present in the technical context. All technology choices are well-defined by the constitution (Python 3.13+, UV, pytest) and spec (in-memory, CLI).
