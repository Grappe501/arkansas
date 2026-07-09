# Canonical Data Constitution v1.0

**Build #15** · **Dashboard:** [/mission-control/data-model.html](/mission-control/data-model.html)

---

## Purpose

Everything in the platform should be **connected**. This document defines the canonical data architecture — one interconnected civic education ecosystem, not separate systems.

**Philosophy:** Everything is connected.

---

## Canonical Objects (10)

| Object | ID Prefix | Schema / Registry |
|--------|-----------|-------------------|
| **Person** | PERSON | `participant-profile-schema.json` |
| **Organization** | ORG | `organization-profile-schema.json` |
| **County** | COUNTY | `county-coalition-index.json` |
| **Educational Resource** | RES | `content-inventory.json` |
| **Event** | EVT | `coalition-events.json` |
| **Research Object** | EV | `evidence-registry.json` |
| **Public Official** | OFF | contact-legislators scaffold |
| **Model Law** | MLAW | draft-laws workspace |
| **Ballot Initiative Concept** | BAL | ballot-lab workspace |
| **Topic** | KG | `knowledge-graph.json` |

---

## Relationship Engine

Example chain: Person → County → Organization → Hosted Event → Downloaded Resource → Shared → Model Law → Presented to Official.

**20 relationship types** in `data/relationship-registry.json`: Member Of, Hosted, Downloaded, Shared, Researches, Presented, and more.

---

## Geographic Intelligence

```
Arkansas → County → City → Community → Organization → Person
```

---

## Mission Control

Relationship health metrics: people connected, organizations connected, counties active, events hosted, resources shared, research objects, model laws, packets shared.

---

## Implementation Pivot (Builds #16–#20)

| Build | Focus |
|-------|-------|
| **#16** | Complete page inventory |
| **#17** | Component inventory |
| **#18** | Database schema & entity relationships |
| **#19** | UX wireframes |
| **#20** | GitHub + Netlify deployment blueprint |

---

## Governing Principle

The platform becomes more valuable because it has **stronger relationships**, not more pages.

**Blueprint:** `data/canonical-data-model.json`
