"""
Generate data/cursor-implementation-package.json — Build #101.
Cursor Implementation Package — 50 executable implementation steps v1.0.
"""
import json
from datetime import date
from pathlib import Path

root = Path(__file__).resolve().parents[1]
today = '2026-07-09'
completion_target_date = '2027-01-01'
completion_target = date(2027, 1, 1)
today_date = date(2026, 7, 9)
days_remaining = max((completion_target - today_date).days, 0)


def load_json(path):
    if path.exists():
        with open(path, encoding='utf-8') as f:
            return json.load(f)
    return {}


mc = load_json(root / 'data/mission-control.json')
ex = mc.get('executive', {})

# Honest operational metrics
steps_implemented = 0
steps_documented = 1  # IMP-01 Technical Constitution
sprint_zero_started = False
cursor_scripts_consolidated = False
qa_gates_passed = 0

BANDS = [
    {
        'id': 'BAND-A',
        'letter': 'A',
        'title': 'Foundation',
        'steps_range': '1–10',
        'focus': 'Repo, stack, deployment, environment, folder structure',
    },
    {
        'id': 'BAND-B',
        'letter': 'B',
        'title': 'Presentation',
        'steps_range': '11–20',
        'focus': 'Routes, layouts, design system, component registry',
    },
    {
        'id': 'BAND-C',
        'letter': 'C',
        'title': 'Data & Access',
        'steps_range': '21–30',
        'focus': 'Data model, database schema, forms, auth, admin permissions',
    },
    {
        'id': 'BAND-D',
        'letter': 'D',
        'title': 'Operations',
        'steps_range': '31–40',
        'focus': 'Mission Control, dashboards, progress tracking, county/city goals',
    },
    {
        'id': 'BAND-E',
        'letter': 'E',
        'title': 'Knowledge & Launch',
        'steps_range': '41–50',
        'focus': 'Content system, evidence registry, Cursor scripts, MVP, QA, launch',
    },
]

