"""
Generate data/arkansas-county-operating-system.json — Build #77.
Master Arkansas County Operating System (ACOS) v1.0.
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
cos = load_json(root / 'data/county-operating-system.json')
acs = load_json(root / 'data/arkansas-command-strategy.json')
counties = load_json(root / 'data/arkansas-counties.json')
cci = load_json(root / 'data/county-coalition-index.json')

ex = mc.get('executive', {})
COUNTIES_TOTAL = counties.get('counties_total', 75)

# Honest zeros
counties_scaffolded = cci.get('counties_total', COUNTIES_TOTAL) if cci else COUNTIES_TOTAL
counties_with_digital_twin = 0
county_dashboards_live = 0
counties_past_awareness = 0
counties_at_level = {i: 0 for i in range(1, 7)}
counties_at_level[1] = COUNTIES_TOTAL  # all at awareness spec only
county_health_index_computed = False
county_listening_reports_submitted = 0
county_event_calendars_live = 0
county_resource_libraries_live = 0
county_mentorship_pairs = 0
statewide_calendar_sync = False

COUNTY_PHILOSOPHY_QUESTIONS = [
    'Who are our Education Leaders?',
    'Which organizations are involved?',
    'Where are community conversations happening?',
    'What educational resources are available?',
    'What questions are people asking?',
    'What progress have we made?',
    'What do we need next?',
]

COUNTY_PROFILE_SECTIONS = [
    {'id': 'ACOS-CP-01', 'section': 'County history', 'status': 'specified'},
    {'id': 'ACOS-CP-02', 'section': 'Population overview', 'status': 'specified'},
    {'id': 'ACOS-CP-03', 'section': 'Major cities', 'status': 'specified'},
    {'id': 'ACOS-CP-04', 'section': 'Legislative districts', 'status': 'specified'},
    {'id': 'ACOS-CP-05', 'section': 'Congressional district', 'status': 'specified'},
    {'id': 'ACOS-CP-06', 'section': 'Libraries', 'status': 'specified'},
    {'id': 'ACOS-CP-07', 'section': 'Colleges (if applicable)', 'status': 'specified'},
    {'id': 'ACOS-CP-08', 'section': 'Historical societies', 'status': 'specified'},
    {'id': 'ACOS-CP-09', 'section': 'Coalition organizations', 'status': 'partial'},
    {'id': 'ACOS-CP-10', 'section': 'Education Leaders', 'status': 'partial'},
    {'id': 'ACOS-CP-11', 'section': 'Upcoming educational events', 'status': 'specified'},
    {'id': 'ACOS-CP-12', 'section': 'Community conversations', 'status': 'specified'},
    {'id': 'ACOS-CP-13', 'section': 'Educational Coverage Score', 'status': 'planned'},
]

LEADERSHIP_ROLES = [
    {'id': 'ACOS-LR-01', 'role': 'County Education Director', 'filled': 0, 'status': 'specified'},
    {'id': 'ACOS-LR-02', 'role': 'City Education Leaders', 'filled': 0, 'status': 'specified'},
    {'id': 'ACOS-LR-03', 'role': 'Neighborhood Education Leaders', 'filled': 0, 'status': 'specified'},
    {'id': 'ACOS-LR-04', 'role': 'Academy Mentors', 'filled': 0, 'status': 'specified'},
    {'id': 'ACOS-LR-05', 'role': 'Coalition Coordinator', 'filled': 0, 'status': 'specified'},
    {'id': 'ACOS-LR-06', 'role': 'Volunteer Coordinator', 'filled': 0, 'status': 'specified'},
    {'id': 'ACOS-LR-07', 'role': 'Research Liaison', 'filled': 0, 'status': 'specified'},
    {'id': 'ACOS-LR-08', 'role': 'Media Liaison', 'filled': 0, 'status': 'specified'},
]

COUNTY_GOAL_EXAMPLES = [
    'Recruit Education Leaders',
    'Host community conversations',
    'Expand coalition partnerships',
    'Complete Academy certifications',
    'Develop local educational resources',
    'Strengthen neighborhood coverage',
]

COUNTY_DASHBOARD = {
    'title': 'County Dashboard',
    'domains': [
        {
            'id': 'ACOS-CD-L',
            'domain': 'Leadership',
            'indicators': ['Education Leaders', 'Mentors', 'Academy graduates'],
            'status': 'planned',
        },
        {
            'id': 'ACOS-CD-C',
            'domain': 'Community',
            'indicators': ['Events', 'Conversations', 'Organizations'],
            'status': 'planned',
        },
        {
            'id': 'ACOS-CD-LN',
            'domain': 'Learning',
            'indicators': ['Course completion', 'Resource downloads', 'Research participation'],
            'status': 'planned',
        },
        {
            'id': 'ACOS-CD-G',
            'domain': 'Growth',
            'indicators': ['Participant growth', 'Volunteer growth', 'Neighborhood expansion'],
            'status': 'planned',
        },
    ],
    'live': False,
    'status': 'specified',
}

RESOURCE_LIBRARY = [
    'Presentation materials',
    'Fact sheets',
    'Community discussion guides',
    'Educational videos',
    'Print-ready resources',
    'Frequently asked questions',
    'County-specific educational opportunities',
]

EVENT_CALENDAR_TYPES = [
    'Community conversations',
    'Academy sessions',
    'Presentations',
    'Coalition meetings',
    'Volunteer gatherings',
    'Educational workshops',
]

LISTENING_REPORT_ITEMS = [
    'Community questions',
    'Educational needs',
    'Research requests',
    'Suggested improvements',
    'Leadership observations',
]

READINESS_LEVELS = [
    {'level': 1, 'id': 'awareness', 'title': 'Awareness', 'counties_at_level': counties_at_level[1]},
    {'level': 2, 'id': 'founding_leader', 'title': 'Founding Education Leader', 'counties_at_level': counties_at_level[2]},
    {'level': 3, 'id': 'leadership_team', 'title': 'Leadership Team', 'counties_at_level': counties_at_level[3]},
    {'level': 4, 'id': 'community_activity', 'title': 'Community Activity', 'counties_at_level': counties_at_level[4]},
    {'level': 5, 'id': 'coalition_network', 'title': 'Coalition Network', 'counties_at_level': counties_at_level[5]},
    {'level': 6, 'id': 'sustainable_system', 'title': 'Sustainable County Education System', 'counties_at_level': counties_at_level[6]},
]

HEALTH_INDEX_FACTORS = [
    'Leadership',
    'Volunteer activity',
    'Academy participation',
    'Community conversations',
    'Coalition participation',
    'Learning engagement',
    'Educational Coverage Score',
    'Resource utilization',
]

MENTORSHIP_TYPES = [
    'Shared presentations',
    'Joint workshops',
    'Leadership mentoring',
    'Resource sharing',
    'Regional planning',
]

SYSTEM_CONNECTIONS = [
    {'system': 'Mission Control', 'route': '/mission-control/', 'status': 'live'},
    {'system': 'Arkansas Civic Atlas (#58)', 'route': '/mission-control/civic-atlas.html', 'status': 'live'},
    {'system': 'Community Education Academy (#68)', 'route': '/mission-control/citizen-leadership-academy.html', 'status': 'live'},
    {'system': 'Relationship Operating System (#59)', 'route': '/mission-control/relationship-os.html', 'status': 'live'},
    {'system': 'Coalition Network (#61)', 'route': '/mission-control/coalition-network.html', 'status': 'live'},
    {'system': 'Citizen Action Center (#62)', 'route': '/mission-control/citizen-action-center.html', 'status': 'live'},
    {'system': 'Knowledge Graph', 'route': '/mission-control/knowledge-graph.html', 'status': 'live'},
    {'system': 'Campaign Finance Observatory (#63)', 'route': '/mission-control/campaign-finance-observatory.html', 'status': 'live'},
    {'system': 'County OS (#31)', 'route': '/mission-control/county-os.html', 'status': 'live', 'note': 'Extended by ACOS'},
    {'system': 'Arkansas Command Strategy (#70)', 'route': '/mission-control/arkansas-command-strategy.html', 'status': 'live'},
    {'system': 'Organizational Constitution (#76)', 'route': '/mission-control/organizational-constitution.html', 'status': 'live'},
]

acos_readiness = min(
    47,
    15
    + len(READINESS_LEVELS) * 2
    + len(COUNTY_PROFILE_SECTIONS) // 2
    + len(LEADERSHIP_ROLES)
    + len(COUNTY_DASHBOARD['domains'])
    + len(HEALTH_INDEX_FACTORS) // 2,
)

out = {
    'version': '1.0',
    'build': 77,
    'updated': today,
    'title': 'Master Arkansas County Operating System (ACOS) v1.0',
    'subtitle': 'Seventy-Five Counties. One Institution.',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/arkansas-county-operating-system.html',
    'constitution': '/docs/MASTER_ARKANSAS_COUNTY_OPERATING_SYSTEM.md',
    'purpose': (
        'Standardized framework for building civic education in every county '
        'while preserving local identity — primary operational framework for statewide expansion.'
    ),
    'governing_principle': (
        'Statewide change is achieved through strong local communities. '
        'Seventy-five strong counties create one strong statewide institution.'
    ),
    'county_philosophy': {
        'title': 'Institutional Philosophy',
        'every_county_living_system': True,
        'questions': COUNTY_PHILOSOPHY_QUESTIONS,
    },
    'county_digital_twin': {
        'title': 'County Digital Twin',
        'description': 'Each county has a digital workspace — operational dashboard, not just a webpage',
        'counties_total': COUNTIES_TOTAL,
        'digital_twins_operational': counties_with_digital_twin,
        'mc_generates_all': True,
        'status': 'specified',
    },
    'county_profile': {
        'title': 'County Profile',
        'sections_total': len(COUNTY_PROFILE_SECTIONS),
        'sections': COUNTY_PROFILE_SECTIONS,
        'living_civic_profile': True,
    },
    'county_leadership_team': {
        'title': 'County Leadership Team',
        'roles_total': len(LEADERSHIP_ROLES),
        'one_volunteer_multiple_roles_initially': True,
        'roles': LEADERSHIP_ROLES,
    },
    'county_goals': {
        'title': 'County Goals',
        'annual_educational_goals': True,
        'examples': COUNTY_GOAL_EXAMPLES,
        'mc_tracks_progress': True,
        'status': 'specified',
    },
    'county_dashboard': COUNTY_DASHBOARD,
    'county_resource_library': {
        'title': 'County Resource Library',
        'items': RESOURCE_LIBRARY,
        'items_total': len(RESOURCE_LIBRARY),
        'live': county_resource_libraries_live > 0,
        'status': 'specified',
    },
    'county_event_calendar': {
        'title': 'County Event Calendar',
        'event_types': EVENT_CALENDAR_TYPES,
        'statewide_calendar_sync': statewide_calendar_sync,
        'live': county_event_calendars_live > 0,
        'status': 'specified',
    },
    'county_listening_reports': {
        'title': 'County Listening Reports',
        'items': LISTENING_REPORT_ITEMS,
        'reports_submitted': county_listening_reports_submitted,
        'mc_aggregates_statewide': True,
        'preserves_county_perspectives': True,
        'status': 'specified',
    },
    'county_readiness_levels': {
        'title': 'County Readiness Levels',
        'levels_total': len(READINESS_LEVELS),
        'levels': READINESS_LEVELS,
        'counties_past_awareness': counties_past_awareness,
        'mc_visualizes_all_counties': True,
        'status': 'specified',
        'note': '6-stage model; extends Command Strategy (#70) 5-stage model',
    },
    'county_health_index': {
        'title': 'County Health Index',
        'factors': HEALTH_INDEX_FACTORS,
        'factors_total': len(HEALTH_INDEX_FACTORS),
        'computed': county_health_index_computed,
        'highlights_strengths_and_support': True,
        'status': 'planned',
    },
    'county_mentorship': {
        'title': 'County Mentorship',
        'stronger_help_emerging': True,
        'types': MENTORSHIP_TYPES,
        'pairs_active': county_mentorship_pairs,
        'collaboration_not_competition': True,
        'status': 'specified',
    },
    'integration': {
        'chain': (
            'Mission Control → Civic Atlas → Education Academy → Relationship OS → '
            'Coalition Network → Citizen Action Center → Knowledge Graph → Campaign Finance Observatory'
        ),
        'each_county_operational_node': True,
        'systems': SYSTEM_CONNECTIONS,
        'extends': 'County Operating System (#31)',
    },
    'long_term_vision': (
        'Twenty years after launch: every county has an active educational dashboard; local leaders '
        'know one another; community conversations year-round; libraries and civic organizations '
        'collaborate; students, teachers, journalists, and citizens find reliable resources. '
        'Every county contributes to statewide civic learning while maintaining local character.'
    ),
    'summary': {
        'counties_total': COUNTIES_TOTAL,
        'counties_scaffolded': counties_scaffolded,
        'counties_with_digital_twin': counties_with_digital_twin,
        'county_dashboards_live': county_dashboards_live,
        'counties_past_awareness': counties_past_awareness,
        'readiness_levels': len(READINESS_LEVELS),
        'profile_sections': len(COUNTY_PROFILE_SECTIONS),
        'leadership_roles': len(LEADERSHIP_ROLES),
        'county_health_index_computed': county_health_index_computed,
        'county_listening_reports_submitted': county_listening_reports_submitted,
        'county_mentorship_pairs': county_mentorship_pairs,
        'arkansas_county_operating_system_readiness_pct': acos_readiness,
        'county_os_readiness_pct': cos.get('summary', {}).get('county_os_readiness_pct', 28),
        'arkansas_command_strategy_readiness_pct': acs.get('summary', {}).get('arkansas_command_strategy_readiness_pct', 39),
        'public_launch_readiness_pct': ex.get('public_launch_readiness', 8),
    },
    'catalog_gaps': [
        '0/75 county digital twins operational — MC generation not implemented',
        '0 counties past Awareness — no founding Education Leaders',
        '0 county dashboards live — operational headquarters not built',
        'County Health Index not computed — factors specified only',
        'County listening reports — 0 submitted; aggregation not live',
        'County event calendars — not per-county; statewide sync off',
        'County resource libraries — not per-county',
        '6-stage readiness vs Command Strategy 5-stage — reconcile models?',
        'Build #77 vs County OS (#31) — ACOS extends but does not replace',
        'Population, districts, libraries not populated on county profiles',
        'County mentorship — 0 pairs; regional planning not operational',
        'Canonical /arkansas/[county] routes still not built',
        'Educational Coverage Score not computed per county',
    ],
    'recommended_next_build': {
        'number': 78,
        'title': 'Implementation Translation Layer & Engineering Artifacts',
        'note': (
            'County digital twin pages, readiness visualization, health index, '
            'listening report intake, event calendar sync, COMP-* specs, GitHub backlog.'
        ),
    },
}

with open(root / 'data/arkansas-county-operating-system.json', 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')

print(
    f'ACOS: {counties_scaffolded}/{COUNTIES_TOTAL} scaffolded, '
    f'{counties_with_digital_twin} digital twins, {acos_readiness}% readiness'
)
