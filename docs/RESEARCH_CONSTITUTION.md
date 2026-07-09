# Research Constitution v1.0

**Build #10** · Master Research & Evidence Framework  
**Blueprint:** `data/research-framework.json` · **Evidence Registry:** `data/evidence-registry.json` · **Dashboard:** [/mission-control/research.html](/mission-control/research.html) · **Source Library:** [/library/](/library/)

---

## Purpose

The Citizens United Education Platform is **not built on opinions**. It is built on **evidence**.

Every educational page, visual, timeline entry, statistic, chart, quote, and conclusion must be traceable to reliable, identifiable sources. Readers must be able to independently verify what they read.

---

## Research Philosophy

### 1. Primary Sources First

Original documents are the foundation: Supreme Court opinions, oral argument transcripts, court briefs, FEC records, congressional records, state legislative text, ballot initiative filings, government datasets. Secondary sources supplement — they do not replace primary materials.

### 2. Multiple Independent Sources

Important factual claims should be supported by more than one reliable source when practical. This reduces error risk and shows where consensus exists and legitimate disagreement remains.

### 3. Transparency

Readers should always be able to answer:

- Where did this information come from?
- When was it published?
- Who produced it?
- Is it primary or secondary?
- Can I verify it myself?

### 4. Distinguish Fact from Interpretation

Clearly separate:

- Verified facts
- Legal holdings
- Historical events
- Statistical observations
- Scholarly analysis
- Policy arguments
- Editorial interpretation

### 5. Continuous Review

Research is never finished. The platform evolves as courts decide, scholarship publishes, spending changes, reforms pass, and primary materials emerge. Mission Control tracks review cycles.

---

## Source Hierarchy

| Tier | Category | Authority | Role |
|------|----------|-----------|------|
| **1** | Foundational | Highest | SCOTUS opinions, Constitution, statutes, official court/election records |
| **2** | Government & Institutional | High | FEC, CRS, GAO, state election offices, legislative agencies |
| **3** | Academic | Scholarly | Peer-reviewed journals, law reviews, university presses |
| **4** | Credible Journalism | Contextual | Investigative reporting, major newspapers, legal journalism |
| **5** | Supplemental Commentary | Interpretive | Advocacy, think tanks, educational orgs — labeled as viewpoint |

---

## Evidence Registry

Every research asset receives a permanent **Evidence ID** (`EV-000001`, `EV-000002`, …).

Each record includes: title, author, publisher, publication date, source type, jurisdiction, topic, URL, reliability tier, summary, related MRIDs, review status, and workflow stage.

Mission Control links content directly to supporting evidence.

---

## Citation Standards

Every educational page includes:

- Inline citations where appropriate
- A reference section
- Links to primary documents when available
- Publication and update dates
- Notes on significant source disagreements

**Rule:** Clarity over citation density — fully traceable.

See also: [CITATION_GUIDE.md](CITATION_GUIDE.md)

---

## Claim Verification

Significant factual statements receive a verification status:

| Status | Meaning |
|--------|---------|
| Verified | Confirmed against reliable source(s) |
| Multiple Independent Sources | Two+ independent sources agree |
| Primary Source Confirmed | Directly supported by Tier 1 document |
| Requires Review | Aging, dispute, or incomplete verification |
| Pending Update | New information available |
| Under Revision | Active editorial revision |

Claims tracked in `data/claims-ledger.json`.

---

## Research Review Workflow

1. Identified → 2. Collected → 3. Cataloged → 4. Summarized → 5. Cross-Checked → 6. Reviewed → 7. Approved → 8. Published → 9. Scheduled for Future Review

---

## Source Library Integration

Every source added to the platform becomes searchable in the [Source Library](/library/) by topic, date, court, state, source type, institution, author, publication, and related content.

---

## Research Dashboard

Mission Control [/mission-control/research.html](/mission-control/research.html) displays:

- Total sources collected
- Primary, government, academic, and journalism counts
- Sources awaiting review / needing updates
- Citation coverage and evidence completeness
- Research gaps

---

## Governing Principle

> The credibility of the Citizens United Education Platform depends not on how much information it contains, but on how confidently readers can verify that information for themselves.

Every page should empower readers to examine the evidence, understand the context, and reach informed conclusions based on transparent, well-documented research.

---

## Governance

- New evidence → register in `evidence-registry.json` before citing on public pages
- New claims → add to `claims-ledger.json` with Evidence IDs
- Citation format → [CITATION_GUIDE.md](CITATION_GUIDE.md)
- Visual trust signals → [DESIGN_LANGUAGE.md](DESIGN_LANGUAGE.md) (`ds-trust-bar`, `ds-evidence-panel`)
