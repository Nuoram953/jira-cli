class Issue:
    def __init__(self, api_response) -> None:
        self.api_response = api_response
        self.fields = api_response["fields"]

        self.summary = None
        self.assignee = None
        self.reporter = None
        self.timeSpentSeconds = 0
        self.subtasks = []
        self.description = []

        set_data_func = (
            self.set_summary,
            self.set_assignee,
            self.set_reporter,
            self.set_worklogs,
            self.set_subtasks,
            self.set_description,
        )

        for func in set_data_func:
            func()

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

    def set_worklogs(self):
        if not self.is_field_exist("worklog"):
            return

        for worklog in self.fields["worklog"]:
            self.timeSpentSeconds += worklog["timeSpentSeconds"]

    def set_subtasks(self):
        if not self.is_field_exist("subtasks"):
            return

        for subtask in self.fields["subtasks"]:
            self.subtasks.append(subtask)

    def set_description(self):
        if not self.is_field_exist("description"):
            return

        for content in self.fields["description"]["content"]:
            for line in content["content"]:
                self.description.append(line["text"])
