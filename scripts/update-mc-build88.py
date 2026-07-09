import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json', encoding='utf-8') as f:
    mc = json.load(f)

title = 'Citizens United Facts Master Execution Schedule v1.0'

with open(root / 'data/execution-schedule.json', encoding='utf-8') as f:
    es = json.load(f)

s = es['summary']
prior_maturity = mc.get('executive', {}).get('institutional_maturity_pct', 32)

mc['version'] = '1.92.0'
mc['build'] = 88
mc['updated'] = '2026-07-09'
mc['execution_schedule'] = '/data/execution-schedule.json'
mc['execution_schedule_dashboard'] = '/mission-control/execution-schedule.html'

mc['executive'] = {
    'overall_completion': 88,
    'current_build': {'number': 88, 'title': title},
    'active_phase': 'Execution Schedule → War Room',
    'last_completed': 'Launch Campaign & First 100 Days',
    'next_build': {'number': 89, 'title': 'Executive war room & countdown dashboard components'},
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
    'execution_schedule_readiness': s['execution_schedule_readiness_pct'],
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
    'pmo_readiness': max(s['execution_schedule_readiness_pct'] - 8, 46),
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
    'public_launch_readiness': s['public_launch_readiness_pct'],
    'public_launch_label': 'Early Foundation',
    'public_launch_recommended': False,
    'completion_target_date': s['completion_target_date'],
    'days_remaining_to_completion': s['days_remaining'],
    'mission_complete_label': 'Mission Complete — January 2027',
    'connected_citizen_goal_pct': mc.get('executive', {}).get('connected_citizen_goal_pct', 15),
}

mc['execution_schedule_inventory'] = {
    'readiness_score': s['execution_schedule_readiness_pct'],
    'completion_target_date': s['completion_target_date'],
    'days_remaining': s['days_remaining'],
    'executive_war_room_live': s['executive_war_room_live'],
    'mission_complete_january_2027': True,
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 88
        bar['note'] = f"Build #88 — Execution Schedule. {s['days_remaining']} days to Jan 2027."
    if bar['id'] == 'pmo':
        bar['value'] = max(bar.get('value', 0), mc['executive']['pmo_readiness'])
        bar['note'] = f"Mission complete Jan 2027 · {s['days_remaining']} days remaining."

if not any(b.get('id') == 'execution_schedule' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'execution_schedule',
        'label': 'Execution Schedule',
        'value': s['execution_schedule_readiness_pct'],
        'max': 100,
        'note': f"{s['days_remaining']} days · war room {'live' if s['executive_war_room_live'] else 'planned'}.",
    })
else:
    for bar in mc['progress_bars']:
        if bar['id'] == 'execution_schedule':
            bar['value'] = s['execution_schedule_readiness_pct']

mc['builds'].insert(0, {
    'number': 88,
    'title': title,
    'version': '1.92.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'January 2027 V1 completion target — master execution countdown',
    'summary': (
        f"Countdown, war room, critical path, 10 departments, Arkansas progress, "
        f"{s['execution_schedule_readiness_pct']}% readiness. "
        f"{s['days_remaining']} days to mission complete · war room "
        f"{'live' if s['executive_war_room_live'] else 'not live'}."
    ),
    'files_created': [
        'data/execution-schedule.json',
        'docs/MASTER_EXECUTION_SCHEDULE.md',
        'builds/088-execution-schedule.md',
        'mission-control/execution-schedule.html',
        'scripts/gen-execution-schedule.py',
        'scripts/update-mc-build88.py',
    ],
    'files_modified': [
        'js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml',
        'scripts/gen-arkansas-strategic-plan-2035.py', 'scripts/gen-master-launch-plan.py',
        'scripts/gen-launch-campaign-first-100-days.py',
        'docs/MASTER_ARKANSAS_STRATEGIC_PLAN_2035.md', 'docs/MASTER_LAUNCH_PLAN.md',
        'docs/MASTER_LAUNCH_CAMPAIGN_FIRST_100_DAYS.md',
    ],
    'pages_created': ['/mission-control/execution-schedule.html'],
    'decisions_made': [
        'January 2027 = V1 substantial completion — not construction start',
        'Mission Control countdown always displays days remaining',
        'Executive War Room — leadership daily operating screen',
        'Department readiness: Planning → Building → Testing → Ready → Complete',
        'Timeline alignment for Builds #84, #85, #87',
        'Every build exists to complete institution by January 2027',
        f"{s['execution_schedule_readiness_pct']}% readiness — blueprint only",
    ],
    'open_questions': [
        'Overall completion % — build count vs V1 deliverable checklist?',
        'War room — separate page or MC home overlay?',
        'Critical path — manual PM or auto from dependencies?',
        'Department stages — who updates?',
    ],
    'risks': es['catalog_gaps'][:4],
    'next_recommended': 89,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/execution-schedule.html',
    'review_status': 'complete',
})

mc['briefing'] = {
    'what_built': 'Execution Schedule v1.0 — Mission Complete by January 2027',
    'building_now': '88 builds — executive war room next',
    'blocked': ['War room UI', 'Live countdown', 'Critical path tracker', 'Department automation'],
    'ready_public': ['Countdown spec', 'War room panels', 'Timeline alignment', 'Governing principle'],
    'next': 'Build #89 — Executive war room & countdown dashboard components',
}

if not any(n.get('id') == 'execution_schedule' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'execution_schedule',
        'label': 'Execution Schedule',
        'href': '/mission-control/execution-schedule.html',
        'status': 'complete',
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
