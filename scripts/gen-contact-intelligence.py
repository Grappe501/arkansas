"""
Generate data/contact-intelligence.json — Build #24 Contact Intelligence & Community Relationship Architecture v1.0.
"""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
today = '2026-07-09'


def module(mid, title, purpose, fields, status, entity=None, notes=None, metrics=None):
    return {
        'id': mid,
        'title': title,
        'purpose': purpose,
        'field_count': len(fields),
        'fields': fields,
        'implementation_status': status,
        'database_entity': entity,
        'mc_metrics': metrics or [],
        'notes': notes,
    }


INTERESTS = [
    'Campaign finance history', 'Constitutional law', 'Supreme Court decisions',
    'Political spending', 'Ballot initiatives', 'Arkansas legislation',
    'Community education', 'Research', 'Data visualization', 'Coalition building',
    'Public speaking', 'Community organizing',
]

SKILLS = [
    'Public speaking', 'Writing', 'Editing', 'Research', 'Legal analysis',
    'Graphic design', 'Video production', 'Photography', 'Social media',
    'Event planning', 'Data analysis', 'Web development', 'Fundraising',
    'Volunteer coordination',
]

COMMUNITY_CONNECTIONS = [
    'Civic organizations', 'Neighborhood associations', 'Faith communities',
    'Schools', 'Colleges', 'Libraries', 'Veteran organizations',
    'Professional associations', 'Community nonprofits',
]

COMM_PREFS = [
    'Monthly newsletter', 'Research updates', 'Event announcements',
    'Volunteer opportunities', 'Coalition news', 'New educational resources',
    'Arkansas legislative education updates',
]

PRIVACY_PRINCIPLES = [
    'Collect only information that supports the educational mission',
    'Clearly distinguish public profile information from private administrative data',
    'Allow participants to update or remove their information',
    'Never sell participant data',
    'Explain how information is used in plain language',
]

RESEARCH_ROLES = [
    'Fact verification', 'Source collection', 'Citation review',
    'Historical research', 'Arkansas legislative monitoring',
    'Ballot initiative research', 'Academic literature review',
]

REFERRAL_TRACKS = [
    'Invitations sent', 'Invitations accepted', 'Educational resources shared',
    'Community conversations initiated', 'Organization referrals',
]

MC_METRICS = [
    {'id': 'MCI-01', 'title': 'Active participants', 'entity': 'person', 'status': 'planned'},
    {'id': 'MCI-02', 'title': 'New participants', 'entity': 'person', 'status': 'planned'},
    {'id': 'MCI-03', 'title': 'Active education leaders', 'entity': 'person', 'status': 'partial'},
    {'id': 'MCI-04', 'title': 'Coalition organizations', 'entity': 'organization', 'status': 'partial'},
    {'id': 'MCI-05', 'title': 'Counties represented', 'entity': 'county', 'status': 'partial'},
    {'id': 'MCI-06', 'title': 'Community conversations', 'entity': 'event', 'status': 'planned'},
    {'id': 'MCI-07', 'title': 'Resource shares', 'entity': 'educational_packet_share', 'status': 'planned'},
    {'id': 'MCI-08', 'title': 'Organization referrals', 'entity': 'referral', 'status': 'planned'},
    {'id': 'MCI-09', 'title': 'Research contributors', 'entity': 'person', 'status': 'planned'},
    {'id': 'MCI-10', 'title': 'Public official educational outreach', 'entity': 'educational_packet_share', 'status': 'planned'},
    {'id': 'MCI-11', 'title': 'Volunteer skills available across Arkansas', 'entity': 'person', 'status': 'planned'},
]

