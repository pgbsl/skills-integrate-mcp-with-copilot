---
title: "Add OpenAPI spec and Redoc UI for backend API"
labels: ["feature-request"]
assignees: []
---

**Summary**

Generate and serve an OpenAPI (Swagger) schema for public and admin APIs and expose Redoc (or Swagger UI) at `/api/docs`.

**Description**

- Produce an OpenAPI schema that documents endpoints for events, participants, users, admin workflows.
- Serve an interactive docs UI (Redoc or Swagger UI) at `/api/docs` or `/documentation`.
- Add CI check to ensure schema is updated with API changes.
- Document how to generate/update the schema locally.

**Acceptance criteria**

- `/api/docs` serves interactive API docs in development and production.
- CI enforces schema generation or warns on mismatch.
- README updated with instructions.
