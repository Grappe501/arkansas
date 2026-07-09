# Build #21 — GitHub Repository & Folder Structure Blueprint

**Version:** 1.25.0 · **Status:** ✅ Complete  
**Dashboard:** [/mission-control/repository.html](/mission-control/repository.html) · **Constitution:** [/docs/REPOSITORY_ARCHITECTURE.md](/docs/REPOSITORY_ARCHITECTURE.md)

---

## Purpose

Define GitHub and codebase structure before implementation — easy to understand, deploy, audit, and expand.

---

## Four Workstreams

1. Public education website  
2. Mission Control dashboard  
3. Arkansas civic action and coalition tools  
4. Research/source library  

---

## Repository Name

**Recommended:** `citizens-united-facts`  
**Current remote:** `Grappe501/arkansas` *(rename optional)*

---

## Honest Status

| Metric | Value |
|--------|-------|
| Structure readiness | **28%** |
| Current pattern | `flat_static_v0` |
| Has `src/` | **No** |
| Migration executed | **No** |
| Scripts | Python generators (target: `.mjs` validators) |

Build #21 is a **blueprint only** — the flat v0 layout remains in production.

---

## Target Structure

- `docs/` — build-plan, governance, research-standards, deployment, mission-control  
- `src/app/` — routes  
- `src/components/` — UI by domain  
- `src/content/` — educational content  
- `src/data/` — registries  
- `src/lib/` — shared logic  
- `scripts/` — validate-content, validate-sources, generate-mission-control, build-route-registry  
- `tests/` — accessibility, content, smoke  

---

## Branch Model

`main` (production) · `develop` (preview) · `feature/*` · `content/*`

---

## Deliverables

- `.env.example` — placeholder environment variables  
- GitHub labels (14) and milestones (9) defined  
- Migration map: `data/` → `src/data/`, `js/` → `src/lib/`, etc.

---

## Recommended Next: Build #22 — Database Schema & ERD
