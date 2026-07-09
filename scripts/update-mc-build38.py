import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json') as f:
    mc = json.load(f)

title = 'Citizens United Facts Interactive Learning Laboratory'

with open(root / 'data/learning-laboratory.json') as f:
    lab = json.load(f)

s = lab['summary']

mc['version'] = '1.42.0'
mc['build'] = 38
mc['updated'] = '2026-07-09'
mc['learning_laboratory'] = '/data/learning-laboratory.json'
mc['learning_lab_dashboard'] = '/mission-control/learning-lab.html'

mc['executive'] = {
    'overall_completion': 38,
    'current_build': {'number': 38, 'title': title},
    'active_phase': 'Civic Discovery — Interactive Learning Laboratory',
    'last_completed': 'Master Research Library & Digital Archive',
    'next_build': {'number': 39, 'title': 'Component specifications with props/states'},
    'github_status': 'connected',
    'netlify_status': 'production_healthy',
    'content_readiness': 26,
    'research_readiness': 28,
    'data_viz_readiness': 6,
    'signup_funnel_readiness': 22,
    'civic_action_readiness': 32,
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
    'learning_lab_readiness': s['learning_lab_readiness_pct'],
    'public_launch_readiness': 8,
    'public_launch_label': 'Early Foundation'
}

mc['learning_lab_inventory'] = {
    'readiness_score': s['learning_lab_readiness_pct'],
    'laboratories_total': s['laboratories_total'],
    'laboratories_partial': s['laboratories_partial'],
    'interactive_experiences_live': s['interactive_experiences_live'],
    'avg_lab_readiness_pct': s['avg_lab_readiness_pct'],
    'engagement_tracking_live': s['engagement_tracking_live'],
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 38
        bar['note'] = f"Learning Lab live — 10 laboratories, {s['interactive_experiences_live']} interactive experiences deployed."
    if bar['id'] == 'data_viz':
        bar['value'] = 6
        bar['note'] = 'Learning Lab architecture — interactive viz planned, static halls interim.'

if not any(b.get('id') == 'learning_lab' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'learning_lab',
        'label': 'Interactive Learning Laboratory',
        'value': s['learning_lab_readiness_pct'],
        'max': 100,
        'note': f"{s['laboratories_partial']}/10 labs partial — 0 true interactive experiences."
    })

mc['builds'].insert(0, {
    'number': 38,
    'title': title,
    'version': '1.42.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Civic Discovery & Simulation System v1.0 — comprehension through interaction',
    'summary': f"10 laboratories, avg {s['avg_lab_readiness_pct']}% lab readiness; {s['learning_lab_readiness_pct']}% overall.",
    'files_created': [
        'data/learning-laboratory.json', 'docs/INTERACTIVE_LEARNING_LABORATORY.md',
        'builds/038-interactive-learning-laboratory.md', 'mission-control/learning-lab.html',
        'scripts/gen-learning-laboratory.py', 'scripts/update-mc-build38.py'
    ],
    'files_modified': ['js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml'],
    'pages_created': ['/mission-control/learning-lab.html'],
    'decisions_made': [
        '10 learning laboratories — timeline through education builder',
        'Discovery not entertainment — deeper comprehension goal',
        '5 accessibility standards per interactive experience',
        'Halls/map pages as interim — 0 interactive labs deployed',
        'KG lab aligned to 38-node registry — no public viz',
        f"{s['learning_lab_readiness_pct']}% honest readiness — architecture only"
    ],
    'open_questions': ['First interactive lab to build?', 'Analytics for lab usage?'],
    'risks': ['0 interactive experiences', 'data_viz at 6%', 'Engagement not tracked'],
    'next_recommended': 39,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/learning-lab.html',
    'review_status': 'complete'
})

mc['briefing'] = {
    'what_built': 'Learning Lab v1.0 — 10 laboratories, accessibility standards, MC engagement metrics',
    'building_now': 'Civic discovery architecture — halls as interim static labs',
    'blocked': ['No interactive viz deployed', 'Engagement tracking', 'Canonical /lab routes'],
    'ready_public': ['Learning Lab MC dashboard', '10-lab taxonomy', 'Interim hall mapping'],
    'next': 'Build #39 — Component specifications with props/states'
}

if not any(n.get('id') == 'learning_lab' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'learning_lab', 'label': 'Interactive Learning Laboratory', 'href': '/mission-control/learning-lab.html', 'status': 'complete'
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
