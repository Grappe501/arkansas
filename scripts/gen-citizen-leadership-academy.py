"""
Generate data/citizen-leadership-academy.json — Build #68.
Master Citizen Leadership Academy v1.0.
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
ea = load_json(root / 'data/education-academy.json')
aan = load_json(root / 'data/arkansas-action-network.json')
im = load_json(root / 'data/impact-measurement.json')

ex = mc.get('executive', {})

# Honest zeros
current_learners = 0
graduates_total = 0
education_leaders = 0
city_coordinators = 0
county_directors = 0
civic_fellows = 0
mentorship_relationships = 0
certifications_issued = 0
portfolios_live = 0

SIX_LEVELS = [
    {
        'level': 1, 'id': 'CLA-L1', 'title': 'Civic Learner',
        'purpose': 'Build foundational knowledge',
        'topics': [
            'Citizens United basics', 'Campaign finance history',
            'Constitutional foundations', 'Arkansas civic processes', 'Platform navigation',
        ],
        'outcome': 'Confident learner',
        'enrolled': 0,
        'status': 'partial',
        'route': '/start-here/',
    },
    {
        'level': 2, 'id': 'CLA-L2', 'title': 'Community Ambassador',
        'purpose': 'Comfortably share educational resources',
        'skills': [
            'Answer common questions', 'Recommend learning paths',
            'Share educational materials', 'Invite others into learning',
        ],
        'outcome': 'Trusted community resource',
        'enrolled': 0,
        'status': 'planned',
    },
    {
        'level': 3, 'id': 'CLA-L3', 'title': 'Education Leader',
        'purpose': 'Teach small groups',
        'skills': [
            'Facilitation', 'Discussion leadership', 'Presentation fundamentals',
            'Evidence-based teaching', 'Handling difficult questions respectfully',
        ],
        'outcome': 'Certified Education Leader',
        'enrolled': 0,
        'status': 'planned',
    },
    {
        'level': 4, 'id': 'CLA-L4', 'title': 'City Education Coordinator',
        'purpose': 'Support education across an entire city',
        'skills': [
            'Volunteer coordination', 'Event planning', 'Community partnerships',
            'Local resource development', 'Leadership coaching',
        ],
        'outcome': 'City leadership certification',
        'enrolled': 0,
        'status': 'planned',
    },
    {
        'level': 5, 'id': 'CLA-L5', 'title': 'County Education Director',
        'purpose': 'Lead county-wide educational infrastructure',
        'skills': [
            'Strategic planning', 'Coalition development', 'Leadership recruitment',
            'Mentorship', 'Community expansion',
        ],
        'outcome': 'County education leadership',
        'enrolled': 0,
        'status': 'planned',
        'route': '/mission-control/county-os.html',
    },
    {
        'level': 6, 'id': 'CLA-L6', 'title': 'Arkansas Civic Fellow',
        'purpose': 'Develop statewide institutional leaders',
        'skills': [
            'Advanced constitutional literacy', 'Research interpretation',
            'Public presentations', 'Leadership development',
            'Institutional stewardship', 'Academy instruction',
        ],
        'outcome': 'Statewide mentor and institutional steward',
        'enrolled': 0,
        'status': 'planned',
    },
]

ACADEMY_PHILOSOPHY_STAGES = [
    {'stage': 'Learn', 'status': 'partial'},
    {'stage': 'Practice', 'status': 'planned'},
    {'stage': 'Teach', 'status': 'planned'},
    {'stage': 'Lead', 'status': 'planned'},
    {'stage': 'Mentor', 'status': 'planned'},
    {'stage': 'Multiply', 'status': 'planned'},
]

LEARNING_MODEL = [
    'Reading', 'Interactive learning', 'Video instruction', 'Knowledge checks',
    'Community practice', 'Reflection', 'Mentorship', 'Certification',
]

LEADERSHIP_COMPETENCIES = [
    'Historical understanding', 'Constitutional literacy', 'Research skills',
    'Communication', 'Facilitation', 'Critical thinking',
    'Community leadership', 'Ethical stewardship',
]

PORTFOLIO_CONTENTS = [
    'Completed lessons', 'Certificates', 'Presentations delivered',
    'Community conversations', 'Educational reflections',
    'Mentorship activity', 'Research contributions',
]

CONTINUING_EDUCATION = [
    'New research briefings', 'Updated lesson modules', 'Legal developments',
    'Historical discoveries', 'Presentation improvements', 'Annual refresher opportunities',
]

GRADUATION_COMMITMENT = [
    'I will pursue truth through evidence.',
    'I will teach with humility.',
    'I will welcome sincere questions.',
    'I will distinguish facts from opinion.',
    'I will encourage respectful dialogue.',
    'I will continue learning.',
    'I will help strengthen civic understanding in Arkansas.',
]

ACADEMY_DASHBOARD_METRICS = [
    {'id': 'CLA-M1', 'metric': 'Current learners', 'current': current_learners, 'status': 'live'},
    {'id': 'CLA-M2', 'metric': 'Graduates', 'current': graduates_total, 'status': 'live'},
    {'id': 'CLA-M3', 'metric': 'Education Leaders', 'current': education_leaders, 'status': 'live'},
    {'id': 'CLA-M4', 'metric': 'City Coordinators', 'current': city_coordinators, 'status': 'live'},
    {'id': 'CLA-M5', 'metric': 'County Directors', 'current': county_directors, 'status': 'live'},
    {'id': 'CLA-M6', 'metric': 'Arkansas Civic Fellows', 'current': civic_fellows, 'status': 'live'},
    {'id': 'CLA-M7', 'metric': 'Mentorship relationships', 'current': mentorship_relationships, 'status': 'planned'},
    {'id': 'CLA-M8', 'metric': 'Course completion', 'current': 0, 'unit': 'percent', 'status': 'planned'},
    {'id': 'CLA-M9', 'metric': 'Certification trends', 'current': certifications_issued, 'status': 'planned'},
    {'id': 'CLA-M10', 'metric': 'Leadership pipeline health', 'current': 'empty', 'status': 'planned'},
]

SYSTEM_CONNECTIONS = [
    {'system': 'Community Education Academy (#28)', 'route': '/mission-control/education-academy.html', 'status': 'partial', 'note': '4-stage foundation'},
    {'system': 'Curriculum (#33)', 'route': '/mission-control/curriculum.html', 'status': 'partial'},
    {'system': 'Research Library (#37)', 'route': '/mission-control/research-library.html', 'status': 'partial'},
    {'system': 'Knowledge Graph', 'route': '/mission-control/knowledge-graph.html', 'status': 'planned'},
    {'system': 'Arkansas Action Network (#64)', 'route': '/mission-control/arkansas-action-network.html', 'status': 'live'},
    {'system': 'Citizen Action Center (#62)', 'route': '/mission-control/citizen-action-center.html', 'status': 'live'},
    {'system': 'Coalition Network (#61)', 'route': '/mission-control/coalition-network.html', 'status': 'live'},
    {'system': 'Civic Atlas (#58)', 'route': '/mission-control/civic-atlas.html', 'status': 'live'},
    {'system': 'Impact Measurement (#67)', 'route': '/mission-control/impact-measurement.html', 'status': 'live'},
    {'system': 'Mission Control', 'route': '/mission-control/', 'status': 'live'},
]

citizen_leadership_academy_readiness = min(
    46,
    14 + len(SIX_LEVELS) * 3 + (2 if ea else 0),
)

out = {
    'version': '1.0',
    'build': 68,
    'updated': today,
    'title': 'Master Citizen Leadership Academy v1.0',
    'subtitle': "Developing Arkansas's Next Generation of Civic Education Leaders",
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/citizen-leadership-academy.html',
    'constitution': '/docs/MASTER_CITIZEN_LEADERSHIP_ACADEMY.md',
    'legacy_academy_route': '/mission-control/education-academy.html',
    'purpose': (
        'Identify, educate, mentor, certify, and support Arkansans as trusted civic education leaders — '
        'the human engine of the institution.'
    ),
    'governing_principle': (
        'People educate people. Prepare ordinary Arkansans to become extraordinary civic education leaders '
        'through patience, scholarship, transparency, and lifelong learning.'
    ),
    'highest_strategic_priority': True,
    'human_engine': True,
    'produces_teachers_not_spokespeople': True,
    'academy_mission': [
        'Explain Citizens United accurately',
        'Teach constitutional concepts clearly',
        'Lead respectful community discussions',
        'Use evidence responsibly',
        'Build local educational networks',
        'Mentor future Education Leaders',
    ],
    'academy_philosophy': {
        'progression': 'Learn → Practice → Teach → Lead → Mentor → Multiply',
        'stages': ACADEMY_PHILOSOPHY_STAGES,
        'every_graduate_develops_future_leaders': True,
    },
    'six_certification_levels': SIX_LEVELS,
    'learning_model': {
        'title': 'Active Learning Model',
        'steps': LEARNING_MODEL,
        'active_not_passive': True,
        'status': 'planned',
    },
    'leadership_competencies': {
        'title': 'Leadership Competencies',
        'competencies': LEADERSHIP_COMPETENCIES,
        'tracked_over_time': True,
        'status': 'planned',
    },
    'leadership_portfolio': {
        'title': 'Leadership Portfolio',
        'living_portfolio': True,
        'contents': PORTFOLIO_CONTENTS,
        'portfolios_live': portfolios_live,
        'status': 'planned',
    },
    'leadership_mentorship': {
        'title': 'Leadership Mentorship',
        'every_graduate_mentors': True,
        'visualize_networks': True,
        'relationships': mentorship_relationships,
        'status': 'planned',
    },
    'continuing_education': {
        'title': 'Continuing Education',
        'offerings': CONTINUING_EDUCATION,
        'never_ends': True,
        'status': 'planned',
    },
    'academy_dashboard': {
        'title': 'Academy Dashboard',
        'metrics': ACADEMY_DASHBOARD_METRICS,
        'measurable_pipeline': True,
        'status': 'partial',
    },
    'graduation_commitment': {
        'title': 'Graduation Commitment',
        'voluntary': True,
        'statements': GRADUATION_COMMITMENT,
        'status': 'specified',
    },
    'integration': {
        'chain': (
            'Curriculum → Research Library → Knowledge Graph → Community Education → '
            'Coalition Network → Citizen Action Center → Civic Atlas → Mission Control'
        ),
        'systems': SYSTEM_CONNECTIONS,
        'extends': 'Community Education Academy (#28) with 6-level certification system',
    },
    'long_term_vision': (
        'Thousands of graduates active statewide. Every county has mentors. Every major city has a '
        'leadership team. New generations teach with integrity, curiosity, and respect for evidence.'
    ),
    'summary': {
        'certification_levels': len(SIX_LEVELS),
        'levels_partial_or_live': sum(1 for l in SIX_LEVELS if l['status'] in ('live', 'partial')),
        'current_learners': current_learners,
        'graduates_total': graduates_total,
        'education_leaders': education_leaders,
        'city_coordinators': city_coordinators,
        'county_directors': county_directors,
        'civic_fellows': civic_fellows,
        'mentorship_relationships': mentorship_relationships,
        'certifications_issued': certifications_issued,
        'portfolios_live': portfolios_live,
        'citizen_leadership_academy_readiness_pct': citizen_leadership_academy_readiness,
        'education_academy_readiness_pct': ea.get('summary', {}).get('academy_readiness_pct', 26) if isinstance(ea.get('summary'), dict) else 26,
        'public_launch_readiness_pct': ex.get('public_launch_readiness', 8),
    },
    'catalog_gaps': [
        '0 current learners — no enrollment or LMS integration',
        '0 graduates at all 6 certification levels',
        '0 Education Leaders certified — Level 3 empty',
        'Learning model specified — no knowledge checks, video, or certification workflow',
        'Leadership portfolios not built — 0 living portfolios',
        'Mentorship network visualization not implemented — 0 relationships',
        'Build #68 Citizen Leadership Academy vs Build #28 Education Academy — unify routes?',
        '6 certification levels vs Action Network (#64) 8-level pyramid — mapping needed',
        'Graduation commitment specified — no public ceremony or badge system',
        'Continuing education modules not created — no refresher content',
        'Competency tracking not wired — 8 competencies planned only',
        'Academy instruction role (Level 6) — no instructor certification path',
    ],
    'recommended_next_build': {
        'number': 69,
        'title': 'Implementation Translation Layer & Engineering Artifacts',
        'note': (
            'LMS schema, certification workflow, portfolio UI, mentorship graph, competency tracking, '
            'level routing, route inventory, COMP-* specs, GitHub backlog.'
        ),
    },
}

with open(root / 'data/citizen-leadership-academy.json', 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')

print(
    f'Citizen Leadership Academy: {len(SIX_LEVELS)} levels, '
    f'{graduates_total} graduates, {education_leaders} leaders, '
    f'{citizen_leadership_academy_readiness}% readiness'
)
