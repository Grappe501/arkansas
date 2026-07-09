import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json') as f:
    mc = json.load(f)

title = 'Component Architecture & Design System Inventory'

with open(root / 'data/component-registry.json') as f:
    cr = json.load(f)
with open(root / 'data/brand-identity.json') as f:
    brand = json.load(f)

s = cr['summary']

mc['version'] = '1.21.0'
mc['build'] = 17
mc['updated'] = '2026-07-09'
mc['component_registry'] = '/data/component-registry.json'
mc['components_dashboard'] = '/mission-control/components.html'
mc['brand_identity'] = '/data/brand-identity.json'

mc['executive'] = {
    'overall_completion': 17,
    'current_build': {'number': 17, 'title': title},
    'active_phase': 'Product Design — Component Registry',
    'last_completed': 'Complete Page & Route Inventory',
    'next_build': {'number': 18, 'title': 'Brand & Identity System (logo, color, typography, voice, messaging)'},
    'github_status': 'connected',
    'netlify_status': 'production_healthy',
    'content_readiness': 12,
    'research_readiness': 18,
    'data_viz_readiness': 2,
    'signup_funnel_readiness': 14,
    'civic_action_readiness': 22,
    'coalition_readiness': 12,
    'data_model_readiness': 8,
    'route_inventory_readiness': 18,
    'component_registry_readiness': 22,
    'public_launch_readiness': 6,
    'public_launch_label': 'Early Foundation'
}

mc['component_inventory'] = {
    'readiness_score': 22,
    'total_components': s['total_components'],
    'categories': s['categories'],
    'live': s['live'],
    'partial': s['partial'],
    'stub': s['stub'],
    'planned': s['planned'],
    'design_system_linked': s['design_system_linked'],
    'organization': brand['organization']['name'],
    'platform': brand['platform']['name']
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 17
        bar['note'] = f"Component registry live — {s['total_components']} components (A–G). Brand & Identity System next."

if not any(b.get('id') == 'components' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'components',
        'label': 'Component Registry',
        'value': 22,
        'max': 100,
        'note': f"{s['live']} live, {s['partial']} partial, {s['stub']} stub, {s['planned']} planned — honest inventory."
    })

mc['builds'].insert(0, {
    'number': 17,
    'title': title,
    'version': '1.21.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Master Component Registry v1.0 — 42 reusable building blocks + ACEI brand separation',
    'summary': f"{s['total_components']} components across 7 categories; ACEI org identity; Citizens United as subject not brand; MC dashboard.",
    'files_created': [
        'data/component-registry.json', 'data/brand-identity.json',
        'docs/COMPONENT_REGISTRY.md', 'builds/017-component-architecture.md',
        'mission-control/components.html', 'scripts/gen-component-registry.py',
        'scripts/update-mc-build17.py'
    ],
    'files_modified': [
        'js/mission-control.js', 'js/layout.js', 'coalition/index.html',
        'arkansas/index.html', 'data/coalition-ecosystem.json', 'data/site.json',
        'BUILD_PLAN.md', 'netlify.toml'
    ],
    'pages_created': ['/mission-control/components.html'],
    'decisions_made': [
        'Organization: Arkansas Civic Education Initiative (ACEI)',
        'Platform subject: The Citizens United Education Platform',
        'ACUCOS renamed to ACEI Coalition System (legacy noted)',
        'Build #18 recommended: Brand & Identity System before UI design'
    ],
    'open_questions': ['Keep public site name Citizens Facts?', 'Full county map vs table?'],
    'risks': ['6 stub + 3 planned components — documented honestly'],
    'next_recommended': 18,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/components.html',
    'review_status': 'complete'
})

mc['briefing'] = {
    'what_built': f'Component Registry v1.0 — {s["total_components"]} components + ACEI branding',
    'building_now': 'Product design phase — Brand & Identity System next (Build #18)',
    'blocked': ['Stub/planned components need implementation', 'Brand system not yet defined'],
    'ready_public': ['Component MC dashboard', 'Brand identity JSON', 'ACEI coalition rebrand on hub pages'],
    'next': 'Build #18 — Brand & Identity System'
}

if not any(n.get('id') == 'components' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'components', 'label': 'Component Registry', 'href': '/mission-control/components.html', 'status': 'complete'
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
