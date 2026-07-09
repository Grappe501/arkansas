import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json', encoding='utf-8') as f:
    mc = json.load(f)

title = 'Citizens United Facts Master Arkansas Community Intelligence & Listening System v1.0'

with open(root / 'data/arkansas-community-listening.json', encoding='utf-8') as f:
    acl = json.load(f)

s = acl['summary']
prior_maturity = mc.get('executive', {}).get('institutional_maturity_pct', 32)

mc['version'] = '1.75.0'
mc['build'] = 71
mc['updated'] = '2026-07-09'
mc['arkansas_community_listening'] = '/data/arkansas-community-listening.json'
mc['arkansas_community_listening_dashboard'] = '/mission-control/arkansas-community-listening.html'

mc['executive'] = {
    'overall_completion': 71,
    'current_build': {'number': 71, 'title': title},
    'active_phase': 'Community Listening → Implementation Translation',
    'last_completed': 'Arkansas Command Strategy',
    'next_build': {'number': 72, 'title': 'Implementation translation layer & engineering artifacts'},
    'github_status': 'connected',
    'netlify_status': 'production_healthy',
    'content_readiness': 28,
    'research_readiness': max(26, s['arkansas_community_listening_readiness_pct'] - 10),
    'data_viz_readiness': 12,
    'signup_funnel_readiness': 26,
    'civic_action_readiness': 28,
    'coalition_readiness': 44,
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
    'relationship_os_readiness': mc.get('executive', {}).get('relationship_os_readiness', 54),
    'institutional_ai_readiness': 42,
    'coalition_network_readiness': 44,
    'citizen_action_center_readiness': 42,
    'campaign_finance_observatory_readiness': 36,
    'arkansas_action_network_readiness': 38,
    'civic_intelligence_command_center_readiness': 43,
    'sustainability_stewardship_readiness': 38,
    'impact_measurement_readiness': 31,
    'citizen_leadership_academy_readiness': 34,
    'relational_organizing_growth_engine_readiness': mc.get('executive', {}).get('relational_organizing_growth_engine_readiness', 34),
    'arkansas_command_strategy_readiness': mc.get('executive', {}).get('arkansas_command_strategy_readiness', 39),
    'arkansas_community_listening_readiness': s['arkansas_community_listening_readiness_pct'],
    'mc2_readiness': 42,
    'ai_engine_readiness': 34,
    'content_factory_readiness': 30,
    'education_academy_readiness': 26,
    'observatory_readiness': max(s['research_observatory_readiness_pct'], s['arkansas_community_listening_readiness_pct'] - 12),
    'outreach_readiness': 34,
    'county_os_readiness': 28,
    'campaign_os_readiness': 34,
    'encyclopedia_readiness': 19,
    'narrative_readiness': 24,
    'curriculum_readiness': 26,
    'trust_readiness': 30,
    'library_readiness': 22,
    'learning_lab_readiness': 22,
    'media_studio_readiness': 18,
    'civic_intelligence_readiness': 36,
    'evidence_ledger_readiness': 22,
    'civic_action_lab_readiness': 26,
    'research_methodology_readiness': 25,
    'institutional_maturity_pct': prior_maturity,
    'current_institutional_version': 'V1',
    'systems_integration_readiness': 44,
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
    'statewide_growth_readiness': mc.get('executive', {}).get('statewide_growth_readiness', 48),
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

mc['arkansas_community_listening_inventory'] = {
    'readiness_score': s['arkansas_community_listening_readiness_pct'],
    'questions_received': s['questions_received'],
    'listening_sources': s['listening_sources'],
    'question_observatory_live': s['question_observatory_live'],
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 71
        bar['note'] = 'Build #71 — Community Intelligence & Listening System.'
    if bar['id'] == 'research':
        bar['value'] = max(bar.get('value', 0), s['arkansas_community_listening_readiness_pct'] - 8)
        bar['note'] = f"Listening network — {s['questions_received']} questions · {s['education_leader_reports']} leader reports."

if not any(b.get('id') == 'arkansas_community_listening' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'arkansas_community_listening',
        'label': 'Community Listening',
        'value': s['arkansas_community_listening_readiness_pct'],
        'max': 100,
        'note': f"{s['questions_received']} questions · observatory {'live' if s['question_observatory_live'] else 'planned'}.",
    })
else:
    for bar in mc['progress_bars']:
        if bar['id'] == 'arkansas_community_listening':
            bar['value'] = s['arkansas_community_listening_readiness_pct']

mc['builds'].insert(0, {
    'number': 71,
    'title': title,
    'version': '1.75.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Community Intelligence & Listening — learn from Arkansas, not only teach',
    'summary': (
        f"Six listening sources, question observatory, needs mapping, workflow, pulse reports; "
        f"{s['arkansas_community_listening_readiness_pct']}% readiness. "
        f"0 questions · 0 leader reports · 0 pulse reports."
    ),
    'files_created': [
        'data/arkansas-community-listening.json',
        'docs/MASTER_ARKANSAS_COMMUNITY_LISTENING.md',
        'builds/071-arkansas-community-listening.md',
        'mission-control/arkansas-community-listening.html',
        'scripts/gen-arkansas-community-listening.py',
        'scripts/update-mc-build71.py',
    ],
    'files_modified': ['js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml'],
    'pages_created': ['/mission-control/arkansas-community-listening.html'],
    'decisions_made': [
        'Listening as important as publishing — learn from Arkansas',
        'Operating principle: begin by listening, not answers',
        'Six sources: learners, leaders, coalition, conversations, research, public',
        'Question Observatory — living inventory drives new content',
        'Listening-to-action workflow — nothing in a black hole',
        'Community Pulse Reports — monthly, quarterly, annual',
        f"{s['arkansas_community_listening_readiness_pct']}% readiness — constitution only",
    ],
    'open_questions': [
        'Reconcile listening (#71) vs Research Observatory (#29)?',
        'Unify feedback channels with Citizen Action Center (#62)?',
        'Conversation analysis privacy model — aggregate only?',
        'Leader reporting: structured form vs free text?',
    ],
    'risks': acl['catalog_gaps'][:4],
    'next_recommended': 72,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/arkansas-community-listening.html',
    'review_status': 'complete',
})

mc['briefing'] = {
    'what_built': 'Arkansas Community Listening v1.0 — statewide civic listening network',
    'building_now': '71 builds specified — implementation translation next',
    'blocked': ['Feedback forms', 'Question Observatory', 'Workflow tracker', 'Pulse reports'],
    'ready_public': ['Six sources', 'Operating principle', 'Workflow spec', 'Listening tour'],
    'next': 'Build #72 — Implementation translation layer & engineering artifacts',
}

if not any(n.get('id') == 'arkansas_community_listening' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'arkansas_community_listening',
        'label': 'Community Listening',
        'href': '/mission-control/arkansas-community-listening.html',
        'status': 'complete',
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
