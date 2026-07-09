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
0e. **Identity & Auth (IMP-05):** [/docs/IMPLEMENTATION_PACKAGE_05_IDENTITY_AUTH.md](/docs/IMPLEMENTATION_PACKAGE_05_IDENTITY_AUTH.md) · [/data/identity-auth-manifest.json](/data/identity-auth-manifest.json)
0f. **Design System (IMP-06):** [/docs/IMPLEMENTATION_PACKAGE_06_DESIGN_SYSTEM.md](/docs/IMPLEMENTATION_PACKAGE_06_DESIGN_SYSTEM.md) · [/data/design-system-manifest.json](/data/design-system-manifest.json)
0g. **Mission Control Architecture (IMP-07):** [/docs/IMPLEMENTATION_PACKAGE_07_MISSION_CONTROL.md](/docs/IMPLEMENTATION_PACKAGE_07_MISSION_CONTROL.md) · [/data/mission-control-architecture-manifest.json](/data/mission-control-architecture-manifest.json)
0h. **LocalBrain Network (IMP-08):** [/docs/IMPLEMENTATION_PACKAGE_08_LOCALBRAIN_ARCHITECTURE.md](/docs/IMPLEMENTATION_PACKAGE_08_LOCALBRAIN_ARCHITECTURE.md) · [/data/localbrain-network-manifest.json](/data/localbrain-network-manifest.json)
0i. **Knowledge Graph (IMP-09):** [/docs/IMPLEMENTATION_PACKAGE_09_KNOWLEDGE_GRAPH.md](/docs/IMPLEMENTATION_PACKAGE_09_KNOWLEDGE_GRAPH.md) · [/data/knowledge-graph-manifest.json](/data/knowledge-graph-manifest.json)
0j. **Content Management (IMP-10):** [/docs/IMPLEMENTATION_PACKAGE_10_CONTENT_MANAGEMENT.md](/docs/IMPLEMENTATION_PACKAGE_10_CONTENT_MANAGEMENT.md) · [/data/content-management-manifest.json](/data/content-management-manifest.json)
0k. **Research Institute (IMP-11):** [/docs/IMPLEMENTATION_PACKAGE_11_RESEARCH_INSTITUTE.md](/docs/IMPLEMENTATION_PACKAGE_11_RESEARCH_INSTITUTE.md) · [/data/research-institute-manifest.json](/data/research-institute-manifest.json)
0l. **Education Academy (IMP-12):** [/docs/IMPLEMENTATION_PACKAGE_12_COMMUNITY_EDUCATION_ACADEMY.md](/docs/IMPLEMENTATION_PACKAGE_12_COMMUNITY_EDUCATION_ACADEMY.md) · [/data/education-academy-manifest.json](/data/education-academy-manifest.json)

## Master timeline (updated IMP-11)

| Phase | Target | Focus |
|-------|--------|-------|
| **Software complete** | **July 11, 2026** | Feature-complete platform |
| **75 counties** | **October 1, 2026** | County profiles, dashboards, Education Leaders in all 75 counties |
| **Organizational readiness** | **January 2027** | Statewide volunteer development, city/neighborhood systems mature, launch certification |

Between the two dates: populate content, train volunteers, expand leadership, validate operations (~6 months build-out).
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

## January 2027 organizational goals (Phase Two)

After **software completion (July 11, 2026)**, organizational build-out targets:

- Mission Control operational with real progress tracking
- 75 county dashboards (template from 1 pilot)
- 250 city targets seeded
- Volunteer signup with county/city attribution
- Coalition partner registry (basic CRM)
- Evidence ledger read path + citation on public pages
- Content publish workflow (draft → review → publish)
- 15% connected-voter tracking per county/city (formula documented)
- Executive countdown to organizational readiness (Jan 2027); software target Jul 11, 2026

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

**IMP-01** through **IMP-12** are **documented**:
- [Technical Constitution](/docs/IMPLEMENTATION_PACKAGE_01_TECHNICAL_CONSTITUTION.md)
- [Technical Architecture](/docs/IMPLEMENTATION_PACKAGE_02_TECHNICAL_ARCHITECTURE.md)
- [Route Map](/docs/IMPLEMENTATION_PACKAGE_03_ROUTE_MAP.md) · [route-manifest.json](/data/route-manifest.json)
- [Database Schema](/docs/IMPLEMENTATION_PACKAGE_04_DATABASE_SCHEMA.md) · [canonical-data-manifest.json](/data/canonical-data-manifest.json)
- [Identity & Auth](/docs/IMPLEMENTATION_PACKAGE_05_IDENTITY_AUTH.md) · [identity-auth-manifest.json](/data/identity-auth-manifest.json)
- [Design System](/docs/IMPLEMENTATION_PACKAGE_06_DESIGN_SYSTEM.md) · [design-system-manifest.json](/data/design-system-manifest.json)
- [Mission Control Architecture](/docs/IMPLEMENTATION_PACKAGE_07_MISSION_CONTROL.md) · [mission-control-architecture-manifest.json](/data/mission-control-architecture-manifest.json)
- [LocalBrain Network](/docs/IMPLEMENTATION_PACKAGE_08_LOCALBRAIN_ARCHITECTURE.md) · [localbrain-network-manifest.json](/data/localbrain-network-manifest.json)
- [Knowledge Graph](/docs/IMPLEMENTATION_PACKAGE_09_KNOWLEDGE_GRAPH.md) · [knowledge-graph-manifest.json](/data/knowledge-graph-manifest.json)
- [Content Management](/docs/IMPLEMENTATION_PACKAGE_10_CONTENT_MANAGEMENT.md) · [content-management-manifest.json](/data/content-management-manifest.json)
- [Research Institute](/docs/IMPLEMENTATION_PACKAGE_11_RESEARCH_INSTITUTE.md) · [research-institute-manifest.json](/data/research-institute-manifest.json)
- [Education Academy](/docs/IMPLEMENTATION_PACKAGE_12_COMMUNITY_EDUCATION_ACADEMY.md) · [education-academy-manifest.json](/data/education-academy-manifest.json)

**IMP-13** is next (doctrinal): Master Volunteer Network, Education Leader Pipeline & Community Organizing Platform.

Engineering **Sprint Zero (IMP-10 step registry)** is the Band A gate before Band B code slices.
