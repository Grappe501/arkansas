# Build #22 — Database Schema & Entity Relationship Blueprint

**Version:** 1.26.0 · **Status:** ✅ Complete  
**Dashboard:** [/mission-control/database.html](/mission-control/database.html) · **Constitution:** [/docs/DATABASE_SCHEMA.md](/docs/DATABASE_SCHEMA.md)

---

## Purpose

Define the future database structure for Citizens United Facts — ready for forms, dashboards, coalition tracking, relational organizing, and Mission Control.

**One purpose:** Turn civic education activity into an organized, measurable Arkansas learning network.

---

## Primary Entities (15)

| # | Entity | Table | Storage |
|---|--------|-------|---------|
| 1 | Person | `people` | partial |
| 2 | Organization | `organizations` | partial |
| 3 | County | `counties` | live |
| 4 | Event | `events` | partial |
| 5 | Educational Resource | `educational_resources` | partial |
| 6 | Source | `sources` | partial |
| 7 | Fact | `facts` | partial |
| 8 | Signup | `signups` | partial |
| 9 | Referral | `referrals` | planned |
| 10 | Public Official | `public_officials` | planned |
| 11 | Educational Packet Share | `educational_packet_shares` | planned |
| 12 | Model Law Concept | `model_law_concepts` | stub |
| 13 | Ballot Initiative Concept | `ballot_initiative_concepts` | stub |
| 14 | Coalition Sign-On | `coalition_sign_ons` | partial |
| 15 | MC Build Record | `mc_build_records` | live |

---

## Join Tables (10)

`person_organizations` · `event_resources` · `resource_sources` · `fact_sources` · `resource_facts` · `county_public_officials` · `model_law_sources` · `ballot_initiative_sources` · `person_events` · `organization_events`

---

## Honest Status

| Metric | Value |
|--------|-------|
| Entities | 15 |
| Fields | ~180 |
| Join tables | 10 |
| Schema readiness | **35%** |
| Database deployed | **No** |
| v1 storage | Static JSON + Netlify Forms |

---

## Signup Types (8)

Education Leader · Contact Network · Research Volunteer · Event Host · Coalition Interest · Public Official Sharing · Model Law Contributor · Ballot Initiative Contributor

---

## Storage Migration Path

**v1:** JSON files · Netlify Forms · Git registries · localStorage  
**v2:** Postgres · Supabase · Neon · serverless API · admin dashboard

---

## Recommended Next: Build #23 — Wireframes

Every major screen wireframed before component specs and framework migration.
