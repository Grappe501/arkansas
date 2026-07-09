# Knowledge Graph Constitution v1.0

**Build #11** · Citizens United Knowledge Graph & Educational Intelligence Architecture  
**Blueprint:** `data/knowledge-graph.json` · **Registry:** `data/kg-registry.json` · **Dashboard:** [/mission-control/knowledge-graph.html](/mission-control/knowledge-graph.html)

---

## Purpose

The platform is **not a collection of pages**. It is a **connected knowledge system**.

Every topic, person, case, law, principle, organization, dataset, timeline event, state initiative, research paper, chart, and civic action exists as an interconnected knowledge graph node.

The platform should **answer questions**, **reveal relationships**, and **encourage exploration**.

---

## Vision

Like the Library of Congress: every court case points to earlier cases; every law to the problem it addressed; every reform to constitutional questions; every statistic to its source. Readers can continue exploring forever.

---

## Core Knowledge Objects (8 types)

| Type | Prefix | Examples |
|------|--------|----------|
| **Supreme Court Cases** | `KG-CASE` | Citizens United, Buckley, McConnell, Austin, Bellotti |
| **Historical Events** | `KG-EVENT` | Tillman Act, Watergate, BCRA, Super PACs |
| **Constitutional Principles** | `KG-PRIN` | Political speech, corporate speech, strict scrutiny |
| **Organizations** | `KG-ORG` | FEC, Supreme Court, Congress, American Promise |
| **People** | `KG-PERSON` | Justices, scholars, legislators |
| **Laws** | `KG-LAW` | FECA, BCRA, First Amendment |
| **Data Objects** | `KG-DATA` | Spending datasets, charts, timelines |
| **Reform Objects** | `KG-REFORM` | Amendments, MT I-194, HI Act 11, Arkansas options |

Every object requires a **KG-ID** and at least one **relationship edge**.

---

## Relationship Engine

Every object answers: **What is this connected to?**

Example — Citizens United connects to:

- Supreme Court · First Amendment · Buckley · McConnell · Super PACs
- Independent expenditures · Montana · Hawaii · Proposed amendments

Readers should never encounter isolated information.

Relationship types: precursor, aftermath, cites, addresses, challenges, enables, influenced, supports, measures, and more.

---

## Universal "Explore Further"

Every page ends with intelligent exploration:

- People also explored…
- Related constitutional principles…
- Related Supreme Court cases…
- Historical events that led here…
- Later events influenced by this…
- Current reform efforts…
- Relevant spending data…
- Primary sources…
- Educational toolkit…
- Become an Education Leader…

Implemented via `js/explore-further.js` on public content pages.

---

## Knowledge Map (10 clusters)

History → Law → Court Cases → Constitution → Money → Impact → Debate → Solutions → Community Education → Leadership

Mission Control displays cluster completeness and node counts.

---

## Educational Intelligence

The platform understands where a visitor is intellectually:

| Condition | Recommendation |
|-----------|----------------|
| Studied case, not Constitution | Constitutional principles |
| Understands spending | Reform proposals |
| Finished learning modules | Teaching resources |
| Visited solutions center | Montana/Hawaii live examples |

Integrates with Citizen Journey (`js/journey.js`) and graph recommendations.

---

## Knowledge Completeness

Each object tracks: research · writing · fact-checking · sources · visuals · related links · downloads · teaching resources · **completion %**

Mission Control monitors graph health: orphan nodes, hub connectivity, average completion.

---

## Future AI Layer (planned)

Capabilities must **cite the verified knowledge base** — never invent information:

- Plain-English Q&A
- Reading-level adaptation
- Personalized learning paths
- Lesson plan generation
- Opinion summarization with source links

---

## Civic Knowledge Network

Every object answers: **"How can someone use this to help another person understand?"**

Connects to discussion guides, handouts, share tools, leadership pathways.

---

## Governing Principle

> The Citizens United Education Platform is a living civic knowledge network. Knowledge should never end at the page where it began.

---

## Governance

- New objects → register in `kg-registry.json` before publishing
- Factual claims → link to Evidence IDs (`evidence-registry.json`)
- Requirements → link to MRIDs (`mrid-registry.json`)
- Visual components → `ds-evidence-panel`, Explore Further block
