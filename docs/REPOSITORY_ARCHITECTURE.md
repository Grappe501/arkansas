# GitHub Repository & Folder Structure Blueprint

**Repository Architecture v1.0** · **Build #21**  
**Dashboard:** [/mission-control/repository.html](/mission-control/repository.html) · **Registry:** [/data/repository-blueprint.json](/data/repository-blueprint.json)

---

## Purpose

Define the project's GitHub and codebase structure before implementation begins.

The repository should be easy to understand, deploy, audit, and expand — supporting four workstreams:

1. Public education website
2. Mission Control dashboard
3. Arkansas civic action and coalition tools
4. Research/source library

---

## Repository Name

**Recommended:** `citizens-united-facts`  
**Alternative:** `citizens-united-education-platform`

**Current GitHub remote:** `Grappe501/arkansas` *(rename optional — documented in blueprint)*

---

## Branch Structure

| Branch | Purpose |
|--------|---------|
| `main` | Production — deploys to live Netlify |
| `develop` | Integration — Netlify preview |
| `feature/*` | Individual features |
| `content/*` | Content-only changes |

---

## Target Root Structure

```
citizens-united-facts/
├── README.md
├── CONTRIBUTING.md
├── netlify.toml
├── package.json
├── .gitignore
├── .env.example
├── docs/
│   ├── build-plan/
│   ├── governance/
│   ├── research-standards/
│   ├── deployment/
│   └── mission-control/
├── src/
│   ├── app/
│   ├── components/
│   ├── content/
│   ├── data/
│   ├── lib/
│   ├── styles/
│   └── types/
├── public/
│   ├── images/
│   ├── downloads/
│   └── source-documents/
├── scripts/
└── tests/
```

---

## Documentation Folders

| Folder | Purpose |
|--------|---------|
| `docs/build-plan/` | Numbered build documents |
| `docs/governance/` | Constitution, editorial, citation, brand |
| `docs/research-standards/` | Research constitution, facts, source tiers |
| `docs/deployment/` | Netlify, GitHub workflow, env vars |
| `docs/mission-control/` | MC spec, progress model, build records |

---

## Source Folders (Target)

| Path | Purpose |
|------|---------|
| `src/app/` | Route-level pages |
| `src/components/` | Reusable UI (navigation, education, data, civic, coalition, MC, trust, layout) |
| `src/content/` | Educational content by domain |
| `src/data/` | Structured registries (MC, routes, facts, sources, timeline, coalition…) |
| `src/lib/` | Shared logic (MC, citations, forms, search, validation) |
| `src/styles/` | Design tokens and global CSS |
| `src/types/` | TypeScript shared types |

---

## Required Scripts (Target)

| Script | Purpose |
|--------|---------|
| `validate-content.mjs` | Content metadata, MRIDs, reading levels |
| `validate-sources.mjs` | Citation completeness, source IDs |
| `generate-mission-control.mjs` | Build MC dashboard data from registries |
| `build-route-registry.mjs` | Route inventory and missing-page detection |

---

## Environment Variables

See `.env.example` — placeholders only. Never commit secrets.

---

## GitHub Labels

`governance` · `content` · `research` · `design` · `frontend` · `mission-control` · `forms` · `coalition` · `data` · `accessibility` · `deployment` · `bug` · `blocked` · `review-needed`

---

## GitHub Milestones

1. Foundation  
2. Mission Control v1  
3. Public Education Core  
4. Source Library v1  
5. Arkansas Civic Action Layer  
6. Coalition Layer  
7. Netlify Launch  
8. Public Beta  
9. Full Version 1  

---

## Current vs Target (Honest)

**v0 (today):** Flat static site — `data/`, `js/`, `css/`, `halls/`, `mission-control/` at repository root. Python generator scripts. No `src/`, no `tests/`, no framework build step.

**v1 (target):** Framework-based app under `src/` with organized `docs/` and validation scripts.

**Migration:** Not executed in Build #21 — blueprint only. Physical restructure is a future implementation task.

---

## Repository Principle

A new contributor should open the repository and immediately understand:

* What the project is
* Where the build plan lives
* Where content lives
* Where data lives
* How Mission Control works
* How the site deploys
* What is safe to edit

**The repository itself should teach the project.**
