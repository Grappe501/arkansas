"""
Generate data/ai-institution.json — Build #91.
Master AI Institution — Every Volunteer Has an AI Partner v1.0.
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
iom = load_json(root / 'data/institutional-operating-manual.json')
ia60 = load_json(root / 'data/institutional-ai.json')

ex = mc.get('executive', {})

# Honest operational metrics
ai_dashboard_live = False
personal_workbench_live = False
ai_specialists_deployed = 0
volunteers_with_ai_partner = 0
ai_usage_sessions = 0
questions_answered = 0
documents_generated = 0
research_assisted = 0
time_saved_hours = 0
knowledge_gaps_identified = 0

INSTITUTIONAL_PHILOSOPHY = [
    {'layer': 1, 'name': 'Human Judgment', 'role': 'Responsible for important decisions'},
    {'layer': 2, 'name': 'AI Assistance', 'role': 'Accelerates research, organization, writing, planning, education'},
    {'layer': 3, 'name': 'Mission Control Oversight', 'role': 'Ensures accountability'},
]

AI_SPECIALISTS = [
    {'id': 'AI-01', 'name': 'Research AI', 'domain': 'Research', 'deployed': False, 'status': 'planned'},
    {'id': 'AI-02', 'name': 'Editorial AI', 'domain': 'Editorial', 'deployed': False, 'status': 'planned'},
    {'id': 'AI-03', 'name': 'Legal Research AI', 'domain': 'Legal', 'deployed': False, 'status': 'planned'},
    {'id': 'AI-04', 'name': 'Constitutional AI', 'domain': 'Constitutional', 'deployed': False, 'status': 'planned'},
    {'id': 'AI-05', 'name': 'Campaign Finance AI', 'domain': 'Campaign Finance', 'deployed': False, 'status': 'planned'},
    {'id': 'AI-06', 'name': 'Volunteer AI', 'domain': 'Volunteers', 'deployed': False, 'status': 'planned'},
    {'id': 'AI-07', 'name': 'County Operations AI', 'domain': 'County', 'deployed': False, 'status': 'planned'},
    {'id': 'AI-08', 'name': 'City Operations AI', 'domain': 'City', 'deployed': False, 'status': 'planned'},
    {'id': 'AI-09', 'name': 'Neighborhood Operations AI', 'domain': 'Neighborhood', 'deployed': False, 'status': 'planned'},
    {'id': 'AI-10', 'name': 'Coalition AI', 'domain': 'Coalition', 'deployed': False, 'status': 'planned'},
    {'id': 'AI-11', 'name': 'Mission Control AI', 'domain': 'Mission Control', 'deployed': False, 'status': 'planned'},
    {'id': 'AI-12', 'name': 'Communications AI', 'domain': 'Communications', 'deployed': False, 'status': 'planned'},
    {'id': 'AI-13', 'name': 'Social Media AI', 'domain': 'Social Media', 'deployed': False, 'status': 'planned'},
    {'id': 'AI-14', 'name': 'Curriculum AI', 'domain': 'Curriculum', 'deployed': False, 'status': 'planned'},
    {'id': 'AI-15', 'name': 'Presentation AI', 'domain': 'Presentations', 'deployed': False, 'status': 'planned'},
    {'id': 'AI-16', 'name': 'Grant Writing AI', 'domain': 'Grants', 'deployed': False, 'status': 'planned'},
    {'id': 'AI-17', 'name': 'Fundraising Support AI', 'domain': 'Fundraising', 'deployed': False, 'status': 'planned'},
    {'id': 'AI-18', 'name': 'Technology AI', 'domain': 'Technology', 'deployed': False, 'status': 'planned'},
    {'id': 'AI-19', 'name': 'Data Analysis AI', 'domain': 'Data', 'deployed': False, 'status': 'planned'},
    {'id': 'AI-20', 'name': 'Relationship AI', 'domain': 'Relationships', 'deployed': False, 'status': 'planned'},
    {'id': 'AI-21', 'name': 'Education Leader AI', 'domain': 'Education Leaders', 'deployed': False, 'status': 'planned'},
]

PERSONAL_WORKBENCH_FIELDS = [
    'Assigned projects', 'Department', 'Role', 'Current tasks',
    'Relevant documentation', 'Training completed', 'Institutional standards',
]

KNOWLEDGE_SOURCES = [
    {'source': 'Institution Constitution', 'route': '/mission-control/organizational-constitution.html', 'grounded': True},
    {'source': 'Research Library', 'route': '/mission-control/research-library.html', 'grounded': True},
    {'source': 'Evidence Ledger', 'route': '/mission-control/evidence-ledger.html', 'grounded': True},
    {'source': 'Claims Registry', 'route': '/data/facts-registry.json', 'grounded': 'partial'},
    {'source': 'Knowledge Graph', 'route': '/mission-control/knowledge-graph.html', 'grounded': 'partial'},
    {'source': 'Operating Manual', 'route': '/mission-control/institutional-operating-manual.html', 'grounded': True},
    {'source': 'Mission Control', 'route': '/mission-control/', 'grounded': True},
    {'source': 'Editorial Standards', 'route': '/mission-control/trust.html', 'grounded': 'partial'},
    {'source': 'Volunteer Handbook', 'route': '/mission-control/volunteer-funding-constitution.html', 'grounded': 'partial'},
    {'source': 'Governance documents', 'route': '/mission-control/governance.html', 'grounded': True},
]

AI_SAFETY_RULES = [
    'Identify uncertainty',
    'Cite institutional sources whenever possible',
    'Distinguish facts from recommendations',
    'Respect volunteer privacy',
    'Protect confidential information',
    'Avoid inventing facts',
    'Escalate important decisions to human leadership',
    'Trust remains paramount',
]

AI_COLLABORATION = [
    'What should I work on today?',
    'What county needs help?',
    'Summarize this research',
    'Draft a presentation',
    'Prepare discussion questions',
    'Compare these sources',
    'Help organize tonight\'s meeting',
]

EDUCATION_LEADER_AI = [
    'Lesson planning',
    'Presentation preparation',
    'Community discussion questions',
    'Follow-up emails',
    'Frequently asked questions',
    'Local resource recommendations',
]

COUNTY_AI_CAPABILITIES = [
    'Track progress',
    'Organize volunteers',
    'Schedule conversations',
    'Coordinate coalition partners',
    'Monitor county goals',
    'Generate reports',
]

MC_AI_IDENTIFIES = [
    'Projects falling behind',
    'Volunteer overload',
    'Research gaps',
    'Community trends',
    'Growth opportunities',
    'Technology risks',
]

AI_LEARNING_TRACKS = [
    'Frequently asked questions',
    'Research requests',
    'Volunteer needs',
    'Documentation gaps',
    'Training improvements',
]

AI_DASHBOARD_INDICATORS = [
    {'id': 'AI-D01', 'indicator': 'AI usage', 'current': ai_usage_sessions, 'status': 'planned'},
    {'id': 'AI-D02', 'indicator': 'Volunteer productivity', 'current': 0, 'unit': '%', 'status': 'planned'},
    {'id': 'AI-D03', 'indicator': 'Questions answered', 'current': questions_answered, 'status': 'planned'},
    {'id': 'AI-D04', 'indicator': 'Documents generated', 'current': documents_generated, 'status': 'planned'},
    {'id': 'AI-D05', 'indicator': 'Research assisted', 'current': research_assisted, 'status': 'planned'},
    {'id': 'AI-D06', 'indicator': 'Time saved (hours)', 'current': time_saved_hours, 'status': 'planned'},
    {'id': 'AI-D07', 'indicator': 'Knowledge gaps identified', 'current': knowledge_gaps_identified, 'status': 'planned'},
    {'id': 'AI-D08', 'indicator': 'AI confidence levels', 'current': 'not tracked', 'status': 'planned'},
]

ai_institution_readiness = min(
    64,
    14
    + len(AI_SPECIALISTS) // 2
    + len(KNOWLEDGE_SOURCES) // 2
    + len(AI_SAFETY_RULES) // 2
    + len(PERSONAL_WORKBENCH_FIELDS) // 2
    + len(AI_COLLABORATION) // 2
    + len(EDUCATION_LEADER_AI) // 2
    + len(COUNTY_AI_CAPABILITIES) // 2
    + len(MC_AI_IDENTIFIES) // 2
    + len(AI_LEARNING_TRACKS) // 2
    + len(AI_DASHBOARD_INDICATORS) // 2
    + len(INSTITUTIONAL_PHILOSOPHY)
    + (2 if ai_dashboard_live else 0),
)

out = {
    'version': '1.0',
    'build': 91,
    'updated': today,
    'completion_target_date': completion_target_date,
    'title': 'Master AI Institution v1.0',
    'subtitle': 'Every Volunteer Has an AI Partner',
    'tagline': 'AI Amplifies Volunteers',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/ai-institution.html',
    'constitution': '/docs/MASTER_AI_INSTITUTION.md',
    'purpose': (
        'Embed artificial intelligence throughout every department to multiply volunteer '
        'effectiveness. AI does not replace volunteers — AI amplifies volunteers. Every '
        'volunteer should feel like they have a knowledgeable assistant. Mission Control '
        'monitors human and AI capacity together.'
    ),
    'governing_principle': (
        'Artificial intelligence should never replace the heart of Citizens United Facts. '
        'It should strengthen it. Every AI should make volunteers more informed. Every '
        'volunteer should make communities stronger. Every stronger community should '
        'strengthen Arkansas.'
    ),
    'founders_principle': (
        'The purpose of AI is not automation for its own sake. The purpose is to free '
        'volunteers to do the work only people can do: build trust, listen, teach, mentor, '
        'encourage, lead. Technology handles information. People build relationships.'
    ),
    'institutional_philosophy': {
        'title': 'Institutional Philosophy',
        'layers': INSTITUTIONAL_PHILOSOPHY,
        'ai_does_not_replace_volunteers': True,
        'ai_amplifies_volunteers': True,
        'mc_monitors_human_and_ai_capacity': True,
    },
    'institutional_ai_team': {
        'title': 'Institutional AI Team',
        'specialists': AI_SPECIALISTS,
        'specialists_total': len(AI_SPECIALISTS),
        'specialists_deployed': ai_specialists_deployed,
        'specialized_partners_not_one_assistant': True,
        'status': 'planned',
    },
    'personal_ai_workbench': {
        'title': 'Personal AI Workbench',
        'fields': PERSONAL_WORKBENCH_FIELDS,
        'live': personal_workbench_live,
        'every_volunteer_receives_workspace': True,
        'daily_working_partner': True,
        'status': 'planned',
    },
    'ai_knowledge_sources': {
        'title': 'AI Knowledge Sources',
        'sources': KNOWLEDGE_SOURCES,
        'sources_total': len(KNOWLEDGE_SOURCES),
        'grounded_in_institutional_knowledge': True,
        'not_random_internet_opinions': True,
        'status': 'partial',
    },
    'ai_safety_rules': {
        'title': 'AI Safety Rules',
        'rules': AI_SAFETY_RULES,
        'trust_remains_paramount': True,
        'status': 'specified',
    },
    'ai_collaboration': {
        'title': 'AI Collaboration',
        'example_prompts': AI_COLLABORATION,
        'reduces_administrative_workload': True,
        'volunteers_focus_on_people': True,
        'status': 'specified',
    },
    'ai_for_education_leaders': {
        'title': 'AI for Education Leaders',
        'assistance_areas': EDUCATION_LEADER_AI,
        'every_education_leader_gains_support': True,
        'status': 'planned',
    },
    'ai_for_county_teams': {
        'title': 'AI for County Teams',
        'capabilities': COUNTY_AI_CAPABILITIES,
        'county_leadership_easier': True,
        'status': 'planned',
    },
    'ai_for_mission_control': {
        'title': 'AI for Mission Control',
        'identifies': MC_AI_IDENTIFIES,
        'proactive_recommendations': True,
        'status': 'planned',
    },
    'ai_learning_system': {
        'title': 'AI Learning System',
        'tracks': AI_LEARNING_TRACKS,
        'every_interaction_improves_institution': True,
        'institution_continuously_smarter': True,
        'status': 'planned',
    },
    'ai_dashboard': {
        'title': 'AI Dashboard',
        'indicators': AI_DASHBOARD_INDICATORS,
        'live': ai_dashboard_live,
        'ai_becomes_measurable': True,
        'status': 'planned',
    },
    'integration': {
        'chain': (
            'Mission Control → Knowledge Graph → Research Institute → Community Education '
            'Academy → Operating Manual → Relationship OS → County OS → Coalition Network'
        ),
        'every_system_ai_assisted': True,
        'systems': [
            {'system': 'Institutional AI (#60)', 'route': '/mission-control/institutional-ai.html', 'status': 'live'},
            {'system': 'Operating Manual (#90)', 'route': '/mission-control/institutional-operating-manual.html', 'status': 'live'},
            {'system': 'Knowledge Graph', 'route': '/mission-control/knowledge-graph.html', 'status': 'partial'},
            {'system': 'Research Institute (#73)', 'route': '/mission-control/arkansas-research-institute.html', 'status': 'live'},
            {'system': 'Relationship OS (#59)', 'route': '/mission-control/relationship-os.html', 'status': 'live'},
            {'system': 'County OS (#77)', 'route': '/mission-control/arkansas-county-operating-system.html', 'status': 'live'},
        ],
        'extends': [
            {'build': 60, 'title': 'Institutional AI Brain', 'route': '/mission-control/institutional-ai.html'},
            {'build': 26, 'title': 'AI Knowledge Engine', 'route': '/mission-control/ai-knowledge.html'},
        ],
    },
    'long_term_vision': (
        'By January 2027, every volunteer should feel like they have an experienced teammate '
        'available at any hour. The AI remembers institutional knowledge, finds documentation '
        'instantly, suggests improvements, organizes work, answers questions, prepares materials. '
        'Not fewer volunteers — volunteers with dramatically greater capacity.'
    ),
    'summary': {
        'completion_target_date': completion_target_date,
        'days_remaining': days_remaining,
        'ai_institution_readiness_pct': ai_institution_readiness,
        'institutional_ai_v60_readiness_pct': ia60.get('summary', {}).get('institutional_ai_readiness_pct', 42),
        'operating_manual_readiness_pct': iom.get('summary', {}).get('institutional_operating_manual_readiness_pct', 60),
        'ai_specialists_deployed': ai_specialists_deployed,
        'ai_specialists_total': len(AI_SPECIALISTS),
        'volunteers_with_ai_partner': volunteers_with_ai_partner,
        'personal_workbench_live': personal_workbench_live,
        'ai_dashboard_live': ai_dashboard_live,
        'ai_usage_sessions': ai_usage_sessions,
        'questions_answered': questions_answered,
        'documents_generated': documents_generated,
        'time_saved_hours': time_saved_hours,
        'institutional_completion_pct': ex.get('overall_completion', mc.get('build', 90)),
    },
    'catalog_gaps': [
        '0/21 AI specialists deployed — blueprint only',
        'Personal AI workbench not live',
        'AI dashboard not live — usage not measurable',
        '0 volunteers with AI partner',
        'No RAG pipeline to institutional knowledge sources',
        'AI safety rules specified — not enforced in product',
        'Extends Institutional AI #60 — two AI dashboards until unified',
        'Knowledge Graph partial — AI grounding incomplete',
        'No AI learning loop — FAQ/volunteer needs not tracked',
        'MC AI proactive recommendations not operational',
        'Education Leader / County AI — no live interfaces',
    ],
    'recommended_next_build': {
        'number': 92,
        'title': 'Executive War Room & Countdown Dashboard Components',
        'note': (
            'War room UI, live countdown, AI dashboard components, workbench MVP, '
            'RAG grounding pipeline, COMP-* specs.'
        ),
    },
}

with open(root / 'data/ai-institution.json', 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')

print(
    f'AI Institution: {ai_specialists_deployed}/{len(AI_SPECIALISTS)} specialists, '
    f'{volunteers_with_ai_partner} volunteers, {ai_institution_readiness}% readiness'
)
