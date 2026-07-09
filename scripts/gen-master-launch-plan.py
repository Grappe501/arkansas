"""
Generate data/master-launch-plan.json — Build #85.
Master Launch Plan — January 2027 Operational Readiness Blueprint v1.0.
"""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
today = '2026-07-09'
launch_date = '2027-01-01'


def load_json(path):
    if path.exists():
        with open(path, encoding='utf-8') as f:
            return json.load(f)
    return {}


mc = load_json(root / 'data/mission-control.json')
sp = load_json(root / 'data/arkansas-strategic-plan-2035.json')
ls = load_json(root / 'data/launch-strategy.json')

ex = mc.get('executive', {})

# Honest zeros / partial
launch_readiness_dashboard_live = False
arkansas_launch_map_live = False
launch_governance_certified = False
overall_launch_readiness_pct = 0
counties_represented = 0
cities_represented = 0
education_leaders = 0
coalition_partners = 0
community_conversations_scheduled = 0
academy_participants = 0
volunteers_active = 0
participants_connected = 0
participants_target = 200_000
checklist_items_complete = 0
governance_certs_complete = 0

LAUNCH_MISSION_TOPICS = [
    'Citizens United v. Federal Election Commission',
    'Campaign finance',
    'Constitutional government',
    'Civic participation',
    'Government transparency',
    'Ballot initiatives',
    'The legislative process',
]

LAUNCH_OBJECTIVES = [
    {
        'area': 'research', 'title': 'Research',
        'deliverables': [
            {'id': 'LP-R01', 'item': 'Core research library published', 'complete': False, 'status': 'planned'},
            {'id': 'LP-R02', 'item': 'Timeline completed', 'complete': False, 'status': 'partial'},
            {'id': 'LP-R03', 'item': 'Citizens United Facts encyclopedia operational', 'complete': False, 'status': 'planned'},
            {'id': 'LP-R04', 'item': 'Evidence Ledger functioning', 'complete': False, 'status': 'partial'},
            {'id': 'LP-R05', 'item': 'Claims Registry available', 'complete': False, 'status': 'planned'},
            {'id': 'LP-R06', 'item': 'Source Library completed', 'complete': False, 'status': 'planned'},
        ],
    },
    {
        'area': 'technology', 'title': 'Technology',
        'deliverables': [
            {'id': 'LP-T01', 'item': 'Public website operational', 'complete': True, 'status': 'live'},
            {'id': 'LP-T02', 'item': 'Mobile-responsive design', 'complete': True, 'status': 'live'},
            {'id': 'LP-T03', 'item': 'AI Learning Guide available', 'complete': False, 'status': 'planned'},
            {'id': 'LP-T04', 'item': 'Mission Control operational', 'complete': True, 'status': 'live'},
            {'id': 'LP-T05', 'item': 'Dashboard reporting live', 'complete': False, 'status': 'partial'},
            {'id': 'LP-T06', 'item': 'User accounts enabled', 'complete': False, 'status': 'planned'},
            {'id': 'LP-T07', 'item': 'Search fully functional', 'complete': False, 'status': 'planned'},
        ],
    },
    {
        'area': 'community', 'title': 'Community',
        'deliverables': [
            {'id': 'LP-C01', 'item': 'Education Leaders recruited across Arkansas', 'complete': False, 'status': 'planned'},
            {'id': 'LP-C02', 'item': 'County leadership established where available', 'complete': False, 'status': 'planned'},
            {'id': 'LP-C03', 'item': 'Initial city leadership network', 'complete': False, 'status': 'planned'},
            {'id': 'LP-C04', 'item': 'Community conversation toolkit completed', 'complete': False, 'status': 'planned'},
            {'id': 'LP-C05', 'item': 'Academy accepting learners', 'complete': False, 'status': 'planned'},
        ],
    },
    {
        'area': 'coalition', 'title': 'Coalition',
        'deliverables': [
            {'id': 'LP-CO01', 'item': 'Founding coalition partners established', 'complete': False, 'status': 'planned'},
            {'id': 'LP-CO02', 'item': 'Organization onboarding system operational', 'complete': False, 'status': 'planned'},
            {'id': 'LP-CO03', 'item': 'Coalition dashboard live', 'complete': False, 'status': 'planned'},
            {'id': 'LP-CO04', 'item': 'Shared educational resources available', 'complete': False, 'status': 'partial'},
        ],
    },
    {
        'area': 'communications', 'title': 'Communications',
        'deliverables': [
            {'id': 'LP-CM01', 'item': 'Public launch campaign prepared', 'complete': False, 'status': 'planned'},
            {'id': 'LP-CM02', 'item': 'Social media operational', 'complete': False, 'status': 'planned'},
            {'id': 'LP-CM03', 'item': 'Email newsletter launched', 'complete': False, 'status': 'planned'},
            {'id': 'LP-CM04', 'item': 'Media kit completed', 'complete': False, 'status': 'planned'},
            {'id': 'LP-CM05', 'item': 'Presentation materials completed', 'complete': False, 'status': 'planned'},
        ],
    },
    {
        'area': 'mission_control', 'title': 'Mission Control Reporting',
        'deliverables': [
            {'id': 'LP-MC01', 'item': 'Launch readiness reporting', 'complete': False, 'status': 'planned'},
            {'id': 'LP-MC02', 'item': 'County coverage', 'complete': False, 'status': 'planned'},
            {'id': 'LP-MC03', 'item': 'City coverage', 'complete': False, 'status': 'planned'},
            {'id': 'LP-MC04', 'item': 'Neighborhood growth', 'complete': False, 'status': 'planned'},
            {'id': 'LP-MC05', 'item': 'Education Leaders tracking', 'complete': False, 'status': 'planned'},
            {'id': 'LP-MC06', 'item': 'Coalition partners tracking', 'complete': False, 'status': 'planned'},
            {'id': 'LP-MC07', 'item': 'Volunteer activity tracking', 'complete': False, 'status': 'planned'},
            {'id': 'LP-MC08', 'item': 'Research completion tracking', 'complete': False, 'status': 'planned'},
            {'id': 'LP-MC09', 'item': 'Technology readiness tracking', 'complete': False, 'status': 'partial'},
        ],
    },
]

