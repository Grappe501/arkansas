"""
Generate data/cursor-implementation-package.json — Build #101.
Cursor Implementation Package — 50 executable implementation steps v1.0.
"""
import json
from datetime import date
from pathlib import Path

root = Path(__file__).resolve().parents[1]
today = '2026-07-09'
software_completion_date = '2026-07-11'
county_milestone_date = '2026-10-01'
organizational_readiness_date = '2027-01-01'
software_completion = date(2026, 7, 11)
county_milestone = date(2026, 10, 1)
organizational_readiness = date(2027, 1, 1)
today_date = date(2026, 7, 9)
engagement_goal_pct = 15
target_cities = 250
arkansans_connected_goal = 200000
days_to_software = max((software_completion - today_date).days, 0)
days_to_county_milestone = max((county_milestone - today_date).days, 0)
days_to_organizational = max((organizational_readiness - today_date).days, 0)
# Backward-compatible aliases used across registries
completion_target_date = organizational_readiness_date
days_remaining = days_to_organizational

MASTER_TIMELINE = {
    'phase_one': {
        'id': 'software_completion',
        'title': 'Software Completion',
        'target_date': software_completion_date,
        'days_remaining': days_to_software,
        'scope': [
            'Public website', 'Mission Control', 'LocalBrains', 'Community Education Academy',
            'Knowledge Platform', 'Research system', 'Volunteer system', 'Coalition system',
            'County, City, and Neighborhood systems', 'AI infrastructure', 'Administrative tools',
        ],
    },
    'phase_two': {
        'id': 'county_milestone',
        'title': '75 Counties by October 1',
        'target_date': county_milestone_date,
        'days_remaining': days_to_county_milestone,
        'scope': [
            'Completed county profile for all 75 counties',
            'Education Leader or active recruitment contact per county',
            'County dashboard operational in Mission Control',
            'Initial local resource information',
            'Development plan for continued growth per county',
        ],
    },
    'phase_three': {
        'id': 'organizational_readiness',
        'title': 'Organizational Readiness',
        'target_date': organizational_readiness_date,
        'days_remaining': days_to_organizational,
        'focus': [
            'Recruiting Education Leaders', 'Expanding county coverage', 'Growing city leadership',
            'Coalition development', 'Volunteer training', 'Community conversations',
            'Research expansion', 'Public testing', 'User feedback', 'System refinement',
            'Launch certification', 'City and neighborhood systems mature',
            'Statewide volunteer development expanded',
        ],
    },
    'sequence': (
        'Software Complete (Jul 11, 2026) → 75 Counties (Oct 1, 2026) → '
        'Organizational Readiness (Jan 2027)'
    ),
    'build_out_months_approx': 6,
    'county_milestone': {
        'target_date': county_milestone_date,
        'counties_total': 75,
        'days_remaining': days_to_county_milestone,
        'label': '75-by-October-1 Milestone',
    },
}


def load_json(path):
    if path.exists():
        with open(path, encoding='utf-8') as f:
            return json.load(f)
    return {}


mc = load_json(root / 'data/mission-control.json')
ex = mc.get('executive', {})

