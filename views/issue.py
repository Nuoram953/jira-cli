from rich.console import Console
from components.issue.time_tracking import TimeTracking
from components.issue.worklogs import Worklogs
from components.table.issues import IssuesTable
from utils import run_all_or_specific


class ViewIssue:
    def __init__(self, issue, single_component=None) -> None:
        self.console = Console()
        self.issue = issue

        run_all_or_specific(self, prefix="generate_", func_name=single_component)

    def generate_detail(self):
        self.console.rule("Details")
        print(f"Title: {self.issue.summary}")
        print(f"Status: {self.issue.status}")
        print(f"Reporter: {self.issue.reporter}")
        print(f"Assignee: {self.issue.assignee}")

        self.console.print("\n")
        self.console.print(TimeTracking(self.issue).print_as_column())

    def generate_subtasks(self):
        self.console.print("\n")
        self.console.print(IssuesTable(self.issue).print())

    def generate_worklogs(self):
        self.console.print("\n")
        self.console.rule("Worklogs")

        for worklog in self.issue.worklogs:
            self.console.print(Worklogs(worklog).print_as_column())

    def generate_comments(self):
        print("\n")
        self.console.rule("Comments")
