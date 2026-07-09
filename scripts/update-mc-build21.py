import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json') as f:
    mc = json.load(f)

title = 'GitHub Repository & Folder Structure Blueprint'

with open(root / 'data/repository-blueprint.json') as f:
    bp = json.load(f)

s = bp['summary']

mc['version'] = '1.25.0'
mc['build'] = 21
mc['updated'] = '2026-07-09'
mc['repository_blueprint'] = '/data/repository-blueprint.json'
mc['repository_dashboard'] = '/mission-control/repository.html'

mc['executive'] = {
    'overall_completion': 21,
    'current_build': {'number': 21, 'title': title},
    'active_phase': 'Implementation Artifacts — Repository Structure',
    'last_completed': 'Master Platform Blueprint & Technical Architecture',
    'next_build': {'number': 22, 'title': 'Database schema and entity-relationship model'},
    'github_status': 'connected',
    'netlify_status': 'production_healthy',
    'content_readiness': 16,
    'research_readiness': 20,
    'data_viz_readiness': 2,
    'signup_funnel_readiness': 14,
    'civic_action_readiness': 22,
    'coalition_readiness': 12,
    'data_model_readiness': 8,
    'route_inventory_readiness': 18,
    'component_registry_readiness': 22,
    'facts_framework_readiness': 12,
    'knowledge_atlas_readiness': 18,
    'platform_architecture_readiness': 20,
    'repository_structure_readiness': 28,
    'public_launch_readiness': 8,
    'public_launch_label': 'Early Foundation'
}

mc['repository_inventory'] = {
    'readiness_score': 28,
    'structure_readiness_pct': s['structure_readiness_pct'],
    'migration_executed': s['migration_executed'],
    'current_pattern': bp['current_layout']['pattern'],
    'recommended_repo_name': bp['repository_names']['recommended'],
    'workstreams': s['workstreams'],
    'target_src_folders': s['target_src_folders']
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 21
        bar['note'] = f"Repository blueprint live — {s['structure_readiness_pct']}% structure readiness. Migration not executed. DB schema next."

if not any(b.get('id') == 'repository' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'repository',
        'label': 'Repository Structure',
        'value': 28,
        'max': 100,
        'note': 'Target src/ layout defined — flat v0 layout still in use.'
    })

mc['builds'].insert(0, {
    'number': 21,
    'title': title,
    'version': '1.25.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Repository Architecture v1.0 — branches, folder structure, scripts, GitHub labels/milestones',
    'summary': f"4 workstreams, target src/ layout, migration map, {s['structure_readiness_pct']}% readiness — blueprint only, no physical migration.",
    'files_created': [
        'data/repository-blueprint.json', 'docs/REPOSITORY_ARCHITECTURE.md',
        'builds/021-repository-folder-structure.md', 'mission-control/repository.html',
        '.env.example', 'scripts/gen-repository-blueprint.py', 'scripts/update-mc-build21.py'
    ],
    'files_modified': ['js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml', 'CONTRIBUTING.md'],
    'pages_created': ['/mission-control/repository.html'],
    'decisions_made': [
        'Recommended repo name: citizens-united-facts',
        'Target: src/app, src/components, src/data, organized docs/',
        'Current v0 flat layout documented with honest migration map',
        'Physical migration deferred — blueprint before restructure',
        '.env.example added with placeholders only'
    ],
    'open_questions': ['Rename GitHub remote to citizens-united-facts?', 'Next.js vs other framework?'],
    'risks': ['28% structure readiness — migration not executed'],
    'next_recommended': 22,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/repository.html',
    'review_status': 'complete'
})

mc['briefing'] = {
    'what_built': 'Repository Blueprint v1.0 — target folder structure and GitHub workflow',
    'building_now': 'Implementation artifacts wave — database schema next (Build #22)',
    'blocked': ['No src/ migration', 'No validation .mjs scripts', 'develop branch not standard'],
    'ready_public': ['Repository MC dashboard', 'Migration map', '.env.example'],
    'next': 'Build #22 — Database schema and ERD'
}

if not any(n.get('id') == 'repository' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'repository', 'label': 'Repository Blueprint', 'href': '/mission-control/repository.html', 'status': 'complete'
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