# Honest operational metrics
steps_implemented = 0
steps_documented = 29  # IMP-01 through IMP-29 (doctrinal)
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
        'package_label': 'Implementation Package 8 of 50',
        'title': 'Master LocalBrain Architecture & Institutional AI Network',
        'summary': 'Distributed intelligence — 20 LocalBrains, common architecture, brain contracts, executive and personal AI',
        'deliverables': [
            'docs/IMPLEMENTATION_PACKAGE_08_LOCALBRAIN_ARCHITECTURE.md',
            'data/localbrain-network-manifest.json',
            'LocalBrain Architecture', 'Institutional AI Network', 'Department Intelligence Model',
            'Knowledge Synchronization Rules', 'Calendar Integration', 'AI Agent Structure',
            'Brain Communication Contracts', 'Executive AI Architecture',
            'Personal AI Architecture', 'Mission Control Reporting Standards',
        ],
        'acceptance_criteria': [
            'LocalBrain definition: memory, knowledge, calendar, projects, tasks, agents, reports, dashboards',
            'Twenty LocalBrains documented with common module architecture',
            'Brain contracts, communication flow, memory rules, and knowledge sync defined',
            'AI safety rules, MC integration, executive AI, and personal AI documented',
            'Brain lifecycle and modular future expansion specified',
            'Mission Control observes entire network; no monolithic AI',
        ],
        'source_blueprints': [
            '/data/localbrain-network-manifest.json',
            '/data/localbrain-architecture.json',
            '/docs/MASTER_LOCALBRAIN_ARCHITECTURE.md',
            '/docs/IMPLEMENTATION_PACKAGE_07_MISSION_CONTROL.md',
        ],
        'constitution': '/docs/IMPLEMENTATION_PACKAGE_08_LOCALBRAIN_ARCHITECTURE.md',
        'manifest': '/data/localbrain-network-manifest.json',
        'status': 'documented',
        'documented_date': today,
    },
    {
        'number': 9, 'id': 'IMP-09', 'band': 'A',
        'package_label': 'Implementation Package 9 of 50',
        'title': 'Master Knowledge Graph, Semantic Search & Institutional Memory',
        'summary': 'Relationship ontology, semantic search, institutional memory, AI retrieval, knowledge health — dual timeline Jul 2026 / Jan 2027',
        'deliverables': [
            'docs/IMPLEMENTATION_PACKAGE_09_KNOWLEDGE_GRAPH.md',
            'data/knowledge-graph-manifest.json',
            'Knowledge Graph Architecture', 'Semantic Search Model', 'Institutional Memory Framework',
            'Relationship Ontology', 'AI Retrieval Standards', 'Knowledge Health Metrics',
            'Mission Control Knowledge Dashboards', 'Updated Master Timeline',
        ],
        'acceptance_criteria': [
            'Dual timeline documented: software complete Jul 11 2026; organizational readiness Jan 2027',
            'Core node types and relationship ontology defined',
            'Semantic search model specified (concepts not keywords alone)',
            'Institutional memory and knowledge health metrics documented',
            'LocalBrain and Mission Control integration with shared graph foundation',
            'Every LocalBrain has a shared knowledge foundation',
        ],
        'source_blueprints': [
            '/data/knowledge-graph-manifest.json',
            '/data/knowledge-graph.json',
            '/data/kg-registry.json',
            '/data/knowledge-atlas.json',
            '/docs/IMPLEMENTATION_PACKAGE_08_LOCALBRAIN_ARCHITECTURE.md',
        ],
        'constitution': '/docs/IMPLEMENTATION_PACKAGE_09_KNOWLEDGE_GRAPH.md',
        'manifest': '/data/knowledge-graph-manifest.json',
        'status': 'documented',
        'documented_date': today,
    },
    {
        'number': 10, 'id': 'IMP-10', 'band': 'A',
        'title': 'Sprint Zero: engineering foundation and exit gate',
        'summary': 'Migration, stack, Netlify, Git, CI, env matrix, CONTRIBUTING, Sprint Zero checklist — gate before Band B',
        'deliverables': [
            'docs/MIGRATION_PLAN.md', 'docs/REPO_AUDIT.md', 'app/README.md',
            'docs/STACK.md', 'docs/SERVICE_BOUNDARIES.md', 'docs/DEPLOYMENT_TOPOLOGY.md',
            'netlify.toml', 'docs/DEPLOYMENT.md', 'docs/GIT_WORKFLOW.md',
            '.github/workflows/ci.yml', 'package.json scripts section', 'docs/SCRIPTS.md',
            '.env.example', 'docs/ENVIRONMENT.md',
            'docs/SPRINT_ZERO_CHECKLIST.md', 'CONTRIBUTING.md',
        ],
        'acceptance_criteria': [
            'IMP-01 through IMP-10 documented; dual timeline aligned across registries',
            'Migration strategy, stack lock, Netlify, Git, CI, env documented and verified',
            'CONTRIBUTING.md links to implementation packages and CURSOR_MASTER_BUILD_PROMPT.md',
            'One successful Netlify preview deploy from develop',
            'Executive sign-off field in checklist (manual)',
        ],
        'source_blueprints': [
            '/data/cursor-implementation-package.json',
            '/docs/IMPLEMENTATION_PACKAGE_02_TECHNICAL_ARCHITECTURE.md',
            '/data/repository-blueprint.json',
            '/netlify.toml', '/package.json', '/scripts/',
        ],
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
        'completion_date': organizational_readiness_date,
        'software_completion_date': software_completion_date,
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

LOCALBRAINS = [
    {'id': 'LB-01', 'name': 'Mission Control Brain', 'domain': 'executive', 'route': '/mission-control/'},
    {'id': 'LB-02', 'name': 'Research Brain', 'domain': 'research', 'route': '/mission-control/arkansas-research-institute.html'},
    {'id': 'LB-03', 'name': 'Evidence Brain', 'domain': 'evidence', 'route': '/mission-control/evidence-ledger.html'},
    {'id': 'LB-04', 'name': 'Claims Brain', 'domain': 'claims', 'route': '/mission-control/facts.html'},
    {'id': 'LB-05', 'name': 'Knowledge Platform Brain', 'domain': 'knowledge', 'route': '/mission-control/knowledge-graph.html'},
    {'id': 'LB-06', 'name': 'Community Education Academy Brain', 'domain': 'academy', 'route': '/mission-control/education-academy.html'},
    {'id': 'LB-07', 'name': 'Volunteer Brain', 'domain': 'volunteers', 'route': '/mission-control/volunteer-funding-constitution.html'},
    {'id': 'LB-08', 'name': 'County Operations Brain', 'domain': 'county', 'route': '/mission-control/arkansas-county-operating-system.html'},
    {'id': 'LB-09', 'name': 'City Operations Brain', 'domain': 'city', 'route': '/mission-control/arkansas-city-operating-system.html'},
    {'id': 'LB-10', 'name': 'Neighborhood Operations Brain', 'domain': 'neighborhood', 'route': '/mission-control/arkansas-neighborhood-operating-system.html'},
    {'id': 'LB-11', 'name': 'Coalition Brain', 'domain': 'coalition', 'route': '/mission-control/coalition-network.html'},
    {'id': 'LB-12', 'name': 'Communications Brain', 'domain': 'communications', 'route': '/mission-control/arkansas-communications.html'},
    {'id': 'LB-13', 'name': 'Media Brain', 'domain': 'media', 'route': '/mission-control/media-studio.html'},
    {'id': 'LB-14', 'name': 'Technology Brain', 'domain': 'technology', 'route': '/mission-control/technical-architecture.html'},
    {'id': 'LB-15', 'name': 'Governance Brain', 'domain': 'governance', 'route': '/mission-control/governance.html'},
    {'id': 'LB-16', 'name': 'PMO Brain', 'domain': 'pmo', 'route': '/mission-control/pmo-execution-office.html'},
    {'id': 'LB-17', 'name': 'Calendar Brain', 'domain': 'calendar', 'route': '/mission-control/execution-schedule.html'},
    {'id': 'LB-18', 'name': 'Relationship Brain', 'domain': 'relationships', 'route': '/mission-control/relationship-os.html'},
    {'id': 'LB-19', 'name': 'Campaign Finance Brain', 'domain': 'campaign_finance', 'route': '/mission-control/campaign-finance-observatory.html'},
    {'id': 'LB-20', 'name': 'Public Engagement Brain', 'domain': 'public_engagement', 'route': '/mission-control/arkansas-community-listening.html'},
]

LOCALBRAIN_CORE_MODULES = [
    {
        'id': 'knowledge_vault',
        'name': 'Knowledge Vault',
        'stores': ['policies', 'research', 'documents', 'templates', 'historical_decisions', 'reference_material'],
    },
    {
        'id': 'operational_memory',
        'name': 'Operational Memory',
        'stores': ['open_work', 'past_work', 'lessons_learned', 'meeting_summaries', 'decision_history', 'volunteer_observations'],
    },
    {
        'id': 'calendar_engine',
        'name': 'Calendar Engine',
        'stores': ['meetings', 'deadlines', 'review_schedules', 'projects', 'volunteer_activities', 'recurring_responsibilities'],
    },
    {
        'id': 'project_workspace',
        'name': 'Project Workspace',
        'stores': ['active_projects', 'tasks', 'dependencies', 'milestones', 'risks', 'assignments'],
    },
    {
        'id': 'ai_team',
        'name': 'AI Team',
        'description': 'Specialized AI agents per domain',
    },
]

LOCALBRAIN_DEFINITION_FIELDS = [
    'memory', 'knowledge', 'calendar', 'projects', 'tasks', 'ai_agents',
    'reports', 'dashboards', 'institutional_rules', 'department_history',
]

BRAIN_CONTRACT_PUBLISHES = [
    'available_knowledge', 'supported_actions', 'reports', 'metrics', 'events', 'requests',
]

COMMUNICATION_FLOW = [
    'research_brain', 'evidence_brain', 'academy_brain', 'county_brain',
    'communications_brain', 'mission_control',
]

RESEARCH_BRAIN_AGENTS = [
    'research_assistant', 'citation_assistant', 'legal_research_assistant',
    'source_verification_assistant', 'writing_assistant', 'review_assistant',
]

MEMORY_RULES = [
    {'brain': 'research_brain', 'remembers': 'citations and sources'},
    {'brain': 'volunteer_brain', 'remembers': 'volunteer activity'},
    {'brain': 'calendar_brain', 'remembers': 'schedules and deadlines'},
    {'brain': 'mission_control_brain', 'remembers': 'summaries across all brains'},
]

CALENDAR_BRAIN_AGGREGATES = [
    'research_deadlines', 'volunteer_meetings', 'community_conversations',
    'leadership_meetings', 'academy_schedule', 'technology_releases',
    'annual_reviews', 'executive_priorities',
]

RELATIONSHIP_BRAIN_MAINTAINS = [
    'volunteer_relationships', 'organization_relationships', 'county_relationships',
    'mentorship', 'education_leader_connections', 'community_conversations',
]

AI_SAFETY_RULES = [
    'reference_institutional_knowledge', 'identify_uncertainty', 'respect_permissions',
    'protect_confidential_information', 'escalate_significant_decisions',
    'avoid_speculation_presented_as_fact',
]

MC_LOCALBRAIN_REPORTS = [
    'health', 'workload', 'projects', 'knowledge_growth',
    'calendar_status', 'volunteer_activity', 'recommendations',
]

EXECUTIVE_AI_QUESTIONS = [
    'Which departments are overloaded?',
    'Which counties need support?',
    'What research should be prioritized?',
    'Which volunteers need mentoring?',
    'Where are institutional risks increasing?',
]

PERSONAL_AI_CAPABILITIES = [
    'retrieve_research', 'recommend_courses', 'schedule_meetings', 'locate_volunteers',
    'summarize_county_activity', 'prepare_presentations',
]

BRAIN_LIFECYCLE = [
    'observe', 'remember', 'organize', 'recommend', 'assist', 'learn', 'improve',
]

FUTURE_LOCALBRAINS = [
    'legislative_tracking', 'public_records', 'election_administration',
    'historical_archives', 'media_monitoring', 'grant_development',
    'youth_leadership', 'university_partnerships',
]

LOCALBRAIN_NETWORK_MANIFEST = {
    'version': '1.0',
    'build': 101,
    'package': 'IMP-08',
    'updated': today,
    'title': 'Master LocalBrain Architecture & Institutional AI Network',
    'constitution': '/docs/IMPLEMENTATION_PACKAGE_08_LOCALBRAIN_ARCHITECTURE.md',
    'source_registries': {
        'localbrain_architecture': '/data/localbrain-architecture.json',
        'master_doc': '/docs/MASTER_LOCALBRAIN_ARCHITECTURE.md',
        'mission_control_architecture': '/data/mission-control-architecture-manifest.json',
        'canonical_data': '/data/canonical-data-manifest.json',
    },
    'philosophy': 'Distributed intelligence — Mission Control is executive brain; LocalBrains are departmental brains',
    'governing_principle': (
        'A single AI eventually reaches its limits. An institution built on '
        'specialized intelligence does not.'
    ),
    'localbrain_definition': LOCALBRAIN_DEFINITION_FIELDS,
    'localbrains': LOCALBRAINS,
    'localbrain_count': len(LOCALBRAINS),
    'modular_expansion': True,
    'core_modules': LOCALBRAIN_CORE_MODULES,
    'brain_contract_publishes': BRAIN_CONTRACT_PUBLISHES,
    'communication_flow': COMMUNICATION_FLOW,
    'research_brain_agents_example': RESEARCH_BRAIN_AGENTS,
    'memory_rules': MEMORY_RULES,
    'calendar_brain_aggregates': CALENDAR_BRAIN_AGGREGATES,
    'relationship_brain_maintains': RELATIONSHIP_BRAIN_MAINTAINS,
    'knowledge_sync': {
        'platform': 'Knowledge Platform Brain',
        'rule': 'Single source of truth — no conflicting departmental copies',
    },
    'ai_safety_rules': AI_SAFETY_RULES,
    'mission_control_reports': MC_LOCALBRAIN_REPORTS,
    'executive_ai_questions': EXECUTIVE_AI_QUESTIONS,
    'personal_ai_route': '/ai',
    'personal_ai_capabilities': PERSONAL_AI_CAPABILITIES,
    'brain_lifecycle': BRAIN_LIFECYCLE,
    'future_localbrains': FUTURE_LOCALBRAINS,
    'status': 'documented',
    'implemented': False,
}

KNOWLEDGE_NODE_TYPES = [
    'people', 'organizations', 'locations', 'research', 'legal_authorities',
    'educational_content', 'projects', 'events', 'institutional_assets',
    'policies', 'media', 'ai_agents', 'localbrains',
]

RELATIONSHIP_ONTOLOGY = [
    {'from': 'person', 'relationship': 'volunteers_in', 'to': 'county'},
    {'from': 'education_leader', 'relationship': 'serves', 'to': 'city'},
    {'from': 'research_article', 'relationship': 'references', 'to': 'court_case'},
    {'from': 'lesson', 'relationship': 'explains', 'to': 'claim'},
    {'from': 'claim', 'relationship': 'supported_by', 'to': 'evidence'},
    {'from': 'volunteer', 'relationship': 'member_of', 'to': 'organization'},
    {'from': 'organization', 'relationship': 'operates_in', 'to': 'county'},
    {'from': 'community_conversation', 'relationship': 'occurred_in', 'to': 'neighborhood'},
]

GRAPH_CONNECTED_ENTITIES = [
    'people', 'organizations', 'counties', 'cities', 'neighborhoods',
    'court_cases', 'research_papers', 'evidence', 'claims', 'lessons', 'courses',
    'projects', 'events', 'volunteers', 'education_leaders', 'community_conversations',
]

SEMANTIC_SEARCH_EXAMPLE = {
    'query': 'Money in politics',
    'discovers': [
        'campaign_finance', 'political_spending', 'independent_expenditures',
        'disclosure', 'citizens_united', 'court_decisions', 'educational_lessons',
        'related_organizations',
    ],
    'principle': 'Concepts, not keywords alone',
}

INSTITUTIONAL_MEMORY_EVENTS = [
    'leadership_decisions', 'research_revisions', 'volunteer_milestones',
    'community_conversations', 'project_completions', 'policy_updates',
]

KNOWLEDGE_HEALTH_METRICS = [
    'orphaned_records', 'broken_relationships', 'duplicate_entities',
    'missing_citations', 'unreviewed_content', 'knowledge_freshness',
    'institutional_memory_quality',
]

MC_KNOWLEDGE_VISUALIZATIONS = [
    'knowledge_growth', 'relationship_density', 'research_completeness',
    'county_knowledge', 'volunteer_connections', 'coalition_development', 'knowledge_gaps',
]

KNOWLEDGE_GRAPH_MANIFEST = {
    'version': '1.0',
    'build': 101,
    'package': 'IMP-09',
    'updated': today,
    'title': 'Master Knowledge Graph, Semantic Search & Institutional Memory',
    'constitution': '/docs/IMPLEMENTATION_PACKAGE_09_KNOWLEDGE_GRAPH.md',
    'source_registries': {
        'knowledge_graph': '/data/knowledge-graph.json',
        'kg_registry': '/data/kg-registry.json',
        'knowledge_atlas': '/data/knowledge-atlas.json',
        'canonical_data': '/data/canonical-data-manifest.json',
        'localbrain_network': '/data/localbrain-network-manifest.json',
    },
    'philosophy': 'Everything is connected; the Knowledge Graph explains relationships',
    'governing_principle': 'Knowledge has value only when it is connected',
    'master_timeline': MASTER_TIMELINE,
    'software_completion_date': software_completion_date,
    'organizational_readiness_date': organizational_readiness_date,
    'days_to_software': days_to_software,
    'days_to_organizational': days_to_organizational,
    'knowledge_node_types': KNOWLEDGE_NODE_TYPES,
    'node_type_count': len(KNOWLEDGE_NODE_TYPES),
    'relationship_ontology': RELATIONSHIP_ONTOLOGY,
    'graph_connected_entities': GRAPH_CONNECTED_ENTITIES,
    'semantic_search': SEMANTIC_SEARCH_EXAMPLE,
    'institutional_memory_events': INSTITUTIONAL_MEMORY_EVENTS,
    'knowledge_health_metrics': KNOWLEDGE_HEALTH_METRICS,
    'mc_knowledge_visualizations': MC_KNOWLEDGE_VISUALIZATIONS,
    'ai_integration': {
        'rule': 'Every LocalBrain retrieves from the graph; AI answers via relationships and evidence',
        'localbrain_manifest': '/data/localbrain-network-manifest.json',
    },
    'status': 'documented',
    'implemented': False,
}

CMS_CONTENT_CLASSES = {
    'research': [
        'white_papers', 'court_case_analysis', 'legal_summaries', 'historical_research',
        'arkansas_research', 'academic_reviews',
    ],
    'education': [
        'lessons', 'courses', 'learning_paths', 'glossary', 'faqs', 'study_guides',
        'discussion_guides', 'presentations',
    ],
    'public_information': [
        'articles', 'news', 'announcements', 'reports', 'press_releases', 'community_updates',
    ],
    'institutional': [
        'policies', 'operating_manuals', 'implementation_packages', 'training_guides',
        'volunteer_handbook', 'governance_documents',
    ],
    'media': [
        'videos', 'infographics', 'podcasts', 'presentations', 'images',
        'downloadable_pdfs', 'interactive_timelines',
    ],
}

CMS_PUBLISHING_PRINCIPLES = [
    'accurate', 'verifiable', 'understandable', 'accessible', 'versioned',
    'reviewable', 'searchable', 'ai_assisted', 'mission_control_aware',
]

EDITORIAL_WORKFLOW_STAGES = [
    {'stage': 'draft', 'title': 'Draft'},
    {'stage': 'ai_review', 'title': 'AI Review'},
    {'stage': 'editorial_review', 'title': 'Editorial Review'},
    {'stage': 'evidence_verification', 'title': 'Evidence Verification'},
    {'stage': 'accessibility_review', 'title': 'Accessibility Review'},
    {'stage': 'legal_policy_review', 'title': 'Legal/Policy Review', 'optional': True},
    {'stage': 'approval', 'title': 'Approval'},
    {'stage': 'publication', 'title': 'Publication'},
    {'stage': 'mc_indexing', 'title': 'Mission Control Indexing'},
    {'stage': 'periodic_review', 'title': 'Periodic Review'},
]

CONTENT_METADATA_FIELDS = [
    'title', 'summary', 'author', 'editor', 'publication_date', 'last_reviewed',
    'review_schedule', 'reading_time', 'difficulty_level', 'categories', 'tags',
    'geographic_relevance', 'related_resources',
]

CONTENT_RELATIONSHIP_TARGETS = [
    'related_research', 'related_lessons', 'related_counties', 'related_organizations',
    'related_events', 'related_court_cases', 'related_glossary_terms', 'related_faqs',
]

EVIDENCE_LINK_TYPES = [
    'primary_source', 'court_opinion', 'government_document',
    'academic_publication', 'historical_record',
]

REVIEW_CYCLE_TRIGGERS = [
    'quarterly', 'annually', 'major_legal_developments', 'new_arkansas_legislation',
]

DISCOVERY_DIMENSIONS = [
    'keyword', 'topic', 'question', 'county', 'city', 'court_case',
    'organization', 'learning_level', 'content_type',
]

AI_EDITORIAL_CAPABILITIES = [
    'summarize', 'proofread', 'suggest_citations', 'identify_unsupported_claims',
    'recommend_related_research', 'suggest_glossary_links', 'generate_faqs',
    'create_lesson_versions', 'prepare_presentation_outlines',
]

WORKSPACE_FEATURES = [
    'rich_text_editing', 'markdown_support', 'citation_insertion', 'evidence_linking',
    'ai_writing_assistance', 'version_comparison', 'reading_level_analysis',
    'accessibility_suggestions', 'related_content_recommendations',
]

PUBLIC_FEEDBACK_ACTIONS = [
    'report_error', 'suggest_source', 'request_clarification',
    'recommend_improvements', 'ask_questions',
]

MC_PUBLISHING_METRICS = [
    'articles_published', 'research_completed', 'pages_awaiting_review',
    'citation_completeness', 'editorial_backlog', 'review_compliance',
    'most_viewed_resources', 'search_success', 'knowledge_growth',
]

FOUNDATIONAL_ARCHITECTURE_PACKAGES = [
    'institutional_constitution', 'technical_architecture', 'route_map',
    'canonical_data_model', 'identity_permissions', 'design_system',
    'mission_control', 'localbrain_network', 'knowledge_graph', 'publishing_system',
]

CONTENT_MANAGEMENT_MANIFEST = {
    'version': '1.0',
    'build': 101,
    'package': 'IMP-10',
    'updated': today,
    'title': 'Master Content Management System, Research Publishing & Editorial Workflow',
    'constitution': '/docs/IMPLEMENTATION_PACKAGE_10_CONTENT_MANAGEMENT.md',
    'source_registries': {
        'content_production_factory': '/data/content-production-factory.json',
        'content_production_matrix': '/data/content-production-matrix.json',
        'content_inventory': '/data/content-inventory.json',
        'knowledge_graph': '/data/knowledge-graph-manifest.json',
        'canonical_data': '/data/canonical-data-manifest.json',
    },
    'philosophy': 'Institutional Knowledge Publishing System — not a blogging platform',
    'governing_principle': (
        'Software makes publication possible; research makes publication valuable; '
        'trust is earned one publication at a time'
    ),
    'master_timeline': MASTER_TIMELINE,
    'software_completion_date': software_completion_date,
    'organizational_readiness_date': organizational_readiness_date,
    'days_to_software': days_to_software,
    'days_to_organizational': days_to_organizational,
    'content_classes': CMS_CONTENT_CLASSES,
    'content_type_count': sum(len(v) for v in CMS_CONTENT_CLASSES.values()),
    'content_class_count': len(CMS_CONTENT_CLASSES),
    'publishing_principles': CMS_PUBLISHING_PRINCIPLES,
    'editorial_workflow': EDITORIAL_WORKFLOW_STAGES,
    'workflow_stage_count': len(EDITORIAL_WORKFLOW_STAGES),
    'content_metadata_fields': CONTENT_METADATA_FIELDS,
    'content_relationship_targets': CONTENT_RELATIONSHIP_TARGETS,
    'evidence_link_types': EVIDENCE_LINK_TYPES,
    'review_cycle_triggers': REVIEW_CYCLE_TRIGGERS,
    'discovery_dimensions': DISCOVERY_DIMENSIONS,
    'ai_editorial_capabilities': AI_EDITORIAL_CAPABILITIES,
    'ai_publish_rule': 'AI assists but never publishes independently',
    'workspace_features': WORKSPACE_FEATURES,
    'public_feedback_actions': PUBLIC_FEEDBACK_ACTIONS,
    'mc_publishing_metrics': MC_PUBLISHING_METRICS,
    'foundational_architecture': FOUNDATIONAL_ARCHITECTURE_PACKAGES,
    'packages_completed': 10,
    'packages_total': 50,
    'foundation_complete_pct': 20,
    'engineering_note': 'Doctrinal IMP-10 CMS; engineering IMP-10 in step registry is Sprint Zero gate',
    'status': 'documented',
    'implemented': False,
}

RESEARCH_PROGRAMS = [
    'citizens_united', 'campaign_finance', 'arkansas_government', 'federal_government',
    'constitutional_law', 'supreme_court_decisions', 'election_administration',
    'ballot_initiatives', 'government_transparency', 'civic_participation',
    'historical_research', 'comparative_state_research',
]

RESEARCH_LIFECYCLE_STAGES = [
    {'stage': 'research_question', 'title': 'Research Question'},
    {'stage': 'research_plan', 'title': 'Research Plan'},
    {'stage': 'evidence_collection', 'title': 'Evidence Collection'},
    {'stage': 'source_evaluation', 'title': 'Source Evaluation'},
    {'stage': 'claim_development', 'title': 'Claim Development'},
    {'stage': 'evidence_verification', 'title': 'Evidence Verification'},
    {'stage': 'editorial_review', 'title': 'Editorial Review'},
    {'stage': 'publication', 'title': 'Publication'},
    {'stage': 'monitoring', 'title': 'Monitoring'},
    {'stage': 'periodic_review', 'title': 'Periodic Review'},
]

EVIDENCE_LEDGER_FIELDS = [
    'claim', 'supporting_evidence', 'primary_sources', 'secondary_sources',
    'date_reviewed', 'reviewer', 'confidence_level', 'related_research',
]

CLAIMS_REGISTRY_FIELDS = [
    'claim_id', 'plain_language_statement', 'supporting_evidence',
    'contrary_evidence', 'status', 'review_history', 'related_educational_resources',
]

SOURCE_EVALUATION_CRITERIA = [
    'authority', 'originality', 'reliability', 'timeliness', 'bias_considerations', 'relevance',
]

AI_RESEARCH_CAPABILITIES = [
    'find_related_materials', 'summarize_documents', 'identify_missing_evidence',
    'compare_sources', 'draft_literature_reviews', 'generate_citation_suggestions',
    'highlight_conflicting_information',
]

PEER_REVIEW_CRITERIA = [
    'accuracy', 'evidence_quality', 'citation_completeness', 'clarity', 'educational_value',
]

RESEARCH_WORKSPACE_FEATURES = [
    'manage_projects', 'organize_evidence', 'create_citations', 'link_claims',
    'track_reviews', 'peer_collaboration', 'ai_assistance',
]

MC_RESEARCH_METRICS = [
    'active_research', 'completed_research', 'research_backlog',
    'claims_awaiting_verification', 'sources_awaiting_review',
    'publication_pipeline', 'research_quality_indicators',
]

MC_RESEARCH_QUALITY_DASHBOARD = [
    'research_completed', 'research_under_review', 'evidence_completeness',
    'claims_verified', 'citation_coverage', 'county_research_completion',
    'research_aging', 'knowledge_gaps', 'institutional_confidence_metrics',
]

COUNTY_PROFILE_ELEMENTS = [
    'history', 'government_structure', 'major_communities', 'educational_organizations',
    'libraries', 'historical_societies', 'community_resources', 'local_civic_information',
]

COUNTY_MILESTONE_REQUIREMENTS = [
    'completed_county_profile',
    'education_leader_or_recruitment_contact',
    'county_dashboard_in_mission_control',
    'initial_local_resource_information',
    'development_plan_for_continued_growth',
]

RESEARCH_SYSTEM_CHAIN = [
    'mission_control', 'knowledge_platform', 'evidence_ledger', 'claims_registry',
    'community_education_academy', 'ai_localbrains', 'county_operating_system', 'communications',
]

MILESTONE_TIMELINE = [
    {
        'date': software_completion_date,
        'title': 'Software Completion',
        'summary': 'Software platform substantially complete',
    },
    {
        'date': county_milestone_date,
        'title': '75 Counties by October 1',
        'summary': 'Representation in all 75 Arkansas counties — profiles, dashboards, local leadership',
    },
    {
        'date': organizational_readiness_date,
        'title': 'Organizational Readiness',
        'summary': 'Full organizational readiness; city/neighborhood systems mature',
    },
]

RESEARCH_INSTITUTE_MANIFEST = {
    'version': '1.0',
    'build': 101,
    'package': 'IMP-11',
    'updated': today,
    'title': 'Master Research Institute, Evidence Ledger & Claims Verification System',
    'constitution': '/docs/IMPLEMENTATION_PACKAGE_11_RESEARCH_INSTITUTE.md',
    'source_registries': {
        'research_observatory': '/data/research-observatory.json',
        'research_framework': '/data/research-framework.json',
        'research_methodology': '/data/research-methodology.json',
        'evidence_ledger': '/data/evidence-ledger.json',
        'evidence_registry': '/data/evidence-registry.json',
        'content_management': '/data/content-management-manifest.json',
        'knowledge_graph': '/data/knowledge-graph-manifest.json',
    },
    'philosophy': 'Questions lead to research; research leads to evidence; evidence supports claims',
    'governing_principle': (
        'Research creates knowledge; verification creates confidence; '
        'education creates understanding; communities create lasting impact'
    ),
    'master_timeline': MASTER_TIMELINE,
    'milestone_timeline': MILESTONE_TIMELINE,
    'software_completion_date': software_completion_date,
    'county_milestone_date': county_milestone_date,
    'organizational_readiness_date': organizational_readiness_date,
    'days_to_software': days_to_software,
    'days_to_county_milestone': days_to_county_milestone,
    'days_to_organizational': days_to_organizational,
    'research_programs': RESEARCH_PROGRAMS,
    'research_program_count': len(RESEARCH_PROGRAMS),
    'research_lifecycle': RESEARCH_LIFECYCLE_STAGES,
    'lifecycle_stage_count': len(RESEARCH_LIFECYCLE_STAGES),
    'evidence_ledger_fields': EVIDENCE_LEDGER_FIELDS,
    'claims_registry_fields': CLAIMS_REGISTRY_FIELDS,
    'source_evaluation_criteria': SOURCE_EVALUATION_CRITERIA,
    'ai_research_capabilities': AI_RESEARCH_CAPABILITIES,
    'ai_research_rule': 'AI accelerates research; judgment remains with human researchers',
    'peer_review_criteria': PEER_REVIEW_CRITERIA,
    'research_workspace_features': RESEARCH_WORKSPACE_FEATURES,
    'mc_research_metrics': MC_RESEARCH_METRICS,
    'mc_research_quality_dashboard': MC_RESEARCH_QUALITY_DASHBOARD,
    'county_profile_elements': COUNTY_PROFILE_ELEMENTS,
    'county_milestone': {
        'target_date': county_milestone_date,
        'counties_total': 75,
        'days_remaining': days_to_county_milestone,
        'label': '75-by-October-1 Milestone',
        'requirements': COUNTY_MILESTONE_REQUIREMENTS,
        'mc_priority': 'highest',
    },
    'research_system_chain': RESEARCH_SYSTEM_CHAIN,
    'packages_completed': 11,
    'packages_total': 50,
    'packages_complete_pct': 22,
    'engineering_note': 'Doctrinal IMP-11 Research Institute; engineering IMP-11 is unified route manifest',
    'status': 'documented',
    'implemented': False,
}

ACADEMY_SCHOOLS = {
    'constitutional_foundations': [
        'us_constitution', 'separation_of_powers', 'federalism',
        'individual_rights', 'judicial_review',
    ],
    'campaign_finance': [
        'citizens_united', 'campaign_finance_history', 'disclosure',
        'independent_expenditures', 'political_action_committees', 'public_financing',
    ],
    'arkansas_government': [
        'state_government', 'local_government', 'county_government',
        'city_government', 'school_boards', 'ballot_initiatives',
    ],
    'civic_participation': [
        'public_meetings', 'legislative_process', 'public_records',
        'community_organizing', 'civic_dialogue', 'volunteer_leadership',
    ],
    'community_leadership': [
        'hosting_conversations', 'public_speaking', 'presentation_skills',
        'facilitation', 'listening_skills', 'building_trust',
    ],
}

LEARNING_LEVELS = [
    {'level': 100, 'title': 'Introduction', 'description': 'No prior knowledge required'},
    {'level': 200, 'title': 'Intermediate', 'description': 'Builds foundational understanding'},
    {'level': 300, 'title': 'Advanced', 'description': 'Deep analysis; leadership preparation'},
    {'level': 400, 'title': 'Education Leader', 'description': 'Teaching, facilitation, mentoring'},
]

CURRICULUM_FACTORY_STAGES = [
    {'stage': 'research', 'title': 'Research'},
    {'stage': 'evidence_verification', 'title': 'Evidence Verification'},
    {'stage': 'learning_objectives', 'title': 'Learning Objectives'},
    {'stage': 'lesson_design', 'title': 'Lesson Design'},
    {'stage': 'ai_review', 'title': 'AI Review'},
    {'stage': 'educational_review', 'title': 'Educational Review'},
    {'stage': 'accessibility_review', 'title': 'Accessibility Review'},
    {'stage': 'publication', 'title': 'Publication'},
    {'stage': 'continuous_improvement', 'title': 'Continuous Improvement'},
]

LEARNING_FORMATS = [
    'articles', 'short_lessons', 'interactive_modules', 'videos', 'podcasts',
    'presentations', 'discussion_guides', 'case_studies', 'knowledge_checks',
    'reference_libraries',
]

PERSONALIZED_LEARNING_FEATURES = [
    'recommended_courses', 'suggested_next_lessons', 'learning_history',
    'certificates_earned', 'bookmarks', 'ai_study_assistant', 'county_specific_resources',
]

CERTIFICATION_TYPES = [
    'constitutional_foundations', 'campaign_finance_fundamentals', 'arkansas_government',
    'community_education', 'research_literacy', 'education_leader_certification',
]

EDUCATION_LEADER_REQUIREMENTS = [
    'core_curriculum', 'presentation_training', 'discussion_facilitation',
    'research_standards', 'evidence_standards', 'community_engagement',
    'ethics_and_public_trust',
]

AI_TUTOR_CAPABILITIES = [
    'explain_concepts', 'recommend_lessons', 'summarize_research',
    'create_practice_questions', 'suggest_related_materials',
    'track_learning_progress', 'encourage_continued_learning',
]

COUNTY_ACADEMY_METRICS = [
    'learners_enrolled', 'courses_completed', 'education_leaders_certified',
    'community_presentations', 'learning_events', 'volunteer_growth',
]

CITY_ACADEMY_METRICS = [
    'active_learners', 'community_classes', 'education_leaders',
    'presentation_activity', 'neighborhood_participation', 'certification_growth',
]

MC_ACADEMY_METRICS = [
    'enrollments', 'completion_rates', 'certificates_awarded',
    'education_leaders_trained', 'lesson_quality', 'learner_satisfaction',
    'knowledge_retention', 'course_usage',
]

CONTINUING_EDUCATION_TRIGGERS = [
    'updated_lessons', 'new_court_decisions', 'arkansas_legislative_developments',
    'research_updates', 'advanced_certifications',
]

ACADEMY_OCTOBER_REQUIREMENTS = [
    'academy_access',
    'education_leader_or_leader_in_training',
    'county_specific_educational_resources',
    'volunteer_certification_pathway',
]

ACADEMY_SYSTEM_CHAIN = [
    'research_institute', 'evidence_ledger', 'knowledge_platform', 'mission_control',
    'volunteer_network', 'county_operating_system', 'city_operating_system',
    'neighborhood_operating_system', 'ai_localbrains',
]

MAJOR_SYSTEMS_COMPLETED = [
    'technical_constitution', 'technical_architecture', 'route_architecture',
    'canonical_data_model', 'identity_permissions', 'design_system',
    'mission_control', 'localbrain_network', 'knowledge_graph',
    'publishing_system', 'research_institute', 'community_education_academy',
]

EDUCATION_ACADEMY_MANIFEST = {
    'version': '1.0',
    'build': 101,
    'package': 'IMP-12',
    'updated': today,
    'title': 'Master Community Education Academy, Curriculum Factory & Certification System',
    'constitution': '/docs/IMPLEMENTATION_PACKAGE_12_COMMUNITY_EDUCATION_ACADEMY.md',
    'source_registries': {
        'education_academy': '/data/education-academy.json',
        'citizen_leadership_academy': '/data/citizen-leadership-academy.json',
        'research_institute': '/data/research-institute-manifest.json',
        'content_management': '/data/content-management-manifest.json',
        'knowledge_graph': '/data/knowledge-graph-manifest.json',
    },
    'philosophy': 'Teach how to think critically, not what to think politically',
    'governing_principle': (
        'Research creates knowledge; education creates understanding; '
        'understanding creates confident leaders; leaders strengthen communities'
    ),
    'master_timeline': MASTER_TIMELINE,
    'software_completion_date': software_completion_date,
    'county_milestone_date': county_milestone_date,
    'organizational_readiness_date': organizational_readiness_date,
    'days_to_software': days_to_software,
    'days_to_county_milestone': days_to_county_milestone,
    'days_to_organizational': days_to_organizational,
    'academy_schools': ACADEMY_SCHOOLS,
    'school_count': len(ACADEMY_SCHOOLS),
    'topic_count': sum(len(v) for v in ACADEMY_SCHOOLS.values()),
    'learning_levels': LEARNING_LEVELS,
    'learning_level_count': len(LEARNING_LEVELS),
    'curriculum_factory': CURRICULUM_FACTORY_STAGES,
    'curriculum_stage_count': len(CURRICULUM_FACTORY_STAGES),
    'learning_formats': LEARNING_FORMATS,
    'personalized_learning_features': PERSONALIZED_LEARNING_FEATURES,
    'certification_types': CERTIFICATION_TYPES,
    'certification_count': len(CERTIFICATION_TYPES),
    'education_leader_requirements': EDUCATION_LEADER_REQUIREMENTS,
    'ai_tutor_capabilities': AI_TUTOR_CAPABILITIES,
    'ai_tutor_rule': 'AI supports education without replacing human curiosity',
    'county_academy_metrics': COUNTY_ACADEMY_METRICS,
    'city_academy_metrics': CITY_ACADEMY_METRICS,
    'mc_academy_metrics': MC_ACADEMY_METRICS,
    'continuing_education_triggers': CONTINUING_EDUCATION_TRIGGERS,
    'october_county_objective': {
        'target_date': county_milestone_date,
        'requirements': ACADEMY_OCTOBER_REQUIREMENTS,
        'aligns_with': '75-by-October-1 Milestone',
    },
    'academy_system_chain': ACADEMY_SYSTEM_CHAIN,
    'major_systems_completed': MAJOR_SYSTEMS_COMPLETED,
    'packages_completed': 12,
    'packages_total': 50,
    'packages_complete_pct': 24,
    'engineering_note': 'Doctrinal IMP-12 Academy; engineering IMP-12 is App Router layout hierarchy',
    'status': 'documented',
    'implemented': False,
}

VOLUNTEER_JOURNEY_STAGES = [
    {'stage': 'interested_citizen', 'title': 'Interested Citizen'},
    {'stage': 'registered_member', 'title': 'Registered Member'},
    {'stage': 'volunteer', 'title': 'Volunteer'},
    {'stage': 'trained_volunteer', 'title': 'Trained Volunteer'},
    {'stage': 'education_leader', 'title': 'Education Leader'},
    {'stage': 'county_or_city_leader', 'title': 'County or City Leader'},
    {'stage': 'mentor', 'title': 'Mentor'},
    {'stage': 'institutional_leader', 'title': 'Institutional Leader'},
]

RECRUITMENT_SOURCES = [
    'website', 'community_conversations', 'academy', 'coalition_partners',
    'education_leaders', 'community_referrals', 'presentations', 'libraries',
    'universities', 'civic_organizations', 'personal_invitations',
]

ONBOARDING_STEPS_VOLUNTEER = [
    'welcome', 'mission_overview', 'institutional_values', 'county_selection',
    'city_selection', 'areas_of_interest', 'volunteer_skills', 'academy_enrollment',
    'ai_introduction', 'first_assignment',
]

VOLUNTEER_SKILLS = [
    'research', 'writing', 'public_speaking', 'teaching', 'graphic_design',
    'photography', 'video_production', 'technology', 'programming',
    'project_management', 'fundraising', 'community_organizing', 'legal_research',
    'historical_research', 'translation', 'data_analysis', 'event_planning',
]

VOLUNTEER_ROLES = [
    'research_volunteer', 'education_volunteer', 'presentation_volunteer',
    'community_conversation_host', 'education_leader', 'county_volunteer_coordinator',
    'city_volunteer_coordinator', 'neighborhood_leader', 'technology_volunteer',
    'media_volunteer', 'academy_mentor', 'coalition_liaison', 'project_volunteer',
]

EDUCATION_LEADER_PIPELINE_STAGES = [
    {'stage': 'volunteer', 'title': 'Volunteer'},
    {'stage': 'academy_completion', 'title': 'Academy Completion'},
    {'stage': 'leadership_training', 'title': 'Leadership Training'},
    {'stage': 'presentation_certification', 'title': 'Presentation Certification'},
    {'stage': 'conversation_facilitation', 'title': 'Community Conversation Facilitation'},
    {'stage': 'mentorship', 'title': 'Mentorship'},
    {'stage': 'county_assignment', 'title': 'County Assignment'},
    {'stage': 'education_leader', 'title': 'Education Leader'},
]

WORKSPACE_FEATURES_VOLUNTEER = [
    'assignments', 'projects', 'training', 'calendar', 'messages', 'county_updates',
    'ai_assistant', 'documents', 'resources', 'progress', 'recognition',
]

MATCHING_CRITERIA = [
    'county', 'skills', 'interests', 'availability', 'leadership_goals',
    'current_workload', 'nearby_opportunities',
]

MENTORSHIP_TRACKING = [
    'mentor_assignments', 'meeting_frequency', 'leadership_development', 'volunteer_satisfaction',
]

RECOGNITION_TYPES = [
    'years_of_service', 'courses_completed', 'education_leader_certification',
    'community_conversations_hosted', 'research_contributions', 'county_milestones',
    'volunteer_anniversaries',
]

RETENTION_METRICS = [
    'active_volunteers', 'inactive_volunteers', 'burnout_indicators',
    'leadership_vacancies', 'training_completion', 'volunteer_engagement',
]

ORGANIZING_TOOLKIT_ITEMS = [
    'presentation_materials', 'discussion_guides', 'fact_sheets', 'county_resources',
    'event_planning_checklists', 'volunteer_recruitment_materials',
    'follow_up_templates', 'ai_presentation_assistance',
]

CITY_LEADERSHIP_METRICS = [
    'education_leaders', 'volunteers', 'academy_participants',
    'community_conversations', 'leadership_readiness',
]

MC_VOLUNTEER_DASHBOARD = [
    'volunteer_growth', 'county_coverage', 'education_leader_pipeline', 'mentorship',
    'training_completion', 'volunteer_retention', 'leadership_readiness',
    'volunteer_workload', 'recognition_opportunities',
]

COUNTY_LEADERSHIP_OBJECTIVE = {
    'target_date': county_milestone_date,
    'counties_total': 75,
    'requirement': 'education_leader_or_pipeline_volunteer_per_county',
    'mc_priority': 'highest',
}

VOLUNTEER_SYSTEM_CHAIN = [
    'community_education_academy', 'mission_control', 'county_operating_system',
    'city_operating_system', 'neighborhood_operating_system', 'coalition_network',
    'knowledge_platform', 'calendar_brain', 'ai_localbrains',
]

PLATFORM_SYSTEMS_WITH_VOLUNTEERS = [
    'institutional_architecture', 'mission_control', 'knowledge_platform',
    'research_institute', 'community_education_academy', 'ai_localbrains',
    'volunteer_leadership_system',
]

VOLUNTEER_NETWORK_MANIFEST = {
    'version': '1.0',
    'build': 101,
    'package': 'IMP-13',
    'updated': today,
    'title': 'Master Volunteer Network, Education Leader Pipeline & Community Organizing Platform',
    'constitution': '/docs/IMPLEMENTATION_PACKAGE_13_VOLUNTEER_NETWORK.md',
    'source_registries': {
        'outreach_engine': '/data/outreach-engine.json',
        'volunteer_funding_constitution': '/data/volunteer-funding-constitution.json',
        'education_academy': '/data/education-academy-manifest.json',
        'identity_auth': '/data/identity-auth-manifest.json',
        'county_operating_system': '/data/county-operating-system.json',
    },
    'philosophy': 'Volunteers build the institution; the platform removes uncertainty and makes service rewarding',
    'governing_principle': (
        'Institutions are built by people; education grows through relationships; '
        'relationships create communities; communities transform states'
    ),
    'master_timeline': MASTER_TIMELINE,
    'software_completion_date': software_completion_date,
    'county_milestone_date': county_milestone_date,
    'organizational_readiness_date': organizational_readiness_date,
    'days_to_software': days_to_software,
    'days_to_county_milestone': days_to_county_milestone,
    'days_to_organizational': days_to_organizational,
    'volunteer_journey': VOLUNTEER_JOURNEY_STAGES,
    'journey_stage_count': len(VOLUNTEER_JOURNEY_STAGES),
    'recruitment_sources': RECRUITMENT_SOURCES,
    'onboarding_steps': ONBOARDING_STEPS_VOLUNTEER,
    'onboarding_step_count': len(ONBOARDING_STEPS_VOLUNTEER),
    'volunteer_skills': VOLUNTEER_SKILLS,
    'skill_count': len(VOLUNTEER_SKILLS),
    'volunteer_roles': VOLUNTEER_ROLES,
    'role_count': len(VOLUNTEER_ROLES),
    'education_leader_pipeline': EDUCATION_LEADER_PIPELINE_STAGES,
    'pipeline_stage_count': len(EDUCATION_LEADER_PIPELINE_STAGES),
    'workspace_features': WORKSPACE_FEATURES_VOLUNTEER,
    'matching_criteria': MATCHING_CRITERIA,
    'mentorship_tracking': MENTORSHIP_TRACKING,
    'recognition_types': RECOGNITION_TYPES,
    'retention_metrics': RETENTION_METRICS,
    'organizing_toolkit': ORGANIZING_TOOLKIT_ITEMS,
    'city_leadership_metrics': CITY_LEADERSHIP_METRICS,
    'cities_tracked': 250,
    'mc_volunteer_dashboard': MC_VOLUNTEER_DASHBOARD,
    'county_leadership_objective': COUNTY_LEADERSHIP_OBJECTIVE,
    'volunteer_system_chain': VOLUNTEER_SYSTEM_CHAIN,
    'platform_systems': PLATFORM_SYSTEMS_WITH_VOLUNTEERS,
    'first_week_contribution_rule': True,
    'packages_completed': 13,
    'packages_total': 50,
    'packages_complete_pct': 26,
    'engineering_note': 'Doctrinal IMP-13 Volunteer Network; engineering IMP-13 is design tokens port',
    'status': 'documented',
    'implemented': False,
}

COALITION_PRINCIPLES = [
    'mutual_respect', 'transparency', 'voluntary_participation', 'shared_educational_goals',
    'evidence_based_information', 'local_leadership', 'long_term_trust',
]

ORGANIZATION_TYPES = [
    'libraries', 'historical_societies', 'universities', 'community_colleges',
    'civic_organizations', 'neighborhood_associations', 'educational_nonprofits',
    'youth_organizations', 'veterans_organizations', 'professional_associations',
    'faith_based_civic_education', 'community_foundations',
]

ORGANIZATION_PROFILE_FIELDS = [
    'mission', 'description', 'service_area', 'counties_served', 'cities_served',
    'programs', 'educational_interests', 'leadership_contacts', 'public_website',
    'upcoming_events', 'volunteer_opportunities', 'educational_resources',
]

ORGANIZATION_WORKSPACE_FEATURES = [
    'dashboard', 'member_directory', 'shared_calendar', 'projects', 'events',
    'educational_resources', 'volunteer_coordination', 'announcements',
    'organization_ai_assistant', 'mission_control_metrics',
]

DIRECTORY_DISCOVERY_DIMENSIONS = [
    'county', 'city', 'topic', 'mission', 'educational_focus',
    'volunteer_opportunities', 'youth_programs', 'public_events',
]

PARTNERSHIP_LIFECYCLE_STAGES = [
    {'stage': 'prospective_partner', 'title': 'Prospective Partner'},
    {'stage': 'initial_conversation', 'title': 'Initial Conversation'},
    {'stage': 'orientation', 'title': 'Orientation'},
    {'stage': 'resource_sharing', 'title': 'Resource Sharing'},
    {'stage': 'active_partner', 'title': 'Active Partner'},
    {'stage': 'collaborative_projects', 'title': 'Collaborative Projects'},
    {'stage': 'long_term_strategic_partner', 'title': 'Long-Term Strategic Partner'},
]

SHARED_RESOURCE_LIBRARY = [
    'presentation_materials', 'research_summaries', 'discussion_guides',
    'educational_videos', 'infographics', 'lesson_plans',
    'volunteer_recruitment_resources', 'community_conversation_toolkits',
]

SHARED_CALENDAR_EVENT_TYPES = [
    'educational_events', 'community_conversations', 'volunteer_opportunities',
    'training_sessions', 'public_meetings', 'academy_events',
]

COALITION_PROJECT_FIELDS = [
    'purpose', 'participating_organizations', 'timeline', 'resources',
    'deliverables', 'milestones', 'community_impact',
]

COALITION_COMMUNICATION_TYPES = [
    'announcements', 'resource_updates', 'research_releases',
    'training_invitations', 'collaboration_requests',
]

GEOGRAPHIC_COVERAGE_METRICS = [
    'organizations_by_county', 'organizations_by_city', 'educational_gaps',
    'coalition_density', 'partnership_growth',
]

ORGANIZATION_AI_CAPABILITIES = [
    'summarize_research', 'find_educational_resources', 'prepare_presentations',
    'locate_partnership_opportunities', 'answer_platform_questions',
    'suggest_community_events', 'onboard_new_volunteers',
]

MC_COALITION_DASHBOARD = [
    'organizations_onboarded', 'county_coverage', 'city_coverage',
    'active_partnerships', 'shared_projects', 'educational_events',
    'resource_sharing', 'partnership_health', 'growth_trends',
]

COALITION_OCTOBER_REQUIREMENTS = [
    'active_or_developing_coalition_relationship',
    'local_civic_education_resource_directory',
    'county_specific_partnership_opportunities',
    'pathway_for_additional_organizations',
]

COALITION_SYSTEM_CHAIN = [
    'mission_control', 'community_education_academy', 'volunteer_network',
    'county_operating_system', 'city_operating_system', 'neighborhood_operating_system',
    'research_institute', 'knowledge_platform', 'calendar_brain', 'ai_localbrains',
]

PLATFORM_SYSTEMS_WITH_COALITION = [
    'technical_architecture', 'mission_control', 'localbrains', 'knowledge_platform',
    'research_institute', 'community_education_academy', 'volunteer_operating_system',
    'coalition_operating_system',
]

COALITION_NETWORK_MANIFEST = {
    'version': '1.0',
    'build': 101,
    'package': 'IMP-14',
    'updated': today,
    'title': 'Master Coalition Network, Organization Portal & Partnership Operating System',
    'constitution': '/docs/IMPLEMENTATION_PACKAGE_14_COALITION_NETWORK.md',
    'source_registries': {
        'coalition_network': '/data/coalition-network.json',
        'coalition_directory': '/data/coalition-directory.json',
        'coalition_ecosystem': '/data/coalition-ecosystem.json',
        'coalition_events': '/data/coalition-events.json',
        'county_coalition_index': '/data/county-coalition-index.json',
        'volunteer_network': '/data/volunteer-network-manifest.json',
    },
    'philosophy': 'Connective infrastructure — collaborate without sacrificing organizational independence',
    'governing_principle': (
        'Strong statewide institutions are built from strong local communities; '
        'the platform strengthens existing organizations rather than replacing them'
    ),
    'master_timeline': MASTER_TIMELINE,
    'software_completion_date': software_completion_date,
    'county_milestone_date': county_milestone_date,
    'organizational_readiness_date': organizational_readiness_date,
    'days_to_software': days_to_software,
    'days_to_county_milestone': days_to_county_milestone,
    'days_to_organizational': days_to_organizational,
    'coalition_principles': COALITION_PRINCIPLES,
    'organization_types': ORGANIZATION_TYPES,
    'organization_type_count': len(ORGANIZATION_TYPES),
    'organization_profile_fields': ORGANIZATION_PROFILE_FIELDS,
    'organization_workspace_features': ORGANIZATION_WORKSPACE_FEATURES,
    'directory_discovery_dimensions': DIRECTORY_DISCOVERY_DIMENSIONS,
    'partnership_lifecycle': PARTNERSHIP_LIFECYCLE_STAGES,
    'lifecycle_stage_count': len(PARTNERSHIP_LIFECYCLE_STAGES),
    'shared_resource_library': SHARED_RESOURCE_LIBRARY,
    'shared_calendar_event_types': SHARED_CALENDAR_EVENT_TYPES,
    'coalition_project_fields': COALITION_PROJECT_FIELDS,
    'coalition_communication_types': COALITION_COMMUNICATION_TYPES,
    'geographic_coverage_metrics': GEOGRAPHIC_COVERAGE_METRICS,
    'organization_ai_capabilities': ORGANIZATION_AI_CAPABILITIES,
    'mc_coalition_dashboard': MC_COALITION_DASHBOARD,
    'october_county_objective': {
        'target_date': county_milestone_date,
        'requirements': COALITION_OCTOBER_REQUIREMENTS,
        'aligns_with': '75-by-October-1 Milestone',
    },
    'coalition_system_chain': COALITION_SYSTEM_CHAIN,
    'platform_systems': PLATFORM_SYSTEMS_WITH_COALITION,
    'packages_completed': 14,
    'packages_total': 50,
    'packages_complete_pct': 28,
    'engineering_note': 'Doctrinal IMP-14 Coalition Network; engineering IMP-14 is core layout components',
    'status': 'documented',
    'implemented': False,
}

LOCAL_FIRST_HIERARCHY = [
    'arkansas', 'county', 'city', 'neighborhood', 'community_conversation', 'citizen',
]

COUNTY_OS_MODULES = [
    'county_dashboard', 'education_leader_directory', 'volunteer_directory',
    'coalition_directory', 'community_calendar', 'research_library',
    'community_conversations', 'county_academy', 'county_projects',
    'county_ai_assistant', 'mission_control_metrics',
]

COUNTY_DASHBOARD_METRICS = [
    'county_health', 'education_leader_status', 'volunteer_growth',
    'academy_participation', 'organizations', 'upcoming_events',
    'community_conversations', 'research_resources', 'engagement_progress_15pct',
    'leadership_pipeline', 'mission_control_recommendations',
]

COUNTY_SCORECARD_METRICS = [
    'education_leaders', 'volunteers', 'academy_enrollments', 'courses_completed',
    'community_conversations', 'organizations_participating', 'neighborhoods_active',
    'research_resources_completed', 'public_engagement', 'citizen_connection_15pct_goal',
]

CITY_OS_MODULES = [
    'city_dashboard', 'leadership_directory', 'volunteer_directory', 'neighborhood_map',
    'community_calendar', 'educational_events', 'organizations', 'local_research',
    'ai_assistant', 'mission_control_metrics',
]

NEIGHBORHOOD_OS_MODULES = [
    'neighborhood_profile', 'neighborhood_leader', 'community_conversations',
    'volunteer_opportunities', 'educational_resources', 'meeting_calendar',
    'neighborhood_projects', 'local_announcements', 'ai_assistant',
]

LEADERSHIP_HIERARCHY = [
    {'level': 'state', 'title': 'State'},
    {'level': 'region', 'title': 'Region (optional)'},
    {'level': 'county_education_leader', 'title': 'County Education Leader'},
    {'level': 'city_education_leader', 'title': 'City Education Leader'},
    {'level': 'neighborhood_leader', 'title': 'Neighborhood Leader'},
    {'level': 'community_volunteers', 'title': 'Community Volunteers'},
]

COMMUNITY_CONVERSATION_FIELDS = [
    'topic', 'facilitator', 'educational_resources', 'attendance',
    'questions_raised', 'follow_up_actions', 'future_meetings',
]

LOCAL_RESOURCE_LIBRARY = [
    'local_government_information', 'libraries', 'historical_societies',
    'educational_organizations', 'community_partners', 'meeting_locations',
    'volunteer_opportunities',
]

COUNTY_ACADEMY_FEATURES = [
    'local_courses', 'upcoming_classes', 'education_leaders',
    'certificates_earned', 'community_presentations', 'volunteer_training',
]

LOCAL_CALENDAR_EVENT_TYPES = [
    'community_conversations', 'academy_classes', 'volunteer_meetings',
    'coalition_meetings', 'public_civic_education_events',
]

LOCAL_AI_EXAMPLE_QUERIES = [
    'events_in_my_county', 'who_is_my_education_leader', 'courses_available_nearby',
    'organizations_in_my_city', 'scheduled_community_conversations',
]

COMMUNITY_HEALTH_METRICS = [
    'leadership', 'volunteer_activity', 'learning', 'coalition_participation',
    'community_conversations', 'educational_events', 'growth_trends', 'citizen_engagement',
]

ENGAGEMENT_CONNECTION_TYPES = [
    'educational_updates', 'academy_participation', 'community_conversations',
    'volunteer_service', 'research_subscriptions', 'organization_membership',
    'educational_event_attendance',
]

GEOGRAPHIC_MAP_LAYERS = [
    'county_coverage', 'city_coverage', 'neighborhood_coverage',
    'education_leaders', 'organizations', 'community_conversations',
    'volunteer_density', 'engagement_progress',
]

OCTOBER_COUNTY_OS_REQUIREMENTS = [
    'live_county_operating_system',
    'completed_county_dashboard',
    'county_research_profile',
    'education_leader_or_leader_in_training',
    'coalition_relationships',
    'community_calendar',
    'academy_presence',
    'mission_control_reporting',
]

LOCAL_OS_SYSTEM_CHAIN = [
    'mission_control', 'community_education_academy', 'volunteer_network',
    'coalition_network', 'research_institute', 'knowledge_platform',
    'calendar_brain', 'ai_localbrains', 'executive_dashboard',
]

STATEWIDE_FRAMEWORK_COMPLETE = [
    'institutional_governance', 'mission_control', 'knowledge_platform',
    'research_institute', 'community_education_academy', 'volunteer_operating_system',
    'coalition_network', 'county_city_neighborhood_operating_systems',
]

LOCAL_OPERATING_SYSTEMS_MANIFEST = {
    'version': '1.0',
    'build': 101,
    'package': 'IMP-15',
    'updated': today,
    'title': 'Master County Operating System, City Operating System & Neighborhood Operating System',
    'constitution': '/docs/IMPLEMENTATION_PACKAGE_15_LOCAL_OPERATING_SYSTEMS.md',
    'source_registries': {
        'county_operating_system': '/data/county-operating-system.json',
        'arkansas_county_os': '/data/arkansas-county-operating-system.json',
        'arkansas_city_os': '/data/arkansas-city-operating-system.json',
        'arkansas_neighborhood_os': '/data/arkansas-neighborhood-operating-system.json',
        'neighborhood_profiles': '/data/neighborhood-profiles.json',
        'neighborhood_organizing': '/data/neighborhood-organizing.json',
        'coalition_network': '/data/coalition-network-manifest.json',
        'volunteer_network': '/data/volunteer-network-manifest.json',
    },
    'philosophy': 'The statewide institution is built locally — one institution with distributed leadership',
    'governing_principle': (
        'A statewide institution is built through thousands of local relationships; '
        'when every county is organized, Arkansas gains permanent infrastructure for informed self-government'
    ),
    'master_timeline': MASTER_TIMELINE,
    'software_completion_date': software_completion_date,
    'county_milestone_date': county_milestone_date,
    'organizational_readiness_date': organizational_readiness_date,
    'days_to_software': days_to_software,
    'days_to_county_milestone': days_to_county_milestone,
    'days_to_organizational': days_to_organizational,
    'local_first_hierarchy': LOCAL_FIRST_HIERARCHY,
    'counties_total': 75,
    'target_cities': target_cities,
    'engagement_goal_pct': engagement_goal_pct,
    'engagement_goal_label': '15% registered voters connected per county and target city',
    'engagement_connection_types': ENGAGEMENT_CONNECTION_TYPES,
    'county_os_modules': COUNTY_OS_MODULES,
    'county_module_count': len(COUNTY_OS_MODULES),
    'county_dashboard_metrics': COUNTY_DASHBOARD_METRICS,
    'county_scorecard_metrics': COUNTY_SCORECARD_METRICS,
    'city_os_modules': CITY_OS_MODULES,
    'city_module_count': len(CITY_OS_MODULES),
    'neighborhood_os_modules': NEIGHBORHOOD_OS_MODULES,
    'neighborhood_module_count': len(NEIGHBORHOOD_OS_MODULES),
    'leadership_hierarchy': LEADERSHIP_HIERARCHY,
    'community_conversation_fields': COMMUNITY_CONVERSATION_FIELDS,
    'local_resource_library': LOCAL_RESOURCE_LIBRARY,
    'county_academy_features': COUNTY_ACADEMY_FEATURES,
    'local_calendar_event_types': LOCAL_CALENDAR_EVENT_TYPES,
    'local_ai_example_queries': LOCAL_AI_EXAMPLE_QUERIES,
    'community_health_metrics': COMMUNITY_HEALTH_METRICS,
    'geographic_map_layers': GEOGRAPHIC_MAP_LAYERS,
    'october_county_milestone': {
        'target_date': county_milestone_date,
        'requirements': OCTOBER_COUNTY_OS_REQUIREMENTS,
        'label': 'Statewide County Operating Network Established',
    },
    'local_os_system_chain': LOCAL_OS_SYSTEM_CHAIN,
    'statewide_framework': STATEWIDE_FRAMEWORK_COMPLETE,
    'packages_completed': 15,
    'packages_total': 50,
    'packages_complete_pct': 30,
    'engineering_note': 'Doctrinal IMP-15 Local OS; engineering IMP-15 is Mission Control shell layout',
    'status': 'documented',
    'implemented': False,
}

COMMUNICATION_PHILOSOPHY = [
    'clearly', 'honestly', 'consistently', 'respectfully', 'only_what_is_useful',
]

COMMUNICATION_LAYERS = {
    'layer_1_public': {
        'title': 'Public Communication',
        'audience': 'everyone',
        'examples': [
            'research_releases', 'educational_articles', 'public_announcements',
            'videos', 'educational_campaigns', 'community_event_listings',
        ],
    },
    'layer_2_member': {
        'title': 'Member Communication',
        'audience': 'registered_users',
        'examples': [
            'learning_reminders', 'recommended_resources', 'saved_topics',
            'personal_calendar_updates', 'account_notifications',
        ],
    },
    'layer_3_volunteer': {
        'title': 'Volunteer Communication',
        'audience': 'volunteers',
        'examples': [
            'assignments', 'projects', 'mentorship', 'training',
            'county_updates', 'education_leader_coordination',
        ],
    },
    'layer_4_organization': {
        'title': 'Organization Communication',
        'audience': 'coalition_partners',
        'examples': [
            'coalition_announcements', 'shared_projects', 'joint_events',
            'resource_updates', 'organization_messaging',
        ],
    },
    'layer_5_executive': {
        'title': 'Executive Communication',
        'audience': 'leadership',
        'examples': [
            'mission_control_alerts', 'executive_briefings', 'risk_notifications',
            'strategic_updates', 'pmo_reports', 'leadership_coordination',
        ],
    },
}

PERSONAL_INBOX_FEATURES = [
    'messages', 'announcements', 'learning_reminders', 'volunteer_assignments',
    'calendar_invitations', 'organization_updates', 'ai_summaries', 'priority_alerts',
]

NOTIFICATION_PREFERENCES = [
    'research_updates', 'county_activity', 'community_conversations',
    'academy_reminders', 'volunteer_assignments', 'coalition_news', 'executive_alerts',
]

BROADCAST_SCOPES = [
    'county', 'city', 'neighborhood', 'volunteer_team', 'organization', 'academy_learners',
]

NEWSLETTER_CHANNELS = [
    'statewide', 'county', 'city', 'topic', 'academy', 'research', 'volunteer', 'coalition',
]

EVENT_COMMUNICATION_STAGES = [
    'invitations', 'reminders', 'attendance_confirmation', 'follow_up_resources',
    'post_event_surveys', 'educational_recommendations',
]

INTERNAL_MESSAGING_CHANNELS = [
    'direct_messages', 'group_discussions', 'project_conversations', 'volunteer_teams',
    'organization_channels', 'county_leadership',
]

AI_COMMUNICATION_CAPABILITIES = [
    'draft_announcements', 'summarize_discussions', 'prepare_presentations',
    'generate_newsletters', 'suggest_responses', 'create_meeting_agendas',
    'translate_research_to_plain_language',
]

CIVIC_MEDIA_FORMATS = [
    'articles', 'videos', 'podcasts', 'infographics', 'presentation_decks',
    'printable_handouts', 'short_educational_clips', 'downloadable_resources',
]

COMMUNICATION_CALENDAR_ITEMS = [
    'research_releases', 'educational_campaigns', 'academy_launches',
    'volunteer_recruitment', 'community_conversations', 'public_events',
    'annual_reports', 'institution_wide_announcements',
]

COMMUNITY_FEEDBACK_ACTIONS = [
    'ask_questions', 'suggest_resources', 'report_errors', 'recommend_topics',
    'provide_event_feedback', 'request_presentations',
]

MC_COMMUNICATION_METRICS = [
    'messages_delivered', 'open_rates', 'resource_downloads', 'newsletter_engagement',
    'community_participation', 'presentation_requests', 'questions_received',
    'response_times', 'most_requested_topics',
]

GROWTH_COMMUNICATION_DASHBOARDS = [
    'county_representation_75', 'city_leadership_250', 'engagement_15pct',
    'arkansans_connected_200k', 'educational_participation', 'volunteer_growth',
]

COMMUNICATION_SYSTEM_CHAIN = [
    'mission_control', 'knowledge_platform', 'community_education_academy',
    'volunteer_network', 'coalition_network', 'county_operating_system',
    'city_operating_system', 'neighborhood_operating_system', 'calendar_brain', 'ai_localbrains',
]

FOUNDATIONAL_SYSTEMS_WITH_COMMUNICATION = [
    'institutional_architecture', 'mission_control', 'localbrains', 'knowledge_platform',
    'research_institute', 'community_education_academy', 'volunteer_network',
    'coalition_network', 'local_operating_systems', 'communication_platform',
]

COMMUNICATION_PLATFORM_MANIFEST = {
    'version': '1.0',
    'build': 101,
    'package': 'IMP-16',
    'updated': today,
    'title': 'Master Communication Platform, Messaging System & Arkansas Civic Media Network',
    'constitution': '/docs/IMPLEMENTATION_PACKAGE_16_COMMUNICATION_PLATFORM.md',
    'source_registries': {
        'arkansas_communications': '/data/arkansas-communications.json',
        'media_studio': '/data/media-studio.json',
        'local_operating_systems': '/data/local-operating-systems-manifest.json',
        'volunteer_network': '/data/volunteer-network-manifest.json',
        'coalition_network': '/data/coalition-network-manifest.json',
        'education_academy': '/data/education-academy-manifest.json',
    },
    'philosophy': 'Signal not noise — every communication strengthens trust and civic learning',
    'governing_principle': (
        'Every message should help someone learn, connect, participate, or lead; '
        'timely, trustworthy communication strengthens relationships'
    ),
    'master_timeline': MASTER_TIMELINE,
    'software_completion_date': software_completion_date,
    'county_milestone_date': county_milestone_date,
    'organizational_readiness_date': organizational_readiness_date,
    'days_to_software': days_to_software,
    'days_to_county_milestone': days_to_county_milestone,
    'days_to_organizational': days_to_organizational,
    'communication_philosophy': COMMUNICATION_PHILOSOPHY,
    'communication_layers': COMMUNICATION_LAYERS,
    'communication_layer_count': len(COMMUNICATION_LAYERS),
    'personal_inbox_features': PERSONAL_INBOX_FEATURES,
    'notification_preferences': NOTIFICATION_PREFERENCES,
    'broadcast_scopes': BROADCAST_SCOPES,
    'newsletter_channels': NEWSLETTER_CHANNELS,
    'event_communication_stages': EVENT_COMMUNICATION_STAGES,
    'internal_messaging_channels': INTERNAL_MESSAGING_CHANNELS,
    'ai_communication_capabilities': AI_COMMUNICATION_CAPABILITIES,
    'ai_communication_rule': 'AI supports communication while preserving human oversight',
    'civic_media_formats': CIVIC_MEDIA_FORMATS,
    'civic_media_format_count': len(CIVIC_MEDIA_FORMATS),
    'communication_calendar_items': COMMUNICATION_CALENDAR_ITEMS,
    'community_feedback_actions': COMMUNITY_FEEDBACK_ACTIONS,
    'mc_communication_metrics': MC_COMMUNICATION_METRICS,
    'growth_communication_dashboards': GROWTH_COMMUNICATION_DASHBOARDS,
    'organizational_goals': {
        'counties_total': 75,
        'target_cities': target_cities,
        'engagement_goal_pct': engagement_goal_pct,
        'arkansans_connected_goal': arkansans_connected_goal,
    },
    'communication_system_chain': COMMUNICATION_SYSTEM_CHAIN,
    'foundational_systems': FOUNDATIONAL_SYSTEMS_WITH_COMMUNICATION,
    'packages_completed': 16,
    'packages_total': 50,
    'packages_complete_pct': 32,
    'engineering_note': 'Doctrinal IMP-16 Communication Platform; engineering IMP-16 is component registry COMP-* index',
    'status': 'documented',
    'implemented': False,
}

TIME_PHILOSOPHY_REQUIREMENTS = [
    'purpose', 'participants', 'preparation', 'resources', 'follow_up',
]

PERSONAL_CALENDAR_FEATURES = [
    'learning_schedule', 'volunteer_assignments', 'events', 'community_conversations',
    'organization_meetings', 'academy_classes', 'presentation_schedule', 'personal_reminders',
]

LOCALBRAIN_CALENDARS = [
    'mission_control', 'research', 'academy', 'volunteer', 'county', 'city',
    'neighborhood', 'coalition', 'technology', 'communications', 'pmo',
]

COUNTY_CALENDAR_EVENTS = [
    'community_conversations', 'academy_classes', 'volunteer_meetings',
    'public_education_events', 'coalition_activities', 'county_planning_meetings',
    'leadership_development',
]

CITY_CALENDAR_EVENTS = [
    'community_presentations', 'volunteer_recruitment', 'neighborhood_meetings',
    'educational_events', 'leadership_training', 'city_projects',
]

NEIGHBORHOOD_CALENDAR_EVENTS = [
    'community_conversations', 'volunteer_gatherings', 'educational_workshops',
    'listening_sessions', 'neighborhood_projects', 'local_leadership_meetings',
]

ACADEMY_CALENDAR_EVENTS = [
    'course_launches', 'live_classes', 'workshops', 'certification_sessions',
    'office_hours', 'education_leader_training', 'continuing_education',
]

PROJECT_CALENDAR_FIELDS = [
    'milestones', 'deadlines', 'dependencies', 'reviews', 'launches', 'completion_dates',
]

EXECUTIVE_CALENDAR_ITEMS = [
    'leadership_meetings', 'mission_control_reviews', 'pmo_milestones',
    'research_releases', 'strategic_planning', 'community_events',
    'annual_reviews', 'critical_deadlines',
]

EVENT_MANAGEMENT_FIELDS = [
    'purpose', 'agenda', 'location', 'virtual_option', 'participants', 'resources',
    'attendance', 'follow_up_actions', 'related_documents', 'related_research',
]

RECURRING_EVENT_TYPES = [
    'county_meetings', 'leadership_meetings', 'community_conversations',
    'academy_classes', 'research_reviews', 'volunteer_onboarding',
    'organization_meetings', 'annual_events',
]

SCHEDULING_INTELLIGENCE_CAPABILITIES = [
    'avoid_conflicts', 'recommend_meeting_times', 'balance_volunteer_workload',
    'identify_resource_conflicts', 'optimize_travel', 'coordinate_statewide_activities',
]

EXTERNAL_CALENDAR_SYNC = [
    'google_calendar', 'microsoft_outlook', 'apple_calendar', 'ics_export', 'ics_import',
]

PERSONAL_AI_SCHEDULER_EXAMPLES = [
    'meetings_this_week', 'when_complete_course', 'meet_mentor_time',
    'schedule_community_conversation',
]

EXECUTIVE_AI_SCHEDULER_CAPABILITIES = [
    'scheduling_conflicts', 'county_event_overlap', 'volunteer_overload',
    'travel_efficiency', 'strategic_opportunities', 'important_anniversaries',
    'upcoming_deadlines',
]

TIME_ANALYTICS_METRICS = [
    'events_held', 'attendance', 'volunteer_participation', 'academy_sessions',
    'community_conversations', 'leadership_meetings', 'event_growth', 'calendar_utilization',
]

TRAVEL_COORDINATION_FEATURES = [
    'travel_routes', 'travel_time_estimates', 'regional_scheduling',
    'multi_county_tours', 'community_visit_planning', 'leadership_itineraries',
]

OCTOBER_TIME_COORDINATION = [
    'remaining_county_visits', 'education_leader_training', 'community_conversations',
    'volunteer_onboarding', 'coalition_meetings', 'research_completion', 'county_readiness',
]

TIME_SYSTEM_CHAIN = [
    'mission_control', 'localbrains', 'volunteer_network', 'community_education_academy',
    'county_operating_system', 'city_operating_system', 'neighborhood_operating_system',
    'coalition_network', 'knowledge_platform', 'communications', 'pmo',
]

INSTITUTIONAL_OS_SYSTEMS = [
    'technical_foundation', 'mission_control', 'localbrains', 'knowledge_platform',
    'research_institute', 'community_education_academy', 'volunteer_network',
    'coalition_network', 'local_operating_systems', 'communication_platform',
    'institutional_time_intelligence', 'institutional_relationship_intelligence',
    'institutional_analytics', 'institutional_automation', 'public_digital_experience',
    'mobile_field_operations', 'institutional_digital_library',
    'institutional_integration_platform', 'institutional_security_trust',
    'institutional_governance_pmo', 'institutional_sustainability_continuity',
]

RELATIONSHIP_PHILOSOPHY_REMEMBERS = [
    'how_we_met', 'shared_interests', 'volunteer_history', 'community_involvement',
    'organizations', 'skills', 'conversations', 'educational_progress',
]

RELATIONSHIP_ARCHITECTURE_TYPES = [
    'person_person', 'person_organization', 'person_county', 'person_city',
    'person_neighborhood', 'person_education_leader', 'volunteer_mentor',
    'researcher_project', 'organization_organization', 'community_event',
]

CONTACT_PROFILE_FIELDS = [
    'basic_information', 'counties', 'cities', 'neighborhoods', 'organizations',
    'volunteer_interests', 'skills', 'education_progress', 'conversation_history',
    'meeting_history', 'community_participation', 'communication_preferences',
    'relationship_strength', 'last_meaningful_interaction',
]

RELATIONSHIP_TIMELINE_EVENTS = [
    'joined_platform', 'completed_course', 'attended_presentation',
    'hosted_community_conversation', 'joined_organization', 'became_education_leader',
    'mentored_volunteer', 'published_research',
]

COMMUNITY_GRAPH_VISUALIZATIONS = [
    'volunteer_connections', 'county_leadership', 'city_leadership',
    'coalition_relationships', 'mentorship_networks', 'organization_partnerships',
    'community_conversation_networks', 'knowledge_sharing_networks',
]

EDUCATION_LEADER_NETWORK_FIELDS = [
    'certified_leaders', 'leaders_in_training', 'mentors', 'presentation_activity',
    'community_reach', 'county_assignments', 'city_assignments', 'leadership_succession',
]

ORGANIZATION_RELATIONSHIP_FIELDS = [
    'partnership_history', 'joint_projects', 'shared_events',
    'educational_collaboration', 'volunteer_sharing', 'research_collaboration',
    'long_term_partnership_growth',
]

MENTORSHIP_NETWORK_FIELDS = [
    'mentor', 'learner', 'goals', 'meetings', 'progress',
    'resources_shared', 'leadership_development',
]

COMMUNITY_CONVERSATION_HISTORY_FIELDS = [
    'topic', 'participants', 'questions_asked', 'resources_shared',
    'follow_up_actions', 'future_meetings', 'related_research',
]

RELATIONSHIP_INTELLIGENCE_ENGINE = [
    'volunteers_to_reconnect', 'organizations_ready_for_partnership',
    'communities_lacking_engagement', 'emerging_leaders', 'mentorship_opportunities',
    'presentation_requests', 'counties_needing_support',
]

AI_RELATIONSHIP_ASSISTANT = [
    'meeting_summaries', 'follow_up_suggestions', 'conversation_memory',
    'shared_interest_identification', 'introduction_recommendations',
    'presentation_briefings', 'community_resource_suggestions',
]

RELATIONSHIP_HEALTH_METRICS = [
    'relationship_growth', 'volunteer_retention', 'mentorship_activity',
    'organization_engagement', 'community_conversations', 'leadership_density',
    'county_connectivity', 'city_connectivity',
]

RELATIONSHIP_PRIVACY_CONTROLS = [
    'profile_visibility', 'communication_preferences', 'organization_visibility',
    'volunteer_availability', 'mentorship_participation', 'personal_information',
]

OCTOBER_RELATIONSHIP_NETWORK = [
    'education_leader_or_training', 'coalition_organizations', 'active_volunteers',
    'community_conversations', 'local_contacts', 'mentorship_pathways',
]

RELATIONSHIP_SYSTEM_CHAIN = [
    'mission_control', 'knowledge_graph', 'volunteer_network',
    'community_education_academy', 'coalition_network', 'county_operating_system',
    'city_operating_system', 'neighborhood_operating_system', 'calendar_brain',
    'ai_localbrains',
]

RELATIONSHIP_INTELLIGENCE_MANIFEST = {
    'version': '1.0',
    'build': 101,
    'package': 'IMP-18',
    'updated': today,
    'title': 'Master Relationship Intelligence, Contact Network & Community Graph',
    'constitution': '/docs/IMPLEMENTATION_PACKAGE_18_RELATIONSHIP_INTELLIGENCE.md',
    'source_registries': {
        'contact_intelligence': '/data/contact-intelligence.json',
        'relationship_registry': '/data/relationship-registry.json',
        'relationship_os': '/data/relationship-os.json',
        'knowledge_graph': '/data/knowledge-graph-manifest.json',
        'volunteer_network': '/data/volunteer-network-manifest.json',
        'coalition_network': '/data/coalition-network-manifest.json',
        'education_academy': '/data/education-academy-manifest.json',
        'time_intelligence': '/data/time-intelligence-manifest.json',
    },
    'philosophy': 'Relationships sustain the institution — strengthen human connection over time',
    'governing_principle': (
        'Technology should never replace relationships; it should help people '
        'remember, strengthen, and expand them'
    ),
    'master_timeline': MASTER_TIMELINE,
    'software_completion_date': software_completion_date,
    'county_milestone_date': county_milestone_date,
    'organizational_readiness_date': organizational_readiness_date,
    'days_to_software': days_to_software,
    'days_to_county_milestone': days_to_county_milestone,
    'days_to_organizational': days_to_organizational,
    'relationship_philosophy_remembers': RELATIONSHIP_PHILOSOPHY_REMEMBERS,
    'relationship_architecture_types': RELATIONSHIP_ARCHITECTURE_TYPES,
    'relationship_architecture_type_count': len(RELATIONSHIP_ARCHITECTURE_TYPES),
    'contact_profile_fields': CONTACT_PROFILE_FIELDS,
    'contact_profile_field_count': len(CONTACT_PROFILE_FIELDS),
    'relationship_timeline_events': RELATIONSHIP_TIMELINE_EVENTS,
    'community_graph_visualizations': COMMUNITY_GRAPH_VISUALIZATIONS,
    'community_graph_visualization_count': len(COMMUNITY_GRAPH_VISUALIZATIONS),
    'education_leader_network_fields': EDUCATION_LEADER_NETWORK_FIELDS,
    'organization_relationship_fields': ORGANIZATION_RELATIONSHIP_FIELDS,
    'mentorship_network_fields': MENTORSHIP_NETWORK_FIELDS,
    'community_conversation_history_fields': COMMUNITY_CONVERSATION_HISTORY_FIELDS,
    'relationship_intelligence_engine': RELATIONSHIP_INTELLIGENCE_ENGINE,
    'ai_relationship_assistant': AI_RELATIONSHIP_ASSISTANT,
    'relationship_health_metrics': RELATIONSHIP_HEALTH_METRICS,
    'relationship_health_metric_count': len(RELATIONSHIP_HEALTH_METRICS),
    'relationship_privacy_controls': RELATIONSHIP_PRIVACY_CONTROLS,
    'october_relationship_goal': {
        'target_date': county_milestone_date,
        'county_network_requirements': OCTOBER_RELATIONSHIP_NETWORK,
        'label': 'Identifiable relationship network in every county',
    },
    'organizational_goals': {
        'counties_total': 75,
        'target_cities': target_cities,
        'engagement_goal_pct': engagement_goal_pct,
        'arkansans_connected_goal': arkansans_connected_goal,
    },
    'relationship_system_chain': RELATIONSHIP_SYSTEM_CHAIN,
    'institutional_systems': INSTITUTIONAL_OS_SYSTEMS,
    'mc_dashboard': '/mission-control/contact-intelligence.html',
    'packages_completed': 18,
    'packages_total': 50,
    'packages_complete_pct': 36,
    'engineering_note': 'Doctrinal IMP-18 Relationship Intelligence; engineering IMP-18 is COMP-06–10 interactive specs',
    'status': 'documented',
    'implemented': False,
}

ANALYTICS_INTELLIGENCE_LAYERS = {
    'layer_1_activity': {
        'title': 'Activity',
        'question': 'What happened?',
        'examples': [
            'new_volunteers', 'course_completions', 'community_conversations',
            'research_publications', 'website_usage', 'organization_growth',
        ],
    },
    'layer_2_performance': {
        'title': 'Performance',
        'question': 'How well are we doing?',
        'examples': [
            'county_progress', 'volunteer_retention', 'research_quality',
            'academy_completion', 'coalition_participation', 'community_engagement',
        ],
    },
    'layer_3_trends': {
        'title': 'Trends',
        'question': 'How are we changing?',
        'examples': [
            'monthly_volunteer_growth', 'county_participation_trends',
            'research_productivity', 'leadership_development', 'relationship_growth',
            'community_health',
        ],
    },
    'layer_4_forecasting': {
        'title': 'Forecasting',
        'question': 'What is likely to happen?',
        'examples': [
            'county_readiness', 'leadership_shortages', 'volunteer_burnout_risk',
            'recruitment_projections', 'timeline_confidence', 'engagement_forecasts',
        ],
    },
    'layer_5_recommendations': {
        'title': 'Recommendations',
        'question': 'What should we do next?',
        'examples': ['prioritized_recommendations_supported_by_data'],
    },
}

EXECUTIVE_SCORECARDS = [
    'institution', 'research', 'academy', 'volunteer_network', 'coalition',
    'county_operations', 'city_operations', 'neighborhood_operations',
    'communications', 'technology', 'governance',
]

SCORECARD_FIELDS = ['current_performance', 'trend', 'target', 'risk', 'recommended_actions']

COUNTY_INTELLIGENCE_METRICS = [
    'volunteer_growth', 'leadership_pipeline', 'academy_participation',
    'community_conversations', 'organization_density', 'research_resources',
    'public_engagement', 'participation_progress_15pct', 'county_health_score',
    'mc_recommendations',
]

CITY_INTELLIGENCE_METRICS = [
    'participation_score', 'education_leader_status', 'volunteer_activity',
    'community_health', 'neighborhood_development', 'event_participation',
    'growth_forecasts',
]

COMMUNITY_HEALTH_INDEX_INDICATORS = [
    'learning_participation', 'volunteer_engagement', 'leadership_development',
    'coalition_strength', 'community_conversations', 'educational_events',
    'relationship_growth', 'resource_availability',
]

INSTITUTIONAL_HEALTH_INDEX_COMPONENTS = [
    'research', 'technology', 'knowledge_platform', 'mission_control', 'academy',
    'volunteer_network', 'coalition', 'county_readiness', 'city_readiness',
    'communications', 'governance', 'ai_systems',
]

GOAL_TRACKING_TARGETS = [
    {'id': 'software_completion', 'target_date': software_completion_date, 'label': 'Software complete'},
    {'id': 'county_milestone', 'target_date': county_milestone_date, 'label': '75 counties represented'},
    {'id': 'city_leadership', 'target': target_cities, 'label': '250 largest cities leadership development'},
    {'id': 'engagement', 'target_pct': engagement_goal_pct, 'label': '15% participation per county/city'},
    {'id': 'arkansans_connected', 'target': arkansans_connected_goal, 'label': '200,000 Arkansans connected'},
    {'id': 'organizational_readiness', 'target_date': organizational_readiness_date, 'label': 'Organizational readiness'},
]

PREDICTIVE_ANALYTICS = [
    'volunteer_recruitment_needs', 'education_leader_pipeline', 'county_readiness_probability',
    'project_completion_confidence', 'community_growth', 'resource_demand',
    'training_requirements',
]

AI_RECOMMENDATION_TYPES = [
    'counties_needing_support', 'cities_ready_for_expansion',
    'high_performing_educational_resources', 'volunteer_recognition_opportunities',
    'research_priorities', 'coalition_opportunities', 'scheduling_conflicts',
]

EXECUTIVE_REPORT_TYPES = [
    'daily_executive_brief', 'weekly_operational_report', 'monthly_institutional_report',
    'quarterly_strategic_review', 'annual_institutional_assessment',
]

BENCHMARKING_COMPARISONS = [
    'month_over_month', 'quarter_over_quarter', 'year_over_year',
    'county_vs_statewide', 'city_vs_statewide', 'department_vs_target',
]

ANALYTICS_VISUALIZATIONS = [
    'executive_scorecards', 'heat_maps', 'trend_lines', 'progress_gauges',
    'forecast_charts', 'county_maps', 'relationship_graphs', 'leadership_pipelines',
]

MC_ANALYTICS_DASHBOARD = [
    'institutional_health_index', 'community_health_index', 'county_rankings',
    'city_rankings', 'goal_completion', 'volunteer_forecasts', 'education_forecasts',
    'research_activity', 'coalition_growth', 'strategic_risks', 'executive_priorities',
]

ANALYTICS_SYSTEM_CHAIN = [
    'mission_control', 'knowledge_platform', 'research_institute',
    'community_education_academy', 'volunteer_network', 'coalition_network',
    'county_operating_system', 'city_operating_system', 'neighborhood_operating_system',
    'relationship_intelligence', 'ai_localbrains',
]

INSTITUTIONAL_ANALYTICS_MANIFEST = {
    'version': '1.0',
    'build': 101,
    'package': 'IMP-19',
    'updated': today,
    'title': 'Master Analytics, Institutional Intelligence & Predictive Insights Engine',
    'constitution': '/docs/IMPLEMENTATION_PACKAGE_19_INSTITUTIONAL_ANALYTICS.md',
    'source_registries': {
        'impact_measurement': '/data/impact-measurement.json',
        'civic_intelligence': '/data/civic-intelligence.json',
        'civic_intelligence_command_center': '/data/civic-intelligence-command-center.json',
        'relationship_intelligence': '/data/relationship-intelligence-manifest.json',
        'local_operating_systems': '/data/local-operating-systems-manifest.json',
        'volunteer_network': '/data/volunteer-network-manifest.json',
        'time_intelligence': '/data/time-intelligence-manifest.json',
    },
    'philosophy': 'Measure only what helps improve the mission — every metric answers a meaningful question',
    'governing_principle': (
        'Institutional intelligence exists to support human judgment—not replace it'
    ),
    'master_timeline': MASTER_TIMELINE,
    'software_completion_date': software_completion_date,
    'county_milestone_date': county_milestone_date,
    'organizational_readiness_date': organizational_readiness_date,
    'days_to_software': days_to_software,
    'days_to_county_milestone': days_to_county_milestone,
    'days_to_organizational': days_to_organizational,
    'intelligence_layers': ANALYTICS_INTELLIGENCE_LAYERS,
    'intelligence_layer_count': len(ANALYTICS_INTELLIGENCE_LAYERS),
    'executive_scorecards': EXECUTIVE_SCORECARDS,
    'executive_scorecard_count': len(EXECUTIVE_SCORECARDS),
    'scorecard_fields': SCORECARD_FIELDS,
    'county_intelligence_metrics': COUNTY_INTELLIGENCE_METRICS,
    'city_intelligence_metrics': CITY_INTELLIGENCE_METRICS,
    'community_health_index_indicators': COMMUNITY_HEALTH_INDEX_INDICATORS,
    'community_health_indicator_count': len(COMMUNITY_HEALTH_INDEX_INDICATORS),
    'institutional_health_index_components': INSTITUTIONAL_HEALTH_INDEX_COMPONENTS,
    'institutional_health_component_count': len(INSTITUTIONAL_HEALTH_INDEX_COMPONENTS),
    'goal_tracking_targets': GOAL_TRACKING_TARGETS,
    'predictive_analytics': PREDICTIVE_ANALYTICS,
    'predictive_analytics_count': len(PREDICTIVE_ANALYTICS),
    'ai_recommendation_types': AI_RECOMMENDATION_TYPES,
    'executive_report_types': EXECUTIVE_REPORT_TYPES,
    'benchmarking_comparisons': BENCHMARKING_COMPARISONS,
    'analytics_visualizations': ANALYTICS_VISUALIZATIONS,
    'mc_analytics_dashboard': MC_ANALYTICS_DASHBOARD,
    'organizational_goals': {
        'counties_total': 75,
        'target_cities': target_cities,
        'engagement_goal_pct': engagement_goal_pct,
        'arkansans_connected_goal': arkansans_connected_goal,
    },
    'analytics_system_chain': ANALYTICS_SYSTEM_CHAIN,
    'institutional_systems': INSTITUTIONAL_OS_SYSTEMS,
    'mc_dashboard': '/mission-control/impact-measurement.html',
    'packages_completed': 19,
    'packages_total': 50,
    'packages_complete_pct': 38,
    'engineering_note': 'Doctrinal IMP-19 Institutional Analytics; engineering IMP-19 is page templates',
    'status': 'documented',
    'implemented': False,
}

AUTOMATION_PHILOSOPHY_CHECKS = [
    'is_repetitive', 'is_rules_based', 'improves_consistency',
    'reduces_volunteer_workload', 'preserves_human_oversight',
]

WORKFLOW_ENGINE_STEPS = [
    'trigger', 'validation', 'ai_assistance', 'task_execution',
    'human_review', 'notification', 'mission_control_update', 'institutional_memory',
]

WORKFLOW_CATEGORIES = {
    'volunteer': [
        'registration', 'onboarding', 'training_reminders', 'mentor_assignment',
        'recognition', 'leadership_advancement', 'county_assignment',
    ],
    'research': [
        'research_proposal', 'evidence_review', 'citation_verification',
        'editorial_review', 'publication_approval', 'scheduled_review', 'archive',
    ],
    'academy': [
        'course_enrollment', 'lesson_completion', 'certificate_issuance',
        'education_leader_progression', 'continuing_education_reminders',
        'learning_recommendations',
    ],
    'coalition': [
        'organization_onboarding', 'partnership_review', 'shared_event_approvals',
        'resource_sharing', 'coalition_communications', 'annual_partnership_review',
    ],
    'community': [
        'community_conversation_creation', 'event_registration', 'attendance_tracking',
        'follow_up_communication', 'resource_distribution', 'community_feedback',
    ],
    'mission_control': [
        'executive_briefings', 'daily_reports', 'weekly_scorecards', 'risk_alerts',
        'goal_monitoring', 'county_readiness_updates', 'forecast_generation',
    ],
}

APPROVAL_RULE_TYPES = [
    'public_content', 'research_publication', 'leadership_role_assignment',
    'organization_onboarding', 'policy_changes', 'system_configuration',
]

AUTOMATION_RULES = [
    'welcome_sequence_after_registration', 'recommend_academy_after_onboarding',
    'assign_mentor_after_training', 'notify_county_leader_new_volunteer',
    'research_review_deadline_reminders', 'daily_executive_briefing',
    'publish_approved_content_on_schedule', 'update_mission_control_automatically',
]

AI_WORKFLOW_ASSISTANCE = [
    'draft_documents', 'summarize_submissions', 'identify_missing_information',
    'suggest_next_actions', 'prepare_reports', 'route_requests', 'prioritize_work',
]

EVENT_AUTOMATION_TASKS = [
    'invitations', 'reminders', 'attendance_tracking', 'follow_up_emails',
    'resource_sharing', 'survey_distribution', 'mission_control_updates',
]

CALENDAR_AUTOMATION = [
    'recurring_meetings', 'training_reminders', 'review_schedules',
    'leadership_check_ins', 'annual_planning', 'publication_calendar',
]

NOTIFICATION_AUTOMATION = [
    'volunteer_assignments', 'community_events', 'research_updates',
    'course_reminders', 'leadership_alerts', 'mission_control_warnings',
]

GOAL_AUTOMATION_MONITORS = [
    'software_completion', 'county_representation', 'education_leader_development',
    'city_leadership', 'participation_15pct', 'arkansans_connected_200k',
]

PROCESS_LIBRARY_FIELDS = [
    'purpose', 'trigger', 'participants', 'automation_steps',
    'human_responsibilities', 'mission_control_metrics',
]

AUTOMATION_DASHBOARD_METRICS = [
    'active_workflows', 'completed_workflows', 'failed_workflows',
    'pending_approvals', 'automation_savings', 'volunteer_time_saved',
    'workflow_bottlenecks', 'system_health',
]

AUTOMATION_SAFETY_CONTROLS = [
    'no_independent_policy_changes', 'no_unreviewed_sensitive_publication',
    'no_permission_alteration', 'no_governance_document_modification',
    'no_autonomous_leadership_appointments', 'no_unauthorized_restricted_access',
]

AUTOMATION_SYSTEM_CHAIN = [
    'mission_control', 'knowledge_platform', 'research_institute',
    'community_education_academy', 'volunteer_network', 'coalition_network',
    'county_operating_system', 'city_operating_system', 'calendar_brain',
    'communications', 'ai_localbrains',
]

AUTOMATION_ENGINE_MANIFEST = {
    'version': '1.0',
    'build': 101,
    'package': 'IMP-20',
    'updated': today,
    'title': 'Master Automation Engine, Workflow Orchestration & Institutional Process Management',
    'constitution': '/docs/IMPLEMENTATION_PACKAGE_20_AUTOMATION_ENGINE.md',
    'source_registries': {
        'pmo_execution_office': '/data/pmo-execution-office.json',
        'execution_schedule': '/data/execution-schedule.json',
        'institutional_analytics': '/data/institutional-analytics-manifest.json',
        'time_intelligence': '/data/time-intelligence-manifest.json',
        'communication_platform': '/data/communication-platform-manifest.json',
        'volunteer_network': '/data/volunteer-network-manifest.json',
        'content_management': '/data/content-management-manifest.json',
    },
    'philosophy': 'Automation eliminates repetitive admin work—not human relationships',
    'governing_principle': (
        'The highest purpose of automation is to return time to people for research, '
        'education, community conversations, and mentorship'
    ),
    'master_timeline': MASTER_TIMELINE,
    'software_completion_date': software_completion_date,
    'county_milestone_date': county_milestone_date,
    'organizational_readiness_date': organizational_readiness_date,
    'days_to_software': days_to_software,
    'days_to_county_milestone': days_to_county_milestone,
    'days_to_organizational': days_to_organizational,
    'automation_philosophy_checks': AUTOMATION_PHILOSOPHY_CHECKS,
    'workflow_engine_steps': WORKFLOW_ENGINE_STEPS,
    'workflow_engine_step_count': len(WORKFLOW_ENGINE_STEPS),
    'workflow_categories': WORKFLOW_CATEGORIES,
    'workflow_category_count': len(WORKFLOW_CATEGORIES),
    'workflow_type_count': sum(len(v) for v in WORKFLOW_CATEGORIES.values()),
    'approval_rule_types': APPROVAL_RULE_TYPES,
    'automation_rules': AUTOMATION_RULES,
    'ai_workflow_assistance': AI_WORKFLOW_ASSISTANCE,
    'event_automation_tasks': EVENT_AUTOMATION_TASKS,
    'calendar_automation': CALENDAR_AUTOMATION,
    'notification_automation': NOTIFICATION_AUTOMATION,
    'goal_automation_monitors': GOAL_AUTOMATION_MONITORS,
    'process_library_fields': PROCESS_LIBRARY_FIELDS,
    'automation_dashboard_metrics': AUTOMATION_DASHBOARD_METRICS,
    'automation_safety_controls': AUTOMATION_SAFETY_CONTROLS,
    'organizational_goals': {
        'counties_total': 75,
        'target_cities': target_cities,
        'engagement_goal_pct': engagement_goal_pct,
        'arkansans_connected_goal': arkansans_connected_goal,
    },
    'automation_system_chain': AUTOMATION_SYSTEM_CHAIN,
    'institutional_systems': INSTITUTIONAL_OS_SYSTEMS,
    'mc_dashboard': '/mission-control/pmo-execution-office.html',
    'packages_completed': 20,
    'packages_total': 50,
    'packages_complete_pct': 40,
    'engineering_note': 'Doctrinal IMP-20 Automation Engine; engineering IMP-20 is accessibility baseline audit',
    'status': 'documented',
    'implemented': False,
}

CORE_PAGE_QUESTIONS = [
    'why_should_i_care', 'what_can_i_learn', 'what_can_i_do_next',
]

HOMEPAGE_SECTIONS = [
    'hero', 'why_this_matters', 'begin_learning', 'explore_arkansas',
    'featured_research', 'community_impact', 'get_involved',
]

HERO_ELEMENTS = [
    'institution_explanation', 'primary_call_to_action', 'search', 'explore_arkansas',
]

BEGIN_LEARNING_ENTRY_POINTS = [
    'new_visitors', 'students', 'educators', 'volunteers', 'researchers', 'community_leaders',
]

GLOBAL_SEARCH_EXAMPLES = [
    'what_is_citizens_united', 'what_does_campaign_finance_mean',
    'who_represents_my_county', 'what_events_are_near_me', 'what_courses_should_i_take',
]

ARKANSAS_MAP_LAYERS = [
    'counties', 'cities', 'community_conversations', 'education_leaders',
    'organizations', 'academy_opportunities', 'events', 'research_resources',
]

COUNTY_PAGE_SECTIONS = [
    'overview', 'research', 'education_leaders', 'organizations', 'events',
    'community_conversations', 'volunteer_opportunities', 'academy',
    'county_progress', 'local_ai_assistant',
]

CITY_PAGE_SECTIONS = [
    'overview', 'leadership', 'neighborhoods', 'events', 'organizations',
    'educational_resources', 'volunteer_opportunities', 'community_health',
]

STORYTELLING_FORMATS = [
    'stories', 'timelines', 'interactive_graphics', 'videos',
    'case_studies', 'historical_context',
]

ACCESSIBILITY_STANDARDS = [
    'keyboard_navigation', 'screen_readers', 'high_contrast', 'responsive_layouts',
    'alternative_text', 'readable_typography', 'captioned_media',
]

PUBLIC_AI_GUIDE_EXAMPLES = [
    'what_does_this_court_case_mean', 'how_do_ballot_initiatives_work',
    'show_me_beginner_lessons', 'what_organizations_are_near_me',
    'what_events_are_coming_up',
]

PUBLIC_ENGAGEMENT_ACTIONS = [
    'bookmark_resources', 'register_for_events', 'join_academy', 'volunteer',
    'subscribe_to_updates', 'request_presentations', 'suggest_research_topics',
    'report_corrections',
]

PUBLIC_DASHBOARD_METRICS = [
    'counties_represented', 'education_leaders', 'community_conversations',
    'research_completed', 'academy_participation', 'organizations_involved',
    'statewide_goal_progress',
]

PERFORMANCE_STANDARDS = [
    'fast_page_load', 'rapid_search', 'intuitive_navigation',
    'desktop', 'tablet', 'mobile', 'public_libraries', 'low_bandwidth',
]

MC_PUBLIC_INTEGRATION_METRICS = [
    'website_traffic', 'search_activity', 'popular_topics', 'learning_pathways',
    'volunteer_conversions', 'county_interest', 'event_registrations',
    'engagement_trends', 'public_feedback',
]

PUBLIC_WEBSITE_SYSTEM_CHAIN = [
    'mission_control', 'knowledge_platform', 'research_institute',
    'community_education_academy', 'county_operating_system', 'city_operating_system',
    'volunteer_network', 'coalition_network', 'ai_localbrains', 'communications',
]

PUBLIC_WEBSITE_MANIFEST = {
    'version': '1.0',
    'build': 101,
    'package': 'IMP-21',
    'updated': today,
    'title': 'Master Public Website, Digital Experience & Citizen Engagement Platform',
    'constitution': '/docs/IMPLEMENTATION_PACKAGE_21_PUBLIC_WEBSITE.md',
    'source_registries': {
        'visitor_journey': '/data/visitor-journey.json',
        'route_manifest': '/data/route-manifest.json',
        'local_operating_systems': '/data/local-operating-systems-manifest.json',
        'education_academy': '/data/education-academy-manifest.json',
        'knowledge_graph': '/data/knowledge-graph-manifest.json',
        'automation_engine': '/data/automation-engine-manifest.json',
    },
    'philosophy': 'Every page answers: Why should I care? What can I learn? What can I do next?',
    'governing_principle': (
        'A trusted institution should welcome people naturally — every page helps an '
        'Arkansan move toward understanding, participation, and community'
    ),
    'master_timeline': MASTER_TIMELINE,
    'software_completion_date': software_completion_date,
    'county_milestone_date': county_milestone_date,
    'organizational_readiness_date': organizational_readiness_date,
    'days_to_software': days_to_software,
    'days_to_county_milestone': days_to_county_milestone,
    'days_to_organizational': days_to_organizational,
    'core_page_questions': CORE_PAGE_QUESTIONS,
    'homepage_sections': HOMEPAGE_SECTIONS,
    'homepage_section_count': len(HOMEPAGE_SECTIONS),
    'hero_elements': HERO_ELEMENTS,
    'begin_learning_entry_points': BEGIN_LEARNING_ENTRY_POINTS,
    'global_search_examples': GLOBAL_SEARCH_EXAMPLES,
    'arkansas_map_layers': ARKANSAS_MAP_LAYERS,
    'arkansas_map_layer_count': len(ARKANSAS_MAP_LAYERS),
    'county_page_sections': COUNTY_PAGE_SECTIONS,
    'city_page_sections': CITY_PAGE_SECTIONS,
    'storytelling_formats': STORYTELLING_FORMATS,
    'accessibility_standards': ACCESSIBILITY_STANDARDS,
    'accessibility_standard_count': len(ACCESSIBILITY_STANDARDS),
    'public_ai_guide_examples': PUBLIC_AI_GUIDE_EXAMPLES,
    'public_engagement_actions': PUBLIC_ENGAGEMENT_ACTIONS,
    'public_dashboard_metrics': PUBLIC_DASHBOARD_METRICS,
    'performance_standards': PERFORMANCE_STANDARDS,
    'mc_public_integration_metrics': MC_PUBLIC_INTEGRATION_METRICS,
    'organizational_goals': {
        'counties_total': 75,
        'target_cities': target_cities,
        'engagement_goal_pct': engagement_goal_pct,
        'arkansans_connected_goal': arkansans_connected_goal,
    },
    'public_website_system_chain': PUBLIC_WEBSITE_SYSTEM_CHAIN,
    'institutional_systems': INSTITUTIONAL_OS_SYSTEMS,
    'mc_dashboard': '/mission-control/visitor-journey.html',
    'public_site_url': '/',
    'packages_completed': 21,
    'packages_total': 50,
    'packages_complete_pct': 42,
    'engineering_note': 'Doctrinal IMP-21 Public Website; engineering IMP-21 is Prisma schema core entities',
    'status': 'documented',
    'implemented': False,
}

PWA_CAPABILITIES = [
    'home_screen_install', 'fast_startup', 'offline_capabilities', 'push_notifications',
    'background_sync', 'app_like_experience',
]

MOBILE_DASHBOARD_WIDGETS = [
    'todays_schedule', 'upcoming_events', 'learning_progress', 'volunteer_assignments',
    'community_conversations', 'county_updates', 'messages', 'personal_ai',
]

MOBILE_VOLUNTEER_ACTIONS = [
    'view_assignments', 'accept_projects', 'navigate_to_events', 'access_training',
    'read_resources', 'check_schedules', 'message_mentors', 'record_community_activity',
]

EDUCATION_LEADER_MOBILE_TOOLS = [
    'launch_presentations', 'discussion_guides', 'research_summaries', 'check_attendance',
    'schedule_follow_ups', 'recruit_volunteers', 'ai_q_and_a',
]

OFFLINE_CACHE_RESOURCES = [
    'downloaded_lessons', 'presentation_materials', 'county_profiles',
    'volunteer_assignments', 'event_agendas', 'community_conversation_guides',
]

QR_CODE_TARGETS = [
    'course_enrollment', 'community_conversations', 'county_pages', 'city_pages',
    'volunteer_sign_up', 'organization_profiles', 'presentation_materials',
]

EVENT_CHECK_IN_TYPES = [
    'qr_code_check_in', 'attendance_tracking', 'volunteer_sign_in',
    'presentation_attendance', 'academy_participation', 'organization_events',
]

LOCATION_RECOMMENDATIONS = [
    'nearby_conversations', 'county_events', 'academy_classes',
    'volunteer_opportunities', 'partner_organizations', 'educational_resources',
]

MOBILE_AI_CAPABILITIES = [
    'questions', 'research', 'scheduling', 'directions', 'volunteer_guidance',
    'presentation_preparation', 'county_information', 'community_recommendations',
]

MOBILE_NOTIFICATION_TYPES = [
    'event_reminders', 'volunteer_assignments', 'course_reminders', 'research_updates',
    'community_announcements', 'leadership_messages', 'mission_control_alerts',
]

MOBILE_MEDIA_ACTIONS = [
    'watch_videos', 'listen_podcasts', 'download_presentations',
    'share_resources', 'read_research', 'bookmark_materials',
]

FIELD_DATA_COLLECTION = [
    'community_conversations', 'presentation_attendance', 'volunteer_interest',
    'local_resource_updates', 'organization_information', 'community_observations',
]

TRAVEL_SUPPORT_FEATURES = [
    'driving_directions', 'multi_stop_itineraries', 'regional_travel',
    'event_routing', 'county_visit_planning',
]

MOBILE_ACCESSIBILITY = [
    'large_touch_targets', 'voice_input', 'screen_readers', 'high_contrast',
    'offline_reading', 'simple_navigation',
]

MC_MOBILE_INTEGRATION_METRICS = [
    'mobile_usage', 'offline_usage', 'qr_scans', 'field_activity',
    'volunteer_check_ins', 'presentation_attendance', 'location_engagement',
    'event_participation',
]

MOBILE_SYSTEM_CHAIN = [
    'mission_control', 'volunteer_network', 'community_education_academy',
    'county_operating_system', 'city_operating_system', 'neighborhood_operating_system',
    'calendar_brain', 'relationship_intelligence', 'knowledge_platform',
    'communications', 'ai_localbrains',
]

MOBILE_PWA_MANIFEST = {
    'version': '1.0',
    'build': 101,
    'package': 'IMP-22',
    'updated': today,
    'title': 'Master Mobile Experience, Progressive Web App & Field Operations Platform',
    'constitution': '/docs/IMPLEMENTATION_PACKAGE_22_MOBILE_PWA.md',
    'source_registries': {
        'public_website': '/data/public-website-manifest.json',
        'volunteer_network': '/data/volunteer-network-manifest.json',
        'education_academy': '/data/education-academy-manifest.json',
        'local_operating_systems': '/data/local-operating-systems-manifest.json',
        'time_intelligence': '/data/time-intelligence-manifest.json',
        'relationship_intelligence': '/data/relationship-intelligence-manifest.json',
        'outreach_engine': '/data/outreach-engine.json',
    },
    'philosophy': 'Mobile is a first-class experience — design for real life in the field',
    'governing_principle': (
        'The institution should travel wherever its volunteers travel — immediate access '
        'to knowledge, tools, relationships, and resources in every community setting'
    ),
    'master_timeline': MASTER_TIMELINE,
    'software_completion_date': software_completion_date,
    'county_milestone_date': county_milestone_date,
    'organizational_readiness_date': organizational_readiness_date,
    'days_to_software': days_to_software,
    'days_to_county_milestone': days_to_county_milestone,
    'days_to_organizational': days_to_organizational,
    'pwa_capabilities': PWA_CAPABILITIES,
    'pwa_capability_count': len(PWA_CAPABILITIES),
    'mobile_dashboard_widgets': MOBILE_DASHBOARD_WIDGETS,
    'mobile_volunteer_actions': MOBILE_VOLUNTEER_ACTIONS,
    'education_leader_mobile_tools': EDUCATION_LEADER_MOBILE_TOOLS,
    'offline_cache_resources': OFFLINE_CACHE_RESOURCES,
    'qr_code_targets': QR_CODE_TARGETS,
    'qr_code_target_count': len(QR_CODE_TARGETS),
    'event_check_in_types': EVENT_CHECK_IN_TYPES,
    'location_recommendations': LOCATION_RECOMMENDATIONS,
    'mobile_ai_capabilities': MOBILE_AI_CAPABILITIES,
    'mobile_notification_types': MOBILE_NOTIFICATION_TYPES,
    'mobile_media_actions': MOBILE_MEDIA_ACTIONS,
    'field_data_collection': FIELD_DATA_COLLECTION,
    'travel_support_features': TRAVEL_SUPPORT_FEATURES,
    'mobile_accessibility': MOBILE_ACCESSIBILITY,
    'mobile_accessibility_count': len(MOBILE_ACCESSIBILITY),
    'mc_mobile_integration_metrics': MC_MOBILE_INTEGRATION_METRICS,
    'organizational_goals': {
        'counties_total': 75,
        'target_cities': target_cities,
        'engagement_goal_pct': engagement_goal_pct,
        'arkansans_connected_goal': arkansans_connected_goal,
    },
    'mobile_system_chain': MOBILE_SYSTEM_CHAIN,
    'institutional_systems': INSTITUTIONAL_OS_SYSTEMS,
    'mc_dashboard': '/mission-control/outreach.html',
    'packages_completed': 22,
    'packages_total': 50,
    'packages_complete_pct': 44,
    'engineering_note': 'Doctrinal IMP-22 Mobile PWA; engineering IMP-22 is Prisma schema knowledge entities',
    'status': 'documented',
    'implemented': False,
}

LIBRARY_PHILOSOPHY_PRINCIPLES = [
    'stored_once', 'versioned', 'searchable', 'connected',
    'protected', 'reusable', 'archived',
]

DIGITAL_LIBRARY_COLLECTIONS = {
    'research': [
        'court_opinions', 'research_papers', 'white_papers', 'academic_journals',
        'government_publications', 'historical_documents', 'legislative_materials',
    ],
    'education': [
        'courses', 'lessons', 'presentations', 'study_guides', 'discussion_guides',
        'worksheets', 'learning_resources',
    ],
    'media': [
        'videos', 'images', 'podcasts', 'infographics', 'photography',
        'logos', 'graphics', 'animations',
    ],
    'governance': [
        'constitution', 'operating_manuals', 'policies', 'implementation_packages',
        'governance_decisions', 'meeting_records', 'strategic_plans',
    ],
    'community': [
        'community_conversations', 'meeting_notes', 'county_reports', 'city_reports',
        'volunteer_reports', 'listening_sessions', 'community_requests',
    ],
    'operations': [
        'project_documents', 'pmo_reports', 'templates', 'forms',
        'training_manuals', 'checklists', 'technical_documentation',
    ],
}

DOCUMENT_METADATA_FIELDS = [
    'unique_id', 'title', 'summary', 'author', 'contributors', 'date_created',
    'date_updated', 'review_schedule', 'category', 'tags', 'county_relevance',
    'city_relevance', 'organizations', 'related_research', 'visibility_level',
    'version_number',
]

VERSION_CONTROL_HISTORY = [
    'current_version', 'previous_versions', 'change_history', 'author_history',
    'approval_history', 'publication_history',
]

ARCHIVE_CATEGORIES = [
    'historical_research', 'retired_policies', 'superseded_publications',
    'completed_projects', 'legacy_training', 'past_reports', 'institutional_history',
]

SEARCH_DIMENSIONS = [
    'title', 'keyword', 'question', 'topic', 'county', 'city', 'organization',
    'author', 'court_case', 'research_category', 'date', 'document_type',
    'natural_language_ai',
]

DOCUMENT_RELATIONSHIP_TARGETS = [
    'research', 'evidence', 'claims', 'courses', 'lessons', 'organizations',
    'counties', 'cities', 'projects', 'events', 'community_conversations',
]

DOCUMENT_ACCESS_LEVELS = [
    'public', 'registered_member', 'volunteer', 'education_leader',
    'organization', 'executive', 'administrator',
]

AI_DOCUMENT_ASSISTANT = [
    'find_documents', 'summarize_reports', 'compare_versions',
    'identify_related_resources', 'extract_citations', 'executive_summaries',
    'prepare_presentations', 'suggest_additional_reading',
]

DOCUMENT_LIFECYCLE_STAGES = [
    'draft', 'review', 'approved', 'published', 'periodic_review',
    'updated', 'archived', 'historical_record',
]

MEDIA_MANAGEMENT_FEATURES = [
    'automatic_metadata', 'captions', 'transcripts', 'alternative_text',
    'copyright_information', 'usage_rights', 'optimized_delivery',
]

MEETING_RECORD_COMPONENTS = [
    'agenda', 'attendance', 'notes', 'decisions', 'action_items',
    'related_documents', 'follow_up_schedule',
]

MC_LIBRARY_DASHBOARD_METRICS = [
    'documents_created', 'documents_reviewed', 'review_compliance', 'archive_growth',
    'library_usage', 'search_performance', 'knowledge_gaps',
    'most_used_resources', 'county_resource_completeness',
]

OCTOBER_COUNTY_LIBRARY_REQUIREMENTS = [
    'county_profile', 'local_government_overview', 'educational_resources',
    'community_contacts', 'local_organizations', 'presentation_materials',
    'community_conversation_toolkit',
]

DIGITAL_LIBRARY_SYSTEM_CHAIN = [
    'mission_control', 'knowledge_platform', 'research_institute',
    'community_education_academy', 'volunteer_network', 'county_operating_system',
    'city_operating_system', 'neighborhood_operating_system', 'communications',
    'ai_localbrains', 'relationship_intelligence',
]

DIGITAL_LIBRARY_MANIFEST = {
    'version': '1.0',
    'build': 101,
    'package': 'IMP-23',
    'updated': today,
    'title': 'Master Document Management, Digital Library & Institutional Archive',
    'constitution': '/docs/IMPLEMENTATION_PACKAGE_23_DIGITAL_LIBRARY.md',
    'source_registries': {
        'master_research_library': '/data/master-research-library.json',
        'encyclopedia': '/data/encyclopedia-knowledge-library.json',
        'content_management': '/data/content-management-manifest.json',
        'knowledge_graph': '/data/knowledge-graph-manifest.json',
        'evidence_registry': '/data/evidence-registry.json',
        'local_operating_systems': '/data/local-operating-systems-manifest.json',
    },
    'philosophy': 'Nothing important should ever be lost — every asset becomes permanent institutional memory',
    'governing_principle': (
        'Institutions endure because they remember; knowledge accumulated today '
        'must strengthen Arkansas for generations to come'
    ),
    'master_timeline': MASTER_TIMELINE,
    'software_completion_date': software_completion_date,
    'county_milestone_date': county_milestone_date,
    'organizational_readiness_date': organizational_readiness_date,
    'days_to_software': days_to_software,
    'days_to_county_milestone': days_to_county_milestone,
    'days_to_organizational': days_to_organizational,
    'library_philosophy_principles': LIBRARY_PHILOSOPHY_PRINCIPLES,
    'digital_library_collections': DIGITAL_LIBRARY_COLLECTIONS,
    'collection_count': len(DIGITAL_LIBRARY_COLLECTIONS),
    'document_metadata_fields': DOCUMENT_METADATA_FIELDS,
    'metadata_field_count': len(DOCUMENT_METADATA_FIELDS),
    'version_control_history': VERSION_CONTROL_HISTORY,
    'archive_categories': ARCHIVE_CATEGORIES,
    'search_dimensions': SEARCH_DIMENSIONS,
    'document_relationship_targets': DOCUMENT_RELATIONSHIP_TARGETS,
    'document_access_levels': DOCUMENT_ACCESS_LEVELS,
    'ai_document_assistant': AI_DOCUMENT_ASSISTANT,
    'document_lifecycle_stages': DOCUMENT_LIFECYCLE_STAGES,
    'lifecycle_stage_count': len(DOCUMENT_LIFECYCLE_STAGES),
    'media_management_features': MEDIA_MANAGEMENT_FEATURES,
    'meeting_record_components': MEETING_RECORD_COMPONENTS,
    'mc_library_dashboard_metrics': MC_LIBRARY_DASHBOARD_METRICS,
    'october_county_library': {
        'target_date': county_milestone_date,
        'requirements': OCTOBER_COUNTY_LIBRARY_REQUIREMENTS,
        'label': 'Foundational digital library in every county',
    },
    'organizational_goals': {
        'counties_total': 75,
        'target_cities': target_cities,
        'engagement_goal_pct': engagement_goal_pct,
        'arkansans_connected_goal': arkansans_connected_goal,
    },
    'digital_library_system_chain': DIGITAL_LIBRARY_SYSTEM_CHAIN,
    'institutional_systems': INSTITUTIONAL_OS_SYSTEMS,
    'mc_dashboard': '/mission-control/research-library.html',
    'packages_completed': 23,
    'packages_total': 50,
    'packages_complete_pct': 46,
    'engineering_note': 'Doctrinal IMP-23 Digital Library; engineering IMP-23 is Neon provisioning and migrations',
    'status': 'documented',
    'implemented': False,
}

INTEGRATION_PIPELINE_STEPS = [
    'external_service', 'integration_layer', 'validation', 'security_review',
    'internal_data_model', 'mission_control', 'knowledge_platform',
]

INTEGRATION_CATEGORIES = {
    'identity': {
        'providers': ['google', 'microsoft', 'apple'],
        'principle': 'institutional_identity_authoritative',
    },
    'calendar': {
        'providers': ['google_calendar', 'microsoft_outlook', 'apple_calendar', 'ics'],
        'principle': 'optional_per_user_sync',
    },
    'email': {
        'providers': ['google_workspace', 'microsoft_365', 'smtp_compatible'],
        'capabilities': [
            'invitations', 'newsletters', 'volunteer_communication', 'research_notifications',
        ],
    },
    'mapping': {
        'capabilities': [
            'county_visualization', 'city_maps', 'driving_directions', 'regional_planning',
            'event_locations', 'volunteer_routing',
        ],
    },
    'video_meetings': {
        'providers': ['zoom', 'google_meet', 'microsoft_teams', 'future_providers'],
        'features': [
            'scheduling', 'registration', 'attendance', 'recording_references', 'calendar_sync',
        ],
    },
    'artificial_intelligence': {
        'principle': 'ai_gateway_modular_providers',
        'rule': 'institutional_knowledge_remains_internal',
    },
    'government_data': {
        'sources': [
            'election_information', 'legislative_information', 'court_information',
            'census_demographic', 'geographic_data',
        ],
        'requirement': 'attributed_and_versioned',
    },
    'file_storage': {
        'asset_types': [
            'documents', 'videos', 'images', 'presentations', 'downloads',
        ],
        'principle': 'indexed_in_institutional_library',
    },
}

OPEN_API_USE_CASES = [
    'county_dashboards', 'organization_integrations', 'educational_resources',
    'research_search', 'calendar_feeds', 'public_statistics', 'mission_control_summaries',
]

INTERNAL_API_STANDARDS = [
    'authentication', 'validation', 'logging', 'error_reporting',
    'rate_limiting', 'monitoring', 'documentation',
]

INSTITUTIONAL_EVENTS = [
    'volunteer_joined', 'course_completed', 'research_published',
    'community_conversation_scheduled', 'organization_onboarded',
]

SYNC_PRINCIPLES = [
    'reliable', 'observable', 'recoverable', 'auditable', 'no_silent_failures',
]

INSTITUTIONAL_DATA_OWNERSHIP = [
    'research', 'educational_content', 'volunteer_records', 'organization_records',
    'knowledge_graph', 'mission_control_metrics', 'analytics',
]

INTEGRATION_SECURITY_STANDARDS = [
    'authentication', 'authorization', 'encryption', 'audit_logging',
    'permission_validation', 'monitoring', 'security_reviews',
]

AI_GATEWAY_BENEFITS = [
    'consistent_prompts', 'institutional_memory_access', 'permission_enforcement',
    'logging', 'future_provider_flexibility',
]

MC_INTEGRATION_DASHBOARD_METRICS = [
    'integration_status', 'sync_success', 'failed_synchronizations', 'api_health',
    'usage_statistics', 'external_dependencies', 'provider_availability',
]

OCTOBER_INTEGRATION_READINESS = [
    'calendar_synchronization', 'email_delivery', 'video_meeting_support', 'mapping',
    'ai_services', 'public_data_ingestion', 'secure_api_infrastructure',
]

INTEGRATION_SYSTEM_CHAIN = [
    'mission_control', 'knowledge_platform', 'calendar_brain', 'volunteer_network',
    'community_education_academy', 'county_operating_system', 'city_operating_system',
    'neighborhood_operating_system', 'communications', 'document_management',
    'ai_localbrains', 'external_services',
]

INTEGRATION_PLATFORM_MANIFEST = {
    'version': '1.0',
    'build': 101,
    'package': 'IMP-24',
    'updated': today,
    'title': 'Master Integration Platform, External Data Services & Open API Architecture',
    'constitution': '/docs/IMPLEMENTATION_PACKAGE_24_INTEGRATION_PLATFORM.md',
    'source_registries': {
        'technical_architecture': '/data/technical-architecture.json',
        'systems_integration': '/data/systems-integration.json',
        'time_intelligence': '/data/time-intelligence-manifest.json',
        'communication_platform': '/data/communication-platform-manifest.json',
        'digital_library': '/data/digital-library-manifest.json',
        'identity_auth': '/data/identity-auth-manifest.json',
    },
    'philosophy': 'The institution owns its data — external services provide capabilities',
    'governing_principle': (
        'Strong institutions cooperate without becoming dependent; integrations expand '
        'capabilities while preserving independence and protecting institutional knowledge'
    ),
    'master_timeline': MASTER_TIMELINE,
    'software_completion_date': software_completion_date,
    'county_milestone_date': county_milestone_date,
    'organizational_readiness_date': organizational_readiness_date,
    'days_to_software': days_to_software,
    'days_to_county_milestone': days_to_county_milestone,
    'days_to_organizational': days_to_organizational,
    'integration_pipeline_steps': INTEGRATION_PIPELINE_STEPS,
    'integration_categories': INTEGRATION_CATEGORIES,
    'integration_category_count': len(INTEGRATION_CATEGORIES),
    'open_api_use_cases': OPEN_API_USE_CASES,
    'internal_api_standards': INTERNAL_API_STANDARDS,
    'institutional_events': INSTITUTIONAL_EVENTS,
    'sync_principles': SYNC_PRINCIPLES,
    'institutional_data_ownership': INSTITUTIONAL_DATA_OWNERSHIP,
    'integration_security_standards': INTEGRATION_SECURITY_STANDARDS,
    'ai_gateway_benefits': AI_GATEWAY_BENEFITS,
    'mc_integration_dashboard_metrics': MC_INTEGRATION_DASHBOARD_METRICS,
    'october_integration_readiness': {
        'target_date': county_milestone_date,
        'requirements': OCTOBER_INTEGRATION_READINESS,
        'label': 'Statewide integration platform operational',
    },
    'organizational_goals': {
        'counties_total': 75,
        'target_cities': target_cities,
        'engagement_goal_pct': engagement_goal_pct,
        'arkansans_connected_goal': arkansans_connected_goal,
    },
    'integration_system_chain': INTEGRATION_SYSTEM_CHAIN,
    'institutional_systems': INSTITUTIONAL_OS_SYSTEMS,
    'mc_dashboard': '/mission-control/systems-integration.html',
    'packages_completed': 24,
    'packages_total': 50,
    'packages_complete_pct': 48,
    'engineering_note': 'Doctrinal IMP-24 Integration Platform; engineering IMP-24 is seed script from JSON registries',
    'status': 'documented',
    'implemented': False,
}

TRUST_PHILOSOPHY_VALUES = [
    'transparent', 'secure', 'accountable', 'privacy_conscious',
    'evidence_driven', 'auditable', 'respectful_of_users',
]

SECURITY_PRINCIPLES = [
    'least_privilege_access', 'role_based_authorization', 'mfa_elevated_roles',
    'encrypted_communications', 'encrypted_sensitive_data', 'continuous_monitoring',
    'comprehensive_audit_logging', 'defense_in_depth',
]

IDENTITY_PROTECTION_FEATURES = [
    'strong_passwords', 'password_reset', 'mfa_privileged_roles', 'session_expiration',
    'device_management_future', 'login_history', 'suspicious_login_detection_future',
]

PRIVACY_CONTROLS = [
    'communication_preferences', 'profile_visibility', 'volunteer_visibility',
    'organization_participation_visibility', 'notification_settings', 'public_profile_info',
]

DATA_CLASSIFICATION_LEVELS = [
    'public', 'internal', 'volunteer', 'education_leader', 'organization',
    'executive', 'administrative', 'restricted',
]

DATA_GOVERNANCE_FIELDS = [
    'owner', 'purpose', 'retention_policy', 'review_schedule',
    'access_policy', 'archive_policy', 'deletion_policy',
]

AUDIT_LOG_EVENTS = [
    'logins', 'permission_changes', 'research_publication', 'content_edits',
    'role_assignments', 'organization_changes', 'workflow_approvals',
    'system_administration',
]

BACKUP_STRATEGY_COMPONENTS = [
    'automated_backups', 'point_in_time_recovery', 'version_history',
    'off_site_storage', 'disaster_recovery_testing',
]

DISASTER_RECOVERY_SCENARIOS = [
    'database_restoration', 'media_restoration', 'configuration_recovery',
    'knowledge_restoration', 'infrastructure_recovery', 'operational_continuity',
]

COMPLIANCE_FRAMEWORK_AREAS = [
    'security_policies', 'privacy_practices', 'accessibility_standards',
    'data_governance', 'volunteer_procedures', 'content_review_standards',
    'institutional_ethics',
]

ACCESSIBILITY_COMPLIANCE_CHECKS = [
    'keyboard_navigation', 'screen_readers', 'contrast', 'captions',
    'alternative_text', 'responsive_design',
]

AI_GOVERNANCE_RULES = [
    'respect_permissions', 'protect_confidential_info', 'cite_institutional_knowledge',
    'identify_uncertainty', 'responsible_conversation_history',
    'no_speculation_as_verified_fact',
]

MC_SECURITY_DASHBOARD_METRICS = [
    'authentication_activity', 'permission_changes', 'audit_events', 'backup_status',
    'integration_security', 'system_health', 'security_alerts', 'executive_trust_indicators',
]

INCIDENT_RESPONSE_PROCEDURES = [
    'security_incidents', 'privacy_incidents', 'data_corruption',
    'unauthorized_access', 'system_outages', 'user_communication', 'post_incident_review',
]

INSTITUTIONAL_ETHICS_STANDARDS = [
    'accuracy', 'transparency', 'respectful_communication', 'evidence_based_education',
    'responsible_ai_use', 'volunteer_information_protection', 'public_accountability',
]

OCTOBER_TRUST_READINESS = [
    'security_standards', 'privacy_standards', 'volunteer_protections',
    'identity_controls', 'document_governance', 'communication_policies',
]

SECURITY_TRUST_SYSTEM_CHAIN = [
    'mission_control', 'knowledge_platform', 'research_institute',
    'community_education_academy', 'volunteer_network', 'coalition_network',
    'county_operating_system', 'city_operating_system', 'neighborhood_operating_system',
    'communications', 'document_management', 'ai_localbrains', 'integration_platform',
]

SECURITY_TRUST_MANIFEST = {
    'version': '1.0',
    'build': 101,
    'package': 'IMP-25',
    'updated': today,
    'title': 'Master Security, Privacy, Compliance & Institutional Trust Framework',
    'constitution': '/docs/IMPLEMENTATION_PACKAGE_25_SECURITY_TRUST.md',
    'source_registries': {
        'trust_framework': '/data/trust-framework.json',
        'identity_auth': '/data/identity-auth-manifest.json',
        'public_trust': '/data/public-trust-institutional-credibility.json',
        'integration_platform': '/data/integration-platform-manifest.json',
        'digital_library': '/data/digital-library-manifest.json',
    },
    'philosophy': 'Trust is the institution\'s most valuable asset — security is an institutional responsibility',
    'governing_principle': (
        'Trust is not claimed; it is earned through consistent actions that protect '
        'credibility and the Arkansans who participate'
    ),
    'master_timeline': MASTER_TIMELINE,
    'software_completion_date': software_completion_date,
    'county_milestone_date': county_milestone_date,
    'organizational_readiness_date': organizational_readiness_date,
    'days_to_software': days_to_software,
    'days_to_county_milestone': days_to_county_milestone,
    'days_to_organizational': days_to_organizational,
    'trust_philosophy_values': TRUST_PHILOSOPHY_VALUES,
    'security_principles': SECURITY_PRINCIPLES,
    'security_principle_count': len(SECURITY_PRINCIPLES),
    'identity_protection_features': IDENTITY_PROTECTION_FEATURES,
    'privacy_controls': PRIVACY_CONTROLS,
    'data_classification_levels': DATA_CLASSIFICATION_LEVELS,
    'data_classification_count': len(DATA_CLASSIFICATION_LEVELS),
    'data_governance_fields': DATA_GOVERNANCE_FIELDS,
    'audit_log_events': AUDIT_LOG_EVENTS,
    'backup_strategy_components': BACKUP_STRATEGY_COMPONENTS,
    'disaster_recovery_scenarios': DISASTER_RECOVERY_SCENARIOS,
    'compliance_framework_areas': COMPLIANCE_FRAMEWORK_AREAS,
    'accessibility_compliance_checks': ACCESSIBILITY_COMPLIANCE_CHECKS,
    'ai_governance_rules': AI_GOVERNANCE_RULES,
    'mc_security_dashboard_metrics': MC_SECURITY_DASHBOARD_METRICS,
    'incident_response_procedures': INCIDENT_RESPONSE_PROCEDURES,
    'institutional_ethics_standards': INSTITUTIONAL_ETHICS_STANDARDS,
    'october_trust_readiness': {
        'target_date': county_milestone_date,
        'requirements': OCTOBER_TRUST_READINESS,
        'label': 'Consistent trust framework in every county',
    },
    'organizational_goals': {
        'counties_total': 75,
        'target_cities': target_cities,
        'engagement_goal_pct': engagement_goal_pct,
        'arkansans_connected_goal': arkansans_connected_goal,
    },
    'security_trust_system_chain': SECURITY_TRUST_SYSTEM_CHAIN,
    'institutional_systems': INSTITUTIONAL_OS_SYSTEMS,
    'mc_dashboard': '/mission-control/trust.html',
    'halfway_milestone': True,
    'packages_completed': 25,
    'packages_total': 50,
    'packages_complete_pct': 50,
    'engineering_note': 'Doctrinal IMP-25 Security & Trust; engineering IMP-25 is Netlify Forms ingestion adapter',
    'status': 'documented',
    'implemented': False,
}

QUALITY_PHILOSOPHY_VALUES = [
    'designed_correctly', 'built_correctly', 'tested_thoroughly',
    'reviewed_independently', 'measured_objectively', 'improved_continuously',
]

TECHNICAL_TESTING_LAYERS = [
    'unit_testing', 'integration_testing', 'api_testing', 'database_validation',
    'security_testing', 'performance_testing', 'mobile_testing', 'offline_testing',
]

UX_TESTING_LAYERS = [
    'navigation', 'accessibility', 'search', 'learning_pathways',
    'volunteer_onboarding', 'community_workflows', 'organization_workspaces',
    'mobile_usability',
]

OPERATIONAL_TESTING_LAYERS = [
    'mission_control', 'county_workflows', 'city_workflows', 'neighborhood_workflows',
    'volunteer_operations', 'academy_operations', 'research_publication',
    'coalition_operations',
]

INSTITUTIONAL_TESTING_LAYERS = [
    'leadership_readiness', 'education_leader_readiness', 'county_readiness',
    'organization_readiness', 'community_engagement', 'communication_systems',
    'executive_reporting', 'statewide_coordination',
]

LAUNCH_CERTIFICATION_MODULES = [
    'mission_control', 'research_institute', 'knowledge_platform',
    'community_education_academy', 'volunteer_network', 'coalition_network',
    'county_operating_system', 'city_operating_system', 'neighborhood_operating_system',
    'communication_platform', 'analytics_engine', 'ai_localbrains',
]

COUNTY_READINESS_CRITERIA = [
    'county_dashboard_operational', 'county_profile_complete',
    'education_leader_identified_or_training', 'volunteer_pipeline_active',
    'community_calendar_established', 'community_conversations_scheduled',
    'county_academy_operational', 'mission_control_reporting_active',
    'research_resources_available', 'active_organizational_partner_participating',
]

ORGANIZATIONAL_PARTNER_TYPES = [
    'libraries', 'historical_societies', 'community_colleges', 'universities',
    'civic_organizations', 'neighborhood_associations', 'educational_nonprofits',
    'youth_organizations', 'community_service_organizations',
    'faith_based_civic_education', 'local_nonprofit_organizations',
]

PARTNERSHIP_MONITORING_METRICS = [
    'partnership_status', 'partnership_activity', 'shared_events',
    'shared_educational_resources', 'joint_community_conversations',
    'partner_onboarding_progress',
]

EDUCATION_LEADER_CERTIFICATION_CRITERIA = [
    'academy_completion', 'presentation_capability', 'research_literacy',
    'facilitation_skills', 'community_engagement', 'ethics_training',
    'platform_proficiency',
]

VOLUNTEER_CERTIFICATION_TRACKS = [
    'research', 'community_conversations', 'event_support', 'technology',
    'communications', 'volunteer_mentoring', 'leadership_preparation',
]

AI_VALIDATION_CRITERIA = [
    'accuracy', 'permission_enforcement', 'evidence_citation', 'consistency',
    'hallucination_resistance', 'user_experience', 'institutional_alignment',
]

PERFORMANCE_CERTIFICATION_CHECKS = [
    'fast_page_loads', 'search_responsiveness', 'mobile_responsiveness',
    'dashboard_performance', 'large_scale_data_handling', 'system_stability',
]

SECURITY_VALIDATION_CHECKS = [
    'authentication', 'authorization', 'encryption', 'audit_logging',
    'backup_validation', 'recovery_testing', 'permission_testing',
]

OPERATIONAL_SIMULATIONS = [
    'statewide_volunteer_onboarding', 'research_publication',
    'community_conversations', 'county_growth', 'organization_onboarding',
    'executive_reporting', 'emergency_communications',
]

MC_READINESS_DASHBOARD_METRICS = [
    'software_readiness', 'county_readiness', 'organization_partnership_readiness',
    'education_leader_readiness', 'volunteer_readiness', 'academy_readiness',
    'research_readiness', 'technology_readiness', 'launch_readiness',
]

STATEWIDE_LAUNCH_CHECKLIST = [
    'software_certified', '75_counties_operational',
    '75_counties_with_organizational_partnerships', 'education_leaders_active',
    'volunteer_system_operational', 'academy_operational',
    'mission_control_operational', 'security_certified', 'accessibility_certified',
    'knowledge_platform_populated', 'executive_approval_completed',
]

QA_LAUNCH_SYSTEM_CHAIN = [
    'mission_control', 'knowledge_platform', 'research_institute',
    'community_education_academy', 'volunteer_network', 'coalition_network',
    'county_operating_system', 'city_operating_system', 'neighborhood_operating_system',
    'communications', 'ai_localbrains', 'integration_platform', 'security_framework',
]

QA_LAUNCH_READINESS_MANIFEST = {
    'version': '1.0',
    'build': 101,
    'package': 'IMP-26',
    'updated': today,
    'title': 'Master Testing, Quality Assurance, Certification & Launch Readiness Framework',
    'constitution': '/docs/IMPLEMENTATION_PACKAGE_26_QA_LAUNCH_READINESS.md',
    'source_registries': {
        'launch_certification': '/data/institutional-launch-certification.json',
        'security_trust': '/data/security-trust-manifest.json',
        'integration_platform': '/data/integration-platform-manifest.json',
        'coalition_network': '/data/coalition-network-manifest.json',
        'local_operating_systems': '/data/local-operating-systems-manifest.json',
    },
    'philosophy': 'Building an institution that consistently delivers quality — not merely building software',
    'governing_principle': (
        'A successful launch is measured by functioning communities — technology, volunteers, '
        'Education Leaders, organizational partners, research, and local infrastructure together'
    ),
    'master_timeline': MASTER_TIMELINE,
    'software_completion_date': software_completion_date,
    'county_milestone_date': county_milestone_date,
    'organizational_readiness_date': organizational_readiness_date,
    'days_to_software': days_to_software,
    'days_to_county_milestone': days_to_county_milestone,
    'days_to_organizational': days_to_organizational,
    'quality_philosophy_values': QUALITY_PHILOSOPHY_VALUES,
    'testing_pyramid': {
        'technical': TECHNICAL_TESTING_LAYERS,
        'user_experience': UX_TESTING_LAYERS,
        'operational': OPERATIONAL_TESTING_LAYERS,
        'institutional': INSTITUTIONAL_TESTING_LAYERS,
    },
    'technical_testing_count': len(TECHNICAL_TESTING_LAYERS),
    'ux_testing_count': len(UX_TESTING_LAYERS),
    'operational_testing_count': len(OPERATIONAL_TESTING_LAYERS),
    'institutional_testing_count': len(INSTITUTIONAL_TESTING_LAYERS),
    'launch_certification_modules': LAUNCH_CERTIFICATION_MODULES,
    'launch_certification_module_count': len(LAUNCH_CERTIFICATION_MODULES),
    'county_readiness_criteria': COUNTY_READINESS_CRITERIA,
    'county_readiness_criteria_count': len(COUNTY_READINESS_CRITERIA),
    'organizational_partnership_certification': {
        'target_date': county_milestone_date,
        'counties_total': 75,
        'requirement': 'At least one active organizational partner per county',
        'partner_types': ORGANIZATIONAL_PARTNER_TYPES,
        'monitoring_metrics': PARTNERSHIP_MONITORING_METRICS,
        'label': '75 counties with organizational partnerships by October 1',
        'priority': 'highest_operational',
    },
    'education_leader_certification_criteria': EDUCATION_LEADER_CERTIFICATION_CRITERIA,
    'education_leader_certification_count': len(EDUCATION_LEADER_CERTIFICATION_CRITERIA),
    'volunteer_certification_tracks': VOLUNTEER_CERTIFICATION_TRACKS,
    'volunteer_certification_track_count': len(VOLUNTEER_CERTIFICATION_TRACKS),
    'accessibility_certification_tracks': [
        'accessibility_issues', 'review_completion', 'compliance_progress',
        'outstanding_improvements',
    ],
    'ai_validation_criteria': AI_VALIDATION_CRITERIA,
    'ai_validation_criteria_count': len(AI_VALIDATION_CRITERIA),
    'performance_certification_checks': PERFORMANCE_CERTIFICATION_CHECKS,
    'performance_certification_check_count': len(PERFORMANCE_CERTIFICATION_CHECKS),
    'security_validation_checks': SECURITY_VALIDATION_CHECKS,
    'security_validation_check_count': len(SECURITY_VALIDATION_CHECKS),
    'operational_simulations': OPERATIONAL_SIMULATIONS,
    'operational_simulation_count': len(OPERATIONAL_SIMULATIONS),
    'mc_readiness_dashboard_metrics': MC_READINESS_DASHBOARD_METRICS,
    'mc_readiness_dashboard_metric_count': len(MC_READINESS_DASHBOARD_METRICS),
    'statewide_launch_checklist': STATEWIDE_LAUNCH_CHECKLIST,
    'statewide_launch_checklist_count': len(STATEWIDE_LAUNCH_CHECKLIST),
    'organizational_goals': {
        'counties_total': 75,
        'counties_with_partnerships_goal': 75,
        'target_cities': target_cities,
        'engagement_goal_pct': engagement_goal_pct,
        'arkansans_connected_goal': arkansans_connected_goal,
    },
    'qa_launch_system_chain': QA_LAUNCH_SYSTEM_CHAIN,
    'institutional_systems': INSTITUTIONAL_OS_SYSTEMS,
    'mc_dashboard': '/mission-control/institutional-launch-certification.html',
    'packages_completed': 26,
    'packages_total': 50,
    'packages_complete_pct': 52,
    'engineering_note': 'Doctrinal IMP-26 QA & Launch Readiness; engineering IMP-26 is Auth provider and admin login shell',
    'status': 'documented',
    'implemented': False,
}

INFRASTRUCTURE_PHILOSOPHY_VALUES = [
    'reliability', 'security', 'observability', 'scalability', 'recoverability',
    'simplicity', 'cost_effectiveness', 'mission_continuity',
]

ENVIRONMENT_ARCHITECTURE = [
    'development', 'testing', 'staging', 'production',
]

DEPLOYMENT_PIPELINE_STEPS = [
    'development', 'automated_testing', 'quality_verification', 'security_review',
    'staging_deployment', 'operational_validation', 'production_approval',
    'production_deployment', 'mission_control_verification',
]

INFRASTRUCTURE_COMPONENTS = [
    'web_application', 'api_services', 'database', 'document_storage',
    'media_storage', 'search_engine', 'ai_gateway', 'background_workers',
    'notification_services', 'monitoring', 'logging', 'backup_systems',
]

DATABASE_OPERATIONS_STANDARDS = [
    'automated_backups', 'migration_management', 'performance_monitoring',
    'index_optimization', 'recovery_procedures', 'integrity_validation',
]

MONITORING_PLATFORM_METRICS = [
    'application_uptime', 'response_times', 'api_performance', 'database_health',
    'storage_utilization', 'background_jobs', 'ai_services', 'integration_health',
    'errors', 'user_activity',
]

LOGGING_EVENT_TYPES = [
    'authentication', 'workflow_execution', 'research_publication',
    'volunteer_onboarding', 'system_errors', 'security_events',
    'integration_failures',
]

SCALING_STRATEGIES = [
    'additional_web_servers', 'database_optimization', 'caching',
    'background_processing', 'media_delivery', 'search_indexing',
    'ai_request_balancing',
]

PRODUCTION_ALERT_TYPES = [
    'system_outages', 'performance_degradation', 'security_incidents',
    'failed_backups', 'integration_failures', 'storage_thresholds',
    'critical_workflow_failures',
]

RELEASE_MANAGEMENT_FIELDS = [
    'version_number', 'release_notes', 'deployment_date',
    'validation_results', 'rollback_plan', 'known_issues',
]

ROLLBACK_STRATEGY_CAPABILITIES = [
    'rapid_rollback', 'database_compatibility', 'configuration_restoration',
    'version_history', 'operational_verification',
]

INFRASTRUCTURE_DOCUMENTATION_FIELDS = [
    'purpose', 'dependencies', 'configuration', 'monitoring',
    'recovery_procedures', 'responsible_owners',
]

BUSINESS_CONTINUITY_CAPABILITIES = [
    'automated_backups', 'redundant_storage', 'disaster_recovery',
    'operational_documentation', 'mission_control_continuity',
    'knowledge_preservation', 'communication_procedures',
]

PRODUCTION_SECURITY_CONTROLS = [
    'encrypted_communications', 'secret_management', 'role_based_administration',
    'infrastructure_audit_logs', 'regular_updates', 'continuous_monitoring',
    'security_reviews',
]

OPERATIONAL_METRICS = [
    'availability', 'performance', 'deployment_frequency', 'recovery_time',
    'error_rates', 'infrastructure_cost', 'growth_capacity', 'operational_readiness',
]

OCTOBER_PRODUCTION_READINESS_SCOPE = [
    '75_county_operating_systems', 'organization_portals',
    'community_education_academy', 'volunteer_network', 'mission_control',
    'knowledge_platform', 'community_conversations', 'public_website',
]

DEVOPS_PRODUCTION_SYSTEM_CHAIN = [
    'mission_control', 'knowledge_platform', 'research_institute',
    'community_education_academy', 'volunteer_network', 'coalition_network',
    'county_operating_system', 'city_operating_system', 'neighborhood_operating_system',
    'communications', 'ai_localbrains', 'integration_platform', 'security_framework',
]

DEVOPS_PRODUCTION_MANIFEST = {
    'version': '1.0',
    'build': 101,
    'package': 'IMP-27',
    'updated': today,
    'title': 'Master Deployment, Infrastructure, DevOps & Production Operations',
    'constitution': '/docs/IMPLEMENTATION_PACKAGE_27_DEVOPS_PRODUCTION.md',
    'source_registries': {
        'technical_architecture': '/data/technical-architecture.json',
        'qa_launch_readiness': '/data/qa-launch-readiness-manifest.json',
        'security_trust': '/data/security-trust-manifest.json',
        'integration_platform': '/data/integration-platform-manifest.json',
        'repository_blueprint': '/data/repository-blueprint.json',
    },
    'philosophy': 'Infrastructure should be invisible — volunteers never think about servers, databases, or scaling',
    'governing_principle': (
        'Technology should never become the institution; it quietly supports people '
        'educating communities and serving Arkansas'
    ),
    'master_timeline': MASTER_TIMELINE,
    'software_completion_date': software_completion_date,
    'county_milestone_date': county_milestone_date,
    'organizational_readiness_date': organizational_readiness_date,
    'days_to_software': days_to_software,
    'days_to_county_milestone': days_to_county_milestone,
    'days_to_organizational': days_to_organizational,
    'infrastructure_philosophy_values': INFRASTRUCTURE_PHILOSOPHY_VALUES,
    'environment_architecture': ENVIRONMENT_ARCHITECTURE,
    'environment_count': len(ENVIRONMENT_ARCHITECTURE),
    'deployment_pipeline_steps': DEPLOYMENT_PIPELINE_STEPS,
    'deployment_pipeline_step_count': len(DEPLOYMENT_PIPELINE_STEPS),
    'infrastructure_components': INFRASTRUCTURE_COMPONENTS,
    'infrastructure_component_count': len(INFRASTRUCTURE_COMPONENTS),
    'database_operations_standards': DATABASE_OPERATIONS_STANDARDS,
    'database_operations_standard_count': len(DATABASE_OPERATIONS_STANDARDS),
    'monitoring_platform_metrics': MONITORING_PLATFORM_METRICS,
    'monitoring_platform_metric_count': len(MONITORING_PLATFORM_METRICS),
    'logging_event_types': LOGGING_EVENT_TYPES,
    'logging_event_type_count': len(LOGGING_EVENT_TYPES),
    'scaling_strategies': SCALING_STRATEGIES,
    'scaling_strategy_count': len(SCALING_STRATEGIES),
    'production_alert_types': PRODUCTION_ALERT_TYPES,
    'production_alert_type_count': len(PRODUCTION_ALERT_TYPES),
    'release_management_fields': RELEASE_MANAGEMENT_FIELDS,
    'release_management_field_count': len(RELEASE_MANAGEMENT_FIELDS),
    'rollback_strategy_capabilities': ROLLBACK_STRATEGY_CAPABILITIES,
    'rollback_strategy_capability_count': len(ROLLBACK_STRATEGY_CAPABILITIES),
    'infrastructure_documentation_fields': INFRASTRUCTURE_DOCUMENTATION_FIELDS,
    'infrastructure_documentation_field_count': len(INFRASTRUCTURE_DOCUMENTATION_FIELDS),
    'business_continuity_capabilities': BUSINESS_CONTINUITY_CAPABILITIES,
    'business_continuity_capability_count': len(BUSINESS_CONTINUITY_CAPABILITIES),
    'production_security_controls': PRODUCTION_SECURITY_CONTROLS,
    'production_security_control_count': len(PRODUCTION_SECURITY_CONTROLS),
    'operational_metrics': OPERATIONAL_METRICS,
    'operational_metric_count': len(OPERATIONAL_METRICS),
    'october_production_readiness': {
        'target_date': county_milestone_date,
        'scope': OCTOBER_PRODUCTION_READINESS_SCOPE,
        'label': 'Production infrastructure supports statewide growth by October 1',
    },
    'organizational_goals': {
        'counties_total': 75,
        'counties_with_partnerships_goal': 75,
        'target_cities': target_cities,
        'engagement_goal_pct': engagement_goal_pct,
        'arkansans_connected_goal': arkansans_connected_goal,
    },
    'devops_production_system_chain': DEVOPS_PRODUCTION_SYSTEM_CHAIN,
    'institutional_systems': INSTITUTIONAL_OS_SYSTEMS,
    'mc_dashboard': '/mission-control/platform.html',
    'packages_completed': 27,
    'packages_total': 50,
    'packages_complete_pct': 54,
    'engineering_note': 'Doctrinal IMP-27 DevOps & Production Ops; engineering IMP-27 is Role model definition',
    'status': 'documented',
    'implemented': False,
}

GOVERNANCE_PHILOSOPHY_VALUES = [
    'clearly_defined', 'transparent', 'documented', 'delegated_appropriately',
    'accountable', 'mission_driven',
]

INSTITUTIONAL_STRUCTURE_LEVELS = [
    'executive_office', 'program_management_office', 'mission_control',
    'functional_departments', 'county_leadership', 'city_leadership',
    'neighborhood_leadership', 'community_volunteers',
]

EXECUTIVE_OFFICE_RESPONSIBILITIES = [
    'mission_stewardship', 'strategic_planning', 'institutional_partnerships',
    'long_term_priorities', 'major_policy_decisions', 'executive_communications',
    'annual_planning',
]

PMO_RESPONSIBILITIES = [
    'project_portfolio_management', 'milestone_tracking', 'risk_management',
    'cross_department_coordination', 'dependency_management', 'resource_planning',
    'operational_reporting',
]

MC_GOVERNANCE_CAPABILITIES = [
    'dashboards', 'forecasts', 'performance_metrics', 'alerts',
    'recommendations', 'operational_visibility',
]

DECISION_FRAMEWORK_STEPS = [
    'issue_identified', 'evidence_collected', 'options_evaluated',
    'stakeholders_consulted', 'decision_documented', 'implementation_planned',
    'mission_control_monitoring', 'post_implementation_review',
]

DELEGATION_PRINCIPLES = [
    'neighborhood_to_neighborhood_leaders', 'city_to_city_leaders',
    'county_to_county_leadership', 'statewide_to_executive_office',
]

POLICY_MANAGEMENT_FIELDS = [
    'purpose', 'scope', 'owner', 'approval_date', 'review_schedule',
    'revision_history', 'related_procedures',
]

STRATEGIC_PLANNING_HORIZONS = [
    'daily_operations', 'weekly_coordination', 'monthly_reviews',
    'quarterly_planning', 'annual_strategic_planning', 'long_term_institutional_vision',
]

RISK_GOVERNANCE_CATEGORIES = [
    'technology', 'volunteer_capacity', 'research_backlog', 'leadership_vacancies',
    'community_engagement', 'funding', 'operational_continuity',
]

ANNUAL_OPERATING_PLAN_ELEMENTS = [
    'strategic_priorities', 'major_initiatives', 'county_objectives',
    'academy_objectives', 'volunteer_goals', 'research_goals', 'technology_roadmap',
]

GOVERNANCE_MEETING_TYPES = [
    'executive_strategy', 'pmo_review', 'mission_control_review',
    'research_leadership', 'academy_leadership', 'volunteer_leadership',
    'county_leadership', 'coalition_coordination',
]

ACCOUNTABILITY_FRAMEWORK_FIELDS = [
    'responsible_owner', 'supporting_team', 'milestones', 'success_metrics',
    'review_schedule',
]

ORGANIZATIONAL_MEMORY_FIELDS = [
    'decision', 'rationale', 'participants', 'supporting_evidence',
    'implementation_date', 'review_outcome',
]

GOVERNANCE_ETHICS_COMMITMENTS = [
    'integrity', 'transparency', 'evidence_based_decision_making',
    'respectful_collaboration', 'responsible_stewardship', 'service_to_mission',
]

OCTOBER_GOVERNANCE_OBJECTIVE_SCOPE = [
    '75_county_leadership_teams', 'county_organizational_partnerships',
    'education_leader_coordination', 'volunteer_oversight',
    'mission_control_reporting', 'operational_consistency_statewide',
]

GOVERNANCE_PMO_SYSTEM_CHAIN = [
    'mission_control', 'pmo', 'knowledge_platform', 'research_institute',
    'community_education_academy', 'volunteer_network', 'coalition_network',
    'county_operating_system', 'city_operating_system', 'neighborhood_operating_system',
    'communications', 'ai_localbrains',
]

GOVERNANCE_PMO_MANIFEST = {
    'version': '1.0',
    'build': 101,
    'package': 'IMP-28',
    'updated': today,
    'title': 'Master Governance, Executive Office, PMO & Institutional Decision Framework',
    'constitution': '/docs/IMPLEMENTATION_PACKAGE_28_GOVERNANCE_PMO.md',
    'source_registries': {
        'organizational_constitution': '/data/organizational-constitution.json',
        'devops_production': '/data/devops-production-manifest.json',
        'qa_launch_readiness': '/data/qa-launch-readiness-manifest.json',
        'mission_control_architecture': '/data/mission-control-architecture-manifest.json',
        'execution_schedule': '/data/execution-schedule.json',
    },
    'philosophy': 'Clear governance creates continuity — build an institution that outlasts its founders',
    'governing_principle': (
        'Strong institutions are defined by systems that enable many people to lead '
        'responsibly over time, accountable to mission and adaptable to change'
    ),
    'master_timeline': MASTER_TIMELINE,
    'software_completion_date': software_completion_date,
    'county_milestone_date': county_milestone_date,
    'organizational_readiness_date': organizational_readiness_date,
    'days_to_software': days_to_software,
    'days_to_county_milestone': days_to_county_milestone,
    'days_to_organizational': days_to_organizational,
    'governance_philosophy_values': GOVERNANCE_PHILOSOPHY_VALUES,
    'institutional_structure_levels': INSTITUTIONAL_STRUCTURE_LEVELS,
    'institutional_structure_level_count': len(INSTITUTIONAL_STRUCTURE_LEVELS),
    'executive_office_responsibilities': EXECUTIVE_OFFICE_RESPONSIBILITIES,
    'executive_office_responsibility_count': len(EXECUTIVE_OFFICE_RESPONSIBILITIES),
    'pmo_responsibilities': PMO_RESPONSIBILITIES,
    'pmo_responsibility_count': len(PMO_RESPONSIBILITIES),
    'mc_governance_capabilities': MC_GOVERNANCE_CAPABILITIES,
    'mc_governance_capability_count': len(MC_GOVERNANCE_CAPABILITIES),
    'decision_framework_steps': DECISION_FRAMEWORK_STEPS,
    'decision_framework_step_count': len(DECISION_FRAMEWORK_STEPS),
    'delegation_principles': DELEGATION_PRINCIPLES,
    'policy_management_fields': POLICY_MANAGEMENT_FIELDS,
    'policy_management_field_count': len(POLICY_MANAGEMENT_FIELDS),
    'strategic_planning_horizons': STRATEGIC_PLANNING_HORIZONS,
    'strategic_planning_horizon_count': len(STRATEGIC_PLANNING_HORIZONS),
    'risk_governance_categories': RISK_GOVERNANCE_CATEGORIES,
    'risk_governance_category_count': len(RISK_GOVERNANCE_CATEGORIES),
    'annual_operating_plan_elements': ANNUAL_OPERATING_PLAN_ELEMENTS,
    'annual_operating_plan_element_count': len(ANNUAL_OPERATING_PLAN_ELEMENTS),
    'governance_meeting_types': GOVERNANCE_MEETING_TYPES,
    'governance_meeting_type_count': len(GOVERNANCE_MEETING_TYPES),
    'accountability_framework_fields': ACCOUNTABILITY_FRAMEWORK_FIELDS,
    'accountability_framework_field_count': len(ACCOUNTABILITY_FRAMEWORK_FIELDS),
    'organizational_memory_fields': ORGANIZATIONAL_MEMORY_FIELDS,
    'organizational_memory_field_count': len(ORGANIZATIONAL_MEMORY_FIELDS),
    'governance_ethics_commitments': GOVERNANCE_ETHICS_COMMITMENTS,
    'governance_ethics_commitment_count': len(GOVERNANCE_ETHICS_COMMITMENTS),
    'october_governance_objective': {
        'target_date': county_milestone_date,
        'scope': OCTOBER_GOVERNANCE_OBJECTIVE_SCOPE,
        'label': 'Consistent governance framework in every county by October 1',
    },
    'organizational_goals': {
        'counties_total': 75,
        'counties_with_partnerships_goal': 75,
        'target_cities': target_cities,
        'engagement_goal_pct': engagement_goal_pct,
        'arkansans_connected_goal': arkansans_connected_goal,
    },
    'governance_pmo_system_chain': GOVERNANCE_PMO_SYSTEM_CHAIN,
    'institutional_systems': INSTITUTIONAL_OS_SYSTEMS,
    'mc_dashboard': '/mission-control/governance.html',
    'packages_completed': 28,
    'packages_total': 50,
    'packages_complete_pct': 56,
    'engineering_note': 'Doctrinal IMP-28 Governance & PMO; engineering IMP-28 is Permission middleware',
    'status': 'documented',
    'implemented': False,
}

SUSTAINABILITY_PHILOSOPHY_PRESERVES = [
    'knowledge', 'processes', 'relationships', 'culture', 'standards',
    'institutional_memory',
]

CONTINUITY_PILLARS = [
    'knowledge', 'people', 'processes', 'technology', 'mission',
]

LEADERSHIP_CONTINUITY_FIELDS = [
    'documented_responsibilities', 'operating_manuals', 'decision_history',
    'successor_recommendations', 'current_priorities', 'open_initiatives',
    'relationship_summaries',
]

SUCCESSION_PLANNING_TRACKING = [
    'critical_leadership_roles', 'potential_future_leaders', 'leadership_readiness',
    'mentorship_progress', 'vacant_positions', 'emerging_leadership_opportunities',
]

KNOWLEDGE_TRANSFER_DELIVERABLES = [
    'lessons_learned', 'best_practices', 'challenges_encountered', 'recommendations',
    'supporting_documents', 'reusable_templates',
]

INSTITUTIONAL_PLAYBOOKS = [
    'research', 'academy', 'volunteer_management', 'community_conversations',
    'coalition_partnerships', 'county_operations', 'technology', 'mission_control',
    'communications',
]

DOCUMENTATION_STANDARD_FIELDS = [
    'purpose', 'responsibilities', 'processes', 'frequently_asked_questions',
    'troubleshooting', 'reference_materials', 'training_resources',
]

VOLUNTEER_DEVELOPMENT_PATHS = [
    'learning', 'leadership', 'mentorship', 'specialization', 'cross_training',
    'institutional_stewardship',
]

ORGANIZATIONAL_LEARNING_OUTPUTS = [
    'best_practices', 'case_studies', 'templates', 'checklists',
    'training_materials', 'improved_workflows',
]

INSTITUTIONAL_MEMORY_PRESERVES = [
    'major_decisions', 'research', 'community_conversations', 'meeting_summaries',
    'project_history', 'leadership_transitions', 'annual_reports',
    'institutional_milestones',
]

LONG_TERM_GROWTH_STRATEGIES = [
    'additional_education_leaders', 'new_organizational_partnerships',
    'expanded_academy_curriculum', 'greater_county_engagement',
    'more_community_conversations', 'improved_volunteer_development',
    'technology_enhancements',
]

EXPANSION_BEYOND_ARKANSAS_PRINCIPLES = [
    'reusable_operating_systems', 'configurable_geography', 'reusable_academy',
    'reusable_mission_control', 'reusable_localbrains',
]

MISSION_PRESERVATION_QUESTIONS = [
    'strengthen_civic_education', 'strengthen_public_trust',
    'strengthen_communities', 'align_with_institutional_mission',
]

OCTOBER_SUSTAINABILITY_OBJECTIVE_SCOPE = [
    'documented_operating_procedures', 'shared_educational_resources',
    'county_knowledge_repository', 'volunteer_onboarding_materials',
    'leadership_continuity_planning',
]

MC_SUSTAINABILITY_DASHBOARD_METRICS = [
    'leadership_readiness', 'succession_planning', 'documentation_completeness',
    'knowledge_growth', 'volunteer_development', 'cross_training',
    'county_sustainability', 'organizational_maturity',
]

SUSTAINABILITY_CONTINUITY_SYSTEM_CHAIN = [
    'mission_control', 'knowledge_platform', 'research_institute',
    'community_education_academy', 'volunteer_network', 'coalition_network',
    'county_operating_system', 'city_operating_system', 'neighborhood_operating_system',
    'communications', 'governance', 'ai_localbrains',
]

SUSTAINABILITY_CONTINUITY_MANIFEST = {
    'version': '1.0',
    'build': 101,
    'package': 'IMP-29',
    'updated': today,
    'title': 'Master Sustainability, Growth Strategy, Knowledge Transfer & Institutional Continuity',
    'constitution': '/docs/IMPLEMENTATION_PACKAGE_29_SUSTAINABILITY_CONTINUITY.md',
    'source_registries': {
        'governance_pmo': '/data/governance-pmo-manifest.json',
        'digital_library': '/data/digital-library-manifest.json',
        'knowledge_graph': '/data/knowledge-graph-manifest.json',
        'volunteer_network': '/data/volunteer-network-manifest.json',
        'local_operating_systems': '/data/local-operating-systems-manifest.json',
    },
    'philosophy': 'Institutional continuity is deliberate — success must never depend on one individual',
    'governing_principle': (
        'Every generation of volunteers leaves behind a stronger, wiser institution — '
        'the mission remains while people, leaders, and technology change'
    ),
    'master_timeline': MASTER_TIMELINE,
    'software_completion_date': software_completion_date,
    'county_milestone_date': county_milestone_date,
    'organizational_readiness_date': organizational_readiness_date,
    'days_to_software': days_to_software,
    'days_to_county_milestone': days_to_county_milestone,
    'days_to_organizational': days_to_organizational,
    'sustainability_philosophy_preserves': SUSTAINABILITY_PHILOSOPHY_PRESERVES,
    'continuity_pillars': CONTINUITY_PILLARS,
    'continuity_pillar_count': len(CONTINUITY_PILLARS),
    'leadership_continuity_fields': LEADERSHIP_CONTINUITY_FIELDS,
    'leadership_continuity_field_count': len(LEADERSHIP_CONTINUITY_FIELDS),
    'succession_planning_tracking': SUCCESSION_PLANNING_TRACKING,
    'succession_planning_tracking_count': len(SUCCESSION_PLANNING_TRACKING),
    'knowledge_transfer_deliverables': KNOWLEDGE_TRANSFER_DELIVERABLES,
    'knowledge_transfer_deliverable_count': len(KNOWLEDGE_TRANSFER_DELIVERABLES),
    'institutional_playbooks': INSTITUTIONAL_PLAYBOOKS,
    'institutional_playbook_count': len(INSTITUTIONAL_PLAYBOOKS),
    'documentation_standard_fields': DOCUMENTATION_STANDARD_FIELDS,
    'documentation_standard_field_count': len(DOCUMENTATION_STANDARD_FIELDS),
    'volunteer_development_paths': VOLUNTEER_DEVELOPMENT_PATHS,
    'volunteer_development_path_count': len(VOLUNTEER_DEVELOPMENT_PATHS),
    'organizational_learning_outputs': ORGANIZATIONAL_LEARNING_OUTPUTS,
    'organizational_learning_output_count': len(ORGANIZATIONAL_LEARNING_OUTPUTS),
    'institutional_memory_preserves': INSTITUTIONAL_MEMORY_PRESERVES,
    'institutional_memory_preserve_count': len(INSTITUTIONAL_MEMORY_PRESERVES),
    'long_term_growth_strategies': LONG_TERM_GROWTH_STRATEGIES,
    'long_term_growth_strategy_count': len(LONG_TERM_GROWTH_STRATEGIES),
    'expansion_beyond_arkansas_principles': EXPANSION_BEYOND_ARKANSAS_PRINCIPLES,
    'expansion_principle_count': len(EXPANSION_BEYOND_ARKANSAS_PRINCIPLES),
    'mission_preservation_questions': MISSION_PRESERVATION_QUESTIONS,
    'mission_preservation_question_count': len(MISSION_PRESERVATION_QUESTIONS),
    'october_sustainability_objective': {
        'target_date': county_milestone_date,
        'scope': OCTOBER_SUSTAINABILITY_OBJECTIVE_SCOPE,
        'label': 'County-level resilience — procedures, resources, knowledge, onboarding, continuity',
    },
    'mc_sustainability_dashboard_metrics': MC_SUSTAINABILITY_DASHBOARD_METRICS,
    'mc_sustainability_dashboard_metric_count': len(MC_SUSTAINABILITY_DASHBOARD_METRICS),
    'organizational_goals': {
        'counties_total': 75,
        'counties_with_partnerships_goal': 75,
        'target_cities': target_cities,
        'engagement_goal_pct': engagement_goal_pct,
        'arkansans_connected_goal': arkansans_connected_goal,
    },
    'sustainability_continuity_system_chain': SUSTAINABILITY_CONTINUITY_SYSTEM_CHAIN,
    'institutional_systems': INSTITUTIONAL_OS_SYSTEMS,
    'mc_dashboard': '/mission-control/sustainability-stewardship.html',
    'packages_completed': 29,
    'packages_total': 50,
    'packages_complete_pct': 58,
    'engineering_note': 'Doctrinal IMP-29 Sustainability & Continuity; engineering IMP-29 is Volunteer signup flow',
    'status': 'documented',
    'implemented': False,
}

TIME_INTELLIGENCE_MANIFEST = {
    'version': '1.0',
    'build': 101,
    'package': 'IMP-17',
    'updated': today,
    'title': 'Master Calendar, Scheduling, Event Management & Time Intelligence System',
    'constitution': '/docs/IMPLEMENTATION_PACKAGE_17_TIME_INTELLIGENCE.md',
    'source_registries': {
        'execution_schedule': '/data/execution-schedule.json',
        'coalition_events': '/data/coalition-events.json',
        'communication_platform': '/data/communication-platform-manifest.json',
        'local_operating_systems': '/data/local-operating-systems-manifest.json',
        'localbrain_network': '/data/localbrain-network-manifest.json',
    },
    'philosophy': 'Every LocalBrain owns its calendar; Mission Control understands them all',
    'governing_principle': (
        'Institutions run on people; people live by calendars; '
        'Citizens United Facts always knows what matters next'
    ),
    'master_timeline': MASTER_TIMELINE,
    'software_completion_date': software_completion_date,
    'county_milestone_date': county_milestone_date,
    'organizational_readiness_date': organizational_readiness_date,
    'days_to_software': days_to_software,
    'days_to_county_milestone': days_to_county_milestone,
    'days_to_organizational': days_to_organizational,
    'time_philosophy_requirements': TIME_PHILOSOPHY_REQUIREMENTS,
    'personal_calendar_features': PERSONAL_CALENDAR_FEATURES,
    'localbrain_calendars': LOCALBRAIN_CALENDARS,
    'localbrain_calendar_count': len(LOCALBRAIN_CALENDARS),
    'county_calendar_events': COUNTY_CALENDAR_EVENTS,
    'city_calendar_events': CITY_CALENDAR_EVENTS,
    'neighborhood_calendar_events': NEIGHBORHOOD_CALENDAR_EVENTS,
    'academy_calendar_events': ACADEMY_CALENDAR_EVENTS,
    'project_calendar_fields': PROJECT_CALENDAR_FIELDS,
    'executive_calendar_items': EXECUTIVE_CALENDAR_ITEMS,
    'event_management_fields': EVENT_MANAGEMENT_FIELDS,
    'recurring_event_types': RECURRING_EVENT_TYPES,
    'scheduling_intelligence': SCHEDULING_INTELLIGENCE_CAPABILITIES,
    'external_calendar_sync': EXTERNAL_CALENDAR_SYNC,
    'personal_ai_scheduler': PERSONAL_AI_SCHEDULER_EXAMPLES,
    'executive_ai_scheduler': EXECUTIVE_AI_SCHEDULER_CAPABILITIES,
    'time_analytics_metrics': TIME_ANALYTICS_METRICS,
    'travel_coordination': TRAVEL_COORDINATION_FEATURES,
    'october_coordination': {
        'target_date': county_milestone_date,
        'monitored_activities': OCTOBER_TIME_COORDINATION,
    },
    'organizational_goals': {
        'counties_total': 75,
        'target_cities': target_cities,
        'engagement_goal_pct': engagement_goal_pct,
        'arkansans_connected_goal': arkansans_connected_goal,
    },
    'time_system_chain': TIME_SYSTEM_CHAIN,
    'institutional_systems': INSTITUTIONAL_OS_SYSTEMS,
    'packages_completed': 17,
    'packages_total': 50,
    'packages_complete_pct': 34,
    'engineering_note': 'Doctrinal IMP-17 Time Intelligence; engineering IMP-17 is COMP-01–05 primitive specs',
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
    {'id': 'CIP-D11', 'indicator': 'LocalBrain Network (IMP-08)', 'current': 'Documented', 'status': 'partial'},
    {'id': 'CIP-D12', 'indicator': 'Knowledge Graph (IMP-09)', 'current': 'Documented', 'status': 'partial'},
    {'id': 'CIP-D13', 'indicator': 'Content Management (IMP-10)', 'current': 'Documented', 'status': 'partial'},
    {'id': 'CIP-D14', 'indicator': 'Research Institute (IMP-11)', 'current': 'Documented', 'status': 'partial'},
    {'id': 'CIP-D15', 'indicator': 'Education Academy (IMP-12)', 'current': 'Documented', 'status': 'partial'},
    {'id': 'CIP-D16', 'indicator': 'Volunteer Network (IMP-13)', 'current': 'Documented', 'status': 'partial'},
    {'id': 'CIP-D17', 'indicator': 'Coalition Network (IMP-14)', 'current': 'Documented', 'status': 'partial'},
    {'id': 'CIP-D18', 'indicator': 'Local Operating Systems (IMP-15)', 'current': 'Documented', 'status': 'partial'},
    {'id': 'CIP-D19', 'indicator': 'Communication Platform (IMP-16)', 'current': 'Documented', 'status': 'partial'},
    {'id': 'CIP-D20', 'indicator': 'Time Intelligence (IMP-17)', 'current': 'Documented', 'status': 'partial'},
    {'id': 'CIP-D21', 'indicator': 'Relationship Intelligence (IMP-18)', 'current': 'Documented', 'status': 'partial'},
    {'id': 'CIP-D22', 'indicator': 'Institutional Analytics (IMP-19)', 'current': 'Documented', 'status': 'partial'},
    {'id': 'CIP-D23', 'indicator': 'Automation Engine (IMP-20)', 'current': 'Documented', 'status': 'partial'},
    {'id': 'CIP-D24', 'indicator': 'Public Website (IMP-21)', 'current': 'Documented', 'status': 'partial'},
    {'id': 'CIP-D25', 'indicator': 'Mobile PWA & Field Ops (IMP-22)', 'current': 'Documented', 'status': 'partial'},
    {'id': 'CIP-D26', 'indicator': 'Digital Library (IMP-23)', 'current': 'Documented', 'status': 'partial'},
    {'id': 'CIP-D27', 'indicator': 'Integration Platform (IMP-24)', 'current': 'Documented', 'status': 'partial'},
    {'id': 'CIP-D28', 'indicator': 'Security & Trust (IMP-25)', 'current': 'Documented', 'status': 'partial'},
    {'id': 'CIP-D29', 'indicator': 'QA & Launch Readiness (IMP-26)', 'current': 'Documented', 'status': 'partial'},
    {'id': 'CIP-D30', 'indicator': 'DevOps & Production Ops (IMP-27)', 'current': 'Documented', 'status': 'partial'},
    {'id': 'CIP-D31', 'indicator': 'Governance & PMO (IMP-28)', 'current': 'Documented', 'status': 'partial'},
    {'id': 'CIP-D32', 'indicator': 'Sustainability & Continuity (IMP-29)', 'current': 'Documented', 'status': 'partial'},
    {'id': 'CIP-D33', 'indicator': 'Sprint Zero started', 'current': 'Yes' if sprint_zero_started else 'No', 'status': 'planned'},
]

implementation_package_readiness = min(
    100,
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
    'completion_target_date': organizational_readiness_date,
    'software_completion_date': software_completion_date,
    'county_milestone_date': county_milestone_date,
    'organizational_readiness_date': organizational_readiness_date,
    'days_to_software': days_to_software,
    'days_to_county_milestone': days_to_county_milestone,
    'days_to_organizational': days_to_organizational,
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
            'status': 'documented',
        },
    },
    'localbrain_network': {
        'title': 'Master LocalBrain Architecture & Institutional AI Network',
        'package': 'Implementation Package 8 of 50',
        'route': '/docs/IMPLEMENTATION_PACKAGE_08_LOCALBRAIN_ARCHITECTURE.md',
        'manifest': '/data/localbrain-network-manifest.json',
        'status': 'documented',
        'documented_date': today,
        'philosophy': LOCALBRAIN_NETWORK_MANIFEST['philosophy'],
        'localbrain_count': LOCALBRAIN_NETWORK_MANIFEST['localbrain_count'],
        'core_module_count': len(LOCALBRAIN_CORE_MODULES),
        'brain_lifecycle_stages': len(BRAIN_LIFECYCLE),
        'ai_safety_rule_count': len(AI_SAFETY_RULES),
        'modular_expansion': True,
        'next_package': {
            'number': 9,
            'id': 'IMP-09',
            'title': 'Master Knowledge Graph, Semantic Search & Institutional Memory',
            'status': 'documented',
        },
    },
    'knowledge_graph': {
        'title': 'Master Knowledge Graph, Semantic Search & Institutional Memory',
        'package': 'Implementation Package 9 of 50',
        'route': '/docs/IMPLEMENTATION_PACKAGE_09_KNOWLEDGE_GRAPH.md',
        'manifest': '/data/knowledge-graph-manifest.json',
        'status': 'documented',
        'documented_date': today,
        'philosophy': KNOWLEDGE_GRAPH_MANIFEST['philosophy'],
        'node_type_count': KNOWLEDGE_GRAPH_MANIFEST['node_type_count'],
        'relationship_count': len(RELATIONSHIP_ONTOLOGY),
        'knowledge_health_metric_count': len(KNOWLEDGE_HEALTH_METRICS),
        'software_completion_date': software_completion_date,
        'organizational_readiness_date': organizational_readiness_date,
        'days_to_software': days_to_software,
        'days_to_organizational': days_to_organizational,
        'next_package': {
            'number': 10,
            'id': 'IMP-10',
            'title': 'Master Content Management System, Research Publishing & Editorial Workflow',
            'status': 'documented',
        },
    },
    'content_management': {
        'title': 'Master Content Management System, Research Publishing & Editorial Workflow',
        'package': 'Implementation Package 10 of 50',
        'route': '/docs/IMPLEMENTATION_PACKAGE_10_CONTENT_MANAGEMENT.md',
        'manifest': '/data/content-management-manifest.json',
        'status': 'documented',
        'documented_date': today,
        'philosophy': CONTENT_MANAGEMENT_MANIFEST['philosophy'],
        'content_type_count': CONTENT_MANAGEMENT_MANIFEST['content_type_count'],
        'content_class_count': CONTENT_MANAGEMENT_MANIFEST['content_class_count'],
        'workflow_stage_count': CONTENT_MANAGEMENT_MANIFEST['workflow_stage_count'],
        'packages_completed': CONTENT_MANAGEMENT_MANIFEST['packages_completed'],
        'foundation_complete_pct': CONTENT_MANAGEMENT_MANIFEST['foundation_complete_pct'],
        'software_completion_date': software_completion_date,
        'organizational_readiness_date': organizational_readiness_date,
        'engineering_note': CONTENT_MANAGEMENT_MANIFEST['engineering_note'],
        'next_package': {
            'number': 11,
            'id': 'IMP-11',
            'title': 'Master Research Institute, Evidence Ledger & Claims Verification System',
            'status': 'documented',
        },
    },
    'research_institute': {
        'title': 'Master Research Institute, Evidence Ledger & Claims Verification System',
        'package': 'Implementation Package 11 of 50',
        'route': '/docs/IMPLEMENTATION_PACKAGE_11_RESEARCH_INSTITUTE.md',
        'manifest': '/data/research-institute-manifest.json',
        'status': 'documented',
        'documented_date': today,
        'philosophy': RESEARCH_INSTITUTE_MANIFEST['philosophy'],
        'research_program_count': RESEARCH_INSTITUTE_MANIFEST['research_program_count'],
        'lifecycle_stage_count': RESEARCH_INSTITUTE_MANIFEST['lifecycle_stage_count'],
        'county_milestone_date': county_milestone_date,
        'counties_total': RESEARCH_INSTITUTE_MANIFEST['county_milestone']['counties_total'],
        'days_to_county_milestone': days_to_county_milestone,
        'packages_completed': RESEARCH_INSTITUTE_MANIFEST['packages_completed'],
        'packages_complete_pct': RESEARCH_INSTITUTE_MANIFEST['packages_complete_pct'],
        'engineering_note': RESEARCH_INSTITUTE_MANIFEST['engineering_note'],
        'next_package': {
            'number': 12,
            'id': 'IMP-12',
            'title': 'Master Community Education Academy, Curriculum Factory & Certification System',
            'status': 'documented',
        },
    },
    'education_academy': {
        'title': 'Master Community Education Academy, Curriculum Factory & Certification System',
        'package': 'Implementation Package 12 of 50',
        'route': '/docs/IMPLEMENTATION_PACKAGE_12_COMMUNITY_EDUCATION_ACADEMY.md',
        'manifest': '/data/education-academy-manifest.json',
        'status': 'documented',
        'documented_date': today,
        'philosophy': EDUCATION_ACADEMY_MANIFEST['philosophy'],
        'school_count': EDUCATION_ACADEMY_MANIFEST['school_count'],
        'topic_count': EDUCATION_ACADEMY_MANIFEST['topic_count'],
        'learning_level_count': EDUCATION_ACADEMY_MANIFEST['learning_level_count'],
        'curriculum_stage_count': EDUCATION_ACADEMY_MANIFEST['curriculum_stage_count'],
        'certification_count': EDUCATION_ACADEMY_MANIFEST['certification_count'],
        'packages_completed': EDUCATION_ACADEMY_MANIFEST['packages_completed'],
        'packages_complete_pct': EDUCATION_ACADEMY_MANIFEST['packages_complete_pct'],
        'county_milestone_date': county_milestone_date,
        'engineering_note': EDUCATION_ACADEMY_MANIFEST['engineering_note'],
        'next_package': {
            'number': 13,
            'id': 'IMP-13',
            'title': 'Master Volunteer Network, Education Leader Pipeline & Community Organizing Platform',
            'status': 'documented',
        },
    },
    'volunteer_network': {
        'title': 'Master Volunteer Network, Education Leader Pipeline & Community Organizing Platform',
        'package': 'Implementation Package 13 of 50',
        'route': '/docs/IMPLEMENTATION_PACKAGE_13_VOLUNTEER_NETWORK.md',
        'manifest': '/data/volunteer-network-manifest.json',
        'status': 'documented',
        'documented_date': today,
        'philosophy': VOLUNTEER_NETWORK_MANIFEST['philosophy'],
        'journey_stage_count': VOLUNTEER_NETWORK_MANIFEST['journey_stage_count'],
        'pipeline_stage_count': VOLUNTEER_NETWORK_MANIFEST['pipeline_stage_count'],
        'role_count': VOLUNTEER_NETWORK_MANIFEST['role_count'],
        'skill_count': VOLUNTEER_NETWORK_MANIFEST['skill_count'],
        'cities_tracked': VOLUNTEER_NETWORK_MANIFEST['cities_tracked'],
        'packages_completed': VOLUNTEER_NETWORK_MANIFEST['packages_completed'],
        'packages_complete_pct': VOLUNTEER_NETWORK_MANIFEST['packages_complete_pct'],
        'county_milestone_date': county_milestone_date,
        'engineering_note': VOLUNTEER_NETWORK_MANIFEST['engineering_note'],
        'next_package': {
            'number': 14,
            'id': 'IMP-14',
            'title': 'Master Coalition Network, Organization Portal & Partnership Operating System',
            'status': 'documented',
        },
    },
    'coalition_network': {
        'title': 'Master Coalition Network, Organization Portal & Partnership Operating System',
        'package': 'Implementation Package 14 of 50',
        'route': '/docs/IMPLEMENTATION_PACKAGE_14_COALITION_NETWORK.md',
        'manifest': '/data/coalition-network-manifest.json',
        'status': 'documented',
        'documented_date': today,
        'philosophy': COALITION_NETWORK_MANIFEST['philosophy'],
        'organization_type_count': COALITION_NETWORK_MANIFEST['organization_type_count'],
        'lifecycle_stage_count': COALITION_NETWORK_MANIFEST['lifecycle_stage_count'],
        'packages_completed': COALITION_NETWORK_MANIFEST['packages_completed'],
        'packages_complete_pct': COALITION_NETWORK_MANIFEST['packages_complete_pct'],
        'county_milestone_date': county_milestone_date,
        'engineering_note': COALITION_NETWORK_MANIFEST['engineering_note'],
        'next_package': {
            'number': 15,
            'id': 'IMP-15',
            'title': 'Master County Operating System, City Operating System & Neighborhood Operating System',
            'status': 'documented',
        },
    },
    'local_operating_systems': {
        'title': 'Master County Operating System, City Operating System & Neighborhood Operating System',
        'package': 'Implementation Package 15 of 50',
        'route': '/docs/IMPLEMENTATION_PACKAGE_15_LOCAL_OPERATING_SYSTEMS.md',
        'manifest': '/data/local-operating-systems-manifest.json',
        'status': 'documented',
        'documented_date': today,
        'philosophy': LOCAL_OPERATING_SYSTEMS_MANIFEST['philosophy'],
        'counties_total': LOCAL_OPERATING_SYSTEMS_MANIFEST['counties_total'],
        'target_cities': LOCAL_OPERATING_SYSTEMS_MANIFEST['target_cities'],
        'engagement_goal_pct': LOCAL_OPERATING_SYSTEMS_MANIFEST['engagement_goal_pct'],
        'county_module_count': LOCAL_OPERATING_SYSTEMS_MANIFEST['county_module_count'],
        'city_module_count': LOCAL_OPERATING_SYSTEMS_MANIFEST['city_module_count'],
        'neighborhood_module_count': LOCAL_OPERATING_SYSTEMS_MANIFEST['neighborhood_module_count'],
        'packages_completed': LOCAL_OPERATING_SYSTEMS_MANIFEST['packages_completed'],
        'packages_complete_pct': LOCAL_OPERATING_SYSTEMS_MANIFEST['packages_complete_pct'],
        'county_milestone_date': county_milestone_date,
        'engineering_note': LOCAL_OPERATING_SYSTEMS_MANIFEST['engineering_note'],
        'next_package': {
            'number': 16,
            'id': 'IMP-16',
            'title': 'Master Communication Platform, Messaging System & Arkansas Civic Media Network',
            'status': 'documented',
        },
    },
    'communication_platform': {
        'title': 'Master Communication Platform, Messaging System & Arkansas Civic Media Network',
        'package': 'Implementation Package 16 of 50',
        'route': '/docs/IMPLEMENTATION_PACKAGE_16_COMMUNICATION_PLATFORM.md',
        'manifest': '/data/communication-platform-manifest.json',
        'status': 'documented',
        'documented_date': today,
        'philosophy': COMMUNICATION_PLATFORM_MANIFEST['philosophy'],
        'communication_layer_count': COMMUNICATION_PLATFORM_MANIFEST['communication_layer_count'],
        'civic_media_format_count': COMMUNICATION_PLATFORM_MANIFEST['civic_media_format_count'],
        'newsletter_channel_count': len(NEWSLETTER_CHANNELS),
        'packages_completed': COMMUNICATION_PLATFORM_MANIFEST['packages_completed'],
        'packages_complete_pct': COMMUNICATION_PLATFORM_MANIFEST['packages_complete_pct'],
        'engagement_goal_pct': engagement_goal_pct,
        'arkansans_connected_goal': arkansans_connected_goal,
        'engineering_note': COMMUNICATION_PLATFORM_MANIFEST['engineering_note'],
        'next_package': {
            'number': 17,
            'id': 'IMP-17',
            'title': 'Master Calendar, Scheduling, Event Management & Time Intelligence System',
            'status': 'documented',
        },
    },
    'time_intelligence': {
        'title': 'Master Calendar, Scheduling, Event Management & Time Intelligence System',
        'package': 'Implementation Package 17 of 50',
        'route': '/docs/IMPLEMENTATION_PACKAGE_17_TIME_INTELLIGENCE.md',
        'manifest': '/data/time-intelligence-manifest.json',
        'status': 'documented',
        'documented_date': today,
        'philosophy': TIME_INTELLIGENCE_MANIFEST['philosophy'],
        'localbrain_calendar_count': TIME_INTELLIGENCE_MANIFEST['localbrain_calendar_count'],
        'external_sync_count': len(EXTERNAL_CALENDAR_SYNC),
        'recurring_event_type_count': len(RECURRING_EVENT_TYPES),
        'packages_completed': TIME_INTELLIGENCE_MANIFEST['packages_completed'],
        'packages_complete_pct': TIME_INTELLIGENCE_MANIFEST['packages_complete_pct'],
        'county_milestone_date': county_milestone_date,
        'engineering_note': TIME_INTELLIGENCE_MANIFEST['engineering_note'],
        'next_package': {
            'number': 19,
            'id': 'IMP-19',
            'title': 'Master Analytics, Institutional Intelligence & Predictive Insights Engine',
            'note': 'Doctrinal package 19; engineering IMP-19 is page templates',
        },
    },
    'relationship_intelligence': {
        'title': 'Master Relationship Intelligence, Contact Network & Community Graph',
        'package': 'Implementation Package 18 of 50',
        'route': '/docs/IMPLEMENTATION_PACKAGE_18_RELATIONSHIP_INTELLIGENCE.md',
        'manifest': '/data/relationship-intelligence-manifest.json',
        'status': 'documented',
        'documented_date': today,
        'philosophy': RELATIONSHIP_INTELLIGENCE_MANIFEST['philosophy'],
        'relationship_architecture_type_count': RELATIONSHIP_INTELLIGENCE_MANIFEST['relationship_architecture_type_count'],
        'contact_profile_field_count': RELATIONSHIP_INTELLIGENCE_MANIFEST['contact_profile_field_count'],
        'community_graph_visualization_count': RELATIONSHIP_INTELLIGENCE_MANIFEST['community_graph_visualization_count'],
        'relationship_health_metric_count': RELATIONSHIP_INTELLIGENCE_MANIFEST['relationship_health_metric_count'],
        'packages_completed': RELATIONSHIP_INTELLIGENCE_MANIFEST['packages_completed'],
        'packages_complete_pct': RELATIONSHIP_INTELLIGENCE_MANIFEST['packages_complete_pct'],
        'county_milestone_date': county_milestone_date,
        'engagement_goal_pct': engagement_goal_pct,
        'arkansans_connected_goal': arkansans_connected_goal,
        'mc_dashboard': RELATIONSHIP_INTELLIGENCE_MANIFEST['mc_dashboard'],
        'engineering_note': RELATIONSHIP_INTELLIGENCE_MANIFEST['engineering_note'],
        'next_package': {
            'number': 20,
            'id': 'IMP-20',
            'title': 'Master Automation Engine, Workflow Orchestration & Institutional Process Management',
            'status': 'specified',
        },
    },
    'institutional_analytics': {
        'title': 'Master Analytics, Institutional Intelligence & Predictive Insights Engine',
        'package': 'Implementation Package 19 of 50',
        'route': '/docs/IMPLEMENTATION_PACKAGE_19_INSTITUTIONAL_ANALYTICS.md',
        'manifest': '/data/institutional-analytics-manifest.json',
        'status': 'documented',
        'documented_date': today,
        'philosophy': INSTITUTIONAL_ANALYTICS_MANIFEST['philosophy'],
        'intelligence_layer_count': INSTITUTIONAL_ANALYTICS_MANIFEST['intelligence_layer_count'],
        'executive_scorecard_count': INSTITUTIONAL_ANALYTICS_MANIFEST['executive_scorecard_count'],
        'community_health_indicator_count': INSTITUTIONAL_ANALYTICS_MANIFEST['community_health_indicator_count'],
        'institutional_health_component_count': INSTITUTIONAL_ANALYTICS_MANIFEST['institutional_health_component_count'],
        'predictive_analytics_count': INSTITUTIONAL_ANALYTICS_MANIFEST['predictive_analytics_count'],
        'packages_completed': INSTITUTIONAL_ANALYTICS_MANIFEST['packages_completed'],
        'packages_complete_pct': INSTITUTIONAL_ANALYTICS_MANIFEST['packages_complete_pct'],
        'county_milestone_date': county_milestone_date,
        'engagement_goal_pct': engagement_goal_pct,
        'arkansans_connected_goal': arkansans_connected_goal,
        'mc_dashboard': INSTITUTIONAL_ANALYTICS_MANIFEST['mc_dashboard'],
        'engineering_note': INSTITUTIONAL_ANALYTICS_MANIFEST['engineering_note'],
        'next_package': {
            'number': 21,
            'id': 'IMP-21',
            'title': 'Master Public Website, Digital Experience & Citizen Engagement Platform',
            'status': 'specified',
        },
    },
    'automation_engine': {
        'title': 'Master Automation Engine, Workflow Orchestration & Institutional Process Management',
        'package': 'Implementation Package 20 of 50',
        'route': '/docs/IMPLEMENTATION_PACKAGE_20_AUTOMATION_ENGINE.md',
        'manifest': '/data/automation-engine-manifest.json',
        'status': 'documented',
        'documented_date': today,
        'philosophy': AUTOMATION_ENGINE_MANIFEST['philosophy'],
        'workflow_engine_step_count': AUTOMATION_ENGINE_MANIFEST['workflow_engine_step_count'],
        'workflow_category_count': AUTOMATION_ENGINE_MANIFEST['workflow_category_count'],
        'workflow_type_count': AUTOMATION_ENGINE_MANIFEST['workflow_type_count'],
        'approval_rule_count': len(APPROVAL_RULE_TYPES),
        'automation_rule_count': len(AUTOMATION_RULES),
        'packages_completed': AUTOMATION_ENGINE_MANIFEST['packages_completed'],
        'packages_complete_pct': AUTOMATION_ENGINE_MANIFEST['packages_complete_pct'],
        'county_milestone_date': county_milestone_date,
        'engagement_goal_pct': engagement_goal_pct,
        'arkansans_connected_goal': arkansans_connected_goal,
        'mc_dashboard': AUTOMATION_ENGINE_MANIFEST['mc_dashboard'],
        'engineering_note': AUTOMATION_ENGINE_MANIFEST['engineering_note'],
        'next_package': {
            'number': 22,
            'id': 'IMP-22',
            'title': 'Master Mobile Experience, Progressive Web App & Field Operations Platform',
            'status': 'specified',
        },
    },
    'public_website': {
        'title': 'Master Public Website, Digital Experience & Citizen Engagement Platform',
        'package': 'Implementation Package 21 of 50',
        'route': '/docs/IMPLEMENTATION_PACKAGE_21_PUBLIC_WEBSITE.md',
        'manifest': '/data/public-website-manifest.json',
        'status': 'documented',
        'documented_date': today,
        'philosophy': PUBLIC_WEBSITE_MANIFEST['philosophy'],
        'homepage_section_count': PUBLIC_WEBSITE_MANIFEST['homepage_section_count'],
        'arkansas_map_layer_count': PUBLIC_WEBSITE_MANIFEST['arkansas_map_layer_count'],
        'accessibility_standard_count': PUBLIC_WEBSITE_MANIFEST['accessibility_standard_count'],
        'begin_learning_entry_count': len(BEGIN_LEARNING_ENTRY_POINTS),
        'public_engagement_action_count': len(PUBLIC_ENGAGEMENT_ACTIONS),
        'packages_completed': PUBLIC_WEBSITE_MANIFEST['packages_completed'],
        'packages_complete_pct': PUBLIC_WEBSITE_MANIFEST['packages_complete_pct'],
        'county_milestone_date': county_milestone_date,
        'engagement_goal_pct': engagement_goal_pct,
        'arkansans_connected_goal': arkansans_connected_goal,
        'mc_dashboard': PUBLIC_WEBSITE_MANIFEST['mc_dashboard'],
        'public_site_url': PUBLIC_WEBSITE_MANIFEST['public_site_url'],
        'engineering_note': PUBLIC_WEBSITE_MANIFEST['engineering_note'],
        'next_package': {
            'number': 22,
            'id': 'IMP-22',
            'title': 'Master Mobile Experience, Progressive Web App & Field Operations Platform',
            'status': 'documented',
        },
    },
    'mobile_pwa': {
        'title': 'Master Mobile Experience, Progressive Web App & Field Operations Platform',
        'package': 'Implementation Package 22 of 50',
        'route': '/docs/IMPLEMENTATION_PACKAGE_22_MOBILE_PWA.md',
        'manifest': '/data/mobile-pwa-manifest.json',
        'status': 'documented',
        'documented_date': today,
        'philosophy': MOBILE_PWA_MANIFEST['philosophy'],
        'pwa_capability_count': MOBILE_PWA_MANIFEST['pwa_capability_count'],
        'qr_code_target_count': MOBILE_PWA_MANIFEST['qr_code_target_count'],
        'mobile_accessibility_count': MOBILE_PWA_MANIFEST['mobile_accessibility_count'],
        'mobile_dashboard_widget_count': len(MOBILE_DASHBOARD_WIDGETS),
        'field_data_collection_count': len(FIELD_DATA_COLLECTION),
        'packages_completed': MOBILE_PWA_MANIFEST['packages_completed'],
        'packages_complete_pct': MOBILE_PWA_MANIFEST['packages_complete_pct'],
        'county_milestone_date': county_milestone_date,
        'engagement_goal_pct': engagement_goal_pct,
        'arkansans_connected_goal': arkansans_connected_goal,
        'mc_dashboard': MOBILE_PWA_MANIFEST['mc_dashboard'],
        'engineering_note': MOBILE_PWA_MANIFEST['engineering_note'],
        'next_package': {
            'number': 23,
            'id': 'IMP-23',
            'title': 'Master Document Management, Digital Library & Institutional Archive',
            'status': 'documented',
        },
    },
    'digital_library': {
        'title': 'Master Document Management, Digital Library & Institutional Archive',
        'package': 'Implementation Package 23 of 50',
        'route': '/docs/IMPLEMENTATION_PACKAGE_23_DIGITAL_LIBRARY.md',
        'manifest': '/data/digital-library-manifest.json',
        'status': 'documented',
        'documented_date': today,
        'philosophy': DIGITAL_LIBRARY_MANIFEST['philosophy'],
        'collection_count': DIGITAL_LIBRARY_MANIFEST['collection_count'],
        'metadata_field_count': DIGITAL_LIBRARY_MANIFEST['metadata_field_count'],
        'lifecycle_stage_count': DIGITAL_LIBRARY_MANIFEST['lifecycle_stage_count'],
        'search_dimension_count': len(SEARCH_DIMENSIONS),
        'document_access_level_count': len(DOCUMENT_ACCESS_LEVELS),
        'packages_completed': DIGITAL_LIBRARY_MANIFEST['packages_completed'],
        'packages_complete_pct': DIGITAL_LIBRARY_MANIFEST['packages_complete_pct'],
        'county_milestone_date': county_milestone_date,
        'engagement_goal_pct': engagement_goal_pct,
        'arkansans_connected_goal': arkansans_connected_goal,
        'mc_dashboard': DIGITAL_LIBRARY_MANIFEST['mc_dashboard'],
        'engineering_note': DIGITAL_LIBRARY_MANIFEST['engineering_note'],
        'next_package': {
            'number': 24,
            'id': 'IMP-24',
            'title': 'Master Integration Platform, External Data Services & Open API Architecture',
            'status': 'documented',
        },
    },
    'integration_platform': {
        'title': 'Master Integration Platform, External Data Services & Open API Architecture',
        'package': 'Implementation Package 24 of 50',
        'route': '/docs/IMPLEMENTATION_PACKAGE_24_INTEGRATION_PLATFORM.md',
        'manifest': '/data/integration-platform-manifest.json',
        'status': 'documented',
        'documented_date': today,
        'philosophy': INTEGRATION_PLATFORM_MANIFEST['philosophy'],
        'integration_category_count': INTEGRATION_PLATFORM_MANIFEST['integration_category_count'],
        'integration_pipeline_step_count': len(INTEGRATION_PIPELINE_STEPS),
        'open_api_use_case_count': len(OPEN_API_USE_CASES),
        'institutional_event_count': len(INSTITUTIONAL_EVENTS),
        'integration_security_standard_count': len(INTEGRATION_SECURITY_STANDARDS),
        'packages_completed': INTEGRATION_PLATFORM_MANIFEST['packages_completed'],
        'packages_complete_pct': INTEGRATION_PLATFORM_MANIFEST['packages_complete_pct'],
        'county_milestone_date': county_milestone_date,
        'engagement_goal_pct': engagement_goal_pct,
        'arkansans_connected_goal': arkansans_connected_goal,
        'mc_dashboard': INTEGRATION_PLATFORM_MANIFEST['mc_dashboard'],
        'engineering_note': INTEGRATION_PLATFORM_MANIFEST['engineering_note'],
        'next_package': {
            'number': 25,
            'id': 'IMP-25',
            'title': 'Master Security, Privacy, Compliance & Institutional Trust Framework',
            'status': 'documented',
        },
    },
    'security_trust': {
        'title': 'Master Security, Privacy, Compliance & Institutional Trust Framework',
        'package': 'Implementation Package 25 of 50',
        'route': '/docs/IMPLEMENTATION_PACKAGE_25_SECURITY_TRUST.md',
        'manifest': '/data/security-trust-manifest.json',
        'status': 'documented',
        'documented_date': today,
        'philosophy': SECURITY_TRUST_MANIFEST['philosophy'],
        'security_principle_count': SECURITY_TRUST_MANIFEST['security_principle_count'],
        'data_classification_count': SECURITY_TRUST_MANIFEST['data_classification_count'],
        'compliance_area_count': len(COMPLIANCE_FRAMEWORK_AREAS),
        'audit_event_count': len(AUDIT_LOG_EVENTS),
        'ethics_standard_count': len(INSTITUTIONAL_ETHICS_STANDARDS),
        'halfway_milestone': SECURITY_TRUST_MANIFEST['halfway_milestone'],
        'packages_completed': SECURITY_TRUST_MANIFEST['packages_completed'],
        'packages_complete_pct': SECURITY_TRUST_MANIFEST['packages_complete_pct'],
        'county_milestone_date': county_milestone_date,
        'engagement_goal_pct': engagement_goal_pct,
        'arkansans_connected_goal': arkansans_connected_goal,
        'mc_dashboard': SECURITY_TRUST_MANIFEST['mc_dashboard'],
        'engineering_note': SECURITY_TRUST_MANIFEST['engineering_note'],
        'next_package': {
            'number': 26,
            'id': 'IMP-26',
            'title': 'Master Testing, Quality Assurance, Certification & Launch Readiness Framework',
            'status': 'documented',
        },
    },
    'qa_launch_readiness': {
        'title': 'Master Testing, Quality Assurance, Certification & Launch Readiness Framework',
        'package': 'Implementation Package 26 of 50',
        'route': '/docs/IMPLEMENTATION_PACKAGE_26_QA_LAUNCH_READINESS.md',
        'manifest': '/data/qa-launch-readiness-manifest.json',
        'status': 'documented',
        'documented_date': today,
        'philosophy': QA_LAUNCH_READINESS_MANIFEST['philosophy'],
        'launch_certification_module_count': QA_LAUNCH_READINESS_MANIFEST['launch_certification_module_count'],
        'county_readiness_criteria_count': QA_LAUNCH_READINESS_MANIFEST['county_readiness_criteria_count'],
        'statewide_launch_checklist_count': QA_LAUNCH_READINESS_MANIFEST['statewide_launch_checklist_count'],
        'counties_with_partnerships_goal': QA_LAUNCH_READINESS_MANIFEST['organizational_goals']['counties_with_partnerships_goal'],
        'operational_simulation_count': QA_LAUNCH_READINESS_MANIFEST['operational_simulation_count'],
        'packages_completed': QA_LAUNCH_READINESS_MANIFEST['packages_completed'],
        'packages_complete_pct': QA_LAUNCH_READINESS_MANIFEST['packages_complete_pct'],
        'county_milestone_date': county_milestone_date,
        'engagement_goal_pct': engagement_goal_pct,
        'arkansans_connected_goal': arkansans_connected_goal,
        'mc_dashboard': QA_LAUNCH_READINESS_MANIFEST['mc_dashboard'],
        'engineering_note': QA_LAUNCH_READINESS_MANIFEST['engineering_note'],
        'next_package': {
            'number': 27,
            'id': 'IMP-27',
            'title': 'Master Deployment, Infrastructure, DevOps & Production Operations',
            'status': 'documented',
        },
    },
    'devops_production': {
        'title': 'Master Deployment, Infrastructure, DevOps & Production Operations',
        'package': 'Implementation Package 27 of 50',
        'route': '/docs/IMPLEMENTATION_PACKAGE_27_DEVOPS_PRODUCTION.md',
        'manifest': '/data/devops-production-manifest.json',
        'status': 'documented',
        'documented_date': today,
        'philosophy': DEVOPS_PRODUCTION_MANIFEST['philosophy'],
        'infrastructure_component_count': DEVOPS_PRODUCTION_MANIFEST['infrastructure_component_count'],
        'deployment_pipeline_step_count': DEVOPS_PRODUCTION_MANIFEST['deployment_pipeline_step_count'],
        'monitoring_platform_metric_count': DEVOPS_PRODUCTION_MANIFEST['monitoring_platform_metric_count'],
        'environment_count': DEVOPS_PRODUCTION_MANIFEST['environment_count'],
        'operational_metric_count': DEVOPS_PRODUCTION_MANIFEST['operational_metric_count'],
        'packages_completed': DEVOPS_PRODUCTION_MANIFEST['packages_completed'],
        'packages_complete_pct': DEVOPS_PRODUCTION_MANIFEST['packages_complete_pct'],
        'county_milestone_date': county_milestone_date,
        'engagement_goal_pct': engagement_goal_pct,
        'arkansans_connected_goal': arkansans_connected_goal,
        'mc_dashboard': DEVOPS_PRODUCTION_MANIFEST['mc_dashboard'],
        'engineering_note': DEVOPS_PRODUCTION_MANIFEST['engineering_note'],
        'next_package': {
            'number': 28,
            'id': 'IMP-28',
            'title': 'Master Governance, Executive Office, PMO & Institutional Decision Framework',
            'status': 'documented',
        },
    },
    'governance_pmo': {
        'title': 'Master Governance, Executive Office, PMO & Institutional Decision Framework',
        'package': 'Implementation Package 28 of 50',
        'route': '/docs/IMPLEMENTATION_PACKAGE_28_GOVERNANCE_PMO.md',
        'manifest': '/data/governance-pmo-manifest.json',
        'status': 'documented',
        'documented_date': today,
        'philosophy': GOVERNANCE_PMO_MANIFEST['philosophy'],
        'institutional_structure_level_count': GOVERNANCE_PMO_MANIFEST['institutional_structure_level_count'],
        'decision_framework_step_count': GOVERNANCE_PMO_MANIFEST['decision_framework_step_count'],
        'pmo_responsibility_count': GOVERNANCE_PMO_MANIFEST['pmo_responsibility_count'],
        'governance_meeting_type_count': GOVERNANCE_PMO_MANIFEST['governance_meeting_type_count'],
        'risk_governance_category_count': GOVERNANCE_PMO_MANIFEST['risk_governance_category_count'],
        'packages_completed': GOVERNANCE_PMO_MANIFEST['packages_completed'],
        'packages_complete_pct': GOVERNANCE_PMO_MANIFEST['packages_complete_pct'],
        'county_milestone_date': county_milestone_date,
        'engagement_goal_pct': engagement_goal_pct,
        'arkansans_connected_goal': arkansans_connected_goal,
        'mc_dashboard': GOVERNANCE_PMO_MANIFEST['mc_dashboard'],
        'engineering_note': GOVERNANCE_PMO_MANIFEST['engineering_note'],
        'next_package': {
            'number': 29,
            'id': 'IMP-29',
            'title': 'Master Sustainability, Growth Strategy, Knowledge Transfer & Institutional Continuity',
            'status': 'documented',
        },
    },
    'sustainability_continuity': {
        'title': 'Master Sustainability, Growth Strategy, Knowledge Transfer & Institutional Continuity',
        'package': 'Implementation Package 29 of 50',
        'route': '/docs/IMPLEMENTATION_PACKAGE_29_SUSTAINABILITY_CONTINUITY.md',
        'manifest': '/data/sustainability-continuity-manifest.json',
        'status': 'documented',
        'documented_date': today,
        'philosophy': SUSTAINABILITY_CONTINUITY_MANIFEST['philosophy'],
        'continuity_pillar_count': SUSTAINABILITY_CONTINUITY_MANIFEST['continuity_pillar_count'],
        'institutional_playbook_count': SUSTAINABILITY_CONTINUITY_MANIFEST['institutional_playbook_count'],
        'succession_planning_tracking_count': SUSTAINABILITY_CONTINUITY_MANIFEST['succession_planning_tracking_count'],
        'institutional_memory_preserve_count': SUSTAINABILITY_CONTINUITY_MANIFEST['institutional_memory_preserve_count'],
        'mc_sustainability_dashboard_metric_count': SUSTAINABILITY_CONTINUITY_MANIFEST['mc_sustainability_dashboard_metric_count'],
        'packages_completed': SUSTAINABILITY_CONTINUITY_MANIFEST['packages_completed'],
        'packages_complete_pct': SUSTAINABILITY_CONTINUITY_MANIFEST['packages_complete_pct'],
        'county_milestone_date': county_milestone_date,
        'engagement_goal_pct': engagement_goal_pct,
        'arkansans_connected_goal': arkansans_connected_goal,
        'mc_dashboard': SUSTAINABILITY_CONTINUITY_MANIFEST['mc_dashboard'],
        'engineering_note': SUSTAINABILITY_CONTINUITY_MANIFEST['engineering_note'],
        'next_package': {
            'number': 30,
            'id': 'IMP-30',
            'title': 'Master Launch Strategy, Statewide Rollout, Adoption Campaign & January 2027 Operational Readiness',
            'status': 'specified',
        },
    },
    'master_timeline': MASTER_TIMELINE,
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
        'organizational_readiness_date': organizational_readiness_date,
        'software_completion_date': software_completion_date,
        'county_milestone_date': county_milestone_date,
        'days_to_software': days_to_software,
        'days_to_county_milestone': days_to_county_milestone,
        'days_to_organizational': days_to_organizational,
        'counties': 75,
        'cities': 250,
        'connected_voter_pct_per_county_city': 15,
        'arkansans_connected_goal': 200000,
        'education_leaders_statewide': True,
        'coalition_partners_onboarded': True,
        'mission_control_operational': True,
        'days_remaining': days_to_organizational,
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
        'software_completion_date': software_completion_date,
        'county_milestone_date': county_milestone_date,
        'organizational_readiness_date': organizational_readiness_date,
        'days_to_software': days_to_software,
        'days_to_county_milestone': days_to_county_milestone,
        'days_to_organizational': days_to_organizational,
        'engagement_goal_pct': engagement_goal_pct,
        'arkansans_connected_goal': arkansans_connected_goal,
        'completion_target_date': organizational_readiness_date,
        'days_remaining': days_to_organizational,
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

