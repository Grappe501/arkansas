import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json', encoding='utf-8') as f:
    mc = json.load(f)

title = 'Citizens United Facts Master Arkansas Communications & Public Education System v1.0'

with open(root / 'data/arkansas-communications.json', encoding='utf-8') as f:
    acom = json.load(f)

s = acom['summary']
prior_maturity = mc.get('executive', {}).get('institutional_maturity_pct', 32)

mc['version'] = '1.76.0'
mc['build'] = 72
mc['updated'] = '2026-07-09'
mc['arkansas_communications'] = '/data/arkansas-communications.json'
mc['arkansas_communications_dashboard'] = '/mission-control/arkansas-communications.html'

mc['executive'] = {
    'overall_completion': 72,
    'current_build': {'number': 72, 'title': title},
    'active_phase': 'Arkansas Communications → Implementation Translation',
    'last_completed': 'Arkansas Community Listening',
    'next_build': {'number': 73, 'title': 'Implementation translation layer & engineering artifacts'},
    'github_status': 'connected',
    'netlify_status': 'production_healthy',
    'content_readiness': max(28, s['arkansas_communications_readiness_pct'] - 10),
    'research_readiness': 26,
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
    'arkansas_community_listening_readiness': mc.get('executive', {}).get('arkansas_community_listening_readiness', 41),
    'arkansas_communications_readiness': s['arkansas_communications_readiness_pct'],
    'mc2_readiness': 42,
    'ai_engine_readiness': 34,
    'content_factory_readiness': max(s['content_factory_readiness_pct'], s['arkansas_communications_readiness_pct'] - 8),
    'education_academy_readiness': 26,
    'observatory_readiness': mc.get('executive', {}).get('observatory_readiness', 20),
    'outreach_readiness': max(34, s['arkansas_communications_readiness_pct'] - 6),
    'county_os_readiness': 28,
    'campaign_os_readiness': 34,
    'encyclopedia_readiness': 19,
    'narrative_readiness': max(24, s['arkansas_communications_readiness_pct'] - 14),
    'curriculum_readiness': 26,
    'trust_readiness': 30,
    'library_readiness': 22,
    'learning_lab_readiness': 22,
    'media_studio_readiness': max(s['media_studio_readiness_pct'], s['arkansas_communications_readiness_pct'] - 20),
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

mc['arkansas_communications_inventory'] = {
    'readiness_score': s['arkansas_communications_readiness_pct'],
    'articles_published': s['articles_published'],
    'editorial_calendar_live': s['editorial_calendar_live'],
    'one_institutional_voice': True,
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 72
        bar['note'] = 'Build #72 — Arkansas Communications & Public Education System.'
    if bar['id'] == 'content':
        bar['value'] = max(bar.get('value', 0), s['arkansas_communications_readiness_pct'] - 6)
        bar['note'] = f"One voice — {s['articles_published']} articles · {s['videos_released']} videos · calendar {'live' if s['editorial_calendar_live'] else 'planned'}."

if not any(b.get('id') == 'arkansas_communications' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'arkansas_communications',
        'label': 'Communications',
        'value': s['arkansas_communications_readiness_pct'],
        'max': 100,
        'note': f"{s['articles_published']} articles · review workflow {'live' if s['review_workflow_operational'] else 'planned'}.",
    })
else:
    for bar in mc['progress_bars']:
        if bar['id'] == 'arkansas_communications':
            bar['value'] = s['arkansas_communications_readiness_pct']

mc['builds'].insert(0, {
    'number': 72,
    'title': title,
    'version': '1.76.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Communications & Public Education — one voice, thousands of conversations',
    'summary': (
        f"Institutional voice, five objectives, content pyramid, editorial calendar, review process; "
        f"{s['arkansas_communications_readiness_pct']}% readiness. "
        f"0 articles · 0 videos · 0 emails · calendar not live."
    ),
    'files_created': [
        'data/arkansas-communications.json',
        'docs/MASTER_ARKANSAS_COMMUNICATIONS.md',
        'builds/072-arkansas-communications.md',
        'mission-control/arkansas-communications.html',
        'scripts/gen-arkansas-communications.py',
        'scripts/update-mc-build72.py',
    ],
    'files_modified': ['js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml'],
    'pages_created': ['/mission-control/arkansas-communications.html'],
    'decisions_made': [
        'One consistent institutional voice across all channels',
        'Education before persuasion — increase understanding not win arguments',
        'Five objectives: Explain, Connect, Invite, Equip, Strengthen',
        'Content pyramid — nine formats per major topic',
        'Six-step review: research → editorial → evidence → accessibility → publish → performance',
        'Educational reach not marketing performance',
        f"{s['arkansas_communications_readiness_pct']}% readiness — constitution only",
    ],
    'open_questions': [
        'Reconcile communications (#72) vs Content Factory (#27)?',
        'Editorial calendar: MC-native vs external tool?',
        'Social media: institutional accounts vs leader-generated?',
        'Communication effectiveness metrics — what counts as educational reach?',
    ],
    'risks': acom['catalog_gaps'][:4],
    'next_recommended': 73,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/arkansas-communications.html',
    'review_status': 'complete',
})

mc['briefing'] = {
    'what_built': 'Arkansas Communications v1.0 — one voice, institutional communications framework',
    'building_now': '72 builds specified — implementation translation next',
    'blocked': ['Editorial calendar', 'Review workflow', 'Presentation kit', 'Communications dashboard'],
    'ready_public': ['Institutional voice', 'Five objectives', 'Content pyramid', 'Review process spec'],
    'next': 'Build #73 — Implementation translation layer & engineering artifacts',
}

if not any(n.get('id') == 'arkansas_communications' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'arkansas_communications',
        'label': 'Communications',
        'href': '/mission-control/arkansas-communications.html',
        'status': 'complete',
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
