import pytest
import httpx

from gh_issues.issue_parser import get_content_issues, parse_issue_markdown

def test_get_content_issues():
    """Tests that a string with multiple issue numbers will return a list of those numbers"""
    assert get_content_issues(
        body={"issues": "This is a test issue #1 #2 #3"},
        issues_tag="issues",
    ) == [1, 2, 3]

def test_issues_markdown_parsing(issue_text):
    """Test the issue text is parsed into segments"""
    issue = parse_issue_markdown(issue_text)
    assert issue["issue_name"] == "Test Issue"
    assert "skipped_session" not in issue
