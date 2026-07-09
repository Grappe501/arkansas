# Cursor Master Build Prompt — Citizens United Facts

Use this as the **single paste-in brief** when starting a Cursor agent session on implementation work.

---

## What this project is

**Citizens United Facts** (public name: **Citizens Facts**) is a volunteer-driven **Arkansas civic education institution** operated by the Arkansas Civic Education Initiative (ACEI).

Subject: **Citizens United**, campaign finance, constitutional literacy, civic education, coalition building, and county/city/neighborhood leadership.

**Not:** a political campaign, party, lobbying org, or temporary project.

---

## Governing principles (always apply)

0. **Technical Constitution (IMP-01):** [/docs/IMPLEMENTATION_PACKAGE_01_TECHNICAL_CONSTITUTION.md](/docs/IMPLEMENTATION_PACKAGE_01_TECHNICAL_CONSTITUTION.md)
0b. **Technical Architecture (IMP-02):** [/docs/IMPLEMENTATION_PACKAGE_02_TECHNICAL_ARCHITECTURE.md](/docs/IMPLEMENTATION_PACKAGE_02_TECHNICAL_ARCHITECTURE.md)
0c. **Route Map (IMP-03):** [/docs/IMPLEMENTATION_PACKAGE_03_ROUTE_MAP.md](/docs/IMPLEMENTATION_PACKAGE_03_ROUTE_MAP.md) · [/data/route-manifest.json](/data/route-manifest.json)
0d. **Database Schema (IMP-04):** [/docs/IMPLEMENTATION_PACKAGE_04_DATABASE_SCHEMA.md](/docs/IMPLEMENTATION_PACKAGE_04_DATABASE_SCHEMA.md) · [/data/canonical-data-manifest.json](/data/canonical-data-manifest.json) · [/prisma/schema.prisma](/prisma/schema.prisma)
1. **Manifesto (#99):** Will this help an ordinary Arkansan understand how self-government works?
2. **Charter (#100):** Knowledge → Citizens → Communities → Arkansas → self-government.
3. **Education before advocacy** — present evidence; Arkansans draw conclusions.
4. **Honest metrics** — never inflate readiness; report generator/formula values only.

---

## Current state

- **100 builds complete** — institutional blueprint documented in `docs/MASTER_*.md`, `data/*.json`, `mission-control/*.html`.
- **Live site:** static HTML/CSS/JS on Netlify — NOT yet Next.js/Prisma/Neon in production.
- **Implementation Package:** 50 ordered steps in `/data/cursor-implementation-package.json`.

---

## Target stack (Technical Architecture #53)

| Layer | Target |
|-------|--------|
| Frontend | Next.js (App Router), React, TypeScript |
| Styling | Tailwind + design tokens from `/design-system/` |
| Hosting | GitHub → Netlify (preview on PR) |
| Database | PostgreSQL (Neon) |
| ORM | Prisma |
| Auth | Email + Google OAuth for admin/MC |

**Migration strategy:** strangler-fig — keep static routes working while migrating slice by slice.

---

## January 2027 MVP goals

- Mission Control operational with real progress tracking
- 75 county dashboards (template from 1 pilot)
- 250 city targets seeded
- Volunteer signup with county/city attribution
- Coalition partner registry (basic CRM)
- Evidence ledger read path + citation on public pages
- Content publish workflow (draft → review → publish)
- 15% connected-voter tracking per county/city (formula documented)
- Executive countdown to 2027-01-01

**Out of scope for MVP:** full ACOS 2.0 personal workspace, autonomous AI institution, 200K relational graph at scale.

---

## How to work

1. Read `/data/cursor-implementation-package.json` — find the **next unimplemented step** (`status: specified`).
2. Read the step's `source_blueprints` JSON routes and `deliverables` file paths.
3. Implement **one step at a time** — minimal diff, match existing conventions in repo.
4. Do not skip auth, permissions, or citation requirements when the step touches them.
5. Update step `status` to `implemented` only when acceptance criteria pass.
6. Never commit secrets (`.env`, credentials).

---

## Key registry files

| Registry | Path |
|----------|------|
| Implementation steps | `/data/cursor-implementation-package.json` |
| Routes | `/data/route-registry.json` |
| Database entities | `/data/database-schema.json` |
| Repository layout | `/data/repository-blueprint.json` |
| Components | `/data/component-registry.json` (if present) or MC components page |
| Evidence | `/data/evidence-registry.json` |
| Mission Control | `/data/mission-control.json` |

---

## Repository conventions

- Build logs: `builds/NNN-slug.md`
- Generators: `scripts/gen-*.py` → `data/*.json`
- MC dashboards: `mission-control/*.html` + `init*()` in `js/mission-control.js`
- Version: `VERSION`, `package.json`, `data/site.json`, `CHANGELOG.md`

---

## When implementing a step, output

1. Files created/modified (exact paths)
2. How to verify (commands or manual checks)
3. Which acceptance criteria are satisfied
4. What remains blocked for the next step

---

## First step to implement

**IMP-01**, **IMP-02**, **IMP-03**, and **IMP-04** are **documented**:
- [Technical Constitution](/docs/IMPLEMENTATION_PACKAGE_01_TECHNICAL_CONSTITUTION.md)
- [Technical Architecture](/docs/IMPLEMENTATION_PACKAGE_02_TECHNICAL_ARCHITECTURE.md)
- [Route Map](/docs/IMPLEMENTATION_PACKAGE_03_ROUTE_MAP.md) · [route-manifest.json](/data/route-manifest.json)
- [Database Schema](/docs/IMPLEMENTATION_PACKAGE_04_DATABASE_SCHEMA.md) · [canonical-data-manifest.json](/data/canonical-data-manifest.json) · [schema.prisma](/prisma/schema.prisma)

**IMP-05** is next: Master User Identity, Authentication, Roles & Permissions (see also engineering IMP-05 repository migration in step registry).

Engineering execution (migration, stack, env, CI) begins at **IMP-05** after data model is documented.
