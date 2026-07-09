import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json') as f:
    mc = json.load(f)

mc['version'] = '1.13.0'
mc['build'] = 9
mc['updated'] = '2026-07-09'
mc['design_system'] = '/data/design-system.json'
mc['design_system_route'] = '/mission-control/design.html'

mc['executive'] = {
    'overall_completion': 9,
    'current_build': {'number': 9, 'title': 'Visual Design System & Experience Blueprint'},
    'active_phase': 'Information Architecture',
    'last_completed': 'User Experience Architecture & Journey System',
    'next_build': {'number': 10, 'title': 'First Deep Content — Priority MRIDs'},
    'github_status': 'connected',
    'netlify_status': 'production_healthy',
    'content_readiness': 8,
    'research_readiness': 3,
    'data_viz_readiness': 2,
    'signup_funnel_readiness': 8,
    'civic_action_readiness': 8,
    'public_launch_readiness': 3,
    'public_launch_label': 'Early Foundation'
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 9
        bar['note'] = 'Six registries + UX journey + design system live. Tokens, 14 components, showcase page. Content depth next.'
    if bar['id'] == 'design':
        bar['value'] = 35
        bar['note'] = 'Design Language v1.0: tokens, component library, accessibility, trust signals, institutional palette.'
    if bar['id'] == 'ia':
        bar['value'] = 50
        bar['note'] = 'Full planning stack complete. Design system governs all future visual work.'

mc['builds'].insert(0, {
    'number': 9,
    'title': 'Visual Design System & Experience Blueprint',
    'version': '1.13.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Institutional design language — museum/library/archive aesthetic, not campaign site',
    'summary': 'Design tokens, 14 ds-* components, showcase page, emotional journey, domain colors, data viz standards, accessibility.',
    'files_created': [
        'data/design-system.json', 'docs/DESIGN_LANGUAGE.md',
        'builds/009-visual-design-system.md', 'css/design-tokens.css',
        'css/components.css', 'design-system/index.html', 'mission-control/design.html'
    ],
    'files_modified': ['css/styles.css', 'js/mission-control.js', 'docs/STYLE_GUIDE.md'],
    'pages_created': ['/design-system/', '/mission-control/design.html'],
    'decisions_made': [
        'Domain accent colors organize information — never persuade',
        'ds-* component prefix for governance',
        'Mission Control dark theme distinct but connected'
    ],
    'open_questions': ['Trust bar auto-inject on all hall pages in Build #10?', 'High-contrast theme toggle?'],
    'risks': ['Component adoption requires discipline in content builds'],
    'next_recommended': 10,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/design-system/',
    'review_status': 'complete'
})

mc['briefing'] = {
    'what_built': 'Full planning stack + UX journey + Design Language v1.0 (tokens, components, showcase)',
    'building_now': 'Design system ready — apply ds-* components in first deep content (Build #10)',
    'blocked': ['Interactive charts', 'Participant backend'],
    'ready_public': ['Design showcase', 'Component library', 'Institutional tokens on all pages'],
    'next': 'Build #10 — First Deep Content with design components and MRIDs'
}

if not any(n.get('id') == 'design' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'design', 'label': 'Design System', 'href': '/mission-control/design.html', 'status': 'complete'
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
