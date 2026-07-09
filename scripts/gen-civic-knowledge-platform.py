"""
Generate data/civic-knowledge-platform.json — Build #93.
Master Arkansas Civic Data Warehouse & Knowledge Platform — One Source of Truth v1.0.
"""
import json
from datetime import date
from pathlib import Path

root = Path(__file__).resolve().parents[1]
today = '2026-07-09'
completion_target_date = '2027-01-01'
completion_target = date(2027, 1, 1)
today_date = date(2026, 7, 9)
days_remaining = max((completion_target - today_date).days, 0)


def load_json(path):
    if path.exists():
        with open(path, encoding='utf-8') as f:
            return json.load(f)
    return {}


mc = load_json(root / 'data/mission-control.json')
lb = load_json(root / 'data/localbrain-architecture.json')
kg = load_json(root / 'data/kg-registry.json')

ex = mc.get('executive', {})

# Honest operational metrics
unified_search_live = False
platform_dashboard_live = False
canonical_records_enforced = False
duplicate_records_tracked = 0
knowledge_gaps_identified = 14
ai_retrieval_quality_pct = 0
search_queries = 0

FOUR_LAYERS = [
    {
        'layer': 1,
        'name': 'Structured Data',
        'description': 'Counties, cities, volunteers, organizations, events, citations, projects, tasks, calendars',
        'status': 'partial',
    },
    {
        'layer': 2,
        'name': 'Institutional Knowledge',
        'description': 'Articles, research, policies, manuals, training, notes, presentations, lessons, archives',
        'status': 'partial',
    },
    {
        'layer': 3,
        'name': 'Relationship Graph',
        'description': 'People, projects, research, organizations, geography, documents, events connected',
        'status': 'partial',
    },
    {
        'layer': 4,
        'name': 'Institutional Intelligence',
        'description': 'AI interprets underlying information — answers institutional questions',
        'status': 'planned',
    },
]

STRUCTURED_DATA_TYPES = [
    {'id': 'SD-01', 'type': 'Counties', 'route': '/data/arkansas-counties.json', 'canonical': False, 'records': 75},
    {'id': 'SD-02', 'type': 'Cities', 'route': '/data/arkansas-cities.json', 'canonical': False, 'records': 250},
    {'id': 'SD-03', 'type': 'Neighborhoods', 'route': '/data/neighborhood-profiles.json', 'canonical': False, 'records': 0},
    {'id': 'SD-04', 'type': 'Education Leaders', 'canonical': False, 'records': 0},
    {'id': 'SD-05', 'type': 'Volunteers', 'canonical': False, 'records': 0},
    {'id': 'SD-06', 'type': 'Organizations', 'route': '/data/coalition-directory.json', 'canonical': False, 'records': 0},
    {'id': 'SD-07', 'type': 'Events', 'canonical': False, 'records': 0},
    {'id': 'SD-08', 'type': 'Research citations', 'route': '/data/evidence-registry.json', 'canonical': False, 'records': 14},
    {'id': 'SD-09', 'type': 'Projects', 'canonical': False, 'records': len(mc.get('builds', []))},
    {'id': 'SD-10', 'type': 'Tasks', 'canonical': False, 'records': 0},
    {'id': 'SD-11', 'type': 'Calendars', 'canonical': False, 'records': 0},
]

INSTITUTIONAL_KNOWLEDGE_TYPES = [
    'Articles', 'Research papers', 'Policies', 'Operating manuals',
    'Training materials', 'Meeting notes', 'Presentations', 'Lesson plans', 'Historical archives',
]

CANONICAL_RECORD_TYPES = [
    'County record', 'City record', 'Education Leader record', 'Organization record',
    'Research citation', 'Article', 'Project', 'Lesson',
]

VERSION_CONTROL_FIELDS = [
    'Current version', 'Previous versions', 'Revision history',
    'Editor', 'Approval status', 'Review schedule',
]

SEARCH_CATEGORIES = [
    'Research', 'Articles', 'People', 'Organizations', 'Projects',
    'Lessons', 'Meetings', 'Events', 'Policies', 'Operating manuals',
]

