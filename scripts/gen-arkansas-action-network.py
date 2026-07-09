"""
Generate data/arkansas-action-network.json — Build #64.
Arkansas Action Network & Leadership Pipeline v1.0.
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
sg = load_json(root / 'data/statewide-growth.json')
no = load_json(root / 'data/neighborhood-organizing.json')
cac = load_json(root / 'data/citizen-action-center.json')
cn = load_json(root / 'data/coalition-network.json')
ros = load_json(root / 'data/relationship-os.json')

ex = mc.get('executive', {})
PARTICIPANTS_TARGET = 200_000
COUNTIES_TOTAL = 75
CITIES_TARGET = 250

# Honest zeros
visitors_tracked = 0
subscribers = 0
active_learners = 0
community_participants = 0
neighborhood_leaders = 0
city_leaders = 0
county_directors = 0
regional_mentors = 0
county_teams = 0
city_teams = 0
connected_arkansans = cac.get('summary', {}).get('participants_connected', 0)
mentors_assigned = 0
future_leaders_identified = 0
leadership_transitions = 0
progress_map_live = False

LEADERSHIP_PYRAMID = [
    {
        'level': 1, 'id': 'AAN-L1', 'role': 'Visitor', 'goal': 'Learn',
        'mc_tracks': ['First visit', 'Topics explored', 'Learning interests'],
        'current': visitors_tracked, 'status': 'partial',
    },
    {
        'level': 2, 'id': 'AAN-L2', 'role': 'Subscriber', 'goal': 'Stay connected',
        'mc_tracks': ['Newsletter enrollment', 'Learning preferences', 'County', 'City'],
        'current': subscribers, 'status': 'planned',
    },
    {
        'level': 3, 'id': 'AAN-L3', 'role': 'Active Learner', 'goal': 'Complete learning paths',
        'mc_tracks': ['Curriculum completion', 'Saved resources', 'Videos watched', 'Research explored'],
        'current': active_learners, 'status': 'planned',
    },
    {
        'level': 4, 'id': 'AAN-L4', 'role': 'Community Participant', 'goal': 'Begin participating locally',
        'examples': ['Attend conversations', 'Volunteer occasionally', 'Share resources'],
        'mc_tracks': ['Community participation history'],
        'current': community_participants, 'status': 'planned',
    },
    {
        'level': 5, 'id': 'AAN-L5', 'role': 'Neighborhood Education Leader', 'goal': 'Help educate neighbors',
        'responsibilities': ['Host conversations', 'Share materials', 'Recruit learners', 'Identify organizations'],
        'mc_tracks': ['Neighborhood activity'],
        'current': neighborhood_leaders, 'status': 'planned',
        'route': '/mission-control/neighborhood-organizing.html',
    },
    {
        'level': 6, 'id': 'AAN-L6', 'role': 'City Education Leader', 'goal': 'Coordinate educational efforts within a city',
        'responsibilities': ['Support neighborhood leaders', 'Coordinate events', 'Develop partnerships'],
        'mc_tracks': ['City educational capacity'],
        'current': city_leaders, 'status': 'planned',
    },
    {
        'level': 7, 'id': 'AAN-L7', 'role': 'County Education Director', 'goal': 'Coordinate county-wide civic education',
        'responsibilities': ['Recruit leaders', 'Mentor volunteers', 'Strengthen coalition', 'Expand reach'],
        'mc_tracks': ['County readiness'],
        'current': county_directors, 'status': 'planned',
        'route': '/mission-control/county-os.html',
    },
    {
        'level': 8, 'id': 'AAN-L8', 'role': 'Regional Mentor', 'goal': 'Strengthen multiple counties',
        'responsibilities': ['Mentor county leaders', 'Share best practices', 'Support expansion'],
        'mc_tracks': ['Regional development'],
        'current': regional_mentors, 'status': 'planned',
    },
]

GROWTH_OBJECTIVES = [
    {
        'id': 'AAN-OBJ-1', 'title': '75 County Education Teams',
        'current': county_teams, 'target': COUNTIES_TOTAL, 'status': 'scaffolded',
    },
    {
        'id': 'AAN-OBJ-2', 'title': '250 City Education Teams',
        'current': city_teams, 'target': CITIES_TARGET, 'status': 'scaffolded',
    },
    {
        'id': 'AAN-OBJ-3', 'title': 'Neighborhood Leaders statewide',
        'current': neighborhood_leaders, 'target': None, 'status': 'scaffolded',
    },
    {
        'id': 'AAN-OBJ-4', 'title': '200,000 Connected Arkansans',
        'current': connected_arkansans, 'target': PARTICIPANTS_TARGET, 'status': 'scaffolded',
    },
    {
        'id': 'AAN-OBJ-5', 'title': 'Self-sustaining civic education network',
        'current': 'not achieved', 'target': 'organic growth', 'status': 'planned',
    },
]

INVITATION_STAGES = [
    {'stage': 'Continue Learning', 'audience': 'Visitor / early learner', 'status': 'partial'},
    {'stage': 'Join the Contact Network', 'audience': 'Subscriber', 'status': 'planned'},
    {'stage': 'Attend a Community Conversation', 'audience': 'Active learner', 'status': 'planned'},
    {'stage': 'Become an Education Leader', 'audience': 'Community participant', 'status': 'planned'},
    {'stage': 'Start a Neighborhood Discussion', 'audience': 'Neighborhood leader candidate', 'status': 'planned'},
    {'stage': 'Help Build Your County Team', 'audience': 'City / county leader', 'status': 'planned'},
    {'stage': 'Invite Friends and Family', 'audience': 'All stages', 'status': 'planned'},
]

LEADERSHIP_ACADEMY = [
    {
        'level': 'Neighborhood Leaders',
        'topics': ['Facilitation', 'Resource sharing', 'Community conversations'],
        'route': '/mission-control/education-academy.html',
        'status': 'planned',
    },
    {
        'level': 'City Leaders',
        'topics': ['Coordination', 'Event planning', 'Partnership building'],
        'status': 'planned',
    },
    {
        'level': 'County Leaders',
        'topics': ['Strategic planning', 'Volunteer development', 'Coalition leadership'],
        'status': 'planned',
    },
]

PROGRESS_MAP_LAYERS = [
    'Education Leaders', 'Neighborhood coverage', 'City leadership',
    'County teams', 'Coalition organizations', 'Community conversations', 'Participant growth',
]

RECOGNITION_TYPES = [
    'First Education Leader in a county',
    'First community conversation in a city',
    'County reaching leadership targets',
    'Coalition milestones',
    'Volunteer anniversaries',
    'Major educational accomplishments',
]

SUCCESSION_METRICS = [
    {'id': 'AAN-S1', 'metric': 'Mentors assigned', 'current': mentors_assigned, 'status': 'planned'},
    {'id': 'AAN-S2', 'metric': 'Future leaders identified', 'current': future_leaders_identified, 'status': 'planned'},
    {'id': 'AAN-S3', 'metric': 'Training completed', 'current': 0, 'status': 'planned'},
    {'id': 'AAN-S4', 'metric': 'Leadership transitions', 'current': leadership_transitions, 'status': 'planned'},
]

GROWTH_ANALYTICS = [
    {'id': 'AAN-G1', 'question': 'How many visitors became learners?', 'status': 'planned'},
    {'id': 'AAN-G2', 'question': 'How many learners became volunteers?', 'status': 'planned'},
    {'id': 'AAN-G3', 'question': 'How many volunteers became Education Leaders?', 'status': 'planned'},
    {'id': 'AAN-G4', 'question': 'Which counties are growing?', 'status': 'planned'},
    {'id': 'AAN-G5', 'question': 'Which cities need support?', 'status': 'planned'},
    {'id': 'AAN-G6', 'question': 'Where are new leaders emerging?', 'status': 'planned'},
]

SYSTEM_CONNECTIONS = [
    {'system': 'Education Academy (#28)', 'route': '/mission-control/education-academy.html', 'status': 'partial'},
    {'system': 'Civic Atlas (#58)', 'route': '/mission-control/civic-atlas.html', 'status': 'live'},
    {'system': 'Relationship OS (#59)', 'route': '/mission-control/relationship-os.html', 'status': 'live'},
    {'system': 'Coalition Network (#61)', 'route': '/mission-control/coalition-network.html', 'status': 'live'},
    {'system': 'Statewide Growth (#56)', 'route': '/mission-control/statewide-growth.html', 'status': 'live', 'note': 'Growth objectives unified'},
    {'system': 'Neighborhood Organizing (#57)', 'route': '/mission-control/neighborhood-organizing.html', 'status': 'live'},
    {'system': 'Citizen Action Center (#62)', 'route': '/mission-control/citizen-action-center.html', 'status': 'live'},
    {'system': 'Knowledge Graph', 'route': '/mission-control/knowledge-graph.html', 'status': 'planned'},
    {'system': 'Contact Network', 'route': '/mission-control/contact-intelligence.html', 'status': 'partial'},
    {'system': 'Mission Control', 'route': '/mission-control/', 'status': 'live'},
]

pyramid_levels = len(LEADERSHIP_PYRAMID)
arkansas_action_network_readiness = min(
    50,
    14 + pyramid_levels * 3 + county_teams * 2 + (1 if progress_map_live else 0),
)

out = {
    'version': '1.0',
    'build': 64,
    'updated': today,
    'title': 'Arkansas Action Network & Leadership Pipeline v1.0',
    'subtitle': 'Building a Statewide Civic Education Movement — From One Learner to 200,000 Arkansans',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/arkansas-action-network.html',
    'constitution': '/docs/MASTER_ARKANSAS_ACTION_NETWORK.md',
    'purpose': (
        'Structured leadership and growth system transforming learning into sustainable local capacity — '
        'intentional growth from one visitor to 200,000 connected Arkansans.'
    ),
    'governing_principle': (
        'Equip ordinary Arkansans to teach other ordinary Arkansans. '
        'Growth measured in people equipped to teach — not website traffic.'
    ),
    'primary_growth_engine': True,
    'leadership_pyramid': LEADERSHIP_PYRAMID,
    'growth_objectives': GROWTH_OBJECTIVES,
    'invitation_engine': {
        'title': 'Context-Appropriate Invitations',
        'principle': 'Invitation always matches visitor stage of development',
        'stages': INVITATION_STAGES,
        'per_page': True,
        'status': 'planned',
    },
    'leadership_academy': {
        'title': 'Leadership Academy Pathways',
        'pathways': LEADERSHIP_ACADEMY,
        'continuous_growth': True,
        'status': 'planned',
    },
    'arkansas_progress_map': {
        'title': 'Statewide Progress Map',
        'layers': PROGRESS_MAP_LAYERS,
        'visual_heartbeat': True,
        'status': 'planned',
        'route': '/mission-control/civic-atlas.html',
    },
    'community_recognition': {
        'title': 'Community Recognition',
        'types': RECOGNITION_TYPES,
        'status': 'planned',
    },
    'leadership_succession': {
        'title': 'Leadership Succession',
        'principle': 'Every role identifies and mentors future leaders',
        'metrics': SUCCESSION_METRICS,
        'status': 'planned',
    },
    'growth_analytics': {
        'title': 'Growth Analytics',
        'focus': 'Leadership development — not raw traffic',
        'questions': GROWTH_ANALYTICS,
        'status': 'planned',
    },
    'integration': {
        'chain': (
            'Education Academy → Civic Atlas → Relationship OS → Coalition Network → '
            'Mission Control → Knowledge Graph → Citizen Action Center → Contact Network'
        ),
        'systems': SYSTEM_CONNECTIONS,
        'unifies': 'Statewide Growth (#56) objectives into operational growth engine',
    },
    'long_term_vision': (
        'Every county with an active education team; every major city with trained leaders; '
        'neighborhood discussions regularly; 200,000 Arkansans sharing civic education through '
        'trusted relationships — organic growth as local leaders develop new local leaders.'
    ),
    'summary': {
        'pyramid_levels': pyramid_levels,
        'county_teams': county_teams,
        'county_teams_target': COUNTIES_TOTAL,
        'city_teams': city_teams,
        'city_teams_target': CITIES_TARGET,
        'neighborhood_leaders': neighborhood_leaders,
        'city_leaders': city_leaders,
        'county_directors': county_directors,
        'regional_mentors': regional_mentors,
        'connected_arkansans': connected_arkansans,
        'connected_target': PARTICIPANTS_TARGET,
        'coalition_orgs': cn.get('summary', {}).get('organizations_total', 0),
        'active_relationships': ros.get('summary', {}).get('active_relationships', 0),
        'progress_map_live': progress_map_live,
        'invitation_engine_wired': False,
        'arkansas_action_network_readiness_pct': arkansas_action_network_readiness,
        'statewide_growth_readiness_pct': sg.get('summary', {}).get('statewide_growth_readiness_pct', 48),
        'public_launch_readiness_pct': ex.get('public_launch_readiness', 8),
    },
    'catalog_gaps': [
        '0 county teams · 0/75 — County Education Director pipeline not operational',
        '0 city teams · 0/250 — City Education Leader coordination not built',
        '0 neighborhood leaders — Level 5 pyramid empty',
        '0/200,000 connected Arkansans — no registration or contact network integration',
        'Invitation engine specified but not wired per-page across educational content',
        'Arkansas Progress Map planned — Civic Atlas map not live',
        'Leadership Academy pathways per level not implemented — Education Academy partial',
        'Growth analytics funnel (visitor→learner→volunteer→leader) not tracked',
        'Build #64 Action Network vs Build #56 Statewide Growth — unified here, reconcile dashboards?',
        'Leadership succession metrics all zero — mentor assignment workflow missing',
        'Community recognition system not built — no achievement tracking',
        '8-level pyramid vs other participation level schemas — mapping needed',
    ],
    'recommended_next_build': {
        'number': 65,
        'title': 'Implementation Translation Layer & Engineering Artifacts',
        'note': (
            'Leader registry schema, invitation component, progress map wiring, funnel analytics, '
            'Academy pathway routes, route inventory, COMP-* specs, GitHub issue backlog.'
        ),
    },
}

with open(root / 'data/arkansas-action-network.json', 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')

print(
    f'Arkansas Action Network: {pyramid_levels} pyramid levels, '
    f'{county_teams}/{COUNTIES_TOTAL} county teams, '
    f'{connected_arkansans}/{PARTICIPANTS_TARGET} connected, '
    f'{arkansas_action_network_readiness}% readiness'
)
