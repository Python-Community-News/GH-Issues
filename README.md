# GH Issues

GH Issues is a wrapper for the GitHub API Issues Endpoint that makes it easy to work with a Github Issue's body as a Python object.

## Installation

`pip install gh-issues`

## Usage

```python
from gh_issues import Repo, Issue

repo = Repo(
    owner="python-community-news", repo="gh-issues"
    )
issue = Issue(id_=1, repo=repo)
```

If the issue text is

```markdown
# Issue Header
This is some text
```
the issue would be represented as

```python
issue.issue_header
>>> "This is some text"
```
