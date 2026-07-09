import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json') as f:
    mc = json.load(f)

title = 'Citizens United Facts Research Encyclopedia & Knowledge Library'

with open(root / 'data/encyclopedia-knowledge-library.json') as f:
    enc = json.load(f)

s = enc['summary']
cs = enc['completion_score']

mc['version'] = '1.37.0'
mc['build'] = 33
mc['updated'] = '2026-07-09'
mc['encyclopedia_knowledge_library'] = '/data/encyclopedia-knowledge-library.json'
mc['encyclopedia_dashboard'] = '/mission-control/encyclopedia.html'

mc['executive'] = {
    'overall_completion': 33,
    'current_build': {'number': 33, 'title': title},
    'active_phase': 'Knowledge Institution — Encyclopedia Architecture',
    'last_completed': 'Educational Campaign Operating System',
    'next_build': {'number': 34, 'title': 'Component specifications with props/states'},
    'github_status': 'connected',
    'netlify_status': 'production_healthy',
    'content_readiness': 22,
    'research_readiness': 24,
    'data_viz_readiness': 2,
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
    'education_academy_readiness': 24,
    'observatory_readiness': 18,
    'outreach_readiness': 22,
    'county_os_readiness': 28,
    'campaign_os_readiness': 34,
    'encyclopedia_readiness': s['encyclopedia_readiness_pct'],
    'public_launch_readiness': 8,
    'public_launch_label': 'Early Foundation'
}

mc['encyclopedia_inventory'] = {
    'readiness_score': s['encyclopedia_readiness_pct'],
    'categories_total': s['categories_total'],
    'entries_planned': s['entries_planned'],
    'entries_published': s['entries_published'],
    'entries_fully_sourced': s['entries_fully_sourced'],
    'completion_score': cs,
    'canonical_routes_live': s['canonical_routes_live'],
    'encyclopedia_search_live': s['encyclopedia_search_live'],
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 33
        bar['note'] = f"Encyclopedia live — {s['entries_published']}/{s['entries_planned']} entries, {cs['overall_completion_pct']}% catalog completion."

if not any(b.get('id') == 'encyclopedia' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'encyclopedia',
        'label': 'Encyclopedia & Knowledge Library',
        'value': s['encyclopedia_readiness_pct'],
        'max': 100,
        'note': f"{s['entries_fully_sourced']} fully sourced — 9 categories, KG-aligned, search planned."
    })

mc['builds'].insert(0, {
    'number': 33,
    'title': title,
    'version': '1.37.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Encyclopedia Architecture v1.0 — living reference connected through knowledge graph',
    'summary': f"{s['categories_total']} categories, {s['entries_published']}/{s['entries_planned']} entries; {s['encyclopedia_readiness_pct']}% readiness.",
    'files_created': [
        'data/encyclopedia-knowledge-library.json', 'docs/ENCYCLOPEDIA_ARCHITECTURE.md',
        'builds/033-encyclopedia-knowledge-library.md', 'mission-control/encyclopedia.html',
        'scripts/gen-encyclopedia-knowledge-library.py', 'scripts/update-mc-build33.py'
    ],
    'files_modified': ['js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml'],
    'pages_created': ['/mission-control/encyclopedia.html'],
    'decisions_made': [
        '9 encyclopedia categories (100–900) aligned to KG node types',
        '9-section entry structure for every encyclopedia page',
        'Completion score tracks planned, published, sourced, cross-links',
        'KG registry (38 nodes) as interim published entry source',
        'Canonical /encyclopedia/[category]/[slug] defined — not built',
        '19% honest readiness — architecture live, 9.5% catalog published'
    ],
    'open_questions': ['When to migrate KG nodes to canonical encyclopedia routes?', 'Glossary scale for Category 700?'],
    'risks': ['Category 700 empty', 'Only 7 entries fully sourced', 'Search not implemented'],
    'next_recommended': 34,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/encyclopedia.html',
    'review_status': 'complete'
})

mc['briefing'] = {
    'what_built': f'Encyclopedia v1.0 — {s["categories_total"]} categories, completion score, KG relationship graph',
    'building_now': 'Knowledge library — 38 KG nodes mapped, 400 entries planned',
    'blocked': ['Canonical encyclopedia routes not built', 'Search not implemented', 'Category 700 (Terms) empty'],
    'ready_public': ['Encyclopedia MC dashboard', '9-category architecture', 'Citation standards', 'KG alignment'],
    'next': 'Build #34 — Component specifications with props/states'
}

if not any(n.get('id') == 'encyclopedia' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'encyclopedia', 'label': 'Encyclopedia & Knowledge Library', 'href': '/mission-control/encyclopedia.html', 'status': 'complete'
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
