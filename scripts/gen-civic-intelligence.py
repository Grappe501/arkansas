"""
Generate data/civic-intelligence.json — Build #40 Master Knowledge Graph & Civic Intelligence Engine v1.0.
"""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
today = '2026-07-09'


def load_json(path):
    if path.exists():
        with open(path) as f:
            return json.load(f)
    return {}


kg = load_json(root / 'data/kg-registry.json')
rel = load_json(root / 'data/relationship-registry.json')
ev = load_json(root / 'data/evidence-registry.json')
counties = load_json(root / 'data/arkansas-counties.json')

kg_summary = kg.get('summary', {})
rel_summary = rel.get('summary', {})
ev_summary = ev.get('summary', {})
county_summary = counties.get('summary', {})

NODE_TYPES = [
    {'id': 'case', 'title': 'Court Cases', 'prefix': 'KG-CASE', 'kg_type': 'case', 'status': 'live', 'nodes_live': kg_summary.get('by_type', {}).get('case', 0)},
    {'id': 'justice', 'title': 'Supreme Court Justices', 'prefix': 'KG-JUSTICE', 'kg_type': None, 'status': 'planned', 'nodes_live': 0},
    {'id': 'principle', 'title': 'Constitutional Principles', 'prefix': 'KG-PRIN', 'kg_type': 'principle', 'status': 'live', 'nodes_live': kg_summary.get('by_type', {}).get('principle', 0)},
    {'id': 'event', 'title': 'Historical Events', 'prefix': 'KG-EVENT', 'kg_type': 'event', 'status': 'live', 'nodes_live': kg_summary.get('by_type', {}).get('event', 0)},
    {'id': 'federal_law', 'title': 'Federal Laws', 'prefix': 'KG-LAW', 'kg_type': 'law', 'status': 'partial', 'nodes_live': kg_summary.get('by_type', {}).get('law', 0),
     'note': 'KG law nodes — Arkansas laws not yet separated'},
    {'id': 'arkansas_law', 'title': 'Arkansas Laws', 'prefix': 'KG-ARLAW', 'kg_type': None, 'status': 'planned', 'nodes_live': 0},
    {'id': 'official', 'title': 'Public Officials', 'prefix': 'KG-OFFICIAL', 'kg_type': None, 'status': 'planned', 'nodes_live': 0},
    {'id': 'ballot', 'title': 'Ballot Initiative Concepts', 'prefix': 'KG-BALLOT', 'kg_type': None, 'status': 'planned', 'nodes_live': 0},
    {'id': 'model_law', 'title': 'Model Law Concepts', 'prefix': 'KG-MODEL', 'kg_type': None, 'status': 'partial', 'nodes_live': kg_summary.get('by_type', {}).get('reform', 0),
     'note': 'Reform nodes in KG — model law taxonomy not split'},
    {'id': 'lesson', 'title': 'Educational Lessons', 'prefix': 'KG-LESSON', 'kg_type': None, 'status': 'planned', 'nodes_live': 0},
    {'id': 'encyclopedia', 'title': 'Encyclopedia Entries', 'prefix': 'KG-ENC', 'kg_type': None, 'status': 'planned', 'nodes_live': 0},
    {'id': 'source', 'title': 'Research Sources', 'prefix': 'EV', 'kg_type': None, 'status': 'partial', 'nodes_live': ev_summary.get('total', 0),
     'note': 'Evidence Registry EV-* — not yet KG-linked as nodes'},
    {'id': 'dataset', 'title': 'Data Sets', 'prefix': 'KG-DATA', 'kg_type': 'data', 'status': 'live', 'nodes_live': kg_summary.get('by_type', {}).get('data', 0)},
    {'id': 'conversation', 'title': 'Community Conversations', 'prefix': 'KG-CONV', 'kg_type': None, 'status': 'planned', 'nodes_live': 0},
    {'id': 'coalition', 'title': 'Coalition Organizations', 'prefix': 'KG-ORG', 'kg_type': 'organization', 'status': 'partial', 'nodes_live': kg_summary.get('by_type', {}).get('organization', 0)},
    {'id': 'county', 'title': 'Arkansas Counties', 'prefix': 'AR-COUNTY', 'kg_type': None, 'status': 'partial', 'nodes_live': counties.get('counties_total', 75),
     'note': '75 counties in arkansas-counties.json — 0 KG edges to counties'},
    {'id': 'educator', 'title': 'Education Leaders', 'prefix': 'KG-EDU', 'kg_type': None, 'status': 'planned', 'nodes_live': 0},
    {'id': 'person', 'title': 'People', 'prefix': 'KG-PERSON', 'kg_type': 'person', 'status': 'live', 'nodes_live': kg_summary.get('by_type', {}).get('person', 0)},
]

