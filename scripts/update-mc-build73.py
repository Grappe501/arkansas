import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json', encoding='utf-8') as f:
    mc = json.load(f)

title = 'Citizens United Facts Master Research Institute & Arkansas Policy Innovation Laboratory v1.0'

with open(root / 'data/arkansas-research-institute.json', encoding='utf-8') as f:
    ari = json.load(f)

s = ari['summary']
prior_maturity = mc.get('executive', {}).get('institutional_maturity_pct', 32)

mc['version'] = '1.77.0'
mc['build'] = 73
mc['updated'] = '2026-07-09'
mc['arkansas_research_institute'] = '/data/arkansas-research-institute.json'
mc['arkansas_research_institute_dashboard'] = '/mission-control/arkansas-research-institute.html'

mc['executive'] = {
    'overall_completion': 73,
    'current_build': {'number': 73, 'title': title},
    'active_phase': 'Research Institute → Implementation Translation',
    'last_completed': 'Arkansas Communications',
    'next_build': {'number': 74, 'title': 'Implementation translation layer & engineering artifacts'},
    'github_status': 'connected',
    'netlify_status': 'production_healthy',
    'content_readiness': 28,
    'research_readiness': max(s['arkansas_research_institute_readiness_pct'], s['research_observatory_readiness_pct']),
    'data_viz_readiness': 12,
    'signup_funnel_readiness': 26,
    'civic_action_readiness': 28,
    'coalition_readiness': 44,
    'data_model_readiness': 54,
    'route_inventory_readiness': 18,
    'component_registry_readiness': 22,
    'facts_framework_readiness': 14,
    'knowledge_atlas_readiness': 20,
    'platform_architecture_readiness': 24,
    'repository_structure_readiness': 28,
    'database_schema_readiness': 42,
    'wireframe_readiness': 38,
    'contact_intelligence_readiness': 34,
    'relationship_os_readiness': mc.get('executive', {}).get('relationship_os_readiness', 54),
    'institutional_ai_readiness': 42,
    'coalition_network_readiness': 44,
    'citizen_action_center_readiness': 42,
    'campaign_finance_observatory_readiness': max(s['campaign_finance_observatory_readiness_pct'], s['arkansas_research_institute_readiness_pct'] - 6),
    'arkansas_action_network_readiness': 38,
    'civic_intelligence_command_center_readiness': 43,
    'sustainability_stewardship_readiness': 38,
    'impact_measurement_readiness': 31,
    'citizen_leadership_academy_readiness': 34,
    'relational_organizing_growth_engine_readiness': mc.get('executive', {}).get('relational_organizing_growth_engine_readiness', 34),
    'arkansas_command_strategy_readiness': mc.get('executive', {}).get('arkansas_command_strategy_readiness', 39),
    'arkansas_community_listening_readiness': mc.get('executive', {}).get('arkansas_community_listening_readiness', 41),
    'arkansas_communications_readiness': mc.get('executive', {}).get('arkansas_communications_readiness', 42),
    'arkansas_research_institute_readiness': s['arkansas_research_institute_readiness_pct'],
    'mc2_readiness': 42,
    'ai_engine_readiness': 34,
    'content_factory_readiness': 30,
    'education_academy_readiness': 26,
    'observatory_readiness': max(s['research_observatory_readiness_pct'], s['arkansas_research_institute_readiness_pct']),
    'outreach_readiness': 34,
    'county_os_readiness': 28,
    'campaign_os_readiness': 34,
    'encyclopedia_readiness': 19,
    'narrative_readiness': 24,
    'curriculum_readiness': 26,
    'trust_readiness': 30,
    'library_readiness': max(22, s['arkansas_research_institute_readiness_pct'] - 18),
    'learning_lab_readiness': 22,
    'media_studio_readiness': 18,
    'civic_intelligence_readiness': 36,
    'evidence_ledger_readiness': max(22, s['arkansas_research_institute_readiness_pct'] - 16),
    'civic_action_lab_readiness': 26,
    'research_methodology_readiness': max(25, s['arkansas_research_institute_readiness_pct'] - 14),
    'institutional_maturity_pct': prior_maturity,
    'current_institutional_version': 'V1',
    'systems_integration_readiness': 44,
    'production_matrix_readiness': 39,
    'visitor_journey_readiness': 40,
    'technical_architecture_readiness': 38,
    'governance_readiness': 44,
    'build_bible_readiness': 49,
    'data_architecture_readiness': 41,
    'ux_architecture_readiness': 39,
    'launch_strategy_readiness': 39,
    'pmo_readiness': 46,
    'master_plan_readiness': 56,
    'statewide_growth_readiness': mc.get('executive', {}).get('statewide_growth_readiness', 48),
    'neighborhood_organizing_readiness': 50,
    'civic_atlas_readiness': 52,
    'rollout_phase': 0,
    'rollout_phase_title': 'Private Development',
    'planning_phase_complete': True,
    'planning_constitution_complete': True,
    'implementation_phase': 'translation_layer_next',
    'public_launch_readiness': s['public_launch_readiness_pct'],
    'public_launch_label': 'Early Foundation',
    'public_launch_recommended': False,
}

