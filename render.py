from rich import print
from rich.console import Console
from components.issue.time_tracking import TimeTracking
from components.table.issues import IssuesTable
from models.issue import Issue


class Render:
    def __init__(self) -> None:
        self.console = Console()

    def clear(self):
        self.console.clear()

    def show_loading(self, clear_console=True):
        if clear_console:
            self.clear()

        return self.console.status(f"[bold green]Loading...")

    def view_issue(self, issue: Issue):
        self.console.rule("Details")
        print(f"Title: {issue.summary}")
        print(f"Status: {issue.status}")
        print(f"Reporter: {issue.reporter}")
        print(f"Assignee: {issue.assignee}")

        self.console.print("\n")
        self.console.print(TimeTracking(issue).print_as_column())

        self.console.rule("Subtasks")
        self.console.print(IssuesTable(issue).print())

        print("\n")
        self.console.rule("Comments")
    
