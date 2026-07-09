"""
Generate data/encyclopedia-knowledge-library.json — Build #33 Encyclopedia & Knowledge Library v1.0.
"""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
today = '2026-07-09'

kg_path = root / 'data/kg-registry.json'
facts_path = root / 'data/facts-registry.json'
evidence_path = root / 'data/evidence-registry.json'

kg = {}
facts = {}
evidence = {}
if kg_path.exists():
    with open(kg_path) as f:
        kg = json.load(f)
if facts_path.exists():
    with open(facts_path) as f:
        facts = json.load(f)
if evidence_path.exists():
    with open(evidence_path) as f:
        evidence = json.load(f)

kg_summary = kg.get('summary', {})
kg_nodes = kg.get('nodes', [])
facts_summary = facts.get('summary', {})
ev_summary = evidence.get('summary', {})

KG_TYPE_TO_CATEGORY = {
    'person': '100',
    'case': '200',
    'law': '300',
    'principle': '400',
    'organization': '500',
    'event': '600',
    'term': '700',
    'data': '800',
    'reform': '900',
}

CATEGORIES = [
    {
        'id': 'ENCY-CAT-100', 'number': 100, 'title': 'People', 'slug': 'people',
        'examples': ['Supreme Court Justices', 'Attorneys involved in the case', 'Constitutional scholars',
                     'Members of Congress', 'Historical reform figures'],
        'entry_fields': ['Biography', 'Historical significance', 'Timeline', 'Related cases',
                       'Related legislation', 'Related educational resources', 'Primary sources'],
        'kg_type': 'person', 'status': 'partial',
    },
    {
        'id': 'ENCY-CAT-200', 'number': 200, 'title': 'Court Cases', 'slug': 'court-cases',
        'examples': ['Citizens United v. FEC', 'Buckley v. Valeo', 'McConnell v. FEC',
                     'Austin v. Michigan Chamber of Commerce', 'McCutcheon v. FEC'],
        'entry_fields': ['Background', 'Legal questions', 'Holding', 'Majority opinion',
                       'Separate opinions', 'Long-term impact', 'Related constitutional principles', 'Source documents'],
        'kg_type': 'case', 'status': 'partial',
    },
    {
        'id': 'ENCY-CAT-300', 'number': 300, 'title': 'Laws', 'slug': 'laws',
        'examples': ['Federal statutes', 'Arkansas campaign finance statutes',
                     'Historical campaign finance legislation', 'Proposed legislation'],
        'entry_fields': ['Current law', 'Historical law', 'Proposals', 'Related cases', 'Primary sources'],
        'kg_type': 'law', 'status': 'partial',
    },
    {
        'id': 'ENCY-CAT-400', 'number': 400, 'title': 'Constitutional Principles', 'slug': 'constitutional-principles',
        'examples': ['Freedom of Speech', 'Political Speech', 'Freedom of Association',
                     'Judicial Review', 'Strict Scrutiny', 'Independent Expenditures'],
        'entry_fields': ['Plain-language explanation', 'Progressive depth', 'Related cases', 'Related events'],
        'kg_type': 'principle', 'status': 'partial',
    },
    {
        'id': 'ENCY-CAT-500', 'number': 500, 'title': 'Organizations', 'slug': 'organizations',
        'examples': ['Federal Election Commission', 'Supreme Court', 'Congressional committees',
                     'Educational institutions', 'Coalition partners (where appropriate)'],
        'entry_fields': ['Role in civic education story', 'Related cases', 'Related legislation', 'Resources'],
        'kg_type': 'organization', 'status': 'partial',
    },
    {
        'id': 'ENCY-CAT-600', 'number': 600, 'title': 'Historical Events', 'slug': 'historical-events',
        'examples': ['Tillman Act', 'Watergate', 'Federal Election Campaign Act',
                     'Bipartisan Campaign Reform Act', 'Citizens United decision', 'Emergence of Super PACs'],
        'entry_fields': ['Historical timeline', 'Related entries', 'Long-term impact', 'Primary sources'],
        'kg_type': 'event', 'status': 'partial',
    },
    {
        'id': 'ENCY-CAT-700', 'number': 700, 'title': 'Terms & Definitions', 'slug': 'terms-definitions',
        'examples': ['PAC', 'Super PAC', 'Independent Expenditure', 'Express Advocacy',
                     'Electioneering Communication', 'Disclosure', 'Dark Money'],
        'entry_fields': ['Simple explanation', 'Legal detail', 'Related cases', 'Related legislation'],
        'kg_type': 'term', 'status': 'planned',
    },
    {
        'id': 'ENCY-CAT-800', 'number': 800, 'title': 'Data & Statistics', 'slug': 'data-statistics',
        'examples': ['Political spending', 'Independent expenditures', 'Election cycles',
                     'Outside spending', 'Disclosure statistics'],
        'entry_fields': ['Methodology', 'Limitations', 'Primary sources', 'Related visualizations'],
        'kg_type': 'data', 'status': 'partial',
    },
    {
        'id': 'ENCY-CAT-900', 'number': 900, 'title': 'Reform Ideas', 'slug': 'reform-ideas',
        'examples': ['Constitutional amendment proposals', 'Federal legislative concepts',
                     'Arkansas legislative concepts', 'Ballot initiative concepts', 'Transparency proposals'],
        'entry_fields': ['Enacted law', 'Proposed reforms', 'Educational analysis', 'Related resources'],
        'kg_type': 'reform', 'status': 'partial',
    },
]

