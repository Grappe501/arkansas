import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json') as f:
    mc = json.load(f)

title = 'Database Schema & Entity Relationship Blueprint'

with open(root / 'data/database-schema.json') as f:
    schema = json.load(f)

s = schema['summary']

mc['version'] = '1.26.0'
mc['build'] = 22
mc['updated'] = '2026-07-09'
mc['database_schema'] = '/data/database-schema.json'
mc['database_dashboard'] = '/mission-control/database.html'

mc['executive'] = {
    'overall_completion': 22,
    'current_build': {'number': 22, 'title': title},
    'active_phase': 'Implementation Artifacts — Database Schema',
    'last_completed': 'GitHub Repository & Folder Structure Blueprint',
    'next_build': {'number': 23, 'title': 'Wireframes for every major screen'},
    'github_status': 'connected',
    'netlify_status': 'production_healthy',
    'content_readiness': 16,
    'research_readiness': 20,
    'data_viz_readiness': 2,
    'signup_funnel_readiness': 14,
    'civic_action_readiness': 22,
    'coalition_readiness': 12,
    'data_model_readiness': 35,
    'route_inventory_readiness': 18,
    'component_registry_readiness': 22,
    'facts_framework_readiness': 12,
    'knowledge_atlas_readiness': 18,
    'platform_architecture_readiness': 20,
    'repository_structure_readiness': 28,
    'database_schema_readiness': 35,
    'public_launch_readiness': 8,
    'public_launch_label': 'Early Foundation'
}

mc['database_inventory'] = {
    'readiness_score': 35,
    'entities': s['entities'],
    'join_tables': s['join_tables'],
    'fields_total': s['fields_total'],
    'schema_readiness_pct': s['schema_readiness_pct'],
    'database_deployed': s['database_deployed'],
    'v1_storage': s['v1_storage'],
    'migration_target': s['migration_target']
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 22
        bar['note'] = f"Database schema live — {s['entities']} entities, {s['join_tables']} join tables. No DB deployed yet. Wireframes next."
    if bar['id'] == 'data_model' or bar.get('label') == 'Data Model':
        bar['value'] = 35
        bar['note'] = f"Schema blueprint — {s['schema_readiness_pct']}% readiness, static JSON v1."

if not any(b.get('id') == 'database' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'database',
        'label': 'Database Schema',
        'value': 35,
        'max': 100,
        'note': f"{s['entities']} entities defined — Supabase/Postgres migration path documented."
    })

mc['builds'].insert(0, {
    'number': 22,
    'title': title,
    'version': '1.26.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Data Architecture v1.0 — 15 entities, 10 join tables, v1 storage strategy',
    'summary': f"{s['entities']} entities, {s['fields_total']} fields, {s['join_tables']} join tables; {s['schema_readiness_pct']}% schema readiness; no DB deployed.",
    'files_created': [
        'data/database-schema.json', 'docs/DATABASE_SCHEMA.md',
        'builds/022-database-schema.md', 'mission-control/database.html',
        'scripts/gen-database-schema.py', 'scripts/update-mc-build22.py'
    ],
    'files_modified': ['js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml'],
    'pages_created': ['/mission-control/database.html'],
    'decisions_made': [
        '15 primary entities extending canonical model (10 → 15)',
        '10 join tables for M:N relationships',
        '8 signup types defined',
        'v1: static JSON + Netlify Forms; v2: Supabase/Postgres',
        'Privacy principle: collect only what is needed'
    ],
    'open_questions': ['Supabase vs Neon for v2?', 'When to migrate forms to person/signup tables?'],
    'risks': ['No database deployed — schema blueprint only'],
    'next_recommended': 23,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/database.html',
    'review_status': 'complete'
})

mc['briefing'] = {
    'what_built': f'Database Schema v1.0 — {s["entities"]} entities, ERD, join tables, MC metrics',
    'building_now': 'Implementation artifacts — wireframes next (Build #23)',
    'blocked': ['No Postgres/Supabase', 'Join tables not in DB', 'Forms not synced to entities'],
    'ready_public': ['Database MC dashboard', 'ERD overview', 'Storage migration path'],
    'next': 'Build #23 — Wireframes for every major screen'
}

if not any(n.get('id') == 'database' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'database', 'label': 'Database Schema', 'href': '/mission-control/database.html', 'status': 'complete'
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
