# Implementation Package 6 of 50

# Citizens United Facts Version 1

## Master Design System, User Experience & Visual Language

**Status:** Implementation Package 6 of 50  
**Target Completion:** January 2027  
**Registry:** [/data/design-system-manifest.json](/data/design-system-manifest.json) · **Prior:** [IMP-05 Identity & Auth](/docs/IMPLEMENTATION_PACKAGE_05_IDENTITY_AUTH.md)

---

# Purpose

The visual experience of Citizens United Facts should immediately communicate:

Professionalism · Trust · Clarity · Warmth · Competence · Hope

Users should feel they are interacting with a **modern civic institution**—not a government website, a campaign website, or a news site.

Every page should reinforce public trust.

---

# Design Philosophy

Design should reduce cognitive effort. The interface should quietly guide users. Nothing should feel overwhelming.

Every screen should answer:

- Where am I?
- What can I do?
- What should I do next?

---

# Brand Personality

The platform should feel:

Trustworthy · Calm · Intelligent · Welcoming · Organized · Optimistic · Respectful · Evidence-driven · Arkansas-rooted

Technology should never feel cold.

---

# Visual Identity

The visual language emphasizes:

- Clean layouts
- Strong typography
- Comfortable spacing
- Simple navigation
- High readability
- Consistent interactions
- Minimal visual clutter

The design should age well over the next decade.

Existing tokens: [/css/design-tokens.css](/css/design-tokens.css) · Showcase: [/design-system/](/design-system/)

---

# Color Philosophy

Colors communicate meaning—not decoration.

| Role | Purpose |
|------|---------|
| Primary | Institution identity |
| Secondary | Navigation and supporting elements |
| Success | Completion, learning progress, healthy systems |
| Warning | Needs attention, risk indicators |
| Information | Educational notices, Mission Control insights |
| Neutral | Reading, backgrounds, cards, typography |

Domain accents (history, legal, data, civic, research) organize content without persuasion. See `design-system.json` color philosophy.

---

# Typography

Typography prioritizes readability.

| Level | Use |
|-------|-----|
| Institution Title | Site and institution name |
| Page Title | Primary page heading |
| Section Heading | Major sections |
| Subheading | Subsections |
| Body | Long-form reading |
| Caption | Supporting labels |
| Metadata | Dates, citations, status |

Fonts: **Source Serif 4** (reading) · **Source Sans 3** (UI) · **Consolas** (data)

Every page maintains consistent visual rhythm.

---

# Layout System

Responsive grid. Content width optimizes reading (`--ds-measure: 65ch`). Dashboards optimize decision-making.

Large screens present more information without crowding. Mobile users receive the same capabilities through simplified layouts.

Layout layers: Orientation → Summary → Main narrative → Visual explanation → Evidence → Related topics → Civic action

---

# Spacing Standards

Whitespace is intentional—it separates ideas, groups related information, improves scanning, and reduces fatigue.

Every screen should breathe. Tokens: `--ds-space-xs` through `--ds-space-2xl`.

---

# Card System

Most information appears within reusable cards:

Research · Volunteer · County · City · Organization · Course · Project · Mission Control

Consistency improves usability. Existing live components: `ds-case-card`, `ds-concept-card`, `ds-timeline-card`, and others in [/data/design-system.json](/data/design-system.json).

---

# Navigation

- **Primary navigation** remains stable (IMP-03)
- **Secondary navigation** reflects the current section
- **Breadcrumbs** show location
- **Search** remains available throughout

Users should never feel lost.

---

# Dashboard Philosophy

Dashboards answer questions—not display everything.

Every dashboard begins with:

1. Current status
2. Key indicators
3. Recommended actions
4. Recent activity
5. Upcoming work
6. Important alerts

Information is prioritized.

---

# Mission Control Design

Mission Control feels like an executive operations center.

Characteristics: large metrics · clear status indicators · interactive maps · trend charts · forecasts · task summaries · institution health · minimal distraction

Theme: NASA-inspired dark cockpit (`mission-control.css`). Rule: reinforce momentum without exaggerating progress.

---

# Maps

Maps are central navigation tools:

Arkansas overview · County health · City participation · Neighborhood coverage · Education Leader locations · Community conversations

Maps always provide drill-down capability.

---

# Charts

Preferred visualizations:

Progress bars · Trend lines · Heat maps · Completion rings · Growth charts · Timeline views · Network diagrams

Every visualization answers: What is measured? Why does it matter? Where did the data come from?

---

# Forms

Forms should:

- Ask one logical question at a time
- Auto-save when practical
- Provide helpful validation
- Support keyboard navigation
- Reduce unnecessary typing

Every form respects volunteer time.

---

# Accessibility

Accessibility is required—not optional.

| Standard | Requirement |
|----------|-------------|
| Keyboard navigation | Full operability without mouse |
| Color contrast | WCAG 2.1 AA minimum |
| Screen readers | Semantic HTML, ARIA where needed |
| Alternative text | All meaningful images |
| Scalable typography | User-adjustable sizing |
| Reduced motion | Respect `prefers-reduced-motion` |
| Focus states | Clear, visible focus indicators |

Accessibility benefits everyone.

---

# Mobile Experience

Mobile is not a reduced version—it is a complete experience.

Prioritize: Learning · Events · County information · Community conversations · Volunteer tasks · AI Assistant · Search

Mission Control remains available to authorized users.

Aligns with IMP-03 mobile nav priority.

---

# AI Experience

AI should feel like a trusted guide.

Every AI interaction should:

- State confidence
- Reference institutional knowledge
- Suggest next steps
- Offer related resources
- Encourage continued learning

The interface remains conversational.

---

# Personal Dashboard

Every user immediately sees:

Welcome · Learning progress · Upcoming events · County updates · Volunteer opportunities · Recent activity · Recommended next step · Personal AI

The dashboard becomes the user's civic home (`/dashboard`).

---

# Executive Dashboard

Executives see:

Mission Control · Institution Health · Critical alerts · County/city progress · Strategic goals · PMO status · Executive AI recommendations

Everything required to steward the institution (`/executive`).

---

# Animation

Animation is subtle—used only to:

- Guide attention
- Confirm actions
- Explain transitions
- Celebrate achievements

Never distract from content. Rule: motion never interferes with readability or accessibility.

---

# Design System Components

Reusable shared components:

| Category | Components |
|----------|------------|
| Actions | Buttons |
| Containers | Cards, Badges, Alerts, Modal dialogs, Knowledge panels |
| Data | Tables, Charts, Maps, Timelines, Progress indicators |
| Input | Search, Filters, Forms, Calendars |

Every component belongs to the shared design system—not isolated page styles.

---

# Design Documentation

Every component includes:

Purpose · Usage guidelines · Accessibility notes · Examples · States · Design tokens

Developers and designers work from the same reference. Governance: extend the system—do not create isolated styles.

---

# Mission Control Integration

Every screen exposes appropriate operational metrics to Mission Control.

UX is measurable: page completion · search success · learning completion · volunteer onboarding · navigation flow

Mission Control continuously improves the experience.

---

# Schema Artifacts

| Artifact | Path |
|----------|------|
| IMP-06 Constitution | This document |
| Design manifest | `/data/design-system-manifest.json` |
| Design language registry | `/data/design-system.json` |
| CSS tokens | `/css/design-tokens.css` |
| Component CSS | `/css/components.css` |
| MC theme | `/css/mission-control.css` |
| Showcase | `/design-system/` |

---

# Success Definition

Package #6 is complete when:

- Visual identity is fully defined
- Component library is specified
- Dashboard philosophy is documented
- Accessibility standards are established
- Responsive behavior is defined
- Every future screen follows one coherent design language

---

# Deliverables Produced

- Visual Design Language
- UX Philosophy
- Dashboard Standards
- Component System
- Accessibility Standards
- Mobile Standards
- Navigation Standards
- Mission Control Design Rules
- AI Interaction Standards
- Responsive Layout Rules

This becomes the visual foundation for the entire Citizens United Facts platform.

---

# Next Package

**Implementation Package 7 of 50 — Master Mission Control Architecture & Executive Command Center**

Every Mission Control dashboard, executive metric, health indicator, statewide map, forecasting engine, operational report, and decision-support tool for real-time institutional leadership.

---

# Governing Principle

People decide whether to trust an institution within moments.

Thoughtful design, clear navigation, accessible interfaces, and a calm visual language communicate that Citizens United Facts is organized, competent, welcoming, and worthy of the public's confidence before a single word is read.
