"""
Generate data/executive-institution.json — Build #94.
Master Executive Institution — Complete Governance & Leadership Architecture v1.0.
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
ckp = load_json(root / 'data/civic-knowledge-platform.json')
lb = load_json(root / 'data/localbrain-architecture.json')
pmo = load_json(root / 'data/pmo-execution-office.json')

ex = mc.get('executive', {})

# Honest operational metrics
executive_dashboard_live = False
meeting_rhythm_operational = False
decision_framework_tracked = False
departments_with_localbrain = 0
leadership_vacancies = 11

LEADERSHIP_PURPOSES = [
    'Serve the mission',
    'Support volunteers',
    'Protect public trust',
    'Strengthen civic education',
    'Develop future leaders',
]

EXECUTIVE_OFFICES = [
    {'id': 'EX-01', 'office': 'Executive Director (or equivalent)', 'filled': False, 'volunteer': None},
    {'id': 'EX-02', 'office': 'Deputy Director', 'filled': False, 'volunteer': None},
    {'id': 'EX-03', 'office': 'Chief Research Officer', 'filled': False, 'volunteer': None},
    {'id': 'EX-04', 'office': 'Chief Technology Officer', 'filled': False, 'volunteer': None},
    {'id': 'EX-05', 'office': 'Chief Education Officer', 'filled': False, 'volunteer': None},
    {'id': 'EX-06', 'office': 'Chief Community Officer', 'filled': False, 'volunteer': None},
    {'id': 'EX-07', 'office': 'Chief Coalition Officer', 'filled': False, 'volunteer': None},
    {'id': 'EX-08', 'office': 'Chief Communications Officer', 'filled': False, 'volunteer': None},
    {'id': 'EX-09', 'office': 'Chief Operations Officer', 'filled': False, 'volunteer': None},
    {'id': 'EX-10', 'office': 'Chief Mission Control Officer', 'filled': False, 'volunteer': None},
    {'id': 'EX-11', 'office': 'Chief Volunteer Officer', 'filled': False, 'volunteer': None},
    {'id': 'EX-12', 'office': 'Chief Data & AI Officer', 'filled': False, 'volunteer': None},
]

leadership_vacancies = sum(1 for o in EXECUTIVE_OFFICES if not o['filled'])

DEPARTMENTS = [
    {'id': 'DEPT-01', 'department': 'Research', 'route': '/mission-control/arkansas-research-institute.html', 'localbrain': False, 'dashboard': 'partial'},
    {'id': 'DEPT-02', 'department': 'Education', 'route': '/mission-control/education-academy.html', 'localbrain': False, 'dashboard': 'partial'},
    {'id': 'DEPT-03', 'department': 'Technology', 'route': '/mission-control/platform.html', 'localbrain': False, 'dashboard': 'partial'},
    {'id': 'DEPT-04', 'department': 'Mission Control', 'route': '/mission-control/', 'localbrain': False, 'dashboard': 'live'},
    {'id': 'DEPT-05', 'department': 'Communications', 'route': '/mission-control/arkansas-communications.html', 'localbrain': False, 'dashboard': 'partial'},
    {'id': 'DEPT-06', 'department': 'Volunteer Development', 'route': '/mission-control/volunteer-funding-constitution.html', 'localbrain': False, 'dashboard': 'partial'},
    {'id': 'DEPT-07', 'department': 'Community Engagement', 'route': '/mission-control/arkansas-community-listening.html', 'localbrain': False, 'dashboard': 'partial'},
    {'id': 'DEPT-08', 'department': 'Coalition Development', 'route': '/mission-control/coalition.html', 'localbrain': False, 'dashboard': 'partial'},
    {'id': 'DEPT-09', 'department': 'County Operations', 'route': '/mission-control/arkansas-county-operating-system.html', 'localbrain': False, 'dashboard': 'partial'},
    {'id': 'DEPT-10', 'department': 'City Operations', 'route': '/mission-control/arkansas-city-operating-system.html', 'localbrain': False, 'dashboard': 'partial'},
    {'id': 'DEPT-11', 'department': 'Neighborhood Operations', 'route': '/mission-control/arkansas-neighborhood-operating-system.html', 'localbrain': False, 'dashboard': 'partial'},
    {'id': 'DEPT-12', 'department': 'Governance', 'route': '/mission-control/organizational-constitution.html', 'localbrain': False, 'dashboard': 'partial'},
    {'id': 'DEPT-13', 'department': 'Finance & Compliance', 'route': None, 'localbrain': False, 'dashboard': 'planned'},
    {'id': 'DEPT-14', 'department': 'Project Management Office', 'route': '/mission-control/pmo-execution-office.html', 'localbrain': False, 'dashboard': 'partial'},
]

departments_with_localbrain = sum(1 for d in DEPARTMENTS if d['localbrain'])

MEETING_RHYTHM = [
    {'cadence': 'Weekly', 'focus': 'Operational review', 'status': 'specified'},
    {'cadence': 'Monthly', 'focus': 'Strategic review', 'status': 'specified'},
    {'cadence': 'Quarterly', 'focus': 'Institutional review', 'status': 'specified'},
    {'cadence': 'Annually', 'focus': 'Mission review', 'status': 'specified'},
]

DECISION_STEPS = [
    {'step': 1, 'stage': 'Issue identified', 'status': 'specified'},
    {'step': 2, 'stage': 'Research completed', 'status': 'specified'},
    {'step': 3, 'stage': 'Alternatives evaluated', 'status': 'specified'},
    {'step': 4, 'stage': 'Volunteer input considered', 'status': 'specified'},
    {'step': 5, 'stage': 'Leadership decision', 'status': 'specified'},
    {'step': 6, 'stage': 'Mission Control documentation', 'status': 'specified'},
    {'step': 7, 'stage': 'Implementation', 'status': 'specified'},
    {'step': 8, 'stage': 'Review', 'status': 'specified'},
]

ACCOUNTABILITY_FIELDS = [
    'Annual goals', 'Quarterly objectives', 'Current projects',
    'Performance indicators', 'Documentation',
]

CROSS_DEPT_EXAMPLES = [
    'Research supports Communications',
    'Communications supports Community',
    'Community supports Leadership',
    'Leadership supports Volunteers',
    'Technology supports everyone',
]

LEADERSHIP_DEVELOPMENT = [
    'Mentoring', 'Documentation', 'Delegation', 'Knowledge transfer', 'Succession planning',
]

EXEC_DASHBOARD_INDICATORS = [
    {'id': 'EI-D01', 'indicator': 'Department health', 'current': 0, 'unit': '%', 'status': 'planned'},
    {'id': 'EI-D02', 'indicator': 'Project completion', 'current': ex.get('overall_completion', mc.get('build', 93)), 'unit': '%', 'status': 'partial'},
    {'id': 'EI-D03', 'indicator': 'Volunteer capacity', 'current': 0, 'status': 'planned'},
    {'id': 'EI-D04', 'indicator': 'Leadership vacancies', 'current': leadership_vacancies, 'status': 'partial'},
    {'id': 'EI-D05', 'indicator': 'Strategic priorities', 'current': 0, 'status': 'planned'},
    {'id': 'EI-D06', 'indicator': 'Institutional risks', 'current': len(mc.get('builds', [{}])[0].get('risks', [])) if mc.get('builds') else 0, 'status': 'partial'},
    {'id': 'EI-D07', 'indicator': 'Upcoming milestones', 'current': days_remaining, 'unit': ' days', 'status': 'partial'},
    {'id': 'EI-D08', 'indicator': 'Executive decisions pending', 'current': 0, 'status': 'planned'},
]

ETHICS_COMMITMENTS = [
    'Evidence-based decision-making',
    'Transparency',
    'Respectful collaboration',
    'Responsible stewardship',
    'Volunteer empowerment',
    'Protection of institutional independence',
]

executive_institution_readiness = min(
    68,
    14
    + len(LEADERSHIP_PURPOSES) // 2
    + len(EXECUTIVE_OFFICES) // 2
    + len(DEPARTMENTS) // 2
    + len(MEETING_RHYTHM)
    + len(DECISION_STEPS) // 2
    + len(ACCOUNTABILITY_FIELDS) // 2
    + len(CROSS_DEPT_EXAMPLES) // 2
    + len(LEADERSHIP_DEVELOPMENT) // 2
    + len(EXEC_DASHBOARD_INDICATORS) // 2
    + len(ETHICS_COMMITMENTS) // 2
    + (2 if executive_dashboard_live else 0),
)

out = {
    'version': '1.0',
    'build': 94,
    'updated': today,
    'completion_target_date': completion_target_date,
    'title': 'Master Executive Institution v1.0',
    'subtitle': 'The Complete Governance & Leadership Architecture',
    'tagline': 'Leadership Is a Responsibility',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/executive-institution.html',
    'constitution': '/docs/MASTER_EXECUTIVE_INSTITUTION.md',
    'purpose': (
        'By January 2027, Citizens United Facts operates as a well-organized institution — '
        'not a loose collection of volunteers. Defines how leadership functions, decisions are '
        'made, departments coordinate, and accountability is maintained while remaining '
        'all-volunteer. Organized enough for extraordinary things; flexible enough to enjoy serving.'
    ),
    'governing_principle': (
        'Leadership exists to make it easier for volunteers to succeed. When volunteers succeed, '
        'communities grow. When communities grow, civic understanding grows. When civic '
        'understanding grows, Arkansas becomes stronger. The Executive Institution exists to '
        'make that chain of success possible every single day.'
    ),
    'founders_principle': (
        'Great institutions are not built because a few people work harder. They are built because '
        'thousands of volunteers know exactly where they fit, understand the mission, trust one '
        'another, and are supported by thoughtful leadership and disciplined organization.'
    ),
    'institutional_philosophy': {
        'title': 'Institutional Philosophy',
        'leadership_purposes': LEADERSHIP_PURPOSES,
        'not_position_of_authority': True,
        'leadership_is_responsibility': True,
    },
    'executive_institution': {
        'title': 'The Executive Institution',
        'executive_office_coordinates_not_controls': True,
        'permanent_departments_supported': True,
        'every_department_advances_mission': True,
    },
    'executive_leadership_council': {
        'title': 'Executive Leadership Council',
        'offices': EXECUTIVE_OFFICES,
        'functional_responsibilities_not_prestige': True,
        'one_volunteer_multiple_roles': True,
        'offices_filled': sum(1 for o in EXECUTIVE_OFFICES if o['filled']),
        'offices_total': len(EXECUTIVE_OFFICES),
        'status': 'planned',
    },
    'permanent_departments': {
        'title': 'Permanent Departments',
        'departments': DEPARTMENTS,
        'each_has_localbrain_and_dashboard': True,
        'departments_with_localbrain': departments_with_localbrain,
        'departments_total': len(DEPARTMENTS),
        'status': 'partial',
    },
    'executive_meetings': {
        'title': 'Executive Meetings',
        'rhythm': MEETING_RHYTHM,
        'mc_prepares_briefing_materials': True,
        'operational': meeting_rhythm_operational,
        'status': 'specified',
    },
    'decision_framework': {
        'title': 'Decision Framework',
        'steps': DECISION_STEPS,
        'institutional_memory_preserved': True,
        'tracked_in_mc': decision_framework_tracked,
        'status': 'specified',
    },
    'delegation_philosophy': {
        'title': 'Delegation Philosophy',
        'delegated_close_to_work': True,
        'county_by_county_leadership': True,
        'city_by_city_leadership': True,
        'research_by_research_leadership': True,
        'mc_coordinates_not_centralizes': True,
    },
    'accountability': {
        'title': 'Accountability',
        'fields_per_department': ACCOUNTABILITY_FIELDS,
        'mc_reports_transparently': True,
        'status': 'specified',
    },
    'cross_department_coordination': {
        'title': 'Cross-Department Coordination',
        'examples': CROSS_DEPT_EXAMPLES,
        'mc_visualizes_continuously': True,
        'status': 'partial',
    },
    'leadership_development': {
        'title': 'Leadership Development',
        'responsibilities': LEADERSHIP_DEVELOPMENT,
        'healthy_institutions_produce_leaders': True,
        'status': 'specified',
    },
    'executive_dashboard': {
        'title': 'Executive Dashboard',
        'indicators': EXEC_DASHBOARD_INDICATORS,
        'live': executive_dashboard_live,
        'leadership_operates_from_shared_information': True,
        'status': 'planned',
    },
    'ethics_integrity': {
        'title': 'Ethics & Integrity',
        'commitments': ETHICS_COMMITMENTS,
        'public_trust_highest_priority': True,
        'status': 'specified',
    },
    'integration': {
        'chain': (
            'Mission Control → PMO → LocalBrains → Research Institute → '
            'Community Education Academy → County/City/Neighborhood OS → '
            'Communications → Coalition Network → Volunteer Network'
        ),
        'every_component_reports_through_governance': True,
        'systems': [
            {'system': 'PMO & Execution Office (#89)', 'route': '/mission-control/pmo-execution-office.html', 'status': 'live'},
            {'system': 'Operating Manual (#90)', 'route': '/mission-control/institutional-operating-manual.html', 'status': 'live'},
            {'system': 'LocalBrain Architecture (#92)', 'route': '/mission-control/localbrain-architecture.html', 'status': 'live'},
            {'system': 'Knowledge Platform (#93)', 'route': '/mission-control/civic-knowledge-platform.html', 'status': 'live'},
            {'system': 'Organizational Constitution (#76)', 'route': '/mission-control/organizational-constitution.html', 'status': 'live'},
            {'system': 'Execution Schedule (#88)', 'route': '/mission-control/execution-schedule.html', 'status': 'live'},
        ],
    },
    'long_term_vision': (
        'By January 2027, Citizens United Facts functions as a mature volunteer institution. '
        'Leadership meetings organized. Departments coordinate effectively. Mission Control '
        'provides real-time visibility. Volunteers understand roles. Decisions documented. '
        'Knowledge preserved. Sustained growth without depending on any one individual.'
    ),
    'summary': {
        'completion_target_date': completion_target_date,
        'days_remaining': days_remaining,
        'executive_institution_readiness_pct': executive_institution_readiness,
        'civic_knowledge_platform_readiness_pct': ckp.get('summary', {}).get('civic_knowledge_platform_readiness_pct', 58),
        'localbrain_architecture_readiness_pct': lb.get('summary', {}).get('localbrain_architecture_readiness_pct', 60),
        'pmo_readiness_pct': pmo.get('summary', {}).get('pmo_execution_office_readiness_pct', 60),
        'executive_dashboard_live': executive_dashboard_live,
        'meeting_rhythm_operational': meeting_rhythm_operational,
        'decision_framework_tracked': decision_framework_tracked,
        'leadership_vacancies': leadership_vacancies,
        'executive_offices_total': len(EXECUTIVE_OFFICES),
        'executive_offices_filled': sum(1 for o in EXECUTIVE_OFFICES if o['filled']),
        'departments_total': len(DEPARTMENTS),
        'departments_with_localbrain': departments_with_localbrain,
        'institutional_completion_pct': ex.get('overall_completion', mc.get('build', 93)),
    },
    'catalog_gaps': [
        'Executive dashboard not live',
        'All 12 leadership council offices vacant',
        'No department LocalBrains assigned yet',
        'Meeting rhythm not scheduled or tracked',
        'Decision framework not tracked in Mission Control',
        'Department accountability metrics not populated',
        'Cross-department coordination not visualized',
        'Leadership development / succession not tracked',
        'Executive briefing materials not auto-generated',
        'Volunteer capacity not measured',
        'Pending executive decisions queue not operational',
        'Finance & Compliance department has no dashboard',
    ],
    'recommended_next_build': {
        'number': 95,
        'title': 'Master Arkansas Action Network',
        'note': (
            'From learning to local civic participation — Action Center, participation library, '
            'legislative resources, community pages, neutral civic engagement.'
        ),
    },
}

with open(root / 'data/executive-institution.json', 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')

print(
    f'Executive Institution: {len(EXECUTIVE_OFFICES)} offices, '
    f'{len(DEPARTMENTS)} departments, {executive_institution_readiness}% readiness'
)
