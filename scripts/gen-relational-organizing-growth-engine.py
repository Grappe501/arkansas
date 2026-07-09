"""
Generate data/relational-organizing-growth-engine.json — Build #69.
Master Relational Organizing & Arkansas Growth Engine v1.0.
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
no = load_json(root / 'data/neighborhood-organizing.json')
ros = load_json(root / 'data/relationship-os.json')
aan = load_json(root / 'data/arkansas-action-network.json')
cla = load_json(root / 'data/citizen-leadership-academy.json')
cn = load_json(root / 'data/coalition-network.json')

ex = mc.get('executive', {})
PARTICIPANTS_TARGET = 200_000

# Honest zeros
relationship_trees = 0
total_invitations = 0
learners_invited = 0
share_hub_wired_pages = 0
learning_circles = 0
coalition_referrals = 0
referral_milestones = 0
connected_arkansans = aan.get('summary', {}).get('connected_arkansans', 0)
active_mentorships = cla.get('summary', {}).get('mentorship_relationships', 0)
relationship_edges = ros.get('summary', {}).get('active_relationships', 0)

TRUST_RELATIONSHIP_TYPES = [
    'Neighbor', 'Friend', 'Family', 'Coworker',
    'Church member', 'Civic organization member', 'Community volunteer', 'Local leader',
]

GROWTH_FORMULA = {
    'question': 'Who are five people in my life who would benefit from understanding this better?',
    'suggested_invitations': 5,
    'no_pressure': True,
    'no_quotas': True,
    'thoughtful_invitations_only': True,
}

RELATIONSHIP_TREE_MODEL = {
    'voluntary': True,
    'example_branch': 'Leader → 5 learners → each 3 more → some become leaders → new branches',
    'visualizes_education_not_recruitment': True,
    'trees_active': relationship_trees,
    'status': 'planned',
}

SHARE_HUB_ITEMS = [
    'Educational articles', 'Timeline entries', 'Videos', 'Infographics',
    'Research summaries', 'Learning paths', 'Community events',
    'Presentation invitations', 'Academy enrollment',
]

FAMILY_LEARNING = [
    'Family discussion guides', 'Conversation starters', 'Short educational videos',
    'Printable timelines', 'Frequently asked questions',
]

LEARNING_CIRCLE_TYPES = [
    'Book clubs', 'Neighborhood gatherings', 'Coffee discussions',
    'Library groups', 'Community centers', 'Service clubs',
]

LEADER_REFERRAL_DASHBOARD = [
    'People invited', 'Learning progress', 'Academy enrollment',
    'Community conversations', 'New leaders developed', 'Recognition milestones',
]

REFERRAL_RECOGNITION = [
    'First learner introduced', 'First Academy graduate mentored',
    'First neighborhood discussion', 'First coalition referral', 'First county leader developed',
]

RELATIONSHIP_HEALTH_INDICATORS = [
    {'id': 'ROG-H1', 'indicator': 'Learning circle activity', 'current': learning_circles, 'status': 'planned'},
    {'id': 'ROG-H2', 'indicator': 'Mentorship continuity', 'current': active_mentorships, 'status': 'planned'},
    {'id': 'ROG-H3', 'indicator': 'Returning participants', 'current': 0, 'status': 'planned'},
    {'id': 'ROG-H4', 'indicator': 'Community engagement', 'current': 0, 'status': 'planned'},
    {'id': 'ROG-H5', 'indicator': 'Leadership development', 'current': 0, 'status': 'planned'},
    {'id': 'ROG-H6', 'indicator': 'Referral pathways', 'current': total_invitations, 'status': 'planned'},
]

PRIVACY_PRINCIPLES = [
    'Never require invitations',
    'Allow anonymous browsing',
    'Clear consent before sharing information',
    'Participants control communication preferences',
    'Trust must always outweigh growth',
]

MC_VISUALIZATION = [
    'Relationship trees', 'County growth', 'City growth', 'Neighborhood expansion',
    'Education Leader mentorship', 'Coalition referrals', 'Participant milestones',
    f'Progress toward {PARTICIPANTS_TARGET:,} connected Arkansans',
]

SYSTEM_CONNECTIONS = [
    {'system': 'Contact Network', 'route': '/mission-control/contact-intelligence.html', 'status': 'partial'},
    {'system': 'Citizen Action Center (#62)', 'route': '/mission-control/citizen-action-center.html', 'status': 'live'},
    {'system': 'Citizen Leadership Academy (#68)', 'route': '/mission-control/citizen-leadership-academy.html', 'status': 'live'},
    {'system': 'Community Education Academy (#28)', 'route': '/mission-control/education-academy.html', 'status': 'partial'},
    {'system': 'Coalition Network (#61)', 'route': '/mission-control/coalition-network.html', 'status': 'live'},
    {'system': 'Neighborhood Organizing (#57)', 'route': '/mission-control/neighborhood-organizing.html', 'status': 'live', 'note': 'Last mile'},
    {'system': 'Relationship OS (#59)', 'route': '/mission-control/relationship-os.html', 'status': 'live'},
    {'system': 'Arkansas Action Network (#64)', 'route': '/mission-control/arkansas-action-network.html', 'status': 'live', 'note': 'Invitation engine'},
    {'system': 'Civic Atlas (#58)', 'route': '/mission-control/civic-atlas.html', 'status': 'live'},
    {'system': 'Knowledge Graph', 'route': '/mission-control/knowledge-graph.html', 'status': 'planned'},
    {'system': 'Mission Control', 'route': '/mission-control/', 'status': 'live'},
]

relational_organizing_growth_engine_readiness = min(
    42,
    14 + len(TRUST_RELATIONSHIP_TYPES) * 2 + 4,
)

out = {
    'version': '1.0',
    'build': 69,
    'updated': today,
    'title': 'Master Relational Organizing & Arkansas Growth Engine v1.0',
    'subtitle': 'The Network Effect — Growing from One Arkansan to 200,000 Through Trusted Relationships',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/relational-organizing-growth-engine.html',
    'constitution': '/docs/MASTER_RELATIONAL_ORGANIZING_GROWTH_ENGINE.md',
    'purpose': (
        'Transform individual learning into statewide educational growth through trusted '
        'personal relationships — primary expansion strategy.'
    ),
    'governing_principle': (
        'Strongest civic education shared freely between people who trust one another. '
        'Opportunity not obligation. Curiosity not pressure.'
    ),
    'primary_expansion_strategy': True,
    'not_advertising_seo_social': True,
    'core_philosophy': {
        'trust_chain': TRUST_RELATIONSHIP_TYPES,
        'knowledge_spreads_through_relationships': True,
        'platform_supports_relationships': True,
    },
    'arkansas_growth_formula': GROWTH_FORMULA,
    'relationship_tree': RELATIONSHIP_TREE_MODEL,
    'share_hub': {
        'title': 'The Share Hub',
        'per_page_panel': True,
        'shareable_items': SHARE_HUB_ITEMS,
        'emphasis': 'I thought you might find this helpful.',
        'not_emphasis': 'You have to agree with this.',
        'pages_wired': share_hub_wired_pages,
        'status': 'planned',
    },
    'family_learning': {
        'title': 'Family Learning',
        'resources': FAMILY_LEARNING,
        'intergenerational': True,
        'status': 'planned',
    },
    'friend_neighbor_circles': {
        'title': 'Friend & Neighbor Circles',
        'circle_types': LEARNING_CIRCLE_TYPES,
        'active_circles': learning_circles,
        'local_conversations': True,
        'status': 'planned',
    },
    'organizational_referrals': {
        'title': 'Organizational Referrals',
        'coalition_tools': True,
        'referrals_tracked': coalition_referrals,
        'privacy_respecting': True,
        'status': 'planned',
    },
    'education_leader_referral_dashboard': {
        'title': 'Education Leader Referral Dashboard',
        'fields': LEADER_REFERRAL_DASHBOARD,
        'mentorship_not_competition': True,
        'status': 'planned',
    },
    'referral_recognition': {
        'title': 'Referral Recognition',
        'milestones': REFERRAL_RECOGNITION,
        'focus': 'Service and education',
        'milestones_achieved': referral_milestones,
        'status': 'planned',
    },
    'relationship_health': {
        'title': 'Relationship Health',
        'indicators': RELATIONSHIP_HEALTH_INDICATORS,
        'status': 'planned',
    },
    'privacy_principles': {
        'title': 'Privacy Principles',
        'principles': PRIVACY_PRINCIPLES,
        'trust_outweighs_growth': True,
        'status': 'live',
    },
    'mc_visualization': {
        'title': 'Mission Control Growth Visualization',
        'layers': MC_VISUALIZATION,
        'private_info_protected': True,
        'status': 'planned',
    },
    'integration': {
        'chain': (
            'Contact Network → Citizen Action Center → Community Education Academy → '
            'Coalition Network → Civic Atlas → Mission Control → Knowledge Graph'
        ),
        'systems': SYSTEM_CONNECTIONS,
        'unifies': 'Neighborhood Organizing (#57) + Relationship OS (#59) + Action Network invitation engine',
    },
    'long_term_vision': (
        'Education Leaders trace journeys through trusted relationship chains. Knowledge spread '
        'person by person. Institution grew because people chose to share — not because it interrupted.'
    ),
    'summary': {
        'trust_relationship_types': len(TRUST_RELATIONSHIP_TYPES),
        'relationship_trees': relationship_trees,
        'total_invitations': total_invitations,
        'learners_invited': learners_invited,
        'share_hub_pages_wired': share_hub_wired_pages,
        'learning_circles': learning_circles,
        'coalition_referrals': coalition_referrals,
        'referral_milestones': referral_milestones,
        'connected_arkansans': connected_arkansans,
        'connected_target': PARTICIPANTS_TARGET,
        'relationship_edges': relationship_edges,
        'relational_organizing_growth_engine_readiness_pct': relational_organizing_growth_engine_readiness,
        'neighborhood_organizing_readiness_pct': ex.get('neighborhood_organizing_readiness', 50),
        'relationship_os_readiness_pct': ex.get('relationship_os_readiness', 54),
        'public_launch_readiness_pct': ex.get('public_launch_readiness', 8),
    },
    'catalog_gaps': [
        '0 relationship trees — voluntary tree builder not implemented',
        '0 invitations tracked — five-people question not wired in UI',
        'Share hub specified — 0 educational pages with sharing panel',
        '0 learning circles registered — friend/neighbor circle tools missing',
        '0 coalition referrals — organizational referral workflow not built',
        'Education Leader referral dashboard not built — 0 leaders to dashboard',
        'Referral recognition system not implemented — 0 milestones',
        'Build #69 Growth Engine vs Build #64 Action Network primary growth — reconcile roles?',
        'Build #69 vs Build #57 Neighborhood Organizing — unify relational specs?',
        'Privacy principles specified — no consent UI or anonymous browse enforcement audit',
        'MC visualization planned — relationship trees not rendered',
        'No referral codes or tracking — by design until privacy model approved',
        f'0/{PARTICIPANTS_TARGET:,} connected — relational engine has no participants',
    ],
    'recommended_next_build': {
        'number': 70,
        'title': 'Implementation Translation Layer & Engineering Artifacts',
        'note': (
            'Share hub component, relationship tree schema, referral tracking with privacy, '
            'leader dashboard, circle registration, route inventory, COMP-* specs, GitHub backlog.'
        ),
    },
}

with open(root / 'data/relational-organizing-growth-engine.json', 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')

print(
    f'Relational Organizing Growth Engine: {relationship_trees} trees, '
    f'{total_invitations} invitations, {connected_arkansans}/{PARTICIPANTS_TARGET} connected, '
    f'{relational_organizing_growth_engine_readiness}% readiness'
)
