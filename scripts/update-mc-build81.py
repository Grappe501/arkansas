import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json', encoding='utf-8') as f:
    mc = json.load(f)

title = 'Citizens United Facts Master Institutional Digital Twin & Executive Simulation System v1.0'

with open(root / 'data/institutional-digital-twin.json', encoding='utf-8') as f:
    dt = json.load(f)

s = dt['summary']
prior_maturity = mc.get('executive', {}).get('institutional_maturity_pct', 32)

mc['version'] = '1.85.0'
mc['build'] = 81
mc['updated'] = '2026-07-09'
mc['institutional_digital_twin'] = '/data/institutional-digital-twin.json'
mc['institutional_digital_twin_dashboard'] = '/mission-control/institutional-digital-twin.html'

mc['executive'] = {
    'overall_completion': 81,
    'current_build': {'number': 81, 'title': title},
    'active_phase': 'Digital Twin → Simulation Engine',
    'last_completed': 'Arkansas Civic Institution Roadmap',
    'next_build': {'number': 82, 'title': 'Digital twin simulation engine & heat map components'},
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
    'civic_intelligence_command_center_readiness': mc.get('executive', {}).get('civic_intelligence_command_center_readiness', 43),
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
    'arkansas_neighborhood_operating_system_readiness': mc.get('executive', {}).get('arkansas_neighborhood_operating_system_readiness', 47),
    'arkansas_civic_institution_roadmap_readiness': mc.get('executive', {}).get('arkansas_civic_institution_roadmap_readiness', 48),
    'institutional_digital_twin_readiness': s['institutional_digital_twin_readiness_pct'],
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
    'neighborhood_organizing_readiness': mc.get('executive', {}).get('neighborhood_organizing_readiness', 50),
    'civic_atlas_readiness': 52,
    'rollout_phase': 0,
    'rollout_phase_title': 'Private Development',
    'planning_phase_complete': True,
    'planning_constitution_complete': True,
    'eighty_builds_complete': True,
    'implementation_phase': 'digital_twin_next',
    'public_launch_readiness': s['public_launch_readiness_pct'],
    'public_launch_label': 'Early Foundation',
    'public_launch_recommended': False,
}

mc['institutional_digital_twin_inventory'] = {
    'readiness_score': s['institutional_digital_twin_readiness_pct'],
    'digital_twin_live': s['digital_twin_live'],
    'simulations_run': s['simulations_run'],
    'heat_map_live': s['heat_map_live'],
    'executive_simulation': True,
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 81
        bar['note'] = 'Build #81 — Institutional Digital Twin & Executive Simulation.'
    if bar['id'] == 'civic_intelligence':
        bar['value'] = max(bar.get('value', 0), s['institutional_digital_twin_readiness_pct'])
        bar['note'] = f"Digital Twin — {s['simulations_run']} simulations · heat map {'live' if s['heat_map_live'] else 'planned'}."

if not any(b.get('id') == 'institutional_digital_twin' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'institutional_digital_twin',
        'label': 'Digital Twin',
        'value': s['institutional_digital_twin_readiness_pct'],
        'max': 100,
        'note': f"{s['county_twins_connected']} county twins · predictive {'live' if s['predictive_intelligence_live'] else 'planned'}.",
    })
else:
    for bar in mc['progress_bars']:
        if bar['id'] == 'institutional_digital_twin':
            bar['value'] = s['institutional_digital_twin_readiness_pct']

mc['builds'].insert(0, {
    'number': 81,
    'title': title,
    'version': '1.85.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Institutional Digital Twin — simulate, forecast, plan before deciding',
    'summary': (
        f"12-system model, executive simulation, geographic layers, forecasting, heat map, "
        f"{s['institutional_digital_twin_readiness_pct']}% readiness. "
        f"{s['simulations_run']} simulations · twin {'live' if s['digital_twin_live'] else 'not live'}."
    ),
    'files_created': [
        'data/institutional-digital-twin.json',
        'docs/MASTER_INSTITUTIONAL_DIGITAL_TWIN.md',
        'builds/081-institutional-digital-twin.md',
        'mission-control/institutional-digital-twin.html',
        'scripts/gen-institutional-digital-twin.py',
        'scripts/update-mc-build81.py',
    ],
    'files_modified': ['js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml'],
    'pages_created': ['/mission-control/institutional-digital-twin.html'],
    'decisions_made': [
        'Digital Twin mirrors entire institution in real time (specified)',
        'Three questions: current, operational, predictive intelligence',
        'Executive what-if simulation before decisions',
        'County/city/neighborhood simulation layers',
        'Statewide heat map as flagship MC view',
        'Decision support engine before major decisions',
        f"{s['institutional_digital_twin_readiness_pct']}% readiness — specification only",
    ],
    'open_questions': [
        'Digital Twin vs CICC (#65) — single executive intelligence layer?',
        'Digital Twin vs geographic OS twins (#77–79) — unify or nest?',
        'Simulation engine — rules-based or data-driven?',
        'Heat map data sources — which registries feed layers?',
    ],
    'risks': dt['catalog_gaps'][:4],
    'next_recommended': 82,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/institutional-digital-twin.html',
    'review_status': 'complete',
})

mc['briefing'] = {
    'what_built': 'Institutional Digital Twin v1.0 — see institution before it happens',
    'building_now': '81 builds — simulation engine next',
    'blocked': ['Simulation engine', 'Heat map', 'Decision support', 'Historical replay', 'Predictive intelligence'],
    'ready_public': ['12-system model', '5 scenarios', 'Forecasting domains', 'Three questions framework'],
    'next': 'Build #82 — Digital twin simulation engine & heat map components',
}

if not any(n.get('id') == 'institutional_digital_twin' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'institutional_digital_twin',
        'label': 'Digital Twin',
        'href': '/mission-control/institutional-digital-twin.html',
        'status': 'complete',
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
