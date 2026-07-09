# Citizens United Education Website — Master Build Plan

100 steps across **12 operational phases**, governed by the **15-phase [Master Phase Registry](/mission-control/phases.html)**.

Status: ✅ Done · 🟡 Partial · ⬜ Not started

**Current version:** 1.9.0 · **OS:** [Mission Control](/mission-control/) · **Registry:** [Phase Registry](/mission-control/phases.html) · **IA:** [Site Architecture](/mission-control/architecture.html)  
**Build #5:** ✅ Site Architecture · **Build #4:** ✅ Phase Registry · **Build #3:** ✅ Mission Control  
**Public map:** [/explore/](/explore/) · **Live site:** [arkansas-facts.netlify.app](https://arkansas-facts.netlify.app/)

> **Governing blueprints:** `docs/PHASE_REGISTRY.md` · `docs/SITE_ARCHITECTURE.md`  
> **Data:** `data/phase-registry.json` · `data/site-architecture.json`

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
| 9 | Reform & Current Developments | |
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
| 15 | Reform Paths | ✅ | `/halls/reform.html` |
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

## Platform Progression

```
Learn          →  Participate     →  Organize         →  Build Solutions
(Halls)           (Sign up, network)  (Share, invite)     (Draft laws, ballot lab)
```

## Progress Summary

| Phase | Focus | Status |
|-------|-------|--------|
| 1–6 | Knowledge system | Mostly ✅ |
| **7** | **Civic Action Layer** | **🟡 Scaffolded v1.4.0** |
| 8–12 | Forms, tech, launch | 🟡 |

**Next:** Build #6 — Master Content Inventory. Then deep subsection pages per architecture blueprint.
