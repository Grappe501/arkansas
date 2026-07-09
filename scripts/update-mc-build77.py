import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json', encoding='utf-8') as f:
    mc = json.load(f)

title = 'Citizens United Facts Master Arkansas County Operating System (ACOS) v1.0'

with open(root / 'data/arkansas-county-operating-system.json', encoding='utf-8') as f:
    acos = json.load(f)

s = acos['summary']
prior_maturity = mc.get('executive', {}).get('institutional_maturity_pct', 32)

mc['version'] = '1.81.0'
mc['build'] = 77
mc['updated'] = '2026-07-09'
mc['arkansas_county_operating_system'] = '/data/arkansas-county-operating-system.json'
mc['arkansas_county_operating_system_dashboard'] = '/mission-control/arkansas-county-operating-system.html'

mc['executive'] = {
    'overall_completion': 77,
    'current_build': {'number': 77, 'title': title},
    'active_phase': 'County Execution → Implementation Translation',
    'last_completed': 'Organizational Constitution',
    'next_build': {'number': 78, 'title': 'Implementation translation layer & engineering artifacts'},
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
    'arkansas_county_operating_system_readiness': s['arkansas_county_operating_system_readiness_pct'],
    'mc2_readiness': 42,
    'ai_engine_readiness': 34,
    'content_factory_readiness': 30,
    'education_academy_readiness': 26,
    'observatory_readiness': mc.get('executive', {}).get('observatory_readiness', 43),
    'outreach_readiness': 34,
    'county_os_readiness': s['county_os_readiness_pct'],
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

mc['arkansas_county_operating_system_inventory'] = {
    'readiness_score': s['arkansas_county_operating_system_readiness_pct'],
    'counties_scaffolded': s['counties_scaffolded'],
    'counties_total': s['counties_total'],
    'digital_twins_operational': s['counties_with_digital_twin'],
    'master_acos': True,
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 77
        bar['note'] = 'Build #77 — Master Arkansas County Operating System.'
    if bar['id'] == 'county_os':
        bar['value'] = max(bar.get('value', 0), s['arkansas_county_operating_system_readiness_pct'])
        bar['note'] = f"ACOS — {s['counties_scaffolded']}/{s['counties_total']} counties · {s['counties_with_digital_twin']} digital twins."

if not any(b.get('id') == 'arkansas_county_operating_system' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'arkansas_county_operating_system',
        'label': 'County Operating System',
        'value': s['arkansas_county_operating_system_readiness_pct'],
        'max': 100,
        'note': f"{s['counties_past_awareness']}/{s['counties_total']} past Awareness · health index {'live' if s['county_health_index_computed'] else 'planned'}.",
    })
else:
    for bar in mc['progress_bars']:
        if bar['id'] == 'arkansas_county_operating_system':
            bar['value'] = s['arkansas_county_operating_system_readiness_pct']

mc['builds'].insert(0, {
    'number': 77,
    'title': title,
    'version': '1.81.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Master ACOS — county execution framework for 75 Arkansas counties',
    'summary': (
        f"County digital twin, 6 readiness levels, health index, leadership team, "
        f"{s['arkansas_county_operating_system_readiness_pct']}% readiness. "
        f"{s['counties_scaffolded']}/{s['counties_total']} scaffolded · "
        f"{s['counties_with_digital_twin']} digital twins."
    ),
    'files_created': [
        'data/arkansas-county-operating-system.json',
        'docs/MASTER_ARKANSAS_COUNTY_OPERATING_SYSTEM.md',
        'builds/077-arkansas-county-operating-system.md',
        'mission-control/arkansas-county-operating-system.html',
        'scripts/gen-arkansas-county-operating-system.py',
        'scripts/update-mc-build77.py',
    ],
    'files_modified': ['js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml'],
    'pages_created': ['/mission-control/arkansas-county-operating-system.html'],
    'decisions_made': [
        'ACOS as primary statewide expansion framework',
        '6-stage county readiness model',
        'County digital twin — operational dashboard per county',
        '8-role county leadership team',
        'County Health Index — 8 factors',
        'Extends County OS (#31), integrates Command Strategy (#70)',
        f"{s['arkansas_county_operating_system_readiness_pct']}% readiness — blueprint only",
    ],
    'open_questions': [
        'Reconcile ACOS 6-stage vs Command Strategy 5-stage readiness?',
        'ACOS vs County OS (#31) — single dashboard or two?',
        'County digital twin route: /arkansas/[county] or MC-native?',
        'Health index weighting formula?',
    ],
    'risks': acos['catalog_gaps'][:4],
    'next_recommended': 78,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/arkansas-county-operating-system.html',
    'review_status': 'complete',
})

mc['briefing'] = {
    'what_built': 'Master ACOS v1.0 — 75-county execution framework',
    'building_now': '77 builds specified — county digital twins next',
    'blocked': ['County digital twins', 'County dashboards', 'Health index', 'Listening reports'],
    'ready_public': ['6 readiness levels', '13 profile sections', '8 leadership roles', 'Integration chain'],
    'next': 'Build #78 — Implementation translation layer & engineering artifacts',
}

if not any(n.get('id') == 'arkansas_county_operating_system' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'arkansas_county_operating_system',
        'label': 'County Operating System',
        'href': '/mission-control/arkansas-county-operating-system.html',
        'status': 'complete',
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
