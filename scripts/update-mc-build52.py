import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json', encoding='utf-8') as f:
    mc = json.load(f)

title = 'Citizens United Facts Master User Experience Architecture v1.0'

with open(root / 'data/ux-architecture.json', encoding='utf-8') as f:
    ux = json.load(f)

s = ux['summary']

mc['version'] = '1.56.0'
mc['build'] = 52
mc['updated'] = '2026-07-09'
mc['ux_architecture'] = '/data/ux-architecture.json'
mc['ux_architecture_dashboard'] = '/mission-control/ux-architecture.html'

mc['executive'] = {
    'overall_completion': 52,
    'current_build': {'number': 52, 'title': title},
    'active_phase': 'Implementation — Experience Blueprint Established',
    'last_completed': 'Master Data Architecture & Canonical Data Dictionary',
    'next_build': {'number': 53, 'title': 'Master implementation roadmap & sprint zero'},
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
    'institutional_maturity_pct': 38,
    'current_institutional_version': 'V1',
    'systems_integration_readiness': 28,
    'production_matrix_readiness': 39,
    'visitor_journey_readiness': 40,
    'technical_architecture_readiness': 38,
    'governance_readiness': 44,
    'build_bible_readiness': 49,
    'data_architecture_readiness': 41,
    'ux_architecture_readiness': s['ux_architecture_readiness_pct'],
    'planning_phase_complete': True,
    'implementation_phase': 'experience_blueprint_established',
    'public_launch_readiness': 8,
    'public_launch_label': 'Early Foundation'
}

mc['ux_architecture_inventory'] = {
    'readiness_score': s['ux_architecture_readiness_pct'],
    'emotional_stages': s['emotional_stages'],
    'action_hub_live_items': s['action_hub_live_items'],
    'learning_compass_questions': s['learning_compass_questions'],
    'search_live': s['search_live'],
    'delight_moments_live': s['delight_moments_live'],
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 52
        bar['note'] = 'Build #52 — Master User Experience Architecture complete.'
    if bar['id'] == 'institutional_maturity':
        bar['value'] = 38
        bar['note'] = 'Experience blueprint — museum-quality civic learning target.'

if not any(b.get('id') == 'ux_architecture' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'ux_architecture',
        'label': 'Master UX Architecture',
        'value': s['ux_architecture_readiness_pct'],
        'max': 100,
        'note': f"{s['action_hub_live_items']} action hub items live · 0 delight moments."
    })
else:
    for bar in mc['progress_bars']:
        if bar['id'] == 'ux_architecture':
            bar['value'] = s['ux_architecture_readiness_pct']
            bar['note'] = 'Experience constitution — compasses and search pending.'

mc['builds'].insert(0, {
    'number': 52,
    'title': title,
    'version': '1.56.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Institutional Experience Blueprint — how every visitor should feel',
    'summary': (
        f"7 emotional stages, Learning + Civic Compass, Action Hub. "
        f"{s['ux_architecture_readiness_pct']}% UX readiness — search and compasses pending."
    ),
    'files_created': [
        'data/ux-architecture.json', 'docs/MASTER_UX_ARCHITECTURE.md',
        'builds/052-master-ux-architecture.md', 'mission-control/ux-architecture.html',
        'scripts/gen-ux-architecture.py', 'scripts/update-mc-build52.py'
    ],
    'files_modified': ['js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml'],
    'pages_created': ['/mission-control/ux-architecture.html'],
    'decisions_made': [
        'Museum metaphor — invited not pressured civic learning experience',
        '7-stage emotional journey distinct from Build #47 behavioral funnel',
        'Question-based navigation — Learn, Research, Explore, Teach, etc.',
        'Learning Compass + Civic Compass — education and participation separated',
        'Floating Action Hub confirmed as primary participation surface',
        f"{s['ux_architecture_readiness_pct']}% UX readiness — Action Hub live, compasses partial"
    ],
    'open_questions': [
        'Unify emotional (7) and behavioral (8) journey models?',
        'Learning Compass COMP-* implementation priority?',
        'Search MVP vs Sprint Zero first?',
        'Mobile-first lesson redesign scope?'
    ],
    'risks': [
        'Three journey models (Build #8, #47, #52) may confuse editors',
        'Civic Compass not separate UI — participation buried in hub',
        '0 community vitality — experience blueprint exceeds live signals',
        'Delight moments deferred — risk of feeling institutional not memorable'
    ],
    'next_recommended': 53,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/ux-architecture.html',
    'review_status': 'complete'
})

mc['briefing'] = {
    'what_built': 'UX Architecture v1.0 — emotional journey, compasses, progressive disclosure, institutional personality',
    'building_now': 'Implementation — experience blueprint established; Sprint Zero next',
    'blocked': ['Learning Compass UI', 'Site search', 'Delight moments', 'Community vitality widgets'],
    'ready_public': ['UX Architecture MC dashboard', 'Action Hub live', 'Experience philosophy documented'],
    'next': 'Build #53 — Master implementation roadmap & sprint zero'
}

if not any(n.get('id') == 'ux_architecture' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'ux_architecture',
        'label': 'Master UX Architecture',
        'href': '/mission-control/ux-architecture.html',
        'status': 'complete'
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
