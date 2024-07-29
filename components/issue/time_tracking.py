from rich.console import Console
from models.issue import Issue
from rich.columns import Columns


class TimeTracking:
    def __init__(self, issue: Issue) -> None:
        self.issue = issue
        self.console = Console()

    def print(self):
        print("Time Tracking:")
        self.console.print(f"Original estimate: {self.issue.original_estimate}"),
        self.console.print(f"Remaining estimate: {self.issue.remaining_estimate}"),
        self.console.print(f"Time spent: {self.issue.timeSpent}"),

    def print_as_column(self):
        print("Time Tracking:")

        time_tracking = [
            (f"Original estimate: {self.issue.original_estimate}"),
            (f"Remaining estimate: {self.issue.remaining_estimate}"),
            (f"Time spent: {self.issue.timeSpent}"),
        ]

        return Columns(time_tracking, equal=True, expand=True)
