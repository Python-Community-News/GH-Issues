import typing
from .github import get_issue
from .repo import Repo
from .issue_parser import parse_issue_markdown, get_content_issues
class Issue:
    """
    The `Issue` class is the main component of the gh_issues package.
    It is used to parse the issue body and provide a simple interface to the issue data.
    It is also used to get the issues that are referenced in the issue body.
    """
    
    def __init__(self, repo: Repo, issue: dict[str, str | int | bool]):
        self._repo = repo
        for key, value in issue.items():
            setattr(self, f"_{key}", value)
        
        for key,value in parse_issue_markdown(issue['body']).items():
            setattr(self, key, value)


    @property
    def issue_fields(self) -> typing.Generator[str, None, None]:
        """
        Returns a generator of the fields that have embedded issues.
        Only shows fields parsed from the issue body.
        """
        for field in filter(lambda x: not x.startswith("_"), vars(self)):
            if get_content_issues(getattr(self, field)):
                yield field

    @property
    def title(self) -> str:
        return self._title
    
    def get_content_issues(self, field_name: str) -> list['Issue']:
        for issue in get_content_issues(getattr(self, field_name)):
            yield type(self).from_issue_number(self._repo, issue)

    @classmethod
    def from_issue_number(cls, repo: Repo, issue_id: int, api_token: str | None=None) -> 'Issue':
        """Get an issue from a repo. This is the preferred method of getting an issue as it also fetches the issue data"""
        issue = get_issue(
            repo=repo,
            issue_id=issue_id,
            api_token=api_token,
            )
        
        return cls(repo=repo, issue=issue)