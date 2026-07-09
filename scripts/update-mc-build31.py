import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json') as f:
    mc = json.load(f)

title = 'Citizens United Facts Arkansas County Operating System'

with open(root / 'data/county-operating-system.json') as f:
    cos = json.load(f)

s = cos['summary']

mc['version'] = '1.35.0'
mc['build'] = 31
mc['updated'] = '2026-07-09'
mc['county_operating_system'] = '/data/county-operating-system.json'
mc['county_os_dashboard'] = '/mission-control/county-os.html'

mc['executive'] = {
    'overall_completion': 31,
    'current_build': {'number': 31, 'title': title},
    'active_phase': 'County Education Network — Arkansas County OS',
    'last_completed': 'Public Engagement & Outreach Engine',
    'next_build': {'number': 32, 'title': 'Component specifications with props/states'},
    'github_status': 'connected',
    'netlify_status': 'production_healthy',
    'content_readiness': 20,
    'research_readiness': 22,
    'data_viz_readiness': 2,
    'signup_funnel_readiness': 22,
    'civic_action_readiness': 32,
    'coalition_readiness': 18,
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
    'observatory_readiness': 18,
    'outreach_readiness': 22,
    'county_os_readiness': 28,
    'public_launch_readiness': 8,
    'public_launch_label': 'Early Foundation'
}

mc['county_os_inventory'] = {
    'readiness_score': s['county_os_readiness_pct'],
    'counties_total': s['counties_total'],
    'counties_scaffolded': s['counties_scaffolded'],
    'counties_with_partner': s['counties_with_partner'],
    'education_score_categories': s['education_score_categories'],
    'regions': s['regions'],
    'canonical_route_live': s['canonical_route_live'],
    'education_score_live': s['education_score_live'],
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 31
        bar['note'] = f"County OS live — {s['counties_scaffolded']} county scaffolds, education score architecture. One county at a time."

if not any(b.get('id') == 'county_os' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'county_os',
        'label': 'County Operating System',
        'value': 28,
        'max': 100,
        'note': f"{s['counties_with_partner']} counties with partners — 75 scaffolds at 0% completeness."
    })

mc['builds'].insert(0, {
    'number': 31,
    'title': title,
    'version': '1.35.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'County Education Network Blueprint v1.0 — 75 locally relevant educational presences',
    'summary': f"{s['counties_scaffolded']} counties, {s['education_score_categories']} score categories, {s['regions']} regions; {s['county_os_readiness_pct']}% readiness.",
    'files_created': [
        'data/county-operating-system.json', 'docs/COUNTY_OPERATING_SYSTEM.md',
        'builds/031-county-operating-system.md', 'mission-control/county-os.html',
        'scripts/gen-county-operating-system.py', 'scripts/update-mc-build31.py'
    ],
    'files_modified': ['js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml'],
    'pages_created': ['/mission-control/county-os.html'],
    'decisions_made': [
        '12 county profile sections per /arkansas/[county-name]',
        '5-category County Education Score — no competitive rankings',
        '6 volunteer leadership roles per county',
        '7 regional groupings for broader trends',
        'Aligned to county-coalition-index (75 counties scaffolded)',
        '28% honest readiness — scaffolds exist, all metrics at zero'
    ],
    'open_questions': ['When to migrate to canonical /arkansas/[county] routes?', 'District data source?'],
    'risks': ['0 counties with partners', 'Public officials not mapped per county'],
    'next_recommended': 32,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/county-os.html',
    'review_status': 'complete'
})

mc['briefing'] = {
    'what_built': f'County OS v1.0 — {s["counties_scaffolded"]} county scaffolds, education score, regional architecture',
    'building_now': 'County network — component specs to map profile sections next',
    'blocked': ['0 counties with partners', 'Canonical /arkansas routes not built', 'Education score not computed'],
    'ready_public': ['County OS MC dashboard', '75 county index', 'Profile section schema', 'Regional groupings'],
    'next': 'Build #32 — Component specifications with props/states'
}

if not any(n.get('id') == 'county_os' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'county_os', 'label': 'County Operating System', 'href': '/mission-control/county-os.html', 'status': 'complete'
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
