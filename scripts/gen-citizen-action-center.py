"""
Generate data/citizen-action-center.json — Build #62.
Master Citizen Action Center & Civic Engagement Hub v1.0.
"""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
today = '2026-07-09'


def load_json(path):
    if path.exists():
        with open(path, encoding='utf-8') as f:
            return json.load(f)
    return {}


mc = load_json(root / 'data/mission-control.json')
cal = load_json(root / 'data/civic-action-lab.json')
sg = load_json(root / 'data/statewide-growth.json')
cn = load_json(root / 'data/coalition-network.json')
vj = load_json(root / 'data/visitor-journey.json')

ex = mc.get('executive', {})
participants = vj.get('summary', {}).get('contact_network_signups', 0)
edu_leaders = vj.get('summary', {}).get('education_leader_signups', 0)
PARTICIPANTS_TARGET = 200_000
counties_total = 75

# Honest zeros
registered_participants = 0
conversations = 0
packets_downloaded = 0
resources_shared = 0
academy_enrolled = 0
submissions_pending = 0
action_hub_live = mc.get('civic_action', {}).get('action_hub_links', 2) if isinstance(mc.get('civic_action'), dict) else 2

GUIDING_SEQUENCE = [
    {'step': 1, 'stage': 'Learn', 'status': 'partial'},
    {'step': 2, 'stage': 'Understand', 'status': 'partial'},
    {'step': 3, 'stage': 'Verify', 'status': 'partial'},
    {'step': 4, 'stage': 'Discuss', 'status': 'planned'},
    {'step': 5, 'stage': 'Participate', 'status': 'planned'},
]

SIX_PATHWAYS = [
    {
        'id': 'PATH-1', 'number': 1, 'title': 'Stay Informed',
        'audience': 'Continued learners',
        'options': ['Email updates', 'New research notifications', 'Recently published resources', 'Upcoming conversations', 'Documentary releases'],
        'mc_tracks': 'Continued learning',
        'status': 'partial',
    },
    {
        'id': 'PATH-2', 'number': 2, 'title': 'Share Knowledge',
        'audience': 'Helpers',
        'options': ['Printable fact sheets', 'QR codes linking to lessons', 'Short educational videos', 'Social media graphics', 'Community discussion guides'],
        'emphasis': 'Educational resources — not slogans',
        'status': 'partial',
    },
    {
        'id': 'PATH-3', 'number': 3, 'title': 'Become an Education Leader',
        'audience': 'Teachers',
        'options': ['Complete Academy training', 'Download presentation materials', 'Host conversations', 'Join county education teams', 'Mentor future leaders'],
        'mc_tracks': 'Leadership development',
        'route': '/mission-control/education-academy.html',
        'status': 'planned',
    },
    {
        'id': 'PATH-4', 'number': 4, 'title': 'Strengthen the Coalition',
        'audience': 'Organizations & individuals',
        'options': ['Join coalition', 'Recommend partner organizations', 'Host educational events', 'Share institutional resources', 'Participate in statewide initiatives'],
        'route': '/mission-control/coalition-network.html',
        'status': 'planned',
    },
    {
        'id': 'PATH-5', 'number': 5, 'title': 'Civic Participation Resources',
        'audience': 'Engaged citizens',
        'options': [
            'Contacting elected officials respectfully',
            'Understanding committee hearings',
            'Following legislation',
            "Learning Arkansas's ballot initiative process",
            'Preparing educational resource packets',
        ],
        'note': 'Explains processes — does not direct toward a position',
        'route': '/mission-control/civic-action-lab.html',
        'status': 'partial',
    },
    {
        'id': 'PATH-6', 'number': 6, 'title': 'Research & Resource Contributions',
        'audience': 'Contributors',
        'options': ['Historical documents', 'Public records', 'Academic sources', 'Educational corrections', 'Community stories', 'Research suggestions'],
        'review': 'Editorial review before institutional content',
        'status': 'planned',
    },
]

OFFICIAL_PACKET_SECTIONS = [
    'Historical background', 'Constitutional context', 'Relevant research',
    'Primary sources', 'Arkansas-specific information',
]

