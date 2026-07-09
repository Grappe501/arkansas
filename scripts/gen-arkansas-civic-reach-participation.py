"""
Generate data/arkansas-civic-reach-participation.json — Build #86.
Master Arkansas Civic Reach & Participation Strategy v1.0.
"""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
today = '2026-07-09'

CONNECTED_CITIZEN_GOAL_PCT = 15


def load_json(path):
    if path.exists():
        with open(path, encoding='utf-8') as f:
            return json.load(f)
    return {}


mc = load_json(root / 'data/mission-control.json')
counties = load_json(root / 'data/arkansas-counties.json')
cities = load_json(root / 'data/arkansas-cities.json')
mlp = load_json(root / 'data/master-launch-plan.json')

ex = mc.get('executive', {})

# Honest zeros
reach_dashboard_live = False
statewide_connected_participants = 0
statewide_registered_voters = 0
registered_voters_tracked = False
statewide_civic_reach_pct = 0
counties_at_goal = 0
cities_at_goal = 0
counties_total = counties.get('counties_total', 75)
cities_total = cities.get('cities_total', 250) if cities else 250
growth_this_month = 0
growth_this_year = 0
projected_completion_year = None

CONNECTION_TYPES = [
    'Email updates', 'Text message updates', 'Mobile app notifications',
    'Website accounts', 'Academy participation', 'Community conversations',
    'Event registration', 'Coalition involvement',
]

ENGAGEMENT_LEVELS = [
    {'level': 1, 'title': 'Receive updates', 'description': 'Stay connected via preferred channel'},
    {'level': 2, 'title': 'Read educational resources', 'description': 'Active learner'},
    {'level': 3, 'title': 'Attend community conversations', 'description': 'Local dialogue participant'},
    {'level': 4, 'title': 'Complete Academy learning', 'description': 'Structured civic education'},
    {'level': 5, 'title': 'Volunteer', 'description': 'Institutional contributor'},
    {'level': 6, 'title': 'Become an Education Leader', 'description': 'Community educator multiplier'},
]

COUNTY_OBJECTIVES = [
    'Registered voters', 'Connected participants', 'Education Leaders',
    'Neighborhood Leaders', 'Academy participants', 'Community conversations',
    'Coalition organizations', 'Volunteer growth',
]

CITY_OBJECTIVES = [
    'Registered voters', 'Connected participants', 'Educational events',
    'Learning circles', 'Volunteer activity', 'Leadership development',
    'Progress toward 15% Connected Citizen Goal',
]

REACH_DASHBOARD_ITEMS = [
    {'id': 'CR-D01', 'indicator': 'Statewide Connected Participants', 'current': statewide_connected_participants, 'status': 'planned'},
    {'id': 'CR-D02', 'indicator': 'County Reach Percentages', 'current': 0, 'unit': 'counties tracked', 'status': 'planned'},
    {'id': 'CR-D03', 'indicator': 'City Reach Percentages', 'current': 0, 'unit': 'cities tracked', 'status': 'planned'},
    {'id': 'CR-D04', 'indicator': 'Progress toward 15% by county', 'current': counties_at_goal, 'target': counties_total, 'status': 'planned'},
    {'id': 'CR-D05', 'indicator': 'Progress toward 15% by city', 'current': cities_at_goal, 'target': cities_total, 'status': 'planned'},
    {'id': 'CR-D06', 'indicator': 'Growth this month', 'current': growth_this_month, 'status': 'planned'},
    {'id': 'CR-D07', 'indicator': 'Growth this year', 'current': growth_this_year, 'status': 'planned'},
    {'id': 'CR-D08', 'indicator': 'Projected completion', 'current': projected_completion_year or 'Not computed', 'status': 'planned'},
]

GROWTH_STRATEGIES = [
    'Neighborhood conversations', 'Education Leaders', 'Community organizations',
    'Libraries', 'Colleges', 'Historical societies', 'Relational organizing',
    'Volunteer referrals', 'Social media', 'Educational presentations',
]

QUALITY_METRICS = [
    'Returning visitors', 'Lesson completion', 'Newsletter engagement',
    'Event attendance', 'Academy progress', 'Volunteer participation', 'Leadership development',
]