RELATIONSHIP_TYPES = [
    {'id': 'precedes', 'title': 'PRECEDES', 'status': 'partial', 'edges_live': 0, 'kg_alias': 'precursor'},
    {'id': 'follows', 'title': 'FOLLOWS', 'status': 'partial', 'edges_live': 0, 'kg_alias': 'aftermath'},
    {'id': 'cites', 'title': 'CITES', 'status': 'live', 'edges_live': 0},
    {'id': 'supports', 'title': 'SUPPORTS', 'status': 'live', 'edges_live': 0},
    {'id': 'references', 'title': 'REFERENCES', 'status': 'partial', 'edges_live': 0, 'note': 'Relationship registry schema — 0 edges'},
    {'id': 'explains', 'title': 'EXPLAINS', 'status': 'planned', 'edges_live': 0},
    {'id': 'modifies', 'title': 'MODIFIES', 'status': 'planned', 'edges_live': 0},
    {'id': 'overrules', 'title': 'OVERRULES', 'status': 'partial', 'edges_live': 0, 'kg_alias': 'overturned_by'},
    {'id': 'related_to', 'title': 'RELATED_TO', 'status': 'live', 'edges_live': 0},
    {'id': 'part_of', 'title': 'PART_OF', 'status': 'planned', 'edges_live': 0},
    {'id': 'taught_in', 'title': 'TAUGHT_IN', 'status': 'planned', 'edges_live': 0},
    {'id': 'used_by', 'title': 'USED_BY', 'status': 'planned', 'edges_live': 0},
    {'id': 'hosted_by', 'title': 'HOSTED_BY', 'status': 'planned', 'edges_live': 0},
    {'id': 'represents', 'title': 'REPRESENTS', 'status': 'planned', 'edges_live': 0},
    {'id': 'located_in', 'title': 'LOCATED_IN', 'status': 'partial', 'edges_live': 0, 'note': 'Relationship registry defined — 0 edges'},
    {'id': 'contributes_to', 'title': 'CONTRIBUTES_TO', 'status': 'planned', 'edges_live': 0},
    {'id': 'mentors', 'title': 'MENTORS', 'status': 'planned', 'edges_live': 0},
    {'id': 'shares', 'title': 'SHARES', 'status': 'planned', 'edges_live': 0},
    {'id': 'referred', 'title': 'REFERRED', 'status': 'planned', 'edges_live': 0},
]

# Count edges per kg edge type
edge_type_counts = {}
for e in kg.get('edges', []):
    t = e.get('type', 'unknown')
    edge_type_counts[t] = edge_type_counts.get(t, 0) + 1

for rt in RELATIONSHIP_TYPES:
    aliases = [rt['id']]
    if rt.get('kg_alias'):
        aliases.append(rt['kg_alias'])
    count = sum(edge_type_counts.get(a, 0) for a in aliases)
    if count:
        rt['edges_live'] = count