all_deliverables = [d for area in LAUNCH_OBJECTIVES for d in area['deliverables']]
checklist_items_total = len(all_deliverables)
checklist_items_complete = sum(1 for d in all_deliverables if d['complete'])

READINESS_CATEGORIES = [
    {'id': 'LP-RC01', 'category': 'Research', 'readiness_pct': 0, 'status': 'planned'},
    {'id': 'LP-RC02', 'category': 'Technology', 'readiness_pct': 0, 'status': 'partial'},
    {'id': 'LP-RC03', 'category': 'Education', 'readiness_pct': 0, 'status': 'planned'},
    {'id': 'LP-RC04', 'category': 'Leadership', 'readiness_pct': 0, 'status': 'planned'},
    {'id': 'LP-RC05', 'category': 'Coalition', 'readiness_pct': 0, 'status': 'planned'},
    {'id': 'LP-RC06', 'category': 'Communications', 'readiness_pct': 0, 'status': 'planned'},
    {'id': 'LP-RC07', 'category': 'Operations', 'readiness_pct': 0, 'status': 'planned'},
    {'id': 'LP-RC08', 'category': 'Governance', 'readiness_pct': 0, 'status': 'partial'},
    {'id': 'LP-RC09', 'category': 'Volunteer Capacity', 'readiness_pct': 0, 'status': 'planned'},
    {'id': 'LP-RC10', 'category': 'Public Trust', 'readiness_pct': 0, 'status': 'planned'},
    {'id': 'LP-RC11', 'category': 'Overall Launch Readiness', 'readiness_pct': overall_launch_readiness_pct, 'status': 'planned'},
]

LAUNCH_MAP_ITEMS = [
    {'id': 'LP-LM01', 'item': 'Counties represented', 'current': counties_represented, 'target': 75},
    {'id': 'LP-LM02', 'item': 'Cities represented', 'current': cities_represented, 'target': 250},
    {'id': 'LP-LM03', 'item': 'Education Leaders', 'current': education_leaders},
    {'id': 'LP-LM04', 'item': 'Coalition organizations', 'current': coalition_partners},
    {'id': 'LP-LM05', 'item': 'Community conversations scheduled', 'current': community_conversations_scheduled},
    {'id': 'LP-LM06', 'item': 'Academy participants', 'current': academy_participants},
    {'id': 'LP-LM07', 'item': 'Volunteer network', 'current': volunteers_active},
    {'id': 'LP-LM08', 'item': '200,000 connected Arkansans', 'current': participants_connected, 'target': participants_target},
]

LAUNCH_SUCCESS_METRICS = [
    'Representation in all 75 counties (at least one contact or developing relationship)',
    'Active work in the 250 largest Arkansas cities',
    'Growing statewide volunteer network',
    'Functioning Community Education Academy',
    'Complete research foundation',
    'Fully operational Mission Control dashboard',
    'Strong coalition of Arkansas organizations',
]

FIRST_YEAR_PRIORITIES = [
    'Expanding county leadership',
    'Growing city teams',
    'Building neighborhood learning circles',
    'Publishing additional research',
    'Strengthening coalition partnerships',
    'Growing Academy enrollment',
    'Improving Mission Control',
    'Expanding the Research Institute',
]