OFFICIAL_AUDIENCES = [
    'Arkansas U.S. Representatives', 'Arkansas U.S. Senators', 'Members of the Arkansas General Assembly',
]

SHARING_AUDIENCES = [
    'Friends', 'Family', 'Neighbors', 'Community organizations',
    'Study groups', 'Libraries', 'Civic clubs', 'Education Leaders',
]

CITIZEN_DASHBOARD_PANELS = [
    'Learning progress', 'Saved resources', 'Upcoming events', 'Community conversations',
    'Academy status', 'Coalition participation', 'Leadership opportunities', 'Recommended next lessons',
]

COUNTY_ACTION_FIELDS = [
    'Education Leaders', 'Community conversations', 'Partner organizations',
    'Upcoming events', 'Available presentations', 'Volunteer opportunities', 'Relevant educational resources',
]

MC_CITIZEN_METRICS = [
    {'id': 'CAC-M1', 'metric': 'Registered participants', 'current': registered_participants, 'target': PARTICIPANTS_TARGET, 'status': 'live'},
    {'id': 'CAC-M2', 'metric': 'Education Leaders', 'current': edu_leaders, 'status': 'live'},
    {'id': 'CAC-M3', 'metric': 'Community conversations', 'current': conversations, 'status': 'live'},
    {'id': 'CAC-M4', 'metric': 'Coalition growth', 'current': cn.get('summary', {}).get('organizations_total', 0), 'status': 'live'},
    {'id': 'CAC-M5', 'metric': 'Educational packets downloaded', 'current': packets_downloaded, 'status': 'planned'},
    {'id': 'CAC-M6', 'metric': 'Resources shared', 'current': resources_shared, 'status': 'planned'},
    {'id': 'CAC-M7', 'metric': 'Academy participation', 'current': academy_enrolled, 'status': 'planned'},
    {'id': 'CAC-M8', 'metric': 'County participation', 'current': 0, 'target': counties_total, 'status': 'live'},
    {'id': 'CAC-M9', 'metric': '200K connected Arkansans', 'current': participants, 'target': PARTICIPANTS_TARGET, 'status': 'live'},
]

FUTURE_EXPANSION = [
    'Local volunteer matching', 'Community discussion circles',
    'Youth civic education initiatives', 'Expanded county resource directories',
    'Additional civic education topics',
]

SYSTEM_CONNECTIONS = [
    {'system': 'Civic Action Lab (#42)', 'route': '/mission-control/civic-action-lab.html', 'status': 'partial'},
    {'system': 'Action Hub', 'route': '/educate/', 'status': 'partial', 'note': f'{action_hub_live} items live'},
    {'system': 'Visitor Journey (#47)', 'route': '/mission-control/visitor-journey.html', 'status': 'partial'},
    {'system': 'Education Academy (#28)', 'route': '/mission-control/education-academy.html', 'status': 'partial'},
    {'system': 'Coalition Network (#61)', 'route': '/mission-control/coalition-network.html', 'status': 'live'},
    {'system': 'Statewide Growth (#56)', 'route': '/mission-control/statewide-growth.html', 'status': 'live'},
    {'system': 'Relationship OS (#59)', 'route': '/mission-control/relationship-os.html', 'status': 'live'},
    {'system': 'Mission Control', 'route': '/mission-control/', 'status': 'live'},
]

citizen_action_center_readiness = min(48, 20 + len(SIX_PATHWAYS) * 3 + action_hub_live * 2)

