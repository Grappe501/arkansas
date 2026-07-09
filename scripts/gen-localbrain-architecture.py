"""
Generate data/localbrain-architecture.json — Build #92.
Master LocalBrain Architecture — Distributed Institutional Intelligence v1.0.
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
ai91 = load_json(root / 'data/ai-institution.json')
iom = load_json(root / 'data/institutional-operating-manual.json')

ex = mc.get('executive', {})

# Honest operational metrics
executive_dashboard_live = False
executive_calendar_merged = False
inter_brain_communication = False
localbrains_online = 0
memory_entries_total = 0
calendar_conflicts = 0
inter_brain_messages = 0

LOCALBRAIN_PRINCIPLE_STACK = [
    'Knowledge', 'Memory', 'Calendar', 'Projects', 'Documents',
    'AI Agents', 'Tasks', 'Dashboards', 'Relationships', 'Reports',
]

CORE_LOCALBRAINS = [
    {'id': 'LB-01', 'name': 'Mission Control Brain', 'domain': 'Executive', 'route': '/mission-control/', 'online': False, 'health': 'planned'},
    {'id': 'LB-02', 'name': 'Research Brain', 'domain': 'Research', 'route': '/mission-control/arkansas-research-institute.html', 'online': False, 'health': 'planned'},
    {'id': 'LB-03', 'name': 'Evidence Brain', 'domain': 'Evidence', 'route': '/mission-control/evidence-ledger.html', 'online': False, 'health': 'planned'},
    {'id': 'LB-04', 'name': 'Claims Brain', 'domain': 'Claims', 'route': '/mission-control/facts.html', 'online': False, 'health': 'planned'},
    {'id': 'LB-05', 'name': 'Knowledge Graph Brain', 'domain': 'Knowledge', 'route': '/mission-control/knowledge-graph.html', 'online': False, 'health': 'partial'},
    {'id': 'LB-06', 'name': 'Community Education Academy Brain', 'domain': 'Academy', 'route': '/mission-control/education-academy.html', 'online': False, 'health': 'planned'},
    {'id': 'LB-07', 'name': 'County Operations Brain', 'domain': 'County', 'route': '/mission-control/arkansas-county-operating-system.html', 'online': False, 'health': 'planned'},
    {'id': 'LB-08', 'name': 'City Operations Brain', 'domain': 'City', 'route': '/mission-control/arkansas-city-operating-system.html', 'online': False, 'health': 'planned'},
    {'id': 'LB-09', 'name': 'Neighborhood Operations Brain', 'domain': 'Neighborhood', 'route': '/mission-control/arkansas-neighborhood-operating-system.html', 'online': False, 'health': 'planned'},
    {'id': 'LB-10', 'name': 'Volunteer Brain', 'domain': 'Volunteers', 'route': '/mission-control/volunteer-funding-constitution.html', 'online': False, 'health': 'planned'},
    {'id': 'LB-11', 'name': 'Coalition Brain', 'domain': 'Coalition', 'route': '/mission-control/coalition-network.html', 'online': False, 'health': 'planned'},
    {'id': 'LB-12', 'name': 'Communications Brain', 'domain': 'Communications', 'route': '/mission-control/arkansas-communications.html', 'online': False, 'health': 'planned'},
    {'id': 'LB-13', 'name': 'Media Brain', 'domain': 'Media', 'route': '/mission-control/media-studio.html', 'online': False, 'health': 'planned'},
    {'id': 'LB-14', 'name': 'Technology Brain', 'domain': 'Technology', 'route': '/mission-control/technical-architecture.html', 'online': False, 'health': 'partial'},
    {'id': 'LB-15', 'name': 'AI Operations Brain', 'domain': 'AI', 'route': '/mission-control/ai-institution.html', 'online': False, 'health': 'partial'},
    {'id': 'LB-16', 'name': 'Governance Brain', 'domain': 'Governance', 'route': '/mission-control/governance.html', 'online': False, 'health': 'partial'},
    {'id': 'LB-17', 'name': 'Project Management Office Brain', 'domain': 'PMO', 'route': '/mission-control/pmo-execution-office.html', 'online': False, 'health': 'partial'},
    {'id': 'LB-18', 'name': 'Relationship Brain', 'domain': 'Relationships', 'route': '/mission-control/relationship-os.html', 'online': False, 'health': 'planned'},
    {'id': 'LB-19', 'name': 'Campaign Finance Observatory Brain', 'domain': 'Campaign Finance', 'route': '/mission-control/campaign-finance-observatory.html', 'online': False, 'health': 'planned'},
    {'id': 'LB-20', 'name': 'Civic Innovation Brain', 'domain': 'Innovation', 'route': '/mission-control/arkansas-civic-innovation-reform.html', 'online': False, 'health': 'planned'},
]

LOCALBRAIN_MEMORY = [
    'Institutional history', 'Notes', 'Decisions', 'Context', 'Lessons learned',
]

LOCALBRAIN_CALENDAR = [
    'Department calendar', 'Milestones', 'Meetings', 'Review dates',
    'Publication schedules', 'Volunteer activities',
]

LOCALBRAIN_AI_TEAM = [
    'Specialized AI agents', 'Research assistants', 'Planning assistants',
    'Writing assistants', 'Review assistants',
]

LOCALBRAIN_TASK_ENGINE = [
    'Current work', 'Backlog', 'Dependencies', 'Assignments', 'Deadlines',
]

LOCALBRAIN_KNOWLEDGE_BASE = [
    'Documents', 'Research', 'Policies', 'Templates', 'Media', 'References',
]

CROSS_BRAIN_FLOW = [
    {'step': 1, 'brain': 'Research Brain', 'action': 'Publishes new research'},
    {'step': 2, 'brain': 'Communications Brain', 'action': 'Prepares educational content'},
    {'step': 3, 'brain': 'Academy Brain', 'action': 'Updates lessons'},
    {'step': 4, 'brain': 'Mission Control Brain', 'action': 'Updates readiness'},
    {'step': 5, 'brain': 'County Brain', 'action': 'Distributes local resources'},
    {'step': 6, 'brain': 'Volunteer Brain', 'action': 'Notifies Education Leaders'},
]

MC_INTEGRATION_VISIBILITY = [
    'Department health', 'Project status', 'Calendar conflicts',
    'Shared resources', 'Cross-department dependencies', 'Institutional readiness',
]

EXECUTIVE_CALENDAR_VIEWS = [
    'Research deadlines', 'Volunteer events', 'Community conversations',
    'Coalition meetings', 'Academy schedules', 'Technology releases', 'Annual reviews',
]

INSTITUTIONAL_MEMORY_PRESERVES = [
    'Meeting notes', 'Project history', 'Major decisions',
    'Lessons learned', 'Revision history',
]

EXECUTIVE_DASHBOARD_INDICATORS = [
    {'id': 'LB-D01', 'indicator': 'LocalBrains online', 'current': localbrains_online, 'target': len(CORE_LOCALBRAINS), 'status': 'planned'},
    {'id': 'LB-D02', 'indicator': 'LocalBrain health', 'current': 0, 'unit': '%', 'status': 'planned'},
    {'id': 'LB-D03', 'indicator': 'Knowledge growth', 'current': 0, 'status': 'planned'},
    {'id': 'LB-D04', 'indicator': 'Memory growth', 'current': memory_entries_total, 'status': 'planned'},
    {'id': 'LB-D05', 'indicator': 'Calendar conflicts', 'current': calendar_conflicts, 'status': 'planned'},
    {'id': 'LB-D06', 'indicator': 'Task completion', 'current': 0, 'unit': '%', 'status': 'planned'},
    {'id': 'LB-D07', 'indicator': 'AI activity', 'current': 0, 'status': 'planned'},
    {'id': 'LB-D08', 'indicator': 'Inter-Brain communication', 'current': inter_brain_messages, 'status': 'planned'},
    {'id': 'LB-D09', 'indicator': 'Institutional synchronization', 'current': 0, 'unit': '%', 'status': 'planned'},
]

FUTURE_EXPANSION = [
    'Arkansas legislative tracking',
    'Ballot initiative education',
    'Federal policy education',
    'Media monitoring',
    'Historical archives',
    'Public records',
    'Research collaborations',
]

localbrain_architecture_readiness = min(
    65,
    15
    + len(CORE_LOCALBRAINS) // 2
    + len(LOCALBRAIN_PRINCIPLE_STACK) // 2
    + len(LOCALBRAIN_MEMORY) // 2
    + len(LOCALBRAIN_CALENDAR) // 2
    + len(LOCALBRAIN_AI_TEAM) // 2
    + len(LOCALBRAIN_TASK_ENGINE) // 2
    + len(LOCALBRAIN_KNOWLEDGE_BASE) // 2
    + len(CROSS_BRAIN_FLOW) // 2
    + len(MC_INTEGRATION_VISIBILITY) // 2
    + len(EXECUTIVE_CALENDAR_VIEWS) // 2
    + len(INSTITUTIONAL_MEMORY_PRESERVES) // 2
    + len(EXECUTIVE_DASHBOARD_INDICATORS) // 2
    + len(FUTURE_EXPANSION) // 2
    + (2 if executive_dashboard_live else 0),
)

out = {
    'version': '1.0',
    'build': 92,
    'updated': today,
    'completion_target_date': completion_target_date,
    'title': 'Master LocalBrain Architecture v1.0',
    'subtitle': 'The Distributed Institutional Intelligence System',
    'tagline': 'Federation of Specialized LocalBrains',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/localbrain-architecture.html',
    'constitution': '/docs/MASTER_LOCALBRAIN_ARCHITECTURE.md',
    'purpose': (
        'Federation of specialized LocalBrains — no single AI, database, or dashboard '
        'carries the entire institution. Each LocalBrain owns one domain while remaining '
        'connected through Mission Control as the executive coordination layer.'
    ),
    'governing_principle': (
        'Locally informed. Globally coordinated. Every LocalBrain masters its own domain. '
        'Mission Control unifies them into one living institution capable of serving '
        'Arkansas with clarity, consistency, intelligence, and purpose for generations.'
    ),
    'founders_principle': (
        'No volunteer should wonder where a document is, who knows the answer, what '
        'happened last year, or what to work on today. Every department remembers, every '
        'AI assists, every calendar coordinates, and every volunteer contributes from day one.'
    ),
    'institutional_philosophy': {
        'title': 'Institutional Philosophy',
        'living_organization': True,
        'every_department_has': [
            'Its own memory', 'Its own calendar', 'Its own tasks',
            'Its own documents', 'Its own AI assistants', 'Its own dashboards',
        ],
        'mission_control_connects': True,
    },
    'localbrain_principle': {
        'title': 'The LocalBrain Principle',
        'stack': LOCALBRAIN_PRINCIPLE_STACK,
        'miniature_institution': True,
        'independently_intelligent': True,
    },
    'core_localbrains': {
        'title': 'Core LocalBrains',
        'brains': CORE_LOCALBRAINS,
        'brains_total': len(CORE_LOCALBRAINS),
        'brains_online': localbrains_online,
        'modular_expansion': True,
        'status': 'planned',
    },
    'every_localbrain_contains': {
        'title': 'Every LocalBrain Contains',
        'memory': {'title': 'Memory', 'items': LOCALBRAIN_MEMORY},
        'calendar': {'title': 'Calendar', 'items': LOCALBRAIN_CALENDAR},
        'ai_team': {'title': 'AI Team', 'items': LOCALBRAIN_AI_TEAM},
        'task_engine': {'title': 'Task Engine', 'items': LOCALBRAIN_TASK_ENGINE},
        'knowledge_base': {'title': 'Knowledge Base', 'items': LOCALBRAIN_KNOWLEDGE_BASE},
        'permanent_department_memory': True,
    },
    'mission_control_integration': {
        'title': 'Mission Control Integration',
        'executive_coordination_layer': True,
        'visibility': MC_INTEGRATION_VISIBILITY,
        'status': 'partial',
    },
    'cross_brain_communication': {
        'title': 'Cross-Brain Communication',
        'automatic': inter_brain_communication,
        'flow_example': CROSS_BRAIN_FLOW,
        'knowledge_flows_automatically': True,
        'status': 'planned',
    },
    'institutional_calendar': {
        'title': 'Institutional Calendar',
        'each_brain_own_calendar': True,
        'executive_calendar_merged': executive_calendar_merged,
        'executive_views': EXECUTIVE_CALENDAR_VIEWS,
        'nothing_operates_in_isolation': True,
        'status': 'planned',
    },
    'institutional_memory': {
        'title': 'Institutional Memory',
        'preserves': INSTITUTIONAL_MEMORY_PRESERVES,
        'entries_total': memory_entries_total,
        'future_volunteers_inherit_immediately': True,
        'status': 'planned',
    },
    'executive_dashboard': {
        'title': 'Executive Dashboard',
        'indicators': EXECUTIVE_DASHBOARD_INDICATORS,
        'live': executive_dashboard_live,
        'leadership_always_understands_status': True,
        'status': 'planned',
    },
    'expansion': {
        'title': 'Expansion',
        'future_localbrains': FUTURE_EXPANSION,
        'modular_by_design': True,
        'status': 'specified',
    },
    'integration': {
        'chain': (
            'Mission Control → Digital Twin → AI Institution → Operating Manual → '
            'Knowledge Graph → Community Education Academy → County OS → Relationship OS'
        ),
        'every_capability_specialized_intelligence_node': True,
        'systems': [
            {'system': 'AI Institution (#91)', 'route': '/mission-control/ai-institution.html', 'status': 'live'},
            {'system': 'Operating Manual (#90)', 'route': '/mission-control/institutional-operating-manual.html', 'status': 'live'},
            {'system': 'Digital Twin (#81)', 'route': '/mission-control/institutional-digital-twin.html', 'status': 'live'},
            {'system': 'Knowledge Graph', 'route': '/mission-control/knowledge-graph.html', 'status': 'partial'},
            {'system': 'PMO (#89)', 'route': '/mission-control/pmo-execution-office.html', 'status': 'live'},
            {'system': 'Relationship OS (#59)', 'route': '/mission-control/relationship-os.html', 'status': 'live'},
        ],
    },
    'long_term_vision': (
        'By January 2027, Citizens United Facts operates as a network of cooperating '
        'institutional intelligences. Every department knows its mission. Every AI knows '
        'its domain. Every volunteer has immediate access to institutional knowledge. '
        'Mission Control provides executive awareness. Intelligence is distributed — '
        'faster, more organized, more resilient.'
    ),
    'summary': {
        'completion_target_date': completion_target_date,
        'days_remaining': days_remaining,
        'localbrain_architecture_readiness_pct': localbrain_architecture_readiness,
        'ai_institution_readiness_pct': ai91.get('summary', {}).get('ai_institution_readiness_pct', 57),
        'operating_manual_readiness_pct': iom.get('summary', {}).get('institutional_operating_manual_readiness_pct', 60),
        'localbrains_online': localbrains_online,
        'localbrains_total': len(CORE_LOCALBRAINS),
        'executive_dashboard_live': executive_dashboard_live,
        'executive_calendar_merged': executive_calendar_merged,
        'inter_brain_communication': inter_brain_communication,
        'memory_entries_total': memory_entries_total,
        'calendar_conflicts': calendar_conflicts,
        'institutional_completion_pct': ex.get('overall_completion', mc.get('build', 91)),
    },
    'catalog_gaps': [
        '0/20 LocalBrains online — architecture blueprint only',
        'Executive dashboard not live',
        'Executive calendar not merged from brain calendars',
        'Inter-brain communication not operational',
        'No per-brain memory/calendar/task stores',
        'Cross-brain flow example specified — not automated',
        'LocalBrain health scores not computed',
        'Institutional synchronization 0%',
        'Future expansion LocalBrains not provisioned',
        'MC dashboards partial — not true LocalBrain nodes yet',
        'AI Operations Brain links to #91 — specialists not deployed per brain',
    ],
    'recommended_next_build': {
        'number': 93,
        'title': 'Executive War Room & Countdown Dashboard Components',
        'note': (
            'War room UI, LocalBrain registry, executive calendar merge, inter-brain '
            'messaging, health dashboard, COMP-* specs.'
        ),
    },
}

with open(root / 'data/localbrain-architecture.json', 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')

print(
    f'LocalBrain Architecture: {localbrains_online}/{len(CORE_LOCALBRAINS)} online, '
    f'{localbrain_architecture_readiness}% readiness'
)
