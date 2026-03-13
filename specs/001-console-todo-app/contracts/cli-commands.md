# CLI Command Contract: Console Todo App

**Feature**: 001-console-todo-app | **Date**: 2026-03-13

## Entry Point

```
uv run python -m todo_app <command> [arguments] [options]
```

## Commands

### `add` — Create a new task

**Usage**: `todo_app add <title> [--description <text>]`

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| title | String (positional) | Yes | Task title. Must be non-empty. |
| --description, -d | String (option) | No | Task description. Defaults to empty string. |

**Success Output**: Confirmation message with assigned task ID.
```
✅ Task #1 added: "Buy groceries"
```

**Error Output**:
- Empty title: `❌ Error: Title cannot be empty.`

---

### `list` — View all tasks

**Usage**: `todo_app list`

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|

No parameters.

**Success Output**: Rich-formatted table with columns: ID, Title, Description, Status, Created At.
```
┌────┬─────────────────┬──────────────┬───────────┬─────────────────────┐
│ ID │ Title           │ Description  │ Status    │ Created At          │
├────┼─────────────────┼──────────────┼───────────┼─────────────────────┤
│  1 │ Buy groceries   │ Milk, eggs   │ ✅ Done   │ 2026-03-13 10:30:00 │
│  2 │ Read book       │              │ ⏳ Pending │ 2026-03-13 10:31:00 │
└────┴─────────────────┴──────────────┴───────────┴─────────────────────┘
```

**Empty List Output**: `📋 No tasks found. Add one with: todo_app add "My task"`

---

### `complete` — Toggle task completion status

**Usage**: `todo_app complete <task_id>`

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| task_id | Integer (positional) | Yes | ID of the task to toggle. Must be positive. |

**Success Output** (pending → completed):
```
✅ Task #1 marked as completed: "Buy groceries"
```

**Success Output** (completed → pending):
```
⏳ Task #1 marked as pending: "Buy groceries"
```

**Error Output**:
- Task not found: `❌ Error: Task #99 not found.`
- Invalid ID: `❌ Error: Task ID must be a positive integer.`

---

### `update` — Modify task title and/or description

**Usage**: `todo_app update <task_id> [--title <text>] [--description <text>]`

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| task_id | Integer (positional) | Yes | ID of the task to update. Must be positive. |
| --title, -t | String (option) | No | New title. If omitted, title unchanged. |
| --description, -d | String (option) | No | New description. If omitted, description unchanged. |

**Success Output**:
```
✏️ Task #1 updated: "Buy organic groceries"
```

**Error Output**:
- Task not found: `❌ Error: Task #99 not found.`
- No changes provided: `⚠️ No changes provided. Use --title or --description to update.`
- Invalid ID: `❌ Error: Task ID must be a positive integer.`

---

### `delete` — Remove a task permanently

**Usage**: `todo_app delete <task_id>`

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| task_id | Integer (positional) | Yes | ID of the task to delete. Must be positive. |

**Success Output**:
```
🗑️ Task #1 deleted: "Buy groceries"
```

**Error Output**:
- Task not found: `❌ Error: Task #99 not found.`
- Invalid ID: `❌ Error: Task ID must be a positive integer.`

## Exit Codes

| Code | Meaning |
|------|---------|
| 0 | Success |
| 1 | Error (invalid input, task not found) |

## Global Options

| Option | Description |
|--------|-------------|
| --help | Show help message for any command |
| --version | Show application version |
