import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json') as f:
    mc = json.load(f)

title = 'Citizens United Knowledge Atlas & Learning Path System'

with open(root / 'data/knowledge-atlas.json') as f:
    atlas = json.load(f)

s = atlas['summary']
ec = atlas['educational_completion']

mc['version'] = '1.23.0'
mc['build'] = 19
mc['updated'] = '2026-07-09'
mc['knowledge_atlas'] = '/data/knowledge-atlas.json'
mc['atlas_dashboard'] = '/mission-control/atlas.html'

mc['executive'] = {
    'overall_completion': 19,
    'current_build': {'number': 19, 'title': title},
    'active_phase': 'Educational Architecture — Knowledge Atlas',
    'last_completed': 'Citizens United Facts Framework',
    'next_build': {'number': 20, 'title': 'Brand & Identity System (logo, color, typography, voice, messaging)'},
    'github_status': 'connected',
    'netlify_status': 'production_healthy',
    'content_readiness': 16,
    'research_readiness': 20,
    'data_viz_readiness': 2,
    'signup_funnel_readiness': 14,
    'civic_action_readiness': 22,
    'coalition_readiness': 12,
    'data_model_readiness': 8,
    'route_inventory_readiness': 18,
    'component_registry_readiness': 22,
    'facts_framework_readiness': 12,
    'knowledge_atlas_readiness': 18,
    'public_launch_readiness': 7,
    'public_launch_label': 'Early Foundation'
}

mc['atlas_inventory'] = {
    'readiness_score': 18,
    'worlds': s['worlds'],
    'districts': s['districts'],
    'districts_live': s['districts_live'],
    'districts_partial': s['districts_partial'],
    'districts_planned': s['districts_planned'],
    'districts_stub': s['districts_stub'],
    'trails': s['trails'],
    'mapped_routes': s['mapped_routes'],
    'atlas_completion_pct': s['atlas_completion_pct'],
    'educational_readiness': ec['overall_educational_readiness'],
    'learning_compass_status': atlas['learning_compass']['status']
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 19
        bar['note'] = f"Knowledge Atlas live — {s['worlds']} worlds, {s['districts']} districts, {ec['overall_educational_readiness']}% educational readiness."

if not any(b.get('id') == 'atlas' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'atlas',
        'label': 'Knowledge Atlas',
        'value': 18,
        'max': 100,
        'note': f"{s['districts_live']} live, {s['districts_partial']} partial districts — 6 knowledge trails defined."
    })

mc['builds'].insert(0, {
    'number': 19,
    'title': title,
    'version': '1.23.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Educational Architecture v1.0 — seven learning worlds, districts, trails, Learning Compass',
    'summary': f"{s['worlds']} worlds, {s['districts']} districts, {s['trails']} trails; {ec['overall_educational_readiness']}% educational readiness; honest route mapping.",
    'files_created': [
        'data/knowledge-atlas.json', 'docs/KNOWLEDGE_ATLAS.md',
        'builds/019-knowledge-atlas.md', 'mission-control/atlas.html',
        'scripts/gen-knowledge-atlas.py', 'scripts/update-mc-build19.py'
    ],
    'files_modified': [
        'js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml'
    ],
    'pages_created': ['/mission-control/atlas.html'],
    'decisions_made': [
        'Seven Learning Worlds replace menu-first navigation mental model',
        '51 districts mapped to honest live/partial/stub/planned status',
        'Six Knowledge Trails including Beginner (20–30 min)',
        'Learning Compass schema tied to COMP-NAV-004',
        'Educational completion measured by dimension, not page count'
    ],
    'open_questions': ['Interactive atlas visualization?', 'Deploy Learning Compass on all halls?'],
    'risks': [f"{s['districts_planned'] + s['districts_stub']} districts not yet built — documented"],
    'next_recommended': 20,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/atlas.html',
    'review_status': 'complete'
})

mc['briefing'] = {
    'what_built': f'Knowledge Atlas v1.0 — {s["worlds"]} worlds, {s["districts"]} districts, {s["trails"]} trails',
    'building_now': 'Educational architecture — Brand & Identity System next (Build #20)',
    'blocked': ['Learning Compass UI not on public pages', '34+ districts need content'],
    'ready_public': ['Atlas MC dashboard', 'Knowledge trails', 'Educational completion metrics'],
    'next': 'Build #20 — Brand & Identity System'
}

if not any(n.get('id') == 'atlas' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'atlas', 'label': 'Knowledge Atlas', 'href': '/mission-control/atlas.html', 'status': 'complete'
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
