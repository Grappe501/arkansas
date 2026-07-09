# Citizens United Education Website — Master Build Plan

100 steps across **13 operational phases**, governed by the **15-phase [Master Phase Registry](/mission-control/phases.html)**.

Status: ✅ Done · 🟡 Partial · ⬜ Not started

**Current version:** 1.33.0 · **Research Observatory:** [/mission-control/research-observatory.html](/mission-control/research-observatory.html) · **OS:** [Mission Control](/mission-control/)  
**Build #29:** ✅ Research Observatory · **Build #28:** ✅ Education Academy · **Build #27:** ✅ Content Factory  
**Organization:** Arkansas Civic Education Initiative (ACEI) · *Citizens United* = subject, not identity  
**Public map:** [/explore/](/explore/) · **Live site:** [arkansas-facts.netlify.app](https://arkansas-facts.netlify.app/)

> **Arkansas pilot (v1):** All civic action frameworks scoped to Arkansas first — modular for future states.

---

## Master Phase Registry (15 phases)

| # | Phase | Registry doc |
|---|-------|--------------|
| 1 | Foundation & Governance | [Phase Registry](/mission-control/phases.html) |
| 2 | Information Architecture | |
| 3 | Historical Foundation | |
| 4 | The Case | |
| 5 | Constitutional Principles | |
| 6 | Impact Analysis | |
| 7 | Data & Visualization | |
| 8 | Debate & Perspectives | |
| 9 | Reform & Current Developments → **Solutions & Policy Options** | |
| 10 | Civic Action Platform | |
| 11 | Community Leadership | |
| 12 | Technical Platform | |
| 13 | Research Library | |
| 14 | Quality Assurance | |
| 15 | Launch & Growth | |

---

## Phase 0 — Mission Control OS

| Component | Status | Route |
|-----------|--------|-------|
| Executive dashboard | ✅ | `/mission-control/` |
| Phase cards (expandable) | ✅ | |
| Build DNA pages | ✅ | `/mission-control/build.html?b=N` |
| Living build map | ✅ | |
| Public readiness tracker | ✅ | |
| Dev console | ✅ | `?dev=1` |
| Data source | ✅ | `data/mission-control.json` |

> **Update rule:** Every build updates `mission-control.json`.

---

## Phase 1 — Project Constitution (1–7)

| # | Step | Status |
|---|------|--------|
| 1 | Site mission: deep public understanding of *Citizens United* | ✅ Build #1 |
| 2 | Conversion goal: local education leaders | ✅ |
| 3 | Reader journey: Understand → Trust → Care → Teach → Lead | ✅ |
| 4 | Site promise: plain language + deep research underneath | ✅ |
| 5 | Editorial standard: accurate, sourced, non-hysterical | ✅ |
| 6 | Primary audience groups | ✅ |
| 7 | Success metric: education lead signups + civic participation | 🟡 Expanded |

---

## Phase 2 — Information Architecture (8–19)

| # | Step | Status | Route |
|---|------|--------|-------|
| 8 | Main landing page | ✅ | `/` |
| 9 | Before Citizens United | ✅ | `/halls/story-before.html` |
| 10 | The Case Itself | ✅ | `/halls/the-case.html` |
| 11 | What the Court Decided | ✅ | `/halls/what-court-decided.html` |
| 12 | After 2010 | ✅ | `/halls/after-2010.html` |
| 13 | Follow the Money | ✅ | `/halls/money-map.html` |
| 14 | Arguments and Debate | ✅ | `/halls/debate.html` |
| 15 | **Solutions & Policy Options** | 🟡 | `/solutions/` |
| 16 | Montana and Hawaii | ✅ | `/halls/montana-hawaii.html` |
| 17 | Teach This Locally | ✅ | `/educate/` |
| 18 | Source Library | ✅ | `/library/` |
| 19 | Signup form page | ✅ | `/educate/` |

---

## Phase 3 — Depth Model (20–27)

| # | Step | Status |
|---|------|--------|
| 20–24 | Four depth levels L1–L4 | 🟡 Hall 7 complete |
| 25 | Reusable depth templates | ✅ |
| 26 | "Go deeper" navigation | ✅ |
| 27 | "Return to simple" via L1 toggle | ✅ |

---

## Phase 4 — Content System (28–37)

| # | Step | Status |
|---|------|--------|
| 28–37 | Inventories, MT/HI files, citation standard, claims ledger | ✅ |

---

## Phase 5 — Data and Visual Layer (38–44)

| # | Step | Status |
|---|------|--------|
| 38 | Define core charts | ✅ |
| 39–42 | Static charts, notes, source links | ⬜ v1.5.0 |
| 43 | Interactive dashboard plan | ✅ |
| 44 | Chart plain-language explanations | ⬜ |

---

## Phase 6 — Website Experience (45–53)

| # | Step | Status |
|---|------|--------|
| 45–53 | Landing, pathway cards, previews, CTAs | ✅ |

---

## Phase 7 — Civic Action Layer (54–65) ★ NEW

*Transforms knowledge website → civic organizing platform.*

| # | Step | Status | Notes |
|---|------|--------|-------|
| 54 | Persistent floating **Action Hub** on every page | 🟡 | v1.4.0 expandable hub |
| 55 | "Become an Education Leader" quick signup | ✅ | Hub + `/educate/` |
| 56 | "Join the Contact Network" signup | 🟡 | `/action/join-network.html` |
| 57 | "Share With Friends & Family" relational organizing | 🟡 | `/action/share.html` |
| 58 | Referral tracking | 🟡 | localStorage stub; backend later |
| 59 | "Draft Better Laws" collaborative workspace | 🟡 | Stub page |
| 60 | "Ballot Initiative Lab" | 🟡 | Stub page |
| 61 | Model Legislation Library | 🟡 | Linked from draft-laws |
| 62 | "Community Ideas" workspace | 🟡 | `/action/ideas.html` form |
| 63 | Volunteer directory + interest matching | ⬜ | Needs backend |
| 64 | Leadership pathway (learner → education lead) | 🟡 | `docs/CIVIC_ACTION.md` |
| 65 | Admin dashboard (signups, referrals, proposals) | ⬜ | Netlify Forms + future backend |

**Participant profile schema:** `data/participant-profile-schema.json`  
**Architecture doc:** `docs/CIVIC_ACTION.md`

### Action Hub menu
Become a Leader · Join the Network · Share · Invite Friends · Draft a Law · Build Ballot Initiative · Contact Legislators · Ask a Question · Give Feedback

---

## Phase 8 — Education Funnel & Forms (66–73)

| # | Step | Status |
|---|------|--------|
| 66 | Volunteer + leadership role definitions | ✅ |
| 67 | Teach This Locally page | ✅ |
| 68 | Starter toolkit request | ✅ |
| 69 | Core signup form fields | ✅ |
| 70 | Role checkboxes + experience level | ✅ |
| 71 | Privacy notice + honeypot spam protection | ✅ |
| 72 | Confirmation page | ✅ |
| 73 | Notification + export workflow | 🟡 Netlify dashboard |

---

## Phase 9 — Technical Stack (74–82)

| # | Step | Status |
|---|------|--------|
| 74–82 | Static-first, GitHub, Netlify, forms, env vars, previews | 🟡 |

---

## Phase 10 — GitHub Workflow (83–91)

| # | Step | Status |
|---|------|--------|
| 83–91 | Branches, PRs, issue templates, guides, README | 🟡 |

---

## Phase 11 — Netlify Deployment (92–97)

| # | Step | Status |
|---|------|--------|
| 92–97 | CD, build settings, previews, form testing | 🟡 |

---

## Phase 12 — Launch & Expansion (98–100)

| # | Step | Status |
|---|------|--------|
| 98 | Test production: deploy, forms, Action Hub, share | 🟡 |
| 99 | Participant profile backend decision (Supabase/etc.) | ⬜ |
| 100 | Launch + continuous content + civic action expansion | 🟡 |

---

## Phase 13 — Coalition Building & Public Outreach (Build #13) ★ NEW

*First-class Coalition & Outreach Layer — alongside Education, Research, and Civic Action.*

| # | Step | Status | Route |
|---|------|--------|-------|
| C1 | Coalition ecosystem blueprint | ✅ | `data/coalition-ecosystem.json` |
| C2 | Organization profile schema | ✅ | `data/organization-profile-schema.json` |
| C3 | Coalition directory (Arkansas) | 🟡 | `data/coalition-directory.json` (0 orgs) |
| C4 | Organization join form (Netlify) | ✅ | `/coalition/join.html` |
| C5 | Five membership levels | ✅ | Supporter → Strategic Partner |
| C6 | Organization Resource Center | 🟡 | `/coalition/resources.html` |
| C7 | Community Event Calendar + submit | 🟡 | `/coalition/events.html` |
| C8 | Coalition Growth Dashboard | ✅ | `/mission-control/coalition.html` |
| C9 | Arkansas coalition map (county table) | 🟡 | MC dashboard; interactive map ⬜ |
| C10 | Social Media Command Center scaffold | 🟡 | Metrics at 0; channels planned |
| C11 | Homepage three-path entry points | ✅ | Learn · Help · Partner |
| C12 | Platform layers in site architecture | ✅ | `platform_layers` in IA |
| C13 | Coalition principles doc | ✅ | `docs/COALITION_OUTREACH.md` |

**Governing principle:** Success is measured by trusted Arkansas organizations that help educate their communities — not only individual learners.

**Architecture doc:** `docs/COALITION_OUTREACH.md` · **Dashboard:** `/mission-control/coalition.html`

### Coalition membership levels

| Level | Role |
|-------|------|
| Supporter | Supports the educational mission |
| Educational Partner | Shares platform resources |
| Community Partner | Hosts educational events |
| Research Partner | Contributes research or expertise |
| Strategic Partner | Statewide educational collaboration |

### Homepage entry paths

| Path | Pillar | Route |
|------|--------|-------|
| I'm Here to Learn | Education | `/explore/` |
| I Want to Help | Leadership | `/educate/` |
| My Organization Wants to Partner | Coalition Building | `/coalition/` |

---

## Platform Progression

```
Learn          →  Participate     →  Organize         →  Build Solutions    →  Coalition
(Halls)           (Sign up, network)  (Share, invite)     (Draft laws, ballot)   (Organizations)
```

## Progress Summary

| Phase | Focus | Status |
|-------|-------|--------|
| 1–6 | Knowledge system | Mostly ✅ |
| **7** | **Civic Action Layer** | **🟡 Scaffolded** |
| 8–12 | Forms, tech, launch | 🟡 |
| **13** | **Coalition & Outreach** | **✅ v1.17.0** |
| **14** | **ACUCOS** | **✅ v1.18.0** |
| **15** | **Canonical Data Model** | **✅ v1.19.0** |
| **16** | **Route Inventory** | **✅ v1.20.0** |
| **17** | **Component Registry** | **✅ v1.21.0** |
| **18** | **Facts Framework** | **✅ v1.22.0** |
| **19** | **Knowledge Atlas** | **✅ v1.23.0** |
| **20** | **Platform Blueprint** | **✅ v1.24.0** |
| **21** | **Repository Structure** | **✅ v1.25.0** |
| **22** | **Database Schema** | **✅ v1.26.0** |
| **23** | **Wireframes** | **✅ v1.27.0** |
| **24** | **Contact Intelligence** | **✅ v1.28.0** |
| **25** | **Mission Control 2.0** | **✅ v1.29.0** |
| **26** | **AI Knowledge Engine** | **✅ v1.30.0** |
| **27** | **Content Production Factory** | **✅ v1.31.0** |
| **28** | **Education Academy** | **✅ v1.32.0** |
| **29** | **Research Observatory** | **✅ v1.33.0** |

**Next:** Build #30 — Component specifications with props/states.

---

## Phase 29 — Research Observatory (Build #29) ★ NEW

*Living Research & Legislative Intelligence — early warning system.*

| # | Step | Status | Route |
|---|------|--------|-------|
| R1 | Observatory Blueprint v1.0 | ✅ | `data/research-observatory.json` |
| R2 | 6 research divisions | ✅ | SCOTUS through Campaign Spending |
| R3 | 9-stage research workflow | ✅ | Identified → Published |
| R4 | 3 priority levels | ✅ | Educational accuracy through long-term |
| R5 | Legislative tracking page structure | ✅ | 7 sections |
| R6 | Research gap tracker | ✅ | Evidence registry + platform gaps |
| R7 | MC observatory dashboard | ✅ | `/mission-control/research-observatory.html` |

---

## Phase 28 — Education Academy (Build #28) ★ NEW

*Arkansas Education Leader Development — highest-impact program.*

| # | Step | Status | Route |
|---|------|--------|-------|
| A1 | Academy Blueprint v1.0 | ✅ | `data/education-academy.json` |
| A2 | 4 learning stages | ✅ | Learn → Lead |
| A3 | 8 curriculum modules | ✅ | Mapped to knowledge worlds |
| A4 | Certification + presentation toolkit | ✅ | Educational only disclaimer |
| A5 | 7 audience toolkits | ✅ | 1 partial (community conversation) |
| A6 | Leadership dashboard metrics | ✅ | 7 metrics defined |
| A7 | MC education academy dashboard | ✅ | `/mission-control/education-academy.html` |

---

## Phase 27 — Content Production Factory (Build #27) ★ NEW

*Editorial Operating System — one institution, one voice.*

| # | Step | Status | Route |
|---|------|--------|-------|
| F1 | Content Factory Blueprint v1.0 | ✅ | `data/content-production-factory.json` |
| F2 | 7 content type templates | ✅ | Educational through Arkansas guides |
| F3 | 10-section article structure | ✅ | Standard reader pattern |
| F4 | 11-stage editorial workflow | ✅ | Aligned to content inventory |
| F5 | L1–L4 reading levels | ✅ | Mapped to facts framework |
| F6 | Quality gates + evergreen review | ✅ | 6 gates, 5 review policies |
| F7 | MC content factory dashboard | ✅ | `/mission-control/content-factory.html` |

---

## Phase 26 — AI Knowledge Engine (Build #26) ★ NEW

*Educational Intelligence Architecture — Arkansas Civic Librarian.*

| # | Step | Status | Route |
|---|------|--------|-------|
| A1 | AI Knowledge Engine Blueprint v1.0 | ✅ | `data/ai-knowledge-engine.json` |
| A2 | Arkansas Civic Librarian persona | ✅ | 7 traits documented |
| A3 | 5 learning modes | ✅ | Quick Answer → Primary Source Explorer |
| A4 | Evidence-first response schema | ✅ | 6 required fields |
| A5 | 9 example questions + fact types | ✅ | Fact / legal / proposal distinction |
| A6 | 10 capabilities + guardrails | ✅ | Research, event, coalition, MC assistants |
| A7 | MC AI dashboard | ✅ | `/mission-control/ai-knowledge.html` |

---

## Phase 25 — Mission Control 2.0 (Build #25) ★ NEW

*Executive Operating System — if it matters, it is visible.*

| # | Step | Status | Route |
|---|------|--------|-------|
| E1 | MC2 Executive Blueprint v1.0 | ✅ | `data/mc2-executive.json` |
| E2 | 9 specialized workspaces | ✅ | Mapped to existing dashboards |
| E3 | 5 executive dashboard panels | ✅ | Including Arkansas readiness map |
| E4 | 9 project health indicators | ✅ | Honest scores from live registries |
| E5 | 8 smart alerts defined | ✅ | 0 automated yet |
| E6 | Build timeline schema | ✅ | Pulls from mission-control.json |
| E7 | MC2 executive dashboard | ✅ | `/mission-control/executive.html` |

---

## Phase 24 — Contact Intelligence (Build #24) ★ NEW

*Arkansas Community Intelligence System — educational relationship network architecture.*

| # | Step | Status | Route |
|---|------|--------|-------|
| C1 | Contact Intelligence Blueprint v1.0 | ✅ | `data/contact-intelligence.json` |
| C2 | 14 intelligence modules | ✅ | Profile, interests, skills, county, etc. |
| C3 | Interest & skills taxonomies | ✅ | 12 interests, 14 skills |
| C4 | Privacy & trust principles | ✅ | 5 principles documented |
| C5 | MC relationship metrics | ✅ | 11 metrics defined |
| C6 | Integration map | ✅ | 10 platform systems |
| C7 | MC contact intelligence dashboard | ✅ | `/mission-control/contact-intelligence.html` |

---

## Phase 23 — Wireframes (Build #23) ★ NEW

*25 major screens with section-level architecture before visual design.*

| # | Step | Status | Route |
|---|------|--------|-------|
| W1 | Wireframe Blueprint v1.0 | ✅ | `data/wireframe-blueprint.json` |
| W2 | 25 screens defined | ✅ | Sections per screen |
| W3 | Four outcome mapping | ✅ | understand · evidence · participate · MC |
| W4 | Route + implementation status | ✅ | Honest vs route registry |
| W5 | Global component mapping | ✅ | Action Hub, Compass, citations |
| W6 | Mobile requirements | ✅ | 7 requirements |
| W7 | MC wireframes dashboard | ✅ | `/mission-control/wireframes.html` |

---

## Phase 22 — Database Schema (Build #22) ★ NEW

*15 entities, 10 join tables, v1 static storage, Supabase migration path.*

| # | Step | Status | Route |
|---|------|--------|-------|
| D1 | Database Schema v1.0 | ✅ | `data/database-schema.json` |
| D2 | 15 primary entities | ✅ | Fields + relationships |
| D3 | 10 join tables | ✅ | M:N relationships |
| D4 | 8 signup types | ✅ | Form taxonomy |
| D5 | v1/v2 storage strategy | ✅ | JSON → Postgres path |
| D6 | MC metrics mapped to tables | ✅ | 14 metrics |
| D7 | Canonical model extension | ✅ | 10 → 15 entities |
| D8 | MC database dashboard | ✅ | `/mission-control/database.html` |

**Note:** No database deployed — schema blueprint only (35% readiness).

---

## Phase 21 — Repository Structure (Build #21) ★ NEW

*GitHub and folder structure blueprint before framework migration.*

| # | Step | Status | Route |
|---|------|--------|-------|
| R1 | Repository Blueprint v1.0 | ✅ | `data/repository-blueprint.json` |
| R2 | Four workstreams mapped | ✅ | Current paths documented |
| R3 | Branch structure (main/develop/feature/content) | ✅ | |
| R4 | Target src/ and docs/ taxonomy | ✅ | Migration map |
| R5 | Target scripts and package.json | ✅ | |
| R6 | .env.example | ✅ | Placeholders only |
| R7 | GitHub labels & milestones | ✅ | Defined, not yet in remote |
| R8 | MC repository dashboard | ✅ | `/mission-control/repository.html` |

**Note:** Physical migration to `src/` not executed — blueprint only (28% structure readiness).

---

## Phase 20 — Platform Blueprint (Build #20) ★ NEW

*Version 1 system architecture — technical foundation before production code.*

| # | Step | Status | Route |
|---|------|--------|-------|
| P1 | Platform Architecture v1.0 | ✅ | `data/platform-architecture.json` |
| P2 | Technology stack documented | ✅ | GitHub, Netlify, FE, DS, Search |
| P3 | Content & data architecture | ✅ | MRID, canonical objects |
| P4 | Platform modules (coalition, contact, organizing, solutions) | ✅ | Honest capability status |
| P5 | Security & performance standards | ✅ | Requirements listed |
| P6 | V1 success criteria | ✅ | 9 criteria with honest % |
| P7 | Development workflow (10 stages) | ✅ | MC-tracked |
| P8 | Implementation roadmap #21–#25 | ✅ | Implementation artifacts |
| P9 | MC platform dashboard | ✅ | `/mission-control/platform.html` |

**Philosophy:** Build once. Expand forever.

---

## Phase 19 — Knowledge Atlas (Build #19) ★ NEW

*Seven learning worlds, districts, trails, and Learning Compass — educational backbone.*

| # | Step | Status | Route |
|---|------|--------|-------|
| K1 | Knowledge Atlas v1.0 | ✅ | `data/knowledge-atlas.json` |
| K2 | Seven Learning Worlds defined | ✅ | 51 districts |
| K3 | Six Knowledge Trails | ✅ | Beginner through Research |
| K4 | Learning Compass schema | ✅ | COMP-NAV-004 linked |
| K5 | Educational checkpoints | ✅ | 5 checkpoint types |
| K6 | Atlas map hierarchy | ✅ | Worlds → districts → pages → sources |
| K7 | Educational completion metrics | ✅ | 8 dimensions |
| K8 | MC atlas dashboard | ✅ | `/mission-control/atlas.html` |

**Governing principle:** The platform should feel like a civic learning environment — not a website with menus.

---

## Phase 18 — Facts Framework (Build #18) ★ NEW

*Canonical facts & evidence architecture — foundation for all educational content.*

| # | Step | Status | Route |
|---|------|--------|-------|
| F1 | Facts Framework v1.0 | ✅ | `data/facts-framework.json` |
| F2 | 6 fact categories (FACT-1000–6000) | ✅ | Constitution |
| F3 | Fact record schema + confidence levels | ✅ | 4 statuses |
| F4 | L1–L4 presentation levels | ✅ | Depth model aligned |
| F5 | Facts registry with seed facts | ✅ | `data/facts-registry.json` |
| F6 | Claims ledger migration (fact_id) | ✅ | 3 claims linked |
| F7 | EV-* and KG-* integrations | ✅ | Traceability |
| F8 | MC facts dashboard | ✅ | `/mission-control/facts.html` |

**Governing principle:** Facts are the foundation. Every resource traces back to verified facts with transparent evidence.

---

## Phase 17 — Component Registry (Build #17) ★ NEW

*Master component inventory + ACEI brand separation.*

| # | Step | Status | Route |
|---|------|--------|-------|
| C1 | Component Registry v1.0 | ✅ | `data/component-registry.json` |
| C2 | 7 categories (A–G), 42 components | ✅ | Honest live/partial/stub/planned |
| C3 | Brand identity scaffold (ACEI) | ✅ | `data/brand-identity.json` |
| C4 | MC components dashboard | ✅ | `/mission-control/components.html` |
| C5 | ACEI coalition rebrand (user-facing) | ✅ | Hub pages, layout, coalition docs |
| C6 | Design system cross-links | ✅ | Build #9 `ds-*` components |

**Component principle:** The platform should feel like one cohesive educational institution.

---

## Phase 16 — Route Inventory (Build #16) ★ NEW

*Complete page & route registry for Arkansas v1.*

| # | Step | Status | Route |
|---|------|--------|-------|
| R1 | Route Registry v1.0 | ✅ | `data/route-registry.json` |
| R2 | 9 route groups documented | ✅ | 81 routes total |
| R3 | Launch priorities (must / stub / later) | ✅ | MC dashboard |
| R4 | Action Hub link registry (10 links) | ✅ | Verified |
| R5 | Hub pages: Start Here, Arkansas, Join | ✅ | `/start-here/` `/arkansas/` `/join/` |
| R6 | Canonical netlify redirects | ✅ | `netlify.toml` |
| R7 | MC routes dashboard | ✅ | `/mission-control/routes.html` |

**Route principle:** Every route answers one reader question — educate, trust, civic, or mission control.

---

## Implementation Pivot — Builds #17–#20

*Master data model & relationship architecture — everything connected.*

| # | Step | Status | Route |
|---|------|--------|-------|
| D1 | Canonical Data Constitution | ✅ | `docs/CANONICAL_DATA_CONSTITUTION.md` |
| D2 | 10 canonical objects | ✅ | `data/canonical-data-model.json` |
| D3 | 20 relationship types | ✅ | `data/relationship-registry.json` |
| D4 | Relationship engine + example chain | ✅ | MC dashboard |
| D5 | Geographic intelligence (75 counties) | ✅ | Hierarchy in model |
| D6 | Timeline & search intelligence scaffold | 🟡 | Planned queries documented |
| D7 | Future AI readiness | 🟡 | Schema ready |
| D8 | Relationship health dashboard | ✅ | `/mission-control/data-model.html` |
| D9 | Platform integration map | ✅ | KG, Research, Civic, ACUCOS |

**Governing principle:** The platform grows in value through stronger relationships, not more pages.

---

## Implementation Pivot — Builds #16–#20

Stop creating high-level constitutions. Next builds are **concrete product design**:

| Build | Title |
|-------|-------|
| ~~**#16**~~ | ~~Complete page inventory~~ ✅ Done |
| ~~**#17**~~ | ~~Component inventory~~ ✅ Done |
| ~~**#18**~~ | ~~Citizens United Facts Framework~~ ✅ Done |
| ~~**#19**~~ | ~~Knowledge Atlas & Learning Paths~~ ✅ Done |
| ~~**#20**~~ | ~~Master Platform Blueprint & Technical Architecture~~ ✅ Done |
| ~~**#21**~~ | ~~Repository & folder structure~~ ✅ Done |
| ~~**#22**~~ | ~~Database schema and ERD~~ ✅ Done |
| ~~**#23**~~ | ~~Wireframes for every major screen~~ ✅ Done |
| ~~**#24**~~ | ~~Contact Intelligence & Community Relationship Architecture~~ ✅ Done |
| ~~**#25**~~ | ~~Mission Control 2.0 & Executive Command Center~~ ✅ Done |
| ~~**#26**~~ | ~~AI Knowledge & Research Engine~~ ✅ Done |
| ~~**#27**~~ | ~~Content Production Factory~~ ✅ Done |
| ~~**#28**~~ | ~~Community Education Academy~~ ✅ Done |
| ~~**#29**~~ | ~~Research Observatory~~ ✅ Done |
| **#30** | **Component specifications with props/states** |

---

**Deferred:** Deep content articles (KG-IDs, Evidence IDs) — after product inventory stabilizes.

---

## Phase 14 — ACUCOS (Build #14) ★ NEW

*Arkansas Citizens United Coalition Operating System — statewide organizational backbone.*

| # | Step | Status | Route |
|---|------|--------|-------|
| A1 | ACUCOS blueprint v2.0 | ✅ | `data/coalition-ecosystem.json` |
| A2 | ACUCOS Constitution | ✅ | `docs/ACUCOS_CONSTITUTION.md` |
| A3 | 6 participation levels | ✅ | Observer → Strategic Partner |
| A4 | 7 coalition categories | ✅ | Civic, nonprofit, educational, faith, professional, veterans, service |
| A5 | 75 county coalition pages | 🟡 | `/coalition/counties.html` |
| A6 | County completeness tracking | ✅ | `data/county-coalition-index.json` |
| A7 | 4-metric ACUCOS dashboard | ✅ | `/mission-control/coalition.html` |
| A8 | Growth engine (5 pathways) | 🟡 | `js/coalition-profile.js` |
| A9 | Recognition system | 🟡 | Scaffold in blueprint |
| A10 | Coalition communications | ⬜ | Newsletter planned |
| A11 | Future integrations map | ✅ | 9 systems linked |

**Governing principle:** Coalition growth is a primary platform success measure — not organizational size, but educational reach across Arkansas.

---

## Solutions & Policy Options Center

*Expands former "Reform Paths" into a structured policy exploration hub.*

**Hub:** [/solutions/](/solutions/) · **Blueprint:** `data/solutions-policy.json` · **Doc:** [SOLUTIONS_POLICY_OPTIONS.md](/docs/SOLUTIONS_POLICY_OPTIONS.md)

### Purpose

Educate readers about the range of policy approaches related to *Citizens United* — who has authority to pursue each, how proposals would work, and legal or constitutional considerations. Clearly distinguish **existing law**, **proposed reforms**, and **educational analysis**.

### Authority levels readers must distinguish

| Level | Mechanism examples |
|-------|-------------------|
| Federal | Legislation, FEC reform, disclosure statutes |
| State | Ballot initiatives, state legislatures, ethics commissions |
| Constitutional amendment | Article V campaigns |
| Private-sector | Shareholder governance, institutional policy |
| Community / civic | Education, forums, local leadership |
| Litigation | Court challenges testing precedent |

### Content pillars

| Pillar | Status | Route |
|--------|--------|-------|
| Federal Policy Options | 🟡 Hub scaffold | `/solutions/#federal` |
| State Policy Options | 🟡 MT/HI live | `/solutions/#state` |
| Arkansas General Assembly | 🟡 Dedicated section | `/solutions/#arkansas` |
| Community Solutions | 🟡 Linked to Teach | `/solutions/#community` |
| Solutions Comparison Matrix | 🟡 Live from `reform.json` | `/solutions/#matrix` |

### Per-proposal content standard

Each proposal explains: what it is · problem addressed · legal authority · constitutional questions · supporter arguments · critic arguments · current status.

### Civic engagement tools

| Tool | Status | Route |
|------|--------|-------|
| Share with U.S. Representative & Senators | 🟡 Scaffold | `/action/contact-legislators.html#federal` |
| Share with Arkansas General Assembly | 🟡 Scaffold | `/action/contact-legislators.html#arkansas` |
| Share with community & educators | 🟡 | `/action/share.html` |
| Invite others to explore | 🟡 | `/action/share.html` |

### Build steps (Solutions Center)

| # | Step | Status |
|---|------|--------|
| S1 | Rename Reform → Solutions in IA & nav | ✅ |
| S2 | Solutions hub page + comparison matrix | ✅ |
| S3 | `solutions-policy.json` blueprint | ✅ |
| S4 | Expand `reform.json` with matrix fields | ✅ |
| S5 | Federal share tool scaffold | 🟡 |
| S6 | Arkansas legislator share scaffold | 🟡 |
| S7 | L2 per-proposal deep pages | ⬜ Build #13+ |
| S8 | ZIP-based legislator lookup | ⬜ |
| S9 | Printable share packets (PDF) | ⬜ |
| S10 | Evidence IDs on every proposal claim | ⬜ |

### URL migration

- Canonical: `/solutions/`
- Legacy `/reform` and `/halls/reform.html` → redirect to `/solutions/`
