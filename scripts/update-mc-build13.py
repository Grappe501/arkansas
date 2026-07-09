import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json') as f:
    mc = json.load(f)

title = 'Coalition Building & Public Outreach'

mc['version'] = '1.17.0'
mc['build'] = 13
mc['updated'] = '2026-07-09'
mc['coalition_ecosystem'] = '/data/coalition-ecosystem.json'
mc['coalition_route'] = '/mission-control/coalition.html'
mc['coalition_hub'] = '/coalition/'

mc['executive'] = {
    'overall_completion': 13,
    'current_build': {'number': 13, 'title': title},
    'active_phase': 'Coalition & Outreach',
    'last_completed': 'Arkansas Civic Action Ecosystem & Leadership Development System',
    'next_build': {'number': 14, 'title': 'First Deep Content — KG-IDs, Evidence IDs, Arkansas articles'},
    'github_status': 'connected',
    'netlify_status': 'production_healthy',
    'content_readiness': 10,
    'research_readiness': 18,
    'data_viz_readiness': 2,
    'signup_funnel_readiness': 14,
    'civic_action_readiness': 22,
    'coalition_readiness': 10,
    'public_launch_readiness': 5,
    'public_launch_label': 'Early Foundation'
}

mc['coalition_outreach'] = {
    'readiness_score': 10,
    'organizations': 0,
    'counties_represented': 0,
    'events_scheduled': 0,
    'community_conversations': 0,
    'social_followers': 0,
    'official_shares': 0,
    'organization_referrals': 0,
    'resource_downloads': 0
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 13
        bar['note'] = 'Ten frameworks live. Coalition layer + three-path homepage. Deep content next.'
    if bar['id'] == 'signup':
        bar['note'] = 'Three homepage paths: Learn, Help, Partner. Org join + event forms scaffolded.'
    if bar['id'] == 'relational':
        bar['value'] = 10
        bar['note'] = 'Coalition directory + org referrals planned alongside relational organizing.'

if not any(b.get('id') == 'coalition' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'coalition',
        'label': 'Coalition & Outreach',
        'value': 10,
        'max': 100,
        'note': 'Directory, join form, resource center, event calendar, MC dashboard — 0 orgs until submissions.'
    })

mc['builds'].insert(0, {
    'number': 13,
    'title': title,
    'version': '1.17.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'First-class Coalition & Outreach Layer — Arkansas educational coalition, not a political campaign',
    'summary': 'Coalition directory, 5 membership levels, org join form, resource center, event calendar, growth dashboard, three-path homepage.',
    'files_created': [
        'data/coalition-ecosystem.json', 'data/coalition-directory.json',
        'data/organization-profile-schema.json', 'data/coalition-events.json',
        'docs/COALITION_OUTREACH.md', 'builds/013-coalition-outreach.md',
        'js/coalition-profile.js', 'coalition/index.html', 'coalition/join.html',
        'coalition/resources.html', 'coalition/events.html',
        'mission-control/coalition.html', 'scripts/update-mc-build13.py'
    ],
    'files_modified': [
        'index.html', 'css/education.css', 'data/site-architecture.json',
        'data/civic-ecosystem.json', 'js/mission-control.js', 'BUILD_PLAN.md',
        'builds/BUILDS.md', 'netlify.toml'
    ],
    'pages_created': [
        '/mission-control/coalition.html', '/coalition/', '/coalition/join.html',
        '/coalition/resources.html', '/coalition/events.html'
    ],
    'decisions_made': [
        'Coalition as first-class platform layer alongside Education, Research, Civic Action',
        'Homepage three parallel entry paths — Learn, Help, Partner',
        'Organizations join educational coalition, not political campaign',
        'County coalition map as table first; interactive map planned'
    ],
    'open_questions': [
        'Public org directory listing vs. approval workflow?',
        'Social media API integration for command center metrics?',
        'Supabase for org profiles and event calendar?'
    ],
    'risks': ['All coalition metrics at 0 until orgs join — honest scaffolding'],
    'next_recommended': 14,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/coalition.html',
    'review_status': 'complete'
})

mc['briefing'] = {
    'what_built': 'Coalition & Outreach Layer — org coalition, three-path homepage, MC dashboard',
    'building_now': 'Coalition framework live — deep Arkansas content next (Build #14)',
    'blocked': ['Org directory backend', 'Interactive coalition map', 'Social metrics APIs'],
    'ready_public': ['Three-path homepage', 'Coalition join form', 'Resource & event scaffolds'],
    'next': 'Build #14 — First Deep Content with KG-IDs, Evidence IDs, Arkansas articles'
}

if not any(n.get('id') == 'coalition' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'coalition', 'label': 'Coalition Hub', 'href': '/coalition/', 'status': 'building'
    })

for n in mc['build_map']:
    if n.get('id') == 'coalition':
        n['label'] = 'Coalition Hub'
        n['href'] = '/coalition/'
        n['status'] = 'building'

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
