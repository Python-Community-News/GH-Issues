import re
from collections import defaultdict

from .github import get_issue
from markdown_it import MarkdownIt
from markdown_it.tree import SyntaxTreeNode
from .repo import Repo

def _parse_text_dict(section: list[str]) -> str | None:
    """Parse the issue dict into a string. If the list is empty, return None"""
    if section == []:
        return
    return "\n".join([value for value in section if value])


def get_content_issues(
    section: str,
) -> list[str]:
    """
    Returns Issues Passed in sections of the issue body
    """
    return re.findall(r"\d+", section)


def parse_issue_markdown(text) -> dict[str, str]:
    """Use markdownit to split at section headings"""
    md = MarkdownIt("zero", {"maxNesting": 1})
    md.enable(["heading", "paragraph"])
    tokens = md.parse(text)
    node = SyntaxTreeNode(tokens)
    issue_object = defaultdict(list)
    
    for n in node.children:
        if n.type == "heading":
            issue_key = n.children[0].content.lower().replace(" ", "_")
            issue_object[issue_key] 
        else:
            issue_object[issue_key].append(n.children[0].content)

    return {key: _parse_text_dict(value) for key, value in issue_object.items()}