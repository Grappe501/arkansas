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
steps_documented = 7  # IMP-01 through IMP-07
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
        'summary': 'Complete technical architecture — where code, data, docs, AI, and Mission Control permanently belong',
        'deliverables': [
            'docs/IMPLEMENTATION_PACKAGE_02_TECHNICAL_ARCHITECTURE.md',
            'Master Repository Structure', 'Folder Architecture', 'Module Standards',
            'Technology Stack', 'Documentation Standards', 'AI Architecture Placement',
            'Mission Control Placement', 'Database Organization', 'Testing Organization',
            'Infrastructure Organization',
        ],
        'acceptance_criteria': [
            'One Institution → One Repository → Many Modules → Shared Foundation documented',
            'Technology stack defined: React, Next.js, TypeScript, Node, PostgreSQL, RBAC auth, search, AI, CI/CD',
            'Repository layers defined: app, components, features, ai, mission-control, database, docs, public, content, data, scripts, tests, infrastructure, config',
            'Module standards: purpose, routes, components, services, models, AI, MC metrics, docs, tests',
            'Feature isolation via shared services, events, APIs, institutional contracts',
            'MC integration rule: health, usage, completion, errors, growth, dependencies, executive metrics',
        ],
        'source_blueprints': [
            '/data/repository-blueprint.json',
            '/data/technical-architecture.json',
            '/docs/MASTER_TECHNICAL_ARCHITECTURE.md',
            '/docs/REPOSITORY_ARCHITECTURE.md',
            '/docs/IMPLEMENTATION_PACKAGE_01_TECHNICAL_CONSTITUTION.md',
        ],
        'constitution': '/docs/IMPLEMENTATION_PACKAGE_02_TECHNICAL_ARCHITECTURE.md',
        'status': 'documented',
        'documented_date': today,
    },
    {
        'number': 3, 'id': 'IMP-03', 'band': 'A',
        'package_label': 'Implementation Package 3 of 50',
        'title': 'Master Route Map & Complete Application Navigation',
        'summary': 'Every page, URL, dashboard, workspace, admin screen, and user journey — navigation before code',
        'deliverables': [
            'docs/IMPLEMENTATION_PACKAGE_03_ROUTE_MAP.md',
            'data/route-manifest.json',
            'Complete Route Map', 'Public Navigation', 'Dashboard Architecture',
            'Executive Navigation', 'Administrative Navigation', 'API Namespace Plan',
            'User Journey Framework', 'Mobile Navigation Standards',
        ],
        'acceptance_criteria': [
            'Navigation philosophy: users arrive with questions, not departments',
            'Primary public nav defined: Home through Search',
            'Public, account, workspace, MC, admin, AI, and API routes documented',
            'Route standards: breadcrumbs, search, related resources, AI, feedback, MC metrics',
            'Mobile priority: Search, Learn, County, Events, Dashboard, AI Assistant',
            'Cursor should never need to invent routes during development',
        ],
        'source_blueprints': [
            '/data/route-registry.json',
            '/data/ux-architecture.json',
            '/data/visitor-journey.json',
            '/docs/IMPLEMENTATION_PACKAGE_02_TECHNICAL_ARCHITECTURE.md',
        ],
        'constitution': '/docs/IMPLEMENTATION_PACKAGE_03_ROUTE_MAP.md',
        'manifest': '/data/route-manifest.json',
        'status': 'documented',
        'documented_date': today,
    },
    {
        'number': 4, 'id': 'IMP-04', 'band': 'A',
        'package_label': 'Implementation Package 4 of 50',
        'title': 'Master Database Schema & Canonical Data Model',
        'summary': 'Every major entity, table, relationship, identifier, and data contract — single source of truth',
        'deliverables': [
            'docs/IMPLEMENTATION_PACKAGE_04_DATABASE_SCHEMA.md',
            'data/canonical-data-manifest.json',
            'prisma/schema.prisma (draft from canonical model)',
            'data/canonical-data-model.json sync',
            'Canonical Data Model', 'Entity Registry', 'Relationship Model',
            'Search Model', 'Security Model', 'Audit Model',
            'AI Data Contracts', 'Mission Control Data Contracts', 'Governance Data Standards',
        ],
        'acceptance_criteria': [
            'Database philosophy: every important entity exists once; everything else references it',
            'Twelve primary domains documented with canonical table homes',
            'Universal record standards: UUID, slug, dates, status, owner, version, visibility, review, tags, notes',
            'Relationship hierarchy, M:N join tables, identifiers, search index, audit trail, soft deletes defined',
            'Security classification levels data-driven; AI and Mission Control integration contracts documented',
            'All entities from data/database-schema.json mapped; prisma/schema.prisma draft aligned',
        ],
        'source_blueprints': [
            '/data/database-schema.json',
            '/data/canonical-data-model.json',
            '/data/relationship-registry.json',
            '/docs/IMPLEMENTATION_PACKAGE_03_ROUTE_MAP.md',
        ],
        'constitution': '/docs/IMPLEMENTATION_PACKAGE_04_DATABASE_SCHEMA.md',
        'manifest': '/data/canonical-data-manifest.json',
        'prisma_draft': '/prisma/schema.prisma',
        'status': 'documented',
        'documented_date': today,
    },
    {
        'number': 5, 'id': 'IMP-05', 'band': 'A',
        'package_label': 'Implementation Package 5 of 50',
        'title': 'Master Identity, Authentication, Roles & Permissions',
        'summary': 'Complete identity and authorization model — one person, one identity, many roles, personalized experience',
        'deliverables': [
            'docs/IMPLEMENTATION_PACKAGE_05_IDENTITY_AUTH.md',
            'data/identity-auth-manifest.json',
            'Identity Architecture', 'Authentication Model', 'Role Hierarchy',
            'Permission Framework', 'Geographic Authorization Model',
            'Organization Authorization Model', 'User Lifecycle',
            'Onboarding Framework', 'Privacy Standards', 'Security Standards',
        ],
        'acceptance_criteria': [
            'Core philosophy: one person → one identity → many roles → personalized experience',
            'Nine-role hierarchy documented with additive permissions',
            'Authentication providers and MFA for elevated roles defined',
            'Anonymous, registered, and role-scoped capabilities documented',
            'Geographic and organization permission scoping defined',
            'Identity lifecycle, onboarding, privacy, security, MC and AI integration documented',
            'Cursor should never need to invent authorization rules during development',
        ],
        'source_blueprints': [
            '/data/identity-auth-manifest.json',
            '/data/arkansas-civic-operating-system.json',
            '/data/canonical-data-manifest.json',
            '/docs/IMPLEMENTATION_PACKAGE_04_DATABASE_SCHEMA.md',
            '/prisma/schema.prisma',
        ],
        'constitution': '/docs/IMPLEMENTATION_PACKAGE_05_IDENTITY_AUTH.md',
        'manifest': '/data/identity-auth-manifest.json',
        'status': 'documented',
        'documented_date': today,
    },
    {
        'number': 6, 'id': 'IMP-06', 'band': 'A',
        'package_label': 'Implementation Package 6 of 50',
        'title': 'Master Design System, User Experience & Visual Language',
        'summary': 'Visual identity, UX philosophy, component system, dashboards, accessibility, mobile, MC and AI interaction standards',
        'deliverables': [
            'docs/IMPLEMENTATION_PACKAGE_06_DESIGN_SYSTEM.md',
            'data/design-system-manifest.json',
            'Visual Design Language', 'UX Philosophy', 'Dashboard Standards',
            'Component System', 'Accessibility Standards', 'Mobile Standards',
            'Navigation Standards', 'Mission Control Design Rules',
            'AI Interaction Standards', 'Responsive Layout Rules',
        ],
        'acceptance_criteria': [
            'Design philosophy: reduce cognitive effort; every screen answers where/what/next',
            'Brand personality and visual identity documented',
            'Color, typography, layout, spacing, and card systems defined',
            'Dashboard, MC, map, chart, form, accessibility, mobile, AI UX standards documented',
            'Component library specified with documentation requirements',
            'Every future screen follows one coherent design language',
        ],
        'source_blueprints': [
            '/data/design-system-manifest.json',
            '/data/design-system.json',
            '/css/design-tokens.css',
            '/css/components.css',
            '/css/mission-control.css',
            '/design-system/',
            '/docs/IMPLEMENTATION_PACKAGE_05_IDENTITY_AUTH.md',
        ],
        'constitution': '/docs/IMPLEMENTATION_PACKAGE_06_DESIGN_SYSTEM.md',
        'manifest': '/data/design-system-manifest.json',
        'status': 'documented',
        'documented_date': today,
    },
    {
        'number': 7, 'id': 'IMP-07', 'band': 'A',
        'package_label': 'Implementation Package 7 of 50',
        'title': 'Master Mission Control Architecture & Executive Command Center',
        'summary': 'Executive cockpit, institutional health, statewide map, domain dashboards, alerts, digital twin, AI advisor',
        'deliverables': [
            'docs/IMPLEMENTATION_PACKAGE_07_MISSION_CONTROL.md',
            'data/mission-control-architecture-manifest.json',
            'Executive Command Center', 'Institutional Health Dashboard',
            'January 2027 Completion Dashboard', 'County, City & Neighborhood Dashboards',
            'Volunteer Command Center', 'Academy Dashboard', 'Research Dashboard',
            'Coalition Dashboard', 'PMO Dashboard', 'Executive Calendar',
            'AI Executive Advisor', 'Digital Twin Integration', 'Alert System',
        ],
        'acceptance_criteria': [
            'MC mission: five executive questions documented for every dashboard',
            'Executive home, health score, Jan 2027 completion, and state map defined',
            'County, city, neighborhood, and domain command center dashboards specified',
            'Executive calendar, briefing, alerts, digital twin, search, AI advisor documented',
            'Role-based MC permissions aligned with IMP-05 identity model',
            'Every major institutional system has a clear reporting destination',
        ],
        'source_blueprints': [
            '/data/mission-control-architecture-manifest.json',
            '/data/mission-control.json',
            '/data/mc2-executive.json',
            '/data/institutional-digital-twin.json',
            '/docs/IMPLEMENTATION_PACKAGE_06_DESIGN_SYSTEM.md',
        ],
        'constitution': '/docs/IMPLEMENTATION_PACKAGE_07_MISSION_CONTROL.md',
        'manifest': '/data/mission-control-architecture-manifest.json',
        'status': 'documented',
        'documented_date': today,
    },
    {
        'number': 8, 'id': 'IMP-08', 'band': 'A',
        'title': 'Repository migration, stack lock, Netlify, Git workflow, and environment',
        'summary': 'Strangler-fig migration, repo audit, pinned stack, netlify.toml, branch model, env matrix',
        'deliverables': [
            'docs/MIGRATION_PLAN.md', 'docs/REPO_AUDIT.md', 'app/README.md',
            'docs/STACK.md', 'docs/SERVICE_BOUNDARIES.md', 'docs/DEPLOYMENT_TOPOLOGY.md',
            'netlify.toml', 'docs/DEPLOYMENT.md', 'docs/GIT_WORKFLOW.md',
            '.env.example', 'docs/ENVIRONMENT.md',
        ],
        'acceptance_criteria': [
            'Current tree diffed against IMP-02 repository structure',
            'Migration strategy chosen with rollback plan',
            'Target folders scaffolded; existing static Netlify deploy unchanged',
            'Pinned versions documented with rationale',
            'Branch purposes match repository-blueprint branch_structure',
            'All required env vars documented with no secrets committed',
        ],
        'source_blueprints': [
            '/docs/IMPLEMENTATION_PACKAGE_02_TECHNICAL_ARCHITECTURE.md',
            '/data/repository-blueprint.json',
            '/data/technical-architecture.json',
            '/netlify.toml',
        ],
        'status': 'specified',
    },
    {
        'number': 9, 'id': 'IMP-09', 'band': 'A',
        'title': 'CI pipeline and package scripts',
        'summary': 'CI gates plus dev, build, db:migrate, gen:* npm scripts',
        'deliverables': ['.github/workflows/ci.yml', 'package.json scripts section', 'docs/SCRIPTS.md'],
        'acceptance_criteria': [
            'CI runs on pull_request to main and develop',
            'Generator scripts invocable via npm run gen:all pattern',
            'Node version pinned in .nvmrc or engines field',
        ],
        'source_blueprints': ['/package.json', '/scripts/', '/data/technical-architecture.json'],
        'status': 'specified',
    },
    {
        'number': 10, 'id': 'IMP-10', 'band': 'A',
        'title': 'Sprint Zero exit checklist',
        'summary': 'Gate before Band B — repo ready for first code slice',
        'deliverables': ['docs/SPRINT_ZERO_CHECKLIST.md', 'CONTRIBUTING.md'],
        'acceptance_criteria': [
            'IMP-01 through IMP-07 documented; IMP-08–09 engineering criteria verified',
            'CONTRIBUTING.md links to implementation packages and CURSOR_MASTER_BUILD_PROMPT.md',
            'One successful Netlify preview deploy from develop',
            'Executive sign-off field in checklist (manual)',
        ],
        'source_blueprints': ['/data/cursor-implementation-package.json', '/docs/IMPLEMENTATION_PACKAGE_02_TECHNICAL_ARCHITECTURE.md'],
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

PRIMARY_NAVIGATION = [
    'Home', 'About', 'Learn', 'Research', 'Evidence', 'Academy', 'Counties', 'Cities',
    'Action Center', 'Coalition', 'News & Updates', 'Get Involved', 'Donate (future)', 'Login', 'Search',
]

PUBLIC_ROUTES = [
    {'id': 'RT-01', 'path': '/', 'name': 'Home', 'zone': 'public', 'purpose': 'Introduce institution; clear next steps'},
    {'id': 'RT-02', 'path': '/about', 'name': 'About', 'zone': 'public', 'sections': ['Mission', 'Vision', 'History', 'Leadership', 'Founding Charter', 'Volunteer model']},
    {'id': 'RT-03', 'path': '/learn', 'name': 'Learn', 'zone': 'public', 'sections': ['Learning paths', 'Beginner guides', 'Courses', 'Videos', 'Glossary', 'FAQ']},
    {'id': 'RT-04', 'path': '/research', 'name': 'Research', 'zone': 'public', 'sections': ['Research Library', 'White Papers', 'Historical research', 'Campaign finance', 'Constitutional research', 'Arkansas research']},
    {'id': 'RT-05', 'path': '/evidence', 'name': 'Evidence', 'zone': 'public', 'sections': ['Evidence Ledger', 'Claims Registry', 'Primary Sources', 'Court opinions', 'Citation explorer']},
    {'id': 'RT-06', 'path': '/academy', 'name': 'Academy', 'zone': 'public', 'sections': ['Course catalog', 'Certificates', 'Leadership pathways', 'Education Leaders', 'Training']},
    {'id': 'RT-07', 'path': '/counties', 'name': 'Counties', 'zone': 'public', 'sections': ['Interactive map', 'Directory', 'Dashboards', 'Education Leaders', 'Resources']},
    {'id': 'RT-08', 'path': '/counties/{county-slug}', 'name': 'County', 'zone': 'public', 'dynamic': True},
    {'id': 'RT-09', 'path': '/cities', 'name': 'Cities', 'zone': 'public'},
    {'id': 'RT-10', 'path': '/cities/{city-slug}', 'name': 'City', 'zone': 'public', 'dynamic': True},
    {'id': 'RT-11', 'path': '/neighborhoods/{slug}', 'name': 'Neighborhood', 'zone': 'public', 'dynamic': True},
    {'id': 'RT-12', 'path': '/action', 'name': 'Arkansas Action Center', 'zone': 'public', 'sections': ['Legislative resources', 'Government process', 'Public meetings', 'How-to guides']},
    {'id': 'RT-13', 'path': '/coalition', 'name': 'Coalition', 'zone': 'public'},
    {'id': 'RT-14', 'path': '/news', 'name': 'News', 'zone': 'public'},
    {'id': 'RT-15', 'path': '/events', 'name': 'Events', 'zone': 'public'},
    {'id': 'RT-16', 'path': '/media', 'name': 'Media', 'zone': 'public'},
    {'id': 'RT-17', 'path': '/faq', 'name': 'FAQ', 'zone': 'public'},
    {'id': 'RT-18', 'path': '/contact', 'name': 'Contact', 'zone': 'public'},
]

ACCOUNT_ROUTES = [
    {'path': '/login', 'name': 'Login'}, {'path': '/register', 'name': 'Register'},
    {'path': '/forgot-password', 'name': 'Forgot Password'}, {'path': '/profile', 'name': 'Profile'},
    {'path': '/settings', 'name': 'Settings'}, {'path': '/notifications', 'name': 'Notifications'},
    {'path': '/messages', 'name': 'Messages'}, {'path': '/dashboard', 'name': 'Personal Dashboard'},
]

WORKSPACE_ROUTES = [
    {'path': '/volunteer', 'name': 'Volunteer Workspace', 'role': 'volunteer'},
    {'path': '/leader', 'name': 'Education Leader Workspace', 'role': 'education_leader'},
    {'path': '/organization', 'name': 'Coalition Workspace', 'role': 'organization'},
    {'path': '/executive', 'name': 'Executive Workspace', 'role': 'executive'},
]

SYSTEM_ROUTES = [
    {'path': '/mission-control', 'name': 'Mission Control', 'zone': 'institution'},
    {'path': '/admin', 'name': 'Admin', 'zone': 'admin', 'auth_required': True},
    {'path': '/ai', 'name': 'AI Workspace', 'zone': 'ai'},
    {'path': '/search', 'name': 'Search', 'zone': 'public'},
]

API_NAMESPACES = [
    'authentication', 'research', 'mission-control', 'academy', 'volunteer',
    'organizations', 'ai', 'knowledge', 'reports', 'search', 'calendar', 'messaging',
]

ROUTE_STANDARDS = [
    'Purpose', 'Breadcrumbs', 'Search', 'Related resources', 'AI assistance',
    'Feedback option', 'Mission Control metrics (internal)',
]

MOBILE_NAV_PRIORITY = ['Search', 'Learn', 'County', 'Events', 'Dashboard', 'AI Assistant']

NAVIGATION_QUESTIONS = [
    'I want to understand…', 'I want to learn…', 'I want to volunteer…',
    'I want to teach…', 'I want to find my county…', 'I want to see the evidence…',
    'I want to ask a question…',
]

DOMAINS = [
    {
        'id': 'DOM-01', 'name': 'Identity', 'number': 1,
        'tables': [
            'users', 'profiles', 'roles', 'permissions', 'sessions',
            'authentication_providers', 'notification_preferences', 'privacy_settings',
        ],
    },
    {
        'id': 'DOM-02', 'name': 'Geography', 'number': 2,
        'tables': [
            'counties', 'cities', 'neighborhoods', 'legislative_districts',
            'congressional_districts', 'school_districts', 'regions', 'zip_codes',
        ],
    },
    {
        'id': 'DOM-03', 'name': 'Organizations', 'number': 3,
        'tables': [
            'organizations', 'coalition_members', 'partner_organizations', 'libraries',
            'universities', 'community_groups', 'historical_societies', 'faith_organizations',
            'organization_contacts',
        ],
    },
    {
        'id': 'DOM-04', 'name': 'People', 'number': 4,
        'tables': [
            'education_leaders', 'volunteers', 'researchers', 'authors', 'presenters',
            'mentors', 'subject_matter_experts', 'staff',
        ],
        'note': 'Person may hold multiple roles; links to users and people table',
    },
    {
        'id': 'DOM-05', 'name': 'Research', 'number': 5,
        'tables': [
            'research_articles', 'court_cases', 'statutes', 'constitutional_provisions',
            'primary_sources', 'secondary_sources', 'citations', 'claims', 'evidence_records',
            'research_reviews',
        ],
        'schema_entities': ['source', 'fact'],
    },
    {
        'id': 'DOM-06', 'name': 'Education', 'number': 6,
        'tables': [
            'courses', 'lessons', 'modules', 'learning_paths', 'quizzes', 'certificates',
            'student_progress', 'academy_cohorts', 'presentation_materials',
        ],
        'schema_entities': ['educational_resource'],
    },
    {
        'id': 'DOM-07', 'name': 'Community', 'number': 7,
        'tables': [
            'community_conversations', 'events', 'meeting_notes', 'questions',
            'community_requests', 'volunteer_opportunities', 'neighborhood_groups',
            'listening_reports',
        ],
        'schema_entities': ['event', 'signup', 'referral'],
    },
    {
        'id': 'DOM-08', 'name': 'Operations', 'number': 8,
        'tables': [
            'projects', 'tasks', 'milestones', 'risks', 'dependencies', 'departments',
            'committees', 'decision_log', 'institutional_calendar',
        ],
    },
    {
        'id': 'DOM-09', 'name': 'Mission Control', 'number': 9,
        'tables': [
            'dashboards', 'metrics', 'kpis', 'goals', 'county_health', 'city_health',
            'neighborhood_health', 'institution_health', 'readiness_scores',
        ],
        'schema_entities': ['mc_build_record'],
        'principle': 'MC reads operational data — does not duplicate',
    },
    {
        'id': 'DOM-10', 'name': 'AI', 'number': 10,
        'tables': [
            'local_brains', 'ai_agents', 'prompt_library', 'knowledge_retrieval',
            'conversation_history', 'ai_tasks', 'ai_recommendations', 'ai_feedback',
        ],
    },
    {
        'id': 'DOM-11', 'name': 'Content', 'number': 11,
        'tables': [
            'articles', 'news', 'videos', 'media_assets', 'faqs', 'glossary_terms',
            'downloads', 'infographics', 'presentation_decks',
        ],
        'schema_entities': ['educational_resource'],
    },
    {
        'id': 'DOM-12', 'name': 'Governance', 'number': 12,
        'tables': [
            'policies', 'operating_manuals', 'constitution', 'implementation_packages',
            'board_decisions', 'review_schedules', 'version_history', 'institutional_standards',
        ],
    },
]

UNIVERSAL_RECORD_STANDARDS = [
    'uuid', 'public_slug', 'created_date', 'updated_date', 'status', 'owner',
    'version', 'visibility', 'last_reviewed', 'tags', 'notes',
]

VISIBILITY_LEVELS = [
    'public', 'volunteer', 'education_leader', 'organization',
    'executive', 'mission_control', 'administrator',
]

RECORD_STATUS_VALUES = ['active', 'archived', 'deprecated', 'historical']

MANY_TO_MANY_RELATIONSHIPS = [
    {'from': 'volunteer', 'to': 'organization', 'join_table': 'volunteer_organizations'},
    {'from': 'volunteer', 'to': 'county', 'join_table': 'volunteer_counties'},
    {'from': 'volunteer', 'to': 'project', 'join_table': 'volunteer_projects'},
    {'from': 'course', 'to': 'lesson', 'join_table': 'course_lessons'},
    {'from': 'research', 'to': 'court_case', 'join_table': 'research_court_cases'},
    {'from': 'organization', 'to': 'event', 'join_table': 'organization_events'},
    {'from': 'education_leader', 'to': 'city', 'join_table': 'leader_cities'},
    {'from': 'community_conversation', 'to': 'resource', 'join_table': 'conversation_resources'},
    {'from': 'person', 'to': 'organization', 'join_table': 'person_organizations'},
    {'from': 'event', 'to': 'educational_resource', 'join_table': 'event_resources'},
    {'from': 'fact', 'to': 'source', 'join_table': 'fact_sources'},
    {'from': 'educational_resource', 'to': 'source', 'join_table': 'resource_sources'},
]

RELATIONSHIP_HIERARCHY = [
    'county', 'cities', 'neighborhoods', 'education_leaders',
    'community_conversations', 'events', 'volunteers', 'projects',
]

AI_KNOWLEDGE_CHAIN = [
    'research_article', 'court_case', 'claim', 'evidence',
    'lesson', 'presentation', 'community_conversation',
]

SEARCH_INDEX_FIELDS = [
    'title', 'summary', 'keywords', 'categories', 'tags',
    'related_entities', 'geographic_references', 'publication_status',
]

AUDIT_TRAIL_FIELDS = ['who', 'when', 'what_changed', 'why_optional']

total_domain_tables = sum(len(d['tables']) for d in DOMAINS)

CANONICAL_DATA_MANIFEST = {
    'version': '1.0',
    'build': 101,
    'package': 'IMP-04',
    'updated': today,
    'title': 'Master Database Schema & Canonical Data Model',
    'constitution': '/docs/IMPLEMENTATION_PACKAGE_04_DATABASE_SCHEMA.md',
    'source_registries': {
        'database_schema': '/data/database-schema.json',
        'canonical_model': '/data/canonical-data-model.json',
        'relationship_registry': '/data/relationship-registry.json',
        'prisma_draft': '/prisma/schema.prisma',
    },
    'philosophy': 'Every important entity exists once; everything else references it',
    'governing_principle': (
        'A trustworthy database creates trustworthy systems. '
        'A trustworthy system earns public trust.'
    ),
    'universal_record_standards': UNIVERSAL_RECORD_STANDARDS,
    'record_status_values': RECORD_STATUS_VALUES,
    'visibility_levels': VISIBILITY_LEVELS,
    'domains': DOMAINS,
    'domain_count': len(DOMAINS),
    'total_tables_defined': total_domain_tables,
    'relationship_hierarchy': RELATIONSHIP_HIERARCHY,
    'many_to_many_relationships': MANY_TO_MANY_RELATIONSHIPS,
    'canonical_identifiers': ['internal_uuid', 'public_slug', 'human_title', 'search_aliases', 'legacy_references'],
    'search_index_fields': SEARCH_INDEX_FIELDS,
    'audit_trail_fields': AUDIT_TRAIL_FIELDS,
    'ai_knowledge_chain': AI_KNOWLEDGE_CHAIN,
    'mission_control_principle': 'Mission Control reads rather than duplicates operational data',
    'schema_entity_count': 14,
    'prisma_models_drafted': 22,
    'status': 'documented',
    'implemented': False,
}

ROLES = [
    {
        'id': 'public', 'name': 'Public Visitor', 'level': 0,
        'account_required': False, 'workspace': '/',
        'capabilities': [
            'Browse public research', 'Read articles', 'Use search',
            'Explore counties and cities', 'Read educational materials',
        ],
        'acos_mapping': None,
    },
    {
        'id': 'member', 'name': 'Registered Member', 'level': 1,
        'account_required': True, 'workspace': '/dashboard',
        'capabilities': [
            'Personal dashboard', 'Learning progress', 'Bookmarks and saved research',
            'Event registration', 'Notifications', 'AI assistant', 'Personal calendar',
            'Community recommendations',
        ],
        'acos_mapping': 'Learner',
    },
    {
        'id': 'volunteer', 'name': 'Volunteer', 'level': 2,
        'account_required': True, 'workspace': '/volunteer',
        'capabilities': [
            'Volunteer workspace', 'Assignments', 'Projects', 'Training',
            'Community conversations',
        ],
        'acos_mapping': 'Volunteer',
    },
    {
        'id': 'education_leader', 'name': 'Education Leader', 'level': 3,
        'account_required': True, 'workspace': '/leader',
        'capabilities': [
            'Presentation materials', 'Local leadership tools', 'County and city resources',
            'Mentoring features', 'Community management',
        ],
        'acos_mapping': 'Education Leader',
    },
    {
        'id': 'research_contributor', 'name': 'Research Contributor', 'level': 3,
        'account_required': True, 'workspace': '/research',
        'capabilities': [
            'Research workspace', 'Draft submissions', 'Evidence management',
            'Citation tools', 'Peer review participation',
        ],
        'acos_mapping': 'Researcher',
    },
    {
        'id': 'organization_admin', 'name': 'Organization Administrator', 'level': 4,
        'account_required': True, 'workspace': '/organization',
        'capabilities': [
            'Organization dashboard', 'Member management', 'Shared resources',
            'Events', 'Coalition reporting',
        ],
        'acos_mapping': 'Coalition partner',
    },
    {
        'id': 'department_lead', 'name': 'Department Lead', 'level': 5,
        'account_required': True, 'workspace': '/executive',
        'capabilities': [
            'Department dashboard', 'Project oversight', 'Volunteer coordination',
            'Mission metrics', 'Reporting',
        ],
        'acos_mapping': None,
    },
    {
        'id': 'executive', 'name': 'Executive Leadership', 'level': 6,
        'account_required': True, 'workspace': '/executive',
        'capabilities': [
            'Mission Control', 'Institution dashboards', 'Strategic planning',
            'Institutional reports', 'Forecasting', 'Executive AI',
        ],
        'acos_mapping': 'Executive',
    },
    {
        'id': 'administrator', 'name': 'System Administrator', 'level': 7,
        'account_required': True, 'workspace': '/admin',
        'capabilities': [
            'Platform configuration', 'User management', 'Security', 'Infrastructure',
            'AI management', 'Deployment tools',
        ],
        'acos_mapping': None,
        'mfa_required': True,
    },
]

PERMISSION_CATEGORIES = [
    {'id': 'read', 'name': 'Read', 'description': 'View content and data within scope'},
    {'id': 'create', 'name': 'Create', 'description': 'Add new records'},
    {'id': 'edit', 'name': 'Edit', 'description': 'Modify existing records'},
    {'id': 'review', 'name': 'Review', 'description': 'Submit for editorial or peer review'},
    {'id': 'approve', 'name': 'Approve', 'description': 'Approve content or actions'},
    {'id': 'publish', 'name': 'Publish', 'description': 'Make content publicly visible'},
    {'id': 'manage', 'name': 'Manage', 'description': 'Oversee users, resources, or projects in scope'},
    {'id': 'delete', 'name': 'Delete', 'description': 'Rare; soft-delete preferred'},
    {'id': 'administer', 'name': 'Administer', 'description': 'Platform configuration'},
    {'id': 'audit', 'name': 'Audit', 'description': 'View change history and security logs'},
]

AUTH_PROVIDERS = [
    {'id': 'email_password', 'name': 'Email/password', 'status': 'recommended'},
    {'id': 'google', 'name': 'Google', 'status': 'recommended'},
    {'id': 'apple', 'name': 'Apple', 'status': 'recommended'},
    {'id': 'microsoft', 'name': 'Microsoft', 'status': 'recommended'},
    {'id': 'enterprise_sso', 'name': 'Enterprise SSO', 'status': 'future'},
]

GEOGRAPHIC_SCOPES = [
    {'scope': 'neighborhood', 'role_example': 'Neighborhood Leader', 'assignment': 'Assigned neighborhood'},
    {'scope': 'city', 'role_example': 'City Education Leader', 'assignment': 'Assigned city'},
    {'scope': 'county', 'role_example': 'County Education Director', 'assignment': 'Assigned county'},
    {'scope': 'region', 'role_example': 'Regional Mentor', 'assignment': 'Assigned region'},
    {'scope': 'statewide', 'role_example': 'Executive', 'assignment': 'All Arkansas'},
]

IDENTITY_LIFECYCLE = [
    {'stage': 1, 'id': 'visitor', 'name': 'Visitor', 'account_required': False},
    {'stage': 2, 'id': 'registered_member', 'name': 'Registered Member', 'account_required': True},
    {'stage': 3, 'id': 'learner', 'name': 'Learner', 'account_required': True},
    {'stage': 4, 'id': 'volunteer', 'name': 'Volunteer', 'account_required': True},
    {'stage': 5, 'id': 'education_leader', 'name': 'Education Leader', 'account_required': True},
    {'stage': 6, 'id': 'mentor', 'name': 'Mentor', 'account_required': True},
    {'stage': 7, 'id': 'institutional_leader', 'name': 'Institutional Leader', 'account_required': True},
]

ONBOARDING_STEPS = [
    'Welcome', 'Mission introduction', 'Personal interests', 'County selection',
    'City selection', 'Learning recommendations', 'Volunteer opportunities (optional)',
    'AI introduction',
]

PRIVACY_CONTROLS = [
    'profile_visibility', 'volunteer_visibility', 'communication_preferences',
    'organization_memberships', 'notification_settings', 'public_facing_information',
]

SECURITY_PRINCIPLES = [
    'Least privilege by default',
    'Multi-factor authentication for elevated roles',
    'Session expiration',
    'Audit logging',
    'Permission review',
    'No shared administrator accounts',
]

MC_IDENTITY_METRICS = [
    'registered_users', 'active_users', 'volunteers', 'education_leaders',
    'organization_administrators', 'county_leadership', 'city_leadership',
    'role_distribution', 'growth_trends',
]

AI_IDENTITY_CONTEXT = [
    'role', 'permissions', 'projects', 'learning_history',
    'volunteer_responsibilities', 'calendar', 'institutional_context',
]

IDENTITY_AUTH_MANIFEST = {
    'version': '1.0',
    'build': 101,
    'package': 'IMP-05',
    'updated': today,
    'title': 'Master Identity, Authentication, Roles & Permissions',
    'constitution': '/docs/IMPLEMENTATION_PACKAGE_05_IDENTITY_AUTH.md',
    'source_registries': {
        'canonical_data_manifest': '/data/canonical-data-manifest.json',
        'acos_roles': '/data/arkansas-civic-operating-system.json',
        'prisma_draft': '/prisma/schema.prisma',
        'route_manifest': '/data/route-manifest.json',
    },
    'philosophy': 'One person → one identity → many roles → personalized experience',
    'governing_principle': (
        'Every person should have exactly the access they need to contribute '
        'confidently, securely, and effectively.'
    ),
    'identity_principles': [
        'permanent_institutional_identity', 'personal_profile', 'role_assignment',
        'permission_set', 'activity_history', 'learning_history', 'volunteer_history',
    ],
    'authentication': {
        'providers': AUTH_PROVIDERS,
        'mfa_required_roles': ['administrator', 'executive', 'department_lead'],
        'session_expiration': True,
    },
    'anonymous_access': ROLES[0]['capabilities'],
    'roles': ROLES,
    'role_count': len(ROLES),
    'multi_role_supported': True,
    'permission_categories': PERMISSION_CATEGORIES,
    'permission_category_count': len(PERMISSION_CATEGORIES),
    'geographic_scopes': GEOGRAPHIC_SCOPES,
    'organization_permissions': {
        'multi_org_membership': True,
        'org_specific_permissions': True,
        'org_entities': ['members', 'roles', 'resources', 'events', 'projects'],
    },
    'identity_lifecycle': IDENTITY_LIFECYCLE,
    'onboarding_steps': ONBOARDING_STEPS,
    'privacy_controls': PRIVACY_CONTROLS,
    'security_principles': SECURITY_PRINCIPLES,
    'mission_control_metrics': MC_IDENTITY_METRICS,
    'ai_context_fields': AI_IDENTITY_CONTEXT,
    'account_routes': [
        '/login', '/register', '/forgot-password', '/profile',
        '/settings', '/notifications', '/messages', '/dashboard',
    ],
    'workspace_routes_by_role': {
        'volunteer': '/volunteer',
        'education_leader': '/leader',
        'organization_admin': '/organization',
        'executive': '/executive',
        'administrator': '/admin',
    },
    'status': 'documented',
    'implemented': False,
}

BRAND_PERSONALITY = [
    'trustworthy', 'calm', 'intelligent', 'welcoming', 'organized',
    'optimistic', 'respectful', 'evidence_driven', 'arkansas_rooted',
]

DESIGN_SCREEN_QUESTIONS = ['Where am I?', 'What can I do?', 'What should I do next?']

COLOR_ROLES = [
    {'role': 'primary', 'purpose': 'Institution identity', 'token': '--ds-primary'},
    {'role': 'secondary', 'purpose': 'Navigation and supporting elements', 'token': '--ds-primary-light'},
    {'role': 'success', 'purpose': 'Completion, learning progress, healthy systems', 'token': '--ds-success'},
    {'role': 'warning', 'purpose': 'Needs attention, risk indicators', 'token': '--ds-warning'},
    {'role': 'information', 'purpose': 'Educational notices, Mission Control insights', 'token': '--ds-info'},
    {'role': 'neutral', 'purpose': 'Reading, backgrounds, cards, typography', 'token': '--ds-text-muted'},
]

TYPOGRAPHY_HIERARCHY = [
    {'level': 'institution_title', 'token': '--ds-text-institutional'},
    {'level': 'page_title', 'token': '--ds-text-h1'},
    {'level': 'section_heading', 'token': '--ds-text-h2'},
    {'level': 'subheading', 'token': '--ds-text-h3'},
    {'level': 'body', 'token': '--ds-text-body'},
    {'level': 'caption', 'token': '--ds-text-caption'},
    {'level': 'metadata', 'token': '--ds-text-data'},
]

CARD_TYPES = [
    'research', 'volunteer', 'county', 'city', 'organization',
    'course', 'project', 'mission_control',
]

DASHBOARD_SECTIONS = [
    'current_status', 'key_indicators', 'recommended_actions',
    'recent_activity', 'upcoming_work', 'important_alerts',
]

MAP_USE_CASES = [
    'arkansas_overview', 'county_health', 'city_participation',
    'neighborhood_coverage', 'education_leader_locations', 'community_conversations',
]

CHART_TYPES = [
    'progress_bars', 'trend_lines', 'heat_maps', 'completion_rings',
    'growth_charts', 'timeline_views', 'network_diagrams',
]

FORM_STANDARDS = [
    'one_logical_question_at_a_time', 'auto_save_when_practical',
    'helpful_validation', 'keyboard_navigation', 'reduce_unnecessary_typing',
]

ACCESSIBILITY_STANDARDS = [
    'keyboard_navigation', 'high_color_contrast', 'screen_reader_compatibility',
    'alternative_text', 'scalable_typography', 'reduced_motion_support', 'clear_focus_states',
]

MOBILE_PRIORITIES = [
    'Learning', 'Events', 'County information', 'Community conversations',
    'Volunteer tasks', 'AI Assistant', 'Search',
]

AI_UX_STANDARDS = [
    'state_confidence', 'reference_institutional_knowledge', 'suggest_next_steps',
    'offer_related_resources', 'encourage_continued_learning', 'conversational_interface',
]

PERSONAL_DASHBOARD_ELEMENTS = [
    'welcome', 'learning_progress', 'upcoming_events', 'county_updates',
    'volunteer_opportunities', 'recent_activity', 'recommended_next_step', 'personal_ai',
]

EXECUTIVE_DASHBOARD_ELEMENTS = [
    'mission_control', 'institution_health', 'critical_alerts', 'county_progress',
    'city_progress', 'strategic_goals', 'pmo_status', 'executive_ai_recommendations',
]

ANIMATION_USES = [
    'guide_attention', 'confirm_actions', 'explain_transitions', 'celebrate_achievements',
]

DESIGN_COMPONENTS = [
    'buttons', 'cards', 'badges', 'alerts', 'tables', 'charts', 'maps',
    'timelines', 'progress_indicators', 'search', 'filters', 'calendars',
    'modal_dialogs', 'knowledge_panels',
]

COMPONENT_DOC_REQUIREMENTS = [
    'purpose', 'usage_guidelines', 'accessibility_notes',
    'examples', 'states', 'design_tokens',
]

MC_UX_METRICS = [
    'page_completion', 'search_success', 'learning_completion',
    'volunteer_onboarding', 'navigation_flow',
]

LAYOUT_LAYERS = [
    'orientation', 'summary', 'main_narrative', 'visual_explanation',
    'supporting_evidence', 'related_topics', 'civic_action_opportunities',
]

DESIGN_SYSTEM_MANIFEST = {
    'version': '1.0',
    'build': 101,
    'package': 'IMP-06',
    'updated': today,
    'title': 'Master Design System, User Experience & Visual Language',
    'constitution': '/docs/IMPLEMENTATION_PACKAGE_06_DESIGN_SYSTEM.md',
    'source_registries': {
        'design_language': '/data/design-system.json',
        'css_tokens': '/css/design-tokens.css',
        'css_components': '/css/components.css',
        'mc_theme': '/css/mission-control.css',
        'showcase': '/design-system/',
    },
    'philosophy': 'Design reduces cognitive effort; every screen answers where/what/next',
    'governing_principle': (
        'People decide whether to trust an institution within moments. '
        'Thoughtful design communicates competence and welcome before a word is read.'
    ),
    'brand_personality': BRAND_PERSONALITY,
    'screen_questions': DESIGN_SCREEN_QUESTIONS,
    'visual_identity': [
        'clean_layouts', 'strong_typography', 'comfortable_spacing',
        'simple_navigation', 'high_readability', 'consistent_interactions', 'minimal_clutter',
    ],
    'color_roles': COLOR_ROLES,
    'typography_hierarchy': TYPOGRAPHY_HIERARCHY,
    'fonts': {'serif': 'Source Serif 4', 'sans': 'Source Sans 3', 'mono': 'Consolas'},
    'layout': {
        'system': 'responsive_grid',
        'reading_measure': '65ch',
        'layers': LAYOUT_LAYERS,
    },
    'spacing_principle': 'Whitespace is intentional; every screen should breathe',
    'card_types': CARD_TYPES,
    'card_type_count': len(CARD_TYPES),
    'navigation': {
        'primary_stable': True,
        'secondary_contextual': True,
        'breadcrumbs': True,
        'search_always_available': True,
    },
    'dashboard_philosophy': {
        'principle': 'Dashboards answer questions, not display everything',
        'sections': DASHBOARD_SECTIONS,
    },
    'mission_control_design': {
        'character': 'executive_operations_center',
        'theme': 'NASA-inspired dark cockpit',
        'features': [
            'large_metrics', 'status_indicators', 'interactive_maps', 'trend_charts',
            'forecasts', 'task_summaries', 'institution_health', 'minimal_distraction',
        ],
    },
    'maps': {'central_navigation': True, 'use_cases': MAP_USE_CASES, 'drill_down_required': True},
    'chart_types': CHART_TYPES,
    'form_standards': FORM_STANDARDS,
    'accessibility_standards': ACCESSIBILITY_STANDARDS,
    'accessibility_wcag': '2.1 AA',
    'mobile_priorities': MOBILE_PRIORITIES,
    'mobile_complete_experience': True,
    'ai_ux_standards': AI_UX_STANDARDS,
    'personal_dashboard_elements': PERSONAL_DASHBOARD_ELEMENTS,
    'executive_dashboard_elements': EXECUTIVE_DASHBOARD_ELEMENTS,
    'animation': {
        'principle': 'Subtle only; never distract from content',
        'uses': ANIMATION_USES,
        'reduced_motion_respected': True,
    },
    'design_components': DESIGN_COMPONENTS,
    'component_count': len(DESIGN_COMPONENTS),
    'component_doc_requirements': COMPONENT_DOC_REQUIREMENTS,
    'mc_ux_metrics': MC_UX_METRICS,
    'live_component_count': 14,
    'status': 'documented',
    'implemented': False,
}

EXECUTIVE_QUESTIONS = [
    {'id': 'EQ-01', 'question': 'Where are we?', 'purpose': 'Current state and progress'},
    {'id': 'EQ-02', 'question': 'What is happening?', 'purpose': 'Active operations and events'},
    {'id': 'EQ-03', 'question': 'Why is it happening?', 'purpose': 'Trends, causes, context'},
    {'id': 'EQ-04', 'question': 'What needs attention?', 'purpose': 'Alerts, risks, gaps'},
    {'id': 'EQ-05', 'question': 'What should we do next?', 'purpose': 'Priorities and recommendations'},
]

STEWARDSHIP_ACTIONS = ['see', 'understand', 'prioritize', 'coordinate', 'improve']

EXECUTIVE_HOME_PANELS = [
    'overall_institutional_health', 'january_2027_completion_progress', 'critical_alerts',
    'top_priorities', 'projects_at_risk', 'volunteer_activity', 'research_progress',
    'county_coverage', 'city_coverage', 'neighborhood_growth',
    'fifteen_percent_engagement_progress', 'two_hundred_k_arkansans_progress',
    'executive_calendar', 'ai_executive_briefing',
]

INSTITUTIONAL_HEALTH_CATEGORIES = [
    'research', 'technology', 'mission_control', 'education', 'volunteer_network',
    'county_operations', 'city_operations', 'neighborhood_operations', 'coalition',
    'communications', 'governance', 'ai_systems', 'knowledge_platform', 'trust', 'pmo',
]

JANUARY_2027_DASHBOARD_METRICS = [
    'overall_completion', 'department_completion', 'open_milestones', 'critical_path',
    'blocked_work', 'volunteer_capacity', 'schedule_variance', 'projected_completion_date',
]

STATE_MAP_LAYERS = [
    'county_health', 'education_leaders', 'city_participation', 'volunteer_density',
    'coalition_partners', 'community_conversations', 'academy_participation',
    'research_activity', 'fifteen_percent_connected_citizen_goal',
]

MC_DASHBOARDS = [
    {
        'id': 'MC-D01', 'name': 'Executive Home', 'route': '/mission-control/',
        'questions': ['EQ-01', 'EQ-02', 'EQ-04', 'EQ-05'],
        'panels': EXECUTIVE_HOME_PANELS,
    },
    {
        'id': 'MC-D02', 'name': 'Institutional Health', 'route': '/mission-control/health',
        'questions': ['EQ-01', 'EQ-03', 'EQ-04', 'EQ-05'],
        'categories': INSTITUTIONAL_HEALTH_CATEGORIES,
    },
    {
        'id': 'MC-D03', 'name': 'January 2027 Completion', 'route': '/mission-control/completion-2027',
        'questions': ['EQ-01', 'EQ-04', 'EQ-05'],
        'metrics': JANUARY_2027_DASHBOARD_METRICS,
    },
    {
        'id': 'MC-D04', 'name': 'Arkansas State Map', 'route': '/mission-control/map',
        'questions': ['EQ-01', 'EQ-02'],
        'layers': STATE_MAP_LAYERS,
    },
    {
        'id': 'MC-D05', 'name': 'County Operations', 'route': '/counties/{county-slug}',
        'questions': ['EQ-01', 'EQ-02', 'EQ-05'],
    },
    {
        'id': 'MC-D06', 'name': 'City Operations', 'route': '/cities/{city-slug}',
        'questions': ['EQ-01', 'EQ-02', 'EQ-05'],
    },
    {
        'id': 'MC-D07', 'name': 'Neighborhood', 'route': '/neighborhoods/{slug}',
        'questions': ['EQ-01', 'EQ-02'],
    },
    {
        'id': 'MC-D08', 'name': 'Volunteer Command Center', 'route': '/mission-control/volunteers',
        'questions': ['EQ-02', 'EQ-04', 'EQ-05'],
    },
    {
        'id': 'MC-D09', 'name': 'Academy Dashboard', 'route': '/mission-control/academy',
        'questions': ['EQ-01', 'EQ-02'],
    },
    {
        'id': 'MC-D10', 'name': 'Research Dashboard', 'route': '/mission-control/research',
        'questions': ['EQ-01', 'EQ-02', 'EQ-04'],
    },
    {
        'id': 'MC-D11', 'name': 'Coalition Dashboard', 'route': '/mission-control/coalition',
        'questions': ['EQ-01', 'EQ-02'],
    },
    {
        'id': 'MC-D12', 'name': 'Communications Dashboard', 'route': '/mission-control/communications',
        'questions': ['EQ-01', 'EQ-02'],
    },
    {
        'id': 'MC-D13', 'name': 'AI Dashboard', 'route': '/mission-control/ai',
        'questions': ['EQ-02', 'EQ-03'],
    },
    {
        'id': 'MC-D14', 'name': 'PMO Dashboard', 'route': '/mission-control/pmo',
        'questions': ['EQ-01', 'EQ-04', 'EQ-05'],
    },
]

EXECUTIVE_CALENDAR_SOURCES = [
    'research', 'community_conversations', 'volunteer_events', 'academy',
    'technology_releases', 'leadership_meetings', 'public_events', 'annual_reviews',
]

EXECUTIVE_BRIEFING_SECTIONS = [
    'institution_summary', 'new_developments', 'critical_alerts', 'volunteer_needs',
    'research_updates', 'executive_recommendations', 'upcoming_deadlines',
]

ALERT_TYPES = [
    {'type': 'research_overdue', 'severity_default': 'high'},
    {'type': 'volunteer_shortage', 'severity_default': 'high'},
    {'type': 'leadership_vacancy', 'severity_default': 'medium'},
    {'type': 'technology_failure', 'severity_default': 'critical'},
    {'type': 'missed_milestone', 'severity_default': 'high'},
    {'type': 'security_concern', 'severity_default': 'critical'},
    {'type': 'county_support_need', 'severity_default': 'medium'},
    {'type': 'community_growth_opportunity', 'severity_default': 'low'},
]

ALERT_SEVERITY_LEVELS = ['critical', 'high', 'medium', 'low', 'informational']

DIGITAL_TWIN_VISUALIZATIONS = [
    'institution_growth', 'leadership_network', 'knowledge_graph', 'county_development',
    'volunteer_movement', 'forecasts', 'scenario_planning',
]

EXECUTIVE_SEARCH_DOMAINS = [
    'people', 'organizations', 'projects', 'research', 'counties',
    'cities', 'documents', 'events', 'tasks',
]

AI_EXECUTIVE_QUESTIONS = [
    'What should leadership focus on this week?',
    'Which counties need immediate support?',
    'What projects threaten January 2027?',
    'What trends should concern us?',
    'Where are opportunities?',
]

MC_ROLE_ACCESS = [
    {'role': 'county_leader', 'dashboards': ['MC-D05', 'MC-D04']},
    {'role': 'city_leader', 'dashboards': ['MC-D06', 'MC-D04']},
    {'role': 'organization_admin', 'dashboards': ['MC-D11']},
    {'role': 'research_contributor', 'dashboards': ['MC-D10']},
    {'role': 'executive', 'dashboards': 'all'},
    {'role': 'administrator', 'dashboards': 'all_plus_admin'},
]

REPORTING_INTEGRATIONS = [
    {'system': 'Build registry', 'registry': '/data/mission-control.json', 'route': '/mission-control/'},
    {'system': 'MC2 Executive', 'registry': '/data/mc2-executive.json', 'route': '/mission-control/executive.html'},
    {'system': 'Digital Twin', 'registry': '/data/institutional-digital-twin.json', 'route': '/mission-control/institutional-digital-twin.html'},
    {'system': 'Launch Certification', 'registry': '/data/institutional-launch-certification.json', 'route': '/mission-control/launch-certification.html'},
    {'system': 'Implementation Package', 'registry': '/data/cursor-implementation-package.json', 'route': '/mission-control/cursor-implementation-package.html'},
]

MISSION_CONTROL_ARCHITECTURE_MANIFEST = {
    'version': '1.0',
    'build': 101,
    'package': 'IMP-07',
    'updated': today,
    'title': 'Master Mission Control Architecture & Executive Command Center',
    'constitution': '/docs/IMPLEMENTATION_PACKAGE_07_MISSION_CONTROL.md',
    'source_registries': {
        'mission_control': '/data/mission-control.json',
        'mc2_executive': '/data/mc2-executive.json',
        'digital_twin': '/data/institutional-digital-twin.json',
        'launch_certification': '/data/institutional-launch-certification.json',
    },
    'philosophy': 'Mission Control is the institutional brain — stewardship, not data overload',
    'governing_principle': (
        'Leaders should never have to guess. Every important question answerable '
        'with evidence, clarity, and confidence.'
    ),
    'integration_rule': 'If it cannot be measured in Mission Control, it is not fully integrated',
    'executive_questions': EXECUTIVE_QUESTIONS,
    'stewardship_actions': STEWARDSHIP_ACTIONS,
    'executive_home_panels': EXECUTIVE_HOME_PANELS,
    'institutional_health_categories': INSTITUTIONAL_HEALTH_CATEGORIES,
    'health_category_count': len(INSTITUTIONAL_HEALTH_CATEGORIES),
    'january_2027_targets': {
        'completion_date': completion_target_date,
        'counties': 75,
        'cities': 250,
        'connected_voter_pct': 15,
        'arkansans_connected': 200000,
    },
    'january_2027_dashboard_metrics': JANUARY_2027_DASHBOARD_METRICS,
    'state_map_layers': STATE_MAP_LAYERS,
    'dashboards': MC_DASHBOARDS,
    'dashboard_count': len(MC_DASHBOARDS),
    'executive_calendar_sources': EXECUTIVE_CALENDAR_SOURCES,
    'executive_briefing_sections': EXECUTIVE_BRIEFING_SECTIONS,
    'alert_types': ALERT_TYPES,
    'alert_severity_levels': ALERT_SEVERITY_LEVELS,
    'digital_twin_visualizations': DIGITAL_TWIN_VISUALIZATIONS,
    'digital_twin_route': '/mission-control/institutional-digital-twin.html',
    'executive_search_domains': EXECUTIVE_SEARCH_DOMAINS,
    'ai_executive_questions': AI_EXECUTIVE_QUESTIONS,
    'mc_role_access': MC_ROLE_ACCESS,
    'reporting_integrations': REPORTING_INTEGRATIONS,
    'honest_metrics_rule': 'Mission Control tells the truth about itself. Never inflate completion.',
    'status': 'documented',
    'implemented': False,
}

ROUTE_MANIFEST = {
    'version': '1.0',
    'build': 101,
    'package': 'IMP-03',
    'updated': today,
    'title': 'Master Route Map & Complete Application Navigation',
    'constitution': '/docs/IMPLEMENTATION_PACKAGE_03_ROUTE_MAP.md',
    'source_registry': '/data/route-registry.json',
    'navigation_philosophy': 'Users arrive with questions, not departments',
    'navigation_questions': NAVIGATION_QUESTIONS,
    'primary_navigation': PRIMARY_NAVIGATION,
    'public_routes': PUBLIC_ROUTES,
    'account_routes': ACCOUNT_ROUTES,
    'workspace_routes': WORKSPACE_ROUTES,
    'system_routes': SYSTEM_ROUTES,
    'api_base': '/api/',
    'api_namespaces': API_NAMESPACES,
    'route_standards': ROUTE_STANDARDS,
    'mobile_nav_priority': MOBILE_NAV_PRIORITY,
    'total_routes_defined': len(PUBLIC_ROUTES) + len(ACCOUNT_ROUTES) + len(WORKSPACE_ROUTES) + len(SYSTEM_ROUTES),
    'status': 'documented',
    'implemented': False,
}

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
    {'id': 'CIP-D05', 'indicator': 'Technical Architecture (IMP-02)', 'current': 'Documented', 'status': 'partial'},
    {'id': 'CIP-D06', 'indicator': 'Route Map (IMP-03)', 'current': 'Documented', 'status': 'partial'},
    {'id': 'CIP-D07', 'indicator': 'Database Schema (IMP-04)', 'current': 'Documented', 'status': 'partial'},
    {'id': 'CIP-D08', 'indicator': 'Identity & Auth (IMP-05)', 'current': 'Documented', 'status': 'partial'},
    {'id': 'CIP-D09', 'indicator': 'Design System (IMP-06)', 'current': 'Documented', 'status': 'partial'},
    {'id': 'CIP-D10', 'indicator': 'Mission Control Architecture (IMP-07)', 'current': 'Documented', 'status': 'partial'},
    {'id': 'CIP-D11', 'indicator': 'Sprint Zero started', 'current': 'Yes' if sprint_zero_started else 'No', 'status': 'planned'},
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
            'status': 'documented',
        },
    },
    'technical_architecture': {
        'title': 'Master Technical Architecture & Repository Blueprint',
        'package': 'Implementation Package 2 of 50',
        'route': '/docs/IMPLEMENTATION_PACKAGE_02_TECHNICAL_ARCHITECTURE.md',
        'status': 'documented',
        'documented_date': today,
        'philosophy': 'One Institution → One Repository → Many Modules → Shared Foundation',
        'technology_stack': {
            'frontend': ['React', 'Next.js', 'TypeScript'],
            'backend': ['Node.js', 'Next.js Server Actions / API Routes'],
            'database': ['PostgreSQL'],
            'auth': ['Secure role-based authentication'],
            'storage': ['Object storage for media and documents'],
            'search': ['Full-text search with structured indexing'],
            'ai': ['OpenAI integration with LocalBrains'],
            'deployment': ['Production cloud deployment with automated CI/CD'],
        },
        'repository_layers': [
            'app', 'components', 'features', 'lib', 'ai', 'mission-control',
            'database', 'docs', 'public', 'content', 'data', 'scripts',
            'tests', 'infrastructure', 'config',
        ],
        'module_standards': [
            'Purpose', 'Routes', 'Components', 'Services', 'Database models',
            'AI integration', 'Mission Control metrics', 'Documentation', 'Tests',
        ],
        'next_package': {
            'number': 3,
            'id': 'IMP-03',
            'title': 'Master Route Map & Complete Application Navigation',
            'status': 'documented',
        },
    },
    'route_map': {
        'title': 'Master Route Map & Complete Application Navigation',
        'package': 'Implementation Package 3 of 50',
        'route': '/docs/IMPLEMENTATION_PACKAGE_03_ROUTE_MAP.md',
        'manifest': '/data/route-manifest.json',
        'status': 'documented',
        'documented_date': today,
        'navigation_philosophy': 'Users arrive with questions, not departments',
        'primary_navigation_count': len(PRIMARY_NAVIGATION),
        'total_routes_defined': ROUTE_MANIFEST['total_routes_defined'],
        'api_namespaces': API_NAMESPACES,
        'mobile_nav_priority': MOBILE_NAV_PRIORITY,
        'next_package': {
            'number': 4,
            'id': 'IMP-04',
            'title': 'Master Database Schema & Canonical Data Model',
            'status': 'documented',
        },
    },
    'database_schema': {
        'title': 'Master Database Schema & Canonical Data Model',
        'package': 'Implementation Package 4 of 50',
        'route': '/docs/IMPLEMENTATION_PACKAGE_04_DATABASE_SCHEMA.md',
        'manifest': '/data/canonical-data-manifest.json',
        'prisma_draft': '/prisma/schema.prisma',
        'status': 'documented',
        'documented_date': today,
        'philosophy': 'Every important entity exists once; everything else references it',
        'domain_count': len(DOMAINS),
        'total_tables_defined': total_domain_tables,
        'universal_record_standards_count': len(UNIVERSAL_RECORD_STANDARDS),
        'visibility_levels': VISIBILITY_LEVELS,
        'schema_entity_count': CANONICAL_DATA_MANIFEST['schema_entity_count'],
        'prisma_models_drafted': CANONICAL_DATA_MANIFEST['prisma_models_drafted'],
        'next_package': {
            'number': 5,
            'id': 'IMP-05',
            'title': 'Master Identity, Authentication, Roles & Permissions',
            'status': 'documented',
        },
    },
    'identity_auth': {
        'title': 'Master Identity, Authentication, Roles & Permissions',
        'package': 'Implementation Package 5 of 50',
        'route': '/docs/IMPLEMENTATION_PACKAGE_05_IDENTITY_AUTH.md',
        'manifest': '/data/identity-auth-manifest.json',
        'status': 'documented',
        'documented_date': today,
        'philosophy': 'One person → one identity → many roles → personalized experience',
        'role_count': IDENTITY_AUTH_MANIFEST['role_count'],
        'permission_category_count': IDENTITY_AUTH_MANIFEST['permission_category_count'],
        'auth_providers': [p['id'] for p in AUTH_PROVIDERS if p['status'] == 'recommended'],
        'onboarding_step_count': len(ONBOARDING_STEPS),
        'multi_role_supported': True,
        'next_package': {
            'number': 6,
            'id': 'IMP-06',
            'title': 'Master Design System, User Experience & Visual Language',
            'status': 'documented',
        },
    },
    'design_system': {
        'title': 'Master Design System, User Experience & Visual Language',
        'package': 'Implementation Package 6 of 50',
        'route': '/docs/IMPLEMENTATION_PACKAGE_06_DESIGN_SYSTEM.md',
        'manifest': '/data/design-system-manifest.json',
        'status': 'documented',
        'documented_date': today,
        'philosophy': DESIGN_SYSTEM_MANIFEST['philosophy'],
        'component_count': DESIGN_SYSTEM_MANIFEST['component_count'],
        'card_type_count': DESIGN_SYSTEM_MANIFEST['card_type_count'],
        'live_component_count': DESIGN_SYSTEM_MANIFEST['live_component_count'],
        'accessibility_wcag': DESIGN_SYSTEM_MANIFEST['accessibility_wcag'],
        'mobile_priorities': MOBILE_PRIORITIES,
        'next_package': {
            'number': 7,
            'id': 'IMP-07',
            'title': 'Master Mission Control Architecture & Executive Command Center',
            'status': 'documented',
        },
    },
    'mission_control_architecture': {
        'title': 'Master Mission Control Architecture & Executive Command Center',
        'package': 'Implementation Package 7 of 50',
        'route': '/docs/IMPLEMENTATION_PACKAGE_07_MISSION_CONTROL.md',
        'manifest': '/data/mission-control-architecture-manifest.json',
        'status': 'documented',
        'documented_date': today,
        'philosophy': MISSION_CONTROL_ARCHITECTURE_MANIFEST['philosophy'],
        'executive_question_count': len(EXECUTIVE_QUESTIONS),
        'dashboard_count': MISSION_CONTROL_ARCHITECTURE_MANIFEST['dashboard_count'],
        'health_category_count': MISSION_CONTROL_ARCHITECTURE_MANIFEST['health_category_count'],
        'alert_type_count': len(ALERT_TYPES),
        'executive_questions': [q['question'] for q in EXECUTIVE_QUESTIONS],
        'next_package': {
            'number': 8,
            'id': 'IMP-08',
            'title': 'Master LocalBrain Architecture & Institutional AI Network',
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

with open(root / 'data/route-manifest.json', 'w', newline='\n') as f:
    json.dump(ROUTE_MANIFEST, f, indent=2)
    f.write('\n')

with open(root / 'data/canonical-data-manifest.json', 'w', newline='\n') as f:
    json.dump(CANONICAL_DATA_MANIFEST, f, indent=2)
    f.write('\n')

with open(root / 'data/identity-auth-manifest.json', 'w', newline='\n') as f:
    json.dump(IDENTITY_AUTH_MANIFEST, f, indent=2)
    f.write('\n')

with open(root / 'data/design-system-manifest.json', 'w', newline='\n') as f:
    json.dump(DESIGN_SYSTEM_MANIFEST, f, indent=2)
    f.write('\n')

with open(root / 'data/mission-control-architecture-manifest.json', 'w', newline='\n') as f:
    json.dump(MISSION_CONTROL_ARCHITECTURE_MANIFEST, f, indent=2)
    f.write('\n')

print(
    f'Implementation Package: {len(IMPLEMENTATION_STEPS)} steps, '
    f'{len(BANDS)} bands, {implementation_package_readiness}% readiness, '
    f'{steps_documented} documented, {steps_implemented} implemented'
)
