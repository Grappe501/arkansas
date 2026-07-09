import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json', encoding='utf-8') as f:
    mc = json.load(f)

title = 'Citizens United Facts Cursor Implementation Package v1.0'

with open(root / 'data/cursor-implementation-package.json', encoding='utf-8') as f:
    cip = json.load(f)

s = cip['summary']
prior_ex = mc.get('executive', {})

mc['version'] = '2.05.5'
mc['build'] = 101
mc['updated'] = '2026-07-09'

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
    'database_schema_readiness': max(58, prior_ex.get('database_schema_readiness', 52)),
    'component_registry_readiness': max(26, prior_ex.get('component_registry_readiness', 22)),
    'route_inventory_readiness': max(28, prior_ex.get('route_inventory_readiness', 28)),
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
    if bar.get('id') == 'cursor_implementation_package':
        bar['value'] = s['implementation_package_readiness_pct']

build_entry = {
    'number': 101,
    'title': title,
    'version': '2.05.5',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': '50 executable implementation steps — blueprint to code',
    'summary': (
        f"50 steps in 5 bands. IMP-01–05 documented. "
        f"{s['implementation_package_readiness_pct']}% readiness · "
        f"{s.get('steps_documented', 0)}/{s['steps_total']} documented · "
        f"{s['steps_implemented']} implemented."
    ),
    'files_created': [
        'docs/IMPLEMENTATION_PACKAGE_05_IDENTITY_AUTH.md',
        'data/identity-auth-manifest.json',
    ],
    'decisions_made': [
        'IMP-05 Identity & Auth: nine-role hierarchy, additive permissions, multi-role support',
        'Engineering IMP-06 merged repository migration + stack lock + environment',
    ],
    'next_recommended': 102,
    'branch': 'main',
    'git_commit': 'pending',
    'review_status': 'complete',
}

mc['builds'] = [b for b in mc['builds'] if b.get('number') != 101]
existing = next((b for b in mc['builds'] if b.get('number') == 101), None)
if existing:
    merged = {**existing, **build_entry}
    merged['files_created'] = list(dict.fromkeys(
        existing.get('files_created', []) + build_entry['files_created']
    ))
    merged['decisions_made'] = list(dict.fromkeys(
        existing.get('decisions_made', []) + build_entry['decisions_made']
    ))
    mc['builds'] = [b for b in mc['builds'] if b.get('number') != 101]
    mc['builds'].insert(0, merged)
else:
    mc['builds'].insert(0, build_entry)

mc['briefing'] = {
    'what_built': 'IMP-01–05 documented: Constitution through Identity & Auth + manifests',
    'building_now': 'IMP-06 Master Design System, User Experience & Visual Language next',
    'blocked': ['Sprint Zero not complete', '0/50 code-implemented', 'Auth not wired in production'],
    'ready_public': [
        'Technical Constitution', 'Technical Architecture', 'Route Map', 'Database Schema',
        'Identity & Auth', 'identity-auth-manifest.json',
    ],
    'next': 'IMP-06 — Master Design System, User Experience & Visual Language',
}

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