modules = [
    module('CI-001', 'Individual Profile', 'Civic Education Profile for every participant', [
        {'name': 'name', 'tier': 'core', 'required': True},
        {'name': 'preferred_contact', 'tier': 'core', 'required': True},
        {'name': 'city', 'tier': 'core', 'required': True},
        {'name': 'county', 'tier': 'core', 'required': True},
        {'name': 'zip_code', 'tier': 'core', 'required': True},
        {'name': 'preferred_communication_method', 'tier': 'core', 'required': True},
        {'name': 'areas_of_interest', 'tier': 'core', 'required': True, 'type': 'multi_select', 'options_ref': 'interests'},
        {'name': 'educational_goals', 'tier': 'core', 'required': False},
        {'name': 'volunteer_interests', 'tier': 'core', 'required': False},
        {'name': 'organization_affiliations', 'tier': 'optional', 'required': False},
        {'name': 'speaking_experience', 'tier': 'optional', 'required': False},
        {'name': 'research_interests', 'tier': 'optional', 'required': False},
        {'name': 'presentation_experience', 'tier': 'optional', 'required': False},
        {'name': 'professional_background', 'tier': 'optional', 'required': False},
        {'name': 'topics_to_learn', 'tier': 'optional', 'required': False},
    ], 'partial', 'person', 'Join/educate forms capture subset; full profile schema defined in database-schema.json',
        ['MCI-01', 'MCI-02', 'MCI-03']),
    module('CI-002', 'Interest Mapping', 'Aggregate participant interests for statewide strengths and gaps', [
        {'name': 'interest_topic', 'type': 'taxonomy', 'options': INTERESTS},
        {'name': 'participant_id', 'type': 'foreign_key', 'entity': 'person'},
        {'name': 'strength_level', 'type': 'optional', 'values': ['learning', 'teaching', 'researching']},
    ], 'schema_ready', 'person_interests', '12 topics defined; MC aggregation not built',
        ['MCI-11']),
    module('CI-003', 'Skills Inventory', 'Connect educational needs with volunteer expertise', [
        {'name': 'skill', 'type': 'taxonomy', 'options': SKILLS},
        {'name': 'participant_id', 'type': 'foreign_key', 'entity': 'person'},
        {'name': 'willing_to_contribute', 'type': 'boolean', 'default': True},
    ], 'schema_ready', 'person_skills', '14 skills defined; matching engine not built',
        ['MCI-11']),
    module('CI-004', 'Community Connections', 'Educational outreach planning via existing relationships', [
        {'name': 'connection_type', 'type': 'taxonomy', 'options': COMMUNITY_CONNECTIONS},
        {'name': 'organization_name', 'type': 'text'},
        {'name': 'participant_id', 'type': 'foreign_key', 'entity': 'person'},
        {'name': 'notes', 'type': 'text', 'required': False},
    ], 'planned', 'person_organizations', 'No political affiliation required; supports outreach planning'),
    module('CI-005', 'Organization Intelligence', 'Coalition partner profiles for educational reach', [
        {'name': 'organization_mission', 'tier': 'core'},
        {'name': 'educational_interests', 'tier': 'core', 'type': 'multi_select'},
        {'name': 'geographic_reach', 'tier': 'core'},
        {'name': 'audience_served', 'tier': 'core'},
        {'name': 'meeting_space_available', 'tier': 'optional', 'type': 'boolean'},
        {'name': 'resources_requested', 'tier': 'optional'},
        {'name': 'event_hosting_capability', 'tier': 'optional', 'type': 'boolean'},
        {'name': 'speaker_requests', 'tier': 'optional'},
        {'name': 'volunteer_opportunities', 'tier': 'optional'},
    ], 'partial', 'organization', 'Coalition sign-on form captures subset',
        ['MCI-04', 'MCI-08']),
    module('CI-006', 'County Intelligence', 'Living education profile per Arkansas county', [
        {'name': 'registered_participants', 'type': 'metric'},
        {'name': 'education_leaders', 'type': 'metric'},
        {'name': 'coalition_organizations', 'type': 'metric'},
        {'name': 'community_conversations', 'type': 'metric'},
        {'name': 'events_hosted', 'type': 'metric'},
        {'name': 'resource_downloads', 'type': 'metric'},
        {'name': 'public_official_outreach', 'type': 'metric'},
        {'name': 'engagement_gap_flag', 'type': 'computed'},
    ], 'partial', 'county', '75 county scaffold + county-coalition-index.json; live metrics partial',
        ['MCI-05']),
    module('CI-007', 'Community Conversation Tracking', 'Continuous improvement of educational materials', [
        {'name': 'topic', 'type': 'text'},
        {'name': 'audience_type', 'type': 'enum', 'values': ['home', 'civic_club', 'faith', 'campus', 'classroom', 'library', 'other']},
        {'name': 'county', 'type': 'foreign_key', 'entity': 'county'},
        {'name': 'attendance', 'type': 'number'},
        {'name': 'resources_used', 'type': 'multi_ref', 'entity': 'educational_resource'},
        {'name': 'questions_asked', 'type': 'text'},
        {'name': 'follow_up_interest', 'type': 'boolean'},
        {'name': 'future_event_opportunities', 'type': 'text'},
    ], 'planned', 'event', 'Event entity in schema; conversation capture form not built',
        ['MCI-06']),
    module('CI-008', 'Referral Intelligence', 'Educational relational organizing metrics', [
        {'name': 'metric', 'type': 'taxonomy', 'options': REFERRAL_TRACKS},
        {'name': 'referrer_id', 'type': 'foreign_key', 'entity': 'person'},
        {'name': 'referred_id', 'type': 'foreign_key', 'entity': 'person'},
        {'name': 'resource_id', 'type': 'foreign_key', 'entity': 'educational_resource', 'required': False},
        {'name': 'status', 'type': 'enum', 'values': ['sent', 'accepted', 'completed']},
    ], 'planned', 'referral', 'Share/invite pages exist; tracking not integrated',
        ['MCI-08']),
    module('CI-009', 'Public Official Engagement', 'Institutional record of educational outreach', [
        {'name': 'office', 'type': 'foreign_key', 'entity': 'public_official'},
        {'name': 'resource_shared', 'type': 'foreign_key', 'entity': 'educational_resource'},
        {'name': 'date', 'type': 'date'},
        {'name': 'follow_up_requested', 'type': 'boolean'},
        {'name': 'response_received', 'type': 'text', 'required': False},
    ], 'planned', 'educational_packet_share', 'Share-with-officials screen planned (WF-018); no backend',
        ['MCI-10']),
    module('CI-010', 'Research Contributor Network', 'Coordinate volunteer research contributions', [
        {'name': 'research_role', 'type': 'taxonomy', 'options': RESEARCH_ROLES},
        {'name': 'participant_id', 'type': 'foreign_key', 'entity': 'person'},
        {'name': 'availability', 'type': 'text'},
        {'name': 'expertise_notes', 'type': 'text', 'required': False},
    ], 'planned', 'person', 'Research volunteer signup redirects to ideas form',
        ['MCI-09']),
    module('CI-011', 'Communication Preferences', 'Respect how participants wish to hear from the project', [
        {'name': 'preference', 'type': 'taxonomy', 'options': COMM_PREFS},
        {'name': 'participant_id', 'type': 'foreign_key', 'entity': 'person'},
        {'name': 'opted_in', 'type': 'boolean', 'default': True},
    ], 'planned', 'person', 'Preference capture not on current forms'),
    module('CI-012', 'Privacy & Trust', 'Privacy-first principles governing all relationship data', [
        {'name': 'principle', 'type': 'policy', 'items': PRIVACY_PRINCIPLES},
        {'name': 'public_profile_fields', 'type': 'field_list'},
        {'name': 'private_admin_fields', 'type': 'field_list'},
        {'name': 'data_retention_policy', 'type': 'policy'},
        {'name': 'participant_update_path', 'type': 'route', 'value': 'planned'},
    ], 'defined', None, 'Principles documented; participant self-service update path not built'),
    module('CI-013', 'Mission Control Metrics', 'Relationship health dashboard measures', [
        {'name': 'metric_id', 'type': 'reference', 'options_ref': 'mc_metrics'},
        {'name': 'aggregation', 'type': 'computed'},
        {'name': 'county_breakdown', 'type': 'boolean', 'default': True},
        {'name': 'trend_period', 'type': 'enum', 'values': ['7d', '30d', '90d', 'all']},
    ], 'partial', None, '11 metrics defined; most counts manual or Netlify Forms only',
        [m['id'] for m in MC_METRICS]),
    module('CI-014', 'Future Integrations', 'Clean integration with platform systems', [
        {'name': 'system', 'type': 'integration'},
        {'name': 'integration_type', 'type': 'enum', 'values': ['read', 'write', 'bidirectional']},
        {'name': 'status', 'type': 'enum', 'values': ['live', 'partial', 'planned']},
    ], 'mapped', None, '10 systems mapped; most partial or planned'),
]

