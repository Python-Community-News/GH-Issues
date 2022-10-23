from gh_issues import Repo

def test_repo_url():
    repo = Repo("foo", "bar")
    assert repo.url == "https://api.github.com/repos/foo/bar"