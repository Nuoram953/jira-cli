from models.issue import Issue
from rich.columns import Columns


class TimeTracking:
    def __init__(self, issue: Issue) -> None:
        self.issue = issue

    def print_as_column(self):
        print("Time Tracking:")

        time_tracking = [
            (f"Original estimate: {self.issue.original_estimate}"),
            (f"Remaining estimate: {self.issue.remaining_estimate}"),
            (f"Time spent: {self.issue.timeSpent}"),
        ]

        return Columns(time_tracking, equal=True, expand=True)