integrations = [
    {'system': 'Contact Network', 'route': '/action/join-network.html', 'build': 12, 'status': 'partial', 'type': 'bidirectional'},
    {'system': 'Coalition Directory', 'route': '/coalition/', 'build': 14, 'status': 'partial', 'type': 'read'},
    {'system': 'Mission Control', 'route': '/mission-control/', 'build': 1, 'status': 'live', 'type': 'read'},
    {'system': 'Community Event Calendar', 'route': '/coalition/events.html', 'build': 13, 'status': 'partial', 'type': 'write'},
    {'system': 'Resource Library', 'route': '/library/', 'build': 6, 'status': 'partial', 'type': 'read'},
    {'system': 'Model Law Workspace', 'route': '/action/draft-laws.html', 'build': 8, 'status': 'stub', 'type': 'write'},
    {'system': 'Ballot Initiative Lab', 'route': '/action/ballot-lab.html', 'build': 8, 'status': 'stub', 'type': 'write'},
    {'system': 'Arkansas County Pages', 'route': '/coalition/county.html', 'build': 14, 'status': 'partial', 'type': 'bidirectional'},
    {'system': 'Social Media Outreach', 'route': '/coalition/resources.html', 'build': 13, 'status': 'partial', 'type': 'read'},
    {'system': 'Future Educational AI', 'route': None, 'build': None, 'status': 'planned', 'type': 'bidirectional'},
]

