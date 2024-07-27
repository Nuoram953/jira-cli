from rich.columns import Columns


class Worklogs:
    def __init__(self, worklog) -> None:
        self.worklog = worklog

    def print_as_column(self):
        worklog_data = [
            (self.worklog["date"]),
            (self.worklog["timeSpent"]),
            (self.worklog["name"]),
            (self.worklog["description"]),
        ]
        return Columns(worklog_data, equal=True, expand=False)
