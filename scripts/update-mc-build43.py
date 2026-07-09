import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json', encoding='utf-8') as f:
    mc = json.load(f)

title = 'Citizens United Facts Master Research Methodology & Standards Manual'

with open(root / 'data/research-methodology.json', encoding='utf-8') as f:
    rm = json.load(f)

s = rm['summary']

mc['version'] = '1.47.0'
mc['build'] = 43
mc['updated'] = '2026-07-09'
mc['research_methodology'] = '/data/research-methodology.json'
mc['research_methodology_dashboard'] = '/mission-control/research-methodology.html'

mc['executive'] = {
    'overall_completion': 43,
    'current_build': {'number': 43, 'title': title},
    'active_phase': 'Institutional Research — Methodology & Standards Manual',
    'last_completed': 'Master Civic Action Lab',
    'next_build': {'number': 44, 'title': 'Component specifications with props/states'},
    'github_status': 'connected',
    'netlify_status': 'production_healthy',
    'content_readiness': 26,
    'research_readiness': s['research_methodology_readiness_pct'],
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
    'research_methodology_readiness': s['research_methodology_readiness_pct'],
    'public_launch_readiness': 8,
    'public_launch_label': 'Early Foundation'
}

mc['research_methodology_inventory'] = {
    'readiness_score': s['research_methodology_readiness_pct'],
    'principles_total': s['principles_total'],
    'principles_partial': s['principles_partial'],
    'evidence_items': s['evidence_items'],
    'citation_coverage_pct': s['citation_coverage_pct'],
    'adherence_tracking_live': s['adherence_tracking_live'],
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 43
        bar['note'] = f"Research Methodology live — 10 principles, {s['evidence_items']} evidence items."
    if bar['id'] == 'civic_action_lab':
        bar['value'] = 26
        bar['note'] = 'Civic Action Lab — 5/6 divisions partial.'

if not any(b.get('id') == 'research_methodology' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'research_methodology',
        'label': 'Research Methodology & Standards',
        'value': s['research_methodology_readiness_pct'],
        'max': 100,
        'note': f"{s['principles_partial']}/10 principles partial — {s['citation_coverage_pct']}% citation coverage."
    })
else:
    for bar in mc['progress_bars']:
        if bar['id'] == 'research_methodology':
            bar['value'] = s['research_methodology_readiness_pct']
            bar['note'] = f"{s['principles_partial']}/10 principles partial."

mc['builds'].insert(0, {
    'number': 43,
    'title': title,
    'version': '1.47.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Institutional Research Constitution v1.0 — how do we know what we know',
    'summary': f"10 principles, 11 workflow stages; {s['evidence_items']} EV-* items; {s['research_methodology_readiness_pct']}% overall.",
    'files_created': [
        'data/research-methodology.json', 'docs/MASTER_RESEARCH_METHODOLOGY.md',
        'builds/043-master-research-methodology-standards-manual.md',
        'mission-control/research-methodology.html',
        'scripts/gen-research-methodology.py', 'scripts/update-mc-build43.py'
    ],
    'files_modified': ['js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml'],
    'pages_created': ['/mission-control/research-methodology.html'],
    'decisions_made': [
        '10 research principles — extends Build #10 (5 principles)',
        '11-stage research workflow — distinct from 9-stage evidence workflow',
        'Source evaluation checklist + QA standards',
        'Extends research-framework.json — not a replacement',
        'Adherence tracking planned — methodology defined first',
        f"{s['research_methodology_readiness_pct']}% honest readiness — {s['citation_coverage_pct']}% citations"
    ],
    'open_questions': ['Per-article adherence scoring?', 'Research project folder structure?', 'Review schedule automation?'],
    'risks': [f'Evidence at {s["evidence_items"]}/{s["evidence_v1_target"]}', '5 new principles unenforced', 'Documentation trail sparse'],
    'next_recommended': 44,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/research-methodology.html',
    'review_status': 'complete'
})

mc['briefing'] = {
    'what_built': 'Research Methodology v1.0 — 10 principles, 11-stage workflow, source checklist, MC metrics',
    'building_now': 'Methodology constitution — research-framework.json as foundation',
    'blocked': ['Adherence tracking', 'Scheduled review automation', 'Per-source evaluation records'],
    'ready_public': ['Research Methodology MC dashboard', '10-principle taxonomy', 'QA checklist'],
    'next': 'Build #44 — Component specifications with props/states'
}

if not any(n.get('id') == 'research_methodology' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'research_methodology', 'label': 'Research Methodology & Standards', 'href': '/mission-control/research-methodology.html', 'status': 'complete'
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
