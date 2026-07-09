# Contributing to Citizens Facts

## Repository

- **GitHub:** [Grappe501/arkansas](https://github.com/Grappe501/arkansas)
- **Recommended name:** `citizens-united-facts` (see [Repository Blueprint](/mission-control/repository.html))
- **Live:** [arkansas-facts.netlify.app](https://arkansas-facts.netlify.app/)

## Branches

| Branch | Purpose |
|--------|---------|
| `main` | Production — auto-deploys to Netlify |
| `develop` | Integration — merge features here first |

**Workflow:** Create a feature branch from `develop` → PR into `develop` → PR into `main` when ready to ship.

> Enable branch protection on `main` in GitHub Settings → Branches → Require pull request.

## Project Board (GitHub UI)

Create a board with columns:

**Backlog → Researching → Drafting → Building → Reviewing → Ready → Shipped**

## Adding Content

1. Read `docs/CONSTITUTION.md`, `docs/STYLE_GUIDE.md`, `docs/CITATION_GUIDE.md`
2. Add topic to appropriate inventory in `data/inventories/`
3. Write hall content at four depths (or start with L1)
4. Add sources to L4 and `data/claims-ledger.json`
5. Run editorial checklist (`docs/EDITORIAL_CHECKLIST.md`)
6. Update `BUILD_PLAN.md` step status
7. Bump `VERSION`, update `CHANGELOG.md`
8. PR with version in title (e.g. `v1.3.0: Hall 2 L2 content`)

## Adding Live Research (Ernie Entries)

1. Create `content/entries/NNN-slug.json`
2. Update hall page (usually Hall 7 or Reform)
3. Add to `data/site.json` entries array
4. Add timeline event to `data/inventories/timeline.json`

## Local Development

```bash
cd H:\Arkansas-citizens-facts
npm start
# http://localhost:8080
```

## Issue Templates

Use GitHub Issues with templates for: Content, Data, Design, Bug, Research.

## Netlify

- Do not commit secrets or `.env` files
- Forms handled by Netlify Forms (honeypot enabled)
- Configure notifications in Netlify dashboard → Forms → education-lead

## All Files on H: Drive

Project root: `H:\Arkansas-citizens-facts`
