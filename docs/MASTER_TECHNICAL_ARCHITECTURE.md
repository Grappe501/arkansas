# Citizens United Facts Master Technical Architecture & Deployment Blueprint

**Production Engineering Constitution v1.0**  
**Dashboard:** [/mission-control/technical-architecture.html](/mission-control/technical-architecture.html) · **Registry:** [/data/technical-architecture.json](/data/technical-architecture.json)

---

# Purpose

This document defines **how the institution will be built**, not merely how it will look.

The objective is a platform that is fast, secure, searchable, maintainable, accessible, scalable, and transparent.

Every technical decision should support the educational mission.

Extends Build #20 Platform Blueprint (`/data/platform-architecture.json`) with production engineering and deployment constitution.

---

# Technical Philosophy

Build like a permanent institution — not a campaign or marketing site.

Think: digital museum · research library · educational university · archive · civic operating system — all under one roof.

---

# Core Technology Stack

| Layer | Target | Current (v1.52) |
|-------|--------|-----------------|
| Frontend | Next.js, React, TypeScript | Static HTML/CSS/JS |
| Styling | Tailwind + design tokens | Build #9 design system, custom CSS |
| Hosting | GitHub → Netlify | **Live** |
| Database | PostgreSQL (Neon) | Static JSON registries |
| ORM | Prisma | None |

---

# Authentication

Email and Google OAuth for admin. Educational content remains public.

---

# Search Architecture

Global index: articles, lessons, timeline, cases, people, organizations, laws, videos, infographics, sources, claims, encyclopedia, Arkansas pages.

---

# CMS Philosophy

Mission Control is the publishing system — workflow, review, approval, publishing, revision, version history. No traditional CMS.

---

# AI Layer

AI draws from Evidence Ledger → Knowledge Graph → Research Library → Claims Registry → Encyclopedia → Curriculum → Mission Control. Never invents knowledge.

---

# Deployment Workflow

Developer → GitHub → Pull Request → Preview Deploy → Testing → Approval → Production → Mission Control updated.

---

# Environment Strategy

Development → Testing → Preview → Production. No dev data in production.

---

# Performance & Accessibility

Homepage and educational pages < 2 seconds. WCAG AA minimum. Keyboard, screen reader, reduced motion, high contrast.

---

# Analytics Philosophy

Measure learning, understanding, participation — not clicks, advertising, or engagement hacks.

---

# Governing Principle

Technology should be nearly invisible to the public — fast, trustworthy, intuitive. Behind the scenes: engineered with the same care, documentation, scalability, and permanence as the knowledge it preserves.

Build for twenty years, not two.
