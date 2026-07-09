# Civic Action Layer

> **Arkansas Civic Participation Constitution v1.0:** [CIVIC_PARTICIPATION_CONSTITUTION.md](CIVIC_PARTICIPATION_CONSTITUTION.md) · **Dashboard:** [/mission-control/civic-ecosystem.html](/mission-control/civic-ecosystem.html) · **Counties:** `data/arkansas-counties.json`

> **Platform evolution:** Knowledge website → Civic organizing platform

## Progression Model

**Learn → Participate → Organize → Build Solutions**

Extends Build #1's journey (Understand → Trust → Care → Teach → Lead) into collective action.

| Stage | What happens |
|-------|--------------|
| **Learn** | Halls, depth levels, source library |
| **Participate** | Sign up, join network, share, invite |
| **Organize** | Volunteer matching, events, relational outreach |
| **Build Solutions** | Draft laws, ballot initiatives, model legislation |

---

## Persistent Floating Action Hub

A compact expandable hub on every page (replaces single sticky CTA).

| Action | Purpose | Route |
|--------|---------|-------|
| Become a Leader | Education lead signup | `/educate/` |
| Join the Network | Contact list + updates | `/action/join-network.html` |
| Share This Page | Relational organizing | `/action/share.html` |
| Invite Friends | Referral tracking | `/action/share.html#invite` |
| Draft a Law | Collaborative legislation | `/action/draft-laws.html` |
| Build a Ballot Initiative | Ballot Initiative Lab | `/action/ballot-lab.html` |
| Contact Legislators | Lawmaker outreach | `/action/contact-legislators.html` |
| Ask a Question | Community ideas | `/action/ideas.html` |
| Give Feedback | Community input | `/action/ideas.html#feedback` |

Future: surface next logical action based on participant profile engagement.

---

## Unified Participant Profile

Every signup feeds one **participant profile** — no repeated data entry as involvement deepens.

```json
{
  "participant_id": "uuid",
  "contact": { "name", "email", "phone", "city", "state", "county", "zip" },
  "learning_progress": { "halls_visited", "depth_levels_used", "topics_completed" },
  "interests": { "topics", "leadership_roles", "volunteer_roles" },
  "organizing": {
    "referrals_made": 0,
    "referral_code": "string",
    "events_attended": [],
    "toolkit_downloads": []
  },
  "solutions": {
    "legislative_ideas_submitted": [],
    "ballot_contributions": [],
    "community_ideas": []
  },
  "leadership_pathway_stage": "learner | volunteer | researcher | organizer | presenter | education_lead"
}
```

**v1.4.0:** Schema + client-side stub (localStorage).  
**Future:** Supabase or secure backend for persistent profiles, admin dashboard, volunteer matching.

---

## Workspaces (Phased)

| Workspace | Build Plan Step | Status |
|-----------|-----------------|--------|
| Action Hub UI | 54 | 🟡 v1.4.0 scaffold |
| Education Leader quick signup | 55 | ✅ `/educate/` |
| Contact Network signup | 56 | 🟡 Form stub |
| Share / relational organizing | 57 | 🟡 v1.4.0 |
| Referral tracking | 58 | 🟡 localStorage stub |
| Draft Better Laws | 59 | ⬜ Workspace stub |
| Ballot Initiative Lab | 60 | ⬜ Workspace stub |
| Model Legislation Library | 61 | ⬜ Linked from draft-laws |
| Community Ideas | 62 | ⬜ Workspace stub |
| Volunteer directory / matching | 63 | ⬜ Requires backend |
| Leadership pathway guide | 64 | 🟡 Documented |
| Admin dashboard | 65 | ⬜ Netlify + future backend |

---

## Architecture Note

Static-first (GitHub + Netlify) handles forms and sharing now. Collaborative workspaces and participant profiles at scale will need a backend phase — schema is designed so that migration does not require redesign.
