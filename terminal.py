from rich.console import Console
from models.issue import Issue
import webbrowser


class Terminal:
    def __init__(self) -> None:
        self.console = Console()

    def clear(self):
        self.console.clear()

    def show_loading(self, clear_console=True):
        if clear_console:
            self.clear()

        return self.console.status(f"[bold green]Loading...")

    def rule(self, title):
        self.console.print("\n")
        self.console.rule(title)

    def print(self, object_to_print):
        self.console.print(object_to_print)

    def open_in_web(self, link):
        webbrowser.open("https://google.ca")

    def view_issue(self, issue: Issue, specific_view, web=False):
        from views.issue import ViewIssue

        if web:
            self.open_in_web(issue.key)
            exit()

        ViewIssue(issue, specific_view)
