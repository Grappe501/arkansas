import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json', encoding='utf-8') as f:
    mc = json.load(f)

title = 'Citizens United Facts Master Visitor Journey & Behavioral Architecture'

with open(root / 'data/visitor-journey.json', encoding='utf-8') as f:
    vj = json.load(f)

s = vj['summary']

mc['version'] = '1.51.0'
mc['build'] = 47
mc['updated'] = '2026-07-09'
mc['visitor_journey'] = '/data/visitor-journey.json'
mc['visitor_journey_dashboard'] = '/mission-control/visitor-journey.html'

mc['executive'] = {
    'overall_completion': 47,
    'current_build': {'number': 47, 'title': title},
    'active_phase': 'Behavioral Architecture — Visitor Transformation Model',
    'last_completed': 'Master Content Production Matrix',
    'next_build': {'number': 48, 'title': 'Component specifications with props/states'},
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
    'platform_architecture_readiness': 20,
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
    'visitor_journey_readiness': s['visitor_journey_readiness_pct'],
    'public_launch_readiness': 8,
    'public_launch_label': 'Early Foundation'
}

mc['visitor_journey_inventory'] = {
    'readiness_score': s['visitor_journey_readiness_pct'],
    'stages_total': s['stages_total'],
    'stages_with_live_tracking': s['stages_with_live_tracking'],
    'education_leader_signups': s['education_leader_signups'],
    'milestones_defined': s['milestones_defined'],
    'journey_analytics_live': s['journey_analytics_live'],
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 47
        bar['note'] = f"Visitor Journey live — 8 stages, {s['stages_with_live_tracking']} tracked, {s['education_leader_signups']} leaders."
    if bar['id'] == 'institutional_maturity':
        bar['value'] = 32
        bar['note'] = 'Institutional maturity V1 — 32% overall.'

if not any(b.get('id') == 'visitor_journey' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'visitor_journey',
        'label': 'Visitor Journey & Behavioral Architecture',
        'value': s['visitor_journey_readiness_pct'],
        'max': 100,
        'note': f"{s['stages_with_live_tracking']}/8 stages tracked — localStorage only."
    })
else:
    for bar in mc['progress_bars']:
        if bar['id'] == 'visitor_journey':
            bar['value'] = s['visitor_journey_readiness_pct']
            bar['note'] = f"{s['stages_with_live_tracking']}/8 stages tracked."

mc['builds'].insert(0, {
    'number': 47,
    'title': title,
    'version': '1.51.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': '8-stage transformation model — curious visitor to community educator',
    'summary': f"8 stages, {s['stages_with_live_tracking']} tracked, {s['milestones_defined']} milestones; {s['visitor_journey_readiness_pct']}% readiness.",
    'files_created': [
        'data/visitor-journey.json', 'docs/MASTER_VISITOR_JOURNEY.md',
        'builds/047-master-visitor-journey-behavioral-architecture.md',
        'mission-control/visitor-journey.html',
        'scripts/gen-visitor-journey.py', 'scripts/update-mc-build47.py'
    ],
    'files_modified': ['js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml'],
    'pages_created': ['/mission-control/visitor-journey.html'],
    'decisions_made': [
        '8 transformation stages — Curiosity through Legacy',
        'Extends Build #8 7-stage ladder — mapping documented',
        '8-role journey map — Visitors through Mentors',
        '8 decision points — gentle invitations, no pressure',
        '7 motivation milestones — learning/service recognition',
        f"{s['stages_with_live_tracking']}/8 stages tracked — localStorage session memory only",
        f"{s['visitor_journey_readiness_pct']}% honest readiness — analytics and signups at zero"
    ],
    'open_questions': ['Server-side journey sync timing?', 'Netlify analytics for return rate?', 'Milestone celebration UI?'],
    'risks': ['0 signups breaks connection→leadership funnel', 'Two journey models may confuse editors', 'No lesson completion tracking'],
    'next_recommended': 48,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/visitor-journey.html',
    'review_status': 'complete'
})

mc['briefing'] = {
    'what_built': 'Visitor Journey v1.0 — 8 stages, journey map, decision points, motivation milestones',
    'building_now': 'Build #8 mapping — localStorage tracking on curiosity stage only',
    'blocked': ['Journey analytics', 'Milestone tracking', 'Education Leader signups'],
    'ready_public': ['Visitor Journey MC dashboard', '8-stage transformation model', 'Behavioral principles'],
    'next': 'Build #48 — Component specifications with props/states'
}

if not any(n.get('id') == 'visitor_journey' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'visitor_journey', 'label': 'Visitor Journey & Behavioral Architecture', 'href': '/mission-control/visitor-journey.html', 'status': 'complete'
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
