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
issue = Issue(repo=repo, issue_number=1)
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

## Nested Issues

Nested issues are supported. If the issue text is

```markdown
# Issue Header
This is some text referencing issue #2
```

You can access the issue referenced by the issue

```python
for issue in Issue.get_content_issues('issue_header'):
    print(issue.issue_header)

>>> <Issue - #2: This is the issue #2 Title by @user>
```

## Community Standards

This project adheres to the standards highlighted in the [organization repo](https://github.com/python-community-news/.github). You should be able to find the code of conduct, contributing guidelines, and other community standards in the **GitHub Interface** or the [organization repo](https://github.com/python-community-news/.github).
