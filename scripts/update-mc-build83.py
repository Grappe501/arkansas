import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json', encoding='utf-8') as f:
    mc = json.load(f)

title = 'Citizens United Facts Master Arkansas Civic Ecosystem v1.0'

with open(root / 'data/arkansas-civic-ecosystem.json', encoding='utf-8') as f:
    eco = json.load(f)

s = eco['summary']
prior_maturity = mc.get('executive', {}).get('institutional_maturity_pct', 32)

mc['version'] = '1.87.0'
mc['build'] = 83
mc['updated'] = '2026-07-09'
mc['arkansas_civic_ecosystem'] = '/data/arkansas-civic-ecosystem.json'
mc['arkansas_civic_ecosystem_dashboard'] = '/mission-control/arkansas-civic-ecosystem.html'

mc['executive'] = {
    'overall_completion': 83,
    'current_build': {'number': 83, 'title': title},
    'active_phase': 'Civic Ecosystem → Health Dashboard',
    'last_completed': 'Public Trust & Institutional Credibility',
    'next_build': {'number': 84, 'title': 'Ecosystem health dashboard & network effect components'},
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
    'arkansas_neighborhood_operating_system_readiness': mc.get('executive', {}).get('arkansas_neighborhood_operating_system_readiness', 47),
    'arkansas_civic_institution_roadmap_readiness': mc.get('executive', {}).get('arkansas_civic_institution_roadmap_readiness', 48),
    'institutional_digital_twin_readiness': mc.get('executive', {}).get('institutional_digital_twin_readiness', 51),
    'public_trust_institutional_credibility_readiness': mc.get('executive', {}).get('public_trust_institutional_credibility_readiness', 50),
    'arkansas_civic_ecosystem_readiness': s['arkansas_civic_ecosystem_readiness_pct'],
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
    'trust_readiness': mc.get('executive', {}).get('trust_readiness', 50),
    'library_readiness': 22,
    'learning_lab_readiness': 22,
    'media_studio_readiness': 18,
    'civic_intelligence_readiness': 36,
    'evidence_ledger_readiness': 22,
    'civic_action_lab_readiness': 26,
    'research_methodology_readiness': mc.get('executive', {}).get('research_methodology_readiness', 29),
    'institutional_maturity_pct': prior_maturity,
    'current_institutional_version': 'V1',
    'systems_integration_readiness': max(44, s['arkansas_civic_ecosystem_readiness_pct'] - 10),
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
    'implementation_phase': 'ecosystem_health_dashboard_next',
    'public_launch_readiness': s['public_launch_readiness_pct'],
    'public_launch_label': 'Early Foundation',
    'public_launch_recommended': False,
}

mc['arkansas_civic_ecosystem_inventory'] = {
    'readiness_score': s['arkansas_civic_ecosystem_readiness_pct'],
    'living_systems': s['living_systems_total'],
    'ecosystem_health_score_live': s['ecosystem_health_score_live'],
    'one_institution_one_state': True,
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 83
        bar['note'] = 'Build #83 — Arkansas Civic Ecosystem.'
    if bar['id'] == 'systems_integration':
        bar['value'] = max(bar.get('value', 0), mc['executive']['systems_integration_readiness'])
        bar['note'] = f"12 living systems · {s['living_systems_instrumented']} instrumented."

if not any(b.get('id') == 'arkansas_civic_ecosystem' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'arkansas_civic_ecosystem',
        'label': 'Civic Ecosystem',
        'value': s['arkansas_civic_ecosystem_readiness_pct'],
        'max': 100,
        'note': f"{s['living_systems_total']} systems · health score {'live' if s['ecosystem_health_score_live'] else 'planned'}.",
    })
else:
    for bar in mc['progress_bars']:
        if bar['id'] == 'arkansas_civic_ecosystem':
            bar['value'] = s['arkansas_civic_ecosystem_readiness_pct']

mc['builds'].insert(0, {
    'number': 83,
    'title': title,
    'version': '1.87.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'One institution, one state, one connected civic network',
    'summary': (
        f"12 living systems, 4 ecosystem loops, health score, executive dashboard, "
        f"{s['arkansas_civic_ecosystem_readiness_pct']}% readiness. "
        f"{s['living_systems_instrumented']}/{s['living_systems_total']} instrumented · "
        f"health score {'live' if s['ecosystem_health_score_live'] else 'not live'}."
    ),
    'files_created': [
        'data/arkansas-civic-ecosystem.json',
        'docs/MASTER_ARKANSAS_CIVIC_ECOSYSTEM.md',
        'builds/083-arkansas-civic-ecosystem.md',
        'mission-control/arkansas-civic-ecosystem.html',
        'scripts/gen-arkansas-civic-ecosystem.py',
        'scripts/update-mc-build83.py',
    ],
    'files_modified': ['js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml'],
    'pages_created': ['/mission-control/arkansas-civic-ecosystem.html'],
    'decisions_made': [
        'Ecosystem philosophy — departments to ecosystems',
        '12 permanently connected living systems',
        '4 reinforcing ecosystem loops + Arkansas learning loop',
        'Ecosystem Health Score — 10 dimensions',
        'Executive Ecosystem Dashboard — one screen',
        'Extends Civic Ecosystem (#12) county layer',
        f"{s['arkansas_civic_ecosystem_readiness_pct']}% readiness — blueprint only",
    ],
    'open_questions': [
        'Build #83 vs Civic Ecosystem (#12) — unify or keep separate dashboards?',
        'Health score — weighted average or minimum dimension?',
        'Imbalance detection — automated thresholds?',
        'Network effects — model in Digital Twin (#81)?',
    ],
    'risks': eco['catalog_gaps'][:4],
    'next_recommended': 84,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/arkansas-civic-ecosystem.html',
    'review_status': 'complete',
})

mc['briefing'] = {
    'what_built': 'Arkansas Civic Ecosystem v1.0 — one connected civic network',
    'building_now': '83 builds — ecosystem health dashboard next',
    'blocked': ['Health score engine', 'Executive ecosystem dashboard', 'System instrumentation', 'Imbalance detection'],
    'ready_public': ['12 living systems', '4 ecosystem loops', 'Founder vision', 'Network effects model'],
    'next': 'Build #84 — Ecosystem health dashboard & network effect components',
}

if not any(n.get('id') == 'arkansas_civic_ecosystem' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'arkansas_civic_ecosystem',
        'label': 'Civic Ecosystem',
        'href': '/mission-control/arkansas-civic-ecosystem.html',
        'status': 'complete',
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
