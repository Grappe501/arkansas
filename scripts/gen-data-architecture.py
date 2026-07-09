"""
Generate data/data-architecture.json — Build #51 Master Data Architecture & Canonical Data Dictionary v1.0.
"""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
today = '2026-07-09'


def load_json(path):
    if path.exists():
        with open(path, encoding='utf-8') as f:
            return json.load(f)
    return {}


mc = load_json(root / 'data/mission-control.json')
cdm = load_json(root / 'data/canonical-data-model.json')
rel = load_json(root / 'data/relationship-registry.json')
evidence = load_json(root / 'data/evidence-registry.json')
content = load_json(root / 'data/content-inventory.json')
counties = load_json(root / 'data/arkansas-counties.json')
coalition = load_json(root / 'data/coalition-directory.json')

published = content.get('summary', {}).get('published', 15)
evidence_total = evidence.get('summary', {}).get('total', 14)
counties_total = counties.get('counties_total', 75)
orgs_total = coalition.get('summary', {}).get('total_organizations', 0)
builds_logged = len(mc.get('builds', []))
rel_types = len(rel.get('relationship_types', []))
rel_edges = len(rel.get('edges', []))
canonical_objects = len(cdm.get('canonical_objects', []))

DOMAINS = [
    {
        'id': 'DOM-100', 'number': 100, 'title': 'Identity', 'id_field': 'Person ID',
        'stores': ['Users', 'Education Leaders', 'Researchers', 'Coalition contacts',
                   'Administrators', 'Volunteers', 'Public officials'],
        'status': 'planned',
        'implementation': 'Participant profile schema — no live Person records',
        'route': '/data/participant-profile-schema.json',
        'records': 0,
    },
    {
        'id': 'DOM-200', 'number': 200, 'title': 'Organizations', 'id_field': 'Organization ID',
        'stores': ['Coalition organizations', 'Government agencies', 'Educational institutions',
                   'Libraries', 'Community groups', 'Universities', 'Media organizations'],
        'status': 'planned',
        'implementation': 'Coalition directory — 0 organizations',
        'route': '/data/coalition-directory.json',
        'records': orgs_total,
    },
    {
        'id': 'DOM-300', 'number': 300, 'title': 'Geography', 'id_field': 'Geography ID',
        'stores': ['Arkansas', 'Regions', 'Counties', 'Cities', 'Legislative districts',
                   'Congressional districts', 'ZIP codes', 'Precinct references (future)'],
        'status': 'partial',
        'implementation': f'{counties_total} counties indexed — districts/ZIPs not modeled',
        'route': '/data/arkansas-counties.json',
        'records': counties_total,
    },
    {
        'id': 'DOM-400', 'number': 400, 'title': 'Knowledge', 'id_field': 'Knowledge ID',
        'stores': ['Articles', 'Lessons', 'Encyclopedia entries', 'FAQ entries',
                   'Definitions', 'Learning modules'],
        'status': 'partial',
        'implementation': f'{published} published / ~{content.get("summary", {}).get("total_estimated", 2700)} target',
        'route': '/data/content-inventory.json',
        'records': published,
    },
    {
        'id': 'DOM-500', 'number': 500, 'title': 'Research', 'id_field': 'Research ID',
        'stores': ['Research projects', 'Research notes', 'Source summaries',
                   'Literature reviews', 'Research tasks', 'Research status'],
        'status': 'partial',
        'implementation': 'Research framework + methodology — no Research ID registry',
        'route': '/data/research-framework.json',
        'records': 0,
    },
    {
        'id': 'DOM-600', 'number': 600, 'title': 'Evidence', 'id_field': 'Evidence ID',
        'stores': ['Claims', 'Sources', 'Evidence ratings', 'Verification status',
                   'Citation relationships', 'Review history'],
        'status': 'partial',
        'implementation': f'{evidence_total} evidence records — Evidence Ledger partial',
        'route': '/data/evidence-registry.json',
        'records': evidence_total,
    },
    {
        'id': 'DOM-700', 'number': 700, 'title': 'Law', 'id_field': 'Legal ID',
        'stores': ['Court cases', 'Statutes', 'Regulations', 'Constitutional provisions',
                   'Legislative proposals', 'Ballot initiative concepts'],
        'status': 'planned',
        'implementation': 'Educational halls reference cases — no Legal ID registry',
        'route': '/halls/the-case.html',
        'records': 0,
    },
    {
        'id': 'DOM-800', 'number': 800, 'title': 'Media', 'id_field': 'Media ID',
        'stores': ['Videos', 'Audio', 'Images', 'Infographics', 'Animations',
                   'Presentations', 'PDFs'],
        'status': 'planned',
        'implementation': 'Media Studio designed — 0 media assets catalogued',
        'route': '/mission-control/media-studio.html',
        'records': 0,
    },
    {
        'id': 'DOM-900', 'number': 900, 'title': 'Community', 'id_field': 'Activity ID',
        'stores': ['Community conversations', 'Events', 'Presentations', 'Academy sessions',
                   'Volunteer activities', 'Education Leader activities'],
        'status': 'planned',
        'implementation': '0 Education Leaders · 0 coalition events live',
        'route': '/coalition/events.html',
        'records': 0,
    },
    {
        'id': 'DOM-1000', 'number': 1000, 'title': 'Mission Control', 'id_field': 'Operations ID',
        'stores': ['Projects', 'Builds', 'Tasks', 'Milestones', 'Progress',
                   'Reports', 'Institutional metrics'],
        'status': 'live',
        'implementation': f'{builds_logged} builds logged in mission-control.json',
        'route': '/data/mission-control.json',
        'records': builds_logged,
    },
    {
        'id': 'DOM-1100', 'number': 1100, 'title': 'Analytics', 'id_field': 'Analytics ID',
        'stores': ['Learning progress', 'Search activity', 'Downloads', 'Learning paths',
                   'Resource usage', 'Community engagement'],
        'status': 'planned',
        'implementation': 'No analytics store — static site only',
        'route': None,
        'records': 0,
    },
    {
        'id': 'DOM-1200', 'number': 1200, 'title': 'Relationships', 'id_field': 'Relationship ID',
        'stores': ['Cross-domain edges', 'Knowledge graph links', 'Citation chains',
                   'Geographic associations', 'Institutional connections'],
        'status': 'partial',
        'implementation': f'{rel_types} relationship types defined · {rel_edges} edges recorded',
        'route': '/data/relationship-registry.json',
        'records': rel_edges,
    },
]

