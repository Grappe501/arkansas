import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json') as f:
    mc = json.load(f)

title = 'Arkansas Citizens United Platform Master Data Model & Relationship Architecture'

mc['version'] = '1.19.0'
mc['build'] = 15
mc['updated'] = '2026-07-09'
mc['canonical_data_model'] = '/data/canonical-data-model.json'
mc['relationship_registry'] = '/data/relationship-registry.json'
mc['data_model_route'] = '/mission-control/data-model.html'

mc['executive'] = {
    'overall_completion': 15,
    'current_build': {'number': 15, 'title': title},
    'active_phase': 'Canonical Data Model',
    'last_completed': 'Arkansas Citizens United Coalition Operating System (ACUCOS)',
    'next_build': {'number': 16, 'title': 'Complete page inventory (every screen and route)'},
    'github_status': 'connected',
    'netlify_status': 'production_healthy',
    'content_readiness': 10,
    'research_readiness': 18,
    'data_viz_readiness': 2,
    'signup_funnel_readiness': 14,
    'civic_action_readiness': 22,
    'coalition_readiness': 12,
    'data_model_readiness': 8,
    'public_launch_readiness': 5,
    'public_launch_label': 'Early Foundation'
}

mc['relationship_health'] = {
    'readiness_score': 8,
    'people_connected': 0,
    'organizations_connected': 0,
    'counties_active': 0,
    'events_hosted': 0,
    'resources_shared': 0,
    'community_conversations': 0,
    'research_objects': 14,
    'model_laws': 0,
    'initiative_concepts': 0,
    'packets_shared': 0,
    'edges_recorded': 0
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 15
        bar['note'] = 'Canonical data model live. Pivot to concrete product: page inventory (Build #16).'
    if bar['id'] == 'coalition':
        bar['note'] = 'ACUCOS objects now linked in canonical Person/Organization/County model.'

if not any(b.get('id') == 'data_model' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'data_model',
        'label': 'Canonical Data Model',
        'value': 8,
        'max': 100,
        'note': '10 objects, 20 relationship types, 0 edges — schema ready for Build #18 database.'
    })

mc['builds'].insert(0, {
    'number': 15,
    'title': title,
    'version': '1.19.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Canonical Data Constitution v1.0 — everything connected',
    'summary': '10 canonical objects, 20 relationship types, geographic/timeline/search intelligence, AI-ready schema, MC relationship health dashboard.',
    'files_created': [
        'data/canonical-data-model.json', 'data/relationship-registry.json',
        'docs/CANONICAL_DATA_CONSTITUTION.md', 'builds/015-canonical-data-model.md',
        'mission-control/data-model.html', 'scripts/update-mc-build15.py'
    ],
    'files_modified': ['js/mission-control.js', 'data/site-architecture.json', 'BUILD_PLAN.md'],
    'pages_created': ['/mission-control/data-model.html'],
    'decisions_made': [
        'Single interconnected ecosystem — not isolated signup/content/coalition systems',
        'Relationship growth as major success indicator',
        'Pivot Builds #16–#20 to concrete product design (pages, components, DB, wireframes, deploy)'
    ],
    'open_questions': ['Supabase/Postgres for edges table?', 'Graph visualization in MC?'],
    'risks': ['0 relationship edges until backend — honest scaffolding'],
    'next_recommended': 16,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/data-model.html',
    'review_status': 'complete'
})

mc['briefing'] = {
    'what_built': 'Canonical Data Constitution — 10 objects, 20 relationships, everything connected',
    'building_now': 'Planning complete for core architecture — pivot to page inventory (Build #16)',
    'blocked': ['Relationship edge storage', 'Search intelligence backend', 'AI layer'],
    'ready_public': ['Data model MC dashboard', 'Relationship registry schema', 'Platform integration map'],
    'next': 'Build #16 — Complete page inventory (every screen and route)'
}

if not any(n.get('id') == 'data_model' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'data_model', 'label': 'Data Model', 'href': '/mission-control/data-model.html', 'status': 'complete'
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
