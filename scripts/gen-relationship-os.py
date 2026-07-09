"""
Generate data/relationship-os.json — Build #59.
Arkansas Civic Action CRM & Relationship Operating System (ROS) v1.0.
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
ci = load_json(root / 'data/contact-intelligence.json')
rr = load_json(root / 'data/relationship-registry.json')
ca = load_json(root / 'data/civic-atlas.json')
coalition = load_json(root / 'data/coalition-directory.json')
vj = load_json(root / 'data/visitor-journey.json')
no = load_json(root / 'data/neighborhood-organizing.json')

ex = mc.get('executive', {})
orgs = coalition.get('summary', {}).get('total_organizations', 0)
edu_leaders = vj.get('summary', {}).get('education_leader_signups', 0)
participants = vj.get('summary', {}).get('contact_network_signups', 0)
edges = len(rr.get('edges', []))
rel_types = len(rr.get('relationship_types', []))

# Honest zeros
active_relationships = 0
conversations = 0
mentor_pairs = 0
official_outreach = 0
opportunities_open = 0
timeline_events = 0
communications_logged = 0
counties_with_gaps = 75

PHILOSOPHY_QUESTIONS = [
    'How do we know this person?',
    'What interests them?',
    'What have they learned?',
    'How have they participated?',
    'What organizations are they connected to?',
    'How can we continue serving them?',
]

FIVE_NETWORKS = [
    {
        'id': 'NET-1', 'number': 1, 'title': 'Individual Network',
        'tracks': ['Learners', 'Volunteers', 'Education Leaders', 'Researchers', 'Presenters', 'Community participants'],
        'current': {'profiles': participants, 'education_leaders': edu_leaders},
        'status': 'scaffolded',
        'extends': 'Contact Intelligence (#24)',
    },
    {
        'id': 'NET-2', 'number': 2, 'title': 'Organization Network',
        'tracks': [
            'Coalition organizations', 'Libraries', 'Colleges', 'Universities',
            'Community organizations', 'Civic clubs', 'Historical societies',
            'Participating nonprofits', 'Other educational partners',
        ],
        'current': {'organizations': orgs},
        'status': 'scaffolded',
        'registry': '/data/community-assets.json',
    },
    {
        'id': 'NET-3', 'number': 3, 'title': 'Community Network',
        'tracks': ['Counties', 'Cities', 'Neighborhoods', 'Community conversations', 'Educational events', 'Local partnerships'],
        'current': {
            'counties': 75, 'cities_indexed': 250,
            'neighborhoods': no.get('summary', {}).get('neighborhoods_represented', 0),
            'conversations': conversations,
        },
        'status': 'scaffolded',
        'extends': 'Civic Atlas (#58)',
    },
    {
        'id': 'NET-4', 'number': 4, 'title': 'Public Official Network',
        'tracks': [
            'Arkansas U.S. Representatives', 'Arkansas U.S. Senators',
            'Arkansas General Assembly members', 'Local elected officials (educational outreach)',
        ],
        'records': ['Educational resource packets shared', 'Meetings requested', 'Responses received', 'Follow-up opportunities'],
        'current': {'officials_tracked': 0, 'outreach_logged': official_outreach},
        'status': 'planned',
        'note': 'Institutional relationship management — not lobbying scores',
    },
    {
        'id': 'NET-5', 'number': 5, 'title': 'Institutional Network',
        'tracks': ['Universities', 'Researchers', 'Historians', 'Constitutional scholars', 'Journalists', 'Subject-matter experts'],
        'current': {'experts_tracked': 0},
        'status': 'planned',
    },
]

TIMELINE_STAGES = [
    {'stage': 1, 'id': 'joined', 'event': 'Joined platform', 'status': 'planned'},
    {'stage': 2, 'id': 'learning', 'event': 'Completed learning path', 'status': 'planned'},
    {'stage': 3, 'id': 'event', 'event': 'Attended event', 'status': 'planned'},
    {'stage': 4, 'id': 'conversation', 'event': 'Hosted conversation', 'status': 'planned'},
    {'stage': 5, 'id': 'coalition', 'event': 'Joined coalition', 'status': 'planned'},
    {'stage': 6, 'id': 'workshop', 'event': 'Presented workshop', 'status': 'planned'},
    {'stage': 7, 'id': 'mentor', 'event': 'Mentored Education Leader', 'status': 'planned'},
    {'stage': 8, 'id': 'research', 'event': 'Contributed research', 'status': 'planned'},
]

HEALTH_INDICATORS = [
    {'id': 'RHS-1', 'indicator': 'Recent engagement', 'weight_pct': 20, 'status': 'planned'},
    {'id': 'RHS-2', 'indicator': 'Educational participation', 'weight_pct': 20, 'status': 'planned'},
    {'id': 'RHS-3', 'indicator': 'Community involvement', 'weight_pct': 15, 'status': 'planned'},
    {'id': 'RHS-4', 'indicator': 'Volunteer activity', 'weight_pct': 15, 'status': 'planned'},
    {'id': 'RHS-5', 'indicator': 'Leadership development', 'weight_pct': 15, 'status': 'planned'},
    {'id': 'RHS-6', 'indicator': 'Coalition participation', 'weight_pct': 15, 'status': 'planned'},
]

COMMUNICATION_TYPES = [
    'Newsletters received', 'Event invitations', 'Presentation requests',
    'Resource requests', 'Volunteer follow-up', 'Research collaboration',
]

OPPORTUNITIES = [
    {'id': 'OPP-1', 'opportunity': 'Ready to become Education Leader', 'count': 0, 'status': 'planned'},
    {'id': 'OPP-2', 'opportunity': 'Coalition org interested in hosting event', 'count': 0, 'status': 'planned'},
    {'id': 'OPP-3', 'opportunity': 'Library requesting materials', 'count': 0, 'status': 'planned'},
    {'id': 'OPP-4', 'opportunity': 'Researcher willing to contribute', 'count': 0, 'status': 'planned'},
    {'id': 'OPP-5', 'opportunity': 'County needing mentorship', 'count': counties_with_gaps, 'status': 'active'},
]

MENTORSHIP_CHAIN = [
    {'level': 1, 'role': 'Education Leader', 'status': 'planned'},
    {'level': 2, 'role': 'Neighborhood Leader', 'status': 'planned'},
    {'level': 3, 'role': 'Community Volunteer', 'status': 'planned'},
    {'level': 4, 'role': 'New Learner', 'status': 'planned'},
]

PRIVACY_PRINCIPLES = [
    'Collect only information that supports the educational mission',
    'Clearly distinguish private administrative information from publicly shared profiles',
    'Allow participants to manage their communication preferences',
    'Never sell participant information',
    'Explain data practices in plain language',
]

CRM_WIDGETS = [
    {'id': 'CRM-1', 'widget': 'Total participants', 'current': participants, 'status': 'live'},
    {'id': 'CRM-2', 'widget': 'Active relationships', 'current': active_relationships, 'status': 'live'},
    {'id': 'CRM-3', 'widget': 'Education Leaders', 'current': edu_leaders, 'status': 'live'},
    {'id': 'CRM-4', 'widget': 'Coalition organizations', 'current': orgs, 'status': 'live'},
    {'id': 'CRM-5', 'widget': 'Community conversations', 'current': conversations, 'status': 'live'},
    {'id': 'CRM-6', 'widget': 'Relationship Health (avg)', 'current': 0, 'status': 'planned'},
    {'id': 'CRM-7', 'widget': 'Mentor network pairs', 'current': mentor_pairs, 'status': 'planned'},
    {'id': 'CRM-8', 'widget': 'Public official outreach', 'current': official_outreach, 'status': 'planned'},
    {'id': 'CRM-9', 'widget': 'Organization partnerships', 'current': 0, 'status': 'planned'},
    {'id': 'CRM-10', 'widget': 'Counties with relationship gaps', 'current': counties_with_gaps, 'status': 'live'},
]

INTEGRATION_STACK = [
    {'system': 'Mission Control', 'route': '/mission-control/', 'status': 'live'},
    {'system': 'Community Education Academy', 'route': '/mission-control/education-academy.html', 'status': 'partial'},
    {'system': 'Coalition Network', 'route': '/coalition/', 'status': 'planned'},
    {'system': 'County Operating System', 'route': '/mission-control/county-os.html', 'status': 'partial'},
    {'system': 'Arkansas Civic Atlas', 'route': '/mission-control/civic-atlas.html', 'status': 'live'},
    {'system': 'Event Calendar', 'route': None, 'status': 'planned'},
    {'system': 'Knowledge Graph', 'route': '/mission-control/civic-intelligence.html', 'status': 'partial'},
    {'system': 'Contact Network', 'route': '/mission-control/contact-intelligence.html', 'status': 'partial'},
    {'system': 'Outreach Engine', 'route': '/mission-control/outreach.html', 'status': 'partial'},
]

# Readiness
networks_score = 38
health_model_score = 10
integration_score = 10
registry_score = 6 if rel_types >= 20 else 0
relationship_os_readiness = min(54, networks_score + health_model_score + integration_score + registry_score)

out = {
    'version': '1.0',
    'build': 59,
    'updated': today,
    'title': 'Relationship Operating System v1.0',
    'subtitle': 'Arkansas Civic Action CRM — The Institutional Relationship Brain',
    'acronym': 'ROS',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/relationship-os.html',
    'constitution': '/docs/MASTER_RELATIONSHIP_OS.md',
    'purpose': (
        'Institutional CRM managing every meaningful relationship — people, organizations, communities, '
        'conversations, commitments, and opportunities. Civic education, not sales or fundraising.'
    ),
    'governing_principle': (
        'The institution is built by people. ROS exists so no person, organization, community, '
        'or contribution is forgotten.'
    ),
    'not_traditional_crm': True,
    'relationship_philosophy': {
        'principle': 'Every participant is a relationship with a story — never just a contact',
        'questions': PHILOSOPHY_QUESTIONS,
        'foundation': 'Relationships—not transactions',
    },
    'five_networks': FIVE_NETWORKS,
    'relationship_timeline': {
        'title': 'Chronological Institutional Memory',
        'flow': ' → '.join(s['event'] for s in TIMELINE_STAGES),
        'stages': TIMELINE_STAGES,
        'events_recorded': timeline_events,
        'status': 'planned',
    },
    'relationship_health_score': {
        'title': 'Relationship Health Score',
        'scale': '0–100 per profile',
        'indicators': HEALTH_INDICATORS,
        'statewide_avg': 0,
        'profiles_scored': 0,
        'purpose': 'Identify relationships benefiting from renewed communication',
        'status': 'planned',
    },
    'communication_history': {
        'title': 'Institutional Communications Log',
        'types': COMMUNICATION_TYPES,
        'communications_logged': communications_logged,
        'status': 'planned',
    },
    'opportunity_tracker': {
        'title': 'Proactive Educational Outreach',
        'opportunities': OPPORTUNITIES,
        'open_count': opportunities_open,
        'status': 'partial',
    },
    'mentorship_mapping': {
        'title': 'Mentorship Relationship Visualization',
        'chain': 'Education Leader → Neighborhood Leader → Community Volunteer → New Learner',
        'levels': MENTORSHIP_CHAIN,
        'mentor_pairs': mentor_pairs,
        'registry_edge_type': 'mentors',
        'status': 'planned',
    },
    'privacy_framework': {
        'title': 'Trust-Centered Relationship Management',
        'principles': PRIVACY_PRINCIPLES,
        'aligned_with': 'Contact Intelligence privacy (#24)',
        'status': 'documented',
    },
    'crm_dashboard': {
        'title': 'Mission Control CRM Dashboard',
        'subtitle': 'Living view of the institution human network',
        'widgets': CRM_WIDGETS,
        'widgets_live': sum(1 for w in CRM_WIDGETS if w['status'] == 'live'),
        'status': 'partial',
    },
    'relationship_registry': {
        'title': 'Canonical Edge Types',
        'route': '/data/relationship-registry.json',
        'relationship_types': rel_types,
        'edges_recorded': edges,
        'status': 'schema_ready' if edges == 0 else 'partial',
    },
    'contact_intelligence_link': {
        'title': 'Contact Intelligence Foundation',
        'route': '/data/contact-intelligence.json',
        'build': 24,
        'modules': len(ci.get('modules', [])),
        'status': 'partial',
    },
    'integration': {
        'title': 'ROS Integration Stack',
        'flow': 'Mission Control → Academy → Coalition → County OS → Civic Atlas → Calendar → KG → Contact → Outreach',
        'systems': INTEGRATION_STACK,
        'systems_live': sum(1 for s in INTEGRATION_STACK if s['status'] == 'live'),
    },
    'long_term_vision': [
        'Remember who learned, who taught, who asked questions',
        'Who hosted conversations and strengthened their county',
        'Who built coalition partnerships and contributed research',
        'Who mentored others — relationships as institutional history',
    ],
    'mc_integration': {
        'title': 'Core Intelligence System',
        'core_system': True,
        'metrics': CRM_WIDGETS,
    },
    'summary': {
        'total_participants': participants,
        'active_relationships': active_relationships,
        'education_leaders': edu_leaders,
        'coalition_orgs': orgs,
        'community_conversations': conversations,
        'relationship_edges': edges,
        'relationship_types_defined': rel_types,
        'timeline_events': timeline_events,
        'communications_logged': communications_logged,
        'mentor_pairs': mentor_pairs,
        'opportunities_open': opportunities_open,
        'statewide_avg_health_score': 0,
        'counties_with_gaps': counties_with_gaps,
        'crm_widgets_live': sum(1 for w in CRM_WIDGETS if w['status'] == 'live'),
        'relationship_os_readiness_pct': relationship_os_readiness,
        'contact_intelligence_readiness_pct': ex.get('contact_intelligence_readiness', 31),
        'civic_atlas_readiness_pct': ca.get('summary', {}).get('civic_atlas_readiness_pct', 52),
        'public_launch_readiness_pct': ex.get('public_launch_readiness', 8),
    },
    'catalog_gaps': [
        f'0 active relationships · {participants} participants — CRM empty',
        f'0/{rel_types} relationship edge types in use — schema only',
        'Relationship Health Score model defined — 0 profiles scored',
        'Timeline and communication history not implemented — 0 events logged',
        'Mentorship mapping planned — 0 mentor pairs',
        'Public Official Network scaffold only — no officials tracked',
        'Opportunity tracker partial — 75 counties need mentorship signal only',
        'ROS vs Contact Intelligence (#24) overlap — ROS supersedes as institutional brain',
        'Neon/Prisma participant schema not migrated — Netlify Forms only',
        'Event calendar integration blocked — calendar not built',
    ],
    'recommended_next_build': {
        'number': 60,
        'title': 'Implementation Translation Layer & Engineering Artifacts',
        'note': (
            'Neon schema for ROS profiles, timeline events, health scores, mentorship edges; '
            'CRM API contracts; route inventory, COMP-* specs, GitHub issue backlog.'
        ),
    },
}

with open(root / 'data/relationship-os.json', 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')

print(
    f'Relationship OS: 5 networks, {edges} edges, {participants} participants, '
    f'{relationship_os_readiness}% readiness'
)
