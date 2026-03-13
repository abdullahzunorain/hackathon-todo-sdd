"""Business logic for Todo operations."""

from todo_app.models import Task


class TaskNotFoundError(Exception):
    """Raised when a task ID does not exist."""

    def __init__(self, task_id: int) -> None:
        self.task_id = task_id
        super().__init__(f"Task #{task_id} not found.")


class NoChangesError(Exception):
    """Raised when an update provides no changes."""

    def __init__(self) -> None:
        super().__init__("No changes provided.")


class TodoService:
    """In-memory todo task manager."""

    def __init__(self) -> None:
        self._tasks: dict[int, Task] = {}
        self._next_id: int = 1

    def add_task(self, title: str, description: str = "") -> Task:
        """Create a new task and return it."""
        task = Task(id=self._next_id, title=title, description=description)
        self._tasks[task.id] = task
        self._next_id += 1
        return task

    def list_tasks(self) -> list[Task]:
        """Return all tasks sorted by ID."""
        return sorted(self._tasks.values(), key=lambda t: t.id)

    def toggle_complete(self, task_id: int) -> Task:
        """Toggle a task's completion status."""
        task = self._get_task(task_id)
        task.completed = not task.completed
        task.updated_at = Task.__dataclass_fields__["updated_at"].default_factory()
        return task

    def update_task(
        self, task_id: int, title: str | None = None, description: str | None = None
    ) -> Task:
        """Update a task's title and/or description."""
        if title is None and description is None:
            raise NoChangesError()
        task = self._get_task(task_id)
        if title is not None:
            task.title = title
        if description is not None:
            task.description = description
        task.updated_at = Task.__dataclass_fields__["updated_at"].default_factory()
        return task

    def delete_task(self, task_id: int) -> Task:
        """Remove a task and return the deleted task."""
        task = self._get_task(task_id)
        del self._tasks[task_id]
        return task

    def _get_task(self, task_id: int) -> Task:
        """Retrieve a task by ID or raise TaskNotFoundError."""
        if task_id not in self._tasks:
            raise TaskNotFoundError(task_id)
        return self._tasks[task_id]
