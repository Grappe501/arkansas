import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json', encoding='utf-8') as f:
    mc = json.load(f)

title = 'Citizens United Facts Master Citizen Leadership Academy v1.0'

with open(root / 'data/citizen-leadership-academy.json', encoding='utf-8') as f:
    cla = json.load(f)

s = cla['summary']
prior_maturity = mc.get('executive', {}).get('institutional_maturity_pct', 32)

mc['version'] = '1.72.0'
mc['build'] = 68
mc['updated'] = '2026-07-09'
mc['citizen_leadership_academy'] = '/data/citizen-leadership-academy.json'
mc['citizen_leadership_academy_dashboard'] = '/mission-control/citizen-leadership-academy.html'

mc['executive'] = {
    'overall_completion': 68,
    'current_build': {'number': 68, 'title': title},
    'active_phase': 'Citizen Leadership Academy → Implementation Translation',
    'last_completed': 'Impact Measurement & Arkansas Civic Scorecard',
    'next_build': {'number': 69, 'title': 'Implementation translation layer & engineering artifacts'},
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
    'sustainability_stewardship_readiness': 38,
    'impact_measurement_readiness': 31,
    'citizen_leadership_academy_readiness': s['citizen_leadership_academy_readiness_pct'],
    'mc2_readiness': 41,
    'ai_engine_readiness': 34,
    'content_factory_readiness': 30,
    'education_academy_readiness': max(s.get('education_academy_readiness_pct', 26), s['citizen_leadership_academy_readiness_pct'] - 8),
    'observatory_readiness': 20,
    'outreach_readiness': 24,
    'county_os_readiness': 28,
    'campaign_os_readiness': 34,
    'encyclopedia_readiness': 19,
    'narrative_readiness': 24,
    'curriculum_readiness': 26,
    'trust_readiness': 28,
    'library_readiness': 22,
    'learning_lab_readiness': 22,
    'media_studio_readiness': 18,
    'civic_intelligence_readiness': 36,
    'evidence_ledger_readiness': 22,
    'civic_action_lab_readiness': 26,
    'research_methodology_readiness': 25,
    'institutional_maturity_pct': prior_maturity,
    'current_institutional_version': 'V1',
    'systems_integration_readiness': 43,
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

mc['citizen_leadership_academy_inventory'] = {
    'readiness_score': s['citizen_leadership_academy_readiness_pct'],
    'certification_levels': s['certification_levels'],
    'education_leaders': s['education_leaders'],
    'highest_strategic_priority': True,
    'human_engine': True,
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 68
        bar['note'] = 'Build #68 — Citizen Leadership Academy.'
    if bar['id'] == 'education_academy':
        bar['value'] = mc['executive']['education_academy_readiness']
        bar['note'] = f"6 certification levels · {s['education_leaders']} leaders · human engine."

if not any(b.get('id') == 'citizen_leadership_academy' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'citizen_leadership_academy',
        'label': 'Citizen Leadership Academy',
        'value': s['citizen_leadership_academy_readiness_pct'],
        'max': 100,
        'note': f"6 levels · {s['graduates_total']} graduates · {s['education_leaders']} leaders.",
    })
else:
    for bar in mc['progress_bars']:
        if bar['id'] == 'citizen_leadership_academy':
            bar['value'] = s['citizen_leadership_academy_readiness_pct']

mc['builds'].insert(0, {
    'number': 68,
    'title': title,
    'version': '1.72.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Citizen Leadership Academy — human engine developing civic education leaders statewide',
    'summary': (
        f"6 certification levels; Learn→Multiply philosophy; portfolios & mentorship; "
        f"{s['citizen_leadership_academy_readiness_pct']}% readiness. "
        f"0 learners · 0 graduates · 0 leaders."
    ),
    'files_created': [
        'data/citizen-leadership-academy.json',
        'docs/MASTER_CITIZEN_LEADERSHIP_ACADEMY.md',
        'builds/068-citizen-leadership-academy.md',
        'mission-control/citizen-leadership-academy.html',
        'scripts/gen-citizen-leadership-academy.py',
        'scripts/update-mc-build68.py',
    ],
    'files_modified': ['js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml'],
    'pages_created': ['/mission-control/citizen-leadership-academy.html'],
    'decisions_made': [
        'Human engine — highest strategic priority alongside coalition',
        '6 certification levels: Civic Learner through Arkansas Civic Fellow',
        'Philosophy: Learn → Practice → Teach → Lead → Mentor → Multiply',
        'Produces teachers, not spokespeople',
        'Extends Education Academy (#28) — 4-stage vs 6-level unification pending',
        'Graduation commitment — voluntary educational values statement',
        f"{s['citizen_leadership_academy_readiness_pct']}% readiness — constitution only, no LMS",
    ],
    'open_questions': [
        'Unify /academy/ public route with education-academy (#28)?',
        'Level 3 Education Leader = Action Network Level 5?',
        'Portfolio: public profile vs private MC view?',
        'Certification badges: digital credentials standard?',
    ],
    'risks': cla['catalog_gaps'][:4],
    'next_recommended': 69,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/citizen-leadership-academy.html',
    'review_status': 'complete',
})

mc['briefing'] = {
    'what_built': 'Citizen Leadership Academy v1.0 — 6 levels, human engine',
    'building_now': '68 builds specified — implementation translation next',
    'blocked': ['LMS', 'Certification workflow', 'Portfolios', 'Mentorship graph'],
    'ready_public': ['6 levels', 'Learning model', 'Competencies', 'Graduation commitment'],
    'next': 'Build #69 — Implementation translation layer & engineering artifacts',
}

if not any(n.get('id') == 'citizen_leadership_academy' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'citizen_leadership_academy',
        'label': 'Citizen Leadership Academy',
        'href': '/mission-control/citizen-leadership-academy.html',
        'status': 'complete',
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
