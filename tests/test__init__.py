import pytest
import httpx
import pytest_httpx
from conftest import TEST_QUERY_URL
from gh_issues import issues_by_query, Issue


def test_items_loaded(httpx_mock):
    test_items = [
        {
            "number": 1,
            "repository_url": "https://api.github.com/repos/repo-owner/repo-name",
            "body": "This is issue 1",
        },
        {
            "number": 2,
            "repository_url": "https://api.github.com/repos/repo-owner/repo-name",
            "body": "This is issue 2",
        },
    ]

    httpx_mock.add_response(
        url=TEST_QUERY_URL,
        json={
            "items": test_items,
        },
    )

    with httpx.Client() as _:
        for idx, issue in enumerate(issues_by_query("this test")):
            assert issue.body == test_items[idx]["body"]
            assert isinstance(issue, Issue)
