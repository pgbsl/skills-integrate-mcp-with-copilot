# Script to create GitHub issues automatically using GitHub CLI or API
# This script is intended to be run by a maintainer locally with proper GH auth.

import os
from github import Github

GITHUB_TOKEN = os.environ.get('GH_TOKEN')
if not GITHUB_TOKEN:
    print('Set GH_TOKEN environment variable and rerun')
    exit(1)

g = Github(GITHUB_TOKEN)
repo = g.get_repo('pgbsl/skills-integrate-mcp-with-copilot')

issues = [
    {
        'title': 'Add admin panel and role-based workflows (Owner / Editor / Organizer)',
        'body': open('.github/ISSUES/001-add-admin-panel-and-rbac.md').read(),
        'labels': ['feature-request'],
    },
    {
        'title': 'Add OpenAPI spec and Redoc UI for backend API',
        'body': open('.github/ISSUES/002-add-openapi-and-redoc.md').read(),
        'labels': ['feature-request'],
    },
    {
        'title': 'Add server-side email templating and scheduled event reminders',
        'body': open('.github/ISSUES/003-add-email-templates-and-reminders.md').read(),
        'labels': ['feature-request'],
    },
    {
        'title': 'Add search, bookmark/save, and subscription UX for event discovery',
        'body': open('.github/ISSUES/004-add-search-bookmark-subscribe.md').read(),
        'labels': ['feature-request'],
    },
]

for i in issues:
    repo.create_issue(title=i['title'], body=i['body'], labels=i['labels'])
    print('Created issue: ', i['title'])
