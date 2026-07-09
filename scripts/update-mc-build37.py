import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json') as f:
    mc = json.load(f)

title = 'Citizens United Facts Master Research Library & Digital Archive'

with open(root / 'data/master-research-library.json') as f:
    lib = json.load(f)

s = lib['summary']

mc['version'] = '1.41.0'
mc['build'] = 37
mc['updated'] = '2026-07-09'
mc['master_research_library'] = '/data/master-research-library.json'
mc['research_library_dashboard'] = '/mission-control/research-library.html'

mc['executive'] = {
    'overall_completion': 37,
    'current_build': {'number': 37, 'title': title},
    'active_phase': 'Institutional Knowledge — Master Research Library & Digital Archive',
    'last_completed': 'Evidence, Transparency & Trust Framework',
    'next_build': {'number': 38, 'title': 'Component specifications with props/states'},
    'github_status': 'connected',
    'netlify_status': 'production_healthy',
    'content_readiness': 26,
    'research_readiness': 28,
    'data_viz_readiness': 4,
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
    'library_readiness': s['library_readiness_pct'],
    'public_launch_readiness': 8,
    'public_launch_label': 'Early Foundation'
}

mc['library_inventory'] = {
    'readiness_score': s['library_readiness_pct'],
    'collections_total': s['collections_total'],
    'documents_archived': s['documents_archived'],
    'documents_planned': s['documents_planned'],
    'archive_completion_pct': s['archive_completion_pct'],
    'collections_with_content': s['collections_with_content'],
    'workspace_live': s['workspace_live'],
    'archive_search_live': s['archive_search_live'],
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 37
        bar['note'] = f"Research Library live — {s['documents_archived']}/{s['documents_planned']} documents, 7 collections A–G."

if not any(b.get('id') == 'research_library' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'research_library',
        'label': 'Master Research Library',
        'value': s['library_readiness_pct'],
        'max': 100,
        'note': f"{s['collections_with_content']}/7 collections with content — preserve don't summarize."
    })

mc['builds'].insert(0, {
    'number': 37,
    'title': title,
    'version': '1.41.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Institutional Knowledge Repository v1.0 — digital archive of documentary record',
    'summary': f"7 collections A–G, {s['documents_archived']}/{s['documents_planned']} docs; {s['library_readiness_pct']}% readiness.",
    'files_created': [
        'data/master-research-library.json', 'docs/MASTER_RESEARCH_LIBRARY.md',
        'builds/037-master-research-library.md', 'mission-control/research-library.html',
        'scripts/gen-master-research-library.py', 'scripts/update-mc-build37.py'
    ],
    'files_modified': ['js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml'],
    'pages_created': ['/mission-control/research-library.html'],
    'decisions_made': [
        '7 master collections A–G (SCOTUS through Public Education)',
        'Archive ID + MRID + evidence EV-ID alignment',
        '5 curated reading lists + research workspace schema',
        '14 evidence items mapped to collections — 405 planned',
        'Relationship engine to encyclopedia, KG, curriculum',
        f"{s['library_readiness_pct']}% honest readiness — workspace and search not built"
    ],
    'open_questions': ['FEC dataset ingestion timing?', 'When to migrate to /archive routes?'],
    'risks': ['3.5% archive completion', 'Collections C/E/F empty', 'No research workspace'],
    'next_recommended': 38,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/research-library.html',
    'review_status': 'complete'
})

mc['briefing'] = {
    'what_built': f'Research Library v1.0 — 7 collections, reading lists, library dashboard',
    'building_now': 'Digital archive — evidence registry as interim archive',
    'blocked': ['Canonical archive routes', 'Research workspace', 'Archive search'],
    'ready_public': ['Library MC dashboard', 'Collection taxonomy', 'Reading lists', '/library/ index'],
    'next': 'Build #38 — Component specifications with props/states'
}

if not any(n.get('id') == 'research_library' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'research_library', 'label': 'Master Research Library', 'href': '/mission-control/research-library.html', 'status': 'complete'
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
