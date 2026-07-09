# Citizens United Education Website — Master Build Plan

100 steps across 11 phases. Status key: ✅ Done · 🟡 Partial · ⬜ Not started

**Current version:** 1.3.0 · **Build #1:** ✅ Complete

**Live site:** [arkansas-facts.netlify.app](https://arkansas-facts.netlify.app/)  
**Repository:** [github.com/Grappe501/arkansas](https://github.com/Grappe501/arkansas)

---

## Phase 1 — Project Constitution

| # | Step | Status |
|---|------|--------|
| 1 | Define site mission: deep public understanding of *Citizens United* | ✅ Build #1 `builds/001-mission-statement.md` |
| 2 | Define conversion goal: recruit local education leaders | ✅ |
| 3 | Define core reader journey: Understand → Trust → Care → Teach → Lead | ✅ |
| 4 | Define site promise: plain language with deep research underneath | ✅ |
| 5 | Define editorial standard: accurate, sourced, non-hysterical | ✅ `docs/STYLE_GUIDE.md` |
| 6 | Define primary audience groups | ✅ `docs/CONSTITUTION.md` |
| 7 | Define success metric: completed local education lead signups | ✅ |

---

## Phase 2 — Information Architecture

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
| 19 | Signup form page | ✅ | `/educate/` (form) + `/educate/thanks.html` |

---

## Phase 3 — Depth Model

| # | Step | Status |
|---|------|--------|
| 20 | Four reader-depth levels on every major topic | 🟡 Hall 7 complete; Halls 1–6 L1 only |
| 21 | Level 1: one-minute overview | 🟡 |
| 22 | Level 2: five-minute article | 🟡 Hall 7 only |
| 23 | Level 3: twenty-minute deep dive | 🟡 Hall 7 only |
| 24 | Level 4: research file | 🟡 Hall 7 + library stubs |
| 25 | Reusable page templates per depth | ✅ `js/depth.js` + hall template |
| 26 | "Go deeper" navigation | ✅ Depth toggle on every hall |
| 27 | "Return to simple explanation" | ✅ L1 always available via toggle |

---

## Phase 4 — Content System

| # | Step | Status |
|---|------|--------|
| 28 | Master topic inventory | ✅ `data/inventories/topics.json` |
| 29 | Legal case inventory | ✅ `data/inventories/cases.json` |
| 30 | Historical timeline inventory | ✅ `data/inventories/timeline.json` |
| 31 | Political spending data inventory | ✅ `data/inventories/spending.json` |
| 32 | Reform proposal inventory | ✅ `data/inventories/reform.json` |
| 33 | Montana initiative research file | ✅ `content/entries/001-*.json` |
| 34 | Hawaii legislative research file | ✅ `content/entries/001-*.json` |
| 35 | Citation/source standard | ✅ `docs/CITATION_GUIDE.md` |
| 36 | Editorial review checklist | ✅ `docs/EDITORIAL_CHECKLIST.md` |
| 37 | Claims ledger | ✅ `data/claims-ledger.json` |

---

## Phase 5 — Data and Visual Layer

| # | Step | Status |
|---|------|--------|
| 38 | Define core charts | ✅ `data/inventories/spending.json` |
| 39 | Decide first data sources | 🟡 FEC, OpenSecrets planned |
| 40 | Static starter charts for v1 | ⬜ v1.3.0 |
| 41 | Expandable chart notes | ⬜ |
| 42 | Source links under every chart | ⬜ |
| 43 | Future interactive dashboards plan | ✅ Noted in BUILD_PLAN |
| 44 | "What this chart means" explanations | ⬜ |

---

## Phase 6 — Website Experience

| # | Step | Status |
|---|------|--------|
| 45 | Landing page as 30,000-foot overview | ✅ |
| 46 | Navigation around reader questions | ✅ |
| 47 | Visual pathway cards per section | ✅ Halls grid |
| 48 | Timeline preview on homepage | ✅ v1.2.0 |
| 49 | Money flow preview on homepage | ✅ v1.2.0 |
| 50 | "What changed after 2010" proof section | ✅ v1.2.0 |
| 51 | "Current fight" — Montana & Hawaii | ✅ |
| 52 | Final leadership invitation | ✅ CTA banner |
| 53 | Persistent "Lead Education Locally" CTA | ✅ v1.2.0 |

---

## Phase 7 — Local Education Funnel

| # | Step | Status |
|---|------|--------|
| 54 | Local education lead roles | ✅ |
| 55 | Beginner-friendly volunteer roles | ✅ |
| 56 | Research volunteer roles | ✅ |
| 57 | Speaker/presenter roles | ✅ |
| 58 | Campus organizer roles | ✅ |
| 59 | Faith/community outreach roles | ✅ |
| 60 | Legal/policy research roles | ✅ |
| 61 | "Teach This Locally" page | ✅ `/educate/` |
| 62 | Starter toolkit request pathway | ✅ Form field |
| 63 | Follow-up email/message framework | ⬜ Admin process |
| 64 | Admin process for reviewing signups | ⬜ Netlify dashboard + export |

---

## Phase 8 — Signup Form

| # | Step | Status |
|---|------|--------|
| 65 | Core fields: name, email, phone, city, state, county, ZIP | ✅ |
| 66 | Role-interest checkboxes | ✅ |
| 67 | Experience-level question | ✅ |
| 68 | Event-hosting question | ✅ |
| 69 | Starter-toolkit request | ✅ |
| 70 | Notes field | ✅ |
| 71 | Privacy notice | ✅ v1.2.0 |
| 72 | Anti-spam protection | ✅ Honeypot |
| 73 | Confirmation page | ✅ `/educate/thanks.html` |
| 74 | Internal notification workflow | 🟡 Netlify email notifications |
| 75 | Exported submission backup | 🟡 Netlify Forms export |

---

## Phase 9 — Technical Stack

| # | Step | Status |
|---|------|--------|
| 76 | Static-first architecture | ✅ |
| 77 | GitHub source repository | ✅ |
| 78 | Netlify continuous deployment | ✅ User-connected |
| 79 | `netlify.toml` | ✅ |
| 80 | Build command + publish directory | ✅ |
| 81 | Environment variables in Netlify only | ✅ Documented |
| 82 | Branch deploys + deploy previews | 🟡 Enable in Netlify UI |
| 83 | Production branch protections | 🟡 Enable in GitHub UI |
| 84 | Netlify Forms | ✅ |
| 85 | Spam protection | ✅ Honeypot |

---

## Phase 10 — GitHub Workflow

| # | Step | Status |
|---|------|--------|
| 86 | Main branch | ✅ |
| 87 | Development branch | ✅ `develop` |
| 88 | Require PRs into main | 🟡 Documented in CONTRIBUTING |
| 89 | Issue templates | ✅ `.github/ISSUE_TEMPLATE/` |
| 90 | Project board columns | 🟡 Documented — create in GitHub UI |
| 91 | README | ✅ |
| 92 | Contribution guide | ✅ `CONTRIBUTING.md` |
| 93 | Content style guide | ✅ `docs/STYLE_GUIDE.md` |
| 94 | Source/citation guide | ✅ `docs/CITATION_GUIDE.md` |

---

## Phase 11 — Netlify Deployment

| # | Step | Status |
|---|------|--------|
| 95 | Connect GitHub to Netlify | ✅ User completed |
| 96 | Build settings | ✅ |
| 97 | Environment variables | 🟡 As needed |
| 98 | Deploy previews | 🟡 Enable in Netlify UI |
| 99 | Test deploy, form, confirmation | 🟡 User verification |
| 100 | Launch v1 + content expansion | 🟡 **v1.2.0 shipped — expansion ongoing** |

---

## Progress Summary

| Phase | Done | Partial | Not started |
|-------|------|---------|-------------|
| 1 Constitution | 7 | 0 | 0 |
| 2 IA | 12 | 0 | 0 |
| 3 Depth | 3 | 4 | 0 |
| 4 Content | 10 | 0 | 0 |
| 5 Data/Visual | 2 | 1 | 5 |
| 6 Experience | 9 | 0 | 0 |
| 7 Funnel | 9 | 2 | 0 |
| 8 Form | 9 | 2 | 0 |
| 9 Technical | 8 | 3 | 0 |
| 10 GitHub | 6 | 2 | 0 |
| 11 Netlify | 2 | 4 | 0 |

**Next priorities (v1.3.0):** Hall 2 L2–L4 content, static spending charts, timeline explorer, guided opinion reading.
