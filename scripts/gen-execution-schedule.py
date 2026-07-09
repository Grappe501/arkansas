"""
Generate data/execution-schedule.json — Build #88.
Master Execution Schedule — Mission Complete by January 2027 v1.0.
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
mlp = load_json(root / 'data/master-launch-plan.json')
l100 = load_json(root / 'data/launch-campaign-first-100-days.json')
sp = load_json(root / 'data/arkansas-strategic-plan-2035.json')

ex = mc.get('executive', {})
build_num = ex.get('overall_completion', mc.get('build', 87))

# Honest metrics
countdown_dashboard_live = False
executive_war_room_live = False
overall_institutional_completion_pct = build_num
critical_path_on_schedule = 0
critical_path_at_risk = 0
critical_path_blocked = 0
open_blockers = 0
top_priorities_tracked = 0
departments_complete = 0

MISSION_V1_DELIVERABLES = [
    'Public website fully operational',
    'Mission Control fully operational',
    'AI Learning Guide available',
    'Research Institute established',
    'Community Education Academy operational',
    'Coalition Network functioning',
    'County, City, and Neighborhood Operating Systems online',
    'Volunteer systems operational',
    'Communications systems operational',
    'Educational resources published',
    'Leadership infrastructure established',
    'Governance documents completed',
]

COMPLETION_TARGETS = [
    'Representation in all 75 Arkansas counties',
    'Leadership development in 250 largest cities',
    'Progress toward 15% connected voters per county and city',
    'Active coalition partnerships across Arkansas',
    'Functioning statewide volunteer organization',
    'Complete research and educational foundation',
    'Fully operational Mission Control',
]

COUNTDOWN_INDICATORS = [
    {'id': 'ES-C01', 'indicator': 'Days Remaining Until January 2027', 'current': days_remaining, 'status': 'live'},
    {'id': 'ES-C02', 'indicator': 'Overall Institutional Completion', 'current': overall_institutional_completion_pct, 'unit': '%', 'status': 'partial'},
    {'id': 'ES-C03', 'indicator': 'Department Completion', 'current': 0, 'unit': '%', 'status': 'planned'},
    {'id': 'ES-C04', 'indicator': 'Research Completion', 'current': ex.get('research_readiness', 43), 'unit': '%', 'status': 'partial'},
    {'id': 'ES-C05', 'indicator': 'Technology Completion', 'current': ex.get('technical_architecture_readiness', 38), 'unit': '%', 'status': 'partial'},
    {'id': 'ES-C06', 'indicator': 'Volunteer Recruitment', 'current': 0, 'status': 'planned'},
    {'id': 'ES-C07', 'indicator': 'County Coverage', 'current': 0, 'target': 75, 'status': 'planned'},
    {'id': 'ES-C08', 'indicator': 'City Coverage', 'current': 0, 'target': 250, 'status': 'planned'},
    {'id': 'ES-C09', 'indicator': 'Neighborhood Coverage', 'current': 0, 'status': 'planned'},
    {'id': 'ES-C10', 'indicator': 'Coalition Growth', 'current': 0, 'status': 'planned'},
    {'id': 'ES-C11', 'indicator': 'Academy Completion', 'current': 0, 'unit': '%', 'status': 'planned'},
    {'id': 'ES-C12', 'indicator': 'Documentation Completion', 'current': 0, 'unit': '%', 'status': 'partial'},
]

CRITICAL_PATH_CATEGORIES = [
    {'id': 'on_schedule', 'label': 'Tasks on schedule', 'count': critical_path_on_schedule},
    {'id': 'at_risk', 'label': 'Tasks at risk', 'count': critical_path_at_risk},
    {'id': 'blocked', 'label': 'Blocked tasks', 'count': critical_path_blocked},
    {'id': 'dependencies', 'label': 'Dependencies', 'count': 0},
    {'id': 'resource_shortages', 'label': 'Resource shortages', 'count': 0},
    {'id': 'volunteer_needs', 'label': 'Volunteer needs', 'count': 0},
]

WAR_ROOM_PANELS = [
    'Overall completion percentage',
    'Critical path items',
    'Top ten priorities',
    'Open blockers',
    'Upcoming deadlines',
    'Volunteer assignments',
    'Recently completed milestones',
]

DEPARTMENT_STAGES = ['Planning', 'Building', 'Testing', 'Ready', 'Complete']

DEPARTMENTS = [
    {'id': 'research', 'name': 'Research', 'stage': 'Building', 'readiness_pct': ex.get('research_readiness', 43)},
    {'id': 'technology', 'name': 'Technology', 'stage': 'Building', 'readiness_pct': ex.get('technical_architecture_readiness', 38)},
    {'id': 'education', 'name': 'Education', 'stage': 'Planning', 'readiness_pct': ex.get('education_academy_readiness', 26)},
    {'id': 'leadership', 'name': 'Leadership', 'stage': 'Planning', 'readiness_pct': ex.get('citizen_leadership_academy_readiness', 34)},
    {'id': 'community', 'name': 'Community', 'stage': 'Planning', 'readiness_pct': ex.get('arkansas_community_listening_readiness', 41)},
    {'id': 'coalition', 'name': 'Coalition', 'stage': 'Building', 'readiness_pct': ex.get('coalition_readiness', 44)},
    {'id': 'communications', 'name': 'Communications', 'stage': 'Planning', 'readiness_pct': ex.get('arkansas_communications_readiness', 42)},
    {'id': 'operations', 'name': 'Operations', 'stage': 'Building', 'readiness_pct': ex.get('pmo_readiness', 46)},
    {'id': 'governance', 'name': 'Governance', 'stage': 'Building', 'readiness_pct': ex.get('governance_readiness', 46)},
    {'id': 'volunteers', 'name': 'Volunteers', 'stage': 'Planning', 'readiness_pct': ex.get('volunteer_funding_constitution_readiness', 45)},
]

ARKANSAS_PROGRESS_INDICATORS = [
    {'id': 'ES-P01', 'indicator': '75 County Goal', 'current': 0, 'target': 75},
    {'id': 'ES-P02', 'indicator': '250 City Goal', 'current': 0, 'target': 250},
    {'id': 'ES-P03', 'indicator': '15% Connected Citizen Goal', 'current': 0, 'target': 75, 'unit': 'counties at goal'},
    {'id': 'ES-P04', 'indicator': '200,000 Connected Arkansans', 'current': 0, 'target': 200_000},
    {'id': 'ES-P05', 'indicator': 'Education Leaders', 'current': 0},
    {'id': 'ES-P06', 'indicator': 'Neighborhood Leaders', 'current': 0},
    {'id': 'ES-P07', 'indicator': 'Coalition Organizations', 'current': 0},
    {'id': 'ES-P08', 'indicator': 'Community Conversations', 'current': 0},
    {'id': 'ES-P09', 'indicator': 'Academy Graduates', 'current': 0},
]

WEEKLY_EXECUTIVE_REVIEW = [
    'Completed milestones', 'Missed milestones', 'Critical risks',
    'Volunteer growth', 'County progress', 'Technology progress',
    'Research progress', 'Mission Control recommendations',
]

TIMELINE_ALIGNMENT = [
    {'build': 84, 'title': 'Strategic Plan 2035', 'jan_2027_role': 'V1 completion milestone within decade plan'},
    {'build': 85, 'title': 'Master Launch Plan', 'jan_2027_role': 'Readiness checklist for V1 mission complete'},
    {'build': 86, 'title': 'Civic Reach', 'jan_2027_role': '15% goal — growth metric after V1 complete'},
    {'build': 87, 'title': 'First 100 Days', 'jan_2027_role': 'Public operation campaign begins upon mission complete'},
    {'build': 88, 'title': 'Execution Schedule', 'jan_2027_role': 'Master countdown — single completion deadline'},
]

execution_readiness = min(
    58,
    20
    + len(MISSION_V1_DELIVERABLES) // 2
    + len(COMPLETION_TARGETS) // 2
    + len(COUNTDOWN_INDICATORS) // 2
    + len(CRITICAL_PATH_CATEGORIES) // 2
    + len(WAR_ROOM_PANELS) // 2
    + len(DEPARTMENT_STAGES)
    + len(ARKANSAS_PROGRESS_INDICATORS) // 2
    + len(WEEKLY_EXECUTIVE_REVIEW) // 2
    + 2,
)

out = {
    'version': '1.0',
    'build': 88,
    'updated': today,
    'completion_target_date': completion_target_date,
    'completion_target_label': 'Mission Complete — January 2027',
    'title': 'Master Execution Schedule v1.0',
    'subtitle': 'Mission Complete by January 2027',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/execution-schedule.html',
    'constitution': '/docs/MASTER_EXECUTION_SCHEDULE.md',
    'purpose': (
        'Execution philosophy for the entire project. January 2027 is the target date for '
        'substantial completion of Version 1 — not the launch of construction. Every department, '
        'build, milestone, and dashboard measures progress toward that deadline.'
    ),
    'governing_principle': (
        'Every build exists for one purpose: Complete the institution by January 2027. Every '
        'feature, document, volunteer, county, city, dashboard, line of code, and decision should '
        'move Mission Control closer to: Mission Complete — January 2027.'
    ),
    'execution_philosophy': {
        'title': 'Execution Philosophy',
        'january_2027_is_completion_not_construction_start': True,
        'v1_substantial_completion': True,
        'single_operational_deadline': True,
        'ready_for_statewide_public_operation': True,
    },
    'the_mission': {
        'title': 'The Mission',
        'completion_date': completion_target_date,
        'deliverables': MISSION_V1_DELIVERABLES,
        'deliverables_total': len(MISSION_V1_DELIVERABLES),
        'status': 'in_progress',
    },
    'completion_targets': {
        'title': 'Completion Targets',
        'targets': COMPLETION_TARGETS,
        'by_completion_date': completion_target_date,
        'status': 'specified',
    },
    'mission_control_countdown': {
        'title': 'Mission Control Countdown',
        'indicators': COUNTDOWN_INDICATORS,
        'days_remaining': days_remaining,
        'live': countdown_dashboard_live,
        'always_displayed': True,
        'status': 'partial',
    },
    'critical_path_management': {
        'title': 'Critical Path Management',
        'categories': CRITICAL_PATH_CATEGORIES,
        'every_deliverable_health_indicator': True,
        'status': 'planned',
    },
    'executive_war_room': {
        'title': 'Executive War Room',
        'panels': WAR_ROOM_PANELS,
        'live': executive_war_room_live,
        'daily_operating_screen': True,
        'status': 'planned',
    },
    'department_readiness': {
        'title': 'Department Readiness',
        'stages': DEPARTMENT_STAGES,
        'departments': DEPARTMENTS,
        'departments_total': len(DEPARTMENTS),
        'departments_complete': departments_complete,
        'auto_summarize_institutional_readiness': True,
        'status': 'partial',
    },
    'arkansas_progress_dashboard': {
        'title': 'Arkansas Progress Dashboard',
        'indicators': ARKANSAS_PROGRESS_INDICATORS,
        'primary_statewide_performance_indicators': True,
        'status': 'planned',
    },
    'weekly_executive_review': {
        'title': 'Weekly Executive Review',
        'review_items': WEEKLY_EXECUTIVE_REVIEW,
        'ends_with_updated_priorities': True,
        'status': 'specified',
    },
    'success_definition': {
        'title': 'Success Definition',
        'text': (
            'By January 2027, Arkansas has a functioning, trusted, volunteer-driven civic education '
            'institution with foundational systems, leadership structure, research library, technology '
            'platform, and statewide operating framework substantially complete and ready for continued growth.'
        ),
    },
    'timeline_alignment': {
        'title': 'Timeline Consistency (Builds #84–#88)',
        'january_2027_is_completion_target': True,
        'builds': TIMELINE_ALIGNMENT,
    },
    'integration': {
        'systems': [
            {'system': 'Master Launch Plan (#85)', 'route': '/mission-control/master-launch-plan.html', 'status': 'live'},
            {'system': 'Strategic Plan 2035 (#84)', 'route': '/mission-control/arkansas-strategic-plan-2035.html', 'status': 'live'},
            {'system': 'First 100 Days (#87)', 'route': '/mission-control/launch-campaign-first-100-days.html', 'status': 'live'},
            {'system': 'Civic Reach (#86)', 'route': '/mission-control/arkansas-civic-reach-participation.html', 'status': 'live'},
            {'system': 'Digital Twin (#81)', 'route': '/mission-control/institutional-digital-twin.html', 'status': 'live'},
            {'system': 'BUILD_PLAN.md', 'route': '/BUILD_PLAN.md', 'status': 'live'},
        ],
    },
    'summary': {
        'completion_target_date': completion_target_date,
        'days_remaining': days_remaining,
        'overall_institutional_completion_pct': overall_institutional_completion_pct,
        'builds_complete': build_num,
        'countdown_dashboard_live': countdown_dashboard_live,
        'executive_war_room_live': executive_war_room_live,
        'critical_path_blocked': critical_path_blocked,
        'open_blockers': open_blockers,
        'departments_complete': departments_complete,
        'departments_total': len(DEPARTMENTS),
        'execution_schedule_readiness_pct': execution_readiness,
        'master_launch_plan_readiness_pct': mlp.get('summary', {}).get('master_launch_plan_readiness_pct', 54),
        'launch_campaign_readiness_pct': l100.get('summary', {}).get('launch_campaign_first_100_days_readiness_pct', 57),
        'strategic_plan_readiness_pct': sp.get('summary', {}).get('arkansas_strategic_plan_2035_readiness_pct', 55),
        'public_launch_readiness_pct': ex.get('public_launch_readiness', 8),
    },
    'catalog_gaps': [
        'Executive War Room not live — no daily operating screen',
        'Countdown dashboard not fully operational — days in JSON only',
        '0 critical path tasks tracked — on schedule/at risk/blocked all 0',
        '0 departments at Complete stage',
        'Department completion % not auto-computed from stages',
        'Arkansas Progress Dashboard not live',
        'Weekly executive review not operationalized in MC',
        'Top ten priorities not tracked',
        'Open blockers registry empty',
        'Builds #84–#87 timeline text updated in Build #88 — regen recommended after alignment',
        'Overall completion uses build count not true % of V1 deliverables',
    ],
    'recommended_next_build': {
        'number': 91,
        'title': 'Executive War Room & Countdown Dashboard Components',
        'note': (
            'War room UI, live countdown, critical path tracker, department stage automation, '
            'Arkansas progress dashboard, weekly review workflow, COMP-* specs.'
        ),
    },
}

with open(root / 'data/execution-schedule.json', 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')

print(
    f'Execution Schedule: {days_remaining} days remaining, '
    f'{overall_institutional_completion_pct}% completion, {execution_readiness}% readiness'
)
