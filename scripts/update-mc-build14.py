import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json') as f:
    mc = json.load(f)

title = 'Arkansas Citizens United Coalition Operating System (ACUCOS)'

mc['version'] = '1.18.0'
mc['build'] = 14
mc['updated'] = '2026-07-09'
mc['acucos'] = '1.0'
mc['acucos_constitution'] = '/docs/ACUCOS_CONSTITUTION.md'
mc['county_coalition_index'] = '/data/county-coalition-index.json'

mc['executive'] = {
    'overall_completion': 14,
    'current_build': {'number': 14, 'title': title},
    'active_phase': 'ACUCOS — Coalition Operating System',
    'last_completed': 'Coalition Building & Public Outreach',
    'next_build': {'number': 15, 'title': 'First Deep Content — KG-IDs, Evidence IDs, Arkansas articles'},
    'github_status': 'connected',
    'netlify_status': 'production_healthy',
    'content_readiness': 10,
    'research_readiness': 18,
    'data_viz_readiness': 2,
    'signup_funnel_readiness': 14,
    'civic_action_readiness': 22,
    'coalition_readiness': 12,
    'public_launch_readiness': 5,
    'public_launch_label': 'Early Foundation'
}

mc['coalition_outreach'] = {
    'readiness_score': 12,
    'acucos_version': '1.0',
    'organizations': 0,
    'new_organizations_month': 0,
    'counties_represented': 0,
    'counties_with_partner': 0,
    'active_partnerships': 0,
    'events_scheduled': 0,
    'upcoming_events': 0,
    'completed_events': 0,
    'community_conversations': 0,
    'average_attendance': 0,
    'counties_hosting_events': 0,
    'toolkit_downloads': 0,
    'presentation_downloads': 0,
    'video_views': 0,
    'research_downloads': 0,
    'faq_usage': 0,
    'individual_referrals': 0,
    'organizational_referrals': 0,
    'returning_organizations': 0,
    'coalition_retention': 0,
    'social_followers': 0,
    'official_shares': 0,
    'organization_referrals': 0
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 14
        bar['note'] = 'ACUCOS live — 75 county coalition pages, 4-metric dashboard, growth engine.'
    if bar['id'] == 'coalition':
        bar['value'] = 12
        bar['note'] = 'ACUCOS v1.0 — observer→strategic partner, county completeness, recognition scaffold.'

mc['builds'].insert(0, {
    'number': 14,
    'title': title,
    'version': '1.18.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Coalition Architecture & Growth Blueprint v1.0 — statewide organizational backbone',
    'summary': 'ACUCOS: 6 participation levels, 7 categories, 75 county pages, growth engine, 4-metric dashboard, recognition & communications scaffold.',
    'files_created': [
        'docs/ACUCOS_CONSTITUTION.md', 'data/county-coalition-index.json',
        'builds/014-acucos.md', 'coalition/county.html', 'coalition/counties.html',
        'js/county-coalition.js', 'scripts/gen-county-coalition-index.py',
        'scripts/update-mc-build14.py'
    ],
    'files_modified': [
        'data/coalition-ecosystem.json', 'data/coalition-directory.json',
        'data/organization-profile-schema.json', 'js/mission-control.js',
        'js/coalition-profile.js', 'coalition/index.html', 'coalition/join.html',
        'mission-control/coalition.html', 'BUILD_PLAN.md'
    ],
    'pages_created': ['/coalition/county.html', '/coalition/counties.html'],
    'decisions_made': [
        'ACUCOS as coalition operating system — not a supporter list',
        'One educational partner per county as long-term vision',
        '6 participation levels including Observer and Event Partner',
        'County completeness tracked in Mission Control'
    ],
    'open_questions': [
        'Org directory approval workflow?',
        'Newsletter and coalition communications backend?',
        'Social API integration for outreach metrics?'
    ],
    'risks': ['County pages and metrics at 0 — honest scaffolding'],
    'next_recommended': 15,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/coalition.html',
    'review_status': 'complete'
})

mc['briefing'] = {
    'what_built': 'ACUCOS v1.0 — Coalition Operating System with 75 county pages and 4-metric dashboard',
    'building_now': 'ACUCOS framework live — deep Arkansas content next (Build #15)',
    'blocked': ['Org profile backend', 'Coalition newsletter', 'Interactive coalition map'],
    'ready_public': ['ACUCOS hub', 'County coalition pages', 'Updated join form', 'MC dashboard'],
    'next': 'Build #15 — First Deep Content with KG-IDs, Evidence IDs, Arkansas articles'
}

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
