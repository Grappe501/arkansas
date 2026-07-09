# Content Master Registry v1.0

**Build #6** · Citizens United Education Platform  
**Data:** `data/content-inventory.json` · **Dashboard:** [/mission-control/inventory.html](/mission-control/inventory.html)

---

## Purpose

The Master Content Inventory is the canonical registry of every educational asset planned for the platform.

Every page, article, timeline event, chart, glossary term, research file, video, interactive module, downloadable resource, and civic engagement tool must be represented in this registry.

**Nothing is created without first existing here.**

---

## Guiding Principle

> Does this help someone understand *Citizens United* more clearly, more accurately, or more deeply?

If yes, it belongs in the inventory. If no, it should not be built.

---

## Stable ID Standard

Every asset receives a stable ID:

| Prefix | Domain |
|--------|--------|
| `LAND-###` | 1000 — Landing Experience |
| `HIST-###` | 2000 — Historical Foundation |
| `CASE-###` | 3000 — The Case |
| `CONST-###` | 4000 — Constitutional Principles |
| `IMPACT-###` | 5000 — Impact |
| `MONEY-###` | 6000 — Money in Politics |
| `DEBATE-###` | 7000 — Debate & Perspectives |
| `REFORM-###` | 8000 — Reform |
| `CIVIC-###` | 9000 — Civic Leadership |
| `SOURCE-###` | 10000 — Source Library |
| `ACTION-###` | Civic Action modules |
| `CROSS-*` | Cross-domain assets (timeline, glossary, FAQ, charts, etc.) |

Example: `CASE-001`, `HIST-014`, `IMPACT-037`

---

## Content Domains (10)

1. **1000 — Landing Experience** (~25 assets)
2. **2000 — Historical Foundation** (~80)
3. **3000 — The Case** (~90)
4. **4000 — Constitutional Principles** (~75)
5. **5000 — Impact** (~120)
6. **6000 — Money in Politics** (~85)
7. **7000 — Debate & Perspectives** (~70)
8. **8000 — Reform** (~100)
9. **9000 — Civic Leadership** (~80)
10. **10000 — Source Library** (500+)

---

## Cross-Domain Assets

- Interactive Timeline (~250 entries)
- Interactive Glossary (~500 terms)
- FAQ (~300 questions)
- Charts & Infographics (~200)
- Interactive Data Visualizations (~50)
- Downloadable Resources (~75)
- Educational Videos (~100)
- Community Discussion Guides (~40)

---

## Status Lifecycle

1. Planned → 2. Researching → 3. Outlined → 4. Drafting → 5. Technical Review → 6. Fact Check → 7. Citation Review → 8. Editorial Review → 9. Ready for Publication → 10. Published → 11. Monitoring → 12. Revision Needed → 13. Archived

---

## Version 1 Targets

| Asset type | Target |
|------------|--------|
| Educational pages | 825 |
| Timeline entries | 250 |
| Glossary terms | 500 |
| Charts & infographics | 200 |
| Interactive visualizations | 50 |
| Downloadable resources | 75 |
| FAQ questions | 300 |
| Primary source records | 500+ |
| **Total estimated** | **~2,700** |

---

## Metadata Standard

Each item includes: ID, title, domain, parent section, reader level, reader stage, reading time, difficulty, audience, sources required/complete, status, completion %, source status, review status, version, updated, URL, related content, Mission Control link.

---

## Relationship to Other Blueprints

| Document | Tracks |
|----------|--------|
| `PHASE_REGISTRY.md` | Project phases |
| `SITE_ARCHITECTURE.md` | Site destinations & URLs |
| `CONTENT_INVENTORY.md` | Every content asset |

---

*Update `data/content-inventory.json` on every build commit. Regenerate with `scripts/gen-content-inventory.py` when architecture changes.*
