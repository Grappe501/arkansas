import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json') as f:
    mc = json.load(f)

title = 'Mission Control 2.0 & Executive Command Center'

with open(root / 'data/mc2-executive.json') as f:
    mc2 = json.load(f)

s = mc2['summary']

mc['version'] = '1.29.0'
mc['build'] = 25
mc['updated'] = '2026-07-09'
mc['mc2_executive'] = '/data/mc2-executive.json'
mc['executive_dashboard'] = '/mission-control/executive.html'

mc['executive'] = {
    'overall_completion': 25,
    'current_build': {'number': 25, 'title': title},
    'active_phase': 'Executive Operating System — Mission Control 2.0',
    'last_completed': 'Contact Intelligence & Community Relationship Architecture',
    'next_build': {'number': 26, 'title': 'Component specifications with props/states'},
    'github_status': 'connected',
    'netlify_status': 'production_healthy',
    'content_readiness': 18,
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
    'public_launch_readiness': 8,
    'public_launch_label': 'Early Foundation'
}

mc['mc2_inventory'] = {
    'readiness_score': s['mc2_readiness_pct'],
    'workspaces': s['workspaces'],
    'health_indicators': s['health_indicators'],
    'overall_project_health': s['overall_project_health'],
    'smart_alerts_defined': s['smart_alerts_defined'],
    'smart_alerts_automated': s['smart_alerts_automated'],
    'builds_in_timeline': s['builds_in_timeline'],
    'workspace_partial': s['workspace_partial'],
    'workspace_planned': s['workspace_planned'],
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 25
        bar['note'] = f"MC2 executive command center live — {s['workspaces']} workspaces, {s['overall_project_health']}% project health."

if not any(b.get('id') == 'mc2' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'mc2',
        'label': 'Mission Control 2.0',
        'value': 33,
        'max': 100,
        'note': f"{s['workspace_partial']} workspaces partial, {s['smart_alerts_automated']} alerts automated — architecture defined."
    })

mc['builds'].insert(0, {
    'number': 25,
    'title': title,
    'version': '1.29.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Executive Operating System v1.0 — if it matters, it is visible',
    'summary': f"{s['workspaces']} workspaces, {s['health_indicators']} health indicators, {s['smart_alerts_defined']} alerts; {s['mc2_readiness_pct']}% MC2 readiness.",
    'files_created': [
        'data/mc2-executive.json', 'docs/MISSION_CONTROL_2.md',
        'builds/025-mission-control-2.md', 'mission-control/executive.html',
        'scripts/gen-mc2-executive.py', 'scripts/update-mc-build25.py'
    ],
    'files_modified': ['js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml'],
    'pages_created': ['/mission-control/executive.html'],
    'decisions_made': [
        '9 MC workspaces mapped to existing dashboards where live',
        '5 executive panels + Arkansas readiness map as signature visualization',
        '9 health indicators with honest scores from live registries',
        '8 smart alerts defined — 0 automated yet',
        'Build timeline pulls from mission-control.json builds array',
        '33% honest MC2 readiness — architecture complete, automation pending'
    ],
    'open_questions': ['When to automate smart alerts?', 'Analytics integration for Communications Center?'],
    'risks': ['33% readiness — reports and alerts not generatable', 'Command Center queues not operational'],
    'next_recommended': 26,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/executive.html',
    'review_status': 'complete'
})

mc['briefing'] = {
    'what_built': f'MC2 Executive Command Center — {s["workspaces"]} workspaces, health scores, build timeline',
    'building_now': 'Executive OS — component specs and alert automation next',
    'blocked': ['Smart alerts not automated', 'Executive reports not generatable', 'Communications Center no analytics'],
    'ready_public': ['Executive dashboard', 'Workspace map', 'Health indicators', 'Build timeline'],
    'next': 'Build #26 — Component specifications with props/states'
}

if not any(n.get('id') == 'mc2_executive' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'mc2_executive', 'label': 'Executive Command Center', 'href': '/mission-control/executive.html', 'status': 'complete'
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
