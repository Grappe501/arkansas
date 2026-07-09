"""
Generate data/arkansas-city-operating-system.json — Build #78.
Master Arkansas City Operating System (ArCOS) v1.0.
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
acos = load_json(root / 'data/arkansas-county-operating-system.json')
acs = load_json(root / 'data/arkansas-command-strategy.json')
cities_data = load_json(root / 'data/arkansas-cities.json')

ex = mc.get('executive', {})
CITIES_TOTAL = cities_data.get('cities_total', 250)

# Honest zeros
cities_scaffolded = len(cities_data.get('cities', [])) or CITIES_TOTAL
cities_with_digital_twin = 0
city_dashboards_live = 0
cities_past_initial_interest = 0
cities_at_level = {i: 0 for i in range(1, 7)}
cities_at_level[1] = CITIES_TOTAL
city_health_index_computed = False
city_listening_reports_submitted = 0
city_event_calendars_live = 0
city_resource_centers_live = 0
city_collaboration_pairs = 0
county_statewide_calendar_sync = False

CITY_PHILOSOPHY_QUESTIONS = [
    'Who are our Education Leaders?',
    'What organizations are helping educate the community?',
    'Where are conversations taking place?',
    'What educational events are scheduled?',
    'What questions are local residents asking?',
    'What progress have we made this year?',
]

DIGITAL_TWIN_SECTIONS = [
    {'id': 'ArCOS-DT-01', 'section': 'City overview', 'status': 'specified'},
    {'id': 'ArCOS-DT-02', 'section': 'Leadership team', 'status': 'specified'},
    {'id': 'ArCOS-DT-03', 'section': 'Community calendar', 'status': 'specified'},
    {'id': 'ArCOS-DT-04', 'section': 'Educational resources', 'status': 'specified'},
    {'id': 'ArCOS-DT-05', 'section': 'Coalition partners', 'status': 'partial'},
    {'id': 'ArCOS-DT-06', 'section': 'Progress dashboard', 'status': 'planned'},
    {'id': 'ArCOS-DT-07', 'section': 'Local news and updates', 'status': 'specified'},
    {'id': 'ArCOS-DT-08', 'section': 'Community learning history', 'status': 'planned'},
]

LEADERSHIP_ROLES = [
    {'id': 'ArCOS-LR-01', 'role': 'City Education Leader', 'filled': 0, 'status': 'specified'},
    {'id': 'ArCOS-LR-02', 'role': 'Neighborhood Leaders', 'filled': 0, 'status': 'specified'},
    {'id': 'ArCOS-LR-03', 'role': 'Academy Mentor', 'filled': 0, 'status': 'specified'},
    {'id': 'ArCOS-LR-04', 'role': 'Community Conversation Coordinator', 'filled': 0, 'status': 'specified'},
    {'id': 'ArCOS-LR-05', 'role': 'Coalition Liaison', 'filled': 0, 'status': 'specified'},
    {'id': 'ArCOS-LR-06', 'role': 'Volunteer Coordinator', 'filled': 0, 'status': 'specified'},
    {'id': 'ArCOS-LR-07', 'role': 'Media & Communications Volunteer', 'filled': 0, 'status': 'specified'},
]

CITY_GOAL_EXAMPLES = [
    'Recruit additional Education Leaders',
    'Increase Academy participation',
    'Host monthly community conversations',
    'Develop new coalition partnerships',
    'Expand neighborhood representation',
    'Share educational resources more broadly',
]

CITY_DASHBOARD = {
    'title': 'City Dashboard',
    'domains': [
        {
            'id': 'ArCOS-CD-L',
            'domain': 'Leadership',
            'indicators': ['Education Leaders', 'Mentors', 'Academy graduates'],
            'status': 'planned',
        },
        {
            'id': 'ArCOS-CD-C',
            'domain': 'Community',
            'indicators': ['Conversations', 'Events', 'Volunteer activity', 'Organizations'],
            'status': 'planned',
        },
        {
            'id': 'ArCOS-CD-LN',
            'domain': 'Learning',
            'indicators': ['Course completion', 'Resource usage', 'Presentation activity'],
            'status': 'planned',
        },
        {
            'id': 'ArCOS-CD-G',
            'domain': 'Growth',
            'indicators': ['Participant growth', 'Neighborhood expansion', 'Coalition participation'],
            'status': 'planned',
        },
    ],
    'live': False,
    'status': 'specified',
}

RESOURCE_CENTER = [
    'Presentation slide decks',
    'Fact sheets',
    'Community discussion guides',
    'Printable handouts',
    'Educational videos',
    'Frequently asked questions',
    'Arkansas-specific resource packets',
]

EVENT_CALENDAR_TYPES = [
    'Community conversations',
    'Academy sessions',
    'Coalition meetings',
    'Volunteer events',
    'Public presentations',
    'Educational workshops',
]

NEIGHBORHOOD_INTEGRATION = [
    'Neighborhoods represented',
    'Neighborhood Leaders',
    'Learning circles',
    'Community conversations',
    'Volunteer opportunities',
    'Educational coverage',
]

LISTENING_REPORT_ITEMS = [
    'Frequently asked questions',
    'Community educational needs',
    'Emerging issues',
    'Resource requests',
    'Success stories',
]

READINESS_LEVELS = [
    {'level': 1, 'id': 'initial_interest', 'title': 'Initial interest', 'cities_at_level': cities_at_level[1]},
    {'level': 2, 'id': 'founding_leader', 'title': 'Founding Education Leader', 'cities_at_level': cities_at_level[2]},
    {'level': 3, 'id': 'leadership_team', 'title': 'Leadership Team', 'cities_at_level': cities_at_level[3]},
    {'level': 4, 'id': 'regular_conversations', 'title': 'Regular Community Conversations', 'cities_at_level': cities_at_level[4]},
    {'level': 5, 'id': 'coalition_partnerships', 'title': 'Strong Coalition Partnerships', 'cities_at_level': cities_at_level[5]},
    {'level': 6, 'id': 'sustainable_network', 'title': 'Sustainable City Civic Education Network', 'cities_at_level': cities_at_level[6]},
]

HEALTH_INDEX_FACTORS = [
    'Leadership strength',
    'Volunteer engagement',
    'Academy participation',
    'Community activity',
    'Coalition participation',
    'Neighborhood coverage',
    'Educational resource usage',
    'Participant retention',
]

COLLABORATION_TYPES = [
    'Joint workshops',
    'Shared presentations',
    'Leadership exchanges',
    'Mentorship',
    'Resource sharing',
]

SYSTEM_CONNECTIONS = [
    {'system': 'Mission Control', 'route': '/mission-control/', 'status': 'live'},
    {'system': 'Arkansas County OS (#77)', 'route': '/mission-control/arkansas-county-operating-system.html', 'status': 'live'},
    {'system': 'Arkansas Civic Atlas (#58)', 'route': '/mission-control/civic-atlas.html', 'status': 'live'},
    {'system': 'Community Education Academy (#68)', 'route': '/mission-control/citizen-leadership-academy.html', 'status': 'live'},
    {'system': 'Coalition Network (#61)', 'route': '/mission-control/coalition-network.html', 'status': 'live'},
    {'system': 'Relationship Operating System (#59)', 'route': '/mission-control/relationship-os.html', 'status': 'live'},
    {'system': 'Citizen Action Center (#62)', 'route': '/mission-control/citizen-action-center.html', 'status': 'live'},
    {'system': 'Knowledge Graph', 'route': '/mission-control/knowledge-graph.html', 'status': 'live'},
    {'system': 'Neighborhood Organizing (#57)', 'route': '/mission-control/neighborhood-organizing.html', 'status': 'live'},
    {'system': 'Arkansas Command Strategy (#70)', 'route': '/mission-control/arkansas-command-strategy.html', 'status': 'live'},
    {'system': 'Statewide Growth (#56)', 'route': '/mission-control/statewide-growth.html', 'status': 'live'},
]

arcity_readiness = min(
    48,
    15
    + len(READINESS_LEVELS) * 2
    + len(DIGITAL_TWIN_SECTIONS) // 2
    + len(LEADERSHIP_ROLES)
    + len(CITY_DASHBOARD['domains'])
    + len(NEIGHBORHOOD_INTEGRATION) // 2
    + len(HEALTH_INDEX_FACTORS) // 2,
)

out = {
    'version': '1.0',
    'build': 78,
    'updated': today,
    'title': 'Master Arkansas City Operating System (ArCOS) v1.0',
    'subtitle': 'Two Hundred Fifty Cities. One Shared Mission.',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/arkansas-city-operating-system.html',
    'constitution': '/docs/MASTER_ARKANSAS_CITY_OPERATING_SYSTEM.md',
    'purpose': (
        'Repeatable framework for civic education teams in the 250 largest Arkansas cities — '
        'operational bridge between county leadership and neighborhood relationships.'
    ),
    'governing_principle': (
        'Counties provide structure. Neighborhoods provide trust. Cities provide connection. '
        'Civic understanding grows through local relationships.'
    ),
    'city_philosophy': {
        'title': 'Institutional Philosophy',
        'every_city_active_learning_community': True,
        'questions': CITY_PHILOSOPHY_QUESTIONS,
    },
    'city_digital_twin': {
        'title': 'City Digital Twin',
        'description': 'Digital workspace — operational headquarters for each participating city',
        'cities_total': CITIES_TOTAL,
        'digital_twins_operational': cities_with_digital_twin,
        'sections': DIGITAL_TWIN_SECTIONS,
        'sections_total': len(DIGITAL_TWIN_SECTIONS),
        'status': 'specified',
    },
    'city_leadership_team': {
        'title': 'City Leadership Team',
        'roles_total': len(LEADERSHIP_ROLES),
        'one_person_multiple_roles_initially': True,
        'roles': LEADERSHIP_ROLES,
    },
    'city_goals': {
        'title': 'City Goals',
        'annual_measurable_objectives': True,
        'examples': CITY_GOAL_EXAMPLES,
        'mc_tracks_progress': True,
        'status': 'specified',
    },
    'city_dashboard': CITY_DASHBOARD,
    'city_resource_center': {
        'title': 'City Resource Center',
        'items': RESOURCE_CENTER,
        'items_total': len(RESOURCE_CENTER),
        'statewide_consistent_local_customization': True,
        'live': city_resource_centers_live > 0,
        'status': 'specified',
    },
    'city_calendar': {
        'title': 'City Calendar',
        'event_types': EVENT_CALENDAR_TYPES,
        'syncs_with_county_and_statewide': county_statewide_calendar_sync,
        'live': city_event_calendars_live > 0,
        'status': 'specified',
    },
    'neighborhood_integration': {
        'title': 'Neighborhood Integration',
        'cities_as_neighborhood_hubs': True,
        'visualizations': NEIGHBORHOOD_INTEGRATION,
        'status': 'specified',
    },
    'city_listening_reports': {
        'title': 'City Listening Reports',
        'items': LISTENING_REPORT_ITEMS,
        'reports_submitted': city_listening_reports_submitted,
        'mc_aggregates_statewide': True,
        'status': 'specified',
    },
    'city_readiness_levels': {
        'title': 'City Readiness Levels',
        'levels_total': len(READINESS_LEVELS),
        'levels': READINESS_LEVELS,
        'cities_past_initial_interest': cities_past_initial_interest,
        'mc_displays_all_cities': True,
        'status': 'specified',
        'note': '6-stage model; extends Command Strategy (#70) city readiness model',
    },
    'city_health_index': {
        'title': 'City Health Index',
        'factors': HEALTH_INDEX_FACTORS,
        'factors_total': len(HEALTH_INDEX_FACTORS),
        'computed': city_health_index_computed,
        'prioritizes_support_and_recognizes_progress': True,
        'status': 'planned',
    },
    'city_collaboration': {
        'title': 'City-to-City Collaboration',
        'cities_learn_from_one_another': True,
        'types': COLLABORATION_TYPES,
        'pairs_active': city_collaboration_pairs,
        'horizontal_spread': True,
        'status': 'specified',
    },
    'integration': {
        'chain': (
            'Mission Control → ACOS (#77) → Civic Atlas → Education Academy → '
            'Coalition Network → Relationship OS → Citizen Action Center → Knowledge Graph'
        ),
        'cities_practical_center_of_activity': True,
        'bridge_county_to_neighborhood': True,
        'systems': SYSTEM_CONNECTIONS,
    },
    'long_term_vision': (
        'Ten to fifteen years after launch: 250 largest cities each have active Education Leaders; '
        'community conversations year-round; libraries, civic organizations, colleges, and volunteers '
        'collaborate locally; neighborhood leaders supported by city teams. Resilient network of '
        'local civic education communities connected to unified statewide institution.'
    ),
    'summary': {
        'cities_total': CITIES_TOTAL,
        'cities_scaffolded': cities_scaffolded,
        'cities_with_digital_twin': cities_with_digital_twin,
        'city_dashboards_live': city_dashboards_live,
        'cities_past_initial_interest': cities_past_initial_interest,
        'readiness_levels': len(READINESS_LEVELS),
        'digital_twin_sections': len(DIGITAL_TWIN_SECTIONS),
        'leadership_roles': len(LEADERSHIP_ROLES),
        'city_health_index_computed': city_health_index_computed,
        'city_listening_reports_submitted': city_listening_reports_submitted,
        'city_collaboration_pairs': city_collaboration_pairs,
        'arkansas_city_operating_system_readiness_pct': arcity_readiness,
        'arkansas_county_operating_system_readiness_pct': acos.get('summary', {}).get('arkansas_county_operating_system_readiness_pct', 47),
        'arkansas_command_strategy_readiness_pct': acs.get('summary', {}).get('arkansas_command_strategy_readiness_pct', 39),
        'public_launch_readiness_pct': ex.get('public_launch_readiness', 8),
    },
    'catalog_gaps': [
        '0/250 city digital twins operational — MC generation not implemented',
        '0 cities past initial interest — no founding Education Leaders',
        '0 city dashboards live — operational headquarters not built',
        'City Health Index not computed — factors specified only',
        'City listening reports — 0 submitted; aggregation not live',
        'City calendars — not per-city; county/statewide sync off',
        'City resource centers — not per-city',
        'Neighborhood integration visualizations — not on city dashboards',
        '6-stage ArCOS vs Command Strategy city model — reconcile?',
        'Build #78 vs Statewide Growth (#56) 250-city index — unify routes?',
        'City-to-city collaboration — 0 pairs',
        'County field null on city records — geographic linkage incomplete',
        'Canonical /arkansas/[city] routes not built',
    ],
    'recommended_next_build': {
        'number': 79,
        'title': 'Implementation Translation Layer & Engineering Artifacts',
        'note': (
            'City digital twin pages, readiness visualization, health index, '
            'neighborhood integration UI, calendar sync, COMP-* specs, GitHub backlog.'
        ),
    },
}

with open(root / 'data/arkansas-city-operating-system.json', 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')

print(
    f'ArCOS: {cities_scaffolded}/{CITIES_TOTAL} scaffolded, '
    f'{cities_with_digital_twin} digital twins, {arcity_readiness}% readiness'
)
