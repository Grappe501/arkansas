"""
Generate data/platform-architecture.json — Build #20 Master Platform Blueprint v1.0.
Honest status for each architectural layer against current repo state.
"""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
today = '2026-07-09'

def layer(lid, title, purpose, status, requirements=None, current=None, future=None, route=None):
    return {
        'id': lid,
        'title': title,
        'purpose': purpose,
        'status': status,
        'requirements': requirements or [],
        'current_implementation': current,
        'future': future,
        'route': route
    }

stack = [
    layer('SRC', 'Source Control — GitHub', 'Version control, branches, PRs, issues, docs',
          'live', ['Version control', 'Branch management', 'Pull requests', 'Issue tracking'],
          'https://github.com/Grappe501/arkansas — main branch, numbered builds'),
    layer('DEPLOY', 'Deployment — Netlify', 'CI/CD, SSL, CDN, forms',
          'live', ['Continuous deployment', 'Deploy previews', 'SSL', 'CDN', 'Form handling'],
          'https://arkansas-facts.netlify.app — static publish, Netlify Forms on educate/'),
    layer('FE', 'Frontend', 'User-facing application layer',
          'partial', ['Static-first rendering', 'Responsive', 'Accessible', 'Progressive enhancement', 'SEO'],
          'Static HTML/CSS/JS — no framework yet; 81 routes inventoried',
          'Component-based framework TBD (Build #24 specs)'),
    layer('STYLE', 'Styling — Design System', 'Centralized visual language',
          'partial', ['Reusable components', 'Mobile-first', 'Accessible', 'Dark/light ready', 'Print-friendly'],
          'Build #9 design-system.json, 14 ds-* components, /design-system/ showcase',
          route='/mission-control/design.html'),
    layer('SEARCH', 'Search', 'Content discovery',
          'planned', ['v1 client-side', 'Future full index'],
          'No client-side search UI yet',
          'Indexed search: articles, cases, timeline, research, glossary, coalition'),
]

objectives = [
    {'id': 'OBJ-1', 'title': "Arkansas's definitive Citizens United educational resource", 'status': 'partial', 'readiness_pct': 18},
    {'id': 'OBJ-2', 'title': 'Develop informed community educators', 'status': 'partial', 'readiness_pct': 22},
    {'id': 'OBJ-3', 'title': 'Statewide coalition of civic education organizations', 'status': 'partial', 'readiness_pct': 12},
    {'id': 'OBJ-4', 'title': 'Transparent research with primary sources', 'status': 'partial', 'readiness_pct': 20},
    {'id': 'OBJ-5', 'title': 'Sustainable expanding educational institution', 'status': 'partial', 'readiness_pct': 19},
]

content_architecture = {
    'page_metadata': ['mrid', 'page_id', 'version', 'status', 'review_state', 'citation_completeness', 'educational_readiness'],
    'trackers': [
        {'system': 'Content Inventory', 'build': 6, 'route': '/mission-control/inventory.html'},
        {'system': 'MRID Registry', 'build': 7, 'route': '/mission-control/mrid.html'},
        {'system': 'Route Registry', 'build': 16, 'route': '/mission-control/routes.html'},
        {'system': 'Facts Framework', 'build': 18, 'route': '/mission-control/facts.html'},
        {'system': 'Knowledge Atlas', 'build': 19, 'route': '/mission-control/atlas.html'},
    ],
    'status': 'live'
}

data_architecture = {
    'canonical_objects': [
        'person', 'organization', 'county', 'event', 'educational_resource',
        'research_object', 'public_official', 'model_law', 'ballot_initiative_concept', 'topic'
    ],
    'relationship_types': 20,
    'registry': '/data/canonical-data-model.json',
    'database': {'status': 'planned', 'build': 22, 'note': 'Schema not yet implemented — JSON files v0'},
    'status': 'partial'
}

mission_control_systems = [
    {'id': 'content', 'label': 'Content progress', 'route': '/mission-control/inventory.html', 'status': 'live'},
    {'id': 'research', 'label': 'Research progress', 'route': '/mission-control/research.html', 'status': 'live'},
    {'id': 'coalition', 'label': 'Coalition growth', 'route': '/mission-control/coalition.html', 'status': 'live'},
    {'id': 'education', 'label': 'Educational readiness', 'route': '/mission-control/atlas.html', 'status': 'live'},
    {'id': 'deployment', 'label': 'Deployment health', 'route': '/mission-control/', 'status': 'partial'},
    {'id': 'forms', 'label': 'Form activity', 'route': '/educate/', 'status': 'partial'},
    {'id': 'county', 'label': 'County participation', 'route': '/mission-control/civic-ecosystem.html', 'status': 'live'},
    {'id': 'sources', 'label': 'Source completeness', 'route': '/mission-control/research.html', 'status': 'live'},
]