INTELLIGENCE_LAYERS = [
    {
        'id': 'CI-01', 'title': 'Knowledge Graph', 'slug': 'knowledge-graph',
        'purpose': 'Every object a node — court cases through education leaders.',
        'status': 'partial', 'readiness_pct': 28,
        'route': '/mission-control/knowledge-graph.html',
        'registry': '/data/kg-registry.json',
        'build': 11,
        'note': f"{kg_summary.get('total_nodes', 0)} nodes, {kg_summary.get('total_edges', 0)} edges — v1 target 500",
    },
    {
        'id': 'CI-02', 'title': 'Educational Dependency Map', 'slug': 'educational-dependency',
        'purpose': 'Curriculum concepts depend on prior concepts.',
        'status': 'partial', 'readiness_pct': 22,
        'route': '/mission-control/curriculum.html',
        'note': 'Master Curriculum tiers — no automated dependency graph',
    },
    {
        'id': 'CI-03', 'title': 'Research Dependency Map', 'slug': 'research-dependency',
        'purpose': 'Sources support, challenge, expand, update, and supersede one another.',
        'status': 'partial', 'readiness_pct': 18,
        'route': '/mission-control/research.html',
        'note': f"{ev_summary.get('total', 0)} evidence items — no dependency edges",
    },
    {
        'id': 'CI-04', 'title': 'Community Intelligence Graph', 'slug': 'community-intelligence',
        'purpose': 'Education leaders, counties, organizations, presentations, conversations.',
        'status': 'planned', 'readiness_pct': 8,
        'route': '/mission-control/county-os.html',
        'note': '0 county participation edges — forms not integrated',
    },
    {
        'id': 'CI-05', 'title': 'Legislative Intelligence Graph', 'slug': 'legislative-intelligence',
        'purpose': 'Proposals connect to laws, constitutional provisions, and court decisions.',
        'status': 'partial', 'readiness_pct': 20,
        'route': '/mission-control/research-observatory.html',
        'note': 'Reform KG nodes + observatory — no lineage visualization',
    },
    {
        'id': 'CI-06', 'title': 'Timeline Intelligence', 'slug': 'timeline-intelligence',
        'purpose': 'Every object understands created, decided, enacted, reviewed, published.',
        'status': 'partial', 'readiness_pct': 16,
        'route': '/halls/story-before.html',
        'note': 'Event nodes have years — no unified timeline engine',
    },
    {
        'id': 'CI-07', 'title': 'Question Engine', 'slug': 'question-engine',
        'purpose': 'Answer questions from stored relationships.',
        'status': 'planned', 'readiness_pct': 4,
        'route': '/mission-control/ai-knowledge.html',
        'note': 'AI Knowledge Engine planned — no graph query layer',
    },
]

EDUCATIONAL_DEPENDENCY_CHAIN = [
    {'id': 'DEP-01', 'title': 'Campaign Finance', 'level': 1},
    {'id': 'DEP-02', 'title': 'Federal Election Campaign Act', 'level': 2, 'depends_on': 'DEP-01'},
    {'id': 'DEP-03', 'title': 'Bipartisan Campaign Reform Act', 'level': 3, 'depends_on': 'DEP-02'},
    {'id': 'DEP-04', 'title': 'Citizens United', 'level': 4, 'depends_on': 'DEP-03', 'kg_id': 'KG-CASE-000003'},
    {'id': 'DEP-05', 'title': 'Independent Expenditures', 'level': 5, 'depends_on': 'DEP-04'},
    {'id': 'DEP-06', 'title': 'Super PACs', 'level': 6, 'depends_on': 'DEP-05', 'kg_id': 'KG-CASE-000006'},
    {'id': 'DEP-07', 'title': 'Disclosure Debates', 'level': 7, 'depends_on': 'DEP-06'},
]

RESEARCH_DEPENDENCY_TYPES = [
    'Supports', 'Challenges', 'Expands', 'Updates', 'Supersedes', 'Historical Context',
]

COMMUNITY_INTELLIGENCE_CHAIN = [
    'Education Leader', 'County', 'Organization', 'Presentation', 'Resources Used',
    'Community Conversation', 'New Participants', 'New Organizations', 'New Counties',
]

TIMELINE_ATTRIBUTES = [
    'Created', 'Modified', 'Decided', 'Introduced', 'Enacted', 'Repealed', 'Updated', 'Reviewed', 'Published',
]

SAMPLE_QUESTIONS = [
    'What Supreme Court decisions influenced Citizens United?',
    'What Arkansas educational resources explain independent expenditures?',
    'Which historical laws preceded the Bipartisan Campaign Reform Act?',
    'Which encyclopedia articles cite this source?',
    'What lessons should I study before reading the majority opinion?',
]

