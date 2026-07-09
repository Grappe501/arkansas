import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json') as f:
    mc = json.load(f)

mc['version'] = '1.14.0'
mc['build'] = 10
mc['updated'] = '2026-07-09'
mc['research_framework'] = '/data/research-framework.json'
mc['evidence_registry'] = '/data/evidence-registry.json'
mc['research_route'] = '/mission-control/research.html'

mc['executive'] = {
    'overall_completion': 10,
    'current_build': {'number': 10, 'title': 'Master Research & Evidence Framework'},
    'active_phase': 'Information Architecture',
    'last_completed': 'Visual Design System & Experience Blueprint',
    'next_build': {'number': 11, 'title': 'First Deep Content — Priority MRIDs'},
    'github_status': 'connected',
    'netlify_status': 'production_healthy',
    'content_readiness': 8,
    'research_readiness': 18,
    'data_viz_readiness': 2,
    'signup_funnel_readiness': 8,
    'civic_action_readiness': 8,
    'public_launch_readiness': 3,
    'public_launch_label': 'Early Foundation'
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 10
        bar['note'] = 'Seven registries + UX + design + research framework. Evidence IDs live. Deep content citation pass next.'
    if bar['id'] == 'research':
        bar['value'] = 18
        bar['note'] = 'Research Constitution v1.0: 14 Evidence IDs, 5-tier hierarchy, claim verification, review workflow. V1 target ~500.'
    if bar['id'] == 'ia':
        bar['value'] = 52
        bar['note'] = 'Full planning stack + design + research governance. Ready for cited deep content.'

mc['builds'].insert(0, {
    'number': 10,
    'title': 'Master Research & Evidence Framework',
    'version': '1.14.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Research Constitution — every claim traceable to Evidence IDs and reliable sources',
    'summary': '5 research principles, 5-tier source hierarchy, Evidence Registry (14 seeded), claim verification, review workflow, research dashboard.',
    'files_created': [
        'data/research-framework.json', 'data/evidence-registry.json',
        'docs/RESEARCH_CONSTITUTION.md', 'builds/010-master-research-evidence-framework.md',
        'mission-control/research.html', 'scripts/gen-evidence-registry.py'
    ],
    'files_modified': ['js/mission-control.js', 'docs/CITATION_GUIDE.md', 'library/index.html', 'data/claims-ledger.json'],
    'pages_created': ['/mission-control/research.html'],
    'decisions_made': [
        'EV-{6-digit} permanent Evidence IDs',
        'Five-tier source hierarchy governs reliability',
        'Claims ledger cross-linked to Evidence IDs',
        'Academic sources flagged as research gap (0 cataloged)'
    ],
    'open_questions': ['Auto-inject evidence panels on hall pages?', 'Hawaii Act 11 legislative text EV-ID?'],
    'risks': ['Citation coverage still ~12% — framework ahead of content depth'],
    'next_recommended': 11,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/research.html',
    'review_status': 'complete'
})

mc['briefing'] = {
    'what_built': 'Research Constitution v1.0 — Evidence Registry, 5-tier hierarchy, claim verification workflow',
    'building_now': 'Framework ready — apply Evidence IDs and ds-* components in first deep content (Build #11)',
    'blocked': ['Interactive charts', 'Participant backend', 'Academic source collection'],
    'ready_public': ['Research dashboard', 'Evidence registry', 'Source Library links', 'Claims ledger'],
    'next': 'Build #11 — First Deep Content with cited L2 articles (HIST-002, CASE-002)'
}

if not any(n.get('id') == 'research' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'research', 'label': 'Research Framework', 'href': '/mission-control/research.html', 'status': 'complete'
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