by_status = {}
for m in modules:
    by_status[m['implementation_status']] = by_status.get(m['implementation_status'], 0) + 1

total_fields = sum(m['field_count'] for m in modules)

# Honest readiness: weighted by implementation status
status_weights = {
    'live': 100, 'partial': 55, 'schema_ready': 40, 'defined': 35,
    'mapped': 30, 'planned': 12,
}
readiness = round(
    sum(status_weights.get(m['implementation_status'], 10) for m in modules) / max(len(modules), 1)
)

out = {
    'version': '1.0',
    'build': 24,
    'updated': today,
    'title': 'Contact Intelligence & Community Relationship Architecture v1.0',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/contact-intelligence.html',
    'constitution': '/docs/CONTACT_INTELLIGENCE.md',
    'purpose': 'Build the most useful educational relationship network in Arkansas — not the largest contact database.',
    'relationship_philosophy': 'Every person is more than a contact — interests, knowledge, relationships, organizations, skills, geography, and educational goals.',
    'governing_principle': 'Remember relationships, not just records. Help people find one another, learn together, and strengthen civic understanding across Arkansas.',
    'taxonomies': {
        'interests': INTERESTS,
        'skills': SKILLS,
        'community_connections': COMMUNITY_CONNECTIONS,
        'communication_preferences': COMM_PREFS,
        'research_roles': RESEARCH_ROLES,
        'referral_tracks': REFERRAL_TRACKS,
        'privacy_principles': PRIVACY_PRINCIPLES,
    },
    'modules': modules,
    'module_count': len(modules),
    'mc_metrics': MC_METRICS,
    'integrations': integrations,
    'related_registries': [
        {'title': 'Database Schema', 'build': 22, 'route': '/data/database-schema.json'},
        {'title': 'Canonical Data Model', 'build': 15, 'route': '/data/canonical-data-model.json'},
        {'title': 'Relationship Registry', 'build': 15, 'route': '/data/relationship-registry.json'},
        {'title': 'County Coalition Index', 'build': 14, 'route': '/data/county-coalition-index.json'},
    ],
    'summary': {
        'modules': len(modules),
        'fields_total': total_fields,
        'interest_topics': len(INTERESTS),
        'skills_defined': len(SKILLS),
        'community_connection_types': len(COMMUNITY_CONNECTIONS),
        'communication_preferences': len(COMM_PREFS),
        'research_roles': len(RESEARCH_ROLES),
        'mc_metrics_defined': len(MC_METRICS),
        'integrations_mapped': len(integrations),
        'by_status': by_status,
        'implementation_live': by_status.get('live', 0),
        'implementation_partial': by_status.get('partial', 0) + by_status.get('schema_ready', 0) + by_status.get('defined', 0) + by_status.get('mapped', 0),
        'implementation_planned': by_status.get('planned', 0),
        'contact_intelligence_readiness_pct': readiness,
    },
    'catalog_gaps': [
        'No backend database — v1 static JSON + Netlify Forms only',
        'Interest/skills taxonomies defined but not on signup forms',
        'Community conversation capture form not built',
        'Referral tracking not integrated with share/invite flows',
        'Public official engagement record not operational',
        'Participant self-service profile update not built',
        'MC relationship health dashboard aggregates mostly manual',
        'Communication preference opt-in not on forms',
    ],
    'recommended_next_build': {
        'number': 25,
        'title': 'GitHub Issues, Milestones, and Sprint Roadmap',
        'note': 'Translate relationship architecture into implementable sprint issues. Component specs deferred.',
    },
}

path = root / 'data/contact-intelligence.json'
with open(path, 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')
print(f'Contact Intelligence: {len(modules)} modules, {readiness}% readiness')
