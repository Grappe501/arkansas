import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json', encoding='utf-8') as f:
    mc = json.load(f)

title = 'Citizens United Facts Master Governance, Stewardship & Institutional Constitution'

with open(root / 'data/governance-constitution.json', encoding='utf-8') as f:
    gov = json.load(f)

s = gov['summary']

mc['version'] = '1.53.0'
mc['build'] = 49
mc['updated'] = '2026-07-09'
mc['governance_constitution'] = '/data/governance-constitution.json'
mc['governance_dashboard'] = '/mission-control/governance.html'

mc['executive'] = {
    'overall_completion': 49,
    'current_build': {'number': 49, 'title': title},
    'active_phase': 'Institutional Constitution — Governance & Stewardship',
    'last_completed': 'Master Technical Architecture & Deployment Blueprint',
    'next_build': {'number': 50, 'title': 'Component specifications with props/states'},
    'github_status': 'connected',
    'netlify_status': 'production_healthy',
    'content_readiness': 28,
    'research_readiness': 25,
    'data_viz_readiness': 6,
    'signup_funnel_readiness': 22,
    'civic_action_readiness': 26,
    'coalition_readiness': 18,
    'data_model_readiness': 38,
    'route_inventory_readiness': 18,
    'component_registry_readiness': 22,
    'facts_framework_readiness': 14,
    'knowledge_atlas_readiness': 20,
    'platform_architecture_readiness': 24,
    'repository_structure_readiness': 28,
    'database_schema_readiness': 36,
    'wireframe_readiness': 38,
    'contact_intelligence_readiness': 31,
    'mc2_readiness': 33,
    'ai_engine_readiness': 14,
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
    'civic_intelligence_readiness': 24,
    'evidence_ledger_readiness': 22,
    'civic_action_lab_readiness': 26,
    'research_methodology_readiness': 25,
    'institutional_maturity_pct': 34,
    'current_institutional_version': 'V1',
    'systems_integration_readiness': 28,
    'production_matrix_readiness': 39,
    'visitor_journey_readiness': 40,
    'technical_architecture_readiness': 38,
    'governance_readiness': s['governance_readiness_pct'],
    'public_launch_readiness': 8,
    'public_launch_label': 'Early Foundation'
}

mc['governance_inventory'] = {
    'readiness_score': s['governance_readiness_pct'],
    'values_total': s['values_total'],
    'stewards_total': s['stewards_total'],
    'stewards_assigned': s['stewards_assigned'],
    'annual_review_live': s['annual_review_live'],
    'public_docs_live': s['public_docs_live'],
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 49
        bar['note'] = f"Governance Constitution live — {s['stewards_total']} steward roles, {s['values_total']} values."
    if bar['id'] == 'institutional_maturity':
        bar['value'] = 34
        bar['note'] = 'Institutional maturity V1 — governance constitution adds stewardship layer.'

if not any(b.get('id') == 'governance' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'governance',
        'label': 'Governance & Stewardship Constitution',
        'value': s['governance_readiness_pct'],
        'max': 100,
        'note': f"{s['stewards_assigned']}/{s['stewards_total']} stewards assigned — annual review planned."
    })
else:
    for bar in mc['progress_bars']:
        if bar['id'] == 'governance':
            bar['value'] = s['governance_readiness_pct']
            bar['note'] = f"{s['stewards_assigned']}/{s['stewards_total']} stewards assigned."

mc['builds'].insert(0, {
    'number': 49,
    'title': title,
    'version': '1.53.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Institutional Constitution — governance, stewardship, public trust, continuity',
    'summary': f"{s['values_total']} values, {s['stewards_total']} steward roles, {s['public_docs_live']} public docs live; {s['governance_readiness_pct']}% readiness.",
    'files_created': [
        'data/governance-constitution.json', 'docs/MASTER_GOVERNANCE_CONSTITUTION.md',
        'builds/049-master-governance-stewardship-institutional-constitution.md',
        'mission-control/governance.html',
        'scripts/gen-governance-constitution.py', 'scripts/update-mc-build49.py'
    ],
    'files_modified': ['js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml'],
    'pages_created': ['/mission-control/governance.html'],
    'decisions_made': [
        'Institutional Constitution v1.0 — supreme governance document for stewardship',
        '6 institutional values — Truth through Long-Term Stewardship',
        '7 steward roles — Executive through Mission Control',
        '4 decision categories — Operational, Editorial, Technical, Strategic',
        '7 public accountability documents — 2 live, 4 partial, 1 planned',
        'Institutional Oath — contributor commitment',
        f"{s['governance_readiness_pct']}% honest readiness — taxonomy live, stewards unassigned"
    ],
    'open_questions': ['Hierarchy vs Build #2 Project Constitution?', 'Steward assignment process?', 'Annual report automation?'],
    'risks': ['Governance without operational enforcement', '0 stewards assigned', 'Two constitutions may confuse'],
    'next_recommended': 50,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/governance.html',
    'review_status': 'complete'
})

mc['briefing'] = {
    'what_built': 'Governance Constitution v1.0 — values, stewards, accountability, oath, annual review framework',
    'building_now': 'Governance as MC first-class system — extends Build #2 constitution',
    'blocked': ['Steward assignments', 'Annual stewardship report', 'Correction log', 'Privacy policy'],
    'ready_public': ['Governance MC dashboard', 'Institutional Constitution', 'Public accountability index'],
    'next': 'Build #50 — Component specifications with props/states'
}

if not any(n.get('id') == 'governance' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'governance', 'label': 'Governance & Institutional Constitution', 'href': '/mission-control/governance.html', 'status': 'complete'
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
