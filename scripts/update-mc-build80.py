import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json', encoding='utf-8') as f:
    mc = json.load(f)

title = 'Citizens United Facts Master Arkansas Civic Institution Roadmap v1.0'

with open(root / 'data/arkansas-civic-institution-roadmap.json', encoding='utf-8') as f:
    leg = json.load(f)

s = leg['summary']
prior_maturity = mc.get('executive', {}).get('institutional_maturity_pct', 32)

mc['version'] = '1.84.0'
mc['build'] = 80
mc['updated'] = '2026-07-09'
mc['arkansas_civic_institution_roadmap'] = '/data/arkansas-civic-institution-roadmap.json'
mc['arkansas_civic_institution_roadmap_dashboard'] = '/mission-control/arkansas-civic-institution-roadmap.html'

mc['executive'] = {
    'overall_completion': 80,
    'current_build': {'number': 80, 'title': title},
    'active_phase': 'Legacy Vision → Implementation Translation',
    'last_completed': 'Arkansas Neighborhood Operating System',
    'next_build': {'number': 81, 'title': 'Implementation translation layer & engineering artifacts'},
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
    'arkansas_civic_institution_roadmap_readiness': s['arkansas_civic_institution_roadmap_readiness_pct'],
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
    'trust_readiness': 30,
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
    'implementation_phase': 'translation_layer_next',
    'public_launch_readiness': s['public_launch_readiness_pct'],
    'public_launch_label': 'Early Foundation',
    'public_launch_recommended': False,
}

mc['arkansas_civic_institution_roadmap_inventory'] = {
    'readiness_score': s['arkansas_civic_institution_roadmap_readiness_pct'],
    'current_era': s['current_era'],
    'milestones_achieved': s['milestones_achieved'],
    'builds_complete': s['builds_complete'],
    'twenty_year_vision': True,
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 80
        bar['note'] = 'Build #80 — Twenty-Year Civic Institution Roadmap. 80 builds complete.'
    if bar['id'] == 'institutional_roadmap':
        bar['value'] = max(bar.get('value', 0), s['arkansas_civic_institution_roadmap_readiness_pct'])
        bar['note'] = f"Legacy vision — era {s['current_era']} · {s['milestones_achieved']}/{s['milestones_total']} milestones."

if not any(b.get('id') == 'arkansas_civic_institution_roadmap' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'arkansas_civic_institution_roadmap',
        'label': 'Civic Institution Roadmap',
        'value': s['arkansas_civic_institution_roadmap_readiness_pct'],
        'max': 100,
        'note': f"Era {s['current_era']} Foundation · legacy map {'live' if s['legacy_map_live'] else 'planned'}.",
    })
else:
    for bar in mc['progress_bars']:
        if bar['id'] == 'arkansas_civic_institution_roadmap':
            bar['value'] = s['arkansas_civic_institution_roadmap_readiness_pct']

mc['builds'].insert(0, {
    'number': 80,
    'title': title,
    'version': '1.84.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Twenty-year vision & institutional legacy plan — 80 builds complete',
    'summary': (
        f"4 eras, 8 twenty-year goals, legacy map, milestones, founder reflection, "
        f"{s['arkansas_civic_institution_roadmap_readiness_pct']}% readiness. "
        f"{s['builds_complete']} builds · era {s['current_era']} · "
        f"{s['milestones_achieved']}/{s['milestones_total']} milestones."
    ),
    'files_created': [
        'data/arkansas-civic-institution-roadmap.json',
        'docs/MASTER_ARKANSAS_CIVIC_INSTITUTION_ROADMAP.md',
        'builds/080-arkansas-civic-institution-roadmap.md',
        'mission-control/arkansas-civic-institution-roadmap.html',
        'scripts/gen-arkansas-civic-institution-roadmap.py',
        'scripts/update-mc-build80.py',
    ],
    'files_modified': ['js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml'],
    'pages_created': ['/mission-control/arkansas-civic-institution-roadmap.html'],
    'decisions_made': [
        '80 builds — planning arc complete',
        'Twenty-year legacy vision, not launch plan',
        'Four eras: Foundation → Expansion → Maturity → Legacy',
        'Success measured by legacy, not traffic',
        'MC compares current state to long-term vision',
        'Extends Institutional Roadmap (#44)',
        f"{s['arkansas_civic_institution_roadmap_readiness_pct']}% readiness — vision document only",
    ],
    'open_questions': [
        'Reconcile four eras vs V1–V10 institutional roadmap?',
        'Legacy map UI — MC-native or public exhibit?',
        'Milestone celebration workflow?',
        'When does implementation translation begin in earnest?',
    ],
    'risks': leg['catalog_gaps'][:4],
    'next_recommended': 81,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/arkansas-civic-institution-roadmap.html',
    'review_status': 'complete',
})

mc['briefing'] = {
    'what_built': 'Civic Institution Roadmap v1.0 — twenty-year legacy vision',
    'building_now': '80 builds specified — implementation translation next',
    'blocked': ['Legacy map', 'Milestone tracker', 'Era comparison dashboard', 'Annual reflection'],
    'ready_public': ['4 eras', '8 goals', '10 milestones', 'Founder reflection', '80 builds'],
    'next': 'Build #81 — Implementation translation layer & engineering artifacts',
}

if not any(n.get('id') == 'arkansas_civic_institution_roadmap' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'arkansas_civic_institution_roadmap',
        'label': 'Civic Institution Roadmap',
        'href': '/mission-control/arkansas-civic-institution-roadmap.html',
        'status': 'complete',
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
