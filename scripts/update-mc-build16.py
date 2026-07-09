import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json') as f:
    mc = json.load(f)

title = 'Complete Page & Route Inventory'

mc['version'] = '1.20.0'
mc['build'] = 16
mc['updated'] = '2026-07-09'
mc['route_registry'] = '/data/route-registry.json'
mc['routes_dashboard'] = '/mission-control/routes.html'

mc['executive'] = {
    'overall_completion': 16,
    'current_build': {'number': 16, 'title': title},
    'active_phase': 'Product Design — Route Inventory',
    'last_completed': 'Master Data Model & Relationship Architecture',
    'next_build': {'number': 17, 'title': 'Component inventory (cards, timelines, Action Hub, dashboards, forms)'},
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
    'public_launch_readiness': 6,
    'public_launch_label': 'Early Foundation'
}

with open(root / 'data/route-registry.json') as f:
    rr = json.load(f)

mc['route_inventory'] = {
    'readiness_score': 18,
    'total_routes': rr['summary']['total_routes'],
    'live': rr['summary']['live'],
    'redirect': rr['summary']['redirect'],
    'stub': rr['summary']['stub'],
    'planned': rr['summary']['planned'],
    'must_launch': rr['summary']['must_launch'],
    'action_hub_links': len(rr['action_hub_links'])
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 16
        bar['note'] = f"Route registry live — {rr['summary']['total_routes']} routes inventoried. Component inventory next."

if not any(b.get('id') == 'routes' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'routes',
        'label': 'Route Inventory',
        'value': 18,
        'max': 100,
        'note': f"{rr['summary']['live']} live, {rr['summary']['redirect']} redirect, {rr['summary']['planned']} planned — honest v1 map."
    })

mc['builds'].insert(0, {
    'number': 16,
    'title': title,
    'version': '1.20.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Route Registry v1.0 — every screen and canonical path for Arkansas v1',
    'summary': f"{rr['summary']['total_routes']} routes, 9 groups, Action Hub links, launch priorities, hub pages, netlify redirects.",
    'files_created': [
        'data/route-registry.json', 'docs/ROUTE_REGISTRY.md',
        'builds/016-page-route-inventory.md', 'mission-control/routes.html',
        'start-here/index.html', 'arkansas/index.html', 'join/index.html',
        'scripts/gen-route-registry.py', 'scripts/update-mc-build16.py'
    ],
    'files_modified': ['netlify.toml', 'js/mission-control.js', 'BUILD_PLAN.md'],
    'pages_created': ['/mission-control/routes.html', '/start-here/', '/arkansas/', '/join/'],
    'decisions_made': [
        'Canonical paths redirect to current destinations until dedicated pages ship',
        'Honest status: live / redirect / stub / planned per route',
        'Pivot continues: Build #17 component inventory'
    ],
    'open_questions': ['Dedicated pages for deep-dive routes?', 'Glossary and FAQ routes?'],
    'risks': ['22 planned routes — not hidden, documented'],
    'next_recommended': 17,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/routes.html',
    'review_status': 'complete'
})

mc['briefing'] = {
    'what_built': 'Route Registry v1.0 — 81 routes inventoried with honest status',
    'building_now': 'Product design phase — component inventory next (Build #17)',
    'blocked': ['22 planned routes need content', 'Admin dashboards'],
    'ready_public': ['Route MC dashboard', 'Start Here', 'Arkansas hub', 'Join hub', 'Canonical redirects'],
    'next': 'Build #17 — Component inventory'
}

if not any(n.get('id') == 'routes' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'routes', 'label': 'Route Registry', 'href': '/mission-control/routes.html', 'status': 'complete'
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
