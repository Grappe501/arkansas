import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json', encoding='utf-8') as f:
    mc = json.load(f)

title = 'Citizens United Facts Master Technical Architecture & Deployment Blueprint'

with open(root / 'data/technical-architecture.json', encoding='utf-8') as f:
    ta = json.load(f)

s = ta['summary']

mc['version'] = '1.52.0'
mc['build'] = 48
mc['updated'] = '2026-07-09'
mc['technical_architecture'] = '/data/technical-architecture.json'
mc['technical_architecture_dashboard'] = '/mission-control/technical-architecture.html'

mc['executive'] = {
    'overall_completion': 48,
    'current_build': {'number': 48, 'title': title},
    'active_phase': 'Production Engineering — Technical Architecture & Deployment',
    'last_completed': 'Master Visitor Journey & Behavioral Architecture',
    'next_build': {'number': 49, 'title': 'Component specifications with props/states'},
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
    'institutional_maturity_pct': 32,
    'current_institutional_version': 'V1',
    'systems_integration_readiness': 28,
    'production_matrix_readiness': 39,
    'visitor_journey_readiness': 40,
    'technical_architecture_readiness': s['technical_architecture_readiness_pct'],
    'public_launch_readiness': 8,
    'public_launch_label': 'Early Foundation'
}

mc['technical_architecture_inventory'] = {
    'readiness_score': s['technical_architecture_readiness_pct'],
    'stack_live': s['stack_live'],
    'stack_layers_total': s['stack_layers_total'],
    'preview_deploys_live': s['preview_deploys_live'],
    'nextjs_migration': s['nextjs_migration'],
    'neon_postgres_live': s['neon_postgres_live'],
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 48
        bar['note'] = f"Technical Architecture live — {s['stack_live']}/{s['stack_layers_total']} stack layers, GitHub→Netlify."
    if bar['id'] == 'institutional_maturity':
        bar['value'] = 32
        bar['note'] = 'Institutional maturity V1 — 32% overall.'

if not any(b.get('id') == 'technical_architecture' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'technical_architecture',
        'label': 'Technical Architecture & Deployment',
        'value': s['technical_architecture_readiness_pct'],
        'max': 100,
        'note': f"{s['stack_live']}/{s['stack_layers_total']} live — static v1, Next.js/Neon planned."
    })
else:
    for bar in mc['progress_bars']:
        if bar['id'] == 'technical_architecture':
            bar['value'] = s['technical_architecture_readiness_pct']
            bar['note'] = f"{s['stack_live']}/{s['stack_layers_total']} stack live."

mc['builds'].insert(0, {
    'number': 48,
    'title': title,
    'version': '1.52.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Production engineering constitution — how the institution will be built',
    'summary': f"{s['stack_live']}/{s['stack_layers_total']} stack live, {s['apis_partial_or_live']}/{s['apis_total']} APIs partial; {s['technical_architecture_readiness_pct']}% readiness.",
    'files_created': [
        'data/technical-architecture.json', 'docs/MASTER_TECHNICAL_ARCHITECTURE.md',
        'builds/048-master-technical-architecture-deployment-blueprint.md',
        'mission-control/technical-architecture.html',
        'scripts/gen-technical-architecture.py', 'scripts/update-mc-build48.py'
    ],
    'files_modified': ['js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml'],
    'pages_created': ['/mission-control/technical-architecture.html'],
    'decisions_made': [
        'Target stack: Next.js, Tailwind, Neon PostgreSQL, Prisma',
        'GitHub → Netlify deployment pipeline — live with PR previews',
        'Mission Control as CMS — not traditional CMS',
        '11 internal APIs documented — static JSON v1',
        'AI layer grounded in institutional registries',
        f"{s['technical_architecture_readiness_pct']}% honest readiness — static v1, migration planned"
    ],
    'open_questions': ['Neon provisioning timing?', 'Next.js migration vs incremental?', 'Auth provider choice?'],
    'risks': ['Two architecture docs (Build #20 + #48)', 'Static v1 diverges from target stack', 'No monitoring'],
    'next_recommended': 49,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/technical-architecture.html',
    'review_status': 'complete'
})

mc['briefing'] = {
    'what_built': 'Technical Architecture v1.0 — stack, deployment, APIs, monitoring, scalability',
    'building_now': 'Static v1 on Netlify — target Next.js/Neon documented',
    'blocked': ['Neon provisioning', 'Next.js migration', 'Global search', 'Auth'],
    'ready_public': ['Technical Architecture MC dashboard', 'Deployment workflow', 'Stack constitution'],
    'next': 'Build #49 — Component specifications with props/states'
}

if not any(n.get('id') == 'technical_architecture' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'technical_architecture', 'label': 'Technical Architecture & Deployment', 'href': '/mission-control/technical-architecture.html', 'status': 'complete'
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
