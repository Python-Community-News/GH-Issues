import typing

from ._github import request_issue, request_issues_by_query
from ._issue_parser import get_content_issues, parse_issue_markdown
from ._repo import Repo


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

        try:
            for key, value in parse_issue_markdown(issue["body"]).items():
                setattr(self, key, value)
        except UnboundLocalError:
            self.body = issue["body"]

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

    def get_content_issues(self, field_name: str) -> list["Issue"]:
        for issue in get_content_issues(getattr(self, field_name)):
            yield type(self).from_issue_number(self._repo, issue)

    @classmethod
    def from_issue_number(
        cls, repo: Repo, issue_id: int, api_token: str | None = None
    ) -> "Issue":
        """Get an issue from a repo. This is the preferred method of getting an issue as it also fetches the issue data"""
        issue = request_issue(
            repo=repo,
            issue_id=issue_id,
            api_token=api_token,
        )

        return cls(repo=repo, issue=issue)


def issues_by_query(query: str, api_token: str | None = None) -> typing.Iterator[Issue]:
    """iterates through the reuqests_issue_query creating an Issue object per request"""
    issues = request_issues_by_query(query, api_token)

    for issue in issues["items"]:
        yield Issue(
            repo=Repo.from_url(issue["repository_url"]),
            issue=issue,
        )
