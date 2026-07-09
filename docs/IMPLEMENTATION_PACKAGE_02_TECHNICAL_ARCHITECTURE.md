# Implementation Package 2 of 50

# Citizens United Facts Version 1

## Master Technical Architecture & Repository Blueprint

**Status:** Implementation Package 2 of 50  
**Target Completion:** January 2027  
**Registry:** [/data/cursor-implementation-package.json](/data/cursor-implementation-package.json) · **Prior:** [IMP-01 Technical Constitution](/docs/IMPLEMENTATION_PACKAGE_01_TECHNICAL_CONSTITUTION.md)

---

# Purpose

This document defines the complete technical architecture for Citizens United Facts.

Every developer, Cursor session, AI assistant, and future contributor should build from this blueprint.

There should never be uncertainty about:

- Where code belongs.
- Where data belongs.
- Where documentation belongs.
- Where AI belongs.
- Where Mission Control belongs.

This repository becomes the permanent home of the institution.

---

# Architectural Philosophy

One Institution → One Repository → Many Modules → Shared Foundation

The system should feel like one application, even though it contains dozens of interconnected systems.

---

# Technology Stack

Modern, production-ready technologies supporting long-term maintainability.

| Layer | Target |
|-------|--------|
| **Frontend** | React, Next.js, TypeScript |
| **Backend** | Node.js, Next.js Server Actions / API Routes |
| **Database** | PostgreSQL (Neon) |
| **Authentication** | Secure role-based authentication |
| **Storage** | Object storage for media and documents |
| **Search** | Full-text search with structured indexing |
| **AI** | OpenAI integration with LocalBrains |
| **Deployment** | Production cloud deployment with automated CI/CD |

Exact providers may evolve; architectural principles remain constant.

Aligns with [/data/technical-architecture.json](/data/technical-architecture.json) and [/data/repository-blueprint.json](/data/repository-blueprint.json).

---

# Repository Structure

```
citizens-united-facts/
    app/
    components/
    features/
    lib/
    ai/
    mission-control/
    database/
    docs/
    public/
    content/
    data/
    scripts/
    tests/
    infrastructure/
    config/
```

Organized by **responsibility**, not technology.

---

# Layer Responsibilities

| Layer | Contains |
|-------|----------|
| **app/** | Public pages, dashboards, volunteer/executive workspace, MC, auth, learning, research portal — every route begins here |
| **components/** | Reusable UI: buttons, cards, maps, charts, tables, nav, forms, dashboards, timelines, evidence viewers |
| **features/** | Major systems: Research Library, Evidence Ledger, Claims Registry, MC, Academy, Volunteer Network, Coalition, County/City/Neighborhood OS, Action Network |
| **ai/** | LocalBrains, prompts, institutional memory, orchestration, retrieval, agent registry, conversation history, safety rules |
| **mission-control/** | Executive dashboards, metrics, progress, Digital Twin, forecasting, institutional health — never buried in unrelated modules |
| **database/** | Schema, migrations, views, reporting, reference/seed data, utilities |
| **docs/** | Operating manuals, architecture, governance, developer/volunteer guides, constitution, implementation packages, research methodology |
| **public/** | Images, videos, PDFs, infographics, downloads, presentation materials |
| **content/** | Articles, lessons, research papers, case summaries, FAQs, glossary, timelines — separate from application code |
| **data/** | Counties, cities, organizations, research/education metadata, configuration, reference datasets |
| **scripts/** | Imports, reporting, testing, maintenance, AI utilities, build tools, deployment helpers |
| **tests/** | Unit, integration, accessibility, performance, MC validation, launch certification tests |
| **infrastructure/** | Deployment, monitoring, logging, backups, security policies, environment templates |
| **config/** | Institution settings, feature flags, permissions, environment, AI config, MC settings |

---

# Module Standards

Every feature module should contain:

Purpose · Routes · Components · Services · Database models · AI integration · Mission Control metrics · Documentation · Tests.

Every module looks familiar.

---

# Feature Isolation

No feature directly manipulates another feature. Communication through:

- Shared services
- Events
- APIs
- Institutional contracts

Loose coupling improves maintainability.

---

# Shared Design System

One design language · One typography system · One icon system · One spacing system · One accessibility standard.

Users should never feel they are moving between separate applications.

---

# Mission Control Integration

Every feature must expose: Health · Usage · Completion · Errors · Growth · Dependencies · Executive metrics.

Mission Control observes the entire institution.

---

# AI Integration Rule

Every feature asks: Can AI assist, summarize, search, teach, organize, or reduce volunteer workload?

If yes, AI hooks belong in the architecture.

---

# Repository Governance

No undocumented folders · No duplicate systems · No abandoned modules · No experimental production code.

Everything has an owner and a purpose.

---

# Success Definition

Package #2 is complete when the institution has:

- A defined repository
- A defined architecture
- A defined module structure
- A defined development pattern
- A defined documentation structure
- A defined AI architecture
- A defined Mission Control architecture

Everything has a permanent home.

---

# Deliverables Produced

- Master Repository Structure
- Folder Architecture
- Module Standards
- Technology Stack
- Documentation Standards
- AI Architecture Placement
- Mission Control Placement
- Database Organization
- Testing Organization
- Infrastructure Organization

This is the technical map of the entire Citizens United Facts codebase.

---

# Governing Principle

A great institution is not built by writing code first.

It is built by designing a structure where every future line of code already knows exactly where it belongs.

---

# Next Package

**Implementation Package 3 of 50 — Master Route Map & Complete Application Navigation**

Every page, URL, dashboard, administrative screen, public-facing experience, and user journey — before a single page is coded.
