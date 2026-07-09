"""
Generate data/wireframe-blueprint.json — Build #23 Major Screen Wireframe Blueprint v1.0.
"""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
today = '2026-07-09'

OUTCOMES = {
    'understand': 'Help readers understand Citizens United',
    'evidence': 'Help readers go deeper into evidence',
    'participate': 'Help Arkansans participate in education',
    'mission_control': 'Help the project team track progress',
}

def screen(sid, number, title, route, goal, sections, outcome, status='planned',
           current_route=None, current_status=None, ctas=None, world=None, notes=None):
    return {
        'id': sid,
        'number': number,
        'title': title,
        'route': route,
        'primary_goal': goal,
        'outcome': outcome,
        'sections': sections,
        'section_count': len(sections),
        'wireframe_status': status,
        'current_route': current_route or route,
        'implementation_status': current_status or status,
        'primary_cta': (ctas or {}).get('primary'),
        'secondary_cta': (ctas or {}).get('secondary'),
        'learning_world': world,
        'notes': notes,
    }

screens = [
    screen('WF-001', 1, 'Homepage', '/', 'Orient new visitors quickly', [
        'Hero: Understand Citizens United', 'Plain-language explanation',
        'What changed after 2010', 'Explore the learning worlds',
        'Follow the money preview', 'Arkansas solutions preview',
        'Coalition invitation', 'Education leader signup CTA', 'Source/trust footer'
    ], 'understand', 'partial', '/', 'live',
        {'primary': 'Start Learning', 'secondary': 'Help Educate Arkansas'}),
    screen('WF-002', 2, 'Start Here', '/start-here', 'Give beginners a clear first lesson', [
        'What is Citizens United?', 'One-minute answer', 'Five-minute explanation',
        'Common misunderstandings', 'What to learn next', 'Share this explanation',
        'Join contact network'
    ], 'understand', 'partial', '/start-here/', 'live', world='WORLD-01'),
    screen('WF-003', 3, 'Learning World Landing', '/the-story', 'Introduce a major learning area', [
        'World title', 'Why this section matters', 'Learning map', 'Featured lessons',
        'Timeline preview', 'Source highlights', 'Related worlds', 'Community education prompt'
    ], 'understand', 'partial', '/halls/story-before.html', 'redirect', world='WORLD-01',
        notes='Canonical /the-story redirects to story-before hall'),
    screen('WF-004', 4, 'Deep Lesson Page', '/the-case/majority-opinion', 'Teach one topic in layered depth', [
        'Breadcrumbs', 'Learning Compass', 'One-minute summary', 'Main explanation',
        'Key facts', 'Evidence panel', 'Related cases or concepts', 'Go deeper section',
        'Discussion questions', 'Share/teach CTA'
    ], 'understand', 'planned', '/halls/what-court-decided.html', 'partial', world='WORLD-02',
        notes='Dedicated deep routes not built — hall pages serve as interim'),
    screen('WF-005', 5, 'Timeline Page', '/the-story/timeline', 'Show historical development over time', [
        'Timeline introduction', 'Filter controls', 'Major eras', 'Expandable event cards',
        'Related laws and cases', 'Source links', 'Why this matters callouts',
        'Download timeline handout'
    ], 'evidence', 'planned', None, 'planned', world='WORLD-01'),
    screen('WF-006', 6, 'Spending Data Page', '/the-impact/spending-data', 'Explain measurable spending changes', [
        'Data overview', 'Before/after 2010 comparison', 'Chart cards', 'Definitions',
        'Source notes', 'Data limitations', 'Download data summary',
        'Share with public officials CTA'
    ], 'evidence', 'planned', '/halls/money-map.html', 'partial', world='WORLD-04'),
    screen('WF-007', 7, 'Follow the Money', '/follow-the-money', 'Help users understand money pathways', [
        'Intro explanation', 'Money flow diagram', 'Key entities: individuals, PACs, Super PACs, nonprofits',
        'Disclosure explanation', 'Coordination explanation', 'Common misconceptions',
        'Related data', 'Explore reform options'
    ], 'evidence', 'partial', '/halls/money-map.html', 'redirect', world='WORLD-04'),
    screen('WF-008', 8, 'Solutions Landing', '/solutions', 'Show possible responses without oversimplifying', [
        'Solutions overview', 'Federal options', 'Congressional action options',
        'Arkansas General Assembly options', 'Model Law Workspace', 'Ballot Initiative Lab',
        'Montana case study', 'Hawaii case study', 'Share with lawmakers CTA'
    ], 'participate', 'partial', '/solutions/', 'partial', world='WORLD-06'),
    screen('WF-009', 9, 'Arkansas Hub', '/arkansas', 'Connect national education to Arkansas civic participation', [
        'Why Arkansas matters', 'Arkansas learning network', 'County participation preview',
        'Arkansas General Assembly education', 'Community education opportunities',
        'Coalition partner invitation', 'Education leader signup', 'Upcoming events'
    ], 'participate', 'partial', '/arkansas/', 'live', world='WORLD-06'),
    screen('WF-010', 10, 'Teach Your Community', '/teach', 'Turn learners into local educators', [
        'Teaching invitation', 'Choose your setting (home, civic club, faith, campus, classroom, library)',
        'Download toolkit', 'Event planning guide', 'Presentation resources',
        'Conversation tips', 'Sign up to lead'
    ], 'participate', 'partial', '/educate/', 'redirect', world='WORLD-07',
        notes='/teach redirects to /educate/'),
    screen('WF-011', 11, 'Join', '/join', 'Let individuals choose their participation path', [
        'Raise your hand', 'Role cards (leader, contact network, research, event host, share)',
        'Signup form preview', 'Privacy note', 'Confirmation expectations'
    ], 'participate', 'partial', '/join/', 'live', world='WORLD-07'),
    screen('WF-012', 12, 'Coalition Landing', '/coalition', 'Invite Arkansas organizations to support education', [
        'Coalition mission', 'Who can join', 'Partnership levels', 'Benefits/resources',
        'Arkansas county map', 'Partner directory preview', 'Organization sign-on CTA',
        'Social media/resource kit'
    ], 'participate', 'partial', '/coalition/', 'live', world='WORLD-07'),
    screen('WF-013', 13, 'Organization Sign-On Form', '/coalition/sign-on', 'Collect organization interest', [
        'Organization intro', 'Form fields', 'Participation level',
        'Public/private profile choices', 'Resource requests', 'Consent language',
        'Confirmation page'
    ], 'participate', 'partial', '/coalition/join.html', 'partial',
        notes='Canonical /coalition/sign-on → join.html'),
    screen('WF-014', 14, 'Floating Action Hub', '*(global)*', 'Persistent civic actions without blocking reading', [
        'Collapsed: small floating button',
        'Expanded: Education Leader, Contact Network, Share Page, Invite Friends',
        'Organization Sign-On, Draft Model Law, Ballot Lab, Share With Officials, Ask Question'
    ], 'participate', 'partial', 'js/action-hub.js', 'live',
        notes='9 actions; context adaptation partial'),
    screen('WF-015', 15, 'Mission Control Dashboard', '/mission-control', 'Track project progress publicly', [
        'Executive summary', 'Overall completion', 'Phase progress cards', 'Build history',
        'Content readiness', 'Research readiness', 'Civic action readiness',
        'Coalition readiness', 'Deployment status', 'Next build recommendation'
    ], 'mission_control', 'live', '/mission-control/', 'live'),
    screen('WF-016', 16, 'Mission Control Phase Detail', '/mission-control/phases', 'Show every phase and step', [
        'Phase filter', 'Progress bars', 'Step table', 'Blocked items',
        'Completed items', 'Related build records', 'Notes'
    ], 'mission_control', 'live', '/mission-control/phases.html', 'live'),
    screen('WF-017', 17, 'Source Library', '/sources', 'Let readers verify evidence', [
        'Source library overview', 'Search/filter', 'Source categories',
        'Featured primary sources', 'Evidence tiers', 'Recently reviewed sources',
        'Downloadable source packets'
    ], 'evidence', 'partial', '/library/', 'redirect',
        notes='/sources redirects to /library/'),
    screen('WF-018', 18, 'Public Official Sharing', '/solutions/share-with-officials', 'Share educational resources with lawmakers', [
        'Educational purpose note', 'Choose official type (House, Senate, AR General Assembly)',
        'Choose resource packet', 'Message template', 'Delivery instructions',
        'Confirmation/follow-up'
    ], 'participate', 'planned', '/action/contact-legislators.html', 'stub', world='WORLD-06'),
    screen('WF-019', 19, 'Model Law Workspace', '/solutions/model-laws', 'Explore potential legislative ideas', [
        'Purpose and disclaimer', 'Federal concepts', 'Arkansas concepts',
        'Research requirements', 'Draft concept cards', 'Submit idea form', 'Review process'
    ], 'participate', 'stub', '/action/draft-laws.html', 'stub', world='WORLD-06'),
    screen('WF-020', 20, 'Ballot Initiative Lab', '/solutions/ballot-initiative-lab', 'Explore Arkansas ballot-petition concepts', [
        'Purpose and disclaimer', 'Arkansas ballot initiative basics', 'Example reform concepts',
        'Research requirements', 'Draft language workspace', 'Submit concept form',
        'Legal review warning'
    ], 'participate', 'stub', '/action/ballot-lab.html', 'stub', world='WORLD-06'),
    screen('WF-021', 21, 'Social Media & Outreach', '/coalition/resources/social', 'Help share educational content', [
        'Social media mission', 'Shareable graphics', 'Post templates', 'Video clips',
        'Suggested captions', 'Link-back instructions', 'Partner sharing guidelines'
    ], 'participate', 'planned', '/coalition/resources.html', 'partial'),
    screen('WF-022', 22, 'County Page Template', '/arkansas/[county]', 'Show county-specific education activity', [
        'County overview', 'Education leaders', 'Coalition partners', 'Events',
        'Resource downloads', 'Public officials', 'Volunteer gaps',
        'Become a county education leader CTA'
    ], 'participate', 'partial', '/coalition/county.html', 'partial', world='WORLD-07',
        notes='75 county scaffold pages via query param'),
    screen('WF-023', 23, 'Admin Signup Review', '/admin/signups', 'Review and manage submissions', [
        'Signup queue', 'Filters', 'Person detail panel', 'Interest tags',
        'Follow-up status', 'Export options', 'Notes'
    ], 'mission_control', 'planned', None, 'planned'),
    screen('WF-024', 24, 'Admin Coalition Review', '/admin/coalition', 'Review organization sign-ons', [
        'Organization queue', 'Partner status', 'County', 'Organization type',
        'Public profile approval', 'Follow-up notes', 'Resource requests'
    ], 'mission_control', 'planned', '/admin/mission-control/', 'stub'),
    screen('WF-025', 25, 'Confirmation Page Template', '*(post-form)*', 'Confirm submission and guide next steps', [
        'Thank-you message', 'What happens next', 'Recommended next resource',
        'Share invitation', 'Contact/network reminder', 'Return to learning path'
    ], 'participate', 'planned', None, 'planned'),
]

