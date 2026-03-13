# Hackathon II — Phase I Workflow Report

**Project**: The Evolution of Todo — Mastering Spec-Driven Development & Cloud Native AI
**Organization**: Panaversity (panaversity.org)
**Phase**: I — In-Memory Python Console App (100 pts)
**Date Completed**: 2026-03-14
**Branch**: `001-console-todo-app`
**PR**: https://github.com/abdullahzunorain/hackathon-todo-sdd/pull/1

---

## Table of Contents

1. [What Is This Project?](#1-what-is-this-project)
2. [Environment Setup](#2-environment-setup)
3. [SDD Workflow Executed](#3-sdd-workflow-executed)
4. [Step-by-Step Breakdown](#4-step-by-step-breakdown)
5. [Architecture & Source Code](#5-architecture--source-code)
6. [Testing & Coverage](#6-testing--coverage)
7. [Files Created](#7-files-created)
8. [Git History](#8-git-history)
9. [What Phase II Will Build On](#9-what-phase-ii-will-build-on)

---

## 1. What Is This Project?

This is a 5-phase hackathon where a simple Todo app evolves from a CLI tool to a cloud-native AI chatbot:

| Phase | Description | Points |
|-------|-------------|--------|
| **I (this one)** | **In-Memory Python Console App** | **100** |
| II | Full-Stack Web App (Next.js + FastAPI + Neon DB) | 150 |
| III | AI-Powered Todo Chatbot (OpenAI Agents + MCP) | 200 |
| IV | Local Kubernetes Deployment (Docker + Minikube + Helm) | 250 |
| V | Advanced Cloud Deployment (Kafka + Dapr + CI/CD) | 300 |

**The key rule**: NO manual coding. Everything must be built using **Spec-Driven Development (SDD)** with Claude Code + Spec-Kit Plus. Every feature goes through: Constitution → Specify → Plan → Tasks → Implement.

---

## 2. Environment Setup

Before any SDD work, we set up the development environment:

### 2.1 Git & GitHub

```
Tool: Git on WSL 2 (Ubuntu) in VS Code
Action: Renamed `master` → `main`, created GitHub repo
Repo: https://github.com/abdullahzunorain/hackathon-todo-sdd
```

- Ran `git branch -M main` to rename the default branch
- Created remote repo via `gh repo create hackathon-todo-sdd --public --source=. --push`
- Created feature branch `001-console-todo-app` (auto-created by `/sp.specify`)

### 2.2 Python & UV

```
Tool: UV v0.9.27 (Python package manager)
Python: 3.13.11 (installed via `uv python install 3.13`)
Virtual env: .venv/ created in WSL by UV automatically
```

- UV was already installed at `/home/zunorain/.local/bin/uv`
- Python 3.13.11 installed via `uv python install 3.13`
- Project initialized via `uv init --python 3.13 --name todo-app`

### 2.3 Dependencies Installed

| Package | Version | Purpose |
|---------|---------|---------|
| typer | 0.24.1 | CLI framework (type-hint based commands) |
| rich | 14.3.3 | Terminal table formatting and styled output |
| pytest | 9.0.2 | Testing framework (dev dependency) |
| pytest-cov | 7.0.0 | Coverage reporting (dev dependency) |
| hatchling | — | Build backend for src layout |

Installed via:
```bash
uv add typer rich
uv add --dev pytest pytest-cov
```

---

## 3. SDD Workflow Executed

Phase I followed the complete Spec-Driven Development lifecycle. Here is the exact order of commands run and what each produced:

```
Step 1: /sp.constitution    → Defined 6 project principles (one-time, on main)
Step 2: /sp.specify         → Created feature spec with 4 user stories
Step 3: /sp.plan            → Generated implementation plan + 5 artifacts
Step 4: /sp.tasks           → Generated 36 ordered tasks with TDD
Step 5: /sp.implement       → Executed all 36 tasks (Red → Green)
Step 6: /sp.git.commit_pr   → Committed 30 files, created PR #1
```

Each step is documented with a **Prompt History Record (PHR)** in `history/prompts/`.

---

## 4. Step-by-Step Breakdown

### Step 1: `/sp.constitution` — Define Project Principles

**What it did**: Created the project constitution at `.specify/memory/constitution.md` — the highest authority document that governs all development.

**6 Principles Defined**:

1. **Spec-Driven Development (NON-NEGOTIABLE)** — No manual coding. All features follow: Constitution → Specify → Plan → Tasks → Implement. Every code file must trace back to a spec requirement.

2. **Incremental Evolution** — Each phase builds on the previous. Code carries forward: Phase I (CLI) → Phase II (Web) → Phase III (AI) → Phase IV (K8s) → Phase V (Cloud).

3. **Test-First Development** — TDD is mandatory. Tests written before implementation. Red-Green-Refactor cycle. pytest for Python, >80% coverage target.

4. **Clean Architecture** — Separation of concerns: Models (data) → Services (logic) → Interfaces (CLI/API/UI). Each layer independently testable. No circular dependencies.

5. **Cloud-Native Ready** — Stateless design, environment variable configuration, 12-factor app principles, structured logging, graceful shutdown.

6. **Security by Default** — No hardcoded secrets, .env files for config, input validation at boundaries, JWT auth (Phase II+).

**Additional Constraints**: Python 3.13+ with UV, WSL 2, Next.js 16+ (Phase II+), Neon PostgreSQL (Phase II+), OpenAI Agents SDK (Phase III+), Docker/K8s (Phase IV+).

**Output**: `.specify/memory/constitution.md` (v1.0.0)
**PHR**: `history/prompts/constitution/002-define-project-constitution.constitution.prompt.md`

---

### Step 2: `/sp.specify` — Create Feature Specification

**What it did**: Created a feature branch `001-console-todo-app` and wrote the feature specification at `specs/001-console-todo-app/spec.md`.

**4 User Stories Defined** (prioritized as independent, testable slices):

| Priority | User Story | What It Delivers |
|----------|-----------|------------------|
| P1 | Add and View Tasks | Core MVP — add tasks with title/description, view in formatted table |
| P2 | Mark Tasks Complete/Incomplete | Toggle completion status by ID |
| P3 | Update Task Details | Modify title and/or description by ID |
| P4 | Delete Tasks | Remove tasks permanently by ID |

**Each story includes**:
- Plain language description
- Why this priority (business value reasoning)
- Independent test criteria
- Acceptance scenarios in Given/When/Then format

**15 Functional Requirements** (FR-001 through FR-015):
- Covers all CRUD operations, ID auto-increment, timestamps, error handling, validation, coverage target

**6 Success Criteria** (SC-001 through SC-006):
- Measurable, technology-agnostic outcomes (e.g., "task lifecycle in under 30 seconds")

**5 Edge Cases** identified:
- Invalid IDs (0, negative, non-numeric), long titles, empty list display

**Quality Checklist**: All 16 items passed — spec ready for planning.

**Output**: `specs/001-console-todo-app/spec.md`, `specs/001-console-todo-app/checklists/requirements.md`
**PHR**: `history/prompts/console-todo-app/003-specify-console-todo-app.spec.prompt.md`

---

### Step 3: `/sp.plan` — Generate Implementation Plan

**What it did**: Generated the implementation plan and 4 supporting design artifacts.

**5 Artifacts Produced**:

#### 3a. `plan.md` — Implementation Plan
- **Technical Context**: Python 3.13+, Typer, Rich, pytest, in-memory dict, single project layout
- **Constitution Check**: All 6 principles verified PASS with evidence
- **Project Structure**: `src/todo_app/` with 6 modules + `tests/` with 3 test files

#### 3b. `research.md` — Technology Decisions
6 research decisions with rationale and alternatives considered:

| Decision | Chosen | Rejected Alternatives |
|----------|--------|----------------------|
| CLI Framework | Typer | argparse, click, fire |
| Output Formatting | Rich (Table) | tabulate, prettytable |
| Data Model | Python dataclass | Pydantic, NamedTuple, plain dict |
| Storage Pattern | Dict wrapped in service class | list, OrderedDict, SQLite in-memory |
| Testing Strategy | pytest + CliRunner | unittest, subprocess testing |
| Package Structure | src/ layout (PEP 517/518) | flat structure, app/ directory |

#### 3c. `data-model.md` — Entity Design
- **Task entity**: 6 fields (id, title, description, completed, created_at, updated_at)
- Validation rules, state transition diagram
- Phase II migration notes (dataclass → SQLModel, add user_id FK)

#### 3d. `contracts/cli-commands.md` — CLI Contract
- 5 commands fully specified: `add`, `list`, `complete`, `update`, `delete`
- Parameter types, success/error output examples, exit codes
- Global options: `--help`, `--version`

#### 3e. `quickstart.md` — Setup & Validation
- Setup instructions, run commands, test commands
- End-to-end validation checklist (8 items)

**Output**: `specs/001-console-todo-app/plan.md` + 4 artifacts
**PHR**: `history/prompts/console-todo-app/004-plan-console-todo-app.plan.prompt.md`

---

### Step 4: `/sp.tasks` — Generate Task List

**What it did**: Generated 36 ordered, dependency-aware tasks organized by user story.

**7 Phases, 36 Tasks**:

| Phase | Name | Tasks | Description |
|-------|------|-------|-------------|
| 1 | Setup | T001–T005 | UV init, dependencies, directory structure, entry point, Typer app |
| 2 | Foundational | T006–T008 | Task dataclass, TodoService skeleton, Rich display helpers |
| 3 | US1: Add/View (P1) | T009–T017 | 4 test tasks + 4 implementation + 1 verification |
| 4 | US2: Complete (P2) | T018–T022 | 2 test tasks + 2 implementation + 1 verification |
| 5 | US3: Update (P3) | T023–T027 | 2 test tasks + 2 implementation + 1 verification |
| 6 | US4: Delete (P4) | T028–T032 | 2 test tasks + 2 implementation + 1 verification |
| 7 | Polish | T033–T036 | Edge cases, coverage check, README, quickstart validation |

**Key Properties**:
- **TDD enforced**: Test tasks (RED) always precede implementation tasks (GREEN) in every phase
- **14 parallel opportunities** marked with `[P]`
- **User story labels** `[US1]`–`[US4]` on every story task for traceability
- **Exact file paths** in every task description
- **Checkpoints** after each phase for independent validation

**Output**: `specs/001-console-todo-app/tasks.md`
**PHR**: `history/prompts/console-todo-app/005-generate-tasks-console-todo.tasks.prompt.md`

---

### Step 5: `/sp.implement` — Execute All Tasks

**What it did**: Executed all 36 tasks following TDD (Red-Green-Refactor).

#### Phase 1: Setup (T001–T005)
- Ran `uv init --python 3.13 --name todo-app`
- Configured `pyproject.toml` with hatchling build backend for `src/` layout
- Installed typer, rich, pytest, pytest-cov
- Created `src/todo_app/` package with `__init__.py` (version), `__main__.py` (entry point)
- Created Typer app instance in `main.py` with `--version` callback
- Removed UV auto-generated `main.py` at root
- Verified: `uv run python -m todo_app --version` → `todo-app v0.1.0`

#### Phase 2: Foundational (T006–T008)
- Created `models.py`: Task dataclass with 6 fields and default factories for timestamps
- Created `services.py`: TodoService class with `__init__` (empty dict + counter), custom exceptions (TaskNotFoundError, NoChangesError)
- Created `display.py`: `render_task_table()` with Rich Table, `render_success/error/warning()` helpers with truncation for long titles

#### Phase 3–6: User Stories with TDD

**RED Phase** (Tests Written First — T009–T012, T018–T019, T023–T024, T028–T029):
- Wrote 42 tests across 3 files BEFORE any implementation
- Tests covered: model creation, all 5 service methods, all 5 CLI commands, error paths
- Verified tests FAIL: 6 passed (model tests), 22 failed (service methods not implemented)

**GREEN Phase** (Implementation — T013–T016, T020–T021, T025–T026, T030–T031):
- Implemented 5 service methods: `add_task`, `list_tasks`, `toggle_complete`, `update_task`, `delete_task`
- Implemented 5 CLI commands: `add`, `list`, `complete`, `update`, `delete`
- Each command: validates input → calls service → renders output via display helper
- Error handling: TaskNotFoundError → exit code 1, NoChangesError → warning message

**Bug Found & Fixed**:
- **Issue**: CLI tests shared a module-level `TodoService` instance — state leaked between tests
- **Symptom**: `test_list_empty` found tasks from previous `test_add` invocations
- **Fix**: Added `@pytest.fixture(autouse=True)` to reset `main_module.service = TodoService()` before each test
- **Result**: All 42 tests pass after fix

#### Phase 7: Polish (T033–T036)
- Coverage check: **92%** (target was >80%)
- Created `README.md` with setup, usage, testing, and architecture docs
- Created `.gitignore` with patterns for Python, .venv, .env, .claude/, IDE, OS, Node.js, Docker, K8s
- Validated quickstart checklist end-to-end (all operations work in single session)

**Final Result**: 36/36 tasks completed, 42/42 tests passed, 92% coverage

**Output**: All source files in `src/todo_app/` and `tests/`
**PHR**: `history/prompts/console-todo-app/006-implement-console-todo-app.green.prompt.md`

---

### Step 6: `/sp.git.commit_pr` — Commit & Create PR

**What it did**: Staged files, committed, pushed, and created a pull request.

- **Updated .gitignore** (user requested before commit): Added comprehensive patterns for Python, virtual environments, .env secrets, .claude/ (local agent config), IDE files, OS files, and future phase technologies (Node.js, Docker, K8s)
- **Staged 30 files** — excluded hackathon PDF (binary, not source code) and `.claude/` directory (local hooks/skills)
- **Committed**: `85319de feat(phase-1): implement in-memory console Todo app`
- **Pushed**: Branch `001-console-todo-app` to `origin`
- **Created PR**: https://github.com/abdullahzunorain/hackathon-todo-sdd/pull/1

**PHR**: `history/prompts/console-todo-app/007-commit-pr-phase-one.misc.prompt.md`

---

## 5. Architecture & Source Code

### Clean Architecture (3 layers)

```
CLI Layer (main.py)          ← User-facing interface (Typer commands)
    │
    ▼
Service Layer (services.py)  ← Business logic (CRUD operations)
    │
    ▼
Model Layer (models.py)      ← Data structures (Task dataclass)

Display Layer (display.py)   ← Output formatting (Rich tables/messages)
```

Dependencies flow inward: CLI → Services → Models. Each layer is independently testable.

### Source Files (244 lines of production code)

| File | Lines | Purpose |
|------|-------|---------|
| `src/todo_app/__init__.py` | 3 | Package init, `__version__ = "0.1.0"` |
| `src/todo_app/__main__.py` | 5 | Entry point for `python -m todo_app` |
| `src/todo_app/models.py` | 16 | Task dataclass with 6 fields |
| `src/todo_app/services.py` | 70 | TodoService: 5 CRUD methods + 2 custom exceptions |
| `src/todo_app/display.py` | 48 | Rich Table rendering + success/error/warning helpers |
| `src/todo_app/main.py` | 102 | 5 Typer commands (add, list, complete, update, delete) |

### Test Files (310 lines of test code)

| File | Lines | Tests | What It Tests |
|------|-------|-------|---------------|
| `tests/test_models.py` | 41 | 6 | Task dataclass creation, defaults, timestamps |
| `tests/test_services.py` | 153 | 22 | add_task, list_tasks, toggle_complete, update_task, delete_task |
| `tests/test_cli.py` | 116 | 14 | All 5 CLI commands via Typer CliRunner + service reset fixture |

### CLI Commands

| Command | Usage | Description |
|---------|-------|-------------|
| `add` | `todo_app add "Title" -d "Description"` | Create a new task |
| `list` | `todo_app list` | View all tasks in a Rich table |
| `complete` | `todo_app complete 1` | Toggle task completion status |
| `update` | `todo_app update 1 -t "New title" -d "New desc"` | Modify task fields |
| `delete` | `todo_app delete 1` | Remove a task permanently |

---

## 6. Testing & Coverage

### Test Results: 42/42 Passed

```
tests/test_cli.py       — 14 passed (CLI integration via CliRunner)
tests/test_models.py    —  6 passed (Task dataclass unit tests)
tests/test_services.py  — 22 passed (TodoService unit tests)
```

### Coverage: 92% (target: >80%)

```
Name                       Stmts   Miss  Cover   Missing
--------------------------------------------------------
src/todo_app/__init__.py       1      0   100%
src/todo_app/__main__.py       2      2     0%   3-5 (entry point, not testable via import)
src/todo_app/display.py       29      0   100%
src/todo_app/main.py          61     10    84%   17-18, 37-38, 56-57, 77-78, 95-96
src/todo_app/models.py        10      0   100%
src/todo_app/services.py      42      0   100%
--------------------------------------------------------
TOTAL                        145     12    92%
```

The 10 missed lines in `main.py` are the `task_id < 1` validation branches (lines 37-38, 56-57, 77-78, 95-96) and the version callback (17-18) — these are edge case paths that Typer handles before reaching the function body.

---

## 7. Files Created

### SDD Artifacts (8 files)

```
.specify/memory/constitution.md                              ← Project principles (v1.0.0)
specs/001-console-todo-app/spec.md                           ← Feature specification
specs/001-console-todo-app/plan.md                           ← Implementation plan
specs/001-console-todo-app/research.md                       ← Technology decisions
specs/001-console-todo-app/data-model.md                     ← Entity design
specs/001-console-todo-app/contracts/cli-commands.md         ← CLI command contract
specs/001-console-todo-app/quickstart.md                     ← Setup & validation guide
specs/001-console-todo-app/tasks.md                          ← 36 tasks (all [x] completed)
specs/001-console-todo-app/checklists/requirements.md        ← Spec quality checklist
```

### Prompt History Records (7 PHRs)

```
history/prompts/general/001-read-codebase-and-remember.general.prompt.md
history/prompts/constitution/002-define-project-constitution.constitution.prompt.md
history/prompts/console-todo-app/003-specify-console-todo-app.spec.prompt.md
history/prompts/console-todo-app/004-plan-console-todo-app.plan.prompt.md
history/prompts/console-todo-app/005-generate-tasks-console-todo.tasks.prompt.md
history/prompts/console-todo-app/006-implement-console-todo-app.green.prompt.md
history/prompts/console-todo-app/007-commit-pr-phase-one.misc.prompt.md
```

### Source Code (6 files, 244 lines)

```
src/todo_app/__init__.py     ← Package init + version
src/todo_app/__main__.py     ← Entry point (python -m todo_app)
src/todo_app/models.py       ← Task dataclass
src/todo_app/services.py     ← TodoService (CRUD business logic)
src/todo_app/display.py      ← Rich table formatting helpers
src/todo_app/main.py         ← 5 Typer CLI commands
```

### Tests (3 files, 42 tests, 310 lines)

```
tests/test_models.py         ← Task model unit tests (6)
tests/test_services.py       ← TodoService unit tests (22)
tests/test_cli.py            ← CLI integration tests (14)
```

### Config & Docs (4 files)

```
pyproject.toml               ← UV project config + dependencies + build system
.gitignore                   ← Comprehensive ignore patterns
.python-version              ← Python 3.13 pinned
README.md                    ← Project description, setup, usage, testing
```

---

## 8. Git History

```
85319de (HEAD -> 001-console-todo-app, origin/001-console-todo-app) feat(phase-1): implement in-memory console Todo app
7c52191 (origin/main, main) Initial commit from Specify template
```

- **Branch**: `001-console-todo-app` (feature branch for Phase I)
- **Base**: `main` (will merge PR #1 into main before starting Phase II)
- **PR**: https://github.com/abdullahzunorain/hackathon-todo-sdd/pull/1
- **Commit**: 30 files changed, 1990 insertions, 49 deletions

---

## 9. What Phase II Will Build On

Phase II (Full-Stack Web App) will extend Phase I's foundation:

| Phase I Asset | Phase II Evolution |
|---------------|-------------------|
| `models.py` (Task dataclass) | → SQLModel table with same fields + `user_id` FK |
| `services.py` (TodoService) | → Backend service layer with DB queries instead of dict |
| In-memory dict storage | → Neon serverless PostgreSQL via SQLModel ORM |
| Typer CLI interface | → FastAPI REST endpoints + Next.js 16 frontend |
| No authentication | → Better Auth (frontend) + JWT (backend) |
| Single project `src/` | → Monorepo: `backend/` + `frontend/` |
| pytest tests | → pytest (backend) + vitest (frontend) |

The clean architecture (models → services → interfaces) was designed from Day 1 to support this evolution. The service layer's interface (`add_task`, `list_tasks`, etc.) will remain the same — only the storage backend changes.

---

**Phase I: COMPLETE** | 42 tests | 92% coverage | 36/36 tasks | PR #1 ready for merge
