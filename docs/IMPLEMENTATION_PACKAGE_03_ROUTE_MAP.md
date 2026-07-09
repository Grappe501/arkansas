# Implementation Package 3 of 50

# Citizens United Facts Version 1

## Master Route Map & Complete Application Navigation

**Status:** Implementation Package 3 of 50  
**Target Completion:** January 2027  
**Registry:** [/data/route-manifest.json](/data/route-manifest.json) · **Prior:** [IMP-02 Technical Architecture](/docs/IMPLEMENTATION_PACKAGE_02_TECHNICAL_ARCHITECTURE.md)

---

# Purpose

Before writing application code, every page and every user journey must be defined.

Nothing should be added randomly. Every page should support the institution's mission. Every route should answer a user question.

This document establishes the complete navigation architecture for Citizens United Facts.

---

# Navigation Philosophy

Users do not think in departments. Users arrive with questions.

The navigation should be organized around those questions:

- I want to understand…
- I want to learn…
- I want to volunteer…
- I want to teach…
- I want to find my county…
- I want to see the evidence…
- I want to ask a question…

Navigation should reduce confusion.

---

# Primary Public Navigation

Home · About · Learn · Research · Evidence · Academy · Counties · Cities · Action Center · Coalition · News & Updates · Get Involved · Donate (future) · Login · Search

These items remain visible throughout the site.

---

# Public Route Map

| Route | Path | Purpose |
|-------|------|---------|
| Home | `/` | Introduce the institution; clear next steps |
| About | `/about` | Mission, vision, history, leadership, founding charter, volunteer model |
| Learn | `/learn` | Learning paths, beginner guides, courses, videos, glossary, FAQ |
| Research | `/research` | Research library, white papers, campaign finance, constitutional, Arkansas research |
| Evidence | `/evidence` | Evidence Ledger, Claims Registry, primary sources, court opinions, citation explorer |
| Academy | `/academy` | Course catalog, certificates, leadership pathways, Education Leaders, training |
| Counties | `/counties` | Interactive map, directory, dashboards, Education Leaders, resources |
| County | `/counties/{county-slug}` | Dashboard, leadership, calendar, resources, conversations, progress, MC metrics |
| Cities | `/cities` | Directory, map, educational coverage, leadership |
| City | `/cities/{city-slug}` | Dashboard, events, leadership, neighborhoods, resources |
| Neighborhood | `/neighborhoods/{slug}` | Profile, conversation calendar, resources, Education Leader, volunteer opportunities |
| Action Center | `/action` | Legislative resources, government process, public meetings, how-to guides |
| Coalition | `/coalition` | Partners, join, shared resources, events, organization directory |
| News | `/news` | Announcements, research releases, community stories, institution updates |
| Events | `/events` | Statewide, county, academy, community, volunteer calendars |
| Media | `/media` | Videos, podcasts, downloads, presentations, infographics |
| FAQ | `/faq` | Institution, Citizens United, campaign finance, academy, volunteer FAQs |
| Contact | `/contact` | General, research requests, corrections, volunteer, speaking |

---

# Account & Personal Routes

| Route | Path |
|-------|------|
| Login | `/login` |
| Register | `/register` |
| Forgot Password | `/forgot-password` |
| Profile | `/profile` |
| Settings | `/settings` |
| Notifications | `/notifications` |
| Messages | `/messages` |
| Personal Dashboard | `/dashboard` — learning, volunteer work, projects, calendar, AI, county updates, progress |

---

# Workspace Routes

| Workspace | Path | Contains |
|-----------|------|----------|
| Volunteer | `/volunteer` | Assignments, training, resources, mentorship, leadership pathway |
| Education Leader | `/leader` | Presentations, conversations, county/city dashboards, resources, coordination |
| Coalition | `/organization` | Org dashboard, events, members, shared resources, reports, calendar |
| Executive | `/executive` | Mission Control, PMO, Digital Twin, health, forecasts, reports, AI insights |

---

# Mission Control & Admin

| Route | Path |
|-------|------|
| Mission Control | `/mission-control` — executive dashboard, health, research, counties, cities, neighborhoods, volunteers, technology, academy, coalition, strategic goals |
| Admin | `/admin` — configuration, users, permissions, content, research, media, reports, system health, AI management |
| AI Workspace | `/ai` — personal AI, department AI, LocalBrains, prompt library, knowledge, history |
| Search | `/search` — unified search across research, articles, lessons, counties, cities, organizations, projects, events, documents, people |

---

# API Structure

`/api/` — Authentication · Research · Mission Control · Academy · Volunteer · Organizations · AI · Knowledge · Reports · Search · Calendar · Messaging

Every module receives its own API namespace.

---

# Route Standards

Every page should include: Purpose · Breadcrumbs · Search · Related resources · AI assistance · Feedback option · Mission Control metrics (internal).

---

# Mobile Navigation Priority

Search · Learn · County · Events · Dashboard · AI Assistant

Navigation must remain usable on phones first.

---

# Success Definition

Package #3 is complete when every public page, dashboard, workspace, administrative area, and user journey has a defined destination. Cursor should never need to invent routes during development.

---

# Governing Principle

Navigation is the visible expression of institutional thinking.

If users always know where they are, where they can go, and what they should do next, the institution becomes approachable, trustworthy, and easy to use.

---

# Next Package

**Implementation Package 4 of 50 — Master Database Schema & Canonical Data Model**

Every major entity, table, relationship, identifier, and data contract — a single coherent source of truth.
