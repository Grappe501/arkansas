"""
Generate data/public-trust-institutional-credibility.json — Build #82.
Master Public Trust & Institutional Credibility Framework v1.0.
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
tf = load_json(root / 'data/trust-framework.json')
el = load_json(root / 'data/evidence-ledger.json')

ex = mc.get('executive', {})

# Honest zeros
trust_dashboard_live = False
citation_completeness_pct = 0
pages_under_review = 0
correction_requests = 0
corrections_completed = 0
source_verification_complete = 0
accessibility_compliance_pct = 0
editorial_review_completion_pct = 0
annual_trust_audit_conducted = False
independent_reviews = 0
public_questions_logged = 0
crisis_responses_documented = 0

FOUNDATIONAL_QUESTIONS = [
    'Where did this information come from?',
    'Who wrote this?',
    'How was it reviewed?',
    'Can I verify it?',
    'When was it last updated?',
    'What if it is wrong?',
]

TRUST_PYRAMID = [
    {
        'layer': 1, 'id': 'transparency', 'title': 'Transparency',
        'principles': ['Show sources', 'Explain methodology', 'Document revisions', 'Publish standards'],
        'status': 'partial',
    },
    {
        'layer': 2, 'id': 'verifiability', 'title': 'Verifiability',
        'principles': ['Primary sources', 'Court opinions', 'Government records', 'Academic research', 'Historical documents'],
        'status': 'partial',
    },
    {
        'layer': 3, 'id': 'consistency', 'title': 'Consistency',
        'principles': ['Consistent terminology', 'Editorial standards', 'Citations', 'Educational quality'],
        'status': 'specified',
    },
    {
        'layer': 4, 'id': 'intellectual_honesty', 'title': 'Intellectual Honesty',
        'principles': ['Documented facts', 'Historical interpretation', 'Legal reasoning', 'Policy proposals', 'Scholarly disagreement', 'Acknowledged uncertainty'],
        'status': 'specified',
    },
    {
        'layer': 5, 'id': 'accountability', 'title': 'Accountability',
        'principles': ['Report an error', 'Suggest sources', 'Request clarification', 'Ask questions', 'Welcome correction'],
        'status': 'planned',
    },
    {
        'layer': 6, 'id': 'stewardship', 'title': 'Stewardship',
        'principles': ['Research', 'Volunteers', 'Technology', 'Financial resources', 'Community relationships', 'Institutional memory'],
        'status': 'specified',
    },
    {
        'layer': 7, 'id': 'time', 'title': 'Time',
        'principles': ['Long-term institutional investment', 'Years of consistent behavior', 'Not a marketing objective'],
        'status': 'specified',
    },
]

TRUST_DASHBOARD_INDICATORS = [
    {'id': 'PT-I01', 'indicator': 'Citation completeness', 'current': citation_completeness_pct, 'unit': '%', 'status': 'planned'},
    {'id': 'PT-I02', 'indicator': 'Pages under review', 'current': pages_under_review, 'status': 'planned'},
    {'id': 'PT-I03', 'indicator': 'Correction requests', 'current': correction_requests, 'status': 'planned'},
    {'id': 'PT-I04', 'indicator': 'Corrections completed', 'current': corrections_completed, 'status': 'planned'},
    {'id': 'PT-I05', 'indicator': 'Source verification status', 'current': source_verification_complete, 'status': 'planned'},
    {'id': 'PT-I06', 'indicator': 'Accessibility compliance', 'current': accessibility_compliance_pct, 'unit': '%', 'status': 'planned'},
    {'id': 'PT-I07', 'indicator': 'Editorial review completion', 'current': editorial_review_completion_pct, 'unit': '%', 'status': 'planned'},
    {'id': 'PT-I08', 'indicator': 'Research review cycle', 'current': 0, 'status': 'planned'},
]

PAGE_TRUST_INDICATORS = [
    'Last reviewed date', 'Primary sources', 'Supporting evidence',
    'Related court decisions', 'Research methodology', 'Version history', 'Correction policy',
]

TRUST_REVIEW_PROCESS = [
    'Research', 'Evidence Verification', 'Editorial Review',
    'Accessibility Review', 'Publication', 'Periodic Review', 'Revision (when necessary)',
]

ANNUAL_TRUST_AUDIT_DOMAINS = [
    'Research quality', 'Correction responsiveness', 'Citation quality',
    'Editorial consistency', 'Accessibility', 'Volunteer standards',
    'Governance', 'Public transparency',
]

INDEPENDENT_REVIEW_AREAS = [
    'Research practices', 'Educational materials', 'Accessibility',
    'Historical accuracy', 'Editorial standards',
]

PUBLIC_QUESTIONS_LOG = [
    'Frequently asked questions', 'Common misconceptions',
    'Clarifications', 'Updated explanations', 'New resources in response',
]

CRISIS_RESPONSE_STEPS = [
    'Investigate promptly', 'Correct carefully', 'Explain transparently',
    'Document revisions', 'Learn institutionally',
]

FOUNDERS_STANDARD = (
    'Trusted by people who reach different conclusions. Highest test: differing viewpoints '
    'still acknowledge accurate history, transparent evidence, fair competing ideas, honest documentation.'
)

SYSTEM_CONNECTIONS = [
    {'system': 'Research Institute (#73)', 'route': '/mission-control/arkansas-research-institute.html', 'status': 'live'},
    {'system': 'Evidence Ledger (#41)', 'route': '/mission-control/evidence-ledger.html', 'status': 'live'},
    {'system': 'Claims Registry (#41)', 'route': '/mission-control/evidence-ledger.html', 'status': 'live'},
    {'system': 'Mission Control', 'route': '/mission-control/', 'status': 'live'},
    {'system': 'Community Education Academy (#68)', 'route': '/mission-control/citizen-leadership-academy.html', 'status': 'live'},
    {'system': 'Arkansas Communications (#72)', 'route': '/mission-control/arkansas-communications.html', 'status': 'live'},
    {'system': 'Governance (#49)', 'route': '/mission-control/governance.html', 'status': 'live'},
    {'system': 'Digital Twin (#81)', 'route': '/mission-control/institutional-digital-twin.html', 'status': 'live'},
    {'system': 'Trust Framework (#36)', 'route': '/mission-control/trust.html', 'status': 'live', 'note': 'Extended by Build #82'},
    {'system': 'Organizational Constitution (#76)', 'route': '/mission-control/organizational-constitution.html', 'status': 'live'},
]

trust_readiness = min(
    52,
    16
    + len(TRUST_PYRAMID) * 2
    + len(FOUNDATIONAL_QUESTIONS) // 2
    + len(TRUST_DASHBOARD_INDICATORS) // 2
    + len(PAGE_TRUST_INDICATORS) // 2
    + len(TRUST_REVIEW_PROCESS) // 2
    + len(ANNUAL_TRUST_AUDIT_DOMAINS) // 2
    + 3,
)

out = {
    'version': '1.0',
    'build': 82,
    'updated': today,
    'title': 'Master Public Trust & Institutional Credibility Framework v1.0',
    'subtitle': 'Trust Is the Product',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/public-trust-institutional-credibility.html',
    'constitution': '/docs/MASTER_PUBLIC_TRUST_INSTITUTIONAL_CREDIBILITY.md',
    'purpose': (
        'Systems, standards, and operational practices ensuring Citizens United Facts '
        'becomes one of the most trusted civic education institutions in Arkansas.'
    ),
    'governing_principle': (
        'Trust is not a communication strategy. Trust is the cumulative result of '
        'thousands of disciplined decisions — every source, correction, volunteer, question, review, year.'
    ),
    'trust_is_greatest_asset': True,
    'foundational_principle': {
        'title': 'Foundational Principle',
        'questions': FOUNDATIONAL_QUESTIONS,
        'answer_before_asked': True,
    },
    'trust_pyramid': {
        'title': 'The Trust Pyramid',
        'layers_total': len(TRUST_PYRAMID),
        'layers': TRUST_PYRAMID,
        'public_trust_rest_upon_layers': True,
    },
    'public_trust_dashboard': {
        'title': 'Public Trust Dashboard',
        'indicators': TRUST_DASHBOARD_INDICATORS,
        'live': trust_dashboard_live,
        'trust_becomes_measurable': True,
        'status': 'planned',
    },
    'page_trust_indicators': {
        'title': 'Trust Indicators on Every Page',
        'indicators': PAGE_TRUST_INDICATORS,
        'quietly_displayed': True,
        'status': 'specified',
    },
    'trust_review_process': {
        'title': 'Trust Review Process',
        'steps': TRUST_REVIEW_PROCESS,
        'quality_institutional_habit': True,
        'status': 'specified',
    },
    'annual_trust_audit': {
        'title': 'Annual Trust Audit',
        'domains': ANNUAL_TRUST_AUDIT_DOMAINS,
        'conducted': annual_trust_audit_conducted,
        'public_trust_report': True,
        'continual_improvement': True,
        'status': 'specified',
    },
    'independent_review': {
        'title': 'Independent Review',
        'areas': INDEPENDENT_REVIEW_AREAS,
        'reviews_completed': independent_reviews,
        'external_review_strengthens_credibility': True,
        'status': 'specified',
    },
    'public_questions': {
        'title': 'Public Questions',
        'log_types': PUBLIC_QUESTIONS_LOG,
        'questions_logged': public_questions_logged,
        'transparent_log': True,
        'listening_strengthens_trust': True,
        'status': 'specified',
    },
    'crisis_response': {
        'title': 'Crisis Response',
        'steps': CRISIS_RESPONSE_STEPS,
        'responses_documented': crisis_responses_documented,
        'trust_grows_through_responsible_response': True,
        'status': 'specified',
    },
    'founders_standard': {
        'title': "Founder's Standard",
        'text': FOUNDERS_STANDARD,
        'trusted_by_different_conclusions': True,
        'highest_test_educational_integrity': True,
    },
    'integration': {
        'chain': (
            'Research Institute → Evidence Ledger → Claims Registry → Mission Control → '
            'Education Academy → Communications → Governance → Digital Twin'
        ),
        'trust_as_connective_tissue': True,
        'systems': SYSTEM_CONNECTIONS,
        'extends': 'Trust Framework (#36)',
    },
    'long_term_vision': (
        'Twenty years: reputation that cannot be purchased. Arkansans instinctively know: '
        '"If Citizens United Facts says it, I can see the evidence." Built one article, citation, '
        'correction, volunteer, conversation, year at a time.'
    ),
    'summary': {
        'trust_pyramid_layers': len(TRUST_PYRAMID),
        'trust_dashboard_live': trust_dashboard_live,
        'citation_completeness_pct': citation_completeness_pct,
        'pages_under_review': pages_under_review,
        'correction_requests': correction_requests,
        'corrections_completed': corrections_completed,
        'annual_trust_audit_conducted': annual_trust_audit_conducted,
        'independent_reviews': independent_reviews,
        'public_questions_logged': public_questions_logged,
        'public_trust_institutional_credibility_readiness_pct': trust_readiness,
        'trust_framework_readiness_pct': tf.get('summary', {}).get('trust_framework_readiness_pct', 30),
        'evidence_ledger_readiness_pct': el.get('summary', {}).get('evidence_ledger_readiness_pct', 22),
        'public_launch_readiness_pct': ex.get('public_launch_readiness', 8),
    },
    'catalog_gaps': [
        'Public Trust Dashboard not live — trust not measurable in MC',
        '0% citation completeness tracking — no audit pipeline',
        '0 correction requests/completions — correction workflow not built',
        'Annual Trust Audit not conducted — no public trust report',
        '0 independent reviews — external review process not operational',
        'Page trust indicators not on educational pages',
        'Trust review process specified — not enforced in publication workflow',
        'Build #82 vs Trust Framework (#36) — 7-layer vs 5-layer pyramid reconcile?',
        'Crisis response workflow not documented in MC',
        'Public questions transparent log not live',
        'Accessibility compliance not measured',
        'Editorial review completion not tracked',
        'Founder standard not on front door',
    ],
    'recommended_next_build': {
        'number': 83,
        'title': 'Trust Dashboard & Citation Audit Components',
        'note': (
            'Trust dashboard UI, citation audit pipeline, correction workflow, annual trust report, '
            'page trust indicators, COMP-* specs, GitHub backlog.'
        ),
    },
}

with open(root / 'data/public-trust-institutional-credibility.json', 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')

print(
    f'Public Trust Framework: {len(TRUST_PYRAMID)} layers, '
    f'{correction_requests} corrections, {trust_readiness}% readiness'
)
