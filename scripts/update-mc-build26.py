import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json') as f:
    mc = json.load(f)

title = 'Citizens United Facts AI Knowledge & Research Engine'

with open(root / 'data/ai-knowledge-engine.json') as f:
    ai = json.load(f)

s = ai['summary']

mc['version'] = '1.30.0'
mc['build'] = 26
mc['updated'] = '2026-07-09'
mc['ai_knowledge_engine'] = '/data/ai-knowledge-engine.json'
mc['ai_knowledge_dashboard'] = '/mission-control/ai-knowledge.html'

mc['executive'] = {
    'overall_completion': 26,
    'current_build': {'number': 26, 'title': title},
    'active_phase': 'Educational Intelligence — AI Knowledge Engine',
    'last_completed': 'Mission Control 2.0 & Executive Command Center',
    'next_build': {'number': 27, 'title': 'Component specifications with props/states'},
    'github_status': 'connected',
    'netlify_status': 'production_healthy',
    'content_readiness': 18,
    'research_readiness': 20,
    'data_viz_readiness': 2,
    'signup_funnel_readiness': 18,
    'civic_action_readiness': 26,
    'coalition_readiness': 14,
    'data_model_readiness': 38,
    'route_inventory_readiness': 18,
    'component_registry_readiness': 22,
    'facts_framework_readiness': 12,
    'knowledge_atlas_readiness': 18,
    'platform_architecture_readiness': 20,
    'repository_structure_readiness': 28,
    'database_schema_readiness': 35,
    'wireframe_readiness': 38,
    'contact_intelligence_readiness': 31,
    'mc2_readiness': 33,
    'ai_engine_readiness': 14,
    'public_launch_readiness': 8,
    'public_launch_label': 'Early Foundation'
}

mc['ai_engine_inventory'] = {
    'readiness_score': s['ai_engine_readiness_pct'],
    'capabilities': s['capabilities'],
    'learning_modes': s['learning_modes'],
    'example_questions': s['example_questions'],
    'knowledge_sources': s['knowledge_sources'],
    'guardrails': s['guardrails'],
    'chat_ui_live': s['chat_ui_live'],
    'rag_pipeline_live': s['rag_pipeline_live'],
    'by_status': s['by_status']
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 26
        bar['note'] = f"AI Knowledge Engine architecture live — {s['learning_modes']} learning modes, Arkansas Civic Librarian persona. No chat UI yet."

if not any(b.get('id') == 'ai_engine' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'ai_engine',
        'label': 'AI Knowledge Engine',
        'value': 14,
        'max': 100,
        'note': 'Architecture + guardrails defined; RAG pipeline and chat UI not built.'
    })

mc['builds'].insert(0, {
    'number': 26,
    'title': title,
    'version': '1.30.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Educational Intelligence Architecture v1.0 — help people understand, not persuade',
    'summary': f"{s['capabilities']} capabilities, {s['learning_modes']} modes, {s['example_questions']} seed questions; {s['ai_engine_readiness_pct']}% readiness.",
    'files_created': [
        'data/ai-knowledge-engine.json', 'docs/AI_KNOWLEDGE_ENGINE.md',
        'builds/026-ai-knowledge-engine.md', 'mission-control/ai-knowledge.html',
        'scripts/gen-ai-knowledge-engine.py', 'scripts/update-mc-build26.py'
    ],
    'files_modified': ['js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml'],
    'pages_created': ['/mission-control/ai-knowledge.html'],
    'decisions_made': [
        'Arkansas Civic Librarian persona — patient, neutral, evidence-focused',
        '5 learning modes: Quick Answer through Primary Source Explorer',
        'Evidence-first response schema with fact/legal/proposal distinction',
        '7 verified knowledge sources mapped; RAG must cite platform data only',
        '14% honest readiness — no chat UI, API, or RAG pipeline',
        'Human review required for generated presentation materials'
    ],
    'open_questions': ['API provider selection?', 'When to build Ask-a-Question UI?', 'Minimum knowledge base size before launch?'],
    'risks': ['14% readiness — architecture only', 'Sparse knowledge base (~13 facts, 14 evidence IDs)'],
    'next_recommended': 27,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/ai-knowledge.html',
    'review_status': 'complete'
})

mc['briefing'] = {
    'what_built': f'AI Knowledge Engine v1.0 — {s["capabilities"]} capabilities, Arkansas Civic Librarian, evidence-first architecture',
    'building_now': 'Educational intelligence architecture — component specs and Ask UI shell next',
    'blocked': ['No chat UI', 'No RAG pipeline', 'Knowledge base too sparse for reliable answers'],
    'ready_public': ['AI architecture MC dashboard', 'Learning modes + guardrails', 'Example question bank', 'Knowledge source map'],
    'next': 'Build #27 — Component specifications with props/states'
}

if not any(n.get('id') == 'ai_knowledge' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'ai_knowledge', 'label': 'AI Knowledge Engine', 'href': '/mission-control/ai-knowledge.html', 'status': 'complete'
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