ENTRY_STRUCTURE = [
    'Plain-language summary', 'Why it matters', 'Historical context', 'Detailed explanation',
    'Related encyclopedia entries', 'Primary sources', 'Frequently asked questions',
    'Timeline placement', 'Suggested learning path',
]

READER_QUESTIONS = [
    'What is this?', 'Why does it matter?', 'How is it connected?',
    'What happened before?', 'What happened after?', 'Where can I verify it?', 'What should I read next?',
]

RELATIONSHIP_TARGETS = [
    'People', 'Court cases', 'Laws', 'Historical events', 'Constitutional principles',
    'Data', 'Educational resources', 'Arkansas-specific content',
]

SEARCH_AXES = [
    'Keyword', 'Topic', 'Date', 'Court case', 'Person', 'Organization', 'Law',
    'Constitutional principle', 'Arkansas content', 'Source type',
]

CITATION_STANDARDS = [
    'Cite authoritative sources',
    'Identify publication and review dates',
    'Link to primary documents whenever available',
    'Distinguish established facts from interpretation',
    'Explain uncertainty when it exists',
]

# Per-category planned targets (v1 encyclopedia scope)
CATEGORY_TARGETS = {
    '100': 60, '200': 45, '300': 40, '400': 35, '500': 30,
    '600': 50, '700': 80, '800': 25, '900': 35,
}

published_by_type = kg_summary.get('by_type', {})
total_planned = sum(CATEGORY_TARGETS.values())
total_published = len(kg_nodes)

fully_sourced = sum(
    1 for n in kg_nodes
    if n.get('evidence_ids') and len(n['evidence_ids']) > 0
)
under_review = facts_summary.get('under_review', 0) + ev_summary.get('awaiting_review', 0)
needing_updates = ev_summary.get('needing_updates', 0)
avg_completion = kg_summary.get('avg_completion_pct', 0)
orphan_nodes = kg_summary.get('orphan_nodes', 0)
total_edges = kg_summary.get('total_edges', 0)
cross_link_pct = min(round((total_edges / max(total_published * 2, 1)) * 100), 100)
reading_level_pct = round(avg_completion * 0.6)  # partial — depth not uniform

categories_with_counts = []
for cat in CATEGORIES:
    kg_type = cat['kg_type']
    published = published_by_type.get(kg_type, 0)
    planned = CATEGORY_TARGETS.get(str(cat['number']), 20)
    categories_with_counts.append({
        **cat,
        'entries_planned': planned,
        'entries_published': published,
        'completion_pct': round(published / planned * 100) if planned else 0,
    })

completion_score = {
    'entries_planned': total_planned,
    'entries_published': total_published,
    'entries_fully_sourced': fully_sourced,
    'entries_under_review': under_review,
    'entries_needing_updates': needing_updates,
    'cross_link_completeness_pct': cross_link_pct,
    'reading_level_completeness_pct': reading_level_pct,
    'overall_completion_pct': round(total_published / total_planned * 100, 1),
    'avg_entry_completion_pct': avg_completion,
    'orphan_entries': orphan_nodes,
}

# Honest readiness: architecture + KG alignment + low publish ratio
structure_score = 30  # 9 categories, entry structure, search, citations defined
publish_ratio = min(total_published / total_planned * 100, 100)
kg_alignment = min(total_published / 10 * 5, 15)  # 38 nodes mapped
encyclopedia_readiness = min(
    round(structure_score * 0.35 + publish_ratio * 0.25 + avg_completion * 0.2 + kg_alignment * 0.2),
    26,
)

