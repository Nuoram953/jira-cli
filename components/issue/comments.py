from rich.columns import Columns
from pprint import pprint

from rich.console import Console


class Comments:
    def __init__(self, comment) -> None:
        self.comment = comment
        self.console = Console()

        self.comment_data = [
            (
                self.comment["date"] + f" (edited - {self.comment['updated']})"
                if self.comment["updated"]
                else self.comment["date"]
            ),
            (self.comment["author"]),
            (" ".join(self.comment["content"])),
        ]

    def print(self):
        for line in self.comment_data:
            self.console.print(line)
        self.console.print("\n")

    def print_as_column(self):
        return Columns(self.comment_data, equal=True, expand=False)
