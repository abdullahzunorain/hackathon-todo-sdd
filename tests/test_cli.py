"""CLI integration tests using Typer CliRunner."""

import pytest
from typer.testing import CliRunner

import todo_app.main as main_module
from todo_app.main import app
from todo_app.services import TodoService

runner = CliRunner()


@pytest.fixture(autouse=True)
def reset_service() -> None:
    """Reset the shared service before each test."""
    main_module.service = TodoService()


class TestAddCommand:
    """Tests for the `add` CLI command."""

    def test_add_with_title(self) -> None:
        result = runner.invoke(app, ["add", "Buy groceries"])
        assert result.exit_code == 0
        assert "added" in result.output.lower()
        assert "Buy groceries" in result.output

    def test_add_with_title_and_description(self) -> None:
        result = runner.invoke(app, ["add", "Buy groceries", "--description", "Milk, eggs"])
        assert result.exit_code == 0
        assert "added" in result.output.lower()


class TestListCommand:
    """Tests for the `list` CLI command."""

    def test_list_empty(self) -> None:
        result = runner.invoke(app, ["list"])
        assert result.exit_code == 0
        assert "no tasks" in result.output.lower()

    def test_list_with_tasks(self) -> None:
        runner.invoke(app, ["add", "Task one"])
        result = runner.invoke(app, ["list"])
        assert result.exit_code == 0
        assert "Task one" in result.output


class TestCompleteCommand:
    """Tests for the `complete` CLI command."""

    def test_complete_success(self) -> None:
        runner.invoke(app, ["add", "Buy groceries"])
        result = runner.invoke(app, ["complete", "1"])
        assert result.exit_code == 0
        assert "completed" in result.output.lower() or "done" in result.output.lower()

    def test_complete_toggle_back(self) -> None:
        runner.invoke(app, ["add", "Buy groceries"])
        runner.invoke(app, ["complete", "1"])
        result = runner.invoke(app, ["complete", "1"])
        assert result.exit_code == 0
        assert "pending" in result.output.lower()

    def test_complete_not_found(self) -> None:
        result = runner.invoke(app, ["complete", "99"])
        assert result.exit_code == 1
        assert "not found" in result.output.lower()


class TestUpdateCommand:
    """Tests for the `update` CLI command."""

    def test_update_title(self) -> None:
        runner.invoke(app, ["add", "Old title"])
        result = runner.invoke(app, ["update", "1", "--title", "New title"])
        assert result.exit_code == 0
        assert "updated" in result.output.lower()

    def test_update_description(self) -> None:
        runner.invoke(app, ["add", "Title"])
        result = runner.invoke(app, ["update", "1", "--description", "New desc"])
        assert result.exit_code == 0
        assert "updated" in result.output.lower()

    def test_update_not_found(self) -> None:
        result = runner.invoke(app, ["update", "99", "--title", "Nope"])
        assert result.exit_code == 1
        assert "not found" in result.output.lower()

    def test_update_no_changes(self) -> None:
        runner.invoke(app, ["add", "Title"])
        result = runner.invoke(app, ["update", "1"])
        assert result.exit_code == 0
        assert "no changes" in result.output.lower()


class TestDeleteCommand:
    """Tests for the `delete` CLI command."""

    def test_delete_success(self) -> None:
        runner.invoke(app, ["add", "Buy groceries"])
        result = runner.invoke(app, ["delete", "1"])
        assert result.exit_code == 0
        assert "deleted" in result.output.lower()

    def test_delete_not_found(self) -> None:
        result = runner.invoke(app, ["delete", "99"])
        assert result.exit_code == 1
        assert "not found" in result.output.lower()

    def test_delete_removes_from_list(self) -> None:
        runner.invoke(app, ["add", "Buy groceries"])
        runner.invoke(app, ["delete", "1"])
        result = runner.invoke(app, ["list"])
        assert "Buy groceries" not in result.output