KNOWLEDGE_NAVIGATION = [
    'What this connects to', 'What influenced it', 'What it influenced',
    'What should be learned next', 'What evidence supports it',
    'Who is involved', 'What Arkansas resources relate to it',
]

MC_METRICS = [
    {'id': 'CI-M01', 'title': 'Knowledge graph growth', 'status': 'partial', 'current': kg_summary.get('total_nodes', 0), 'target': 500},
    {'id': 'CI-M02', 'title': 'Relationship count', 'status': 'partial', 'current': kg_summary.get('total_edges', 0)},
    {'id': 'CI-M03', 'title': 'Unconnected topics', 'status': 'partial', 'current': kg_summary.get('orphan_nodes', 0)},
    {'id': 'CI-M04', 'title': 'Missing sources', 'status': 'planned', 'current': 0},
    {'id': 'CI-M05', 'title': 'Research gaps', 'status': 'planned', 'current': 0},
    {'id': 'CI-M06', 'title': 'Learning dependencies', 'status': 'partial', 'current': len(EDUCATIONAL_DEPENDENCY_CHAIN)},
    {'id': 'CI-M07', 'title': 'County relationships', 'status': 'planned', 'current': 0},
    {'id': 'CI-M08', 'title': 'Coalition connections', 'status': 'planned', 'current': 0},
    {'id': 'CI-M09', 'title': 'Curriculum coverage', 'status': 'partial', 'current': 0},
]

FUTURE_AI = [
    'Suggesting new educational pathways', 'Finding missing research',
    'Building presentation packets', 'Connecting volunteers',
    'Identifying underserved counties', 'Explaining complex legal relationships',
    'Generating personalized reading plans',
]

node_types_live = sum(1 for n in NODE_TYPES if n['status'] == 'live')
node_types_partial = sum(1 for n in NODE_TYPES if n['status'] == 'partial')
layers_partial = sum(1 for l in INTELLIGENCE_LAYERS if l['status'] == 'partial')
avg_layer_readiness = round(sum(l['readiness_pct'] for l in INTELLIGENCE_LAYERS) / len(INTELLIGENCE_LAYERS))

nodes_total = kg_summary.get('total_nodes', 0)
v1_target = kg_summary.get('v1_target_nodes', 500)
node_growth_pct = round(nodes_total / v1_target * 100) if v1_target else 0

civic_intelligence_readiness = min(
    round(avg_layer_readiness * 0.35 + node_growth_pct * 0.25 + (layers_partial / 7 * 100) * 0.2 + 10),
    24,
)

