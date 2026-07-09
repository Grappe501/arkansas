import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json') as f:
    mc = json.load(f)

title = 'Citizens United Facts Master Civic Action Lab'

with open(root / 'data/civic-action-lab.json') as f:
    lab = json.load(f)

s = lab['summary']

mc['version'] = '1.46.0'
mc['build'] = 42
mc['updated'] = '2026-07-09'
mc['civic_action_lab'] = '/data/civic-action-lab.json'
mc['civic_action_lab_dashboard'] = '/mission-control/civic-action-lab.html'

mc['executive'] = {
    'overall_completion': 42,
    'current_build': {'number': 42, 'title': title},
    'active_phase': 'Civic Participation — Master Civic Action Lab',
    'last_completed': 'Master Evidence Ledger & Claims Registry',
    'next_build': {'number': 43, 'title': 'Component specifications with props/states'},
    'github_status': 'connected',
    'netlify_status': 'production_healthy',
    'content_readiness': 26,
    'research_readiness': 28,
    'data_viz_readiness': 6,
    'signup_funnel_readiness': 22,
    'civic_action_readiness': s['civic_action_lab_readiness_pct'],
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
    'evidence_ledger_readiness': 22,
    'civic_action_lab_readiness': s['civic_action_lab_readiness_pct'],
    'public_launch_readiness': 8,
    'public_launch_label': 'Early Foundation'
}

mc['civic_action_lab_inventory'] = {
    'readiness_score': s['civic_action_lab_readiness_pct'],
    'divisions_total': s['divisions_total'],
    'divisions_partial': s['divisions_partial'],
    'comparative_studies_live': s['comparative_studies_live'],
    'guided_draft_builder_live': s['guided_draft_builder_live'],
    'submission_tracking_live': s['submission_tracking_live'],
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 42
        bar['note'] = f"Civic Action Lab live — 6 divisions, {s['comparative_studies_live']} comparative studies."
    if bar['id'] == 'evidence_ledger':
        bar['value'] = 22
        bar['note'] = 'Evidence Ledger — 3/500 CLAIM-* records.'

if not any(b.get('id') == 'civic_action_lab' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'civic_action_lab',
        'label': 'Master Civic Action Lab',
        'value': s['civic_action_lab_readiness_pct'],
        'max': 100,
        'note': f"{s['divisions_partial']}/6 divisions partial — no guided draft builder."
    })
else:
    for bar in mc['progress_bars']:
        if bar['id'] == 'civic_action_lab':
            bar['value'] = s['civic_action_lab_readiness_pct']
            bar['note'] = f"{s['divisions_partial']}/6 divisions partial."

mc['builds'].insert(0, {
    'number': 42,
    'title': title,
    'version': '1.46.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Civic Solutions & Ballot Initiative Architecture v1.0 — educate first bridge to participation',
    'summary': f"6 divisions, {s['comparative_studies_live']} live comparisons; {s['civic_action_lab_readiness_pct']}% overall.",
    'files_created': [
        'data/civic-action-lab.json', 'docs/MASTER_CIVIC_ACTION_LAB.md',
        'builds/042-master-civic-action-lab.md', 'mission-control/civic-action-lab.html',
        'scripts/gen-civic-action-lab.py', 'scripts/update-mc-build42.py'
    ],
    'files_modified': ['js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml'],
    'pages_created': ['/mission-control/civic-action-lab.html'],
    'decisions_made': [
        '6 lab divisions — federal through community review panels',
        'Learn→Share philosophy — every stage on verified information',
        'Not campaign HQ — educational laboratory only',
        'Solutions hub + action pages as interim workspaces',
        'MT/HI as live comparative reform examples',
        f"{s['civic_action_lab_readiness_pct']}% honest readiness — draft builder not guided"
    ],
    'open_questions': ['First Arkansas ballot initiative educational draft?', 'Review panel recruitment?', 'Form integration for submissions?'],
    'risks': ['Submission counts at 0', 'Community review panels planned', 'Arkansas legislative library empty'],
    'next_recommended': 43,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/civic-action-lab.html',
    'review_status': 'complete'
})

mc['briefing'] = {
    'what_built': 'Civic Action Lab v1.0 — 6 divisions, legislative tracker, draft builder schema, MC metrics',
    'building_now': 'Solutions hub and action pages as interim — MT/HI comparisons live',
    'blocked': ['Guided draft builder', 'Community review panels', 'Submission tracking'],
    'ready_public': ['Civic Action Lab MC dashboard', '6-division taxonomy', 'Public official center link'],
    'next': 'Build #43 — Component specifications with props/states'
}

if not any(n.get('id') == 'civic_action_lab' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'civic_action_lab', 'label': 'Master Civic Action Lab', 'href': '/mission-control/civic-action-lab.html', 'status': 'complete'
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
