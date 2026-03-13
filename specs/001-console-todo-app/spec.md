# Feature Specification: Console Todo App

**Feature Branch**: `001-console-todo-app`
**Created**: 2026-03-13
**Status**: Draft
**Input**: User description: "In-memory Python console Todo app with Add, Delete, Update, View, and Mark Complete operations. Phase I of Hackathon II - The Evolution of Todo."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Add and View Tasks (Priority: P1)

A user opens the console app and adds a new task by providing a title and an optional description. After adding one or more tasks, the user views all tasks displayed in a formatted table showing ID, title, description, completion status, and creation time.

**Why this priority**: Adding and viewing tasks is the core value proposition. Without it, no other operation is meaningful. This alone delivers a usable MVP.

**Independent Test**: Can be fully tested by running the add command followed by the view command and verifying the task appears with correct details in the formatted output.

**Acceptance Scenarios**:

1. **Given** no tasks exist, **When** the user adds a task with title "Buy groceries", **Then** the system confirms creation and assigns a unique numeric ID starting from 1.
2. **Given** no tasks exist, **When** the user adds a task with title "Buy groceries" and description "Milk, eggs, bread", **Then** the system stores both title and description.
3. **Given** one or more tasks exist, **When** the user views all tasks, **Then** a formatted table displays each task's ID, title, description, status (pending/completed), and creation timestamp.
4. **Given** no tasks exist, **When** the user views all tasks, **Then** the system displays a friendly message indicating no tasks are found.
5. **Given** the user omits the description, **When** adding a task, **Then** the task is created with an empty description and no error occurs.

---

### User Story 2 - Mark Tasks Complete and Incomplete (Priority: P2)

A user has existing tasks and wants to mark specific tasks as complete or toggle them back to incomplete. The user provides the task ID, and the system updates the status accordingly.

**Why this priority**: Tracking completion is the second most important capability — it transforms a simple list into a task management tool.

**Independent Test**: Can be tested by adding a task, marking it complete, viewing the list to confirm status changed, then toggling it back to incomplete.

**Acceptance Scenarios**:

1. **Given** a task with ID 1 exists and is pending, **When** the user marks task 1 as complete, **Then** the task's status changes to completed and a confirmation message is shown.
2. **Given** a task with ID 1 exists and is completed, **When** the user marks task 1 as complete again, **Then** the task's status toggles back to pending (incomplete).
3. **Given** no task with ID 99 exists, **When** the user attempts to mark task 99 as complete, **Then** the system displays an error message indicating the task was not found.

---

### User Story 3 - Update Task Details (Priority: P3)

A user realizes a task's title or description needs correction. The user provides the task ID along with a new title and/or description, and the system updates the specified fields.

**Why this priority**: Editing is important but secondary — users can delete and re-add as a workaround, so this is an enhancement over the core add/view/complete flow.

**Independent Test**: Can be tested by adding a task, updating its title, and viewing the list to confirm the change is reflected.

**Acceptance Scenarios**:

1. **Given** a task with ID 1 exists with title "Buy groceries", **When** the user updates task 1 with a new title "Buy organic groceries", **Then** the title is updated and a confirmation message is shown.
2. **Given** a task with ID 1 exists, **When** the user updates only the description, **Then** only the description changes while the title remains unchanged.
3. **Given** a task with ID 1 exists, **When** the user updates both title and description, **Then** both fields are updated.
4. **Given** no task with ID 99 exists, **When** the user attempts to update task 99, **Then** the system displays an error message indicating the task was not found.

---

### User Story 4 - Delete Tasks (Priority: P4)

A user wants to remove a task entirely from the list. The user provides the task ID, and the system permanently removes it.

**Why this priority**: Deletion is the lowest priority CRUD operation — tasks can remain in the list without harm, and completion status already communicates "done."

**Independent Test**: Can be tested by adding a task, deleting it by ID, and viewing the list to confirm it no longer appears.

**Acceptance Scenarios**:

1. **Given** a task with ID 1 exists, **When** the user deletes task 1, **Then** the task is removed and a confirmation message is shown.
2. **Given** no task with ID 99 exists, **When** the user attempts to delete task 99, **Then** the system displays an error message indicating the task was not found.
3. **Given** a task with ID 1 is deleted, **When** the user views all tasks, **Then** task 1 no longer appears in the list.

---

### Edge Cases

- What happens when the user provides an ID of 0 or a negative number? The system rejects the input with a clear error message.
- What happens when the user adds a task with an extremely long title (over 200 characters)? The system accepts it but truncates display in the table view for readability.
- What happens when all tasks are deleted and the user views the list? The system shows the "no tasks found" message.
- What happens when the user provides a non-numeric ID? The system displays a clear error message about invalid input.
- What happens when the user tries to update a task with no changes (same title and description)? The system accepts it without error and shows a confirmation.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST allow users to add a task with a required title and an optional description.
- **FR-002**: System MUST assign a unique, auto-incrementing numeric ID to each new task, starting from 1.
- **FR-003**: System MUST display all tasks in a formatted table with columns: ID, Title, Description, Status, Created At.
- **FR-004**: System MUST show a friendly message when the task list is empty.
- **FR-005**: System MUST allow users to mark a task as complete by its ID, toggling between pending and completed states.
- **FR-006**: System MUST allow users to update a task's title and/or description by its ID.
- **FR-007**: System MUST allow users to delete a task by its ID.
- **FR-008**: System MUST display an error message when an operation targets a non-existent task ID.
- **FR-009**: System MUST store tasks in memory only — no file or database persistence across sessions.
- **FR-010**: System MUST record a creation timestamp for each task.
- **FR-011**: System MUST record an updated-at timestamp whenever a task is modified.
- **FR-012**: Each task MUST track its completion status as either "pending" or "completed".
- **FR-013**: System MUST provide clear confirmation messages after each successful operation (add, update, delete, complete).
- **FR-014**: System MUST validate that task IDs are positive integers and display an error for invalid input.
- **FR-015**: System MUST achieve greater than 80% test coverage.

### Key Entities

- **Task**: Represents a single todo item. Attributes: unique numeric ID, title (required string), description (optional string), completion status (pending or completed), creation timestamp, last-updated timestamp.

### Assumptions

- Tasks are stored in memory only; restarting the application clears all data. This is by design for Phase I.
- Task IDs are auto-incrementing and never reused within a session (even after deletion).
- The application is single-user — no authentication or multi-user support is needed for Phase I.
- The toggle behavior for mark-complete means: if pending → completed, if completed → pending.
- Display truncation for long titles/descriptions is a cosmetic concern only; full data is retained internally.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can add a new task in under 5 seconds from command entry to confirmation.
- **SC-002**: Users can view all tasks displayed in a readable, aligned table format.
- **SC-003**: All five operations (add, view, update, delete, mark complete) work correctly as verified by automated tests.
- **SC-004**: Automated test suite achieves greater than 80% code coverage.
- **SC-005**: All error scenarios (invalid ID, empty list, non-existent task) produce clear, user-friendly messages rather than crashes or stack traces.
- **SC-006**: Users can complete a full task lifecycle (add → view → update → complete → delete) in under 30 seconds.
