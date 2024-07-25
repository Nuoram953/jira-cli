import requests
from requests.auth import HTTPBasicAuth
import json
from rich.console import Console
from time import sleep
from rich import print
from rich.panel import Panel
from rich.pretty import pprint

from models.issue import Issue

console = Console()

class Jira:
    def __init__(self) -> None:
        pass
        # self.url = f"https://{JIRA_DOMAIN}.atlassian.net/rest/api/3/"
        # self.auth = HTTPBasicAuth(JIRA_EMAIL, JIRA_API_TOKEN)
        # self.headers = {"Accept": "application/json"}

    def get(self, endpoint):
        url = self.url + endpoint
        response = requests.request("GET", url, headers=self.headers, auth=self.auth)

        return self.parse_response(response)

    def parse_response(response):
        status_code = response.status_code
        if status_code == 200:
            return json.loads(response.text)
        elif status_code == 404:
            raise Exception("Not Found")

    def get_issue_by_id(self, id):
        # data = self.get(f"issue/{id}")
        with open('mock.json') as f:
            return Issue(json.load(f))
