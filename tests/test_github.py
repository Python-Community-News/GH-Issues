from gh_issues.github import get_issue
import httpx

def test_get_issue_passes_correct_url(httpx_mock, test_repo):
    httpx_mock.add_response(
        url="https://api.github.com/repos/kjaymiller/Python-Community-News/issues/1",
        json={"id": 1},
    )

    with httpx.Client() as _:
        request = get_issue(test_repo, "1")

def test_request_passes_in_api_token(httpx_mock, test_repo):
    httpx_mock.add_response(
        url="https://api.github.com/repos/kjaymiller/Python-Community-News/issues/1",
        json={"id": 1},
        match_headers={"Authorization": "Bearer test"},
    )

    with httpx.Client() as _:
        request = get_issue(test_repo, "1", api_token="test")