out = {
    'version': '1.0',
    'build': 62,
    'updated': today,
    'title': 'Master Citizen Action Center & Civic Engagement Hub v1.0',
    'subtitle': 'The Arkansas Citizen Action Center — From Understanding to Responsible Civic Participation',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/citizen-action-center.html',
    'constitution': '/docs/MASTER_CITIZEN_ACTION_CENTER.md',
    'purpose': (
        'Structured educational pathways for constructive civic participation — '
        'bridge between learning and community participation.'
    ),
    'governing_principle': (
        'Strengthen civic participation through education. Knowledge first. '
        'Participation is a personal choice supported by reliable information.'
    ),
    'not_advocacy': True,
    'bridge_role': 'Learning → community participation',
    'guiding_philosophy': {
        'sequence': 'Learn → Understand → Verify → Discuss → Participate',
        'rule': 'Education always comes before action',
        'stages': GUIDING_SEQUENCE,
    },
    'six_pathways': SIX_PATHWAYS,
    'public_official_resource_center': {
        'title': 'Educational Packets for Respectful Communication',
        'sections': OFFICIAL_PACKET_SECTIONS,
        'audiences': OFFICIAL_AUDIENCES,
        'principle': 'Educational materials — not advocacy scripts',
        'packets_available': 0,
        'status': 'planned',
    },
    'relational_sharing_hub': {
        'title': 'Share Through Trusted Relationships',
        'audiences': SHARING_AUDIENCES,
        'per_page_tools': True,
        'visualization_status': 'planned',
        'resources_shared': resources_shared,
    },
    'citizen_dashboard': {
        'title': 'Personal Participant Dashboard',
        'panels': CITIZEN_DASHBOARD_PANELS,
        'requires_registration': True,
        'registered_users': registered_participants,
        'status': 'planned',
    },
    'county_action_pages': {
        'title': 'Local Educational Opportunities',
        'fields': COUNTY_ACTION_FIELDS,
        'counties_total': counties_total,
        'counties_with_activity': 0,
        'route': '/coalition/counties.html',
        'status': 'scaffolded',
    },
    'mc_citizen_dashboard': {
        'title': 'Mission Control Citizen Metrics',
        'metrics': MC_CITIZEN_METRICS,
        'measures': 'Civic education capacity — not political influence',
        'status': 'partial',
    },
    'future_expansion': FUTURE_EXPANSION,
    'integration': {
        'systems': SYSTEM_CONNECTIONS,
        'extends': 'Civic Action Lab (#42) with citizen-facing engagement hub',
    },
    'long_term_vision': (
        "Arkansas's central gateway from learning to constructive civic participation — "
        'invited, never pressured, at each visitor\'s own pace.'
    ),
    'summary': {
        'pathways_total': len(SIX_PATHWAYS),
        'pathways_partial_or_live': sum(1 for p in SIX_PATHWAYS if p['status'] in ('live', 'partial')),
        'registered_participants': registered_participants,
        'participants_connected': participants,
        'participants_target': PARTICIPANTS_TARGET,
        'education_leaders': edu_leaders,
        'community_conversations': conversations,
        'packets_downloaded': packets_downloaded,
        'resources_shared': resources_shared,
        'academy_enrolled': academy_enrolled,
        'submissions_pending': submissions_pending,
        'action_hub_items_live': action_hub_live,
        'counties_with_activity': 0,
        'citizen_action_center_readiness_pct': citizen_action_center_readiness,
        'civic_action_readiness_pct': ex.get('civic_action_readiness', 28),
        'civic_action_lab_readiness_pct': cal.get('summary', {}).get('civic_action_lab_readiness_pct', 26),
        'public_launch_readiness_pct': ex.get('public_launch_readiness', 8),
    },
    'catalog_gaps': [
        f'0 registered participants — citizen dashboard not built',
        f'Action hub {action_hub_live}/10 items live — pathways mostly planned',
        'Public official packet builder not implemented — 0 packets',
        'Relational sharing visualization not built',
        'County action pages scaffold only — 0 counties with activity',
        'Pathway 6 submission workflow not implemented — editorial review queue empty',
        'Build #62 Citizen Action Center vs Build #42 Civic Action Lab — complementary, unify UI?',
        'No signup/registration for citizen dashboard — Netlify Forms only',
        '200K goal tracked in registry — 0 progress',
        'Per-page share tools not wired across educational pages',
    ],
    'recommended_next_build': {
        'number': 63,
        'title': 'Implementation Translation Layer & Engineering Artifacts',
        'note': (
            'Citizen dashboard schema, pathway routing, packet builder API, share tracking, '
            'route inventory, COMP-* specs, GitHub issue backlog.'
        ),
    },
}

with open(root / 'data/citizen-action-center.json', 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')

print(
    f'Citizen Action Center: {len(SIX_PATHWAYS)} pathways, '
    f'{registered_participants} registered, {citizen_action_center_readiness}% readiness'
)
