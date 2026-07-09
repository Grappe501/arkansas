# Citizen Journey Blueprint v1.0

**Build #8** · Citizens United Education Platform  
**Data:** `data/ux-journey.json` · **Dashboard:** [/mission-control/journey.html](/mission-control/journey.html)

---

## Purpose

The platform is designed around **people**, not pages.

Every visitor arrives with different knowledge, curiosity, time, and desired involvement. The UX Architecture ensures the right information at the right time—with clear paths to go deeper or engage.

The experience should feel like a **museum + documentary + university course + civic action center** — seamlessly connected.

---

## Design Philosophy

1. **Curiosity First** — create curiosity, not overload
2. **Progressive Discovery** — deeper layers unlock naturally
3. **No Dead Ends** — every page offers next steps
4. **Evidence Before Opinion** — education precedes interpretation
5. **Education Before Action** — civic invitations rooted in understanding

---

## Six Visitor Personas

| Persona | Goal | Entry journey |
|---------|------|---------------|
| Curious Citizen | Why does this still matter? | Home → What Changed → Share |
| Student | History + legal principles | Story → Case → Constitution → Sources |
| Journalist | Verified facts fast | Search → Timeline → Sources → Reform |
| Teacher | Classroom materials | Teach → Lessons → Presentations |
| Community Leader | Educate locally | Leadership → Toolkit → Signup |
| Researcher | Original sources | Sources → Case → Timeline → Data |

---

## Learning Ladder (7 stages)

Discover → Understand → Explore → Evaluate → Discuss → Teach → Lead

Mission Control estimates visitor stage via session memory (localStorage v1).

---

## Session Memory (v1)

Stored locally: last page, stage, pages visited, milestones, bookmarks, visit count.

Returning visitors see **Continue Learning** prompt.

---

## Adaptive Recommendations

End-of-page next steps based on current learning stage and page context.

---

## Persistent Learning Panel

Collapsible side panel: progress, stage, bookmarks, recent activity, suggested lesson.

---

## Stage-Aware Action Hub

- **Early** (Discover/Understand): Share, Save, Join Network
- **Advanced** (Explore+): Education Leader, Host Conversation, Model Law, Ballot Lab, Lawmakers

Hub never interrupts learning.

---

## Completion Milestones

- Completed The Story · The Case · Constitutional Principles · Impact · Reform · Community Education

---

## Success Indicators

Track educational outcomes: learning path completion, depth, toolkit downloads, leader signups, shares, return rate.

---

## UX Guiding Principle

> Visitors leave more informed than they arrived—and confident enough to help someone else understand *Citizens United*.

---

*Update `data/ux-journey.json` and `js/journey.js` on every UX build.*
