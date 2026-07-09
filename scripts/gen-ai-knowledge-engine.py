"""
Generate data/ai-knowledge-engine.json — Build #26 AI Knowledge & Research Engine v1.0.
"""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
today = '2026-07-09'

CORE_PRINCIPLES = [
    'Explain', 'Teach', 'Connect', 'Clarify', 'Cite', 'Encourage exploration'
]

LIBRARIAN_TRAITS = [
    'Patient', 'Curious', 'Neutral in tone', 'Evidence-focused',
    'Encouraging', 'Clear', 'Respectful'
]

LEARNING_MODES = [
    {'id': 'AI-LM-01', 'title': 'Quick Answer', 'description': 'One-minute explanation for first-time visitors', 'status': 'planned'},
    {'id': 'AI-LM-02', 'title': 'Guided Lesson', 'description': 'Step-by-step educational walkthrough', 'status': 'planned'},
    {'id': 'AI-LM-03', 'title': 'Deep Research', 'description': 'Detailed explanations with evidence links', 'status': 'planned'},
    {'id': 'AI-LM-04', 'title': 'Compare Perspectives', 'description': 'Multiple viewpoints with supporting evidence for each', 'status': 'planned'},
    {'id': 'AI-LM-05', 'title': 'Primary Source Explorer', 'description': 'Direct to original documents', 'status': 'planned'},
]

EXAMPLE_QUESTIONS = [
    {'q': 'What was Citizens United actually about?', 'category': 'case', 'fact_type': 'established_fact'},
    {'q': 'Why did the Supreme Court rule the way it did?', 'category': 'legal_analysis', 'fact_type': 'legal_analysis'},
    {'q': 'What is an independent expenditure?', 'category': 'terminology', 'fact_type': 'established_fact'},
    {'q': 'What is the difference between a PAC and a Super PAC?', 'category': 'terminology', 'fact_type': 'established_fact'},
    {'q': 'How did campaign finance law evolve before 2010?', 'category': 'history', 'fact_type': 'established_fact'},
    {'q': 'What reforms have been proposed since the decision?', 'category': 'reform', 'fact_type': 'current_proposal'},
    {'q': 'What options could Congress consider?', 'category': 'federal_policy', 'fact_type': 'current_proposal'},
    {'q': 'What options are available to Arkansas lawmakers?', 'category': 'arkansas', 'fact_type': 'current_proposal'},
    {'q': 'What is the ballot initiative process in Arkansas?', 'category': 'arkansas', 'fact_type': 'established_fact'},
]

RESPONSE_SCHEMA = [
    'plain_language_explanation', 'supporting_facts', 'relevant_cases',
    'historical_context', 'primary_source_links', 'suggested_next_lessons'
]

GUARDRAILS = [
    'Identify when summarizing versus quoting',
    'Encourage primary source consultation for important legal questions',
    'Distinguish educational explanations from policy proposals',
    'Acknowledge uncertainty when evidence is incomplete or evolving',
    'Never invent citations or factual claims',
]

def capability(cid, title, purpose, features, status, notes=None, integration=None):
    return {
        'id': cid,
        'title': title,
        'purpose': purpose,
        'feature_count': len(features),
        'features': features,
        'implementation_status': status,
        'notes': notes,
        'integration': integration,
    }

