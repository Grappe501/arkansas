import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json') as f:
    mc = json.load(f)
with open(root / 'data/mrid-registry.json') as f:
    mrid = json.load(f)
s = mrid['summary']

mc['version'] = '1.11.0'
mc['build'] = 7
mc['updated'] = '2026-07-09'
mc['mrid_registry'] = '/data/mrid-registry.json'
mc['mrid_route'] = '/mission-control/mrid.html'

mc['executive'] = {
    'overall_completion': 7,
    'current_build': {'number': 7, 'title': 'Master Requirement ID System'},
    'active_phase': 'Foundation & Governance',
    'last_completed': 'Master Content Inventory',
    'next_build': {'number': 8, 'title': 'First Deep Content — Priority MRIDs'},
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
        bar['value'] = 7
        bar['note'] = 'Four planning registries complete (phases, IA, content, MRID). Traceability framework live. Educational content remains early.'
    if bar['id'] == 'build_plan':
        bar['value'] = 28
        bar['note'] = 'MRID system links requirements to phases, content, builds, and deployments.'

mc['builds'].insert(0, {
    'number': 7,
    'title': 'Master Requirement ID System & Traceability Framework',
    'version': '1.11.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Permanent MRIDs for every platform component — Mission Control central nervous system',
    'summary': f"MRID v1.0: {s['total_requirements']} requirements, 16 domains, traceability matrix, dependency lookup. {s['content_items_linked']} content items cross-linked.",
    'files_created': [
        'data/mrid-registry.json', 'docs/MRID_SYSTEM.md',
        'builds/007-master-requirement-id.md', 'mission-control/mrid.html',
        'scripts/gen-mrid-registry.py'
    ],
    'files_modified': [
        'data/content-inventory.json', 'data/mission-control.json',
        'js/mission-control.js', 'css/mission-control.css'
    ],
    'pages_created': ['/mission-control/mrid.html'],
    'decisions_made': [
        '16 domain codes (GOV, NAV, HOME, CASE, etc.)',
        'Content inventory IDs map to MRIDs — dual registry',
        '12-step requirement lifecycle distinct from content status'
    ],
    'open_questions': ['Display MRIDs on public pages in Build #8?', 'GitHub commit auto-link to MRIDs?'],
    'risks': ['165 MRIDs of growing universe — regenerate discipline required'],
    'next_recommended': 8,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/mrid.html',
    'review_status': 'complete'
})

mc['briefing'] = {
    'what_built': 'Phase Registry, Site Architecture, Content Inventory, MRID traceability (165 requirements)',
    'building_now': 'Registry infrastructure complete — ready for first deep content against MRIDs',
    'blocked': ['Participant backend', 'Spending charts', 'Search/glossary'],
    'ready_public': ['Mission Control', 'MRID dashboard', 'Site map', 'Montana/Hawaii'],
    'next': 'Build #8 — First Deep Content (HIST-002, CASE-002 priority)'
}

if not any(n.get('id') == 'mrid' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'mrid', 'label': 'MRID System',
        'href': '/mission-control/mrid.html', 'status': 'complete'
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
