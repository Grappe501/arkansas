import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json') as f:
    mc = json.load(f)

title = 'Citizens United Facts Research Observatory'

with open(root / 'data/research-observatory.json') as f:
    obs = json.load(f)

s = obs['summary']

mc['version'] = '1.33.0'
mc['build'] = 29
mc['updated'] = '2026-07-09'
mc['research_observatory'] = '/data/research-observatory.json'
mc['research_observatory_dashboard'] = '/mission-control/research-observatory.html'

mc['executive'] = {
    'overall_completion': 29,
    'current_build': {'number': 29, 'title': title},
    'active_phase': 'Living Research — Research Observatory',
    'last_completed': 'Community Education Academy',
    'next_build': {'number': 30, 'title': 'Component specifications with props/states'},
    'github_status': 'connected',
    'netlify_status': 'production_healthy',
    'content_readiness': 20,
    'research_readiness': 22,
    'data_viz_readiness': 2,
    'signup_funnel_readiness': 20,
    'civic_action_readiness': 28,
    'coalition_readiness': 14,
    'data_model_readiness': 38,
    'route_inventory_readiness': 18,
    'component_registry_readiness': 22,
    'facts_framework_readiness': 12,
    'knowledge_atlas_readiness': 18,
    'platform_architecture_readiness': 20,
    'repository_structure_readiness': 28,
    'database_schema_readiness': 35,
    'wireframe_readiness': 38,
    'contact_intelligence_readiness': 31,
    'mc2_readiness': 33,
    'ai_engine_readiness': 14,
    'content_factory_readiness': 28,
    'education_academy_readiness': 24,
    'observatory_readiness': 18,
    'public_launch_readiness': 8,
    'public_launch_label': 'Early Foundation'
}

mc['observatory_inventory'] = {
    'readiness_score': s['observatory_readiness_pct'],
    'divisions': s['divisions'],
    'workflow_stages': s['workflow_stages'],
    'research_gaps_tracked': s['research_gaps_tracked'],
    'evidence_records': s['evidence_records'],
    'future_alerts_automated': s['future_alerts_automated'],
    'automated_monitoring_live': s['automated_monitoring_live'],
    'legislative_tracking_live': s['legislative_tracking_live'],
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 29
        bar['note'] = f"Research Observatory live — {s['divisions']} divisions, early warning system architecture."
    if bar['id'] == 'research':
        bar['value'] = 22
        bar['note'] = f"Observatory defined — {s['evidence_records']} evidence records, {s['research_gaps_tracked']} gaps tracked. No automated feeds."

if not any(b.get('id') == 'observatory' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'observatory',
        'label': 'Research Observatory',
        'value': 18,
        'max': 100,
        'note': f"{s['divisions_partial']} divisions partial — SCOTUS/AR legislature monitors not automated."
    })

mc['builds'].insert(0, {
    'number': 29,
    'title': title,
    'version': '1.33.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Living Research & Legislative Intelligence System v1.0 — platform early warning system',
    'summary': f"{s['divisions']} divisions, {s['workflow_stages']}-stage workflow, {s['research_gaps_tracked']} gaps; {s['observatory_readiness_pct']}% readiness.",
    'files_created': [
        'data/research-observatory.json', 'docs/RESEARCH_OBSERVATORY.md',
        'builds/029-research-observatory.md', 'mission-control/research-observatory.html',
        'scripts/gen-research-observatory.py', 'scripts/update-mc-build29.py'
    ],
    'files_modified': ['js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml'],
    'pages_created': ['/mission-control/research-observatory.html'],
    'decisions_made': [
        '6 research divisions: SCOTUS, federal, Arkansas, ballot, academic, spending',
        '9-stage workflow from Identified to Published',
        '3 priority levels for educational significance',
        'Legislative tracking page structure (7 sections)',
        'Research gaps pulled from evidence registry + platform gaps',
        '18% honest readiness — no automated monitoring feeds'
    ],
    'open_questions': ['Legislative data API source?', 'When to automate SCOTUS cert alerts?'],
    'risks': ['18% readiness — architecture only', '14 evidence records vs 500 target'],
    'next_recommended': 30,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/research-observatory.html',
    'review_status': 'complete'
})

mc['briefing'] = {
    'what_built': f'Research Observatory v1.0 — {s["divisions"]} divisions, early warning system for living research',
    'building_now': 'Legislative intelligence architecture — component specs next',
    'blocked': ['No automated monitoring', 'Legislative tracking not live', '0 academic sources'],
    'ready_public': ['Observatory MC dashboard', 'Division map', 'Workflow + priorities', 'Gap tracker'],
    'next': 'Build #30 — Component specifications with props/states'
}

if not any(n.get('id') == 'research_observatory' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'research_observatory', 'label': 'Research Observatory', 'href': '/mission-control/research-observatory.html', 'status': 'complete'
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
