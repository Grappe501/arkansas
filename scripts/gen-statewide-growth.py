"""
Generate data/statewide-growth.json and data/arkansas-cities.json — Build #56.
Statewide Growth & Leadership Blueprint — Arkansas Civic Education Network v1.0.
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
counties_data = load_json(root / 'data/arkansas-counties.json')
coalition = load_json(root / 'data/coalition-directory.json')
vj = load_json(root / 'data/visitor-journey.json')

ex = mc.get('executive', {})
orgs = coalition.get('summary', {}).get('total_organizations', 0)
edu_leaders = vj.get('summary', {}).get('education_leader_signups', 0)
participants = vj.get('summary', {}).get('contact_network_signups', 0)

with open(root / 'scripts/arkansas-top250-cities.json', encoding='utf-8') as f:
    top250 = json.load(f)

COUNTY_LEADER_MIN = 1
COUNTY_LEADER_TARGET = 3
COUNTY_LEADER_MATURE = 10
PARTICIPANTS_TARGET = 200_000

counties = counties_data.get('counties', [])
counties_total = len(counties) or 75

# County coverage tiers (honest: all zero today)
counties_no_leaders = counties_total
counties_one_leader = 0
counties_meeting_target = 0
counties_exceeding_target = 0

cities = []
for c in top250:
    cities.append({
        'rank': c['rank'],
        'name': c['name'],
        'population_estimate': c['population_estimate'],
        'county': None,
        'education_leaders': 0,
        'coalition_orgs': 0,
        'conversations': 0,
        'events': 0,
        'participants': 0,
        'status': 'no_coverage',
    })

cities_with_leaders = sum(1 for c in cities if c['education_leaders'] > 0)
counties_with_leaders = sum(1 for c in counties if c.get('educators', 0) > 0)

LEADERSHIP_LADDER = [
    {'stage': 1, 'id': 'visitor', 'title': 'Visitor', 'status': 'live'},
    {'stage': 2, 'id': 'subscriber', 'title': 'Subscriber', 'status': 'planned'},
    {'stage': 3, 'id': 'learner', 'title': 'Learner', 'status': 'partial'},
    {'stage': 4, 'id': 'community_participant', 'title': 'Community Participant', 'status': 'planned'},
    {'stage': 5, 'id': 'volunteer', 'title': 'Volunteer', 'status': 'planned'},
    {'stage': 6, 'id': 'education_leader', 'title': 'Education Leader', 'status': 'planned'},
    {'stage': 7, 'id': 'county_leader', 'title': 'County Leader', 'status': 'planned'},
    {'stage': 8, 'id': 'regional_mentor', 'title': 'Regional Mentor', 'status': 'planned'},
]

OBJECTIVES = [
    {
        'id': 'OBJ-1',
        'number': 1,
        'title': 'Education Leaders in All 75 Counties',
        'minimum': COUNTY_LEADER_MIN,
        'target_range': '3–5 active Education Leaders',
        'mature': f'{COUNTY_LEADER_MATURE}+ depending on population',
        'current': {
            'counties_represented': counties_with_leaders,
            'counties_total': counties_total,
            'education_leaders': edu_leaders,
            'no_leaders': counties_no_leaders,
            'one_leader': counties_one_leader,
            'meeting_target': counties_meeting_target,
            'exceeding_target': counties_exceeding_target,
        },
        'mc_displays': [
            'Counties with no leaders',
            'Counties with one leader',
            'Counties meeting target',
            'Counties exceeding target',
        ],
        'status': 'scaffolded',
        'progress_pct': round((counties_with_leaders / counties_total) * 100, 1) if counties_total else 0,
    },
    {
        'id': 'OBJ-2',
        'number': 2,
        'title': 'Education Leaders in the 250 Largest Arkansas Cities',
        'cities_total': 250,
        'current': {
            'cities_represented': cities_with_leaders,
            'education_leaders': edu_leaders,
        },
        'city_dashboard_fields': [
            'Education Leaders',
            'Coalition organizations',
            'Community conversations',
            'Educational events',
            'Resource distribution',
            'Growth trends',
        ],
        'status': 'scaffolded',
        'progress_pct': round((cities_with_leaders / 250) * 100, 1),
    },
    {
        'id': 'OBJ-3',
        'number': 3,
        'title': '200,000 Arkansas Community Participants',
        'target': PARTICIPANTS_TARGET,
        'current': participants,
        'involvement_levels': [
            'Receive educational updates',
            'Attend community conversations',
            'Share educational resources',
            'Participate in surveys',
            'Volunteer occasionally',
            'Become an Education Leader',
            'Join coalition activities',
        ],
        'status': 'scaffolded',
        'progress_pct': round((participants / PARTICIPANTS_TARGET) * 100, 4),
    },
]

BENCHMARKS = [
    {'id': 'BM-1', 'benchmark': '75 of 75 counties represented', 'target': 75, 'current': counties_with_leaders, 'status': 'not_started'},
    {'id': 'BM-2', 'benchmark': '250 largest cities represented', 'target': 250, 'current': cities_with_leaders, 'status': 'not_started'},
    {'id': 'BM-3', 'benchmark': '200,000 participants connected', 'target': PARTICIPANTS_TARGET, 'current': participants, 'status': 'not_started'},
    {'id': 'BM-4', 'benchmark': 'Coalition organizations in every region', 'target': 7, 'current': 0, 'status': 'not_started', 'note': f'{orgs} orgs statewide — regional coverage not mapped'},
    {'id': 'BM-5', 'benchmark': 'Community conversations occurring statewide', 'target': 'ongoing', 'current': 0, 'status': 'not_started'},
]

RECRUITMENT_CHANNELS = [
    {'id': 'web', 'channel': 'Website signups', 'status': 'partial', 'route': '/educate/'},
    {'id': 'presentations', 'channel': 'Community presentations', 'status': 'planned'},
    {'id': 'coalition', 'channel': 'Coalition organizations', 'status': 'planned', 'route': '/coalition/'},
    {'id': 'libraries', 'channel': 'Libraries', 'status': 'planned'},
    {'id': 'civic', 'channel': 'Civic organizations', 'status': 'planned'},
    {'id': 'colleges', 'channel': 'Colleges and universities', 'status': 'planned'},
    {'id': 'faith', 'channel': 'Faith communities', 'status': 'planned'},
    {'id': 'social', 'channel': 'Social media', 'status': 'planned'},
    {'id': 'referrals', 'channel': 'Friend and family referrals (relational organizing)', 'status': 'planned'},
]

SUCCESS_INDICATORS = [
    {'id': 'SI-1', 'indicator': 'Education Leaders trained', 'current': edu_leaders, 'status': 'not_started'},
    {'id': 'SI-2', 'indicator': 'Counties represented', 'current': counties_with_leaders, 'target': 75, 'status': 'not_started'},
    {'id': 'SI-3', 'indicator': 'Cities represented', 'current': cities_with_leaders, 'target': 250, 'status': 'not_started'},
    {'id': 'SI-4', 'indicator': 'Active community participants', 'current': participants, 'target': PARTICIPANTS_TARGET, 'status': 'not_started'},
    {'id': 'SI-5', 'indicator': 'Coalition organizations', 'current': orgs, 'status': 'not_started'},
    {'id': 'SI-6', 'indicator': 'Community conversations held', 'current': 0, 'status': 'not_started'},
    {'id': 'SI-7', 'indicator': 'Educational resources shared', 'current': 0, 'status': 'not_started'},
    {'id': 'SI-8', 'indicator': 'Returning learners', 'current': 0, 'status': 'not_started'},
]

GEO_DASHBOARDS = [
    {'id': 'county_map', 'title': 'County Coverage', 'metrics': ['Education Leaders', 'Coalition partners', 'Community activity'], 'status': 'planned'},
    {'id': 'city_map', 'title': 'City Coverage', 'metrics': ['Education Leaders', 'Events', 'Organization participation'], 'status': 'planned'},
    {'id': 'statewide', 'title': 'Statewide Participation', 'metrics': ['Total participants', 'Growth over time', 'Regional distribution'], 'status': 'planned'},
]

MC_METRICS = [
    {'id': 'counties_no_leaders', 'title': 'Counties with no leaders', 'current': counties_no_leaders, 'status': 'live'},
    {'id': 'counties_one_leader', 'title': 'Counties with one leader', 'current': counties_one_leader, 'status': 'live'},
    {'id': 'counties_meeting_target', 'title': 'Counties meeting target (3–5)', 'current': counties_meeting_target, 'status': 'live'},
    {'id': 'counties_exceeding_target', 'title': 'Counties exceeding target (10+)', 'current': counties_exceeding_target, 'status': 'live'},
    {'id': 'cities_represented', 'title': 'Cities with Education Leaders', 'current': cities_with_leaders, 'target': 250, 'status': 'live'},
    {'id': 'participants', 'title': 'Community participants', 'current': participants, 'target': PARTICIPANTS_TARGET, 'status': 'live'},
    {'id': 'education_leaders', 'title': 'Education Leaders statewide', 'current': edu_leaders, 'status': 'live'},
]

# Readiness: objectives documented + county/city scaffolds; no live growth data
scaffold_score = 40
maps_score = 5
data_integration = 8 if counties_total == 75 else 0
statewide_growth_readiness = min(48, scaffold_score + maps_score + data_integration)

out_cities = {
    'version': '1.0',
    'build': 56,
    'updated': today,
    'title': 'Arkansas Top 250 Communities Index',
    'source': 'Population estimates — World Population Review 2026 (scaffold)',
    'cities_total': 250,
    'summary': {
        'cities_with_education_leaders': cities_with_leaders,
        'cities_with_events': 0,
        'total_education_leaders': edu_leaders,
        'total_participants': participants,
        'coverage_pct': round((cities_with_leaders / 250) * 100, 1),
    },
    'cities': cities,
}

out = {
    'version': '1.0',
    'build': 56,
    'updated': today,
    'title': 'Statewide Growth & Leadership Blueprint v1.0',
    'subtitle': 'Arkansas Civic Education Network — County, City & Neighborhood Expansion Strategy',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/statewide-growth.html',
    'constitution': '/docs/MASTER_STATEWIDE_GROWTH.md',
    'purpose': (
        'Measurable statewide growth objectives Mission Control monitors from launch forward — '
        'infrastructure for a durable civic education movement across Arkansas.'
    ),
    'governing_principle': (
        'Success is not website visits — it is whether every Arkansan has a nearby opportunity to learn, '
        'ask questions, access reliable evidence, and participate in thoughtful civic education.'
    ),
    'arkansas_vision': (
        'Every Arkansan should have a reasonable opportunity to learn about Citizens United through '
        'someone they know or an organization in their own community.'
    ),
    'growth_model': 'Trusted local relationships outward — not solely statewide communications',
    'statewide_objectives': OBJECTIVES,
    'neighborhood_network': {
        'principle': 'Community connection — not precise location tracking',
        'privacy_first': True,
        'participation_types': [
            'Neighborhood conversations',
            'Local discussion groups',
            'Community presentations',
            'Resource sharing',
            'Event hosting',
        ],
    },
    'leadership_ladder': {
        'title': 'Eight-Stage Leadership Development',
        'stages': LEADERSHIP_LADDER,
        'flow': 'Visitor → Subscriber → Learner → Community Participant → Volunteer → Education Leader → County Leader → Regional Mentor',
    },
    'geographic_dashboards': GEO_DASHBOARDS,
    'community_benchmarks': BENCHMARKS,
    'recruitment_channels': RECRUITMENT_CHANNELS,
    'county_growth_plans': {
        'title': 'Per-County Local Growth Strategy',
        'components': [
            'Leadership recruitment',
            'Organization outreach',
            'Educational events',
            'Resource distribution',
            'Community conversation schedule',
        ],
        'counties_needing_support': counties_total,
        'route': '/mission-control/county-os.html',
        'status': 'scaffolded',
    },
    'success_indicators': SUCCESS_INDICATORS,
    'long_term_vision': [
        'Every Arkansas county has trusted local Education Leaders',
        '250 largest cities have visible civic education activity',
        '200,000 Arkansans connected through voluntary participation',
        'Coalition organizations sustain local education',
        'Learning rooted in neighborhoods, communities, and trusted local relationships',
    ],
    'mc_integration': {
        'title': 'Statewide Growth Metrics',
        'status': 'partial',
        'metrics': MC_METRICS,
        'related_routes': {
            'counties': '/data/arkansas-counties.json',
            'cities': '/data/arkansas-cities.json',
            'county_os': '/mission-control/county-os.html',
            'education_academy': '/mission-control/education-academy.html',
            'coalition': '/coalition/',
        },
    },
    'summary': {
        'counties_total': counties_total,
        'counties_with_leaders': counties_with_leaders,
        'counties_no_leaders': counties_no_leaders,
        'cities_total': 250,
        'cities_with_leaders': cities_with_leaders,
        'education_leaders': edu_leaders,
        'participants_current': participants,
        'participants_target': PARTICIPANTS_TARGET,
        'participants_progress_pct': round((participants / PARTICIPANTS_TARGET) * 100, 4),
        'coalition_orgs': orgs,
        'benchmarks_met': 0,
        'benchmarks_total': len(BENCHMARKS),
        'interactive_maps_status': 'planned',
        'statewide_growth_readiness_pct': statewide_growth_readiness,
        'public_launch_readiness_pct': ex.get('public_launch_readiness', 8),
    },
    'catalog_gaps': [
        f'0/{counties_total} counties with Education Leaders — objectives defined, network empty',
        f'0/250 cities with local leadership — index scaffolded from population estimates',
        f'0/{PARTICIPANTS_TARGET:,} community participants — no signup funnel integrated',
        'Interactive geographic maps not built — dashboard tables only',
        'County-to-city linkage pending — city county field null',
        'Neighborhood network privacy model documented — no participant geo fields in schema',
        'Leadership ladder 2/8 stages operational — mostly planned',
        'County growth plans exist in County OS (#31) — not unified with this blueprint',
        'Recruitment channels 1/9 partial — website only',
        'Relational organizing / referral tracking not implemented',
    ],
    'recommended_next_build': {
        'number': 57,
        'title': 'Implementation Translation Layer & Engineering Artifacts',
        'note': (
            'Neon schema for participants/leaders/geo, route inventory, COMP-* specs, API contracts, '
            'GitHub issue backlog — connect growth objectives to buildable systems.'
        ),
    },
}

with open(root / 'data/arkansas-cities.json', 'w', newline='\n') as f:
    json.dump(out_cities, f, indent=2)
    f.write('\n')

with open(root / 'data/statewide-growth.json', 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')

print(
    f'Statewide Growth: {counties_total} counties, 250 cities indexed, '
    f'{edu_leaders} leaders, {participants} participants, {statewide_growth_readiness}% readiness'
)
