import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json', encoding='utf-8') as f:
    mc = json.load(f)

with open(root / 'data/cursor-implementation-package.json', encoding='utf-8') as f:
    cip = json.load(f)

s = cip['summary']
prior_ex = mc.get('executive', {})

mc['version'] = '2.05.7'
mc['updated'] = '2026-07-09'

mc['executive'] = {
    **prior_ex,
    'implementation_package_readiness': s['implementation_package_readiness_pct'],
    'cursor_implementation_package_readiness': s['implementation_package_readiness_pct'],
    'implementation_steps_documented': s.get('steps_documented', 0),
    'mc2_readiness': max(48, prior_ex.get('mc2_readiness', 42)),
    'institutional_digital_twin_readiness': max(55, prior_ex.get('institutional_digital_twin_readiness', 51)),
}

mc['cursor_implementation_package_inventory'] = {
    **mc.get('cursor_implementation_package_inventory', {}),
    'readiness_score': s['implementation_package_readiness_pct'],
    'steps_documented': s.get('steps_documented', 0),
}

for bar in mc['progress_bars']:
    if bar.get('id') == 'cursor_implementation_package':
        bar['value'] = s['implementation_package_readiness_pct']

mc['briefing'] = {
    'what_built': 'IMP-01–07 documented: Constitution through Mission Control Architecture + manifests',
    'building_now': 'IMP-08 Master LocalBrain Architecture & Institutional AI Network next',
    'blocked': ['Sprint Zero not complete', '0/50 code-implemented'],
    'ready_public': [
        'Technical Constitution', 'Route Map', 'Database Schema', 'Identity & Auth',
        'Design System', 'Mission Control Architecture', 'mission-control-architecture-manifest.json',
    ],
    'next': 'IMP-08 — Master LocalBrain Architecture & Institutional AI Network',
}

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
