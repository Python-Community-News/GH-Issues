import pytest
from gh_issues import Repo
from gh_issues.issue_parser import parse_issue_markdown

@pytest.fixture(scope="session")
def test_repo():
    return Repo(owner="Python-Community-News", repo="Topics")


@pytest.fixture(scope="session")
def issue_dict():
    issue_text = """### Issue Name
Test Issue
### Skipped Section
### Markup Section
**This is bold**
### Issues
Issues Covered: #1, #2, #3, #4
### TextArea Content
Aliquip eiusmod minim excepteur officia **tempor** est incididunt adipisicing elit. Aliqua tempor incididunt magna occaecat esse Nonea nostrud. Irure incididunt Nonea id eu et. Occaecat quis sit laborum labore nisi minim esse ex ea.

Laboris anim pariatur nisi mollit. Qui nostrud id ipsum quis mollit aliqua est amet tempor Nonea. Aute pariatur ullamco qui consequat anim ad nisi ex sit. Quis officia esse incididunt tempor aliqua quis qui est amet. Nisi nostrud sit ea anim voluptate. Est amet mollit consectetur sit et aliquip pariatur nisi enim. Ex sit enim do culpa consectetur irure est duis minim magna do eiusmod est.
"""
    
    return parse_issue_markdown(issue_text)


issue_response = {
    "url": "https://api.github.com/repos/Python-Community-News/Topics/issues/14",
    "repository_url": "https://api.github.com/repos/Python-Community-News/Topics",
    "labels_url": "https://api.github.com/repos/Python-Community-News/Topics/issues/14/labels{/name}",
    "comments_url": "https://api.github.com/repos/Python-Community-News/Topics/issues/14/comments",
    "events_url": "https://api.github.com/repos/Python-Community-News/Topics/issues/14/events",
    "html_url": "https://github.com/Python-Community-News/Topics/issues/14",
    "id": 1409402210,
    "node_id": "I_kwDOH-F6O85UAcVi",
    "number": 14,
    "title": "Test Issue",
    "user": {
        "login": "jonafato",
        "id": 392720,
        "node_id": "MDQ6VXNlcjM5MjcyMA==",
        "avatar_url": "https://avatars.githubusercontent.com/u/392720?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/jonafato",
        "html_url": "https://github.com/jonafato",
        "followers_url": "https://api.github.com/users/jonafato/followers",
        "following_url": "https://api.github.com/users/jonafato/following{/other_user}",
        "gists_url": "https://api.github.com/users/jonafato/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/jonafato/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/jonafato/subscriptions",
        "organizations_url": "https://api.github.com/users/jonafato/orgs",
        "repos_url": "https://api.github.com/users/jonafato/repos",
        "events_url": "https://api.github.com/users/jonafato/events{/privacy}",
        "received_events_url": "https://api.github.com/users/jonafato/received_events",
        "type": "User",
        "site_admin": False
    },
    "labels": [
        {
        "id": 4635205915,
        "node_id": "LA_kwDOH-F6O88AAAABFEehGw",
        "url": "https://api.github.com/repos/Python-Community-News/Topics/labels/content",
        "name": "content",
        "color": "538132",
        "default": False,
        "description": ""
        }
    ],
    "state": "closed",
    "locked": False,
    "assignee": None,
    "assignees": [],
    "milestone": None,
    "comments": 0,
    "created_at": "2022-10-14T14:00:14Z",
    "updated_at": "2022-10-16T13:27:05Z",
    "closed_at": "2022-10-16T13:27:05Z",
    "author_association": "CONTRIBUTOR",
    "active_lock_reason": None,
    "body": "### URL\n\nhttps://surveys.jetbrains.com/s3/c1-python-developers-survey-2022\n\n### When was this post released\n\n20221013\n\n### Summary\n\nThe Python Software Foundation has announced via [Twitter](https://twitter.com/ThePSF/status/1580668956154527745) that the 2022 Developers Survey is now online and accepting responses. The survey, hosted by JetBrains, helps the PSF gain insight into the state of the Python community. Responding takes 10 - 15 minutes, and recipients will be entered into a raffle for a $100 gift card. We encourage all members of the Python community to fill it out. For comparison, results from 2021 survey and links to previous years are available at https://lp.jetbrains.com/python-developers-survey-2021/.\n\n### Code of Conduct\n\n- [ ] I would like my name mentioned on the podcast\n- [X] I agree to follow this project's Code of Conduct",
    "closed_by": {
        "login": "kjaymiller",
        "id": 8632637,
        "node_id": "MDQ6VXNlcjg2MzI2Mzc=",
        "avatar_url": "https://avatars.githubusercontent.com/u/8632637?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/kjaymiller",
        "html_url": "https://github.com/kjaymiller",
        "followers_url": "https://api.github.com/users/kjaymiller/followers",
        "following_url": "https://api.github.com/users/kjaymiller/following{/other_user}",
        "gists_url": "https://api.github.com/users/kjaymiller/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/kjaymiller/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/kjaymiller/subscriptions",
        "organizations_url": "https://api.github.com/users/kjaymiller/orgs",
        "repos_url": "https://api.github.com/users/kjaymiller/repos",
        "events_url": "https://api.github.com/users/kjaymiller/events{/privacy}",
        "received_events_url": "https://api.github.com/users/kjaymiller/received_events",
        "type": "User",
        "site_admin": False
    },
    "reactions": {
        "url": "https://api.github.com/repos/Python-Community-News/Topics/issues/14/reactions",
        "total_count": 0,
        "+1": 0,
        "-1": 0,
        "laugh": 0,
        "hooray": 0,
        "confused": 0,
        "heart": 0,
        "rocket": 0,
        "eyes": 0
    },
    "timeline_url": "https://api.github.com/repos/Python-Community-News/Topics/issues/14/timeline",
    "performed_via_github_app": None,
    "state_reason": "completed"
}

@pytest.fixture(scope="session")
def issue_json():
    return issue_response