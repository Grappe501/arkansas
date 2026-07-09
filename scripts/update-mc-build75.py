import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json', encoding='utf-8') as f:
    mc = json.load(f)

title = 'Citizens United Facts Master Volunteer & Funding Constitution v1.0'

with open(root / 'data/volunteer-funding-constitution.json', encoding='utf-8') as f:
    vfc = json.load(f)

s = vfc['summary']
prior_maturity = mc.get('executive', {}).get('institutional_maturity_pct', 32)

mc['version'] = '1.79.0'
mc['build'] = 75
mc['updated'] = '2026-07-09'
mc['volunteer_funding_constitution'] = '/data/volunteer-funding-constitution.json'
mc['volunteer_funding_constitution_dashboard'] = '/mission-control/volunteer-funding-constitution.html'

mc['executive'] = {
    'overall_completion': 75,
    'current_build': {'number': 75, 'title': title},
    'active_phase': 'Volunteer & Funding Constitution → Implementation Translation',
    'last_completed': 'Civic Innovation & Reform Center',
    'next_build': {'number': 76, 'title': 'Implementation translation layer & engineering artifacts'},
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
    'sustainability_stewardship_readiness': max(s['sustainability_stewardship_readiness_pct'], s['volunteer_funding_constitution_readiness_pct'] - 4),
    'impact_measurement_readiness': 31,
    'citizen_leadership_academy_readiness': 34,
    'relational_organizing_growth_engine_readiness': mc.get('executive', {}).get('relational_organizing_growth_engine_readiness', 34),
    'arkansas_command_strategy_readiness': mc.get('executive', {}).get('arkansas_command_strategy_readiness', 39),
    'arkansas_community_listening_readiness': mc.get('executive', {}).get('arkansas_community_listening_readiness', 41),
    'arkansas_communications_readiness': mc.get('executive', {}).get('arkansas_communications_readiness', 42),
    'arkansas_research_institute_readiness': mc.get('executive', {}).get('arkansas_research_institute_readiness', 43),
    'arkansas_civic_innovation_reform_readiness': mc.get('executive', {}).get('arkansas_civic_innovation_reform_readiness', 44),
    'volunteer_funding_constitution_readiness': s['volunteer_funding_constitution_readiness_pct'],
    'mc2_readiness': 42,
    'ai_engine_readiness': 34,
    'content_factory_readiness': 30,
    'education_academy_readiness': 26,
    'observatory_readiness': mc.get('executive', {}).get('observatory_readiness', 43),
    'outreach_readiness': 34,
    'county_os_readiness': 28,
    'campaign_os_readiness': 34,
    'encyclopedia_readiness': 19,
    'narrative_readiness': 24,
    'curriculum_readiness': 26,
    'trust_readiness': max(30, s['volunteer_funding_constitution_readiness_pct'] - 10),
    'library_readiness': 22,
    'learning_lab_readiness': 22,
    'media_studio_readiness': 18,
    'civic_intelligence_readiness': 36,
    'evidence_ledger_readiness': 22,
    'civic_action_lab_readiness': 26,
    'research_methodology_readiness': mc.get('executive', {}).get('research_methodology_readiness', 29),
    'institutional_maturity_pct': prior_maturity,
    'current_institutional_version': 'V1',
    'systems_integration_readiness': 44,
    'production_matrix_readiness': 39,
    'visitor_journey_readiness': 40,
    'technical_architecture_readiness': 38,
    'governance_readiness': max(44, s['volunteer_funding_constitution_readiness_pct'] - 2),
    'build_bible_readiness': 49,
    'data_architecture_readiness': 41,
    'ux_architecture_readiness': 39,
    'launch_strategy_readiness': 39,
    'pmo_readiness': 46,
    'master_plan_readiness': 56,
    'statewide_growth_readiness': mc.get('executive', {}).get('statewide_growth_readiness', 48),
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

mc['volunteer_funding_constitution_inventory'] = {
    'readiness_score': s['volunteer_funding_constitution_readiness_pct'],
    'active_volunteers': s['active_volunteers'],
    'funding_sources': s['funding_sources'],
    'all_volunteer_institution': True,
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 75
        bar['note'] = 'Build #75 — Volunteer & Funding Constitution.'
    if bar['id'] == 'coalition':
        bar['note'] = f"Independence charter — {s['active_volunteers']} volunteers · {s['funding_sources']} funding sources."

if not any(b.get('id') == 'volunteer_funding_constitution' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'volunteer_funding_constitution',
        'label': 'Volunteer & Funding',
        'value': s['volunteer_funding_constitution_readiness_pct'],
        'max': 100,
        'note': f"{s['active_volunteers']} volunteers · adherence {'live' if s['adherence_monitoring_live'] else 'planned'}.",
    })
else:
    for bar in mc['progress_bars']:
        if bar['id'] == 'volunteer_funding_constitution':
            bar['value'] = s['volunteer_funding_constitution_readiness_pct']

mc['builds'].insert(0, {
    'number': 75,
    'title': title,
    'version': '1.79.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Volunteer & Funding Constitution — institutional independence charter',
    'summary': (
        f"All-volunteer institution, financial independence, Arkansas citizen support, no special access; "
        f"{s['volunteer_funding_constitution_readiness_pct']}% readiness. "
        f"0 volunteers · 0 funding sources · adherence not monitored."
    ),
    'files_created': [
        'data/volunteer-funding-constitution.json',
        'docs/MASTER_VOLUNTEER_FUNDING_CONSTITUTION.md',
        'builds/075-volunteer-funding-constitution.md',
        'mission-control/volunteer-funding-constitution.html',
        'scripts/gen-volunteer-funding-constitution.py',
        'scripts/update-mc-build75.py',
    ],
    'files_modified': ['js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml'],
    'pages_created': ['/mission-control/volunteer-funding-constitution.html'],
    'decisions_made': [
        'All-volunteer Arkansas civic education institution — educate first and always',
        'Volunteer first — every major function designed for trained volunteers',
        'Financial independence — neutrality protected from conflicting interests',
        'Preferred funding: individual voluntary Arkansas citizen contributions',
        'No special access — contributions never purchase influence',
        'Extends Sustainability (#66) with constitutional foundation',
        f"{s['volunteer_funding_constitution_readiness_pct']}% readiness — constitution only",
    ],
    'open_questions': [
        'Reconcile #75 constitution vs #66 sustainability operational blueprint?',
        'Volunteer hours: self-report vs leader attestation?',
        'Donation intake: when to activate Arkansas citizen funding model?',
        'Adherence monitoring: automated checklist vs manual review?',
    ],
    'risks': vfc['catalog_gaps'][:4],
    'next_recommended': 76,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/volunteer-funding-constitution.html',
    'review_status': 'complete',
})

mc['briefing'] = {
    'what_built': 'Volunteer & Funding Constitution v1.0 — institutional independence charter',
    'building_now': '75 builds specified — implementation translation next',
    'blocked': ['Volunteer registry', 'Funding transparency', 'Adherence monitoring', 'Recognition'],
    'ready_public': ['Volunteer first', 'Financial independence', 'No special access', 'Stewardship question'],
    'next': 'Build #76 — Implementation translation layer & engineering artifacts',
}

if not any(n.get('id') == 'volunteer_funding_constitution' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'volunteer_funding_constitution',
        'label': 'Volunteer & Funding',
        'href': '/mission-control/volunteer-funding-constitution.html',
        'status': 'complete',
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
