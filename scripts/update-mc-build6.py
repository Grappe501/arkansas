import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json') as f:
    mc = json.load(f)
with open(root / 'data/content-inventory.json') as f:
    inv = json.load(f)
s = inv['summary']

mc['version'] = '1.10.0'
mc['build'] = 6
mc['updated'] = '2026-07-09'
mc['content_inventory'] = '/data/content-inventory.json'
mc['content_inventory_route'] = '/mission-control/inventory.html'

mc['executive'] = {
    'overall_completion': 6,
    'current_build': {'number': 6, 'title': 'Master Content Inventory'},
    'active_phase': 'Information Architecture',
    'last_completed': 'Master Site Architecture',
    'next_build': {'number': 7, 'title': 'First Deep Content — Hall Priority'},
    'github_status': 'connected',
    'netlify_status': 'production_healthy',
    'content_readiness': 8,
    'research_readiness': 3,
    'data_viz_readiness': 0,
    'signup_funnel_readiness': 5,
    'civic_action_readiness': 6,
    'public_launch_readiness': 2,
    'public_launch_label': 'Early Foundation'
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 6
        bar['note'] = 'Planning blueprints complete (phases, IA, content inventory). Published educational content remains early.'
    if bar['id'] == 'content':
        bar['value'] = 12
        bar['note'] = (
            f"Content Master Registry: {s['registered_items']} items with stable IDs. "
            f"{s['published']} published, {s['planned']} planned. V1 target ~{s['v1_target_total']}."
        )

mc['builds'].insert(0, {
    'number': 6,
    'title': 'Master Content Inventory',
    'version': '1.10.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Bill of materials for every educational asset — page-level tracking from day one',
    'summary': (
        f"Content Master Registry v1.0: {s['registered_items']} items with stable IDs. "
        '10 domains, cross-domain assets, 13-step lifecycle.'
    ),
    'files_created': [
        'data/content-inventory.json', 'docs/CONTENT_INVENTORY.md',
        'builds/006-master-content-inventory.md', 'mission-control/inventory.html',
        'scripts/gen-content-inventory.py'
    ],
    'files_modified': ['data/mission-control.json', 'js/mission-control.js', 'css/mission-control.css'],
    'pages_created': ['/mission-control/inventory.html'],
    'decisions_made': [
        'Stable ID standard (DOMAIN-NNN)',
        'Nothing created without registry entry',
        'L2-L4 depth slots pre-registered per subsection'
    ],
    'open_questions': [
        'Which subsection gets first L2 draft in Build #7?',
        'Timeline vs glossary priority for cross-domain?'
    ],
    'risks': ['351 registered of ~2700 v1 targets — discipline needed to expand registry as content grows'],
    'next_recommended': 7,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/inventory.html',
    'review_status': 'complete'
})

mc['briefing'] = {
    'what_built': 'Phase Registry, Site Architecture, Content Inventory with 351 stable IDs',
    'building_now': 'Registry tracking — most items planned; MT/HI and homepage partial live',
    'blocked': ['Participant backend', 'Spending charts', 'Search/glossary pages'],
    'ready_public': ['Home L1', 'Site map', 'Montana/Hawaii', 'Mission Control', 'Content inventory dashboard'],
    'next': 'Build #7 — First Deep Content (priority L2 articles)'
}

if not any(n.get('id') == 'inventory' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'inventory', 'label': 'Content Inventory',
        'href': '/mission-control/inventory.html', 'status': 'complete'
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
