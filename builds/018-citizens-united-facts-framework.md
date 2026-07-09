# Build #18 — Citizens United Facts Framework

**Version:** 1.22.0 · **Status:** ✅ Complete  
**Dashboard:** [/mission-control/facts.html](/mission-control/facts.html) · **Constitution:** [/docs/FACTS_CONSTITUTION.md](/docs/FACTS_CONSTITUTION.md)

---

## Purpose

Define what the platform considers a **fact** and how facts are organized — the foundation for all educational content before hundreds of pages are written.

Every factual statement must be traceable, categorized, and connected to supporting evidence.

---

## Deliverables

| Item | Location |
|------|----------|
| Facts Framework JSON | `data/facts-framework.json` |
| Facts Registry JSON | `data/facts-registry.json` |
| Constitution | `docs/FACTS_CONSTITUTION.md` |
| MC dashboard | `/mission-control/facts.html` |
| Generator script | `scripts/gen-facts-registry.py` |

---

## Fact Categories (6)

| ID | Category |
|----|----------|
| FACT-1000 | The Case |
| FACT-2000 | Historical Context |
| FACT-3000 | Constitutional Principles |
| FACT-4000 | Political Spending |
| FACT-5000 | Current Developments |
| FACT-6000 | Arkansas |

---

## Honest Status Summary

| Metric | Count |
|--------|-------|
| Facts cataloged | 13 |
| Verified (confirmed + strongly supported) | 8 |
| Under review | 3 |
| Awaiting evidence sources | 2 |
| Migrated from claims ledger | 3 |
| V1 target | ~200 |

---

## Confidence Levels

- **Confirmed** — primary or authoritative sources
- **Strongly Supported** — multiple reliable independent sources
- **Context Dependent** — accurate but needs explanation
- **Under Review** — pending verification

---

## Presentation Levels

L1 one-sentence → L2 plain language → L3 detailed discussion → L4 primary sources & citations.

---

## Integrations

| System | Link |
|--------|------|
| Evidence Registry | `EV-*` IDs |
| Claims Ledger | `fact_id` on 3 legacy claims |
| Knowledge Graph | `KG-*` related topics |
| Research Constitution | Source tiers govern verification |

---

## Recommended Next: Build #19 — Brand & Identity System

Logo, color, typography, voice, and messaging — before mass content production.

---

## Governing Principle

Facts are the foundation. Every article, chart, guide, and resource should trace back to verified facts supported by transparent evidence.
