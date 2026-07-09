import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json', encoding='utf-8') as f:
    mc = json.load(f)

title = 'Citizens United Facts Institutional AI Brain & Knowledge Assistant v1.0'

with open(root / 'data/institutional-ai.json', encoding='utf-8') as f:
    ia = json.load(f)

s = ia['summary']

mc['version'] = '1.64.0'
mc['build'] = 60
mc['updated'] = '2026-07-09'
mc['institutional_ai'] = '/data/institutional-ai.json'
mc['institutional_ai_dashboard'] = '/mission-control/institutional-ai.html'

mc['executive'] = {
    'overall_completion': 60,
    'current_build': {'number': 60, 'title': title},
    'active_phase': 'Institutional AI Brain → Implementation Translation',
    'last_completed': 'Relationship Operating System',
    'next_build': {'number': 61, 'title': 'Implementation translation layer & engineering artifacts'},
    'github_status': 'connected',
    'netlify_status': 'production_healthy',
    'content_readiness': 28,
    'research_readiness': 25,
    'data_viz_readiness': 8,
    'signup_funnel_readiness': 22,
    'civic_action_readiness': 28,
    'coalition_readiness': 18,
    'data_model_readiness': 54,
    'route_inventory_readiness': 18,
    'component_registry_readiness': 22,
    'facts_framework_readiness': 14,
    'knowledge_atlas_readiness': 20,
    'platform_architecture_readiness': 24,
    'repository_structure_readiness': 28,
    'database_schema_readiness': 42,
    'wireframe_readiness': 38,
    'contact_intelligence_readiness': 34,
    'relationship_os_readiness': 54,
    'institutional_ai_readiness': s['institutional_ai_readiness_pct'],
    'mc2_readiness': 33,
    'ai_engine_readiness': s['ai_engine_readiness_pct'],
    'content_factory_readiness': 30,
    'education_academy_readiness': 26,
    'observatory_readiness': 20,
    'outreach_readiness': 22,
    'county_os_readiness': 28,
    'campaign_os_readiness': 34,
    'encyclopedia_readiness': 19,
    'narrative_readiness': 24,
    'curriculum_readiness': 26,
    'trust_readiness': 24,
    'library_readiness': 22,
    'learning_lab_readiness': 22,
    'media_studio_readiness': 18,
    'civic_intelligence_readiness': 28,
    'evidence_ledger_readiness': 22,
    'civic_action_lab_readiness': 26,
    'research_methodology_readiness': 25,
    'institutional_maturity_pct': 47,
    'current_institutional_version': 'V1',
    'systems_integration_readiness': 32,
    'production_matrix_readiness': 39,
    'visitor_journey_readiness': 40,
    'technical_architecture_readiness': 38,
    'governance_readiness': 44,
    'build_bible_readiness': 49,
    'data_architecture_readiness': 41,
    'ux_architecture_readiness': 39,
    'launch_strategy_readiness': 39,
    'pmo_readiness': 46,
    'master_plan_readiness': 56,
    'statewide_growth_readiness': 48,
    'neighborhood_organizing_readiness': 50,
    'civic_atlas_readiness': 52,
    'rollout_phase': 0,
    'rollout_phase_title': 'Private Development',
    'planning_phase_complete': True,
    'planning_constitution_complete': True,
    'implementation_phase': 'translation_layer_next',
    'public_launch_readiness': s['public_launch_readiness_pct'],
    'public_launch_label': 'Early Foundation',
    'public_launch_recommended': False,
}

mc['institutional_ai_inventory'] = {
    'readiness_score': s['institutional_ai_readiness_pct'],
    'seven_roles': s['seven_roles_defined'],
    'roles_operational': s['roles_operational'],
    'questions_answered': s['questions_answered'],
    'chat_ui_live': s['chat_ui_live'],
    'rag_pipeline_live': s['rag_pipeline_live'],
    'evidence_is_authority': True,
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 60
        bar['note'] = 'Build #60 — Institutional AI Brain.'
    if bar['id'] == 'institutional_maturity':
        bar['value'] = 47
        bar['note'] = 'AI teaches, never replaces thinking — no runtime yet.'
    if bar['id'] == 'ai_knowledge' or bar.get('label', '').startswith('AI'):
        pass

if not any(b.get('id') == 'institutional_ai' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'institutional_ai',
        'label': 'Institutional AI',
        'value': s['institutional_ai_readiness_pct'],
        'max': 100,
        'note': f"7 roles · 0 operational · RAG not live."
    })
else:
    for bar in mc['progress_bars']:
        if bar['id'] == 'institutional_ai':
            bar['value'] = s['institutional_ai_readiness_pct']
            bar['note'] = 'Evidence is authority — librarian not teacher.'

# Update AI Knowledge Engine bar if present
for bar in mc['progress_bars']:
    if bar.get('id') == 'ai_knowledge' or bar.get('label') == 'AI Knowledge Engine':
        bar['value'] = s['ai_engine_readiness_pct']
        bar['note'] = 'Extended by Build #60 Institutional AI Brain.'

mc['builds'].insert(0, {
    'number': 60,
    'title': title,
    'version': '1.64.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Institutional AI Brain — Arkansas Civic Intelligence System',
    'summary': (
        f"7 AI roles; Rule #1 source grounding; confidence levels; "
        f"{s['institutional_ai_readiness_pct']}% institutional AI readiness. "
        f"0 questions answered · no chat UI."
    ),
    'files_created': [
        'data/institutional-ai.json', 'docs/MASTER_INSTITUTIONAL_AI.md',
        'builds/060-institutional-ai.md', 'mission-control/institutional-ai.html',
        'scripts/gen-institutional-ai.py', 'scripts/update-mc-build60.py',
    ],
    'files_modified': ['js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml'],
    'pages_created': ['/mission-control/institutional-ai.html'],
    'decisions_made': [
        'Not a chatbot — institutional intelligence layer',
        'Institutional Rule #1: never invent knowledge — trace to 8 source types',
        'Evidence is authority; AI is librarian/guide',
        '7 roles: Learning, Research, Constitutional, Arkansas Civic, Leader, Coalition, MC (internal)',
        '4 confidence levels — never disguise uncertainty',
        'Extends AI Knowledge Engine (#26) — Arkansas Civic Librarian persona',
        f"{s['institutional_ai_readiness_pct']}% readiness — architecture only, no RAG/chat",
    ],
    'open_questions': [
        'Consolidate #26 ai-knowledge.html with #60 institutional-ai.html?',
        'RAG provider: OpenAI vs Anthropic vs local?',
        'Public vs authenticated role boundaries?',
        'MC Assistant access control model?',
    ],
    'risks': ia['catalog_gaps'][:4],
    'next_recommended': 61,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/institutional-ai.html',
    'review_status': 'complete'
})

mc['briefing'] = {
    'what_built': 'Institutional AI Brain v1.0 — 7 roles, Rule #1 grounding, confidence model',
    'building_now': 'Full intelligence stack (#56–#60) specified — implementation translation next',
    'blocked': ['RAG pipeline', 'Chat UI', 'API provider', 'Citation runtime'],
    'ready_public': ['7 role model', 'Safety principles', 'Source panel spec', 'MC AI metrics'],
    'next': 'Build #61 — Implementation translation layer & engineering artifacts'
}

if not any(n.get('id') == 'institutional_ai' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'institutional_ai',
        'label': 'Institutional AI',
        'href': '/mission-control/institutional-ai.html',
        'status': 'complete'
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