CANONICAL_FIELDS = [
    {'field': 'id', 'title': 'Unique ID', 'required': True, 'enforced': 'partial'},
    {'field': 'title', 'title': 'Title', 'required': True, 'enforced': 'partial'},
    {'field': 'description', 'title': 'Description', 'required': True, 'enforced': 'partial'},
    {'field': 'created_date', 'title': 'Created Date', 'required': True, 'enforced': 'partial'},
    {'field': 'updated_date', 'title': 'Updated Date', 'required': True, 'enforced': 'live'},
    {'field': 'status', 'title': 'Status', 'required': True, 'enforced': 'partial'},
    {'field': 'owner', 'title': 'Owner', 'required': False, 'enforced': 'planned'},
    {'field': 'review_date', 'title': 'Review Date', 'required': False, 'enforced': 'planned'},
    {'field': 'tags', 'title': 'Tags', 'required': False, 'enforced': 'planned'},
    {'field': 'relationships', 'title': 'Relationships', 'required': False, 'enforced': 'planned'},
    {'field': 'version', 'title': 'Version', 'required': True, 'enforced': 'partial'},
    {'field': 'visibility', 'title': 'Visibility', 'required': False, 'enforced': 'planned'},
]

METADATA_STANDARDS = [
    {'id': 'META-01', 'field': 'keywords', 'status': 'planned'},
    {'id': 'META-02', 'field': 'reading_level', 'status': 'planned'},
    {'id': 'META-03', 'field': 'topic', 'status': 'partial'},
    {'id': 'META-04', 'field': 'category', 'status': 'partial'},
    {'id': 'META-05', 'field': 'county_relevance', 'status': 'planned'},
    {'id': 'META-06', 'field': 'arkansas_relevance', 'status': 'partial'},
    {'id': 'META-07', 'field': 'educational_level', 'status': 'partial'},
    {'id': 'META-08', 'field': 'review_cycle', 'status': 'planned'},
    {'id': 'META-09', 'field': 'primary_source_availability', 'status': 'partial'},
]

