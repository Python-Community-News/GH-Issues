import httpx
from .repo import Repo


def get_issue(
    Repo: Repo,
    issue_id: int,
    api_token: str | None = None
) -> dict[str, str]:
    """
    Returns the issue with the given id.
    This is a wrapper around the GitHub API Issue call.
    """

    url = (
        f"https://api.github.com/repos/{Repo.owner}/{Repo.repo}/issues/{str(issue_id)}"
    )
    
    if api_token:
        headers = {
            "Authorization": f"Bearer {api_token}",
        }
        request = httpx.get(url, headers=headers)
    else:
        request = httpx.get(url)
    
        if request.status_code not in [200, 201]:
            raise ConnectionRefusedError(f"Unable to connect: {request.json()}") # TODO Better error handling

    return request.json()
