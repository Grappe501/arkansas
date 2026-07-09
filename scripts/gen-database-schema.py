"""
Generate data/database-schema.json — Build #22 Database Schema & ERD Blueprint v1.0.
"""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
today = '2026-07-09'

def entity(eid, table, title, fields, relationships, storage='planned', canonical_id=None):
    return {
        'id': eid,
        'table': table,
        'title': title,
        'fields': fields,
        'relationships': relationships,
        'storage_status': storage,
        'canonical_model_id': canonical_id,
    }

entities = [
    entity('person', 'people', 'Person', [
        'id', 'first_name', 'last_name', 'email', 'phone', 'city', 'county', 'zip',
        'role_interest', 'experience_level', 'learning_stage', 'signup_source',
        'created_at', 'updated_at'
    ], [
        'Belongs to Organizations (M:N via person_organizations)',
        'Attends Events', 'Downloads Resources', 'Submits Ideas',
        'Invites People', 'May become Education Leader'
    ], 'partial', 'person'),
    entity('organization', 'organizations', 'Organization', [
        'id', 'name', 'organization_type', 'website', 'city', 'county', 'service_area',
        'primary_contact_name', 'primary_contact_email', 'primary_contact_phone',
        'partnership_level', 'public_profile_enabled', 'status', 'created_at', 'updated_at'
    ], [
        'Has many People', 'Hosts Events', 'Downloads Resources',
        'Coalition Sign-On', 'Refers Organizations'
    ], 'partial', 'organization'),
    entity('county', 'counties', 'County', [
        'id', 'name', 'region', 'population', 'status',
        'education_leader_count', 'organization_count', 'event_count', 'last_activity_at'
    ], [
        'Has People, Organizations, Events', 'Has Public Officials', 'Mission Control metrics'
    ], 'live', 'county'),
    entity('event', 'events', 'Event', [
        'id', 'title', 'event_type', 'host_person_id', 'host_organization_id',
        'county', 'city', 'location', 'start_time', 'end_time', 'public_event',
        'estimated_attendance', 'actual_attendance', 'status', 'created_at', 'updated_at'
    ], [
        'Belongs to County', 'Hosted by Person or Organization',
        'Uses Resources', 'Creates follow-up Signups'
    ], 'partial', 'event'),
    entity('educational_resource', 'educational_resources', 'Educational Resource', [
        'id', 'mrid', 'title', 'resource_type', 'parent_section', 'difficulty_level',
        'reading_time', 'download_url', 'public_url', 'status', 'source_count',
        'last_reviewed_at', 'created_at', 'updated_at'
    ], [
        'Cites Sources', 'Supports Events', 'Downloaded by People',
        'Shared with Public Officials', 'Belongs to Learning Path'
    ], 'partial', 'educational_resource'),
    entity('source', 'sources', 'Source', [
        'id', 'evidence_id', 'title', 'author', 'publisher', 'publication_date',
        'source_type', 'source_tier', 'url', 'archive_url', 'summary',
        'review_status', 'created_at', 'updated_at'
    ], [
        'Supports Facts, Resources, Charts', 'Supports Model Laws and Ballot Concepts'
    ], 'partial', 'research_object'),
    entity('fact', 'facts', 'Fact', [
        'id', 'fact_id', 'short_statement', 'plain_language_explanation',
        'detailed_explanation', 'category', 'verification_status',
        'last_verified_at', 'created_at', 'updated_at'
    ], [
        'Has many Sources', 'Appears in Resources', 'Supports Timeline and Charts'
    ], 'partial', None),
    entity('signup', 'signups', 'Signup', [
        'id', 'person_id', 'signup_type', 'interest_area', 'message',
        'source_page', 'status', 'assigned_to', 'created_at', 'updated_at'
    ], ['Links to Person'], 'partial', None),
    entity('referral', 'referrals', 'Referral', [
        'id', 'referrer_person_id', 'referred_name', 'referred_email',
        'relationship_type', 'shared_resource_id', 'message', 'status', 'created_at'
    ], [
        'Belongs to Person', 'May connect Resource', 'May create new Person'
    ], 'planned', None),
    entity('public_official', 'public_officials', 'Public Official', [
        'id', 'name', 'office', 'jurisdiction', 'district', 'level', 'party',
        'public_contact_url', 'public_email', 'phone', 'status', 'last_verified_at'
    ], [
        'Represents Counties', 'Receives Educational Packets', 'Relates to Model Laws'
    ], 'planned', 'public_official'),
    entity('educational_packet_share', 'educational_packet_shares', 'Educational Packet Share', [
        'id', 'person_id', 'public_official_id', 'resource_id', 'packet_type',
        'delivery_method', 'message', 'status', 'created_at'
    ], ['Person shares Resource with Public Official'], 'planned', None),
    entity('model_law_concept', 'model_law_concepts', 'Model Law Concept', [
        'id', 'title', 'jurisdiction_level', 'summary', 'problem_statement',
        'draft_text', 'legal_questions', 'research_status', 'review_status',
        'created_by_person_id', 'created_at', 'updated_at'
    ], [
        'Cites Sources', 'Shared with Public Officials', 'Relates to Ballot Concepts'
    ], 'stub', 'model_law'),
    entity('ballot_initiative_concept', 'ballot_initiative_concepts', 'Ballot Initiative Concept', [
        'id', 'title', 'summary', 'problem_statement', 'draft_language',
        'constitutional_questions', 'statutory_questions', 'research_status',
        'review_status', 'created_by_person_id', 'created_at', 'updated_at'
    ], [
        'Cites Sources', 'Relates to Model Laws', 'Has Contributors'
    ], 'stub', 'ballot_initiative_concept'),
    entity('coalition_sign_on', 'coalition_sign_ons', 'Coalition Sign-On', [
        'id', 'organization_id', 'contact_person_id', 'participation_level',
        'public_support_statement', 'resources_requested', 'status',
        'created_at', 'updated_at'
    ], ['Organization joins coalition via contact Person'], 'partial', None),
    entity('mc_build_record', 'mc_build_records', 'Mission Control Build Record', [
        'id', 'build_number', 'title', 'phase', 'status', 'completion_percentage',
        'summary', 'files_created', 'files_modified', 'risks', 'next_build',
        'created_at', 'updated_at'
    ], ['Tracked in mission-control.json builds array'], 'live', None),
]

