from rich.columns import Columns


class Comments:
    def __init__(self, comment) -> None:
        self.comment = comment

    def print_as_column(self):
        comment_data = [
            (self.comment["date"] + " (edited)" if self.comment["updated"] else self.comment["date"]),
            (self.comment["author"]),
            (" ".join(self.comment["content"])),
        ]
        return Columns(comment_data, equal=True, expand=False)
