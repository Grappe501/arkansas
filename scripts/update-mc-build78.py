import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json', encoding='utf-8') as f:
    mc = json.load(f)

title = 'Citizens United Facts Master Arkansas City Operating System (ArCOS) v1.0'

with open(root / 'data/arkansas-city-operating-system.json', encoding='utf-8') as f:
    arcity = json.load(f)

s = arcity['summary']
prior_maturity = mc.get('executive', {}).get('institutional_maturity_pct', 32)

mc['version'] = '1.82.0'
mc['build'] = 78
mc['updated'] = '2026-07-09'
mc['arkansas_city_operating_system'] = '/data/arkansas-city-operating-system.json'
mc['arkansas_city_operating_system_dashboard'] = '/mission-control/arkansas-city-operating-system.html'

mc['executive'] = {
    'overall_completion': 78,
    'current_build': {'number': 78, 'title': title},
    'active_phase': 'City Execution → Implementation Translation',
    'last_completed': 'Arkansas County Operating System',
    'next_build': {'number': 79, 'title': 'Implementation translation layer & engineering artifacts'},
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
    'arkansas_city_operating_system_readiness': s['arkansas_city_operating_system_readiness_pct'],
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

mc['arkansas_city_operating_system_inventory'] = {
    'readiness_score': s['arkansas_city_operating_system_readiness_pct'],
    'cities_scaffolded': s['cities_scaffolded'],
    'cities_total': s['cities_total'],
    'digital_twins_operational': s['cities_with_digital_twin'],
    'master_arcity': True,
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 78
        bar['note'] = 'Build #78 — Master Arkansas City Operating System.'
    if bar['id'] == 'arkansas_county_operating_system':
        bar['note'] = f"ACOS county layer — see ArCOS (#78) for city bridge."

if not any(b.get('id') == 'arkansas_city_operating_system' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'arkansas_city_operating_system',
        'label': 'City Operating System',
        'value': s['arkansas_city_operating_system_readiness_pct'],
        'max': 100,
        'note': f"{s['cities_past_initial_interest']}/{s['cities_total']} past initial interest · health index {'live' if s['city_health_index_computed'] else 'planned'}.",
    })
else:
    for bar in mc['progress_bars']:
        if bar['id'] == 'arkansas_city_operating_system':
            bar['value'] = s['arkansas_city_operating_system_readiness_pct']

mc['builds'].insert(0, {
    'number': 78,
    'title': title,
    'version': '1.82.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Master ArCOS — city execution framework for 250 largest Arkansas cities',
    'summary': (
        f"City digital twin, 6 readiness levels, health index, neighborhood integration, "
        f"{s['arkansas_city_operating_system_readiness_pct']}% readiness. "
        f"{s['cities_scaffolded']}/{s['cities_total']} scaffolded · "
        f"{s['cities_with_digital_twin']} digital twins."
    ),
    'files_created': [
        'data/arkansas-city-operating-system.json',
        'docs/MASTER_ARKANSAS_CITY_OPERATING_SYSTEM.md',
        'builds/078-arkansas-city-operating-system.md',
        'mission-control/arkansas-city-operating-system.html',
        'scripts/gen-arkansas-city-operating-system.py',
        'scripts/update-mc-build78.py',
    ],
    'files_modified': ['js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml'],
    'pages_created': ['/mission-control/arkansas-city-operating-system.html'],
    'decisions_made': [
        'ArCOS as bridge between county leadership and neighborhoods',
        '6-stage city readiness model',
        'City digital twin — 8-section operational headquarters',
        '7-role city leadership team',
        'Neighborhood integration on city dashboards',
        'Integrates ACOS (#77), Neighborhood Organizing (#57)',
        f"{s['arkansas_city_operating_system_readiness_pct']}% readiness — blueprint only",
    ],
    'open_questions': [
        'Reconcile ArCOS 6-stage vs Command Strategy city model?',
        'City digital twin route: /arkansas/[city] or MC-native?',
        'County linkage on city records — populate from atlas?',
        'Health index weighting formula?',
    ],
    'risks': arcity['catalog_gaps'][:4],
    'next_recommended': 79,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/arkansas-city-operating-system.html',
    'review_status': 'complete',
})

mc['briefing'] = {
    'what_built': 'Master ArCOS v1.0 — 250-city execution framework',
    'building_now': '78 builds specified — city digital twins next',
    'blocked': ['City digital twins', 'City dashboards', 'Health index', 'Neighborhood integration UI'],
    'ready_public': ['6 readiness levels', '8 digital twin sections', '7 leadership roles', 'Integration chain'],
    'next': 'Build #79 — Implementation translation layer & engineering artifacts',
}

if not any(n.get('id') == 'arkansas_city_operating_system' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'arkansas_city_operating_system',
        'label': 'City Operating System',
        'href': '/mission-control/arkansas-city-operating-system.html',
        'status': 'complete',
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