with open(root / 'data/localbrain-network-manifest.json', 'w', newline='\n') as f:
    json.dump(LOCALBRAIN_NETWORK_MANIFEST, f, indent=2)
    f.write('\n')

with open(root / 'data/knowledge-graph-manifest.json', 'w', newline='\n') as f:
    json.dump(KNOWLEDGE_GRAPH_MANIFEST, f, indent=2)
    f.write('\n')

with open(root / 'data/content-management-manifest.json', 'w', newline='\n') as f:
    json.dump(CONTENT_MANAGEMENT_MANIFEST, f, indent=2)
    f.write('\n')

with open(root / 'data/research-institute-manifest.json', 'w', newline='\n') as f:
    json.dump(RESEARCH_INSTITUTE_MANIFEST, f, indent=2)
    f.write('\n')

with open(root / 'data/education-academy-manifest.json', 'w', newline='\n') as f:
    json.dump(EDUCATION_ACADEMY_MANIFEST, f, indent=2)
    f.write('\n')

with open(root / 'data/volunteer-network-manifest.json', 'w', newline='\n') as f:
    json.dump(VOLUNTEER_NETWORK_MANIFEST, f, indent=2)
    f.write('\n')

with open(root / 'data/coalition-network-manifest.json', 'w', newline='\n') as f:
    json.dump(COALITION_NETWORK_MANIFEST, f, indent=2)
    f.write('\n')