RELATIONSHIP_VERBS = [
    {'verb': 'SUPPORTED_BY', 'description': 'Claim or assertion backed by source/evidence'},
    {'verb': 'RELATED_TO', 'description': 'General associative link between objects'},
    {'verb': 'PRECEDES', 'description': 'Temporal ordering — earlier object'},
    {'verb': 'FOLLOWS', 'description': 'Temporal ordering — later object'},
    {'verb': 'LOCATED_IN', 'description': 'Geographic containment'},
    {'verb': 'MENTORS', 'description': 'Person guides another person'},
    {'verb': 'USES', 'description': 'Object employs another object (e.g. presentation uses video)'},
    {'verb': 'PART_OF', 'description': 'Hierarchical membership'},
    {'verb': 'CITED_BY', 'description': 'Citation inbound reference'},
    {'verb': 'REFERRED_TO', 'description': 'Outbound reference link'},
]

PUBLISHING_STATES = [
    {'state': 'draft', 'order': 1, 'mc_tracked': 'partial'},
    {'state': 'research', 'order': 2, 'mc_tracked': 'partial'},
    {'state': 'review', 'order': 3, 'mc_tracked': 'partial'},
    {'state': 'approved', 'order': 4, 'mc_tracked': 'planned'},
    {'state': 'published', 'order': 5, 'mc_tracked': 'partial'},
    {'state': 'scheduled_review', 'order': 6, 'mc_tracked': 'planned'},
]

API_DOMAINS = [
    {'id': 'API-100', 'name': 'Identity API', 'status': 'planned'},
    {'id': 'API-200', 'name': 'Knowledge API', 'status': 'planned'},
    {'id': 'API-300', 'name': 'Research API', 'status': 'planned'},
    {'id': 'API-400', 'name': 'Evidence API', 'status': 'planned'},
    {'id': 'API-500', 'name': 'Coalition API', 'status': 'planned'},
    {'id': 'API-600', 'name': 'Mission Control API', 'status': 'planned'},
    {'id': 'API-700', 'name': 'Media API', 'status': 'planned'},
    {'id': 'API-800', 'name': 'Analytics API', 'status': 'planned'},
]

SEARCH_INDEX = {
    'status': 'planned',
    'indexed_fields': [
        'title', 'description', 'keywords', 'relationships', 'topics',
        'arkansas_relevance', 'counties', 'organizations', 'people', 'cases', 'sources',
    ],
    'current': 'Static HTML — no search index service',
}

DATABASE_PHILOSOPHY = {
    'normalize': True,
    'denormalize_when': 'Performance requires it only',
    'referential_integrity': 'planned',
    'historical_records': 'partial',
    'current': 'Neon/Prisma documented in Technical Architecture — not provisioned',
    'schema_route': '/data/database-schema.json',
}

domains_live = sum(1 for d in DOMAINS if d['status'] == 'live')
domains_partial = sum(1 for d in DOMAINS if d['status'] == 'partial')
domains_planned = sum(1 for d in DOMAINS if d['status'] == 'planned')
meta_partial = sum(1 for m in METADATA_STANDARDS if m['status'] == 'partial')
meta_planned = sum(1 for m in METADATA_STANDARDS if m['status'] == 'planned')

MC_METRICS = [
    {'id': 'DATA-01', 'title': 'Canonical domains defined', 'status': 'live', 'current': f'{len(DOMAINS)}/12'},
    {'id': 'DATA-02', 'title': 'Domains with live registries', 'status': 'partial', 'current': f'{domains_live} live, {domains_partial} partial'},
    {'id': 'DATA-03', 'title': 'Canonical object fields specified', 'status': 'live', 'current': f'{len(CANONICAL_FIELDS)} fields'},
    {'id': 'DATA-04', 'title': 'Metadata standards enforced', 'status': 'planned', 'current': f'{meta_partial} partial, {meta_planned} planned'},
    {'id': 'DATA-05', 'title': 'Relationship verbs institutional', 'status': 'live', 'current': f'{len(RELATIONSHIP_VERBS)} verbs + {rel_types} legacy types'},
    {'id': 'DATA-06', 'title': 'Relationship edges recorded', 'status': 'planned', 'current': f'{rel_edges} edges'},
    {'id': 'DATA-07', 'title': 'Publishing state machine', 'status': 'partial', 'current': '6 states defined — partial MC tracking'},
    {'id': 'DATA-08', 'title': 'Search index operational', 'status': 'planned', 'current': 'No index service'},
    {'id': 'DATA-09', 'title': 'Domain APIs deployed', 'status': 'planned', 'current': '0/8 APIs'},
    {'id': 'DATA-10', 'title': 'Database provisioned', 'status': 'planned', 'current': 'Schema blueprint only'},
    {'id': 'DATA-11', 'title': 'Knowledge assets (Domain 400)', 'status': 'partial', 'current': str(published)},
    {'id': 'DATA-12', 'title': 'Evidence records (Domain 600)', 'status': 'partial', 'current': str(evidence_total)},
    {'id': 'DATA-13', 'title': 'County coverage (Domain 300)', 'status': 'partial', 'current': f'{counties_total} counties · 0 with participants'},
    {'id': 'DATA-14', 'title': 'Institutional data health score', 'status': 'partial', 'current': 'See summary.data_architecture_readiness_pct'},
]