platform_modules = [
    {
        'id': 'coalition',
        'title': 'Coalition Platform',
        'capabilities': [
            {'cap': 'Create profiles', 'status': 'stub'},
            {'cap': 'Join coalition', 'status': 'live'},
            {'cap': 'Download resources', 'status': 'partial'},
            {'cap': 'Register events', 'status': 'stub'},
            {'cap': 'Request speakers', 'status': 'planned'},
            {'cap': 'Submit educational materials', 'status': 'planned'},
        ],
        'route': '/coalition/'
    },
    {
        'id': 'contact_network',
        'title': 'Contact Network',
        'capabilities': [
            {'cap': 'Create profiles', 'status': 'partial'},
            {'cap': 'Save progress', 'status': 'live'},
            {'cap': 'Download resources', 'status': 'partial'},
            {'cap': 'Join newsletters', 'status': 'partial'},
            {'cap': 'Become education leaders', 'status': 'live'},
            {'cap': 'Join county teams', 'status': 'partial'},
        ],
        'route': '/educate/'
    },
    {
        'id': 'relational_organizing',
        'title': 'Relational Organizing',
        'capabilities': [
            {'cap': 'Invite family and friends', 'status': 'live'},
            {'cap': 'Share educational pages', 'status': 'live'},
            {'cap': 'Recommend resources', 'status': 'partial'},
            {'cap': 'Host conversations', 'status': 'live'},
            {'cap': 'Introduce organizations', 'status': 'partial'},
        ],
        'route': '/action/'
    },
    {
        'id': 'solutions_center',
        'title': 'Solutions Center',
        'capabilities': [
            {'cap': 'Federal legislative concepts', 'status': 'partial'},
            {'cap': 'Arkansas legislative concepts', 'status': 'planned'},
            {'cap': 'Model law workspace', 'status': 'stub'},
            {'cap': 'Ballot initiative lab', 'status': 'stub'},
            {'cap': 'Share with U.S. Representatives', 'status': 'planned'},
            {'cap': 'Share with U.S. Senators', 'status': 'planned'},
            {'cap': 'Share with Arkansas General Assembly', 'status': 'planned'},
        ],
        'route': '/solutions/'
    },
]

security = [
    {'req': 'HTTPS everywhere', 'status': 'live', 'note': 'Netlify SSL'},
    {'req': 'Secure environment variables', 'status': 'planned', 'note': 'No secrets in repo'},
    {'req': 'Spam protection', 'status': 'partial', 'note': 'Netlify Forms honeypot'},
    {'req': 'Form validation', 'status': 'partial'},
    {'req': 'Role-based administration', 'status': 'planned'},
    {'req': 'Audit logging', 'status': 'planned'},
    {'req': 'Regular dependency updates', 'status': 'partial', 'note': 'Minimal npm deps'},
]

performance = [
    {'std': 'Fast page loads', 'status': 'live', 'note': 'Static site'},
    {'std': 'Mobile optimization', 'status': 'partial'},
    {'std': 'Efficient images', 'status': 'partial'},
    {'std': 'Lazy loading', 'status': 'planned'},
    {'std': 'Search engine optimization', 'status': 'partial'},
    {'std': 'Accessible navigation', 'status': 'partial'},
]

workflow = [
    {'stage': 1, 'title': 'Master Build Plan', 'status': 'live'},
    {'stage': 2, 'title': 'Architecture', 'status': 'live'},
    {'stage': 3, 'title': 'Research', 'status': 'live'},
    {'stage': 4, 'title': 'Content', 'status': 'partial'},
    {'stage': 5, 'title': 'Components', 'status': 'partial'},
    {'stage': 6, 'title': 'Development', 'status': 'planned'},
    {'stage': 7, 'title': 'Testing', 'status': 'planned'},
    {'stage': 8, 'title': 'Review', 'status': 'partial'},
    {'stage': 9, 'title': 'Deployment', 'status': 'live'},
    {'stage': 10, 'title': 'Continuous Improvement', 'status': 'live'},
]

