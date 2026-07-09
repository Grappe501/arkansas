# Build #13 — Coalition Building & Public Outreach

**Status:** ✅ Complete (scaffold)  
**Version:** 1.17.0  
**Routes:** [/mission-control/coalition.html](/mission-control/coalition.html) · [/coalition/](/coalition/)

---

## Purpose

Establish the **Coalition & Outreach Layer** as a first-class system — not another signup form. Unite Arkansas organizations around educational coalition building alongside Education, Research, and Civic Action.

## What Shipped

- **`data/coalition-ecosystem.json`** — membership levels, workspaces, growth metrics, principles
- **`data/coalition-directory.json`** — directory scaffold (0 organizations)
- **`data/organization-profile-schema.json`** — org profile fields + privacy model
- **`data/coalition-events.json`** — event calendar scaffold
- **`docs/COALITION_OUTREACH.md`** — governing documentation
- **`/coalition/`** — public hub, join form, resource center, event calendar
- **`/mission-control/coalition.html`** — Coalition Growth Dashboard + county map table
- **Homepage** — three parallel entry paths (Learn · Help · Partner)
- **`platform_layers`** in `data/site-architecture.json`
- **Action Hub** — "My Organization Wants to Partner" action

## Homepage Three Paths

| Entry | Pillar | Route |
|-------|--------|-------|
| I'm Here to Learn | Education | `/explore/` |
| I Want to Help | Leadership | `/educate/` |
| My Organization Wants to Partner | Coalition | `/coalition/` |

## Honest Status

Coalition **framework live**. Directory, events, and social metrics at **0** until organizations join and forms integrate. Interactive map planned.

## Next Recommended Build

**Build #14 — First Deep Content** — Arkansas-focused L2 articles with KG-IDs and Evidence IDs.
