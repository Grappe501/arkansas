import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json', encoding='utf-8') as f:
    mc = json.load(f)

title = 'Citizens United Facts Master Master Plan v1.0'

with open(root / 'data/master-plan.json', encoding='utf-8') as f:
    mp = json.load(f)

s = mp['summary']

mc['version'] = '1.59.0'
mc['build'] = 55
mc['updated'] = '2026-07-09'
mc['master_plan'] = '/data/master-plan.json'
mc['master_plan_dashboard'] = '/mission-control/master-plan.html'

mc['executive'] = {
    'overall_completion': 55,
    'current_build': {'number': 55, 'title': title},
    'active_phase': '★ Planning Constitution Complete → Engineering Translation',
    'last_completed': 'Master Project Management Office (PMO)',
    'next_build': {'number': 56, 'title': 'Implementation translation layer & engineering artifacts'},
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
    'institutional_maturity_pct': 42,
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
    'pmo_readiness': 46,
    'master_plan_readiness': s['master_plan_readiness_pct'],
    'rollout_phase': 0,
    'rollout_phase_title': 'Private Development',
    'planning_phase_complete': True,
    'planning_constitution_complete': True,
    'implementation_phase': 'translation_layer_next',
    'public_launch_readiness': s['public_launch_readiness_pct'],
    'public_launch_label': 'Early Foundation',
    'public_launch_recommended': False,
}

mc['master_plan_inventory'] = {
    'readiness_score': s['master_plan_readiness_pct'],
    'planning_builds': s['planning_builds_total'],
    'constitution_docs': s['constitution_docs'],
    'avg_engine_readiness_pct': s['avg_engine_readiness_pct'],
    'planning_constitution_complete': s['planning_constitution_complete'],
    'translation_layer_started': s['implementation_translation_started'],
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 55
        bar['note'] = '★ Build #55 — Master Master Plan. Planning constitution complete.'
    if bar['id'] == 'institutional_maturity':
        bar['value'] = 42
        bar['note'] = 'North Star document live — engineering translation next.'

if not any(b.get('id') == 'master_plan' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'master_plan',
        'label': 'Master Master Plan ★',
        'value': s['master_plan_readiness_pct'],
        'max': 100,
        'note': f"{s['planning_builds_total']} builds synthesized · {s['avg_engine_readiness_pct']}% avg engines."
    })
else:
    for bar in mc['progress_bars']:
        if bar['id'] == 'master_plan':
            bar['value'] = s['master_plan_readiness_pct']
            bar['note'] = 'Permanent North Star — translation layer next.'

mc['builds'].insert(0, {
    'number': 55,
    'title': title,
    'version': '1.59.0',
    'status': 'complete',
    'milestone': True,
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Complete institutional blueprint — permanent North Star constitution',
    'summary': (
        f"★ Milestone — {s['planning_builds_total']} builds synthesized, 12 pillars, 4 engines, "
        f"{s['master_plan_readiness_pct']}% master plan readiness. Translation layer next."
    ),
    'files_created': [
        'data/master-plan.json', 'docs/MASTER_MASTER_PLAN.md',
        'builds/055-master-master-plan.md', 'mission-control/master-plan.html',
        'scripts/gen-master-plan.py', 'scripts/update-mc-build55.py'
    ],
    'files_modified': ['js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml'],
    'pages_created': ['/mission-control/master-plan.html'],
    'decisions_made': [
        '★ Planning constitution complete at Build #55',
        'MASTER_MASTER_PLAN.md = first document for any new steward',
        'North Star governing principle — expand never contradict',
        'Institutional motto: Understand First. Verify Always. Teach Others.',
        'Synthesizes Builds #1–54 into single execution constitution',
        'Next phase: engineering translation — not Build #56 of planning',
        f"{s['master_plan_readiness_pct']}% readiness — vision documented, execution pending"
    ],
    'open_questions': [
        'Translation layer scope for Build #56?',
        'Neon migration vs content production priority?',
        'Unify three journey models?',
        'Build Bible vs Master Plan hierarchy for editors?',
    ],
    'risks': mp['catalog_gaps'][:4],
    'next_recommended': 56,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/master-plan.html',
    'review_status': 'complete'
})

mc['briefing'] = {
    'what_built': '★ Master Master Plan v1.0 — North Star constitution synthesizing 55 builds',
    'building_now': 'SHIFT: Planning constitution complete → Implementation translation layer',
    'blocked': ['Translation layer', 'Neon/Prisma', 'COMP-* specs', 'GitHub issue backlog'],
    'ready_public': ['Master Plan dashboard', 'Constitution index', 'Institutional motto', 'Five-year vision'],
    'next': 'Build #56 — Implementation translation layer & engineering artifacts'
}

if not any(n.get('id') == 'master_plan' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'master_plan',
        'label': 'Master Master Plan ★',
        'href': '/mission-control/master-plan.html',
        'status': 'complete'
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
