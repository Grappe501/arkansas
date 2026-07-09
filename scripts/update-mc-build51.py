import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json', encoding='utf-8') as f:
    mc = json.load(f)

title = 'Citizens United Facts Master Data Architecture & Canonical Data Dictionary v1.0'

with open(root / 'data/data-architecture.json', encoding='utf-8') as f:
    da = json.load(f)

s = da['summary']

mc['version'] = '1.55.0'
mc['build'] = 51
mc['updated'] = '2026-07-09'
mc['data_architecture'] = '/data/data-architecture.json'
mc['data_architecture_dashboard'] = '/mission-control/data-architecture.html'

mc['executive'] = {
    'overall_completion': 51,
    'current_build': {'number': 51, 'title': title},
    'active_phase': 'Implementation — Data Constitution Established',
    'last_completed': 'Master Build Bible',
    'next_build': {'number': 52, 'title': 'Master implementation roadmap & sprint zero'},
    'github_status': 'connected',
    'netlify_status': 'production_healthy',
    'content_readiness': 28,
    'research_readiness': 25,
    'data_viz_readiness': 6,
    'signup_funnel_readiness': 22,
    'civic_action_readiness': 26,
    'coalition_readiness': 18,
    'data_model_readiness': 52,
    'route_inventory_readiness': 18,
    'component_registry_readiness': 22,
    'facts_framework_readiness': 14,
    'knowledge_atlas_readiness': 20,
    'platform_architecture_readiness': 24,
    'repository_structure_readiness': 28,
    'database_schema_readiness': 40,
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
    'institutional_maturity_pct': 37,
    'current_institutional_version': 'V1',
    'systems_integration_readiness': 28,
    'production_matrix_readiness': 39,
    'visitor_journey_readiness': 40,
    'technical_architecture_readiness': 38,
    'governance_readiness': 44,
    'build_bible_readiness': 49,
    'data_architecture_readiness': s['data_architecture_readiness_pct'],
    'planning_phase_complete': True,
    'implementation_phase': 'data_constitution_established',
    'public_launch_readiness': 8,
    'public_launch_label': 'Early Foundation'
}

mc['data_architecture_inventory'] = {
    'readiness_score': s['data_architecture_readiness_pct'],
    'domains_total': s['domains_total'],
    'domains_live': s['domains_live'],
    'domains_partial': s['domains_partial'],
    'relationship_edges': s['relationship_edges'],
    'knowledge_published': s['knowledge_published'],
    'evidence_records': s['evidence_records'],
    'database_provisioned': s['database_provisioned'],
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 51
        bar['note'] = 'Build #51 — Master Data Architecture & Canonical Data Dictionary complete.'
    if bar['id'] == 'institutional_maturity':
        bar['value'] = 37
        bar['note'] = '12-domain data constitution — implementation continues.'

if not any(b.get('id') == 'data_architecture' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'data_architecture',
        'label': 'Master Data Architecture',
        'value': s['data_architecture_readiness_pct'],
        'max': 100,
        'note': f"{s['domains_live']} live + {s['domains_partial']} partial domains · {s['relationship_edges']} edges."
    })
else:
    for bar in mc['progress_bars']:
        if bar['id'] == 'data_architecture':
            bar['value'] = s['data_architecture_readiness_pct']
            bar['note'] = f"12 domains · {s['relationship_edges']} relationship edges."

mc['builds'].insert(0, {
    'number': 51,
    'title': title,
    'version': '1.55.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Institutional Data Constitution — 12 canonical domains, single source of truth',
    'summary': (
        f"12 domains (100–1200), {s['relationship_verbs']} relationship verbs, "
        f"{s['data_architecture_readiness_pct']}% readiness — {s['relationship_edges']} edges."
    ),
    'files_created': [
        'data/data-architecture.json', 'docs/MASTER_DATA_ARCHITECTURE.md',
        'builds/051-master-data-architecture.md', 'mission-control/data-architecture.html',
        'scripts/gen-data-architecture.py', 'scripts/update-mc-build51.py'
    ],
    'files_modified': ['js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml'],
    'pages_created': ['/mission-control/data-architecture.html'],
    'decisions_made': [
        '12 canonical data domains (100–1200) — permanent institutional taxonomy',
        'Canonical object model — 12 shared fields on every major object',
        '10 institutional relationship verbs — graph built from structured edges',
        '6-state publishing lifecycle — Draft through Scheduled Review',
        '8 domain APIs defined — none deployed; raw data access prohibited',
        f"{s['data_architecture_readiness_pct']}% readiness — constitution live, database/APIs pending"
    ],
    'open_questions': [
        'Migrate Build #15 canonical objects to 12-domain model?',
        'First domain API — Identity or Knowledge?',
        'Neon provisioning timeline?',
        'Relationship edge pilot scope?'
    ],
    'risks': [
        'Two data models coexist (Build #15 + Build #51) until migration',
        '0 relationship edges — knowledge graph remains theoretical',
        'Metadata standards defined but not enforced',
        'Constitution without database = documentation only'
    ],
    'next_recommended': 52,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/data-architecture.html',
    'review_status': 'complete'
})

mc['briefing'] = {
    'what_built': 'Data Architecture v1.0 — 12 domains, canonical dictionary, relationship standards, API philosophy',
    'building_now': 'Implementation — data constitution established; Sprint Zero next',
    'blocked': ['Neon provisioning', 'Domain APIs', 'Relationship edge population', 'Search index'],
    'ready_public': ['Data Architecture MC dashboard', '12-domain taxonomy', 'Institutional data philosophy'],
    'next': 'Build #52 — Master implementation roadmap & sprint zero'
}

if not any(n.get('id') == 'data_architecture' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'data_architecture',
        'label': 'Master Data Architecture',
        'href': '/mission-control/data-architecture.html',
        'status': 'complete'
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
