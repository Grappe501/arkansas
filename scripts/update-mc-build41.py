import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json') as f:
    mc = json.load(f)

title = 'Citizens United Facts Master Evidence Ledger & Claims Registry'

with open(root / 'data/evidence-ledger.json') as f:
    ledger = json.load(f)

s = ledger['summary']

mc['version'] = '1.45.0'
mc['build'] = 41
mc['updated'] = '2026-07-09'
mc['evidence_ledger'] = '/data/evidence-ledger.json'
mc['evidence_ledger_dashboard'] = '/mission-control/evidence-ledger.html'

mc['executive'] = {
    'overall_completion': 41,
    'current_build': {'number': 41, 'title': title},
    'active_phase': 'Institutional Truth — Master Evidence Ledger & Claims Registry',
    'last_completed': 'Master Knowledge Graph & Civic Intelligence Engine',
    'next_build': {'number': 42, 'title': 'Component specifications with props/states'},
    'github_status': 'connected',
    'netlify_status': 'production_healthy',
    'content_readiness': 26,
    'research_readiness': 28,
    'data_viz_readiness': 6,
    'signup_funnel_readiness': 22,
    'civic_action_readiness': 32,
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
    'evidence_ledger_readiness': s['evidence_ledger_readiness_pct'],
    'public_launch_readiness': 8,
    'public_launch_label': 'Early Foundation'
}

mc['evidence_ledger_inventory'] = {
    'readiness_score': s['evidence_ledger_readiness_pct'],
    'claims_total': s['claims_total'],
    'claims_verified': s['claims_verified'],
    'claims_awaiting_review': s['claims_awaiting_review'],
    'evidence_items_total': s['evidence_items_total'],
    'audit_trail_live': s['audit_trail_live'],
    'public_claim_pages_live': s['public_claim_pages_live'],
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 41
        bar['note'] = f"Evidence Ledger live — {s['claims_total']} CLAIM-* records, {s['claims_verified']} verified."
    if bar['id'] == 'civic_intelligence':
        bar['value'] = 24
        bar['note'] = 'Institutional Brain — 38/500 KG nodes.'

if not any(b.get('id') == 'evidence_ledger' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'evidence_ledger',
        'label': 'Master Evidence Ledger',
        'value': s['evidence_ledger_readiness_pct'],
        'max': 100,
        'note': f"{s['claims_total']}/500 claims — no public claim pages or audit trail."
    })
else:
    for bar in mc['progress_bars']:
        if bar['id'] == 'evidence_ledger':
            bar['value'] = s['evidence_ledger_readiness_pct']
            bar['note'] = f"{s['claims_total']}/500 claims — no public claim pages."

mc['builds'].insert(0, {
    'number': 41,
    'title': title,
    'version': '1.45.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Institutional Truth Architecture v1.0 — every claim traceable to evidence',
    'summary': f"{s['claims_total']} CLAIM-* records, {s['evidence_items_total']} EV-* items; {s['evidence_ledger_readiness_pct']}% overall.",
    'files_created': [
        'data/evidence-ledger.json', 'docs/MASTER_EVIDENCE_LEDGER.md',
        'builds/041-master-evidence-ledger-claims-registry.md',
        'mission-control/evidence-ledger.html',
        'scripts/gen-evidence-ledger.py', 'scripts/update-mc-build41.py'
    ],
    'files_modified': ['js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml'],
    'pages_created': ['/mission-control/evidence-ledger.html'],
    'decisions_made': [
        'CLAIM-{6-digit} canonical format — extends legacy claim-* and FACT-*',
        '5 evidence strength levels A–E — adds synthesis level',
        '7-stage review workflow — scheduled review planned',
        '3 claims seeded from claims-ledger with full record structure',
        'Contradictory evidence policy — transparency over hiding disagreement',
        f"{s['evidence_ledger_readiness_pct']}% honest readiness — 3/500 claims"
    ],
    'open_questions': ['Migrate all FACT-* to CLAIM-*?', 'Public claim page design?', 'Audit trail storage?'],
    'risks': [f'Only {s["claims_growth_pct"]}% of claim target', '0 audit history records', 'Hawaii claim requires review'],
    'next_recommended': 42,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/evidence-ledger.html',
    'review_status': 'complete'
})

mc['briefing'] = {
    'what_built': 'Evidence Ledger v1.0 — CLAIM-* registry, A–E strength levels, review workflow, MC metrics',
    'building_now': '3 canonical claims from legacy ledger — facts and evidence linked',
    'blocked': ['Public claim pages', 'Audit trail', 'Scheduled review automation'],
    'ready_public': ['Evidence Ledger MC dashboard', 'CLAIM-* format', 'Strength level taxonomy'],
    'next': 'Build #42 — Component specifications with props/states'
}

if not any(n.get('id') == 'evidence_ledger' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'evidence_ledger', 'label': 'Master Evidence Ledger', 'href': '/mission-control/evidence-ledger.html', 'status': 'complete'
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
