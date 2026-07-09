"""
Generate data/technical-architecture.json — Build #48 Master Technical Architecture & Deployment Blueprint v1.0.
"""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
today = '2026-07-09'


def load_json(path):
    if path.exists():
        with open(path, encoding='utf-8') as f:
            return json.load(f)
    return {}


pa = load_json(root / 'data/platform-architecture.json')
db = load_json(root / 'data/database-schema.json')
mc = load_json(root / 'data/mission-control.json')
repo = load_json(root / 'data/repository-blueprint.json')

STACK = [
    {
        'id': 'FE', 'layer': 'Frontend', 'target': 'Next.js (App Router), React, TypeScript',
        'rationale': 'SSR, SEO, performance, long-term maintainability',
        'status': 'planned', 'current': 'Static HTML/CSS/JS — 81 routes, no framework',
        'live': False,
    },
    {
        'id': 'STYLE', 'layer': 'Styling', 'target': 'Tailwind CSS + component library + design tokens',
        'rationale': 'Themeable, consistent, accessible',
        'status': 'partial', 'current': 'Build #9 design-system.json, 14 ds-* components, custom CSS',
        'live': True, 'route': '/design-system/',
    },
    {
        'id': 'SRC', 'layer': 'Source Control', 'target': 'GitHub',
        'rationale': 'Version control, PRs, issues, institutional memory',
        'status': 'live', 'current': 'https://github.com/Grappe501/arkansas — main, numbered builds',
        'live': True,
    },
    {
        'id': 'DEPLOY', 'layer': 'Hosting & CI/CD', 'target': 'GitHub → automatic deploy → Netlify',
        'rationale': 'Preview deploys, SSL, CDN, forms',
        'status': 'live', 'current': 'https://arkansas-facts.netlify.app — static publish, preview on PR',
        'live': True,
    },
    {
        'id': 'DB', 'layer': 'Database', 'target': 'PostgreSQL (Neon)',
        'rationale': 'Scalable, branching, Git-style workflows, low maintenance',
        'status': 'planned', 'current': 'Static JSON in /data — 40+ registries, no live DB',
        'live': False, 'route': '/mission-control/database.html',
    },
    {
        'id': 'ORM', 'layer': 'ORM', 'target': 'Prisma',
        'rationale': 'Contact, Coalition, MC, events, content, claims, evidence, users',
        'status': 'planned', 'current': 'Schema blueprint only (Build #22) — not provisioned',
        'live': False,
    },
    {
        'id': 'AUTH', 'layer': 'Authentication', 'target': 'Email + Google OAuth',
        'rationale': 'Admin protected; education public',
        'status': 'planned', 'current': 'No auth — /admin/ mission-control shell only',
        'live': False,
    },
    {
        'id': 'SEARCH', 'layer': 'Search', 'target': 'Global indexed search',
        'rationale': 'Articles, cases, timeline, sources, claims, encyclopedia, Arkansas',
        'status': 'planned', 'current': 'No search UI or index',
        'live': False,
    },
]

SEARCH_INDEX = [
    'Articles', 'Lessons', 'Timeline', 'Court cases', 'People', 'Organizations',
    'Laws', 'Videos', 'Infographics', 'Sources', 'Claims', 'Encyclopedia', 'Arkansas pages',
]

APIS = [
    {'id': 'API-01', 'name': 'Content', 'status': 'planned', 'current': 'Static JSON files'},
    {'id': 'API-02', 'name': 'Research', 'status': 'planned', 'current': 'evidence-registry.json'},
    {'id': 'API-03', 'name': 'Mission Control', 'status': 'partial', 'current': 'mission-control.json — read-only static'},
    {'id': 'API-04', 'name': 'Contact Network', 'status': 'planned', 'current': 'Forms not integrated'},
    {'id': 'API-05', 'name': 'Coalition', 'status': 'planned', 'current': 'civic-ecosystem.json'},
    {'id': 'API-06', 'name': 'Academy', 'status': 'planned', 'current': 'education-academy.json'},
    {'id': 'API-07', 'name': 'Events', 'status': 'planned', 'current': 'No event calendar'},
    {'id': 'API-08', 'name': 'Media', 'status': 'planned', 'current': 'media-studio.json'},
    {'id': 'API-09', 'name': 'Knowledge Graph', 'status': 'partial', 'current': 'civic-intelligence.json — 38 nodes'},
    {'id': 'API-10', 'name': 'Claims Registry', 'status': 'partial', 'current': 'evidence-ledger.json — 3 claims'},
    {'id': 'API-11', 'name': 'Evidence', 'status': 'partial', 'current': '14 EV-* items'},
]

