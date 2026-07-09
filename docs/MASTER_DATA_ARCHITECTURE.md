# Citizens United Facts Master Data Architecture & Canonical Data Dictionary

**The Institutional Data Constitution v1.0**  
**Dashboard:** [/mission-control/data-architecture.html](/mission-control/data-architecture.html) · **Registry:** [/data/data-architecture.json](/data/data-architecture.json)

---

# Purpose

Information is the lifeblood of Citizens United Facts.

If Build #50 established **what** the institution is, Build #51 establishes **how the institution thinks about information**.

Everything in the platform—from a Supreme Court case to an Education Leader, from a county page to a research citation—should exist as structured, reusable data.

This document becomes the Canonical Data Dictionary for the entire institution.

Mission Control should treat this document as one of the platform's most important engineering references.

Extends Build #15 Canonical Data Model · Build #22 Database Schema · Build #48 Technical Architecture · Build #50 Build Bible.

---

# Data Philosophy

The platform should never ask:

> "Where else did we write this?"

Instead it should ask:

> "Where is the single source of truth?"

Every important piece of information should exist once and be referenced everywhere else.

No duplication. No conflicting versions. No disconnected data.

---

# The Twelve Canonical Data Domains

## Domain 100 — Identity

Stores: Users · Education Leaders · Researchers · Coalition contacts · Administrators · Volunteers · Public officials

Every person receives a permanent **Person ID**.

## Domain 200 — Organizations

Stores: Coalition organizations · Government agencies · Educational institutions · Libraries · Community groups · Universities · Media organizations

Every organization receives an **Organization ID**.

## Domain 300 — Geography

Stores: Arkansas · Regions · Counties · Cities · Legislative districts · Congressional districts · ZIP codes · Precinct references (future)

Every geographic object receives a **Geography ID**.

## Domain 400 — Knowledge

Stores: Articles · Lessons · Encyclopedia entries · FAQ entries · Definitions · Learning modules

Every knowledge asset receives a **Knowledge ID**.

## Domain 500 — Research

Stores: Research projects · Research notes · Source summaries · Literature reviews · Research tasks · Research status

Every research project receives a **Research ID**.

## Domain 600 — Evidence

Stores: Claims · Sources · Evidence ratings · Verification status · Citation relationships · Review history

Every evidence object receives an **Evidence ID**.

## Domain 700 — Law

Stores: Court cases · Statutes · Regulations · Constitutional provisions · Legislative proposals · Ballot initiative concepts

Each legal object receives a **Legal ID**.

## Domain 800 — Media

Stores: Videos · Audio · Images · Infographics · Animations · Presentations · PDFs

Each asset receives a **Media ID**.

## Domain 900 — Community

Stores: Community conversations · Events · Presentations · Academy sessions · Volunteer activities · Education Leader activities

Each activity receives an **Activity ID**.

## Domain 1000 — Mission Control

Stores: Projects · Builds · Tasks · Milestones · Progress · Reports · Institutional metrics

Each operational object receives an **Operations ID**.

## Domain 1100 — Analytics

Stores: Learning progress · Search activity · Downloads · Learning paths · Resource usage · Community engagement

Every analytic object receives an **Analytics ID**.

## Domain 1200 — Relationships

Stores every connection between domains.

Examples: Person teaches Lesson · Lesson cites Source · Source supports Claim · County hosts Event · Organization joins Coalition · Presentation uses Video

Everything becomes connected through relationship records.

---

# Canonical Object Model

Every major object should contain:

Unique ID · Title · Description · Created Date · Updated Date · Status · Owner · Review Date · Tags · Relationships · Version · Visibility

Everything shares a common structure.

---

# Metadata Standards

Every object should include:

Keywords · Reading level · Topic · Category · County relevance · Arkansas relevance · Educational level · Review cycle · Primary source availability

Mission Control depends on high-quality metadata.

---

# Relationship Standards

Relationships should never be hardcoded. They exist as structured data.

Institutional relationship verbs:

`SUPPORTED_BY` · `RELATED_TO` · `PRECEDES` · `FOLLOWS` · `LOCATED_IN` · `MENTORS` · `USES` · `PART_OF` · `CITED_BY` · `REFERRED_TO`

The Knowledge Graph is built from these relationships.

---

# Versioning

Every object maintains:

Current Version → Historical Versions → Revision Notes → Review History → Publication History

Institutional memory is preserved automatically.

---

# Publishing States

Every object moves through:

**Draft** → **Research** → **Review** → **Approved** → **Published** → **Scheduled Review**

Mission Control monitors these states across the institution.

---

# Search Index

Every object becomes searchable across: Title · Description · Keywords · Relationships · Topics · Arkansas relevance · Counties · Organizations · People · Cases · Sources

Everything should be discoverable.

---

# API Philosophy

Every domain exposes clean APIs. Future systems should never access raw data directly.

Examples: Identity API · Knowledge API · Research API · Evidence API · Coalition API · Mission Control API · Media API · Analytics API

Everything communicates through documented services.

---

# Database Philosophy

Normalize where appropriate. Denormalize only when performance requires it.

Protect referential integrity. Preserve historical records. Never lose institutional memory.

---

# Mission Control Data Dashboard

Mission Control should report: Objects created · Relationships created · Evidence records · Research records · Knowledge assets · Media assets · County coverage · Community activity · Overall institutional data health

The institution's knowledge becomes measurable.

---

# Future Expansion

The architecture should easily accommodate: Additional civic education topics · New Arkansas initiatives · Expanded research collections · Future AI capabilities · Additional states (if ever desired)

Without changing the core data model.

---

# Long-Term Vision

Every educational institution eventually develops an internal language. This Data Constitution defines that language.

Whether the platform contains 5,000 records or 5 million, every piece of information should fit into the same coherent structure.

Future developers should immediately understand how the institution thinks about knowledge.

---

# Governing Principle

The Citizens United Facts platform should never become a collection of disconnected databases.

It should function as one integrated knowledge institution where every person, place, idea, document, law, lesson, source, event, and educational resource exists within a shared data architecture.

When the data model is sound, every future feature becomes easier to build, easier to maintain, and more valuable to every Arkansan who comes to learn.
