from rich.table import Table


class IssueSubtasksTable:
    def __init__(self, issue, expand=True) -> None:
        self.table = Table(expand=expand)
        self.issue = issue

        self.create_columns()
        self.create_rows()

    def create_columns(self):
        self.table.add_column("Key", justify="left", style="cyan", no_wrap=True, vertical="middle", ratio=2)
        self.table.add_column("Summary", justify="left", style="green", no_wrap=True, ratio=6)
        self.table.add_column("status", justify="left", style="green", no_wrap=True, max_width=30, ratio=2)

    def create_rows(self):
        for subtask in self.issue.subtasks:
            self.table.add_row(f"{subtask['id']} ({subtask['type']})", subtask["summary"], subtask["status"])

    def print_as_table(self):
        return self.table