v1_success = [
    {'criterion': 'Educational core complete', 'status': 'partial', 'pct': 40},
    {'criterion': 'Research transparent', 'status': 'partial', 'pct': 20},
    {'criterion': 'Mission Control operational', 'status': 'live', 'pct': 95},
    {'criterion': 'Coalition onboarding functional', 'status': 'partial', 'pct': 35},
    {'criterion': 'Community education resources available', 'status': 'partial', 'pct': 45},
    {'criterion': 'Contact Network active', 'status': 'partial', 'pct': 30},
    {'criterion': 'Organizations can join coalition', 'status': 'live', 'pct': 70},
    {'criterion': 'Share materials with Arkansas public officials', 'status': 'planned', 'pct': 5},
    {'criterion': 'GitHub and Netlify reliable', 'status': 'live', 'pct': 90},
]

implementation_roadmap = [
    {'build': 21, 'title': 'Repository & folder structure', 'status': 'planned'},
    {'build': 22, 'title': 'Database schema and entity-relationship model', 'status': 'planned'},
    {'build': 23, 'title': 'Wireframes for every major screen', 'status': 'planned'},
    {'build': 24, 'title': 'Component specifications with props/states', 'status': 'planned'},
    {'build': 25, 'title': 'GitHub issues, milestones, and sprint roadmap', 'status': 'planned'},
]

scalability = [
    'Additional educational topics',
    'Expanded Arkansas civic education resources',
    'AI-assisted educational search',
    'Interactive learning experiences',
    'Advanced coalition management',
    'Enhanced analytics',
]

live_stack = sum(1 for s in stack if s['status'] == 'live')
partial_stack = sum(1 for s in stack if s['status'] == 'partial')
v1_avg = round(sum(c['pct'] for c in v1_success) / len(v1_success))
obj_avg = round(sum(o['readiness_pct'] for o in objectives) / len(objectives))

out = {
    'version': '1.0',
    'build': 20,
    'updated': today,
    'title': 'Master Platform Blueprint & Technical Architecture v1.0',
    'organization': 'Arkansas Civic Education Initiative',
    'organization_note': 'Working title until branding finalized (Build deferred)',
    'platform': 'Citizens United Education Platform',
    'route': '/mission-control/platform.html',
    'constitution': '/docs/PLATFORM_ARCHITECTURE.md',
    'philosophy': 'Build once. Expand forever.',
    'technical_philosophy': ['speed', 'simplicity', 'reliability', 'accessibility', 'transparency', 'searchability', 'scalability'],
    'governing_principle': 'Built with enterprise discipline, academic credibility, museum clarity, and library accessibility.',
    'objectives': objectives,
    'technology_stack': stack,
    'content_architecture': content_architecture,
    'data_architecture': data_architecture,
    'mission_control_systems': mission_control_systems,
    'platform_modules': platform_modules,
    'security_principles': security,
    'performance_standards': performance,
    'development_workflow': workflow,
    'v1_success_criteria': v1_success,
    'scalability_targets': scalability,
    'implementation_roadmap': implementation_roadmap,
    'integrations': [
        {'system': 'Site Architecture', 'build': 5, 'route': '/mission-control/architecture.html', 'note': 'Information architecture (IA)'},
        {'system': 'Canonical Data Model', 'build': 15, 'route': '/mission-control/data-model.html'},
        {'system': 'Component Registry', 'build': 17, 'route': '/mission-control/components.html'},
        {'system': 'Facts Framework', 'build': 18, 'route': '/mission-control/facts.html'},
        {'system': 'Knowledge Atlas', 'build': 19, 'route': '/mission-control/atlas.html'},
    ],
    'summary': {
        'stack_layers': len(stack),
        'stack_live': live_stack,
        'stack_partial': partial_stack,
        'stack_planned': sum(1 for s in stack if s['status'] == 'planned'),
        'objectives_avg_readiness': obj_avg,
        'v1_success_avg_pct': v1_avg,
        'mc_systems_live': sum(1 for m in mission_control_systems if m['status'] == 'live'),
        'implementation_builds_planned': len(implementation_roadmap),
        'architecture_readiness_pct': round((live_stack * 100 + partial_stack * 50) / (len(stack) * 100) * 100),
    },
    'catalog_gaps': [
        'Frontend framework not selected',
        'Database schema deferred to Build #22',
        'Client-side search not implemented',
        'Public official sharing automation planned',
        'Role-based admin and audit logging planned',
        'Brand & Identity System deferred — working titles in use',
    ],
    'recommended_next_build': {
        'number': 21,
        'title': 'Repository & Folder Structure',
        'note': 'Implementation artifacts wave — folder layout before production code.'
    },
}

path = root / 'data/platform-architecture.json'
with open(path, 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')
print(f'Platform architecture: {out["summary"]["architecture_readiness_pct"]}% readiness, v1 success {v1_avg}%')
