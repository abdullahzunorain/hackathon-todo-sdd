"""Unit tests for Task model."""

from datetime import datetime

from todo_app.models import Task


class TestTaskCreation:
    """Test Task dataclass creation and defaults."""

    def test_task_requires_id_and_title(self) -> None:
        task = Task(id=1, title="Buy groceries")
        assert task.id == 1
        assert task.title == "Buy groceries"

    def test_description_defaults_to_empty(self) -> None:
        task = Task(id=1, title="Buy groceries")
        assert task.description == ""

    def test_completed_defaults_to_false(self) -> None:
        task = Task(id=1, title="Buy groceries")
        assert task.completed is False

    def test_created_at_auto_set(self) -> None:
        before = datetime.now()
        task = Task(id=1, title="Buy groceries")
        after = datetime.now()
        assert before <= task.created_at <= after

    def test_updated_at_auto_set(self) -> None:
        before = datetime.now()
        task = Task(id=1, title="Buy groceries")
        after = datetime.now()
        assert before <= task.updated_at <= after

    def test_task_with_all_fields(self) -> None:
        task = Task(id=5, title="Read book", description="Chapter 3", completed=True)
        assert task.id == 5
        assert task.title == "Read book"
        assert task.description == "Chapter 3"
        assert task.completed is True
