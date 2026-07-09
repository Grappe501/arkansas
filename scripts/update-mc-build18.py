import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json') as f:
    mc = json.load(f)

title = 'Citizens United Facts Framework'

with open(root / 'data/facts-registry.json') as f:
    fr = json.load(f)
with open(root / 'data/facts-framework.json') as f:
    fw = json.load(f)

s = fr['summary']

mc['version'] = '1.22.0'
mc['build'] = 18
mc['updated'] = '2026-07-09'
mc['facts_framework'] = '/data/facts-framework.json'
mc['facts_registry'] = '/data/facts-registry.json'
mc['facts_dashboard'] = '/mission-control/facts.html'

mc['executive'] = {
    'overall_completion': 18,
    'current_build': {'number': 18, 'title': title},
    'active_phase': 'Content Foundation — Facts Framework',
    'last_completed': 'Component Architecture & Design System Inventory',
    'next_build': {'number': 19, 'title': 'Brand & Identity System (logo, color, typography, voice, messaging)'},
    'github_status': 'connected',
    'netlify_status': 'production_healthy',
    'content_readiness': 14,
    'research_readiness': 20,
    'data_viz_readiness': 2,
    'signup_funnel_readiness': 14,
    'civic_action_readiness': 22,
    'coalition_readiness': 12,
    'data_model_readiness': 8,
    'route_inventory_readiness': 18,
    'component_registry_readiness': 22,
    'facts_framework_readiness': 12,
    'public_launch_readiness': 6,
    'public_launch_label': 'Early Foundation'
}

mc['facts_inventory'] = {
    'readiness_score': 12,
    'total_facts': s['total'],
    'verified': s['verified'],
    'confirmed': s['confirmed'],
    'strongly_supported': s['strongly_supported'],
    'context_dependent': s['context_dependent'],
    'under_review': s['under_review'],
    'awaiting_sources': s['awaiting_sources'],
    'arkansas_facts': s['arkansas_facts'],
    'categories': len(fw['categories']),
    'fact_completeness_pct': s['fact_completeness_pct'],
    'v1_target': s['v1_target']
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 18
        bar['note'] = f"Facts framework live — {s['total']} facts cataloged ({s['verified']} verified). Brand & Identity next."

if not any(b.get('id') == 'facts' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'facts',
        'label': 'Facts Framework',
        'value': 12,
        'max': 100,
        'note': f"{s['total']} facts, {s['verified']} verified, {s['under_review']} under review — honest v1 catalog."
    })

mc['builds'].insert(0, {
    'number': 18,
    'title': title,
    'version': '1.22.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Canonical Facts & Evidence Architecture v1.0 — foundation for all educational content',
    'summary': f"{s['total']} facts in 6 categories; 4 confidence levels; L1–L4 presentation; EV/KG integration; claims migrated.",
    'files_created': [
        'data/facts-framework.json', 'data/facts-registry.json',
        'docs/FACTS_CONSTITUTION.md', 'builds/018-citizens-united-facts-framework.md',
        'mission-control/facts.html', 'scripts/gen-facts-registry.py',
        'scripts/update-mc-build18.py'
    ],
    'files_modified': [
        'js/mission-control.js', 'data/claims-ledger.json', 'data/site.json',
        'BUILD_PLAN.md', 'netlify.toml', 'data/brand-identity.json'
    ],
    'pages_created': ['/mission-control/facts.html'],
    'decisions_made': [
        'FACT-1000 through FACT-6000 category system',
        'Four confidence levels: confirmed, strongly_supported, context_dependent, under_review',
        'Facts trace to Evidence Registry (EV-*) and Knowledge Graph (KG-*)',
        'Claims ledger linked via fact_id — 3 claims migrated',
        'Build #19: Brand & Identity System before mass content'
    ],
    'open_questions': ['Public FACT-IDs on educational pages?', 'FEC dataset integration timeline?'],
    'risks': [f"Only {s['total']} of ~{s['v1_target']} v1 target facts cataloged — gaps documented"],
    'next_recommended': 19,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/facts.html',
    'review_status': 'complete'
})

mc['briefing'] = {
    'what_built': f'Facts Framework v1.0 — {s["total"]} canonical facts with evidence traceability',
    'building_now': 'Content foundation — Brand & Identity System next (Build #19)',
    'blocked': ['Hundreds of facts not yet cataloged', 'FEC spending data for FACT-4000 series'],
    'ready_public': ['Facts MC dashboard', 'FACTS_CONSTITUTION.md', 'Claims-to-facts migration'],
    'next': 'Build #19 — Brand & Identity System'
}

if not any(n.get('id') == 'facts' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'facts', 'label': 'Facts Framework', 'href': '/mission-control/facts.html', 'status': 'complete'
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
