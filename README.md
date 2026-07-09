# Citizens Facts

A versioned research system tracking **Citizens United** reform, ballot initiatives, and democratic finance policy across the United States.

Built incrementally from verified research snapshots provided by Ernie. Each entry receives a new version, GitHub commit, and Netlify deployment.

## Research Tracks

1. **Citizens United Legal & Political History** — What the decision held, Super PAC power, state regulatory limits.
2. **Anti–Citizens United Reform Efforts** — Maine litigation, American Promise amendment, state test cases.
3. **Ballot Initiatives & Legislative Routes** — Missouri, Florida, California, and state-specific paths.

## Current Version: 1.0.0

### Entry 001 — Montana & Hawaii: Two Paths Against Citizens United

- **Montana** — Initiative 194 (ballot initiative path); county signature verification due July 17, 2026.
- **Hawaii** — Act 11 (legislative corporate-charter path); effective July 1, 2027.

## Project Structure

```
├── index.html              # Homepage
├── entries/                # Published research entries (HTML)
├── content/entries/        # Structured entry data (JSON)
├── data/site.json          # Site manifest & entry index
├── css/styles.css          # Design system
├── js/app.js               # Site utilities
├── VERSION                 # Current release version
└── netlify.toml            # Netlify deployment config
```

## Local Development

```bash
npm start
```

Opens a local server at `http://localhost:8080`.

## Deployment

- **GitHub:** [Grappe501/Arkansas-citizens-facts](https://github.com/Grappe501/Arkansas-citizens-facts)
- **Netlify:** Connected for automatic deploys on push to `main`

## Versioning

| Version | Entry | Description |
|---------|-------|-------------|
| 1.0.0   | 001   | Initial site + Montana/Hawaii Citizens United snapshot |
