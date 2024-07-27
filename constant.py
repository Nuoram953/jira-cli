from enum import Enum


class Option(Enum):
    ID = {"full": "--id", "short": "-i", "help": ""}
    SPRINT = {"full": "--sprint", "short": "-s", "help": ""}
    PARENT = {"full": "--parent", "short": "-p", "help": ""}
    WHO = "--who"
    CREATION = "--creation"
    TYPE = "--type"
    WEB = {"full": "--web", "short": "-w", "help": ""}
    TIME = "--time"
    COMMENT = "--comment"
    PING = "--ping"
    VIEW = {"full": "--view", "short": "-v", "help": "", "choice": ["detail", "subtasks", "worklogs", "comments"]}

    def full(self):
        return self.value["full"]

    def short(self):
        return self.value["short"]

    def help(self):
        return self.value["help"]

    def choice(self):
        return self.value["choice"]


class ErrorMessage(Enum):
    WIP = "Not Implemented"
