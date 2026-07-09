# Major Screen Wireframe Blueprint

**Screen Architecture v1.0** · **Build #23**  
**Dashboard:** [/mission-control/wireframes.html](/mission-control/wireframes.html) · **Registry:** [/data/wireframe-blueprint.json](/data/wireframe-blueprint.json)

---

## Purpose

Define the major screens before visual design and coding begin.

Each screen supports one of four outcomes:

1. Help readers **understand** *Citizens United*
2. Help readers go deeper into **evidence**
3. Help Arkansans **participate** in education
4. Help the project team track progress through **Mission Control**

---

## Screen Inventory (25 + template)

| # | Screen | Route |
|---|--------|-------|
| 1 | Homepage | `/` |
| 2 | Start Here | `/start-here` |
| 3 | Learning World Landing | `/the-story` (example) |
| 4 | Deep Lesson Page | `/the-case/majority-opinion` |
| 5 | Timeline Page | `/the-story/timeline` |
| 6 | Spending Data Page | `/the-impact/spending-data` |
| 7 | Follow the Money | `/follow-the-money` |
| 8 | Solutions Landing | `/solutions` |
| 9 | Arkansas Hub | `/arkansas` |
| 10 | Teach Your Community | `/teach` |
| 11 | Join | `/join` |
| 12 | Coalition Landing | `/coalition` |
| 13 | Organization Sign-On | `/coalition/sign-on` |
| 14 | Floating Action Hub | *(global)* |
| 15 | Mission Control Dashboard | `/mission-control` |
| 16 | MC Phase Detail | `/mission-control/phases` |
| 17 | Source Library | `/sources` |
| 18 | Public Official Sharing | `/solutions/share-with-officials` |
| 19 | Model Law Workspace | `/solutions/model-laws` |
| 20 | Ballot Initiative Lab | `/solutions/ballot-initiative-lab` |
| 21 | Social Media & Outreach | `/coalition/resources/social` |
| 22 | County Page Template | `/arkansas/[county]` |
| 23 | Admin Signup Review | `/admin/signups` |
| 24 | Admin Coalition Review | `/admin/coalition` |
| 25 | Confirmation Page Template | *(post-form)* |

---

## Mobile Requirements

Every screen must support: thumb-friendly navigation · collapsible sections · readable text · sticky/floating CTA · accessible forms · fast load · clear return paths.

---

## Screen Principle

Every screen should make the next step obvious without making the reader feel pushed. The experience should feel educational, trustworthy, and purposeful.

---

## Integrations

| System | Build | Role |
|--------|-------|------|
| Knowledge Atlas | #19 | Learning worlds → screen groups |
| Component Registry | #17 | UI blocks per section |
| Route Registry | #16 | Canonical routes |
| Database Schema | #22 | Form/signup entities |