readiness_factors = [
    100,  # constitution defined
    (domains_live * 100 + domains_partial * 45) / len(DOMAINS),
    min(100, canonical_objects / 12 * 100),  # build 15 objects vs 12 domains
    (meta_partial * 50) / len(METADATA_STANDARDS),
    50 if rel_types else 0,  # types defined
    0 if rel_edges == 0 else 80,
    35,  # publishing states partial
    0,   # search
    0,   # APIs
    25,  # database schema only
    100,  # MC dashboard after this build
]
data_architecture_readiness = round(sum(readiness_factors) / len(readiness_factors))

out = {
    'version': '1.0',
    'build': 51,
    'updated': today,
    'title': 'Master Data Architecture & Canonical Data Dictionary v1.0',
    'subtitle': 'The Institutional Data Constitution',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/data-architecture.html',
    'constitution': '/docs/MASTER_DATA_ARCHITECTURE.md',
    'purpose': 'How the institution thinks about information — single source of truth for every person, place, idea, and document.',
    'governing_principle': (
        'One integrated knowledge institution — never a collection of disconnected databases. '
        'Every object exists once and is referenced everywhere else.'
    ),
    'data_philosophy': {
        'wrong_question': 'Where else did we write this?',
        'right_question': 'Where is the single source of truth?',
        'rules': ['No duplication', 'No conflicting versions', 'No disconnected data'],
    },
    'extends': [
        {'title': 'Canonical Data Model', 'build': 15, 'route': '/data/canonical-data-model.json'},
        {'title': 'Database Schema', 'build': 22, 'route': '/data/database-schema.json'},
        {'title': 'Knowledge Graph', 'build': 11, 'route': '/data/knowledge-graph.json'},
        {'title': 'Technical Architecture', 'build': 48, 'route': '/data/technical-architecture.json'},
        {'title': 'Master Build Bible', 'build': 50, 'route': '/data/build-bible.json'},
    ],
    'canonical_domains': {
        'title': 'Twelve Canonical Data Domains',
        'domains': DOMAINS,
        'domains_total': len(DOMAINS),
        'domains_live': domains_live,
        'domains_partial': domains_partial,
        'domains_planned': domains_planned,
    },
    'canonical_object_model': {
        'title': 'Shared Object Structure',
        'fields': CANONICAL_FIELDS,
        'fields_total': len(CANONICAL_FIELDS),
        'note': 'Build #15 canonical objects map into domains 100–900; MC objects map to domain 1000.',
        'legacy_objects': canonical_objects,
        'legacy_route': '/data/canonical-data-model.json',
    },
    'metadata_standards': {
        'title': 'Required Metadata',
        'fields': METADATA_STANDARDS,
        'enforcement': 'planned',
        'mc_dependency': 'Mission Control reporting requires high-quality metadata on all published objects.',
    },
    'relationship_standards': {
        'title': 'Institutional Relationship Verbs',
        'principle': 'Relationships never hardcoded — structured data only',
        'verbs': RELATIONSHIP_VERBS,
        'legacy_types': rel_types,
        'edges_recorded': rel_edges,
        'registry_route': '/data/relationship-registry.json',
        'knowledge_graph_route': '/mission-control/knowledge-graph.html',
    },
    'versioning': {
        'chain': ['Current Version', 'Historical Versions', 'Revision Notes', 'Review History', 'Publication History'],
        'status': 'partial',
        'current': 'Git + VERSION + CHANGELOG for repo; per-object versioning not unified',
    },
    'publishing_states': {
        'title': 'Publication Lifecycle',
        'states': PUBLISHING_STATES,
        'flow': 'Draft → Research → Review → Approved → Published → Scheduled Review',
    },
    'search_index': SEARCH_INDEX,
    'api_philosophy': {
        'principle': 'Future systems never access raw data directly — documented services only',
        'apis': API_DOMAINS,
        'apis_deployed': 0,
    },
    'database_philosophy': DATABASE_PHILOSOPHY,
    'mc_data_dashboard': {
        'title': 'Institutional Data Health',
        'reports': [
            'Objects created', 'Relationships created', 'Evidence records', 'Research records',
            'Knowledge assets', 'Media assets', 'County coverage', 'Community activity',
            'Overall institutional data health',
        ],
        'current_counts': {
            'knowledge_published': published,
            'evidence_records': evidence_total,
            'counties_indexed': counties_total,
            'organizations': orgs_total,
            'relationship_edges': rel_edges,
            'builds_logged': builds_logged,
            'media_assets': 0,
            'education_leaders': 0,
        },
    },
    'future_expansion': [
        'Additional civic education topics',
        'New Arkansas initiatives',
        'Expanded research collections',
        'Future AI capabilities',
        'Additional states (if ever desired)',
    ],
    'long_term_vision': (
        'Whether the platform contains 5,000 records or 5 million, every piece of information '
        'fits the same coherent structure. Future developers immediately understand how the '
        'institution thinks about knowledge.'
    ),
    'mc_integration': {
        'title': 'Mission Control Data Architecture Metrics',
        'status': 'partial',
        'metrics': MC_METRICS,
        'authoritative_reference': True,
    },
    'related_blueprints': [
        {'title': 'Canonical Data Model (Build #15)', 'route': '/mission-control/data-model.html', 'build': 15},
        {'title': 'Database Schema (Build #22)', 'route': '/mission-control/database.html', 'build': 22},
        {'title': 'Knowledge Graph (Build #11)', 'route': '/mission-control/knowledge-graph.html', 'build': 11},
        {'title': 'Systems Integration (Build #45)', 'route': '/mission-control/systems-integration.html', 'build': 45},
        {'title': 'Technical Architecture (Build #48)', 'route': '/mission-control/technical-architecture.html', 'build': 48},
    ],
    'summary': {
        'domains_total': len(DOMAINS),
        'domains_live': domains_live,
        'domains_partial': domains_partial,
        'domains_planned': domains_planned,
        'canonical_fields': len(CANONICAL_FIELDS),
        'metadata_fields': len(METADATA_STANDARDS),
        'relationship_verbs': len(RELATIONSHIP_VERBS),
        'relationship_types_legacy': rel_types,
        'relationship_edges': rel_edges,
        'publishing_states': len(PUBLISHING_STATES),
        'apis_defined': len(API_DOMAINS),
        'apis_deployed': 0,
        'search_index_live': False,
        'database_provisioned': False,
        'knowledge_published': published,
        'evidence_records': evidence_total,
        'counties_indexed': counties_total,
        'builds_logged': builds_logged,
        'data_architecture_readiness_pct': data_architecture_readiness,
    },
    'catalog_gaps': [
        '0 relationship edges recorded — schema ready, graph empty',
        '0/8 domain APIs deployed — philosophy documented only',
        'No search index service — static HTML site',
        'Neon/Prisma database not provisioned — schema blueprint from Build #22',
        'Build #15 canonical objects (10 types) predate 12-domain model — mapping documented, migration pending',
        'Metadata standards defined — not enforced on published content',
        'Domain 700 Law — no Legal ID registry despite educational hall content',
        'Domain 800 Media — 0 catalogued media assets',
        'Domain 900 Community — 0 Education Leaders, 0 coalition orgs, 0 events',
        'Domain 1100 Analytics — no learning progress or engagement store',
        'Unified Person ID / Knowledge ID / Legal ID issuance not operational',
        'Publishing state machine partial — approved and scheduled_review not tracked in MC',
    ],
    'recommended_next_build': {
        'number': 52,
        'title': 'Master Implementation Roadmap & Sprint Zero',
        'note': 'Neon/Prisma provisioning, COMP-* specs, first domain API, relationship edge pilot, Sprint backlog from Build Bible phases A–E.',
    },
}

path = root / 'data/data-architecture.json'
with open(path, 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')
print(
    f'Data Architecture: {domains_live} live + {domains_partial} partial domains, '
    f'{rel_edges} edges, {data_architecture_readiness}% readiness'
)
