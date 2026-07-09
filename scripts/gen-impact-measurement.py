"""
Generate data/impact-measurement.json — Build #67.
Master Impact Measurement & Arkansas Civic Scorecard v1.0.
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
el = load_json(root / 'data/evidence-ledger.json')
aan = load_json(root / 'data/arkansas-action-network.json')
cn = load_json(root / 'data/coalition-network.json')
atlas = load_json(root / 'data/civic-atlas.json')
cicc = load_json(root / 'data/civic-intelligence-command-center.json')

ex = mc.get('executive', {})
el_sum = el.get('summary', {})
aan_sum = aan.get('summary', {})
PARTICIPANTS_TARGET = 200_000

# Honest zeros — measure understanding, not traffic
learning_paths_completed = 0
curriculum_progress_pct = 0
returning_learners = 0
education_leaders = 0
academy_graduates = 0
community_conversations = 0
educational_events = 0
libraries_participating = 0
claims_verified = el_sum.get('claims_verified', 0)
counties_represented = 0
cities_represented = 0
neighborhood_participation = 0
connected_arkansans = aan_sum.get('connected_arkansans', 0)
coalition_orgs = cn.get('summary', {}).get('organizations_total', 0)
county_scorecards_live = 0
city_scorecards_live = 0
leadership_scorecards_live = 0
annual_civic_report_live = False
community_feedback_collected = 0

FIVE_IMPACT_PILLARS = [
    {
        'id': 'IMP-P1', 'number': 1, 'pillar': 'Knowledge Impact',
        'question': 'Are people learning?',
        'tracks': [
            'Learning path completion', 'Curriculum progress', 'Encyclopedia usage',
            'Research Library usage', 'Video completion', 'Returning learners',
        ],
        'primary_kpi': 'Growth in completed educational journeys',
        'current': learning_paths_completed,
        'status': 'planned',
    },
    {
        'id': 'IMP-P2', 'number': 2, 'pillar': 'Leadership Impact',
        'question': 'Are we developing educators?',
        'tracks': [
            'Education Leaders', 'County Leaders', 'City Leaders', 'Mentors',
            'Academy graduates', 'Leadership retention',
        ],
        'primary_kpi': 'Growth in active educational leadership',
        'current': education_leaders,
        'status': 'planned',
        'route': '/mission-control/arkansas-action-network.html',
    },
    {
        'id': 'IMP-P3', 'number': 3, 'pillar': 'Community Impact',
        'question': 'Is learning spreading into communities?',
        'tracks': [
            'Community conversations', 'Educational events', 'Libraries participating',
            'Coalition organizations', 'Neighborhood participation', 'County activity',
        ],
        'primary_kpi': 'Growth in local civic education activity',
        'current': community_conversations,
        'status': 'planned',
    },
    {
        'id': 'IMP-P4', 'number': 4, 'pillar': 'Institutional Impact',
        'question': 'Is the institution becoming stronger?',
        'tracks': [
            'Research growth', 'Claims verified', 'Sources added',
            'Educational assets', 'Technology readiness', 'Governance completion',
        ],
        'primary_kpi': 'Institutional maturity',
        'current': ex.get('institutional_maturity_pct', 32),
        'unit': 'percent',
        'status': 'partial',
        'route': '/mission-control/civic-intelligence-command-center.html',
    },
    {
        'id': 'IMP-P5', 'number': 5, 'pillar': 'Arkansas Impact',
        'question': 'Is statewide educational capacity improving?',
        'tracks': [
            'Counties represented', 'Cities represented', 'Neighborhood participation',
            '200,000 participant progress', 'Coalition growth', 'Geographic coverage',
        ],
        'primary_kpi': 'Educational reach across Arkansas',
        'current': counties_represented,
        'target': 75,
        'status': 'planned',
        'route': '/mission-control/civic-atlas.html',
    },
]

ARKANSAS_CIVIC_SCORECARD = [
    {'id': 'ACS-1', 'indicator': 'Research Score', 'current': ex.get('research_readiness', 26), 'unit': 'percent', 'status': 'partial'},
    {'id': 'ACS-2', 'indicator': 'Education Score', 'current': ex.get('education_academy_readiness', 26), 'unit': 'percent', 'status': 'partial'},
    {'id': 'ACS-3', 'indicator': 'Leadership Score', 'current': education_leaders, 'status': 'planned'},
    {'id': 'ACS-4', 'indicator': 'County Coverage Score', 'current': counties_represented, 'target': 75, 'status': 'planned'},
    {'id': 'ACS-5', 'indicator': 'City Coverage Score', 'current': cities_represented, 'target': 250, 'status': 'planned'},
    {'id': 'ACS-6', 'indicator': 'Coalition Score', 'current': coalition_orgs, 'status': 'live'},
    {'id': 'ACS-7', 'indicator': 'Community Conversation Score', 'current': community_conversations, 'status': 'planned'},
    {'id': 'ACS-8', 'indicator': 'Knowledge Growth Score', 'current': learning_paths_completed, 'status': 'planned'},
    {'id': 'ACS-9', 'indicator': 'Institutional Health Score', 'current': cicc.get('summary', {}).get('institutional_health_score', 32), 'unit': 'percent', 'status': 'partial'},
    {'id': 'ACS-10', 'indicator': 'Overall Arkansas Civic Education Score', 'current': 0, 'unit': 'composite', 'status': 'planned'},
]

COUNTY_SCORECARD_FIELDS = [
    'Education Leaders', 'Academy graduates', 'Community conversations',
    'Coalition organizations', 'Educational events', 'Participant growth',
    'Resource usage', 'Coverage score',
]

CITY_SCORECARD_FIELDS = [
    'Leadership score', 'Community participation', 'Educational events',
    'Coalition participation', 'Learning engagement', 'Growth trend',
]

LEADERSHIP_SCORECARD_FIELDS = [
    'Learning completed', 'Presentations delivered', 'Community conversations',
    'Resources shared', 'Mentorship activity', 'Volunteer development',
]

OUTCOME_EXAMPLES = [
    {
        'output': '50 presentations delivered',
        'outcome': 'More communities now understand Citizens United',
    },
    {
        'output': '100 videos published',
        'outcome': 'Learners complete more educational pathways',
    },
]

COMMUNITY_FEEDBACK_TYPES = [
    'Visitor reflections', 'Education Leader observations',
    'Community conversation summaries', 'Coalition feedback', 'Suggestions for improvement',
]

IMPACT_DASHBOARD_WIDGETS = [
    {'id': 'IMD-W1', 'widget': 'Knowledge Growth', 'current': learning_paths_completed, 'status': 'planned'},
    {'id': 'IMD-W2', 'widget': 'Leadership Growth', 'current': education_leaders, 'status': 'planned'},
    {'id': 'IMD-W3', 'widget': 'County Progress', 'current': f'{counties_represented}/75', 'status': 'planned'},
    {'id': 'IMD-W4', 'widget': 'City Progress', 'current': f'{cities_represented}/250', 'status': 'planned'},
    {'id': 'IMD-W5', 'widget': 'Neighborhood Growth', 'current': neighborhood_participation, 'status': 'planned'},
    {'id': 'IMD-W6', 'widget': 'Participant Growth', 'current': f'{connected_arkansans}/{PARTICIPANTS_TARGET}', 'status': 'live'},
    {'id': 'IMD-W7', 'widget': 'Coalition Health', 'current': coalition_orgs, 'status': 'live'},
    {'id': 'IMD-W8', 'widget': 'Research Growth', 'current': claims_verified, 'status': 'partial'},
    {'id': 'IMD-W9', 'widget': 'Institutional Readiness', 'current': ex.get('institutional_maturity_pct', 32), 'unit': 'percent', 'status': 'partial'},
    {'id': 'IMD-W10', 'widget': 'Arkansas Civic Score', 'current': 0, 'status': 'planned'},
]

BENCHMARK_PERIODS = [
    {'period': 'Current year', 'status': 'partial'},
    {'period': 'Previous year', 'status': 'planned'},
    {'period': 'Five-year trend', 'status': 'planned'},
    {'period': 'Ten-year trend', 'status': 'planned'},
]

SYSTEM_CONNECTIONS = [
    {'system': 'Civic Atlas (#58)', 'route': '/mission-control/civic-atlas.html', 'status': 'live', 'note': 'Educational Coverage Score'},
    {'system': 'Arkansas Action Network (#64)', 'route': '/mission-control/arkansas-action-network.html', 'status': 'live'},
    {'system': 'Command Center (#65)', 'route': '/mission-control/civic-intelligence-command-center.html', 'status': 'live'},
    {'system': 'Evidence Ledger (#41)', 'route': '/mission-control/evidence-ledger.html', 'status': 'partial'},
    {'system': 'Visitor Journey (#47)', 'route': '/mission-control/visitor-journey.html', 'status': 'partial'},
    {'system': 'Coalition Network (#61)', 'route': '/mission-control/coalition-network.html', 'status': 'live'},
    {'system': 'Sustainability Stewardship (#66)', 'route': '/mission-control/sustainability-stewardship.html', 'status': 'live'},
    {'system': 'Mission Control', 'route': '/mission-control/', 'status': 'live'},
]

# Composite score honest: mostly zeros
overall_arkansas_civic_score = 0
impact_measurement_readiness = min(
    42,
    12 + len(FIVE_IMPACT_PILLARS) * 3 + 4,
)

out = {
    'version': '1.0',
    'build': 67,
    'updated': today,
    'title': 'Master Impact Measurement & Arkansas Civic Scorecard v1.0',
    'subtitle': 'Measuring What Actually Matters — The Institutional Impact Framework',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/impact-measurement.html',
    'constitution': '/docs/MASTER_IMPACT_MEASUREMENT.md',
    'purpose': (
        'Evaluate whether the institution truly strengthens civic literacy — '
        'measure understanding, not just activity.'
    ),
    'governing_principle': (
        'Success measured by quality of civic understanding created. '
        'Ordinary Arkansans better equipped to understand, explain, discuss, and teach.'
    ),
    'core_philosophy': (
        'Do not celebrate traffic, impressions, or page views unless they deepen understanding. '
        'Primary question: Are more Arkansans able to understand, explain, and teach than before?'
    ),
    'measures_understanding_not_traffic': True,
    'five_impact_pillars': FIVE_IMPACT_PILLARS,
    'arkansas_civic_scorecard': {
        'title': 'Arkansas Civic Scorecard',
        'indicators': ARKANSAS_CIVIC_SCORECARD,
        'overall_score': overall_arkansas_civic_score,
        'published': False,
        'status': 'partial',
    },
    'county_scorecards': {
        'title': 'County Scorecards',
        'counties_total': 75,
        'scorecards_live': county_scorecards_live,
        'fields': COUNTY_SCORECARD_FIELDS,
        'route': '/mission-control/civic-atlas.html',
        'status': 'planned',
    },
    'city_scorecards': {
        'title': 'City Scorecards',
        'cities_target': 250,
        'scorecards_live': city_scorecards_live,
        'fields': CITY_SCORECARD_FIELDS,
        'compare_over_time_not_between': True,
        'status': 'planned',
    },
    'leadership_scorecards': {
        'title': 'Leadership Scorecards',
        'personal_growth_not_competition': True,
        'scorecards_live': leadership_scorecards_live,
        'fields': LEADERSHIP_SCORECARD_FIELDS,
        'status': 'planned',
    },
    'annual_institutional_benchmarks': {
        'title': 'Annual Institutional Benchmarks',
        'periods': BENCHMARK_PERIODS,
        'long_term_perspective': True,
        'status': 'planned',
    },
    'outcomes_over_outputs': {
        'title': 'Outcomes Over Outputs',
        'principle': 'Continually distinguish activity from impact',
        'examples': OUTCOME_EXAMPLES,
        'status': 'live',
    },
    'community_feedback': {
        'title': 'Community Feedback',
        'types': COMMUNITY_FEEDBACK_TYPES,
        'collected': community_feedback_collected,
        'qualitative_impact': True,
        'status': 'planned',
    },
    'impact_dashboard': {
        'title': 'Mission Control Impact Dashboard',
        'institutional_report_card': True,
        'widgets': IMPACT_DASHBOARD_WIDGETS,
        'status': 'partial',
    },
    'public_accountability': {
        'title': 'Annual Arkansas Civic Education Report',
        'sections': [
            'Institutional accomplishments', 'Research expansion', 'Leadership development',
            'Community education', 'Coalition growth', 'Future priorities',
        ],
        'live': annual_civic_report_live,
        'status': 'planned',
    },
    'integration': {
        'systems': SYSTEM_CONNECTIONS,
        'ecs_from': 'Civic Atlas Educational Coverage Score',
    },
    'long_term_vision': (
        'Twenty years after launch: measurable improvements in civic education infrastructure — '
        'more understand, teach, participate, collaborate; stronger learning ecosystem statewide.'
    ),
    'summary': {
        'pillars_total': len(FIVE_IMPACT_PILLARS),
        'pillars_partial_or_live': sum(1 for p in FIVE_IMPACT_PILLARS if p['status'] in ('live', 'partial')),
        'scorecard_indicators': len(ARKANSAS_CIVIC_SCORECARD),
        'overall_arkansas_civic_score': overall_arkansas_civic_score,
        'learning_paths_completed': learning_paths_completed,
        'education_leaders': education_leaders,
        'community_conversations': community_conversations,
        'counties_represented': counties_represented,
        'cities_represented': cities_represented,
        'connected_arkansans': connected_arkansans,
        'connected_target': PARTICIPANTS_TARGET,
        'claims_verified': claims_verified,
        'county_scorecards_live': county_scorecards_live,
        'impact_measurement_readiness_pct': impact_measurement_readiness,
        'civic_atlas_readiness_pct': ex.get('civic_atlas_readiness', 52),
        'public_launch_readiness_pct': ex.get('public_launch_readiness', 8),
    },
    'catalog_gaps': [
        'Overall Arkansas Civic Education Score = 0 — composite formula not implemented',
        '0 learning paths completed — no learner tracking pipeline',
        '0 Education Leaders — leadership impact pillar empty',
        '0 community conversations — community impact not measured',
        '0/75 county scorecards live — Civic Atlas ECS=0 for all counties',
        '0/250 city scorecards — city progress not tracked',
        'Leadership personal dashboards not built — no competition policy enforced in UI',
        'Annual benchmarks — no year-over-year data stored',
        'Community feedback collection not implemented — 0 qualitative records',
        'Annual Arkansas Civic Education Report not published',
        'Build #67 Impact vs Visitor Journey (#47) metrics — unify funnel?',
        'Traffic/analytics explicitly deprioritized — no GA integration by design',
        'Outcome vs output distinction documented — not automated in MC widgets',
    ],
    'recommended_next_build': {
        'number': 68,
        'title': 'Implementation Translation Layer & Engineering Artifacts',
        'note': (
            'Scorecard composite formula, county/city scorecard schema, learner tracking, '
            'impact widget components, annual report generator, route inventory, GitHub backlog.'
        ),
    },
}

with open(root / 'data/impact-measurement.json', 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')

print(
    f'Impact Measurement: {len(FIVE_IMPACT_PILLARS)} pillars, '
    f'overall civic score {overall_arkansas_civic_score}, '
    f'{impact_measurement_readiness}% readiness'
)
