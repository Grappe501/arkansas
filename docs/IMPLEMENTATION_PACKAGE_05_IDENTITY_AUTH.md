# Implementation Package 5 of 50

# Citizens United Facts Version 1

## Master Identity, Authentication, Roles & Permissions

**Status:** Implementation Package 5 of 50  
**Target Completion:** January 2027  
**Registry:** [/data/identity-auth-manifest.json](/data/identity-auth-manifest.json) · **Prior:** [IMP-04 Database Schema](/docs/IMPLEMENTATION_PACKAGE_04_DATABASE_SCHEMA.md)

---

# Purpose

The Citizens United Facts platform is built around people.

Not every person needs the same capabilities. A first-time visitor, a learner, an Education Leader, a researcher, and an executive should each have an experience appropriate to their responsibilities.

This package defines the complete identity and authorization model for the institution.

---

# Core Philosophy

```text
One Person
  ↓
One Identity
  ↓
Many Roles
  ↓
Personalized Experience
```

A person signs in once. The platform adapts to who they are and what they do.

---

# Identity Principles

Every account should have:

- A permanent institutional identity
- A personal profile
- A role assignment
- Permission set
- Activity history
- Learning history
- Volunteer history

Institutional memory should follow the person—not the device.

---

# Authentication

The system should support secure authentication.

| Method | Status |
|--------|--------|
| Email/password | Recommended |
| Google | Recommended |
| Apple | Recommended |
| Microsoft | Recommended |
| Enterprise SSO | Future (if needed) |
| Multi-factor authentication | Required for elevated privileges |

Security is mandatory for administrative roles.

---

# Anonymous Visitors

No account required. Visitors may:

- Browse public research
- Read articles
- Use search
- Explore counties and cities
- Read educational materials

Education should remain broadly accessible.

---

# Registered Members

After creating an account, users gain access to:

| Capability | Route / Workspace |
|------------|-------------------|
| Personal dashboard | `/dashboard` |
| Learning progress | `/learn`, `/academy` |
| Bookmarks & saved research | `/dashboard` |
| Event registration | `/events` |
| Notifications | `/notifications` |
| AI assistant | `/ai` |
| Personal calendar | `/dashboard` |
| Community recommendations | `/dashboard` |

---

# Role Hierarchy

Permissions are **additive**. Higher roles include lower-role capabilities unless explicitly scoped.

| Role | ID | Account Required | Primary Workspace |
|------|-----|------------------|-------------------|
| Public Visitor | `public` | No | Public site |
| Registered Member | `member` | Yes | `/dashboard` |
| Volunteer | `volunteer` | Yes | `/volunteer` |
| Education Leader | `education_leader` | Yes | `/leader` |
| Research Contributor | `research_contributor` | Yes | `/research` (draft workspace) |
| Organization Administrator | `organization_admin` | Yes | `/organization` |
| Department Lead | `department_lead` | Yes | Department dashboard |
| Executive Leadership | `executive` | Yes | `/executive`, `/mission-control` |
| System Administrator | `administrator` | Yes | `/admin` |

Users may hold **multiple roles simultaneously**. The platform combines permissions automatically.

Example: Volunteer + Education Leader + Research Contributor.

---

# Permission Categories

Permissions are grouped by **capability**, not individual screens.

| Category | Description |
|----------|-------------|
| Read | View content and data within scope |
| Create | Add new records |
| Edit | Modify existing records |
| Review | Submit for editorial or peer review |
| Approve | Approve content or actions |
| Publish | Make content publicly visible |
| Manage | Oversee users, resources, or projects in scope |
| Delete | Rare; soft-delete preferred |
| Administer | Platform configuration |
| Audit | View change history and security logs |

---

# Geographic Permissions

Leadership permissions should be scoped where appropriate.

| Scope | Role Example | Assignment |
|-------|--------------|------------|
| Neighborhood | Neighborhood Leader | Assigned neighborhood |
| City | City Education Leader | Assigned city |
| County | County Education Director | Assigned county |
| Region | Regional Mentor | Assigned region |
| Statewide | Executive | All Arkansas |

Local responsibility remains local.

---

# Organization Permissions

Users may belong to multiple organizations. Each organization has members, roles, resources, events, and projects.

Organization permissions remain **organization-specific** when appropriate—a coalition partner admin does not automatically gain county leadership permissions.

---

# Identity Lifecycle

```text
Visitor → Registered Member → Learner → Volunteer → Education Leader → Mentor → Institutional Leader
```

Mission Control tracks this progression. See manifest `identity_lifecycle` for stage definitions.

---

# Onboarding

Every new account should experience:

1. Welcome
2. Mission introduction
3. Personal interests
4. County selection
5. City selection
6. Learning recommendations
7. Volunteer opportunities (optional)
8. AI introduction

The first experience should be welcoming and purposeful.

---

# Privacy Controls

Every user controls:

- Profile visibility
- Volunteer visibility
- Communication preferences
- Organization memberships (where appropriate)
- Notification settings
- Public-facing information

Respect for privacy strengthens trust. Aligns with IMP-04 visibility levels.

---

# Security Principles

- Least privilege by default
- Multi-factor authentication for elevated roles
- Session expiration
- Audit logging
- Permission review
- No shared administrator accounts

Security is designed into the platform from the beginning.

---

# Mission Control Integration

Mission Control tracks:

- Registered users · Active users · Volunteers · Education Leaders
- Organization administrators · County leadership · City leadership
- Role distribution · Growth trends

Leadership always understands institutional capacity.

---

# AI Integration

Every user's AI assistant should understand:

- Role and permissions
- Projects and calendar
- Learning history
- Volunteer responsibilities
- Institutional context

The AI becomes increasingly helpful as the user's involvement grows.

---

# Schema & Route Alignment

| Artifact | Path |
|----------|------|
| Identity manifest | `/data/identity-auth-manifest.json` |
| Identity domain (IMP-04) | Domain 1 — Users, Profiles, Roles, Permissions, Sessions |
| Prisma draft | `/prisma/schema.prisma` — User, Role, Permission, UserRole, Session |
| Account routes (IMP-03) | `/login`, `/register`, `/profile`, `/settings`, `/dashboard` |
| ACOS roles | `/data/arkansas-civic-operating-system.json` — 6 roles mapped to 9-role hierarchy |

---

# Success Definition

Package #5 is complete when:

- Every user type is defined
- Every role is documented
- Every permission category is established
- Every identity lifecycle stage is understood
- Every onboarding experience is planned
- Cursor should never need to invent authorization rules during implementation

---

# Deliverables Produced

- Identity Architecture
- Authentication Model
- Role Hierarchy
- Permission Framework
- Geographic Authorization Model
- Organization Authorization Model
- User Lifecycle
- Onboarding Framework
- Privacy Standards
- Security Standards

This becomes the authoritative identity model for the entire Citizens United Facts platform.

---

# Next Package

**Implementation Package 6 of 50 — Master Design System, User Experience & Visual Language**

Typography, colors, layouts, accessibility, reusable components, responsive behavior, dashboard design, maps, charts, and interaction patterns — one cohesive institution.

---

# Governing Principle

Every person should have exactly the access they need to contribute confidently, securely, and effectively.

A well-designed identity system protects the institution, empowers volunteers, and creates a personalized experience that grows alongside each person's journey through Citizens United Facts.
