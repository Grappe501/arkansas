import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json', encoding='utf-8') as f:
    mc = json.load(f)

title = 'Citizens United Facts Master Arkansas Strategic Plan 2035 v1.0'

with open(root / 'data/arkansas-strategic-plan-2035.json', encoding='utf-8') as f:
    sp = json.load(f)

s = sp['summary']
prior_maturity = mc.get('executive', {}).get('institutional_maturity_pct', 32)

mc['version'] = '1.88.0'
mc['build'] = 84
mc['updated'] = '2026-07-09'
mc['arkansas_strategic_plan_2035'] = '/data/arkansas-strategic-plan-2035.json'
mc['arkansas_strategic_plan_2035_dashboard'] = '/mission-control/arkansas-strategic-plan-2035.html'

mc['executive'] = {
    'overall_completion': 84,
    'current_build': {'number': 84, 'title': title},
    'active_phase': 'Strategic Plan → Scorecard',
    'last_completed': 'Arkansas Civic Ecosystem',
    'next_build': {'number': 85, 'title': 'Strategic scorecard & annual review components'},
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
    'arkansas_civic_ecosystem_readiness': mc.get('executive', {}).get('arkansas_civic_ecosystem_readiness', 54),
    'arkansas_strategic_plan_2035_readiness': s['arkansas_strategic_plan_2035_readiness_pct'],
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
    'systems_integration_readiness': mc.get('executive', {}).get('systems_integration_readiness', 44),
    'production_matrix_readiness': 39,
    'visitor_journey_readiness': 40,
    'technical_architecture_readiness': 38,
    'governance_readiness': mc.get('executive', {}).get('governance_readiness', 46),
    'build_bible_readiness': 49,
    'data_architecture_readiness': 41,
    'ux_architecture_readiness': 39,
    'launch_strategy_readiness': 39,
    'pmo_readiness': 46,
    'master_plan_readiness': max(56, s['arkansas_strategic_plan_2035_readiness_pct']),
    'statewide_growth_readiness': mc.get('executive', {}).get('statewide_growth_readiness', 48),
    'neighborhood_organizing_readiness': mc.get('executive', {}).get('neighborhood_organizing_readiness', 50),
    'civic_atlas_readiness': 52,
    'rollout_phase': 0,
    'rollout_phase_title': 'Private Development',
    'planning_phase_complete': True,
    'planning_constitution_complete': True,
    'eighty_builds_complete': True,
    'implementation_phase': 'strategic_scorecard_next',
    'public_launch_readiness': s['public_launch_readiness_pct'],
    'public_launch_label': 'Early Foundation',
    'public_launch_recommended': False,
}

mc['arkansas_strategic_plan_2035_inventory'] = {
    'readiness_score': s['arkansas_strategic_plan_2035_readiness_pct'],
    'strategic_goals': s['strategic_goals_total'],
    'horizon_year': 2035,
    'strategic_scorecard_live': s['strategic_scorecard_live'],
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 84
        bar['note'] = 'Build #84 — Arkansas Strategic Plan 2035.'
    if bar['id'] == 'master_plan':
        bar['value'] = max(bar.get('value', 0), mc['executive']['master_plan_readiness'])
        bar['note'] = f"7 goals · {s['five_year_milestones_achieved']}/{s['five_year_milestones_total']} 5yr milestones."

if not any(b.get('id') == 'arkansas_strategic_plan_2035' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'arkansas_strategic_plan_2035',
        'label': 'Strategic Plan 2035',
        'value': s['arkansas_strategic_plan_2035_readiness_pct'],
        'max': 100,
        'note': f"{s['counties_active']}/{s['participants_target']} counties/participants · scorecard {'live' if s['strategic_scorecard_live'] else 'planned'}.",
    })
else:
    for bar in mc['progress_bars']:
        if bar['id'] == 'arkansas_strategic_plan_2035':
            bar['value'] = s['arkansas_strategic_plan_2035_readiness_pct']

mc['builds'].insert(0, {
    'number': 84,
    'title': title,
    'version': '1.88.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Roadmap to statewide civic education institution by 2035',
    'summary': (
        f"7 strategic goals, 10 metrics, 5yr/10yr milestones, annual review, "
        f"{s['arkansas_strategic_plan_2035_readiness_pct']}% readiness. "
        f"{s['five_year_milestones_achieved']}/{s['five_year_milestones_total']} 5yr · "
        f"scorecard {'live' if s['strategic_scorecard_live'] else 'not live'}."
    ),
    'files_created': [
        'data/arkansas-strategic-plan-2035.json',
        'docs/MASTER_ARKANSAS_STRATEGIC_PLAN_2035.md',
        'builds/084-arkansas-strategic-plan-2035.md',
        'mission-control/arkansas-strategic-plan-2035.html',
        'scripts/gen-arkansas-strategic-plan-2035.py',
        'scripts/update-mc-build84.py',
    ],
    'files_modified': ['js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml'],
    'pages_created': ['/mission-control/arkansas-strategic-plan-2035.html'],
    'decisions_made': [
        'Strategic Plan distinct from Master Build Plan — accomplishment vs construction',
        '7 strategic goals through 2035',
        '10-metric strategic scorecard',
        '5-year and 10-year milestones',
        'Annual strategic review — living document',
        "Founder's commitment — informed citizens essential",
        f"{s['arkansas_strategic_plan_2035_readiness_pct']}% readiness — blueprint only",
    ],
    'open_questions': [
        'Build #84 vs BUILD_PLAN.md — unify strategic and build tracking?',
        'Milestone achievement — manual or automated from MC data?',
        'Trust score — pull from Public Trust (#82)?',
        'Annual review — calendar workflow in MC?',
    ],
    'risks': sp['catalog_gaps'][:4],
    'next_recommended': 85,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/arkansas-strategic-plan-2035.html',
    'review_status': 'complete',
})

mc['briefing'] = {
    'what_built': 'Arkansas Strategic Plan 2035 v1.0 — decade accomplishment roadmap',
    'building_now': '84 builds — strategic scorecard next',
    'blocked': ['Strategic scorecard', 'Annual review workflow', 'Milestone tracking', 'Risk dashboard'],
    'ready_public': ['7 strategic goals', '10 metrics', '5yr/10yr milestones', "Founder's commitment"],
    'next': 'Build #85 — Strategic scorecard & annual review components',
}

if not any(n.get('id') == 'arkansas_strategic_plan_2035' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'arkansas_strategic_plan_2035',
        'label': 'Strategic Plan 2035',
        'href': '/mission-control/arkansas-strategic-plan-2035.html',
        'status': 'complete',
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
