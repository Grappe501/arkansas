"""
Generate data/institutional-manifesto.json — Build #99.
Master Institutional Manifesto — Why We Are Building This v1.0.
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
manifesto_dashboard_live = False
required_reading_enforced = False
volunteer_acknowledgments = 0
public_manifesto_page_live = False

CORE_BELIEFS = [
    'Democracy depends upon informed citizens',
    'Informed citizens require access to trustworthy information',
    'Trustworthy information requires transparency, evidence, humility, and intellectual honesty',
    'Civic education should belong to everyone',
]

EXAMPLE_QUESTIONS = [
    'What does Citizens United actually mean?',
    'Why was the decision made?',
    'What changed?',
    'What can states do?',
    'What can Congress do?',
    'How does this affect me?',
]

BELIEF_SECTIONS = [
    {
        'id': 'MB-01',
        'title': 'We Believe',
        'summary': 'Democracy, trustworthy information, transparency, civic education for everyone',
        'beliefs': CORE_BELIEFS,
    },
    {
        'id': 'MB-02',
        'title': 'We Believe Questions Matter',
        'summary': 'Questions are the beginning of understanding — not weaknesses',
        'example_questions': EXAMPLE_QUESTIONS,
        'questions_strengthen_democracy': True,
    },
    {
        'id': 'MB-03',
        'title': 'We Believe Knowledge Should Be Accessible',
        'summary': 'Complex legal and government topics explained for every Arkansan',
        'accessible_to_all': True,
        'not_only_for_lawyers_or_insiders': True,
    },
    {
        'id': 'MB-04',
        'title': 'We Believe Civic Education Should Unite Communities',
        'summary': 'Learning → conversations → understanding → respect → stronger communities',
        'neighbors_learn_together_even_when_disagree': True,
    },
    {
        'id': 'MB-05',
        'title': 'We Believe Arkansas Can Lead',
        'summary': 'Great civic institutions can begin in Arkansas — built by volunteers, guided by evidence',
        'arkansas_can_demonstrate_healthy_civic_education': True,
    },
    {
        'id': 'MB-06',
        'title': 'We Believe Volunteers Change History',
        'summary': 'Institutions built by ordinary Arkansans accomplishing extraordinary things',
        'ordinary_volunteer_examples': [
            'Retired teacher', 'College student', 'Librarian', 'Veteran',
            'Farmer', 'Small business owner', 'Parent', 'Neighbor',
        ],
    },
    {
        'id': 'MB-07',
        'title': 'We Believe Trust Must Be Earned',
        'summary': 'Trust through careful research, transparent sources, respectful dialogue, responsible leadership',
        'trust_earned_through': [
            'Careful research', 'Transparent sources', 'Respectful dialogue',
            'Responsible leadership', 'Consistent behavior',
        ],
        'every_article_strengthens_or_weakens_trust': True,
    },
    {
        'id': 'MB-08',
        'title': 'We Believe Institutions Should Outlive Their Founders',
        'summary': 'Success measured by continued service to Arkansas decades from now',
        'stewardship_for_future_volunteers': True,
    },
    {
        'id': 'MB-09',
        'title': 'We Believe Education Comes Before Advocacy',
        'summary': 'Help people understand — Arkansans draw their own conclusions',
        'responsibilities': [
            'Help people understand', 'Explain', 'Document', 'Preserve history',
            'Present evidence', 'Distinguish fact from interpretation and policy',
        ],
    },
    {
        'id': 'MB-10',
        'title': 'We Believe Communities Matter More Than Algorithms',
        'summary': 'Civic education built through relationships — technology supports, does not replace',
        'built_through': [
            'Neighborhood conversations', 'Library programs', 'Community organizations',
            'Education Leaders', 'Volunteers', 'Families', 'Friends',
        ],
        'one_conversation_at_a_time': True,
    },
    {
        'id': 'MB-11',
        'title': 'We Believe in Arkansas',
        'summary': 'Arkansas deserves civic understanding, volunteers, transparent research, thoughtful leadership',
        'arkansas_deserves': [
            'Institution devoted to civic understanding',
            'Volunteers willing to teach',
            'Transparent research',
            'Thoughtful leadership',
            'Respectful exploration of constitutional questions',
        ],
    },
]

OUR_PROMISE = [
    'Pursue evidence before assumptions',
    'Welcome sincere questions',
    'Acknowledge uncertainty when it exists',
    'Correct mistakes openly',
    'Continue learning',
    'Treat every Arkansan with dignity',
    'Protect the public trust entrusted to us',
]

INSTITUTIONAL_MOTTO = [
    {'line': 'Learn with Curiosity.', 'theme': 'curiosity'},
    {'line': 'Lead with Integrity.', 'theme': 'integrity'},
    {'line': 'Serve with Humility.', 'theme': 'humility'},
    {'line': 'Strengthen Arkansas.', 'theme': 'service'},
]

MANIFESTO_DASHBOARD_INDICATORS = [
    {'id': 'IM-D01', 'indicator': 'Volunteer acknowledgments', 'current': volunteer_acknowledgments, 'status': 'planned'},
    {'id': 'IM-D02', 'indicator': 'Required reading completion', 'current': 0, 'unit': '%', 'status': 'planned'},
    {'id': 'IM-D03', 'indicator': 'Belief sections documented', 'current': len(BELIEF_SECTIONS), 'status': 'partial'},
    {'id': 'IM-D04', 'indicator': 'Promise commitments', 'current': len(OUR_PROMISE), 'status': 'partial'},
    {'id': 'IM-D05', 'indicator': 'Public manifesto page', 'current': 'Partial', 'status': 'partial'},
    {'id': 'IM-D06', 'indicator': 'Onboarding integration', 'current': 0, 'unit': '%', 'status': 'planned'},
]

institutional_manifesto_readiness = min(
    66,
    14
    + len(CORE_BELIEFS) // 2
    + len(BELIEF_SECTIONS) // 2
    + len(EXAMPLE_QUESTIONS) // 2
    + len(OUR_PROMISE) // 2
    + len(INSTITUTIONAL_MOTTO) // 2
    + len(MANIFESTO_DASHBOARD_INDICATORS) // 2
    + 4  # founders reflection, january 2027, governing principle, motto
    + (2 if manifesto_dashboard_live else 0),
)

out = {
    'version': '1.0',
    'build': 99,
    'updated': today,
    'completion_target_date': completion_target_date,
    'title': 'Master Institutional Manifesto v1.0',
    'subtitle': 'Why We Are Building This',
    'tagline': 'The Moral and Philosophical Foundation',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/institutional-manifesto.html',
    'constitution': '/docs/MASTER_INSTITUTIONAL_MANIFESTO.md',
    'purpose': (
        'Technical plans explain how. Strategic plans explain what. The manifesto explains why. '
        'Moral and philosophical foundation of Citizens United Facts. Read by every volunteer, '
        'Education Leader, coalition partner, and future leader before serving. If every other '
        'document were lost, this explains the institution\'s purpose.'
    ),
    'governing_principle': (
        'Everything we build ultimately answers one question: Will this help an ordinary Arkansan '
        'better understand how self-government works? If yes, we build it. If no, we do not. '
        'That simple question guides Citizens United Facts long after every founder, volunteer, '
        'technology platform, and generation has changed. It is the institution\'s compass — always '
        'pointing toward service.'
    ),
    'founders_principle': (
        'One day, someone who has never met the founders may log in simply to understand something. '
        'They may never know how many volunteers built it, how many conversations shaped it, how '
        'many evenings were spent researching, how many communities contributed. That is exactly as '
        'it should be. The institution was never built to honor its founders. It was built to serve '
        'Arkansas.'
    ),
    'founders_reflection': {
        'title': "Founder's Reflection",
        'institution_not_built_to_honor_founders': True,
        'built_to_serve_arkansas': True,
    },
    'document_hierarchy': {
        'technical_plans': 'How the institution is built',
        'strategic_plans': 'What it will accomplish',
        'manifesto': 'Why it must exist',
        'if_all_else_lost_manifesto_remains': True,
    },
    'belief_sections': {
        'title': 'We Believe',
        'sections': BELIEF_SECTIONS,
        'sections_total': len(BELIEF_SECTIONS),
    },
    'our_promise': {
        'title': 'Our Promise',
        'commitments': OUR_PROMISE,
        'status': 'specified',
    },
    'january_2027': {
        'title': 'January 2027',
        'not_finish_line': True,
        'begins_fulfilling_promise': True,
        'buildings_designed_research_assembled_volunteers_prepared': True,
        'responsibility_begins': True,
        'days_remaining': days_remaining,
    },
    'institutional_motto': {
        'title': 'Institutional Motto',
        'lines': INSTITUTIONAL_MOTTO,
        'full': 'Learn with Curiosity. Lead with Integrity. Serve with Humility. Strengthen Arkansas.',
    },
    'required_reading': {
        'title': 'Required Reading',
        'audiences': [
            'Every volunteer', 'Every Education Leader',
            'Every coalition partner', 'Every future leader',
        ],
        'before_beginning_service': True,
        'enforced': required_reading_enforced,
        'acknowledgments': volunteer_acknowledgments,
        'status': 'planned',
    },
    'manifesto_dashboard': {
        'title': 'Manifesto Dashboard',
        'indicators': MANIFESTO_DASHBOARD_INDICATORS,
        'live': manifesto_dashboard_live,
        'status': 'planned',
    },
    'integration': {
        'chain': (
            'Manifesto → Organizational Constitution → Operating Manual → '
            'Public Trust Framework → Volunteer Network → Education Academy'
        ),
        'moral_foundation_for_all_systems': True,
        'systems': [
            {'system': 'Organizational Constitution (#76)', 'route': '/mission-control/organizational-constitution.html', 'status': 'live'},
            {'system': 'Operating Manual (#90)', 'route': '/mission-control/institutional-operating-manual.html', 'status': 'live'},
            {'system': 'Public Trust (#82)', 'route': '/mission-control/public-trust-institutional-credibility.html', 'status': 'live'},
            {'system': 'Launch Certification (#97)', 'route': '/mission-control/institutional-launch-certification.html', 'status': 'live'},
            {'system': 'Continuous Improvement (#98)', 'route': '/mission-control/institutional-continuous-improvement.html', 'status': 'live'},
            {'system': 'Project Constitution (#2)', 'route': '/builds/002-project-constitution.html', 'status': 'live'},
        ],
    },
    'long_term_vision': (
        'The manifesto remains the compass when technology changes, volunteers rotate, and '
        'generations pass. Every decision returns to one question: Does this help an ordinary '
        'Arkansan understand self-government? The institution serves Arkansas — not its founders.'
    ),
    'summary': {
        'completion_target_date': completion_target_date,
        'days_remaining': days_remaining,
        'institutional_manifesto_readiness_pct': institutional_manifesto_readiness,
        'belief_sections': len(BELIEF_SECTIONS),
        'promise_commitments': len(OUR_PROMISE),
        'motto_lines': len(INSTITUTIONAL_MOTTO),
        'manifesto_dashboard_live': manifesto_dashboard_live,
        'required_reading_enforced': required_reading_enforced,
        'volunteer_acknowledgments': volunteer_acknowledgments,
        'public_manifesto_page_live': public_manifesto_page_live,
        'trust_readiness_pct': ex.get('trust_readiness', 50),
        'governance_readiness_pct': ex.get('governance_readiness', 50),
        'institutional_completion_pct': ex.get('overall_completion', mc.get('build', 98)),
    },
    'catalog_gaps': [
        'Required reading not enforced in onboarding',
        'Zero volunteer manifesto acknowledgments',
        'No public-facing manifesto page separate from MC',
        'Manifesto dashboard not live',
        'Onboarding flow does not gate service on manifesto read',
        'Coalition partners not prompted to acknowledge manifesto',
        'Education Leaders no manifesto certification step',
        'Manifesto not linked from volunteer signup funnel',
        'No translation or accessibility review of manifesto',
        'Motto not displayed consistently across public site',
    ],
    'recommended_next_build': {
        'number': 100,
        'title': 'Executive War Room & Countdown Dashboard Components',
        'note': (
            'War room UI, countdown dashboard, manifesto onboarding integration, '
            'acknowledgment tracker, public manifesto page, COMP-* specs.'
        ),
    },
}

with open(root / 'data/institutional-manifesto.json', 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')

print(
    f'Institutional Manifesto: {len(BELIEF_SECTIONS)} belief sections, '
    f'{len(OUR_PROMISE)} promises, {institutional_manifesto_readiness}% readiness'
)
