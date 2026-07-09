import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json', encoding='utf-8') as f:
    mc = json.load(f)

title = 'Citizens United Facts Arkansas Civic Intelligence & Community Mapping System v1.0'

with open(root / 'data/civic-atlas.json', encoding='utf-8') as f:
    ca = json.load(f)

s = ca['summary']

mc['version'] = '1.62.0'
mc['build'] = 58
mc['updated'] = '2026-07-09'
mc['civic_atlas'] = '/data/civic-atlas.json'
mc['civic_atlas_dashboard'] = '/mission-control/civic-atlas.html'

mc['executive'] = {
    'overall_completion': 58,
    'current_build': {'number': 58, 'title': title},
    'active_phase': 'Civic Atlas Intelligence → Implementation Translation',
    'last_completed': 'Neighborhood Organizing & Relational Network',
    'next_build': {'number': 59, 'title': 'Implementation translation layer & engineering artifacts'},
    'github_status': 'connected',
    'netlify_status': 'production_healthy',
    'content_readiness': 28,
    'research_readiness': 25,
    'data_viz_readiness': 8,
    'signup_funnel_readiness': 22,
    'civic_action_readiness': 26,
    'coalition_readiness': 18,
    'data_model_readiness': 52,
    'route_inventory_readiness': 18,
    'component_registry_readiness': 22,
    'facts_framework_readiness': 14,
    'knowledge_atlas_readiness': 20,
    'platform_architecture_readiness': 24,
    'repository_structure_readiness': 28,
    'database_schema_readiness': 40,
    'wireframe_readiness': 38,
    'contact_intelligence_readiness': 31,
    'mc2_readiness': 33,
    'ai_engine_readiness': 14,
    'content_factory_readiness': 30,
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
    'civic_intelligence_readiness': 28,
    'evidence_ledger_readiness': 22,
    'civic_action_lab_readiness': 26,
    'research_methodology_readiness': 25,
    'institutional_maturity_pct': 45,
    'current_institutional_version': 'V1',
    'systems_integration_readiness': 28,
    'production_matrix_readiness': 39,
    'visitor_journey_readiness': 40,
    'technical_architecture_readiness': 38,
    'governance_readiness': 44,
    'build_bible_readiness': 49,
    'data_architecture_readiness': 41,
    'ux_architecture_readiness': 39,
    'launch_strategy_readiness': 39,
    'pmo_readiness': 46,
    'master_plan_readiness': 56,
    'statewide_growth_readiness': s['statewide_growth_readiness_pct'],
    'neighborhood_organizing_readiness': s['neighborhood_organizing_readiness_pct'],
    'civic_atlas_readiness': s['civic_atlas_readiness_pct'],
    'rollout_phase': 0,
    'rollout_phase_title': 'Private Development',
    'planning_phase_complete': True,
    'planning_constitution_complete': True,
    'implementation_phase': 'translation_layer_next',
    'public_launch_readiness': s['public_launch_readiness_pct'],
    'public_launch_label': 'Early Foundation',
    'public_launch_recommended': False,
}

mc['civic_atlas_inventory'] = {
    'readiness_score': s['civic_atlas_readiness_pct'],
    'counties_scored': s['counties_total'],
    'statewide_avg_coverage_score': s['statewide_avg_coverage_score'],
    'communities_joined': s['communities_joined'],
    'assets_cataloged': s['assets_cataloged'],
    'interactive_map_status': s['interactive_map_status'],
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 58
        bar['note'] = 'Build #58 — Arkansas Civic Atlas.'
    if bar['id'] == 'institutional_maturity':
        bar['value'] = 45
        bar['note'] = 'Geographic intelligence layer live — map planned.'

if not any(b.get('id') == 'civic_atlas' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'civic_atlas',
        'label': 'Civic Atlas',
        'value': s['civic_atlas_readiness_pct'],
        'max': 100,
        'note': f"75 counties ECS=0 · {s['assets_cataloged']} assets · map planned."
    })
else:
    for bar in mc['progress_bars']:
        if bar['id'] == 'civic_atlas':
            bar['value'] = s['civic_atlas_readiness_pct']
            bar['note'] = 'Geographic heartbeat — educational planning system.'

mc['builds'].insert(0, {
    'number': 58,
    'title': title,
    'version': '1.62.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Arkansas Civic Atlas — geographic intelligence & community mapping',
    'summary': (
        f"7-level hierarchy; Educational Coverage Score; 75 county scores; "
        f"{s['civic_atlas_readiness_pct']}% atlas readiness. 0 communities · map planned."
    ),
    'files_created': [
        'data/civic-atlas.json', 'data/community-profiles.json', 'data/community-assets.json',
        'docs/MASTER_CIVIC_ATLAS.md', 'builds/058-civic-atlas.md',
        'mission-control/civic-atlas.html',
        'scripts/gen-civic-atlas.py', 'scripts/update-mc-build58.py',
    ],
    'files_modified': ['js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml'],
    'pages_created': ['/mission-control/civic-atlas.html'],
    'decisions_made': [
        'Educational planning system — not political targeting',
        '7-level geographic hierarchy through Education Leader',
        'Educational Coverage Score: Leadership, Learning, Community, Coalition, Resources',
        '75 counties scored at 0 — honest baseline',
        'Community assets directory: 10 asset types scaffolded',
        'Integrates #56 statewide, #57 neighborhood, #31 county OS',
        f"{s['civic_atlas_readiness_pct']}% readiness — intelligence documented, map not built",
    ],
    'open_questions': [
        'Unify ECS with County OS education score categories?',
        'Map tech: Leaflet + GeoJSON vs SVG Arkansas?',
        'Faith community opt-in listing workflow?',
        'Community asset ingestion: manual vs API?',
    ],
    'risks': ca['catalog_gaps'][:4],
    'next_recommended': 59,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/civic-atlas.html',
    'review_status': 'complete'
})

mc['briefing'] = {
    'what_built': 'Arkansas Civic Atlas v1.0 — geographic intelligence, ECS scores, assets directory',
    'building_now': 'Community growth stack complete (#56–#58) — implementation translation next',
    'blocked': ['Interactive map', 'Civic calendar', 'Asset ingestion', 'Story archive'],
    'ready_public': ['75 county ECS baseline', '7 regions', 'Planning questions', 'Needs assessment'],
    'next': 'Build #59 — Implementation translation layer & engineering artifacts'
}

if not any(n.get('id') == 'civic_atlas' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'civic_atlas',
        'label': 'Civic Atlas',
        'href': '/mission-control/civic-atlas.html',
        'status': 'complete'
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
