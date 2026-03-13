"""Typer CLI application for Todo management."""

from typing import Optional

import typer

from todo_app import __version__
from todo_app.display import render_error, render_success, render_task_table, render_warning
from todo_app.services import NoChangesError, TaskNotFoundError, TodoService

app = typer.Typer(name="todo", help="In-memory Todo application.")
service = TodoService()


def version_callback(value: bool) -> None:
    if value:
        print(f"todo-app v{__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: bool = typer.Option(
        False, "--version", "-v", help="Show version.", callback=version_callback, is_eager=True
    ),
) -> None:
    """In-memory Todo application with Add, View, Update, Delete, and Complete commands."""


@app.command()
def add(
    title: str = typer.Argument(..., help="Task title."),
    description: str = typer.Option("", "--description", "-d", help="Task description."),
) -> None:
    """Add a new task."""
    if not title.strip():
        render_error("❌ Error: Title cannot be empty.")
        raise typer.Exit(code=1)
    task = service.add_task(title, description)
    render_success(f'✅ Task #{task.id} added: "{task.title}"')


@app.command("list")
def list_tasks() -> None:
    """View all tasks."""
    tasks = service.list_tasks()
    render_task_table(tasks)


@app.command()
def complete(
    task_id: int = typer.Argument(..., help="Task ID to toggle completion."),
) -> None:
    """Toggle task completion status."""
    if task_id < 1:
        render_error("❌ Error: Task ID must be a positive integer.")
        raise typer.Exit(code=1)
    try:
        task = service.toggle_complete(task_id)
        if task.completed:
            render_success(f'✅ Task #{task.id} marked as completed: "{task.title}"')
        else:
            render_success(f'⏳ Task #{task.id} marked as pending: "{task.title}"')
    except TaskNotFoundError:
        render_error(f"❌ Error: Task #{task_id} not found.")
        raise typer.Exit(code=1)


@app.command()
def update(
    task_id: int = typer.Argument(..., help="Task ID to update."),
    title: Optional[str] = typer.Option(None, "--title", "-t", help="New title."),
    description: Optional[str] = typer.Option(None, "--description", "-d", help="New description."),
) -> None:
    """Update a task's title and/or description."""
    if task_id < 1:
        render_error("❌ Error: Task ID must be a positive integer.")
        raise typer.Exit(code=1)
    try:
        task = service.update_task(task_id, title=title, description=description)
        render_success(f'✏️ Task #{task.id} updated: "{task.title}"')
    except TaskNotFoundError:
        render_error(f"❌ Error: Task #{task_id} not found.")
        raise typer.Exit(code=1)
    except NoChangesError:
        render_warning("⚠️ No changes provided. Use --title or --description to update.")


@app.command()
def delete(
    task_id: int = typer.Argument(..., help="Task ID to delete."),
) -> None:
    """Delete a task permanently."""
    if task_id < 1:
        render_error("❌ Error: Task ID must be a positive integer.")
        raise typer.Exit(code=1)
    try:
        task = service.delete_task(task_id)
        render_success(f'🗑️ Task #{task.id} deleted: "{task.title}"')
    except TaskNotFoundError:
        render_error(f"❌ Error: Task #{task_id} not found.")
        raise typer.Exit(code=1)