with open(root / 'data/local-operating-systems-manifest.json', 'w', newline='\n') as f:
    json.dump(LOCAL_OPERATING_SYSTEMS_MANIFEST, f, indent=2)
    f.write('\n')

with open(root / 'data/communication-platform-manifest.json', 'w', newline='\n') as f:
    json.dump(COMMUNICATION_PLATFORM_MANIFEST, f, indent=2)
    f.write('\n')

with open(root / 'data/time-intelligence-manifest.json', 'w', newline='\n') as f:
    json.dump(TIME_INTELLIGENCE_MANIFEST, f, indent=2)
    f.write('\n')

with open(root / 'data/relationship-intelligence-manifest.json', 'w', newline='\n') as f:
    json.dump(RELATIONSHIP_INTELLIGENCE_MANIFEST, f, indent=2)
    f.write('\n')

with open(root / 'data/institutional-analytics-manifest.json', 'w', newline='\n') as f:
    json.dump(INSTITUTIONAL_ANALYTICS_MANIFEST, f, indent=2)
    f.write('\n')

with open(root / 'data/automation-engine-manifest.json', 'w', newline='\n') as f:
    json.dump(AUTOMATION_ENGINE_MANIFEST, f, indent=2)
    f.write('\n')

with open(root / 'data/public-website-manifest.json', 'w', newline='\n') as f:
    json.dump(PUBLIC_WEBSITE_MANIFEST, f, indent=2)
    f.write('\n')

