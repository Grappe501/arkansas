"""
Generate data/master-arkansas-action-network.json — Build #95.
Master Arkansas Action Network — From Learning to Local Civic Participation v2.0.
"""
import json
from datetime import date
from pathlib import Path

root = Path(__file__).resolve().parents[1]
today = '2026-07-09'
completion_target_date = '2027-01-01'
completion_target = date(2027, 1, 1)
today_date = date(2026, 7, 9)
days_remaining = max((completion_target - today_date).days, 0)


def load_json(path):
    if path.exists():
        with open(path, encoding='utf-8') as f:
            return json.load(f)
    return {}


mc = load_json(root / 'data/mission-control.json')
aan = load_json(root / 'data/arkansas-action-network.json')
cac = load_json(root / 'data/citizen-action-center.json')
counties = load_json(root / 'data/arkansas-counties.json')

ex = mc.get('executive', {})

# Honest operational metrics
action_center_live = False
participation_calendar_live = False
action_dashboard_live = False
community_pages_enriched = False
bill_tracker_live = False
letter_builder_live = False
action_center_usage = 0

LEARNING_SEQUENCE = [
    {'step': 1, 'stage': 'Learn', 'status': 'partial'},
    {'step': 2, 'stage': 'Understand', 'status': 'partial'},
    {'step': 3, 'stage': 'Discuss', 'status': 'planned'},
    {'step': 4, 'stage': 'Decide', 'status': 'planned'},
    {'step': 5, 'stage': 'Participate', 'status': 'planned'},
]

ACTION_CENTER_QUESTIONS = [
    'Who represents me?',
    'When does the Arkansas General Assembly meet?',
    'How do I contact my state representative?',
    'How do I contact my state senator?',
    'Who is my member of Congress?',
    'How do I submit public comments?',
    'How do I testify before a committee?',
    'How does a bill become law in Arkansas?',
    'How does Congress pass a federal law?',
    'How do ballot initiatives work?',
    'Where can I find election information?',
]

PARTICIPATION_LIBRARY = [
    'Contacting elected officials',
    'Writing effective letters',
    'Meeting respectfully with elected officials',
    'Attending public meetings',
    'Speaking during public comment',
    'Following legislation',
    'Reading committee agendas',
    'Tracking bills',
    'Understanding public records',
    'Participating in civic organizations',
    'Registering to vote',
    'Serving as a poll worker',
    'Serving on local boards and commissions',
]

ACTION_OPPORTUNITIES = [
    {'id': 'AO-01', 'type': 'Arkansas General Assembly calendar', 'status': 'planned'},
    {'id': 'AO-02', 'type': 'Congressional calendar', 'status': 'planned'},
    {'id': 'AO-03', 'type': 'County quorum court meetings', 'status': 'partial'},
    {'id': 'AO-04', 'type': 'City council meetings', 'status': 'partial'},
    {'id': 'AO-05', 'type': 'School board meetings', 'status': 'planned'},
    {'id': 'AO-06', 'type': 'Public hearings', 'status': 'planned'},
    {'id': 'AO-07', 'type': 'Election deadlines', 'status': 'planned'},
    {'id': 'AO-08', 'type': 'Ballot initiative deadlines', 'status': 'planned'},
    {'id': 'AO-09', 'type': 'Educational events', 'status': 'partial'},
]

COMMUNITY_PAGE_FIELDS = [
    'Upcoming public meetings',
    'Local government contacts',
    'Legislative districts',
    'Community organizations',
    'Volunteer opportunities',
    'Educational events',
]

LEGISLATIVE_RESOURCES = [
    {'id': 'LR-01', 'resource': 'Bill tracker', 'status': 'planned'},
    {'id': 'LR-02', 'resource': 'Committee directory', 'status': 'planned'},
    {'id': 'LR-03', 'resource': 'Legislator directory', 'status': 'planned'},
    {'id': 'LR-04', 'resource': 'Congressional directory', 'status': 'planned'},
    {'id': 'LR-05', 'resource': 'Legislative glossary', 'status': 'partial'},
    {'id': 'LR-06', 'resource': 'How a bill moves', 'status': 'partial'},
    {'id': 'LR-07', 'resource': 'Legislative calendars', 'status': 'planned'},
    {'id': 'LR-08', 'resource': 'Committee testimony guide', 'status': 'planned'},
    {'id': 'LR-09', 'resource': 'Federal legislative process', 'status': 'partial'},
]

LETTER_TEMPLATES = [
    'Questions for elected officials',
    'Meeting request templates',
    'Public comment outlines',
    'Legislative testimony structure',
    'Research citation references',
]

COMMUNITY_ISSUES = [
    'Campaign finance',
    'Transparency',
    'Ballot initiatives',
    'Election administration',
    'Constitutional amendments',
    'Government ethics',
]

