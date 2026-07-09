import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json', encoding='utf-8') as f:
    mc = json.load(f)

title = 'Citizens United Facts Master Arkansas Coalition & Civic Alliance Network v1.0'

with open(root / 'data/coalition-network.json', encoding='utf-8') as f:
    cn = json.load(f)

s = cn['summary']

mc['version'] = '1.65.0'
mc['build'] = 61
mc['updated'] = '2026-07-09'
mc['coalition_network'] = '/data/coalition-network.json'
mc['coalition_network_dashboard'] = '/mission-control/coalition-network.html'

mc['executive'] = {
    'overall_completion': 61,
    'current_build': {'number': 61, 'title': title},
    'active_phase': 'Coalition Network → Implementation Translation',
    'last_completed': 'Institutional AI Brain',
    'next_build': {'number': 62, 'title': 'Implementation translation layer & engineering artifacts'},
    'github_status': 'connected',
    'netlify_status': 'production_healthy',
    'content_readiness': 28,
    'research_readiness': 25,
    'data_viz_readiness': 8,
    'signup_funnel_readiness': 22,
    'civic_action_readiness': 28,
    'coalition_readiness': max(s['coalition_readiness_pct'], s['coalition_network_readiness_pct'] - 4),
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
    'coalition_network_readiness': s['coalition_network_readiness_pct'],
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
    'civic_action_lab_readiness': 26,
    'research_methodology_readiness': 25,
    'institutional_maturity_pct': 48,
    'current_institutional_version': 'V1',
    'systems_integration_readiness': 34,
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
    'civic_atlas_readiness': s['civic_atlas_readiness_pct'],
    'rollout_phase': 0,
    'rollout_phase_title': 'Private Development',
    'planning_phase_complete': True,
    'planning_constitution_complete': True,
    'implementation_phase': 'translation_layer_next',
    'public_launch_readiness': s['public_launch_readiness_pct'],
    'public_launch_label': 'Early Foundation',
    'public_launch_recommended': False,
}

mc['coalition_network_inventory'] = {
    'readiness_score': s['coalition_network_readiness_pct'],
    'organizations': s['organizations_total'],
    'counties_represented': s['counties_represented'],
    'counties_total': s['counties_total'],
    'strategic_priority': 'highest',
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 61
        bar['note'] = 'Build #61 — Coalition & Civic Alliance Network.'
    if bar['id'] == 'institutional_maturity':
        bar['value'] = 48
        bar['note'] = 'Coalition framework live — 0 orgs, 0/75 counties.'
    if bar['id'] == 'coalition':
        bar['value'] = mc['executive']['coalition_readiness']
        bar['note'] = 'Master coalition network — highest strategic priority.'

if not any(b.get('id') == 'coalition_network' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'coalition_network',
        'label': 'Coalition Network',
        'value': s['coalition_network_readiness_pct'],
        'max': 100,
        'note': f"0 orgs · {s['counties_represented']}/{s['counties_total']} counties."
    })
else:
    for bar in mc['progress_bars']:
        if bar['id'] == 'coalition_network':
            bar['value'] = s['coalition_network_readiness_pct']

mc['builds'].insert(0, {
    'number': 61,
    'title': title,
    'version': '1.65.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Master coalition operating framework — Building Arkansas Together',
    'summary': (
        f"6 categories, 4 partnership levels, resource center, collaboration hub; "
        f"{s['coalition_network_readiness_pct']}% coalition network readiness. "
        f"0 orgs · 0/75 counties."
    ),
    'files_created': [
        'data/coalition-network.json', 'docs/MASTER_COALITION_NETWORK.md',
        'builds/061-coalition-network.md', 'mission-control/coalition-network.html',
        'scripts/gen-coalition-network.py', 'scripts/update-mc-build61.py',
    ],
    'files_modified': ['js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml'],
    'pages_created': ['/mission-control/coalition-network.html'],
    'decisions_made': [
        'Coalition multiplies capacity — does not replace organizations',
        'Common ground: evidence-based education regardless of policy disagreement',
        '6 partnership categories + 4 partnership levels',
        'County coalition dashboard per county — 75 scaffolds',
        'Coalition health = highest MC strategic priority',
        'Unifies ACUCOS (#14) into master operating framework',
        f"{s['coalition_network_readiness_pct']}% readiness — framework documented, 0 partners",
    ],
    'open_questions': [
        'Map Build #61 levels to ACUCOS six participation levels?',
        'Faith communities: separate category or under community orgs?',
        'Partner portal vs coalition hub at /coalition/?',
        'Partnership request workflow: Netlify Forms vs Neon?',
    ],
    'risks': cn['catalog_gaps'][:4],
    'next_recommended': 62,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/coalition-network.html',
    'review_status': 'complete'
})

mc['briefing'] = {
    'what_built': 'Coalition Network v1.0 — 6 categories, 4 levels, resource center, collaboration hub',
    'building_now': '61 builds specified — implementation translation next',
    'blocked': ['Partner signup', 'Request workflow', 'Collaboration hub', 'Recognition archive'],
    'ready_public': ['Coalition principles', 'Growth metrics', 'County dashboard spec', 'Resource center index'],
    'next': 'Build #62 — Implementation translation layer & engineering artifacts'
}

if not any(n.get('id') == 'coalition_network' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'coalition_network',
        'label': 'Coalition Network',
        'href': '/mission-control/coalition-network.html',
        'status': 'complete'
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
