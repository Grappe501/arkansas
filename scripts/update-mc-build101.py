import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json', encoding='utf-8') as f:
    mc = json.load(f)

title = 'Citizens United Facts Cursor Implementation Package v1.0'

with open(root / 'data/cursor-implementation-package.json', encoding='utf-8') as f:
    cip = json.load(f)

s = cip['summary']
prior_maturity = mc.get('executive', {}).get('institutional_maturity_pct', 32)
prior_ex = mc.get('executive', {})

mc['version'] = '2.05.1'
mc['build'] = 101
mc['updated'] = '2026-07-09'
mc['cursor_implementation_package'] = '/data/cursor-implementation-package.json'
mc['cursor_implementation_package_dashboard'] = '/mission-control/cursor-implementation-package.html'

mc['executive'] = {
    **{k: v for k, v in prior_ex.items() if k not in (
        'overall_completion', 'current_build', 'active_phase', 'last_completed', 'next_build',
        'implementation_package_readiness', 'cursor_implementation_package_readiness',
        'implementation_phase_started', 'sprint_zero_started',
    )},
    'overall_completion': 101,
    'current_build': {'number': 101, 'title': title},
    'active_phase': 'Implementation Package → Sprint Zero',
    'last_completed': 'Founding Charter',
    'next_build': {'number': 102, 'title': 'Executive war room & countdown dashboard components'},
    'implementation_package_readiness': s['implementation_package_readiness_pct'],
    'cursor_implementation_package_readiness': s['implementation_package_readiness_pct'],
    'implementation_phase_started': False,
    'sprint_zero_started': s['sprint_zero_started'],
    'implementation_steps_total': s['steps_total'],
    'implementation_steps_implemented': s['steps_implemented'],
    'implementation_steps_documented': s.get('steps_documented', 0),
    'content_readiness': max(s['implementation_package_readiness_pct'], prior_ex.get('content_readiness', 28)),
    'repository_structure_readiness': max(32, prior_ex.get('repository_structure_readiness', 28)),
    'database_schema_readiness': max(44, prior_ex.get('database_schema_readiness', 42)),
    'component_registry_readiness': max(26, prior_ex.get('component_registry_readiness', 22)),
    'route_inventory_readiness': max(22, prior_ex.get('route_inventory_readiness', 18)),
    'build_bible_readiness': max(58, prior_ex.get('build_bible_readiness', 54)),
    'technical_architecture_readiness': prior_ex.get('technical_architecture_readiness', 59),
    'wireframe_readiness': prior_ex.get('wireframe_readiness', 38),
    'founding_charter_readiness': prior_ex.get('founding_charter_readiness', 56),
    'institutional_manifesto_readiness': prior_ex.get('institutional_manifesto_readiness', 36),
    'hundred_builds_complete': True,
    'founding_blueprint_complete': True,
    'implementation_phase': 'sprint_zero_next',
}

mc['cursor_implementation_package_inventory'] = {
    'readiness_score': s['implementation_package_readiness_pct'],
    'steps_total': s['steps_total'],
    'steps_implemented': s['steps_implemented'],
    'steps_documented': s.get('steps_documented', 0),
    'bands_total': s['bands_total'],
    'sprint_zero_started': s['sprint_zero_started'],
    'cursor_master_prompt_ready': s['cursor_master_prompt_ready'],
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 101
        bar['note'] = f"Build #101 — Implementation Package. {s['steps_implemented']}/{s['steps_total']} steps · {s['days_remaining']} days to Jan 2027."
    if bar.get('id') == 'founding_charter':
        bar['note'] = f"Founding charter · {prior_ex.get('founding_charter_readiness', 56)}% readiness."

if not any(b.get('id') == 'cursor_implementation_package' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'cursor_implementation_package',
        'label': 'Implementation Package',
        'value': s['implementation_package_readiness_pct'],
        'max': 100,
        'note': f"{s['steps_implemented']}/{s['steps_total']} steps implemented · Sprint Zero {'started' if s['sprint_zero_started'] else 'pending'}.",
    })
else:
    for bar in mc['progress_bars']:
        if bar['id'] == 'cursor_implementation_package':
            bar['value'] = s['implementation_package_readiness_pct']

build_entry = {
    'number': 101,
    'title': title,
    'version': '2.05.1',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': '50 executable implementation steps — blueprint to code',
    'summary': (
        f"50 steps in 5 bands. IMP-01 Technical Constitution documented. "
        f"{s['implementation_package_readiness_pct']}% readiness · "
        f"{s.get('steps_documented', 0)}/{s['steps_total']} documented · "
        f"{s['steps_implemented']} implemented."
    ),
    'files_created': [
        'data/cursor-implementation-package.json',
        'docs/MASTER_CURSOR_IMPLEMENTATION_PACKAGE.md',
        'docs/CURSOR_MASTER_BUILD_PROMPT.md',
        'docs/IMPLEMENTATION_PACKAGE_01_TECHNICAL_CONSTITUTION.md',
        'builds/101-cursor-implementation-package.md',
        'mission-control/cursor-implementation-package.html',
        'scripts/gen-cursor-implementation-package.py',
        'scripts/update-mc-build101.py',
    ],
    'files_modified': [
        'js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml',
    ],
    'pages_created': ['/mission-control/cursor-implementation-package.html'],
    'decisions_made': [
        '50 steps — thorough without drifting into abstract planning',
        'IMP-01 Master Technical Constitution governs all future packages',
        'Five bands of 10: foundation, presentation, data, operations, knowledge/launch',
        'Supersedes Build Bible v1 as executable engineering layer (Build Bible v2)',
        f"{s.get('steps_documented', 0)} documented · {s['steps_implemented']} implemented — honest status",
        f"{s['implementation_package_readiness_pct']}% readiness",
    ],
    'open_questions': [
        'IMP-02 architecture and repository — next package',
        'MC read paths public vs auth-gated — IMP-28 decision',
        'Single source of truth: JSON registries vs DB — per-entity in IMP-47',
    ],
    'risks': cip['catalog_gaps'][:4],
    'next_recommended': 102,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/cursor-implementation-package.html',
    'review_status': 'complete',
}

mc['builds'] = [b for b in mc['builds'] if b.get('number') != 101]
mc['builds'].insert(0, build_entry)

mc['briefing'] = {
    'what_built': 'IMP-01 Technical Constitution + 50-step implementation package',
    'building_now': 'IMP-02 Technical Architecture & Repository Blueprint next',
    'blocked': ['Sprint Zero not complete', '0/50 steps code-implemented', 'No Neon/Prisma in production'],
    'ready_public': ['Technical Constitution', '50 step specs', 'Cursor master prompt', 'MVP scope'],
    'next': 'IMP-02 — Master Technical Architecture & Repository Blueprint',
}

if not any(n.get('id') == 'cursor_implementation_package' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'cursor_implementation_package',
        'label': 'Implementation Package',
        'href': '/mission-control/cursor-implementation-package.html',
        'status': 'complete',
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