FILE_STRUCTURE = [
    '/app', '/components', '/content', '/research', '/encyclopedia', '/timeline',
    '/curriculum', '/academy', '/coalition', '/mission-control', '/laboratory',
    '/solutions', '/media', '/sources', '/api', '/admin', '/lib', '/prisma', '/public', '/docs',
]

AI_LAYER = [
    'Evidence Ledger', 'Knowledge Graph', 'Research Library', 'Claims Registry',
    'Encyclopedia', 'Curriculum', 'Mission Control',
]

DEPLOYMENT_WORKFLOW = [
    'Developer', 'GitHub', 'Pull Request', 'Preview Deploy', 'Testing',
    'Approval', 'Production', 'Mission Control updated',
]

ENVIRONMENTS = [
    {'id': 'dev', 'title': 'Development', 'status': 'partial', 'current': 'Local static + JSON'},
    {'id': 'test', 'title': 'Testing', 'status': 'planned', 'current': 'No automated test env'},
    {'id': 'preview', 'title': 'Preview', 'status': 'live', 'current': 'Netlify deploy previews on PR'},
    {'id': 'prod', 'title': 'Production', 'status': 'live', 'current': 'arkansas-facts.netlify.app'},
]

PERFORMANCE = [
    {'id': 'PERF-01', 'standard': 'Homepage < 2 seconds', 'status': 'partial', 'note': 'Static — not measured'},
    {'id': 'PERF-02', 'standard': 'Educational pages < 2 seconds', 'status': 'partial', 'note': 'Static — not measured'},
    {'id': 'PERF-03', 'standard': 'Search instant', 'status': 'planned', 'note': 'No search'},
    {'id': 'PERF-04', 'standard': 'Images optimized', 'status': 'partial', 'note': 'Minimal imagery'},
    {'id': 'PERF-05', 'standard': 'Video lazy loaded', 'status': 'planned', 'note': '0 videos'},
    {'id': 'PERF-06', 'standard': 'Charts deferred', 'status': 'planned', 'note': 'No interactive charts live'},
]

ACCESSIBILITY = [
    {'id': 'A11Y-01', 'standard': 'WCAG AA minimum', 'status': 'partial'},
    {'id': 'A11Y-02', 'standard': 'Keyboard navigation', 'status': 'partial'},
    {'id': 'A11Y-03', 'standard': 'Screen reader support', 'status': 'partial'},
    {'id': 'A11Y-04', 'standard': 'Reduced motion', 'status': 'partial'},
    {'id': 'A11Y-05', 'standard': 'High contrast', 'status': 'partial'},
    {'id': 'A11Y-06', 'standard': 'Accessible forms', 'status': 'partial', 'note': 'Netlify Forms on educate/'},
    {'id': 'A11Y-07', 'standard': 'Transcript support', 'status': 'planned', 'note': '0 videos'},
]

SECURITY = [
    {'id': 'SEC-01', 'area': 'Contact information', 'status': 'planned', 'note': 'No DB — forms not wired'},
    {'id': 'SEC-02', 'area': 'Administrative tools', 'status': 'planned', 'note': 'No auth gate'},
    {'id': 'SEC-03', 'area': 'Draft content', 'status': 'partial', 'note': 'JSON in repo — no draft isolation'},
    {'id': 'SEC-04', 'area': 'Review workflows', 'status': 'partial', 'note': 'MC workflow documented'},
    {'id': 'SEC-05', 'area': 'Authentication', 'status': 'planned'},
    {'id': 'SEC-06', 'area': 'API endpoints', 'status': 'planned', 'note': 'No APIs yet'},
]

MONITORING = [
    {'id': 'MON-01', 'area': 'Deployment', 'status': 'partial', 'current': 'Netlify deploy status in MC'},
    {'id': 'MON-02', 'area': 'Performance', 'status': 'planned'},
    {'id': 'MON-03', 'area': 'Errors', 'status': 'planned'},
    {'id': 'MON-04', 'area': 'Broken links', 'status': 'planned'},
    {'id': 'MON-05', 'area': 'Accessibility', 'status': 'planned'},
    {'id': 'MON-06', 'area': 'Search', 'status': 'planned'},
    {'id': 'MON-07', 'area': 'Database health', 'status': 'planned', 'note': 'No DB'},
    {'id': 'MON-08', 'area': 'API health', 'status': 'planned'},
    {'id': 'MON-09', 'area': 'Content freshness', 'status': 'partial', 'current': 'MC registries manual'},
]

