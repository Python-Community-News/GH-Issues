import httpx
from pytest_httpx import httpx_mock
from gh_issues import Issue
from gh_issues.repo import Repo


# 14 is just the issue number that was pulled to test this package

def test_issue_from_json(test_repo, issue_json):
    assert Issue(test_repo, issue_json)._number == 14


def test_issue_from_issue_number(test_repo, issue_json, httpx_mock):
    httpx_mock.add_response(
        url="https://api.github.com/repos/Python-Community-News/Topics/issues/14",
        json=issue_json,
    )

    with httpx.Client() as _: 
        issue = Issue.from_issue_number(repo=test_repo, issue_id=14)
        assert issue._number == 14

def test_issue_with_issues_detected(test_repo):
    issue = Issue(test_repo, {"body": "### Issue Header\n #1"""})
    assert 'issue_header' in list(issue.issue_fields)


def test_issue_title(test_repo, issue_json):
    issue = Issue(test_repo, issue_json)
    assert issue.title == "Test Issue"


def test_issue_nested_issue(httpx_mock, test_repo, issue_json):
    issue = Issue(test_repo, {"body": "### Issue Header\n #14"""})
    
    httpx_mock.add_response(
        url="https://api.github.com/repos/Python-Community-News/Topics/issues/14",
        json=issue_json,
    )

    with httpx.Client() as _:
        assert list(issue.get_content_issues('issue_header'))[0]._number == 14