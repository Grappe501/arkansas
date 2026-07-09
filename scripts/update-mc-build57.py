import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json', encoding='utf-8') as f:
    mc = json.load(f)

title = 'Citizens United Facts Arkansas Neighborhood Organizing & Relational Network v1.0'

with open(root / 'data/neighborhood-organizing.json', encoding='utf-8') as f:
    no = json.load(f)

s = no['summary']

mc['version'] = '1.61.0'
mc['build'] = 57
mc['updated'] = '2026-07-09'
mc['neighborhood_organizing'] = '/data/neighborhood-organizing.json'
mc['neighborhood_organizing_dashboard'] = '/mission-control/neighborhood-organizing.html'

mc['executive'] = {
    'overall_completion': 57,
    'current_build': {'number': 57, 'title': title},
    'active_phase': 'Last Mile Architecture → Implementation Translation',
    'last_completed': 'Statewide Growth & Leadership Blueprint',
    'next_build': {'number': 58, 'title': 'Implementation translation layer & engineering artifacts'},
    'github_status': 'connected',
    'netlify_status': 'production_healthy',
    'content_readiness': 28,
    'research_readiness': 25,
    'data_viz_readiness': 6,
    'signup_funnel_readiness': 22,
    'civic_action_readiness': 26,
    'coalition_readiness': 18,
    'data_model_readiness': 52,
    'route_inventory_readiness': 18,
    'component_registry_readiness': 22,
    'facts_framework_readiness': 14,
    'knowledge_atlas_readiness': 20,
    'platform_architecture_readiness': 24,
    'repository_structure_readiness': 28,
    'database_schema_readiness': 40,
    'wireframe_readiness': 38,
    'contact_intelligence_readiness': 31,
    'mc2_readiness': 33,
    'ai_engine_readiness': 14,
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
    'civic_intelligence_readiness': 24,
    'evidence_ledger_readiness': 22,
    'civic_action_lab_readiness': 26,
    'research_methodology_readiness': 25,
    'institutional_maturity_pct': 44,
    'current_institutional_version': 'V1',
    'systems_integration_readiness': 28,
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
    'statewide_growth_readiness': s['statewide_growth_readiness_pct'],
    'neighborhood_organizing_readiness': s['neighborhood_organizing_readiness_pct'],
    'rollout_phase': 0,
    'rollout_phase_title': 'Private Development',
    'planning_phase_complete': True,
    'planning_constitution_complete': True,
    'implementation_phase': 'translation_layer_next',
    'public_launch_readiness': s['public_launch_readiness_pct'],
    'public_launch_label': 'Early Foundation',
    'public_launch_recommended': False,
}

mc['neighborhood_organizing_inventory'] = {
    'readiness_score': s['neighborhood_organizing_readiness_pct'],
    'neighborhoods_represented': s['neighborhoods_represented'],
    'neighborhood_leaders': s['neighborhood_leaders'],
    'active_conversations': s['active_conversations'],
    'participants_target': s['participants_target'],
    'participants_current': s['participants_current'],
    'illumination_map_status': s['illumination_map_status'],
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 57
        bar['note'] = 'Build #57 — Neighborhood Organizing & Relational Network.'
    if bar['id'] == 'institutional_maturity':
        bar['value'] = 44
        bar['note'] = 'Last mile architecture live — 0 neighborhoods illuminated.'

if not any(b.get('id') == 'neighborhood_organizing' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'neighborhood_organizing',
        'label': 'Neighborhood Organizing',
        'value': s['neighborhood_organizing_readiness_pct'],
        'max': 100,
        'note': f"0 neighborhoods · {s['neighborhood_leaders']} leaders · map planned."
    })
else:
    for bar in mc['progress_bars']:
        if bar['id'] == 'neighborhood_organizing':
            bar['value'] = s['neighborhood_organizing_readiness_pct']
            bar['note'] = 'Last mile dashboard — relational organizing scaffolded.'

mc['builds'].insert(0, {
    'number': 57,
    'title': title,
    'version': '1.61.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Last mile architecture — neighborhood organizing & relational network',
    'summary': (
        f"4 geographic layers; relational organizing; neighborhood dashboard; "
        f"{s['neighborhood_organizing_readiness_pct']}% last mile readiness. "
        f"0 neighborhoods · 0 leaders."
    ),
    'files_created': [
        'data/neighborhood-organizing.json', 'data/neighborhood-profiles.json',
        'docs/MASTER_NEIGHBORHOOD_ORGANIZING.md', 'builds/057-neighborhood-organizing.md',
        'mission-control/neighborhood-organizing.html',
        'scripts/gen-neighborhood-organizing.py', 'scripts/update-mc-build57.py',
    ],
    'files_modified': ['js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml'],
    'pages_created': ['/mission-control/neighborhood-organizing.html'],
    'decisions_made': [
        'Four geographic layers: statewide → county → city → neighborhood',
        'Neighborhood Leaders are educators and connectors — not campaign managers',
        'Relational organizing over mass messaging — 5 pathways defined',
        'Privacy-first neighborhood profiles — no precise residential data public',
        'Mentorship ladder: Education Leader → Regional Mentor (5 stages)',
        '200K neighbor goal visualized by county, city, neighborhood, region',
        f"{s['neighborhood_organizing_readiness_pct']}% readiness — architecture documented, network empty",
    ],
    'open_questions': [
        'Neighborhood illumination map: heatmap vs discrete pins?',
        'Referral tracking: invite codes vs relationship graph edges?',
        'Unify #56 leadership ladder with #57 mentorship pathway?',
        'Neighborhood kit bundle: single PDF vs modular downloads?',
    ],
    'risks': no['catalog_gaps'][:4],
    'next_recommended': 58,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/neighborhood-organizing.html',
    'review_status': 'complete'
})

mc['briefing'] = {
    'what_built': 'Neighborhood Organizing v1.0 — last mile architecture, relational network, 4 layers',
    'building_now': 'Community growth stack complete (#56+#57) — implementation translation next',
    'blocked': ['Illumination map', 'Referral tracking', 'Neighborhood profiles DB', 'Event calendar'],
    'ready_public': ['Last mile dashboard', '4-layer model', 'Resource kit index', 'Privacy principles'],
    'next': 'Build #58 — Implementation translation layer & engineering artifacts'
}

if not any(n.get('id') == 'neighborhood_organizing' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'neighborhood_organizing',
        'label': 'Neighborhood Organizing',
        'href': '/mission-control/neighborhood-organizing.html',
        'status': 'complete'
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
