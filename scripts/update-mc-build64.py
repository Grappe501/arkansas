import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json', encoding='utf-8') as f:
    mc = json.load(f)

title = 'Citizens United Facts Arkansas Action Network & Leadership Pipeline v1.0'

with open(root / 'data/arkansas-action-network.json', encoding='utf-8') as f:
    aan = json.load(f)

s = aan['summary']

mc['version'] = '1.68.0'
mc['build'] = 64
mc['updated'] = '2026-07-09'
mc['arkansas_action_network'] = '/data/arkansas-action-network.json'
mc['arkansas_action_network_dashboard'] = '/mission-control/arkansas-action-network.html'

mc['executive'] = {
    'overall_completion': 64,
    'current_build': {'number': 64, 'title': title},
    'active_phase': 'Arkansas Action Network → Implementation Translation',
    'last_completed': 'Campaign Finance Data Observatory',
    'next_build': {'number': 65, 'title': 'Implementation translation layer & engineering artifacts'},
    'github_status': 'connected',
    'netlify_status': 'production_healthy',
    'content_readiness': 28,
    'research_readiness': 26,
    'data_viz_readiness': 12,
    'signup_funnel_readiness': 24,
    'civic_action_readiness': 28,
    'coalition_readiness': 44,
    'data_model_readiness': 54,
    'route_inventory_readiness': 18,
    'component_registry_readiness': 22,
    'facts_framework_readiness': 14,
    'knowledge_atlas_readiness': 20,
    'platform_architecture_readiness': 24,
    'repository_structure_readiness': 28,
    'database_schema_readiness': 42,
    'wireframe_readiness': 38,
    'contact_intelligence_readiness': 34,
    'relationship_os_readiness': 54,
    'institutional_ai_readiness': 42,
    'coalition_network_readiness': 44,
    'citizen_action_center_readiness': 42,
    'campaign_finance_observatory_readiness': 36,
    'arkansas_action_network_readiness': s['arkansas_action_network_readiness_pct'],
    'mc2_readiness': 33,
    'ai_engine_readiness': 34,
    'content_factory_readiness': 30,
    'education_academy_readiness': 26,
    'observatory_readiness': 20,
    'outreach_readiness': 24,
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
    'institutional_maturity_pct': 51,
    'current_institutional_version': 'V1',
    'systems_integration_readiness': 38,
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
    'statewide_growth_readiness': max(s['statewide_growth_readiness_pct'], s['arkansas_action_network_readiness_pct']),
    'neighborhood_organizing_readiness': 50,
    'civic_atlas_readiness': 52,
    'rollout_phase': 0,
    'rollout_phase_title': 'Private Development',
    'planning_phase_complete': True,
    'planning_constitution_complete': True,
    'implementation_phase': 'translation_layer_next',
    'public_launch_readiness': s['public_launch_readiness_pct'],
    'public_launch_label': 'Early Foundation',
    'public_launch_recommended': False,
}

mc['arkansas_action_network_inventory'] = {
    'readiness_score': s['arkansas_action_network_readiness_pct'],
    'pyramid_levels': s['pyramid_levels'],
    'county_teams': s['county_teams'],
    'connected_arkansans': s['connected_arkansans'],
    'primary_growth_engine': True,
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 64
        bar['note'] = 'Build #64 — Arkansas Action Network.'
    if bar['id'] == 'institutional_maturity':
        bar['value'] = 51
        bar['note'] = 'Primary growth engine — 0 leaders · 0/200K connected.'
    if bar['id'] == 'signup_funnel':
        bar['value'] = min(100, s['connected_arkansans'] // 2000)
        bar['note'] = f"{s['connected_arkansans']}/{s['connected_target']} connected Arkansans."

if not any(b.get('id') == 'arkansas_action_network' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'arkansas_action_network',
        'label': 'Arkansas Action Network',
        'value': s['arkansas_action_network_readiness_pct'],
        'max': 100,
        'note': f"8 pyramid levels · {s['county_teams']}/{s['county_teams_target']} county teams.",
    })
else:
    for bar in mc['progress_bars']:
        if bar['id'] == 'arkansas_action_network':
            bar['value'] = s['arkansas_action_network_readiness_pct']

mc['builds'].insert(0, {
    'number': 64,
    'title': title,
    'version': '1.68.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Arkansas Action Network — primary growth engine from one learner to 200,000 Arkansans',
    'summary': (
        f"8-level leadership pyramid; invitation engine; progress map; growth analytics; "
        f"{s['arkansas_action_network_readiness_pct']}% readiness. "
        f"0 county teams · 0/{s['connected_target']} connected."
    ),
    'files_created': [
        'data/arkansas-action-network.json', 'docs/MASTER_ARKANSAS_ACTION_NETWORK.md',
        'builds/064-arkansas-action-network.md',
        'mission-control/arkansas-action-network.html',
        'scripts/gen-arkansas-action-network.py', 'scripts/update-mc-build64.py',
    ],
    'files_modified': ['js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml'],
    'pages_created': ['/mission-control/arkansas-action-network.html'],
    'decisions_made': [
        'Primary growth engine — people equipped to teach, not traffic',
        '8-level Arkansas Leadership Pyramid from Visitor to Regional Mentor',
        'Growth objectives: 75 counties → 250 cities → 200K connected → self-sustaining',
        'Invitation engine matches visitor stage — per-page spec',
        'Unifies Statewide Growth (#56) into operational leadership pipeline',
        'Progress map = visual heartbeat via Civic Atlas integration',
        f"{s['arkansas_action_network_readiness_pct']}% readiness — blueprint only, 0 leaders",
    ],
    'open_questions': [
        '8-level pyramid vs ACUCOS participation levels — mapping table?',
        'Progress map: Civic Atlas vs dedicated Action Network map?',
        'Contact Network signup → pyramid level auto-assignment?',
        'Recognition badges: public profiles vs MC-only?',
    ],
    'risks': aan['catalog_gaps'][:4],
    'next_recommended': 65,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/arkansas-action-network.html',
    'review_status': 'complete',
})

mc['briefing'] = {
    'what_built': 'Arkansas Action Network v1.0 — 8-level pyramid, primary growth engine',
    'building_now': '64 builds specified — implementation translation next',
    'blocked': ['Progress map', 'Invitation engine', 'Leader registry', 'Funnel analytics'],
    'ready_public': ['8 pyramid levels', 'Growth objectives', 'Academy pathways spec', 'Succession model'],
    'next': 'Build #65 — Implementation translation layer & engineering artifacts',
}

if not any(n.get('id') == 'arkansas_action_network' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'arkansas_action_network',
        'label': 'Arkansas Action Network',
        'href': '/mission-control/arkansas-action-network.html',
        'status': 'complete',
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
