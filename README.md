# Citizens Facts

**The definitive public encyclopedia on one Supreme Court case and its consequences.**

A civic education engine — not a brochure. Turn a curious reader into a local educator.

**Mission path:** Understand → Trust → Care → Teach → Lead

## Live Site

**[arkansas-facts.netlify.app](https://arkansas-facts.netlify.app/)**

## Architecture

| Level | What it is |
|-------|------------|
| **0 — Front Door** | Six plain-language questions. "Why should I care?" |
| **1 — Learning Halls** | Seven halls from history through live reform (Montana/Hawaii) |
| **2 — Depth** | Every topic: 1-min → 5-min → 20-min → Research file |
| **3 — Educate** | Education Lead signup — host, teach, research, lead locally |

### Seven Learning Halls

1. The Story Before Citizens United
2. The Case Itself
3. What Changed After 2010
4. The Money Map
5. The Debate
6. Reform Paths
7. **Montana and Hawaii** (LIVE)

## Current Version: 1.1.0

Phase 1 civic education engine scaffold. Halls 1–6 have L1 content; deeper levels expand in future versions.

## Project Structure

```
├── index.html              # Level 0 — Front Door
├── halls/                  # Level 1 — Seven Learning Halls
├── educate/                # Level 3 — Education Lead funnel + form
├── content/entries/        # Structured live research nodes (JSON)
├── data/
│   ├── site.json           # Site manifest
│   └── knowledge.json      # Halls, ladder, depths schema
├── css/                    # styles.css + education.css
└── js/                     # layout.js, depth.js, app.js
```

## Local Development

```bash
npm start
```

## Deployment

- **GitHub:** [Grappe501/arkansas](https://github.com/Grappe501/arkansas)
- **Netlify:** [arkansas-facts.netlify.app](https://arkansas-facts.netlify.app/) — auto-deploys on push to `main`

## Versioning

| Version | Description |
|---------|-------------|
| 1.1.0   | Civic education engine — Front Door, 7 Halls, Educate funnel |
| 1.0.0   | Initial site + Montana/Hawaii research entry |
