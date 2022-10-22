from .github import get_issue
from .repo import Repo
from .issue_parser import parse_issue_markdown, get_content_issues
class Issue:
    def __init__(self, issue_text: dict[str, str]):
        self.body = parse_issue_markdown(issue_text)

        for key, value in self.body.items():
            setattr(self, key, value)

    def get_content_issue_field(self, field_name: str) -> list['Issue']:
        for issue in get_content_issues(getattr(self, field_name)):
            yield type(self)(issue, Repo=self.Repo)

    @property
    def title(self) -> str:
        return self.raw["title"]
    
    @classmethod
    def from_repo(cls, issue_id: int, Repo: Repo, api_token: str | None = None) -> 'Issue':
        issue = get_issue(Repo, issue_id, api_token)
        return cls(issue)