import pytest
import httpx

from gh_issues.issue_parser import get_content_issues, parse_issue_markdown

def test_get_content_issues():
    """Tests that a string with multiple issue numbers will return a list of those numbers"""
    assert list(get_content_issues(
        "This is a test issue #1 #2 #3",
    )) == ['1', '2', '3']

def test_issues_markdown_parsing(issue_dict):
    """Test the issue text is parsed into segments"""
    assert issue_dict["issue_name"] == "Test Issue"

def test_markup_section(issue_dict):
    assert issue_dict["markup_section"] == "**This is bold**"

def test_empty_sections(issue_dict):
    assert issue_dict["skipped_section"] is None