mc['arkansas_research_institute_inventory'] = {
    'readiness_score': s['arkansas_research_institute_readiness_pct'],
    'research_projects_underway': s['research_projects_underway'],
    'divisions_total': s['research_divisions'],
    'permanent_pillar': True,
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 73
        bar['note'] = 'Build #73 — Research Institute & Policy Innovation Laboratory.'
    if bar['id'] == 'research':
        bar['value'] = s['arkansas_research_institute_readiness_pct']
        bar['note'] = (
            f"Research institute — {s['research_projects_underway']} projects · "
            f"{s['divisions_operational']}/{s['research_divisions']} divisions operational."
        )

if not any(b.get('id') == 'arkansas_research_institute' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'arkansas_research_institute',
        'label': 'Research Institute',
        'value': s['arkansas_research_institute_readiness_pct'],
        'max': 100,
        'note': f"{s['completed_white_papers']} white papers · dashboard {'live' if s['research_dashboard_live'] else 'planned'}.",
    })
else:
    for bar in mc['progress_bars']:
        if bar['id'] == 'arkansas_research_institute':
            bar['value'] = s['arkansas_research_institute_readiness_pct']

mc['builds'].insert(0, {
    'number': 73,
    'title': title,
    'version': '1.77.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Research Institute & Policy Innovation Lab — expand knowledge not certainty',
    'summary': (
        f"Eight divisions, research standards, review workflow, repository, policy lab; "
        f"{s['arkansas_research_institute_readiness_pct']}% readiness. "
        f"0 projects · 0 white papers · 0/8 divisions operational."
    ),
    'files_created': [
        'data/arkansas-research-institute.json',
        'docs/MASTER_ARKANSAS_RESEARCH_INSTITUTE.md',
        'builds/073-arkansas-research-institute.md',
        'mission-control/arkansas-research-institute.html',
        'scripts/gen-arkansas-research-institute.py',
        'scripts/update-mc-build73.py',
    ],
    'files_modified': ['js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml'],
    'pages_created': ['/mission-control/arkansas-research-institute.html'],
    'decisions_made': [
        'Permanent institutional pillar — not advocacy for predetermined answers',
        'Eight divisions including Policy Innovation Lab and Future Trends Observatory',
        'Research standards: 8 required elements per publication',
        'Six-stage review: research through scheduled review',
        'Distinguish facts, viewpoints, and policy proposals',
        'Expand knowledge not certainty — teach evidence evaluation',
        f"{s['arkansas_research_institute_readiness_pct']}% readiness — constitution only",
    ],
    'open_questions': [
        'Reconcile Research Institute (#73) vs Research Observatory (#29)?',
        'Policy Innovation Lab: public draft workspace or internal only?',
        'Peer review: internal board vs external scholars?',
        'Knowledge Graph: auto-link research or manual curation?',
    ],
    'risks': ari['catalog_gaps'][:4],
    'next_recommended': 74,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/arkansas-research-institute.html',
    'review_status': 'complete',
})

mc['briefing'] = {
    'what_built': 'Arkansas Research Institute v1.0 — civic research & policy innovation lab',
    'building_now': '73 builds specified — implementation translation next',
    'blocked': ['Research pipeline', 'Division pages', 'Policy lab UI', 'Repository'],
    'ready_public': ['Eight divisions', 'Research standards', 'Review workflow spec', 'Mission topics'],
    'next': 'Build #74 — Implementation translation layer & engineering artifacts',
}

if not any(n.get('id') == 'arkansas_research_institute' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'arkansas_research_institute',
        'label': 'Research Institute',
        'href': '/mission-control/arkansas-research-institute.html',
        'status': 'complete',
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
