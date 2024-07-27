from rich.table import Table


class IssuesTable:
    def __init__(self, issue, expand=True) -> None:
        self.table = Table(expand=expand)
        self.issue = issue

        self.create_columns()
        self.create_rows()

    def create_columns(self):
        self.table.add_column("Key", justify="right", style="cyan", no_wrap=True)
        self.table.add_column("Type", style="magenta", max_width=10)
        self.table.add_column("Summary", justify="right", style="green")
        self.table.add_column("status", justify="right", style="green", max_width=30)

    def create_rows(self):
        for subtask in self.issue.subtasks:
            self.table.add_row(
                subtask["id"], subtask["type"], subtask["summary"], subtask["status"]
            )

    def print(self):
        return self.table
