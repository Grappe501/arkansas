import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json', encoding='utf-8') as f:
    mc = json.load(f)

title = 'Citizens United Facts Master Content Production Matrix'

with open(root / 'data/content-production-matrix.json', encoding='utf-8') as f:
    cpm = json.load(f)

s = cpm['summary']

mc['version'] = '1.50.0'
mc['build'] = 46
mc['updated'] = '2026-07-09'
mc['content_production_matrix'] = '/data/content-production-matrix.json'
mc['content_production_matrix_dashboard'] = '/mission-control/content-production-matrix.html'

mc['executive'] = {
    'overall_completion': 46,
    'current_build': {'number': 46, 'title': title},
    'active_phase': 'Content Production Matrix — Master Library & Build Sequencing',
    'last_completed': 'Master Systems Integration Blueprint',
    'next_build': {'number': 47, 'title': 'Component specifications with props/states'},
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
    'platform_architecture_readiness': 20,
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
    'institutional_maturity_pct': 32,
    'current_institutional_version': 'V1',
    'systems_integration_readiness': 28,
    'production_matrix_readiness': s['production_matrix_readiness_pct'],
    'public_launch_readiness': 8,
    'public_launch_label': 'Early Foundation'
}

mc['production_matrix_inventory'] = {
    'readiness_score': s['production_matrix_readiness_pct'],
    'domains_total': s['domains_total'],
    'institutional_target_total': s['institutional_target_total'],
    'assets_registered': s['assets_registered'],
    'assets_published': s['assets_published'],
    'overall_completion_pct': s['overall_completion_pct'],
    'production_automation_live': s['production_automation_live'],
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 46
        bar['note'] = f"Production Matrix live — {s['assets_registered']} assets queued, {s['overall_completion_pct']}% complete."
    if bar['id'] == 'institutional_maturity':
        bar['value'] = 32
        bar['note'] = 'Institutional maturity V1 — 32% overall.'

if not any(b.get('id') == 'production_matrix' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'production_matrix',
        'label': 'Content Production Matrix',
        'value': s['production_matrix_readiness_pct'],
        'max': 100,
        'note': f"{s['assets_published']}/{s['institutional_target_total']} published — no automation."
    })
else:
    for bar in mc['progress_bars']:
        if bar['id'] == 'production_matrix':
            bar['value'] = s['production_matrix_readiness_pct']
            bar['note'] = f"{s['assets_published']}/{s['institutional_target_total']} published."

mc['builds'].insert(0, {
    'number': 46,
    'title': title,
    'version': '1.50.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Master production matrix — every educational asset ID\'d and sequenced',
    'summary': f"14 domains, {s['assets_registered']} queued, {s['assets_published']} published; {s['overall_completion_pct']}% institutional completion.",
    'files_created': [
        'data/content-production-matrix.json', 'docs/MASTER_CONTENT_PRODUCTION_MATRIX.md',
        'builds/046-master-content-production-matrix.md', 'mission-control/content-production-matrix.html',
        'scripts/gen-content-production-matrix.py', 'scripts/update-mc-build46.py'
    ],
    'files_modified': ['js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml'],
    'pages_created': ['/mission-control/content-production-matrix.html'],
    'decisions_made': [
        '14 content domains (1000–14000) — master library production taxonomy',
        '11-stage production pipeline — extends Build #6 inventory lifecycle',
        '10 production ID prefixes — ARTICLE, CASE, TIMELINE, VIDEO, etc.',
        'Executive production dashboard — 11 completion metrics from live registries',
        f"{s['assets_registered']} assets registered of {s['institutional_target_total']} target — honest queue coverage",
        f"{s['production_matrix_readiness_pct']}% readiness — taxonomy live, automation none"
    ],
    'open_questions': ['Unified domain IDs vs Build #6 inventory?', 'Velocity tracking for capacity model?', 'CMS workflow enforcement?'],
    'risks': ['~2000 assets target vs 15 published', 'Domain ID remap may confuse editors', 'No automated sequencing'],
    'next_recommended': 47,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/content-production-matrix.html',
    'review_status': 'complete'
})

mc['briefing'] = {
    'what_built': 'Production Matrix v1.0 — 14 domains, production queue, executive dashboard, capacity planning',
    'building_now': 'Registry linking — 351 inventory items mapped to matrix domains',
    'blocked': ['Production automation', 'Capacity velocity model', 'CMS stage enforcement'],
    'ready_public': ['Production Matrix MC dashboard', '14-domain taxonomy', 'Production queue sample'],
    'next': 'Build #47 — Component specifications with props/states'
}

if not any(n.get('id') == 'production_matrix' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'production_matrix', 'label': 'Content Production Matrix', 'href': '/mission-control/content-production-matrix.html', 'status': 'complete'
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