out = {
    'version': '1.0',
    'build': 40,
    'updated': today,
    'title': 'Master Knowledge Graph & Civic Intelligence Engine v1.0',
    'subtitle': 'Institutional Brain Architecture',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/civic-intelligence.html',
    'canonical_brain_route': '/brain/[node-id]',
    'current_brain_route': 'KG registry + explore-further — no public interactive brain viz',
    'constitution': '/docs/INSTITUTIONAL_BRAIN.md',
    'purpose': 'The Institutional Brain — everything connected, nothing stands alone.',
    'vision': 'Visible threads between every idea — touch one and see what came before, what followed, and what Arkansas teaches it.',
    'governing_principle': 'A living civic knowledge institution where every fact, source, lesson, county, educator, and organization strengthens every other part.',
    'long_term_vision': 'Invisible intelligence layer — visitors see content, Mission Control sees relationships and gaps.',
    'node_types': NODE_TYPES,
    'relationship_types': RELATIONSHIP_TYPES,
    'intelligence_layers': INTELLIGENCE_LAYERS,
    'educational_dependency_chain': EDUCATIONAL_DEPENDENCY_CHAIN,
    'research_dependency_types': RESEARCH_DEPENDENCY_TYPES,
    'community_intelligence_chain': COMMUNITY_INTELLIGENCE_CHAIN,
    'timeline_attributes': TIMELINE_ATTRIBUTES,
    'sample_questions': SAMPLE_QUESTIONS,
    'knowledge_navigation': KNOWLEDGE_NAVIGATION,
    'future_ai_integration': FUTURE_AI,
    'mc_integration': {
        'title': 'Mission Control Institutional Brain Metrics',
        'status': 'partial',
        'metrics': MC_METRICS,
        'visualization_live': False,
    },
    'kg_foundation': {
        'build': 11,
        'registry': '/data/kg-registry.json',
        'constitution': '/data/knowledge-graph.json',
        'dashboard': '/mission-control/knowledge-graph.html',
        'hub_node': kg.get('hub_node', 'KG-CASE-000003'),
        'summary': kg_summary,
    },
    'related_systems': [
        {'title': 'Knowledge Graph (Build #11)', 'route': '/data/kg-registry.json', 'build': 11},
        {'title': 'Relationship Registry', 'route': '/data/relationship-registry.json', 'build': 15},
        {'title': 'Evidence Registry', 'route': '/data/evidence-registry.json', 'build': 10},
        {'title': 'Encyclopedia', 'route': '/data/encyclopedia-knowledge-library.json', 'build': 33},
        {'title': 'Master Curriculum', 'route': '/data/master-curriculum.json', 'build': 35},
        {'title': 'County OS', 'route': '/data/arkansas-counties.json', 'build': 31},
        {'title': 'AI Knowledge Engine', 'route': '/data/ai-knowledge-engine.json', 'build': 26},
        {'title': 'Learning Laboratory', 'route': '/data/learning-laboratory.json', 'build': 38},
    ],
    'summary': {
        'node_types_total': len(NODE_TYPES),
        'node_types_live': node_types_live,
        'node_types_partial': node_types_partial,
        'node_types_planned': sum(1 for n in NODE_TYPES if n['status'] == 'planned'),
        'relationship_types_total': len(RELATIONSHIP_TYPES),
        'relationship_types_with_edges': sum(1 for r in RELATIONSHIP_TYPES if r['edges_live'] > 0),
        'intelligence_layers_total': len(INTELLIGENCE_LAYERS),
        'intelligence_layers_partial': layers_partial,
        'kg_nodes': nodes_total,
        'kg_edges': kg_summary.get('total_edges', 0),
        'kg_orphan_nodes': kg_summary.get('orphan_nodes', 0),
        'kg_v1_target_nodes': v1_target,
        'kg_growth_pct': node_growth_pct,
        'evidence_sources': ev_summary.get('total', 0),
        'relationship_registry_edges': rel_summary.get('edges_recorded', 0),
        'arkansas_counties': counties.get('counties_total', 75),
        'counties_with_participants': county_summary.get('counties_with_participants', 0),
        'question_engine_live': False,
        'brain_visualization_live': False,
        'avg_layer_readiness_pct': avg_layer_readiness,
        'civic_intelligence_readiness_pct': civic_intelligence_readiness,
    },
    'catalog_gaps': [
        f'KG at {nodes_total}/{v1_target} nodes ({node_growth_pct}%) — Institutional Brain incomplete',
        f'{kg_summary.get("orphan_nodes", 0)} orphan nodes — unconnected topics remain',
        '9 of 17 node types planned — justices, lessons, encyclopedia, educators not in KG',
        'Relationship registry has 0 edges — community/coalition graph not populated',
        'No public interactive brain visualization — explore-further only',
        'Question engine not built — sample questions unanswered automatically',
        'County nodes exist but 0 KG edges to 75 Arkansas counties',
        'Research dependency edges not recorded — evidence items not linked as graph',
        'Educational dependency chain defined — not wired to curriculum paths',
        'Timeline intelligence partial — no unified temporal query layer',
    ],
    'recommended_next_build': {
        'number': 42,
        'title': 'Component Specifications with Props/States',
        'note': 'Map brain visualization shells, node panels, relationship edges, and explore-further widgets to COMP-* from Build #17.',
    },
}

path = root / 'data/civic-intelligence.json'
with open(path, 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')
print(f'Civic Intelligence: {nodes_total} KG nodes, {layers_partial}/7 layers partial, {civic_intelligence_readiness}% readiness')
