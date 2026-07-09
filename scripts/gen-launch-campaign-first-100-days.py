"""
Generate data/launch-campaign-first-100-days.json — Build #87.
Master Launch Campaign & First 100 Days Blueprint v1.0.
"""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
today = '2026-07-09'
launch_date = '2027-01-01'
campaign_days = 100

def load_json(path):
    if path.exists():
        with open(path, encoding='utf-8') as f:
            return json.load(f)
    return {}


mc = load_json(root / 'data/mission-control.json')
mlp = load_json(root / 'data/master-launch-plan.json')
cr = load_json(root / 'data/arkansas-civic-reach-participation.json')

ex = mc.get('executive', {})

# Honest zeros — pre-launch
campaign_dashboard_live = False
campaign_started = False
campaign_day = 0
new_participants = 0
volunteer_growth = 0
education_leaders_recruited = 0
counties_represented = 0
cities_represented = 0
neighborhood_activity_count = 0
coalition_partners = 0
academy_enrollment = 0
community_conversations = 0
resource_downloads = 0
fifteen_pct_progress_counties = 0
first_100_days_report_published = False
community_pulse_report_published = False
institutional_progress_report_published = False

PRIMARY_OBJECTIVES = [
    'Introduce Citizens United Facts to Arkansas',
    'Recruit volunteers and Education Leaders',
    'Build relationships with organizations',
    'Expand educational participation',
    'Establish foundation for long-term county growth',
]

PHASES = [
    {
        'phase': 1, 'id': 'public_awareness', 'title': 'The First 30 Days — Public Awareness',
        'days': '1–30',
        'goals': [
            'Public website fully operational', 'Daily educational content',
            'Active social media presence', 'Email newsletter launched',
            'Community presentations begin', 'Coalition invitations distributed',
            'Initial media outreach', 'Academy enrollment opens',
        ],
        'mc_tracks_daily': True,
        'status': 'specified',
    },
    {
        'phase': 2, 'id': 'community_activation', 'title': 'Days 31–60 — Community Activation',
        'days': '31–60',
        'goals': [
            'Launch community conversations', 'Recruit additional county volunteers',
            'Expand city leadership', 'Introduce neighborhood learning circles',
            'Host online educational events', 'Publish additional research',
            'Grow the volunteer network',
        ],
        'broadcasting_to_relationships': True,
        'status': 'specified',
    },
    {
        'phase': 3, 'id': 'institutional_expansion', 'title': 'Days 61–100 — Institutional Expansion',
        'days': '61–100',
        'goals': [
            'Strengthen county leadership teams', 'Expand coalition partnerships',
            'Increase Academy completion', 'Identify future mentors',
            'Improve Mission Control using community feedback',
            'Publish first Community Pulse Report', 'Publish first Institutional Progress Report',
        ],
        'launch_to_sustainable_growth': True,
        'status': 'specified',
    },
]

DASHBOARD_INDICATORS = [
    {'id': 'LC-D01', 'indicator': 'New participants', 'current': new_participants, 'status': 'planned'},
    {'id': 'LC-D02', 'indicator': 'Volunteer growth', 'current': volunteer_growth, 'status': 'planned'},
    {'id': 'LC-D03', 'indicator': 'Education Leaders recruited', 'current': education_leaders_recruited, 'status': 'planned'},
    {'id': 'LC-D04', 'indicator': 'County representation', 'current': counties_represented, 'target': 75, 'status': 'planned'},
    {'id': 'LC-D05', 'indicator': 'City representation', 'current': cities_represented, 'target': 250, 'status': 'planned'},
    {'id': 'LC-D06', 'indicator': 'Neighborhood activity', 'current': neighborhood_activity_count, 'status': 'planned'},
    {'id': 'LC-D07', 'indicator': 'Coalition partners', 'current': coalition_partners, 'status': 'planned'},
    {'id': 'LC-D08', 'indicator': 'Academy enrollment', 'current': academy_enrollment, 'status': 'planned'},
    {'id': 'LC-D09', 'indicator': 'Community conversations', 'current': community_conversations, 'status': 'planned'},
    {'id': 'LC-D10', 'indicator': 'Educational resource downloads', 'current': resource_downloads, 'status': 'planned'},
    {'id': 'LC-D11', 'indicator': 'Progress toward 15% Connected Citizen Goal', 'current': fifteen_pct_progress_counties, 'target': 75, 'status': 'planned'},
]

WEEKLY_RHYTHM = [
    'Research publication', 'Educational video or presentation', 'Community conversation',
    'Volunteer onboarding', 'Coalition outreach', 'Mission Control review',
    'Leadership meeting', 'Community listening review',
]

