import requests
from requests.auth import HTTPBasicAuth
import json
from rich.console import Console
from dotenv import load_dotenv
from mocks.generate_issue import MockIssue
import os

console = Console()
load_dotenv()


class Jira:
    def __init__(self) -> None:
        self.is_debug = os.getenv("IS_DEBUG") == "True"
        self.url = f"https://{os.getenv('JIRA_DOMAIN')}.atlassian.net/rest/api/3/"
        self.auth = HTTPBasicAuth(os.getenv("JIRA_EMAIL"), os.getenv("JIRA_API_TOKEN"))
        self.headers = {"Accept": "application/json"}

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
        if self.is_debug:
            return MockIssue()

        return self.get(f"issue/{id}")
