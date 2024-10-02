import httpx
import pytest
from gh_issues._github import (
    __check_for_response,
    _api_token_headers,
    _get_issue,
    _request_issue_by_query,
)


TEST_REPO_URL = "https://api.github.com/repos/Python-Community-News/Topics/issues/1"
TEST_QUERY_URL = "https://api.github.com/search/issues?q=this%20test"


def test_api_token_headers_with_token():
    """
    tests that a string can be passed into the _api_token_headers
    and returns a bearer token header
    """

    assert _api_token_headers("test") == {"Authorization": "Bearer test"}


def test_api_token_header_with_env_var(monkeypatch):
    """
    tests that the GITHUB_API_TOKEN environment variable can be passed into the _api_token_headers
    and returns a bearer token header
    """

    monkeypatch.setenv("GITHUB_API_TOKEN", "test")
    assert _api_token_headers("test") == {"Authorization": "Bearer test"}


def test__check_for_response_returns_response(httpx_mock, test_repo):
    httpx_mock.add_response(
        url=TEST_REPO_URL,
        json={"id": 1},
    )

    with httpx.Client() as _:
        response = __check_for_response(TEST_REPO_URL)
        assert response["id"] == 1


def test_request_raises_error_on_404(httpx_mock):
    httpx_mock.add_response(
        url=TEST_REPO_URL,
        status_code=404,
        json={"id": 1},
    )

    with httpx.Client() as _:
        with pytest.raises(ConnectionRefusedError):
            request = __check_for_response(TEST_REPO_URL, "1")


@pytest.mark.parametrize("api_token", [None, "test"])
def test_request_raises_error_on_404(httpx_mock, test_repo, api_token):
    httpx_mock.add_response(
        url=TEST_REPO_URL,
        status_code=404,
        json={"id": 1},
    )

    with httpx.Client() as _:
        with pytest.raises(ConnectionRefusedError):
            request = _get_issue(test_repo, "1", api_token=api_token)


def test_issues_by_query(httpx_mock):
    httpx_mock.add_response(
        url=TEST_QUERY_URL,
        json={"id": 1},
    )

    with httpx.Client() as _:
        request = _request_issue_by_query("this test")
