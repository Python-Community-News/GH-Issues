import httpx
from .repo import Repo
import os


def get_issue(
    repo: Repo,
    issue_id: int,
    api_token: str | None = None
) -> dict[str, str]:
    """
    Returns the issue with the given id.
    This is a wrapper around the GitHub API Issue call.
    """

    url = (
        f"{repo.url}/issues/{str(issue_id)}"
    )
    
    if api_token:
        headers = {
            "Authorization": f"Bearer {api_token}",
        }
    
    elif (api_token := os.environ.get('GITHUB_API_TOKEN', None)):
        headers = {
            "Authorization": f"Bearer {api_token}",
        }  
    else:
        headers = {}
    
    response = httpx.get(url, headers=headers)
    if response.status_code not in [200, 201]:
        raise ConnectionRefusedError(f"Unable to connect: {response.json()}") # TODO Better error handling

    return response.json()