COUNTY_CHALLENGE = [
    'Identifying local volunteers', 'Building relationships',
    'Recruiting Education Leaders', 'Scheduling community conversations',
    'Connecting with local organizations', 'Beginning progress toward long-term county goals',
]

COALITION_PRIORITIES = [
    'Libraries', 'Historical societies', 'Community colleges', 'Universities',
    'Nonprofits', 'Civic organizations', 'Community groups',
]

VOLUNTEER_DEVELOPMENT = [
    'Orientation', 'Academy enrollment', 'Mission explanation',
    'Resource toolkit', 'Mentor assignment (when available)', 'Leadership pathway',
]

REPORT_SECTIONS = [
    'Research completed', 'Participants connected', 'Counties represented',
    'Education Leaders', 'Community conversations', 'Coalition growth',
    'Lessons learned', 'Next priorities',
]

LEARNING_QUESTIONS = [
    'What worked?', 'What confused people?', 'What questions are repeated?',
    'What resources are missing?', 'Which counties need help?', 'How can the institution improve?',
]

SUCCESS_CRITERIA = [
    'Arkansans know the institution exists',
    'Communities begin using educational resources',
    'Volunteers begin building local leadership',
    'Coalition organizations begin collaborating',
    'Mission Control provides clear operational picture',
    'Reputation for accuracy, transparency, respectful civic education',
]

FOUNDERS_STANDARD = (
    'First 100 days are not about becoming the biggest civic education organization — '
    'they are about becoming the most trusted. Every presentation, article, volunteer, '
    'conversation, correction, partnership, interaction reinforces: Citizens United Facts '
    'is here to help Arkansas understand—not to tell Arkansas what to think.'
)

SYSTEM_CONNECTIONS = [
    {'system': 'Mission Control', 'route': '/mission-control/', 'status': 'live'},
    {'system': 'Community Education Academy (#68)', 'route': '/mission-control/citizen-leadership-academy.html', 'status': 'live'},
    {'system': 'Coalition Network (#61)', 'route': '/mission-control/coalition-network.html', 'status': 'live'},
    {'system': 'ACOS (#77)', 'route': '/mission-control/arkansas-county-operating-system.html', 'status': 'live'},
    {'system': 'ArCOS (#78)', 'route': '/mission-control/arkansas-city-operating-system.html', 'status': 'live'},
    {'system': 'ANOS (#79)', 'route': '/mission-control/arkansas-neighborhood-operating-system.html', 'status': 'live'},
    {'system': 'Arkansas Communications (#72)', 'route': '/mission-control/arkansas-communications.html', 'status': 'live'},
    {'system': 'Volunteer Network (#75)', 'route': '/mission-control/volunteer-funding-constitution.html', 'status': 'live'},
    {'system': 'Master Launch Plan (#85)', 'route': '/mission-control/master-launch-plan.html', 'status': 'live'},
    {'system': 'Civic Reach (#86)', 'route': '/mission-control/arkansas-civic-reach-participation.html', 'status': 'live'},
]

launch_campaign_readiness = min(
    57,
    19
    + len(PRIMARY_OBJECTIVES) * 2
    + len(PHASES) * 2
    + len(DASHBOARD_INDICATORS) // 2
    + len(WEEKLY_RHYTHM) // 2
    + len(COUNTY_CHALLENGE) // 2
    + len(VOLUNTEER_DEVELOPMENT) // 2
    + len(REPORT_SECTIONS) // 2
    + len(SUCCESS_CRITERIA) // 2
    + 3,
)

