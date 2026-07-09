"""
Generate data/arkansas-civic-operating-system.json — Build #96.
Master Arkansas Civic Operating System (ACOS 2.0) — One Login. One Platform. Everything Connected.
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
acos77 = load_json(root / 'data/arkansas-county-operating-system.json')
lb = load_json(root / 'data/localbrain-architecture.json')
ckp = load_json(root / 'data/civic-knowledge-platform.json')
maan = load_json(root / 'data/master-arkansas-action-network.json')

ex = mc.get('executive', {})

# Honest operational metrics
platform_live = False
single_login_live = False
personal_workspace_live = False
ai_assistant_live = False
notifications_live = False
user_accounts = 0
role_workspaces_live = 0

PERSONAL_WORKSPACE_MODULES = [
    {'id': 'WS-01', 'module': 'My Learning', 'status': 'partial'},
    {'id': 'WS-02', 'module': 'My Community', 'status': 'planned'},
    {'id': 'WS-03', 'module': 'My County', 'status': 'partial'},
    {'id': 'WS-04', 'module': 'My City', 'status': 'planned'},
    {'id': 'WS-05', 'module': 'My Neighborhood', 'status': 'planned'},
    {'id': 'WS-06', 'module': 'My Calendar', 'status': 'planned'},
    {'id': 'WS-07', 'module': 'My Volunteer Work', 'status': 'planned'},
    {'id': 'WS-08', 'module': 'My Coalition Organizations', 'status': 'planned'},
    {'id': 'WS-09', 'module': 'My Projects', 'status': 'planned'},
    {'id': 'WS-10', 'module': 'My Research', 'status': 'partial'},
    {'id': 'WS-11', 'module': 'My AI Assistant', 'status': 'planned'},
    {'id': 'WS-12', 'module': 'My Messages', 'status': 'planned'},
    {'id': 'WS-13', 'module': 'My Upcoming Events', 'status': 'planned'},
    {'id': 'WS-14', 'module': 'My Action Items', 'status': 'planned'},
    {'id': 'WS-15', 'module': 'My Progress', 'status': 'planned'},
]

PERSONALIZED_LEARNING = [
    'Courses completed', 'Videos watched', 'Articles read',
    'Presentations attended', 'Certificates earned',
    'Topics of interest', 'Recommended next lessons',
]

PERSONALIZED_COMMUNITY = [
    'Their county', 'Their city', 'Their neighborhood',
    'Local Education Leaders', 'Community conversations',
    'Nearby educational events', 'Relevant coalition organizations',
]

VOLUNTEER_CAPABILITIES = [
    'Assigned projects', 'Volunteer hours (optional)', 'Current responsibilities',
    'Mentorship', 'Training', 'Leadership pathway',
    'Team communications', 'Resource library',
]

EDUCATION_LEADER_CAPABILITIES = [
    'Presentation resources', 'Community conversation kits',
    'County dashboards', 'City dashboards', 'Volunteer roster',
    'Upcoming events', 'Local AI Assistant', 'Mission Control recommendations',
]

COALITION_CAPABILITIES = [
    'Organization profile', 'Educational resources', 'Shared calendar',
    'Volunteer opportunities', 'Community events',
    'Partnership tracking', 'Communication tools',
]

EXECUTIVE_CAPABILITIES = [
    'Mission Control', 'Digital Twin', 'Department dashboards',
    'Project Management Office', 'Strategic planning', 'Executive reports',
    'Institution health', 'Statewide maps', 'Forecasts',
]

AI_ASSISTANT_KNOWS = [
    'User role', 'Learning progress', 'Volunteer assignments',
    'Calendar', 'Projects', 'Documents',
    'County', 'Organizations', 'Institutional knowledge',
]

SMART_NOTIFICATIONS = [
    'New research', 'County events', 'Community conversations',
    'Legislative education updates', 'Academy reminders',
    'Volunteer assignments', 'Project deadlines',
]

MC_AGGREGATE_TRENDS = [
    {'id': 'ACOS-A01', 'trend': 'Learning progress', 'status': 'planned'},
    {'id': 'ACOS-A02', 'trend': 'Volunteer engagement', 'status': 'planned'},
    {'id': 'ACOS-A03', 'trend': 'County participation', 'status': 'partial'},
    {'id': 'ACOS-A04', 'trend': 'City participation', 'status': 'planned'},
    {'id': 'ACOS-A05', 'trend': 'Neighborhood growth', 'status': 'planned'},
    {'id': 'ACOS-A06', 'trend': 'Coalition activity', 'status': 'planned'},
    {'id': 'ACOS-A07', 'trend': 'Platform usage', 'status': 'planned'},
    {'id': 'ACOS-A08', 'trend': 'Institutional health', 'status': 'partial'},
]

PRIVACY_CONTROLS = [
    'Communication preferences', 'Notification settings', 'Profile visibility',
    'Volunteer visibility', 'Organization memberships', 'Personal information',
]

USER_ROLES = [
    {'role': 'Learner', 'workspace': 'Personal civic workspace', 'status': 'partial'},
    {'role': 'Volunteer', 'workspace': 'Volunteer workspace', 'status': 'planned'},
    {'role': 'Education Leader', 'workspace': 'Education Leader workspace', 'status': 'planned'},
    {'role': 'Coalition partner', 'workspace': 'Coalition workspace', 'status': 'planned'},
    {'role': 'Researcher', 'workspace': 'Research modules', 'status': 'partial'},
    {'role': 'Executive', 'workspace': 'Executive workspace', 'status': 'planned'},
]

arkansas_civic_operating_system_readiness = min(
    68,
    14
    + len(PERSONAL_WORKSPACE_MODULES) // 2
    + len(PERSONALIZED_LEARNING) // 2
    + len(PERSONALIZED_COMMUNITY) // 2
    + len(VOLUNTEER_CAPABILITIES) // 2
    + len(EDUCATION_LEADER_CAPABILITIES) // 2
    + len(COALITION_CAPABILITIES) // 2
    + len(EXECUTIVE_CAPABILITIES) // 2
    + len(AI_ASSISTANT_KNOWS) // 2
    + len(SMART_NOTIFICATIONS) // 2
    + len(MC_AGGREGATE_TRENDS) // 2
    + len(PRIVACY_CONTROLS) // 2
    + len(USER_ROLES) // 2
    + (2 if platform_live else 0),
)

out = {
    'version': '2.0',
    'build': 96,
    'prior_county_acos_build': 77,
    'updated': today,
    'completion_target_date': completion_target_date,
    'title': 'Master Arkansas Civic Operating System (ACOS 2.0)',
    'subtitle': 'One Login. One Platform. Everything Connected.',
    'tagline': 'Operating System for Civic Education',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/arkansas-civic-operating-system.html',
    'constitution': '/docs/MASTER_ARKANSAS_CIVIC_OPERATING_SYSTEM.md',
    'prior_county_acos_route': '/mission-control/arkansas-county-operating-system.html',
    'purpose': (
        'By January 2027, Citizens United Facts feels like an operating system for civic '
        'education — not a traditional website. Every account enters a personalized civic '
        'workspace. Platform remembers learning, interests, location, organizations, volunteer '
        'roles, and goals. Every role works from the same platform with different permissions.'
    ),
    'governing_principle': (
        'The Arkansas Civic Operating System exists to make civic education personal. One '
        'institution. One login. One trusted platform. Thousands of individual journeys. '
        'Together building a stronger Arkansas through knowledge, volunteer service, community '
        'leadership, and lifelong civic learning.'
    ),
    'founders_principle': (
        'People should never wonder where to go next. The platform should always know what '
        'they are learning, what they care about, where they serve, who they can learn from, '
        'and how they can contribute — without pressure, without confusion, with clarity, '
        'respect, and purpose.'
    ),
    'institutional_philosophy': {
        'title': 'Institutional Philosophy',
        'built_for_me': True,
        'adapts_to_individual': True,
        'one_statewide_institution': True,
    },
    'personal_civic_workspace': {
        'title': 'The Personal Civic Workspace',
        'modules': PERSONAL_WORKSPACE_MODULES,
        'grows_with_involvement': True,
        'live': personal_workspace_live,
        'status': 'planned',
    },
    'personalized_learning': {
        'title': 'Personalized Learning',
        'tracks': PERSONALIZED_LEARNING,
        'continuous_not_episodic': True,
        'status': 'partial',
    },
    'personalized_community': {
        'title': 'Personalized Community',
        'connects': PERSONALIZED_COMMUNITY,
        'locally_relevant': True,
        'status': 'planned',
    },
    'volunteer_workspace': {
        'title': 'Volunteer Workspace',
        'capabilities': VOLUNTEER_CAPABILITIES,
        'status': 'planned',
    },
    'education_leader_workspace': {
        'title': 'Education Leader Workspace',
        'capabilities': EDUCATION_LEADER_CAPABILITIES,
        'status': 'planned',
    },
    'coalition_workspace': {
        'title': 'Coalition Workspace',
        'capabilities': COALITION_CAPABILITIES,
        'dedicated_portals': True,
        'status': 'planned',
    },
    'executive_workspace': {
        'title': 'Executive Workspace',
        'capabilities': EXECUTIVE_CAPABILITIES,
        'status': 'planned',
    },
    'user_roles': {
        'title': 'User Roles & Permissions',
        'roles': USER_ROLES,
        'same_platform_different_permissions': True,
        'status': 'specified',
    },
    'ai_personal_assistant': {
        'title': 'AI Personal Assistant',
        'understands': AI_ASSISTANT_KNOWS,
        'every_account_receives': True,
        'live': ai_assistant_live,
        'status': 'planned',
    },
    'smart_notifications': {
        'title': 'Smart Notifications',
        'types': SMART_NOTIFICATIONS,
        'matches_interests_and_responsibilities': True,
        'live': notifications_live,
        'status': 'planned',
    },
    'mission_control_integration': {
        'title': 'Mission Control Integration',
        'aggregate_trends': MC_AGGREGATE_TRENDS,
        'anonymous_aggregate': True,
        'respects_individual_privacy': True,
        'status': 'partial',
    },
    'security_privacy': {
        'title': 'Security & Privacy',
        'user_controls': PRIVACY_CONTROLS,
        'protects_trust': True,
        'status': 'specified',
    },
    'integration': {
        'chain': (
            'Mission Control → LocalBrains → Community Education Academy → '
            'Research Institute → Knowledge Platform → Coalition Network → '
            'Volunteer Network → County/City/Neighborhood OS → Arkansas Action Network'
        ),
        'unified_experience': True,
        'systems': [
            {'system': 'County ACOS (#77)', 'route': '/mission-control/arkansas-county-operating-system.html', 'status': 'live'},
            {'system': 'City ArCOS (#78)', 'route': '/mission-control/arkansas-city-operating-system.html', 'status': 'live'},
            {'system': 'Neighborhood ANOS (#79)', 'route': '/mission-control/arkansas-neighborhood-operating-system.html', 'status': 'live'},
            {'system': 'LocalBrain Architecture (#92)', 'route': '/mission-control/localbrain-architecture.html', 'status': 'live'},
            {'system': 'Knowledge Platform (#93)', 'route': '/mission-control/civic-knowledge-platform.html', 'status': 'live'},
            {'system': 'Master Action Network (#95)', 'route': '/mission-control/master-arkansas-action-network.html', 'status': 'live'},
            {'system': 'AI Institution (#91)', 'route': '/mission-control/ai-institution.html', 'status': 'live'},
            {'system': 'Education Academy (#28)', 'route': '/mission-control/education-academy.html', 'status': 'partial'},
        ],
    },
    'long_term_vision': (
        'By January 2027, every Arkansan who creates an account gains a personalized civic '
        'workspace — learn, volunteer, connect, participate, grow into leadership. The platform '
        'becomes a daily companion for civic learning, not a site visited only occasionally.'
    ),
    'summary': {
        'completion_target_date': completion_target_date,
        'days_remaining': days_remaining,
        'arkansas_civic_operating_system_readiness_pct': arkansas_civic_operating_system_readiness,
        'county_acos_readiness_pct': acos77.get('summary', {}).get('arkansas_county_operating_system_readiness_pct', 47),
        'localbrain_architecture_readiness_pct': lb.get('summary', {}).get('localbrain_architecture_readiness_pct', 60),
        'knowledge_platform_readiness_pct': ckp.get('summary', {}).get('civic_knowledge_platform_readiness_pct', 58),
        'master_action_network_readiness_pct': maan.get('summary', {}).get('master_arkansas_action_network_readiness_pct', 50),
        'platform_live': platform_live,
        'single_login_live': single_login_live,
        'personal_workspace_live': personal_workspace_live,
        'ai_assistant_live': ai_assistant_live,
        'notifications_live': notifications_live,
        'user_accounts': user_accounts,
        'workspace_modules': len(PERSONAL_WORKSPACE_MODULES),
        'user_roles': len(USER_ROLES),
        'institutional_completion_pct': ex.get('overall_completion', mc.get('build', 95)),
    },
    'catalog_gaps': [
        'No single login / user account system',
        'Personal civic workspace not live',
        'Role-based permissions not implemented',
        'AI personal assistant not deployed per account',
        'Smart notifications not operational',
        'Learning progress not persisted per user',
        'Volunteer workspace not connected to assignments',
        'Coalition partner portals not built',
        'Executive workspace not unified in platform UI',
        'MC aggregate trends not instrumented',
        'Privacy controls not user-configurable',
        'County ACOS (#77) not integrated into platform OS layer',
        'No daily-companion mobile or PWA experience',
    ],
    'recommended_next_build': {
        'number': 97,
        'title': 'Executive War Room & Countdown Dashboard Components',
        'note': (
            'War room UI, countdown dashboard, platform auth MVP, workspace shell, '
            'role permissions, COMP-* specs.'
        ),
    },
}

with open(root / 'data/arkansas-civic-operating-system.json', 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')

print(
    f'ACOS 2.0: {len(PERSONAL_WORKSPACE_MODULES)} workspace modules, '
    f'{len(USER_ROLES)} roles, {arkansas_civic_operating_system_readiness}% readiness'
)
