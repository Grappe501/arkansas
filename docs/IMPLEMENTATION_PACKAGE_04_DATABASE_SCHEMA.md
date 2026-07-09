# Implementation Package 4 of 50

# Citizens United Facts Version 1

## Master Database Schema & Canonical Data Model

**Status:** Implementation Package 4 of 50  
**Target Completion:** January 2027  
**Registry:** [/data/canonical-data-manifest.json](/data/canonical-data-manifest.json) · **Prior:** [IMP-03 Route Map](/docs/IMPLEMENTATION_PACKAGE_03_ROUTE_MAP.md)

---

# Purpose

The database is the institutional memory of Citizens United Facts.

If the database is designed correctly, every page, dashboard, AI assistant, report, LocalBrain, Mission Control view, and future feature will naturally fit together.

This document defines the **canonical data model** for the institution. There should be **one source of truth** for every important piece of information.

---

# Database Philosophy

Every important entity exists **once**. Everything else references it.

Examples: one county · one city · one volunteer · one organization · one research article · one court case · one lesson · one project · one event.

Duplicate information creates institutional confusion.

---

# Universal Record Standards

Every major table should include:

| Field | Purpose |
|-------|---------|
| UUID | Stable internal identifier |
| Public Slug | URL-safe identifier (if applicable) |
| Created Date | When record entered the system |
| Updated Date | Last modification timestamp |
| Status | Lifecycle state (see Soft Deletes) |
| Owner | Responsible person or role |
| Version | Content or schema version |
| Visibility | Security classification level |
| Last Reviewed | Editorial or governance review date |
| Tags | Cross-cutting categorization |
| Notes | Internal context (non-public) |

Every record becomes traceable.

---

# Core Entity Groups

The platform is organized into twelve primary domains.

| # | Domain | Primary Tables |
|---|--------|----------------|
| 1 | Identity | Users, Profiles, Roles, Permissions, Sessions, Auth Providers, Notification Preferences, Privacy Settings |
| 2 | Geography | Counties, Cities, Neighborhoods, Legislative Districts, Congressional Districts, School Districts, Regions, ZIP Codes |
| 3 | Organizations | Organizations, Coalition Members, Partners, Libraries, Universities, Community Groups, Historical Societies, Faith Organizations, Contacts |
| 4 | People | Education Leaders, Volunteers, Researchers, Authors, Presenters, Mentors, SMEs, Staff (future) |
| 5 | Research | Articles, Court Cases, Statutes, Constitutional Provisions, Primary/Secondary Sources, Citations, Claims, Evidence, Reviews |
| 6 | Education | Courses, Lessons, Modules, Learning Paths, Quizzes, Certificates, Progress, Cohorts, Presentation Materials |
| 7 | Community | Conversations, Events, Meeting Notes, Questions, Requests, Volunteer Opportunities, Neighborhood Groups, Listening Reports |
| 8 | Operations | Projects, Tasks, Milestones, Risks, Dependencies, Departments, Committees, Decision Log, Institutional Calendar |
| 9 | Mission Control | Dashboards, Metrics, KPIs, Goals, County/City/Neighborhood Health, Institution Health, Readiness Scores |
| 10 | AI | LocalBrains, Agents, Prompt Library, Knowledge Retrieval, Conversation History, Tasks, Recommendations, Feedback |
| 11 | Content | Articles, News, Videos, Media Assets, FAQs, Glossary, Downloads, Infographics, Presentation Decks |
| 12 | Governance | Policies, Operating Manuals, Constitution, Implementation Packages, Board Decisions, Review Schedules, Version History, Standards |

---

# Relationship Standards

Relationships should be modeled explicitly.

```text
County
  ↓ Cities
    ↓ Neighborhoods
      ↓ Education Leaders
        ↓ Community Conversations
          ↓ Events
            ↓ Volunteers
              ↓ Projects
```

Nothing should exist without context.

---

# Many-to-Many Relationships

Join tables preserve flexibility. Examples:

| Relationship | Join Table Pattern |
|--------------|-------------------|
| Volunteer ↔ Organization | `volunteer_organizations` |
| Volunteer ↔ County | `volunteer_counties` |
| Volunteer ↔ Project | `volunteer_projects` |
| Course ↔ Lesson | `course_lessons` |
| Research ↔ Court Case | `research_court_cases` |
| Organization ↔ Event | `organization_events` |
| Education Leader ↔ City | `leader_cities` |
| Community Conversation ↔ Resources | `conversation_resources` |

