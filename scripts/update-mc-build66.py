import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json', encoding='utf-8') as f:
    mc = json.load(f)

title = 'Citizens United Facts Master Sustainability, Funding & Institutional Stewardship Blueprint v1.0'

with open(root / 'data/sustainability-stewardship.json', encoding='utf-8') as f:
    ss = json.load(f)

s = ss['summary']

mc['version'] = '1.70.0'
mc['build'] = 66
mc['updated'] = '2026-07-09'
mc['sustainability_stewardship'] = '/data/sustainability-stewardship.json'
mc['sustainability_stewardship_dashboard'] = '/mission-control/sustainability-stewardship.html'

mc['executive'] = {
    'overall_completion': 66,
    'current_build': {'number': 66, 'title': title},
    'active_phase': 'Sustainability Stewardship → Implementation Translation',
    'last_completed': 'Civic Intelligence Command Center',
    'next_build': {'number': 67, 'title': 'Implementation translation layer & engineering artifacts'},
    'github_status': 'connected',
    'netlify_status': 'production_healthy',
    'content_readiness': 28,
    'research_readiness': 26,
    'data_viz_readiness': 12,
    'signup_funnel_readiness': 24,
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
    'relationship_os_readiness': 54,
    'institutional_ai_readiness': 42,
    'coalition_network_readiness': 44,
    'citizen_action_center_readiness': 42,
    'campaign_finance_observatory_readiness': 36,
    'arkansas_action_network_readiness': 38,
    'civic_intelligence_command_center_readiness': 43,
    'sustainability_stewardship_readiness': s['sustainability_stewardship_readiness_pct'],
    'mc2_readiness': 39,
    'ai_engine_readiness': 34,
    'content_factory_readiness': 30,
    'education_academy_readiness': 26,
    'observatory_readiness': 20,
    'outreach_readiness': 24,
    'county_os_readiness': 28,
    'campaign_os_readiness': 34,
    'encyclopedia_readiness': 19,
    'narrative_readiness': 24,
    'curriculum_readiness': 26,
    'trust_readiness': max(24, s['sustainability_stewardship_readiness_pct'] - 10),
    'library_readiness': 22,
    'learning_lab_readiness': 22,
    'media_studio_readiness': 18,
    'civic_intelligence_readiness': 35,
    'evidence_ledger_readiness': 22,
    'civic_action_lab_readiness': 26,
    'research_methodology_readiness': 25,
    'institutional_maturity_pct': s['institutional_maturity_pct'],
    'current_institutional_version': 'V1',
    'systems_integration_readiness': 41,
    'production_matrix_readiness': 39,
    'visitor_journey_readiness': 40,
    'technical_architecture_readiness': 38,
    'governance_readiness': s['governance_readiness_pct'],
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

mc['sustainability_stewardship_inventory'] = {
    'readiness_score': s['sustainability_stewardship_readiness_pct'],
    'funding_sources_active': s['funding_sources_active'],
    'volunteers_onboarded': s['volunteers_onboarded'],
    'annual_report_live': s['annual_report_live'],
    'long_term_institution': True,
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 66
        bar['note'] = 'Build #66 — Sustainability & Stewardship.'
    if bar['id'] == 'institutional_maturity':
        bar['value'] = s['institutional_maturity_pct']
        bar['note'] = f"Long-term institution — {s['funding_sources_active']} funding sources."
    if bar['id'] == 'trust':
        bar['value'] = mc['executive']['trust_readiness']
        bar['note'] = '5 sustainability principles · 0 active funding sources.'

if not any(b.get('id') == 'sustainability_stewardship' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'sustainability_stewardship',
        'label': 'Sustainability & Stewardship',
        'value': s['sustainability_stewardship_readiness_pct'],
        'max': 100,
        'note': f"5 principles · {s['documentation_builds']} builds documented.",
    })
else:
    for bar in mc['progress_bars']:
        if bar['id'] == 'sustainability_stewardship':
            bar['value'] = s['sustainability_stewardship_readiness_pct']

mc['builds'].insert(0, {
    'number': 66,
    'title': title,
    'version': '1.70.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Sustainability & Stewardship — long-term institution without compromising educational integrity',
    'summary': (
        f"5 sustainability principles; funding portfolio; volunteer stewardship; knowledge preservation; "
        f"{s['sustainability_stewardship_readiness_pct']}% readiness. "
        f"0 funding sources · 0 volunteers · reserve not established."
    ),
    'files_created': [
        'data/sustainability-stewardship.json',
        'docs/MASTER_SUSTAINABILITY_STEWARDSHIP.md',
        'builds/066-sustainability-stewardship.md',
        'mission-control/sustainability-stewardship.html',
        'scripts/gen-sustainability-stewardship.py',
        'scripts/update-mc-build66.py',
    ],
    'files_modified': ['js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml'],
    'pages_created': ['/mission-control/sustainability-stewardship.html'],
    'decisions_made': [
        'Long-term sustainability — never choose survival over educational integrity',
        '5-test funding filter: mission, independence, transparency, value, trust',
        '5 funding categories — diversify, document transparently',
        'Knowledge preservation as important as financial continuity',
        'Annual Sustainability Report specified — not yet generated',
        'Integrates Governance (#49), PMO (#54), Command Center (#65)',
        f"{s['sustainability_stewardship_readiness_pct']}% readiness — blueprint only, no revenue tracking",
    ],
    'open_questions': [
        '501(c)(3) structure vs fiscal sponsor for Arkansas pilot?',
        'Public donor recognition policy vs confidentiality?',
        'Reserve target: months of operating expenses?',
        'Unify annual report with Governance stewardship report (#49)?',
    ],
    'risks': ss['catalog_gaps'][:4],
    'next_recommended': 67,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/sustainability-stewardship.html',
    'review_status': 'complete',
})

mc['briefing'] = {
    'what_built': 'Sustainability & Stewardship v1.0 — institution that lasts',
    'building_now': '66 builds specified — implementation translation next',
    'blocked': ['Funding registry', 'Volunteer tracking', 'Annual report', 'Reserve policy'],
    'ready_public': ['5 principles', 'Funding portfolio spec', 'Knowledge preservation', 'Sustainability dashboard'],
    'next': 'Build #67 — Implementation translation layer & engineering artifacts',
}

if not any(n.get('id') == 'sustainability_stewardship' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'sustainability_stewardship',
        'label': 'Sustainability & Stewardship',
        'href': '/mission-control/sustainability-stewardship.html',
        'status': 'complete',
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
