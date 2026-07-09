import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json', encoding='utf-8') as f:
    mc = json.load(f)

title = 'Citizens United Facts Master Launch Campaign & First 100 Days Blueprint v1.0'

with open(root / 'data/launch-campaign-first-100-days.json', encoding='utf-8') as f:
    lc = json.load(f)

s = lc['summary']
prior_maturity = mc.get('executive', {}).get('institutional_maturity_pct', 32)

mc['version'] = '1.91.0'
mc['build'] = 87
mc['updated'] = '2026-07-09'
mc['launch_campaign_first_100_days'] = '/data/launch-campaign-first-100-days.json'
mc['launch_campaign_first_100_days_dashboard'] = '/mission-control/launch-campaign-first-100-days.html'

mc['executive'] = {
    'overall_completion': 87,
    'current_build': {'number': 87, 'title': title},
    'active_phase': 'Launch Campaign → Campaign Tracker',
    'last_completed': 'Arkansas Civic Reach & Participation',
    'next_build': {'number': 88, 'title': 'First 100 days dashboard & campaign tracker components'},
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
    'launch_campaign_first_100_days_readiness': s['launch_campaign_first_100_days_readiness_pct'],
    'mc2_readiness': 42,
    'ai_engine_readiness': 34,
    'content_factory_readiness': 30,
    'education_academy_readiness': 26,
    'observatory_readiness': mc.get('executive', {}).get('observatory_readiness', 43),
    'outreach_readiness': mc.get('executive', {}).get('outreach_readiness', 44),
    'county_os_readiness': mc.get('executive', {}).get('county_os_readiness', 28),
    'campaign_os_readiness': max(s['launch_campaign_first_100_days_readiness_pct'] - 10, 34),
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
    'statewide_growth_readiness': mc.get('executive', {}).get('statewide_growth_readiness', 48),
    'neighborhood_organizing_readiness': mc.get('executive', {}).get('neighborhood_organizing_readiness', 50),
    'civic_atlas_readiness': 52,
    'rollout_phase': 0,
    'rollout_phase_title': 'Private Development',
    'planning_phase_complete': True,
    'planning_constitution_complete': True,
    'eighty_builds_complete': True,
    'implementation_phase': 'first_100_days_tracker_next',
    'public_launch_readiness': s['public_launch_readiness_pct'],
    'public_launch_label': 'Early Foundation',
    'public_launch_recommended': False,
    'launch_target_date': s['launch_date'],
    'connected_citizen_goal_pct': mc.get('executive', {}).get('connected_citizen_goal_pct', 15),
}

mc['launch_campaign_first_100_days_inventory'] = {
    'readiness_score': s['launch_campaign_first_100_days_readiness_pct'],
    'launch_date': s['launch_date'],
    'campaign_day': s['campaign_day'],
    'campaign_dashboard_live': s['campaign_dashboard_live'],
    'first_100_days_campaign': True,
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 87
        bar['note'] = 'Build #87 — Launch Campaign & First 100 Days.'
    if bar['id'] == 'launch':
        bar['value'] = max(bar.get('value', 0), s['launch_campaign_first_100_days_readiness_pct'])
        bar['note'] = f"First 100 days · day {s['campaign_day']}/{s['campaign_days']} · dashboard {'live' if s['campaign_dashboard_live'] else 'planned'}."

if not any(b.get('id') == 'launch_campaign_first_100_days' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'launch_campaign_first_100_days',
        'label': 'First 100 Days',
        'value': s['launch_campaign_first_100_days_readiness_pct'],
        'max': 100,
        'note': f"{s['new_participants']} participants · report {'published' if s['first_100_days_report_published'] else 'pending'}.",
    })
else:
    for bar in mc['progress_bars']:
        if bar['id'] == 'launch_campaign_first_100_days':
            bar['value'] = s['launch_campaign_first_100_days_readiness_pct']

mc['builds'].insert(0, {
    'number': 87,
    'title': title,
    'version': '1.91.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'First 100 days after Jan 2027 launch — statewide movement campaign',
    'summary': (
        f"3 phases, 11 dashboard indicators, weekly rhythm, county challenge, "
        f"{s['launch_campaign_first_100_days_readiness_pct']}% readiness. "
        f"Day {s['campaign_day']}/{s['campaign_days']} · "
        f"campaign {'started' if s['campaign_started'] else 'not started'}."
    ),
    'files_created': [
        'data/launch-campaign-first-100-days.json',
        'docs/MASTER_LAUNCH_CAMPAIGN_FIRST_100_DAYS.md',
        'builds/087-launch-campaign-first-100-days.md',
        'mission-control/launch-campaign-first-100-days.html',
        'scripts/gen-launch-campaign-first-100-days.py',
        'scripts/update-mc-build87.py',
    ],
    'files_modified': ['js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml'],
    'pages_created': ['/mission-control/launch-campaign-first-100-days.html'],
    'decisions_made': [
        'First 100 days = dedicated operational campaign in MC',
        '3 phases: awareness (1-30), activation (31-60), expansion (61-100)',
        '5 primary mission objectives',
        '11-indicator campaign dashboard — leadership reviews daily',
        'Weekly operations rhythm · county challenge · volunteer development',
        "Founder standard — most trusted, help understand not tell what to think",
        f"{s['launch_campaign_first_100_days_readiness_pct']}% readiness — blueprint only",
    ],
    'open_questions': [
        'Build #87 vs Launch Plan (#85) — campaign vs readiness checklist?',
        'Day counter — auto from launch date or manual?',
        'First 100 Days Report — auto-generate from MC data?',
        'Phase transitions — automatic at day 30/60?',
    ],
    'risks': lc['catalog_gaps'][:4],
    'next_recommended': 88,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/launch-campaign-first-100-days.html',
    'review_status': 'complete',
})

mc['briefing'] = {
    'what_built': 'Launch Campaign & First 100 Days v1.0 — post-launch movement blueprint',
    'building_now': '87 builds — campaign tracker next',
    'blocked': ['Campaign dashboard', 'Day counter', 'Phase tracker', 'First 100 Days report'],
    'ready_public': ['3 phases', '5 objectives', 'Weekly rhythm', "Founder's standard"],
    'next': 'Build #88 — First 100 days dashboard & campaign tracker components',
}

if not any(n.get('id') == 'launch_campaign_first_100_days' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'launch_campaign_first_100_days',
        'label': 'First 100 Days',
        'href': '/mission-control/launch-campaign-first-100-days.html',
        'status': 'complete',
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