KNOWLEDGE_LIFECYCLE = [
    {'stage': 'Draft', 'status': 'specified'},
    {'stage': 'Review', 'status': 'specified'},
    {'stage': 'Approved', 'status': 'specified'},
    {'stage': 'Published', 'status': 'partial'},
    {'stage': 'Archived', 'status': 'planned'},
    {'stage': 'Historical Record', 'status': 'planned'},
]

DATA_GOVERNANCE_FIELDS = [
    'Owner', 'Purpose', 'Source', 'Update schedule',
    'Validation rules', 'Privacy classification', 'Retention policy',
]

EXECUTIVE_INTELLIGENCE_QUESTIONS = [
    'Which counties are missing Education Leaders?',
    'Which research topics need updating?',
    'Where are coalition gaps?',
    'Which volunteers have specialized expertise?',
    'What documents are overdue for review?',
]

ACCESS_LEVELS = [
    {'level': 'public', 'label': 'Public educational resources'},
    {'level': 'volunteer', 'label': 'Volunteer-only resources'},
    {'level': 'leadership', 'label': 'Leadership materials'},
    {'level': 'administrative', 'label': 'Administrative documents'},
    {'level': 'sensitive', 'label': 'Sensitive operational information'},
]

AI_INTEGRATION_BENEFITS = [
    'Consistent answers', 'Current information', 'Shared institutional memory',
    'Reduced duplication', 'Higher trust',
]

PLATFORM_DASHBOARD_INDICATORS = [
    {'id': 'KP-D01', 'indicator': 'Knowledge growth', 'current': 0, 'status': 'planned'},
    {'id': 'KP-D02', 'indicator': 'Research growth', 'current': 14, 'status': 'partial'},
    {'id': 'KP-D03', 'indicator': 'Document health', 'current': 0, 'unit': '%', 'status': 'planned'},
    {'id': 'KP-D04', 'indicator': 'Review status', 'current': 0, 'status': 'planned'},
    {'id': 'KP-D05', 'indicator': 'Search usage', 'current': search_queries, 'status': 'planned'},
    {'id': 'KP-D06', 'indicator': 'AI retrieval quality', 'current': ai_retrieval_quality_pct, 'unit': '%', 'status': 'planned'},
    {'id': 'KP-D07', 'indicator': 'Duplicate records', 'current': duplicate_records_tracked, 'status': 'planned'},
    {'id': 'KP-D08', 'indicator': 'Knowledge gaps', 'current': knowledge_gaps_identified, 'status': 'partial'},
    {'id': 'KP-D09', 'indicator': 'Institutional completeness', 'current': ex.get('overall_completion', mc.get('build', 92)), 'unit': '%', 'status': 'partial'},
]

kg_nodes = kg.get('summary', {}).get('nodes_total', 0) if kg else 0
kg_edges = kg.get('summary', {}).get('edges_total', 0) if kg else 0

civic_knowledge_platform_readiness = min(
    66,
    14
    + len(FOUR_LAYERS)
    + len(STRUCTURED_DATA_TYPES) // 2
    + len(INSTITUTIONAL_KNOWLEDGE_TYPES) // 2
    + len(CANONICAL_RECORD_TYPES) // 2
    + len(VERSION_CONTROL_FIELDS) // 2
    + len(SEARCH_CATEGORIES) // 2
    + len(KNOWLEDGE_LIFECYCLE)
    + len(DATA_GOVERNANCE_FIELDS) // 2
    + len(EXECUTIVE_INTELLIGENCE_QUESTIONS) // 2
    + len(ACCESS_LEVELS) // 2
    + len(PLATFORM_DASHBOARD_INDICATORS) // 2
    + len(AI_INTEGRATION_BENEFITS) // 2
    + (2 if platform_dashboard_live else 0),
)

