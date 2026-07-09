# Changelog

All notable changes to Citizens Facts are documented here.
Each entry from Ernie corresponds to a new version and GitHub commit.

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
