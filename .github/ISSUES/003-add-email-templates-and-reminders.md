---
title: "Add server-side email templating and scheduled event reminders"
labels: ["feature-request"]
assignees: []
---

**Summary**

Add templated email support for reminders, confirmations, and organizer notifications and implement scheduled reminders.

**Description**

- Add email templates for event reminders, registration confirmations, and organizer notices (repo-stored or DB-backed editable templates).
- Provide admin/dev preview for templates.
- Implement scheduled reminder delivery (e.g., via Celery/RQ/cron worker) that sends reminders X hours before events.
- Add tests and developer docs for template editing and scheduler configuration.

**Acceptance criteria**

- Templates exist and can be previewed/sent in development.
- Scheduled reminders enqueue and send test emails.
- Documentation added on editing templates and configuring the scheduler.
