import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json', encoding='utf-8') as f:
    mc = json.load(f)

title = 'Citizens United Facts Master Campaign Finance Data Observatory v1.0'

with open(root / 'data/campaign-finance-observatory.json', encoding='utf-8') as f:
    cfo = json.load(f)

s = cfo['summary']

mc['version'] = '1.67.0'
mc['build'] = 63
mc['updated'] = '2026-07-09'
mc['campaign_finance_observatory'] = '/data/campaign-finance-observatory.json'
mc['campaign_finance_observatory_dashboard'] = '/mission-control/campaign-finance-observatory.html'

mc['executive'] = {
    'overall_completion': 63,
    'current_build': {'number': 63, 'title': title},
    'active_phase': 'Campaign Finance Observatory → Implementation Translation',
    'last_completed': 'Citizen Action Center & Civic Engagement Hub',
    'next_build': {'number': 64, 'title': 'Implementation translation layer & engineering artifacts'},
    'github_status': 'connected',
    'netlify_status': 'production_healthy',
    'content_readiness': 28,
    'research_readiness': 26,
    'data_viz_readiness': s['data_viz_readiness_pct'],
    'signup_funnel_readiness': 22,
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
    'campaign_finance_observatory_readiness': s['campaign_finance_observatory_readiness_pct'],
    'mc2_readiness': 33,
    'ai_engine_readiness': 34,
    'content_factory_readiness': 30,
    'education_academy_readiness': 26,
    'observatory_readiness': max(s['observatory_readiness_pct'], s['campaign_finance_observatory_readiness_pct'] // 2),
    'outreach_readiness': 22,
    'county_os_readiness': 28,
    'campaign_os_readiness': 34,
    'encyclopedia_readiness': 19,
    'narrative_readiness': 24,
    'curriculum_readiness': 26,
    'trust_readiness': 24,
    'library_readiness': 22,
    'learning_lab_readiness': 22,
    'media_studio_readiness': 18,
    'civic_intelligence_readiness': 28,
    'evidence_ledger_readiness': 22,
    'civic_action_lab_readiness': 26,
    'research_methodology_readiness': 25,
    'institutional_maturity_pct': 50,
    'current_institutional_version': 'V1',
    'systems_integration_readiness': 37,
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

mc['campaign_finance_observatory_inventory'] = {
    'readiness_score': s['campaign_finance_observatory_readiness_pct'],
    'divisions_total': s['divisions_total'],
    'datasets_published': s['datasets_published'],
    'charts_completed': s['charts_completed'],
    'flagship_system': True,
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 63
        bar['note'] = 'Build #63 — Campaign Finance Data Observatory.'
    if bar['id'] == 'institutional_maturity':
        bar['value'] = 50
        bar['note'] = 'Flagship data observatory — 0 charts, 0 datasets.'
    if bar['id'] == 'observatory':
        bar['value'] = mc['executive']['observatory_readiness']
        bar['note'] = f"8 divisions defined · {s['charts_completed']} charts · {s['datasets_published']} datasets."

if not any(b.get('id') == 'campaign_finance_observatory' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'campaign_finance_observatory',
        'label': 'Campaign Finance Observatory',
        'value': s['campaign_finance_observatory_readiness_pct'],
        'max': 100,
        'note': f"8 divisions · {s['charts_completed']} charts · {s['datasets_published']} datasets.",
    })
else:
    for bar in mc['progress_bars']:
        if bar['id'] == 'campaign_finance_observatory':
            bar['value'] = s['campaign_finance_observatory_readiness_pct']

mc['builds'].insert(0, {
    'number': 63,
    'title': title,
    'version': '1.67.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Campaign Finance Data Observatory — answer "What actually changed?" with transparent evidence',
    'summary': (
        f"8 research divisions; Before & After Explorer; data integrity standards; "
        f"{s['campaign_finance_observatory_readiness_pct']}% readiness. "
        f"0 datasets · 0 charts."
    ),
    'files_created': [
        'data/campaign-finance-observatory.json', 'docs/MASTER_CAMPAIGN_FINANCE_OBSERVATORY.md',
        'builds/063-campaign-finance-observatory.md',
        'mission-control/campaign-finance-observatory.html',
        'scripts/gen-campaign-finance-observatory.py', 'scripts/update-mc-build63.py',
    ],
    'files_modified': ['js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml'],
    'pages_created': ['/mission-control/campaign-finance-observatory.html'],
    'decisions_made': [
        'Flagship educational system — replaces speculation with understanding',
        '8 divisions from Historical Spending to FAQ — all planned, 0 live charts',
        'Before & After Explorer — educational comparison, not unsupported causation',
        'Data integrity: source, date, review, methodology, version on every chart',
        'Distinct from Research Observatory (#29) — monitor vs spending data',
        'Integrates Research Library, Evidence Ledger, Knowledge Graph chain',
        f"{s['campaign_finance_observatory_readiness_pct']}% readiness — constitution only, no data feeds",
    ],
    'open_questions': [
        'FEC vs OpenSecrets vs Arkansas SOS — primary data source priority?',
        'Public /observatory/ route vs MC-only dashboard?',
        'Unify navigation with Research Observatory (#29)?',
        'Inflation adjustment methodology — which CPI series?',
    ],
    'risks': cfo['catalog_gaps'][:4],
    'next_recommended': 64,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/campaign-finance-observatory.html',
    'review_status': 'complete',
})

mc['briefing'] = {
    'what_built': 'Campaign Finance Data Observatory v1.0 — 8 divisions, transparent evidence',
    'building_now': '63 builds specified — implementation translation next',
    'blocked': ['FEC data feeds', 'Chart library', 'Before & After Explorer', 'Arkansas datasets'],
    'ready_public': ['8 divisions', 'Methodology standards', 'Data integrity spec', 'MC observatory metrics'],
    'next': 'Build #64 — Implementation translation layer & engineering artifacts',
}

if not any(n.get('id') == 'campaign_finance_observatory' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'campaign_finance_observatory',
        'label': 'Campaign Finance Observatory',
        'href': '/mission-control/campaign-finance-observatory.html',
        'status': 'complete',
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