out = {
    'version': '1.0',
    'build': 33,
    'updated': today,
    'title': 'Research Encyclopedia & Knowledge Library v1.0',
    'subtitle': 'Encyclopedia Architecture',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/encyclopedia.html',
    'canonical_entry_route': '/encyclopedia/[category]/[slug]',
    'current_entry_route': 'KG nodes via /explore/ and hall pages',
    'constitution': '/docs/ENCYCLOPEDIA_ARCHITECTURE.md',
    'purpose': 'Definitive living encyclopedia — every topic connected through a single knowledge system.',
    'encyclopedia_philosophy': 'Every page answers one question exceptionally well.',
    'governing_principle': 'Help readers see how history, law, Constitution, spending, reform, and civic education fit together.',
    'reader_questions': READER_QUESTIONS,
    'categories': categories_with_counts,
    'entry_structure': ENTRY_STRUCTURE,
    'relationship_graph': {
        'title': 'Encyclopedia Relationship Graph',
        'status': 'partial',
        'targets': RELATIONSHIP_TARGETS,
        'registry': '/data/kg-registry.json',
        'nodes': kg_summary.get('total_nodes', 0),
        'edges': total_edges,
        'hub_node': kg.get('hub_node'),
        'fully_connected_hub': kg_summary.get('fully_connected_hub', False),
    },
    'search': {
        'title': 'Encyclopedia Search',
        'status': 'planned',
        'axes': SEARCH_AXES,
        'note': 'Educational relevance over simple keyword matching.',
    },
    'completion_score': completion_score,
    'citation_standards': CITATION_STANDARDS,
    'kg_type_mapping': KG_TYPE_TO_CATEGORY,
    'future_expansion': {
        'title': 'Future Topic Expansion',
        'status': 'defined',
        'note': 'Same encyclopedia framework accommodates additional civic education subjects.',
        'current_focus': 'Citizens United only',
    },
    'related_systems': [
        {'title': 'Knowledge Graph Registry', 'route': '/data/kg-registry.json', 'build': 11},
        {'title': 'Facts Registry', 'route': '/data/facts-registry.json', 'build': 18},
        {'title': 'Evidence Registry', 'route': '/data/evidence-registry.json', 'build': 10},
        {'title': 'Knowledge Atlas', 'route': '/mission-control/atlas.html', 'build': 19},
        {'title': 'Research Observatory', 'route': '/mission-control/research-observatory.html', 'build': 29},
        {'title': 'AI Knowledge Engine', 'route': '/mission-control/ai-knowledge.html', 'build': 26},
    ],
    'summary': {
        'categories_total': len(CATEGORIES),
        'entry_structure_sections': len(ENTRY_STRUCTURE),
        'reader_questions': len(READER_QUESTIONS),
        'search_axes': len(SEARCH_AXES),
        'entries_planned': total_planned,
        'entries_published': total_published,
        'entries_fully_sourced': fully_sourced,
        'facts_linked': facts_summary.get('total', 0),
        'evidence_linked': ev_summary.get('total', 0),
        'canonical_routes_live': False,
        'encyclopedia_search_live': False,
        'completion_tracking_live': True,
        'encyclopedia_readiness_pct': encyclopedia_readiness,
    },
    'catalog_gaps': [
        'Canonical /encyclopedia/[category]/[slug] routes not built — KG nodes link to hall pages',
        'Category 700 (Terms & Definitions) has 0 published entries — glossary not encyclopedia-scale',
        f'Only {fully_sourced}/{total_published} entries fully sourced with evidence IDs',
        'Encyclopedia search not implemented — axes defined only',
        '9-section entry structure not enforced on all published entries',
        f'{orphan_nodes} orphan KG nodes — cross-link completeness incomplete',
        f'{total_published}/{total_planned} planned entries published ({completion_score["overall_completion_pct"]}%)',
        'Reading-level progression (simple → legal depth) not uniform across entries',
    ],
    'recommended_next_build': {
        'number': 35,
        'title': 'Component Specifications with Props/States',
        'note': 'Map encyclopedia entry structure and category pages to COMP-* components from Build #17.',
    },
}

path = root / 'data/encyclopedia-knowledge-library.json'
with open(path, 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')
print(f'Encyclopedia: {total_published}/{total_planned} entries, {encyclopedia_readiness}% readiness')
