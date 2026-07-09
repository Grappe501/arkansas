# Citation & Source Guide

**Research Constitution:** [RESEARCH_CONSTITUTION.md](RESEARCH_CONSTITUTION.md) · **Evidence Registry:** `data/evidence-registry.json` · **Dashboard:** [/mission-control/research.html](/mission-control/research.html)

## Standard

Every L4 research file and claims-ledger entry must include:

1. **Source title**
2. **Publisher / author**
3. **URL** (permanent link preferred)
4. **Access date** (for web sources)
5. **Source type** (court opinion, news, government, academic, NGO)

## Source Type Tags

| Tag | Tier | Examples |
|-----|------|----------|
| `court` | 1 | Supreme Court opinions, lower court rulings |
| `primary` | 1 | Statutes, initiative text, legislative acts |
| `government` | 2 | FEC, Secretary of State, Congress.gov |
| `academic` | 3 | Law reviews, peer-reviewed studies |
| `news` / `journalism` | 4 | AP, major outlets |
| `ngo` | 5 | Ballotpedia, OpenSecrets, American Promise |

## Preferred Sources

- **Case law:** [Supreme Court](https://www.supremecourt.gov/), Cornell LII
- **Campaign finance data:** [FEC](https://www.fec.gov/), [OpenSecrets](https://www.opensecrets.org/)
- **Ballot measures:** [Ballotpedia](https://ballotpedia.org/), state Secretary of State
- **Legislation:** State legislature sites, Congress.gov

## In-Page Format

```html
<a href="URL" target="_blank" rel="noopener">Publisher — Title</a>
```

## Claims Ledger

Major factual claims are tracked in `data/claims-ledger.json` with:

- `claim_id`
- `claim_text`
- `evidence_ids[]` — links to Evidence Registry (`EV-000001`, …)
- `sources[]`
- `verification_status`
- `last_verified`
- `hall` / `topic`

Register new sources in `data/evidence-registry.json` before citing.

## Live Research (Ernie Entries)

Structured entries in `content/entries/` are the canonical source for live state research. HTML halls summarize; JSON holds full detail.
