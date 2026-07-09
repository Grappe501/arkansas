"""
Generate data/founding-charter.json — Build #100.
Master Founding Charter — The Arkansas Declaration for an Informed Citizenry v1.0.
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
ex = mc.get('executive', {})

# Honest operational metrics
charter_dashboard_live = False
required_reading_enforced = False
charter_acknowledgments = 0
public_charter_page_live = False
founding_blueprint_documented = True

PREAMBLE_BELIEFS = [
    'A free people cannot govern themselves if they cannot understand the systems that govern them',
    'Knowledge is the foundation of liberty',
    'Understanding is the foundation of participation',
    'Trust is the foundation of healthy institutions',
]

WHY_WE_EXIST_TOPICS = [
    'Complex court decisions',
    'Campaign finance laws',
    'Government processes',
    'Constitutional questions',
    'Legislative procedures',
    'Public transparency',
]

NOT_BUILDING = [
    'A political campaign',
    'A political party',
    'A lobbying organization',
    'A temporary project',
    'A collection of webpages',
]

BUILDING = [
    'An institution',
    'A public educational resource',
    'A statewide volunteer network',
    'A civic research center',
    'A leadership academy',
    'A coalition of Arkansas organizations',
    'A permanent civic education infrastructure',
]

WHO_WE_SERVE = [
    'Every Arkansas citizen',
    'Every student',
    'Every teacher',
    'Every librarian',
    'Every journalist',
    'Every volunteer',
    'Every community organization',
    'Every elected official seeking accurate information',
    'Every person who sincerely wants to understand',
]

COMMITMENTS = [
    'Research before assumption',
    'Evidence before opinion',
    'Transparency before convenience',
    'Listening before speaking',
    'Teaching before persuading',
    'Communities before institutions',
    'Volunteers before bureaucracy',
    'Service before recognition',
    'Arkansas before ourselves',
]

STANDARDS = [
    'Every page should answer questions honestly',
    'Every citation should be verifiable',
    'Every volunteer should feel valued',
    'Every community should feel welcomed',
    'Every correction should be made openly',
    'Every decision should strengthen trust',
]

STEWARDSHIP_GOALS = [
    'Better documented',
    'Better researched',
    'Better organized',
    'More accessible',
    'More trusted',
    'More useful',
]

JANUARY_2027_GOALS = [
    'A fully operational statewide civic education institution',
    'Mission Control functioning',
    'Education Leaders across Arkansas',
    'Leadership developing in all 75 counties',
    'Leadership growing in the 250 largest cities',
    'A thriving Community Education Academy',
    'A strong coalition of Arkansas organizations',
    'A trusted research library',
    'A volunteer-powered organization',
    'A foundation capable of serving Arkansas for decades',
]

NEXT_GENERATION_INHERITANCE = [
    'Clear documentation',
    'Reliable systems',
    'Thoughtful governance',
    'Strong leadership',
    'Trusted research',
    'Healthy communities',
    'An institution worthy of continuing',
]

NOT_MEASURED_BY = [
    'Money',
    'Popularity',
    'Recognition',
    'Awards',
    'Media attention',
]

MEASURED_BY = [
    'Did more Arkansans understand?',
    'Did communities become stronger?',
    'Did volunteers become leaders?',
    'Did neighbors learn together?',
    'Did trust increase?',
    'Did the institution remain faithful to its mission?',
]

ARKANSAS_PROMISE_SEQUENCE = [
    'Volunteer by volunteer',
    'County by county',
    'City by city',
    'Neighborhood by neighborhood',
    'Conversation by conversation',
    'Generation by generation',
]

FOUNDING_SYSTEMS_DESIGNED = [
    'Research', 'Technology', 'Mission Control', 'Education', 'Leadership',
    'Coalition', 'Volunteers', 'Counties', 'Cities', 'Neighborhoods',
    'Artificial Intelligence', 'Knowledge Systems', 'Governance', 'Operations',
]

COVENANT = [
    'We will seek truth with humility',
    'We will teach with integrity',
    'We will serve without expectation of recognition',
    'We will protect the public trust entrusted to us',
    'We will leave this institution stronger for those who follow',
    'We dedicate Citizens United Facts to the people of Arkansas',
]

GOVERNING_PRINCIPLE_LINES = [
    'Knowledge strengthens citizens',
    'Citizens strengthen communities',
    'Communities strengthen Arkansas',
    'Arkansas, strengthened by informed citizens, strengthens the American promise of self-government',
]

CHARTER_SECTIONS = [
    {
        'id': 'FC-01',
        'title': 'Preamble',
        'summary': 'Founding volunteers establish an enduring institution devoted to civic education',
        'beliefs': PREAMBLE_BELIEFS,
        'permanent_foundation': True,
    },
    {
        'id': 'FC-02',
        'title': 'Why We Exist',
        'summary': 'Important civic questions should never belong only to insiders',
        'topics': WHY_WE_EXIST_TOPICS,
        'belong_to_the_people': True,
    },
    {
        'id': 'FC-03',
        'title': 'What We Are Building',
        'summary': 'An institution — not a campaign, party, or temporary project',
        'not_building': NOT_BUILDING,
        'building': BUILDING,
    },
    {
        'id': 'FC-04',
        'title': 'Who We Serve',
        'summary': 'The institution belongs to all who come seeking knowledge',
        'audiences': WHO_WE_SERVE,
    },
    {
        'id': 'FC-05',
        'title': 'Our Commitments',
        'summary': 'These commitments define our culture',
        'commitments': COMMITMENTS,
    },
    {
        'id': 'FC-06',
        'title': 'Our Standard',
        'summary': 'These standards never expire',
        'standards': STANDARDS,
    },
    {
        'id': 'FC-07',
        'title': 'Our Responsibility',
        'summary': 'Every generation becomes a steward',
        'stewardship_goals': STEWARDSHIP_GOALS,
    },
    {
        'id': 'FC-08',
        'title': 'Our Goals',
        'summary': 'January 2027 — completion of founding build, not completion of mission',
        'january_2027_goals': JANUARY_2027_GOALS,
        'founding_build_complete_target': True,
    },
    {
        'id': 'FC-09',
        'title': 'The Next Generation',
        'summary': 'New volunteers should inherit an institution worthy of continuing',
        'inheritance': NEXT_GENERATION_INHERITANCE,
        'should_never_need_to_know_founders': True,
    },
    {
        'id': 'FC-10',
        'title': 'Our Measure of Success',
        'summary': 'Measured by understanding, trust, and faithfulness — not popularity',
        'not_measured_by': NOT_MEASURED_BY,
        'measured_by': MEASURED_BY,
    },
    {
        'id': 'FC-11',
        'title': 'The Arkansas Promise',
        'summary': 'Arkansas can become a national example of thoughtful civic education',
        'built_sequence': ARKANSAS_PROMISE_SEQUENCE,
        'arkansas_not_perfect_but_cares': True,
    },
    {
        'id': 'FC-12',
        'title': "Founder's Closing Reflection",
        'summary': 'One hundred builds — from idea to complete institutional blueprint',
        'systems_designed': FOUNDING_SYSTEMS_DESIGNED,
        'enduring_belief': 'An informed citizen is the strongest guardian of self-government',
        'builds_from_idea': 100,
    },
    {
        'id': 'FC-13',
        'title': 'Institutional Covenant',
        'summary': 'Dedicated to the people of Arkansas — with gratitude, responsibility, and hope',
        'covenant': COVENANT,
    },
    {
        'id': 'FC-14',
        'title': 'Final Governing Principle',
        'summary': 'This is the founding charter of Citizens United Facts',
        'principle_lines': GOVERNING_PRINCIPLE_LINES,
    },
]

CHARTER_DASHBOARD_INDICATORS = [
    {'id': 'FC-D01', 'indicator': 'Charter acknowledgments', 'current': charter_acknowledgments, 'status': 'planned'},
    {'id': 'FC-D02', 'indicator': 'Founding blueprint documented', 'current': 'Yes' if founding_blueprint_documented else 'No', 'status': 'partial'},
    {'id': 'FC-D03', 'indicator': 'Charter sections documented', 'current': len(CHARTER_SECTIONS), 'status': 'partial'},
    {'id': 'FC-D04', 'indicator': 'January 2027 goals specified', 'current': len(JANUARY_2027_GOALS), 'status': 'partial'},
    {'id': 'FC-D05', 'indicator': 'Public charter page', 'current': 'Partial', 'status': 'partial'},
    {'id': 'FC-D06', 'indicator': 'Charter dashboard', 'current': 'Planned', 'status': 'planned'},
]

founding_charter_readiness = min(
    72,
    18
    + len(CHARTER_SECTIONS) // 2
    + len(COMMITMENTS) // 2
    + len(STANDARDS) // 2
    + len(JANUARY_2027_GOALS) // 2
    + len(COVENANT) // 2
    + len(WHO_WE_SERVE) // 2
    + len(BUILDING) // 2
    + len(CHARTER_DASHBOARD_INDICATORS) // 2
    + 6  # preamble, governing principle, founders reflection, arkansas promise, 100-build milestone
    + (2 if charter_dashboard_live else 0),
)

out = {
    'version': '1.0',
    'build': 100,
    'updated': today,
    'completion_target_date': completion_target_date,
    'title': 'Master Founding Charter v1.0',
    'subtitle': 'The Arkansas Declaration for an Informed Citizenry',
    'tagline': 'The Completion of the Founding Blueprint',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/founding-charter.html',
    'constitution': '/docs/MASTER_FOUNDING_CHARTER.md',
    'purpose': (
        'Build #100 completes the founding blueprint. One hundred builds ago there was only an idea; '
        'today there is a complete institutional blueprint. This Charter becomes the permanent '
        'foundation upon which every future generation may continue building. The Arkansas Declaration '
        'for an Informed Citizenry.'
    ),
    'governing_principle': (
        'Knowledge strengthens citizens. Citizens strengthen communities. Communities strengthen Arkansas. '
        'And Arkansas, strengthened by informed citizens, strengthens the American promise of self-government. '
        'This is the founding charter of Citizens United Facts.'
    ),
    'founders_closing': (
        'One hundred builds ago there was only an idea. Today there is a complete institutional blueprint. '
        'If Citizens United Facts helps even one generation of Arkansans better understand their constitutional '
        'system, strengthens public trust through careful scholarship, and inspires neighbors to learn together '
        'with respect and curiosity, then this institution will have fulfilled its highest purpose.'
    ),
    'founding_milestone': {
        'title': 'Build #100 — Founding Blueprint Complete',
        'builds_from_idea': 100,
        'blueprint_complete': founding_blueprint_documented,
        'january_2027_founding_build_complete': True,
        'mission_continues_beyond_january_2027': True,
        'days_remaining': days_remaining,
    },
    'document_hierarchy': {
        'manifesto': 'Why the institution must exist (#99)',
        'charter': 'Permanent founding foundation (#100)',
        'constitution': 'Governance and operating rules',
        'technical_plans': 'How the institution is built',
        'if_all_else_lost_charter_and_manifesto_remain': True,
    },
    'charter_sections': {
        'title': 'The Founding Charter',
        'sections': CHARTER_SECTIONS,
        'sections_total': len(CHARTER_SECTIONS),
    },
    'our_commitments': {
        'title': 'Our Commitments',
        'items': COMMITMENTS,
        'define_culture': True,
    },
    'our_standard': {
        'title': 'Our Standard',
        'standards': STANDARDS,
        'never_expire': True,
    },
    'january_2027': {
        'title': 'January 2027',
        'founding_build_complete': True,
        'mission_continues': True,
        'goals': JANUARY_2027_GOALS,
        'days_remaining': days_remaining,
    },
    'institutional_covenant': {
        'title': 'Institutional Covenant',
        'items': COVENANT,
        'dedicated_to_people_of_arkansas': True,
    },
    'final_governing_principle': {
        'title': 'Final Governing Principle',
        'lines': GOVERNING_PRINCIPLE_LINES,
        'full': (
            'Knowledge strengthens citizens. Citizens strengthen communities. '
            'Communities strengthen Arkansas. And Arkansas, strengthened by informed citizens, '
            'strengthens the American promise of self-government.'
        ),
    },
    'required_reading': {
        'title': 'Founding Documents',
        'audiences': [
            'Every founding volunteer', 'Every volunteer', 'Every Education Leader',
            'Every coalition partner', 'Every future leader',
        ],
        'includes_manifesto_and_charter': True,
        'enforced': required_reading_enforced,
        'acknowledgments': charter_acknowledgments,
        'status': 'planned',
    },
    'charter_dashboard': {
        'title': 'Founding Charter Dashboard',
        'indicators': CHARTER_DASHBOARD_INDICATORS,
        'live': charter_dashboard_live,
        'status': 'planned',
    },
    'integration': {
        'chain': (
            'Founding Charter → Institutional Manifesto → Organizational Constitution → '
            'Project Constitution → Launch Certification → Continuous Improvement'
        ),
        'founding_blueprint_capstone': True,
        'systems': [
            {'system': 'Institutional Manifesto (#99)', 'route': '/mission-control/institutional-manifesto.html', 'status': 'live'},
            {'system': 'Organizational Constitution (#76)', 'route': '/mission-control/organizational-constitution.html', 'status': 'live'},
            {'system': 'Project Constitution (#2)', 'route': '/builds/002-project-constitution.html', 'status': 'live'},
            {'system': 'Launch Certification (#97)', 'route': '/mission-control/institutional-launch-certification.html', 'status': 'live'},
            {'system': 'Continuous Improvement (#98)', 'route': '/mission-control/institutional-continuous-improvement.html', 'status': 'live'},
            {'system': 'Operating Manual (#90)', 'route': '/mission-control/institutional-operating-manual.html', 'status': 'live'},
        ],
    },
    'long_term_vision': (
        'The founding charter remains when founders are forgotten and generations change. '
        'Every steward leaves the institution better documented, more trusted, and more useful. '
        'Arkansas strengthened by informed citizens strengthens the American promise of self-government.'
    ),
    'summary': {
        'completion_target_date': completion_target_date,
        'days_remaining': days_remaining,
        'founding_charter_readiness_pct': founding_charter_readiness,
        'charter_sections': len(CHARTER_SECTIONS),
        'commitments': len(COMMITMENTS),
        'standards': len(STANDARDS),
        'january_2027_goals': len(JANUARY_2027_GOALS),
        'covenant_items': len(COVENANT),
        'charter_dashboard_live': charter_dashboard_live,
        'required_reading_enforced': required_reading_enforced,
        'charter_acknowledgments': charter_acknowledgments,
        'public_charter_page_live': public_charter_page_live,
        'founding_blueprint_documented': founding_blueprint_documented,
        'trust_readiness_pct': ex.get('trust_readiness', 50),
        'governance_readiness_pct': ex.get('governance_readiness', 50),
        'institutional_completion_pct': ex.get('overall_completion', mc.get('build', 99)),
    },
    'catalog_gaps': [
        'Charter acknowledgments not tracked in onboarding',
        'No public-facing charter page separate from MC',
        'Charter dashboard not live',
        'Founding documents bundle not enforced before service',
        'Coalition partners not prompted to acknowledge charter',
        'Education Leaders no charter certification step',
        'Charter not linked from volunteer signup funnel',
        'No translation or accessibility review of charter',
        'January 2027 goals not instrumented against live metrics',
        'War Room countdown not yet built (#101)',
    ],
    'recommended_next_build': {
        'number': 101,
        'title': 'Cursor Implementation Package (50 Executable Steps)',
        'note': (
            '50 ordered implementation steps, Cursor master prompt, MVP scope, '
            'Sprint Zero gate, file-level acceptance criteria. Master Build Bible v2.'
        ),
    },
}

with open(root / 'data/founding-charter.json', 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')

print(
    f'Founding Charter: {len(CHARTER_SECTIONS)} sections, '
    f'{len(COMMITMENTS)} commitments, {founding_charter_readiness}% readiness'
)
