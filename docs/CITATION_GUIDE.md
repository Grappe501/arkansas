# Citation & Source Guide

## Standard

Every L4 research file and claims-ledger entry must include:

1. **Source title**
2. **Publisher / author**
3. **URL** (permanent link preferred)
4. **Access date** (for web sources)
5. **Source type** (court opinion, news, government, academic, NGO)

## Source Type Tags

| Tag | Examples |
|-----|----------|
| `court` | Supreme Court opinions, lower court rulings |
| `government` | FEC, Secretary of State, Congress.gov |
| `news` | AP, major outlets |
| `academic` | Law reviews, peer-reviewed studies |
| `ngo` | Ballotpedia, OpenSecrets, American Promise |
| `primary` | Statutes, initiative text, legislative acts |

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
- `sources[]`
- `last_verified`
- `hall` / `topic`

## Live Research (Ernie Entries)

Structured entries in `content/entries/` are the canonical source for live state research. HTML halls summarize; JSON holds full detail.
