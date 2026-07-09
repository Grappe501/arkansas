import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json', encoding='utf-8') as f:
    mc = json.load(f)

title = 'Citizens United Facts Master Arkansas Civic Operating System (ACOS 2.0)'

with open(root / 'data/arkansas-civic-operating-system.json', encoding='utf-8') as f:
    acos = json.load(f)

s = acos['summary']
prior_maturity = mc.get('executive', {}).get('institutional_maturity_pct', 32)

mc['version'] = '2.00.0'
mc['build'] = 96
mc['updated'] = '2026-07-09'
mc['arkansas_civic_operating_system'] = '/data/arkansas-civic-operating-system.json'
mc['arkansas_civic_operating_system_dashboard'] = '/mission-control/arkansas-civic-operating-system.html'

mc['executive'] = {
    'overall_completion': 96,
    'current_build': {'number': 96, 'title': title},
    'active_phase': 'Civic OS → War Room',
    'last_completed': 'Master Action Network',
    'next_build': {'number': 97, 'title': 'Executive war room & countdown dashboard components'},
    'github_status': 'connected',
    'netlify_status': 'production_healthy',
    'content_readiness': 28,
    'research_readiness': mc.get('executive', {}).get('research_readiness', 43),
    'data_viz_readiness': 12,
    'signup_funnel_readiness': 26,
    'civic_action_readiness': mc.get('executive', {}).get('civic_action_readiness', 50),
    'coalition_readiness': 44,
    'data_model_readiness': mc.get('executive', {}).get('data_model_readiness', 58),
    'route_inventory_readiness': 18,
    'component_registry_readiness': 22,
    'facts_framework_readiness': 14,
    'knowledge_atlas_readiness': mc.get('executive', {}).get('knowledge_atlas_readiness', 58),
    'platform_architecture_readiness': max(s['arkansas_civic_operating_system_readiness_pct'], mc.get('executive', {}).get('platform_architecture_readiness', 24)),
    'repository_structure_readiness': 28,
    'database_schema_readiness': 42,
    'wireframe_readiness': 38,
    'contact_intelligence_readiness': 34,
    'relationship_os_readiness': mc.get('executive', {}).get('relationship_os_readiness', 54),
    'institutional_ai_readiness': mc.get('executive', {}).get('institutional_ai_readiness', 57),
    'ai_institution_readiness': mc.get('executive', {}).get('ai_institution_readiness', 57),
    'localbrain_architecture_readiness': mc.get('executive', {}).get('localbrain_architecture_readiness', 60),
    'civic_knowledge_platform_readiness': mc.get('executive', {}).get('civic_knowledge_platform_readiness', 58),
    'executive_institution_readiness': mc.get('executive', {}).get('executive_institution_readiness', 50),
    'master_arkansas_action_network_readiness': mc.get('executive', {}).get('master_arkansas_action_network_readiness', 50),
    'arkansas_civic_operating_system_readiness': s['arkansas_civic_operating_system_readiness_pct'],
    'coalition_network_readiness': 44,
    'citizen_action_center_readiness': mc.get('executive', {}).get('citizen_action_center_readiness', 42),
    'campaign_finance_observatory_readiness': mc.get('executive', {}).get('campaign_finance_observatory_readiness', 38),
    'arkansas_action_network_readiness': mc.get('executive', {}).get('arkansas_action_network_readiness', 50),
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
    'institutional_operating_manual_readiness': mc.get('executive', {}).get('institutional_operating_manual_readiness', 60),
    'mc2_readiness': 42,
    'ai_engine_readiness': mc.get('executive', {}).get('ai_engine_readiness', 57),
    'content_factory_readiness': 30,
    'education_academy_readiness': 26,
    'observatory_readiness': mc.get('executive', {}).get('observatory_readiness', 43),
    'outreach_readiness': mc.get('executive', {}).get('outreach_readiness', 44),
    'county_os_readiness': max(s['arkansas_civic_operating_system_readiness_pct'], mc.get('executive', {}).get('county_os_readiness', 28)),
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
    'systems_integration_readiness': max(s['arkansas_civic_operating_system_readiness_pct'], mc.get('executive', {}).get('systems_integration_readiness', 44)),
    'production_matrix_readiness': 39,
    'visitor_journey_readiness': max(s['arkansas_civic_operating_system_readiness_pct'], mc.get('executive', {}).get('visitor_journey_readiness', 40)),
    'technical_architecture_readiness': max(s['arkansas_civic_operating_system_readiness_pct'], mc.get('executive', {}).get('technical_architecture_readiness', 38)),
    'governance_readiness': mc.get('executive', {}).get('governance_readiness', 50),
    'build_bible_readiness': 49,
    'data_architecture_readiness': mc.get('executive', {}).get('data_architecture_readiness', 58),
    'ux_architecture_readiness': max(s['arkansas_civic_operating_system_readiness_pct'], mc.get('executive', {}).get('ux_architecture_readiness', 39)),
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

mc['arkansas_civic_operating_system_inventory'] = {
    'readiness_score': s['arkansas_civic_operating_system_readiness_pct'],
    'platform_live': s['platform_live'],
    'single_login_live': s['single_login_live'],
    'personal_workspace_live': s['personal_workspace_live'],
    'ai_assistant_live': s['ai_assistant_live'],
    'user_accounts': s['user_accounts'],
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 96
        bar['note'] = f"Build #96 — ACOS 2.0. {s['days_remaining']} days to Jan 2027."
    if bar.get('id') == 'master_arkansas_action_network':
        bar['note'] = f"Action Network · {mc.get('executive', {}).get('master_arkansas_action_network_readiness', 50)}% readiness."

if not any(b.get('id') == 'arkansas_civic_operating_system' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'arkansas_civic_operating_system',
        'label': 'ACOS 2.0',
        'value': s['arkansas_civic_operating_system_readiness_pct'],
        'max': 100,
        'note': f"{s['user_accounts']} accounts · workspace {'live' if s['personal_workspace_live'] else 'planned'}.",
    })
else:
    for bar in mc['progress_bars']:
        if bar['id'] == 'arkansas_civic_operating_system':
            bar['value'] = s['arkansas_civic_operating_system_readiness_pct']

mc['builds'].insert(0, {
    'number': 96,
    'title': title,
    'version': '2.00.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'One login — personalized civic workspace — platform OS for Arkansas',
    'summary': (
        f"15 workspace modules, 6 user roles, personalized learning/community, volunteer/leader/"
        f"coalition/executive workspaces, AI assistant, notifications, privacy. "
        f"{s['arkansas_civic_operating_system_readiness_pct']}% readiness · "
        f"{s['user_accounts']} accounts · platform {'live' if s['platform_live'] else 'not live'}."
    ),
    'files_created': [
        'data/arkansas-civic-operating-system.json',
        'docs/MASTER_ARKANSAS_CIVIC_OPERATING_SYSTEM.md',
        'builds/096-arkansas-civic-operating-system.md',
        'mission-control/arkansas-civic-operating-system.html',
        'scripts/gen-arkansas-civic-operating-system.py',
        'scripts/update-mc-build96.py',
    ],
    'files_modified': [
        'js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml',
    ],
    'pages_created': ['/mission-control/arkansas-civic-operating-system.html'],
    'decisions_made': [
        'ACOS 2.0 — platform OS layer above County ACOS (#77)',
        'One login, one platform, role-based permissions',
        'Personal civic workspace — 15 modules growing with involvement',
        'AI personal assistant per account grounded in institutional knowledge',
        'MC anonymous aggregate trends — respects individual privacy',
        f"{s['arkansas_civic_operating_system_readiness_pct']}% readiness — blueprint only",
    ],
    'open_questions': [
        'Auth provider — Supabase Auth vs custom?',
        'Workspace shell — SPA vs server-rendered dashboards?',
        'How does County ACOS (#77) nest inside platform OS?',
        'PWA / daily companion mobile experience timeline?',
    ],
    'risks': acos['catalog_gaps'][:4],
    'next_recommended': 97,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/arkansas-civic-operating-system.html',
    'review_status': 'complete',
})

mc['briefing'] = {
    'what_built': 'Master Arkansas Civic Operating System (ACOS 2.0) — One Login. One Platform.',
    'building_now': '96 builds — executive war room next',
    'blocked': ['Single login', 'Personal workspace', 'AI assistant', 'Role permissions'],
    'ready_public': ['Workspace modules spec', 'Role workspaces', 'Privacy controls', 'MC integration model'],
    'next': 'Build #97 — Executive war room & countdown dashboard components',
}

if not any(n.get('id') == 'arkansas_civic_operating_system' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'arkansas_civic_operating_system',
        'label': 'ACOS 2.0',
        'href': '/mission-control/arkansas-civic-operating-system.html',
        'status': 'complete',
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
