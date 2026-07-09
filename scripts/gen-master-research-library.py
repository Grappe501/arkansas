"""
Generate data/master-research-library.json — Build #37 Master Research Library & Digital Archive v1.0.
"""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
today = '2026-07-09'

ev_path = root / 'data/evidence-registry.json'
kg_path = root / 'data/kg-registry.json'
trust_path = root / 'data/trust-framework.json'

evidence = {}
kg = {}
trust = {}
if ev_path.exists():
    with open(ev_path) as f:
        evidence = json.load(f)
if kg_path.exists():
    with open(kg_path) as f:
        kg = json.load(f)
if trust_path.exists():
    with open(trust_path) as f:
        trust = json.load(f)

es = evidence.get('summary', {})
items = evidence.get('items', [])

TYPE_TO_COLLECTION = {
    'court': 'A',
    'primary': 'B',
    'government': 'B',
    'ngo': 'G',
    'journalism': 'D',
    'platform': 'G',
    'academic': 'E',
    'data': 'F',
}

COLLECTIONS = [
    {
        'id': 'LIB-COL-A', 'letter': 'A', 'title': 'Supreme Court Collection', 'slug': 'supreme-court',
        'contains': ['Opinions', 'Dissents', 'Oral argument transcripts', 'Briefs', 'Related cases', 'Court orders', 'Historical notes'],
        'annotations': ['Plain-language summary', 'Historical significance', 'Related lessons', 'Related encyclopedia entries'],
        'status': 'partial', 'documents_archived': 0, 'documents_planned': 85,
    },
    {
        'id': 'LIB-COL-B', 'letter': 'B', 'title': 'Federal Law Collection', 'slug': 'federal-law',
        'contains': ['Campaign finance statutes', 'Federal regulations', 'Congressional reports', 'Legislative history', 'Committee materials', 'Hearing transcripts'],
        'annotations': ['Educational annotations per document'],
        'status': 'partial', 'documents_archived': 0, 'documents_planned': 60,
    },
    {
        'id': 'LIB-COL-C', 'letter': 'C', 'title': 'Arkansas Collection', 'slug': 'arkansas',
        'contains': ['Arkansas statutes', 'Arkansas constitutional provisions', 'Ballot initiative materials', 'Legislative history', 'Educational resources', 'Arkansas election law references'],
        'annotations': ['Arkansas-specific foundation'],
        'status': 'planned', 'documents_archived': 0, 'documents_planned': 45,
    },
    {
        'id': 'LIB-COL-D', 'letter': 'D', 'title': 'Historical Collection', 'slug': 'historical',
        'contains': ['Campaign finance history', 'Reform movements', 'Watergate resources', 'Progressive Era materials', 'Major historical timelines', 'Significant political developments'],
        'annotations': ['Historical context for Citizens United'],
        'status': 'partial', 'documents_archived': 0, 'documents_planned': 70,
    },
    {
        'id': 'LIB-COL-E', 'letter': 'E', 'title': 'Academic Collection', 'slug': 'academic',
        'contains': ['Law review articles', 'Peer-reviewed research', 'University publications', 'Empirical studies', 'Constitutional scholarship'],
        'annotations': ['Citation', 'Abstract', 'Educational summary', 'Related topics'],
        'status': 'planned', 'documents_archived': 0, 'documents_planned': 55,
    },
    {
        'id': 'LIB-COL-F', 'letter': 'F', 'title': 'Data Collection', 'slug': 'data',
        'contains': ['Political spending datasets', 'Independent expenditure reports', 'Election finance statistics', 'Disclosure reports', 'Government data'],
        'annotations': ['Methodology', 'Definitions', 'Limitations', 'Educational significance'],
        'status': 'planned', 'documents_archived': 0, 'documents_planned': 40,
    },
    {
        'id': 'LIB-COL-G', 'letter': 'G', 'title': 'Public Education Collection', 'slug': 'public-education',
        'contains': ['Presentation slides', 'Handouts', 'Infographics', 'Discussion guides', 'Community conversation materials', 'Educational videos'],
        'annotations': ['Education Leaders and coalition partners'],
        'status': 'partial', 'documents_archived': 0, 'documents_planned': 50,
    },
]

# Count evidence items per collection
col_counts = {c['letter']: 0 for c in COLLECTIONS}
for item in items:
    st = item.get('source_type', 'platform')
    letter = TYPE_TO_COLLECTION.get(st, 'G')
    # Arkansas items -> C
    if item.get('jurisdiction') == 'Arkansas' or 'Arkansas' in (item.get('topic') or ''):
        letter = 'C'
    col_counts[letter] = col_counts.get(letter, 0) + 1

