import dataclasses


@dataclasses.dataclass
class Repo:
    owner: str
    repo: str

    @property
    def url(self):
        return f"https://api.github.com/repos/{self.owner}/{self.repo}"
