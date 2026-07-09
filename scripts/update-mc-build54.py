import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json', encoding='utf-8') as f:
    mc = json.load(f)

title = 'Citizens United Facts Master Project Management Office (PMO) v1.0'

with open(root / 'data/pmo.json', encoding='utf-8') as f:
    pmo = json.load(f)

s = pmo['summary']

mc['version'] = '1.58.0'
mc['build'] = 54
mc['updated'] = '2026-07-09'
mc['pmo'] = '/data/pmo.json'
mc['pmo_dashboard'] = '/mission-control/pmo.html'

mc['executive'] = {
    'overall_completion': 54,
    'current_build': {'number': 54, 'title': title},
    'active_phase': 'PMO — Institutional Execution System',
    'last_completed': 'Master Launch Strategy & Arkansas Rollout Blueprint',
    'next_build': {'number': 55, 'title': 'Master implementation roadmap & sprint zero'},
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
    'institutional_maturity_pct': 40,
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
    'pmo_readiness': s['pmo_readiness_pct'],
    'rollout_phase': 0,
    'rollout_phase_title': 'Private Development',
    'planning_phase_complete': True,
    'implementation_phase': 'pmo_established',
    'public_launch_readiness': 8,
    'public_launch_label': 'Early Foundation',
    'public_launch_recommended': False,
}

mc['pmo_inventory'] = {
    'readiness_score': s['pmo_readiness_pct'],
    'departments_total': s['departments_total'],
    'avg_department_readiness_pct': s['avg_department_readiness_pct'],
    'owners_assigned': s['owners_assigned'],
    'risks_open': s['risks_open'],
    'work_items_logged': s['work_items_logged'],
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 54
        bar['note'] = 'Build #54 — Master PMO established. Execution system live.'
    if bar['id'] == 'institutional_maturity':
        bar['value'] = 40
        bar['note'] = '10 departments · PMO cockpit operational.'

if not any(b.get('id') == 'pmo' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'pmo',
        'label': 'Project Management Office',
        'value': s['pmo_readiness_pct'],
        'max': 100,
        'note': f"{s['avg_department_readiness_pct']}% avg dept readiness · {s['owners_assigned']}/10 owners."
    })
else:
    for bar in mc['progress_bars']:
        if bar['id'] == 'pmo':
            bar['value'] = s['pmo_readiness_pct']
            bar['note'] = 'PMO constitution — sprint backlog pending.'

mc['builds'].insert(0, {
    'number': 54,
    'title': title,
    'version': '1.58.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Institutional execution system — 10 departments, PMO workflow, risk register',
    'summary': (
        f"10 departments, {s['avg_department_readiness_pct']}% avg readiness, "
        f"{s['risks_open']} open risks, {s['pmo_readiness_pct']}% PMO readiness."
    ),
    'files_created': [
        'data/pmo.json', 'docs/MASTER_PMO.md',
        'builds/054-master-pmo.md', 'mission-control/pmo.html',
        'scripts/gen-pmo.py', 'scripts/update-mc-build54.py'
    ],
    'files_modified': ['js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml'],
    'pages_created': ['/mission-control/pmo.html'],
    'decisions_made': [
        '10 permanent PMO departments (100–1000) with primary dashboards',
        '10-stage initiative lifecycle — Idea through Maintenance',
        'Universal work item schema — builds registry as interim store',
        'Living risk register — 10 institutional risks documented',
        'Dependency chain Evidence → Claims → Articles → Curriculum → Academy → Conversations',
        'Mission Control = PMO operational cockpit',
        f"{s['pmo_readiness_pct']}% PMO readiness — owners and sprint backlog pending"
    ],
    'open_questions': [
        'Department owner assignments?',
        'Sprint Zero start date?',
        'Weekly briefing automation?',
        'Work items in Neon vs builds[]?',
    ],
    'risks': pmo['catalog_gaps'][:4],
    'next_recommended': 55,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/pmo.html',
    'review_status': 'complete'
})

mc['briefing'] = {
    'what_built': 'PMO v1.0 — 10 departments, workflow, risk register, dependency maps, PMO dashboard',
    'building_now': 'PMO established — Sprint Zero and department owners next',
    'blocked': ['0 department owners', 'No sprint backlog', 'Unified task DB', 'Calendar integration'],
    'ready_public': ['PMO dashboard', 'Department readiness matrix', 'Risk register', 'Daily five questions'],
    'next': 'Build #55 — Master implementation roadmap & sprint zero'
}

if not any(n.get('id') == 'pmo' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'pmo',
        'label': 'Project Management Office',
        'href': '/mission-control/pmo.html',
        'status': 'complete'
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
