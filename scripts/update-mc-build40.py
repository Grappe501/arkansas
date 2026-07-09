import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json') as f:
    mc = json.load(f)

title = 'Citizens United Facts Master Knowledge Graph & Civic Intelligence Engine'

with open(root / 'data/civic-intelligence.json') as f:
    ci = json.load(f)

s = ci['summary']

mc['version'] = '1.44.0'
mc['build'] = 40
mc['updated'] = '2026-07-09'
mc['civic_intelligence'] = '/data/civic-intelligence.json'
mc['civic_intelligence_dashboard'] = '/mission-control/civic-intelligence.html'

mc['executive'] = {
    'overall_completion': 40,
    'current_build': {'number': 40, 'title': title},
    'active_phase': 'Institutional Brain — Master Knowledge Graph & Civic Intelligence',
    'last_completed': 'Documentary Experience & Media Studio',
    'next_build': {'number': 41, 'title': 'Component specifications with props/states'},
    'github_status': 'connected',
    'netlify_status': 'production_healthy',
    'content_readiness': 26,
    'research_readiness': 28,
    'data_viz_readiness': 6,
    'signup_funnel_readiness': 22,
    'civic_action_readiness': 32,
    'coalition_readiness': 18,
    'data_model_readiness': 38,
    'route_inventory_readiness': 18,
    'component_registry_readiness': 22,
    'facts_framework_readiness': 14,
    'knowledge_atlas_readiness': 20,
    'platform_architecture_readiness': 20,
    'repository_structure_readiness': 28,
    'database_schema_readiness': 36,
    'wireframe_readiness': 38,
    'contact_intelligence_readiness': 31,
    'mc2_readiness': 33,
    'ai_engine_readiness': 14,
    'content_factory_readiness': 28,
    'education_academy_readiness': 26,
    'observatory_readiness': 20,
    'outreach_readiness': 22,
    'county_os_readiness': 28,
    'campaign_os_readiness': 34,
    'encyclopedia_readiness': 19,
    'narrative_readiness': 24,
    'curriculum_readiness': 26,
    'trust_readiness': 24,
    'library_readiness': 22,
    'learning_lab_readiness': 22,
    'media_studio_readiness': 18,
    'civic_intelligence_readiness': s['civic_intelligence_readiness_pct'],
    'public_launch_readiness': 8,
    'public_launch_label': 'Early Foundation'
}

mc['civic_intelligence_inventory'] = {
    'readiness_score': s['civic_intelligence_readiness_pct'],
    'kg_nodes': s['kg_nodes'],
    'kg_edges': s['kg_edges'],
    'kg_orphan_nodes': s['kg_orphan_nodes'],
    'intelligence_layers_partial': s['intelligence_layers_partial'],
    'question_engine_live': s['question_engine_live'],
    'brain_visualization_live': s['brain_visualization_live'],
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 40
        bar['note'] = f"Institutional Brain live — {s['kg_nodes']} KG nodes, {s['kg_edges']} relationships."
    if bar['id'] == 'knowledge_graph':
        bar['value'] = s['kg_growth_pct']
        bar['note'] = f"{s['kg_nodes']}/{s['kg_v1_target_nodes']} nodes — {s['kg_orphan_nodes']} orphans."
    if bar['id'] == 'media_studio':
        bar['value'] = 18
        bar['note'] = 'Media Studio architecture — 0 videos published.'

if not any(b.get('id') == 'civic_intelligence' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'civic_intelligence',
        'label': 'Institutional Brain & Civic Intelligence',
        'value': s['civic_intelligence_readiness_pct'],
        'max': 100,
        'note': f"{s['kg_nodes']} nodes, {s['intelligence_layers_partial']}/7 layers partial — no brain viz."
    })
else:
    for bar in mc['progress_bars']:
        if bar['id'] == 'civic_intelligence':
            bar['value'] = s['civic_intelligence_readiness_pct']
            bar['note'] = f"{s['kg_nodes']} nodes, {s['intelligence_layers_partial']}/7 layers partial."

mc['builds'].insert(0, {
    'number': 40,
    'title': title,
    'version': '1.44.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Institutional Brain Architecture v1.0 — unified civic knowledge intelligence',
    'summary': f"17 node types, 7 intelligence layers, {s['kg_nodes']} KG nodes; {s['civic_intelligence_readiness_pct']}% overall.",
    'files_created': [
        'data/civic-intelligence.json', 'docs/INSTITUTIONAL_BRAIN.md',
        'builds/040-master-knowledge-graph-civic-intelligence.md',
        'mission-control/civic-intelligence.html',
        'scripts/gen-civic-intelligence.py', 'scripts/update-mc-build40.py'
    ],
    'files_modified': ['js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml'],
    'pages_created': ['/mission-control/civic-intelligence.html'],
    'decisions_made': [
        'Institutional Brain extends Build #11 KG — not a replacement',
        '17 node types, 19 relationship types, 7 intelligence layers',
        'Educational dependency chain — campaign finance through disclosure',
        'Community intelligence chain — leader through new counties',
        'Question engine planned — grounded in verified graph',
        f"{s['civic_intelligence_readiness_pct']}% honest readiness — {s['kg_nodes']}/{s['kg_v1_target_nodes']} nodes"
    ],
    'open_questions': ['First brain visualization?', 'County graph integration timing?', 'Question engine vs AI engine?'],
    'risks': [f'KG at {s["kg_growth_pct"]}% of target', f'{s["kg_orphan_nodes"]} orphan nodes', '0 relationship-registry edges'],
    'next_recommended': 41,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/civic-intelligence.html',
    'review_status': 'complete'
})

mc['briefing'] = {
    'what_built': 'Institutional Brain v1.0 — 17 node types, 7 intelligence layers, dependency maps, MC metrics',
    'building_now': 'KG registry as foundation — explore-further interim navigation',
    'blocked': ['No brain visualization', 'Question engine', 'County/community graph edges'],
    'ready_public': ['Civic Intelligence MC dashboard', 'Educational dependency chain', 'KG foundation link'],
    'next': 'Build #41 — Component specifications with props/states'
}

if not any(n.get('id') == 'civic_intelligence' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'civic_intelligence', 'label': 'Institutional Brain & Civic Intelligence', 'href': '/mission-control/civic-intelligence.html', 'status': 'complete'
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
