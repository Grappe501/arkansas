"""
Generate data/arkansas-civic-institution-roadmap.json — Build #80.
Master Arkansas Civic Institution Roadmap v1.0 — Twenty-Year Vision & Legacy Plan.
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
ir = load_json(root / 'data/institutional-roadmap.json')
anos = load_json(root / 'data/arkansas-neighborhood-operating-system.json')
oc = load_json(root / 'data/organizational-constitution.json')

ex = mc.get('executive', {})

# Honest zeros
current_era = 1
milestones_achieved = 0  # updated after INSTITUTIONAL_MILESTONES defined
legacy_map_live = False
annual_reflection_conducted = False
legacy_projects_started = 0
counties_with_leaders = 0
cities_with_teams = 0
connected_arkansans = anos.get('summary', {}).get('connected_arkansans', 0)
education_leaders = 0
neighborhood_conversations = 0
builds_complete = 80

FOUNDING_VISION = (
    'Help Arkansans understand Citizens United v. FEC and strengthen constitutional '
    'literacy, civic participation, and public trust. Website is the beginning; '
    'institution is the destination.'
)

TWENTY_YEAR_GOALS = [
    {'id': 'LEG-G01', 'goal': 'Education Leaders in all 75 counties', 'current': counties_with_leaders, 'target': 75, 'status': 'scaffolded'},
    {'id': 'LEG-G02', 'goal': 'Leadership teams in 250 largest cities', 'current': cities_with_teams, 'target': 250, 'status': 'scaffolded'},
    {'id': 'LEG-G03', 'goal': '200,000 connected Arkansans', 'current': connected_arkansans, 'target': 200_000, 'status': 'scaffolded'},
    {'id': 'LEG-G04', 'goal': 'Thousands of neighborhood learning conversations', 'current': neighborhood_conversations, 'target': None, 'status': 'planned'},
    {'id': 'LEG-G05', 'goal': 'Mature Community Education Academy', 'current': 0, 'target': None, 'status': 'partial'},
    {'id': 'LEG-G06', 'goal': 'Thriving coalition of Arkansas organizations', 'current': 0, 'target': None, 'status': 'partial'},
    {'id': 'LEG-G07', 'goal': 'Comprehensive research library on Citizens United and campaign finance', 'current': 0, 'target': None, 'status': 'partial'},
    {'id': 'LEG-G08', 'goal': "Recognition as Arkansas's most trusted educational resource", 'current': 0, 'target': None, 'status': 'aspirational'},
]

FOUR_ERAS = [
    {
        'era': 1, 'id': 'foundation', 'title': 'Foundation', 'focus': 'Build the institution',
        'objectives': [
            'Launch the platform', 'Complete Mission Control', 'Develop curriculum',
            'Recruit founding volunteers', 'Establish first county teams',
        ],
        'status': 'active',
    },
    {
        'era': 2, 'id': 'expansion', 'title': 'Expansion', 'focus': 'Reach Arkansas',
        'objectives': [
            'County coverage', 'City leadership', 'Coalition growth',
            'Community conversations', 'Academy expansion', 'Relationship network growth',
        ],
        'status': 'planned',
    },
    {
        'era': 3, 'id': 'maturity', 'title': 'Maturity', 'focus': 'Strengthen quality',
        'objectives': [
            'Research excellence', 'Advanced curriculum', 'Leadership succession',
            'Institutional sustainability', 'Comprehensive educational resources',
        ],
        'status': 'planned',
    },
    {
        'era': 4, 'id': 'legacy', 'title': 'Legacy', 'focus': 'Preserve the institution',
        'objectives': [
            'Institutional continuity', 'Knowledge preservation', 'Generational leadership',
            'Historical archives', 'Ongoing civic education',
        ],
        'status': 'planned',
    },
]

INSTITUTIONAL_MILESTONES = [
    {'id': 'LEG-M01', 'milestone': 'First county represented', 'achieved': False, 'status': 'pending'},
    {'id': 'LEG-M02', 'milestone': 'All 75 counties represented', 'achieved': False, 'status': 'pending'},
    {'id': 'LEG-M03', 'milestone': '100 Education Leaders', 'achieved': False, 'status': 'pending'},
    {'id': 'LEG-M04', 'milestone': '500 Education Leaders', 'achieved': False, 'status': 'pending'},
    {'id': 'LEG-M05', 'milestone': '250 city teams established', 'achieved': False, 'status': 'pending'},
    {'id': 'LEG-M06', 'milestone': '100,000 connected Arkansans', 'achieved': False, 'status': 'pending'},
    {'id': 'LEG-M07', 'milestone': '200,000 connected Arkansans', 'achieved': False, 'status': 'pending'},
    {'id': 'LEG-M08', 'milestone': 'Major research milestones', 'achieved': False, 'status': 'pending'},
    {'id': 'LEG-M09', 'milestone': 'Coalition anniversaries', 'achieved': False, 'status': 'pending'},
    {'id': 'LEG-M10', 'milestone': '80 builds complete', 'achieved': True, 'status': 'complete'},
]

milestones_achieved = sum(1 for m in INSTITUTIONAL_MILESTONES if m['achieved'])

LEGACY_PROJECTS = [
    'Comprehensive historical archives', 'Documentary collections',
    'Oral history interviews', 'Interactive constitutional exhibits',
    'Educational traveling displays', 'Arkansas civic education conferences',
    'Annual State of Civic Education reports',
]

LEADERSHIP_LEGACY = [
    'Mentorship', 'Documentation', 'Leadership development',
    'Succession planning', 'Institutional stewardship',
]

RESEARCH_LEGACY = [
    'New court decisions', 'Campaign finance developments',
    'Arkansas historical materials', 'Comparative state studies', 'Updated policy research',
]

COMMUNITY_LEGACY_PARTNERS = [
    'Libraries', 'Schools', 'Colleges', 'Community organizations',
    'Historical societies', 'Service clubs', 'Neighborhood groups', 'Education Leaders',
]

TECHNOLOGY_LEGACY_REVIEWS = [
    'Infrastructure', 'Security', 'Accessibility', 'Preservation', 'Modernization',
]

ANNUAL_REFLECTION_QUESTIONS = [
    'Are we serving Arkansas better than last year?',
    'Are our resources more accurate?',
    'Are our leaders better prepared?',
    'Are our communities more connected?',
    'Are we earning greater public trust?',
]

LEGACY_MAP_SECTIONS = [
    'County development', 'City development', 'Neighborhood growth',
    'Leadership succession', 'Coalition expansion', 'Research milestones',
    'Institutional history',
]

NOT_JUDGED_BY = [
    'Website traffic', 'Press attention', 'Awards', 'Technology',
]

SUCCESS_MEASURES = [
    'Did more Arkansans understand the Constitution?',
    'Did communities become stronger?',
    'Did respectful civic dialogue become more common?',
    'Did ordinary citizens become trusted educators?',
    'Did future generations inherit better civic resources?',
]

SYSTEM_CONNECTIONS = [
    {'system': 'Organizational Constitution (#76)', 'route': '/mission-control/organizational-constitution.html', 'status': 'live'},
    {'system': 'Institutional Roadmap V1–V10 (#44)', 'route': '/mission-control/institutional-roadmap.html', 'status': 'live', 'note': 'Version evolution plan'},
    {'system': 'Master Plan (#55)', 'route': '/mission-control/master-plan.html', 'status': 'live'},
    {'system': 'ACOS (#77)', 'route': '/mission-control/arkansas-county-operating-system.html', 'status': 'live'},
    {'system': 'ArCOS (#78)', 'route': '/mission-control/arkansas-city-operating-system.html', 'status': 'live'},
    {'system': 'ANOS (#79)', 'route': '/mission-control/arkansas-neighborhood-operating-system.html', 'status': 'live'},
    {'system': 'Research Institute (#73)', 'route': '/mission-control/arkansas-research-institute.html', 'status': 'live'},
    {'system': 'Citizen Leadership Academy (#68)', 'route': '/mission-control/citizen-leadership-academy.html', 'status': 'live'},
    {'system': 'Coalition Network (#61)', 'route': '/mission-control/coalition-network.html', 'status': 'live'},
    {'system': 'Mission Control', 'route': '/mission-control/', 'status': 'live'},
]

legacy_readiness = min(
    50,
    18
    + len(FOUR_ERAS) * 2
    + len(TWENTY_YEAR_GOALS) // 2
    + len(INSTITUTIONAL_MILESTONES) // 2
    + len(LEGACY_PROJECTS) // 2
    + len(LEGACY_MAP_SECTIONS)
    + 3,
)

out = {
    'version': '1.0',
    'build': 80,
    'updated': today,
    'title': 'Master Arkansas Civic Institution Roadmap v1.0',
    'subtitle': 'The Twenty-Year Vision & Institutional Legacy Plan',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/arkansas-civic-institution-roadmap.html',
    'constitution': '/docs/MASTER_ARKANSAS_CIVIC_INSTITUTION_ROADMAP.md',
    'purpose': (
        'Answer: if everything succeeds, what does Citizens United Facts look like '
        'twenty years from now? Plans for legacy, not merely launch.'
    ),
    'governing_principle': (
        'Institutions are remembered not because they were launched. '
        'They are remembered because they endured. Purpose larger than any one person.'
    ),
    'plans_for_legacy_not_launch': True,
    'eighty_builds_blueprint_complete': True,
    'founding_vision': FOUNDING_VISION,
    'website_beginning_institution_destination': True,
    'twenty_year_goals': {
        'title': 'Twenty-Year Goals',
        'direction_not_rigid_deadlines': True,
        'goals': TWENTY_YEAR_GOALS,
        'goals_total': len(TWENTY_YEAR_GOALS),
    },
    'four_eras': {
        'title': 'Four Eras of Growth',
        'current_era': current_era,
        'eras': FOUR_ERAS,
    },
    'institutional_milestones': {
        'title': 'Institutional Milestones',
        'milestones': INSTITUTIONAL_MILESTONES,
        'achieved_count': milestones_achieved,
        'mc_celebrates': True,
        'status': 'specified',
    },
    'legacy_projects': {
        'title': 'Legacy Projects',
        'projects': LEGACY_PROJECTS,
        'projects_started': legacy_projects_started,
        'preserve_knowledge_for_future_generations': True,
        'status': 'specified',
    },
    'leadership_legacy': {
        'title': 'Leadership Legacy',
        'every_generation_prepares_next': True,
        'practices': LEADERSHIP_LEGACY,
        'never_depend_on_one_individual': True,
    },
    'research_legacy': {
        'title': 'Research Legacy',
        'continually_expand': True,
        'future_collections': RESEARCH_LEGACY,
        'future_scholars_build_upon_work': True,
    },
    'community_legacy': {
        'title': 'Community Legacy',
        'woven_into_arkansas_civic_life': True,
        'partners': COMMUNITY_LEGACY_PARTNERS,
        'stronger_statewide_culture': True,
    },
    'technology_legacy': {
        'title': 'Technology Legacy',
        'remain_adaptable': True,
        'mc_regularly_reviews': TECHNOLOGY_LEGACY_REVIEWS,
        'educational_mission_constant': True,
    },
    'annual_institutional_reflection': {
        'title': 'Annual Institutional Reflection',
        'questions': ANNUAL_REFLECTION_QUESTIONS,
        'conducted': annual_reflection_conducted,
        'guides_next_year_priorities': True,
        'status': 'specified',
    },
    'arkansas_civic_legacy_map': {
        'title': 'Arkansas Civic Legacy Map',
        'permanent_visual_record': True,
        'sections': LEGACY_MAP_SECTIONS,
        'live': legacy_map_live,
        'institution_story_part_of_arkansas_history': True,
        'status': 'planned',
    },
    'measure_of_success': {
        'title': 'Measure of Success',
        'not_judged_by': NOT_JUDGED_BY,
        'true_measures': SUCCESS_MEASURES,
        'legacy_not_metrics': True,
    },
    'founders_reflection': (
        'Ultimate hope: someday people no longer remember who built it. They simply know '
        'that whenever an Arkansan wanted to understand Citizens United, campaign finance, '
        'constitutional government, or civic participation, there was one place they could trust — '
        'built patiently, grounded in evidence, strengthened by volunteers, sustained by communities, '
        'never stopped learning.'
    ),
    'integration': {
        'chain': (
            'Constitution (#76) → Institutional Roadmap (#44) → Master Plan (#55) → '
            'ACOS → ArCOS → ANOS → Research → Academy → Coalition → Mission Control'
        ),
        'mc_compares_current_to_vision': True,
        'systems': SYSTEM_CONNECTIONS,
        'extends': 'Institutional Roadmap V1–V10 (#44)',
        'complements': 'Master Plan (#55)',
    },
    'long_term_vision': (
        'Year twenty: trusted statewide civic education institution; 75 counties, 250 cities, '
        '200K connected; thousands of neighborhood conversations; mature academy and coalition; '
        'comprehensive research library; stronger civic foundation than inherited.'
    ),
    'summary': {
        'builds_complete': builds_complete,
        'current_era': current_era,
        'current_era_title': 'Foundation',
        'twenty_year_goals': len(TWENTY_YEAR_GOALS),
        'milestones_achieved': milestones_achieved,
        'milestones_total': len(INSTITUTIONAL_MILESTONES),
        'legacy_map_live': legacy_map_live,
        'annual_reflection_conducted': annual_reflection_conducted,
        'legacy_projects_started': legacy_projects_started,
        'counties_with_leaders': counties_with_leaders,
        'cities_with_teams': cities_with_teams,
        'connected_arkansans': connected_arkansans,
        'participants_target': 200_000,
        'arkansas_civic_institution_roadmap_readiness_pct': legacy_readiness,
        'institutional_roadmap_readiness_pct': ir.get('summary', {}).get('institutional_roadmap_readiness_pct', 48),
        'organizational_constitution_readiness_pct': oc.get('summary', {}).get('organizational_constitution_readiness_pct', 46),
        'public_launch_readiness_pct': ex.get('public_launch_readiness', 8),
    },
    'catalog_gaps': [
        'Legacy map not live — permanent visual record not built',
        '0/9 milestones achieved (except 80 builds complete)',
        'Annual reflection workflow not operational',
        '0 legacy projects started',
        'Era tracking — MC does not compare current state to 20-year vision',
        'Build #80 vs Institutional Roadmap (#44) — reconcile V1–V10 vs four eras?',
        'Milestone celebration system not implemented',
        '20-year goal progress not tracked in MC executive dashboard',
        'Founder reflection not on public front door',
        'Technology legacy review schedule not automated',
        'Research legacy collections — 0 items beyond scaffold',
        'Community legacy partner registry empty',
        'Implementation translation layer still pending after 80 spec builds',
    ],
    'recommended_next_build': {
        'number': 81,
        'title': 'Implementation Translation Layer & Engineering Artifacts',
        'note': (
            'Legacy map, milestone tracker, era dashboard, annual reflection workflow, '
            '20-year goal progress UI, COMP-* specs, GitHub backlog — begin implementation.'
        ),
    },
}

with open(root / 'data/arkansas-civic-institution-roadmap.json', 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')

print(
    f'Civic Institution Roadmap: era {current_era}, '
    f'{milestones_achieved}/{len(INSTITUTIONAL_MILESTONES)} milestones, '
    f'{legacy_readiness}% readiness'
)
