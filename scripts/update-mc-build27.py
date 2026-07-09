import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json') as f:
    mc = json.load(f)

title = 'Citizens United Facts Content Production Factory'

with open(root / 'data/content-production-factory.json') as f:
    cpf = json.load(f)

s = cpf['summary']

mc['version'] = '1.31.0'
mc['build'] = 27
mc['updated'] = '2026-07-09'
mc['content_production_factory'] = '/data/content-production-factory.json'
mc['content_factory_dashboard'] = '/mission-control/content-factory.html'

mc['executive'] = {
    'overall_completion': 27,
    'current_build': {'number': 27, 'title': title},
    'active_phase': 'Editorial Operating System — Content Production Factory',
    'last_completed': 'AI Knowledge & Research Engine',
    'next_build': {'number': 28, 'title': 'Component specifications with props/states'},
    'github_status': 'connected',
    'netlify_status': 'production_healthy',
    'content_readiness': 20,
    'research_readiness': 20,
    'data_viz_readiness': 2,
    'signup_funnel_readiness': 18,
    'civic_action_readiness': 26,
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
    'public_launch_readiness': 8,
    'public_launch_label': 'Early Foundation'
}

mc['content_factory_inventory'] = {
    'readiness_score': s['factory_readiness_pct'],
    'content_types': s['content_types'],
    'workflow_stages': s['workflow_stages'],
    'assets_registered': s['assets_registered'],
    'assets_published': s['assets_published'],
    'assets_in_pipeline': s['assets_in_pipeline'],
    'automated_review_scheduling': s['automated_review_scheduling'],
    'workflow_dashboard_live': s['workflow_dashboard_live'],
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 27
        bar['note'] = f"Content factory live — {s['content_types']} types, {s['assets_registered']} assets registered, {s['workflow_stages']}-stage workflow."
    if bar['id'] == 'content':
        bar['value'] = 20
        bar['note'] = f"Editorial OS defined — {s['assets_published']} published of {s['assets_registered']} registered. Factory dashboard at content-factory.html."

if not any(b.get('id') == 'content_factory' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'content_factory',
        'label': 'Content Production Factory',
        'value': 28,
        'max': 100,
        'note': f"{s['assets_in_pipeline']} in pipeline — workflow aligned with content inventory; automation pending."
    })

mc['builds'].insert(0, {
    'number': 27,
    'title': title,
    'version': '1.31.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Editorial Operating System v1.0 — one institution, one voice',
    'summary': f"{s['content_types']} types, {s['workflow_stages']} workflow stages, {s['assets_registered']} assets; {s['factory_readiness_pct']}% factory readiness.",
    'files_created': [
        'data/content-production-factory.json', 'docs/CONTENT_PRODUCTION_FACTORY.md',
        'builds/027-content-production-factory.md', 'mission-control/content-factory.html',
        'scripts/gen-content-production-factory.py', 'scripts/update-mc-build27.py'
    ],
    'files_modified': ['js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml'],
    'pages_created': ['/mission-control/content-factory.html'],
    'decisions_made': [
        '7 content type templates with standard article structure (10 sections)',
        '11-stage editorial workflow aligned to content-inventory lifecycle',
        'L1–L4 reading levels mapped to facts framework depths',
        '6 quality gates before publication',
        '5 evergreen review policies defined',
        '28% honest readiness — inventory exists, factory automation not built'
    ],
    'open_questions': ['When to automate evergreen review alerts?', 'Minimum published count before public launch?'],
    'risks': ['351 assets registered but few published', 'Citation completeness not computed'],
    'next_recommended': 28,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/content-factory.html',
    'review_status': 'complete'
})

mc['briefing'] = {
    'what_built': f'Content Production Factory v1.0 — {s["content_types"]} types, {s["workflow_stages"]}-stage workflow, institutional voice',
    'building_now': 'Editorial OS — component specs to map article sections next',
    'blocked': ['Workflow dashboard not unified', 'Evergreen review not automated', 'L3/L4 sparse'],
    'ready_public': ['Factory MC dashboard', 'Content type templates', 'Workflow + quality gates', 'Inventory alignment'],
    'next': 'Build #28 — Component specifications with props/states'
}

if not any(n.get('id') == 'content_factory' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'content_factory', 'label': 'Content Production Factory', 'href': '/mission-control/content-factory.html', 'status': 'complete'
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