for c in COLLECTIONS:
    c['documents_archived'] = col_counts.get(c['letter'], 0)
    c['completion_pct'] = round(c['documents_archived'] / c['documents_planned'] * 100, 1) if c['documents_planned'] else 0

ARCHIVE_FIELDS = [
    'Archive ID', 'MRID', 'Collection', 'Category', 'Subject', 'Keywords',
    'Publication date', 'Review date', 'Source level', 'Related entries',
]

RELATIONSHIP_TARGETS = [
    'Encyclopedia entries', 'Educational lessons', 'Supreme Court cases', 'Historical events',
    'Data visualizations', 'Community education resources', 'Coalition toolkits', 'Arkansas content',
]

RESEARCH_WORKSPACE = [
    {'id': 'LIB-RW-01', 'title': 'Save documents', 'status': 'planned'},
    {'id': 'LIB-RW-02', 'title': 'Build reading lists', 'status': 'planned'},
    {'id': 'LIB-RW-03', 'title': 'Bookmark sources', 'status': 'planned'},
    {'id': 'LIB-RW-04', 'title': 'Compare materials', 'status': 'planned'},
    {'id': 'LIB-RW-05', 'title': 'Track research progress', 'status': 'planned'},
    {'id': 'LIB-RW-06', 'title': 'Export citations', 'status': 'planned'},
]

READING_LISTS = [
    {'id': 'LIB-RL-01', 'title': 'Beginner Collection', 'focus': 'Introductory materials', 'status': 'partial', 'route': '/start-here/'},
    {'id': 'LIB-RL-02', 'title': 'Constitutional Collection', 'focus': 'First Amendment and jurisprudence', 'status': 'partial', 'route': '/halls/what-court-decided.html'},
    {'id': 'LIB-RL-03', 'title': 'Historical Collection', 'focus': 'Campaign finance history', 'status': 'partial', 'route': '/halls/story-before.html'},
    {'id': 'LIB-RL-04', 'title': 'Arkansas Collection', 'focus': 'Arkansas-specific resources', 'status': 'planned', 'route': '/solutions/#arkansas'},
    {'id': 'LIB-RL-05', 'title': 'Research Collection', 'focus': 'Primary sources and advanced scholarship', 'status': 'partial', 'route': '/library/'},
]

SEARCH_AXES = [
    'Keyword', 'Topic', 'Person', 'Court case', 'Law', 'Historical period',
    'Arkansas content', 'Collection', 'Document type', 'Source level',
]

LIBRARY_METRICS = [
    {'id': 'LIB-M01', 'title': 'Documents archived', 'status': 'partial', 'current': es.get('total', 0)},
    {'id': 'LIB-M02', 'title': 'Collections with content', 'status': 'partial', 'current': sum(1 for c in COLLECTIONS if c['documents_archived'] > 0)},
    {'id': 'LIB-M03', 'title': 'Sources verified', 'status': 'partial', 'current': es.get('published', 0)},
    {'id': 'LIB-M04', 'title': 'Research summaries published', 'status': 'partial', 'current': sum(1 for i in items if i.get('summary'))},
    {'id': 'LIB-M05', 'title': 'Documents awaiting review', 'status': 'partial', 'current': es.get('awaiting_review', 0)},
    {'id': 'LIB-M06', 'title': 'Broken external links', 'status': 'planned', 'current': 0},
    {'id': 'LIB-M07', 'title': 'Archive growth (month)', 'status': 'planned', 'current': 0},
    {'id': 'LIB-M08', 'title': 'Reader usage', 'status': 'planned', 'current': 0},
]

PRESERVATION_FIELDS = [
    'Metadata', 'Review history', 'Version history', 'Source availability', 'Educational summaries',
]

FUTURE_EXPANSION = [
    'Audio recordings', 'Educational podcasts', 'Interactive exhibits', 'Video archives',
    'Oral histories', 'Additional civic education topics',
]

total_archived = es.get('total', 0)
total_planned = sum(c['documents_planned'] for c in COLLECTIONS)
collections_with_content = sum(1 for c in COLLECTIONS if c['documents_archived'] > 0)

library_readiness = min(
    round(
        (total_archived / total_planned * 100) * 0.35
        + (collections_with_content / 7 * 100) * 0.2
        + (es.get('evidence_completeness_pct', 3) or 3) * 0.2
        + 22  # architecture defined
    ),
    22,
)

