import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json', encoding='utf-8') as f:
    mc = json.load(f)

title = 'Citizens United Facts Master Arkansas Civic Reach & Participation Strategy v1.0'

with open(root / 'data/arkansas-civic-reach-participation.json', encoding='utf-8') as f:
    cr = json.load(f)

s = cr['summary']
prior_maturity = mc.get('executive', {}).get('institutional_maturity_pct', 32)

mc['version'] = '1.90.0'
mc['build'] = 86
mc['updated'] = '2026-07-09'
mc['arkansas_civic_reach_participation'] = '/data/arkansas-civic-reach-participation.json'
mc['arkansas_civic_reach_participation_dashboard'] = '/mission-control/arkansas-civic-reach-participation.html'

mc['executive'] = {
    'overall_completion': 86,
    'current_build': {'number': 86, 'title': title},
    'active_phase': 'Civic Reach → Reach Dashboard',
    'last_completed': 'Master Launch Plan',
    'next_build': {'number': 87, 'title': 'Civic reach dashboard & county/city score components'},
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
    'arkansas_civic_reach_participation_readiness': s['arkansas_civic_reach_participation_readiness_pct'],
    'mc2_readiness': 42,
    'ai_engine_readiness': 34,
    'content_factory_readiness': 30,
    'education_academy_readiness': 26,
    'observatory_readiness': mc.get('executive', {}).get('observatory_readiness', 43),
    'outreach_readiness': max(s['arkansas_civic_reach_participation_readiness_pct'] - 12, mc.get('executive', {}).get('outreach_readiness', 34)),
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
    'launch_strategy_readiness': mc.get('executive', {}).get('launch_strategy_readiness', 44),
    'pmo_readiness': 46,
    'master_plan_readiness': mc.get('executive', {}).get('master_plan_readiness', 56),
    'statewide_growth_readiness': max(s['arkansas_civic_reach_participation_readiness_pct'] - 8, mc.get('executive', {}).get('statewide_growth_readiness', 48)),
    'neighborhood_organizing_readiness': mc.get('executive', {}).get('neighborhood_organizing_readiness', 50),
    'civic_atlas_readiness': 52,
    'rollout_phase': 0,
    'rollout_phase_title': 'Private Development',
    'planning_phase_complete': True,
    'planning_constitution_complete': True,
    'eighty_builds_complete': True,
    'implementation_phase': 'civic_reach_dashboard_next',
    'public_launch_readiness': s['public_launch_readiness_pct'],
    'public_launch_label': 'Early Foundation',
    'public_launch_recommended': False,
    'connected_citizen_goal_pct': s['connected_citizen_goal_pct'],
}

mc['arkansas_civic_reach_participation_inventory'] = {
    'readiness_score': s['arkansas_civic_reach_participation_readiness_pct'],
    'connected_citizen_goal_pct': s['connected_citizen_goal_pct'],
    'reach_dashboard_live': s['reach_dashboard_live'],
    'fifteen_percent_framework': True,
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 86
        bar['note'] = 'Build #86 — Civic Reach & Participation (15% goal).'
    if bar['id'] == 'outreach':
        bar['value'] = max(bar.get('value', 0), mc['executive']['outreach_readiness'])
        bar['note'] = f"15% goal · {s['counties_at_goal']}/{s['counties_total']} counties · {s['statewide_connected_participants']} connected."

if not any(b.get('id') == 'arkansas_civic_reach_participation' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'arkansas_civic_reach_participation',
        'label': 'Civic Reach',
        'value': s['arkansas_civic_reach_participation_readiness_pct'],
        'max': 100,
        'note': f"{s['connected_citizen_goal_pct']}% goal · dashboard {'live' if s['reach_dashboard_live'] else 'planned'}.",
    })
else:
    for bar in mc['progress_bars']:
        if bar['id'] == 'arkansas_civic_reach_participation':
            bar['value'] = s['arkansas_civic_reach_participation_readiness_pct']

mc['builds'].insert(0, {
    'number': 86,
    'title': title,
    'version': '1.90.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': '15% Connected Citizen Goal — reaching every community',
    'summary': (
        f"15% goal, 6 engagement levels, reach dashboard, county/city objectives, "
        f"{s['arkansas_civic_reach_participation_readiness_pct']}% readiness. "
        f"{s['statewide_connected_participants']} connected · "
        f"{s['counties_at_goal']}/{s['counties_total']} counties at goal."
    ),
    'files_created': [
        'data/arkansas-civic-reach-participation.json',
        'docs/MASTER_ARKANSAS_CIVIC_REACH_PARTICIPATION.md',
        'builds/086-arkansas-civic-reach-participation.md',
        'mission-control/arkansas-civic-reach-participation.html',
        'scripts/gen-arkansas-civic-reach-participation.py',
        'scripts/update-mc-build86.py',
    ],
    'files_modified': ['js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml'],
    'pages_created': ['/mission-control/arkansas-civic-reach-participation.html'],
    'decisions_made': [
        '15% Connected Citizen Goal per county and major city',
        'Participation = connection, not agreement',
        'Civic Reach Score formula specified',
        '6 engagement levels · quality over raw registration',
        'Ethical standards — trust over growth',
        'Rankings by educational reach, not political influence',
        f"{s['arkansas_civic_reach_participation_readiness_pct']}% readiness — blueprint only",
    ],
    'open_questions': [
        'Build #86 vs 200K goal (#64) — reconcile metrics?',
        'Registered voter data source — SOS integration?',
        '15% per county vs statewide average?',
        'Heat maps — Civic Atlas or new MC view?',
    ],
    'risks': cr['catalog_gaps'][:4],
    'next_recommended': 87,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/arkansas-civic-reach-participation.html',
    'review_status': 'complete',
})

mc['briefing'] = {
    'what_built': 'Civic Reach Strategy v1.0 — 15% Arkansas Engagement Framework',
    'building_now': '86 builds — civic reach dashboard next',
    'blocked': ['Reach dashboard', 'Civic Reach Score engine', 'Voter denominator', 'Heat maps'],
    'ready_public': ['15% goal', '6 engagement levels', 'Ethical standards', "Founder's standard"],
    'next': 'Build #87 — Civic reach dashboard & county/city score components',
}

if not any(n.get('id') == 'arkansas_civic_reach_participation' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'arkansas_civic_reach_participation',
        'label': 'Civic Reach',
        'href': '/mission-control/arkansas-civic-reach-participation.html',
        'status': 'complete',
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
