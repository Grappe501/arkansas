import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json', encoding='utf-8') as f:
    mc = json.load(f)

title = 'Citizens United Facts Master Impact Measurement & Arkansas Civic Scorecard v1.0'

with open(root / 'data/impact-measurement.json', encoding='utf-8') as f:
    im = json.load(f)

s = im['summary']
prior_ex = mc.get('executive', {})
prior_maturity = prior_ex.get('institutional_maturity_pct', 32)

mc['version'] = '1.71.0'
mc['build'] = 67
mc['updated'] = '2026-07-09'
mc['impact_measurement'] = '/data/impact-measurement.json'
mc['impact_measurement_dashboard'] = '/mission-control/impact-measurement.html'

mc['executive'] = {
    'overall_completion': 67,
    'current_build': {'number': 67, 'title': title},
    'active_phase': 'Impact Measurement → Implementation Translation',
    'last_completed': 'Sustainability, Funding & Institutional Stewardship',
    'next_build': {'number': 68, 'title': 'Implementation translation layer & engineering artifacts'},
    'github_status': 'connected',
    'netlify_status': 'production_healthy',
    'content_readiness': 28,
    'research_readiness': 26,
    'data_viz_readiness': 12,
    'signup_funnel_readiness': 24,
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
    'relationship_os_readiness': 54,
    'institutional_ai_readiness': 42,
    'coalition_network_readiness': 44,
    'citizen_action_center_readiness': 42,
    'campaign_finance_observatory_readiness': 36,
    'arkansas_action_network_readiness': 38,
    'civic_intelligence_command_center_readiness': 43,
    'sustainability_stewardship_readiness': 38,
    'impact_measurement_readiness': s['impact_measurement_readiness_pct'],
    'mc2_readiness': 40,
    'ai_engine_readiness': 34,
    'content_factory_readiness': 30,
    'education_academy_readiness': 26,
    'observatory_readiness': 20,
    'outreach_readiness': 24,
    'county_os_readiness': 28,
    'campaign_os_readiness': 34,
    'encyclopedia_readiness': 19,
    'narrative_readiness': 24,
    'curriculum_readiness': 26,
    'trust_readiness': 28,
    'library_readiness': 22,
    'learning_lab_readiness': 22,
    'media_studio_readiness': 18,
    'civic_intelligence_readiness': 36,
    'evidence_ledger_readiness': 22,
    'civic_action_lab_readiness': 26,
    'research_methodology_readiness': 25,
    'institutional_maturity_pct': prior_maturity,
    'current_institutional_version': 'V1',
    'systems_integration_readiness': 42,
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
    'statewide_growth_readiness': 48,
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

mc['impact_measurement_inventory'] = {
    'readiness_score': s['impact_measurement_readiness_pct'],
    'pillars_total': s['pillars_total'],
    'overall_arkansas_civic_score': s['overall_arkansas_civic_score'],
    'measures_understanding': True,
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 67
        bar['note'] = 'Build #67 — Impact Measurement & Civic Scorecard.'
    if bar['id'] == 'institutional_maturity':
        bar['value'] = prior_maturity
        bar['note'] = f"Impact framework — civic score {s['overall_arkansas_civic_score']}."

if not any(b.get('id') == 'impact_measurement' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'impact_measurement',
        'label': 'Impact Measurement',
        'value': s['impact_measurement_readiness_pct'],
        'max': 100,
        'note': f"5 pillars · score {s['overall_arkansas_civic_score']} · understanding not traffic.",
    })
else:
    for bar in mc['progress_bars']:
        if bar['id'] == 'impact_measurement':
            bar['value'] = s['impact_measurement_readiness_pct']

mc['builds'].insert(0, {
    'number': 67,
    'title': title,
    'version': '1.71.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Impact Measurement — measure understanding, not activity; Arkansas Civic Scorecard',
    'summary': (
        f"5 impact pillars; statewide scorecard; county/city/leader scorecards; "
        f"{s['impact_measurement_readiness_pct']}% readiness. "
        f"Overall civic score {s['overall_arkansas_civic_score']} · 0 leaders."
    ),
    'files_created': [
        'data/impact-measurement.json', 'docs/MASTER_IMPACT_MEASUREMENT.md',
        'builds/067-impact-measurement.md', 'mission-control/impact-measurement.html',
        'scripts/gen-impact-measurement.py', 'scripts/update-mc-build67.py',
    ],
    'files_modified': ['js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml'],
    'pages_created': ['/mission-control/impact-measurement.html'],
    'decisions_made': [
        'Measure understanding — not traffic, impressions, or page views',
        '5 impact pillars: Knowledge, Leadership, Community, Institutional, Arkansas',
        'Arkansas Civic Scorecard — 10 indicators + composite score',
        'Outcomes over outputs — activity vs impact distinction',
        'County/city/leadership scorecards — progress over time, not competition',
        'Integrates Civic Atlas ECS, Action Network, Command Center',
        f"{s['impact_measurement_readiness_pct']}% readiness — framework only, score=0",
    ],
    'open_questions': [
        'Composite civic score weighting across 10 indicators?',
        'Public scorecard page vs MC-only?',
        'Learner tracking without compromising privacy?',
        'Unify with Sustainability annual report (#66)?',
    ],
    'risks': im['catalog_gaps'][:4],
    'next_recommended': 68,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/impact-measurement.html',
    'review_status': 'complete',
})

mc['briefing'] = {
    'what_built': 'Impact Measurement v1.0 — Arkansas Civic Scorecard, 5 pillars',
    'building_now': '67 builds specified — implementation translation next',
    'blocked': ['Composite score', 'County scorecards', 'Learner tracking', 'Annual civic report'],
    'ready_public': ['5 pillars', 'Scorecard spec', 'Outcomes framework', 'Impact dashboard widgets'],
    'next': 'Build #68 — Implementation translation layer & engineering artifacts',
}

if not any(n.get('id') == 'impact_measurement' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'impact_measurement',
        'label': 'Impact Measurement',
        'href': '/mission-control/impact-measurement.html',
        'status': 'complete',
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