out = {
    'version': '1.0',
    'build': 37,
    'updated': today,
    'title': 'Master Research Library & Digital Archive v1.0',
    'subtitle': 'Institutional Knowledge Repository',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/research-library.html',
    'public_route': '/library/',
    'canonical_archive_route': '/archive/[collection]/[slug]',
    'current_archive_route': 'Evidence registry + /library/ index',
    'constitution': '/docs/MASTER_RESEARCH_LIBRARY.md',
    'purpose': 'Preserve the documentary record — largest publicly understandable CU knowledge repository.',
    'library_philosophy': 'Presidential library + university research + constitutional archive + civic education museum.',
    'governing_principle': 'Preserve the record from which the story is told — evidence never hidden behind conclusions.',
    'long_term_vision': 'Trace every important claim back to underlying documents and evidence.',
    'master_collections': COLLECTIONS,
    'archive_organization': {
        'id_format': 'LIB-{collection}-{6-digit}',
        'evidence_id_format': 'EV-{6-digit}',
        'fields': ARCHIVE_FIELDS,
        'searchable': True,
        'status': 'partial',
    },
    'relationship_engine': {
        'title': 'Library Relationship Engine',
        'status': 'partial',
        'targets': RELATIONSHIP_TARGETS,
        'evidence_registry': '/data/evidence-registry.json',
        'knowledge_graph': '/data/kg-registry.json',
        'kg_nodes': kg.get('summary', {}).get('total_nodes', 0),
    },
    'research_workspace': {
        'title': 'Research Workspace',
        'status': 'planned',
        'tools': RESEARCH_WORKSPACE,
    },
    'reading_lists': READING_LISTS,
    'digital_preservation': {
        'title': 'Digital Preservation',
        'status': 'partial',
        'fields': PRESERVATION_FIELDS,
        'official_links_maintained': 'partial',
    },
    'search_discovery': {
        'title': 'Search & Discovery',
        'status': 'planned',
        'axes': SEARCH_AXES,
        'note': 'Educational relevance and transparency over keyword matching only.',
    },
    'library_dashboard_metrics': LIBRARY_METRICS,
    'future_expansion': FUTURE_EXPANSION,
    'evidence_alignment': {
        'registry': '/data/evidence-registry.json',
        'items_mapped': total_archived,
        'v1_target': es.get('v1_target', 500),
        'research_gaps': es.get('research_gaps', []),
    },
    'related_systems': [
        {'title': 'Evidence Registry', 'route': '/data/evidence-registry.json', 'build': 10},
        {'title': 'Trust Framework', 'route': '/data/trust-framework.json', 'build': 36},
        {'title': 'Encyclopedia', 'route': '/data/encyclopedia-knowledge-library.json', 'build': 33},
        {'title': 'Research Observatory', 'route': '/mission-control/research-observatory.html', 'build': 29},
        {'title': 'Facts Registry', 'route': '/data/facts-registry.json', 'build': 18},
        {'title': 'Source Library', 'route': '/library/', 'build': 10},
    ],
    'summary': {
        'collections_total': len(COLLECTIONS),
        'documents_archived': total_archived,
        'documents_planned': total_planned,
        'archive_completion_pct': round(total_archived / total_planned * 100, 1),
        'collections_with_content': collections_with_content,
        'reading_lists': len(READING_LISTS),
        'search_axes': len(SEARCH_AXES),
        'workspace_live': False,
        'archive_search_live': False,
        'canonical_routes_live': False,
        'library_readiness_pct': library_readiness,
    },
    'catalog_gaps': [
        'Canonical /archive/[collection]/[slug] routes not built',
        '14/405 planned documents — 3.5% archive completion',
        'Collections C, E, F largely empty — Arkansas and academic gaps',
        'Research workspace (save, bookmark, export) not implemented',
        'Archive search not built — browse via evidence registry only',
        'Oral arguments, briefs, FEC datasets not in archive',
        'Digital preservation version history not per-document',
        'Broken link monitoring not automated',
    ],
    'recommended_next_build': {
        'number': 38,
        'title': 'Component Specifications with Props/States',
        'note': 'Map library collections, archive cards, and reading lists to COMP-* from Build #17.',
    },
}

path = root / 'data/master-research-library.json'
with open(path, 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')
print(f'Research Library: {total_archived}/{total_planned} docs, {library_readiness}% readiness')
