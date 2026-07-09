# Changelog

All notable changes to Citizens Facts are documented here.
Each entry from Ernie corresponds to a new version and GitHub commit.

## [1.5.0] - 2026-07-09 — Build #2 Complete

### Build #2: Project Constitution v1.0 (Governing)
- Canonical constitution in `builds/002-project-constitution.md` + HTML
- Supersedes Build #1 as governing document
- Reader journey: Discover → Understand → Explore → Evaluate → Discuss → Teach → Lead
- Governance test for all future features (3 objectives)
- Action Hub labels aligned to Constitution §8
- Front Door + footer updated to Constitution v1.0

## [1.17.0] - 2026-07-09 — Build #13 Coalition & Outreach

### Coalition Building & Public Outreach System
- First-class **Coalition & Outreach Layer** alongside Education, Research, and Civic Action
- Coalition directory, org profiles, membership levels, resource center, event calendar
- Mission Control coalition dashboard with 75-county org table
- **Homepage three paths:** I'm Here to Learn · I Want to Help · My Organization Wants to Partner

## [1.16.1] - 2026-07-09 — Build #12 Arkansas focus

### Arkansas Civic Participation Constitution
- Refocused Build #12 on **Arkansas as pilot state** — 75-county dashboard, Arkansas Education Ladder, Arkansas Action Hub labels
- `data/arkansas-counties.json` · county-centric participant profiles

## [1.16.0] - 2026-07-09 — Build #12 Complete

### Build #12: Civic Action Ecosystem & Leadership Development System
- **Civic Participation Constitution v1.0** — 7-level growth ladder, education before action
- `data/civic-ecosystem.json` + `js/civic-profile.js` — ladder-aware Action Hub (11 actions)
- Community Conversation Program · Leadership dashboard · Participant schema v1.5

## [1.15.0] - 2026-07-09 — Build #11 Complete

### Build #11: Citizens United Knowledge Graph & Educational Intelligence Architecture
- **Knowledge Graph Constitution v1.0** — 8 object types, 10 clusters, relationship engine
- `data/knowledge-graph.json` + `data/kg-registry.json` (38 nodes, 40 edges)
- `js/explore-further.js` — universal Explore Further on content pages
- Educational intelligence rules · future AI layer spec · Mission Control knowledge map

## [1.14.0] - 2026-07-09 — Build #10 Complete

### Build #10: Master Research & Evidence Framework
- **Research Constitution v1.0** — 5 principles, 5-tier source hierarchy, claim verification
- `data/research-framework.json` + `data/evidence-registry.json` (14 Evidence IDs)
- `docs/RESEARCH_CONSTITUTION.md` · Research dashboard at `/mission-control/research.html`
- Claims ledger cross-linked to Evidence IDs · Source Library trust bar

## [1.13.0] - 2026-07-09 — Build #9 Complete

### Build #9: Visual Design System & Experience Blueprint
- **Design Language v1.0** — institutional identity (museum, library, archive aesthetic)
- `css/design-tokens.css` + `css/components.css` — 14 reusable `ds-*` components
- `data/design-system.json` + `docs/DESIGN_LANGUAGE.md`
- Living showcase at `/design-system/` · Team dashboard at `/mission-control/design.html`
- Emotional journey, domain accent colors, data viz standards, accessibility, trust signals

## [1.12.0] - 2026-07-09 — Build #8 Complete

### Build #8: User Experience Architecture & Journey System
- **Citizen Journey Blueprint v1.0** — 6 personas, 7-stage learning ladder
- `data/ux-journey.json` + `docs/UX_JOURNEY.md`
- Session memory (localStorage), learning panel, Continue Learning prompt
- Adaptive page recommendations · stage-aware Action Hub
- Milestone tracking · success indicators dashboard

## [1.11.0] - 2026-07-09 — Build #7 Complete

### Build #7: Master Requirement ID System & Traceability Framework
- **MRID v1.0** — 165 permanent requirements across 16 domains (GOV, NAV, HOME, CASE, etc.)
- `data/mrid-registry.json` + `docs/MRID_SYSTEM.md`
- Traceability dashboard at `/mission-control/mrid.html` with dependency lookup
- 132 content inventory items cross-linked to MRIDs
- 12-step requirement lifecycle · traceability matrix (phases, builds, content, sources)

## [1.10.0] - 2026-07-09 — Build #6 Complete

### Build #6: Master Content Inventory
- **Content Master Registry v1.0** — 351 items with stable IDs (LAND, HIST, CASE, etc.)
- `data/content-inventory.json` + `docs/CONTENT_INVENTORY.md`
- Filterable inventory at `/mission-control/inventory.html`
- 10 content domains, 8 cross-domain asset classes, 13-step status lifecycle
- V1 targets ~2,700 assets documented; nothing created without registry entry

## [1.9.0] - 2026-07-09 — Build #5 Complete

