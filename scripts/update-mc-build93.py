import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json', encoding='utf-8') as f:
    mc = json.load(f)

title = 'Citizens United Facts Master Arkansas Civic Data Warehouse & Knowledge Platform v1.0'

with open(root / 'data/civic-knowledge-platform.json', encoding='utf-8') as f:
    ckp = json.load(f)

s = ckp['summary']
prior_maturity = mc.get('executive', {}).get('institutional_maturity_pct', 32)

mc['version'] = '1.97.0'
mc['build'] = 93
mc['updated'] = '2026-07-09'
mc['civic_knowledge_platform'] = '/data/civic-knowledge-platform.json'
mc['civic_knowledge_platform_dashboard'] = '/mission-control/civic-knowledge-platform.html'

mc['executive'] = {
    'overall_completion': 93,
    'current_build': {'number': 93, 'title': title},
    'active_phase': 'Knowledge Platform → War Room',
    'last_completed': 'LocalBrain Architecture',
    'next_build': {'number': 94, 'title': 'Executive war room & countdown dashboard components'},
    'github_status': 'connected',
    'netlify_status': 'production_healthy',
    'content_readiness': 28,
    'research_readiness': mc.get('executive', {}).get('research_readiness', 43),
    'data_viz_readiness': 12,
    'signup_funnel_readiness': 26,
    'civic_action_readiness': 28,
    'coalition_readiness': 44,
    'data_model_readiness': max(s['civic_knowledge_platform_readiness_pct'], mc.get('executive', {}).get('data_model_readiness', 54)),
    'route_inventory_readiness': 18,
    'component_registry_readiness': 22,
    'facts_framework_readiness': 14,
    'knowledge_atlas_readiness': max(s['civic_knowledge_platform_readiness_pct'], mc.get('executive', {}).get('knowledge_atlas_readiness', 20)),
    'platform_architecture_readiness': 24,
    'repository_structure_readiness': 28,
    'database_schema_readiness': 42,
    'wireframe_readiness': 38,
    'contact_intelligence_readiness': 34,
    'relationship_os_readiness': mc.get('executive', {}).get('relationship_os_readiness', 54),
    'institutional_ai_readiness': mc.get('executive', {}).get('institutional_ai_readiness', 57),
    'ai_institution_readiness': mc.get('executive', {}).get('ai_institution_readiness', 57),
    'localbrain_architecture_readiness': mc.get('executive', {}).get('localbrain_architecture_readiness', 60),
    'civic_knowledge_platform_readiness': s['civic_knowledge_platform_readiness_pct'],
    'coalition_network_readiness': 44,
    'citizen_action_center_readiness': 42,
    'campaign_finance_observatory_readiness': mc.get('executive', {}).get('campaign_finance_observatory_readiness', 38),
    'arkansas_action_network_readiness': 38,
    'civic_intelligence_command_center_readiness': 43,
    'sustainability_stewardship_readiness': mc.get('executive', {}).get('sustainability_stewardship_readiness', 38),
    'impact_measurement_readiness': 31,
    'citizen_leadership_academy_readiness': 34,
    'relational_organizing_growth_engine_readiness': mc.get('executive', {}).get('relational_organizing_growth_engine_readiness', 34),
    'arkansas_command_strategy_readiness': mc.get('executive', {}).get('arkansas_command_strategy_readiness', 39),
    'arkansas_community_listening_readiness': mc.get('executive', {}).get('arkansas_community_listening_readiness', 41),
    'arkansas_communications_readiness': mc.get('executive', {}).get('arkansas_communications_readiness', 42),
    'arkansas_research_institute_readiness': mc.get('executive', {}).get('arkansas_research_institute_readiness', 43),
    'arkansas_civic_innovation_reform_readiness': mc.get('executive', {}).get('arkansas_civic_innovation_reform_readiness', 44),
    'volunteer_funding_constitution_readiness': mc.get('executive', {}).get('volunteer_funding_constitution_readiness', 45),
    'organizational_constitution_readiness': mc.get('executive', {}).get('organizational_constitution_readiness', 46),
    'arkansas_county_operating_system_readiness': mc.get('executive', {}).get('arkansas_county_operating_system_readiness', 47),
    'arkansas_city_operating_system_readiness': mc.get('executive', {}).get('arkansas_city_operating_system_readiness', 48),
    'arkansas_neighborhood_operating_system_readiness': mc.get('executive', {}).get('arkansas_neighborhood_operating_system_readiness', 47),
    'arkansas_civic_institution_roadmap_readiness': mc.get('executive', {}).get('arkansas_civic_institution_roadmap_readiness', 48),
    'institutional_digital_twin_readiness': mc.get('executive', {}).get('institutional_digital_twin_readiness', 51),
    'public_trust_institutional_credibility_readiness': mc.get('executive', {}).get('public_trust_institutional_credibility_readiness', 50),
    'arkansas_civic_ecosystem_readiness': mc.get('executive', {}).get('arkansas_civic_ecosystem_readiness', 54),
    'arkansas_strategic_plan_2035_readiness': mc.get('executive', {}).get('arkansas_strategic_plan_2035_readiness', 55),
    'master_launch_plan_readiness': mc.get('executive', {}).get('master_launch_plan_readiness', 54),
    'arkansas_civic_reach_participation_readiness': mc.get('executive', {}).get('arkansas_civic_reach_participation_readiness', 56),
    'launch_campaign_first_100_days_readiness': mc.get('executive', {}).get('launch_campaign_first_100_days_readiness', 57),
    'execution_schedule_readiness': mc.get('executive', {}).get('execution_schedule_readiness', 56),
    'pmo_execution_office_readiness': mc.get('executive', {}).get('pmo_execution_office_readiness', 60),
    'institutional_operating_manual_readiness': mc.get('executive', {}).get('institutional_operating_manual_readiness', 60),
    'mc2_readiness': 42,
    'ai_engine_readiness': mc.get('executive', {}).get('ai_engine_readiness', 57),
    'content_factory_readiness': 30,
    'education_academy_readiness': 26,
    'observatory_readiness': mc.get('executive', {}).get('observatory_readiness', 43),
    'outreach_readiness': mc.get('executive', {}).get('outreach_readiness', 44),
    'county_os_readiness': mc.get('executive', {}).get('county_os_readiness', 28),
    'campaign_os_readiness': mc.get('executive', {}).get('campaign_os_readiness', 44),
    'encyclopedia_readiness': 19,
    'narrative_readiness': 24,
    'curriculum_readiness': 26,
    'trust_readiness': mc.get('executive', {}).get('trust_readiness', 50),
    'library_readiness': 22,
    'learning_lab_readiness': 22,
    'media_studio_readiness': 18,
    'civic_intelligence_readiness': 36,
    'evidence_ledger_readiness': 22,
    'civic_action_lab_readiness': 26,
    'research_methodology_readiness': mc.get('executive', {}).get('research_methodology_readiness', 29),
    'institutional_maturity_pct': prior_maturity,
    'current_institutional_version': 'V1',
    'systems_integration_readiness': mc.get('executive', {}).get('systems_integration_readiness', 44),
    'production_matrix_readiness': 39,
    'visitor_journey_readiness': 40,
    'technical_architecture_readiness': 38,
    'governance_readiness': mc.get('executive', {}).get('governance_readiness', 46),
    'build_bible_readiness': 49,
    'data_architecture_readiness': max(s['civic_knowledge_platform_readiness_pct'], mc.get('executive', {}).get('data_architecture_readiness', 41)),
    'ux_architecture_readiness': 39,
    'launch_strategy_readiness': mc.get('executive', {}).get('launch_strategy_readiness', 44),
    'pmo_readiness': mc.get('executive', {}).get('pmo_readiness', 60),
    'master_plan_readiness': mc.get('executive', {}).get('master_plan_readiness', 56),
    'statewide_growth_readiness': mc.get('executive', {}).get('statewide_growth_readiness', 48),
    'neighborhood_organizing_readiness': mc.get('executive', {}).get('neighborhood_organizing_readiness', 50),
    'civic_atlas_readiness': 52,
    'rollout_phase': 0,
    'rollout_phase_title': 'Private Development',
    'planning_phase_complete': True,
    'planning_constitution_complete': True,
    'eighty_builds_complete': True,
    'implementation_phase': 'executive_war_room_next',
    'public_launch_readiness': mc.get('executive', {}).get('public_launch_readiness', 8),
    'public_launch_label': 'Early Foundation',
    'public_launch_recommended': False,
    'completion_target_date': s['completion_target_date'],
    'days_remaining_to_completion': s['days_remaining'],
    'mission_complete_label': 'Mission Complete — January 2027',
    'connected_citizen_goal_pct': mc.get('executive', {}).get('connected_citizen_goal_pct', 15),
}

