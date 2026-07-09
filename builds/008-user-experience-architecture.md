# Build #8 — User Experience Architecture & Journey System

**Status:** ✅ Complete  
**Version:** 1.12.0  
**Routes:** [/mission-control/journey.html](/mission-control/journey.html)

---

## Purpose

Design the platform around **people**, not pages — the Citizen Journey Blueprint.

## Citizen Journey Blueprint v1.0

### What Shipped

- **`data/ux-journey.json`** — personas, ladder, milestones, recommendations, success indicators
- **`docs/UX_JOURNEY.md`** — governing document
- **`js/journey.js`** — session memory, learning panel, adaptive recommendations
- **`css/journey-panel.css`** — persistent learning panel styles
- **Stage-aware Action Hub** — early vs advanced civic actions
- **`/mission-control/journey.html`** — UX architecture dashboard

### v1 Implementation

| Feature | Status |
|---------|--------|
| Session memory (localStorage) | Live |
| Learning stage estimation | Live |
| Collapsible learning panel | Live |
| Page recommendations | Live |
| Continue Learning prompt | Live (homepage) |
| Milestone tracking | Live |
| Action Hub by stage | Live |

### Six Personas

Curious Citizen · Student · Journalist · Teacher · Community Leader · Researcher

## Next Recommended Build

**Build #9 — First Deep Content** — L2 articles with journey-aware cross-links and MRIDs.

## Data Discipline

Update `ux-journey.json` when personas, milestones, or recommendation logic changes.
