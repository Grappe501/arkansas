"""
Generate data/institutional-continuous-improvement.json — Build #98.
Master Institutional Self-Build & Continuous Improvement System v1.0.
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
ilc = load_json(root / 'data/institutional-launch-certification.json')
pmo = load_json(root / 'data/pmo-execution-office.json')

ex = mc.get('executive', {})

# Honest operational metrics
improvement_dashboard_live = False
improvement_backlog_items = 0
innovation_pipeline_active = 0
lessons_learned_entries = 0
ai_recommendations_pending = 0
volunteer_suggestions = 0
annual_assessments_completed = 0

IMPROVEMENT_CYCLE = [
    {'step': 1, 'stage': 'Observe', 'status': 'specified'},
    {'step': 2, 'stage': 'Measure', 'status': 'specified'},
    {'step': 3, 'stage': 'Analyze', 'status': 'specified'},
    {'step': 4, 'stage': 'Improve', 'status': 'specified'},
    {'step': 5, 'stage': 'Verify', 'status': 'specified'},
    {'step': 6, 'stage': 'Document', 'status': 'partial'},
    {'step': 7, 'stage': 'Teach', 'status': 'planned'},
    {'step': 8, 'stage': 'Repeat', 'status': 'specified'},
]

SOURCES_OF_IMPROVEMENT = [
    'Research updates',
    'Volunteer suggestions',
    'Education Leaders',
    'Community conversations',
    'Coalition partners',
    'Mission Control metrics',
    'AI recommendations',
    'Public questions',
    'Technology advances',
    'Lessons learned',
    'Launch certification gaps',
]

ANNUAL_ASSESSMENT_QUESTIONS = [
    'What worked well?',
    'What created confusion?',
    'What should be simplified?',
    'What should be expanded?',
    'What no longer serves the mission?',
    'What should be retired?',
]

IMPROVEMENT_BACKLOG_CATEGORIES = [
    {'id': 'IB-01', 'category': 'Research improvements', 'items': 0, 'status': 'planned'},
    {'id': 'IB-02', 'category': 'Technology improvements', 'items': 0, 'status': 'planned'},
    {'id': 'IB-03', 'category': 'Educational improvements', 'items': 0, 'status': 'planned'},
    {'id': 'IB-04', 'category': 'Volunteer improvements', 'items': 0, 'status': 'planned'},
    {'id': 'IB-05', 'category': 'Leadership improvements', 'items': 0, 'status': 'planned'},
    {'id': 'IB-06', 'category': 'Community improvements', 'items': 0, 'status': 'planned'},
    {'id': 'IB-07', 'category': 'Coalition improvements', 'items': 0, 'status': 'planned'},
    {'id': 'IB-08', 'category': 'Documentation improvements', 'items': 0, 'status': 'planned'},
    {'id': 'IB-09', 'category': 'Governance improvements', 'items': 0, 'status': 'planned'},
    {'id': 'IB-10', 'category': 'AI improvements', 'items': 0, 'status': 'planned'},
]

INNOVATION_PIPELINE = [
    {'step': 1, 'stage': 'Idea Submitted', 'status': 'specified'},
    {'step': 2, 'stage': 'Research', 'status': 'specified'},
    {'step': 3, 'stage': 'Discussion', 'status': 'specified'},
    {'step': 4, 'stage': 'Prototype', 'status': 'planned'},
    {'step': 5, 'stage': 'Pilot', 'status': 'planned'},
    {'step': 6, 'stage': 'Evaluation', 'status': 'planned'},
    {'step': 7, 'stage': 'Approval', 'status': 'planned'},
    {'step': 8, 'stage': 'Institution-wide Adoption', 'status': 'planned'},
]

VOLUNTEER_IMPROVEMENT_EXAMPLES = [
    'Suggest better lessons',
    'Improve documentation',
    'Recommend new research',
    'Simplify processes',
    'Improve presentations',
    'Identify outdated information',
]

AI_ASSISTED_IMPROVEMENT = [
    'Frequently asked questions',
    'Repeated volunteer challenges',
    'Research gaps',
    'Documentation gaps',
    'Broken workflows',
    'Emerging opportunities',
]

LESSONS_LEARNED_QUESTIONS = [
    'What succeeded?',
    'What failed?',
    'What surprised us?',
    'What should future volunteers know?',
]

EXEC_DASHBOARD_INDICATORS = [
    {'id': 'ICI-D01', 'indicator': 'Improvement projects', 'current': 0, 'status': 'planned'},
    {'id': 'ICI-D02', 'indicator': 'Projects completed', 'current': len(mc.get('builds', [])), 'status': 'partial'},
    {'id': 'ICI-D03', 'indicator': 'Ideas awaiting review', 'current': volunteer_suggestions + ai_recommendations_pending, 'status': 'planned'},
    {'id': 'ICI-D04', 'indicator': 'Volunteer suggestions', 'current': volunteer_suggestions, 'status': 'planned'},
    {'id': 'ICI-D05', 'indicator': 'AI recommendations', 'current': ai_recommendations_pending, 'status': 'planned'},
    {'id': 'ICI-D06', 'indicator': 'Department improvement scores', 'current': 0, 'unit': '%', 'status': 'planned'},
    {'id': 'ICI-D07', 'indicator': 'Institutional improvement trend', 'current': ex.get('overall_completion', mc.get('build', 97)), 'unit': '%', 'status': 'partial'},
]

HEALTH_TREND_PERIODS = [
    'Today', 'Last Month', 'Last Quarter', 'Last Year', 'Since January 2027',
]

RECOGNITION_CATEGORIES = [
    'Volunteers who improve systems',
    'Education Leaders who develop better resources',
    'Researchers who strengthen accuracy',
    'Coalition partners who contribute new ideas',
    'Communities that identify meaningful improvements',
]

institutional_continuous_improvement_readiness = min(
    66,
    14
    + len(IMPROVEMENT_CYCLE)
    + len(SOURCES_OF_IMPROVEMENT) // 2
    + len(ANNUAL_ASSESSMENT_QUESTIONS) // 2
    + len(IMPROVEMENT_BACKLOG_CATEGORIES) // 2
    + len(INNOVATION_PIPELINE) // 2
    + len(VOLUNTEER_IMPROVEMENT_EXAMPLES) // 2
    + len(AI_ASSISTED_IMPROVEMENT) // 2
    + len(LESSONS_LEARNED_QUESTIONS) // 2
    + len(EXEC_DASHBOARD_INDICATORS) // 2
    + len(HEALTH_TREND_PERIODS) // 2
    + len(RECOGNITION_CATEGORIES) // 2
    + (2 if improvement_dashboard_live else 0),
)

out = {
    'version': '1.0',
    'build': 98,
    'updated': today,
    'completion_target_date': completion_target_date,
    'v1_completion_begins_improvement': True,
    'title': 'Master Institutional Self-Build & Continuous Improvement System v1.0',
    'subtitle': 'The Institution That Improves Itself',
    'tagline': 'Never Finished. Always Improving.',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/institutional-continuous-improvement.html',
    'constitution': '/docs/MASTER_INSTITUTIONAL_CONTINUOUS_IMPROVEMENT.md',
    'purpose': (
        'January 2027 V1 completion begins permanent learning and improvement. Institution '
        'continually evaluates itself, identifies weaknesses, improves operations, strengthens '
        'resources, adapts to new research, technologies, and community needs. Mission Control '
        'monitors improvement with same rigor as construction.'
    ),
    'governing_principle': (
        'Completion is a milestone. Improvement is a culture. Every volunteer, conversation, '
        'lesson, research paper, community, and year should leave Citizens United Facts stronger '
        'than before. That is how an institution earns the privilege of serving Arkansas for '
        'generations.'
    ),
    'founders_principle': (
        'No institution is perfect. The strongest recognize imperfections, learn from them, and '
        'improve without losing sight of mission. Citizens United Facts should become known for '
        'quality civic education, humility, willingness to learn, and commitment to continual '
        'improvement.'
    ),
    'institutional_philosophy': {
        'title': 'Institutional Philosophy',
        'every_day_a_little_better': True,
        'improvement_intentional': True,
        'improvement_measured': True,
        'improvement_documented': True,
        'improvement_never_stops': True,
    },
    'continuous_improvement_cycle': {
        'title': 'The Continuous Improvement Cycle',
        'steps': IMPROVEMENT_CYCLE,
        'mc_visualizes_across_institution': True,
        'status': 'specified',
    },
    'sources_of_improvement': {
        'title': 'Sources of Improvement',
        'sources': SOURCES_OF_IMPROVEMENT,
        'every_observation_opportunity': True,
        'status': 'specified',
    },
    'annual_institutional_assessment': {
        'title': 'Annual Institutional Assessment',
        'questions': ANNUAL_ASSESSMENT_QUESTIONS,
        'every_department_annually': True,
        'assessments_completed': annual_assessments_completed,
        'status': 'planned',
    },
    'improvement_backlog': {
        'title': 'Improvement Backlog',
        'categories': IMPROVEMENT_BACKLOG_CATEGORIES,
        'permanent_backlog': True,
        'total_items': improvement_backlog_items,
        'captured_prioritized_tracked': True,
        'status': 'planned',
    },
    'innovation_pipeline': {
        'title': 'Innovation Pipeline',
        'stages': INNOVATION_PIPELINE,
        'encourages_innovation_without_sacrificing_quality': True,
        'active_items': innovation_pipeline_active,
        'status': 'specified',
    },
    'volunteer_improvement_program': {
        'title': 'Volunteer Improvement Program',
        'examples': VOLUNTEER_IMPROVEMENT_EXAMPLES,
        'every_volunteer_can_contribute': True,
        'suggestions_received': volunteer_suggestions,
        'status': 'planned',
    },
    'ai_assisted_improvement': {
        'title': 'AI-Assisted Improvement',
        'identifies': AI_ASSISTED_IMPROVEMENT,
        'mc_reviews_before_implementation': True,
        'recommendations_pending': ai_recommendations_pending,
        'status': 'planned',
    },
    'lessons_learned_library': {
        'title': 'Lessons Learned Library',
        'questions': LESSONS_LEARNED_QUESTIONS,
        'part_of_institutional_memory': True,
        'entries': lessons_learned_entries,
        'status': 'planned',
    },
    'executive_improvement_dashboard': {
        'title': 'Executive Improvement Dashboard',
        'indicators': EXEC_DASHBOARD_INDICATORS,
        'live': improvement_dashboard_live,
        'leadership_knows_where_progress_occurs': True,
        'status': 'planned',
    },
    'institutional_health_trend': {
        'title': 'Institutional Health Trend',
        'periods': HEALTH_TREND_PERIODS,
        'measures_improvement_over_time': True,
        'not_snapshots_only': True,
        'status': 'planned',
    },
    'recognition': {
        'title': 'Recognition',
        'categories': RECOGNITION_CATEGORIES,
        'improvement_part_of_culture': True,
        'status': 'planned',
    },
    'integration': {
        'chain': (
            'Mission Control → Digital Twin → PMO → Research Institute → '
            'Community Education Academy → Volunteer Network → Knowledge Platform → '
            'Operating Manual → AI Institution'
        ),
        'every_component_continually_improves': True,
        'systems': [
            {'system': 'Launch Certification (#97)', 'route': '/mission-control/institutional-launch-certification.html', 'status': 'live'},
            {'system': 'PMO (#89)', 'route': '/mission-control/pmo-execution-office.html', 'status': 'live'},
            {'system': 'Knowledge Platform (#93)', 'route': '/mission-control/civic-knowledge-platform.html', 'status': 'live'},
            {'system': 'AI Institution (#91)', 'route': '/mission-control/ai-institution.html', 'status': 'live'},
            {'system': 'Operating Manual (#90)', 'route': '/mission-control/institutional-operating-manual.html', 'status': 'live'},
            {'system': 'Digital Twin (#81)', 'route': '/mission-control/institutional-digital-twin.html', 'status': 'live'},
        ],
    },
    'long_term_vision': (
        'Twenty years from now, Citizens United Facts looks dramatically different from January '
        '2027 — not because it abandoned its mission, but because it continually improved while '
        'remaining faithful to its purpose. Research stronger. Technology smarter. Volunteers '
        'better equipped. Communities more connected. Mission Control more insightful.'
    ),
    'summary': {
        'completion_target_date': completion_target_date,
        'days_remaining': days_remaining,
        'institutional_continuous_improvement_readiness_pct': institutional_continuous_improvement_readiness,
        'launch_certification_readiness_pct': ilc.get('summary', {}).get('institutional_launch_certification_readiness_pct', 57),
        'pmo_readiness_pct': pmo.get('summary', {}).get('pmo_execution_office_readiness_pct', 60),
        'improvement_dashboard_live': improvement_dashboard_live,
        'improvement_backlog_items': improvement_backlog_items,
        'innovation_pipeline_active': innovation_pipeline_active,
        'lessons_learned_entries': lessons_learned_entries,
        'ai_recommendations_pending': ai_recommendations_pending,
        'volunteer_suggestions': volunteer_suggestions,
        'annual_assessments_completed': annual_assessments_completed,
        'improvement_cycle_steps': len(IMPROVEMENT_CYCLE),
        'backlog_categories': len(IMPROVEMENT_BACKLOG_CATEGORIES),
        'institutional_completion_pct': ex.get('overall_completion', mc.get('build', 97)),
    },
    'catalog_gaps': [
        'Improvement dashboard not live',
        'Improvement backlog empty — no tracking system',
        'Innovation pipeline not operational',
        'Lessons learned library has no entries',
        'AI improvement recommendations not generated',
        'Volunteer suggestion intake not connected',
        'Annual department assessments not scheduled',
        'Health trend comparison not instrumented',
        'Recognition system not implemented',
        'Improvement cycle not visualized in MC',
        'No link from certification gaps to improvement backlog',
        'Post-Jan 2027 improvement cadence not defined',
    ],
    'recommended_next_build': {
        'number': 101,
        'title': 'Executive War Room & Countdown Dashboard Components',
        'note': (
            'War room UI, countdown dashboard, improvement backlog tracker, '
            'innovation pipeline board, lessons learned registry, COMP-* specs.'
        ),
    },
}

with open(root / 'data/institutional-continuous-improvement.json', 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')

print(
    f'Continuous Improvement: {len(IMPROVEMENT_CYCLE)} cycle steps, '
    f'{len(IMPROVEMENT_BACKLOG_CATEGORIES)} backlog categories, '
    f'{institutional_continuous_improvement_readiness}% readiness'
)