IMPLEMENTATION_STEPS = [
    # Band A — 1–10
    {
        'number': 1, 'id': 'IMP-01', 'band': 'A',
        'package_label': 'Implementation Package 1 of 50',
        'title': 'Master Technical Constitution & Build Doctrine',
        'summary': 'Technical constitution for every developer, AI system, Cursor session, and contributor — every line of code aligns here',
        'deliverables': [
            'docs/IMPLEMENTATION_PACKAGE_01_TECHNICAL_CONSTITUTION.md',
            'Technical Constitution', 'Development Doctrine', 'Platform Philosophy',
            'Build Standards', 'Architectural Rules', 'AI Rules', 'Documentation Rules',
            'Mission Control Rules', 'Volunteer-First Standards', 'Arkansas-First Standards',
        ],
        'acceptance_criteria': [
            'Prime Directive documented: one integrated institution',
            'Three-question feature test: why / who / how',
            'Four-layer architecture defined (Experience, Application, Knowledge, Institution)',
            'Build order rule: Design through Acceptance — nothing skips sequence',
            'Platform, technical, user, MC-first, AI-first, knowledge-first principles documented',
            'Governing principle: Build once, correctly, for decades',
        ],
        'source_blueprints': [
            '/docs/MASTER_TECHNICAL_ARCHITECTURE.md',
            '/docs/MASTER_FOUNDING_CHARTER.md',
            '/docs/MASTER_INSTITUTIONAL_MANIFESTO.md',
            '/docs/CURSOR_MASTER_BUILD_PROMPT.md',
        ],
        'constitution': '/docs/IMPLEMENTATION_PACKAGE_01_TECHNICAL_CONSTITUTION.md',
        'status': 'documented',
        'documented_date': today,
    },
    {
        'number': 2, 'id': 'IMP-02', 'band': 'A',
        'package_label': 'Implementation Package 2 of 50',
        'title': 'Master Technical Architecture & Repository Blueprint',
        'summary': 'Repository structure, application architecture, technology stack, folder organization, service boundaries, naming conventions, deployment topology',
        'deliverables': [
            'docs/MIGRATION_PLAN.md', 'docs/REPO_AUDIT.md', 'docs/STACK.md',
            'src/README.md', 'prisma/README.md', 'tests/README.md',
        ],
        'acceptance_criteria': [
            'Current tree diffed against data/repository-blueprint.json target_root_structure',
            'Migration strategy chosen with rollback plan (strangler-fig vs Next.js monorepo)',
            'Stack locked: Next.js, TypeScript, Tailwind, Neon, Prisma, Netlify',
            'Target folders scaffolded without breaking static Netlify deploy',
            'Safe-edit zones listed for volunteer contributors',
        ],
        'source_blueprints': [
            '/data/repository-blueprint.json',
            '/data/technical-architecture.json',
            '/docs/MASTER_TECHNICAL_ARCHITECTURE.md',
            '/docs/REPOSITORY_ARCHITECTURE.md',
        ],
        'status': 'specified',
    },
    {
        'number': 3, 'id': 'IMP-03', 'band': 'A',
        'title': 'Service boundaries and deployment topology',
        'summary': 'Service boundaries, API surface, and deployment units per technical architecture',
        'deliverables': ['docs/SERVICE_BOUNDARIES.md', 'docs/DEPLOYMENT_TOPOLOGY.md'],
        'acceptance_criteria': [
            'Public site, MC, API, and admin deployment units defined',
            'Service boundaries map to four-layer architecture (IMP-01)',
            'Aligns with data/technical-architecture.json deployment section',
        ],
        'source_blueprints': ['/data/technical-architecture.json', '/docs/IMPLEMENTATION_PACKAGE_01_TECHNICAL_CONSTITUTION.md'],
        'status': 'specified',
    },
    {
        'number': 4, 'id': 'IMP-04', 'band': 'A',
        'title': 'Environment and secrets matrix',
        'summary': '.env.example for Neon, auth, Netlify, and local dev',
        'deliverables': ['.env.example', 'docs/ENVIRONMENT.md'],
        'acceptance_criteria': [
            'All required env vars documented with no secrets committed',
            'Netlify env var mapping documented',
            'Local setup steps reproducible in under 15 minutes',
        ],
        'source_blueprints': ['/data/technical-architecture.json'],
        'status': 'specified',
    },
    {
        'number': 5, 'id': 'IMP-05', 'band': 'A',
        'title': 'Netlify hybrid deployment config',
        'summary': 'Prepare netlify.toml for static + future Next.js/API routes',
        'deliverables': ['netlify.toml', 'docs/DEPLOYMENT.md'],
        'acceptance_criteria': [
            'Current static publish path unchanged',
            'Preview deploys documented for develop branch',
            'Redirect rules preserved from existing netlify.toml',
        ],
        'source_blueprints': ['/netlify.toml', '/data/technical-architecture.json'],
        'status': 'specified',
    },
    {
        'number': 6, 'id': 'IMP-06', 'band': 'A',
        'title': 'GitHub branch and protection model',
        'summary': 'main + develop + feature/* + content/* branch workflow',
        'deliverables': ['docs/GIT_WORKFLOW.md'],
        'acceptance_criteria': [
            'Branch purposes match repository-blueprint branch_structure',
            'PR review requirement documented for main',
            'Content-only branch workflow for volunteers',
        ],
        'source_blueprints': ['/data/repository-blueprint.json'],
        'status': 'specified',
    },
    {
        'number': 7, 'id': 'IMP-07', 'band': 'A',
        'title': 'CI pipeline gates',
        'summary': 'Lint, typecheck, build, test jobs on PR',
        'deliverables': ['.github/workflows/ci.yml'],
        'acceptance_criteria': [
            'CI runs on pull_request to main and develop',
            'Fails on lint/type errors when TS introduced',
            'Documents how to run checks locally',
        ],
        'source_blueprints': ['/data/technical-architecture.json'],
        'status': 'specified',
    },
    {
        'number': 8, 'id': 'IMP-08', 'band': 'A',
        'title': 'Package scripts and tooling',
        'summary': 'dev, build, db:migrate, gen:* npm scripts',
        'deliverables': ['package.json scripts section', 'docs/SCRIPTS.md'],
        'acceptance_criteria': [
            'npm run dev documented (static or Next when ready)',
            'Generator scripts invocable via npm run gen:all pattern',
            'Node version pinned in .nvmrc or engines field',
        ],
        'source_blueprints': ['/package.json', '/scripts/'],
        'status': 'specified',
    },
    {
        'number': 9, 'id': 'IMP-09', 'band': 'A',
        'title': 'Contributor onboarding doc',
        'summary': 'CONTRIBUTING.md — what volunteers may edit safely',
        'deliverables': ['CONTRIBUTING.md'],
        'acceptance_criteria': [
            'Links to CURSOR_MASTER_BUILD_PROMPT.md',
            'Separates content/* from engineering feature/* paths',
            'Code of conduct and evidence standards referenced',
        ],
        'source_blueprints': ['/data/repository-blueprint.json', '/docs/CURSOR_MASTER_BUILD_PROMPT.md'],
        'status': 'specified',
    },
    {
        'number': 10, 'id': 'IMP-10', 'band': 'A',
        'title': 'Sprint Zero exit checklist',
        'summary': 'Gate before Band B — repo ready for first code slice',
        'deliverables': ['docs/SPRINT_ZERO_CHECKLIST.md'],
        'acceptance_criteria': [
            'IMP-01 through IMP-09 acceptance criteria verified',
            'One successful Netlify preview deploy from develop',
            'Executive sign-off field in checklist (manual)',
        ],
        'source_blueprints': ['/data/cursor-implementation-package.json'],
        'status': 'specified',
    },
    # Band B — 11–20
    {
        'number': 11, 'id': 'IMP-11', 'band': 'B',
        'title': 'Unified route manifest',
        'summary': 'Export public / MC / API / auth-gated routes from route-registry',
        'deliverables': ['data/route-manifest.json', 'docs/ROUTE_MANIFEST.md'],
        'acceptance_criteria': [
            'Every live route from data/route-registry.json categorized',
            'launch_priorities must_launch vs stub_ok vs later preserved',
            'Each route has purpose: educate | trust | civic | mission_control',
        ],
        'source_blueprints': ['/data/route-registry.json', '/mission-control/routes.html'],
        'status': 'specified',
    },
    {
        'number': 12, 'id': 'IMP-12', 'band': 'B',
        'title': 'App Router layout hierarchy',
        'summary': 'Root, public, mission-control, admin layout shells',
        'deliverables': ['src/app/layout.tsx (when Next adopted)', 'docs/LAYOUTS.md'],
        'acceptance_criteria': [
            'Layout tree documented matching UX architecture visitor zones',
            'Static js/layout.js behavior preserved during migration',
            'Breadcrumb pattern consistent across zones',
        ],
        'source_blueprints': ['/data/ux-architecture.json', '/js/layout.js'],
        'status': 'specified',
    },
    {
        'number': 13, 'id': 'IMP-13', 'band': 'B',
        'title': 'Design tokens port',
        'summary': 'design-system.json → CSS variables and Tailwind config',
        'deliverables': ['src/styles/tokens.css', 'tailwind.config.ts', 'docs/DESIGN_TOKENS.md'],
        'acceptance_criteria': [
            'Colors, typography, spacing match /design-system/ showcase',
            'Existing css/styles.css tokens mapped or aliased',
            'No visual regression on homepage and MC home',
        ],
        'source_blueprints': ['/data/design-system.json', '/design-system/'],
        'status': 'specified',
    },
    {
        'number': 14, 'id': 'IMP-14', 'band': 'B',
        'title': 'Core layout components',
        'summary': 'SiteHeader, SiteFooter, Breadcrumb — COMP layout family',
        'deliverables': ['src/components/layout/SiteHeader.tsx', 'SiteFooter.tsx', 'Breadcrumb.tsx'],
        'acceptance_criteria': [
            'Match current site-header and site-footer behavior',
            'data-site-version badge reads from site.json',
            'Mobile nav accessible (keyboard + aria)',
        ],
        'source_blueprints': ['/js/layout.js', '/data/site.json'],
        'status': 'specified',
    },
    {
        'number': 15, 'id': 'IMP-15', 'band': 'B',
        'title': 'Mission Control shell layout',
        'summary': 'MC sidebar, mc-body, mc-header, mc-stat grid',
        'deliverables': ['src/components/mc/McShell.tsx', 'docs/MC_LAYOUT.md'],
        'acceptance_criteria': [
            'Matches mission-control.css patterns',
            'Breadcrumb mc-breadcrumb pattern preserved',
            'initDevConsole hook point documented',
        ],
        'source_blueprints': ['/css/mission-control.css', '/js/mission-control.js'],
        'status': 'specified',
    },
    {
        'number': 16, 'id': 'IMP-16', 'band': 'B',
        'title': 'Component registry COMP-* index',
        'summary': 'Machine-readable component specs with IDs, props, routes',
        'deliverables': ['data/component-specs.json', 'mission-control/components.html sync'],
        'acceptance_criteria': [
            'Every ds-* and mc-* pattern assigned COMP-* ID',
            'Props and states documented for top 10 components',
            'Links to design-system showcase pages',
        ],
        'source_blueprints': ['/mission-control/components.html', '/data/design-system.json'],
        'status': 'specified',
    },
    {
        'number': 17, 'id': 'IMP-17', 'band': 'B',
        'title': 'COMP-01–05 primitive specs',
        'summary': 'Button, Card, Badge, Stat, Table components',
        'deliverables': ['src/components/ui/Button.tsx', 'Card.tsx', 'Badge.tsx', 'Stat.tsx', 'Table.tsx'],
        'acceptance_criteria': [
            'Each COMP has props table in component-specs.json',
            'Used in at least one MC dashboard page as proof',
            'Variant styles match design-system',
        ],
        'source_blueprints': ['/data/component-specs.json'],
        'status': 'specified',
    },
    {
        'number': 18, 'id': 'IMP-18', 'band': 'B',
        'title': 'COMP-06–10 interactive specs',
        'summary': 'Form field, Modal, Alert, ProgressBar, InlineLink',
        'deliverables': ['src/components/ui/FormField.tsx', 'Modal.tsx', 'Alert.tsx', 'ProgressBar.tsx'],
        'acceptance_criteria': [
            'Form fields work with Netlify Forms adapter (step 25)',
            'Progress bar reads value/max/note like MC progress_bars',
            'Focus trap on modal documented',
        ],
        'source_blueprints': ['/data/component-specs.json', '/data/mission-control.json'],
        'status': 'specified',
    },
    {
        'number': 19, 'id': 'IMP-19', 'band': 'B',
        'title': 'Page templates',
        'summary': 'Hall, entry-card, mc-dashboard, build-log templates',
        'deliverables': ['src/templates/HallPage.tsx', 'McDashboard.tsx', 'BuildLog.tsx'],
        'acceptance_criteria': [
            'Hall template matches education.css hall-header pattern',
            'Build log template renders builds/NNN-*.md metadata',
            'Entry-card used on builds/index.html equivalent',
        ],
        'source_blueprints': ['/css/education.css', '/builds/index.html'],
        'status': 'specified',
    },
    {
        'number': 20, 'id': 'IMP-20', 'band': 'B',
        'title': 'Accessibility baseline audit',
        'summary': 'WCAG 2.1 AA checklist per layout and template',
        'deliverables': ['docs/ACCESSIBILITY_AUDIT.md', 'tests/a11y/README.md'],
        'acceptance_criteria': [
            'Homepage, Start Here, one hall, MC home audited',
            'Issues triaged must-fix vs post-MVP',
            'Color contrast verified against design tokens',
        ],
        'source_blueprints': ['/data/launch-strategy.json'],
        'status': 'specified',
    },
    # Band C — 21–30
    {
        'number': 21, 'id': 'IMP-21', 'band': 'C',
        'title': 'Prisma schema core entities',
        'summary': 'people, organizations, counties from database-schema.json',
        'deliverables': ['prisma/schema.prisma (Person, Organization, County)'],
        'acceptance_criteria': [
            'Fields match data/database-schema.json entity definitions',
            'M:N person_organizations join table included',
            'Privacy principle documented on PII fields',
        ],
        'source_blueprints': ['/data/database-schema.json'],
        'status': 'specified',
    },
    {
        'number': 22, 'id': 'IMP-22', 'band': 'C',
        'title': 'Prisma schema knowledge entities',
        'summary': 'sources, facts, educational_resources, events, signups',
        'deliverables': ['prisma/schema.prisma extensions'],
        'acceptance_criteria': [
            'Source → Fact relationship matches evidence ledger model',
            'signup and referral entities support county attribution',
            'mc_build_record entity for build registry sync',
        ],
        'source_blueprints': ['/data/database-schema.json', '/data/evidence-registry.json'],
        'status': 'specified',
    },
    {
        'number': 23, 'id': 'IMP-23', 'band': 'C',
        'title': 'Neon provisioning and migrations',
        'summary': 'Neon project, connection string, prisma migrate workflow',
        'deliverables': ['docs/DATABASE_SETUP.md', 'prisma/migrations/'],
        'acceptance_criteria': [
            'prisma migrate dev succeeds locally',
            'Neon branch strategy documented (main/preview)',
            'No production credentials in repo',
        ],
        'source_blueprints': ['/data/technical-architecture.json'],
        'status': 'specified',
    },
    {
        'number': 24, 'id': 'IMP-24', 'band': 'C',
        'title': 'Seed script from JSON registries',
        'summary': 'Seed 75 counties, site metadata, pilot organizations',
        'deliverables': ['prisma/seed.ts', 'data/arkansas-counties.json import'],
        'acceptance_criteria': [
            '75 Arkansas counties seeded',
            'Seed idempotent (safe to re-run)',
            'Documented in DATABASE_SETUP.md',
        ],
        'source_blueprints': ['/data/arkansas-counties.json', '/data/site.json'],
        'status': 'specified',
    },
    {
        'number': 25, 'id': 'IMP-25', 'band': 'C',
        'title': 'Netlify Forms ingestion adapter',
        'summary': 'Design webhook or manual import from Netlify Forms to people/signups',
        'deliverables': ['docs/FORMS_INGESTION.md', 'scripts/import-netlify-forms.py'],
        'acceptance_criteria': [
            'Join/coalition form fields mapped to schema',
            'County/city captured on signup',
            'PII handling documented',
        ],
        'source_blueprints': ['/data/contact-intelligence.json'],
        'status': 'specified',
    },
    {
        'number': 26, 'id': 'IMP-26', 'band': 'C',
        'title': 'Auth provider and admin login shell',
        'summary': 'Email + Google OAuth for Mission Control admins',
        'deliverables': ['src/app/admin/login/', 'docs/AUTH.md'],
        'acceptance_criteria': [
            'Public education pages remain unauthenticated',
            'Session stored securely (httpOnly cookies)',
            'Aligns with technical-architecture auth section',
        ],
        'source_blueprints': ['/data/technical-architecture.json'],
        'status': 'specified',
    },
    {
        'number': 27, 'id': 'IMP-27', 'band': 'C',
        'title': 'Role model definition',
        'summary': 'public, volunteer, editor, education_leader, admin, executive roles',
        'deliverables': ['prisma/schema.prisma Role enum', 'docs/Roles.md'],
        'acceptance_criteria': [
            'Roles map to ACOS 2.0 six user roles where applicable',
            'Default role is public for anonymous visitors',
            'Role assignment manual for MVP (no self-serve executive)',
        ],
        'source_blueprints': ['/data/arkansas-civic-operating-system.json'],
        'status': 'specified',
    },
    {
        'number': 28, 'id': 'IMP-28', 'band': 'C',
        'title': 'Permission middleware',
        'summary': 'Protect /mission-control/* write paths and /admin/*',
        'deliverables': ['src/middleware.ts', 'docs/PERMISSIONS.md'],
        'acceptance_criteria': [
            'Read-only MC dashboards public or role-gated per decision doc',
            'Write operations require editor+ role',
            '403 page matches site design',
        ],
        'source_blueprints': ['/data/governance-constitution.json'],
        'status': 'specified',
    },
    {
        'number': 29, 'id': 'IMP-29', 'band': 'C',
        'title': 'Volunteer signup flow',
        'summary': 'Join form → people + county + signup_source',
        'deliverables': ['join/ form wired to DB', 'docs/VOLUNTEER_SIGNUP.md'],
        'acceptance_criteria': [
            'Signup creates Person record with county attribution',
            'Confirmation message without exposing PII',
            'Matches contact-intelligence signup_source taxonomy',
        ],
        'source_blueprints': ['/join/', '/data/contact-intelligence.json'],
        'status': 'specified',
    },
    {
        'number': 30, 'id': 'IMP-30', 'band': 'C',
        'title': 'Coalition partner intake',
        'summary': 'Coalition form → organizations + coalition_sign_on',
        'deliverables': ['coalition/ intake wired to DB', 'docs/COALITION_INTAKE.md'],
        'acceptance_criteria': [
            'Organization record created with public fields only',
            'Partner approval workflow state: pending → active',
            'Aligns with coalition-network.json fields',
        ],
        'source_blueprints': ['/coalition/', '/data/coalition-network.json'],
        'status': 'specified',
    },
    # Band D — 31–40
    {
        'number': 31, 'id': 'IMP-31', 'band': 'D',
        'title': 'MC executive dashboard API',
        'summary': 'Serve executive stats from DB with JSON fallback',
        'deliverables': ['src/api/mc/executive.ts', 'mission-control/index data wiring'],
        'acceptance_criteria': [
            'Reads data/mission-control.json when DB empty (honest fallback)',
            'Switch to DB when mc_build_record populated',
            'Version and build number from site.json',
        ],
        'source_blueprints': ['/data/mission-control.json', '/js/mission-control.js'],
        'status': 'specified',
    },
    {
        'number': 32, 'id': 'IMP-32', 'band': 'D',
        'title': 'Launch certification progress bars',
        'summary': 'Wire 12 certification domains (#97) to live checklist state',
        'deliverables': ['src/components/mc/CertificationBars.tsx'],
        'acceptance_criteria': [
            'Domains from institutional-launch-certification.json rendered',
            'Honest 0/12 certified until manually verified',
            'Links to domain detail pages',
        ],
        'source_blueprints': ['/data/institutional-launch-certification.json'],
        'status': 'specified',
    },
    {
        'number': 33, 'id': 'IMP-33', 'band': 'D',
        'title': 'Build registry sync',
        'summary': 'Sync builds/ markdown + git tags to mc_build_record',
        'deliverables': ['scripts/sync-build-registry.py', 'docs/BUILD_REGISTRY_SYNC.md'],
        'acceptance_criteria': [
            'builds/BUILDS.md entries match DB records after sync',
            'Build number, version, status, completed date captured',
            'Runnable via npm run sync:builds',
        ],
        'source_blueprints': ['/builds/BUILDS.md', '/data/mission-control.json'],
        'status': 'specified',
    },
    {
        'number': 34, 'id': 'IMP-34', 'band': 'D',
        'title': 'County dashboard template',
        'summary': 'One pilot county dashboard → template for 75',
        'deliverables': ['arkansas/counties/[slug].html or dynamic route', 'docs/COUNTY_DASHBOARD.md'],
        'acceptance_criteria': [
            'Shows volunteers, events, connected % for pilot county',
            'Template parameterized by county id',
            'Data from county OS blueprint (#77)',
        ],
        'source_blueprints': ['/data/arkansas-county-operating-system.json', '/data/arkansas-counties.json'],
        'status': 'specified',
    },
    {
        'number': 35, 'id': 'IMP-35', 'band': 'D',
        'title': 'City dashboard template',
        'summary': '250 largest cities seeded with dashboard stub',
        'deliverables': ['data/arkansas-cities.json wiring', 'docs/CITY_DASHBOARD.md'],
        'acceptance_criteria': [
            'City pages link from county dashboard',
            'Population rank and county parent shown',
            '15% connected voter formula documented (even if 0%)',
        ],
        'source_blueprints': ['/data/arkansas-city-operating-system.json', '/data/arkansas-cities.json'],
        'status': 'specified',
    },
    {
        'number': 36, 'id': 'IMP-36', 'band': 'D',
        'title': 'Connected citizen percentage calculator',
        'summary': 'Formula: connected / registered voters per county and city',
        'deliverables': ['src/lib/metrics/connected-pct.ts', 'docs/METRICS.md'],
        'acceptance_criteria': [
            '15% goal from founding charter displayed honestly',
            'Registered voter denominator source documented',
            'Returns null when denominator unknown (not fake %)',
        ],
        'source_blueprints': ['/data/founding-charter.json', '/data/arkansas-civic-reach-participation.json'],
        'status': 'specified',
    },
    {
        'number': 37, 'id': 'IMP-37', 'band': 'D',
        'title': 'January 2027 countdown component',
        'summary': 'Live days-remaining to 2027-01-01 on MC executive home',
        'deliverables': ['src/components/mc/Countdown2027.tsx'],
        'acceptance_criteria': [
            'Uses completion_target_date from registries',
            'Updates daily without manual edit',
            'Copy: founding build complete, mission continues',
        ],
        'source_blueprints': ['/data/founding-charter.json', '/data/mission-control.json'],
        'status': 'specified',
    },
    {
        'number': 38, 'id': 'IMP-38', 'band': 'D',
        'title': 'Executive War Room view',
        'summary': 'Briefing panel: what_built, blocked, ready_public, next',
        'deliverables': ['mission-control/war-room.html', 'initWarRoom() in mission-control.js'],
        'acceptance_criteria': [
            'Reads mc.briefing from mission-control.json',
            'Links to implementation package step progress',
            'Blocked items honest (not hidden)',
        ],
        'source_blueprints': ['/data/mission-control.json'],
        'status': 'specified',
    },
    {
        'number': 39, 'id': 'IMP-39', 'band': 'D',
        'title': 'Education Leader roster by county',
        'summary': 'List Education Leaders with county assignment',
        'deliverables': ['mission-control/education-leaders.html or MC section'],
        'acceptance_criteria': [
            'Filter by county',
            '0 leaders shown honestly when empty',
            'Links to education academy blueprint',
        ],
        'source_blueprints': ['/data/education-academy.json', '/data/database-schema.json'],
        'status': 'specified',
    },
    {
        'number': 40, 'id': 'IMP-40', 'band': 'D',
        'title': 'Statewide goals dashboard',
        'summary': '200K Arkansans, 75 counties, coalition count, academy status',
        'deliverables': ['src/components/mc/StatewideGoals.tsx'],
        'acceptance_criteria': [
            'All January 2027 goals from charter displayed',
            'Current values from DB or honest 0',
            'Goal definitions link to founding-charter.json',
        ],
        'source_blueprints': ['/data/founding-charter.json', '/data/master-launch-plan.json'],
        'status': 'specified',
    },
    # Band E — 41–50
    {
        'number': 41, 'id': 'IMP-41', 'band': 'E',
        'title': 'Content model and migration path',
        'summary': 'Article, lesson, hall section schema + MD/HTML migration plan',
        'deliverables': ['docs/CONTENT_MODEL.md', 'prisma ContentArticle model'],
        'acceptance_criteria': [
            'Existing content/ and halls/ mapped to model',
            'Frontmatter spec for markdown content',
            'URL slugs preserved for SEO',
        ],
        'source_blueprints': ['/content/', '/data/content-production-matrix.json'],
        'status': 'specified',
    },
    {
        'number': 42, 'id': 'IMP-42', 'band': 'E',
        'title': 'Evidence ledger write path',
        'summary': 'Source → Fact → citation link creation in MC',
        'deliverables': ['mission-control/evidence-ledger write UI spec', 'docs/EVIDENCE_WORKFLOW.md'],
        'acceptance_criteria': [
            'Every fact requires source_id',
            'Verification status: unverified | verified | disputed',
            'Matches evidence-registry.json schema',
        ],
        'source_blueprints': ['/data/evidence-registry.json', '/docs/MASTER_EVIDENCE_LEDGER.md'],
        'status': 'specified',
    },
    {
        'number': 43, 'id': 'IMP-43', 'band': 'E',
        'title': 'Source library browse and verify UI',
        'summary': 'Public /library/ with filter, verify badge, link to claims',
        'deliverables': ['library/ enhanced browse', 'COMP SourceCard'],
        'acceptance_criteria': [
            'Sources searchable by title, author, year',
            'Verify action requires editor role',
            'Citation export format documented',
        ],
        'source_blueprints': ['/library/', '/data/evidence-registry.json'],
        'status': 'specified',
    },
    {
        'number': 44, 'id': 'IMP-44', 'band': 'E',
        'title': 'Research workflow states',
        'summary': 'draft → review → approved → published pipeline',
        'deliverables': ['docs/RESEARCH_WORKFLOW.md', 'prisma ContentStatus enum'],
        'acceptance_criteria': [
            'State transitions logged with actor and timestamp',
            'Only approved content publishable to public site',
            'Matches research-methodology.json stages',
        ],
        'source_blueprints': ['/data/research-methodology.json'],
        'status': 'specified',
    },
    {
        'number': 45, 'id': 'IMP-45', 'band': 'E',
        'title': 'MC publishing workflow',
        'summary': 'Editor submit → approver publish → revision history',
        'deliverables': ['docs/PUBLISHING_WORKFLOW.md', 'MC publish UI slice'],
        'acceptance_criteria': [
            'Revision history stored per content item',
            'Rollback to prior version supported',
            'No publish without citation check for factual claims',
        ],
        'source_blueprints': ['/docs/MASTER_TECHNICAL_ARCHITECTURE.md'],
        'status': 'specified',
    },
    {
        'number': 46, 'id': 'IMP-46', 'band': 'E',
        'title': 'Citation component on public pages',
        'summary': 'Inline citation linking to source library for factual claims',
        'deliverables': ['src/components/content/Citation.tsx', 'docs/CITATION_STANDARD.md'],
        'acceptance_criteria': [
            'Every numbered claim links to source record',
            'Missing citation blocks publish (lint rule or manual gate)',
            'Accessible footnote pattern',
        ],
        'source_blueprints': ['/docs/MASTER_EVIDENCE_LEDGER.md', '/data/facts-registry.json'],
        'status': 'specified',
    },
    {
        'number': 47, 'id': 'IMP-47', 'band': 'E',
        'title': 'Claims registry DB sync',
        'summary': 'Sync facts-registry.json ↔ facts table',
        'deliverables': ['scripts/sync-claims-registry.py', 'docs/CLAIMS_SYNC.md'],
        'acceptance_criteria': [
            'Bidirectional or single-source-of-truth documented',
            'Claim id stable across syncs',
            'Conflicts surfaced in MC queue',
        ],
        'source_blueprints': ['/data/facts-registry.json', '/data/database-schema.json'],
        'status': 'specified',
    },
    {
        'number': 48, 'id': 'IMP-48', 'band': 'E',
        'title': 'Content search MVP',
        'summary': 'Static search index → DB full-text for articles and sources',
        'deliverables': ['src/app/search/', 'docs/SEARCH.md'],
        'acceptance_criteria': [
            'Search covers must_launch routes minimum',
            'Results show content type and hall',
            'Sub-500ms on static index; DB path documented for scale',
        ],
        'source_blueprints': ['/data/route-registry.json', '/data/technical-architecture.json'],
        'status': 'specified',
    },
    {
        'number': 49, 'id': 'IMP-49', 'band': 'E',
        'title': 'Cursor build scripts consolidation',
        'summary': 'gen:* pipeline, sync:* scripts, npm run gen:all',
        'deliverables': ['scripts/gen-all.py', 'package.json gen:all', 'docs/GENERATORS.md'],
        'acceptance_criteria': [
            'All scripts/gen-*.py invocable from one entry point',
            'Generator output overwrites JSON atomically',
            'CI verifies JSON valid after gen:all',
        ],
        'source_blueprints': ['/scripts/'],
        'status': 'specified',
    },
    {
        'number': 50, 'id': 'IMP-50', 'band': 'E',
        'title': 'MVP acceptance, QA gates, and launch checklist',
        'summary': 'End-to-end MVP sign-off against Launch Certification (#97) and Charter goals',
        'deliverables': ['docs/MVP_ACCEPTANCE.md', 'docs/LAUNCH_CHECKLIST.md', 'docs/QA_GATES.md'],
        'acceptance_criteria': [
            'All IMP-01–49 acceptance criteria traceable in checklist',
            '12 certification domains have pass/fail with evidence links',
            'Public launch readiness score computed honestly from checklist',
            'Executive sign-off before January 2027 public launch recommendation',
        ],
        'source_blueprints': [
            '/data/institutional-launch-certification.json',
            '/data/founding-charter.json',
            '/docs/CURSOR_MASTER_BUILD_PROMPT.md',
        ],
        'status': 'specified',
    },
]

