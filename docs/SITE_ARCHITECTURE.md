# Master Information Architecture v1.0

**Build #5** · Citizens United Education Platform  
**Data:** `data/site-architecture.json` · **Blueprint:** [/mission-control/architecture.html](/mission-control/architecture.html) · **Public map:** [/explore/](/explore/)

---

## Design Philosophy

The platform uses a **layered exploration model**.

Every visitor should be able to:

- Learn the basics in minutes
- Drill down into increasing levels of detail
- Return to higher-level summaries at any time
- Follow natural connections between topics
- Never feel lost

**Navigation rule:** Answer questions rather than expose technical categories.

**Architecture principle:** The platform should never feel like a collection of articles. It should feel like exploring a living institution dedicated to helping citizens understand one of the most consequential Supreme Court decisions in modern American history.

---

## Primary Navigation

| Section | Question | Canonical URL | Status |
|---------|----------|---------------|--------|
| **Home** | — | `/` | Live |
| **The Story** | How did we get here? | `/the-story` | Stub → `/halls/story-before.html` |
| **The Case** | What actually happened? | `/the-case` | Stub |
| **The Constitution** | Why did the Court rule this way? | `/the-constitution` | Stub |
| **The Impact** | What changed after 2010? | `/the-impact` | Stub |
| **Follow the Money** | Where does political money go? | `/follow-the-money` | Stub |
| **The Debate** | Why do intelligent people disagree? | `/the-debate` | Stub |
| **Reform** | What are people trying to do now? | `/reform` | Partial (MT/HI live) |
| **Teach Your Community** | How can I help educate others? | `/teach` | Partial |
| **Source Library** | Where did this information come from? | `/sources` | Partial |

Each section has defined subsections in `site-architecture.json`. Deep pages use the pattern `/parent-section/subsection-slug`.

---

## Secondary Navigation

Persistent throughout the platform:

- Timeline · Search · Glossary · Interactive Maps · FAQ · Latest Research · Mission Control · Site Map

Most secondary destinations are **planned** (Build #6+). Canonical URLs are reserved.

---

## Reader Journey

Every page should indicate where the reader is:

```
Discover → Understand → Explore → Evaluate → Discuss → Teach → Lead
```

Aligned with the Project Constitution (Build #2).

---

## Cross-Linking Standards

Every page must include:

- Related Topics · Previous Topic · Next Topic · Go Deeper · Return to Overview · Primary Sources · Share This Page · Take Action

**Rule:** No page should become a dead end.

---

## Search Strategy

Nine search modes planned (global keyword, topic, timeline, SCOTUS case, historical event, spending data, state reform, source library, glossary). Implementation deferred to Build #6+.

---

## URL Standards

- Short, descriptive, stable
- Deep pages extend beneath parent: `/the-story/watergate`, `/reform/montana`
- Canonical URLs redirect to current hall pages during migration

---

## Floating Action Hub

Ten persistent actions on every page. Future: highlight next recommended action based on visitor progress (localStorage journey tracking).

---

## Relationship to Other Blueprints

| Document | Purpose |
|----------|---------|
| `PHASE_REGISTRY.md` | 15-phase project roadmap |
| `SITE_ARCHITECTURE.md` | Every destination on the site |
| Build #6 (next) | Master Content Inventory — every page, chart, dataset, glossary term |

---

*Update `data/site-architecture.json` on every build commit.*
