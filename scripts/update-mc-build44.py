import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json', encoding='utf-8') as f:
    mc = json.load(f)

title = 'Citizens United Facts Master Institutional Roadmap'

with open(root / 'data/institutional-roadmap.json', encoding='utf-8') as f:
    ir = json.load(f)

s = ir['summary']

mc['version'] = '1.48.0'
mc['build'] = 44
mc['updated'] = '2026-07-09'
mc['institutional_roadmap'] = '/data/institutional-roadmap.json'
mc['institutional_roadmap_dashboard'] = '/mission-control/institutional-roadmap.html'

mc['executive'] = {
    'overall_completion': 44,
    'current_build': {'number': 44, 'title': title},
    'active_phase': 'Strategic Evolution — Master Institutional Roadmap V1–V10',
    'last_completed': 'Master Research Methodology & Standards Manual',
    'next_build': {'number': 45, 'title': 'Component specifications with props/states'},
    'github_status': 'connected',
    'netlify_status': 'production_healthy',
    'content_readiness': 26,
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
    'platform_architecture_readiness': 20,
    'repository_structure_readiness': 28,
    'database_schema_readiness': 36,
    'wireframe_readiness': 38,
    'contact_intelligence_readiness': 31,
    'mc2_readiness': 33,
    'ai_engine_readiness': 14,
    'content_factory_readiness': 28,
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
    'institutional_maturity_pct': s['institutional_maturity_pct'],
    'current_institutional_version': s['current_institutional_version'],
    'public_launch_readiness': 8,
    'public_launch_label': 'Early Foundation'
}

mc['institutional_roadmap_inventory'] = {
    'readiness_score': s['institutional_maturity_pct'],
    'current_version': s['current_institutional_version'],
    'next_version': s['next_institutional_version'],
    'versions_partial': s['versions_partial'],
    'v1_maturity_pct': s['v1_maturity_pct'],
    'software_builds': s['software_builds_complete'],
    'annual_review_live': s['annual_review_live'],
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 44
        bar['note'] = f"Institutional Roadmap live — {s['current_institutional_version']} at {s['v1_maturity_pct']}%, {s['institutional_maturity_pct']}% maturity."
    if bar['id'] == 'research_methodology':
        bar['value'] = 25
        bar['note'] = 'Research Methodology — 10 principles defined.'

if not any(b.get('id') == 'institutional_maturity' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'institutional_maturity',
        'label': 'Institutional Maturity (V1–V10)',
        'value': s['institutional_maturity_pct'],
        'max': 100,
        'note': f"Current: {s['current_institutional_version']} — software build #44 ≠ V10."
    })
else:
    for bar in mc['progress_bars']:
        if bar['id'] == 'institutional_maturity':
            bar['value'] = s['institutional_maturity_pct']
            bar['note'] = f"Current: {s['current_institutional_version']} at {s['v1_maturity_pct']}%."

mc['builds'].insert(0, {
    'number': 44,
    'title': title,
    'version': '1.48.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'V1–V10 Strategic Evolution Plan — institutional maturity over software completion',
    'summary': f"10 institutional versions, {s['current_institutional_version']} active; {s['institutional_maturity_pct']}% overall maturity.",
    'files_created': [
        'data/institutional-roadmap.json', 'docs/MASTER_INSTITUTIONAL_ROADMAP.md',
        'builds/044-master-institutional-roadmap.md', 'mission-control/institutional-roadmap.html',
        'scripts/gen-institutional-roadmap.py', 'scripts/update-mc-build44.py'
    ],
    'files_modified': ['js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml'],
    'pages_created': ['/mission-control/institutional-roadmap.html'],
    'decisions_made': [
        '10 institutional versions V1 Foundation through V10 Permanent Institution',
        'Institutional maturity distinct from software build count (44 builds ≠ V10)',
        'Current position: V1 completing, early V2 Arkansas Expansion',
        'Cross-version priorities + annual review + preservation + sustainability',
        'Success definition — quality of understanding, not platform size',
        f"{s['institutional_maturity_pct']}% honest institutional maturity"
    ],
    'open_questions': ['First annual strategic review date?', 'V2 county activation strategy?', 'Governance framework timing?'],
    'risks': ['44 builds may imply false maturity', 'V1 enrollment at 0', 'V4–V7 architecture without delivery'],
    'next_recommended': 45,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/institutional-roadmap.html',
    'review_status': 'complete'
})

mc['briefing'] = {
    'what_built': 'Institutional Roadmap v1.0 — V1–V10 versions, maturity metrics, preservation strategy',
    'building_now': 'V1 Foundation completing — platform live, enrollment and content partial',
    'blocked': ['Annual review workflow', 'Governance framework', 'V2 county activation'],
    'ready_public': ['Institutional Roadmap MC dashboard', '10-version taxonomy', 'Honest maturity scoring'],
    'next': 'Build #45 — Component specifications with props/states'
}

if not any(n.get('id') == 'institutional_roadmap' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'institutional_roadmap', 'label': 'Master Institutional Roadmap', 'href': '/mission-control/institutional-roadmap.html', 'status': 'complete'
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
