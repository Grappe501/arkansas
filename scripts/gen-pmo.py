"""
Generate data/pmo.json — Build #54 Master Project Management Office (PMO) v1.0.
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


def avg(*vals):
    return round(sum(vals) / len(vals)) if vals else 0


mc = load_json(root / 'data/mission-control.json')
ls = load_json(root / 'data/launch-strategy.json')
coalition = load_json(root / 'data/coalition-directory.json')

ex = mc.get('executive', {})
builds_logged = len(mc.get('builds', []))
orgs = coalition.get('summary', {}).get('total_organizations', 0)
briefing = mc.get('briefing', {})

DEPARTMENTS = [
    {
        'id': 'DEPT-100', 'number': 100, 'title': 'Executive Office',
        'responsibilities': [
            'Institutional vision', 'Strategic planning', 'Major decisions', 'Governance',
            'Annual planning', 'Cross-department coordination',
        ],
        'primary_dashboard': 'Institution Health',
        'route': '/mission-control/executive.html',
        'readiness_pct': avg(ex.get('institutional_maturity_pct', 39), ex.get('governance_readiness', 44), ex.get('build_bible_readiness', 49)),
        'status': 'partial',
        'owner_assigned': False,
        'note': '0/7 stewards formally assigned — vision documented',
    },
    {
        'id': 'DEPT-200', 'number': 200, 'title': 'Research Office',
        'responsibilities': [
            'Research Observatory', 'Source Library', 'Evidence Ledger', 'Claims Registry',
            'Research standards', 'Citation review',
        ],
        'primary_dashboard': 'Research Health',
        'route': '/mission-control/research-observatory.html',
        'readiness_pct': avg(ex.get('research_readiness', 25), ex.get('observatory_readiness', 20),
                              ex.get('evidence_ledger_readiness', 22), ex.get('library_readiness', 22),
                              ex.get('research_methodology_readiness', 25)),
        'status': 'partial',
        'owner_assigned': False,
        'note': '14 evidence IDs · 3 claims — ledger partial',
    },
    {
        'id': 'DEPT-300', 'number': 300, 'title': 'Editorial Office',
        'responsibilities': [
            'Educational writing', 'Encyclopedia', 'Curriculum', 'Storytelling',
            'Editing', 'Publication workflows',
        ],
        'primary_dashboard': 'Content Production',
        'route': '/mission-control/content-production-matrix.html',
        'readiness_pct': avg(ex.get('content_readiness', 28), ex.get('production_matrix_readiness', 39),
                              ex.get('encyclopedia_readiness', 19), ex.get('curriculum_readiness', 26),
                              ex.get('narrative_readiness', 24), ex.get('content_factory_readiness', 30)),
        'status': 'partial',
        'owner_assigned': False,
        'note': '15 published / ~2700 target — factory designed not operational',
    },
    {
        'id': 'DEPT-400', 'number': 400, 'title': 'Technology Office',
        'responsibilities': [
            'Engineering', 'Infrastructure', 'GitHub', 'Netlify', 'Database',
            'APIs', 'Security', 'Performance',
        ],
        'primary_dashboard': 'Technical Health',
        'route': '/mission-control/technical-architecture.html',
        'readiness_pct': avg(ex.get('technical_architecture_readiness', 38), ex.get('database_schema_readiness', 40),
                              ex.get('platform_architecture_readiness', 24), ex.get('data_model_readiness', 52)),
        'status': 'partial',
        'owner_assigned': False,
        'note': 'Static Netlify live — Neon/Prisma not provisioned',
    },
    {
        'id': 'DEPT-500', 'number': 500, 'title': 'Design Office',
        'responsibilities': [
            'User experience', 'Accessibility', 'Visual identity', 'Infographics',
            'Interactive experiences', 'Design system',
        ],
        'primary_dashboard': 'Experience Health',
        'route': '/mission-control/ux-architecture.html',
        'readiness_pct': avg(ex.get('ux_architecture_readiness', 39), ex.get('wireframe_readiness', 38)),
        'status': 'partial',
        'owner_assigned': False,
        'note': 'v1.1 design tokens — WCAG audit not done',
    },
    {
        'id': 'DEPT-600', 'number': 600, 'title': 'Community Office',
        'responsibilities': [
            'Education Leaders', 'Contact Network', 'Community conversations',
            'Events', 'Academy',
        ],
        'primary_dashboard': 'Community Growth',
        'route': '/mission-control/education-academy.html',
        'readiness_pct': avg(ex.get('education_academy_readiness', 26), ex.get('signup_funnel_readiness', 22),
                              ex.get('visitor_journey_readiness', 40), ex.get('civic_action_readiness', 26)),
        'status': 'planned',
        'owner_assigned': False,
        'note': '0 Education Leaders · 0 contact signups',
    },
    {
        'id': 'DEPT-700', 'number': 700, 'title': 'Coalition Office',
        'responsibilities': [
            'Organization partnerships', 'Coalition onboarding', 'County outreach',
            'Resource distribution', 'Social media partnerships',
        ],
        'primary_dashboard': 'Coalition Health',
        'route': '/mission-control/coalition.html',
        'readiness_pct': avg(ex.get('coalition_readiness', 18), ex.get('county_os_readiness', 28), ex.get('outreach_readiness', 22)),
        'status': 'planned',
        'owner_assigned': False,
        'note': f'{orgs} coalition organizations',
    },
    {
        'id': 'DEPT-800', 'number': 800, 'title': 'Media Office',
        'responsibilities': [
            'Documentary production', 'Video', 'Audio', 'Presentations',
            'Graphics', 'Classroom resources',
        ],
        'primary_dashboard': 'Media Production',
        'route': '/mission-control/media-studio.html',
        'readiness_pct': ex.get('media_studio_readiness', 18),
        'status': 'planned',
        'owner_assigned': False,
        'note': '0 videos catalogued',
    },
    {
        'id': 'DEPT-900', 'number': 900, 'title': 'Mission Control Office',
        'responsibilities': [
            'Executive reporting', 'Progress tracking', 'Analytics', 'Alerts',
            'Readiness', 'Institutional intelligence',
        ],
        'primary_dashboard': 'Executive Overview',
        'route': '/mission-control/',
        'readiness_pct': 72,
        'status': 'live',
        'owner_assigned': False,
        'note': f'{builds_logged} builds logged · executive dashboard live',
    },
    {
        'id': 'DEPT-1000', 'number': 1000, 'title': 'Operations Office',
        'responsibilities': [
            'Project scheduling', 'Sprint planning', 'Documentation', 'Build sequencing',
            'Risk management', 'Institutional memory',
        ],
        'primary_dashboard': 'Execution Status',
        'route': '/mission-control/launch-strategy.html',
        'readiness_pct': avg(ex.get('launch_strategy_readiness', 39), ex.get('data_architecture_readiness', 41)),
        'status': 'partial',
        'owner_assigned': False,
        'note': 'Build registry live — unified sprint backlog not built',
    },
]

PMO_WORKFLOW = [
    {'stage': 'idea', 'order': 1, 'title': 'Idea', 'mc_tracked': 'partial'},
    {'stage': 'research', 'order': 2, 'title': 'Research', 'mc_tracked': 'partial'},
    {'stage': 'approval', 'order': 3, 'title': 'Approval', 'mc_tracked': 'partial'},
    {'stage': 'planning', 'order': 4, 'title': 'Planning', 'mc_tracked': 'live'},
    {'stage': 'design', 'order': 5, 'title': 'Design', 'mc_tracked': 'partial'},
    {'stage': 'development', 'order': 6, 'title': 'Development', 'mc_tracked': 'partial'},
    {'stage': 'review', 'order': 7, 'title': 'Review', 'mc_tracked': 'planned'},
    {'stage': 'testing', 'order': 8, 'title': 'Testing', 'mc_tracked': 'planned'},
    {'stage': 'publication', 'order': 9, 'title': 'Publication', 'mc_tracked': 'partial'},
    {'stage': 'maintenance', 'order': 10, 'title': 'Maintenance', 'mc_tracked': 'planned'},
]

WORK_ITEM_FIELDS = [
    {'field': 'project_id', 'required': True, 'enforced': 'partial'},
    {'field': 'department', 'required': True, 'enforced': 'partial'},
    {'field': 'owner', 'required': True, 'enforced': 'planned'},
    {'field': 'priority', 'required': True, 'enforced': 'planned'},
    {'field': 'dependencies', 'required': False, 'enforced': 'planned'},
    {'field': 'estimated_effort', 'required': False, 'enforced': 'planned'},
    {'field': 'status', 'required': True, 'enforced': 'live'},
    {'field': 'review_date', 'required': False, 'enforced': 'planned'},
    {'field': 'completion_date', 'required': False, 'enforced': 'partial'},
    {'field': 'documentation_links', 'required': True, 'enforced': 'partial'},
]

WEEKLY_BRIEFING = {
    'title': 'Executive Weekly Review',
    'frequency': 'Weekly',
    'status': 'partial',
    'current_briefing': briefing,
    'topics': [
        'Overall completion', 'Department progress', 'Major accomplishments', 'Current blockers',
        'Upcoming priorities', 'Research updates', 'Technology status', 'Community growth', 'Coalition activity',
    ],
    'automation': 'planned',
    'note': 'mc.briefing updated per build — not auto-generated weekly',
}

MONTHLY_REVIEW = {
    'title': 'Monthly Institutional Review',
    'frequency': 'Monthly',
    'status': 'planned',
    'dimensions': [
        'Mission alignment', 'Budget (future)', 'Research quality', 'Educational progress',
        'County expansion', 'Community engagement', 'Technology', 'Institutional risks',
    ],
    'note': 'Governance annual review planned — monthly cycle not scheduled',
}

RISK_REGISTER = [
    {'id': 'RISK-01', 'risk': 'Research delays', 'likelihood': 'high', 'impact': 'high', 'mitigation': 'Research Observatory + methodology', 'owner': 'unassigned', 'status': 'open'},
    {'id': 'RISK-02', 'risk': 'Citation gaps', 'likelihood': 'high', 'impact': 'high', 'mitigation': 'Evidence Ledger expansion', 'owner': 'unassigned', 'status': 'open'},
    {'id': 'RISK-03', 'risk': 'Technical debt', 'likelihood': 'medium', 'impact': 'high', 'mitigation': 'Next.js migration plan', 'owner': 'unassigned', 'status': 'open'},
    {'id': 'RISK-04', 'risk': 'Volunteer shortages', 'likelihood': 'high', 'impact': 'medium', 'mitigation': 'Education Leader pipeline', 'owner': 'unassigned', 'status': 'open'},
    {'id': 'RISK-05', 'risk': 'Accessibility issues', 'likelihood': 'high', 'impact': 'high', 'mitigation': 'WCAG audit sprint', 'owner': 'unassigned', 'status': 'open'},
    {'id': 'RISK-06', 'risk': 'Infrastructure risks', 'likelihood': 'medium', 'impact': 'high', 'mitigation': 'Neon provisioning + backups', 'owner': 'unassigned', 'status': 'open'},
    {'id': 'RISK-07', 'risk': 'Knowledge loss', 'likelihood': 'medium', 'impact': 'high', 'mitigation': 'PMO documentation + git', 'owner': 'unassigned', 'status': 'partial'},
    {'id': 'RISK-08', 'risk': 'Blueprint fatigue', 'likelihood': 'medium', 'impact': 'medium', 'mitigation': 'PMO execution focus — Build #54', 'owner': 'unassigned', 'status': 'open'},
    {'id': 'RISK-09', 'risk': 'Premature public launch', 'likelihood': 'medium', 'impact': 'high', 'mitigation': 'Launch Strategy Phase 0 gate', 'owner': 'unassigned', 'status': 'partial'},
    {'id': 'RISK-10', 'risk': '0 signups breaks community funnel', 'likelihood': 'high', 'impact': 'high', 'mitigation': 'Pilot cohort + Academy test', 'owner': 'unassigned', 'status': 'open'},
]

DEPENDENCY_CHAIN = [
    {'id': 'DEP-01', 'from': 'Evidence Ledger', 'to': 'Claims Registry', 'status': 'partial'},
    {'id': 'DEP-02', 'from': 'Claims Registry', 'to': 'Educational Articles', 'status': 'partial'},
    {'id': 'DEP-03', 'from': 'Educational Articles', 'to': 'Curriculum', 'status': 'planned'},
    {'id': 'DEP-04', 'from': 'Curriculum', 'to': 'Academy', 'status': 'planned'},
    {'id': 'DEP-05', 'from': 'Academy', 'to': 'Community Conversations', 'status': 'planned'},
    {'id': 'DEP-06', 'from': 'Data Architecture', 'to': 'Database Schema', 'status': 'partial'},
    {'id': 'DEP-07', 'from': 'Database Schema', 'to': 'Domain APIs', 'status': 'planned'},
    {'id': 'DEP-08', 'from': 'UX Architecture', 'to': 'Learning Compass UI', 'status': 'planned'},
]

RESOURCE_ALLOCATION = [
    {'area': 'Research', 'effort_pct': 20, 'readiness_pct': ex.get('research_readiness', 25), 'bottleneck': 'Citation verification'},
    {'area': 'Writing', 'effort_pct': 25, 'readiness_pct': ex.get('content_readiness', 28), 'bottleneck': '15/2700 published'},
    {'area': 'Engineering', 'effort_pct': 20, 'readiness_pct': ex.get('technical_architecture_readiness', 38), 'bottleneck': 'No database'},
    {'area': 'Design', 'effort_pct': 10, 'readiness_pct': ex.get('ux_architecture_readiness', 39), 'bottleneck': 'Compass UI'},
    {'area': 'Media', 'effort_pct': 5, 'readiness_pct': ex.get('media_studio_readiness', 18), 'bottleneck': '0 videos'},
    {'area': 'Community', 'effort_pct': 10, 'readiness_pct': ex.get('education_academy_readiness', 26), 'bottleneck': '0 leaders'},
    {'area': 'Coalition', 'effort_pct': 5, 'readiness_pct': ex.get('coalition_readiness', 18), 'bottleneck': '0 orgs'},
    {'area': 'Operations', 'effort_pct': 5, 'readiness_pct': ex.get('launch_strategy_readiness', 39), 'bottleneck': 'No sprint backlog'},
]

INSTITUTIONAL_CALENDAR = {
    'status': 'planned',
    'event_types': [
        'Research reviews', 'Editorial deadlines', 'Sprint cycles', 'Community events',
        'Coalition meetings', 'Annual reports', 'Platform updates',
    ],
    'integrations_planned': ['Google Calendar', 'Microsoft Outlook', 'Apple Calendar'],
    'current': 'No unified calendar — build dates in registry only',
}

PMO_DASHBOARD_WIDGETS = [
    {'id': 'W-01', 'widget': 'Overall completion', 'status': 'live', 'source': 'executive.overall_completion'},
    {'id': 'W-02', 'widget': 'Department completion', 'status': 'partial', 'source': 'This dashboard'},
    {'id': 'W-03', 'widget': 'Sprint status', 'status': 'planned', 'source': 'Sprint Zero not started'},
    {'id': 'W-04', 'widget': 'Open risks', 'status': 'partial', 'source': 'Risk register — manual'},
    {'id': 'W-05', 'widget': 'Blocked work', 'status': 'partial', 'source': 'mc.briefing.blocked'},
    {'id': 'W-06', 'widget': 'Upcoming milestones', 'status': 'partial', 'source': 'Launch phases + builds'},
    {'id': 'W-07', 'widget': 'Launch readiness', 'status': 'live', 'source': 'launch-strategy.json'},
    {'id': 'W-08', 'widget': 'Institution health', 'status': 'partial', 'source': 'executive + progress_bars'},
]

DAILY_QUESTIONS = [
    {'q': 'What are we building?', 'status': 'live', 'source': 'mc.briefing + builds[]'},
    {'q': 'Why are we building it?', 'status': 'live', 'source': 'Build purpose fields'},
    {'q': 'Who owns it?', 'status': 'planned', 'source': '0 department owners assigned'},
    {'q': 'What is blocked?', 'status': 'partial', 'source': 'mc.briefing.blocked'},
    {'q': 'What should happen next?', 'status': 'live', 'source': 'recommended_next_build'},
]

dept_live = sum(1 for d in DEPARTMENTS if d['status'] == 'live')
dept_partial = sum(1 for d in DEPARTMENTS if d['status'] == 'partial')
dept_planned = sum(1 for d in DEPARTMENTS if d['status'] == 'planned')
avg_dept_readiness = round(sum(d['readiness_pct'] for d in DEPARTMENTS) / len(DEPARTMENTS))
owners_assigned = sum(1 for d in DEPARTMENTS if d.get('owner_assigned'))
risks_open = sum(1 for r in RISK_REGISTER if r['status'] == 'open')
questions_live = sum(1 for q in DAILY_QUESTIONS if q['status'] == 'live')
widgets_live = sum(1 for w in PMO_DASHBOARD_WIDGETS if w['status'] == 'live')

MC_METRICS = [
    {'id': 'PMO-01', 'title': 'Departments defined', 'status': 'live', 'current': f'{len(DEPARTMENTS)}/10'},
    {'id': 'PMO-02', 'title': 'Department owners assigned', 'status': 'planned', 'current': f'{owners_assigned}/10'},
    {'id': 'PMO-03', 'title': 'Avg department readiness', 'status': 'partial', 'current': f'{avg_dept_readiness}%'},
    {'id': 'PMO-04', 'title': 'Daily five questions answerable', 'status': 'partial', 'current': f'{questions_live}/5 instant'},
    {'id': 'PMO-05', 'title': 'Workflow stages in MC', 'status': 'partial', 'current': f'{len(PMO_WORKFLOW)} stages defined'},
    {'id': 'PMO-06', 'title': 'Work items in PMO registry', 'status': 'partial', 'current': f'{builds_logged} builds — no unified task DB'},
    {'id': 'PMO-07', 'title': 'Weekly briefing automated', 'status': 'planned', 'current': 'Manual per build'},
    {'id': 'PMO-08', 'title': 'Monthly institutional review', 'status': 'planned', 'current': 'Not scheduled'},
    {'id': 'PMO-09', 'title': 'Risk register maintained', 'status': 'partial', 'current': f'{len(RISK_REGISTER)} risks · {risks_open} open'},
    {'id': 'PMO-10', 'title': 'Dependency map visible', 'status': 'partial', 'current': f'{len(DEPENDENCY_CHAIN)} chains documented'},
    {'id': 'PMO-11', 'title': 'Institutional calendar', 'status': 'planned', 'current': 'Not built'},
    {'id': 'PMO-12', 'title': 'PMO dashboard widgets live', 'status': 'partial', 'current': f'{widgets_live}/{len(PMO_DASHBOARD_WIDGETS)}'},
]

readiness_factors = [
    100,  # PMO constitution
    avg_dept_readiness,
    (questions_live / 5) * 100,
    (widgets_live / len(PMO_DASHBOARD_WIDGETS)) * 100,
    50 if WEEKLY_BRIEFING['status'] == 'partial' else 20,
    30,  # monthly review
    40 if risks_open else 60,  # risk register exists
    35,  # work item enforcement
    0,   # owners
    80,  # PMO dashboard after this build
]
pmo_readiness = round(sum(readiness_factors) / len(readiness_factors))

out = {
    'version': '1.0',
    'build': 54,
    'updated': today,
    'title': 'Master Project Management Office (PMO) v1.0',
    'subtitle': 'The Institutional Execution System — Turning Vision Into Reality',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/pmo.html',
    'constitution': '/docs/MASTER_PMO.md',
    'purpose': 'How the institution gets built — PMO coordinates every phase toward one mission.',
    'governing_principle': (
        'Planning without execution is aspiration. Execution without planning is confusion. '
        'The PMO unites every department into disciplined execution.'
    ),
    'pmo_mission': {
        'daily_questions': DAILY_QUESTIONS,
        'questions_answerable_instantly': questions_live,
    },
    'extends': [
        {'title': 'Master Build Bible', 'build': 50, 'route': '/data/build-bible.json'},
        {'title': 'Launch Strategy', 'build': 53, 'route': '/data/launch-strategy.json'},
        {'title': 'Data Architecture', 'build': 51, 'route': '/data/data-architecture.json'},
        {'title': 'Governance Constitution', 'build': 49, 'route': '/data/governance-constitution.json'},
        {'title': 'Systems Integration', 'build': 45, 'route': '/data/systems-integration.json'},
    ],
    'departments': {
        'title': 'Ten Permanent Departments',
        'departments': DEPARTMENTS,
        'departments_total': len(DEPARTMENTS),
        'departments_live': dept_live,
        'departments_partial': dept_partial,
        'departments_planned': dept_planned,
        'avg_readiness_pct': avg_dept_readiness,
        'owners_assigned': owners_assigned,
    },
    'pmo_workflow': {
        'title': 'Initiative Lifecycle',
        'stages': PMO_WORKFLOW,
        'flow': 'Idea → Research → Approval → Planning → Design → Development → Review → Testing → Publication → Maintenance',
    },
    'work_item_structure': {
        'title': 'Universal Task Schema',
        'fields': WORK_ITEM_FIELDS,
        'enforcement': 'partial',
        'current': f'Builds registry = {builds_logged} work items with partial schema',
    },
    'executive_weekly_review': WEEKLY_BRIEFING,
    'monthly_institutional_review': MONTHLY_REVIEW,
    'risk_register': {
        'title': 'Living Risk Register',
        'risks': RISK_REGISTER,
        'open_count': risks_open,
        'total': len(RISK_REGISTER),
    },
    'dependency_management': {
        'title': 'Dependency Maps',
        'chains': DEPENDENCY_CHAIN,
        'visualization': 'planned',
    },
    'resource_allocation': {
        'title': 'Effort Tracking',
        'areas': RESOURCE_ALLOCATION,
    },
    'institutional_calendar': INSTITUTIONAL_CALENDAR,
    'pmo_dashboard': {
        'title': 'Mission Control PMO Dashboard',
        'route': '/mission-control/pmo.html',
        'widgets': PMO_DASHBOARD_WIDGETS,
        'widgets_live': widgets_live,
    },
    'long_term_vision': (
        'PMO operates like a university or presidential library administrative office — '
        'every project advances educational mission with quality, transparency, and public trust.'
    ),
    'mc_integration': {
        'title': 'Mission Control PMO Metrics',
        'status': 'partial',
        'metrics': MC_METRICS,
        'mc_as_pmo_cockpit': True,
    },
    'related_blueprints': [
        {'title': 'Build Bible (#50)', 'route': '/mission-control/build-bible.html', 'build': 50},
        {'title': 'Launch Strategy (#53)', 'route': '/mission-control/launch-strategy.html', 'build': 53},
        {'title': 'Content Production Matrix (#46)', 'route': '/mission-control/content-production-matrix.html', 'build': 46},
        {'title': 'Executive Command Center', 'route': '/mission-control/executive.html', 'build': 25},
    ],
    'summary': {
        'departments_total': len(DEPARTMENTS),
        'departments_live': dept_live,
        'departments_partial': dept_partial,
        'departments_planned': dept_planned,
        'avg_department_readiness_pct': avg_dept_readiness,
        'owners_assigned': owners_assigned,
        'workflow_stages': len(PMO_WORKFLOW),
        'work_items_logged': builds_logged,
        'risks_open': risks_open,
        'risks_total': len(RISK_REGISTER),
        'dependencies_documented': len(DEPENDENCY_CHAIN),
        'daily_questions_live': questions_live,
        'pmo_widgets_live': widgets_live,
        'weekly_briefing_automated': False,
        'monthly_review_scheduled': False,
        'calendar_live': False,
        'pmo_readiness_pct': pmo_readiness,
    },
    'catalog_gaps': [
        '0/10 department owners assigned — stewardship roles undefined in PMO',
        'No unified work item database — builds[] only partial PMO schema',
        'Weekly briefing manual per build — not auto-generated',
        'Monthly institutional review not scheduled',
        'Institutional calendar not built — no sprint cycles tracked',
        'Sprint status widget planned — Sprint Zero not started',
        'Dependency map documented — not visualized in MC',
        'Risk register manual — no MC risk triage workflow',
        'Community + Coalition departments planned — 0 leaders, 0 orgs',
        'PMO cockpit partial — 3/8 dashboard widgets live',
        'Owner field on work items not enforced',
    ],
    'recommended_next_build': {
        'number': 55,
        'title': 'Master Implementation Roadmap & Sprint Zero',
        'note': 'First sprint backlog, department owner assignment, work item schema in Neon, weekly briefing generator.',
    },
}

path = root / 'data/pmo.json'
with open(path, 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')
print(f'PMO: {dept_live} live + {dept_partial} partial depts, {avg_dept_readiness}% avg, {pmo_readiness}% PMO readiness')
