import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json') as f:
    mc = json.load(f)

title = 'Citizens United Facts Master Curriculum & Learning Standards'

with open(root / 'data/master-curriculum.json') as f:
    curr = json.load(f)

s = curr['summary']
cc = curr['curriculum_completion']

mc['version'] = '1.39.0'
mc['build'] = 35
mc['updated'] = '2026-07-09'
mc['master_curriculum'] = '/data/master-curriculum.json'
mc['curriculum_dashboard'] = '/mission-control/curriculum.html'

mc['executive'] = {
    'overall_completion': 35,
    'current_build': {'number': 35, 'title': title},
    'active_phase': 'Educational Framework — Six-Tier Master Curriculum',
    'last_completed': 'Storytelling & Narrative Architecture',
    'next_build': {'number': 36, 'title': 'Component specifications with props/states'},
    'github_status': 'connected',
    'netlify_status': 'production_healthy',
    'content_readiness': 26,
    'research_readiness': 24,
    'data_viz_readiness': 4,
    'signup_funnel_readiness': 22,
    'civic_action_readiness': 32,
    'coalition_readiness': 18,
    'data_model_readiness': 38,
    'route_inventory_readiness': 18,
    'component_registry_readiness': 22,
    'facts_framework_readiness': 12,
    'knowledge_atlas_readiness': 20,
    'platform_architecture_readiness': 20,
    'repository_structure_readiness': 28,
    'database_schema_readiness': 35,
    'wireframe_readiness': 38,
    'contact_intelligence_readiness': 31,
    'mc2_readiness': 33,
    'ai_engine_readiness': 14,
    'content_factory_readiness': 28,
    'education_academy_readiness': 26,
    'observatory_readiness': 18,
    'outreach_readiness': 22,
    'county_os_readiness': 28,
    'campaign_os_readiness': 34,
    'encyclopedia_readiness': 19,
    'narrative_readiness': 24,
    'curriculum_readiness': s['curriculum_readiness_pct'],
    'public_launch_readiness': 8,
    'public_launch_label': 'Early Foundation'
}

mc['curriculum_inventory'] = {
    'readiness_score': s['curriculum_readiness_pct'],
    'tiers_total': s['tiers_total'],
    'avg_tier_completion_pct': s['avg_tier_completion_pct'],
    'lessons_live': s['lessons_live'],
    'lessons_total': s['lessons_total'],
    'learning_paths': s['learning_paths'],
    'curriculum_completion': cc,
    'enrollment_tracking_live': s['enrollment_tracking_live'],
    'assessments_live': s['assessments_live'],
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 35
        bar['note'] = f"Curriculum live — 6 tiers, {s['lessons_live']}/{s['lessons_total']} lessons, understanding before opinion."

if not any(b.get('id') == 'curriculum' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'curriculum',
        'label': 'Master Curriculum',
        'value': s['curriculum_readiness_pct'],
        'max': 100,
        'note': f"Avg tier {s['avg_tier_completion_pct']}% — enrollment tracking not live."
    })

mc['builds'].insert(0, {
    'number': 35,
    'title': title,
    'version': '1.39.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Educational Framework v1.0 — six tiers, five paths, knowledge over page views',
    'summary': f"{s['tiers_total']} tiers, {s['learning_paths']} paths, {s['lessons_live']}/{s['lessons_total']} lessons; {s['curriculum_readiness_pct']}% readiness.",
    'files_created': [
        'data/master-curriculum.json', 'docs/MASTER_CURRICULUM.md',
        'builds/035-master-curriculum.md', 'mission-control/curriculum.html',
        'scripts/gen-master-curriculum.py', 'scripts/update-mc-build35.py'
    ],
    'files_modified': ['js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml'],
    'pages_created': ['/mission-control/curriculum.html'],
    'decisions_made': [
        '6 learning tiers — Foundations through Arkansas Civic Education',
        '6 guided learning paths including Public Official Resource Path',
        '4 reading levels aligned to facts/narrative layers',
        'Understanding before opinion — civic engagement after foundation',
        'Aligned to Education Academy (8 modules) and Narrative (8 acts)',
        f"{s['curriculum_readiness_pct']}% honest readiness — interim hall content, no enrollment tracking"
    ],
    'open_questions': ['When to build canonical /learn routes?', 'Self-assessment implementation?'],
    'risks': ['No lesson completion tracking', 'Tier 6 untested', 'Assessments not built'],
    'next_recommended': 36,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/curriculum.html',
    'review_status': 'complete'
})

mc['briefing'] = {
    'what_built': f'Curriculum v1.0 — 6 tiers, 6 paths, 4 reading levels, 9-system integration',
    'building_now': 'Master curriculum — halls as interim tier content',
    'blocked': ['Enrollment not tracked', 'Assessments not built', 'Canonical lesson routes not built'],
    'ready_public': ['Curriculum MC dashboard', 'Tier architecture', 'Learning paths', 'Academy alignment'],
    'next': 'Build #36 — Component specifications with props/states'
}

if not any(n.get('id') == 'curriculum' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'curriculum', 'label': 'Master Curriculum', 'href': '/mission-control/curriculum.html', 'status': 'complete'
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
