"""
Generate data/organizational-constitution.json — Build #76.
Master Organizational Constitution & Operating Charter v1.0.
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
vfc = load_json(root / 'data/volunteer-funding-constitution.json')
gov = load_json(root / 'data/governance-constitution.json')

ex = mc.get('executive', {})

# Honest zeros
departments_operational = 0
constitutional_amendments = 0
adherence_monitoring_live = False
constitution_dashboard_live = False
articles_ratified = 15  # all specified in constitution text

CORE_VALUES = [
    {'id': 'OC-V1', 'value': 'Truth', 'principle': 'Evidence before opinion'},
    {'id': 'OC-V2', 'value': 'Transparency', 'principle': 'Show sources, explain methods, document decisions'},
    {'id': 'OC-V3', 'value': 'Curiosity', 'principle': 'Questions strengthen learning'},
    {'id': 'OC-V4', 'value': 'Respect', 'principle': 'Dignity; welcome honest questions and thoughtful dialogue'},
    {'id': 'OC-V5', 'value': 'Service', 'principle': 'Knowledge exists to serve the people of Arkansas'},
    {'id': 'OC-V6', 'value': 'Stewardship', 'principle': 'Every generation leaves the institution stronger'},
]

CONSTITUTION_ARTICLES = [
    {
        'article': 1, 'id': 'art-i', 'title': 'Name',
        'text': 'Citizens United Facts — educate about Citizens United v. FEC; does not support or oppose by name',
        'status': 'ratified',
    },
    {
        'article': 2, 'id': 'art-ii', 'title': 'Mission',
        'text': 'Most trusted, transparent, evidence-based educational institution for Citizens United, campaign finance, constitutional government, civic participation, and related policy',
        'status': 'ratified',
    },
    {
        'article': 3, 'id': 'art-iii', 'title': 'Vision',
        'text': '75 counties · 250 cities · 200,000 connected · lasting statewide civic education infrastructure',
        'status': 'ratified',
    },
    {
        'article': 4, 'id': 'art-iv', 'title': 'Core Values',
        'text': 'Truth, Transparency, Curiosity, Respect, Service, Stewardship',
        'status': 'ratified',
    },
    {
        'article': 5, 'id': 'art-v', 'title': 'Educational Commitment',
        'text': 'Teach, explain, document, research, clarify, preserve — reduce confusion not inflame controversy',
        'status': 'ratified',
    },
    {
        'article': 6, 'id': 'art-vi', 'title': 'Organizational Structure',
        'text': 'Permanent departments; additional departments may be created as institution grows',
        'status': 'ratified',
    },
    {
        'article': 7, 'id': 'art-vii', 'title': 'Leadership',
        'text': 'Stewardship — protect research quality, public trust, develop leaders, maintain transparency',
        'status': 'ratified',
    },
    {
        'article': 8, 'id': 'art-viii', 'title': 'Volunteer Foundation',
        'text': 'All-volunteer institution; volunteers central to all functions',
        'status': 'ratified',
    },
    {
        'article': 9, 'id': 'art-ix', 'title': 'Financial Principles',
        'text': 'Arkansas citizen contributions preferred; support never determines conclusions',
        'status': 'ratified',
    },
    {
        'article': 10, 'id': 'art-x', 'title': 'Coalition',
        'text': 'Collaboration with evidence-based orgs; each retains identity',
        'status': 'ratified',
    },
    {
        'article': 11, 'id': 'art-xi', 'title': 'Mission Control',
        'text': 'Executive operating system — monitors all institutional domains',
        'status': 'ratified',
    },
    {
        'article': 12, 'id': 'art-xii', 'title': 'Research Standards',
        'text': 'Documented, verified, reviewed, sourced; subject to continual improvement',
        'status': 'ratified',
    },
    {
        'article': 13, 'id': 'art-xiii', 'title': 'Community Leadership',
        'text': 'Academy → Neighborhood Leaders → City → County → Regional Mentors',
        'status': 'ratified',
    },
    {
        'article': 14, 'id': 'art-xiv', 'title': 'Public Trust',
        'text': 'Greatest asset — transparency, evidence, respect, consistency, accessibility, accountability',
        'status': 'ratified',
    },
    {
        'article': 15, 'id': 'art-xv', 'title': 'Amendment Process',
        'text': 'Evolve preserving mission, transparency, stewardship; MC documents revisions',
        'status': 'ratified',
    },
]

PERMANENT_DEPARTMENTS = [
    {'id': 'OC-D1', 'department': 'Executive Office', 'status': 'specified'},
    {'id': 'OC-D2', 'department': 'Research Office', 'status': 'specified'},
    {'id': 'OC-D3', 'department': 'Editorial Office', 'status': 'specified'},
    {'id': 'OC-D4', 'department': 'Technology Office', 'status': 'specified'},
    {'id': 'OC-D5', 'department': 'Design Office', 'status': 'specified'},
    {'id': 'OC-D6', 'department': 'Community Office', 'status': 'specified'},
    {'id': 'OC-D7', 'department': 'Coalition Office', 'status': 'specified'},
    {'id': 'OC-D8', 'department': 'Media Office', 'status': 'specified'},
    {'id': 'OC-D9', 'department': 'Mission Control Office', 'status': 'partial', 'route': '/mission-control/'},
    {'id': 'OC-D10', 'department': 'Operations Office', 'status': 'specified'},
]

EDUCATIONAL_COMMITMENT = ['Teach', 'Explain', 'Document', 'Research', 'Clarify', 'Preserve']

LEADERSHIP_RESPONSIBILITIES = [
    'Protecting research quality', 'Protecting public trust', 'Developing future leaders',
    'Maintaining transparency', 'Supporting volunteers', 'Strengthening Arkansas civic education',
]

VOLUNTEER_DOMAINS = [
    'Research', 'Education', 'Leadership', 'Community conversations',
    'Coalition development', 'Technology', 'Operations',
]

MC_MONITORS = [
    'Research', 'Technology', 'Education', 'Community', 'Coalition',
    'Leadership', 'Operations', 'Institutional health',
]

LEADERSHIP_LADDER = [
    'Community Education Academy', 'Neighborhood Education Leaders',
    'City Education Leaders', 'County Education Directors', 'Regional Mentors',
]

PUBLIC_TRUST_PILLARS = [
    'Transparency', 'Evidence', 'Respect', 'Consistency', 'Accessibility', 'Accountability',
]

AMENDMENT_CRITERIA = [
    'Preserve the educational mission', 'Strengthen transparency',
    'Improve institutional stewardship', 'Support Arkansas civic education',
]

INSTITUTIONAL_CREED = [
    'An informed citizenry is essential to self-government',
    'Complex issues deserve careful explanation',
    'Evidence strengthens democracy',
    'Respectful dialogue strengthens communities',
    'Ordinary Arkansans can become extraordinary civic educators',
    'Knowledge shared freely is one of the greatest public services',
]

SYSTEM_CONNECTIONS = [
    {'system': 'Governance Constitution (#49)', 'route': '/mission-control/governance.html', 'status': 'live', 'note': 'Institutional governance'},
    {'system': 'Volunteer & Funding (#75)', 'route': '/mission-control/volunteer-funding-constitution.html', 'status': 'live'},
    {'system': 'Project Constitution (#2)', 'route': '/builds/002-project-constitution.md', 'status': 'live'},
    {'system': 'Master Master Plan (#55)', 'route': '/mission-control/master-plan.html', 'status': 'live'},
    {'system': 'Civic Intelligence Command Center (#65)', 'route': '/mission-control/civic-intelligence-command-center.html', 'status': 'live'},
    {'system': 'Citizen Leadership Academy (#68)', 'route': '/mission-control/citizen-leadership-academy.html', 'status': 'live'},
    {'system': 'Coalition Network (#61)', 'route': '/mission-control/coalition-network.html', 'status': 'live'},
    {'system': 'Mission Control', 'route': '/mission-control/', 'status': 'live'},
]

organizational_constitution_readiness = min(
    46,
    10 + len(CONSTITUTION_ARTICLES) * 2 + len(CORE_VALUES) + 4,
)

out = {
    'version': '1.0',
    'build': 76,
    'updated': today,
    'title': 'Master Organizational Constitution & Operating Charter v1.0',
    'subtitle': 'The Founding Constitution',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/organizational-constitution.html',
    'constitution': '/docs/MASTER_ORGANIZATIONAL_CONSTITUTION.md',
    'purpose': (
        'Permanent constitutional framework — everything in the institution flows from this document.'
    ),
    'founders_principle': (
        'Not built merely to explain one Supreme Court decision. Built to strengthen '
        'Arkansas civic culture — every article, lesson, volunteer, leader, partner, county, '
        'neighborhood, conversation, generation.'
    ),
    'permanent_founding_framework': True,
    'supersedes_as_founding_charter': True,
    'institutional_motto': {
        'lines': ['Understand First.', 'Verify Always.', 'Teach Others.'],
    },
    'institutional_creed': INSTITUTIONAL_CREED,
    'articles': {
        'title': 'Fifteen Articles',
        'total': len(CONSTITUTION_ARTICLES),
        'ratified': articles_ratified,
        'items': CONSTITUTION_ARTICLES,
    },
    'core_values': {
        'title': 'Core Values (Article IV)',
        'values': CORE_VALUES,
    },
    'educational_commitment': {
        'title': 'Educational Commitment (Article V)',
        'commitments': EDUCATIONAL_COMMITMENT,
        'reduce_confusion_not_inflame': True,
    },
    'organizational_structure': {
        'title': 'Organizational Structure (Article VI)',
        'departments_total': len(PERMANENT_DEPARTMENTS),
        'departments_operational': departments_operational,
        'departments': PERMANENT_DEPARTMENTS,
        'additional_departments_allowed': True,
    },
    'leadership': {
        'title': 'Leadership (Article VII)',
        'stewardship': True,
        'responsibilities': LEADERSHIP_RESPONSIBILITIES,
    },
    'volunteer_foundation': {
        'title': 'Volunteer Foundation (Article VIII)',
        'all_volunteer_institution': True,
        'domains': VOLUNTEER_DOMAINS,
        'aligns_with': 'Volunteer & Funding Constitution (#75)',
    },
    'financial_principles': {
        'title': 'Financial Principles (Article IX)',
        'arkansas_citizen_contributions_preferred': True,
        'independence_preserved': True,
        'aligns_with': 'Volunteer & Funding Constitution (#75)',
    },
    'coalition': {
        'title': 'Coalition (Article X)',
        'organizations_retain_identity': True,
        'evidence_based_collaboration': True,
    },
    'mission_control_article': {
        'title': 'Mission Control (Article XI)',
        'executive_operating_system': True,
        'monitors': MC_MONITORS,
        'enables_informed_stewardship': True,
    },
    'research_standards': {
        'title': 'Research Standards (Article XII)',
        'requirements': ['Documented', 'Verified', 'Reviewed', 'Supported by appropriate sources'],
        'continual_improvement': True,
    },
    'community_leadership': {
        'title': 'Community Leadership (Article XIII)',
        'ladder': LEADERSHIP_LADDER,
        'multiplies_civic_education': True,
    },
    'public_trust': {
        'title': 'Public Trust (Article XIV)',
        'greatest_asset': True,
        'pillars': PUBLIC_TRUST_PILLARS,
    },
    'amendment_process': {
        'title': 'Amendment Process (Article XV)',
        'criteria': AMENDMENT_CRITERIA,
        'mc_documents_revisions': True,
        'amendments_recorded': constitutional_amendments,
        'status': 'specified',
    },
    'long_term_vision': (
        'Fifty years from now, still serving Arkansas. New technology, leaders, research, questions — '
        'purpose unchanged: help Arkansans understand constitutional system through research, evidence, '
        'education, and community leadership.'
    ),
    'integration': {
        'chain': (
            'Founding Constitution → Governance → Volunteer & Funding → Master Plan → '
            'Mission Control → All institutional systems'
        ),
        'systems': SYSTEM_CONNECTIONS,
        'everything_flows_from_constitution': True,
    },
    'summary': {
        'articles_total': len(CONSTITUTION_ARTICLES),
        'articles_ratified': articles_ratified,
        'core_values': len(CORE_VALUES),
        'departments_total': len(PERMANENT_DEPARTMENTS),
        'departments_operational': departments_operational,
        'constitutional_amendments': constitutional_amendments,
        'adherence_monitoring_live': adherence_monitoring_live,
        'constitution_dashboard_live': constitution_dashboard_live,
        'organizational_constitution_readiness_pct': organizational_constitution_readiness,
        'governance_readiness_pct': gov.get('summary', {}).get('governance_readiness_pct', 44),
        'volunteer_funding_constitution_readiness_pct': vfc.get('summary', {}).get('volunteer_funding_constitution_readiness_pct', 45),
        'public_launch_readiness_pct': ex.get('public_launch_readiness', 8),
    },
    'catalog_gaps': [
        '15 articles specified — no per-article public pages',
        '0/10 departments operational — department registry not built',
        '0 constitutional amendments recorded — amendment log not implemented',
        'Adherence monitoring not live — MC does not enforce constitution checks',
        'Build #76 vs Governance (#49) — reconcile founding vs governance constitutions?',
        'Build #76 vs Project Constitution (#2) — document supersession chain',
        'Build #76 vs Volunteer & Funding (#75) — Articles VIII-IX align but not linked in UI',
        'Department heads unassigned — organizational structure aspirational',
        'No public-facing constitution page on front door',
        'Amendment process specified — no workflow for proposing amendments',
        'MC Office partial — other 9 departments at 0% operational',
        'Founder principle not displayed on site header/footer',
        '50-year vision — no generational stewardship tracking',
    ],
    'recommended_next_build': {
        'number': 77,
        'title': 'Implementation Translation Layer & Engineering Artifacts',
        'note': (
            'Article pages, department registry, amendment log, adherence checklist, '
            'public constitution route, COMP-* specs, GitHub backlog.'
        ),
    },
}

with open(root / 'data/organizational-constitution.json', 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')

print(
    f'Organizational Constitution: {articles_ratified}/{len(CONSTITUTION_ARTICLES)} articles, '
    f'{departments_operational}/{len(PERMANENT_DEPARTMENTS)} departments, '
    f'{organizational_constitution_readiness}% readiness'
)
