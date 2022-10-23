import httpx
from gh_issues import Issue
from gh_issues.repo import Repo


# 14 is just the issue number that was pulled to test this package

def test_issue_from_json(issue_json):
    assert Issue(issue_json)._number == 14


def test_issue_from_repo(issue_json, httpx_mock):
    httpx_mock.add_response(
        url="https://api.github.com/repos/Python-Community-News/Topics/issues/14",
        json=issue_json,
    )

    with httpx.Client() as _: 
        issue = Issue.from_repo(14, Repo("Python-Community-News", "Topics"))
        assert issue._number == 14

