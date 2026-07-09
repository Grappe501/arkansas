import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json') as f:
    mc = json.load(f)

title = 'Citizens United Facts Evidence, Transparency & Trust Framework'

with open(root / 'data/trust-framework.json') as f:
    trust = json.load(f)

s = trust['summary']
snap = trust['registry_snapshot']
db_dec = trust['database_decision']

mc['version'] = '1.40.0'
mc['build'] = 36
mc['updated'] = '2026-07-09'
mc['trust_framework'] = '/data/trust-framework.json'
mc['trust_dashboard'] = '/mission-control/trust.html'

mc['executive'] = {
    'overall_completion': 36,
    'current_build': {'number': 36, 'title': title},
    'active_phase': 'Public Trust — Evidence, Transparency & Verification',
    'last_completed': 'Master Curriculum & Learning Standards',
    'next_build': {'number': 37, 'title': 'Component specifications with props/states'},
    'github_status': 'connected',
    'netlify_status': 'production_healthy',
    'content_readiness': 26,
    'research_readiness': 26,
    'data_viz_readiness': 4,
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
    'observatory_readiness': 18,
    'outreach_readiness': 22,
    'county_os_readiness': 28,
    'campaign_os_readiness': 34,
    'encyclopedia_readiness': 19,
    'narrative_readiness': 24,
    'curriculum_readiness': 26,
    'trust_readiness': s['trust_readiness_pct'],
    'public_launch_readiness': 8,
    'public_launch_label': 'Early Foundation'
}

mc['trust_inventory'] = {
    'readiness_score': s['trust_readiness_pct'],
    'trust_pyramid_levels': s['trust_pyramid_levels'],
    'facts_verified': snap['facts_verified'],
    'facts_total': snap['facts_total'],
    'evidence_total': snap['evidence_total'],
    'citation_coverage_pct': snap['citation_coverage_pct'],
    'transparency_panels_live': s['transparency_panels_live'],
    'page_sourcing_live': s['page_sourcing_live'],
    'database_decision': db_dec['governing_rule'],
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 36
        bar['note'] = f"Trust OS live — {snap['facts_verified']}/{snap['facts_total']} facts verified, show don't tell."

if not any(b.get('id') == 'trust' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'trust',
        'label': 'Trust Framework',
        'value': s['trust_readiness_pct'],
        'max': 100,
        'note': f"{snap['citation_coverage_pct']}% citation coverage — transparency panels planned."
    })

mc['builds'].insert(0, {
    'number': 36,
    'title': title,
    'version': '1.40.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Public Trust Operating System v1.0 — trust as measurable objective',
    'summary': f"5-level trust pyramid, 4 evidence levels, 8 trust metrics; v2 DB: Netlify or Neon; {s['trust_readiness_pct']}% readiness.",
    'files_created': [
        'data/trust-framework.json', 'docs/PUBLIC_TRUST_OPERATING_SYSTEM.md',
        'builds/036-evidence-transparency-trust.md', 'mission-control/trust.html',
        'scripts/gen-trust-framework.py', 'scripts/update-mc-build36.py'
    ],
    'files_modified': ['js/mission-control.js', 'data/site.json', 'data/database-schema.json', 'BUILD_PLAN.md', 'netlify.toml'],
    'pages_created': ['/mission-control/trust.html'],
    'decisions_made': [
        'Trust philosophy: show verification, do not ask for blind trust',
        '5-level trust pyramid + 4 evidence levels (A–D)',
        '6-stage fact review process + 3 transparency panel types',
        'v1: static JSON + Netlify Forms (unchanged)',
        'v2 trial: Netlify Database OR Neon (Postgres)',
        'Supabase deferred until auth/RLS/participant profiles needed',
        f"{s['trust_readiness_pct']}% honest readiness — panels and page sourcing not live"
    ],
    'open_questions': ['Correction policy page timing?', 'When to provision Netlify Database trial?'],
    'risks': ['12% citation coverage', '0 academic Level C sources', 'Transparency panels not on halls'],
    'next_recommended': 37,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/trust.html',
    'review_status': 'complete'
})

mc['briefing'] = {
    'what_built': 'Trust OS v1.0 — pyramid, evidence levels, trust dashboard, database v2 decision',
    'building_now': 'Public trust architecture — verify don\'t believe',
    'blocked': ['Transparency panels not on pages', 'Reader feedback workflow', 'Correction policy page'],
    'ready_public': ['Trust MC dashboard', 'Evidence A–D taxonomy', 'Database decision documented'],
    'next': 'Build #37 — Component specifications with props/states'
}

if not any(n.get('id') == 'trust' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'trust', 'label': 'Trust Framework', 'href': '/mission-control/trust.html', 'status': 'complete'
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
