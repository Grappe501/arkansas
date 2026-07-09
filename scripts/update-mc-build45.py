import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json', encoding='utf-8') as f:
    mc = json.load(f)

title = 'Citizens United Facts Master Systems Integration Blueprint'

with open(root / 'data/systems-integration.json', encoding='utf-8') as f:
    si = json.load(f)

s = si['summary']
health = si['systems_health_dashboard']

mc['version'] = '1.49.0'
mc['build'] = 45
mc['updated'] = '2026-07-09'
mc['systems_integration'] = '/data/systems-integration.json'
mc['systems_integration_dashboard'] = '/mission-control/systems-integration.html'

mc['executive'] = {
    'overall_completion': 45,
    'current_build': {'number': 45, 'title': title},
    'active_phase': 'Institutional Operating Model — Systems Integration Blueprint',
    'last_completed': 'Master Institutional Roadmap',
    'next_build': {'number': 46, 'title': 'Component specifications with props/states'},
    'github_status': 'connected',
    'netlify_status': 'production_healthy',
    'content_readiness': 26,
    'research_readiness': 25,
    'data_viz_readiness': 6,
    'signup_funnel_readiness': 22,
    'civic_action_readiness': 26,
    'coalition_readiness': 18,
    'data_model_readiness': 38,
    'route_inventory_readiness': 18,
    'component_registry_readiness': 22,
    'facts_framework_readiness': 14,
    'knowledge_atlas_readiness': 20,
    'platform_architecture_readiness': 20,
    'repository_structure_readiness': 28,
    'database_schema_readiness': 36,
    'wireframe_readiness': 38,
    'contact_intelligence_readiness': 31,
    'mc2_readiness': 33,
    'ai_engine_readiness': 14,
    'content_factory_readiness': 28,
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
    'institutional_maturity_pct': 32,
    'current_institutional_version': 'V1',
    'systems_integration_readiness': s['systems_integration_readiness_pct'],
    'public_launch_readiness': 8,
    'public_launch_label': 'Early Foundation'
}

mc['systems_integration_inventory'] = {
    'readiness_score': s['systems_integration_readiness_pct'],
    'systems_total': s['systems_total'],
    'systems_with_live_data_flow': s['systems_with_live_data_flow'],
    'avg_system_integration_pct': s['avg_system_integration_pct'],
    'avg_systems_health_score': s['avg_systems_health_score'],
    'executive_synthesis_live': s['executive_synthesis_live'],
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 45
        bar['note'] = f"Systems Integration live — 12 systems, {s['systems_with_live_data_flow']} live data flows."
    if bar['id'] == 'institutional_maturity':
        bar['value'] = 32
        bar['note'] = 'Institutional maturity V1 — 32% overall.'

if not any(b.get('id') == 'systems_integration' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'systems_integration',
        'label': 'Systems Integration Blueprint',
        'value': s['systems_integration_readiness_pct'],
        'max': 100,
        'note': f"{s['systems_with_live_data_flow']}/12 live flows — no event bus."
    })
else:
    for bar in mc['progress_bars']:
        if bar['id'] == 'systems_integration':
            bar['value'] = s['systems_integration_readiness_pct']
            bar['note'] = f"{s['systems_with_live_data_flow']}/12 live flows."

mc['builds'].insert(0, {
    'number': 45,
    'title': title,
    'version': '1.49.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Institutional Operating Model v1.0 — twelve systems working as one institution',
    'summary': f"12 systems, {s['systems_with_live_data_flow']} live flows, avg {s['avg_system_integration_pct']}% integration; {s['systems_integration_readiness_pct']}% overall.",
    'files_created': [
        'data/systems-integration.json', 'docs/MASTER_SYSTEMS_INTEGRATION.md',
        'builds/045-master-systems-integration-blueprint.md', 'mission-control/systems-integration.html',
        'scripts/gen-systems-integration.py', 'scripts/update-mc-build45.py'
    ],
    'files_modified': ['js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml'],
    'pages_created': ['/mission-control/systems-integration.html'],
    'decisions_made': [
        '12 primary systems — public education through contact network',
        'Produces/consumes model per system — KG as nervous system, MC as conductor',
        '10-stage information flow cycle — research back to research',
        'Systems Health dashboard — 10 health indicators from MC executive',
        '3 systems with live data flow — Source Library, Evidence Ledger, Mission Control',
        f"{s['systems_integration_readiness_pct']}% honest readiness — no event bus"
    ],
    'open_questions': ['Event bus vs static JSON linking?', 'User journey progress tracking?', 'KG consume-all-systems timing?'],
    'risks': ['Architecture without operational integration', 'Executive questions manual only', '0 signups breaks journey'],
    'next_recommended': 46,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/systems-integration.html',
    'review_status': 'complete'
})

mc['briefing'] = {
    'what_built': 'Systems Integration v1.0 — 12 systems, information flow, Systems Health, executive questions',
    'building_now': 'Taxonomy and MC linking — 3/12 live cross-system data flows',
    'blocked': ['Cross-system event bus', 'Executive synthesis', 'User journey tracking'],
    'ready_public': ['Systems Integration MC dashboard', '12-system operating model', 'Health indicators'],
    'next': 'Build #46 — Component specifications with props/states'
}

if not any(n.get('id') == 'systems_integration' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'systems_integration', 'label': 'Systems Integration Blueprint', 'href': '/mission-control/systems-integration.html', 'status': 'complete'
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
