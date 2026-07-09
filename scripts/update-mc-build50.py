import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json', encoding='utf-8') as f:
    mc = json.load(f)

title = 'Citizens United Facts Master Build Bible v1.0'

with open(root / 'data/build-bible.json', encoding='utf-8') as f:
    bb = json.load(f)

s = bb['summary']

mc['version'] = '1.54.0'
mc['build'] = 50
mc['updated'] = '2026-07-09'
mc['build_bible'] = '/data/build-bible.json'
mc['build_bible_dashboard'] = '/mission-control/build-bible.html'

mc['executive'] = {
    'overall_completion': 50,
    'current_build': {'number': 50, 'title': title},
    'active_phase': 'Implementation — Design Complete, Engineering Begins',
    'last_completed': 'Master Governance & Institutional Constitution',
    'next_build': {'number': 51, 'title': 'Master implementation roadmap & sprint zero'},
    'github_status': 'connected',
    'netlify_status': 'production_healthy',
    'content_readiness': 28,
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
    'platform_architecture_readiness': 24,
    'repository_structure_readiness': 28,
    'database_schema_readiness': 36,
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
    'institutional_maturity_pct': 36,
    'current_institutional_version': 'V1',
    'systems_integration_readiness': 28,
    'production_matrix_readiness': 39,
    'visitor_journey_readiness': 40,
    'technical_architecture_readiness': 38,
    'governance_readiness': 44,
    'build_bible_readiness': s['build_bible_readiness_pct'],
    'planning_phase_complete': True,
    'implementation_phase': 'sprint_zero_pending',
    'public_launch_readiness': 8,
    'public_launch_label': 'Early Foundation'
}

mc['build_bible_inventory'] = {
    'readiness_score': s['build_bible_readiness_pct'],
    'planning_builds': s['planning_builds_complete'],
    'foundation_systems': s['foundation_systems'],
    'pillars_total': s['pillars_total'],
    'avg_engine_readiness_pct': s['avg_engine_readiness_pct'],
    'planning_phase_complete': s['planning_phase_complete'],
    'implementation_started': s['implementation_phase_started'],
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 50
        bar['note'] = f"Build Bible — 50 planning builds complete. Implementation phase begins."
    if bar['id'] == 'institutional_maturity':
        bar['value'] = 36
        bar['note'] = 'Planning foundation complete — V1 implementation starting.'

if not any(b.get('id') == 'build_bible' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'build_bible',
        'label': 'Master Build Bible',
        'value': s['build_bible_readiness_pct'],
        'max': 100,
        'note': f"50 builds indexed — {s['avg_engine_readiness_pct']}% avg engine readiness."
    })
else:
    for bar in mc['progress_bars']:
        if bar['id'] == 'build_bible':
            bar['value'] = s['build_bible_readiness_pct']
            bar['note'] = 'Planning complete — engineering next.'

mc['builds'].insert(0, {
    'number': 50,
    'title': title,
    'version': '1.54.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Master index — first complete architecture, shift design → implementation',
    'summary': f"50 builds, {s['foundation_systems']} systems, {s['pillars_total']} pillars, {s['avg_engine_readiness_pct']}% avg engine readiness.",
    'files_created': [
        'data/build-bible.json', 'docs/MASTER_BUILD_BIBLE.md',
        'builds/050-master-build-bible.md', 'mission-control/build-bible.html',
        'scripts/gen-build-bible.py', 'scripts/update-mc-build50.py'
    ],
    'files_modified': ['js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml'],
    'pages_created': ['/mission-control/build-bible.html'],
    'decisions_made': [
        'Planning phase complete — 50 numbered builds establish institutional blueprint',
        '28 foundation systems indexed — Phase I complete',
        '12 pillars + 4 engines + 6 workstreams — permanent institutional taxonomy',
        '5 implementation phases (A–E) — engineering roadmap',
        'Governing question locked for all future builds',
        f"{s['build_bible_readiness_pct']}% bible readiness — index live, implementation pending"
    ],
    'open_questions': ['Sprint Zero scope?', 'Next.js migration timing?', 'First content vs first code priority?'],
    'risks': ['50 builds ≠ working institution', 'Blueprint fatigue', 'Implementation without sprint discipline'],
    'next_recommended': 51,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/build-bible.html',
    'review_status': 'complete'
})

mc['briefing'] = {
    'what_built': 'Build Bible v1.0 — master index, pillars, engines, workstreams, implementation phases',
    'building_now': 'SHIFT: Design complete → Implementation (Sprint Zero next)',
    'blocked': ['Component specs', 'Neon provisioning', 'Sprint backlog'],
    'ready_public': ['Build Bible MC dashboard', 'Complete blueprint index', 'Governing question'],
    'next': 'Build #51 — Master implementation roadmap & sprint zero'
}

if not any(n.get('id') == 'build_bible' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'build_bible', 'label': 'Master Build Bible', 'href': '/mission-control/build-bible.html', 'status': 'complete'
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
