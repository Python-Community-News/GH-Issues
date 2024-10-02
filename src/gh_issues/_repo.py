import dataclasses

from ._api import API_URL_BASE


@dataclasses.dataclass
class Repo:
    owner: str
    repo: str

    @property
    def url(self):
        return f"{API_URL_BASE}/repos/{self.owner}/{self.repo}"
