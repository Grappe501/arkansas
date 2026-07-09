import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json') as f:
    mc = json.load(f)

mc['version'] = '1.12.0'
mc['build'] = 8
mc['updated'] = '2026-07-09'
mc['ux_journey'] = '/data/ux-journey.json'
mc['ux_journey_route'] = '/mission-control/journey.html'

mc['executive'] = {
    'overall_completion': 8,
    'current_build': {'number': 8, 'title': 'User Experience Architecture & Journey System'},
    'active_phase': 'Information Architecture',
    'last_completed': 'Master Requirement ID System',
    'next_build': {'number': 9, 'title': 'First Deep Content — Priority MRIDs'},
    'github_status': 'connected',
    'netlify_status': 'production_healthy',
    'content_readiness': 8,
    'research_readiness': 3,
    'data_viz_readiness': 0,
    'signup_funnel_readiness': 8,
    'civic_action_readiness': 8,
    'public_launch_readiness': 3,
    'public_launch_label': 'Early Foundation'
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 8
        bar['note'] = 'Five registries + UX journey system live. Session memory, learning panel, stage-aware Action Hub. Content depth remains early.'
    if bar['id'] == 'ia':
        bar['value'] = 45
        bar['note'] = 'Citizen Journey Blueprint: personas, ladder, milestones, recommendations, accessibility standards.'
    if bar['id'] == 'signup':
        bar['value'] = 8
        bar['note'] = 'Education funnel integrated with journey stage Lead.'

mc['builds'].insert(0, {
    'number': 8,
    'title': 'User Experience Architecture & Journey System',
    'version': '1.12.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Design around people — Citizen Journey Blueprint with session memory and adaptive UX',
    'summary': '6 personas, 7-stage ladder, learning panel, continue-learning prompt, stage-aware Action Hub, success indicators.',
    'files_created': [
        'data/ux-journey.json', 'docs/UX_JOURNEY.md', 'builds/008-user-experience-architecture.md',
        'mission-control/journey.html', 'js/journey.js', 'css/journey-panel.css'
    ],
    'files_modified': ['js/action-hub.js', 'js/layout.js', 'js/mission-control.js', 'css/action-hub.css'],
    'pages_created': ['/mission-control/journey.html'],
    'decisions_made': [
        'localStorage session memory v1',
        'Education before action — hub adapts by stage',
        'No gamification — milestones encourage without points'
    ],
    'open_questions': ['Server-side journey sync when backend exists?', 'Persona self-selection on first visit?'],
    'risks': ['localStorage-only — journey resets on clear data'],
    'next_recommended': 9,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/journey.html',
    'review_status': 'complete'
})

mc['briefing'] = {
    'what_built': 'Full planning stack + Citizen Journey UX (panel, recommendations, stage-aware hub)',
    'building_now': 'UX v1 live on all public pages — ready for deep content with journey cross-links',
    'blocked': ['Participant backend', 'Spending charts', 'Server analytics'],
    'ready_public': ['Learning panel', 'Continue learning', 'Stage-aware Action Hub', 'Journey dashboard'],
    'next': 'Build #9 — First Deep Content with MRIDs and journey-aware cross-links'
}

if not any(n.get('id') == 'journey' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'journey', 'label': 'Citizen Journey', 'href': '/mission-control/journey.html', 'status': 'complete'
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
