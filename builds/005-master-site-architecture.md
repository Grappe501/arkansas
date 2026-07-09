# Build #5 — Master Site Architecture & Navigation Blueprint

**Status:** ✅ Complete  
**Version:** 1.9.0  
**Routes:** [/mission-control/architecture.html](/mission-control/architecture.html) · [/explore/](/explore/)

---

## Purpose

Before designing individual pages, the platform needs a **canonical map of every destination**.

This blueprint is what every future build references when adding routes, navigation, cross-links, or content.

## Master Information Architecture v1.0

### Design Philosophy

Layered exploration model — learn basics in minutes, drill down, return to summaries, follow connections, never feel lost.

### What Shipped

- **`data/site-architecture.json`** — 10 primary sections, 82 subsections, secondary nav, action hub, cross-linking rules, URL standards
- **`docs/SITE_ARCHITECTURE.md`** — governing document
- **`/explore/`** — public site map (visitor-facing)
- **`/mission-control/architecture.html`** — team blueprint dashboard
- **Canonical URL redirects** — `/the-story`, `/the-case`, etc. → current hall pages
- **Updated primary navigation** — question-based labels with canonical URLs
- **Reader journey** aligned to Discover → Lead in `knowledge.json`

### Destination Summary

| Status | Count |
|--------|-------|
| Live primary sections | 1 (Home) + partial Reform/Teach/Sources |
| Stub sections (L1 hall pages) | 7 |
| Planned subsections | 76 |
| Total planned destinations | ~100 |

### Honest IA Completion

Information Architecture phase: **~38%** — blueprint locked, URLs reserved, redirects live. Search, glossary, and deep subsection pages not built.

## Next Recommended Build

**Build #6 — Master Content Inventory** — enumerate every page, article, timeline entry, chart, dataset, glossary term, and source file for Version 1.

## Data Discipline

Update `site-architecture.json` and `mission-control.json` on every commit.
