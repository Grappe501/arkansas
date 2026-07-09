import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json') as f:
    mc = json.load(f)

title = 'Arkansas Civic Action Ecosystem & Leadership Development System'

mc['version'] = '1.16.1'
mc['updated'] = '2026-07-09'
mc['arkansas_counties'] = '/data/arkansas-counties.json'
mc['pilot_state'] = 'Arkansas'

mc['executive']['current_build'] = {'number': 12, 'title': title}
mc['executive']['active_phase'] = 'Arkansas Civic Action Platform'

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['note'] = 'Nine frameworks live. Arkansas Education Ladder + county dashboard. Deep content next.'
    if bar['id'] == 'signup':
        bar['note'] = 'Arkansas Participation Constitution: 7-level ladder, 75-county scaffold, participant schema v1.6.'
    if bar['id'] == 'action_hub':
        bar['note'] = '11 Arkansas Action Hub actions gated by education level. civic-profile.js tracks county + signals.'

for b in mc['builds']:
    if b.get('number') == 12:
        b['title'] = title
        b['version'] = '1.16.1'
        b['purpose'] = 'Arkansas Civic Participation Constitution — educate first, Arkansas pilot state'
        b['summary'] = (
            'Arkansas Education Ladder (7 levels), 75-county participation table, '
            'Arkansas Action Hub, community conversation program, leadership dashboard, participant schema v1.6.'
        )
        if 'data/arkansas-counties.json' not in b.get('files_created', []):
            b.setdefault('files_created', []).insert(1, 'data/arkansas-counties.json')
        b['decisions_made'] = [
            'Arkansas as pilot state — prove model in 75 counties before expansion',
            '7-level Arkansas Education Ladder governs hub action visibility',
            'Education before action — min_level gates on all hub actions',
            'County-level participation tracking for outreach planning'
        ]
        b['open_questions'] = [
            'Backend for unified participant profiles?',
            'Interactive Arkansas county map vs. table?',
            'Civic education certification timeline?'
        ]
        break

mc['briefing'] = {
    'what_built': 'Arkansas Civic Participation Constitution v1.0 — Education Ladder, county dashboard, Arkansas Action Hub',
    'building_now': 'Arkansas civic ecosystem ready — deep Arkansas content next (Build #13)',
    'blocked': ['Participant profile backend', 'County coordinators', 'Interactive county map'],
    'ready_public': ['Arkansas Action Hub 11 actions', 'Community conversation page', '75-county table in Mission Control'],
    'next': 'Build #13 — First Deep Content with KG-IDs, Evidence IDs, Arkansas-focused articles'
}

for n in mc['build_map']:
    if n.get('id') == 'civic_ecosystem':
        n['label'] = 'Arkansas Civic Ecosystem'

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