out = {
    'version': '1.0',
    'build': 87,
    'updated': today,
    'launch_date': launch_date,
    'campaign_days': campaign_days,
    'title': 'Master Launch Campaign & First 100 Days Blueprint v1.0',
    'subtitle': 'The First 100 Days',
    'tagline': 'Turning a Platform into a Statewide Movement',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/launch-campaign-first-100-days.html',
    'constitution': '/docs/MASTER_LAUNCH_CAMPAIGN_FIRST_100_DAYS.md',
    'purpose': (
        'First 100 days after January 2027 public launch — coordinated campaign for momentum, '
        'trust, volunteers, county leadership, and permanent civic education infrastructure.'
    ),
    'governing_principle': (
        'Launch creates attention. Trust creates institutions. Earn trust one conversation, '
        'one county, one volunteer, one coalition partner, one Arkansan at a time.'
    ),
    'primary_mission': {
        'title': 'Primary Mission',
        'objectives': PRIMARY_OBJECTIVES,
        'every_activity_supports_objectives': True,
    },
    'campaign_phases': {
        'title': 'Campaign Phases',
        'phases': PHASES,
        'phases_total': len(PHASES),
        'dedicated_operational_campaign': True,
    },
    'first_100_day_dashboard': {
        'title': 'First 100-Day Dashboard',
        'indicators': DASHBOARD_INDICATORS,
        'live': campaign_dashboard_live,
        'leadership_reviews_daily': True,
        'status': 'planned',
    },
    'weekly_operations_rhythm': {
        'title': 'Weekly Operations Rhythm',
        'activities': WEEKLY_RHYTHM,
        'predictable_operational_rhythm': True,
        'status': 'specified',
    },
    'county_challenge': {
        'title': 'County Challenge',
        'objectives': COUNTY_CHALLENGE,
        'no_county_left_behind': True,
        'status': 'specified',
    },
    'coalition_growth': {
        'title': 'Coalition Growth',
        'priority_partnerships': COALITION_PRIORITIES,
        'every_partnership_expands_reach': True,
        'status': 'specified',
    },
    'volunteer_development': {
        'title': 'Volunteer Development',
        'every_new_volunteer_receives': VOLUNTEER_DEVELOPMENT,
        'mc_tracks_progress': True,
        'status': 'specified',
    },
    'public_reporting': {
        'title': 'Public Reporting',
        'first_100_days_report': {
            'title': 'The First 100 Days Report',
            'sections': REPORT_SECTIONS,
            'published': first_100_days_report_published,
            'transparency_begins_immediately': True,
        },
        'community_pulse_report': community_pulse_report_published,
        'institutional_progress_report': institutional_progress_report_published,
        'status': 'specified',
    },
    'learning_during_launch': {
        'title': 'Learning During Launch',
        'questions': LEARNING_QUESTIONS,
        'learning_as_much_as_growing': True,
        'status': 'specified',
    },
    'success_definition': {
        'title': 'Success Definition',
        'criteria': SUCCESS_CRITERIA,
        'status': 'specified',
    },
    'founders_standard': {
        'title': "Founder's Standard",
        'text': FOUNDERS_STANDARD,
        'most_trusted_not_biggest': True,
        'help_understand_not_tell_what_to_think': True,
    },
    'integration': {
        'chain': (
            'Mission Control → Education Academy → Coalition Network → ACOS → ArCOS → '
            'ANOS → Communications → Volunteer Network'
        ),
        'every_system_participates_in_launch': True,
        'systems': SYSTEM_CONNECTIONS,
    },
    'long_term_vision': (
        'First 100 days transition launch into sustainable growth. Momentum becomes infrastructure. '
        'Attention becomes trust. Platform becomes statewide movement.'
    ),
    'summary': {
        'launch_date': launch_date,
        'campaign_days': campaign_days,
        'campaign_started': campaign_started,
        'campaign_day': campaign_day,
        'campaign_dashboard_live': campaign_dashboard_live,
        'new_participants': new_participants,
        'volunteer_growth': volunteer_growth,
        'education_leaders_recruited': education_leaders_recruited,
        'counties_represented': counties_represented,
        'cities_represented': cities_represented,
        'coalition_partners': coalition_partners,
        'community_conversations': community_conversations,
        'first_100_days_report_published': first_100_days_report_published,
        'launch_campaign_first_100_days_readiness_pct': launch_campaign_readiness,
        'master_launch_plan_readiness_pct': mlp.get('summary', {}).get('master_launch_plan_readiness_pct', 54),
        'civic_reach_readiness_pct': cr.get('summary', {}).get('arkansas_civic_reach_participation_readiness_pct', 56),
        'public_launch_readiness_pct': ex.get('public_launch_readiness', 8),
    },
    'catalog_gaps': [
        'First 100-day campaign dashboard not live',
        'Campaign not started — pre-launch (Jan 2027 target)',
        '0/100 campaign days tracked',
        '0 new participants · 0 volunteers · 0 Education Leaders',
        '0 counties/cities represented during campaign',
        'First 100 Days Report not published',
        'Community Pulse Report not published',
        'Institutional Progress Report not published',
        'Weekly rhythm specified — not enforced in MC workflow',
        'County Challenge not tracked per county',
        'Volunteer development pipeline not operational',
        'Build #87 vs Master Launch Plan (#85) — campaign vs readiness checklist',
    ],
    'recommended_next_build': {
        'number': 88,
        'title': 'First 100 Days Dashboard & Campaign Tracker Components',
        'note': (
            'Campaign dashboard UI, day counter, phase tracker, weekly rhythm checklist, '
            'county challenge tracker, First 100 Days report generator, COMP-* specs.'
        ),
    },
}

with open(root / 'data/launch-campaign-first-100-days.json', 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')

print(
    f'Launch Campaign First 100 Days: day {campaign_day}/{campaign_days}, '
    f'{new_participants} participants, {launch_campaign_readiness}% readiness'
)
