import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json') as f:
    mc = json.load(f)

title = 'Citizens United Facts Educational Campaign Operating System'

with open(root / 'data/educational-campaign-operating-system.json') as f:
    ecos = json.load(f)

s = ecos['summary']
ch = ecos['current_horizon']

mc['version'] = '1.36.0'
mc['build'] = 32
mc['updated'] = '2026-07-09'
mc['educational_campaign_operating_system'] = '/data/educational-campaign-operating-system.json'
mc['campaign_os_dashboard'] = '/mission-control/campaign-os.html'

mc['executive'] = {
    'overall_completion': 32,
    'current_build': {'number': 32, 'title': title},
    'active_phase': 'Multi-Year Strategic Growth — Horizon One: Build the Institution',
    'last_completed': 'Arkansas County Operating System',
    'next_build': {'number': 33, 'title': 'Component specifications with props/states'},
    'github_status': 'connected',
    'netlify_status': 'production_healthy',
    'content_readiness': 20,
    'research_readiness': 22,
    'data_viz_readiness': 2,
    'signup_funnel_readiness': 22,
    'civic_action_readiness': 32,
    'coalition_readiness': 18,
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
    'county_os_readiness': 28,
    'campaign_os_readiness': s['campaign_os_readiness_pct'],
    'public_launch_readiness': 8,
    'public_launch_label': 'Early Foundation'
}

mc['campaign_os_inventory'] = {
    'readiness_score': s['campaign_os_readiness_pct'],
    'current_horizon': s['current_horizon'],
    'horizons_total': s['horizons_total'],
    'horizon_one_objectives_pct': s['horizon_one_objectives_pct'],
    'success_indicators_met': s['success_indicators_met'],
    'success_indicators_total': s['success_indicators_total'],
    'quarterly_reports_live': s['quarterly_reports_live'],
    'innovation_queue_live': s['innovation_queue_live'],
    'annual_summit_live': s['annual_summit_live'],
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 32
        bar['note'] = f"Campaign OS live — Horizon {s['current_horizon']} active, {s['success_indicators_met']}/{s['success_indicators_total']} H1 indicators met."

if not any(b.get('id') == 'campaign_os' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'campaign_os',
        'label': 'Educational Campaign OS',
        'value': s['campaign_os_readiness_pct'],
        'max': 100,
        'note': f"Horizon One at {s['horizon_one_objectives_pct']}% — master roadmap defined, engagement metrics at zero."
    })

mc['builds'].insert(0, {
    'number': 32,
    'title': title,
    'version': '1.36.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Multi-Year Strategic Growth Blueprint v1.0 — institution over project',
    'summary': f"4 horizons, {s['annual_seasons']}-season cycle, {s['quarterly_topics']} quarterly topics; Horizon 1 at {s['horizon_one_objectives_pct']}%; {s['campaign_os_readiness_pct']}% readiness.",
    'files_created': [
        'data/educational-campaign-operating-system.json', 'docs/EDUCATIONAL_CAMPAIGN_OPERATING_SYSTEM.md',
        'builds/032-educational-campaign-operating-system.md', 'mission-control/campaign-os.html',
        'scripts/gen-educational-campaign-operating-system.py', 'scripts/update-mc-build32.py'
    ],
    'files_modified': ['js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml'],
    'pages_created': ['/mission-control/campaign-os.html'],
    'decisions_made': [
        '4 strategic horizons — no horizon complete until objectives achieved',
        'Horizon One active: Build the Institution',
        'Annual operating cycle: Winter/Spring/Summer/Fall',
        '8 quarterly review topics — reports planned, not automated',
        '7 innovation pipeline categories — queue not built',
        '7 strategic risks with 2 active (county participation, coalition inactivity)',
        '34% honest readiness — roadmap live, engagement at zero'
    ],
    'open_questions': ['Horizon transition criteria?', 'When to schedule first annual summit?'],
    'risks': ['0 coalition orgs', '0 Education Leaders', 'Quarterly reports not automated'],
    'next_recommended': 33,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/campaign-os.html',
    'review_status': 'complete'
})

mc['briefing'] = {
    'what_built': f'Campaign OS v1.0 — 4 horizons, annual cycle, quarterly framework, innovation & risk architecture',
    'building_now': 'Horizon One — Build the Institution (3/5 success indicators met)',
    'blocked': ['0 coalition organizations', '0 Education Leaders enrolled', 'Quarterly reports not automated'],
    'ready_public': ['Campaign OS MC dashboard', '4-horizon roadmap', 'Annual cycle', 'Institutional memory links'],
    'next': 'Build #33 — Component specifications with props/states'
}

if not any(n.get('id') == 'campaign_os' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'campaign_os', 'label': 'Educational Campaign OS', 'href': '/mission-control/campaign-os.html', 'status': 'complete'
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