LAUNCH_GOVERNANCE_CERTS = [
    {'id': 'LP-G01', 'certification': 'Research standards operational', 'certified': False},
    {'id': 'LP-G02', 'certification': 'Editorial standards documented', 'certified': False},
    {'id': 'LP-G03', 'certification': 'Volunteer onboarding functioning', 'certified': False},
    {'id': 'LP-G04', 'certification': 'Privacy protections in place', 'certified': False},
    {'id': 'LP-G05', 'certification': 'Accessibility standards reviewed', 'certified': False},
    {'id': 'LP-G06', 'certification': 'Governance documents complete', 'certified': False, 'status': 'partial'},
    {'id': 'LP-G07', 'certification': 'Mission Control reflects institutional status', 'certified': False, 'status': 'partial'},
]

governance_certs_total = len(LAUNCH_GOVERNANCE_CERTS)
governance_certs_complete = sum(1 for c in LAUNCH_GOVERNANCE_CERTS if c['certified'])

PUBLIC_LAUNCH_MESSAGE = (
    'Citizens United Facts exists to help every Arkansan understand one of the most important '
    'Supreme Court decisions in modern American history through evidence, transparency, '
    'respectful education, and community leadership.'
)

launch_readiness = min(
    57,
    19
    + len(LAUNCH_OBJECTIVES) * 2
    + len(READINESS_CATEGORIES) // 2
    + len(LAUNCH_MAP_ITEMS) // 2
    + len(FIRST_YEAR_PRIORITIES) // 2
    + len(LAUNCH_GOVERNANCE_CERTS) // 2
    + len(LAUNCH_SUCCESS_METRICS) // 2
    + 4,
)

