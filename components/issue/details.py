from models.issue import Issue


class Details:
    def __init__(self, issue: Issue) -> None:
        self.issue = issue

    def print(self):
        print(f"Title: {self.issue.summary}")
        print(f"Status: {self.issue.status}")
        print(f"Reporter: {self.issue.reporter}")
        print(f"Time: {self.issue.timeSpent} / {self.issue.original_estimate}")
