"""
Generate data/coalition-network.json — Build #61.
Master Arkansas Coalition & Civic Alliance Network v1.0.
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
coalition = load_json(root / 'data/coalition-directory.json')
county_idx = load_json(root / 'data/county-coalition-index.json')
vj = load_json(root / 'data/visitor-journey.json')
ca = load_json(root / 'data/civic-atlas.json')

ex = mc.get('executive', {})
orgs = coalition.get('summary', {}).get('total_organizations', 0)
counties_represented = coalition.get('summary', {}).get('counties_represented', 0)
edu_leaders = vj.get('summary', {}).get('education_leader_signups', 0)
counties_total = county_idx.get('counties_total', 75)

joint_events = 0
shared_resources = 0
conversations = 0
pending_requests = 0
recognition_items = 0

COALITION_PRINCIPLES = [
    'Evidence-based civic education',
    'Respectful public dialogue',
    'Transparent sourcing',
    'Intellectual honesty',
    'Constitutional literacy',
    'Community education',
    'Local leadership development',
]

PARTNERSHIP_CATEGORIES = [
    {
        'id': 'CAT-1', 'number': 1, 'title': 'Civic Organizations',
        'examples': ['Civic engagement groups', 'Good-government organizations', 'Community leadership organizations', 'Local civic associations'],
        'current': 0, 'status': 'scaffolded',
    },
    {
        'id': 'CAT-2', 'number': 2, 'title': 'Educational Institutions',
        'examples': ['Colleges', 'Universities', 'Community colleges', 'Libraries', 'Museums', 'Historical societies'],
        'current': 0, 'status': 'scaffolded',
    },
    {
        'id': 'CAT-3', 'number': 3, 'title': 'Nonprofit Organizations',
        'examples': ['Civic education', 'Constitutional literacy', 'Government transparency', 'Community leadership', 'Public participation'],
        'current': 0, 'status': 'scaffolded',
    },
    {
        'id': 'CAT-4', 'number': 4, 'title': 'Professional Organizations',
        'examples': ['Bar associations', 'Academic associations', 'Civic education professionals', 'Public administration organizations'],
        'current': 0, 'status': 'scaffolded',
    },
    {
        'id': 'CAT-5', 'number': 5, 'title': 'Community Organizations',
        'examples': ['Neighborhood associations', 'Community centers', 'Service clubs', 'Local educational initiatives'],
        'current': 0, 'status': 'scaffolded',
    },
    {
        'id': 'CAT-6', 'number': 6, 'title': 'Media & Educational Content Partners',
        'examples': ['Educational media organizations', 'Local journalism initiatives', 'Public media', 'Independent educational creators'],
        'current': 0, 'status': 'scaffolded',
    },
]

PARTNERSHIP_LEVELS = [
    {'id': 'LVL-1', 'level': 'Supporting Partner', 'commitment': 'Shares educational resources', 'current': 0, 'status': 'defined'},
    {'id': 'LVL-2', 'level': 'Educational Partner', 'commitment': 'Hosts learning opportunities', 'current': 0, 'status': 'defined'},
    {'id': 'LVL-3', 'level': 'Community Partner', 'commitment': 'Coordinates local conversations', 'current': 0, 'status': 'defined'},
    {'id': 'LVL-4', 'level': 'Leadership Partner', 'commitment': 'Mentors Education Leaders; strengthens county infrastructure', 'current': 0, 'status': 'defined'},
]

PROFILE_FIELDS = [
    'Organization description', 'Mission', 'Areas of expertise',
    'Educational resources offered', 'Counties served', 'Events hosted',
    'Community partnerships', 'Relationship history',
]

RESOURCE_CENTER_ITEMS = [
    'Presentation kits', 'Fact sheets', 'Community conversation guides',
    'Educational videos', 'Printable resources', 'Research summaries',
    'Event planning materials', 'Branding guidelines for coalition participation',
]

COUNTY_DASHBOARD_FIELDS = [
    'Coalition organizations', 'Education Leaders', 'Community events',
    'Libraries', 'Educational institutions', 'Community conversations', 'Resource distribution',
]

COLLABORATION_HUB_FEATURES = [
    'Share educational events', 'Request speakers', 'Exchange resources',
    'Coordinate presentations', 'Identify overlapping service areas', 'Avoid duplication of effort',
]

RECOGNITION_TYPES = [
    'New partner organizations', 'Educational milestones', 'Community partnerships',
    'Outstanding educational initiatives', 'Innovative local programs',
]

GROWTH_METRICS = [
    {'id': 'CGM-1', 'metric': 'Organizations participating', 'current': orgs, 'target': 'open', 'status': 'live'},
    {'id': 'CGM-2', 'metric': 'Counties represented', 'current': counties_represented, 'target': counties_total, 'status': 'live'},
    {'id': 'CGM-3', 'metric': 'Cities represented', 'current': 0, 'target': 250, 'status': 'live'},
    {'id': 'CGM-4', 'metric': 'Joint educational events', 'current': joint_events, 'status': 'planned'},
    {'id': 'CGM-5', 'metric': 'Shared educational resources', 'current': shared_resources, 'status': 'planned'},
    {'id': 'CGM-6', 'metric': 'Community conversations', 'current': conversations, 'status': 'planned'},
    {'id': 'CGM-7', 'metric': 'Education Leaders supported', 'current': edu_leaders, 'status': 'live'},
    {'id': 'CGM-8', 'metric': 'Growth over time', 'current': 0, 'status': 'planned'},
]

PARTNERSHIP_REQUEST_TYPES = [
    {'id': 'REQ-1', 'request': 'Coalition membership', 'workflow_status': 'planned'},
    {'id': 'REQ-2', 'request': 'Educational presentations', 'workflow_status': 'planned'},
    {'id': 'REQ-3', 'request': 'Resource packets', 'workflow_status': 'planned'},
    {'id': 'REQ-4', 'request': 'Community conversation support', 'workflow_status': 'planned'},
    {'id': 'REQ-5', 'request': 'Education Leader training', 'workflow_status': 'planned'},
    {'id': 'REQ-6', 'request': 'Research collaboration', 'workflow_status': 'planned'},
]

SYSTEM_CONNECTIONS = [
    {'system': 'ACUCOS / ACEI Coalition (#14)', 'route': '/coalition/', 'status': 'partial'},
    {'system': 'Coalition Directory', 'route': '/data/coalition-directory.json', 'status': 'scaffolded'},
    {'system': 'County Coalition Index', 'route': '/data/county-coalition-index.json', 'status': 'scaffolded'},
    {'system': 'Relationship OS (#59)', 'route': '/mission-control/relationship-os.html', 'status': 'live'},
    {'system': 'Civic Atlas (#58)', 'route': '/mission-control/civic-atlas.html', 'status': 'live'},
    {'system': 'Outreach Engine', 'route': '/mission-control/outreach.html', 'status': 'partial'},
    {'system': 'Education Academy', 'route': '/mission-control/education-academy.html', 'status': 'partial'},
    {'system': 'Mission Control', 'route': '/mission-control/', 'status': 'live'},
]

coalition_network_readiness = min(50, 32 + len(PARTNERSHIP_CATEGORIES) * 2)

out = {
    'version': '1.0',
    'build': 61,
    'updated': today,
    'title': 'Master Arkansas Coalition & Civic Alliance Network v1.0',
    'subtitle': 'Building Arkansas Together — The Coalition Operating Framework',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/coalition-network.html',
    'constitution': '/docs/MASTER_COALITION_NETWORK.md',
    'purpose': (
        'Common educational platform enabling organizations to work together while maintaining '
        'their identities — statewide ecosystem multiplying civic education capacity.'
    ),
    'governing_principle': (
        'The institution does not replace existing organizations — it connects them. '
        'Civic education is strongest when communities learn together.'
    ),
    'coalition_mission': 'Every Arkansan deserves access to accurate, transparent, evidence-based civic education.',
    'common_ground': 'Organizations may disagree on policy; they can agree citizens should understand facts.',
    'coalition_principles': COALITION_PRINCIPLES,
    'partnership_categories': PARTNERSHIP_CATEGORIES,
    'partnership_levels': PARTNERSHIP_LEVELS,
    'coalition_profile': {
        'title': 'Partner Organization Profiles',
        'fields': PROFILE_FIELDS,
        'organizations_count': orgs,
        'registry': '/data/coalition-directory.json',
        'status': 'scaffolded',
    },
    'resource_center': {
        'title': 'Coalition Resource Center',
        'items': RESOURCE_CENTER_ITEMS,
        'items_available': 2,
        'items_total': len(RESOURCE_CENTER_ITEMS),
        'status': 'partial',
    },
    'county_coalition_dashboard': {
        'title': 'Per-County Coalition View',
        'fields': COUNTY_DASHBOARD_FIELDS,
        'counties_total': counties_total,
        'counties_with_partners': counties_represented,
        'index': '/data/county-coalition-index.json',
        'public_route': '/coalition/counties.html',
        'status': 'scaffolded',
    },
    'collaboration_hub': {
        'title': 'Coalition Collaboration Hub',
        'features': COLLABORATION_HUB_FEATURES,
        'principle': 'The institution becomes a connector',
        'status': 'planned',
    },
    'coalition_recognition': {
        'title': 'Celebrate Coalition Contributions',
        'types': RECOGNITION_TYPES,
        'items_documented': recognition_items,
        'status': 'planned',
    },
    'growth_metrics': GROWTH_METRICS,
    'partnership_requests': {
        'title': 'Structured Review Workflow',
        'request_types': PARTNERSHIP_REQUEST_TYPES,
        'pending': pending_requests,
        'status': 'planned',
    },
    'strategic_priority': {
        'title': 'Mission Control Strategic Priority',
        'monitor_coalition_health': True,
        'rank': 'highest',
    },
    'integration': {
        'systems': SYSTEM_CONNECTIONS,
        'unifies': 'ACUCOS (#14) into master coalition operating framework',
    },
    'long_term_vision': [
        'Libraries host exhibits; communities conduct neighborhood discussions',
        'Universities contribute research; historical societies preserve context',
        'Civic organizations train Education Leaders; counties strengthened',
        'Largest collaborative civic education network on Citizens United in Arkansas',
    ],
    'mc_integration': {
        'title': 'Coalition Health Monitoring',
        'status': 'partial',
        'metrics': GROWTH_METRICS,
    },
    'summary': {
        'organizations_total': orgs,
        'counties_represented': counties_represented,
        'counties_total': counties_total,
        'cities_represented': 0,
        'education_leaders_supported': edu_leaders,
        'joint_events': joint_events,
        'shared_resources': shared_resources,
        'community_conversations': conversations,
        'pending_requests': pending_requests,
        'partnership_categories': len(PARTNERSHIP_CATEGORIES),
        'partnership_levels': len(PARTNERSHIP_LEVELS),
        'coalition_network_readiness_pct': coalition_network_readiness,
        'coalition_readiness_pct': ex.get('coalition_readiness', 18),
        'civic_atlas_readiness_pct': ca.get('summary', {}).get('civic_atlas_readiness_pct', 52),
        'public_launch_readiness_pct': ex.get('public_launch_readiness', 8),
    },
    'catalog_gaps': [
        f'0 coalition organizations — {counties_total} counties need partners',
        'Build #61 six categories vs ACUCOS seven categories — unification pending',
        'Build #61 four levels vs ACUCOS six levels — mapping needed',
        'Collaboration hub not built — no event sharing or speaker requests',
        'Partnership request workflow not implemented — 0 pending tracked',
        'Resource center 2/8 items partial — no dedicated partner portal',
        'Coalition recognition archive empty',
        'County dashboard scaffold only — 0 counties with partners',
        'No Netlify/Neon org signup integration',
        'Faith community category in ACUCOS not explicit in Build #61 six categories',
    ],
    'recommended_next_build': {
        'number': 62,
        'title': 'Implementation Translation Layer & Engineering Artifacts',
        'note': (
            'Neon org/partner schema, request workflow API, county dashboard wiring, '
            'route inventory, COMP-* specs, GitHub issue backlog.'
        ),
    },
}

with open(root / 'data/coalition-network.json', 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')

print(
    f'Coalition Network: {orgs} orgs, {counties_represented}/{counties_total} counties, '
    f'{coalition_network_readiness}% readiness'
)
