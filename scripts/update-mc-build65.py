import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json', encoding='utf-8') as f:
    mc = json.load(f)

title = 'Citizens United Facts Arkansas Civic Intelligence Command Center v1.0'

with open(root / 'data/civic-intelligence-command-center.json', encoding='utf-8') as f:
    cicc = json.load(f)

s = cicc['summary']

mc['version'] = '1.69.0'
mc['build'] = 65
mc['updated'] = '2026-07-09'
mc['civic_intelligence_command_center'] = '/data/civic-intelligence-command-center.json'
mc['civic_intelligence_command_center_dashboard'] = '/mission-control/civic-intelligence-command-center.html'

mc['executive'] = {
    'overall_completion': 65,
    'current_build': {'number': 65, 'title': title},
    'active_phase': 'Civic Intelligence Command Center → Implementation Translation',
    'last_completed': 'Arkansas Action Network & Leadership Pipeline',
    'next_build': {'number': 66, 'title': 'Implementation translation layer & engineering artifacts'},
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
    'civic_intelligence_command_center_readiness': s['civic_intelligence_command_center_readiness_pct'],
    'mc2_readiness': max(s['mc2_readiness_pct'], s['civic_intelligence_command_center_readiness_pct'] - 4),
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
    'trust_readiness': 24,
    'library_readiness': 22,
    'learning_lab_readiness': 22,
    'media_studio_readiness': 18,
    'civic_intelligence_readiness': max(28, s['civic_intelligence_command_center_readiness_pct'] - 8),
    'evidence_ledger_readiness': 22,
    'civic_action_lab_readiness': 26,
    'research_methodology_readiness': 25,
    'institutional_maturity_pct': s['institutional_readiness_index'],
    'current_institutional_version': 'V1',
    'systems_integration_readiness': 40,
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

mc['civic_intelligence_command_center_inventory'] = {
    'readiness_score': s['civic_intelligence_command_center_readiness_pct'],
    'institutional_readiness_index': s['institutional_readiness_index'],
    'departments_total': s['departments_total'],
    'operations_map_live': s['operations_map_live'],
    'operational_brain': True,
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 65
        bar['note'] = 'Build #65 — Civic Intelligence Command Center.'
    if bar['id'] == 'institutional_maturity':
        bar['value'] = s['institutional_readiness_index']
        bar['note'] = f"Executive nervous system — readiness index {s['institutional_readiness_index']}."
    if bar['id'] == 'mc2':
        bar['value'] = mc['executive']['mc2_readiness']
        bar['note'] = 'Command Center extends MC 2.0 — unified executive view.'

if not any(b.get('id') == 'civic_intelligence_command_center' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'civic_intelligence_command_center',
        'label': 'Civic Intelligence Command Center',
        'value': s['civic_intelligence_command_center_readiness_pct'],
        'max': 100,
        'note': f"{s['departments_total']} departments · index {s['institutional_readiness_index']}.",
    })
else:
    for bar in mc['progress_bars']:
        if bar['id'] == 'civic_intelligence_command_center':
            bar['value'] = s['civic_intelligence_command_center_readiness_pct']

mc['builds'].insert(0, {
    'number': 65,
    'title': title,
    'version': '1.69.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Civic Intelligence Command Center — executive nervous system unifying all institutional components',
    'summary': (
        f"Executive dashboard, KPI cards, operations map, 10 department boards, pulse, alerts; "
        f"{s['civic_intelligence_command_center_readiness_pct']}% readiness. "
        f"Index {s['institutional_readiness_index']} · 8% launch readiness."
    ),
    'files_created': [
        'data/civic-intelligence-command-center.json',
        'docs/MASTER_CIVIC_INTELLIGENCE_COMMAND_CENTER.md',
        'builds/065-civic-intelligence-command-center.md',
        'mission-control/civic-intelligence-command-center.html',
        'scripts/gen-civic-intelligence-command-center.py',
        'scripts/update-mc-build65.py',
    ],
    'files_modified': ['js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml'],
    'pages_created': ['/mission-control/civic-intelligence-command-center.html'],
    'decisions_made': [
        'Operational brain — answer institutional health in <5 seconds (aspirational)',
        'Extends MC 2.0 (#25) — does not replace executive.html',
        '10 department operations boards with shared field schema',
        'Institutional Readiness Index across 11 categories',
        'Executive Alerts + Opportunity Engine — proactive leadership tools',
        'Weekly briefing + annual State of Civic Education report specified',
        f"{s['civic_intelligence_command_center_readiness_pct']}% readiness — constitution, partial KPI aggregation",
    ],
    'open_questions': [
        'Command Center as MC home vs separate executive route?',
        'Operations map: Civic Atlas embed vs dedicated fullscreen?',
        'Weekly briefing: automated script vs manual template?',
        'AI Executive Advisor: separate role vs Institutional AI extension?',
    ],
    'risks': cicc['catalog_gaps'][:4],
    'next_recommended': 66,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/civic-intelligence-command-center.html',
    'review_status': 'complete',
})

mc['briefing'] = {
    'what_built': 'Civic Intelligence Command Center v1.0 — executive nervous system',
    'building_now': '65 builds specified — implementation translation next',
    'blocked': ['Operations map', 'Alert engine', 'Weekly briefing', 'Unified data pipeline'],
    'ready_public': ['Executive dashboard spec', '15 KPI cards', '11-category readiness index', '10 department boards'],
    'next': 'Build #66 — Implementation translation layer & engineering artifacts',
}

if not any(n.get('id') == 'civic_intelligence_command_center' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'civic_intelligence_command_center',
        'label': 'Civic Intelligence Command Center',
        'href': '/mission-control/civic-intelligence-command-center.html',
        'status': 'complete',
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
