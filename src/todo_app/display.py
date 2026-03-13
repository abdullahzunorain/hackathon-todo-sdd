"""Rich display helpers for terminal output."""

from rich.console import Console
from rich.table import Table

from todo_app.models import Task

console = Console()


def render_task_table(tasks: list[Task]) -> None:
    """Display tasks in a formatted Rich table."""
    if not tasks:
        console.print("\n[bold blue]📋 No tasks found. Add one with:[/] todo_app add \"My task\"\n")
        return

    table = Table(title="Todo List", show_lines=True)
    table.add_column("ID", style="cyan", justify="right", width=5)
    table.add_column("Title", style="white", min_width=15)
    table.add_column("Description", style="dim", min_width=10)
    table.add_column("Status", justify="center", width=12)
    table.add_column("Created At", style="dim", width=20)

    for task in tasks:
        status = "[green]✅ Done[/]" if task.completed else "[yellow]⏳ Pending[/]"
        desc = task.description if len(task.description) <= 50 else task.description[:47] + "..."
        title_display = task.title if len(task.title) <= 40 else task.title[:37] + "..."
        created = task.created_at.strftime("%Y-%m-%d %H:%M:%S")
        table.add_row(str(task.id), title_display, desc, status, created)

    console.print()
    console.print(table)
    console.print()


def render_success(message: str) -> None:
    """Display a success message."""
    console.print(f"[green]{message}[/]")


def render_error(message: str) -> None:
    """Display an error message."""
    console.print(f"[bold red]{message}[/]")


def render_warning(message: str) -> None:
    """Display a warning message."""
    console.print(f"[yellow]{message}[/]")
