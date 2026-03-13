# Data Model: Console Todo App

**Feature**: 001-console-todo-app | **Date**: 2026-03-13

## Entities

### Task

Represents a single todo item managed by the application.

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| id | Integer | Yes | Auto-assigned | Unique, auto-incrementing identifier starting from 1. Never reused within a session. |
| title | String | Yes | — | The task title. Must be non-empty. |
| description | String | No | Empty string | Optional details about the task. |
| completed | Boolean | Yes | False | Completion status. False = pending, True = completed. |
| created_at | DateTime | Yes | Current time | Timestamp when the task was created. |
| updated_at | DateTime | Yes | Current time | Timestamp of last modification. Updated on any field change. |

### Validation Rules

- **title**: Must be a non-empty string (whitespace-only strings are rejected)
- **id**: Must be a positive integer (>0) when used as a command argument
- **description**: Can be empty string; no maximum length enforced at model level
- **completed**: Binary state only (no "in-progress" or other states in Phase I)

### State Transitions

```
Task Lifecycle:
  [Created] → pending (completed=False)
       │
       ├── toggle → completed (completed=True)
       │                │
       │                └── toggle → pending (completed=False)
       │
       ├── update → pending/completed (same status, fields changed)
       │
       └── delete → [Removed from memory]
```

### Storage

- **Mechanism**: Python dict with integer keys (task ID) and Task dataclass values
- **ID Generation**: Auto-incrementing counter starting at 1, maintained by the service layer
- **Persistence**: None — all data lost on application exit (by design for Phase I)
- **Capacity**: Limited only by available system memory

## Relationships

No relationships in Phase I. Single entity model.

## Phase II Migration Notes

- The Task dataclass will map to a SQLModel table with the same fields
- `id` becomes a database-generated primary key
- `user_id` foreign key will be added for multi-user support
- `created_at` and `updated_at` will use database-level defaults
- The in-memory dict storage will be replaced by database queries through a repository layer
