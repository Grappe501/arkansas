import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json', encoding='utf-8') as f:
    mc = json.load(f)

title = 'Citizens United Facts Master Citizen Action Center & Civic Engagement Hub v1.0'

with open(root / 'data/citizen-action-center.json', encoding='utf-8') as f:
    cac = json.load(f)

s = cac['summary']

mc['version'] = '1.66.0'
mc['build'] = 62
mc['updated'] = '2026-07-09'
mc['citizen_action_center'] = '/data/citizen-action-center.json'
mc['citizen_action_center_dashboard'] = '/mission-control/citizen-action-center.html'

mc['executive'] = {
    'overall_completion': 62,
    'current_build': {'number': 62, 'title': title},
    'active_phase': 'Citizen Action Center → Implementation Translation',
    'last_completed': 'Coalition & Civic Alliance Network',
    'next_build': {'number': 63, 'title': 'Implementation translation layer & engineering artifacts'},
    'github_status': 'connected',
    'netlify_status': 'production_healthy',
    'content_readiness': 28,
    'research_readiness': 25,
    'data_viz_readiness': 8,
    'signup_funnel_readiness': 22,
    'civic_action_readiness': max(s['civic_action_readiness_pct'], s['citizen_action_center_readiness_pct'] - 4),
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
    'citizen_action_center_readiness': s['citizen_action_center_readiness_pct'],
    'mc2_readiness': 33,
    'ai_engine_readiness': 34,
    'content_factory_readiness': 30,
    'education_academy_readiness': 26,
    'observatory_readiness': 20,
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
    'civic_action_lab_readiness': s['civic_action_lab_readiness_pct'],
    'research_methodology_readiness': 25,
    'institutional_maturity_pct': 49,
    'current_institutional_version': 'V1',
    'systems_integration_readiness': 36,
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

mc['citizen_action_center_inventory'] = {
    'readiness_score': s['citizen_action_center_readiness_pct'],
    'pathways_total': s['pathways_total'],
    'registered_participants': s['registered_participants'],
    'action_hub_items_live': s['action_hub_items_live'],
    'bridge_learning_to_participation': True,
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 62
        bar['note'] = 'Build #62 — Citizen Action Center.'
    if bar['id'] == 'institutional_maturity':
        bar['value'] = 49
        bar['note'] = 'Learn → Participate bridge — 0 registered citizens.'
    if bar['id'] == 'action_hub':
        bar['value'] = min(100, s['action_hub_items_live'] * 10)
        bar['note'] = f"{s['action_hub_items_live']} action hub items live — 6 pathways defined."

if not any(b.get('id') == 'citizen_action_center' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'citizen_action_center',
        'label': 'Citizen Action Center',
        'value': s['citizen_action_center_readiness_pct'],
        'max': 100,
        'note': f"6 pathways · {s['registered_participants']} registered."
    })
else:
    for bar in mc['progress_bars']:
        if bar['id'] == 'citizen_action_center':
            bar['value'] = s['citizen_action_center_readiness_pct']

mc['builds'].insert(0, {
    'number': 62,
    'title': title,
    'version': '1.66.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Citizen Action Center — bridge from learning to responsible civic participation',
    'summary': (
        f"6 citizen pathways; public official packets; relational sharing; "
        f"{s['citizen_action_center_readiness_pct']}% readiness. "
        f"0 registered · {s['action_hub_items_live']} hub items live."
    ),
    'files_created': [
        'data/citizen-action-center.json', 'docs/MASTER_CITIZEN_ACTION_CENTER.md',
        'builds/062-citizen-action-center.md', 'mission-control/citizen-action-center.html',
        'scripts/gen-citizen-action-center.py', 'scripts/update-mc-build62.py',
    ],
    'files_modified': ['js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml'],
    'pages_created': ['/mission-control/citizen-action-center.html'],
    'decisions_made': [
        'Bridge between learning and participation — not advocacy',
        'Guiding sequence: Learn → Understand → Verify → Discuss → Participate',
        '6 pathways from Stay Informed to Research Contributions',
        'Public official packets = educational materials, not advocacy scripts',
        'Measures civic education capacity — not political influence',
        'Extends Civic Action Lab (#42) with citizen-facing hub',
        f"{s['citizen_action_center_readiness_pct']}% readiness — pathways documented, dashboard not built",
    ],
    'open_questions': [
        'Unify Citizen Action Center with Civic Action Lab public routes?',
        'Citizen dashboard: separate /my/ vs integrated profile?',
        'Official packet PDF generator vs static templates?',
        'Share tracking: referral codes vs anonymous counts?',
    ],
    'risks': cac['catalog_gaps'][:4],
    'next_recommended': 63,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/citizen-action-center.html',
    'review_status': 'complete'
})

mc['briefing'] = {
    'what_built': 'Citizen Action Center v1.0 — 6 pathways, learn-to-participate bridge',
    'building_now': '62 builds specified — implementation translation next',
    'blocked': ['Citizen dashboard', 'Packet builder', 'Share visualization', 'Registration'],
    'ready_public': ['6 pathways', 'Guiding philosophy', 'County action spec', 'MC citizen metrics'],
    'next': 'Build #63 — Implementation translation layer & engineering artifacts'
}

if not any(n.get('id') == 'citizen_action_center' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'citizen_action_center',
        'label': 'Citizen Action Center',
        'href': '/mission-control/citizen-action-center.html',
        'status': 'complete'
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