with open(root / 'data/mobile-pwa-manifest.json', 'w', newline='\n') as f:
    json.dump(MOBILE_PWA_MANIFEST, f, indent=2)
    f.write('\n')

with open(root / 'data/digital-library-manifest.json', 'w', newline='\n') as f:
    json.dump(DIGITAL_LIBRARY_MANIFEST, f, indent=2)
    f.write('\n')

with open(root / 'data/integration-platform-manifest.json', 'w', newline='\n') as f:
    json.dump(INTEGRATION_PLATFORM_MANIFEST, f, indent=2)
    f.write('\n')

with open(root / 'data/security-trust-manifest.json', 'w', newline='\n') as f:
    json.dump(SECURITY_TRUST_MANIFEST, f, indent=2)
    f.write('\n')

with open(root / 'data/qa-launch-readiness-manifest.json', 'w', newline='\n') as f:
    json.dump(QA_LAUNCH_READINESS_MANIFEST, f, indent=2)
    f.write('\n')

with open(root / 'data/devops-production-manifest.json', 'w', newline='\n') as f:
    json.dump(DEVOPS_PRODUCTION_MANIFEST, f, indent=2)
    f.write('\n')

with open(root / 'data/governance-pmo-manifest.json', 'w', newline='\n') as f:
    json.dump(GOVERNANCE_PMO_MANIFEST, f, indent=2)
    f.write('\n')

with open(root / 'data/sustainability-continuity-manifest.json', 'w', newline='\n') as f:
    json.dump(SUSTAINABILITY_CONTINUITY_MANIFEST, f, indent=2)
    f.write('\n')

print(
    f'Implementation Package: {len(IMPLEMENTATION_STEPS)} steps, '
    f'{len(BANDS)} bands, {implementation_package_readiness}% readiness, '
    f'{steps_documented} documented, {steps_implemented} implemented'
)
