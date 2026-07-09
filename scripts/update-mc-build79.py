import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json', encoding='utf-8') as f:
    mc = json.load(f)

title = 'Citizens United Facts Master Arkansas Neighborhood Operating System (ANOS) v1.0'

with open(root / 'data/arkansas-neighborhood-operating-system.json', encoding='utf-8') as f:
    anos = json.load(f)

s = anos['summary']
prior_maturity = mc.get('executive', {}).get('institutional_maturity_pct', 32)

mc['version'] = '1.83.0'
mc['build'] = 79
mc['updated'] = '2026-07-09'
mc['arkansas_neighborhood_operating_system'] = '/data/arkansas-neighborhood-operating-system.json'
mc['arkansas_neighborhood_operating_system_dashboard'] = '/mission-control/arkansas-neighborhood-operating-system.html'

mc['executive'] = {
    'overall_completion': 79,
    'current_build': {'number': 79, 'title': title},
    'active_phase': 'Neighborhood Execution → Implementation Translation',
    'last_completed': 'Arkansas City Operating System',
    'next_build': {'number': 80, 'title': 'Implementation translation layer & engineering artifacts'},
    'github_status': 'connected',
    'netlify_status': 'production_healthy',
    'content_readiness': 28,
    'research_readiness': mc.get('executive', {}).get('research_readiness', 43),
    'data_viz_readiness': 12,
    'signup_funnel_readiness': 26,
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
    'relationship_os_readiness': mc.get('executive', {}).get('relationship_os_readiness', 54),
    'institutional_ai_readiness': 42,
    'coalition_network_readiness': 44,
    'citizen_action_center_readiness': 42,
    'campaign_finance_observatory_readiness': mc.get('executive', {}).get('campaign_finance_observatory_readiness', 38),
    'arkansas_action_network_readiness': 38,
    'civic_intelligence_command_center_readiness': 43,
    'sustainability_stewardship_readiness': mc.get('executive', {}).get('sustainability_stewardship_readiness', 38),
    'impact_measurement_readiness': 31,
    'citizen_leadership_academy_readiness': 34,
    'relational_organizing_growth_engine_readiness': mc.get('executive', {}).get('relational_organizing_growth_engine_readiness', 34),
    'arkansas_command_strategy_readiness': mc.get('executive', {}).get('arkansas_command_strategy_readiness', 39),
    'arkansas_community_listening_readiness': mc.get('executive', {}).get('arkansas_community_listening_readiness', 41),
    'arkansas_communications_readiness': mc.get('executive', {}).get('arkansas_communications_readiness', 42),
    'arkansas_research_institute_readiness': mc.get('executive', {}).get('arkansas_research_institute_readiness', 43),
    'arkansas_civic_innovation_reform_readiness': mc.get('executive', {}).get('arkansas_civic_innovation_reform_readiness', 44),
    'volunteer_funding_constitution_readiness': mc.get('executive', {}).get('volunteer_funding_constitution_readiness', 45),
    'organizational_constitution_readiness': mc.get('executive', {}).get('organizational_constitution_readiness', 46),
    'arkansas_county_operating_system_readiness': mc.get('executive', {}).get('arkansas_county_operating_system_readiness', 47),
    'arkansas_city_operating_system_readiness': mc.get('executive', {}).get('arkansas_city_operating_system_readiness', 48),
    'arkansas_neighborhood_operating_system_readiness': s['arkansas_neighborhood_operating_system_readiness_pct'],
    'mc2_readiness': 42,
    'ai_engine_readiness': 34,
    'content_factory_readiness': 30,
    'education_academy_readiness': 26,
    'observatory_readiness': mc.get('executive', {}).get('observatory_readiness', 43),
    'outreach_readiness': 34,
    'county_os_readiness': mc.get('executive', {}).get('county_os_readiness', 28),
    'campaign_os_readiness': 34,
    'encyclopedia_readiness': 19,
    'narrative_readiness': 24,
    'curriculum_readiness': 26,
    'trust_readiness': 30,
    'library_readiness': 22,
    'learning_lab_readiness': 22,
    'media_studio_readiness': 18,
    'civic_intelligence_readiness': 36,
    'evidence_ledger_readiness': 22,
    'civic_action_lab_readiness': 26,
    'research_methodology_readiness': mc.get('executive', {}).get('research_methodology_readiness', 29),
    'institutional_maturity_pct': prior_maturity,
    'current_institutional_version': 'V1',
    'systems_integration_readiness': 44,
    'production_matrix_readiness': 39,
    'visitor_journey_readiness': 40,
    'technical_architecture_readiness': 38,
    'governance_readiness': mc.get('executive', {}).get('governance_readiness', 46),
    'build_bible_readiness': 49,
    'data_architecture_readiness': 41,
    'ux_architecture_readiness': 39,
    'launch_strategy_readiness': 39,
    'pmo_readiness': 46,
    'master_plan_readiness': 56,
    'statewide_growth_readiness': mc.get('executive', {}).get('statewide_growth_readiness', 48),
    'neighborhood_organizing_readiness': max(s['neighborhood_organizing_readiness_pct'], s['arkansas_neighborhood_operating_system_readiness_pct']),
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

mc['arkansas_neighborhood_operating_system_inventory'] = {
    'readiness_score': s['arkansas_neighborhood_operating_system_readiness_pct'],
    'neighborhood_profiles': s['neighborhood_profiles_total'],
    'digital_twins_operational': s['neighborhoods_with_digital_twin'],
    'final_institutional_layer': True,
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 79
        bar['note'] = 'Build #79 — Master Arkansas Neighborhood Operating System.'
    if bar['id'] == 'neighborhood_organizing':
        bar['value'] = max(bar.get('value', 0), s['arkansas_neighborhood_operating_system_readiness_pct'])
        bar['note'] = f"ANOS final layer — {s['neighborhood_profiles_total']} profiles · {s['connected_arkansans']}/{s['participants_target']} connected."

if not any(b.get('id') == 'arkansas_neighborhood_operating_system' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'arkansas_neighborhood_operating_system',
        'label': 'Neighborhood Operating System',
        'value': s['arkansas_neighborhood_operating_system_readiness_pct'],
        'max': 100,
        'note': f"{s['neighborhoods_with_leader']} leaders · health score {'live' if s['neighborhood_health_score_computed'] else 'planned'}.",
    })
else:
    for bar in mc['progress_bars']:
        if bar['id'] == 'arkansas_neighborhood_operating_system':
            bar['value'] = s['arkansas_neighborhood_operating_system_readiness_pct']

mc['builds'].insert(0, {
    'number': 79,
    'title': title,
    'version': '1.83.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Master ANOS — final layer; neighborhood trust foundation',
    'summary': (
        f"Growth cycle, health score, mentorship trees, 200K strategy, "
        f"{s['arkansas_neighborhood_operating_system_readiness_pct']}% readiness. "
        f"{s['neighborhood_profiles_total']} profiles · "
        f"{s['connected_arkansans']}/{s['participants_target']} connected."
    ),
    'files_created': [
        'data/arkansas-neighborhood-operating-system.json',
        'docs/MASTER_ARKANSAS_NEIGHBORHOOD_OPERATING_SYSTEM.md',
        'builds/079-arkansas-neighborhood-operating-system.md',
        'mission-control/arkansas-neighborhood-operating-system.html',
        'scripts/gen-arkansas-neighborhood-operating-system.py',
        'scripts/update-mc-build79.py',
    ],
    'files_modified': ['js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml'],
    'pages_created': ['/mission-control/arkansas-neighborhood-operating-system.html'],
    'decisions_made': [
        'ANOS as final institutional architecture layer',
        '8-step neighborhood growth cycle',
        'Privacy: no residential data publicly displayed',
        '6-role neighborhood leadership team',
        '200K Arkansan strategy via local relationships',
        'Extends Neighborhood Organizing (#57)',
        f"{s['arkansas_neighborhood_operating_system_readiness_pct']}% readiness — blueprint only",
    ],
    'open_questions': [
        'ANOS vs Neighborhood Organizing (#57) — single dashboard?',
        'Neighborhood profile creation workflow?',
        'Health score weighting formula?',
        'Mentorship tree data model — ROS or MC-native?',
    ],
    'risks': anos['catalog_gaps'][:4],
    'next_recommended': 80,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/arkansas-neighborhood-operating-system.html',
    'review_status': 'complete',
})

mc['briefing'] = {
    'what_built': 'Master ANOS v1.0 — final layer, last 500 feet',
    'building_now': '79 builds specified — neighborhood profiles next',
    'blocked': ['Neighborhood profiles', 'Growth cycle tracking', 'Health score', 'Mentorship trees'],
    'ready_public': ['8-step growth cycle', '10 profile sections', '6 leadership roles', '200K strategy'],
    'next': 'Build #80 — Implementation translation layer & engineering artifacts',
}

if not any(n.get('id') == 'arkansas_neighborhood_operating_system' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'arkansas_neighborhood_operating_system',
        'label': 'Neighborhood Operating System',
        'href': '/mission-control/arkansas-neighborhood-operating-system.html',
        'status': 'complete',
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
