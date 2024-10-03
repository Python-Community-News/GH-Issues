import os

import urllib.parse
import httpx

from ._api import API_URL_BASE
from ._repo import Repo


def _api_token_headers(api_token: str | None = None) -> dict[str, str] | None:
    if api_token := os.getenv("GITHUB_API_TOKEN", api_token):
        return {
            "Authorization": f"Bearer {api_token}",
        }


def __check_for_response(url: str, api_token=None) -> httpx.Response:
    response = httpx.get(url, headers=_api_token_headers(api_token))

    if response.status_code not in [200, 201]:
        raise ConnectionRefusedError(
            f"Unable to connect: {response.json()}"
        )  # TODO Better error handling
    return response.json()


def request_issue(
    repo: Repo, issue_id: int, api_token: str | None = None
) -> dict[str, str]:
    """
    Returns the issue with the given id.
    This is a wrapper around the GitHub API Issue call.
    """

    url = f"{repo.url}/issues/{str(issue_id)}"
    return __check_for_response(url=url, api_token=api_token)


def request_issues_by_query(query: str, api_token: str | None = None) -> dict[str, str]:
    """api call to get issues that match a query"""

    url = f"{API_URL_BASE}/search/issues?q={urllib.parse.quote(query, safe='')}"
    return __check_for_response(url=url, api_token=api_token)