VOLUNTEER_OPPORTUNITIES = [
    'Become an Education Leader',
    'Host community conversations',
    'Join research projects',
    'Help with technology',
    'Support communications',
    'Assist coalition partners',
    'Serve their county or city team',
]

ACTION_DASHBOARD_INDICATORS = [
    {'id': 'MAAN-D01', 'indicator': 'Public meeting calendar', 'current': 0, 'status': 'planned'},
    {'id': 'MAAN-D02', 'indicator': 'Legislative activity', 'current': 0, 'status': 'planned'},
    {'id': 'MAAN-D03', 'indicator': 'Educational participation', 'current': 0, 'status': 'planned'},
    {'id': 'MAAN-D04', 'indicator': 'Volunteer opportunities', 'current': 0, 'status': 'partial'},
    {'id': 'MAAN-D05', 'indicator': 'County activity', 'current': len(counties.get('counties', [])) if counties else 75, 'status': 'partial'},
    {'id': 'MAAN-D06', 'indicator': 'City activity', 'current': 0, 'status': 'planned'},
    {'id': 'MAAN-D07', 'indicator': 'Community conversations', 'current': 0, 'status': 'planned'},
    {'id': 'MAAN-D08', 'indicator': 'Action Center usage', 'current': action_center_usage, 'status': 'planned'},
]

master_arkansas_action_network_readiness = min(
    66,
    14
    + len(LEARNING_SEQUENCE) // 2
    + len(ACTION_CENTER_QUESTIONS) // 2
    + len(PARTICIPATION_LIBRARY) // 2
    + len(ACTION_OPPORTUNITIES) // 2
    + len(COMMUNITY_PAGE_FIELDS) // 2
    + len(LEGISLATIVE_RESOURCES) // 2
    + len(LETTER_TEMPLATES) // 2
    + len(COMMUNITY_ISSUES) // 2
    + len(VOLUNTEER_OPPORTUNITIES) // 2
    + len(ACTION_DASHBOARD_INDICATORS) // 2
    + (2 if action_dashboard_live else 0),
)