BACKUP = [
    {'item': 'Automatic database backups', 'status': 'planned'},
    {'item': 'Repository backups', 'status': 'live', 'note': 'GitHub'},
    {'item': 'Media backups', 'status': 'planned', 'note': 'No media pipeline'},
    {'item': 'Research archive backups', 'status': 'partial', 'note': 'JSON in repo'},
    {'item': 'Version history', 'status': 'live', 'note': 'Git + numbered builds'},
]

CMS_PHILOSOPHY = {
    'approach': 'Mission Control as publishing system — not traditional CMS',
    'article_lifecycle': ['Workflow', 'Review', 'Approval', 'Publishing', 'Revision', 'Version history'],
    'status': 'partial',
    'current': 'JSON registries + gen scripts — no write API or approval gates',
}

stack_live = sum(1 for s in STACK if s['live'])
stack_partial = sum(1 for s in STACK if s['status'] == 'partial')
stack_planned = sum(1 for s in STACK if s['status'] == 'planned')
apis_live_partial = sum(1 for a in APIS if a['status'] in ('live', 'partial'))

MC_METRICS = [
    {'id': 'TA-01', 'title': 'Stack layers defined', 'status': 'live', 'current': f'{len(STACK)} layers'},
    {'id': 'TA-02', 'title': 'Stack components live', 'status': 'partial', 'current': f'{stack_live}/{len(STACK)}'},
    {'id': 'TA-03', 'title': 'Target Next.js migration', 'status': 'planned', 'current': 'Static v1 — repository blueprint defines src/ target'},
    {'id': 'TA-04', 'title': 'Neon PostgreSQL provisioned', 'status': 'planned', 'current': 'Not provisioned'},
    {'id': 'TA-05', 'title': 'Prisma ORM', 'status': 'planned', 'current': 'Schema blueprint only'},
    {'id': 'TA-06', 'title': 'Global search', 'status': 'planned', 'current': f'0/{len(SEARCH_INDEX)} index types'},
    {'id': 'TA-07', 'title': 'Documented APIs', 'status': 'partial', 'current': f'{apis_live_partial}/{len(APIS)} partial static'},
    {'id': 'TA-08', 'title': 'Deployment pipeline', 'status': 'live', 'current': 'GitHub → Netlify'},
    {'id': 'TA-09', 'title': 'Preview environments', 'status': 'live', 'current': 'Netlify PR previews'},
    {'id': 'TA-10', 'title': 'Production monitoring', 'status': 'planned', 'current': '1/9 monitors partial'},
]

readiness_factors = [
    min(100, stack_live / len(STACK) * 100 * 2),
    min(100, stack_partial / len(STACK) * 100),
    100 if CMS_PHILOSOPHY['status'] == 'partial' else 0,
    apis_live_partial / len(APIS) * 100 * 0.5,
    sum(1 for e in ENVIRONMENTS if e['status'] == 'live') / len(ENVIRONMENTS) * 100,
    sum(1 for m in MONITORING if m['status'] != 'planned') / len(MONITORING) * 100 * 2,
    0,  # Next.js not started
    0,  # Neon not started
]
technical_architecture_readiness = round(sum(readiness_factors) / len(readiness_factors))