### Build #5: Master Site Architecture & Navigation Blueprint
- **Master IA v1.0** — 10 primary sections, 82 subsections, reader journey, cross-linking standards
- `data/site-architecture.json` + `docs/SITE_ARCHITECTURE.md`
- Public site map at `/explore/` · Team blueprint at `/mission-control/architecture.html`
- Canonical URL redirects (`/the-story`, `/the-case`, `/teach`, `/sources`, etc.)
- Question-based primary navigation · Discover → Lead ladder aligned

## [1.8.0] - 2026-07-09 — Build #4 Complete

### Build #4: Master Phase Registry v1.0
- Governing **15-phase roadmap** — every feature belongs to exactly one phase
- `data/phase-registry.json` + `docs/PHASE_REGISTRY.md`
- Full registry at `/mission-control/phases.html`
- 100 BUILD_PLAN steps mapped to registry phases in Mission Control
- Phase dependency map, deliverables, completion criteria per phase

## [1.7.0] - 2026-07-09 — Build #3 spec locked

### Build #3: Mission Control Dashboard (governing spec)
- Honest **3%** overall baseline; never inflate completion
- 19 layered progress bars with explanations
- Five questions, step tracker, 20-node build map
- Public readiness score, research readiness (13 categories)
- Deployment + civic action dashboards
- Admin route: `/admin/mission-control/`

## [1.6.0] - 2026-07-09 — Build #3: Mission Control OS

### Added
- **/mission-control/** — NASA-style project operating system dashboard
- `data/mission-control.json` — live BUILD_PLAN data source
- Executive summary, phase cards, build dimensions, public readiness
- Living build map (color-coded nodes)
- Build DNA pages at `/mission-control/build.html?b=N`
- Daily mission briefing, dev console (`?dev=1`)
- Research, content, leadership, repository status cards

## [1.5.0] - 2026-07-09 — Build #2: Project Constitution v1.0

### Added
- Governing constitution (Build #2)
- Reader journey: Discover → Understand → Explore → Evaluate → Discuss → Teach → Lead
- Action Hub aligned to Constitution §8
- Governance test for all features

## [1.4.0] - 2026-07-09 — Civic Action Layer

### Added — Phase 7: Civic Organizing Platform
- **Floating Action Hub** on every page (Take Action menu)
- Action routes: join network, share, invite, draft laws, ballot lab, legislators, ideas
- Participant profile schema (`data/participant-profile-schema.json`)
- `docs/CIVIC_ACTION.md` architecture
- Referral tracking stub (localStorage)
- BUILD_PLAN restructured: 12 phases, steps 54–65 = Civic Action Layer
- Platform model: Learn → Participate → Organize → Build Solutions

## [1.3.0] - 2026-07-09 — Build #1 Complete

### Build #1: Project Mission Statement
- Canonical mission locked in `builds/001-mission-statement.md` + HTML page
- Build registry at `builds/BUILDS.md` and `/builds/`
- Constitution updated to reference Build #1
- Front Door hero aligned with mission (5-minute promise, no overwhelm)

## [1.2.0] - 2026-07-09

### Added — Master Build Plan (100 steps)
- `BUILD_PLAN.md` — full 100-step tracker with completion status
- Project constitution, style guide, citation guide, editorial checklist
- `CONTRIBUTING.md` + GitHub issue templates (content, research, data, design, bug)
- Content inventories: topics, cases, timeline, spending, reform
- Claims ledger (`data/claims-ledger.json`)
- **§3 What the Court Decided** hall page
- **Source Library** at `/library/`
- Homepage: timeline preview, money flow preview, proof section, current fight
- Persistent "Lead Education Locally" sticky CTA
- Form privacy notice
- `develop` branch for PR workflow

## [1.1.0] - 2026-07-09

### Added — Civic Education Engine (Phase 1)
- **Level 0 Front Door** — six plain-language questions + civic education ladder
- **Seven Learning Halls** with drill-down topic lists and four depth levels
- **Hall 7 (LIVE)** — Montana Initiative 194 & Hawaii Act 11 with full depth content
- **Education-to-Action funnel** at `/educate/` with Education Lead signup form (Netlify Forms)
- Knowledge schema at `data/knowledge.json`
- Shared layout (`js/layout.js`) and depth toggle (`js/depth.js`)
- Education design system (`css/education.css`)

## [1.0.0] - 2026-07-09

### Added
- Initial site scaffold (HTML/CSS/JS static site)
- Three-track research framework (legal history, reform efforts, ballot initiatives)
- **Entry 001:** Montana & Hawaii Citizens United comparison
  - Montana Initiative 194 (ballot initiative path)
  - Hawaii Act 11 (legislative test-case path)
- Structured JSON content at `content/entries/001-montana-hawaii-citizens-united.json`
- Site manifest at `data/site.json`
- Netlify deployment configuration
- Version tracking via `VERSION` and `package.json`
