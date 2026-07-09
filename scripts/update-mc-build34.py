import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json') as f:
    mc = json.load(f)

title = 'Citizens United Facts Storytelling & Narrative Architecture'

with open(root / 'data/narrative-architecture.json') as f:
    narr = json.load(f)

s = narr['summary']
nc = narr['narrative_completion']

mc['version'] = '1.38.0'
mc['build'] = 34
mc['updated'] = '2026-07-09'
mc['narrative_architecture'] = '/data/narrative-architecture.json'
mc['narrative_dashboard'] = '/mission-control/narrative.html'

mc['executive'] = {
    'overall_completion': 34,
    'current_build': {'number': 34, 'title': title},
    'active_phase': 'Educational Narrative — Eight Acts Documentary Museum',
    'last_completed': 'Research Encyclopedia & Knowledge Library',
    'next_build': {'number': 35, 'title': 'Component specifications with props/states'},
    'github_status': 'connected',
    'netlify_status': 'production_healthy',
    'content_readiness': 24,
    'research_readiness': 24,
    'data_viz_readiness': 4,
    'signup_funnel_readiness': 22,
    'civic_action_readiness': 32,
    'coalition_readiness': 18,
    'data_model_readiness': 38,
    'route_inventory_readiness': 18,
    'component_registry_readiness': 22,
    'facts_framework_readiness': 12,
    'knowledge_atlas_readiness': 20,
    'platform_architecture_readiness': 20,
    'repository_structure_readiness': 28,
    'database_schema_readiness': 35,
    'wireframe_readiness': 38,
    'contact_intelligence_readiness': 31,
    'mc2_readiness': 33,
    'ai_engine_readiness': 14,
    'content_factory_readiness': 28,
    'education_academy_readiness': 24,
    'observatory_readiness': 18,
    'outreach_readiness': 22,
    'county_os_readiness': 28,
    'campaign_os_readiness': 34,
    'encyclopedia_readiness': 19,
    'narrative_readiness': s['narrative_readiness_pct'],
    'public_launch_readiness': 8,
    'public_launch_label': 'Early Foundation'
}

mc['narrative_inventory'] = {
    'readiness_score': s['narrative_readiness_pct'],
    'acts_total': s['acts_total'],
    'avg_act_narrative_pct': s['avg_act_narrative_pct'],
    'acts_with_primary_page': s['acts_with_primary_page'],
    'narrative_completion': nc,
    'continuity_live': s['continuity_live'],
    'act_navigation_live': s['act_navigation_live'],
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 34
        bar['note'] = f"Narrative live — 8 acts, avg {s['avg_act_narrative_pct']}% act completion, documentary museum architecture."

if not any(b.get('id') == 'narrative' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'narrative',
        'label': 'Narrative Architecture',
        'value': s['narrative_readiness_pct'],
        'max': 100,
        'note': f"{s['acts_with_primary_page']}/8 acts mapped to hall pages — continuity not live."
    })

mc['builds'].insert(0, {
    'number': 34,
    'title': title,
    'version': '1.38.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Educational Narrative System v1.0 — eight acts, four layers, documentary museum',
    'summary': f"{s['acts_total']} acts, {s['narrative_layers']} layers, avg act {s['avg_act_narrative_pct']}%; {s['narrative_readiness_pct']}% readiness.",
    'files_created': [
        'data/narrative-architecture.json', 'docs/NARRATIVE_ARCHITECTURE.md',
        'builds/034-narrative-architecture.md', 'mission-control/narrative.html',
        'scripts/gen-narrative-architecture.py', 'scripts/update-mc-build34.py'
    ],
    'files_modified': ['js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml'],
    'pages_created': ['/mission-control/narrative.html'],
    'decisions_made': [
        'Master narrative: one Supreme Court decision to civic meaning today',
        '8 narrative acts mapped to existing hall and solutions pages',
        '4 storytelling layers (1 min → research archive)',
        '8 reusable story components + 6 visual storytelling elements',
        'Narrative continuity requirements — not yet on all pages',
        f"{s['narrative_readiness_pct']}% honest readiness — acts I–V partial, VI/VIII weakest"
    ],
    'open_questions': ['When to migrate to canonical /story/act routes?', 'Layer 3 depth per act?'],
    'risks': ['Act continuity not live', 'Acts VI and VIII thin', 'Visual storytelling mostly planned'],
    'next_recommended': 35,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/narrative.html',
    'review_status': 'complete'
})

mc['briefing'] = {
    'what_built': f'Narrative v1.0 — 8 acts, 4 layers, master narrative, MC completion tracking',
    'building_now': 'Documentary museum journey — halls mapped as Acts I–V, solutions as VII',
    'blocked': ['Act-aware continuity not on pages', 'Layer 3 narratives not written', 'Canonical act routes not built'],
    'ready_public': ['Narrative MC dashboard', '8-act architecture', 'Story components schema', 'Hall page mapping'],
    'next': 'Build #35 — Component specifications with props/states'
}

if not any(n.get('id') == 'narrative' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'narrative', 'label': 'Narrative Architecture', 'href': '/mission-control/narrative.html', 'status': 'complete'
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
