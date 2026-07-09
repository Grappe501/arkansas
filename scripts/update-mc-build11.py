import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json') as f:
    mc = json.load(f)

mc['version'] = '1.15.0'
mc['build'] = 11
mc['updated'] = '2026-07-09'
mc['knowledge_graph'] = '/data/knowledge-graph.json'
mc['kg_registry'] = '/data/kg-registry.json'
mc['knowledge_graph_route'] = '/mission-control/knowledge-graph.html'

mc['executive'] = {
    'overall_completion': 11,
    'current_build': {'number': 11, 'title': 'Citizens United Knowledge Graph & Educational Intelligence Architecture'},
    'active_phase': 'Information Architecture',
    'last_completed': 'Master Research & Evidence Framework',
    'next_build': {'number': 12, 'title': 'First Deep Content — KG-IDs, Evidence IDs, ds-* components'},
    'github_status': 'connected',
    'netlify_status': 'production_healthy',
    'content_readiness': 10,
    'research_readiness': 18,
    'data_viz_readiness': 2,
    'signup_funnel_readiness': 8,
    'civic_action_readiness': 8,
    'public_launch_readiness': 4,
    'public_launch_label': 'Early Foundation'
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 11
        bar['note'] = 'Eight registries + knowledge graph live. 38 KG nodes, Explore Further on content pages. Deep content next.'
    if bar['id'] == 'ia':
        bar['value'] = 55
        bar['note'] = 'Full planning stack + knowledge graph. Connected exploration replaces isolated pages.'
    if bar['id'] == 'content':
        bar['value'] = 14
        bar['note'] = 'Knowledge graph links 38 objects. L2 deep pages with KG-IDs next (Build #12).'

if not any(b.get('id') == 'knowledge_graph' for b in mc['progress_bars']):
    mc['progress_bars'].insert(4, {
        'id': 'knowledge_graph',
        'label': 'Knowledge Graph',
        'value': 12,
        'note': 'KG Constitution v1.0: 38 nodes, 62 edges, 10 clusters, Explore Further component. V1 target ~500 nodes.'
    })

mc['builds'].insert(0, {
    'number': 11,
    'title': 'Citizens United Knowledge Graph & Educational Intelligence Architecture',
    'version': '1.15.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Connected knowledge system — every object interrelated, Explore Further on every page',
    'summary': '8 object types, 38 nodes, 62 edges, 10 clusters, educational intelligence rules, Explore Further JS, Mission Control knowledge map.',
    'files_created': [
        'data/knowledge-graph.json', 'data/kg-registry.json',
        'docs/KNOWLEDGE_GRAPH.md', 'builds/011-knowledge-graph.md',
        'js/explore-further.js', 'css/explore-further.css',
        'mission-control/knowledge-graph.html', 'scripts/gen-kg-registry.py'
    ],
    'files_modified': ['js/mission-control.js', 'js/layout.js', 'data/knowledge.json'],
    'pages_created': ['/mission-control/knowledge-graph.html'],
    'decisions_made': [
        'KG-{TYPE}-{6-digit} permanent node IDs',
        'Citizens United as hub node (KG-CASE-000003)',
        'Explore Further auto-injected on all non-MC content pages',
        'AI layer planned — must cite verified knowledge base only'
    ],
    'open_questions': ['Interactive visual graph renderer?', 'KG-ID display on public pages?'],
    'risks': ['Graph completeness ~8% of v1 target — framework ahead of content depth'],
    'next_recommended': 12,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/knowledge-graph.html',
    'review_status': 'complete'
})

mc['briefing'] = {
    'what_built': 'Knowledge Graph Constitution v1.0 — 38 connected nodes, Explore Further, educational intelligence',
    'building_now': 'Graph ready — wire KG-IDs and Evidence IDs into first deep content (Build #12)',
    'blocked': ['Visual graph renderer', 'AI Q&A layer', 'Interactive charts'],
    'ready_public': ['Explore Further on hall pages', 'Knowledge graph dashboard', 'Hub-and-spoke case network'],
    'next': 'Build #12 — First Deep Content with KG-IDs, Evidence IDs, ds-* components'
}

if not any(n.get('id') == 'knowledge_graph' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'knowledge_graph', 'label': 'Knowledge Graph', 'href': '/mission-control/knowledge-graph.html', 'status': 'complete'
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
