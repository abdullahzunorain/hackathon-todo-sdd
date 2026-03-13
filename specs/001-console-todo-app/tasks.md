# Tasks: Console Todo App

**Input**: Design documents from `/specs/001-console-todo-app/`
**Prerequisites**: plan.md (required), spec.md (required), research.md, data-model.md, contracts/cli-commands.md

**Tests**: Included — spec FR-015 requires >80% coverage, constitution principle III mandates TDD.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3, US4)
- Include exact file paths in descriptions

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and dependency management

- [x] T001 Initialize Python project with UV: run `uv init --python 3.13 --name todo-app` and configure pyproject.toml
- [x] T002 Install dependencies: run `uv add typer rich` and `uv add --dev pytest pytest-cov`
- [x] T003 Create project directory structure: `src/todo_app/` with `__init__.py` and `tests/` with `__init__.py`
- [x] T004 [P] Create entry point module `src/todo_app/__main__.py` with `python -m todo_app` support
- [x] T005 [P] Create Typer app instance in `src/todo_app/main.py` with app name "todo" and version callback

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core model and service that ALL user stories depend on

**CRITICAL**: No user story work can begin until this phase is complete

- [x] T006 Create Task dataclass in `src/todo_app/models.py` with fields: id (int), title (str), description (str, default=""), completed (bool, default=False), created_at (datetime), updated_at (datetime)
- [x] T007 Create TodoService class in `src/todo_app/services.py` with `__init__` method initializing empty tasks dict and `_next_id` counter at 1
- [x] T008 Create display helper module `src/todo_app/display.py` with `render_task_table(tasks: list[Task])` using Rich Table and `render_message(text: str, style: str)` helper

**Checkpoint**: Foundation ready — Task model, TodoService skeleton, and display helpers exist. User story implementation can now begin.

---

## Phase 3: User Story 1 — Add and View Tasks (Priority: P1)

**Goal**: Users can add tasks with title/description and view all tasks in a formatted table.

**Independent Test**: Run `add` command then `list` command; verify task appears in formatted output.

### Tests for User Story 1

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [x] T009 [P] [US1] Write unit tests for Task model creation and defaults in `tests/test_models.py` — test id assignment, title required, description defaults to empty, completed defaults to False, timestamps auto-set
- [x] T010 [P] [US1] Write unit tests for TodoService.add_task() in `tests/test_services.py` — test adding task returns Task with correct fields, auto-increments ID, stores in internal dict
- [x] T011 [P] [US1] Write unit tests for TodoService.list_tasks() in `tests/test_services.py` — test returns all tasks, returns empty list when no tasks
- [x] T012 [P] [US1] Write CLI integration tests for `add` and `list` commands in `tests/test_cli.py` using Typer CliRunner — test add with title only, add with title+description, list with tasks, list empty

### Implementation for User Story 1

- [x] T013 [US1] Implement `TodoService.add_task(title: str, description: str = "") -> Task` in `src/todo_app/services.py` — create Task with auto-incremented ID, store in dict, return Task
- [x] T014 [US1] Implement `TodoService.list_tasks() -> list[Task]` in `src/todo_app/services.py` — return all tasks sorted by ID
- [x] T015 [US1] Implement `add` command in `src/todo_app/main.py` — Typer command accepting title (str argument) and description (str option, default=""), calls service.add_task(), prints confirmation via display helper
- [x] T016 [US1] Implement `list` command in `src/todo_app/main.py` — Typer command with no args, calls service.list_tasks(), renders Rich table via display helper or shows empty message
- [x] T017 [US1] Verify all US1 tests pass: run `uv run pytest tests/test_models.py tests/test_services.py::test_add_task tests/test_services.py::test_list_tasks tests/test_cli.py -v -k "add or list"`

**Checkpoint**: User Story 1 complete — add and list commands work. MVP is functional.

---

## Phase 4: User Story 2 — Mark Tasks Complete/Incomplete (Priority: P2)

**Goal**: Users can toggle task completion status by ID.

**Independent Test**: Add a task, mark it complete, verify status changed; mark again, verify toggled back.

### Tests for User Story 2

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [x] T018 [P] [US2] Write unit tests for TodoService.toggle_complete(task_id: int) in `tests/test_services.py` — test pending→completed, completed→pending, task not found raises error
- [x] T019 [P] [US2] Write CLI integration test for `complete` command in `tests/test_cli.py` using CliRunner — test toggle success, toggle back, task not found error, invalid ID error

### Implementation for User Story 2

- [x] T020 [US2] Implement `TodoService.toggle_complete(task_id: int) -> Task` in `src/todo_app/services.py` — find task by ID, toggle completed field, update updated_at, return task. Raise KeyError if not found.
- [x] T021 [US2] Implement `complete` command in `src/todo_app/main.py` — Typer command accepting task_id (int argument), calls service.toggle_complete(), prints status-appropriate confirmation or error via display helper
- [x] T022 [US2] Verify all US2 tests pass: run `uv run pytest tests/ -v -k "complete"`