out = {
    'version': '2.0',
    'build': 95,
    'prior_build': 64,
    'updated': today,
    'completion_target_date': completion_target_date,
    'title': 'Master Arkansas Action Network v2.0',
    'subtitle': 'From Learning to Local Civic Participation',
    'tagline': 'Educate. Connect. Act.',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/master-arkansas-action-network.html',
    'constitution': '/docs/MASTER_ARKANSAS_ACTION_NETWORK_PARTICIPATION.md',
    'prior_constitution': '/docs/MASTER_ARKANSAS_ACTION_NETWORK.md',
    'prior_route': '/mission-control/arkansas-action-network.html',
    'purpose': (
        'Neutral, factual information about civic participation opportunities — without directing '
        'people to support or oppose particular candidates, parties, or policy positions. Makes '
        'participation understandable and accessible. Mission Control monitors statewide civic '
        'participation as a public service.'
    ),
    'governing_principle': (
        'The institution does not tell Arkansans what positions to take. It helps them understand '
        'how to engage thoughtfully, respectfully, and effectively in the civic life of their '
        'communities, their state, and their nation. That is the highest purpose of the Arkansas '
        'Action Network.'
    ),
    'founders_principle': (
        'Democracy depends upon citizens who understand how government actually works. Citizens '
        'United Facts removes confusion by explaining processes clearly, providing trustworthy '
        'resources, and making civic participation less intimidating. Knowledge creates confidence. '
        'Confidence encourages participation. Participation strengthens self-government.'
    ),
    'institutional_philosophy': {
        'title': 'Institutional Philosophy',
        'sequence': LEARNING_SEQUENCE,
        'institution_teaches_process': True,
        'individuals_make_own_decisions': True,
        'neutral_not_partisan': True,
    },
    'arkansas_action_center': {
        'title': 'The Arkansas Action Center',
        'questions': ACTION_CENTER_QUESTIONS,
        'emphasis_education_and_process': True,
        'live': action_center_live,
        'status': 'planned',
    },
    'civic_participation_library': {
        'title': 'Civic Participation Library',
        'guides': PARTICIPATION_LIBRARY,
        'explains_process_not_outcomes': True,
        'status': 'partial',
    },
    'action_opportunities': {
        'title': 'Action Opportunities',
        'calendar_types': ACTION_OPPORTUNITIES,
        'mc_maintains_calendar': True,
        'live': participation_calendar_live,
        'status': 'planned',
        'note': 'Arkansas civic participation calendar — not yet unified',
    },
    'community_action_pages': {
        'title': 'Community Action Pages',
        'fields_per_county_city': COMMUNITY_PAGE_FIELDS,
        'enriched': community_pages_enriched,
        'counties_total': len(counties.get('counties', [])) if counties else 75,
        'status': 'partial',
    },
    'legislative_resource_center': {
        'title': 'Legislative Resource Center',
        'resources': LEGISLATIVE_RESOURCES,
        'bill_tracker_live': bill_tracker_live,
        'status': 'partial',
    },
    'letter_communication_builder': {
        'title': 'Letter & Communication Builder',
        'templates': LETTER_TEMPLATES,
        'respectful_evidence_based': True,
        'live': letter_builder_live,
        'status': 'planned',
    },
    'community_issue_hub': {
        'title': 'Community Issue Hub',
        'topics': COMMUNITY_ISSUES,
        'tracks_educational_interest_not_positions': True,
        'status': 'planned',
    },
    'volunteer_opportunities': {
        'title': 'Volunteer Opportunities',
        'opportunities': VOLUNTEER_OPPORTUNITIES,
        'status': 'partial',
    },
    'mission_control_action_dashboard': {
        'title': 'Mission Control Action Dashboard',
        'indicators': ACTION_DASHBOARD_INDICATORS,
        'live': action_dashboard_live,
        'connects_learning_with_participation': True,
        'status': 'planned',
    },
    'integration': {
        'chain': (
            'Mission Control → Community Education Academy → County OS → City OS → '
            'Neighborhood OS → Coalition Network → Research Institute → Communications → '
            'Knowledge Platform'
        ),
        'systems': [
            {'system': 'Action Network Pipeline (#64)', 'route': '/mission-control/arkansas-action-network.html', 'status': 'live'},
            {'system': 'Citizen Action Center', 'route': '/mission-control/citizen-action-center.html', 'status': 'partial'},
            {'system': 'County OS (#77)', 'route': '/mission-control/arkansas-county-operating-system.html', 'status': 'live'},
            {'system': 'City OS (#78)', 'route': '/mission-control/arkansas-city-operating-system.html', 'status': 'live'},
            {'system': 'Neighborhood OS (#79)', 'route': '/mission-control/arkansas-neighborhood-operating-system.html', 'status': 'live'},
            {'system': 'Education Academy (#28)', 'route': '/mission-control/education-academy.html', 'status': 'partial'},
            {'system': 'Knowledge Platform (#93)', 'route': '/mission-control/civic-knowledge-platform.html', 'status': 'live'},
            {'system': 'Coalition Network', 'route': '/mission-control/coalition.html', 'status': 'partial'},
        ],
    },
    'long_term_vision': (
        'By January 2027, every Arkansan who visits Citizens United Facts leaves with a clearer '
        'understanding of how their government functions and how they can participate respectfully '
        'and effectively if they choose. The institution becomes a gateway to informed civic participation.'
    ),
    'summary': {
        'completion_target_date': completion_target_date,
        'days_remaining': days_remaining,
        'master_arkansas_action_network_readiness_pct': master_arkansas_action_network_readiness,
        'legacy_action_network_readiness_pct': aan.get('summary', {}).get('arkansas_action_network_readiness_pct', 38),
        'action_center_live': action_center_live,
        'participation_calendar_live': participation_calendar_live,
        'action_dashboard_live': action_dashboard_live,
        'community_pages_enriched': community_pages_enriched,
        'bill_tracker_live': bill_tracker_live,
        'letter_builder_live': letter_builder_live,
        'action_center_usage': action_center_usage,
        'participation_guides': len(PARTICIPATION_LIBRARY),
        'action_center_questions': len(ACTION_CENTER_QUESTIONS),
        'institutional_completion_pct': ex.get('overall_completion', mc.get('build', 94)),
    },
    'catalog_gaps': [
        'Action Center not live — no unified public-facing hub',
        'Participation calendar not unified across state/local/federal',
        'Community county/city pages not enriched with action fields',
        'Bill tracker not operational',
        'Letter & communication builder not live',
        'Community issue hub not tracking educational interest',
        'Action dashboard not live in Mission Control',
        'Legislative directories not populated',
        'Neutral-participation guardrails not enforced in UI',
        'Action Center usage not measured',
        'School board / public hearing calendars not integrated',
        'Federal legislative process guides incomplete',
    ],
    'recommended_next_build': {
        'number': 96,
        'title': 'Master Arkansas Civic Operating System (ACOS 2.0)',
        'note': (
            'One login, personalized civic workspace, role-based permissions, '
            'AI assistant, smart notifications, platform OS layer.'
        ),
    },
}

with open(root / 'data/master-arkansas-action-network.json', 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')

print(
    f'Master Arkansas Action Network: {len(ACTION_CENTER_QUESTIONS)} questions, '
    f'{len(PARTICIPATION_LIBRARY)} guides, {master_arkansas_action_network_readiness}% readiness'
)
