import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json') as f:
    mc = json.load(f)

title = 'Master Platform Blueprint & Technical Architecture'

with open(root / 'data/platform-architecture.json') as f:
    arch = json.load(f)

s = arch['summary']

mc['version'] = '1.24.0'
mc['build'] = 20
mc['updated'] = '2026-07-09'
mc['platform_architecture'] = '/data/platform-architecture.json'
mc['platform_dashboard'] = '/mission-control/platform.html'

mc['executive'] = {
    'overall_completion': 20,
    'current_build': {'number': 20, 'title': title},
    'active_phase': 'Technical Architecture — Platform Blueprint',
    'last_completed': 'Citizens United Knowledge Atlas & Learning Path System',
    'next_build': {'number': 21, 'title': 'Repository & folder structure'},
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
    'public_launch_readiness': 8,
    'public_launch_label': 'Early Foundation'
}

mc['platform_blueprint'] = {
    'readiness_score': 20,
    'architecture_readiness_pct': s['architecture_readiness_pct'],
    'v1_success_avg_pct': s['v1_success_avg_pct'],
    'stack_live': s['stack_live'],
    'stack_partial': s['stack_partial'],
    'objectives_avg': s['objectives_avg_readiness'],
    'mc_systems_live': s['mc_systems_live'],
    'philosophy': arch['philosophy'],
    'next_implementation_builds': '21–25'
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 20
        bar['note'] = f"Platform blueprint live — {s['architecture_readiness_pct']}% arch readiness, v1 success {s['v1_success_avg_pct']}%. Implementation wave #21–#25 next."

if not any(b.get('id') == 'platform' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'platform',
        'label': 'Platform Architecture',
        'value': 20,
        'max': 100,
        'note': f"Stack {s['stack_live']} live / {s['stack_partial']} partial — honest v1 criteria at {s['v1_success_avg_pct']}%."
    })

mc['builds'].insert(0, {
    'number': 20,
    'title': title,
    'version': '1.24.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Version 1 System Architecture — stack, data, security, v1 success, implementation roadmap',
    'summary': f"5 objectives, {s['stack_layers']} stack layers, 4 platform modules, v1 success {s['v1_success_avg_pct']}%; Builds #21–#25 implementation artifacts defined.",
    'files_created': [
        'data/platform-architecture.json', 'docs/PLATFORM_ARCHITECTURE.md',
        'builds/020-master-platform-blueprint.md', 'mission-control/platform.html',
        'scripts/gen-platform-architecture.py', 'scripts/update-mc-build20.py'
    ],
    'files_modified': [
        'js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml'
    ],
    'pages_created': ['/mission-control/platform.html'],
    'decisions_made': [
        'Build once. Expand forever.',
        'Static HTML/CSS/JS interim stack documented honestly',
        'Database deferred to Build #22',
        'Implementation wave: #21 repo structure, #22 DB, #23 wireframes, #24 component specs, #25 GitHub roadmap',
        'Brand deferred — ACEI working title retained'
    ],
    'open_questions': ['Frontend framework selection?', 'Supabase vs alternatives for Build #22?'],
    'risks': ['v1 success at 48% — most criteria partial or planned'],
    'next_recommended': 21,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/platform.html',
    'review_status': 'complete'
})

mc['briefing'] = {
    'what_built': 'Platform Blueprint v1.0 — complete technical architecture before production code',
    'building_now': 'Constitutional foundation complete (Builds 1–20) — implementation artifacts next (#21–#25)',
    'blocked': ['No database', 'No frontend framework', 'Public official sharing automation'],
    'ready_public': ['Platform MC dashboard', 'v1 success criteria', 'Implementation roadmap'],
    'next': 'Build #21 — Repository & folder structure'
}

if not any(n.get('id') == 'platform' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'platform', 'label': 'Platform Blueprint', 'href': '/mission-control/platform.html', 'status': 'complete'
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
