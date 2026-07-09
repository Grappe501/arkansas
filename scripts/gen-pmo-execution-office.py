"""
Generate data/pmo-execution-office.json — Build #89.
Master PMO & Execution Office — Building the Institution With Discipline v1.0.
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
es = load_json(root / 'data/execution-schedule.json')
pmo54 = load_json(root / 'data/pmo.json')

ex = mc.get('executive', {})
builds_logged = len(mc.get('builds', []))

# Honest operational metrics
pmo_dashboard_live = False
project_registry_live = False
weekly_briefing_automated = False
portfolio_owners_assigned = 0
projects_in_pmo_registry = 0
projects_completed = builds_logged
projects_active = 0
projects_delayed = 0
milestones_achieved = 0
volunteer_assignments = 0
decisions_recorded = 0

PMO_RESPONSIBILITIES = [
    'Master project schedule',
    'Department coordination',
    'Volunteer assignments',
    'Milestone tracking',
    'Risk management',
    'Documentation',
    'Quality assurance',
    'Mission Control reporting',
    'Executive briefings',
    'Launch readiness',
]

EXECUTIVE_PORTFOLIO = [
    {'id': 'PF-01', 'name': 'Research', 'owner': 'unassigned', 'readiness_pct': ex.get('research_readiness', 43), 'status': 'partial'},
    {'id': 'PF-02', 'name': 'Technology', 'owner': 'unassigned', 'readiness_pct': ex.get('technical_architecture_readiness', 38), 'status': 'partial'},
    {'id': 'PF-03', 'name': 'Mission Control', 'owner': 'unassigned', 'readiness_pct': ex.get('mc2_readiness', 42), 'status': 'partial'},
    {'id': 'PF-04', 'name': 'Community Education Academy', 'owner': 'unassigned', 'readiness_pct': ex.get('education_academy_readiness', 26), 'status': 'planned'},
    {'id': 'PF-05', 'name': 'Coalition Development', 'owner': 'unassigned', 'readiness_pct': ex.get('coalition_readiness', 44), 'status': 'partial'},
    {'id': 'PF-06', 'name': 'Communications', 'owner': 'unassigned', 'readiness_pct': ex.get('arkansas_communications_readiness', 42), 'status': 'partial'},
    {'id': 'PF-07', 'name': 'County Operations', 'owner': 'unassigned', 'readiness_pct': ex.get('arkansas_county_operating_system_readiness', 47), 'status': 'partial'},
    {'id': 'PF-08', 'name': 'City Operations', 'owner': 'unassigned', 'readiness_pct': ex.get('arkansas_city_operating_system_readiness', 48), 'status': 'partial'},
    {'id': 'PF-09', 'name': 'Neighborhood Operations', 'owner': 'unassigned', 'readiness_pct': ex.get('arkansas_neighborhood_operating_system_readiness', 47), 'status': 'partial'},
    {'id': 'PF-10', 'name': 'Volunteer Development', 'owner': 'unassigned', 'readiness_pct': ex.get('volunteer_funding_constitution_readiness', 45), 'status': 'planned'},
    {'id': 'PF-11', 'name': 'Governance', 'owner': 'unassigned', 'readiness_pct': ex.get('governance_readiness', 46), 'status': 'partial'},
    {'id': 'PF-12', 'name': 'Operations', 'owner': 'unassigned', 'readiness_pct': ex.get('pmo_readiness', 48), 'status': 'partial'},
]

PROJECT_REGISTRY_FIELDS = [
    'Project ID', 'Project name', 'Purpose', 'Dependencies', 'Owner',
    'Priority', 'Status', 'Completion percentage', 'Target completion date', 'Supporting documents',
]

MILESTONES = [
    {'id': 'MS-01', 'milestone': 'Research completion', 'acceptance_criteria': 'Research Institute operational with published standards', 'achieved': False, 'status': 'planned'},
    {'id': 'MS-02', 'milestone': 'Website readiness', 'acceptance_criteria': 'Public site fully operational for statewide civic education', 'achieved': False, 'status': 'partial'},
    {'id': 'MS-03', 'milestone': 'Mission Control readiness', 'acceptance_criteria': 'MC dashboards, registries, and executive reporting live', 'achieved': False, 'status': 'partial'},
    {'id': 'MS-04', 'milestone': 'Academy readiness', 'acceptance_criteria': 'Community Education Academy curriculum and enrollment operational', 'achieved': False, 'status': 'planned'},
    {'id': 'MS-05', 'milestone': 'Coalition readiness', 'acceptance_criteria': 'Active coalition partnerships across Arkansas', 'achieved': False, 'status': 'planned'},
    {'id': 'MS-06', 'milestone': 'County readiness', 'acceptance_criteria': 'Representation in all 75 Arkansas counties', 'achieved': False, 'status': 'planned'},
    {'id': 'MS-07', 'milestone': 'City readiness', 'acceptance_criteria': 'Leadership development in 250 largest cities', 'achieved': False, 'status': 'planned'},
    {'id': 'MS-08', 'milestone': 'Volunteer readiness', 'acceptance_criteria': 'Functioning statewide volunteer organization', 'achieved': False, 'status': 'planned'},
    {'id': 'MS-09', 'milestone': 'Governance readiness', 'acceptance_criteria': 'Governance documents completed and certified', 'achieved': False, 'status': 'partial'},
    {'id': 'MS-10', 'milestone': 'Institution readiness', 'acceptance_criteria': 'V1 substantially complete — ready for statewide public operation', 'achieved': False, 'status': 'planned'},
]

RISK_REGISTER = [
    {'id': 'PMO-R01', 'risk': 'Volunteer shortages', 'likelihood': 'high', 'impact': 'high', 'owner': 'unassigned', 'mitigation': 'Volunteer pipeline + Education Leader recruitment', 'status': 'open'},
    {'id': 'PMO-R02', 'risk': 'Technology delays', 'likelihood': 'medium', 'impact': 'high', 'owner': 'unassigned', 'mitigation': 'Critical path prioritization + infrastructure sprint', 'status': 'open'},
    {'id': 'PMO-R03', 'risk': 'Research backlog', 'likelihood': 'high', 'impact': 'high', 'owner': 'unassigned', 'mitigation': 'Research Observatory + citation verification workflow', 'status': 'open'},
    {'id': 'PMO-R04', 'risk': 'Leadership gaps', 'likelihood': 'high', 'impact': 'high', 'owner': 'unassigned', 'mitigation': 'Citizen Leadership Academy + county/city OS', 'status': 'open'},
    {'id': 'PMO-R05', 'risk': 'Documentation gaps', 'likelihood': 'medium', 'impact': 'medium', 'owner': 'unassigned', 'mitigation': 'PMO documentation standards + quality gates', 'status': 'open'},
    {'id': 'PMO-R06', 'risk': 'Coalition delays', 'likelihood': 'medium', 'impact': 'medium', 'owner': 'unassigned', 'mitigation': 'Coalition Network onboarding sprint', 'status': 'open'},
    {'id': 'PMO-R07', 'risk': 'Schedule conflicts', 'likelihood': 'medium', 'impact': 'high', 'owner': 'unassigned', 'mitigation': 'Dependency map + weekly executive briefing', 'status': 'open'},
]

DECISION_REGISTER_EXAMPLES = [
    'Strategic priorities',
    'Governance changes',
    'Technology decisions',
    'Editorial standards',
    'Research policies',
    'Volunteer policies',
]

DEPENDENCY_MAP = [
    {'id': 'DM-01', 'element': 'What must be completed first', 'status': 'specified', 'tracked': False},
    {'id': 'DM-02', 'element': 'What can proceed in parallel', 'status': 'specified', 'tracked': False},
    {'id': 'DM-03', 'element': 'What blocks other work', 'status': 'specified', 'tracked': False},
    {'id': 'DM-04', 'element': 'Critical path', 'status': 'planned', 'tracked': False},
    {'id': 'DM-05', 'element': 'Float', 'status': 'planned', 'tracked': False},
    {'id': 'DM-06', 'element': 'Priority', 'status': 'partial', 'tracked': False},
]

VOLUNTEER_ASSIGNMENT_FIELDS = [
    'Current assignment', 'Upcoming assignment', 'Skills needed', 'Training required',
    'Mentor', 'Department', 'Mission contribution',
]

WEEKLY_EXECUTIVE_BRIEFING = [
    'Overall completion', 'Major accomplishments', 'Critical risks', 'Projects behind schedule',
    'Upcoming milestones', 'Volunteer growth', 'Research progress', 'Technology progress',
    'Recommended executive actions',
]

PMO_DASHBOARD_WIDGETS = [
    {'id': 'PMO-W01', 'widget': 'Projects completed', 'current': projects_completed, 'status': 'partial'},
    {'id': 'PMO-W02', 'widget': 'Projects active', 'current': projects_active, 'status': 'planned'},
    {'id': 'PMO-W03', 'widget': 'Projects delayed', 'current': projects_delayed, 'status': 'planned'},
    {'id': 'PMO-W04', 'widget': 'Milestones completed', 'current': milestones_achieved, 'status': 'planned'},
    {'id': 'PMO-W05', 'widget': 'Risks open', 'current': len(RISK_REGISTER), 'status': 'partial'},
    {'id': 'PMO-W06', 'widget': 'Critical path', 'current': 0, 'status': 'planned'},
    {'id': 'PMO-W07', 'widget': 'Volunteer assignments', 'current': volunteer_assignments, 'status': 'planned'},
    {'id': 'PMO-W08', 'widget': 'Department readiness', 'current': f"{es.get('department_readiness', {}).get('departments_complete', 0)}/10", 'status': 'partial'},
    {'id': 'PMO-W09', 'widget': 'Institutional completion %', 'current': ex.get('overall_completion', mc.get('build', 88)), 'unit': '%', 'status': 'partial'},
]

QUALITY_GATES = [
    'Purpose fulfilled',
    'Documentation complete',
    'Quality reviewed',
    'Integrated with Mission Control',
    'Dependencies resolved',
    'Executive acceptance',
]

risks_open = sum(1 for r in RISK_REGISTER if r['status'] == 'open')

pmo_execution_office_readiness = min(
    62,
    16
    + len(PMO_RESPONSIBILITIES) // 2
    + len(EXECUTIVE_PORTFOLIO) // 2
    + len(PROJECT_REGISTRY_FIELDS) // 2
    + len(MILESTONES) // 2
    + len(RISK_REGISTER) // 2
    + len(DECISION_REGISTER_EXAMPLES) // 2
    + len(DEPENDENCY_MAP) // 2
    + len(VOLUNTEER_ASSIGNMENT_FIELDS) // 2
    + len(WEEKLY_EXECUTIVE_BRIEFING) // 2
    + len(PMO_DASHBOARD_WIDGETS) // 2
    + len(QUALITY_GATES) // 2
    + (2 if pmo_dashboard_live else 0),
)

out = {
    'version': '1.0',
    'build': 89,
    'updated': today,
    'completion_target_date': completion_target_date,
    'completion_target_label': 'Mission Complete — January 2027',
    'title': 'Master PMO & Execution Office v1.0',
    'subtitle': 'Building the Institution With Discipline',
    'tagline': 'The Executive Program Management System',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/pmo-execution-office.html',
    'constitution': '/docs/MASTER_PMO_EXECUTION_OFFICE.md',
    'purpose': (
        'Permanent Project Management Office responsible for planning, coordinating, monitoring, '
        'documenting, and delivering every part of the institution before January 2027. Mission '
        'Control treats the PMO as the central execution office.'
    ),
    'governing_principle': (
        'Ideas create possibility. Plans create direction. Execution creates institutions. The PMO '
        'ensures every volunteer, department, project, and decision moves Citizens United Facts one '
        'measurable step closer to a fully operational Arkansas civic education institution '
        'completed by January 2027.'
    ),
    'founders_principle': (
        'Large institutions are rarely built because of brilliant ideas alone. They are built because '
        'thousands of small commitments are coordinated with discipline. The PMO transforms vision '
        'into execution, execution into completion, and completion into an enduring institution.'
    ),
    'pmo_mission': {
        'title': 'PMO Mission',
        'statement': 'Deliver a fully operational Citizens United Facts institution by January 2027.',
        'completion_target_date': completion_target_date,
        'days_remaining': days_remaining,
    },
    'pmo_responsibilities': {
        'title': 'PMO Responsibilities',
        'responsibilities': PMO_RESPONSIBILITIES,
        'nothing_major_without_visibility': True,
    },
    'executive_portfolio': {
        'title': 'Executive Portfolio',
        'portfolios': EXECUTIVE_PORTFOLIO,
        'portfolios_total': len(EXECUTIVE_PORTFOLIO),
        'owners_assigned': portfolio_owners_assigned,
        'every_portfolio_has_owner_milestones_progress': True,
        'status': 'partial',
    },
    'project_registry': {
        'title': 'Project Registry',
        'fields': PROJECT_REGISTRY_FIELDS,
        'fields_total': len(PROJECT_REGISTRY_FIELDS),
        'projects_in_registry': projects_in_pmo_registry,
        'builds_logged_in_mc': builds_logged,
        'live': project_registry_live,
        'nothing_lost_traceable': True,
        'status': 'planned',
        'note': f'{builds_logged} builds in MC registry — unified PMO project DB not operational',
    },
    'milestone_management': {
        'title': 'Milestone Management',
        'milestones': MILESTONES,
        'milestones_total': len(MILESTONES),
        'milestones_achieved': milestones_achieved,
        'measurable_acceptance_criteria': True,
        'status': 'specified',
    },
    'risk_register': {
        'title': 'Risk Register',
        'risks': RISK_REGISTER,
        'risks_total': len(RISK_REGISTER),
        'risks_open': risks_open,
        'tracks_likelihood_impact_owner_mitigation_status': True,
        'status': 'partial',
    },
    'decision_register': {
        'title': 'Decision Register',
        'examples': DECISION_REGISTER_EXAMPLES,
        'decisions_recorded': decisions_recorded,
        'institutional_memory': True,
        'status': 'planned',
    },
    'dependency_map': {
        'title': 'Dependency Map',
        'elements': DEPENDENCY_MAP,
        'pmo_coordinates_not_reacts': True,
        'status': 'planned',
    },
    'volunteer_assignment_system': {
        'title': 'Volunteer Assignment System',
        'fields': VOLUNTEER_ASSIGNMENT_FIELDS,
        'assignments_tracked': volunteer_assignments,
        'volunteers_always_know_where_they_fit': True,
        'status': 'planned',
    },
    'weekly_executive_briefing': {
        'title': 'Weekly Executive Briefing',
        'briefing_items': WEEKLY_EXECUTIVE_BRIEFING,
        'automated': weekly_briefing_automated,
        'one_authoritative_report': True,
        'status': 'specified',
    },
    'pmo_dashboard': {
        'title': 'PMO Dashboard',
        'widgets': PMO_DASHBOARD_WIDGETS,
        'widgets_total': len(PMO_DASHBOARD_WIDGETS),
        'live': pmo_dashboard_live,
        'leadership_operational_cockpit': True,
        'status': 'planned',
    },
    'quality_gates': {
        'title': 'Quality Gates',
        'gates': QUALITY_GATES,
        'completion_means_operational_readiness': True,
        'status': 'specified',
    },
    'integration': {
        'chain': (
            'Mission Control → Digital Twin → Research Institute → Community Education Academy → '
            'Coalition Network → County Operating System → Technology Office → Governance'
        ),
        'every_component_reports_into_pmo': True,
        'systems': [
            {'system': 'Execution Schedule (#88)', 'route': '/mission-control/execution-schedule.html', 'status': 'live'},
            {'system': 'PMO (#54)', 'route': '/mission-control/pmo.html', 'status': 'live'},
            {'system': 'Master Launch Plan (#85)', 'route': '/mission-control/master-launch-plan.html', 'status': 'live'},
            {'system': 'Digital Twin (#81)', 'route': '/mission-control/institutional-digital-twin.html', 'status': 'live'},
            {'system': 'Research Institute (#73)', 'route': '/mission-control/arkansas-research-institute.html', 'status': 'live'},
            {'system': 'County OS (#77)', 'route': '/mission-control/arkansas-county-operating-system.html', 'status': 'live'},
            {'system': 'Governance (#49)', 'route': '/mission-control/governance.html', 'status': 'live'},
        ],
        'extends': [
            {'build': 54, 'title': 'Master PMO v1.0', 'route': '/mission-control/pmo.html'},
            {'build': 88, 'title': 'Execution Schedule', 'route': '/mission-control/execution-schedule.html'},
        ],
    },
    'long_term_vision': (
        'By January 2027, the PMO coordinates hundreds of individual projects into one unified '
        'institution. After completion, the PMO transitions from construction management to continuous '
        'improvement — preserving quality, institutional memory, and strategic direction.'
    ),
    'summary': {
        'completion_target_date': completion_target_date,
        'days_remaining': days_remaining,
        'pmo_execution_office_readiness_pct': pmo_execution_office_readiness,
        'pmo_v54_readiness_pct': pmo54.get('summary', {}).get('pmo_readiness_pct', 46),
        'execution_schedule_readiness_pct': es.get('summary', {}).get('execution_schedule_readiness_pct', 56),
        'projects_completed': projects_completed,
        'projects_active': projects_active,
        'projects_delayed': projects_delayed,
        'projects_in_pmo_registry': projects_in_pmo_registry,
        'milestones_achieved': milestones_achieved,
        'milestones_total': len(MILESTONES),
        'risks_open': risks_open,
        'portfolio_owners_assigned': portfolio_owners_assigned,
        'portfolios_total': len(EXECUTIVE_PORTFOLIO),
        'volunteer_assignments': volunteer_assignments,
        'pmo_dashboard_live': pmo_dashboard_live,
        'weekly_briefing_automated': weekly_briefing_automated,
        'institutional_completion_pct': ex.get('overall_completion', mc.get('build', 88)),
    },
    'catalog_gaps': [
        'PMO dashboard not live — no operational cockpit',
        'Project registry not operational — builds in MC only',
        '0 portfolio owners assigned',
        '0 milestones achieved with acceptance criteria',
        '0 volunteer assignments tracked',
        'Weekly briefing not auto-generated',
        'Decision register empty — 0 decisions recorded',
        'Dependency map not visualized in MC',
        'Critical path not integrated from Execution Schedule',
        'Quality gates not enforced in workflow',
        'Extends PMO #54 — two PMO dashboards until unified',
    ],
    'recommended_next_build': {
        'number': 90,
        'title': 'Executive War Room & Countdown Dashboard Components',
        'note': (
            'War room UI, live countdown, critical path tracker, PMO project registry, '
            'automated weekly briefing, COMP-* specs.'
        ),
    },
}

with open(root / 'data/pmo-execution-office.json', 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')

print(
    f'PMO Execution Office: {projects_completed} builds logged, {milestones_achieved}/{len(MILESTONES)} '
    f'milestones, {pmo_execution_office_readiness}% readiness'
)