join_tables = [
    {'table': 'person_organizations', 'from': 'person', 'to': 'organization', 'status': 'planned'},
    {'table': 'event_resources', 'from': 'event', 'to': 'educational_resource', 'status': 'planned'},
    {'table': 'resource_sources', 'from': 'educational_resource', 'to': 'source', 'status': 'partial'},
    {'table': 'fact_sources', 'from': 'fact', 'to': 'source', 'status': 'partial'},
    {'table': 'resource_facts', 'from': 'educational_resource', 'to': 'fact', 'status': 'planned'},
    {'table': 'county_public_officials', 'from': 'county', 'to': 'public_official', 'status': 'planned'},
    {'table': 'model_law_sources', 'from': 'model_law_concept', 'to': 'source', 'status': 'planned'},
    {'table': 'ballot_initiative_sources', 'from': 'ballot_initiative_concept', 'to': 'source', 'status': 'planned'},
    {'table': 'person_events', 'from': 'person', 'to': 'event', 'status': 'planned'},
    {'table': 'organization_events', 'from': 'organization', 'to': 'event', 'status': 'planned'},
]

signup_types = [
    'Education Leader', 'Contact Network', 'Research Volunteer', 'Event Host',
    'Coalition Interest', 'Public Official Sharing', 'Model Law Contributor',
    'Ballot Initiative Contributor'
]

storage_strategy = {
    'v1_current': [
        {'method': 'Static JSON files', 'status': 'live', 'examples': ['data/mission-control.json', 'data/facts-registry.json']},
        {'method': 'Netlify Forms', 'status': 'partial', 'examples': ['educate/index.html']},
        {'method': 'Git-tracked registries', 'status': 'live', 'examples': ['data/evidence-registry.json']},
        {'method': 'Manual CSV exports', 'status': 'planned'},
        {'method': 'localStorage session', 'status': 'live', 'examples': ['js/journey.js']},
    ],
    'v2_future': [
        {'method': 'Postgres', 'status': 'planned'},
        {'method': 'Supabase', 'status': 'planned', 'note': 'Auth, RLS, realtime'},
        {'method': 'Neon', 'status': 'planned'},
        {'method': 'Serverless API routes', 'status': 'planned'},
        {'method': 'Authenticated admin dashboard', 'status': 'planned'},
    ]
}