capabilities = [
    capability('AI-CAP-01', 'Core Principles', 'Educational intelligence purpose', CORE_PRINCIPLES, 'defined'),
    capability('AI-CAP-02', 'Arkansas Civic Librarian', 'AI persona and tone', LIBRARIAN_TRAITS, 'defined',
        'Persona documented; no chat interface yet'),
    capability('AI-CAP-03', 'Learning Modes', 'Visitor-selected learning depth', [m['title'] for m in LEARNING_MODES], 'planned',
        '5 modes defined; UI not built'),
    capability('AI-CAP-04', 'Example Question Bank', 'Seed questions with fact-type distinction', EXAMPLE_QUESTIONS, 'defined',
        '9 questions with fact/legal/proposal tags'),
    capability('AI-CAP-05', 'Evidence-First Responses', 'Required response structure', RESPONSE_SCHEMA, 'defined',
        'Schema defined; no response generator'),
    capability('AI-CAP-06', 'Intelligent Learning Paths', 'Activity-based recommendations', [
        'Next lessons', 'Related constitutional concepts', 'Historical background',
        'Spending data', 'Community education resources', 'Coalition opportunities'
    ], 'partial', 'Knowledge Atlas trails + KG Explore Further exist; AI routing not built',
        '/data/knowledge-atlas.json'),
    capability('AI-CAP-07', 'Research Assistant', 'Source finding and legal terminology', [
        'Find related sources', 'Explain legal terminology', 'Summarize lengthy opinions',
        'Compare historical developments', 'Organize research materials', 'Identify knowledge gaps'
    ], 'planned', 'Research framework + evidence registry scaffold only'),
    capability('AI-CAP-08', 'Educational Event Assistant', 'Help Education Leaders prepare presentations', [
        'Discussion questions', 'Handout recommendations', 'Relevant charts',
        'Presentation outlines', 'Audience-specific learning plans'
    ], 'planned', 'User review required before use — not built'),
    capability('AI-CAP-09', 'Coalition Assistant', 'Resource discovery for organizations', [
        'Locate educational resources', 'Find presentation materials',
        'Community conversation guides', 'Upcoming events', 'Coalition participation'
    ], 'planned', 'Coalition hub exists; AI layer not built'),
    capability('AI-CAP-10', 'Mission Control Intelligence', 'Admin decision support', [
        'Research areas needing updates', 'Counties with limited activity',
        'FAQs lacking coverage', 'Pages with incomplete citations', 'Resources needing revision'
    ], 'partial', 'MC2 future_intelligence layer documented; no AI integration',
        '/data/mc2-executive.json'),
]

knowledge_sources = [
    {'id': 'KS-01', 'title': 'Facts Framework', 'route': '/data/facts-registry.json', 'build': 18, 'status': 'partial', 'records': 13},
    {'id': 'KS-02', 'title': 'Evidence Registry', 'route': '/data/evidence-registry.json', 'build': 10, 'status': 'partial', 'records': 14},
    {'id': 'KS-03', 'title': 'Knowledge Graph', 'route': '/data/kg-registry.json', 'build': 11, 'status': 'partial', 'records': 38},
    {'id': 'KS-04', 'title': 'Knowledge Atlas', 'route': '/data/knowledge-atlas.json', 'build': 19, 'status': 'partial', 'records': 51},
    {'id': 'KS-05', 'title': 'Content Inventory', 'route': '/data/content-inventory.json', 'build': 6, 'status': 'partial'},
    {'id': 'KS-06', 'title': 'Research Framework', 'route': '/data/research-framework.json', 'build': 10, 'status': 'partial'},
    {'id': 'KS-07', 'title': 'Canonical Data Model', 'route': '/data/canonical-data-model.json', 'build': 15, 'status': 'schema_ready'},
]

future_vision_destinations = [
    'Relevant lessons', 'Historical timelines', 'Supreme Court opinions',
    'Research papers', 'Arkansas-specific materials', 'Coalition resources',
    'Community conversation guides'
]

by_status = {}
for c in capabilities:
    by_status[c['implementation_status']] = by_status.get(c['implementation_status'], 0) + 1
for m in LEARNING_MODES:
    by_status['learning_mode_planned'] = by_status.get('learning_mode_planned', 0) + 1

status_weights = {'live': 100, 'partial': 45, 'schema_ready': 35, 'defined': 25, 'planned': 8}
cap_readiness = round(sum(status_weights.get(c['implementation_status'], 5) for c in capabilities) / max(len(capabilities), 1))
# No chat UI, API, or RAG — cap overall at honest architecture-only score
ai_readiness = min(cap_readiness, 14)