MVP_SCOPE = {
    'title': 'January 2027 MVP Scope',
    'in_scope': [
        'Public education site (halls + search MVP)',
        'Mission Control executive + certification progress',
        'Volunteer signup with county/city attribution',
        'Coalition partner registry (basic CRM)',
        'County dashboard template (1 pilot → 75)',
        'City dashboard stubs (250 largest)',
        'Evidence ledger read path + citations on public pages',
        'Content publish workflow (draft → review → publish)',
        'January 2027 countdown and statewide goals dashboard',
        'Implementation package step tracking',
    ],
    'out_of_scope': [
        'Full ACOS 2.0 personal workspace (#96)',
        'Autonomous AI institution (#91)',
        '200K relational graph at scale',
        'Full 250-city automation without pilot validation',
        'Public official sharing automation',
        'Ballot initiative lab operational',
    ],
}

PACKAGE_DASHBOARD_INDICATORS = [
    {'id': 'CIP-D01', 'indicator': 'Steps specified', 'current': len(IMPLEMENTATION_STEPS), 'status': 'partial'},
    {'id': 'CIP-D02', 'indicator': 'Steps documented', 'current': steps_documented, 'status': 'partial'},
    {'id': 'CIP-D03', 'indicator': 'Steps implemented', 'current': steps_implemented, 'status': 'planned'},
    {'id': 'CIP-D04', 'indicator': 'Technical Constitution (IMP-01)', 'current': 'Documented', 'status': 'partial'},
    {'id': 'CIP-D05', 'indicator': 'Sprint Zero started', 'current': 'Yes' if sprint_zero_started else 'No', 'status': 'planned'},
    {'id': 'CIP-D06', 'indicator': 'QA gates passed', 'current': qa_gates_passed, 'status': 'planned'},
]

