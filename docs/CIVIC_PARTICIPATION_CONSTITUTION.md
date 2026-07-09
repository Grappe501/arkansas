# Civic Participation Constitution v1.0

**Build #12** · Civic Action Ecosystem & Leadership Development System  
**Blueprint:** `data/civic-ecosystem.json` · **Dashboard:** [/mission-control/civic-ecosystem.html](/mission-control/civic-ecosystem.html) · **Action Hub:** on every page

---

## Purpose

The platform **educates first**. Its second purpose is to build a nationwide network of informed citizens who **voluntarily** help educate others.

The Civic Action Ecosystem transforms knowledge into sustained civic participation through education, relationship-building, collaboration, and constructive engagement with public institutions.

**Rule:** Never ask visitors to act before they understand. Guide progression from learner to trusted community educator.

---

## The Civic Growth Ladder (7 levels)

| Level | Role | Mission |
|-------|------|---------|
| **1** | Visitor | Curiosity and foundational understanding |
| **2** | Subscriber | Stay connected; continue learning |
| **3** | Advocate for Education | Share through trusted relationships |
| **4** | Community Educator | Host evidence-based conversations |
| **5** | Regional Education Leader | Coordinate and mentor locally |
| **6** | Research Contributor | Keep platform accurate and current |
| **7** | National Leadership Network | Sustain national educational community |

Tracked client-side: `js/civic-profile.js` · Schema: `data/participant-profile-schema.json`

---

## Civic Action Hub

Persistent floating hub on every page. **11 core actions** adapt to learning stage and civic growth level:

- Become an Education Leader
- Join the Contact Network
- Share This Page
- Invite Friends & Family
- Host a Community Conversation
- Download Educational Resources
- Model Law Workspace
- Ballot Initiative Lab
- Share with Public Officials
- Submit Community Ideas
- Ask a Question

---

## Relational Organizing

Education spreads through **trusted personal relationships** — family, friends, civic clubs, faith communities, campuses.

Privacy: aggregate tracking only; no public exposure of individual outreach.

---

## Community Conversation Program

[/action/community-conversation.html](/action/community-conversation.html) — guides, discussion questions, handouts, timelines, FAQs.

Emphasis: respectful dialogue, evidence-based learning.

---

## Policy Development Center

| Workspace | Route | Purpose |
|-----------|-------|---------|
| **Model Law Workspace** | `/action/draft-laws.html` | Collaborative educational legislative concepts |
| **Ballot Initiative Lab** | `/action/ballot-lab.html` | Research, comparison, draft language — educational only |

Clearly distinguished from enacted law.

---

## Public Official Resource Center

[/action/contact-legislators.html](/action/contact-legislators.html) — share factual educational materials with:

- U.S. Representatives & Senators
- Arkansas General Assembly
- Other state legislators (future)

---

## Participant Profiles

Unified profile — one record, deepening involvement without repeated data entry.

Elements: learning progress · interests · region · events · downloads · invitations · leadership pathway · research contributions.

**v1:** localStorage + Netlify Forms · **Future:** backend (Supabase/etc.)

---

## Leadership Dashboard

Mission Control [/mission-control/civic-ecosystem.html](/mission-control/civic-ecosystem.html) tracks network growth — **educational metrics**, not political success.

---

## Participation Principles

Encourage: curiosity · respectful dialogue · evidence · civic learning · leadership · constructive engagement.

Avoid: harassment · misinformation · disrespect · pressure before understanding.

---

## Governing Principle

> Success is measured by how many people become confident enough to help someone else understand *Citizens United*, contribute thoughtfully to civic discussions, and participate constructively through education.

---

## Governance

- Hub actions gated by civic growth level (`min_level` in `civic-ecosystem.json`)
- Aligns with Citizen Journey (`ux-journey.json`) and Knowledge Graph civic network
- See also: [CIVIC_ACTION.md](CIVIC_ACTION.md) (architecture notes)
