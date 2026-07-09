import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json', encoding='utf-8') as f:
    mc = json.load(f)

title = 'Citizens United Facts Master Launch Plan v1.0'

with open(root / 'data/master-launch-plan.json', encoding='utf-8') as f:
    lp = json.load(f)

s = lp['summary']
prior_maturity = mc.get('executive', {}).get('institutional_maturity_pct', 32)

mc['version'] = '1.89.0'
mc['build'] = 85
mc['updated'] = '2026-07-09'
mc['master_launch_plan'] = '/data/master-launch-plan.json'
mc['master_launch_plan_dashboard'] = '/mission-control/master-launch-plan.html'

mc['executive'] = {
    'overall_completion': 85,
    'current_build': {'number': 85, 'title': title},
    'active_phase': 'Launch Plan → Readiness Dashboard',
    'last_completed': 'Arkansas Strategic Plan 2035',
    'next_build': {'number': 86, 'title': 'Launch readiness dashboard & certification components'},
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
    'master_launch_plan_readiness': s['master_launch_plan_readiness_pct'],
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
    'launch_strategy_readiness': max(s['master_launch_plan_readiness_pct'] - 10, mc.get('executive', {}).get('launch_strategy_readiness', 39)),
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
    'implementation_phase': 'launch_readiness_dashboard_next',
    'public_launch_readiness': s['public_launch_readiness_pct'],
    'public_launch_label': 'Early Foundation',
    'public_launch_recommended': False,
    'launch_target_date': s['launch_date'],
}

mc['master_launch_plan_inventory'] = {
    'readiness_score': s['master_launch_plan_readiness_pct'],
    'launch_date': s['launch_date'],
    'checklist_complete': s['checklist_items_complete'],
    'checklist_total': s['checklist_items_total'],
    'launch_readiness_dashboard_live': s['launch_readiness_dashboard_live'],
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 85
        bar['note'] = 'Build #85 — Master Launch Plan (Jan 2027).'
    if bar['id'] == 'launch':
        bar['value'] = max(bar.get('value', 0), s['master_launch_plan_readiness_pct'])
        bar['note'] = f"Jan 2027 · {s['checklist_items_complete']}/{s['checklist_items_total']} checklist · map {'live' if s['arkansas_launch_map_live'] else 'planned'}."

if not any(b.get('id') == 'master_launch_plan' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'master_launch_plan',
        'label': 'Launch Plan 2027',
        'value': s['master_launch_plan_readiness_pct'],
        'max': 100,
        'note': f"{s['governance_certs_complete']}/{s['governance_certs_total']} certs · dashboard {'live' if s['launch_readiness_dashboard_live'] else 'planned'}.",
    })
else:
    for bar in mc['progress_bars']:
        if bar['id'] == 'master_launch_plan':
            bar['value'] = s['master_launch_plan_readiness_pct']

mc['builds'].insert(0, {
    'number': 85,
    'title': title,
    'version': '1.89.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'January 2027 operational readiness blueprint for launch',
    'summary': (
        f"36 checklist items, 11 readiness categories, launch map, governance certs, "
        f"{s['master_launch_plan_readiness_pct']}% readiness. "
        f"{s['checklist_items_complete']}/{s['checklist_items_total']} complete · "
        f"launch {s['launch_date']}."
    ),
    'files_created': [
        'data/master-launch-plan.json',
        'docs/MASTER_LAUNCH_PLAN.md',
        'builds/085-master-launch-plan.md',
        'mission-control/master-launch-plan.html',
        'scripts/gen-master-launch-plan.py',
        'scripts/update-mc-build85.py',
    ],
    'files_modified': ['js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml'],
    'pages_created': ['/mission-control/master-launch-plan.html'],
    'decisions_made': [
        'January 2027 launch target — operational checklist not wish list',
        '6 launch objective areas · 36 deliverables',
        '11-category launch readiness dashboard',
        'Arkansas Launch Map — public symbol of growth',
        '7 governance certifications before launch',
        'Distinct from Launch Strategy (#53) and Strategic Plan (#84)',
        f"{s['master_launch_plan_readiness_pct']}% readiness — blueprint only",
    ],
    'open_questions': [
        'Build #85 vs Launch Strategy (#53) — merge dashboards?',
        'Checklist completion — auto-detect from MC or manual?',
        'Launch date Jan 2027 — hard gate or target?',
        'Governance certification — who signs off?',
    ],
    'risks': lp['catalog_gaps'][:4],
    'next_recommended': 86,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/master-launch-plan.html',
    'review_status': 'complete',
})

mc['briefing'] = {
    'what_built': 'Master Launch Plan v1.0 — January 2027 readiness blueprint',
    'building_now': '85 builds — launch readiness dashboard next',
    'blocked': ['Launch readiness dashboard', 'Arkansas Launch Map', 'Checklist tracker', 'Governance certification'],
    'ready_public': ['36-item checklist', '11 categories', 'Launch message', 'First-year priorities'],
    'next': 'Build #86 — Launch readiness dashboard & certification components',
}

if not any(n.get('id') == 'master_launch_plan' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'master_launch_plan',
        'label': 'Launch Plan 2027',
        'href': '/mission-control/master-launch-plan.html',
        'status': 'complete',
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
