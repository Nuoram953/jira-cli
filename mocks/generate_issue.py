from faker import Faker
from random import randint

fake = Faker()


class MockIssue:
    def __init__(self) -> None:
        self.key = ""
        self.summary = fake.text(80)
        self.status = fake.text(20)
        self.assignee = fake.name()
        self.reporter = fake.name()
        self.subtasks = [self.generate_random_subtask() for _ in range(randint(1, 10))]
        self.description = []
        self.comments = []
        self.worklogs = [self.generate_random_worklogs() for _ in range(randint(2, 5))]
        self.original_estimate = self.generate_random_time()
        self.remaining_estimate = self.generate_random_time()
        self.timeSpent = self.generate_random_time()

    def generate_random_subtask(self):
        return {
            "id": f"TEST-{randint(1, 5000)}",
            "type": " ".join(fake.words(randint(1, 3))),
            "summary": fake.text(100),
            "status": " ".join(fake.words(randint(1, 3))),
        }

    def generate_random_worklogs(self):
        return {
            "name": fake.name(),
            "timeSpent": self.generate_random_time(),
            "date": fake.date(),
            "description": fake.text(30),
        }

    def generate_random_time(self):
        return f"{randint(1,24)}h {randint(1,60)}m {randint(1,60)}s"