**Checkpoint**: User Stories 1 and 2 complete — add, list, and complete commands work independently.

---

## Phase 5: User Story 3 — Update Task Details (Priority: P3)

**Goal**: Users can modify a task's title and/or description by ID.

**Independent Test**: Add a task, update its title, verify change reflected in list.

### Tests for User Story 3

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [x] T023 [P] [US3] Write unit tests for TodoService.update_task(task_id, title, description) in `tests/test_services.py` — test update title only, update description only, update both, task not found, no changes provided
- [x] T024 [P] [US3] Write CLI integration test for `update` command in `tests/test_cli.py` using CliRunner — test update title, update description, update both, not found error, no changes warning, invalid ID

### Implementation for User Story 3

- [x] T025 [US3] Implement `TodoService.update_task(task_id: int, title: str | None = None, description: str | None = None) -> Task` in `src/todo_app/services.py` — find task, update provided fields, update updated_at, return task. Raise KeyError if not found, ValueError if no changes.
- [x] T026 [US3] Implement `update` command in `src/todo_app/main.py` — Typer command accepting task_id (int argument), --title/-t (optional str), --description/-d (optional str), calls service.update_task(), prints confirmation or error
- [x] T027 [US3] Verify all US3 tests pass: run `uv run pytest tests/ -v -k "update"`

**Checkpoint**: User Stories 1, 2, and 3 complete — add, list, complete, and update commands work.

---

## Phase 6: User Story 4 — Delete Tasks (Priority: P4)

**Goal**: Users can permanently remove a task by ID.

**Independent Test**: Add a task, delete it, verify it no longer appears in list.

### Tests for User Story 4

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [x] T028 [P] [US4] Write unit tests for TodoService.delete_task(task_id: int) in `tests/test_services.py` — test successful deletion removes from dict, task not found raises error, deleted ID not reused
- [x] T029 [P] [US4] Write CLI integration test for `delete` command in `tests/test_cli.py` using CliRunner — test delete success, task not found error, invalid ID, verify task gone from list

### Implementation for User Story 4

- [x] T030 [US4] Implement `TodoService.delete_task(task_id: int) -> Task` in `src/todo_app/services.py` — find task, remove from dict, return deleted task. Raise KeyError if not found.
- [x] T031 [US4] Implement `delete` command in `src/todo_app/main.py` — Typer command accepting task_id (int argument), calls service.delete_task(), prints confirmation or error
- [x] T032 [US4] Verify all US4 tests pass: run `uv run pytest tests/ -v -k "delete"`

**Checkpoint**: All user stories complete — all 5 commands functional.

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Coverage validation, edge cases, and cleanup

- [x] T033 [P] Add edge case tests in `tests/test_cli.py` — test ID=0, negative ID, non-numeric ID handling, empty title rejection, long title display truncation
- [x] T034 Run full test suite with coverage: `uv run pytest -v --cov=src/todo_app --cov-report=term-missing` and verify >80% coverage
- [x] T035 [P] Create README.md with project description, setup instructions, usage examples, and test commands
- [x] T036 Run quickstart.md validation checklist end-to-end

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies — can start immediately
- **Foundational (Phase 2)**: Depends on Setup (Phase 1) completion — BLOCKS all user stories
- **User Story 1 (Phase 3)**: Depends on Foundational (Phase 2) — P1 priority, start first
- **User Story 2 (Phase 4)**: Depends on Foundational (Phase 2) — Can start after Phase 2, but recommended after US1
- **User Story 3 (Phase 5)**: Depends on Foundational (Phase 2) — Can start after Phase 2
- **User Story 4 (Phase 6)**: Depends on Foundational (Phase 2) — Can start after Phase 2
- **Polish (Phase 7)**: Depends on all user stories being complete

### Within Each User Story

- Tests MUST be written and FAIL before implementation (Red)
- Implementation makes tests pass (Green)
- Models/Services before CLI commands
- Verification step confirms all story tests pass

### Parallel Opportunities

- T004 + T005: Entry point and Typer app instance (different files)
- T009 + T010 + T011 + T012: All US1 test files can be written in parallel
- T018 + T019: US2 test files in parallel
- T023 + T024: US3 test files in parallel
- T028 + T029: US4 test files in parallel
- T033 + T035: Edge case tests and README (different files)
- US2, US3, US4 are technically independent after Phase 2, but sequential execution recommended for single developer

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (T001–T005)
2. Complete Phase 2: Foundational (T006–T008)
3. Complete Phase 3: User Story 1 (T009–T017)
4. **STOP and VALIDATE**: Test add + list commands independently
5. This alone delivers a working Todo app with basic value

### Incremental Delivery

1. Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → MVP!
3. Add User Story 2 → Test independently → Mark complete works
4. Add User Story 3 → Test independently → Update works
5. Add User Story 4 → Test independently → Delete works
6. Polish → Full coverage, README, validation

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story is independently completable and testable
- Verify tests fail before implementing (Red phase)
- Commit after each phase or logical group
- Stop at any checkpoint to validate story independently