out = {
    'version': '1.0',
    'build': 48,
    'updated': today,
    'title': 'Master Technical Architecture & Deployment Blueprint v1.0',
    'subtitle': 'Production Engineering Constitution',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/technical-architecture.html',
    'constitution': '/docs/MASTER_TECHNICAL_ARCHITECTURE.md',
    'purpose': 'How the institution will be built — fast, secure, searchable, maintainable, scalable, transparent.',
    'governing_principle': 'Technology nearly invisible to public — engineered for permanence like the knowledge it preserves.',
    'technical_philosophy': 'Digital museum · research library · educational university · archive · civic OS — under one roof.',
    'technical_principles': [
        'Build for twenty years, not two',
        'Maintainability over shortcuts',
        'Documentation over assumptions',
        'Transparency over cleverness',
        'Institutional continuity over individual developers',
    ],
    'extends': [
        {'title': 'Platform Blueprint', 'build': 20, 'route': '/data/platform-architecture.json'},
        {'title': 'Database Schema', 'build': 22, 'route': '/data/database-schema.json'},
        {'title': 'Repository Blueprint', 'build': 21, 'route': '/data/repository-blueprint.json'},
    ],
    'technology_stack': STACK,
    'stack_summary': {
        'layers_total': len(STACK),
        'live': stack_live,
        'partial': stack_partial,
        'planned': stack_planned,
    },
    'search_architecture': {
        'title': 'Global Search',
        'status': 'planned',
        'index_types': SEARCH_INDEX,
        'index_types_total': len(SEARCH_INDEX),
    },
    'cms_philosophy': CMS_PHILOSOPHY,
    'ai_layer': {
        'title': 'Grounded AI',
        'principle': 'AI never invents knowledge',
        'sources': AI_LAYER,
        'status': 'partial',
        'current': 'Build #26 AI Knowledge Engine — architecture only, 14% readiness',
        'route': '/mission-control/ai-knowledge.html',
    },
    'apis': APIS,
    'file_architecture': {
        'title': 'Target Repository Structure',
        'status': 'planned',
        'directories': FILE_STRUCTURE,
        'current': 'Flat static site — repository blueprint defines migration path',
        'route': '/mission-control/repository.html',
    },
    'performance_standards': PERFORMANCE,
    'accessibility_standards': ACCESSIBILITY,
    'security': SECURITY,
    'analytics_philosophy': {
        'measure': ['Learning', 'Understanding', 'Participation'],
        'avoid': ['Clicks', 'Advertising', 'Engagement hacks'],
        'host': '/mission-control/visitor-journey.html',
    },
    'deployment_workflow': DEPLOYMENT_WORKFLOW,
    'environments': ENVIRONMENTS,
    'backup_strategy': BACKUP,
    'monitoring': MONITORING,
    'scalability': {
        'targets': [
            'Hundreds of thousands of pages',
            'Millions of relationships',
            'Thousands of educational assets',
            'Large research libraries',
            'Interactive laboratories',
            'Future civic education topics',
        ],
        'status': 'planned',
        'note': 'Architecture designed — static v1 not yet at scale',
    },
    'technical_documentation': {
        'required_per_subsystem': [
            'Architecture', 'Dependencies', 'Data model', 'Workflow',
            'API documentation', 'Deployment', 'Recovery', 'Maintenance schedule',
        ],
        'status': 'partial',
        'current': f'{len(mc.get("build_map", []))} MC dashboards + docs/ constitutions',
    },
    'mc_integration': {
        'title': 'Mission Control Technical Architecture Metrics',
        'status': 'partial',
        'metrics': MC_METRICS,
    },
    'related_blueprints': [
        {'title': 'Platform Architecture', 'route': '/data/platform-architecture.json', 'build': 20},
        {'title': 'Systems Integration', 'route': '/data/systems-integration.json', 'build': 45},
        {'title': 'Content Production Matrix', 'route': '/data/content-production-matrix.json', 'build': 46},
        {'title': 'AI Knowledge Engine', 'route': '/data/ai-knowledge-engine.json', 'build': 26},
    ],
    'summary': {
        'stack_layers_total': len(STACK),
        'stack_live': stack_live,
        'stack_partial': stack_partial,
        'stack_planned': stack_planned,
        'apis_total': len(APIS),
        'apis_partial_or_live': apis_live_partial,
        'search_index_types': len(SEARCH_INDEX),
        'search_live': False,
        'nextjs_migration': False,
        'neon_postgres_live': False,
        'prisma_live': False,
        'auth_live': False,
        'preview_deploys_live': True,
        'production_deploy_live': True,
        'github_connected': True,
        'monitoring_partial': sum(1 for m in MONITORING if m['status'] != 'planned'),
        'technical_architecture_readiness_pct': technical_architecture_readiness,
    },
    'catalog_gaps': [
        'Static HTML v1 — Next.js/React/TypeScript target not started',
        'No Neon PostgreSQL — all data in JSON files',
        'No Prisma ORM — schema blueprint only',
        'No authentication — admin routes unprotected',
        'No global search — 13 index types planned, 0 live',
        'No REST/GraphQL APIs — static JSON read by fetch()',
        'Mission Control publishing partial — no write workflow or approval gates',
        'Performance standards not measured — no Lighthouse CI',
        'Monitoring 1/9 partial — no error tracking, link checker, or DB health',
        'Component specifications still deferred — stack migration UI unmapped',
    ],
    'recommended_next_build': {
        'number': 51,
        'title': 'Component Specifications with Props/States',
        'note': 'Map stack status panels, deployment pipeline viz, environment badges, and monitoring widgets to COMP-* from Build #17.',
    },
}

path = root / 'data/technical-architecture.json'
with open(path, 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')
print(f'Technical Architecture: {stack_live}/{len(STACK)} stack live, {technical_architecture_readiness}% readiness')
