import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json') as f:
    mc = json.load(f)

mc['version'] = '1.16.0'
mc['build'] = 12
mc['updated'] = '2026-07-09'
mc['civic_ecosystem'] = '/data/civic-ecosystem.json'
mc['civic_ecosystem_route'] = '/mission-control/civic-ecosystem.html'

mc['executive'] = {
    'overall_completion': 12,
    'current_build': {'number': 12, 'title': 'Civic Action Ecosystem & Leadership Development System'},
    'active_phase': 'Civic Action Platform',
    'last_completed': 'Citizens United Knowledge Graph & Educational Intelligence Architecture',
    'next_build': {'number': 13, 'title': 'First Deep Content — KG-IDs, Evidence IDs, ds-* components'},
    'github_status': 'connected',
    'netlify_status': 'production_healthy',
    'content_readiness': 10,
    'research_readiness': 18,
    'data_viz_readiness': 2,
    'signup_funnel_readiness': 12,
    'civic_action_readiness': 22,
    'public_launch_readiness': 4,
    'public_launch_label': 'Early Foundation'
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 12
        bar['note'] = 'Nine frameworks live. Civic Growth Ladder + ladder-aware Action Hub. Deep content next.'
    if bar['id'] == 'signup':
        bar['value'] = 12
        bar['note'] = 'Civic Participation Constitution: 7-level ladder, participant schema v1.5, community conversation scaffold.'
    if bar['id'] == 'action_hub':
        bar['value'] = 18
        bar['note'] = '11 hub actions gated by civic growth level. civic-profile.js tracks participation signals.'
    if bar['id'] == 'relational':
        bar['value'] = 8
        bar['note'] = 'Relational organizing framework + referral/share tracking stubs.'
    if bar['id'] == 'model_law':
        bar['value'] = 5
        bar['note'] = 'Model Law Workspace linked from Policy Development Center.'
    if bar['id'] == 'ballot_lab':
        bar['value'] = 5
        bar['note'] = 'Ballot Initiative Lab linked from Policy Development Center.'

mc['civic_action']['readiness_score'] = 22

mc['builds'].insert(0, {
    'number': 12,
    'title': 'Civic Action Ecosystem & Leadership Development System',
    'version': '1.16.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Civic Participation Constitution — educate first, voluntary leadership network',
    'summary': '7-level Civic Growth Ladder, 11 ladder-aware hub actions, community conversation program, leadership dashboard, participant schema v1.5.',
    'files_created': [
        'data/civic-ecosystem.json', 'docs/CIVIC_PARTICIPATION_CONSTITUTION.md',
        'builds/012-civic-action-ecosystem.md', 'js/civic-profile.js',
        'action/community-conversation.html', 'mission-control/civic-ecosystem.html'
    ],
    'files_modified': ['js/action-hub.js', 'js/layout.js', 'js/mission-control.js', 'data/participant-profile-schema.json', 'docs/CIVIC_ACTION.md'],
    'pages_created': ['/mission-control/civic-ecosystem.html', '/action/community-conversation.html'],
    'decisions_made': [
        '7-level Civic Growth Ladder governs hub action visibility',
        'Education before action — min_level gates on all hub actions',
        'Leadership metrics measure educational network, not political wins',
        'Community Conversation as dedicated program route'
    ],
    'open_questions': ['Backend for unified participant profiles?', 'Civic education certification timeline?'],
    'risks': ['Metrics at 0 until forms/backend — honest scaffolding'],
    'next_recommended': 13,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/civic-ecosystem.html',
    'review_status': 'complete'
})

mc['briefing'] = {
    'what_built': 'Civic Participation Constitution v1.0 — growth ladder, ladder-aware hub, leadership dashboard',
    'building_now': 'Civic ecosystem ready — deep content and facilitator materials next (Build #13)',
    'blocked': ['Participant profile backend', 'County coordinators', 'Certification program'],
    'ready_public': ['Action Hub 11 actions', 'Community conversation page', 'Civic level display in hub'],
    'next': 'Build #13 — First Deep Content with KG-IDs, Evidence IDs, ds-* components'
}

if not any(n.get('id') == 'civic_ecosystem' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'civic_ecosystem', 'label': 'Civic Ecosystem', 'href': '/mission-control/civic-ecosystem.html', 'status': 'complete'
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