mc['civic_knowledge_platform_inventory'] = {
    'readiness_score': s['civic_knowledge_platform_readiness_pct'],
    'unified_search_live': s['unified_search_live'],
    'platform_dashboard_live': s['platform_dashboard_live'],
    'canonical_records_enforced': s['canonical_records_enforced'],
    'knowledge_gaps_identified': s['knowledge_gaps_identified'],
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 93
        bar['note'] = f"Build #93 — Knowledge Platform. {s['days_remaining']} days to Jan 2027."
    if bar.get('id') == 'localbrain_architecture':
        bar['note'] = f"LocalBrains read from platform · search {'live' if s['unified_search_live'] else 'planned'}."

if not any(b.get('id') == 'civic_knowledge_platform' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'civic_knowledge_platform',
        'label': 'Knowledge Platform',
        'value': s['civic_knowledge_platform_readiness_pct'],
        'max': 100,
        'note': f"Unified search {'live' if s['unified_search_live'] else 'planned'} · {s['knowledge_gaps_identified']} gaps.",
    })
else:
    for bar in mc['progress_bars']:
        if bar['id'] == 'civic_knowledge_platform':
            bar['value'] = s['civic_knowledge_platform_readiness_pct']

mc['builds'].insert(0, {
    'number': 93,
    'title': title,
    'version': '1.97.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'One source of truth — institutional intelligence backbone',
    'summary': (
        f"4 layers, 11 structured data types, canonical records, version control, unified search, "
        f"knowledge lifecycle, data governance, executive intelligence. "
        f"{s['civic_knowledge_platform_readiness_pct']}% readiness · "
        f"search {'live' if s['unified_search_live'] else 'not live'} · "
        f"warehouse not unified."
    ),
    'files_created': [
        'data/civic-knowledge-platform.json',
        'docs/MASTER_CIVIC_DATA_WAREHOUSE_KNOWLEDGE_PLATFORM.md',
        'builds/093-civic-knowledge-platform.md',
        'mission-control/civic-knowledge-platform.html',
        'scripts/gen-civic-knowledge-platform.py',
        'scripts/update-mc-build93.py',
    ],
    'files_modified': [
        'js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml',
    ],
    'pages_created': ['/mission-control/civic-knowledge-platform.html'],
    'decisions_made': [
        'One source of truth — exist once, maintain once',
        'Four layers: structured data, knowledge, relationship graph, intelligence',
        'Canonical records — everything references authoritative record',
        'Knowledge lifecycle Draft → Historical Record',
        'Data governance + access levels per record',
        f"{s['civic_knowledge_platform_readiness_pct']}% readiness — blueprint only",
    ],
    'open_questions': [
        'Warehouse DB — Neon/Postgres vs unified JSON layer?',
        'Canonical ID scheme — MRID extension?',
        'Unified search — Elasticsearch or MC client-side?',
        'When do JSON registries migrate to warehouse?',
    ],
    'risks': ckp['catalog_gaps'][:4],
    'next_recommended': 94,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/civic-knowledge-platform.html',
    'review_status': 'complete',
})

mc['briefing'] = {
    'what_built': 'Civic Data Warehouse & Knowledge Platform v1.0 — One Source of Truth',
    'building_now': '93 builds — executive war room next',
    'blocked': ['Unified warehouse', 'Unified search', 'Canonical enforcement', 'Platform dashboard'],
    'ready_public': ['Four layers', 'Canonical model', 'Lifecycle', 'Governance fields'],
    'next': 'Build #94 — Executive war room & countdown dashboard components',
}

if not any(n.get('id') == 'civic_knowledge_platform' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'civic_knowledge_platform',
        'label': 'Knowledge Platform',
        'href': '/mission-control/civic-knowledge-platform.html',
        'status': 'complete',
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
