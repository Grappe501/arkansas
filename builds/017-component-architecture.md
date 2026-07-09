# Build #17 — Component Architecture & Design System Inventory

**Version:** 1.21.0 · **Status:** ✅ Complete  
**Dashboard:** [/mission-control/components.html](/mission-control/components.html) · **Registry:** [/docs/COMPONENT_REGISTRY.md](/docs/COMPONENT_REGISTRY.md)

---

## Purpose

Define every reusable building block of the platform so pages are assembled from standardized components — not designed one-off.

The Component Registry catalogs **42 components** across **7 categories** (A–G): navigation, educational, data, civic participation, coalition, Mission Control, and trust.

---

## Deliverables

| Item | Location |
|------|----------|
| Master Component Registry JSON | `data/component-registry.json` |
| Registry documentation | `docs/COMPONENT_REGISTRY.md` |
| MC dashboard | `/mission-control/components.html` |
| Generator script | `scripts/gen-component-registry.py` |
| Brand identity scaffold | `data/brand-identity.json` |

---

## Honest Status Summary

| Status | Count |
|--------|-------|
| Live | 22 |
| Partial | 11 |
| Stub | 6 |
| Planned | 3 |
| Design-system linked | 12 |

---

## ACEI Brand Separation (Build #17)

To avoid the impression that the organization endorses the *Citizens United* decision:

| Layer | Name |
|-------|------|
| **Organization** | Arkansas Civic Education Initiative (**ACEI**) |
| **Platform** | *The Citizens United Education Platform* |
| **Coalition system** | ACEI Coalition System *(formerly ACUCOS)* |
| **Public site** | Citizens Facts *(unchanged URL)* |

*Citizens United* names the **subject of education**, not organizational identity.

---

## Component Principles

Every component should:

- Educate before persuading
- Reinforce credibility
- Be reusable across the platform
- Be fully responsive
- Meet accessibility standards
- Integrate with Mission Control
- Support future expansion without redesign

---

## Recommended Next: Build #18 — Brand & Identity System

Before UI design proceeds, define:

- Permanent project name
- Logo philosophy
- Color system
- Typography
- Voice
- Messaging

---

## Notes

Component inventory is **honest** — stub and planned components are documented, not hidden. The platform should feel like one cohesive educational institution as features are added over time.
