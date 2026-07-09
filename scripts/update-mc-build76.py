import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json', encoding='utf-8') as f:
    mc = json.load(f)

title = 'Citizens United Facts Master Organizational Constitution & Operating Charter v1.0'

with open(root / 'data/organizational-constitution.json', encoding='utf-8') as f:
    oc = json.load(f)

s = oc['summary']
prior_maturity = mc.get('executive', {}).get('institutional_maturity_pct', 32)

mc['version'] = '1.80.0'
mc['build'] = 76
mc['updated'] = '2026-07-09'
mc['organizational_constitution'] = '/data/organizational-constitution.json'
mc['organizational_constitution_dashboard'] = '/mission-control/organizational-constitution.html'

mc['executive'] = {
    'overall_completion': 76,
    'current_build': {'number': 76, 'title': title},
    'active_phase': 'Founding Constitution → Implementation Translation',
    'last_completed': 'Volunteer & Funding Constitution',
    'next_build': {'number': 77, 'title': 'Implementation translation layer & engineering artifacts'},
    'github_status': 'connected',
    'netlify_status': 'production_healthy',
    'content_readiness': 28,
    'research_readiness': mc.get('executive', {}).get('research_readiness', 43),
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
    'campaign_finance_observatory_readiness': mc.get('executive', {}).get('campaign_finance_observatory_readiness', 38),
    'arkansas_action_network_readiness': 38,
    'civic_intelligence_command_center_readiness': 43,
    'sustainability_stewardship_readiness': mc.get('executive', {}).get('sustainability_stewardship_readiness', 38),
    'impact_measurement_readiness': 31,
    'citizen_leadership_academy_readiness': 34,
    'relational_organizing_growth_engine_readiness': mc.get('executive', {}).get('relational_organizing_growth_engine_readiness', 34),
    'arkansas_command_strategy_readiness': mc.get('executive', {}).get('arkansas_command_strategy_readiness', 39),
    'arkansas_community_listening_readiness': mc.get('executive', {}).get('arkansas_community_listening_readiness', 41),
    'arkansas_communications_readiness': mc.get('executive', {}).get('arkansas_communications_readiness', 42),
    'arkansas_research_institute_readiness': mc.get('executive', {}).get('arkansas_research_institute_readiness', 43),
    'arkansas_civic_innovation_reform_readiness': mc.get('executive', {}).get('arkansas_civic_innovation_reform_readiness', 44),
    'volunteer_funding_constitution_readiness': mc.get('executive', {}).get('volunteer_funding_constitution_readiness', 45),
    'organizational_constitution_readiness': s['organizational_constitution_readiness_pct'],
    'mc2_readiness': 42,
    'ai_engine_readiness': 34,
    'content_factory_readiness': 30,
    'education_academy_readiness': 26,
    'observatory_readiness': mc.get('executive', {}).get('observatory_readiness', 43),
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
    'research_methodology_readiness': mc.get('executive', {}).get('research_methodology_readiness', 29),
    'institutional_maturity_pct': prior_maturity,
    'current_institutional_version': 'V1',
    'systems_integration_readiness': 44,
    'production_matrix_readiness': 39,
    'visitor_journey_readiness': 40,
    'technical_architecture_readiness': 38,
    'governance_readiness': max(s['governance_readiness_pct'], s['organizational_constitution_readiness_pct']),
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

mc['organizational_constitution_inventory'] = {
    'readiness_score': s['organizational_constitution_readiness_pct'],
    'articles_ratified': s['articles_ratified'],
    'departments_total': s['departments_total'],
    'founding_constitution': True,
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 76
        bar['note'] = 'Build #76 — Founding Organizational Constitution.'
    if bar['id'] == 'governance':
        bar['value'] = max(bar.get('value', 0), s['organizational_constitution_readiness_pct'])
        bar['note'] = f"Founding charter — {s['articles_ratified']} articles · {s['departments_operational']}/{s['departments_total']} departments."

if not any(b.get('id') == 'organizational_constitution' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'organizational_constitution',
        'label': 'Founding Constitution',
        'value': s['organizational_constitution_readiness_pct'],
        'max': 100,
        'note': f"{s['constitutional_amendments']} amendments · adherence {'live' if s['adherence_monitoring_live'] else 'planned'}.",
    })
else:
    for bar in mc['progress_bars']:
        if bar['id'] == 'organizational_constitution':
            bar['value'] = s['organizational_constitution_readiness_pct']

mc['builds'].insert(0, {
    'number': 76,
    'title': title,
    'version': '1.80.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Founding Constitution — permanent framework for entire institution',
    'summary': (
        f"15 articles, 6 values, 10 departments, motto, creed, founder principle; "
        f"{s['organizational_constitution_readiness_pct']}% readiness. "
        f"0/10 departments operational · 0 amendments."
    ),
    'files_created': [
        'data/organizational-constitution.json',
        'docs/MASTER_ORGANIZATIONAL_CONSTITUTION.md',
        'builds/076-organizational-constitution.md',
        'mission-control/organizational-constitution.html',
        'scripts/gen-organizational-constitution.py',
        'scripts/update-mc-build76.py',
    ],
    'files_modified': ['js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml'],
    'pages_created': ['/mission-control/organizational-constitution.html'],
    'decisions_made': [
        'Founding Constitution — everything flows from this document',
        '15 articles: name through amendment process',
        'Motto: Understand First · Verify Always · Teach Others',
        'Vision: 75 counties · 250 cities · 200K connected',
        '10 permanent departments; MC as executive operating system',
        'Aligns Articles VIII-IX with Volunteer & Funding (#75)',
        f"{s['organizational_constitution_readiness_pct']}% readiness — constitution only",
    ],
    'open_questions': [
        'Reconcile #76 founding vs #49 governance vs #2 project constitution?',
        'Public constitution page on front door?',
        'Department registry: MC-native or external?',
        'Amendment workflow: who proposes, who ratifies?',
    ],
    'risks': oc['catalog_gaps'][:4],
    'next_recommended': 77,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/organizational-constitution.html',
    'review_status': 'complete',
})

mc['briefing'] = {
    'what_built': 'Organizational Constitution v1.0 — founding charter, 15 articles',
    'building_now': '76 builds specified — implementation translation next',
    'blocked': ['Department registry', 'Amendment log', 'Adherence monitoring', 'Public constitution page'],
    'ready_public': ['15 articles', '6 values', 'Motto', 'Creed', 'Founder principle'],
    'next': 'Build #77 — Implementation translation layer & engineering artifacts',
}

if not any(n.get('id') == 'organizational_constitution' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'organizational_constitution',
        'label': 'Founding Constitution',
        'href': '/mission-control/organizational-constitution.html',
        'status': 'complete',
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
