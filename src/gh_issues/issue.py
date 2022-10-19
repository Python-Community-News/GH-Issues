import re
from collections import defaultdict

from github import get_issue
from markdown_it import MarkdownIt
from markdown_it.tree import SyntaxTreeNode
from repo import Repo


def get_content_issues(
    body: dict[str, Any],
    issues_tag: str,
) -> list[int]:
    """
    Returns Issues Passed in sections of the issue body
    """
    issues = body.get(issues_tag, "")
    return [int(n) for n in re.findall(r"\d+", issues)]


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
        elif content := n.children[0].content == "_No response_":
            continue
        else:
            issue_object[issue_key].append(n.children[0].content)

    return {key: "\n".join(value) for key, value in issue_object.items()}


class Issue:
    def __init__(self, id_: int, issue_fields: list, Repo: Repo):
        self.id_ = id_
        self.raw = get_issue(issue_id=self.episode_id, Repo=Repo)
        self.body = parse_issue_markdown(self.raw["body"])

        for key, value in self.body.items():
            setattr(self, key, value)

        for field in issue_fields:
            issues = get_content_issues(self.body, field)
            
            setattr(
                self,
                field,
                [get_issue(issue, Repo=Repo) for issue in issues],
            )

    @property
    def title(self) -> str:
        return self.raw["title"]