import dataclasses
import urllib.parse

from ._api import API_URL_BASE


@dataclasses.dataclass
class Repo:
    owner: str
    repo: str

    @property
    def url(self):
        return f"{API_URL_BASE}/repos/{self.owner}/{self.repo}"

    @classmethod
    def from_url(cls, url: str):
        """
        # Example: 'https://api.github.com/repos/<REPO_OWNER>/<REPO_NAME>'
        # path: 'repos/<REPO_OWNER>/<REPO_NAME>'

        """
        _owner_repo = urllib.parse.urlparse(url).path

        owner = _owner_repo[1]
        repo = _owner_repo[2]
        return cls(owner=owner, repo=repo)
