import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json', encoding='utf-8') as f:
    mc = json.load(f)

with open(root / 'data/cursor-implementation-package.json', encoding='utf-8') as f:
    cip = json.load(f)

s = cip['summary']
prior_ex = mc.get('executive', {})

mc['version'] = '2.05.6'
mc['updated'] = '2026-07-09'

mc['executive'] = {
    **prior_ex,
    'implementation_package_readiness': s['implementation_package_readiness_pct'],
    'cursor_implementation_package_readiness': s['implementation_package_readiness_pct'],
    'implementation_steps_documented': s.get('steps_documented', 0),
    'component_registry_readiness': max(38, prior_ex.get('component_registry_readiness', 26)),
    'wireframe_readiness': max(42, prior_ex.get('wireframe_readiness', 38)),
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
    'what_built': 'IMP-01–06 documented: Constitution through Design System + manifests',
    'building_now': 'IMP-07 Master Mission Control Architecture & Executive Command Center next',
    'blocked': ['Sprint Zero not complete', '0/50 code-implemented'],
    'ready_public': [
        'Technical Constitution', 'Technical Architecture', 'Route Map', 'Database Schema',
        'Identity & Auth', 'Design System', 'design-system-manifest.json',
    ],
    'next': 'IMP-07 — Master Mission Control Architecture & Executive Command Center',
}

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
