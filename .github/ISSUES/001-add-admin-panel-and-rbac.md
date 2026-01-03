---
title: "Add admin panel and role-based workflows (Owner / Editor / Organizer)"
labels: ["feature-request"]
assignees: []
---

**Summary**

Build a web admin UI and server-side RBAC to manage events, participants, certificates, and roles (Owner / Editor / Organizer).

**Description**

- Add a web admin interface to manage events and participants.
- Implement role-based permissions to allow Owners/Editors/Organizers to approve/edit events, manage participants, upload certificates, and assign winners.
- Backend changes: roles/permissions model, endpoints to CRUD roles, and enforcement on event/participant endpoints.
- Frontend changes: admin listing for pending events, event edit UI, role assignment UI, audit logs.

**Acceptance criteria**

- Admin UI reachable at `/admin` or equivalent.
- RBAC enforced server-side for relevant endpoints.
- Tests cover permission-critical flows.
- README updated with admin setup and role docs.
