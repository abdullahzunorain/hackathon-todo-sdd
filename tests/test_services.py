"""Unit tests for TodoService."""

import pytest

from todo_app.services import NoChangesError, TaskNotFoundError, TodoService


class TestAddTask:
    """Tests for TodoService.add_task()."""

    def test_add_task_returns_task(self) -> None:
        service = TodoService()
        task = service.add_task("Buy groceries")
        assert task.title == "Buy groceries"

    def test_add_task_assigns_id_starting_from_1(self) -> None:
        service = TodoService()
        task = service.add_task("First task")
        assert task.id == 1

    def test_add_task_auto_increments_id(self) -> None:
        service = TodoService()
        t1 = service.add_task("First")
        t2 = service.add_task("Second")
        assert t1.id == 1
        assert t2.id == 2

    def test_add_task_with_description(self) -> None:
        service = TodoService()
        task = service.add_task("Buy groceries", "Milk, eggs, bread")
        assert task.description == "Milk, eggs, bread"

    def test_add_task_description_defaults_empty(self) -> None:
        service = TodoService()
        task = service.add_task("Buy groceries")
        assert task.description == ""

    def test_add_task_stores_in_service(self) -> None:
        service = TodoService()
        service.add_task("Buy groceries")
        assert len(service._tasks) == 1

    def test_add_task_completed_defaults_false(self) -> None:
        service = TodoService()
        task = service.add_task("Buy groceries")
        assert task.completed is False


class TestListTasks:
    """Tests for TodoService.list_tasks()."""

    def test_list_empty_returns_empty(self) -> None:
        service = TodoService()
        assert service.list_tasks() == []

    def test_list_returns_all_tasks(self) -> None:
        service = TodoService()
        service.add_task("First")
        service.add_task("Second")
        tasks = service.list_tasks()
        assert len(tasks) == 2

    def test_list_returns_tasks_sorted_by_id(self) -> None:
        service = TodoService()
        service.add_task("First")
        service.add_task("Second")
        tasks = service.list_tasks()
        assert tasks[0].id < tasks[1].id


class TestToggleComplete:
    """Tests for TodoService.toggle_complete()."""

    def test_toggle_pending_to_completed(self) -> None:
        service = TodoService()
        service.add_task("Buy groceries")
        task = service.toggle_complete(1)
        assert task.completed is True

    def test_toggle_completed_to_pending(self) -> None:
        service = TodoService()
        service.add_task("Buy groceries")
        service.toggle_complete(1)
        task = service.toggle_complete(1)
        assert task.completed is False

    def test_toggle_not_found_raises(self) -> None:
        service = TodoService()
        with pytest.raises(TaskNotFoundError):
            service.toggle_complete(99)


class TestUpdateTask:
    """Tests for TodoService.update_task()."""

    def test_update_title_only(self) -> None:
        service = TodoService()
        service.add_task("Old title")
        task = service.update_task(1, title="New title")
        assert task.title == "New title"

    def test_update_description_only(self) -> None:
        service = TodoService()
        service.add_task("Title", "Old desc")
        task = service.update_task(1, description="New desc")
        assert task.description == "New desc"
        assert task.title == "Title"

    def test_update_both(self) -> None:
        service = TodoService()
        service.add_task("Old", "Old desc")
        task = service.update_task(1, title="New", description="New desc")
        assert task.title == "New"
        assert task.description == "New desc"

    def test_update_not_found_raises(self) -> None:
        service = TodoService()
        with pytest.raises(TaskNotFoundError):
            service.update_task(99, title="Nope")

    def test_update_no_changes_raises(self) -> None:
        service = TodoService()
        service.add_task("Title")
        with pytest.raises(NoChangesError):
            service.update_task(1)


class TestDeleteTask:
    """Tests for TodoService.delete_task()."""

    def test_delete_removes_task(self) -> None:
        service = TodoService()
        service.add_task("Buy groceries")
        service.delete_task(1)
        assert len(service._tasks) == 0

    def test_delete_returns_deleted_task(self) -> None:
        service = TodoService()
        service.add_task("Buy groceries")
        task = service.delete_task(1)
        assert task.title == "Buy groceries"

    def test_delete_not_found_raises(self) -> None:
        service = TodoService()
        with pytest.raises(TaskNotFoundError):
            service.delete_task(99)

    def test_deleted_id_not_reused(self) -> None:
        service = TodoService()
        service.add_task("First")
        service.delete_task(1)
        t2 = service.add_task("Second")
        assert t2.id == 2