out = {
    'version': '1.0',
    'build': 93,
    'updated': today,
    'completion_target_date': completion_target_date,
    'title': 'Master Arkansas Civic Data Warehouse & Knowledge Platform v1.0',
    'subtitle': 'One Source of Truth',
    'tagline': 'The Institutional Intelligence Backbone',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/civic-knowledge-platform.html',
    'constitution': '/docs/MASTER_CIVIC_DATA_WAREHOUSE_KNOWLEDGE_PLATFORM.md',
    'purpose': (
        'Single institutional data and knowledge platform — authoritative source for every '
        'system. Every LocalBrain reads from it, Mission Control monitors it, AI learns from '
        'it, volunteers contribute to it. One source of truth.'
    ),
    'governing_principle': (
        'Information becomes wisdom only when it is organized. Organized knowledge becomes '
        'institutional intelligence. Institutional intelligence becomes better decisions. '
        'Better decisions strengthen public trust. The Knowledge Platform is the intellectual '
        'foundation upon which the entire institution is built.'
    ),
    'founders_principle': (
        'The institution should never waste volunteer time searching for information that '
        'already exists. Knowledge should be organized once and reused everywhere. The platform '
        'becomes the collective memory — each generation begins where the previous left off.'
    ),
    'institutional_philosophy': {
        'title': 'Institutional Philosophy',
        'exist_once_maintain_once': True,
        'may_appear_many_places': True,
        'eliminates_duplication_confusion_inconsistency': True,
    },
    'four_layers': {
        'title': 'The Four Layers',
        'layers': FOUR_LAYERS,
        'connected_platform': True,
    },
    'structured_data': {
        'title': 'Layer One — Structured Data',
        'types': STRUCTURED_DATA_TYPES,
        'stored_in_databases': True,
        'unified_warehouse': False,
        'status': 'partial',
        'note': 'Data exists in JSON registries — not unified warehouse DB',
    },
    'institutional_knowledge': {
        'title': 'Layer Two — Institutional Knowledge',
        'types': INSTITUTIONAL_KNOWLEDGE_TYPES,
        'preserves_institutional_memory': True,
        'status': 'partial',
    },
    'relationship_graph': {
        'title': 'Layer Three — Relationship Graph',
        'connects': [
            'People', 'Projects', 'Research', 'Organizations',
            'Counties', 'Cities', 'Documents', 'Events',
        ],
        'nodes': kg_nodes,
        'edges': kg_edges,
        'mc_visualizes': True,
        'status': 'partial',
        'route': '/mission-control/knowledge-graph.html',
    },
    'institutional_intelligence': {
        'title': 'Layer Four — Institutional Intelligence',
        'ai_interprets_not_replaces': True,
        'example_questions': [
            'What counties need help?',
            'What research supports this lesson?',
            'What projects are blocked?',
            'What organizations operate in this county?',
            'What community conversations occurred this month?',
        ],
        'useful_because_data_organized': True,
        'status': 'planned',
    },
    'canonical_records': {
        'title': 'Canonical Records',
        'record_types': CANONICAL_RECORD_TYPES,
        'everything_references_canonical': True,
        'enforced': canonical_records_enforced,
        'status': 'planned',
    },
    'version_control': {
        'title': 'Version Control',
        'fields': VERSION_CONTROL_FIELDS,
        'nothing_disappears': True,
        'status': 'partial',
        'note': 'Git history for code/docs — not unified doc version registry',
    },
    'search_everything': {
        'title': 'Search Everything',
        'categories': SEARCH_CATEGORIES,
        'unified_search_experience': True,
        'live': unified_search_live,
        'status': 'planned',
    },
    'knowledge_lifecycle': {
        'title': 'Knowledge Lifecycle',
        'stages': KNOWLEDGE_LIFECYCLE,
        'mc_tracks_every_stage': True,
        'status': 'specified',
    },
    'data_governance': {
        'title': 'Data Governance',
        'fields': DATA_GOVERNANCE_FIELDS,
        'data_stewardship_institutional_practice': True,
        'status': 'specified',
    },
    'executive_intelligence': {
        'title': 'Executive Intelligence',
        'questions': EXECUTIVE_INTELLIGENCE_QUESTIONS,
        'leadership_answers_in_seconds': True,
        'status': 'planned',
    },
    'ai_integration': {
        'title': 'AI Integration',
        'localbrains_retrieve_not_copy': True,
        'benefits': AI_INTEGRATION_BENEFITS,
        'reliable_because_knowledge_reliable': True,
        'status': 'planned',
    },
    'public_vs_internal': {
        'title': 'Public vs Internal Knowledge',
        'access_levels': ACCESS_LEVELS,
        'every_record_has_access_level': True,
        'status': 'specified',
    },
    'mission_control_dashboard': {
        'title': 'Mission Control Dashboard',
        'indicators': PLATFORM_DASHBOARD_INDICATORS,
        'live': platform_dashboard_live,
        'knowledge_base_health_at_glance': True,
        'status': 'planned',
    },
    'integration': {
        'chain': (
            'Mission Control → LocalBrains → Digital Twin → Academy → Research Institute → '
            'Operating Manual → Volunteer Network → Communications → County/City/Neighborhood OS'
        ),
        'informational_foundation': True,
        'systems': [
            {'system': 'LocalBrain Architecture (#92)', 'route': '/mission-control/localbrain-architecture.html', 'status': 'live'},
            {'system': 'Knowledge Graph', 'route': '/mission-control/knowledge-graph.html', 'status': 'partial'},
            {'system': 'Data Architecture (#51)', 'route': '/mission-control/data-architecture.html', 'status': 'live'},
            {'system': 'Database Schema (#22)', 'route': '/mission-control/database.html', 'status': 'live'},
            {'system': 'Research Library', 'route': '/mission-control/research-library.html', 'status': 'partial'},
            {'system': 'Evidence Ledger', 'route': '/mission-control/evidence-ledger.html', 'status': 'partial'},
        ],
    },
    'long_term_vision': (
        'By January 2027, every volunteer knows there is exactly one place for the '
        'institution\'s most current knowledge. Every article, citation, lesson, project, '
        'organization, calendar, policy, and decision — connected, searchable, trustworthy.'
    ),
    'summary': {
        'completion_target_date': completion_target_date,
        'days_remaining': days_remaining,
        'civic_knowledge_platform_readiness_pct': civic_knowledge_platform_readiness,
        'localbrain_architecture_readiness_pct': lb.get('summary', {}).get('localbrain_architecture_readiness_pct', 60),
        'unified_search_live': unified_search_live,
        'platform_dashboard_live': platform_dashboard_live,
        'canonical_records_enforced': canonical_records_enforced,
        'duplicate_records_tracked': duplicate_records_tracked,
        'knowledge_gaps_identified': knowledge_gaps_identified,
        'structured_data_types': len(STRUCTURED_DATA_TYPES),
        'relationship_graph_nodes': kg_nodes,
        'relationship_graph_edges': kg_edges,
        'ai_retrieval_quality_pct': ai_retrieval_quality_pct,
        'search_queries': search_queries,
        'institutional_completion_pct': ex.get('overall_completion', mc.get('build', 92)),
    },
    'catalog_gaps': [
        'No unified warehouse database — data scattered in JSON registries',
        'Unified search not live',
        'Canonical records not enforced — duplicates possible',
        'Knowledge lifecycle not tracked in MC',
        'Data governance metadata missing on most datasets',
        'Platform dashboard not live',
        'AI retrieval quality not measured',
        'Relationship graph partial — not all entities linked',
        'Version control for docs not centralized',
        'Access levels not enforced per record',
        'Executive intelligence queries not operational',
    ],
    'recommended_next_build': {
        'number': 94,
        'title': 'Executive War Room & Countdown Dashboard Components',
        'note': (
            'War room UI, unified search, canonical record registry, knowledge lifecycle '
            'tracker, platform health dashboard, COMP-* specs.'
        ),
    },
}

with open(root / 'data/civic-knowledge-platform.json', 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')

print(
    f'Civic Knowledge Platform: {len(STRUCTURED_DATA_TYPES)} data types, '
    f'{kg_nodes} KG nodes, {civic_knowledge_platform_readiness}% readiness'
)
