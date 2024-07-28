from utils import run_all_or_specific


class Issue:
    def __init__(self, api_response) -> None:
        self.api_response = api_response
        self.fields = api_response["fields"]

        self.key = ""
        self.summary = None
        self.status = None
        self.assignee = None
        self.reporter = None
        self.subtasks = []
        self.description = []
        self.comments = []
        self.worklogs = []

        self.original_estimate = None
        self.remaining_estimate = None
        self.timeSpent = None

        run_all_or_specific("set_")

    def is_field_exist(self, field):
        return field in self.fields

    def set_summary(self):
        if not self.is_field_exist("summary"):
            return

        self.summary = self.fields["summary"]

    def set_assignee(self):
        if not self.is_field_exist("assignee"):
            return

        self.assignee = self.fields["assignee"]["displayName"]

    def set_reporter(self):
        if not self.is_field_exist("reporter"):
            return

        self.reporter = self.fields["reporter"]["displayName"]

    def set_timetracking(self):
        if not self.is_field_exist("timetracking"):
            return

        self.original_estimate = self.fields["timetracking"]["originalEstimate"]
        self.remaining_estimate = self.fields["timetracking"]["remainingEstimate"]
        self.timeSpent = self.fields["timetracking"]["timeSpent"]

    def set_worklogs(self):
        if not self.is_field_exist("worklog"):
            return

        for worklog in self.fields["worklog"]:
            self.worklogs.append({"name": "", "timeSpent": "", "date": "", "description": ""})

    def set_subtasks(self):
        if not self.is_field_exist("subtasks"):
            return

        for subtask in self.fields["subtasks"]:
            self.subtasks.append(
                {
                    "id": subtask["key"],
                    "type": subtask["fields"]["issuetype"]["name"],
                    "summary": subtask["fields"]["summary"],
                    "status": subtask["fields"]["status"]["name"],
                }
            )

    def set_description(self):
        if not self.is_field_exist("description"):
            return

        for content in self.fields["description"]["content"]:
            for line in content["content"]:
                self.description.append(line["text"])

    def set_comments(self):
        if not self.is_field_exist("comment"):
            return

        for comment in self.fields["comment"]:
            self.comments.append(
                {
                    "author": comment["author"]["displayName"],
                    "content": [content["text"] for content in comment["body"]["content"]],
                    "date": comment["created"],
                    "updated": comment["updated"],
                }
            ),
