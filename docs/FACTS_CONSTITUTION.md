# Citizens United Facts Framework

**Canonical Facts & Evidence Architecture v1.0** · **Build #18**  
**Dashboard:** [/mission-control/facts.html](/mission-control/facts.html) · **Registry:** [/data/facts-registry.json](/data/facts-registry.json)

---

## Purpose

The Citizens United Facts Framework establishes the official structure for every factual statement presented on the platform.

Rather than collecting facts randomly, the platform organizes them into a structured knowledge system that allows readers to move from simple understanding to expert-level research.

Every fact must be traceable, categorized, and connected to supporting evidence.

Mission Control tracks fact completeness alongside content, research, and platform progress.

---

## Fact Philosophy

Every fact should answer one of five questions:

* **What happened?**
* **When did it happen?**
* **Why did it happen?**
* **What changed because of it?**
* **How do we know?**

Facts should be presented clearly, with supporting evidence available for readers who want to explore further.

---

## Fact Categories

### FACT-1000 — The Case

Core facts about *Citizens United v. Federal Election Commission*.

Examples: parties involved, procedural history, questions before the Court, vote breakdown, holding, constitutional provisions discussed, opinions issued.

### FACT-2000 — Historical Context

Facts explaining the development of campaign finance law before 2010.

Examples: major federal legislation, significant Supreme Court decisions, historical events influencing reform, evolution of campaign finance regulation.

### FACT-3000 — Constitutional Principles

Facts describing constitutional doctrines discussed in the case.

Examples: First Amendment protections, political speech, corporate speech, independent expenditures, judicial standards of review.

### FACT-4000 — Political Spending

Verified facts describing campaign finance before and after the decision.

Examples: independent expenditure trends, outside spending, Super PAC development, disclosure rules, election spending comparisons.

### FACT-5000 — Current Developments

Facts describing ongoing legal and legislative developments.

Examples: state legislation, ballot initiatives, court challenges, Congressional proposals, regulatory developments.

### FACT-6000 — Arkansas

Arkansas-specific educational information.

Examples: Arkansas campaign finance framework, legislative process, ballot initiative process, Arkansas reform discussions, Arkansas educational activities.

---

## Fact Record Structure

Every fact includes:

| Field | Description |
|-------|-------------|
| `fact_id` | Permanent identifier (e.g. `FACT-1001`) |
| `short_statement` | One-sentence summary (Level 1) |
| `plain_explanation` | Plain-language explanation (Level 2) |
| `detailed_explanation` | Detailed educational discussion (Level 3) |
| `source_type` | Primary, government, academic, journalism, etc. |
| `supporting_sources` | Evidence IDs (`EV-*`) and source links |
| `related_topics` | Knowledge graph nodes (`KG-*`) |
| `related_timeline_events` | Timeline entries |
| `related_cases` | Supreme Court cases |
| `related_charts` | Data visualizations |
| `related_educational_resources` | Articles, guides, presentations |
| `last_verification_date` | ISO date |
| `review_status` | Confidence level (see below) |
| `philosophy_question` | What / When / Why / What changed / How we know |

---

## Fact Confidence Levels

| Status | Meaning |
|--------|---------|
| **Confirmed** | Supported by primary or authoritative sources |
| **Strongly Supported** | Multiple reliable independent sources |
| **Context Dependent** | Accurate but requires additional explanation |
| **Under Review** | Pending verification or update |

Mission Control displays verification status for every educational page.

---

## Fact Relationships

Every fact connects to other platform objects:

* Timeline entries
* Supreme Court cases
* Historical legislation
* Charts
* Research sources (`EV-*`)
* Educational videos
* Frequently asked questions
* Community discussion guides

**No fact should exist without context.**

---

## Fact Presentation Levels

| Level | Format |
|-------|--------|
| **L1** | One-sentence summary |
| **L2** | Plain-language explanation |
| **L3** | Detailed educational discussion |
| **L4** | Primary sources, citations, and related research |

Readers control how deeply they explore.

---

## "How We Know" Section

Every major educational page should include a dedicated section explaining how the platform reached its conclusions:

* Primary documents
* Historical records
* Government publications
* Court opinions
* Academic research
* Data sources

Transparency strengthens trust.

---

## Mission Control Integration

Mission Control monitors:

* Total facts cataloged
* Facts verified
* Facts needing review
* Facts awaiting additional sources
* Arkansas-specific facts
* Facts by category (case, historical, constitutional, spending, developments, Arkansas)

This measures **factual completeness** separately from page completion.

---

## Platform Integrations

| System | Relationship |
|--------|--------------|
| Evidence Registry (Build #10) | `EV-*` IDs support facts |
| Claims Ledger | Legacy claims migrate to `FACT-*` |
| Knowledge Graph (Build #11) | `KG-*` nodes provide context |
| Research Constitution | Source tiers govern verification |
| Canonical Data Model (Build #15) | Facts as first-class objects |

---

## Future Expansion

The framework accommodates:

* New court decisions
* Updated spending data
* Additional state reforms
* Congressional activity
* Arkansas legislative developments
* New academic scholarship

The structure remains stable while the knowledge base grows.

---

## Governing Principle

Facts are the foundation of the Citizens United Education Platform.

Every article, chart, discussion guide, presentation, and educational resource should ultimately trace back to verified facts supported by transparent evidence.

Readers should leave the platform not only with greater understanding, but also with confidence that they can examine the evidence for themselves.
