"""
Generate data/arkansas-community-listening.json — Build #71.
Master Arkansas Community Intelligence & Listening System v1.0.
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
cla = load_json(root / 'data/citizen-leadership-academy.json')
cn = load_json(root / 'data/coalition-network.json')

ex = mc.get('executive', {})

# Honest zeros
questions_received = 0
education_leader_reports = 0
coalition_feedback_items = 0
conversation_analyses = 0
research_recommendations = 0
public_feedback_submissions = 0
pulse_reports_generated = 0
listening_sessions_hosted = 0
workflow_items_closed = 0
question_observatory_live = False
listening_dashboard_live = False

LISTENING_SOURCES = [
    {
        'id': 'ACL-S1',
        'number': 1,
        'title': 'Individual Learners',
        'channels': ['Website', 'AI Guide', 'Community conversations', 'Academy', 'Educational events'],
        'mc_identifies_recurring': True,
        'submissions': 0,
        'status': 'planned',
    },
    {
        'id': 'ACL-S2',
        'number': 2,
        'title': 'Education Leaders',
        'reports': [
            'Questions people ask', 'Areas of confusion', 'Successful teaching approaches',
            'Resource requests', 'New educational needs',
        ],
        'role': "Institution's eyes and ears throughout Arkansas",
        'reports_submitted': education_leader_reports,
        'leaders_reporting': 0,
        'status': 'planned',
    },
    {
        'id': 'ACL-S3',
        'number': 3,
        'title': 'Coalition Organizations',
        'feedback_areas': [
            'Community interests', 'Educational challenges', 'Resource needs',
            'Event opportunities', 'Research requests',
        ],
        'items_received': coalition_feedback_items,
        'status': 'planned',
    },
    {
        'id': 'ACL-S4',
        'number': 4,
        'title': 'Community Conversations',
        'outputs': [
            'Questions asked', 'Topics discussed', 'Frequently misunderstood concepts',
            'Recommended improvements', 'Future discussion topics',
        ],
        'privacy_respecting': True,
        'analyses_completed': conversation_analyses,
        'status': 'planned',
    },
    {
        'id': 'ACL-S5',
        'number': 5,
        'title': 'Research Community',
        'suggestions': [
            'New studies', 'Updated sources', 'Emerging legal developments',
            'Historical materials', 'Data improvements',
        ],
        'recommendations_received': research_recommendations,
        'status': 'planned',
    },
    {
        'id': 'ACL-S6',
        'number': 6,
        'title': 'Public Feedback',
        'submission_types': [
            'Corrections', 'Questions', 'Suggestions',
            'Additional sources', 'Requests for clarification',
        ],
        'structured_review': True,
        'submissions': public_feedback_submissions,
        'status': 'planned',
    },
]

QUESTION_OBSERVATORY_CATEGORIES = [
    {'id': 'ACL-Q1', 'category': 'Most Frequently Asked Questions', 'count': 0, 'status': 'planned'},
    {'id': 'ACL-Q2', 'category': 'Most Difficult Questions', 'count': 0, 'status': 'planned'},
    {'id': 'ACL-Q3', 'category': 'Emerging Questions', 'count': 0, 'status': 'planned'},
    {'id': 'ACL-Q4', 'category': 'Unanswered Questions', 'count': 0, 'status': 'planned'},
    {'id': 'ACL-Q5', 'category': 'Recently Answered Questions', 'count': 0, 'status': 'planned'},
    {'id': 'ACL-Q6', 'category': 'Questions Requiring Additional Research', 'count': 0, 'status': 'planned'},
]

EDUCATIONAL_NEEDS_PATTERNS = [
    'Counties requesting presentations',
    'Cities asking similar questions',
    'Topics receiving increased attention',
    'Curriculum areas needing expansion',
    'Research gaps',
]

LISTENING_DASHBOARD_INDICATORS = [
    {'id': 'ACL-D1', 'indicator': 'Questions received', 'current': questions_received, 'status': 'planned'},
    {'id': 'ACL-D2', 'indicator': 'Topics trending', 'current': 0, 'status': 'planned'},
    {'id': 'ACL-D3', 'indicator': 'Educational requests', 'current': 0, 'status': 'planned'},
    {'id': 'ACL-D4', 'indicator': 'Resource requests', 'current': 0, 'status': 'planned'},
    {'id': 'ACL-D5', 'indicator': 'Presentation requests', 'current': 0, 'status': 'planned'},
    {'id': 'ACL-D6', 'indicator': 'Community feedback', 'current': public_feedback_submissions, 'status': 'planned'},
    {'id': 'ACL-D7', 'indicator': 'Research recommendations', 'current': research_recommendations, 'status': 'planned'},
    {'id': 'ACL-D8', 'indicator': 'Coalition observations', 'current': coalition_feedback_items, 'status': 'planned'},
]

LISTENING_WORKFLOW = [
    {'step': 1, 'id': 'received', 'title': 'Question Received', 'items': questions_received, 'status': 'planned'},
    {'step': 2, 'id': 'categorized', 'title': 'Categorized', 'items': 0, 'status': 'planned'},
    {'step': 3, 'id': 'reviewed', 'title': 'Reviewed', 'items': 0, 'status': 'planned'},
    {'step': 4, 'id': 'research_assigned', 'title': 'Research Assigned', 'items': 0, 'status': 'planned'},
    {'step': 5, 'id': 'content_updated', 'title': 'Educational Content Updated', 'items': 0, 'status': 'planned'},
    {'step': 6, 'id': 'closed', 'title': 'Mission Control Closed', 'items': workflow_items_closed, 'status': 'planned'},
]

PULSE_REPORT_TYPES = [
    {'id': 'ACL-P1', 'type': 'Monthly', 'reports_generated': 0, 'status': 'planned'},
    {'id': 'ACL-P2', 'type': 'Quarterly', 'reports_generated': 0, 'status': 'planned'},
    {'id': 'ACL-P3', 'type': 'Annual', 'reports_generated': 0, 'status': 'planned'},
]

PULSE_REPORT_CONTENT = [
    'Questions', 'Needs', 'Educational trends',
    'Research priorities', 'Community observations',
]

LISTENING_TOUR_TOPICS = [
    'What remains confusing?',
    'What resources are missing?',
    'What would help your community?',
    'How can the institution better serve Arkansas?',
]

SYSTEM_CONNECTIONS = [
    {'system': 'Mission Control', 'route': '/mission-control/', 'status': 'live'},
    {'system': 'Research Observatory (#29)', 'route': '/mission-control/research-observatory.html', 'status': 'live'},
    {'system': 'Evidence Ledger (#41)', 'route': '/mission-control/evidence-ledger.html', 'status': 'live'},
    {'system': 'Master Curriculum (#35)', 'route': '/mission-control/curriculum.html', 'status': 'live'},
    {'system': 'Community Education Academy (#28)', 'route': '/mission-control/education-academy.html', 'status': 'partial'},
    {'system': 'Coalition Network (#61)', 'route': '/mission-control/coalition-network.html', 'status': 'live'},
    {'system': 'Citizen Action Center (#62)', 'route': '/mission-control/citizen-action-center.html', 'status': 'live'},
    {'system': 'Arkansas Civic Atlas (#58)', 'route': '/mission-control/civic-atlas.html', 'status': 'live'},
    {'system': 'Citizen Leadership Academy (#68)', 'route': '/mission-control/citizen-leadership-academy.html', 'status': 'live', 'note': 'Leader reporting'},
    {'system': 'Arkansas Command Strategy (#70)', 'route': '/mission-control/arkansas-command-strategy.html', 'status': 'live'},
]

arkansas_community_listening_readiness = min(
    41,
    11 + len(LISTENING_SOURCES) * 3 + len(LISTENING_WORKFLOW) * 2 + 3,
)

out = {
    'version': '1.0',
    'build': 71,
    'updated': today,
    'title': 'Master Arkansas Community Intelligence & Listening System v1.0',
    'subtitle': 'Listening Before Leading — The Statewide Civic Listening Network',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/arkansas-community-listening.html',
    'constitution': '/docs/MASTER_ARKANSAS_COMMUNITY_LISTENING.md',
    'purpose': (
        'Collect questions, misunderstandings, educational needs, and suggestions from '
        'Arkansans — and use that information to improve the institution.'
    ),
    'governing_principle': (
        'Never become an institution that only speaks. Listen just as carefully as you teach. '
        'Curiosity begins with questions. Questions begin with listening.'
    ),
    'operating_principle': 'We do not begin with answers. We begin by listening.',
    'listening_as_important_as_publishing': True,
    'learn_from_arkansas': True,
    'listening_sources': {
        'title': 'The Arkansas Listening Network',
        'sources_total': len(LISTENING_SOURCES),
        'sources': LISTENING_SOURCES,
    },
    'question_observatory': {
        'title': 'The Question Observatory',
        'living_inventory': True,
        'live': question_observatory_live,
        'categories': QUESTION_OBSERVATORY_CATEGORIES,
        'total_questions': questions_received,
        'questions_become_content': True,
        'status': 'planned',
    },
    'educational_needs_mapping': {
        'title': 'Educational Needs Mapping',
        'patterns': EDUCATIONAL_NEEDS_PATTERNS,
        'prioritizes_resources': True,
        'status': 'planned',
    },
    'community_listening_dashboard': {
        'title': 'Community Listening Dashboard',
        'live': listening_dashboard_live,
        'indicators': LISTENING_DASHBOARD_INDICATORS,
        'status': 'planned',
    },
    'listening_to_action_workflow': {
        'title': 'Listening-to-Action Workflow',
        'principle': 'Nothing disappears into a black hole',
        'steps': LISTENING_WORKFLOW,
        'status': 'planned',
    },
    'community_pulse_reports': {
        'title': 'Community Pulse Reports',
        'report_types': PULSE_REPORT_TYPES,
        'content_areas': PULSE_REPORT_CONTENT,
        'reports_generated': pulse_reports_generated,
        'guides_planning': True,
        'status': 'planned',
    },
    'arkansas_civic_listening_tour': {
        'title': 'The Arkansas Civic Listening Tour',
        'purpose': 'Not to lecture — to learn',
        'hosted_by': 'Education Leaders',
        'sessions_hosted': listening_sessions_hosted,
        'topics': LISTENING_TOUR_TOPICS,
        'strengthens_trust': True,
        'status': 'planned',
    },
    'integration': {
        'chain': (
            'Mission Control → Research Observatory → Evidence Ledger → Curriculum → '
            'Education Academy → Coalition Network → Citizen Action Center → Civic Atlas'
        ),
        'systems': SYSTEM_CONNECTIONS,
        'improves_every_system': True,
    },
    'long_term_vision': (
        'Mission Control displays Arkansas\'s questions — what citizens want to understand, '
        'where confusion remains, which counties need resources. Institution evolves through listening.'
    ),
    'summary': {
        'listening_sources': len(LISTENING_SOURCES),
        'questions_received': questions_received,
        'education_leader_reports': education_leader_reports,
        'coalition_feedback_items': coalition_feedback_items,
        'conversation_analyses': conversation_analyses,
        'research_recommendations': research_recommendations,
        'public_feedback_submissions': public_feedback_submissions,
        'pulse_reports_generated': pulse_reports_generated,
        'listening_sessions_hosted': listening_sessions_hosted,
        'workflow_items_closed': workflow_items_closed,
        'question_observatory_live': question_observatory_live,
        'listening_dashboard_live': listening_dashboard_live,
        'education_leaders_available': cla.get('summary', {}).get('education_leaders', 0),
        'coalition_orgs': cn.get('summary', {}).get('coalition_organizations', 0),
        'arkansas_community_listening_readiness_pct': arkansas_community_listening_readiness,
        'research_observatory_readiness_pct': ex.get('observatory_readiness', 20),
        'public_launch_readiness_pct': ex.get('public_launch_readiness', 8),
    },
    'catalog_gaps': [
        '0 questions received — no feedback intake forms wired',
        '0 education leader reports — leader reporting tool not built',
        '0 coalition feedback items — organizational listening workflow missing',
        '0 community conversation analyses — post-conversation capture not implemented',
        '0 public feedback submissions — structured review queue not built',
        'Question Observatory specified — not live; 0 questions in inventory',
        'Listening-to-action workflow specified — 0 items in pipeline',
        '0 pulse reports generated — monthly/quarterly/annual generator not built',
        '0 listening tour sessions — session registration and notes not implemented',
        'Educational needs mapping planned — no pattern detection engine',
        'Build #71 vs Research Observatory (#29) — reconcile listening vs research roles?',
        'Build #71 vs Citizen Action Center (#62) — unify feedback channels?',
        f'0/{cla.get("summary", {}).get("education_leaders", 0)} leaders to report — no leaders enrolled',
        'Privacy model for conversation analysis not specified in UI',
    ],
    'recommended_next_build': {
        'number': 72,
        'title': 'Implementation Translation Layer & Engineering Artifacts',
        'note': (
            'Feedback forms, question observatory UI, listening workflow tracker, pulse report '
            'generator, leader reporting tools, needs mapping, COMP-* specs, GitHub backlog.'
        ),
    },
}

with open(root / 'data/arkansas-community-listening.json', 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')

print(
    f'Arkansas Community Listening: {questions_received} questions, '
    f'{education_leader_reports} leader reports, {pulse_reports_generated} pulse reports, '
    f'{arkansas_community_listening_readiness}% readiness'
)
