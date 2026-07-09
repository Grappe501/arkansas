"""
Generate data/governance-constitution.json — Build #49 Master Governance, Stewardship & Institutional Constitution v1.0.
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
rm = load_json(root / 'data/research-methodology.json')
trust = load_json(root / 'data/trust-framework.json')

MISSION = (
    'Citizens United Facts exists to provide Arkansans with accurate, transparent, '
    'well-documented civic education about Citizens United v. FEC, its historical context, '
    'constitutional foundations, measurable impacts, and related public policy discussions.'
)

VALUES = [
    {
        'id': 'VAL-01', 'title': 'Truth',
        'description': 'Facts matter. Claims require evidence. Corrections are welcomed.',
        'status': 'live', 'implementation': 'Evidence Ledger + Research Methodology',
    },
    {
        'id': 'VAL-02', 'title': 'Transparency',
        'description': 'Readers understand sources, review, updates, and revision reasons.',
        'status': 'partial', 'implementation': 'Trust Framework partial — 24% readiness',
    },
    {
        'id': 'VAL-03', 'title': 'Respect',
        'description': 'Different viewpoints welcomed; perspectives explained fairly.',
        'status': 'partial', 'implementation': 'Debate hall planned — narrative architecture',
    },
    {
        'id': 'VAL-04', 'title': 'Intellectual Curiosity',
        'description': 'Questions encouraged. Research ongoing. Learning never ends.',
        'status': 'live', 'implementation': 'Research Observatory + Learning Lab designed',
    },
    {
        'id': 'VAL-05', 'title': 'Arkansas First',
        'description': 'Built for Arkansas. National context supports local civic education.',
        'status': 'live', 'implementation': '75-county OS, Arkansas pilot in all frameworks',
    },
    {
        'id': 'VAL-06', 'title': 'Long-Term Stewardship',
        'description': 'Valuable decades from now. Credibility over short-term popularity.',
        'status': 'partial', 'implementation': 'Institutional Roadmap V1–V10 — succession planned',
    },
]

RESPONSIBILITIES = [
    {'id': 'RES-01', 'title': 'Maintain research quality', 'status': 'partial', 'route': '/mission-control/research-methodology.html'},
    {'id': 'RES-02', 'title': 'Maintain source transparency', 'status': 'partial', 'route': '/library/'},
    {'id': 'RES-03', 'title': 'Correct verified errors', 'status': 'partial', 'route': '/mission-control/trust.html'},
    {'id': 'RES-04', 'title': 'Review content regularly', 'status': 'planned', 'route': '/mission-control/content-factory.html'},
    {'id': 'RES-05', 'title': 'Protect participant privacy', 'status': 'partial', 'route': '/mission-control/contact-intelligence.html'},
    {'id': 'RES-06', 'title': 'Document important decisions', 'status': 'partial', 'route': '/builds/'},
    {'id': 'RES-07', 'title': 'Preserve institutional memory', 'status': 'partial', 'route': '/mission-control/'},
]

STEWARDS = [
    {'id': 'STW-01', 'title': 'Executive Steward', 'scope': 'Mission, strategy, institutional health', 'status': 'partial', 'assigned': False},
    {'id': 'STW-02', 'title': 'Research Steward', 'scope': 'Research quality, methodology, evidence', 'status': 'planned', 'assigned': False},
    {'id': 'STW-03', 'title': 'Editorial Steward', 'scope': 'Content standards, review, publication', 'status': 'planned', 'assigned': False},
    {'id': 'STW-04', 'title': 'Technology Steward', 'scope': 'Software, infrastructure, security, MC', 'status': 'partial', 'assigned': False},
    {'id': 'STW-05', 'title': 'Community Steward', 'scope': 'Education leaders, academy, outreach', 'status': 'planned', 'assigned': False},
    {'id': 'STW-06', 'title': 'Coalition Steward', 'scope': 'Partnerships, Arkansas organizations', 'status': 'planned', 'assigned': False},
    {'id': 'STW-07', 'title': 'Mission Control Steward', 'scope': 'MC operations, reporting, governance data', 'status': 'partial', 'assigned': False},
]

DECISION_CATEGORIES = [
    {'id': 'DEC-OP', 'title': 'Operational', 'description': 'Routine administration', 'mc_logging': 'partial'},
    {'id': 'DEC-ED', 'title': 'Editorial', 'description': 'Educational content, research, publications', 'mc_logging': 'partial'},
    {'id': 'DEC-TE', 'title': 'Technical', 'description': 'Software, infrastructure, security, Mission Control', 'mc_logging': 'live'},
    {'id': 'DEC-ST', 'title': 'Strategic', 'description': 'Mission, expansion, partnerships, long-term planning', 'mc_logging': 'partial'},
]

PUBLIC_ACCOUNTABILITY = [
    {'id': 'PUB-01', 'document': 'Mission', 'status': 'live', 'route': '/docs/MASTER_GOVERNANCE_CONSTITUTION.md'},
    {'id': 'PUB-02', 'document': 'Editorial standards', 'status': 'partial', 'route': '/mission-control/content-factory.html'},
    {'id': 'PUB-03', 'document': 'Research methodology', 'status': 'live', 'route': '/docs/MASTER_RESEARCH_METHODOLOGY.md'},
    {'id': 'PUB-04', 'document': 'Correction policy', 'status': 'partial', 'route': '/mission-control/trust.html'},
    {'id': 'PUB-05', 'document': 'Privacy policy', 'status': 'planned', 'route': None},
    {'id': 'PUB-06', 'document': 'Accessibility commitment', 'status': 'partial', 'route': '/mission-control/design.html'},
    {'id': 'PUB-07', 'document': 'Governance principles', 'status': 'live', 'route': '/docs/MASTER_GOVERNANCE_CONSTITUTION.md'},
]

CORRECTION_POLICY = {
    'steps': ['Investigate', 'Correct', 'Document', 'Explain', 'Learn'],
    'principle': 'Corrections strengthen trust — never viewed as failures',
    'status': 'partial',
    'current': 'Trust Framework documents process — no public correction log live',
    'route': '/mission-control/trust.html',
}

COMMUNITY_PARTICIPATION = [
    {'channel': 'Research suggestions', 'status': 'planned'},
    {'channel': 'Source recommendations', 'status': 'planned'},
    {'channel': 'Educational questions', 'status': 'partial', 'note': 'FAQ planned'},
    {'channel': 'Coalition participation', 'status': 'planned', 'note': '0 orgs'},
    {'channel': 'Community education', 'status': 'planned', 'note': '0 leaders'},
    {'channel': 'Volunteer service', 'status': 'planned'},
]

INSTITUTIONAL_MEMORY = [
    {'type': 'Major decisions', 'status': 'partial', 'current': 'Build decisions in MC builds[]'},
    {'type': 'Version history', 'status': 'live', 'current': 'Git + VERSION + CHANGELOG'},
    {'type': 'Research milestones', 'status': 'planned'},
    {'type': 'Editorial milestones', 'status': 'planned'},
    {'type': 'Coalition growth', 'status': 'planned', 'current': '0 orgs'},
    {'type': 'Mission Control history', 'status': 'live', 'current': f'{len(mc.get("builds", []))} builds logged'},
    {'type': 'Annual reports', 'status': 'planned'},
]

ANNUAL_REVIEW = {
    'title': 'Institutional Stewardship Report',
    'frequency': 'Annual',
    'status': 'planned',
    'dimensions': [
        'Mission alignment', 'Research quality', 'Educational impact',
        'Coalition development', 'Technical health', 'Accessibility',
        'Transparency', 'Governance improvements',
    ],
    'note': 'Institutional Roadmap defines annual review — report generator not built',
    'route': '/mission-control/institutional-roadmap.html',
}

INSTITUTIONAL_OATH = [
    'We will seek truth through evidence.',
    'We will explain complex issues with honesty and clarity.',
    'We will acknowledge uncertainty when it exists.',
    'We will distinguish documented facts from interpretation.',
    'We will preserve transparency in our methods.',
    'We will welcome thoughtful questions.',
    'We will continue improving the institution for future generations of Arkansans.',
]

values_live = sum(1 for v in VALUES if v['status'] == 'live')
values_partial = sum(1 for v in VALUES if v['status'] == 'partial')
stewards_assigned = sum(1 for s in STEWARDS if s.get('assigned'))
pub_live = sum(1 for p in PUBLIC_ACCOUNTABILITY if p['status'] == 'live')
pub_partial = sum(1 for p in PUBLIC_ACCOUNTABILITY if p['status'] == 'partial')
mem_live = sum(1 for m in INSTITUTIONAL_MEMORY if m['status'] == 'live')
mem_partial = sum(1 for m in INSTITUTIONAL_MEMORY if m['status'] == 'partial')

MC_METRICS = [
    {'id': 'GOV-01', 'title': 'Institutional values defined', 'status': 'live', 'current': f'{len(VALUES)}/6'},
    {'id': 'GOV-02', 'title': 'Values implemented', 'status': 'partial', 'current': f'{values_live} live, {values_partial} partial'},
    {'id': 'GOV-03', 'title': 'Steward roles defined', 'status': 'live', 'current': f'{len(STEWARDS)}/7'},
    {'id': 'GOV-04', 'title': 'Stewards formally assigned', 'status': 'planned', 'current': f'{stewards_assigned}/7'},
    {'id': 'GOV-05', 'title': 'Public accountability documents', 'status': 'partial', 'current': f'{pub_live + pub_partial}/{len(PUBLIC_ACCOUNTABILITY)}'},
    {'id': 'GOV-06', 'title': 'Correction policy operational', 'status': 'partial', 'current': 'Documented — no correction log'},
    {'id': 'GOV-07', 'title': 'Annual stewardship report', 'status': 'planned', 'current': 'Not generated'},
    {'id': 'GOV-08', 'title': 'Succession planning', 'status': 'partial', 'current': 'Roadmap sustainability — not operational'},
    {'id': 'GOV-09', 'title': 'Community contribution review', 'status': 'planned', 'current': 'No intake workflow'},
    {'id': 'GOV-10', 'title': 'Strategic decision logging', 'status': 'partial', 'current': 'MC builds[] — not full decision registry'},
]

readiness_factors = [
    100,  # constitution defined
    (values_live + values_partial * 0.5) / len(VALUES) * 100,
    len(STEWARDS) / 7 * 100 * 0.5,  # roles defined not assigned
    (pub_live + pub_partial * 0.5) / len(PUBLIC_ACCOUNTABILITY) * 100,
    (mem_live + mem_partial * 0.5) / len(INSTITUTIONAL_MEMORY) * 100,
    0,  # annual review
    0,  # stewards assigned
    30,  # correction policy partial
]
governance_readiness = round(sum(readiness_factors) / len(readiness_factors))

out = {
    'version': '1.0',
    'build': 49,
    'updated': today,
    'title': 'Master Governance, Stewardship & Institutional Constitution v1.0',
    'subtitle': 'The Rules That Govern the Institution',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/governance.html',
    'constitution': '/docs/MASTER_GOVERNANCE_CONSTITUTION.md',
    'purpose': 'How the institution governs itself, protects its mission, and ensures continuity beyond founders.',
    'governing_principle': 'Evidence-based civic education, transparent scholarship, respectful dialogue, long-term Arkansas service.',
    'mission_statement': MISSION,
    'extends': [
        {'title': 'Project Constitution', 'build': 2, 'route': '/builds/002-project-constitution.md'},
        {'title': 'Research Methodology', 'build': 43, 'route': '/data/research-methodology.json'},
        {'title': 'Trust Framework', 'build': 36, 'route': '/data/trust-framework.json'},
        {'title': 'Institutional Roadmap', 'build': 44, 'route': '/data/institutional-roadmap.json'},
    ],
    'institutional_values': VALUES,
    'institutional_responsibilities': RESPONSIBILITIES,
    'editorial_independence': {
        'principle': 'Evidence, documentation, historical accuracy, educational value — not popularity or political pressure',
        'standards_route': '/mission-control/content-factory.html',
        'research_route': '/mission-control/research-methodology.html',
        'status': 'partial',
    },
    'conflict_disclosure': {
        'disclosures': ['Funding (where appropriate)', 'Author disclosures', 'Research limitations', 'Source conflicts'],
        'status': 'planned',
        'current': 'Not enforced in content metadata',
    },
    'correction_policy': CORRECTION_POLICY,
    'governance_structure': {
        'title': 'Steward Roles',
        'stewards': STEWARDS,
        'stewards_total': len(STEWARDS),
        'stewards_assigned': stewards_assigned,
        'note': 'One individual may hold multiple roles initially',
    },
    'decision_categories': DECISION_CATEGORIES,
    'public_accountability': PUBLIC_ACCOUNTABILITY,
    'community_participation': {
        'channels': COMMUNITY_PARTICIPATION,
        'review_gate': 'Every contribution reviewed before becoming institutional knowledge',
        'status': 'planned',
    },
    'institutional_memory': INSTITUTIONAL_MEMORY,
    'succession_planning': {
        'principle': 'Institution should not depend on one individual',
        'status': 'partial',
        'current': ir.get('sustainability_planning', ['Documentation in Institutional Roadmap'])[0] if ir.get('sustainability_planning') else 'Roadmap only',
        'route': '/mission-control/institutional-roadmap.html',
    },
    'annual_institutional_review': ANNUAL_REVIEW,
    'institutional_oath': INSTITUTIONAL_OATH,
    'long_term_vision': {
        'recognition': 'Trusted civic education — not loudest argument',
        'audiences': ['Teachers', 'Students', 'Journalists', 'Community organizations', 'Public officials', 'Citizens'],
        'defining_quality': 'Evidence above rhetoric',
    },
    'mc_integration': {
        'title': 'Mission Control Governance Metrics',
        'status': 'partial',
        'metrics': MC_METRICS,
        'governance_as_system': True,
    },
    'related_blueprints': [
        {'title': 'Institutional Roadmap', 'route': '/data/institutional-roadmap.json', 'build': 44},
        {'title': 'Research Methodology', 'route': '/data/research-methodology.json', 'build': 43},
        {'title': 'Trust Framework', 'route': '/data/trust-framework.json', 'build': 36},
        {'title': 'Systems Integration', 'route': '/data/systems-integration.json', 'build': 45},
    ],
    'summary': {
        'values_total': len(VALUES),
        'values_live': values_live,
        'values_partial': values_partial,
        'responsibilities_total': len(RESPONSIBILITIES),
        'stewards_total': len(STEWARDS),
        'stewards_assigned': stewards_assigned,
        'decision_categories': len(DECISION_CATEGORIES),
        'public_docs_live': pub_live,
        'public_docs_partial': pub_partial,
        'institutional_memory_live': mem_live,
        'annual_review_live': False,
        'correction_log_live': False,
        'succession_operational': False,
        'builds_logged': len(mc.get('builds', [])),
        'governance_readiness_pct': governance_readiness,
    },
    'catalog_gaps': [
        '0/7 stewards formally assigned — roles defined only',
        'Annual Institutional Stewardship Report not generated',
        'No public correction log — policy documented in Trust Framework only',
        'Privacy policy not published',
        'Community contribution review workflow not built',
        'Conflict disclosure not enforced in content metadata',
        'Editorial independence principles live — enforcement workflow partial',
        'Institutional memory = build history — research/editorial/coalition milestones missing',
        'Build #2 Project Constitution and Build #49 Governance Constitution coexist — hierarchy documented',
        'Component specifications still deferred — governance UI widgets unmapped',
    ],
    'recommended_next_build': {
        'number': 50,
        'title': 'Component Specifications with Props/States',
        'note': 'Map steward role cards, values panels, accountability doc links, and annual review widgets to COMP-* from Build #17.',
    },
}

path = root / 'data/governance-constitution.json'
with open(path, 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')
print(f'Governance Constitution: {stewards_assigned}/{len(STEWARDS)} stewards assigned, {governance_readiness}% readiness')
