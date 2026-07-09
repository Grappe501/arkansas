"""
Generate data/neighborhood-organizing.json and data/neighborhood-profiles.json — Build #57.
Arkansas Neighborhood Organizing & Relational Network — The Last Mile Architecture v1.0.
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
sg = load_json(root / 'data/statewide-growth.json')
counties_data = load_json(root / 'data/arkansas-counties.json')
cities_data = load_json(root / 'data/arkansas-cities.json')
coalition = load_json(root / 'data/coalition-directory.json')
vj = load_json(root / 'data/visitor-journey.json')

ex = mc.get('executive', {})
orgs = coalition.get('summary', {}).get('total_organizations', 0)
edu_leaders = vj.get('summary', {}).get('education_leader_signups', 0)
participants = vj.get('summary', {}).get('contact_network_signups', 0)
PARTICIPANTS_TARGET = 200_000

counties_total = counties_data.get('counties_total', 75)
cities_total = cities_data.get('cities_total', 250)

# Honest: no neighborhoods onboarded yet
neighborhoods_represented = 0
neighborhood_leaders = 0
active_conversations = 0
resources_shared = 0
events_held = 0
returning_participants = 0
referrals_tracked = 0

GEOGRAPHIC_LAYERS = [
    {
        'layer': 1, 'id': 'statewide', 'title': 'Statewide',
        'mission': 'Coordinate the entire institution',
        'target': None,
        'current': {'status': 'partial', 'route': '/mission-control/'},
        'status': 'partial',
    },
    {
        'layer': 2, 'id': 'county', 'title': 'County',
        'mission': 'Coordinate county education',
        'target': '75 county teams',
        'current': {'teams': 0, 'counties_total': counties_total},
        'status': 'scaffolded',
        'route': '/mission-control/county-os.html',
    },
    {
        'layer': 3, 'id': 'city', 'title': 'City',
        'mission': 'Coordinate community education',
        'target': '250 largest Arkansas cities',
        'current': {'cities_represented': 0, 'cities_total': cities_total},
        'status': 'scaffolded',
        'route': '/data/arkansas-cities.json',
    },
    {
        'layer': 4, 'id': 'neighborhood', 'title': 'Neighborhood',
        'mission': 'Bring civic education directly into communities',
        'target': 'Lasting local relationships',
        'current': {'neighborhoods_represented': neighborhoods_represented, 'leaders': neighborhood_leaders},
        'status': 'planned',
        'note': 'Last mile — where relationships are built',
    },
]

NEIGHBORHOOD_LEADER_ACTIVITIES = [
    'Sharing educational resources',
    'Hosting small discussions',
    'Connecting neighbors with local events',
    'Introducing people to the Community Education Academy',
    'Identifying local organizations interested in civic education',
]

PROFILE_FIELDS = [
    'General neighborhood name or identifier',
    'Associated city',
    'Associated county',
    'Education Leader(s)',
    'Community conversations',
    'Coalition connections',
    'Educational events',
    'Resource distribution',
]

RELATIONAL_PATHWAYS = [
    {'id': 'friend', 'pathway': 'Friend invites friend', 'status': 'planned'},
    {'id': 'neighbor', 'pathway': 'Neighbor invites neighbor', 'status': 'planned'},
    {'id': 'family', 'pathway': 'Family member shares learning resources', 'status': 'planned'},
    {'id': 'org', 'pathway': 'Community organization introduces participants', 'status': 'planned'},
    {'id': 'mentor', 'pathway': 'Education Leader mentors another Education Leader', 'status': 'planned'},
]

RESOURCE_KIT_ITEMS = [
    {'id': 'RK-1', 'item': 'Conversation guides', 'status': 'planned'},
    {'id': 'RK-2', 'item': 'One-page summaries', 'status': 'partial', 'route': '/educate/'},
    {'id': 'RK-3', 'item': 'Printable handouts', 'status': 'planned'},
    {'id': 'RK-4', 'item': 'QR codes linking to lessons', 'status': 'planned'},
    {'id': 'RK-5', 'item': 'Frequently asked questions', 'status': 'partial', 'route': '/educate/'},
    {'id': 'RK-6', 'item': 'Presentation materials', 'status': 'planned', 'route': '/mission-control/education-academy.html'},
    {'id': 'RK-7', 'item': 'Source packets', 'status': 'planned', 'route': '/mission-control/research-library.html'},
]

CONVERSATION_FORMATS = [
    'Living rooms',
    'Libraries',
    'Coffee shops',
    'Community centers',
    'Civic organizations',
    'Faith community meeting spaces',
]

MENTORSHIP_LADDER = [
    {'stage': 1, 'id': 'education_leader', 'title': 'Education Leader', 'status': 'planned'},
    {'stage': 2, 'id': 'neighborhood_mentor', 'title': 'Neighborhood Mentor', 'status': 'planned'},
    {'stage': 3, 'id': 'city_mentor', 'title': 'City Mentor', 'status': 'planned'},
    {'stage': 4, 'id': 'county_mentor', 'title': 'County Mentor', 'status': 'planned'},
    {'stage': 5, 'id': 'regional_mentor', 'title': 'Regional Mentor', 'status': 'planned'},
]

HEALTH_INDICATORS = [
    {'id': 'HI-1', 'indicator': 'Neighborhood activity', 'current': 0, 'status': 'not_started'},
    {'id': 'HI-2', 'indicator': 'Returning participants', 'current': returning_participants, 'status': 'not_started'},
    {'id': 'HI-3', 'indicator': 'Educational event frequency', 'current': events_held, 'status': 'not_started'},
    {'id': 'HI-4', 'indicator': 'Resource usage', 'current': resources_shared, 'status': 'not_started'},
    {'id': 'HI-5', 'indicator': 'Leadership development', 'current': neighborhood_leaders, 'status': 'not_started'},
    {'id': 'HI-6', 'indicator': 'Coalition participation', 'current': orgs, 'status': 'not_started'},
    {'id': 'HI-7', 'indicator': 'Volunteer capacity', 'current': 0, 'status': 'not_started'},
]

PRIVACY_PRINCIPLES = [
    'Avoid collecting unnecessary personal information',
    'Allow participants to control what is shared publicly',
    'Use general geographic identifiers where appropriate',
    'Clearly explain how information is used',
]

SYSTEM_CONNECTIONS = [
    {'system': 'Community Education Academy', 'route': '/mission-control/education-academy.html', 'status': 'partial'},
    {'system': 'Contact Network', 'route': '/mission-control/contact-intelligence.html', 'status': 'partial'},
    {'system': 'Coalition Network', 'route': '/coalition/', 'status': 'planned'},
    {'system': 'County Operating System', 'route': '/mission-control/county-os.html', 'status': 'partial'},
    {'system': 'Event Calendar', 'route': None, 'status': 'planned'},
    {'system': 'Mission Control', 'route': '/mission-control/', 'status': 'live'},
    {'system': 'Resource Library', 'route': '/mission-control/research-library.html', 'status': 'partial'},
    {'system': 'Outreach Engine', 'route': '/mission-control/outreach.html', 'status': 'partial'},
    {'system': 'Statewide Growth (#56)', 'route': '/mission-control/statewide-growth.html', 'status': 'live'},
]

NEIGHBOR_DASHBOARD_METRICS = [
    {'id': 'neighborhoods', 'title': 'Neighborhoods represented', 'current': neighborhoods_represented, 'status': 'live'},
    {'id': 'leaders', 'title': 'Neighborhood Leaders', 'current': neighborhood_leaders, 'status': 'live'},
    {'id': 'conversations', 'title': 'Active conversations', 'current': active_conversations, 'status': 'live'},
    {'id': 'participants', 'title': 'New participants', 'current': participants, 'target': PARTICIPANTS_TARGET, 'status': 'live'},
    {'id': 'events', 'title': 'Educational events', 'current': events_held, 'status': 'live'},
    {'id': 'resources', 'title': 'Resources shared', 'current': resources_shared, 'status': 'live'},
    {'id': 'referrals', 'title': 'Relational referrals', 'current': referrals_tracked, 'status': 'planned'},
]

VISUALIZATION_DIMENSIONS = [
    {'dimension': 'County', 'current': 0, 'target': counties_total, 'status': 'scaffolded'},
    {'dimension': 'City', 'current': 0, 'target': cities_total, 'status': 'scaffolded'},
    {'dimension': 'Neighborhood', 'current': neighborhoods_represented, 'target': 'open', 'status': 'planned'},
    {'dimension': 'Region', 'current': 0, 'target': 7, 'status': 'planned', 'note': '7 Arkansas regions from County OS'},
]

# Readiness: last-mile architecture documented; extends #56; no neighborhoods live
layer_score = 38
relational_score = 8
privacy_score = 10
integration_score = 6
neighborhood_organizing_readiness = min(50, layer_score + relational_score + privacy_score + integration_score)

out_profiles = {
    'version': '1.0',
    'build': 57,
    'updated': today,
    'title': 'Neighborhood Profiles Registry',
    'privacy_note': 'No precise residential information — general geographic identifiers only',
    'summary': {
        'profiles_total': neighborhoods_represented,
        'with_leaders': 0,
        'with_conversations': 0,
        'with_events': 0,
    },
    'profile_schema': {
        'fields': PROFILE_FIELDS,
        'public_fields': [
            'neighborhood_identifier',
            'city',
            'county',
            'leader_count',
            'conversation_count',
            'event_count',
        ],
        'private_fields': [
            'leader_contact',
            'participant_details',
            'precise_location',
        ],
    },
    'neighborhoods': [],
}

out = {
    'version': '1.0',
    'build': 57,
    'updated': today,
    'title': 'Neighborhood Organizing & Relational Network v1.0',
    'subtitle': 'The Last Mile Architecture — Connecting Knowledge to Communities',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/neighborhood-organizing.html',
    'constitution': '/docs/MASTER_NEIGHBORHOOD_ORGANIZING.md',
    'purpose': (
        'Connect the institution with Arkansas neighborhoods through relational organizing '
        'and community education — the largest neighborhood-based civic education network in Arkansas.'
    ),
    'governing_principle': (
        'The institution grows one trusted relationship at a time. The most powerful educational '
        'technology is one informed Arkansan helping another understand reliable evidence.'
    ),
    'vision': (
        'Mission Control shows Arkansas illuminated one neighborhood at a time — not by party or ideology, '
        'but by civic education.'
    ),
    'not_a_political_machine': True,
    'four_geographic_layers': GEOGRAPHIC_LAYERS,
    'neighborhood_education_leaders': {
        'title': 'Neighborhood Education Leaders',
        'role': 'Educators and connectors — not campaign managers',
        'purpose': 'Help neighbors learn',
        'activities': NEIGHBORHOOD_LEADER_ACTIVITIES,
        'current': neighborhood_leaders,
        'status': 'planned',
    },
    'neighborhood_profiles': {
        'title': 'Participating Neighborhood Profiles',
        'registry': '/data/neighborhood-profiles.json',
        'fields': PROFILE_FIELDS,
        'privacy': 'No precise residential information publicly displayed',
        'profiles_count': neighborhoods_represented,
        'status': 'scaffolded',
    },
    'relational_organizing': {
        'title': 'Growth Through Trusted Relationships',
        'principle': 'Spread through existing relationships — not mass messaging alone',
        'pathways': RELATIONAL_PATHWAYS,
        'referrals_tracked': referrals_tracked,
        'status': 'planned',
    },
    'arkansas_neighbor_goal': {
        'title': '200,000 Arkansans Connected',
        'target': PARTICIPANTS_TARGET,
        'current': participants,
        'progress_pct': round((participants / PARTICIPANTS_TARGET) * 100, 4),
        'visualization_dimensions': VISUALIZATION_DIMENSIONS,
        'aligned_with': 'Build #56 Objective Three',
    },
    'neighborhood_resource_kits': {
        'title': 'Neighborhood Resource Kits',
        'emphasis': 'Learning and respectful discussion',
        'items': RESOURCE_KIT_ITEMS,
        'items_ready': sum(1 for i in RESOURCE_KIT_ITEMS if i['status'] in ('live', 'partial')),
        'items_total': len(RESOURCE_KIT_ITEMS),
    },
    'community_conversation_model': {
        'title': 'Intentionally Small Conversations',
        'emphasis': 'Dialogue, questions, and evidence-based learning',
        'formats': CONVERSATION_FORMATS,
        'active_conversations': active_conversations,
        'status': 'planned',
    },
    'neighborhood_dashboard': {
        'title': 'Last Mile Dashboard',
        'subtitle': 'Civic education reach at the neighborhood level',
        'metrics': NEIGHBOR_DASHBOARD_METRICS,
        'illumination_map_status': 'planned',
        'status': 'partial',
    },
    'mentorship_network': {
        'title': 'Leader Mentorship Pathway',
        'flow': 'Education Leader → Neighborhood Mentor → City Mentor → County Mentor → Regional Mentor',
        'stages': MENTORSHIP_LADDER,
        'principle': 'Knowledge grows through personal relationships',
    },
    'community_health_indicators': HEALTH_INDICATORS,
    'privacy_principles': {
        'title': 'Privacy-First Organizing',
        'principles': PRIVACY_PRINCIPLES,
        'status': 'documented',
    },
    'system_connections': SYSTEM_CONNECTIONS,
    'long_term_vision': [
        'Every county has Education Leaders',
        '250 largest cities have active civic education communities',
        'Thousands of neighborhood conversations have taken place',
        '200,000 Arkansans connected through learning and trusted relationships',
        'Civic education at kitchen tables, libraries, community centers, and civic clubs',
    ],
    'mc_integration': {
        'title': 'Last Mile Metrics',
        'status': 'partial',
        'measures_alongside': ['County coverage (#56)', 'City coverage (#56)', 'Neighborhood coverage (#57)'],
        'metrics': NEIGHBOR_DASHBOARD_METRICS,
    },
    'summary': {
        'neighborhoods_represented': neighborhoods_represented,
        'neighborhood_leaders': neighborhood_leaders,
        'active_conversations': active_conversations,
        'participants_current': participants,
        'participants_target': PARTICIPANTS_TARGET,
        'resources_shared': resources_shared,
        'events_held': events_held,
        'referrals_tracked': referrals_tracked,
        'resource_kit_items_ready': sum(1 for i in RESOURCE_KIT_ITEMS if i['status'] in ('live', 'partial')),
        'relational_pathways_live': 0,
        'system_connections_live': sum(1 for s in SYSTEM_CONNECTIONS if s['status'] == 'live'),
        'illumination_map_status': 'planned',
        'neighborhood_organizing_readiness_pct': neighborhood_organizing_readiness,
        'statewide_growth_readiness_pct': sg.get('summary', {}).get('statewide_growth_readiness_pct', 48),
        'public_launch_readiness_pct': ex.get('public_launch_readiness', 8),
    },
    'catalog_gaps': [
        f'0 neighborhoods onboarded — last mile architecture documented only',
        f'0 neighborhood leaders · {edu_leaders} statewide Education Leaders total',
        'Neighborhood illumination map not built — MC tables only',
        'Relational referral tracking not implemented — 0 pathways live',
        'Neighborhood profiles registry empty — schema defined',
        'Resource kit 2/7 partial — no dedicated neighborhood kit bundle',
        'Event calendar not built — conversation scheduling manual',
        'Privacy controls documented — no participant visibility settings in schema',
        'Mentorship ladder 0/5 operational — no mentor matching',
        'Unify Build #56 leadership ladder with Build #57 mentorship pathway',
    ],
    'recommended_next_build': {
        'number': 58,
        'title': 'Implementation Translation Layer & Engineering Artifacts',
        'note': (
            'Neon schema for neighborhoods, referrals, and privacy fields; relational graph edges; '
            'route inventory, COMP-* specs, API contracts, GitHub issue backlog.'
        ),
    },
}

with open(root / 'data/neighborhood-profiles.json', 'w', newline='\n') as f:
    json.dump(out_profiles, f, indent=2)
    f.write('\n')

with open(root / 'data/neighborhood-organizing.json', 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')

print(
    f'Neighborhood Organizing: {neighborhoods_represented} neighborhoods, '
    f'{neighborhood_leaders} leaders, {participants} participants, '
    f'{neighborhood_organizing_readiness}% readiness'
)
