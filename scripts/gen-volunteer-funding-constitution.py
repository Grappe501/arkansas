"""
Generate data/volunteer-funding-constitution.json — Build #75.
Master Volunteer & Funding Constitution v1.0.
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
ss = load_json(root / 'data/sustainability-stewardship.json')
aan = load_json(root / 'data/arkansas-action-network.json')
cla = load_json(root / 'data/citizen-leadership-academy.json')

ex = mc.get('executive', {})

# Honest zeros
active_volunteers = ss.get('summary', {}).get('volunteers_onboarded', 0)
volunteer_hours_reported = 0
education_leaders = cla.get('summary', {}).get('education_leaders', 0)
county_leadership_coverage = aan.get('summary', {}).get('county_teams', 0)
counties_target = aan.get('summary', {}).get('county_teams_target', 75)
coalition_participation = 0
community_conversations = 0
funding_sources = ss.get('summary', {}).get('funding_sources_active', 0)
revenue_tracked = 0
adherence_monitoring_live = False
constitution_dashboard_live = False
recognition_milestones_awarded = 0

VOLUNTEER_FUNCTIONS = [
    'Research assistance', 'Educational writing', 'Community conversations',
    'Education Leaders', 'County leadership', 'Coalition coordination',
    'Event support', 'Presentation teams', 'Community outreach', 'Mentorship',
]

FUNDING_USE_CASES = [
    'Ballot initiative education', 'Petition administration', 'Required legal compliance',
    'Accounting', 'Technology infrastructure', 'Educational materials', 'Administrative expenses',
]

ORGANIZATIONAL_CONTRIBUTIONS = [
    'Educational collaboration', 'Sharing facilities', 'Volunteers', 'Expertise',
    'Joint educational programming', 'Resource sharing',
]

TRANSPARENCY_RECORDS = [
    'Revenue sources', 'Major expense categories', 'Financial policies', 'Governance decisions',
]

NO_SPECIAL_ACCESS_PROHIBITIONS = [
    'Editorial influence', 'Research outcomes', 'Educational conclusions',
    'Governance authority', 'Preferred treatment',
]

STEWARDSHIP_EXAMPLES = [
    'Educational materials', 'Technology improvements', 'Accessibility enhancements',
    'Community education resources', 'Volunteer support', 'Research infrastructure',
]

VOLUNTEER_RECOGNITION = [
    'Service milestones', 'Leadership development', 'Mentorship recognition',
    'Educational achievements', 'Community impact',
]

SUSTAINABILITY_REQUIREMENTS = [
    'Strong documentation', 'Volunteer leadership', 'Efficient technology',
    'Shared knowledge', 'Careful planning',
]

CONSTITUTION_DASHBOARD = [
    {'id': 'VFC-D1', 'indicator': 'Active volunteers', 'current': active_volunteers, 'status': 'planned'},
    {'id': 'VFC-D2', 'indicator': 'Volunteer hours (voluntarily reported)', 'current': volunteer_hours_reported, 'status': 'planned'},
    {'id': 'VFC-D3', 'indicator': 'Education Leaders', 'current': education_leaders, 'status': 'planned'},
    {'id': 'VFC-D4', 'indicator': 'County leadership coverage', 'current': county_leadership_coverage, 'target': counties_target, 'status': 'planned'},
    {'id': 'VFC-D5', 'indicator': 'Coalition participation', 'current': coalition_participation, 'status': 'planned'},
    {'id': 'VFC-D6', 'indicator': 'Community conversations', 'current': community_conversations, 'status': 'planned'},
    {'id': 'VFC-D7', 'indicator': 'Funding sources (transparent)', 'current': funding_sources, 'status': 'planned'},
    {'id': 'VFC-D8', 'indicator': 'Sustainability indicators', 'current': 'not_tracked', 'status': 'planned'},
]

SYSTEM_CONNECTIONS = [
    {'system': 'Community Education Academy (#28)', 'route': '/mission-control/education-academy.html', 'status': 'partial'},
    {'system': 'Coalition Network (#61)', 'route': '/mission-control/coalition-network.html', 'status': 'live'},
    {'system': 'Relationship OS (#59)', 'route': '/mission-control/relationship-os.html', 'status': 'live'},
    {'system': 'Citizen Action Center (#62)', 'route': '/mission-control/citizen-action-center.html', 'status': 'live'},
    {'system': 'Arkansas Action Network (#64)', 'route': '/mission-control/arkansas-action-network.html', 'status': 'live'},
    {'system': 'Sustainability & Stewardship (#66)', 'route': '/mission-control/sustainability-stewardship.html', 'status': 'live', 'note': 'Operational blueprint'},
    {'system': 'Governance Constitution (#49)', 'route': '/mission-control/governance.html', 'status': 'live'},
    {'system': 'Mission Control', 'route': '/mission-control/', 'status': 'live'},
]

volunteer_funding_constitution_readiness = min(
    45,
    11 + len(VOLUNTEER_FUNCTIONS) * 2 + len(NO_SPECIAL_ACCESS_PROHIBITIONS) * 2 + 6,
)

out = {
    'version': '1.0',
    'build': 75,
    'updated': today,
    'title': 'Master Volunteer & Funding Constitution v1.0',
    'subtitle': 'The Institutional Independence Charter',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/volunteer-funding-constitution.html',
    'constitution': '/docs/MASTER_VOLUNTEER_FUNDING_CONSTITUTION.md',
    'purpose': (
        'Founding principles protecting institutional independence and public trust — '
        'how the institution is organized and supported.'
    ),
    'governing_principle': (
        'Belongs to people who build it and communities it serves. Foundation: volunteer service. '
        'Mission: civic education. Strength: public trust. Education independent, transparent, '
        'evidence-based, rooted in voluntary Arkansas support.'
    ),
    'founding_principle': {
        'all_volunteer_arkansas_institution': True,
        'educate_first_and_always': True,
        'strength_from_arkansans': True,
    },
    'volunteer_first': {
        'title': 'Volunteer First',
        'designed_for_trained_volunteers': True,
        'functions': VOLUNTEER_FUNCTIONS,
        'celebrate_volunteer_service': True,
        'active_volunteers': active_volunteers,
        'status': 'specified',
    },
    'financial_independence': {
        'title': 'Financial Independence',
        'neutrality_protected': True,
        'stewardship_supports_mission_not_defines': True,
        'status': 'specified',
    },
    'arkansas_citizen_support': {
        'title': 'Arkansas Citizen Support',
        'preferred_model': 'Individual voluntary contributions from Arkansas citizens',
        'when_necessary_for': FUNDING_USE_CASES,
        'supported_by_people_served': True,
        'funding_sources': funding_sources,
        'status': 'specified',
    },
    'organizational_contributions': {
        'title': 'Organizational Contributions',
        'contribution_types': ORGANIZATIONAL_CONTRIBUTIONS,
        'distinguish_collaboration_from_financial': True,
        'status': 'specified',
    },
    'transparency': {
        'title': 'Transparency',
        'internal_records': TRANSPARENCY_RECORDS,
        'public_transparency': True,
        'revenue_tracked': revenue_tracked,
        'status': 'specified',
    },
    'no_special_access': {
        'title': 'No Special Access',
        'contributions_never_purchase': NO_SPECIAL_ACCESS_PROHIBITIONS,
        'integrity_independent_of_support': True,
        'status': 'live',
    },
    'stewardship_philosophy': {
        'title': 'Stewardship Philosophy',
        'question': 'How does this improve civic education for Arkansas?',
        'examples': STEWARDSHIP_EXAMPLES,
        'connect_investments_to_outcomes': True,
        'status': 'specified',
    },
    'volunteer_recognition': {
        'title': 'Volunteer Recognition',
        'recognition_types': VOLUNTEER_RECOGNITION,
        'honors_service_not_status': True,
        'milestones_awarded': recognition_milestones_awarded,
        'status': 'planned',
    },
    'sustainability': {
        'title': 'Sustainability',
        'operate_during_limited_resources': True,
        'requirements': SUSTAINABILITY_REQUIREMENTS,
        'resilience_by_design': True,
        'status': 'specified',
    },
    'constitution_dashboard': {
        'title': 'Mission Control Constitution Dashboard',
        'live': constitution_dashboard_live,
        'adherence_monitoring': adherence_monitoring_live,
        'indicators': CONSTITUTION_DASHBOARD,
        'status': 'planned',
    },
    'integration': {
        'chain': (
            'Education Academy → Coalition Network → Relationship OS → Citizen Action Center → '
            'Action Network → Governance → Sustainability → Mission Control'
        ),
        'systems': SYSTEM_CONNECTIONS,
        'every_system_reflects_principles': True,
        'extends': 'Sustainability & Stewardship (#66) — constitutional foundation for volunteer and funding principles',
    },
    'long_term_vision': (
        'Recognized as built by Arkansans, for Arkansans. Greatest resource: thousands of volunteers '
        'helping neighbors understand constitutional system, campaign finance, civic participation. '
        'Financial support strengthens mission while preserving independence and public trust.'
    ),
    'summary': {
        'volunteer_functions': len(VOLUNTEER_FUNCTIONS),
        'active_volunteers': active_volunteers,
        'volunteer_hours_reported': volunteer_hours_reported,
        'education_leaders': education_leaders,
        'county_leadership_coverage': county_leadership_coverage,
        'counties_target': counties_target,
        'coalition_participation': coalition_participation,
        'community_conversations': community_conversations,
        'funding_sources': funding_sources,
        'revenue_tracked': revenue_tracked,
        'recognition_milestones_awarded': recognition_milestones_awarded,
        'adherence_monitoring_live': adherence_monitoring_live,
        'constitution_dashboard_live': constitution_dashboard_live,
        'volunteer_funding_constitution_readiness_pct': volunteer_funding_constitution_readiness,
        'sustainability_stewardship_readiness_pct': ss.get('summary', {}).get('sustainability_stewardship_readiness_pct', 38),
        'public_launch_readiness_pct': ex.get('public_launch_readiness', 8),
    },
    'catalog_gaps': [
        '0 active volunteers — volunteer registry not built',
        '0 volunteer hours reported — no voluntary hours tracking UI',
        '0 funding sources — revenue transparency not operational',
        'Adherence monitoring specified — not live in Mission Control',
        'Constitution dashboard planned — not live',
        '0 recognition milestones — volunteer recognition system not built',
        'Build #75 vs Sustainability (#66) — reconcile constitution vs operational blueprint?',
        'Organizational vs financial contribution distinction — no UI pattern',
        'No special access policy — not enforced in workflow',
        'Arkansas citizen funding model specified — no donation intake',
        'County leadership coverage 0/75 — volunteer constitution ahead of network',
        'Financial records internal only — no public transparency page',
        'MC does not yet monitor constitution adherence alongside health indicators',
    ],
    'recommended_next_build': {
        'number': 76,
        'title': 'Implementation Translation Layer & Engineering Artifacts',
        'note': (
            'Volunteer registry, funding transparency UI, adherence checklist, recognition milestones, '
            'donation intake spec, COMP-* specs, GitHub backlog.'
        ),
    },
}

with open(root / 'data/volunteer-funding-constitution.json', 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')

print(
    f'Volunteer & Funding Constitution: {active_volunteers} volunteers, '
    f'{funding_sources} funding sources, {volunteer_funding_constitution_readiness}% readiness'
)