implementation_package_readiness = min(
    72,
    14
    + len(IMPLEMENTATION_STEPS) // 2
    + len(BANDS) * 2
    + len(MVP_SCOPE['in_scope']) // 2
    + len(PACKAGE_DASHBOARD_INDICATORS) // 2
    + steps_documented * 2
    + (4 if steps_implemented else 0)
    + (2 if sprint_zero_started else 0),
)

out = {
    'version': '1.0',
    'build': 101,
    'updated': today,
    'completion_target_date': completion_target_date,
    'title': 'Cursor Implementation Package v1.0',
    'subtitle': '50 Executable Implementation Steps',
    'tagline': 'From Blueprint to Code — Master Build Bible v2.0',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/cursor-implementation-package.html',
    'constitution': '/docs/MASTER_CURSOR_IMPLEMENTATION_PACKAGE.md',
    'cursor_master_prompt': '/docs/CURSOR_MASTER_BUILD_PROMPT.md',
    'purpose': (
        'Build #101 turns the 100-build institutional blueprint into ordered, file-level coding '
        'instructions. Fifty steps across five bands — repo through launch — each with deliverables, '
        'acceptance criteria, and source blueprint links. No abstract planning; build-ready slices only.'
    ),
    'governing_principle': (
        'Build once. Build correctly. Build for decades. '
        'Does this implementation step help an Arkansan understand self-government through a '
        'working, trustworthy platform? If yes, ship the slice. If no, defer.'
    ),
    'technical_constitution': {
        'title': 'Master Technical Constitution & Build Doctrine',
        'package': 'Implementation Package 1 of 50',
        'route': '/docs/IMPLEMENTATION_PACKAGE_01_TECHNICAL_CONSTITUTION.md',
        'status': 'documented',
        'documented_date': today,
        'prime_directive': 'Build one integrated institution — one login, one design language, one data model, one knowledge platform, one AI ecosystem, one Mission Control, one Arkansas.',
        'feature_test': ['Why does this exist? (Mission)', 'Who does it serve? (User)', 'How does it strengthen the institution? (System)'],
        'platform_principles': [
            'Volunteer-first', 'Mobile-first', 'Accessibility-first', 'Research-first', 'Evidence-first',
            'AI-assisted', 'Mission-Control-driven', 'Arkansas-focused', 'Future-ready',
        ],
        'four_layer_architecture': [
            {'layer': 1, 'name': 'Experience', 'scope': 'User Interface'},
            {'layer': 2, 'name': 'Application', 'scope': 'Business Logic'},
            {'layer': 3, 'name': 'Knowledge', 'scope': 'Data & Documents'},
            {'layer': 4, 'name': 'Institution', 'scope': 'Mission Control & Governance'},
        ],
        'build_order': [
            'Design', 'Data', 'API', 'Business Logic', 'User Interface',
            'Mission Control', 'AI', 'Testing', 'Documentation', 'Acceptance',
        ],
        'next_package': {
            'number': 2,
            'id': 'IMP-02',
            'title': 'Master Technical Architecture & Repository Blueprint',
        },
    },
    'supersedes': {
        'build': 50,
        'title': 'Master Build Bible v1.0',
        'note': 'Build Bible indexed blueprints; this package orders executable engineering work.',
        'route': '/mission-control/build-bible.html',
    },
    'bands': BANDS,
    'implementation_steps': IMPLEMENTATION_STEPS,
    'implementation_steps_total': len(IMPLEMENTATION_STEPS),
    'mvp_scope': MVP_SCOPE,
    'january_2027_targets': {
        'counties': 75,
        'cities': 250,
        'connected_voter_pct_per_county_city': 15,
        'arkansans_connected_goal': 200000,
        'education_leaders_statewide': True,
        'coalition_partners_onboarded': True,
        'mission_control_operational': True,
        'days_remaining': days_remaining,
    },
    'package_dashboard': {
        'title': 'Implementation Package Dashboard',
        'indicators': PACKAGE_DASHBOARD_INDICATORS,
        'live': False,
        'status': 'planned',
    },
    'integration': {
        'chain': (
            'Founding Charter (#100) → Implementation Package (#101) → Sprint Zero (IMP-10) → '
            'Code Slices (IMP-01–50) → War Room (#102) → Launch Certification (#97)'
        ),
        'source_blueprints': [
            {'system': 'Build Bible (#50)', 'route': '/data/build-bible.json'},
            {'system': 'Repository (#21)', 'route': '/data/repository-blueprint.json'},
            {'system': 'Database Schema (#22)', 'route': '/data/database-schema.json'},
            {'system': 'Route Registry (#16)', 'route': '/data/route-registry.json'},
            {'system': 'Technical Architecture (#53)', 'route': '/data/technical-architecture.json'},
            {'system': 'Founding Charter (#100)', 'route': '/data/founding-charter.json'},
            {'system': 'Launch Certification (#97)', 'route': '/data/institutional-launch-certification.json'},
        ],
    },
    'summary': {
        'completion_target_date': completion_target_date,
        'days_remaining': days_remaining,
        'implementation_package_readiness_pct': implementation_package_readiness,
        'steps_total': len(IMPLEMENTATION_STEPS),
        'steps_documented': steps_documented,
        'steps_implemented': steps_implemented,
        'steps_remaining': len(IMPLEMENTATION_STEPS) - steps_implemented,
        'bands_total': len(BANDS),
        'bands_complete': 0,
        'sprint_zero_started': sprint_zero_started,
        'cursor_master_prompt_ready': True,
        'mvp_in_scope_count': len(MVP_SCOPE['in_scope']),
        'mvp_out_of_scope_count': len(MVP_SCOPE['out_of_scope']),
        'qa_gates_passed': qa_gates_passed,
        'public_launch_readiness_pct': ex.get('public_launch_readiness', 8),
    },
    'catalog_gaps': [
        'Zero implementation steps completed — package is specification only',
        'Sprint Zero not started — no Neon/Prisma in production',
        'Component specs (IMP-16–18) not yet created',
        'War Room (IMP-38) specified here but Build #102 may extend it',
        'No automated step status tracking in MC yet',
        'QA gates (IMP-50) not instrumented',
        'Search MVP depends on content model (IMP-41) first',
        'Auth roles depend on Prisma schema (IMP-21–22) first',
        'County/city dashboards need seed data (IMP-24) first',
        'Generator consolidation (IMP-49) not run as unified pipeline',
    ],
    'recommended_next_build': {
        'number': 102,
        'title': 'Executive War Room & Countdown Dashboard Components',
        'note': (
            'War room UI wired to implementation step progress, live countdown, '
            'briefing panel, blocked/ready lists, sprint backlog from IMP-38.'
        ),
    },
}

with open(root / 'data/cursor-implementation-package.json', 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')

print(
    f'Implementation Package: {len(IMPLEMENTATION_STEPS)} steps, '
    f'{len(BANDS)} bands, {implementation_package_readiness}% readiness, '
    f'{steps_documented} documented, {steps_implemented} implemented'
)
