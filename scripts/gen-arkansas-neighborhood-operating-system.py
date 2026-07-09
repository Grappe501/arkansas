"""
Generate data/arkansas-neighborhood-operating-system.json — Build #79.
Master Arkansas Neighborhood Operating System (ANOS) v1.0.
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
arcity = load_json(root / 'data/arkansas-city-operating-system.json')
acos = load_json(root / 'data/arkansas-county-operating-system.json')
no = load_json(root / 'data/neighborhood-organizing.json')
profiles = load_json(root / 'data/neighborhood-profiles.json')
rog = load_json(root / 'data/relational-organizing-growth-engine.json')

ex = mc.get('executive', {})

# Honest zeros
neighborhood_profiles_total = profiles.get('summary', {}).get('profiles_total', 0)
neighborhoods_with_digital_twin = 0
neighborhood_dashboards_live = 0
neighborhoods_with_leader = profiles.get('summary', {}).get('with_leaders', 0)
neighborhood_health_score_computed = False
neighborhood_listening_reports = 0
mentorship_trees_live = False
mentorship_pairs = 0
recognition_milestones_awarded = 0
connected_arkansans = rog.get('summary', {}).get('connected_arkansans', 0)
PARTICIPANTS_TARGET = 200_000

TRUSTED_RELATIONSHIPS = [
    'Neighbors', 'Friends', 'Coworkers', 'Church members',
    'Fellow volunteers', 'Community leaders',
]

NEIGHBORHOOD_MISSION_ITEMS = [
    'Neighborhood Education Leader',
    'Welcoming place for discussion',
    'Access to educational materials',
    'Connections to city and county teams',
    'Pathway into Community Education Academy',
    'Connection to broader institution',
]

PROFILE_SECTIONS = [
    {'id': 'ANOS-PS-01', 'section': 'Neighborhood name', 'status': 'specified'},
    {'id': 'ANOS-PS-02', 'section': 'Associated city', 'status': 'specified'},
    {'id': 'ANOS-PS-03', 'section': 'Associated county', 'status': 'specified'},
    {'id': 'ANOS-PS-04', 'section': 'General geographic description', 'status': 'specified'},
    {'id': 'ANOS-PS-05', 'section': 'Education Leaders', 'status': 'planned'},
    {'id': 'ANOS-PS-06', 'section': 'Community partners', 'status': 'planned'},
    {'id': 'ANOS-PS-07', 'section': 'Conversation history', 'status': 'planned'},
    {'id': 'ANOS-PS-08', 'section': 'Educational events', 'status': 'planned'},
    {'id': 'ANOS-PS-09', 'section': 'Resource usage', 'status': 'planned'},
    {'id': 'ANOS-PS-10', 'section': 'Growth indicators', 'status': 'planned'},
]

LEADERSHIP_ROLES = [
    {'id': 'ANOS-LR-01', 'role': 'Neighborhood Education Leader', 'filled': 0, 'status': 'specified'},
    {'id': 'ANOS-LR-02', 'role': 'Conversation Host', 'filled': 0, 'status': 'specified'},
    {'id': 'ANOS-LR-03', 'role': 'Volunteer Coordinator', 'filled': 0, 'status': 'specified'},
    {'id': 'ANOS-LR-04', 'role': 'Community Connector', 'filled': 0, 'status': 'specified'},
    {'id': 'ANOS-LR-05', 'role': 'Academy Ambassador', 'filled': 0, 'status': 'specified'},
    {'id': 'ANOS-LR-06', 'role': 'Coalition Liaison', 'filled': 0, 'status': 'specified'},
]

CONVERSATION_ENVIRONMENTS = [
    'Living rooms', 'Libraries', 'Coffee shops', 'Community centers',
    'Parks', 'Service clubs', 'Faith community meeting spaces',
]

LEARNING_CIRCLE_RESOURCES = [
    'Lesson guides', 'Presentation slides', 'Fact sheets',
    'Frequently asked questions', 'Source packets', 'Videos',
    'Discussion questions', 'QR codes to learning paths',
]

GROWTH_CYCLE = [
    {'step': 1, 'id': 'one_learner', 'title': 'One learner', 'neighborhoods_at_step': 0},
    {'step': 2, 'id': 'one_conversation', 'title': 'One conversation', 'neighborhoods_at_step': 0},
    {'step': 3, 'id': 'five_learners', 'title': 'Five learners', 'neighborhoods_at_step': 0},
    {'step': 4, 'id': 'one_education_leader', 'title': 'One Education Leader', 'neighborhoods_at_step': 0},
    {'step': 5, 'id': 'regular_conversations', 'title': 'Regular conversations', 'neighborhoods_at_step': 0},
    {'step': 6, 'id': 'new_volunteers', 'title': 'New volunteers', 'neighborhoods_at_step': 0},
    {'step': 7, 'id': 'new_leaders', 'title': 'New leaders', 'neighborhoods_at_step': 0},
    {'step': 8, 'id': 'healthy_community', 'title': 'Healthy neighborhood learning community', 'neighborhoods_at_step': 0},
]

DASHBOARD_SECTIONS = [
    'Leadership', 'Conversation schedule', 'Participant growth', 'Learning progress',
    'Volunteer activity', 'Resource requests', 'Community questions', 'Relationship network',
]

HEALTH_SCORE_FACTORS = [
    'Leadership', 'Learning participation', 'Conversation frequency',
    'Volunteer engagement', 'Academy participation', 'Resource usage',
    'Relationship growth', 'Mentorship',
]

RESOURCE_CENTER = [
    'Conversation kits', 'Presentation templates', 'Printable handouts',
    'Educational posters', 'Shareable graphics', 'Videos',
    'Community discussion guides',
]

MENTORSHIP_VISUALIZATIONS = [
    'Mentorship trees', 'Leadership succession', 'Volunteer development', 'Knowledge transfer',
]

RECOGNITION_MILESTONES = [
    'First community conversation', 'First Academy graduate', 'First coalition partnership',
    'First neighborhood learning circle', 'Volunteer anniversaries', 'Leadership achievements',
]

TWO_HUNDRED_K_QUESTIONS = [
    'Who in my own neighborhood would enjoy learning this?',
    'Who might host a conversation?',
    'Who could become the next leader?',
]

SYSTEM_CONNECTIONS = [
    {'system': 'Arkansas City OS (#78)', 'route': '/mission-control/arkansas-city-operating-system.html', 'status': 'live'},
    {'system': 'Arkansas County OS (#77)', 'route': '/mission-control/arkansas-county-operating-system.html', 'status': 'live'},
    {'system': 'Community Education Academy (#68)', 'route': '/mission-control/citizen-leadership-academy.html', 'status': 'live'},
    {'system': 'Citizen Action Center (#62)', 'route': '/mission-control/citizen-action-center.html', 'status': 'live'},
    {'system': 'Relationship Operating System (#59)', 'route': '/mission-control/relationship-os.html', 'status': 'live'},
    {'system': 'Arkansas Civic Atlas (#58)', 'route': '/mission-control/civic-atlas.html', 'status': 'live'},
    {'system': 'Mission Control', 'route': '/mission-control/', 'status': 'live'},
    {'system': 'Neighborhood Organizing (#57)', 'route': '/mission-control/neighborhood-organizing.html', 'status': 'live', 'note': 'Extended by ANOS'},
    {'system': 'Relational Growth Engine (#69)', 'route': '/mission-control/relational-organizing-growth-engine.html', 'status': 'live'},
    {'system': 'Arkansas Command Strategy (#70)', 'route': '/mission-control/arkansas-command-strategy.html', 'status': 'live'},
]

anos_readiness = min(
    49,
    15
    + len(GROWTH_CYCLE)
    + len(PROFILE_SECTIONS) // 2
    + len(LEADERSHIP_ROLES)
    + len(DASHBOARD_SECTIONS) // 2
    + len(HEALTH_SCORE_FACTORS) // 2
    + len(LEARNING_CIRCLE_RESOURCES) // 4
    + 3,
)

out = {
    'version': '1.0',
    'build': 79,
    'updated': today,
    'title': 'Master Arkansas Neighborhood Operating System (ANOS) v1.0',
    'subtitle': 'The Last 500 Feet',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/arkansas-neighborhood-operating-system.html',
    'constitution': '/docs/MASTER_ARKANSAS_NEIGHBORHOOD_OPERATING_SYSTEM.md',
    'purpose': (
        'Final layer of institutional architecture — repeatable framework for neighborhood-level '
        'learning, relationship building, and community leadership across Arkansas.'
    ),
    'governing_principle': (
        'Healthy democracy begins close to home — around kitchen tables, in libraries, '
        'at community centers, among neighbors willing to learn together.'
    ),
    'final_institutional_layer': True,
    'institutional_philosophy': {
        'title': 'Institutional Philosophy',
        'life_happens_in_neighborhoods': True,
        'trusted_relationships': TRUSTED_RELATIONSHIPS,
        'designed_around_trust': True,
    },
    'neighborhood_mission': {
        'title': 'Neighborhood Mission',
        'items': NEIGHBORHOOD_MISSION_ITEMS,
        'items_total': len(NEIGHBORHOOD_MISSION_ITEMS),
    },
    'neighborhood_profile': {
        'title': 'Neighborhood Identity',
        'sections_total': len(PROFILE_SECTIONS),
        'sections': PROFILE_SECTIONS,
        'private_residential_never_public': True,
        'living_profile': True,
    },
    'neighborhood_leadership_team': {
        'title': 'Neighborhood Leadership Team',
        'roles_total': len(LEADERSHIP_ROLES),
        'one_volunteer_multiple_roles_initially': True,
        'roles': LEADERSHIP_ROLES,
    },
    'neighborhood_conversation_model': {
        'title': 'Neighborhood Conversation Model',
        'intentionally_small': True,
        'thoughtful_discussion_not_rallies': True,
        'ideal_environments': CONVERSATION_ENVIRONMENTS,
    },
    'neighborhood_learning_circles': {
        'title': 'Neighborhood Learning Circles',
        'resources': LEARNING_CIRCLE_RESOURCES,
        'connected_to_verified_resources': True,
        'status': 'specified',
    },
    'neighborhood_growth_cycle': {
        'title': 'Neighborhood Growth Cycle',
        'steps_total': len(GROWTH_CYCLE),
        'steps': GROWTH_CYCLE,
        'mc_visualizes_growth': True,
        'status': 'specified',
    },
    'neighborhood_dashboard': {
        'title': 'Neighborhood Dashboard',
        'sections': DASHBOARD_SECTIONS,
        'sections_total': len(DASHBOARD_SECTIONS),
        'live': neighborhood_dashboards_live > 0,
        'local_operating_center': True,
        'status': 'specified',
    },
    'neighborhood_health_score': {
        'title': 'Neighborhood Health Score',
        'factors': HEALTH_SCORE_FACTORS,
        'factors_total': len(HEALTH_SCORE_FACTORS),
        'computed': neighborhood_health_score_computed,
        'identifies_support_needs': True,
        'status': 'planned',
    },
    'neighborhood_resource_center': {
        'title': 'Neighborhood Resource Center',
        'items': RESOURCE_CENTER,
        'items_total': len(RESOURCE_CENTER),
        'status': 'specified',
    },
    'neighborhood_mentorship': {
        'title': 'Neighborhood Mentorship',
        'experienced_mentors_another': True,
        'visualizations': MENTORSHIP_VISUALIZATIONS,
        'trees_live': mentorship_trees_live,
        'pairs_active': mentorship_pairs,
        'multiplication_growth': True,
        'status': 'specified',
    },
    'neighborhood_recognition': {
        'title': 'Neighborhood Recognition',
        'milestones': RECOGNITION_MILESTONES,
        'milestones_awarded': recognition_milestones_awarded,
        'reinforces_service_not_competition': True,
        'status': 'specified',
    },
    'two_hundred_k_strategy': {
        'title': 'The 200,000 Arkansan Strategy',
        'target': PARTICIPANTS_TARGET,
        'current_connected': connected_arkansans,
        'growth_at_neighborhood_level': True,
        'leader_questions': TWO_HUNDRED_K_QUESTIONS,
        'statewide_sum_of_local_relationships': True,
    },
    'integration': {
        'chain': (
            'ArCOS (#78) → ACOS (#77) → Education Academy → Citizen Action Center → '
            'Relationship OS → Civic Atlas → Mission Control'
        ),
        'every_neighborhood_connected_node': True,
        'final_layer_of_architecture': True,
        'systems': SYSTEM_CONNECTIONS,
        'extends': 'Neighborhood Organizing (#57)',
    },
    'long_term_vision': (
        'Twenty years after launch: thousands of neighborhood conversations; children see respectful '
        'civic discussion as normal; neighbors gather to learn rather than argue; Education Leaders '
        'become trusted local resources. Institution defined by relationships created throughout Arkansas.'
    ),
    'summary': {
        'neighborhood_profiles_total': neighborhood_profiles_total,
        'neighborhoods_with_digital_twin': neighborhoods_with_digital_twin,
        'neighborhood_dashboards_live': neighborhood_dashboards_live,
        'neighborhoods_with_leader': neighborhoods_with_leader,
        'growth_cycle_steps': len(GROWTH_CYCLE),
        'profile_sections': len(PROFILE_SECTIONS),
        'leadership_roles': len(LEADERSHIP_ROLES),
        'neighborhood_health_score_computed': neighborhood_health_score_computed,
        'mentorship_trees_live': mentorship_trees_live,
        'mentorship_pairs': mentorship_pairs,
        'recognition_milestones_awarded': recognition_milestones_awarded,
        'connected_arkansans': connected_arkansans,
        'participants_target': PARTICIPANTS_TARGET,
        'arkansas_neighborhood_operating_system_readiness_pct': anos_readiness,
        'arkansas_city_operating_system_readiness_pct': arcity.get('summary', {}).get('arkansas_city_operating_system_readiness_pct', 48),
        'arkansas_county_operating_system_readiness_pct': acos.get('summary', {}).get('arkansas_county_operating_system_readiness_pct', 47),
        'neighborhood_organizing_readiness_pct': no.get('summary', {}).get('neighborhood_organizing_readiness_pct', 50),
        'public_launch_readiness_pct': ex.get('public_launch_readiness', 8),
    },
    'catalog_gaps': [
        '0 neighborhood profiles — registry empty',
        '0 neighborhood digital twins operational',
        '0 neighborhood dashboards live — local operating center not built',
        'Neighborhood Health Score not computed — factors specified only',
        'Mentorship trees not live — multiplication visualization missing',
        '0 recognition milestones awarded',
        'Growth cycle specified — no per-neighborhood tracking',
        'Build #79 vs Neighborhood Organizing (#57) — ANOS extends but does not replace',
        'Privacy: residential data policy specified — enforcement not automated',
        'Learning circle resources — not per-neighborhood',
        '200K strategy — 0/200,000 connected',
        'Conversation model environments — no venue registry',
        'Canonical neighborhood routes not built',
    ],
    'recommended_next_build': {
        'number': 80,
        'title': 'Implementation Translation Layer & Engineering Artifacts',
        'note': (
            'Neighborhood profile pages, growth cycle UI, health score, mentorship trees, '
            'recognition milestones, conversation kit delivery, COMP-* specs, GitHub backlog.'
        ),
    },
}

with open(root / 'data/arkansas-neighborhood-operating-system.json', 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')

print(
    f'ANOS: {neighborhood_profiles_total} profiles, '
    f'{neighborhoods_with_digital_twin} digital twins, {anos_readiness}% readiness'
)