Existing schema join tables in [/data/database-schema.json](/data/database-schema.json): `person_organizations`, `event_resources`, `resource_sources`, `fact_sources`, and others.

---

# Canonical Identifiers

Every entity receives:

- **Internal UUID** — database primary key
- **Public slug** — human-readable URL segment
- **Human-readable title** — display name
- **Search aliases** — alternate names for search
- **Legacy references** — migration IDs from JSON registries (if needed)

Stable identifiers simplify integration across routes (IMP-03), APIs, and Mission Control.

---

# Search Index

Every searchable object should include:

Title · Summary · Keywords · Categories · Tags · Related entities · Geographic references · Publication status

The search engine indexes all major institutional knowledge. Unified search route: `/search` (IMP-03).

---

# Audit Trail

Every important change records:

- Who changed it
- When it changed
- What changed
- Why it changed (optional note)

Mission Control can reconstruct institutional history.

---

# Soft Deletes

Records should rarely be permanently deleted. Status values:

| Status | Meaning |
|--------|---------|
| Active | Current, visible per visibility rules |
| Archived | Retained but not actively displayed |
| Deprecated | Superseded; link to replacement |
| Historical | Preserved for institutional memory |

---

# Data Validation

Every table should define:

- Required fields
- Optional fields
- Validation rules
- Business rules
- Relationship constraints

Data quality begins at entry.

---

# Security Classification

Every record carries a visibility level. Permissions are data-driven rather than hard-coded.

| Level | Audience |
|-------|----------|
| Public | Anyone |
| Volunteer | Authenticated volunteers |
| Education Leader | Leaders and above |
| Organization | Coalition workspace members |
| Executive | Executive workspace |
| Mission Control | Institution operators |
| Administrator | System administrators |

---

# AI Integration

Every major entity should be available to LocalBrains through structured retrieval. AI reasons from connected knowledge:

```text
Research Article → Court Case → Claim → Evidence → Lesson → Presentation → Community Conversation
```

See [/data/canonical-data-model.json](/data/canonical-data-model.json) for relationship engine and future AI readiness.

---

# Mission Control Integration

Mission Control reads rather than duplicates operational data. It reports on every county, city, project, volunteer, lesson, organization, and dashboard without creating duplicate databases.

MC metrics source: entity tables and [/data/database-schema.json](/data/database-schema.json) `mission_control_metrics`.

---

# Schema Artifacts

| Artifact | Path | Role |
|----------|------|------|
| IMP-04 Constitution | This document | Governing data model doctrine |
| Canonical Manifest | `/data/canonical-data-manifest.json` | 12 domains, standards, contracts |
| Canonical Model | `/data/canonical-data-model.json` | Relationship engine + canonical objects |
| Database Schema | `/data/database-schema.json` | Entity tables, fields, join tables |
| Prisma Draft | `/prisma/schema.prisma` | Migration-ready ORM schema (draft) |
| Relationship Registry | `/data/relationship-registry.json` | Typed relationship definitions |

---

# Success Definition

Package #4 is complete when:

- Every major institutional concept has a canonical home
- Every relationship is defined
- Every future module knows where its data belongs
- Every AI has a structured knowledge source
- Mission Control has a complete institutional data model

---

# Deliverables Produced

- Canonical Data Model
- Entity Registry (12 domains)
- Relationship Model
- Search Model
- Security Model
- Audit Model
- AI Data Contracts
- Mission Control Data Contracts
- Governance Data Standards

This becomes the blueprint for every database migration, API, report, AI query, and dashboard built for Citizens United Facts.

---

# Next Package

**Implementation Package 5 of 50 — Master User Identity, Authentication, Roles & Permissions**

Every user type, authentication flow, authorization rule, role hierarchy, permission model, onboarding path, and identity lifecycle across the platform.

---

# Governing Principle

A healthy institution is built on trustworthy information.

A trustworthy database creates trustworthy systems.

A trustworthy system earns public trust.

That is why the canonical data model is one of the most important foundations of the entire institution.
