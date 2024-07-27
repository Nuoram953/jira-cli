from enum import Enum


class Option(Enum):
    ID = {"full": "--id", "short": "-i", "help": ""}
    SPRINT = {"full": "--sprint", "short": "-s", "help": ""}
    PARENT = {"full": "--parent", "short": "-p", "help": ""}
    WHO = "--who"
    CREATION = "--creation"
    TYPE = "--type"
    WEB = "--web"
    TIME = "--time"
    COMMENT = "--comment"
    PING = "--ping"

    def full(self):
        return self.value["full"]

    def short(self):
        return self.value["short"]

    def help(self):
        return self.value["help"]


class ErrorMessage(Enum):
    WIP = "Not Implemented"
