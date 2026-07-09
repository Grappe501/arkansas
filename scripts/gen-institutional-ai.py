"""
Generate data/institutional-ai.json — Build #60.
Institutional AI Brain & Knowledge Assistant — Arkansas Civic Intelligence System v1.0.
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
ai26 = load_json(root / 'data/ai-knowledge-engine.json')
claims = load_json(root / 'data/claims-ledger.json')
evidence = load_json(root / 'data/evidence-registry.json')
kg = load_json(root / 'data/kg-registry.json')
content = load_json(root / 'data/content-inventory.json')

ex = mc.get('executive', {})
claims_count = len(claims.get('claims', []))
evidence_count = len(evidence.get('entries', evidence.get('evidence', [])))
if isinstance(evidence.get('summary'), dict):
    evidence_count = evidence.get('summary', {}).get('total', evidence_count)
kg_nodes = kg.get('summary', {}).get('total_nodes', 38)
published = content.get('summary', {}).get('published', 15)

# Honest: no AI runtime
questions_answered = 0
unanswered_questions = 0
knowledge_gaps_identified = 0
research_requests = 0

SOURCE_GROUNDING = [
    {'id': 'SRC-1', 'source': 'Evidence Ledger', 'route': '/mission-control/evidence-ledger.html', 'status': 'partial'},
    {'id': 'SRC-2', 'source': 'Claims Registry', 'route': '/data/claims-ledger.json', 'status': 'partial', 'count': claims_count},
    {'id': 'SRC-3', 'source': 'Source Library', 'route': '/mission-control/research-library.html', 'status': 'partial'},
    {'id': 'SRC-4', 'source': 'Research Library', 'route': '/mission-control/research-library.html', 'status': 'partial'},
    {'id': 'SRC-5', 'source': 'Encyclopedia', 'route': '/mission-control/encyclopedia.html', 'status': 'planned'},
    {'id': 'SRC-6', 'source': 'Curriculum', 'route': '/mission-control/curriculum.html', 'status': 'partial'},
    {'id': 'SRC-7', 'source': 'Knowledge Graph', 'route': '/data/kg-registry.json', 'status': 'partial', 'count': kg_nodes},
    {'id': 'SRC-8', 'source': 'Published educational content', 'route': '/educate/', 'status': 'partial', 'count': published},
]

SEVEN_ROLES = [
    {
        'id': 'AI-R1', 'number': 1, 'title': 'Learning Guide', 'audience': 'Visitors',
        'examples': ['What should I read first?', "I don't understand this term.", 'Explain at beginner level.', 'Show me the next lesson.'],
        'status': 'planned', 'visibility': 'public',
    },
    {
        'id': 'AI-R2', 'number': 2, 'title': 'Research Guide', 'audience': 'Researchers',
        'examples': ['Show every source on this topic.', 'Find related court cases.', 'Compare these decisions.', 'Locate supporting evidence.'],
        'status': 'planned', 'visibility': 'public',
    },
    {
        'id': 'AI-R3', 'number': 3, 'title': 'Constitutional Guide', 'audience': 'Learners',
        'examples': ['What does the First Amendment say?', 'Why did the majority rely on this precedent?', 'What did the dissent argue?'],
        'status': 'planned', 'visibility': 'public',
        'note': 'Describe legal reasoning — not legal advice',
    },
    {
        'id': 'AI-R4', 'number': 4, 'title': 'Arkansas Civic Guide', 'audience': 'Arkansans',
        'examples': ['How does a ballot initiative work in Arkansas?', 'How does a bill become law?', 'What resources are available near me?'],
        'status': 'planned', 'visibility': 'public',
    },
    {
        'id': 'AI-R5', 'number': 5, 'title': 'Education Leader Assistant', 'audience': 'Volunteers',
        'examples': ['Recommend presentations.', 'Suggest discussion questions.', 'Build reading lists.', 'Prepare workshop packets.', 'Locate printable resources.'],
        'status': 'planned', 'visibility': 'authenticated',
        'note': 'Assists educators — does not replace judgment',
    },
    {
        'id': 'AI-R6', 'number': 6, 'title': 'Coalition Assistant', 'audience': 'Organizations',
        'examples': ['Locate partnership resources.', 'Find educational toolkits.', 'Suggest Academy modules.', 'Recommend conversation materials.'],
        'status': 'planned', 'visibility': 'authenticated',
    },
    {
        'id': 'AI-R7', 'number': 7, 'title': 'Mission Control Assistant', 'audience': 'Staff',
        'examples': ['Find unfinished work.', 'Identify research gaps.', 'Suggest content needing review.', 'Highlight counties without leaders.', 'Find broken KG relationships.'],
        'status': 'planned', 'visibility': 'internal',
    },
]

CONFIDENCE_LEVELS = [
    {'id': 'high', 'level': 'High', 'definition': 'Supported directly by primary institutional sources', 'status': 'defined'},
    {'id': 'medium', 'level': 'Medium', 'definition': 'Supported through multiple institutional resources', 'status': 'defined'},
    {'id': 'needs_review', 'level': 'Needs Review', 'definition': 'Limited supporting material', 'status': 'defined'},
    {'id': 'unknown', 'level': 'Unknown', 'definition': 'No verified institutional information available', 'status': 'defined'},
]

SOURCE_PANEL_ITEMS = [
    'Supporting sources', 'Related lessons', 'Claims used', 'Court opinions',
    'Timeline events', 'Videos', 'Research summaries',
]

MEMORY_PREFERENCES = [
    'Preferred learning depth', 'Completed curriculum', 'Saved reading lists',
    'Favorite topics', 'Communication preferences',
]

SAFETY_PRINCIPLES = [
    'Encourage learning', 'Encourage source verification',
    'Distinguish facts from interpretation', 'Respect uncertainty',
    'Avoid speculation presented as fact', 'Remain transparent about knowledge limits',
]

MC_AI_METRICS = [
    {'id': 'AI-M1', 'metric': 'Questions answered', 'current': questions_answered, 'status': 'live'},
    {'id': 'AI-M2', 'metric': 'Most searched topics', 'current': 0, 'status': 'planned'},
    {'id': 'AI-M3', 'metric': 'Knowledge gaps identified', 'current': knowledge_gaps_identified, 'status': 'planned'},
    {'id': 'AI-M4', 'metric': 'Articles recommended', 'current': 0, 'status': 'planned'},
    {'id': 'AI-M5', 'metric': 'Research requests', 'current': research_requests, 'status': 'planned'},
    {'id': 'AI-M6', 'metric': 'Unanswered questions', 'current': unanswered_questions, 'status': 'live'},
    {'id': 'AI-M7', 'metric': 'Content needing expansion', 'current': 0, 'status': 'planned'},
    {'id': 'AI-M8', 'metric': 'AI-assisted learning trends', 'current': 0, 'status': 'planned'},
]

FUTURE_CAPABILITIES = [
    'Personalized learning plans', 'Adaptive curriculum recommendations',
    'Natural-language search across Research Library',
    'Interactive constitutional study sessions', 'Voice-guided learning',
    'Multilingual educational assistance',
]

INTEGRATION_STACK = [
    {'system': 'Knowledge Graph', 'route': '/mission-control/civic-intelligence.html', 'status': 'partial'},
    {'system': 'Evidence Ledger', 'route': '/mission-control/evidence-ledger.html', 'status': 'partial'},
    {'system': 'Claims Registry', 'route': '/data/claims-ledger.json', 'status': 'partial'},
    {'system': 'Research Library', 'route': '/mission-control/research-library.html', 'status': 'partial'},
    {'system': 'Encyclopedia', 'route': '/mission-control/encyclopedia.html', 'status': 'planned'},
    {'system': 'Curriculum', 'route': '/mission-control/curriculum.html', 'status': 'partial'},
    {'system': 'Community Education Academy', 'route': '/mission-control/education-academy.html', 'status': 'partial'},
    {'system': 'Mission Control', 'route': '/mission-control/', 'status': 'live'},
    {'system': 'Arkansas Civic Atlas', 'route': '/mission-control/civic-atlas.html', 'status': 'live'},
    {'system': 'AI Knowledge Engine (#26)', 'route': '/mission-control/ai-knowledge.html', 'status': 'partial'},
]

roles_defined = len(SEVEN_ROLES)
sources_partial = sum(1 for s in SOURCE_GROUNDING if s['status'] in ('live', 'partial'))
institutional_ai_readiness = min(42, 18 + roles_defined * 2 + sources_partial * 2)
ai_engine_readiness = max(ai26.get('summary', {}).get('ai_engine_readiness_pct', 14), institutional_ai_readiness - 8)

out = {
    'version': '1.0',
    'build': 60,
    'updated': today,
    'title': 'Institutional AI Brain & Knowledge Assistant v1.0',
    'subtitle': 'Arkansas Civic Intelligence System — AI That Teaches, Never Replaces Thinking',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/institutional-ai.html',
    'constitution': '/docs/MASTER_INSTITUTIONAL_AI.md',
    'purpose': (
        'Institutional intelligence layer helping Arkansans learn, discover, navigate, research, '
        'and connect — grounded in verified knowledge. Not a chatbot. Evidence is the authority.'
    ),
    'governing_principle': (
        'The AI is the librarian. The evidence is the teacher. The learner draws informed conclusions.'
    ),
    'not_a_chatbot': True,
    'evidence_is_authority': True,
    'ai_philosophy': {
        'core_question': 'Help me understand.',
        'not_designed_for': ['Persuasion', 'Debate', 'Telling people what to believe'],
        'mission': 'Lead people to evidence about history, constitutional law, campaign finance, and Arkansas civic processes',
    },
    'institutional_rule_one': {
        'title': 'Never Invent Institutional Knowledge',
        'rule': 'Every educational answer traces to verified platform sources',
        'sources': SOURCE_GROUNDING,
        'unknown_response': 'Say clearly when the platform does not know',
    },
    'seven_roles': SEVEN_ROLES,
    'persona': {
        'name': 'Arkansas Civic Librarian',
        'extends': 'AI Knowledge Engine (#26)',
        'role': 'Guide — not authority',
    },
    'confidence_levels': {
        'title': 'Internal Confidence Classification',
        'levels': CONFIDENCE_LEVELS,
        'never_disguise_uncertainty': True,
    },
    'source_panel': {
        'title': 'Evidence Exploration Panel',
        'items': SOURCE_PANEL_ITEMS,
        'principle': 'Always invite users to examine underlying evidence',
        'status': 'planned',
    },
    'ai_memory': {
        'title': 'User Preference Memory',
        'allowed': MEMORY_PREFERENCES,
        'prohibited': 'Assume or infer sensitive personal information',
        'user_control': True,
        'status': 'planned',
    },
    'safety_principles': SAFETY_PRINCIPLES,
    'mc_ai_dashboard': {
        'title': 'Mission Control AI Quality Monitoring',
        'metrics': MC_AI_METRICS,
        'metrics_live': sum(1 for m in MC_AI_METRICS if m['status'] == 'live'),
        'monitors_like_research': True,
        'status': 'partial',
    },
    'technical_status': {
        'chat_ui_live': ai26.get('summary', {}).get('chat_ui_live', False),
        'rag_pipeline_live': ai26.get('summary', {}).get('rag_pipeline_live', False),
        'api_provider': ai26.get('technical_requirements', {}).get('api_provider', 'undecided'),
        'embedding_store': 'planned',
        'citation_required': True,
        'human_review_for_generated': True,
    },
    'future_capabilities': FUTURE_CAPABILITIES,
    'integration': {
        'title': 'AI Navigation Layer',
        'flow': 'KG → Evidence → Claims → Library → Encyclopedia → Curriculum → Academy → MC → Civic Atlas',
        'systems': INTEGRATION_STACK,
        'principle': 'Does not replace systems — helps users navigate them',
    },
    'long_term_vision': (
        'Guide Arkansans through thoughtful evidence-based learning journeys — concepts gradually, '
        'historical context, primary sources, recommended lessons — building understanding not single answers.'
    ),
    'extends_build_26': {
        'title': 'AI Knowledge Engine',
        'route': '/data/ai-knowledge-engine.json',
        'learning_modes': ai26.get('summary', {}).get('learning_modes', 5),
        'guardrails': ai26.get('summary', {}).get('guardrails', 5),
    },
    'summary': {
        'seven_roles_defined': roles_defined,
        'source_grounding_types': len(SOURCE_GROUNDING),
        'confidence_levels': len(CONFIDENCE_LEVELS),
        'safety_principles': len(SAFETY_PRINCIPLES),
        'claims_in_registry': claims_count,
        'kg_nodes': kg_nodes,
        'published_content': published,
        'questions_answered': questions_answered,
        'unanswered_questions': unanswered_questions,
        'chat_ui_live': False,
        'rag_pipeline_live': False,
        'roles_operational': 0,
        'institutional_ai_readiness_pct': institutional_ai_readiness,
        'ai_engine_readiness_pct': ai_engine_readiness,
        'ai_knowledge_engine_v26_pct': ai26.get('summary', {}).get('ai_engine_readiness_pct', 14),
        'public_launch_readiness_pct': ex.get('public_launch_readiness', 8),
    },
    'catalog_gaps': [
        'No chat UI or public AI assistant route — architecture only',
        'No RAG pipeline or embedding store — cannot ground responses in KB',
        f'Sparse knowledge base: ~{claims_count} claims, {kg_nodes} KG nodes, {published} published articles',
        '7 roles defined — 0 operational',
        'Source panel UI not built — citation flow theoretical',
        'Mission Control Assistant (internal) not implemented',
        'Confidence classification defined — no runtime scoring',
        'AI memory/preferences schema not in Neon',
        'Build #26 AI Knowledge Engine and Build #60 Institutional AI coexist — #60 supersedes scope',
        'API provider undecided — no LLM integration',
    ],
    'recommended_next_build': {
        'number': 61,
        'title': 'Implementation Translation Layer & Engineering Artifacts',
        'note': (
            'RAG pipeline spec, Neon query logs, citation API, COMP-* Ask UI, route inventory, '
            'GitHub issue backlog for AI implementation.'
        ),
    },
}

with open(root / 'data/institutional-ai.json', 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')

print(
    f'Institutional AI: {roles_defined} roles, {questions_answered} answered, '
    f'{institutional_ai_readiness}% readiness'
)
