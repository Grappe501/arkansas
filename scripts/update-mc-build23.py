import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json') as f:
    mc = json.load(f)

title = 'Major Screen Wireframe Blueprint'

with open(root / 'data/wireframe-blueprint.json') as f:
    wf = json.load(f)

s = wf['summary']

mc['version'] = '1.27.0'
mc['build'] = 23
mc['updated'] = '2026-07-09'
mc['wireframe_blueprint'] = '/data/wireframe-blueprint.json'
mc['wireframes_dashboard'] = '/mission-control/wireframes.html'

mc['executive'] = {
    'overall_completion': 23,
    'current_build': {'number': 23, 'title': title},
    'active_phase': 'Implementation Artifacts — Wireframes',
    'last_completed': 'Database Schema & Entity Relationship Blueprint',
    'next_build': {'number': 24, 'title': 'Component specifications with props/states'},
    'github_status': 'connected',
    'netlify_status': 'production_healthy',
    'content_readiness': 18,
    'research_readiness': 20,
    'data_viz_readiness': 2,
    'signup_funnel_readiness': 16,
    'civic_action_readiness': 24,
    'coalition_readiness': 12,
    'data_model_readiness': 35,
    'route_inventory_readiness': 18,
    'component_registry_readiness': 22,
    'facts_framework_readiness': 12,
    'knowledge_atlas_readiness': 18,
    'platform_architecture_readiness': 20,
    'repository_structure_readiness': 28,
    'database_schema_readiness': 35,
    'wireframe_readiness': 38,
    'public_launch_readiness': 8,
    'public_launch_label': 'Early Foundation'
}

mc['wireframe_inventory'] = {
    'readiness_score': 38,
    'screens': s['screens'],
    'sections_total': s['sections_total'],
    'wireframe_readiness_pct': s['wireframe_readiness_pct'],
    'implementation_live': s['implementation_live'],
    'implementation_partial': s['implementation_partial'],
    'by_outcome': s['by_outcome']
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 23
        bar['note'] = f"Wireframe blueprint live — {s['screens']} screens, {s['sections_total']} sections. Component specs next."

if not any(b.get('id') == 'wireframes' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'wireframes',
        'label': 'Wireframe Blueprint',
        'value': 38,
        'max': 100,
        'note': f"{s['implementation_live']} live, {s['implementation_partial']} partial screens — section wireframes defined."
    })

mc['builds'].insert(0, {
    'number': 23,
    'title': title,
    'version': '1.27.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Screen Architecture v1.0 — 25 major screens before visual design and coding',
    'summary': f"{s['screens']} screens, {s['sections_total']} sections, 4 outcomes; {s['wireframe_readiness_pct']}% wireframe readiness.",
    'files_created': [
        'data/wireframe-blueprint.json', 'docs/WIREFRAME_BLUEPRINT.md',
        'builds/023-wireframe-blueprint.md', 'mission-control/wireframes.html',
        'scripts/gen-wireframe-blueprint.py', 'scripts/update-mc-build23.py'
    ],
    'files_modified': ['js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml'],
    'pages_created': ['/mission-control/wireframes.html'],
    'decisions_made': [
        '25 screens + confirmation template defined with sections',
        'Four outcomes: understand, evidence, participate, mission_control',
        'Honest implementation status per screen vs route registry',
        'Mobile requirements on every screen',
        'No Figma yet — structural wireframe blueprint only'
    ],
    'open_questions': ['Visual mockups in Build #24?', 'Dedicated deep lesson routes when?'],
    'risks': ['38% readiness — many screens planned/stub'],
    'next_recommended': 24,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/wireframes.html',
    'review_status': 'complete'
})

mc['briefing'] = {
    'what_built': f'Wireframe Blueprint v1.0 — {s["screens"]} screens with section-level architecture',
    'building_now': 'Implementation artifacts — component specs next (Build #24)',
    'blocked': ['No visual mockups', 'Admin screens not built', 'Confirmation template not standardized'],
    'ready_public': ['Wireframe MC dashboard', 'Screen-to-route mapping', 'Mobile requirements'],
    'next': 'Build #24 — Component specifications with props/states'
}

if not any(n.get('id') == 'wireframes' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'wireframes', 'label': 'Wireframe Blueprint', 'href': '/mission-control/wireframes.html', 'status': 'complete'
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