mobile_requirements = [
    'Thumb-friendly navigation', 'Collapsible sections', 'Readable text',
    'Sticky or floating CTA', 'Accessible forms', 'Fast load times', 'Clear return paths'
]

by_outcome = {}
by_status = {}
for sc in screens:
    by_outcome[sc['outcome']] = by_outcome.get(sc['outcome'], 0) + 1
    by_status[sc['wireframe_status']] = by_status.get(sc['wireframe_status'], 0) + 1

out = {
    'version': '1.0',
    'build': 23,
    'updated': today,
    'title': 'Major Screen Wireframe Blueprint v1.0',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/wireframes.html',
    'constitution': '/docs/WIREFRAME_BLUEPRINT.md',
    'purpose': 'Define major screens before visual design and coding begin.',
    'screen_principle': 'Make the next step obvious without pushing. Educational, trustworthy, purposeful.',
    'outcomes': OUTCOMES,
    'screens': screens,
    'screen_count': len(screens),
    'mobile_requirements': mobile_requirements,
    'global_components': [
        {'id': 'COMP-NAV-001', 'title': 'Global Header', 'screens': 'all public'},
        {'id': 'COMP-NAV-003', 'title': 'Breadcrumbs', 'screens': 'deep lesson, county'},
        {'id': 'COMP-NAV-004', 'title': 'Learning Compass', 'screens': 'deep lesson, world landing'},
        {'id': 'COMP-CIVIC-001', 'title': 'Floating Action Hub', 'screens': 'WF-014 global'},
        {'id': 'COMP-EDU-006', 'title': 'Fact vs Interpretation', 'screens': 'debate, deep lesson'},
        {'id': 'COMP-EDU-007', 'title': 'Primary Source Panel', 'screens': 'source library, deep lesson'},
        {'id': 'COMP-TRUST-001', 'title': 'Citation Panel', 'screens': 'all educational'},
    ],
    'summary': {
        'screens': len(screens),
        'sections_total': sum(s['section_count'] for s in screens),
        'by_outcome': by_outcome,
        'wireframe_defined': len(screens),
        'wireframe_partial': by_status.get('partial', 0),
        'wireframe_planned': by_status.get('planned', 0),
        'wireframe_stub': by_status.get('stub', 0),
        'wireframe_live': by_status.get('live', 0),
        'implementation_live': sum(1 for s in screens if s['implementation_status'] == 'live'),
        'implementation_partial': sum(1 for s in screens if s['implementation_status'] in ('partial', 'redirect')),
        'implementation_planned': sum(1 for s in screens if s['implementation_status'] in ('planned', 'stub')),
        'wireframe_readiness_pct': round(
            (by_status.get('live', 0) * 100 + by_status.get('partial', 0) * 55 +
             by_status.get('stub', 0) * 20) / max(len(screens), 1)
        ),
    },
    'integrations': [
        {'system': 'Knowledge Atlas', 'build': 19, 'route': '/mission-control/atlas.html'},
        {'system': 'Component Registry', 'build': 17, 'route': '/mission-control/components.html'},
        {'system': 'Route Registry', 'build': 16, 'route': '/mission-control/routes.html'},
        {'system': 'Database Schema', 'build': 22, 'route': '/mission-control/database.html'},
    ],
    'catalog_gaps': [
        'No visual mockups/Figma — wireframe sections only',
        'Dedicated deep lesson routes not built',
        'Timeline and spending-data pages planned',
        'Admin signup/coalition review screens not built',
        'Confirmation page template not standardized',
        'Learning Compass UI not on all screens',
    ],
    'recommended_next_build': {
        'number': 24,
        'title': 'Component Specifications with Props/States',
        'note': 'Map wireframe sections to component props. Deferred — contact intelligence prioritized in Build #24.'
    },
}

path = root / 'data/wireframe-blueprint.json'
with open(path, 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')
print(f'Wireframes: {len(screens)} screens, {out["summary"]["wireframe_readiness_pct"]}% readiness')
