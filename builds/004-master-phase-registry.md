# Build #4 — Master Phase Registry v1.0

**Status:** ✅ Complete  
**Version:** 1.8.0  
**Routes:** [/mission-control/phases.html](/mission-control/phases.html) · [/mission-control/](/mission-control/)

---

## Purpose

The Master Phase Registry is the project's governing roadmap.

Every feature, page, research task, visual, dataset, workflow, and deployment activity belongs to exactly one of **15 phases**.

Each phase has:

- A clear mission
- Measurable deliverables
- Completion criteria
- Defined dependencies

## Guiding Principle

> Does this help an ordinary citizen understand *Citizens United* more deeply and, if they choose, become equipped to educate others?

## What Shipped

- **`data/phase-registry.json`** — canonical 15-phase registry (machine-readable)
- **`docs/PHASE_REGISTRY.md`** — governing markdown document
- **`/mission-control/phases.html`** — full registry dashboard view
- Mission Control updated with 15 expandable phase cards (mission, deliverables, criteria, dependencies)
- BUILD_PLAN ↔ Registry mapping documented
- Honest per-phase completion percentages

## Phase Dependency Sequence

```
Foundation → IA → History → Case → Constitution → Impact → Data Viz
  → Debate → Reform → Civic Action → Community Leadership
  → Technical + Research (parallel) → QA → Launch
```

## Relationship to BUILD_PLAN

The 100-step BUILD_PLAN (12 operational phases) remains the execution tracker.

The 15-phase Registry is the educational roadmap. Both live in Mission Control.

## Next Recommended Build

**Build #5 — Historical Foundation (Hall 1 Depth)** — L2–L4 content for the path to *Citizens United*.

## Data Discipline

Update `phase-registry.json` and `mission-control.json` on every commit.
