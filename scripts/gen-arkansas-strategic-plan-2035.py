"""
Generate data/arkansas-strategic-plan-2035.json — Build #84.
Master Arkansas Strategic Plan 2035 v1.0.
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
eco = load_json(root / 'data/arkansas-civic-ecosystem.json')

ex = mc.get('executive', {})

# Honest zeros
strategic_scorecard_live = False
annual_strategic_review_conducted = False
counties_active = 0
counties_target = 75
cities_active = 0
cities_target = 250
participants_connected = 0
participants_target = 200_000
academy_graduates = 0
education_leaders = 0
coalition_organizations = 0
research_library_items = 0
educational_assets = 0
institutional_health_score = 0
trust_score = 0
five_year_milestones_achieved = 0
ten_year_milestones_achieved = 0

STRATEGIC_VISION_TOPICS = [
    'Citizens United v. Federal Election Commission',
    'Campaign finance',
    'Constitutional government',
    'Civic participation',
    'Government transparency',
    'Public policy processes',
]

STRATEGIC_MISSION_PILLARS = [
    'Evidence', 'Research', 'Volunteer leadership',
    'Community conversations', 'Constitutional literacy', 'Public trust',
]

STRATEGIC_GOALS = [
    {
        'goal': 1, 'id': 'build_institution', 'title': 'Build the Institution',
        'description': 'Complete technological, operational, and educational infrastructure',
        'initiatives': [
            'Mission Control', 'Knowledge Graph', 'Community Education Academy',
            'Campaign Finance Observatory', 'Arkansas Civic Atlas', 'Volunteer systems',
        ],
        'status': 'in_progress',
    },
    {
        'goal': 2, 'id': 'build_knowledge', 'title': 'Build the Knowledge Base',
        'description': 'Most comprehensive Arkansas educational library on civic topics',
        'initiatives': [
            'Citizens United', 'Campaign finance', 'Constitutional history',
            'Supreme Court precedent', 'Arkansas civic processes', 'Government transparency',
        ],
        'status': 'in_progress',
    },
    {
        'goal': 3, 'id': 'build_leadership', 'title': 'Build Leadership',
        'description': 'Leadership as the institution greatest multiplier',
        'initiatives': [
            'Education Leaders', 'City Coordinators', 'County Directors',
            'Regional Mentors', 'Academy Fellows',
        ],
        'status': 'planned',
    },
    {
        'goal': 4, 'id': 'build_communities', 'title': 'Build Communities',
        'description': 'Active educational networks statewide',
        'initiatives': ['75 counties', '250 cities', 'Neighborhoods statewide', 'Community conversations'],
        'status': 'planned',
    },
    {
        'goal': 5, 'id': 'build_partnerships', 'title': 'Build Partnerships',
        'description': 'Coalition broadens statewide educational reach',
        'initiatives': [
            'Libraries', 'Colleges', 'Universities', 'Historical societies',
            'Community organizations', 'Nonprofits', 'Civic organizations', 'Educational partners',
        ],
        'status': 'planned',
    },
    {
        'goal': 6, 'id': 'build_trust', 'title': 'Build Trust',
        'description': 'Trust remains the institution most valuable asset',
        'initiatives': [
            'Transparent research', 'Evidence verification', 'Editorial standards',
            'Public accountability', 'Accessibility', 'Volunteer stewardship',
        ],
        'status': 'specified',
    },
    {
        'goal': 7, 'id': 'build_legacy', 'title': 'Build Legacy',
        'description': 'Institution continues serving Arkansas for generations',
        'initiatives': [
            'Leadership succession', 'Documentation', 'Institutional memory',
            'Financial stewardship', 'Volunteer development', 'Technology modernization',
        ],
        'status': 'specified',
    },
]

STRATEGIC_METRICS = [
    {'id': 'SP-M01', 'metric': '75 County Goal', 'current': counties_active, 'target': counties_target, 'status': 'planned'},
    {'id': 'SP-M02', 'metric': '250 City Goal', 'current': cities_active, 'target': cities_target, 'status': 'planned'},
    {'id': 'SP-M03', 'metric': '200,000 Participant Goal', 'current': participants_connected, 'target': participants_target, 'status': 'planned'},
    {'id': 'SP-M04', 'metric': 'Academy Graduates', 'current': academy_graduates, 'status': 'planned'},
    {'id': 'SP-M05', 'metric': 'Education Leaders', 'current': education_leaders, 'status': 'planned'},
    {'id': 'SP-M06', 'metric': 'Coalition Organizations', 'current': coalition_organizations, 'status': 'planned'},
    {'id': 'SP-M07', 'metric': 'Research Library Growth', 'current': research_library_items, 'status': 'planned'},
    {'id': 'SP-M08', 'metric': 'Educational Asset Growth', 'current': educational_assets, 'status': 'planned'},
    {'id': 'SP-M09', 'metric': 'Institutional Health', 'current': institutional_health_score, 'status': 'planned'},
    {'id': 'SP-M10', 'metric': 'Trust Score', 'current': trust_score, 'status': 'planned'},
]

FIVE_YEAR_MILESTONES = [
    {'id': 'SP-5Y01', 'milestone': 'Operational Mission Control', 'achieved': False, 'status': 'partial'},
    {'id': 'SP-5Y02', 'milestone': 'Comprehensive curriculum', 'achieved': False, 'status': 'planned'},
    {'id': 'SP-5Y03', 'milestone': 'County leadership in every region', 'achieved': False, 'status': 'planned'},
    {'id': 'SP-5Y04', 'milestone': 'Growing coalition', 'achieved': False, 'status': 'planned'},
    {'id': 'SP-5Y05', 'milestone': 'Research Institute established', 'achieved': False, 'status': 'partial'},
    {'id': 'SP-5Y06', 'milestone': 'Community conversations occurring statewide', 'achieved': False, 'status': 'planned'},
]

TEN_YEAR_MILESTONES = [
    {'id': 'SP-10Y01', 'milestone': 'Education Leaders in all counties', 'achieved': False, 'status': 'planned'},
    {'id': 'SP-10Y02', 'milestone': 'Leadership teams in major cities', 'achieved': False, 'status': 'planned'},
    {'id': 'SP-10Y03', 'milestone': 'Mature Academy', 'achieved': False, 'status': 'planned'},
    {'id': 'SP-10Y04', 'milestone': 'Comprehensive Research Library', 'achieved': False, 'status': 'planned'},
    {'id': 'SP-10Y05', 'milestone': 'Strong institutional reputation', 'achieved': False, 'status': 'planned'},
    {'id': 'SP-10Y06', 'milestone': 'Growing neighborhood network', 'achieved': False, 'status': 'planned'},
    {'id': 'SP-10Y07', 'milestone': 'Broad coalition participation', 'achieved': False, 'status': 'planned'},
]

STRATEGIC_RISKS = [
    'Volunteer burnout', 'Leadership succession', 'Research backlog',
    'Technology modernization', 'Knowledge preservation', 'Coalition engagement',
    'Institutional sustainability',
]

STRATEGIC_OPPORTUNITIES = [
    'New educational partnerships', 'Emerging research', 'Technology improvements',
    'Community expansion', 'Academy innovation', 'Volunteer leadership growth',
]

ANNUAL_REVIEW_ITEMS = [
    'Mission alignment', 'Strategic goals', 'Progress indicators',
    'Emerging opportunities', 'Institutional risks', 'Priority initiatives',
]

FOUNDERS_COMMITMENT = (
    'Informed citizens are essential to self-government. Every strategic objective strengthens '
    'one idea: an Arkansas where more people understand how their constitutional system works, '
    'know how to evaluate evidence, engage respectfully, and feel equipped to participate '
    'thoughtfully in civic life.'
)

SYSTEM_ALIGNMENTS = [
    {'system': 'Mission Control', 'route': '/mission-control/', 'build': 1, 'status': 'live'},
    {'system': 'Research Institute (#73)', 'route': '/mission-control/arkansas-research-institute.html', 'build': 73, 'status': 'live', 'goals': [2, 6]},
    {'system': 'Community Education Academy (#68)', 'route': '/mission-control/citizen-leadership-academy.html', 'build': 68, 'status': 'live', 'goals': [1, 3]},
    {'system': 'Coalition Network (#61)', 'route': '/mission-control/coalition-network.html', 'build': 61, 'status': 'live', 'goals': [4, 5]},
    {'system': 'Arkansas Civic Atlas (#58)', 'route': '/mission-control/civic-atlas.html', 'build': 58, 'status': 'live', 'goals': [1, 4]},
    {'system': 'Relationship OS (#59)', 'route': '/mission-control/relationship-os.html', 'build': 59, 'status': 'live', 'goals': [3, 4]},
    {'system': 'Volunteer Network (#75)', 'route': '/mission-control/volunteer-funding-constitution.html', 'build': 75, 'status': 'live', 'goals': [1, 7]},
    {'system': 'Campaign Finance Observatory (#63)', 'route': '/mission-control/campaign-finance-observatory.html', 'build': 63, 'status': 'live', 'goals': [1, 2]},
    {'system': 'Public Trust (#82)', 'route': '/mission-control/public-trust-institutional-credibility.html', 'build': 82, 'status': 'live', 'goals': [6]},
    {'system': 'Civic Ecosystem (#83)', 'route': '/mission-control/arkansas-civic-ecosystem.html', 'build': 83, 'status': 'live', 'goals': [1, 4, 6]},
]

strategic_readiness = min(
    56,
    18
    + len(STRATEGIC_GOALS) * 2
    + len(STRATEGIC_METRICS) // 2
    + len(FIVE_YEAR_MILESTONES) // 2
    + len(TEN_YEAR_MILESTONES) // 2
    + len(STRATEGIC_RISKS) // 2
    + len(STRATEGIC_OPPORTUNITIES) // 2
    + len(ANNUAL_REVIEW_ITEMS) // 2
    + 3,
)

out = {
    'version': '1.0',
    'build': 84,
    'updated': today,
    'horizon_year': 2035,
    'title': 'Master Arkansas Strategic Plan 2035 v1.0',
    'subtitle': 'The Roadmap to a Statewide Civic Education Institution',
    'tagline': 'Vision • Strategy • Execution',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/arkansas-strategic-plan-2035.html',
    'constitution': '/docs/MASTER_ARKANSAS_STRATEGIC_PLAN_2035.md',
    'purpose': (
        'Long-range strategic plan for what the institution will accomplish over the next decade. '
        'Unlike the Master Build Plan (construction), this focuses on accomplishment through 2035.'
    ),
    'governing_principle': (
        'Strategic planning is not about predicting the future. It is about preparing the '
        'institution to serve Arkansas regardless of what the future brings. Every year: more '
        'knowledgeable, trusted, connected, resilient, useful, capable, worthy of confidence.'
    ),
    'distinct_from_build_plan': {
        'master_build_plan': '/BUILD_PLAN.md',
        'build_plan_focus': 'Constructing the institution (83 builds)',
        'strategic_plan_focus': 'What the institution accomplishes by 2035',
    },
    'strategic_vision': {
        'title': 'Strategic Vision',
        'horizon': 2035,
        'aspiration': "Arkansas's most trusted institution for civic understanding",
        'topics': STRATEGIC_VISION_TOPICS,
        'accessible_to_every_arkansan': True,
    },
    'strategic_mission': {
        'title': 'Strategic Mission',
        'pillars': STRATEGIC_MISSION_PILLARS,
        'enduring_statewide_network': True,
    },
    'strategic_goals': {
        'title': 'Strategic Goals',
        'goals_total': len(STRATEGIC_GOALS),
        'goals': STRATEGIC_GOALS,
    },
    'strategic_metrics': {
        'title': 'Strategic Metrics',
        'scorecard': STRATEGIC_METRICS,
        'live': strategic_scorecard_live,
        'institutional_scorecard': True,
        'status': 'planned',
    },
    'five_year_milestones': {
        'title': 'Five-Year Milestones',
        'milestones': FIVE_YEAR_MILESTONES,
        'achieved_count': five_year_milestones_achieved,
        'mc_updates_annually': True,
        'status': 'specified',
    },
    'ten_year_milestones': {
        'title': 'Ten-Year Milestones',
        'milestones': TEN_YEAR_MILESTONES,
        'achieved_count': ten_year_milestones_achieved,
        'horizon': 2035,
        'status': 'specified',
    },
    'strategic_risks': {
        'title': 'Strategic Risks',
        'risks': STRATEGIC_RISKS,
        'mc_monitors_continually': True,
        'early_awareness_proactive_planning': True,
        'status': 'specified',
    },
    'strategic_opportunities': {
        'title': 'Strategic Opportunities',
        'opportunities': STRATEGIC_OPPORTUNITIES,
        'mc_identifies': True,
        'institutional_learning_never_stops': True,
        'status': 'specified',
    },
    'annual_strategic_review': {
        'title': 'Annual Strategic Review',
        'review_items': ANNUAL_REVIEW_ITEMS,
        'conducted': annual_strategic_review_conducted,
        'living_document': True,
        'status': 'specified',
    },
    'founders_commitment': {
        'title': "Founder's Commitment",
        'text': FOUNDERS_COMMITMENT,
        'informed_citizens_essential': True,
    },
    'integration': {
        'every_system_advances_goal': True,
        'systems': SYSTEM_ALIGNMENTS,
        'aligns_with': ['Civic Ecosystem (#83)', 'Legacy Roadmap (#80)', 'Command Strategy (#70)', 'BUILD_PLAN.md'],
    },
    'long_term_vision': (
        'By 2035: recognized not simply for explaining a Supreme Court decision but for '
        'strengthening Arkansas civic capacity. Communities find reliable information. Education '
        'Leaders mentor generations. Libraries recommend the institution. Students learn from it. '
        'Researchers contribute. Citizens trust it. Legacy measured by civic understanding cultivated.'
    ),
    'summary': {
        'strategic_goals_total': len(STRATEGIC_GOALS),
        'strategic_metrics_total': len(STRATEGIC_METRICS),
        'five_year_milestones_achieved': five_year_milestones_achieved,
        'five_year_milestones_total': len(FIVE_YEAR_MILESTONES),
        'ten_year_milestones_achieved': ten_year_milestones_achieved,
        'ten_year_milestones_total': len(TEN_YEAR_MILESTONES),
        'strategic_scorecard_live': strategic_scorecard_live,
        'annual_strategic_review_conducted': annual_strategic_review_conducted,
        'counties_active': counties_active,
        'cities_active': cities_active,
        'participants_connected': participants_connected,
        'participants_target': participants_target,
        'education_leaders': education_leaders,
        'academy_graduates': academy_graduates,
        'coalition_organizations': coalition_organizations,
        'trust_score': trust_score,
        'arkansas_strategic_plan_2035_readiness_pct': strategic_readiness,
        'civic_ecosystem_readiness_pct': eco.get('summary', {}).get('arkansas_civic_ecosystem_readiness_pct', 54),
        'public_launch_readiness_pct': ex.get('public_launch_readiness', 8),
    },
    'catalog_gaps': [
        'Strategic scorecard not live — 10 metrics not tracked in MC',
        'Annual strategic review not conducted — living document not operational',
        '0/75 counties active — county goal not progressing',
        '0/250 cities active — city goal not progressing',
        '0/200,000 participants — participant goal not progressing',
        '0 academy graduates · 0 education leaders · 0 coalition organizations',
        '0% trust score computed at strategic level',
        'Five-year milestones: 0/6 achieved (2 partial in blueprint only)',
        'Ten-year milestones: 0/7 achieved',
        'Strategic risks monitored in spec only — no risk dashboard',
        'Opportunity identification not automated',
        'Build #84 vs BUILD_PLAN.md — accomplishment vs construction distinction',
        'Milestone annual update workflow not in MC',
    ],
    'recommended_next_build': {
        'number': 85,
        'title': 'Strategic Scorecard & Annual Review Components',
        'note': (
            'Strategic scorecard UI, milestone tracking, annual review workflow, '
            'risk/opportunity dashboard, COMP-* specs, GitHub backlog.'
        ),
    },
}

with open(root / 'data/arkansas-strategic-plan-2035.json', 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')

print(
    f'Arkansas Strategic Plan 2035: {len(STRATEGIC_GOALS)} goals, '
    f'{five_year_milestones_achieved}/{len(FIVE_YEAR_MILESTONES)} 5yr milestones, '
    f'{strategic_readiness}% readiness'
)
