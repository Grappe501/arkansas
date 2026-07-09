import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json', encoding='utf-8') as f:
    mc = json.load(f)

title = 'Citizens United Facts Master Public Trust & Institutional Credibility Framework v1.0'

with open(root / 'data/public-trust-institutional-credibility.json', encoding='utf-8') as f:
    pt = json.load(f)

s = pt['summary']
prior_maturity = mc.get('executive', {}).get('institutional_maturity_pct', 32)

mc['version'] = '1.86.0'
mc['build'] = 82
mc['updated'] = '2026-07-09'
mc['public_trust_institutional_credibility'] = '/data/public-trust-institutional-credibility.json'
mc['public_trust_institutional_credibility_dashboard'] = '/mission-control/public-trust-institutional-credibility.html'

mc['executive'] = {
    'overall_completion': 82,
    'current_build': {'number': 82, 'title': title},
    'active_phase': 'Public Trust → Trust Dashboard',
    'last_completed': 'Institutional Digital Twin',
    'next_build': {'number': 83, 'title': 'Trust dashboard & citation audit components'},
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
    'public_trust_institutional_credibility_readiness': s['public_trust_institutional_credibility_readiness_pct'],
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
    'trust_readiness': max(s['public_trust_institutional_credibility_readiness_pct'], mc.get('executive', {}).get('trust_readiness', 30)),
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
    'implementation_phase': 'trust_dashboard_next',
    'public_launch_readiness': s['public_launch_readiness_pct'],
    'public_launch_label': 'Early Foundation',
    'public_launch_recommended': False,
}

mc['public_trust_institutional_credibility_inventory'] = {
    'readiness_score': s['public_trust_institutional_credibility_readiness_pct'],
    'trust_pyramid_layers': s['trust_pyramid_layers'],
    'trust_dashboard_live': s['trust_dashboard_live'],
    'trust_is_product': True,
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 82
        bar['note'] = 'Build #82 — Public Trust & Institutional Credibility.'
    if bar['id'] == 'trust':
        bar['value'] = max(bar.get('value', 0), s['public_trust_institutional_credibility_readiness_pct'])
        bar['note'] = f"Trust architecture — {s['corrections_completed']} corrections · audit {'done' if s['annual_trust_audit_conducted'] else 'pending'}."

if not any(b.get('id') == 'public_trust_institutional_credibility' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'public_trust_institutional_credibility',
        'label': 'Public Trust',
        'value': s['public_trust_institutional_credibility_readiness_pct'],
        'max': 100,
        'note': f"{s['citation_completeness_pct']}% citations · dashboard {'live' if s['trust_dashboard_live'] else 'planned'}.",
    })
else:
    for bar in mc['progress_bars']:
        if bar['id'] == 'public_trust_institutional_credibility':
            bar['value'] = s['public_trust_institutional_credibility_readiness_pct']

mc['builds'].insert(0, {
    'number': 82,
    'title': title,
    'version': '1.86.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Arkansas Trust Architecture — trust is the greatest asset',
    'summary': (
        f"7-layer trust pyramid, dashboard, review process, annual audit, founder standard, "
        f"{s['public_trust_institutional_credibility_readiness_pct']}% readiness. "
        f"{s['corrections_completed']} corrections · audit {'done' if s['annual_trust_audit_conducted'] else 'not conducted'}."
    ),
    'files_created': [
        'data/public-trust-institutional-credibility.json',
        'docs/MASTER_PUBLIC_TRUST_INSTITUTIONAL_CREDIBILITY.md',
        'builds/082-public-trust-institutional-credibility.md',
        'mission-control/public-trust-institutional-credibility.html',
        'scripts/gen-public-trust-institutional-credibility.py',
        'scripts/update-mc-build82.py',
    ],
    'files_modified': ['js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml'],
    'pages_created': ['/mission-control/public-trust-institutional-credibility.html'],
    'decisions_made': [
        'Trust is greatest asset — measure like research and growth',
        '7-layer trust pyramid (extends #36 5-layer)',
        'Public Trust Dashboard — 8 indicators',
        'Annual Trust Audit — public report',
        'Founder standard — trusted by different conclusions',
        f"{s['public_trust_institutional_credibility_readiness_pct']}% readiness — blueprint only",
    ],
    'open_questions': [
        'Build #82 vs Trust Framework (#36) — unify dashboards?',
        'Citation audit — automated or manual?',
        'Correction workflow — Netlify Forms or MC-native?',
        'Independent review — who qualifies as outside reviewer?',
    ],
    'risks': pt['catalog_gaps'][:4],
    'next_recommended': 83,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/public-trust-institutional-credibility.html',
    'review_status': 'complete',
})

mc['briefing'] = {
    'what_built': 'Public Trust Framework v1.0 — trust is the product',
    'building_now': '82 builds — trust dashboard next',
    'blocked': ['Trust dashboard', 'Citation audit', 'Correction workflow', 'Annual trust report'],
    'ready_public': ['7-layer pyramid', 'Review process', 'Founder standard', 'Crisis response'],
    'next': 'Build #83 — Trust dashboard & citation audit components',
}

if not any(n.get('id') == 'public_trust_institutional_credibility' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'public_trust_institutional_credibility',
        'label': 'Public Trust',
        'href': '/mission-control/public-trust-institutional-credibility.html',
        'status': 'complete',
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
