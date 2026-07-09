import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json', encoding='utf-8') as f:
    mc = json.load(f)

with open(root / 'data/cursor-implementation-package.json', encoding='utf-8') as f:
    cip = json.load(f)

s = cip['summary']
prior_ex = mc.get('executive', {})

mc['version'] = '2.05.8'
mc['updated'] = '2026-07-09'

mc['executive'] = {
    **prior_ex,
    'implementation_package_readiness': s['implementation_package_readiness_pct'],
    'cursor_implementation_package_readiness': s['implementation_package_readiness_pct'],
    'implementation_steps_documented': s.get('steps_documented', 0),
    'localbrain_architecture_readiness': max(65, prior_ex.get('localbrain_architecture_readiness', 60)),
    'institutional_ai_readiness': max(62, prior_ex.get('institutional_ai_readiness', 57)),
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
    'what_built': 'IMP-01–08 documented: Constitution through LocalBrain Network + manifests',
    'building_now': 'IMP-09 Master Knowledge Graph, Semantic Search & Institutional Memory next',
    'blocked': ['Sprint Zero not complete', '0/50 code-implemented', '0 LocalBrains online'],
    'ready_public': [
        'LocalBrain Network', 'localbrain-network-manifest.json',
        'Mission Control Architecture', 'Design System', 'Identity & Auth',
    ],
    'next': 'IMP-09 — Master Knowledge Graph, Semantic Search & Institutional Memory',
}

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