out = {
    'version': '1.0',
    'build': 26,
    'updated': today,
    'title': 'AI Knowledge & Research Engine v1.0',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/ai-knowledge.html',
    'constitution': '/docs/AI_KNOWLEDGE_ENGINE.md',
    'purpose': 'Help people understand — not persuade. Guide toward primary sources, context, and verified evidence.',
    'persona': {
        'name': 'Arkansas Civic Librarian',
        'traits': LIBRARIAN_TRAITS,
        'role': 'Help visitors understand complex topics, not debate them',
    },
    'core_principles': CORE_PRINCIPLES,
    'learning_modes': LEARNING_MODES,
    'example_questions': EXAMPLE_QUESTIONS,
    'response_schema': RESPONSE_SCHEMA,
    'guardrails': GUARDRAILS,
    'capabilities': capabilities,
    'capability_count': len(capabilities),
    'knowledge_sources': knowledge_sources,
    'learning_path_recommendations': [
        'Next lessons', 'Related constitutional concepts', 'Historical background',
        'Spending data', 'Community education resources', 'Coalition opportunities'
    ],
    'future_vision': {
        'destinations': future_vision_destinations,
        'role': 'Doorway into platform knowledge — not a replacement for it',
    },
    'governing_principle': 'Success measured by evidence discovery and continued learning — not question volume.',
    'technical_requirements': {
        'rag_pipeline': 'planned',
        'verified_knowledge_base_only': True,
        'citation_required': True,
        'human_review_for_generated_materials': True,
        'api_provider': 'undecided',
        'chat_ui_route': 'planned',
        'embedding_store': 'planned',
    },
    'related_registries': [
        {'title': 'Knowledge Graph', 'route': '/mission-control/knowledge-graph.html', 'rule': 'AI must cite verified knowledge base'},
        {'title': 'Facts Framework', 'route': '/mission-control/facts.html'},
        {'title': 'Research Framework', 'route': '/mission-control/research.html'},
        {'title': 'Knowledge Atlas', 'route': '/mission-control/atlas.html'},
        {'title': 'MC2 Future Intelligence', 'route': '/mission-control/executive.html'},
    ],
    'summary': {
        'capabilities': len(capabilities),
        'learning_modes': len(LEARNING_MODES),
        'example_questions': len(EXAMPLE_QUESTIONS),
        'guardrails': len(GUARDRAILS),
        'knowledge_sources': len(knowledge_sources),
        'response_schema_fields': len(RESPONSE_SCHEMA),
        'by_status': by_status,
        'implementation_defined': by_status.get('defined', 0),
        'implementation_partial': by_status.get('partial', 0) + by_status.get('schema_ready', 0),
        'implementation_planned': by_status.get('planned', 0) + len(LEARNING_MODES),
        'ai_engine_readiness_pct': ai_readiness,
        'chat_ui_live': False,
        'rag_pipeline_live': False,
    },
    'catalog_gaps': [
        'No chat UI or AI learning assistant route',
        'No RAG pipeline or embedding store',
        'No API provider selected or integrated',
        'Learning modes defined but not selectable',
        'Evidence-first response generator not built',
        'Research/Event/Coalition assistants not operational',
        'MC intelligence recommendations not AI-powered',
        'Knowledge base too sparse for reliable answers (~13 facts, 14 evidence IDs)',
    ],
    'recommended_next_build': {
        'number': 27,
        'title': 'Component Specifications with Props/States',
        'note': 'Map wireframes to components; prepare Ask-a-Question UI shell for future AI integration.',
    },
}

path = root / 'data/ai-knowledge-engine.json'
with open(path, 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')
print(f'AI Engine: {len(capabilities)} capabilities, {ai_readiness}% readiness')
