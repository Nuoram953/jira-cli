from rich.console import Console
from models.issue import Issue
import webbrowser
from views.issue import ViewIssue


class Render:
    def __init__(self) -> None:
        self.console = Console()

    def clear(self):
        self.console.clear()

    def show_loading(self, clear_console=True):
        if clear_console:
            self.clear()

        return self.console.status(f"[bold green]Loading...")

    def open_in_web(self, link):
        webbrowser.open("https://google.ca")

    def view_issue(self, issue: Issue, specific_view, web=False):
        if web:
            self.open_in_web(issue.key)
            exit()

        ViewIssue(issue, specific_view)
