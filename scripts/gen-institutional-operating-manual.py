"""
Generate data/institutional-operating-manual.json — Build #90.
Master Institutional Operating Manual — If Every Founder Walked Away Tomorrow v1.0.
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
peo = load_json(root / 'data/pmo-execution-office.json')
es = load_json(root / 'data/execution-schedule.json')

ex = mc.get('executive', {})
builds_logged = len(mc.get('builds', []))

# Honest operational metrics
operations_dashboard_live = False
annual_review_conducted = False
institutional_memory_entries = 0
sops_written = 0
role_manuals_complete = 0
system_manuals_complete = 0
training_guides_complete = 0
knowledge_gaps_identified = 12

FOUNDING_PHILOSOPHY = [
    'People are temporary',
    'Institutions should endure',
    'Knowledge should never disappear because one volunteer leaves',
    'Every important process should be documented',
    'Every important decision should be traceable',
    'Every important responsibility should be transferable',
]

PLAYBOOK_SYSTEMS = [
    {'id': 'OM-S01', 'system': 'Mission Control', 'route': '/mission-control/', 'manual_status': 'partial', 'operating_manual_complete': False},
    {'id': 'OM-S02', 'system': 'Research Institute', 'route': '/mission-control/arkansas-research-institute.html', 'manual_status': 'partial', 'operating_manual_complete': False},
    {'id': 'OM-S03', 'system': 'Community Education Academy', 'route': '/mission-control/education-academy.html', 'manual_status': 'planned', 'operating_manual_complete': False},
    {'id': 'OM-S04', 'system': 'Coalition Network', 'route': '/mission-control/coalition-network.html', 'manual_status': 'partial', 'operating_manual_complete': False},
    {'id': 'OM-S05', 'system': 'Volunteer Operations', 'route': '/mission-control/volunteer-funding-constitution.html', 'manual_status': 'partial', 'operating_manual_complete': False},
    {'id': 'OM-S06', 'system': 'County Operating System', 'route': '/mission-control/arkansas-county-operating-system.html', 'manual_status': 'partial', 'operating_manual_complete': False},
    {'id': 'OM-S07', 'system': 'City Operating System', 'route': '/mission-control/arkansas-city-operating-system.html', 'manual_status': 'partial', 'operating_manual_complete': False},
    {'id': 'OM-S08', 'system': 'Neighborhood Operating System', 'route': '/mission-control/arkansas-neighborhood-operating-system.html', 'manual_status': 'partial', 'operating_manual_complete': False},
    {'id': 'OM-S09', 'system': 'Communications', 'route': '/mission-control/arkansas-communications.html', 'manual_status': 'partial', 'operating_manual_complete': False},
    {'id': 'OM-S10', 'system': 'Technology', 'route': '/mission-control/technical-architecture.html', 'manual_status': 'partial', 'operating_manual_complete': False},
    {'id': 'OM-S11', 'system': 'AI Systems', 'route': '/mission-control/institutional-ai.html', 'manual_status': 'planned', 'operating_manual_complete': False},
    {'id': 'OM-S12', 'system': 'Governance', 'route': '/mission-control/governance.html', 'manual_status': 'partial', 'operating_manual_complete': False},
    {'id': 'OM-S13', 'system': 'PMO', 'route': '/mission-control/pmo-execution-office.html', 'manual_status': 'partial', 'operating_manual_complete': False},
]

SOPS = [
    {'id': 'SOP-01', 'activity': 'Publishing an article', 'written': False, 'status': 'planned'},
    {'id': 'SOP-02', 'activity': 'Reviewing a research paper', 'written': False, 'status': 'planned'},
    {'id': 'SOP-03', 'activity': 'Onboarding a volunteer', 'written': False, 'status': 'planned'},
    {'id': 'SOP-04', 'activity': 'Creating a county page', 'written': False, 'status': 'planned'},
    {'id': 'SOP-05', 'activity': 'Hosting a community conversation', 'written': False, 'status': 'planned'},
    {'id': 'SOP-06', 'activity': 'Updating curriculum', 'written': False, 'status': 'planned'},
    {'id': 'SOP-07', 'activity': 'Adding a coalition partner', 'written': False, 'status': 'planned'},
    {'id': 'SOP-08', 'activity': 'Correcting an error', 'written': False, 'status': 'planned'},
    {'id': 'SOP-09', 'activity': 'Publishing an annual report', 'written': False, 'status': 'planned'},
    {'id': 'SOP-10', 'activity': 'Updating Mission Control after a build', 'written': False, 'status': 'partial'},
]

INSTITUTIONAL_MEMORY = [
    'Major decisions',
    'Meeting summaries',
    'Governance changes',
    'Research milestones',
    'Technology milestones',
    'Lessons learned',
    'Historical timelines',
]

ROLE_MANUALS = [
    {'id': 'RM-01', 'role': 'Executive Director (future)', 'complete': False, 'status': 'planned'},
    {'id': 'RM-02', 'role': 'Research Director', 'complete': False, 'status': 'planned'},
    {'id': 'RM-03', 'role': 'Technology Lead', 'complete': False, 'status': 'planned'},
    {'id': 'RM-04', 'role': 'County Education Director', 'complete': False, 'status': 'planned'},
    {'id': 'RM-05', 'role': 'City Education Leader', 'complete': False, 'status': 'planned'},
    {'id': 'RM-06', 'role': 'Neighborhood Education Leader', 'complete': False, 'status': 'planned'},
    {'id': 'RM-07', 'role': 'Volunteer Coordinator', 'complete': False, 'status': 'planned'},
    {'id': 'RM-08', 'role': 'Coalition Coordinator', 'complete': False, 'status': 'planned'},
    {'id': 'RM-09', 'role': 'Communications Lead', 'complete': False, 'status': 'planned'},
    {'id': 'RM-10', 'role': 'Mission Control Administrator', 'complete': False, 'status': 'planned'},
]

VOLUNTEER_KNOWLEDGE_BASE = [
    'Training guides',
    'Frequently asked questions',
    'Presentation materials',
    'Research standards',
    'Editorial standards',
    'Technology documentation',
    'Mission explanations',
    'Best practices',
]

DECISION_FRAMEWORK = [
    'Does this strengthen civic education?',
    'Does this improve public trust?',
    'Is it evidence-based?',
    'Does it align with the Constitution?',
    'Will it help future volunteers?',
    'Can it be documented clearly?',
]

CHANGE_MANAGEMENT = [
    'Purpose', 'Reason', 'Expected benefits', 'Potential risks',
    'Approval', 'Documentation', 'Mission Control update', 'Institutional memory update',
]

EMERGENCY_CONTINUITY = [
    {'id': 'EC-01', 'scenario': 'Leadership transitions', 'plan_status': 'planned'},
    {'id': 'EC-02', 'scenario': 'Technology failures', 'plan_status': 'planned'},
    {'id': 'EC-03', 'scenario': 'Volunteer turnover', 'plan_status': 'planned'},
    {'id': 'EC-04', 'scenario': 'Data restoration', 'plan_status': 'planned'},
    {'id': 'EC-05', 'scenario': 'Unexpected disruptions', 'plan_status': 'planned'},
]

DOCUMENTATION_STANDARDS = [
    'Purpose', 'Owner', 'Version', 'Revision history', 'Related systems', 'Review schedule',
]

ANNUAL_OPERATING_REVIEW = [
    'Operating manuals', 'SOPs', 'Governance documents',
    'Technology documentation', 'Training materials', 'Mission Control accuracy',
]

MC_OPERATIONS_DASHBOARD = [
    {'id': 'OM-D01', 'indicator': 'Documentation completion', 'current': 0, 'unit': '%', 'status': 'planned'},
    {'id': 'OM-D02', 'indicator': 'SOP completion', 'current': sops_written, 'target': len(SOPS), 'status': 'planned'},
    {'id': 'OM-D03', 'indicator': 'Training completion', 'current': training_guides_complete, 'status': 'planned'},
    {'id': 'OM-D04', 'indicator': 'Role manuals completed', 'current': role_manuals_complete, 'target': len(ROLE_MANUALS), 'status': 'planned'},
    {'id': 'OM-D05', 'indicator': 'Knowledge gaps', 'current': knowledge_gaps_identified, 'status': 'partial'},
    {'id': 'OM-D06', 'indicator': 'Review schedules current', 'current': 0, 'status': 'planned'},
    {'id': 'OM-D07', 'indicator': 'Institutional readiness', 'current': ex.get('overall_completion', mc.get('build', 89)), 'unit': '%', 'status': 'partial'},
]

institutional_operating_manual_readiness = min(
    62,
    16
    + len(FOUNDING_PHILOSOPHY) // 2
    + len(PLAYBOOK_SYSTEMS) // 2
    + len(SOPS) // 2
    + len(INSTITUTIONAL_MEMORY) // 2
    + len(ROLE_MANUALS) // 2
    + len(VOLUNTEER_KNOWLEDGE_BASE) // 2
    + len(DECISION_FRAMEWORK) // 2
    + len(CHANGE_MANAGEMENT) // 2
    + len(EMERGENCY_CONTINUITY) // 2
    + len(DOCUMENTATION_STANDARDS) // 2
    + len(ANNUAL_OPERATING_REVIEW) // 2
    + len(MC_OPERATIONS_DASHBOARD) // 2
    + (2 if operations_dashboard_live else 0),
)

out = {
    'version': '1.0',
    'build': 90,
    'updated': today,
    'completion_target_date': completion_target_date,
    'title': 'Master Institutional Operating Manual v1.0',
    'subtitle': 'If Every Founder Walked Away Tomorrow — The Institution Must Continue',
    'tagline': 'The Institution Must Continue',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/institutional-operating-manual.html',
    'constitution': '/docs/MASTER_INSTITUTIONAL_OPERATING_MANUAL.md',
    'purpose': (
        'Complete guide allowing future volunteers and leaders to understand, operate, improve, '
        'and preserve Citizens United Facts without relying on institutional memory held by a '
        'few individuals. If every founding volunteer stepped away tomorrow, a new generation '
        'should continue the mission using this manual and Mission Control.'
    ),
    'governing_principle': (
        'Institutions fail when knowledge disappears. Institutions endure when knowledge is '
        'preserved. The Operating Manual exists so Citizens United Facts will never depend upon '
        'one person, one memory, or one generation — every generation leaves the next a better '
        'map than the one they inherited.'
    ),
    'founders_legacy': (
        'The greatest gift the founders can leave is not a website — it is clarity. Future '
        'volunteers should never have to guess. They should inherit an institution where every '
        'important process has been thoughtfully documented, every major decision preserved, '
        'and every lesson learned passed forward. That is how institutions outlive individuals.'
    ),
    'founding_philosophy': {
        'title': 'Founding Philosophy',
        'principles': FOUNDING_PHILOSOPHY,
        'people_temporary_institutions_endure': True,
    },
    'institutional_playbook': {
        'title': 'Institutional Playbook',
        'systems': PLAYBOOK_SYSTEMS,
        'systems_total': len(PLAYBOOK_SYSTEMS),
        'manuals_complete': system_manuals_complete,
        'every_system_independently_understandable': True,
        'status': 'partial',
        'note': f'{builds_logged} builds documented — formal per-system operating manuals not complete',
    },
    'standard_operating_procedures': {
        'title': 'Standard Operating Procedures',
        'sops': SOPS,
        'sops_total': len(SOPS),
        'sops_written': sops_written,
        'no_tribal_knowledge': True,
        'status': 'planned',
    },
    'institutional_memory': {
        'title': 'Institutional Memory',
        'categories': INSTITUTIONAL_MEMORY,
        'entries_preserved': institutional_memory_entries,
        'mc_permanently_preserves': True,
        'status': 'planned',
    },
    'role_manuals': {
        'title': 'Role Manuals',
        'roles': ROLE_MANUALS,
        'roles_total': len(ROLE_MANUALS),
        'manuals_complete': role_manuals_complete,
        'responsibilities_before_beginning': True,
        'status': 'planned',
    },
    'volunteer_knowledge_base': {
        'title': 'Volunteer Knowledge Base',
        'resources': VOLUNTEER_KNOWLEDGE_BASE,
        'institution_teaches_its_own_volunteers': True,
        'status': 'partial',
    },
    'decision_framework': {
        'title': 'Decision Framework',
        'questions': DECISION_FRAMEWORK,
        'decision_compass': True,
        'status': 'specified',
    },
    'change_management': {
        'title': 'Change Management',
        'steps': CHANGE_MANAGEMENT,
        'future_leaders_understand_why': True,
        'status': 'specified',
    },
    'emergency_continuity': {
        'title': 'Emergency Continuity',
        'scenarios': EMERGENCY_CONTINUITY,
        'essential_operations_continue': True,
        'status': 'planned',
    },
    'documentation_standards': {
        'title': 'Documentation Standards',
        'fields': DOCUMENTATION_STANDARDS,
        'documentation_as_infrastructure': True,
        'status': 'specified',
    },
    'annual_operating_review': {
        'title': 'Annual Operating Review',
        'review_items': ANNUAL_OPERATING_REVIEW,
        'conducted': annual_review_conducted,
        'manual_remains_current': True,
        'status': 'planned',
    },
    'mission_control_operations_dashboard': {
        'title': 'Mission Control Operations Dashboard',
        'indicators': MC_OPERATIONS_DASHBOARD,
        'live': operations_dashboard_live,
        'documentation_health_measurable': True,
        'status': 'planned',
    },
    'integration': {
        'chain': (
            'Mission Control → PMO → Research Institute → Community Education Academy → '
            'Volunteer Network → Technology → Governance → Digital Twin'
        ),
        'every_system_contributes_to_continuity': True,
        'systems': [
            {'system': 'PMO Execution Office (#89)', 'route': '/mission-control/pmo-execution-office.html', 'status': 'live'},
            {'system': 'Execution Schedule (#88)', 'route': '/mission-control/execution-schedule.html', 'status': 'live'},
            {'system': 'Organizational Constitution (#76)', 'route': '/mission-control/organizational-constitution.html', 'status': 'live'},
            {'system': 'Digital Twin (#81)', 'route': '/mission-control/institutional-digital-twin.html', 'status': 'live'},
            {'system': 'Research Institute (#73)', 'route': '/mission-control/arkansas-research-institute.html', 'status': 'live'},
            {'system': 'Governance (#49)', 'route': '/mission-control/governance.html', 'status': 'live'},
        ],
    },
    'long_term_vision': (
        'Imagine Citizens United Facts thirty years from now. Most volunteers have never met the '
        'founders. Yet they understand why the institution exists, how it operates, how decisions '
        'are made, how research is conducted, how communities are served, and how Mission Control '
        'functions — because every generation inherited complete operational knowledge.'
    ),
    'summary': {
        'completion_target_date': completion_target_date,
        'days_remaining': days_remaining,
        'institutional_operating_manual_readiness_pct': institutional_operating_manual_readiness,
        'pmo_execution_office_readiness_pct': peo.get('summary', {}).get('pmo_execution_office_readiness_pct', 60),
        'execution_schedule_readiness_pct': es.get('summary', {}).get('execution_schedule_readiness_pct', 56),
        'system_manuals_complete': system_manuals_complete,
        'system_manuals_total': len(PLAYBOOK_SYSTEMS),
        'sops_written': sops_written,
        'sops_total': len(SOPS),
        'role_manuals_complete': role_manuals_complete,
        'role_manuals_total': len(ROLE_MANUALS),
        'institutional_memory_entries': institutional_memory_entries,
        'operations_dashboard_live': operations_dashboard_live,
        'annual_review_conducted': annual_review_conducted,
        'knowledge_gaps_identified': knowledge_gaps_identified,
        'builds_documented': builds_logged,
        'institutional_completion_pct': ex.get('overall_completion', mc.get('build', 89)),
    },
    'catalog_gaps': [
        'Operations dashboard not live — documentation health not measurable',
        '0/13 system operating manuals complete',
        '0/10 SOPs written — processes depend on tribal knowledge',
        '0/10 role manuals complete',
        'Institutional memory registry empty — 0 entries',
        'Annual operating review not conducted',
        'Emergency continuity plans not written',
        'Volunteer knowledge base partial — no unified portal',
        'Change management workflow not operational in MC',
        'MASTER docs exist for many systems — operating manuals distinct and incomplete',
        'Decision register from PMO #89 empty — not linked to institutional memory',
    ],
    'recommended_next_build': {
        'number': 92,
        'title': 'Executive War Room & Countdown Dashboard Components',
        'note': (
            'War room UI, live countdown, documentation health dashboard, SOP registry, '
            'institutional memory store, COMP-* specs.'
        ),
    },
}

with open(root / 'data/institutional-operating-manual.json', 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')

print(
    f'Institutional Operating Manual: {system_manuals_complete}/{len(PLAYBOOK_SYSTEMS)} manuals, '
    f'{sops_written}/{len(SOPS)} SOPs, {institutional_operating_manual_readiness}% readiness'
)
