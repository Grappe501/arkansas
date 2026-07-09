import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json', encoding='utf-8') as f:
    mc = json.load(f)

title = 'Citizens United Facts Master Arkansas Command Strategy v1.0'

with open(root / 'data/arkansas-command-strategy.json', encoding='utf-8') as f:
    acs = json.load(f)

s = acs['summary']
prior_maturity = mc.get('executive', {}).get('institutional_maturity_pct', 32)

mc['version'] = '1.74.0'
mc['build'] = 70
mc['updated'] = '2026-07-09'
mc['arkansas_command_strategy'] = '/data/arkansas-command-strategy.json'
mc['arkansas_command_strategy_dashboard'] = '/mission-control/arkansas-command-strategy.html'

mc['executive'] = {
    'overall_completion': 70,
    'current_build': {'number': 70, 'title': title},
    'active_phase': 'Arkansas Command Strategy → Implementation Translation',
    'last_completed': 'Relational Organizing Growth Engine',
    'next_build': {'number': 71, 'title': 'Implementation translation layer & engineering artifacts'},
    'github_status': 'connected',
    'netlify_status': 'production_healthy',
    'content_readiness': 28,
    'research_readiness': 26,
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
    'campaign_finance_observatory_readiness': 36,
    'arkansas_action_network_readiness': 38,
    'civic_intelligence_command_center_readiness': 43,
    'sustainability_stewardship_readiness': 38,
    'impact_measurement_readiness': 31,
    'citizen_leadership_academy_readiness': 34,
    'relational_organizing_growth_engine_readiness': mc.get('executive', {}).get('relational_organizing_growth_engine_readiness', 34),
    'arkansas_command_strategy_readiness': s['arkansas_command_strategy_readiness_pct'],
    'mc2_readiness': 42,
    'ai_engine_readiness': 34,
    'content_factory_readiness': 30,
    'education_academy_readiness': 26,
    'observatory_readiness': 20,
    'outreach_readiness': 34,
    'county_os_readiness': 28,
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
    'research_methodology_readiness': 25,
    'institutional_maturity_pct': prior_maturity,
    'current_institutional_version': 'V1',
    'systems_integration_readiness': 44,
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
    'statewide_growth_readiness': max(s['statewide_growth_readiness_pct'], s['arkansas_command_strategy_readiness_pct']),
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

mc['arkansas_command_strategy_inventory'] = {
    'readiness_score': s['arkansas_command_strategy_readiness_pct'],
    'counties_with_leaders': s['counties_with_leaders'],
    'cities_with_leaders': s['cities_with_leaders'],
    'connected_arkansans': s['connected_arkansans'],
    'current_execution_phase': s['current_execution_phase'],
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 70
        bar['note'] = 'Build #70 — Arkansas Command Strategy.'
    if bar['id'] == 'signup_funnel':
        bar['value'] = min(100, s['connected_arkansans'] // 2000)
        bar['note'] = (
            f"Statewide execution — {s['counties_with_leaders']}/{s['counties_target']} counties · "
            f"{s['connected_arkansans']}/{s['connected_target']} connected."
        )

if not any(b.get('id') == 'arkansas_command_strategy' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'arkansas_command_strategy',
        'label': 'Command Strategy',
        'value': s['arkansas_command_strategy_readiness_pct'],
        'max': 100,
        'note': (
            f"Phase {s['current_execution_phase']} · "
            f"{s['counties_with_leaders']}/{s['counties_target']} counties · "
            f"{s['cities_with_leaders']}/{s['cities_target']} cities."
        ),
    })
else:
    for bar in mc['progress_bars']:
        if bar['id'] == 'arkansas_command_strategy':
            bar['value'] = s['arkansas_command_strategy_readiness_pct']

mc['builds'].insert(0, {
    'number': 70,
    'title': title,
    'version': '1.74.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Statewide execution playbook — 75 counties, 250 cities, 200K Arkansans',
    'summary': (
        f"Five phases, county/city readiness models, monthly targets, regional strategy, flywheel; "
        f"{s['arkansas_command_strategy_readiness_pct']}% readiness. "
        f"0/{s['counties_target']} counties · 0/{s['cities_target']} cities · "
        f"0/{s['connected_target']} connected."
    ),
    'files_created': [
        'data/arkansas-command-strategy.json',
        'docs/MASTER_ARKANSAS_COMMAND_STRATEGY.md',
        'builds/070-arkansas-command-strategy.md',
        'mission-control/arkansas-command-strategy.html',
        'scripts/gen-arkansas-command-strategy.py',
        'scripts/update-mc-build70.py',
    ],
    'files_modified': ['js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml'],
    'pages_created': ['/mission-control/arkansas-command-strategy.html'],
    'decisions_made': [
        'Statewide execution strategy — operational playbook after 69 design builds',
        'Three objectives: 75 counties, 250 cities, 200,000 connected',
        'Five phases: Core → County Anchors → City → Neighborhood → Multiplication',
        'County 5-stage and city 6-stage readiness models',
        '7 regional strategy — mentorship and coordination',
        'Grow deliberately — not advertising, pressure, or campaigning',
        f"{s['arkansas_command_strategy_readiness_pct']}% readiness — constitution only",
    ],
    'open_questions': [
        'Reconcile Build #70 command vs Build #56 statewide growth blueprint?',
        'Growth dashboard: replace or augment Civic Intelligence Command Center?',
        'Monthly targets: manual entry vs automated from forms?',
        'Projected completion timeline modeling approach?',
    ],
    'risks': acs['catalog_gaps'][:4],
    'next_recommended': 71,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/arkansas-command-strategy.html',
    'review_status': 'complete',
})

mc['briefing'] = {
    'what_built': 'Arkansas Command Strategy v1.0 — statewide execution playbook',
    'building_now': '70 builds specified — implementation translation next',
    'blocked': ['County readiness UI', 'City maturity maps', 'Monthly targets', 'Growth dashboard'],
    'ready_public': ['Three objectives', 'Five phases', 'Readiness models', 'Regional strategy', 'Flywheel'],
    'next': 'Build #71 — Implementation translation layer & engineering artifacts',
}

if not any(n.get('id') == 'arkansas_command_strategy' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'arkansas_command_strategy',
        'label': 'Command Strategy',
        'href': '/mission-control/arkansas-command-strategy.html',
        'status': 'complete',
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
