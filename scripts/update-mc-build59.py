import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json', encoding='utf-8') as f:
    mc = json.load(f)

title = 'Citizens United Facts Arkansas Civic Action CRM & Relationship Operating System v1.0'

with open(root / 'data/relationship-os.json', encoding='utf-8') as f:
    ros = json.load(f)

s = ros['summary']

mc['version'] = '1.63.0'
mc['build'] = 59
mc['updated'] = '2026-07-09'
mc['relationship_os'] = '/data/relationship-os.json'
mc['relationship_os_dashboard'] = '/mission-control/relationship-os.html'

mc['executive'] = {
    'overall_completion': 59,
    'current_build': {'number': 59, 'title': title},
    'active_phase': 'Relationship OS → Implementation Translation',
    'last_completed': 'Arkansas Civic Atlas',
    'next_build': {'number': 60, 'title': 'Implementation translation layer & engineering artifacts'},
    'github_status': 'connected',
    'netlify_status': 'production_healthy',
    'content_readiness': 28,
    'research_readiness': 25,
    'data_viz_readiness': 8,
    'signup_funnel_readiness': 22,
    'civic_action_readiness': 28,
    'coalition_readiness': 18,
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
    'relationship_os_readiness': s['relationship_os_readiness_pct'],
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
    'civic_intelligence_readiness': 28,
    'evidence_ledger_readiness': 22,
    'civic_action_lab_readiness': 26,
    'research_methodology_readiness': 25,
    'institutional_maturity_pct': 46,
    'current_institutional_version': 'V1',
    'systems_integration_readiness': 30,
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

mc['relationship_os_inventory'] = {
    'readiness_score': s['relationship_os_readiness_pct'],
    'five_networks': 5,
    'active_relationships': s['active_relationships'],
    'relationship_edges': s['relationship_edges'],
    'crm_widgets_live': s['crm_widgets_live'],
    'core_intelligence_system': True,
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 59
        bar['note'] = 'Build #59 — Relationship Operating System (ROS).'
    if bar['id'] == 'institutional_maturity':
        bar['value'] = 46
        bar['note'] = 'Institutional relationship brain live — 0 active relationships.'

if not any(b.get('id') == 'relationship_os' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'relationship_os',
        'label': 'Relationship OS',
        'value': s['relationship_os_readiness_pct'],
        'max': 100,
        'note': f"5 networks · {s['relationship_edges']} edges · {s['active_relationships']} active."
    })
else:
    for bar in mc['progress_bars']:
        if bar['id'] == 'relationship_os':
            bar['value'] = s['relationship_os_readiness_pct']
            bar['note'] = 'Institutional CRM — civic education relationships.'

mc['builds'].insert(0, {
    'number': 59,
    'title': title,
    'version': '1.63.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Relationship Operating System — institutional CRM for civic education',
    'summary': (
        f"5 relationship networks; CRM dashboard; health score model; "
        f"{s['relationship_os_readiness_pct']}% ROS readiness. "
        f"0 active relationships · {s['relationship_edges']} edges."
    ),
    'files_created': [
        'data/relationship-os.json', 'docs/MASTER_RELATIONSHIP_OS.md',
        'builds/059-relationship-os.md', 'mission-control/relationship-os.html',
        'scripts/gen-relationship-os.py', 'scripts/update-mc-build59.py',
    ],
    'files_modified': ['js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml'],
    'pages_created': ['/mission-control/relationship-os.html'],
    'decisions_made': [
        'ROS = institutional relationship brain — not sales/fundraising CRM',
        'Five networks: Individual, Organization, Community, Public Official, Institutional',
        'Relationship philosophy: story not contact',
        'Extends Contact Intelligence (#24) and Relationship Registry (#15)',
        'Relationship Health Score — 6 indicators defined',
        '10 CRM dashboard widgets — 5 live with zero counts',
        f"{s['relationship_os_readiness_pct']}% readiness — architecture documented, CRM empty",
    ],
    'open_questions': [
        'ROS vs Contact Intelligence UI consolidation?',
        'Public official tracking: opt-in vs public record only?',
        'Health score weighting and decay model?',
        'Timeline events: single table vs activity stream?',
    ],
    'risks': ros['catalog_gaps'][:4],
    'next_recommended': 60,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/relationship-os.html',
    'review_status': 'complete'
})

mc['briefing'] = {
    'what_built': 'Relationship OS v1.0 — 5 networks, CRM dashboard, institutional relationship brain',
    'building_now': 'Community + relationship intelligence stack (#56–#59) — translation next',
    'blocked': ['Neon participant schema', 'Timeline events', 'Health scoring', 'Mentorship graph'],
    'ready_public': ['5 network model', 'CRM widgets', 'Privacy framework', 'Opportunity tracker'],
    'next': 'Build #60 — Implementation translation layer & engineering artifacts'
}

if not any(n.get('id') == 'relationship_os' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'relationship_os',
        'label': 'Relationship OS',
        'href': '/mission-control/relationship-os.html',
        'status': 'complete'
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
