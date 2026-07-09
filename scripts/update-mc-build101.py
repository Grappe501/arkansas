import json

from pathlib import Path



root = Path(__file__).resolve().parents[1]

with open(root / 'data/mission-control.json', encoding='utf-8') as f:

    mc = json.load(f)



with open(root / 'data/cursor-implementation-package.json', encoding='utf-8') as f:

    cip = json.load(f)



s = cip['summary']

prior_ex = mc.get('executive', {})

tl = cip.get('master_timeline', {})



mc['version'] = '2.05.12'

mc['updated'] = '2026-07-09'



mc['executive'] = {

    **prior_ex,

    'implementation_package_readiness': s['implementation_package_readiness_pct'],

    'cursor_implementation_package_readiness': s['implementation_package_readiness_pct'],

    'implementation_steps_documented': s.get('steps_documented', 0),

    'software_completion_date': s.get('software_completion_date', '2026-07-11'),

    'county_milestone_date': s.get('county_milestone_date', '2026-10-01'),

    'organizational_readiness_date': s.get('organizational_readiness_date', '2027-01-01'),

    'days_to_software': s.get('days_to_software', 0),

    'days_to_county_milestone': s.get('days_to_county_milestone', 0),

    'days_to_organizational': s.get('days_to_organizational', s.get('days_remaining', 0)),

    'knowledge_atlas_readiness': max(62, prior_ex.get('knowledge_atlas_readiness', 58)),

    'knowledge_graph_readiness': max(55, prior_ex.get('knowledge_graph_readiness', 0)),

}



if 'executive' in mc:

    mc['executive']['completion_target_date'] = s.get('organizational_readiness_date', '2027-01-01')

    mc['executive']['days_remaining_to_completion'] = s.get('days_to_organizational', s.get('days_remaining', 0))



mc['cursor_implementation_package_inventory'] = {

    **mc.get('cursor_implementation_package_inventory', {}),

    'readiness_score': s['implementation_package_readiness_pct'],

    'steps_documented': s.get('steps_documented', 0),

}



for bar in mc['progress_bars']:

    if bar.get('id') == 'cursor_implementation_package':

        bar['value'] = s['implementation_package_readiness_pct']



mc['briefing'] = {

    'what_built': 'IMP-01–12 documented — institutional foundation complete (24%)',

    'building_now': 'IMP-13 Volunteer Network & Education Leader Pipeline next; Sprint Zero pending',

    'blocked': ['Sprint Zero not complete', '0/50 code-implemented', f"{s.get('days_to_software', 0)} days to software target"],

    'ready_public': [

        'Education Academy', 'education-academy-manifest.json', 'Curriculum Factory',

        'Research Institute', 'Content Management', '75-by-October-1 Milestone',

    ],

    'next': 'IMP-13 — Master Volunteer Network, Education Leader Pipeline & Community Organizing Platform',

}



with open(root / 'data/mission-control.json', 'w', newline='\n') as f:

    json.dump(mc, f, indent=2)

    f.write('\n')

print('done')