mc_metrics = [
    {'id': 'total_people', 'title': 'Total people', 'source': 'people', 'current': 0},
    {'id': 'education_leaders', 'title': 'Education leaders', 'source': 'people', 'current': 0},
    {'id': 'coalition_orgs', 'title': 'Coalition organizations', 'source': 'organizations', 'current': 0},
    {'id': 'counties_represented', 'title': 'Counties represented', 'source': 'counties', 'current': 0},
    {'id': 'counties_inactive', 'title': 'Counties with no activity', 'source': 'counties', 'current': 75},
    {'id': 'events_hosted', 'title': 'Events hosted', 'source': 'events', 'current': 0},
    {'id': 'resource_downloads', 'title': 'Resource downloads', 'source': 'educational_resources', 'current': 0},
    {'id': 'referrals_sent', 'title': 'Referrals sent', 'source': 'referrals', 'current': 0},
    {'id': 'official_shares', 'title': 'Public official shares', 'source': 'educational_packet_shares', 'current': 0},
    {'id': 'model_law_submissions', 'title': 'Model law submissions', 'source': 'model_law_concepts', 'current': 0},
    {'id': 'ballot_submissions', 'title': 'Ballot initiative submissions', 'source': 'ballot_initiative_concepts', 'current': 0},
    {'id': 'research_completeness', 'title': 'Research completeness', 'source': 'sources', 'current': 3},
    {'id': 'content_completion', 'title': 'Content completion', 'source': 'educational_resources', 'current': 12},
    {'id': 'deployment_readiness', 'title': 'Deployment readiness', 'source': 'mc_build_records', 'current': 8},
]

by_storage = {}
for e in entities:
    by_storage[e['storage_status']] = by_storage.get(e['storage_status'], 0) + 1

out = {
    'version': '1.0',
    'build': 22,
    'updated': today,
    'title': 'Database Schema & Entity Relationship Blueprint v1.0',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/database.html',
    'constitution': '/docs/DATABASE_SCHEMA.md',
    'erd_diagram': 'mermaid',
    'purpose': 'Turn civic education activity into an organized, measurable Arkansas learning network.',
    'philosophy_questions': [
        'Who is learning?', 'What are they learning?', 'Where are they located?',
        'What resources are they using?', 'Who are they connected to?',
        'What organizations are participating?', 'What counties are active?',
        'What public officials are being educated?', 'What research supports the platform?'
    ],
    'privacy_principle': 'Collect only what is needed. Protect participant data. Distinguish public vs private org fields.',
    'governing_principle': 'Map the growth of Arkansas civic education — not merely store contacts.',
    'entities': entities,
    'entity_count': len(entities),
    'join_tables': join_tables,
    'join_table_count': len(join_tables),
    'signup_types': signup_types,
    'storage_strategy': storage_strategy,
    'mission_control_metrics': mc_metrics,
    'canonical_model': {
        'build': 15,
        'route': '/mission-control/data-model.html',
        'objects_in_canonical': 10,
        'objects_in_schema': len(entities),
        'new_entities': ['fact', 'signup', 'referral', 'educational_packet_share', 'coalition_sign_on', 'mc_build_record'],
        'relationship_registry': '/data/relationship-registry.json',
        'relationship_types': 20
    },
    'integrations': [
        {'system': 'Facts Framework', 'build': 18, 'entity': 'fact', 'route': '/mission-control/facts.html'},
        {'system': 'Evidence Registry', 'build': 10, 'entity': 'source', 'route': '/mission-control/research.html'},
        {'system': 'Content Inventory', 'build': 6, 'entity': 'educational_resource', 'route': '/mission-control/inventory.html'},
        {'system': 'Coalition', 'build': 14, 'entities': ['organization', 'coalition_sign_on'], 'route': '/mission-control/coalition.html'},
        {'system': 'Repository Blueprint', 'build': 21, 'note': 'Future src/data/ tables', 'route': '/mission-control/repository.html'},
    ],
    'summary': {
        'entities': len(entities),
        'join_tables': len(join_tables),
        'fields_total': sum(len(e['fields']) for e in entities),
        'entities_live': by_storage.get('live', 0),
        'entities_partial': by_storage.get('partial', 0),
        'entities_planned': by_storage.get('planned', 0),
        'entities_stub': by_storage.get('stub', 0),
        'database_deployed': False,
        'schema_readiness_pct': 35,
        'migration_target': 'supabase_postgres',
        'v1_storage': 'static_json_netlify_forms'
    },
    'catalog_gaps': [
        'No Postgres/Supabase instance deployed',
        'Join tables exist only as schema — no DB tables',
        'Referral and packet share entities not implemented',
        'Public officials directory not populated',
        'Form submissions not synced to person/signup tables',
    ],
    'recommended_next_build': {
        'number': 23,
        'title': 'Wireframes for Every Major Screen',
        'note': 'UX artifacts before component specs and framework migration.'
    },
}

path = root / 'data/database-schema.json'
with open(path, 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')
print(f'Database schema: {len(entities)} entities, {len(join_tables)} join tables, {out["summary"]["schema_readiness_pct"]}% readiness')
