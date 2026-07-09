import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json', encoding='utf-8') as f:
    mc = json.load(f)

title = 'Citizens United Facts Master Institutional Operating Manual v1.0'

with open(root / 'data/institutional-operating-manual.json', encoding='utf-8') as f:
    iom = json.load(f)

s = iom['summary']
prior_maturity = mc.get('executive', {}).get('institutional_maturity_pct', 32)

mc['version'] = '1.94.0'
mc['build'] = 90
mc['updated'] = '2026-07-09'
mc['institutional_operating_manual'] = '/data/institutional-operating-manual.json'
mc['institutional_operating_manual_dashboard'] = '/mission-control/institutional-operating-manual.html'

mc['executive'] = {
    'overall_completion': 90,
    'current_build': {'number': 90, 'title': title},
    'active_phase': 'Institutional Operating Manual → War Room',
    'last_completed': 'PMO & Execution Office',
    'next_build': {'number': 91, 'title': 'Executive war room & countdown dashboard components'},
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
    'pmo_execution_office_readiness': mc.get('executive', {}).get('pmo_execution_office_readiness', 60),
    'institutional_operating_manual_readiness': s['institutional_operating_manual_readiness_pct'],
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
    'pmo_readiness': mc.get('executive', {}).get('pmo_readiness', 60),
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

mc['institutional_operating_manual_inventory'] = {
    'readiness_score': s['institutional_operating_manual_readiness_pct'],
    'system_manuals_complete': s['system_manuals_complete'],
    'system_manuals_total': s['system_manuals_total'],
    'sops_written': s['sops_written'],
    'operations_dashboard_live': s['operations_dashboard_live'],
    'institutional_memory_entries': s['institutional_memory_entries'],
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 90
        bar['note'] = f"Build #90 — Operating Manual. {s['days_remaining']} days to Jan 2027."
    if bar.get('id') == 'pmo_execution_office':
        bar['note'] = f"PMO coordinates · {s['sops_written']}/{s['sops_total']} SOPs written."

if not any(b.get('id') == 'institutional_operating_manual' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'institutional_operating_manual',
        'label': 'Operating Manual',
        'value': s['institutional_operating_manual_readiness_pct'],
        'max': 100,
        'note': f"{s['system_manuals_complete']}/{s['system_manuals_total']} manuals · dashboard {'live' if s['operations_dashboard_live'] else 'planned'}.",
    })
else:
    for bar in mc['progress_bars']:
        if bar['id'] == 'institutional_operating_manual':
            bar['value'] = s['institutional_operating_manual_readiness_pct']

mc['builds'].insert(0, {
    'number': 90,
    'title': title,
    'version': '1.94.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Institutional continuity — institution continues without founders',
    'summary': (
        f"13 playbook systems, 10 SOPs, role manuals, institutional memory, decision framework, "
        f"change management, emergency continuity, documentation standards. "
        f"{s['institutional_operating_manual_readiness_pct']}% readiness · "
        f"{s['system_manuals_complete']}/{s['system_manuals_total']} manuals · "
        f"{s['sops_written']}/{s['sops_total']} SOPs."
    ),
    'files_created': [
        'data/institutional-operating-manual.json',
        'docs/MASTER_INSTITUTIONAL_OPERATING_MANUAL.md',
        'builds/090-institutional-operating-manual.md',
        'mission-control/institutional-operating-manual.html',
        'scripts/gen-institutional-operating-manual.py',
        'scripts/update-mc-build90.py',
    ],
    'files_modified': [
        'js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml',
    ],
    'pages_created': ['/mission-control/institutional-operating-manual.html'],
    'decisions_made': [
        'Operating Manual = institution continues if founders walk away',
        '13 system playbooks — each independently understandable',
        'SOPs for every recurring activity — no tribal knowledge',
        'Institutional memory permanently preserved in MC',
        'Decision framework — six questions before major decisions',
        'Documentation standards — purpose, owner, version, review schedule',
        f"{s['institutional_operating_manual_readiness_pct']}% readiness — blueprint only",
    ],
    'open_questions': [
        'SOP registry — separate from builds?',
        'Institutional memory — link to PMO decision register?',
        'Volunteer knowledge base — MC portal or wiki?',
        'Annual review — who conducts first cycle?',
    ],
    'risks': iom['catalog_gaps'][:4],
    'next_recommended': 91,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/institutional-operating-manual.html',
    'review_status': 'complete',
})

mc['briefing'] = {
    'what_built': 'Institutional Operating Manual v1.0 — If Every Founder Walked Away Tomorrow',
    'building_now': '90 builds — executive war room next',
    'blocked': ['Operations dashboard', 'SOP registry', 'Institutional memory store', 'Role manuals'],
    'ready_public': ['Playbook structure', 'Decision framework', 'Documentation standards', 'Founder legacy'],
    'next': 'Build #91 — Executive war room & countdown dashboard components',
}

if not any(n.get('id') == 'institutional_operating_manual' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'institutional_operating_manual',
        'label': 'Operating Manual',
        'href': '/mission-control/institutional-operating-manual.html',
        'status': 'complete',
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