ETHICAL_STANDARDS = [
    'Voluntary', 'Transparent', 'Privacy-respecting',
    'Easy to manage', 'Easy to unsubscribe from',
]

FOUNDERS_STANDARD = (
    'Build an informed audience, not merely a large one. If the institution earns trust of '
    'at least 15% of registered voters in every county and major city — people who voluntarily '
    'stay connected for thoughtful, evidence-based civic education — it creates one of the '
    'strongest civic education networks in Arkansas history.'
)

SYSTEM_CONNECTIONS = [
    {'system': 'Mission Control', 'route': '/mission-control/', 'status': 'live'},
    {'system': 'Relationship OS (#59)', 'route': '/mission-control/relationship-os.html', 'status': 'live'},
    {'system': 'Arkansas Civic Atlas (#58)', 'route': '/mission-control/civic-atlas.html', 'status': 'live'},
    {'system': 'Community Education Academy (#68)', 'route': '/mission-control/citizen-leadership-academy.html', 'status': 'live'},
    {'system': 'Coalition Network (#61)', 'route': '/mission-control/coalition-network.html', 'status': 'live'},
    {'system': 'ANOS (#79)', 'route': '/mission-control/arkansas-neighborhood-operating-system.html', 'status': 'live'},
    {'system': 'ACOS (#77)', 'route': '/mission-control/arkansas-county-operating-system.html', 'status': 'live'},
    {'system': 'Citizen Action Center (#62)', 'route': '/mission-control/citizen-action-center.html', 'status': 'live'},
    {'system': 'Relational Growth Engine (#69)', 'route': '/mission-control/relational-organizing-growth-engine.html', 'status': 'live'},
    {'system': 'Master Launch Plan (#85)', 'route': '/mission-control/master-launch-plan.html', 'status': 'live'},
]

civic_reach_readiness = min(
    56,
    19
    + len(ENGAGEMENT_LEVELS) * 2
    + len(CONNECTION_TYPES) // 2
    + len(COUNTY_OBJECTIVES) // 2
    + len(CITY_OBJECTIVES) // 2
    + len(REACH_DASHBOARD_ITEMS) // 2
    + len(GROWTH_STRATEGIES) // 3
    + len(QUALITY_METRICS) // 2
    + len(ETHICAL_STANDARDS) // 2
    + 3,
)

