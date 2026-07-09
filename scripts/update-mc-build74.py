import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json', encoding='utf-8') as f:
    mc = json.load(f)

title = 'Citizens United Facts Master Arkansas Civic Innovation & Reform Center v1.0'

with open(root / 'data/arkansas-civic-innovation-reform.json', encoding='utf-8') as f:
    acir = json.load(f)

s = acir['summary']
prior_maturity = mc.get('executive', {}).get('institutional_maturity_pct', 32)

mc['version'] = '1.78.0'
mc['build'] = 74
mc['updated'] = '2026-07-09'
mc['arkansas_civic_innovation_reform'] = '/data/arkansas-civic-innovation-reform.json'
mc['arkansas_civic_innovation_reform_dashboard'] = '/mission-control/arkansas-civic-innovation-reform.html'

mc['executive'] = {
    'overall_completion': 74,
    'current_build': {'number': 74, 'title': title},
    'active_phase': 'Civic Innovation & Reform → Implementation Translation',
    'last_completed': 'Arkansas Research Institute',
    'next_build': {'number': 75, 'title': 'Implementation translation layer & engineering artifacts'},
    'github_status': 'connected',
    'netlify_status': 'production_healthy',
    'content_readiness': max(28, s['arkansas_civic_innovation_reform_readiness_pct'] - 12),
    'research_readiness': mc.get('executive', {}).get('research_readiness', 43),
    'data_viz_readiness': 12,
    'signup_funnel_readiness': 26,
    'civic_action_readiness': max(28, s['arkansas_civic_innovation_reform_readiness_pct'] - 14),
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
    'campaign_finance_observatory_readiness': max(mc.get('executive', {}).get('campaign_finance_observatory_readiness', 36), s['arkansas_civic_innovation_reform_readiness_pct'] - 6),
    'arkansas_action_network_readiness': 38,
    'civic_intelligence_command_center_readiness': 43,
    'sustainability_stewardship_readiness': 38,
    'impact_measurement_readiness': 31,
    'citizen_leadership_academy_readiness': 34,
    'relational_organizing_growth_engine_readiness': mc.get('executive', {}).get('relational_organizing_growth_engine_readiness', 34),
    'arkansas_command_strategy_readiness': mc.get('executive', {}).get('arkansas_command_strategy_readiness', 39),
    'arkansas_community_listening_readiness': mc.get('executive', {}).get('arkansas_community_listening_readiness', 41),
    'arkansas_communications_readiness': mc.get('executive', {}).get('arkansas_communications_readiness', 42),
    'arkansas_research_institute_readiness': mc.get('executive', {}).get('arkansas_research_institute_readiness', 43),
    'arkansas_civic_innovation_reform_readiness': s['arkansas_civic_innovation_reform_readiness_pct'],
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
    'trust_readiness': 30,
    'library_readiness': 22,
    'learning_lab_readiness': 22,
    'media_studio_readiness': 18,
    'civic_intelligence_readiness': 36,
    'evidence_ledger_readiness': max(22, s['arkansas_civic_innovation_reform_readiness_pct'] - 18),
    'civic_action_lab_readiness': max(26, s['arkansas_civic_innovation_reform_readiness_pct'] - 16),
    'research_methodology_readiness': mc.get('executive', {}).get('research_methodology_readiness', 29),
    'institutional_maturity_pct': prior_maturity,
    'current_institutional_version': 'V1',
    'systems_integration_readiness': 44,
    'production_matrix_readiness': 39,
    'visitor_journey_readiness': 40,
    'technical_architecture_readiness': 38,
    'governance_readiness': 44,
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

mc['arkansas_civic_innovation_reform_inventory'] = {
    'readiness_score': s['arkansas_civic_innovation_reform_readiness_pct'],
    'reform_analyses_completed': s['reform_analyses_completed'],
    'reform_libraries': s['reform_libraries'],
    'signature_educational_resource': True,
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 74
        bar['note'] = 'Build #74 — Civic Innovation & Reform Center.'
    if bar['id'] == 'civic_action':
        bar['value'] = max(bar.get('value', 0), s['arkansas_civic_innovation_reform_readiness_pct'] - 12)
        bar['note'] = f"Reform center — {s['reform_analyses_completed']} analyses · {s['libraries_operational']}/{s['reform_libraries']} libraries."

if not any(b.get('id') == 'arkansas_civic_innovation_reform' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'arkansas_civic_innovation_reform',
        'label': 'Reform Center',
        'value': s['arkansas_civic_innovation_reform_readiness_pct'],
        'max': 100,
        'note': f"{s['reform_analyses_completed']} analyses · solution builder {'live' if s['civic_solution_builder_live'] else 'planned'}.",
    })
else:
    for bar in mc['progress_bars']:
        if bar['id'] == 'arkansas_civic_innovation_reform':
            bar['value'] = s['arkansas_civic_innovation_reform_readiness_pct']

mc['builds'].insert(0, {
    'number': 74,
    'title': title,
    'version': '1.78.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Civic Innovation & Reform Center — educational library of reform ideas',
    'summary': (
        f"Eight reform libraries, six-question framework, proposal template, solution builder; "
        f"{s['arkansas_civic_innovation_reform_readiness_pct']}% readiness. "
        f"0 analyses · 0/8 libraries operational."
    ),
    'files_created': [
        'data/arkansas-civic-innovation-reform.json',
        'docs/MASTER_ARKANSAS_CIVIC_INNOVATION_REFORM.md',
        'builds/074-arkansas-civic-innovation-reform.md',
        'mission-control/arkansas-civic-innovation-reform.html',
        'scripts/gen-arkansas-civic-innovation-reform.py',
        'scripts/update-mc-build74.py',
    ],
    'files_modified': ['js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml'],
    'pages_created': ['/mission-control/arkansas-civic-innovation-reform.html'],
    'decisions_made': [
        'Signature educational resource — not single-solution advocacy',
        'Center explains ideas; citizens decide what they support',
        'Eight reform libraries: congressional, Arkansas, ballot, amendment, state, international, local, citizen lab',
        'Six questions every proposal answers — same educational framework',
        'Proposal framework: 11 standardized sections',
        'Civic Solution Builder — education not advocacy',
        f"{s['arkansas_civic_innovation_reform_readiness_pct']}% readiness — constitution only",
    ],
    'open_questions': [
        'Reconcile Reform Center (#74) vs Research Institute Policy Lab (#73)?',
        'Institutional neutrality badge on reform pages?',
        'Citizen Innovation Lab: public drafts or editorial-only?',
        'Solution builder: static compare or interactive tool?',
    ],
    'risks': acir['catalog_gaps'][:4],
    'next_recommended': 75,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/arkansas-civic-innovation-reform.html',
    'review_status': 'complete',
})

mc['briefing'] = {
    'what_built': 'Civic Innovation & Reform Center v1.0 — civic solutions laboratory',
    'building_now': '74 builds specified — implementation translation next',
    'blocked': ['Reform library pages', 'Proposal template', 'Solution builder', 'Citizen lab'],
    'ready_public': ['Eight libraries', 'Six questions', 'Proposal framework', 'Mission scope'],
    'next': 'Build #75 — Implementation translation layer & engineering artifacts',
}

if not any(n.get('id') == 'arkansas_civic_innovation_reform' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'arkansas_civic_innovation_reform',
        'label': 'Reform Center',
        'href': '/mission-control/arkansas-civic-innovation-reform.html',
        'status': 'complete',
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
