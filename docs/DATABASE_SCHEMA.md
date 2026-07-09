# Database Schema & Entity Relationship Blueprint

**Data Architecture v1.0** · **Build #22**  
**Dashboard:** [/mission-control/database.html](/mission-control/database.html) · **Registry:** [/data/database-schema.json](/data/database-schema.json)

---

## Purpose

Define the future database structure for Citizens United Facts.

Version 1 may begin static-first, but the architecture must be ready for forms, dashboards, coalition tracking, relational organizing, public official sharing, research management, and Mission Control.

**One purpose:** Turn civic education activity into an organized, measurable Arkansas learning network.

---

## Core Data Philosophy

Every record should answer:

* Who is learning?
* What are they learning?
* Where are they located?
* What resources are they using?
* Who are they connected to?
* What organizations are participating?
* What counties are active?
* What public officials are being educated?
* What research supports the platform?

---

## Primary Entities (15)

1. **Person** — individual participant  
2. **Organization** — coalition partner  
3. **County** — Arkansas county hub  
4. **Event** — community education activity  
5. **Educational Resource** — teaching/learning material  
6. **Source** — evidence (EV-ID)  
7. **Fact** — verified factual claim (FACT-ID)  
8. **Signup** — form submission  
9. **Referral** — relational organizing  
10. **Public Official** — federal/state officials  
11. **Educational Packet Share** — materials shared with officials  
12. **Model Law Concept** — legislative ideas  
13. **Ballot Initiative Concept** — Arkansas petition ideas  
14. **Coalition Sign-On** — organization joining coalition  
15. **Mission Control Build Record** — build step tracking  

---

## Join Tables

Many-to-many relationships:

* `person_organizations`
* `event_resources`
* `resource_sources`
* `fact_sources`
* `resource_facts`
* `county_public_officials`
* `model_law_sources`
* `ballot_initiative_sources`
* `person_events`
* `organization_events`

---

## Mission Control Metrics

Total people · education leaders · coalition organizations · counties represented · counties with no activity · events hosted · resource downloads · referrals · public official shares · model law submissions · ballot initiative submissions · research completeness · content completion · deployment readiness

---

## Version 1 Storage Strategy

**Current (v0):** Static JSON files · Netlify Forms · Git-tracked registries · manual CSV exports

**Future:** Postgres · Supabase · Neon · serverless API · authenticated admin dashboard

The data model is designed now so migration later is clean.

---

## Privacy Principle

Collect only what is needed. Participant information protected, exportable, never exposed publicly without consent. Organization profiles distinguish public vs. private administrative fields.

---

## Data Architecture Principle

The database should map the growth of Arkansas civic education — not merely store contacts. Every record strengthens understanding of where education happens, where gaps remain, and how people and organizations connect across the state.

---

## Integrations

| System | Build | Role |
|--------|-------|------|
| Canonical Data Model | #15 | 10 objects — extended to 15 entities here |
| Relationship Registry | #15 | 20 relationship types |
| Facts Framework | #18 | Fact entity |
| Evidence Registry | #10 | Source entity |
| Repository Blueprint | #21 | Future `src/data/` migration target |
