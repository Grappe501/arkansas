import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json', encoding='utf-8') as f:
    mc = json.load(f)

title = 'Citizens United Facts Statewide Growth & Leadership Blueprint v1.0'

with open(root / 'data/statewide-growth.json', encoding='utf-8') as f:
    sg = json.load(f)

s = sg['summary']

mc['version'] = '1.60.0'
mc['build'] = 56
mc['updated'] = '2026-07-09'
mc['statewide_growth'] = '/data/statewide-growth.json'
mc['statewide_growth_dashboard'] = '/mission-control/statewide-growth.html'

mc['executive'] = {
    'overall_completion': 56,
    'current_build': {'number': 56, 'title': title},
    'active_phase': 'Statewide Growth Objectives → Implementation Translation',
    'last_completed': 'Master Master Plan (North Star)',
    'next_build': {'number': 57, 'title': 'Implementation translation layer & engineering artifacts'},
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
    'institutional_maturity_pct': 43,
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
    'master_plan_readiness': 56,
    'statewide_growth_readiness': s['statewide_growth_readiness_pct'],
    'rollout_phase': 0,
    'rollout_phase_title': 'Private Development',
    'planning_phase_complete': True,
    'planning_constitution_complete': True,
    'implementation_phase': 'translation_layer_next',
    'public_launch_readiness': s['public_launch_readiness_pct'],
    'public_launch_label': 'Early Foundation',
    'public_launch_recommended': False,
}

mc['statewide_growth_inventory'] = {
    'readiness_score': s['statewide_growth_readiness_pct'],
    'counties_total': s['counties_total'],
    'counties_with_leaders': s['counties_with_leaders'],
    'cities_indexed': s['cities_total'],
    'participants_target': s['participants_target'],
    'participants_current': s['participants_current'],
    'benchmarks_met': s['benchmarks_met'],
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 56
        bar['note'] = 'Build #56 — Statewide Growth & Leadership Blueprint.'
    if bar['id'] == 'institutional_maturity':
        bar['value'] = 43
        bar['note'] = 'Measurable statewide objectives live — 0/75 counties, 0/250 cities.'

if not any(b.get('id') == 'statewide_growth' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'statewide_growth',
        'label': 'Statewide Growth',
        'value': s['statewide_growth_readiness_pct'],
        'max': 100,
        'note': f"0 leaders · 0/{s['participants_target']:,} participants · maps planned."
    })
else:
    for bar in mc['progress_bars']:
        if bar['id'] == 'statewide_growth':
            bar['value'] = s['statewide_growth_readiness_pct']
            bar['note'] = f"75 counties + 250 cities indexed — {s['education_leaders']} leaders."

mc['builds'].insert(0, {
    'number': 56,
    'title': title,
    'version': '1.60.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Measurable statewide growth objectives — Arkansas Civic Education Network',
    'summary': (
        f"75 counties + 250 cities indexed; 3 statewide objectives; "
        f"{s['statewide_growth_readiness_pct']}% growth blueprint readiness. "
        f"0 leaders · 0 participants."
    ),
    'files_created': [
        'data/statewide-growth.json', 'data/arkansas-cities.json',
        'docs/MASTER_STATEWIDE_GROWTH.md', 'builds/056-statewide-growth.md',
        'mission-control/statewide-growth.html',
        'scripts/gen-statewide-growth.py', 'scripts/update-mc-build56.py',
        'scripts/arkansas-top250-cities.json',
    ],
    'files_modified': ['js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml'],
    'pages_created': ['/mission-control/statewide-growth.html'],
    'decisions_made': [
        'Three statewide objectives: 75 counties, 250 cities, 200,000 participants',
        'Eight-stage leadership ladder from Visitor to Regional Mentor',
        'Geographic dashboards planned — county, city, statewide maps',
        'Privacy-first neighborhood network — general area, not precise tracking',
        '250 largest communities indexed from 2026 population estimates',
        'Recruitment channels must lead back to learning resources',
        f"{s['statewide_growth_readiness_pct']}% readiness — objectives documented, network empty",
    ],
    'open_questions': [
        'County-to-city linkage in canonical schema?',
        'Interactive maps: Leaflet vs static SVG Arkansas?',
        'Participant levels vs leadership ladder unification?',
        'Integrate County OS growth plans with statewide benchmarks?',
    ],
    'risks': sg['catalog_gaps'][:4],
    'next_recommended': 57,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/statewide-growth.html',
    'review_status': 'complete'
})

mc['briefing'] = {
    'what_built': 'Statewide Growth Blueprint v1.0 — 75 counties, 250 cities, 200K participant objective',
    'building_now': 'Growth objectives defined — implementation translation next',
    'blocked': ['Interactive maps', 'Participant schema', 'Signup funnel', 'Leader training pipeline'],
    'ready_public': ['Statewide objectives dashboard', '250-city index', 'Leadership ladder', 'Community benchmarks'],
    'next': 'Build #57 — Implementation translation layer & engineering artifacts'
}

if not any(n.get('id') == 'statewide_growth' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'statewide_growth',
        'label': 'Statewide Growth',
        'href': '/mission-control/statewide-growth.html',
        'status': 'complete'
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
