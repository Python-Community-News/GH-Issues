from gh_issues.github import get_issue
import httpx
import pytest

def test_get_issue_passes_correct_url(httpx_mock, test_repo):
    httpx_mock.add_response(
        url="https://api.github.com/repos/Python-Community-News/Topics/issues/1",
        json={"id": 1},
    )

    with httpx.Client() as _:
        request = get_issue(test_repo, "1")

def test_request_passes_in_api_token(httpx_mock, test_repo):
    """Test that the API token is passed in the request"""
    httpx_mock.add_response(
        url="https://api.github.com/repos/Python-Community-News/Topics/issues/1",
        json={"id": 1},
        match_headers={"Authorization": "Bearer test"},
    )

    with httpx.Client() as _:
        request = get_issue(test_repo, "1", api_token="test")

        
def test_request_api_from_env(monkeypatch, httpx_mock, test_repo):
    """Test that the API token is read from the environment variable"""
    monkeypatch.setenv("GITHUB_API_TOKEN", "test")
    httpx_mock.add_response(
        url="https://api.github.com/repos/Python-Community-News/Topics/issues/1",
        json={"id": 1},
        match_headers={"Authorization": "Bearer test"},
    )

    with httpx.Client() as _:
        request = get_issue(test_repo, "1")
    
def test_request_raises_error_on_404(httpx_mock, test_repo):
    httpx_mock.add_response(
        url="https://api.github.com/repos/Python-Community-News/Topics/issues/1",
        status_code=404,
        json={"id": 1},
    )

    with httpx.Client() as _:
        with pytest.raises(ConnectionRefusedError):
            request = get_issue(test_repo, "1")