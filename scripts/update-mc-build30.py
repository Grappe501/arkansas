import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json') as f:
    mc = json.load(f)

title = 'Citizens United Facts Public Engagement & Education Campaign System'

with open(root / 'data/outreach-engine.json') as f:
    out = json.load(f)

s = out['summary']

mc['version'] = '1.34.0'
mc['build'] = 30
mc['updated'] = '2026-07-09'
mc['outreach_engine'] = '/data/outreach-engine.json'
mc['outreach_dashboard'] = '/mission-control/outreach.html'

mc['executive'] = {
    'overall_completion': 30,
    'current_build': {'number': 30, 'title': title},
    'active_phase': 'Arkansas Outreach — Public Engagement Campaign System',
    'last_completed': 'Research Observatory',
    'next_build': {'number': 31, 'title': 'Component specifications with props/states'},
    'github_status': 'connected',
    'netlify_status': 'production_healthy',
    'content_readiness': 20,
    'research_readiness': 22,
    'data_viz_readiness': 2,
    'signup_funnel_readiness': 22,
    'civic_action_readiness': 30,
    'coalition_readiness': 16,
    'data_model_readiness': 38,
    'route_inventory_readiness': 18,
    'component_registry_readiness': 22,
    'facts_framework_readiness': 12,
    'knowledge_atlas_readiness': 18,
    'platform_architecture_readiness': 20,
    'repository_structure_readiness': 28,
    'database_schema_readiness': 35,
    'wireframe_readiness': 38,
    'contact_intelligence_readiness': 31,
    'mc2_readiness': 33,
    'ai_engine_readiness': 14,
    'content_factory_readiness': 28,
    'education_academy_readiness': 24,
    'observatory_readiness': 18,
    'outreach_readiness': 22,
    'public_launch_readiness': 8,
    'public_launch_label': 'Early Foundation'
}

mc['outreach_inventory'] = {
    'readiness_score': s['outreach_readiness_pct'],
    'pillars': s['pillars'],
    'campaigns': s['campaigns'],
    'campaigns_partial': s['campaigns_partial'],
    'analytics_live': s['analytics_live'],
    'campaign_management_live': s['campaign_management_live'],
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 30
        bar['note'] = f"Outreach Engine live — {s['pillars']} pillars, {s['campaigns']} campaigns. Help more Arkansans understand."
    if bar['id'] == 'relational':
        bar['value'] = 14
        bar['note'] = f"Outreach defined — share page partial; referral tracking not integrated."

if not any(b.get('id') == 'outreach' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'outreach',
        'label': 'Outreach Engine',
        'value': 22,
        'max': 100,
        'note': f"{s['pillars_partial']} pillars partial — no analytics or campaign management yet."
    })

mc['builds'].insert(0, {
    'number': 30,
    'title': title,
    'version': '1.34.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Arkansas Outreach Engine v1.0 — expand understanding, not attention',
    'summary': f"{s['pillars']} pillars, {s['campaigns']} campaigns, {s['share_toolkit_items']} share toolkit items; {s['outreach_readiness_pct']}% readiness.",
    'files_created': [
        'data/outreach-engine.json', 'docs/OUTREACH_ENGINE.md',
        'builds/030-outreach-engine.md', 'mission-control/outreach.html',
        'scripts/gen-outreach-engine.py', 'scripts/update-mc-build30.py'
    ],
    'files_modified': ['js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml'],
    'pages_created': ['/mission-control/outreach.html'],
    'decisions_made': [
        '7-step outreach sequence: Discover through Build Community',
        '5 pillars: digital, social, conversations, coalition, public officials',
        '7 campaign types defined',
        '10 analytics metrics — educational impact over popularity',
        'County outreach profiles linked to coalition index',
        '22% honest readiness — share/coalition partial, no analytics'
    ],
    'open_questions': ['Analytics provider (GA vs Plausible)?', 'When to launch first campaign?'],
    'risks': ['22% readiness — campaigns architecture only', 'No social content library'],
    'next_recommended': 31,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/outreach.html',
    'review_status': 'complete'
})

mc['briefing'] = {
    'what_built': f'Outreach Engine v1.0 — {s["pillars"]} pillars, {s["campaigns"]} campaigns, Arkansas county outreach',
    'building_now': 'Public engagement architecture — component specs next',
    'blocked': ['No analytics integration', 'Campaign management not built', 'Social library planned'],
    'ready_public': ['Outreach MC dashboard', 'Pillar + campaign map', 'Share toolkit schema', 'County outreach profile'],
    'next': 'Build #31 — Component specifications with props/states'
}

if not any(n.get('id') == 'outreach_engine' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'outreach_engine', 'label': 'Outreach Engine', 'href': '/mission-control/outreach.html', 'status': 'complete'
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
