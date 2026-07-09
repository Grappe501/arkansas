"""
Generate data/civic-intelligence-command-center.json — Build #65.
Arkansas Civic Intelligence Command Center v1.0.
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
mc2 = load_json(root / 'data/mc2-executive.json')
el = load_json(root / 'data/evidence-ledger.json')
aan = load_json(root / 'data/arkansas-action-network.json')
cn = load_json(root / 'data/coalition-network.json')
cac = load_json(root / 'data/citizen-action-center.json')

ex = mc.get('executive', {})
el_sum = el.get('summary', {})
aan_sum = aan.get('summary', {})

# Honest metrics from registries
research_articles = len(mc.get('entries', [])) if isinstance(mc.get('entries'), list) else 1
evidence_claims = el_sum.get('claims_total', 0)
verified_sources = el_sum.get('evidence_items_total', 0) - el_sum.get('evidence_awaiting_review', 0)
published_lessons = 0
academy_graduates = 0
education_leaders = aan_sum.get('neighborhood_leaders', 0) + aan_sum.get('city_leaders', 0) + aan_sum.get('county_directors', 0)
county_teams = aan_sum.get('county_teams', 0)
city_teams = aan_sum.get('city_teams', 0)
neighborhood_leaders = aan_sum.get('neighborhood_leaders', 0)
coalition_orgs = cn.get('summary', {}).get('organizations_total', 0)
community_conversations = 0
registered_participants = cac.get('summary', {}).get('registered_participants', 0)
avg_learning_completion = 0
volunteer_retention = 0
PARTICIPANTS_TARGET = 200_000

EXECUTIVE_DASHBOARD = [
    {'id': 'CICC-ED-1', 'metric': 'Overall Institutional Health Score', 'current': ex.get('institutional_maturity_pct', 51), 'unit': 'percent', 'status': 'partial'},
    {'id': 'CICC-ED-2', 'metric': 'Overall Launch Readiness', 'current': ex.get('public_launch_readiness', 8), 'unit': 'percent', 'status': 'live'},
    {'id': 'CICC-ED-3', 'metric': 'Overall Educational Reach', 'current': 0, 'unit': 'counties_active', 'target': 75, 'status': 'planned'},
    {'id': 'CICC-ED-4', 'metric': 'Research Completion', 'current': ex.get('research_readiness', 26), 'unit': 'percent', 'status': 'partial'},
    {'id': 'CICC-ED-5', 'metric': 'Engineering Completion', 'current': ex.get('technical_architecture_readiness', 38), 'unit': 'percent', 'status': 'partial'},
    {'id': 'CICC-ED-6', 'metric': 'Content Completion', 'current': ex.get('content_readiness', 28), 'unit': 'percent', 'status': 'partial'},
    {'id': 'CICC-ED-7', 'metric': 'Coalition Growth', 'current': coalition_orgs, 'target': None, 'status': 'live'},
    {'id': 'CICC-ED-8', 'metric': 'Education Leader Growth', 'current': education_leaders, 'status': 'live'},
    {'id': 'CICC-ED-9', 'metric': 'County Coverage', 'current': county_teams, 'target': 75, 'status': 'live'},
    {'id': 'CICC-ED-10', 'metric': 'City Coverage', 'current': city_teams, 'target': 250, 'status': 'live'},
    {'id': 'CICC-ED-11', 'metric': 'Neighborhood Coverage', 'current': neighborhood_leaders, 'status': 'live'},
    {'id': 'CICC-ED-12', 'metric': 'Progress toward 200,000 Arkansans', 'current': aan_sum.get('connected_arkansans', 0), 'target': PARTICIPANTS_TARGET, 'status': 'live'},
]

EXECUTIVE_KPI_CARDS = [
    {'id': 'CICC-KPI-1', 'label': 'Research Articles', 'current': research_articles, 'route': '/mission-control/research-library.html', 'status': 'partial'},
    {'id': 'CICC-KPI-2', 'label': 'Evidence Claims', 'current': evidence_claims, 'route': '/mission-control/evidence-ledger.html', 'status': 'live'},
    {'id': 'CICC-KPI-3', 'label': 'Verified Sources', 'current': verified_sources, 'route': '/mission-control/evidence-ledger.html', 'status': 'live'},
    {'id': 'CICC-KPI-4', 'label': 'Published Lessons', 'current': published_lessons, 'route': '/mission-control/curriculum.html', 'status': 'planned'},
    {'id': 'CICC-KPI-5', 'label': 'Academy Graduates', 'current': academy_graduates, 'route': '/mission-control/education-academy.html', 'status': 'planned'},
    {'id': 'CICC-KPI-6', 'label': 'Education Leaders', 'current': education_leaders, 'route': '/mission-control/arkansas-action-network.html', 'status': 'live'},
    {'id': 'CICC-KPI-7', 'label': 'County Teams', 'current': county_teams, 'target': 75, 'route': '/mission-control/county-os.html', 'status': 'live'},
    {'id': 'CICC-KPI-8', 'label': 'City Teams', 'current': city_teams, 'target': 250, 'route': '/mission-control/civic-atlas.html', 'status': 'live'},
    {'id': 'CICC-KPI-9', 'label': 'Neighborhood Leaders', 'current': neighborhood_leaders, 'route': '/mission-control/neighborhood-organizing.html', 'status': 'live'},
    {'id': 'CICC-KPI-10', 'label': 'Coalition Organizations', 'current': coalition_orgs, 'route': '/mission-control/coalition-network.html', 'status': 'live'},
    {'id': 'CICC-KPI-11', 'label': 'Community Conversations', 'current': community_conversations, 'status': 'planned'},
    {'id': 'CICC-KPI-12', 'label': 'Registered Participants', 'current': registered_participants, 'route': '/mission-control/citizen-action-center.html', 'status': 'live'},
    {'id': 'CICC-KPI-13', 'label': 'Average Learning Completion', 'current': avg_learning_completion, 'unit': 'percent', 'status': 'planned'},
    {'id': 'CICC-KPI-14', 'label': 'Volunteer Retention', 'current': volunteer_retention, 'unit': 'percent', 'status': 'planned'},
    {'id': 'CICC-KPI-15', 'label': 'Overall Institutional Readiness', 'current': ex.get('institutional_maturity_pct', 51), 'unit': 'percent', 'status': 'partial'},
]

DEPARTMENT_BOARDS = [
    {'id': 'CICC-DEPT-1', 'department': 'Research Office', 'route': '/mission-control/research-observatory.html', 'status': 'partial'},
    {'id': 'CICC-DEPT-2', 'department': 'Editorial Office', 'route': '/mission-control/content-factory.html', 'status': 'planned'},
    {'id': 'CICC-DEPT-3', 'department': 'Engineering Office', 'route': '/mission-control/technical-architecture.html', 'status': 'partial'},
    {'id': 'CICC-DEPT-4', 'department': 'Design Office', 'route': '/mission-control/design.html', 'status': 'partial'},
    {'id': 'CICC-DEPT-5', 'department': 'Academy Office', 'route': '/mission-control/education-academy.html', 'status': 'partial'},
    {'id': 'CICC-DEPT-6', 'department': 'Coalition Office', 'route': '/mission-control/coalition-network.html', 'status': 'live'},
    {'id': 'CICC-DEPT-7', 'department': 'Community Office', 'route': '/mission-control/neighborhood-organizing.html', 'status': 'partial'},
    {'id': 'CICC-DEPT-8', 'department': 'Media Office', 'route': '/mission-control/media-studio.html', 'status': 'planned'},
    {'id': 'CICC-DEPT-9', 'department': 'Mission Control Office', 'route': '/mission-control/', 'status': 'live'},
    {'id': 'CICC-DEPT-10', 'department': 'Operations Office', 'route': '/mission-control/pmo.html', 'status': 'partial'},
]

BOARD_FIELDS = ['Projects', 'Progress', 'Blockers', 'Risks', 'Upcoming milestones']

INSTITUTIONAL_PULSE = [
    {'id': 'CICC-PULSE-1', 'signal': 'Research velocity', 'status': 'planned'},
    {'id': 'CICC-PULSE-2', 'signal': 'Content production', 'status': 'planned'},
    {'id': 'CICC-PULSE-3', 'signal': 'Volunteer growth', 'status': 'planned'},
    {'id': 'CICC-PULSE-4', 'signal': 'Leadership development', 'status': 'planned'},
    {'id': 'CICC-PULSE-5', 'signal': 'Coalition expansion', 'status': 'planned'},
    {'id': 'CICC-PULSE-6', 'signal': 'Website health', 'status': 'partial', 'note': 'Netlify production_healthy'},
    {'id': 'CICC-PULSE-7', 'signal': 'Learning engagement', 'status': 'planned'},
    {'id': 'CICC-PULSE-8', 'signal': 'Relationship health', 'status': 'planned'},
    {'id': 'CICC-PULSE-9', 'signal': 'Community activity', 'status': 'planned'},
]

GROWTH_DASHBOARD = [
    {'id': 'CICC-GROW-1', 'goal': '75 County Goal', 'current': county_teams, 'target': 75, 'progress_pct': 0},
    {'id': 'CICC-GROW-2', 'goal': '250 City Goal', 'current': city_teams, 'target': 250, 'progress_pct': 0},
    {'id': 'CICC-GROW-3', 'goal': '200,000 Participant Goal', 'current': aan_sum.get('connected_arkansans', 0), 'target': PARTICIPANTS_TARGET, 'progress_pct': 0},
    {'id': 'CICC-GROW-4', 'goal': 'Education Leader Goal', 'current': education_leaders, 'target': None, 'progress_pct': 0},
    {'id': 'CICC-GROW-5', 'goal': 'Neighborhood Growth', 'current': neighborhood_leaders, 'status': 'scaffolded'},
    {'id': 'CICC-GROW-6', 'goal': 'Coalition Growth', 'current': coalition_orgs, 'status': 'scaffolded'},
    {'id': 'CICC-GROW-7', 'goal': 'Monthly Growth Rate', 'current': 'not tracked', 'status': 'planned'},
    {'id': 'CICC-GROW-8', 'goal': 'Projected Completion', 'current': 'not calculated', 'status': 'planned'},
]

EXECUTIVE_ALERTS = [
    {'id': 'CICC-ALERT-1', 'example': 'County lost its only Education Leader', 'status': 'planned'},
    {'id': 'CICC-ALERT-2', 'example': 'Research review overdue', 'status': 'planned'},
    {'id': 'CICC-ALERT-3', 'example': 'Broken citation detected', 'status': 'planned'},
    {'id': 'CICC-ALERT-4', 'example': 'Coalition partner inactive', 'status': 'planned'},
    {'id': 'CICC-ALERT-5', 'example': 'Community conversation cancelled', 'status': 'planned'},
    {'id': 'CICC-ALERT-6', 'example': 'Technology outage', 'status': 'planned'},
    {'id': 'CICC-ALERT-7', 'example': 'Accessibility regression', 'status': 'planned'},
    {'id': 'CICC-ALERT-8', 'example': 'Upcoming legislative session', 'status': 'planned'},
]

OPPORTUNITY_ENGINE = [
    {'id': 'CICC-OPP-1', 'example': 'County approaching leadership target', 'status': 'planned'},
    {'id': 'CICC-OPP-2', 'example': 'City ready for first Education Leader', 'status': 'planned'},
    {'id': 'CICC-OPP-3', 'example': 'Organization interested in joining coalition', 'status': 'planned'},
    {'id': 'CICC-OPP-4', 'example': 'Popular lesson needing expansion', 'status': 'planned'},
    {'id': 'CICC-OPP-5', 'example': 'Frequently searched topic lacking content', 'status': 'planned'},
    {'id': 'CICC-OPP-6', 'example': 'Community requesting presentation', 'status': 'planned'},
]

READINESS_INDEX_CATEGORIES = [
    {'category': 'Research', 'score': ex.get('research_readiness', 26), 'status': 'partial'},
    {'category': 'Evidence', 'score': ex.get('evidence_ledger_readiness', 22), 'status': 'partial'},
    {'category': 'Engineering', 'score': ex.get('technical_architecture_readiness', 38), 'status': 'partial'},
    {'category': 'Education', 'score': ex.get('education_academy_readiness', 26), 'status': 'partial'},
    {'category': 'Community', 'score': ex.get('neighborhood_organizing_readiness', 50), 'status': 'partial'},
    {'category': 'Coalition', 'score': ex.get('coalition_readiness', 44), 'status': 'partial'},
    {'category': 'Media', 'score': ex.get('media_studio_readiness', 18), 'status': 'planned'},
    {'category': 'Technology', 'score': ex.get('technical_architecture_readiness', 38), 'status': 'partial'},
    {'category': 'Accessibility', 'score': 0, 'status': 'planned'},
    {'category': 'Governance', 'score': ex.get('governance_readiness', 44), 'status': 'partial'},
    {'category': 'Operations', 'score': ex.get('pmo_readiness', 46), 'status': 'partial'},
]

operations_map_live = False
weekly_briefing_live = False
ai_advisor_live = False
decision_log_entries = len(mc.get('builds', [])) if isinstance(mc.get('builds'), list) else 0
alerts_active = 0
opportunities_active = 0

readiness_scores = [c['score'] for c in READINESS_INDEX_CATEGORIES if isinstance(c['score'], (int, float))]
institutional_readiness_index = round(sum(readiness_scores) / len(readiness_scores)) if readiness_scores else 0

civic_intelligence_command_center_readiness = min(
    52,
    16 + len(DEPARTMENT_BOARDS) * 2 + len(READINESS_INDEX_CATEGORIES) // 2
    + (2 if mc2 else 0),
)

out = {
    'version': '1.0',
    'build': 65,
    'updated': today,
    'title': 'Arkansas Civic Intelligence Command Center v1.0',
    'subtitle': 'The Executive Mission Control — Operating an Educational Institution in Real Time',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/civic-intelligence-command-center.html',
    'constitution': '/docs/MASTER_CIVIC_INTELLIGENCE_COMMAND_CENTER.md',
    'legacy_executive_route': '/mission-control/executive.html',
    'purpose': (
        'Unify all institutional components into one executive command center — '
        'answer "How healthy is Citizens United Facts today?" in less than five seconds.'
    ),
    'governing_principle': (
        'Leadership never has to guess. Every decision informed by evidence. '
        'Mission Control is the executive nervous system of the institution.'
    ),
    'operational_brain': True,
    'five_second_health_check': True,
    'executive_philosophy': {
        'audience': 'Institutional leadership — not engineers',
        'questions': [
            'Are we accomplishing our mission?',
            'Where are we strongest?',
            'Where are we weakest?',
            'Who needs help?',
            'What should we build next?',
            'How close are we to statewide coverage?',
        ],
    },
    'executive_dashboard': {
        'title': 'Executive Dashboard',
        'no_drilling_required': True,
        'metrics': EXECUTIVE_DASHBOARD,
        'status': 'partial',
    },
    'executive_kpi_cards': {
        'title': 'Executive KPI Cards',
        'always_visible': True,
        'link_to_detail': True,
        'cards': EXECUTIVE_KPI_CARDS,
        'status': 'partial',
    },
    'arkansas_operations_map': {
        'title': 'Arkansas Operations Map',
        'fullscreen': True,
        'layers': [
            '75 Counties', '250 Largest Cities', 'Neighborhood Networks',
            'Education Leaders', 'Coalition Partners', 'Upcoming Events',
            'Community Conversations', 'Educational Coverage Score',
        ],
        'health_color_coding': True,
        'route': '/mission-control/civic-atlas.html',
        'status': 'planned',
        'live': operations_map_live,
    },
    'department_operations_boards': {
        'title': 'Department Operations Boards',
        'departments': DEPARTMENT_BOARDS,
        'board_fields': BOARD_FIELDS,
        'status': 'partial',
    },
    'institutional_pulse': {
        'title': 'Institutional Pulse',
        'signals': INSTITUTIONAL_PULSE,
        'measurable_heartbeat': True,
        'status': 'planned',
    },
    'arkansas_growth_dashboard': {
        'title': 'Arkansas Growth Dashboard',
        'flagship': True,
        'metrics': GROWTH_DASHBOARD,
        'route': '/mission-control/arkansas-action-network.html',
        'status': 'partial',
    },
    'executive_alerts': {
        'title': 'Executive Alerts',
        'proactive': True,
        'priority_by_urgency': True,
        'alert_types': EXECUTIVE_ALERTS,
        'active_alerts': alerts_active,
        'status': 'planned',
    },
    'opportunity_engine': {
        'title': 'Opportunity Engine',
        'proactive': True,
        'opportunity_types': OPPORTUNITY_ENGINE,
        'active_opportunities': opportunities_active,
        'status': 'planned',
    },
    'weekly_executive_briefing': {
        'title': 'Weekly Executive Briefing',
        'auto_generated': True,
        'sections': [
            'Institutional summary', 'Major accomplishments', 'Research completed',
            'Leadership growth', 'Coalition updates', 'County highlights',
            'Technology status', 'Open risks', 'Recommendations',
        ],
        'status': 'planned',
        'live': weekly_briefing_live,
    },
    'annual_state_of_civic_education': {
        'title': 'Annual State of Civic Education Report',
        'signature_publication': True,
        'sections': [
            'Institutional Growth', 'Research Progress', 'Educational Reach',
            'County Development', 'Coalition Expansion', 'Leadership Pipeline',
            'Community Conversations', 'Platform Improvements', 'Future Priorities',
        ],
        'status': 'planned',
    },
    'ai_executive_advisor': {
        'title': 'AI Executive Advisor',
        'future': True,
        'example_questions': [
            'What are our three largest risks?',
            'Which counties need immediate attention?',
            'Show me where coalition growth has slowed.',
            'What educational topics are most requested?',
        ],
        'data_source': 'Verified Mission Control data only',
        'route': '/mission-control/institutional-ai.html',
        'status': 'planned',
        'live': ai_advisor_live,
    },
    'executive_decision_log': {
        'title': 'Executive Decision Log',
        'preserves': [
            'Strategic priorities', 'Major partnerships', 'Curriculum revisions',
            'Technology changes', 'Research standards', 'Launch milestones',
        ],
        'entries_from_builds': decision_log_entries,
        'status': 'partial',
    },
    'institutional_readiness_index': {
        'title': 'Institutional Readiness Index',
        'overall_score': institutional_readiness_index,
        'categories': READINESS_INDEX_CATEGORIES,
        'measures': 'Institutional maturity — not website completion',
        'status': 'partial',
    },
    'integration': {
        'unifies': 'All 65 builds into one executive nervous system',
        'extends': 'Mission Control 2.0 (#25) executive command center',
        'systems': [
            {'system': 'MC 2.0 Executive (#25)', 'route': '/mission-control/executive.html', 'status': 'live'},
            {'system': 'Arkansas Action Network (#64)', 'route': '/mission-control/arkansas-action-network.html', 'status': 'live'},
            {'system': 'Civic Atlas (#58)', 'route': '/mission-control/civic-atlas.html', 'status': 'live'},
            {'system': 'Institutional AI (#60)', 'route': '/mission-control/institutional-ai.html', 'status': 'partial'},
            {'system': 'PMO (#54)', 'route': '/mission-control/pmo.html', 'status': 'live'},
            {'system': 'Mission Control Home', 'route': '/mission-control/', 'status': 'live'},
        ],
    },
    'long_term_vision': (
        'Ten years after launch: Arkansas as a living educational network. '
        'Mission Control guides — not merely reports — comprehensive civic education statewide.'
    ),
    'summary': {
        'departments_total': len(DEPARTMENT_BOARDS),
        'kpi_cards_total': len(EXECUTIVE_KPI_CARDS),
        'readiness_categories': len(READINESS_INDEX_CATEGORIES),
        'institutional_readiness_index': institutional_readiness_index,
        'institutional_health_score': ex.get('institutional_maturity_pct', 51),
        'launch_readiness_pct': ex.get('public_launch_readiness', 8),
        'operations_map_live': operations_map_live,
        'weekly_briefing_live': weekly_briefing_live,
        'alerts_active': alerts_active,
        'opportunities_active': opportunities_active,
        'education_leaders': education_leaders,
        'connected_arkansans': aan_sum.get('connected_arkansans', 0),
        'connected_target': PARTICIPANTS_TARGET,
        'civic_intelligence_command_center_readiness_pct': civic_intelligence_command_center_readiness,
        'mc2_readiness_pct': ex.get('mc2_readiness', 33),
        'public_launch_readiness_pct': ex.get('public_launch_readiness', 8),
    },
    'catalog_gaps': [
        'Executive dashboard partial — KPIs from registries, not unified live feed',
        'Arkansas Operations Map not live — Civic Atlas map planned, 0 counties active',
        'Department boards specified — no per-department blocker/risk tracking wired',
        'Institutional Pulse signals mostly planned — no automated heartbeat',
        'Executive Alerts engine not built — 0 active alerts',
        'Opportunity Engine not built — 0 active opportunities',
        'Weekly Executive Briefing not auto-generated',
        'Annual State of Civic Education Report not implemented',
        'AI Executive Advisor future — Institutional AI has no MC integration',
        'Build #65 Command Center vs Build #25 MC 2.0 Executive — extend, not replace?',
        'Accessibility readiness score 0 — not audited',
        '5-second health check aspirational — requires unified data pipeline',
        '0 Education Leaders · 0/200K — growth dashboard shows zeros honestly',
    ],
    'recommended_next_build': {
        'number': 66,
        'title': 'Implementation Translation Layer & Engineering Artifacts',
        'note': (
            'Unified MC data pipeline, operations map component, alert/opportunity engines, '
            'weekly briefing generator, readiness index automation, route inventory, GitHub backlog.'
        ),
    },
}

with open(root / 'data/civic-intelligence-command-center.json', 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')

print(
    f'Civic Intelligence Command Center: {len(DEPARTMENT_BOARDS)} departments, '
    f'readiness index {institutional_readiness_index}, '
    f'{civic_intelligence_command_center_readiness}% command center readiness'
)
