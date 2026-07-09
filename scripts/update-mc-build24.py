import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json') as f:
    mc = json.load(f)

title = 'Contact Intelligence & Community Relationship Architecture'

with open(root / 'data/contact-intelligence.json') as f:
    ci = json.load(f)

s = ci['summary']

mc['version'] = '1.28.0'
mc['build'] = 24
mc['updated'] = '2026-07-09'
mc['contact_intelligence'] = '/data/contact-intelligence.json'
mc['contact_intelligence_dashboard'] = '/mission-control/contact-intelligence.html'

mc['executive'] = {
    'overall_completion': 24,
    'current_build': {'number': 24, 'title': title},
    'active_phase': 'Implementation Artifacts — Contact Intelligence',
    'last_completed': 'Major Screen Wireframe Blueprint',
    'next_build': {'number': 25, 'title': 'GitHub issues, milestones, and sprint roadmap'},
    'github_status': 'connected',
    'netlify_status': 'production_healthy',
    'content_readiness': 18,
    'research_readiness': 20,
    'data_viz_readiness': 2,
    'signup_funnel_readiness': 18,
    'civic_action_readiness': 26,
    'coalition_readiness': 14,
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
    'public_launch_readiness': 8,
    'public_launch_label': 'Early Foundation'
}

mc['contact_intelligence_inventory'] = {
    'readiness_score': s['contact_intelligence_readiness_pct'],
    'modules': s['modules'],
    'fields_total': s['fields_total'],
    'interest_topics': s['interest_topics'],
    'skills_defined': s['skills_defined'],
    'mc_metrics_defined': s['mc_metrics_defined'],
    'integrations_mapped': s['integrations_mapped'],
    'by_status': s['by_status']
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 24
        bar['note'] = f"Contact intelligence live — {s['modules']} modules, {s['interest_topics']} interest topics. Sprint roadmap next."

if not any(b.get('id') == 'contact_intelligence' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'contact_intelligence',
        'label': 'Contact Intelligence',
        'value': 31,
        'max': 100,
        'note': f"{s['implementation_partial']} modules schema/partial, {s['implementation_planned']} planned — no backend yet."
    })

mc['builds'].insert(0, {
    'number': 24,
    'title': title,
    'version': '1.28.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Arkansas Community Intelligence System v1.0 — educational relationship network architecture',
    'summary': f"{s['modules']} modules, {s['fields_total']} fields, {s['interest_topics']} interests, {s['skills_defined']} skills; {s['contact_intelligence_readiness_pct']}% readiness.",
    'files_created': [
        'data/contact-intelligence.json', 'docs/CONTACT_INTELLIGENCE.md',
        'builds/024-contact-intelligence.md', 'mission-control/contact-intelligence.html',
        'scripts/gen-contact-intelligence.py', 'scripts/update-mc-build24.py'
    ],
    'files_modified': ['js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml'],
    'pages_created': ['/mission-control/contact-intelligence.html'],
    'decisions_made': [
        '14 intelligence modules: profile, interests, skills, connections, org, county, events, referrals, officials, research, comms, privacy, metrics, integrations',
        'Privacy-first: collect only for educational mission; never sell data',
        'Maps to database schema entities from Build #22',
        '31% honest readiness — architecture defined, forms/backend not integrated',
        'Component specs deferred to post-#25 sprint work'
    ],
    'open_questions': ['Supabase vs Neon for v2?', 'When to add interest/skills to signup forms?'],
    'risks': ['31% readiness — tracking mostly manual', 'No participant self-service profile update'],
    'next_recommended': 25,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/contact-intelligence.html',
    'review_status': 'complete'
})

mc['briefing'] = {
    'what_built': f'Contact Intelligence v1.0 — {s["modules"]} modules defining Arkansas educational relationship network',
    'building_now': 'Implementation artifacts — GitHub sprint roadmap next (Build #25)',
    'blocked': ['No backend database', 'Referral tracking not integrated', 'MC metrics mostly manual'],
    'ready_public': ['Contact Intelligence MC dashboard', 'Interest/skills taxonomies', 'Privacy principles', 'Integration map'],
    'next': 'Build #25 — GitHub issues, milestones, and sprint roadmap'
}

if not any(n.get('id') == 'contact_intelligence' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'contact_intelligence', 'label': 'Contact Intelligence', 'href': '/mission-control/contact-intelligence.html', 'status': 'complete'
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
