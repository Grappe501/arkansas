import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json', encoding='utf-8') as f:
    mc = json.load(f)

title = 'Citizens United Facts Master Relational Organizing & Arkansas Growth Engine v1.0'

with open(root / 'data/relational-organizing-growth-engine.json', encoding='utf-8') as f:
    rog = json.load(f)

s = rog['summary']
prior_maturity = mc.get('executive', {}).get('institutional_maturity_pct', 32)

mc['version'] = '1.73.0'
mc['build'] = 69
mc['updated'] = '2026-07-09'
mc['relational_organizing_growth_engine'] = '/data/relational-organizing-growth-engine.json'
mc['relational_organizing_growth_engine_dashboard'] = '/mission-control/relational-organizing-growth-engine.html'

mc['executive'] = {
    'overall_completion': 69,
    'current_build': {'number': 69, 'title': title},
    'active_phase': 'Relational Organizing Growth Engine → Implementation Translation',
    'last_completed': 'Citizen Leadership Academy',
    'next_build': {'number': 70, 'title': 'Implementation translation layer & engineering artifacts'},
    'github_status': 'connected',
    'netlify_status': 'production_healthy',
    'content_readiness': 28,
    'research_readiness': 26,
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
    'relationship_os_readiness': max(s['relationship_os_readiness_pct'], s['relational_organizing_growth_engine_readiness_pct']),
    'institutional_ai_readiness': 42,
    'coalition_network_readiness': 44,
    'citizen_action_center_readiness': 42,
    'campaign_finance_observatory_readiness': 36,
    'arkansas_action_network_readiness': 38,
    'civic_intelligence_command_center_readiness': 43,
    'sustainability_stewardship_readiness': 38,
    'impact_measurement_readiness': 31,
    'citizen_leadership_academy_readiness': 34,
    'relational_organizing_growth_engine_readiness': s['relational_organizing_growth_engine_readiness_pct'],
    'mc2_readiness': 42,
    'ai_engine_readiness': 34,
    'content_factory_readiness': 30,
    'education_academy_readiness': 26,
    'observatory_readiness': 20,
    'outreach_readiness': max(24, s['relational_organizing_growth_engine_readiness_pct'] - 8),
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
    'evidence_ledger_readiness': 22,
    'civic_action_lab_readiness': 26,
    'research_methodology_readiness': 25,
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
    'statewide_growth_readiness': 48,
    'neighborhood_organizing_readiness': max(s['neighborhood_organizing_readiness_pct'], s['relational_organizing_growth_engine_readiness_pct']),
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

mc['relational_organizing_growth_engine_inventory'] = {
    'readiness_score': s['relational_organizing_growth_engine_readiness_pct'],
    'relationship_trees': s['relationship_trees'],
    'connected_arkansans': s['connected_arkansans'],
    'primary_expansion_strategy': True,
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 69
        bar['note'] = 'Build #69 — Relational Organizing Growth Engine.'
    if bar['id'] == 'signup_funnel':
        bar['value'] = min(100, s['connected_arkansans'] // 2000)
        bar['note'] = f"Relational growth — {s['total_invitations']} invitations · {s['connected_arkansans']}/{s['connected_target']} connected."

if not any(b.get('id') == 'relational_organizing_growth_engine' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'relational_organizing_growth_engine',
        'label': 'Relational Growth Engine',
        'value': s['relational_organizing_growth_engine_readiness_pct'],
        'max': 100,
        'note': f"{s['relationship_trees']} trees · {s['share_hub_pages_wired']} pages with share hub.",
    })
else:
    for bar in mc['progress_bars']:
        if bar['id'] == 'relational_organizing_growth_engine':
            bar['value'] = s['relational_organizing_growth_engine_readiness_pct']

mc['builds'].insert(0, {
    'number': 69,
    'title': title,
    'version': '1.73.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Relational Organizing Engine — primary expansion through trusted relationships to 200K',
    'summary': (
        f"Growth formula, relationship trees, share hub, circles, leader referral dashboard; "
        f"{s['relational_organizing_growth_engine_readiness_pct']}% readiness. "
        f"0 trees · 0 invitations · 0/{s['connected_target']} connected."
    ),
    'files_created': [
        'data/relational-organizing-growth-engine.json',
        'docs/MASTER_RELATIONAL_ORGANIZING_GROWTH_ENGINE.md',
        'builds/069-relational-organizing-growth-engine.md',
        'mission-control/relational-organizing-growth-engine.html',
        'scripts/gen-relational-organizing-growth-engine.py',
        'scripts/update-mc-build69.py',
    ],
    'files_modified': ['js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml'],
    'pages_created': ['/mission-control/relational-organizing-growth-engine.html'],
    'decisions_made': [
        'Primary expansion strategy — relational, not advertising/SEO/social',
        'Five-people question — no pressure, no quotas',
        'Share hub emphasis: helpful, not agreement-required',
        'Privacy: trust outweighs growth; never require invitations',
        'Unifies Neighborhood Organizing (#57) + Relationship OS (#59) + Action Network',
        'Leader referral dashboard — mentorship not competition',
        f"{s['relational_organizing_growth_engine_readiness_pct']}% readiness — constitution only",
    ],
    'open_questions': [
        'Referral tracking: anonymous counts vs named trees?',
        'Share hub: single component vs per-content-type?',
        'Reconcile primary expansion (#69) vs primary growth engine (#64)?',
        'Public relationship tree opt-in model?',
    ],
    'risks': rog['catalog_gaps'][:4],
    'next_recommended': 70,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/relational-organizing-growth-engine.html',
    'review_status': 'complete',
})

mc['briefing'] = {
    'what_built': 'Relational Organizing Growth Engine v1.0 — network effect, trusted relationships',
    'building_now': '69 builds specified — implementation translation next',
    'blocked': ['Share hub', 'Relationship trees', 'Referral tracking', 'Leader dashboard'],
    'ready_public': ['Growth formula', 'Privacy principles', 'Share hub spec', 'Recognition milestones'],
    'next': 'Build #70 — Implementation translation layer & engineering artifacts',
}

if not any(n.get('id') == 'relational_organizing_growth_engine' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'relational_organizing_growth_engine',
        'label': 'Relational Growth Engine',
        'href': '/mission-control/relational-organizing-growth-engine.html',
        'status': 'complete',
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
