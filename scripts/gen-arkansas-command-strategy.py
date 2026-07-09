"""
Generate data/arkansas-command-strategy.json — Build #70.
Master Arkansas Command Strategy v1.0.
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
aan = load_json(root / 'data/arkansas-action-network.json')
rog = load_json(root / 'data/relational-organizing-growth-engine.json')
cos = load_json(root / 'data/county-operating-system.json')
cities = load_json(root / 'data/arkansas-cities.json')
counties = load_json(root / 'data/arkansas-counties.json')

ex = mc.get('executive', {})
COUNTIES_TARGET = counties.get('counties_total', 75)
CITIES_TARGET = cities.get('cities_total', 250)
PARTICIPANTS_TARGET = 200_000
REGIONS_TARGET = len(cos.get('regions', [])) or 7

# Honest zeros
counties_with_leaders = counties.get('summary', {}).get('counties_with_educators', 0)
cities_with_leaders = cities.get('summary', {}).get('cities_with_education_leaders', 0)
connected_arkansans = aan.get('summary', {}).get('connected_arkansans', 0)
education_leaders = aan.get('summary', {}).get('education_leaders', 0)
county_teams = aan.get('summary', {}).get('county_teams', 0)
city_teams = aan.get('summary', {}).get('city_teams', 0)
regional_mentors = 0
counties_past_awareness = 0
cities_with_sustained_activity = 0
monthly_targets_tracked = 0
growth_dashboard_live = False
current_phase = 1
current_phase_title = 'Build the Core'

STATEWIDE_OBJECTIVES = [
    {
        'id': 'ACS-O1',
        'number': 1,
        'title': 'Every County',
        'description': '75 of 75 counties with active educational leadership',
        'current': counties_with_leaders,
        'target': COUNTIES_TARGET,
        'status': 'scaffolded',
    },
    {
        'id': 'ACS-O2',
        'number': 2,
        'title': 'Every Major City',
        'description': 'Educational teams in the 250 largest Arkansas cities',
        'current': cities_with_leaders,
        'target': CITIES_TARGET,
        'status': 'scaffolded',
    },
    {
        'id': 'ACS-O3',
        'number': 3,
        'title': '200,000 Connected Arkansans',
        'description': 'Voluntary network committed to ongoing civic education',
        'current': connected_arkansans,
        'target': PARTICIPANTS_TARGET,
        'status': 'scaffolded',
    },
]

EXPANSION_PYRAMID = [
    'Research', 'Website', 'Learners', 'Education Leaders',
    'Neighborhood Teams', 'City Teams', 'County Teams',
    'Regional Networks', 'Statewide Institution',
]

EXECUTION_PHASES = [
    {
        'phase': 1,
        'id': 'build_core',
        'title': 'Build the Core',
        'objectives': [
            'Launch platform', 'Publish curriculum', 'Complete Mission Control',
            'Launch Community Education Academy', 'Recruit founding Education Leaders',
        ],
        'success_metric': 'The institution is operational',
        'status': 'in_progress',
    },
    {
        'phase': 2,
        'id': 'county_anchors',
        'title': 'County Anchors',
        'goal': 'Recruit at least one Education Leader in every county',
        'priority': 'Coverage over density',
        'mc_displays': 'Counties without representation',
        'status': 'planned',
    },
    {
        'phase': 3,
        'id': 'city_expansion',
        'title': 'City Expansion',
        'goal': 'Establish Education Leaders in the 250 largest cities',
        'priority': 'Local visibility, community conversations, partnership development',
        'mc_displays': 'City readiness',
        'status': 'planned',
    },
    {
        'phase': 4,
        'id': 'neighborhood_growth',
        'title': 'Neighborhood Growth',
        'goal': 'Develop neighborhood learning networks',
        'focus': ['Living rooms', 'Libraries', 'Coffee shops', 'Community centers'],
        'method': 'Small-group conversations as primary growth method',
        'status': 'planned',
    },
    {
        'phase': 5,
        'id': 'leadership_multiplication',
        'title': 'Leadership Multiplication',
        'goal': 'Every leader mentors another; institution becomes self-replicating',
        'status': 'planned',
    },
]

COUNTY_READINESS_STAGES = [
    {'stage': 1, 'id': 'awareness', 'title': 'Awareness', 'counties_at_stage': 0},
    {'stage': 2, 'id': 'leader_identified', 'title': 'Education Leader identified', 'counties_at_stage': 0},
    {'stage': 3, 'id': 'conversations', 'title': 'Community conversations occurring', 'counties_at_stage': 0},
    {'stage': 4, 'id': 'coalition', 'title': 'Coalition organizations participating', 'counties_at_stage': 0},
    {'stage': 5, 'id': 'sustainable_team', 'title': 'Sustainable county education team', 'counties_at_stage': 0},
]

CITY_READINESS_STAGES = [
    {'stage': 1, 'id': 'interested_learners', 'title': 'Interested learners', 'cities_at_stage': 0},
    {'stage': 2, 'id': 'education_leader', 'title': 'Education Leader', 'cities_at_stage': 0},
    {'stage': 3, 'id': 'conversations', 'title': 'Community conversations', 'cities_at_stage': 0},
    {'stage': 4, 'id': 'coalition_partnerships', 'title': 'Coalition partnerships', 'cities_at_stage': 0},
    {'stage': 5, 'id': 'educational_calendar', 'title': 'Educational calendar', 'cities_at_stage': 0},
    {'stage': 6, 'id': 'sustained_activity', 'title': 'Sustained local activity', 'cities_at_stage': 0},
]

GROWTH_CHANNELS = [
    'Education Leaders', 'Community conversations', 'Coalition partners',
    'Libraries', 'Universities', 'Community organizations',
    'Social media', 'Relational organizing', 'Word of mouth',
]

MONTHLY_TARGETS = [
    {'id': 'ACS-M1', 'metric': 'New Education Leaders', 'current': education_leaders, 'status': 'planned'},
    {'id': 'ACS-M2', 'metric': 'County coverage', 'current': counties_with_leaders, 'target': COUNTIES_TARGET, 'status': 'planned'},
    {'id': 'ACS-M3', 'metric': 'City coverage', 'current': cities_with_leaders, 'target': CITIES_TARGET, 'status': 'planned'},
    {'id': 'ACS-M4', 'metric': 'Community conversations', 'current': 0, 'status': 'planned'},
    {'id': 'ACS-M5', 'metric': 'Academy graduates', 'current': 0, 'status': 'planned'},
    {'id': 'ACS-M6', 'metric': 'Coalition organizations', 'current': 0, 'status': 'planned'},
    {'id': 'ACS-M7', 'metric': 'Participant growth', 'current': connected_arkansans, 'status': 'planned'},
    {'id': 'ACS-M8', 'metric': 'Research published', 'current': 0, 'status': 'planned'},
    {'id': 'ACS-M9', 'metric': 'Content completed', 'current': 0, 'status': 'planned'},
    {'id': 'ACS-M10', 'metric': 'Technology milestones', 'current': 0, 'status': 'planned'},
]

REGIONS = [
    {
        'id': r['id'],
        'title': r['title'],
        'regional_mentor': 0,
        'county_leaders': 0,
        'city_leaders': 0,
        'coalition_orgs': 0,
        'status': r.get('status', 'defined'),
    }
    for r in cos.get('regions', [])
]

ARKANSAS_FLYWHEEL = [
    'Research', 'Educational Resources', 'Learning', 'Education Leaders',
    'Community Conversations', 'New Learners', 'Coalition Growth', 'More Research',
]

GROWTH_DASHBOARD_INDICATORS = [
    {'id': 'ACS-D1', 'indicator': '75 County Goal', 'current': counties_with_leaders, 'target': COUNTIES_TARGET, 'status': 'planned'},
    {'id': 'ACS-D2', 'indicator': '250 City Goal', 'current': cities_with_leaders, 'target': CITIES_TARGET, 'status': 'planned'},
    {'id': 'ACS-D3', 'indicator': '200,000 Participant Goal', 'current': connected_arkansans, 'target': PARTICIPANTS_TARGET, 'status': 'planned'},
    {'id': 'ACS-D4', 'indicator': 'Neighborhood Growth', 'current': 0, 'status': 'planned'},
    {'id': 'ACS-D5', 'indicator': 'Leadership Pipeline', 'current': education_leaders, 'status': 'planned'},
    {'id': 'ACS-D6', 'indicator': 'Academy Growth', 'current': 0, 'status': 'planned'},
    {'id': 'ACS-D7', 'indicator': 'Coalition Growth', 'current': 0, 'status': 'planned'},
    {'id': 'ACS-D8', 'indicator': 'Regional Health', 'current': regional_mentors, 'target': REGIONS_TARGET, 'status': 'planned'},
    {'id': 'ACS-D9', 'indicator': 'Institutional Readiness', 'current': ex.get('public_launch_readiness', 8), 'unit': '%', 'status': 'partial'},
    {'id': 'ACS-D10', 'indicator': 'Projected Completion Timeline', 'current': 'not_modeled', 'status': 'planned'},
]

ANNUAL_GOALS = [
    'Increase county coverage', 'Increase city leadership', 'Improve curriculum',
    'Expand coalition', 'Grow Academy enrollment', 'Strengthen research',
    'Improve Educational Coverage Scores',
]

SYSTEM_CONNECTIONS = [
    {'system': 'Statewide Growth (#56)', 'route': '/mission-control/statewide-growth.html', 'status': 'live', 'note': 'Objectives foundation'},
    {'system': 'Arkansas Action Network (#64)', 'route': '/mission-control/arkansas-action-network.html', 'status': 'live', 'note': 'Leadership pyramid'},
    {'system': 'Relational Organizing (#69)', 'route': '/mission-control/relational-organizing-growth-engine.html', 'status': 'live', 'note': 'Primary expansion'},
    {'system': 'Citizen Leadership Academy (#68)', 'route': '/mission-control/citizen-leadership-academy.html', 'status': 'live'},
    {'system': 'Neighborhood Organizing (#57)', 'route': '/mission-control/neighborhood-organizing.html', 'status': 'live'},
    {'system': 'Coalition Network (#61)', 'route': '/mission-control/coalition-network.html', 'status': 'live'},
    {'system': 'Civic Atlas (#58)', 'route': '/mission-control/civic-atlas.html', 'status': 'live', 'note': 'County/city maps'},
    {'system': 'County OS (#31)', 'route': '/mission-control/county-os.html', 'status': 'live', 'note': '7 regions'},
    {'system': 'Impact Measurement (#67)', 'route': '/mission-control/impact-measurement.html', 'status': 'live'},
    {'system': 'Mission Control', 'route': '/mission-control/', 'status': 'live'},
]

arkansas_command_strategy_readiness = min(
    42,
    12 + len(EXECUTION_PHASES) * 3 + len(STATEWIDE_OBJECTIVES) * 2 + 6,
)

out = {
    'version': '1.0',
    'build': 70,
    'updated': today,
    'title': 'Master Arkansas Command Strategy v1.0',
    'subtitle': 'The Road to 75 Counties, 250 Cities & 200,000 Arkansans',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/arkansas-command-strategy.html',
    'constitution': '/docs/MASTER_ARKANSAS_COMMAND_STRATEGY.md',
    'purpose': (
        'Statewide execution strategy — how to reach every county, every major city, '
        'and 200,000 Arkansans without losing quality.'
    ),
    'governing_principle': (
        'Grow deliberately — trustworthy research produces excellent education, '
        'confident leaders strengthen communities, communities invite others to learn. '
        'One county, city, neighborhood, conversation, and Arkansan at a time.'
    ),
    'not_advertising_pressure_campaigning': True,
    'statewide_execution_playbook': True,
    'central_question': (
        'Exactly how do we reach every county, every major city, and 200,000 Arkansans '
        'without losing quality?'
    ),
    'statewide_objectives': STATEWIDE_OBJECTIVES,
    'expansion_pyramid': {
        'title': 'The Expansion Pyramid',
        'layers': EXPANSION_PYRAMID,
        'principle': 'Every layer strengthens the next',
        'status': 'specified',
    },
    'execution_phases': {
        'title': 'Five Execution Phases',
        'current_phase': current_phase,
        'current_phase_title': current_phase_title,
        'phases': EXECUTION_PHASES,
    },
    'county_readiness_model': {
        'title': 'County Readiness Model',
        'stages': COUNTY_READINESS_STAGES,
        'counties_past_awareness': counties_past_awareness,
        'mc_displays_all_counties': True,
        'status': 'planned',
    },
    'city_readiness_model': {
        'title': 'City Readiness Model',
        'stages': CITY_READINESS_STAGES,
        'cities_with_sustained_activity': cities_with_sustained_activity,
        'mc_visualizes_maturity': True,
        'status': 'planned',
    },
    'participant_growth_model': {
        'title': 'The 200,000 Arkansas Model',
        'target': PARTICIPANTS_TARGET,
        'current': connected_arkansans,
        'channels': GROWTH_CHANNELS,
        'no_single_channel': True,
        'status': 'scaffolded',
    },
    'monthly_operational_targets': {
        'title': 'Monthly Operational Targets',
        'targets': MONTHLY_TARGETS,
        'targets_tracked': monthly_targets_tracked,
        'status': 'planned',
    },
    'regional_strategy': {
        'title': 'Regional Strategy',
        'regions_total': REGIONS_TARGET,
        'regions': REGIONS,
        'regional_mentors': regional_mentors,
        'components': [
            'Regional Mentor', 'County Leaders', 'City Leaders',
            'Coalition relationships', 'Educational calendar',
        ],
        'status': 'defined',
    },
    'arkansas_flywheel': {
        'title': 'The Arkansas Flywheel',
        'cycle': ARKANSAS_FLYWHEEL,
        'principle': 'Each cycle strengthens the next',
        'status': 'specified',
    },
    'growth_dashboard': {
        'title': 'Mission Control Growth Dashboard',
        'primary_statewide_dashboard': True,
        'live': growth_dashboard_live,
        'indicators': GROWTH_DASHBOARD_INDICATORS,
        'status': 'planned',
    },
    'annual_goals': {
        'title': 'Annual Arkansas Goals',
        'goals': ANNUAL_GOALS,
        'maturity_over_raw_growth': True,
        'status': 'planned',
    },
    'integration': {
        'chain': (
            'Statewide Growth → Action Network → Relational Organizing → '
            'Leadership Academy → Coalition → Civic Atlas → Mission Control'
        ),
        'systems': SYSTEM_CONNECTIONS,
        'extends': 'Statewide Growth Blueprint (#56) — adds operational phases, readiness models, monthly targets',
    },
    'long_term_vision': (
        'Every county represented; every major city has active Education Leaders; '
        'weekly conversations statewide; 200,000+ voluntarily connected; platform is '
        'Arkansas civic education infrastructure. Local leaders develop local leaders.'
    ),
    'summary': {
        'counties_with_leaders': counties_with_leaders,
        'counties_target': COUNTIES_TARGET,
        'cities_with_leaders': cities_with_leaders,
        'cities_target': CITIES_TARGET,
        'connected_arkansans': connected_arkansans,
        'connected_target': PARTICIPANTS_TARGET,
        'education_leaders': education_leaders,
        'county_teams': county_teams,
        'city_teams': city_teams,
        'regional_mentors': regional_mentors,
        'regions_target': REGIONS_TARGET,
        'current_execution_phase': current_phase,
        'monthly_targets_tracked': monthly_targets_tracked,
        'growth_dashboard_live': growth_dashboard_live,
        'arkansas_command_strategy_readiness_pct': arkansas_command_strategy_readiness,
        'statewide_growth_readiness_pct': sg.get('summary', {}).get('statewide_growth_readiness_pct', 48),
        'public_launch_readiness_pct': ex.get('public_launch_readiness', 8),
    },
    'catalog_gaps': [
        f'0/{COUNTIES_TARGET} counties with Education Leaders — Phase Two not started',
        f'0/{CITIES_TARGET} cities with teams — Phase Three not started',
        f'0/{PARTICIPANTS_TARGET:,} connected — participant tracking not operational',
        'County readiness model specified — 0 counties past Awareness stage',
        'City readiness model specified — 0 cities with sustained activity',
        '0 monthly operational targets tracked — no pacing dashboard',
        'Growth dashboard planned — not live as primary statewide view',
        f'0/{REGIONS_TARGET} regional mentors assigned',
        'Phase One in progress — institution not fully operational (8% launch readiness)',
        'Build #70 vs Build #56 Statewide Growth — reconcile command vs blueprint roles?',
        'Build #70 vs Build #64 Action Network — unify county/city team metrics?',
        'Projected completion timeline not modeled',
        'Annual goals specified — no year-over-year tracking UI',
    ],
    'recommended_next_build': {
        'number': 71,
        'title': 'Implementation Translation Layer & Engineering Artifacts',
        'note': (
            'County/city readiness UI, monthly target tracking, growth dashboard components, '
            'regional maps, flywheel metrics, route inventory, COMP-* specs, GitHub backlog.'
        ),
    },
}

with open(root / 'data/arkansas-command-strategy.json', 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')

print(
    f'Arkansas Command Strategy: {counties_with_leaders}/{COUNTIES_TARGET} counties, '
    f'{cities_with_leaders}/{CITIES_TARGET} cities, '
    f'{connected_arkansans}/{PARTICIPANTS_TARGET} connected, '
    f'phase {current_phase}, {arkansas_command_strategy_readiness}% readiness'
)