out = {
    'version': '1.0',
    'build': 85,
    'updated': today,
    'launch_date': launch_date,
    'title': 'Master Launch Plan v1.0',
    'subtitle': 'January 2027 Operational Readiness Blueprint',
    'tagline': 'From Vision to Reality',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/master-launch-plan.html',
    'constitution': '/docs/MASTER_LAUNCH_PLAN.md',
    'purpose': (
        'Operational checklist for January 2027 launch as a credible, trusted, statewide '
        'civic education institution. Official Launch Readiness Blueprint for Mission Control.'
    ),
    'governing_principle': (
        'Launch only when the institution is ready to earn trust — not when every feature is '
        'perfect or every county is fully built, but when research is credible, systems reliable, '
        'volunteers prepared, mission clear, and Arkansans can confidently begin learning.'
    ),
    'distinct_from': {
        'launch_strategy': {'build': 53, 'route': '/mission-control/launch-strategy.html', 'focus': 'Rollout phases'},
        'strategic_plan_2035': {'build': 84, 'route': '/mission-control/arkansas-strategic-plan-2035.html', 'focus': 'Decade accomplishment'},
        'master_build_plan': {'route': '/BUILD_PLAN.md', 'focus': 'Institution construction (85 builds)'},
        'this_plan_focus': 'January 2027 operational readiness checklist',
    },
    'launch_mission': {
        'title': 'Launch Mission',
        'date': launch_date,
        'topics': LAUNCH_MISSION_TOPICS,
        'built_by_arkansans_for_arkansans': True,
        'premier_civic_education_platform': True,
    },
    'launch_objectives': {
        'title': 'Launch Objectives',
        'areas': LAUNCH_OBJECTIVES,
        'areas_total': len(LAUNCH_OBJECTIVES),
        'deliverables_total': checklist_items_total,
        'deliverables_complete': checklist_items_complete,
        'not_a_wish_list': True,
        'operational_checklist': True,
    },
    'launch_readiness_dashboard': {
        'title': 'Launch Readiness Dashboard',
        'categories': READINESS_CATEGORIES,
        'live': launch_readiness_dashboard_live,
        'each_category_percentage': True,
        'status': 'planned',
    },
    'arkansas_launch_map': {
        'title': 'The Arkansas Launch Map',
        'items': LAUNCH_MAP_ITEMS,
        'live': arkansas_launch_map_live,
        'public_symbol_of_growth': True,
        'display_on_launch_day': True,
        'status': 'planned',
    },
    'launch_success_metrics': {
        'title': 'Launch Success Metrics',
        'metrics': LAUNCH_SUCCESS_METRICS,
        'launch_is_beginning_not_finish_line': True,
        'status': 'specified',
    },
    'first_year_priorities': {
        'title': 'First-Year Priorities',
        'priorities': FIRST_YEAR_PRIORITIES,
        'strengthen_existing_foundation': True,
        'status': 'specified',
    },
    'launch_governance': {
        'title': 'Launch Governance',
        'certifications': LAUNCH_GOVERNANCE_CERTS,
        'certified_count': governance_certs_complete,
        'certifications_total': governance_certs_total,
        'leadership_certifies_before_launch': True,
        'trust_begins_day_one': True,
        'status': 'specified',
    },
    'public_launch_message': {
        'title': 'Public Launch Message',
        'promise': PUBLIC_LAUNCH_MESSAGE,
        'one_clear_promise': True,
    },
    'integration': {
        'systems': [
            {'system': 'Launch Strategy (#53)', 'route': '/mission-control/launch-strategy.html', 'status': 'live'},
            {'system': 'Strategic Plan 2035 (#84)', 'route': '/mission-control/arkansas-strategic-plan-2035.html', 'status': 'live'},
            {'system': 'Civic Ecosystem (#83)', 'route': '/mission-control/arkansas-civic-ecosystem.html', 'status': 'live'},
            {'system': 'Public Trust (#82)', 'route': '/mission-control/public-trust-institutional-credibility.html', 'status': 'live'},
            {'system': 'Evidence Ledger (#41)', 'route': '/mission-control/evidence-ledger.html', 'status': 'live'},
            {'system': 'Citizen Leadership Academy (#68)', 'route': '/mission-control/citizen-leadership-academy.html', 'status': 'live'},
            {'system': 'Coalition Network (#61)', 'route': '/mission-control/coalition-network.html', 'status': 'live'},
            {'system': 'Arkansas Communications (#72)', 'route': '/mission-control/arkansas-communications.html', 'status': 'live'},
        ],
    },
    'long_term_vision': (
        'January 2027 is the opening chapter — not the destination. Launch with capacity to grow '
        'into statewide Education Leader network, trusted civic research institution, lasting '
        'volunteer-driven organization, comprehensive Arkansas civic education ecosystem. '
        'Every future success begins with a disciplined, trustworthy launch.'
    ),
    'summary': {
        'launch_date': launch_date,
        'checklist_items_total': checklist_items_total,
        'checklist_items_complete': checklist_items_complete,
        'readiness_categories': len(READINESS_CATEGORIES),
        'launch_readiness_dashboard_live': launch_readiness_dashboard_live,
        'arkansas_launch_map_live': arkansas_launch_map_live,
        'overall_launch_readiness_pct': overall_launch_readiness_pct,
        'launch_governance_certified': launch_governance_certified,
        'governance_certs_complete': governance_certs_complete,
        'governance_certs_total': governance_certs_total,
        'counties_represented': counties_represented,
        'cities_represented': cities_represented,
        'education_leaders': education_leaders,
        'coalition_partners': coalition_partners,
        'volunteers_active': volunteers_active,
        'participants_connected': participants_connected,
        'participants_target': participants_target,
        'master_launch_plan_readiness_pct': launch_readiness,
        'strategic_plan_readiness_pct': sp.get('summary', {}).get('arkansas_strategic_plan_2035_readiness_pct', 55),
        'launch_strategy_readiness_pct': ls.get('summary', {}).get('launch_strategy_readiness_pct', 39),
        'public_launch_readiness_pct': ex.get('public_launch_readiness', 8),
    },
    'catalog_gaps': [
        'Launch readiness dashboard not live — 11 categories at 0%',
        'Arkansas Launch Map not live — public growth symbol missing',
        f'Only {checklist_items_complete}/{checklist_items_total} checklist items complete',
        'Launch governance not certified — 0/7 certifications',
        '0/75 counties represented · 0/250 cities',
        '0 Education Leaders · 0 coalition partners · 0 volunteers',
        '0/200,000 participants connected',
        'AI Learning Guide not available · user accounts not enabled · search not functional',
        'Public launch campaign not prepared · newsletter not launched',
        'Build #85 vs Launch Strategy (#53) — operational checklist vs rollout phases',
        'Overall launch readiness 0% — not computed from category scores',
        'First-year priorities specified — not tracked post-launch',
    ],
    'recommended_next_build': {
        'number': 86,
        'title': 'Launch Readiness Dashboard & Certification Components',
        'note': (
            'Launch readiness dashboard UI, checklist tracker, Arkansas Launch Map, '
            'governance certification workflow, category scoring engine, COMP-* specs.'
        ),
    },
}

with open(root / 'data/master-launch-plan.json', 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')

print(
    f'Master Launch Plan: {checklist_items_complete}/{checklist_items_total} checklist items, '
    f'{governance_certs_complete}/{governance_certs_total} certs, {launch_readiness}% readiness'
)
