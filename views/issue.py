from components.issue.comments import Comments
from components.issue.details import Details
from components.issue.time_tracking import TimeTracking
from components.issue.worklogs import Worklogs
from components.table.issues import IssueSubtasksTable
from models.issue import Issue
from terminal import Terminal
from utils import run_all_or_specific


class ViewIssue:
    def __init__(self, issue: Issue, single_component=None):
        self.issue = issue
        self.terminal = Terminal()

        run_all_or_specific(
            self,
            prefix="generate_",
            func_name=single_component,
            order=[
                "generate_detail",
                "generate_time_tracking",
                "generate_subtasks",
                "generate_comments",
                "generate_worklogs",
            ],
        )

    def generate_detail(self):
        self.terminal.rule("Details")
        Details(self.issue).print()
        self.terminal.print("\n")

    def generate_time_tracking(self):
        TimeTracking(self.issue).print()
        self.terminal.print("\n")

    def generate_subtasks(self):
        self.terminal.print(IssueSubtasksTable(self.issue).print_as_table())
        self.terminal.print("\n")

    def generate_worklogs(self):
        self.terminal.rule("Worklogs")

        for worklog in self.issue.worklogs:
            self.terminal.print(Worklogs(worklog).print_as_column())

    def generate_comments(self):
        self.terminal.rule("Comments")

        for comment in self.issue.comments:
            Comments(comment).print()
