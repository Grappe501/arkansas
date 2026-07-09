# Master Requirement Identification System v1.0

**Build #7** · Citizens United Education Platform  
**Data:** `data/mrid-registry.json` · **Dashboard:** [/mission-control/mrid.html](/mission-control/mrid.html)

---

## Purpose

The Master Requirement ID (MRID) System establishes a **permanent identification framework** for every component of the platform.

Nothing is anonymous. Mission Control uses MRIDs as the platform's central nervous system.

---

## Governing Principle

> If it cannot be identified, it cannot be measured.  
> If it cannot be measured, it cannot be managed.  
> If it cannot be managed, it cannot reliably educate the public.

---

## ID Rules

Every MRID must be:

- Permanent · Unique · Human-readable · Searchable
- Stable across versions · Never reused after retirement · Traceable to parent domain

Format: `DOMAIN-NNN` (e.g. `CASE-021`, `REFORM-015`, `DASH-001`)

---

## Master Domain Codes (16)

| Code | Domain |
|------|--------|
| `GOV` | Governance |
| `NAV` | Navigation |
| `HOME` | Landing Experience |
| `HIST` | Historical Foundation |
| `CASE` | Citizens United Case |
| `CONST` | Constitutional Principles |
| `IMPACT` | Impact Analysis |
| `MONEY` | Money Flow |
| `DEBATE` | Perspectives |
| `REFORM` | Reform |
| `EDUCATE` | Community Education |
| `ACTION` | Civic Action |
| `DATA` | Research & Visualization |
| `SOURCE` | Source Library |
| `TECH` | Technical Platform |
| `DASH` | Mission Control |

---

## Requirement Lifecycle

1. Proposed → 2. Approved → 3. Planned → 4. Researching → 5. Designing → 6. Building → 7. Internal Review → 8. Testing → 9. Published → 10. Monitoring → 11. Revision Required → 12. Retired

---

## Traceability Matrix

Every MRID links to:

- Parent Phase · Parent Domain · Related Requirements · Dependencies
- Content Pages · Research Sources · Charts · Downloads
- Volunteer Resources · Build Numbers · Commits · Deployments · Testing Records

Every page, chart, or feature should display the MRIDs it satisfies.

---

## Relationship to Other Registries

| Registry | ID Type | Purpose |
|----------|---------|---------|
| Phase Registry | Phase 1–15 | Project roadmap |
| Site Architecture | URLs | Destinations |
| Content Inventory | `LAND-001`, etc. | Content assets |
| **MRID System** | `HOME-001`, etc. | **Permanent requirements & traceability** |

Content inventory items map to MRIDs via `content_id` ↔ `mrid` cross-reference in `mrid-registry.json`.

---

## Dependency Queries

Mission Control answers:

- What depends on `CASE-021`?
- What pages use `DATA-001`?
- Which builds modified `NAV-004`?

---

*Update `data/mrid-registry.json` on every build. Regenerate with `scripts/gen-mrid-registry.py` when content inventory changes.*
