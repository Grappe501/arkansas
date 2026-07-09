import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json') as f:
    mc = json.load(f)

title = 'Citizens United Facts Community Education Academy'

with open(root / 'data/education-academy.json') as f:
    acad = json.load(f)

s = acad['summary']

mc['version'] = '1.32.0'
mc['build'] = 28
mc['updated'] = '2026-07-09'
mc['education_academy'] = '/data/education-academy.json'
mc['education_academy_dashboard'] = '/mission-control/education-academy.html'

mc['executive'] = {
    'overall_completion': 28,
    'current_build': {'number': 28, 'title': title},
    'active_phase': 'Education Leader Development — Community Education Academy',
    'last_completed': 'Content Production Factory',
    'next_build': {'number': 29, 'title': 'Component specifications with props/states'},
    'github_status': 'connected',
    'netlify_status': 'production_healthy',
    'content_readiness': 20,
    'research_readiness': 20,
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
    'public_launch_readiness': 8,
    'public_launch_label': 'Early Foundation'
}

mc['education_academy_inventory'] = {
    'readiness_score': s['academy_readiness_pct'],
    'learning_stages': s['learning_stages'],
    'curriculum_modules': s['curriculum_modules'],
    'modules_partial': s['modules_partial'],
    'audience_toolkits': s['audience_toolkits'],
    'enrollment_tracking_live': s['enrollment_tracking_live'],
    'module_progress_live': s['module_progress_live'],
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 28
        bar['note'] = f"Education Academy live — {s['curriculum_modules']} modules, 4 learning stages. Highest-impact program architecture."
    if bar['id'] == 'signup':
        bar['value'] = 20
        bar['note'] = f"Academy defined — educate signup partial; module progress tracking not built."

if not any(b.get('id') == 'education_academy' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'education_academy',
        'label': 'Education Academy',
        'value': 24,
        'max': 100,
        'note': f"{s['modules_partial']} modules partial via hall pages — no enrollment/progress backend."
    })

mc['builds'].insert(0, {
    'number': 28,
    'title': title,
    'version': '1.32.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Arkansas Education Leader Development System v1.0 — civic education, not advocacy',
    'summary': f"{s['learning_stages']} stages, {s['curriculum_modules']} modules, certification + toolkit; {s['academy_readiness_pct']}% readiness.",
    'files_created': [
        'data/education-academy.json', 'docs/COMMUNITY_EDUCATION_ACADEMY.md',
        'builds/028-education-academy.md', 'mission-control/education-academy.html',
        'scripts/gen-education-academy.py', 'scripts/update-mc-build28.py'
    ],
    'files_modified': ['js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml'],
    'pages_created': ['/mission-control/education-academy.html'],
    'decisions_made': [
        '4 learning stages: Learn → Understand → Communicate → Lead',
        '8 curriculum modules mapped to knowledge atlas worlds + interim routes',
        'Community Conversation Certification — educational only, not government credential',
        '7 audience-specific toolkits + 8-item presentation toolkit',
        '24% honest readiness — educate signup partial, no module tracking',
        'Highest-impact program per MC briefing'
    ],
    'open_questions': ['When to build module progress UI?', 'Certification badge design?'],
    'risks': ['24% readiness — curriculum is architecture not full academy', 'No enrollment backend'],
    'next_recommended': 29,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/education-academy.html',
    'review_status': 'complete'
})

mc['briefing'] = {
    'what_built': f'Education Academy v1.0 — {s["learning_stages"]} stages, {s["curriculum_modules"]} modules, leader development system',
    'building_now': 'Highest-impact program architecture — component specs next',
    'blocked': ['No module progress tracking', 'Certification not operational', 'Most toolkit materials planned'],
    'ready_public': ['Academy MC dashboard', 'Curriculum map', 'Learning stages', 'Leadership metrics schema'],
    'next': 'Build #29 — Component specifications with props/states'
}

if not any(n.get('id') == 'education_academy' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'education_academy', 'label': 'Education Academy', 'href': '/mission-control/education-academy.html', 'status': 'complete'
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
