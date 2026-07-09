"""
Generate data/arkansas-civic-ecosystem.json — Build #83.
Master Arkansas Civic Ecosystem v1.0.
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
legacy_eco = load_json(root / 'data/civic-ecosystem.json')
pt = load_json(root / 'data/public-trust-institutional-credibility.json')

ex = mc.get('executive', {})

# Honest zeros
ecosystem_health_score_live = False
executive_ecosystem_dashboard_live = False
health_score_computed = False
imbalances_detected = 0
living_systems_instrumented = 0
participants_connected = 0
participants_target = 200_000
arkansas_coverage_pct = 0

LIVING_SYSTEMS = [
    {
        'system': 1, 'id': 'research', 'title': 'Research',
        'role': 'Produces knowledge',
        'feeds': ['Evidence', 'Curriculum', 'Media', 'Academy', 'Mission Control'],
        'route': '/mission-control/arkansas-research-institute.html',
        'build': 73,
        'status': 'live',
    },
    {
        'system': 2, 'id': 'evidence', 'title': 'Evidence',
        'role': 'Verifies knowledge',
        'feeds': ['Articles', 'Lessons', 'AI', 'Research', 'Communications', 'Trust Framework'],
        'route': '/mission-control/evidence-ledger.html',
        'build': 41,
        'status': 'live',
    },
    {
        'system': 3, 'id': 'education', 'title': 'Education',
        'role': 'Transforms knowledge into learning',
        'feeds': ['Academy', 'Community conversations', 'Presentations', 'Neighborhood learning'],
        'route': '/mission-control/citizen-leadership-academy.html',
        'build': 68,
        'status': 'live',
    },
    {
        'system': 4, 'id': 'leadership', 'title': 'Leadership',
        'role': 'Develops people',
        'feeds': ['Cities', 'Counties', 'Neighborhoods', 'Coalition', 'Mentorship'],
        'route': '/mission-control/arkansas-action-network.html',
        'build': 64,
        'status': 'live',
    },
    {
        'system': 5, 'id': 'community', 'title': 'Community',
        'role': 'Creates local relationships',
        'feeds': ['Learning', 'Feedback', 'Volunteer growth', 'Listening Network', 'Mission Control'],
        'route': '/mission-control/arkansas-community-listening.html',
        'build': 71,
        'status': 'live',
    },
    {
        'system': 6, 'id': 'coalition', 'title': 'Coalition',
        'role': 'Connects organizations',
        'feeds': ['Community reach', 'Educational events', 'Resources', 'Leadership recruitment'],
        'route': '/mission-control/coalition-network.html',
        'build': 61,
        'status': 'live',
    },
    {
        'system': 7, 'id': 'communications', 'title': 'Communications',
        'role': 'Shares knowledge',
        'feeds': ['Website', 'Email', 'Presentations', 'Social media', 'Videos', 'Media'],
        'route': '/mission-control/arkansas-communications.html',
        'build': 72,
        'status': 'live',
    },
    {
        'system': 8, 'id': 'technology', 'title': 'Technology',
        'role': 'Enables the institution',
        'feeds': ['Mission Control', 'Digital Twin', 'Knowledge Graph', 'Relationship OS', 'Every public experience'],
        'route': '/mission-control/technical-architecture.html',
        'build': 47,
        'status': 'live',
    },
    {
        'system': 9, 'id': 'mission_control', 'title': 'Mission Control',
        'role': 'Observes the institution',
        'feeds': ['Planning', 'Resource allocation', 'Leadership', 'Forecasting', 'Executive decisions'],
        'route': '/mission-control/',
        'build': 1,
        'status': 'live',
    },
    {
        'system': 10, 'id': 'civic_innovation', 'title': 'Civic Innovation',
        'role': 'Explores future possibilities',
        'feeds': ['Research', 'Educational resources', 'Policy comparisons', 'Citizen questions'],
        'route': '/mission-control/arkansas-civic-innovation-reform.html',
        'build': 74,
        'status': 'live',
    },
    {
        'system': 11, 'id': 'trust', 'title': 'Trust',
        'role': 'Strengthens every other system',
        'feeds': ['All systems'],
        'route': '/mission-control/public-trust-institutional-credibility.html',
        'build': 82,
        'status': 'live',
        'note': 'Environment in which institution operates',
    },
    {
        'system': 12, 'id': 'arkansas', 'title': 'Arkansas',
        'role': 'Everything ultimately serves Arkansas',
        'feeds': ['Statewide coverage', 'County OS', 'City OS', 'Neighborhood OS', 'Civic Atlas'],
        'route': '/mission-control/civic-atlas.html',
        'build': 58,
        'status': 'live',
        'note': 'State is the ecosystem, not one audience',
    },
]

ECOSYSTEM_LOOPS = [
    {
        'id': 'knowledge', 'title': 'Knowledge Loop',
        'steps': ['Research', 'Education', 'Community Conversations', 'New Questions', 'Research'],
        'outcome': 'Knowledge continuously improves',
    },
    {
        'id': 'leadership', 'title': 'Leadership Loop',
        'steps': ['Leadership', 'Community', 'Relationships', 'New Leaders', 'Leadership'],
        'outcome': 'People continuously develop people',
    },
    {
        'id': 'coalition', 'title': 'Coalition Loop',
        'steps': ['Coalition', 'Events', 'Participants', 'Education Leaders', 'Coalition'],
        'outcome': 'Organizations strengthen one another',
    },
    {
        'id': 'technology', 'title': 'Technology Loop',
        'steps': ['Technology', 'Mission Control', 'Insights', 'Better Decisions', 'Better Technology'],
        'outcome': 'The institution continuously learns',
    },
]

ARKANSAS_LEARNING_LOOP = [
    'Listen', 'Research', 'Verify', 'Teach', 'Discuss', 'Learn', 'Improve', 'Repeat',
]

HEALTH_DIMENSIONS = [
    {'id': 'EC-H01', 'dimension': 'Research', 'score': 0, 'status': 'planned'},
    {'id': 'EC-H02', 'dimension': 'Evidence', 'score': 0, 'status': 'planned'},
    {'id': 'EC-H03', 'dimension': 'Education', 'score': 0, 'status': 'planned'},
    {'id': 'EC-H04', 'dimension': 'Leadership', 'score': 0, 'status': 'planned'},
    {'id': 'EC-H05', 'dimension': 'Community', 'score': 0, 'status': 'planned'},
    {'id': 'EC-H06', 'dimension': 'Coalition', 'score': 0, 'status': 'planned'},
    {'id': 'EC-H07', 'dimension': 'Technology', 'score': 0, 'status': 'planned'},
    {'id': 'EC-H08', 'dimension': 'Trust', 'score': 0, 'status': 'planned'},
    {'id': 'EC-H09', 'dimension': 'Volunteer strength', 'score': 0, 'status': 'planned'},
    {'id': 'EC-H10', 'dimension': 'Institutional sustainability', 'score': 0, 'status': 'planned'},
]

EXECUTIVE_DASHBOARD_PANELS = [
    'Overall Ecosystem Health',
    'Knowledge Health',
    'Leadership Health',
    'Community Health',
    'Coalition Health',
    'Technology Health',
    'Trust Health',
    'Arkansas Coverage',
    '200,000 Participant Progress',
    'Institutional Sustainability',
]

ECOSYSTEM_BALANCE_EXAMPLES = [
    'Strong research but weak leadership',
    'Strong leadership but weak community activity',
    'Growing coalition with insufficient educational materials',
    'Technology advancing faster than volunteer capacity',
]

NETWORK_EFFECT_CHAIN = [
    'More conversations', 'More learners', 'More Academy enrollments',
    'More volunteers', 'More coalition partnerships', 'More community questions',
    'Better research', 'Better educational materials',
]

FOUNDERS_VISION = (
    'Demonstrate what a healthy civic institution looks like: transparent, evidence-based, '
    'volunteer-driven, community-centered, technologically sophisticated, locally rooted — '
    'built to outlast founders and strengthen the next generation.'
)

ecosystem_readiness = min(
    54,
    17
    + len(LIVING_SYSTEMS) * 2
    + len(ECOSYSTEM_LOOPS)
    + len(HEALTH_DIMENSIONS) // 2
    + len(ARKANSAS_LEARNING_LOOP) // 2
    + len(EXECUTIVE_DASHBOARD_PANELS) // 3,
)

out = {
    'version': '1.0',
    'build': 83,
    'updated': today,
    'title': 'Master Arkansas Civic Ecosystem v1.0',
    'subtitle': 'One Institution. One State. One Connected Civic Network.',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/arkansas-civic-ecosystem.html',
    'constitution': '/docs/MASTER_ARKANSAS_CIVIC_ECOSYSTEM.md',
    'purpose': (
        'Framework connecting people, organizations, knowledge, technology, communities, '
        'and leadership into one living civic education system. Every component strengthens every other.'
    ),
    'governing_principle': (
        'Healthy ecosystems are resilient because no single component carries the entire burden. '
        'Research strengthens education. Education develops leaders. Leaders strengthen communities. '
        'Communities strengthen coalition. Coalition expands opportunity. Mission Control strengthens '
        'stewardship. Trust strengthens everything.'
    ),
    'ecosystem_philosophy': {
        'title': 'Ecosystem Philosophy',
        'departments_to_ecosystems': True,
        'core_question': 'How does this strengthen the entire institution?',
        'every_project_increases_ecosystem_health': True,
    },
    'living_systems': {
        'title': 'The Twelve Living Systems',
        'systems_total': len(LIVING_SYSTEMS),
        'permanently_connected': True,
        'systems': LIVING_SYSTEMS,
        'nothing_in_isolation': True,
    },
    'ecosystem_loops': {
        'title': 'Ecosystem Loops',
        'loops': ECOSYSTEM_LOOPS,
        'institution_grows_through_cycles': True,
    },
    'arkansas_learning_loop': {
        'title': 'Arkansas Learning Loop',
        'steps': ARKANSAS_LEARNING_LOOP,
        'permanently_adaptive': True,
        'status': 'specified',
    },
    'ecosystem_health_score': {
        'title': 'Ecosystem Health Score',
        'dimensions': HEALTH_DIMENSIONS,
        'overall_score': 0,
        'live': ecosystem_health_score_live,
        'computed': health_score_computed,
        'optimize_entire_ecosystem': True,
        'status': 'planned',
    },
    'positive_network_effects': {
        'title': 'Positive Network Effects',
        'example': 'One new Education Leader',
        'chain': NETWORK_EFFECT_CHAIN,
        'growth_compounds': True,
        'status': 'specified',
    },
    'ecosystem_balance': {
        'title': 'Ecosystem Balance',
        'imbalances_detected': imbalances_detected,
        'examples': ECOSYSTEM_BALANCE_EXAMPLES,
        'balanced_institutions_endure': True,
        'status': 'planned',
    },
    'executive_ecosystem_dashboard': {
        'title': 'Executive Ecosystem Dashboard',
        'panels': EXECUTIVE_DASHBOARD_PANELS,
        'live': executive_ecosystem_dashboard_live,
        'one_screen_summarizes_institution': True,
        'status': 'planned',
    },
    'founders_vision': {
        'title': "Founder's Vision",
        'text': FOUNDERS_VISION,
        'demonstrate_healthy_civic_institution': True,
        'not_simply_educate_about_citizens_united': True,
    },
    'integration': {
        'chain': (
            'Research → Evidence → Education → Leadership → Community → Coalition → '
            'Communications → Technology → Mission Control → Civic Innovation → Trust → Arkansas'
        ),
        'extends': 'Civic Ecosystem (#12) county layer',
        'unifies_builds': '#36–#82',
        'systems': [
            {'system': 'Civic Ecosystem (#12)', 'route': '/mission-control/civic-ecosystem.html', 'status': 'live', 'note': 'County layer'},
            {'system': 'Public Trust (#82)', 'route': '/mission-control/public-trust-institutional-credibility.html', 'status': 'live'},
            {'system': 'Digital Twin (#81)', 'route': '/mission-control/institutional-digital-twin.html', 'status': 'live'},
            {'system': 'Legacy Roadmap (#80)', 'route': '/mission-control/arkansas-civic-institution-roadmap.html', 'status': 'live'},
            {'system': 'ANOS (#79)', 'route': '/mission-control/arkansas-neighborhood-operating-system.html', 'status': 'live'},
            {'system': 'ArCOS (#78)', 'route': '/mission-control/arkansas-city-operating-system.html', 'status': 'live'},
            {'system': 'ACOS (#77)', 'route': '/mission-control/arkansas-county-operating-system.html', 'status': 'live'},
            {'system': 'Organizational Constitution (#76)', 'route': '/mission-control/organizational-constitution.html', 'status': 'live'},
            {'system': 'Systems Integration (#45)', 'route': '/mission-control/systems-integration.html', 'status': 'live'},
            {'system': 'Civic Atlas (#58)', 'route': '/mission-control/civic-atlas.html', 'status': 'live'},
        ],
    },
    'long_term_vision': (
        'Twenty-five years: no longer viewed as a website but as a civic ecosystem. Researchers improve '
        'curriculum. Curriculum develops leaders. Leaders strengthen communities. Communities generate questions. '
        'Questions improve research. Technology connects everything. Mission Control stewards the system. '
        'Every healthy part strengthens every other healthy part.'
    ),
    'summary': {
        'living_systems_total': len(LIVING_SYSTEMS),
        'living_systems_instrumented': living_systems_instrumented,
        'ecosystem_loops': len(ECOSYSTEM_LOOPS),
        'ecosystem_health_score_live': ecosystem_health_score_live,
        'executive_ecosystem_dashboard_live': executive_ecosystem_dashboard_live,
        'health_score_computed': health_score_computed,
        'overall_ecosystem_health': 0,
        'imbalances_detected': imbalances_detected,
        'participants_connected': participants_connected,
        'participants_target': participants_target,
        'arkansas_coverage_pct': arkansas_coverage_pct,
        'arkansas_civic_ecosystem_readiness_pct': ecosystem_readiness,
        'public_trust_readiness_pct': pt.get('summary', {}).get('public_trust_institutional_credibility_readiness_pct', 50),
        'legacy_civic_ecosystem_build': legacy_eco.get('build', 12),
        'public_launch_readiness_pct': ex.get('public_launch_readiness', 8),
    },
    'catalog_gaps': [
        'Ecosystem Health Score not computed — no health engine',
        'Executive Ecosystem Dashboard not live — one-screen view missing',
        '0/12 living systems instrumented — feeds not tracked in MC',
        '0 imbalances detected — balance monitoring not built',
        '0/200,000 participants connected — network effects not measured',
        '0% Arkansas coverage tracked at ecosystem level',
        'Positive network effects specified — not modeled',
        'Arkansas Learning Loop specified — not operationalized in workflow',
        'Build #83 vs Civic Ecosystem (#12) — master vs county layer distinction',
        'Ecosystem loops not visualized in MC',
        'Cross-system feed mapping not in Knowledge Graph',
        'Volunteer strength & sustainability dimensions at 0',
    ],
    'recommended_next_build': {
        'number': 84,
        'title': 'Ecosystem Health Dashboard & Network Effect Components',
        'note': (
            'Health score engine, imbalance detection, executive ecosystem dashboard UI, '
            'network effect modeling, living system instrumentation, COMP-* specs.'
        ),
    },
}

with open(root / 'data/arkansas-civic-ecosystem.json', 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')

print(
    f'Arkansas Civic Ecosystem: {len(LIVING_SYSTEMS)} systems, '
    f'{imbalances_detected} imbalances, {ecosystem_readiness}% readiness'
)
