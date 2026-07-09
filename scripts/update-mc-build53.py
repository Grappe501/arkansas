import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json', encoding='utf-8') as f:
    mc = json.load(f)

title = 'Citizens United Facts Master Launch Strategy & Arkansas Rollout Blueprint v1.0'

with open(root / 'data/launch-strategy.json', encoding='utf-8') as f:
    ls = json.load(f)

s = ls['summary']

mc['version'] = '1.57.0'
mc['build'] = 53
mc['updated'] = '2026-07-09'
mc['launch_strategy'] = '/data/launch-strategy.json'
mc['launch_strategy_dashboard'] = '/mission-control/launch-strategy.html'

mc['executive'] = {
    'overall_completion': 53,
    'current_build': {'number': 53, 'title': title},
    'active_phase': 'Rollout — Phase 0 Private Development',
    'last_completed': 'Master User Experience Architecture',
    'next_build': {'number': 54, 'title': 'Master implementation roadmap & sprint zero'},
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
    'institutional_maturity_pct': 39,
    'current_institutional_version': 'V1',
    'systems_integration_readiness': 28,
    'production_matrix_readiness': 39,
    'visitor_journey_readiness': 40,
    'technical_architecture_readiness': 38,
    'governance_readiness': 44,
    'build_bible_readiness': 49,
    'data_architecture_readiness': 41,
    'ux_architecture_readiness': 39,
    'launch_strategy_readiness': s['launch_strategy_readiness_pct'],
    'rollout_phase': 0,
    'rollout_phase_title': 'Private Development',
    'planning_phase_complete': True,
    'implementation_phase': 'phase_0_private_development',
    'public_launch_readiness': s['public_launch_readiness_pct'],
    'public_launch_label': 'Early Foundation',
    'public_launch_recommended': False,
}

mc['launch_strategy_inventory'] = {
    'readiness_score': s['launch_strategy_readiness_pct'],
    'current_phase': s['current_phase'],
    'checklist_score_pct': s['checklist_score_pct'],
    'public_launch_readiness_pct': s['public_launch_readiness_pct'],
    'public_launch_recommended': s['public_launch_recommended'],
    'checklist_live': s['checklist_live'],
    'checklist_partial': s['checklist_partial'],
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 53
        bar['note'] = 'Build #53 — Master Launch Strategy & Arkansas Rollout Blueprint complete.'
    if bar['id'] == 'institutional_maturity':
        bar['value'] = 39
        bar['note'] = 'Phase 0 Private Development — public launch not recommended.'

if not any(b.get('id') == 'launch_strategy' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'launch_strategy',
        'label': 'Launch Strategy',
        'value': s['launch_strategy_readiness_pct'],
        'max': 100,
        'note': f"Phase 0 active · {s['public_launch_readiness_pct']}% public launch readiness."
    })
else:
    for bar in mc['progress_bars']:
        if bar['id'] == 'launch_strategy':
            bar['value'] = s['launch_strategy_readiness_pct']
            bar['note'] = 'Launch Command Center live — rollout gated on checklist.'

mc['builds'].insert(0, {
    'number': 53,
    'title': title,
    'version': '1.57.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Arkansas rollout blueprint — six phases, readiness gate, Launch Command Center',
    'summary': (
        f"Phase 0 active, {s['checklist_live']}+{s['checklist_partial']}/12 checklist partial, "
        f"{s['public_launch_readiness_pct']}% public launch — not recommended."
    ),
    'files_created': [
        'data/launch-strategy.json', 'docs/MASTER_LAUNCH_STRATEGY.md',
        'builds/053-master-launch-strategy.md', 'mission-control/launch-strategy.html',
        'scripts/gen-launch-strategy.py', 'scripts/update-mc-build53.py'
    ],
    'files_modified': ['js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml'],
    'pages_created': ['/mission-control/launch-strategy.html'],
    'decisions_made': [
        'Six launch phases (0–5) — private development through long-term stewardship',
        'Public launch gated on 12-item readiness checklist — not deadlines',
        'Educational metrics over page views — mission-aligned success definition',
        'County-by-county Arkansas growth strategy',
        'Annual relaunch as living institution model',
        f"Phase 0 active — {s['public_launch_readiness_pct']}% public launch readiness, not recommended"
    ],
    'open_questions': [
        'Netlify public URL vs Phase 0 private development — formal staging?',
        'Review Feedback dashboard scope for Phase 1?',
        'Pilot cohort selection criteria?',
        'First annual relaunch date?',
    ],
    'risks': [
        'Site already public — phase model vs reality mismatch',
        '8% public launch readiness — premature publicity risk',
        '0 signups — Phase 2 pilot has no cohort',
        'Privacy + accessibility gaps block checklist',
    ],
    'next_recommended': 54,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/launch-strategy.html',
    'review_status': 'complete'
})

mc['briefing'] = {
    'what_built': 'Launch Strategy v1.0 — 6 phases, readiness checklist, Launch Command Center, Arkansas growth plan',
    'building_now': 'Phase 0 Private Development — public launch not recommended',
    'blocked': ['Privacy policy', 'Accessibility audit', 'Review Feedback dashboard', 'Launch metrics instrumentation'],
    'ready_public': ['Launch Command Center dashboard', 'Six-phase rollout model', 'Readiness checklist'],
    'next': 'Build #54 — Master implementation roadmap & sprint zero'
}

if not any(n.get('id') == 'launch_strategy' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'launch_strategy',
        'label': 'Launch Strategy',
        'href': '/mission-control/launch-strategy.html',
        'status': 'complete'
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