out = {
    'version': '1.0',
    'build': 86,
    'updated': today,
    'title': 'Master Arkansas Civic Reach & Participation Strategy v1.0',
    'subtitle': 'Reaching Every Community',
    'tagline': 'The 15% Arkansas Engagement Framework',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/arkansas-civic-reach-participation.html',
    'constitution': '/docs/MASTER_ARKANSAS_CIVIC_REACH_PARTICIPATION.md',
    'purpose': (
        'Establish 15% Connected Citizen Goal — voluntary relationship with at least 15% of '
        'registered voters in every county and major city. Primary statewide performance indicator.'
    ),
    'governing_principle': (
        'Growth is not measured by popularity. It is measured by trust. Every new participant '
        'chose to continue learning. Every county reaching 15% represents stronger local civic '
        'education. When every county advances, Arkansas advances.'
    ),
    'institutional_philosophy': {
        'title': 'Institutional Philosophy',
        'not_persuade_15_percent': True,
        'educate_and_remain_connected': True,
        'participation_not_agreement': True,
        'connection_types': CONNECTION_TYPES,
        'every_participant_chooses_level': True,
    },
    'arkansas_reach_goal': {
        'title': 'The Arkansas Reach Goal',
        'connected_citizen_goal_pct': CONNECTED_CITIZEN_GOAL_PCT,
        'formula': 'Active Connected Participants ÷ Registered Voters = Civic Reach Percentage',
        'every_county_city_civic_reach_score': True,
        'mc_continuously_updates': True,
    },
    'county_objectives': {
        'title': 'County Objectives',
        'objectives': COUNTY_OBJECTIVES,
        'counties_total': counties_total,
        'counties_at_goal': counties_at_goal,
        'each_county_own_pace': True,
        'status': 'specified',
    },
    'city_objectives': {
        'title': 'City Objectives',
        'objectives': CITY_OBJECTIVES,
        'cities_total': cities_total,
        'cities_at_goal': cities_at_goal,
        'rankings_by_educational_reach': True,
        'not_political_influence': True,
        'status': 'specified',
    },
    'engagement_levels': {
        'title': 'Engagement Levels',
        'levels': ENGAGEMENT_LEVELS,
        'every_level_strengthens_network': True,
        'status': 'specified',
    },
    'mission_control_reach_dashboard': {
        'title': 'Mission Control Reach Dashboard',
        'indicators': REACH_DASHBOARD_ITEMS,
        'live': reach_dashboard_live,
        'executive_heat_maps': True,
        'identify_outreach_needs': True,
        'status': 'planned',
    },
    'community_growth_strategies': {
        'title': 'Community Growth Strategies',
        'strategies': GROWTH_STRATEGIES,
        'invitation_not_pressure': True,
        'status': 'specified',
    },
    'quality_of_participation': {
        'title': 'Quality of Participation',
        'metrics': QUALITY_METRICS,
        'meaningful_over_raw_registration': True,
        'status': 'specified',
    },
    'ethical_standards': {
        'title': 'Ethical Standards',
        'standards': ETHICAL_STANDARDS,
        'trust_more_important_than_growth': True,
        'clear_communications_control': True,
        'status': 'specified',
    },
    'founders_standard': {
        'title': "Founder's Standard",
        'text': FOUNDERS_STANDARD,
        'informed_not_large_audience': True,
    },
    'integration': {
        'chain': (
            'Mission Control → Relationship OS → Civic Atlas → Education Academy → '
            'Coalition Network → ANOS → ACOS → Citizen Action Center'
        ),
        'every_connected_arkansan_strengthens_ecosystem': True,
        'systems': SYSTEM_CONNECTIONS,
    },
    'long_term_vision': (
        'Years after launch: every county displays Civic Reach Percentage, every city tracks '
        'educational participation. Leadership identifies flourishing communities and outreach '
        'needs. Largest voluntary civic learning network in Arkansas with meaningful connections '
        'in every corner of the state.'
    ),
    'summary': {
        'connected_citizen_goal_pct': CONNECTED_CITIZEN_GOAL_PCT,
        'statewide_connected_participants': statewide_connected_participants,
        'statewide_registered_voters': statewide_registered_voters,
        'registered_voters_tracked': registered_voters_tracked,
        'statewide_civic_reach_pct': statewide_civic_reach_pct,
        'counties_at_goal': counties_at_goal,
        'counties_total': counties_total,
        'cities_at_goal': cities_at_goal,
        'cities_total': cities_total,
        'engagement_levels': len(ENGAGEMENT_LEVELS),
        'reach_dashboard_live': reach_dashboard_live,
        'growth_this_month': growth_this_month,
        'growth_this_year': growth_this_year,
        'arkansas_civic_reach_participation_readiness_pct': civic_reach_readiness,
        'master_launch_plan_readiness_pct': mlp.get('summary', {}).get('master_launch_plan_readiness_pct', 54),
        'public_launch_readiness_pct': ex.get('public_launch_readiness', 8),
    },
    'catalog_gaps': [
        'Reach dashboard not live — Civic Reach Score not computed',
        '0 statewide connected participants — no tracking pipeline',
        'Registered voters not tracked — denominator missing for reach %',
        '0/75 counties at 15% goal · 0/250 cities at 15%',
        'County/city Civic Reach Scores not in MC or Civic Atlas',
        'Quality of participation metrics not measured',
        'Growth this month/year not tracked',
        'Projected completion not computed',
        'Executive heat maps not live',
        'Engagement levels specified — not assigned to participants',
        'Ethical unsubscribe/preference management not built',
        'Build #86 vs 200K goal (#64) — 15% voters vs connected Arkansans reconcile?',
    ],
    'recommended_next_build': {
        'number': 87,
        'title': 'Civic Reach Dashboard & County/City Score Components',
        'note': (
            'Reach dashboard UI, Civic Reach Score engine, county/city heat maps, '
            'registered voter integration, engagement level tracking, COMP-* specs.'
        ),
    },
}

with open(root / 'data/arkansas-civic-reach-participation.json', 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')

print(
    f'Civic Reach Strategy: {statewide_connected_participants} connected, '
    f'{counties_at_goal}/{counties_total} counties at 15%, {civic_reach_readiness}% readiness'
)
