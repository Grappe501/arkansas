import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json', encoding='utf-8') as f:
    mc = json.load(f)

title = 'Citizens United Facts Master PMO & Execution Office v1.0'

with open(root / 'data/pmo-execution-office.json', encoding='utf-8') as f:
    peo = json.load(f)

s = peo['summary']
prior_maturity = mc.get('executive', {}).get('institutional_maturity_pct', 32)

mc['version'] = '1.93.0'
mc['build'] = 89
mc['updated'] = '2026-07-09'
mc['pmo_execution_office'] = '/data/pmo-execution-office.json'
mc['pmo_execution_office_dashboard'] = '/mission-control/pmo-execution-office.html'

mc['executive'] = {
    'overall_completion': 89,
    'current_build': {'number': 89, 'title': title},
    'active_phase': 'PMO Execution Office → War Room',
    'last_completed': 'Master Execution Schedule',
    'next_build': {'number': 90, 'title': 'Executive war room & countdown dashboard components'},
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
    'arkansas_strategic_plan_2035_readiness': mc.get('executive', {}).get('arkansas_strategic_plan_2035_readiness', 55),
    'master_launch_plan_readiness': mc.get('executive', {}).get('master_launch_plan_readiness', 54),
    'arkansas_civic_reach_participation_readiness': mc.get('executive', {}).get('arkansas_civic_reach_participation_readiness', 56),
    'launch_campaign_first_100_days_readiness': mc.get('executive', {}).get('launch_campaign_first_100_days_readiness', 57),
    'execution_schedule_readiness': mc.get('executive', {}).get('execution_schedule_readiness', 56),
    'pmo_execution_office_readiness': s['pmo_execution_office_readiness_pct'],
    'mc2_readiness': 42,
    'ai_engine_readiness': 34,
    'content_factory_readiness': 30,
    'education_academy_readiness': 26,
    'observatory_readiness': mc.get('executive', {}).get('observatory_readiness', 43),
    'outreach_readiness': mc.get('executive', {}).get('outreach_readiness', 44),
    'county_os_readiness': mc.get('executive', {}).get('county_os_readiness', 28),
    'campaign_os_readiness': mc.get('executive', {}).get('campaign_os_readiness', 44),
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
    'launch_strategy_readiness': mc.get('executive', {}).get('launch_strategy_readiness', 44),
    'pmo_readiness': max(s['pmo_execution_office_readiness_pct'], mc.get('executive', {}).get('pmo_readiness', 48)),
    'master_plan_readiness': mc.get('executive', {}).get('master_plan_readiness', 56),
    'statewide_growth_readiness': mc.get('executive', {}).get('statewide_growth_readiness', 48),
    'neighborhood_organizing_readiness': mc.get('executive', {}).get('neighborhood_organizing_readiness', 50),
    'civic_atlas_readiness': 52,
    'rollout_phase': 0,
    'rollout_phase_title': 'Private Development',
    'planning_phase_complete': True,
    'planning_constitution_complete': True,
    'eighty_builds_complete': True,
    'implementation_phase': 'executive_war_room_next',
    'public_launch_readiness': mc.get('executive', {}).get('public_launch_readiness', 8),
    'public_launch_label': 'Early Foundation',
    'public_launch_recommended': False,
    'completion_target_date': s['completion_target_date'],
    'days_remaining_to_completion': s['days_remaining'],
    'mission_complete_label': 'Mission Complete — January 2027',
    'connected_citizen_goal_pct': mc.get('executive', {}).get('connected_citizen_goal_pct', 15),
}

mc['pmo_execution_office_inventory'] = {
    'readiness_score': s['pmo_execution_office_readiness_pct'],
    'completion_target_date': s['completion_target_date'],
    'days_remaining': s['days_remaining'],
    'pmo_dashboard_live': s['pmo_dashboard_live'],
    'portfolios_total': s['portfolios_total'],
    'portfolio_owners_assigned': s['portfolio_owners_assigned'],
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 89
        bar['note'] = f"Build #89 — PMO Execution Office. {s['days_remaining']} days to Jan 2027."
    if bar['id'] == 'pmo':
        bar['value'] = max(bar.get('value', 0), mc['executive']['pmo_readiness'])
        bar['note'] = f"PMO cockpit planned · {s['portfolio_owners_assigned']}/{s['portfolios_total']} owners."
    if bar.get('id') == 'execution_schedule':
        bar['note'] = f"{s['days_remaining']} days · PMO coordinates execution."

if not any(b.get('id') == 'pmo_execution_office' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'pmo_execution_office',
        'label': 'PMO Execution Office',
        'value': s['pmo_execution_office_readiness_pct'],
        'max': 100,
        'note': f"{s['milestones_achieved']}/{s['milestones_total']} milestones · dashboard {'live' if s['pmo_dashboard_live'] else 'planned'}.",
    })
else:
    for bar in mc['progress_bars']:
        if bar['id'] == 'pmo_execution_office':
            bar['value'] = s['pmo_execution_office_readiness_pct']

mc['builds'].insert(0, {
    'number': 89,
    'title': title,
    'version': '1.93.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Central execution office — deliver institution by January 2027',
    'summary': (
        f"12 portfolios, project registry, milestones, risk/decision registers, dependency map, "
        f"volunteer assignments, weekly briefing, quality gates. "
        f"{s['pmo_execution_office_readiness_pct']}% readiness · "
        f"{s['milestones_achieved']}/{s['milestones_total']} milestones · "
        f"dashboard {'live' if s['pmo_dashboard_live'] else 'not live'}."
    ),
    'files_created': [
        'data/pmo-execution-office.json',
        'docs/MASTER_PMO_EXECUTION_OFFICE.md',
        'builds/089-pmo-execution-office.md',
        'mission-control/pmo-execution-office.html',
        'scripts/gen-pmo-execution-office.py',
        'scripts/update-mc-build89.py',
    ],
    'files_modified': [
        'js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml',
        'data/execution-schedule.json',
    ],
    'pages_created': ['/mission-control/pmo-execution-office.html'],
    'decisions_made': [
        'PMO = central execution office for Jan 2027 mission complete',
        'Extends PMO #54 with portfolio, registry, milestone, risk, decision systems',
        '12 executive portfolios with owner/milestone/progress model',
        'Quality gates — completion means operational readiness',
        'Weekly executive briefing — one authoritative report',
        f"{s['pmo_execution_office_readiness_pct']}% readiness — blueprint only",
    ],
    'open_questions': [
        'Unify PMO #54 and #89 dashboards?',
        'Project registry — builds[] or separate PMO DB?',
        'Weekly briefing — auto from MC JSON or manual?',
        'Portfolio owners — volunteer or executive assignment?',
    ],
    'risks': peo['catalog_gaps'][:4],
    'next_recommended': 90,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/pmo-execution-office.html',
    'review_status': 'complete',
})

mc['briefing'] = {
    'what_built': 'PMO & Execution Office v1.0 — Building the Institution With Discipline',
    'building_now': '89 builds — executive war room next',
    'blocked': ['PMO dashboard UI', 'Project registry', 'Auto weekly briefing', 'Dependency visualization'],
    'ready_public': ['Portfolio model', 'Milestone acceptance criteria', 'Risk register', 'Quality gates'],
    'next': 'Build #90 — Executive war room & countdown dashboard components',
}

if not any(n.get('id') == 'pmo_execution_office' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'pmo_execution_office',
        'label': 'PMO Execution Office',
        'href': '/mission-control/pmo-execution-office.html',
        'status': 'complete',
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
