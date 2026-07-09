"""
Generate data/sustainability-stewardship.json — Build #66.
Master Sustainability, Funding & Institutional Stewardship Blueprint v1.0.
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
gov = load_json(root / 'data/governance-constitution.json')
pmo = load_json(root / 'data/pmo.json')
cicc = load_json(root / 'data/civic-intelligence-command-center.json')
ir = load_json(root / 'data/institutional-roadmap.json')
cn = load_json(root / 'data/coalition-network.json')

ex = mc.get('executive', {})
builds_complete = len(mc.get('builds', [])) if isinstance(mc.get('builds'), list) else 66

# Honest zeros — no funding, no volunteers tracked, no reserve
funding_sources_active = 0
annual_revenue_tracked = False
operational_reserve = 0
volunteers_onboarded = 0
volunteer_training_completed = 0
volunteer_retention_pct = 0
annual_sustainability_report_live = False
financial_transparency_report_live = False

SUSTAINABILITY_PRINCIPLES = [
    {'id': 'SS-P1', 'principle': 'Educational Mission', 'test': 'Does it advance civic education?', 'status': 'live'},
    {'id': 'SS-P2', 'principle': 'Independence', 'test': 'Can the institution maintain editorial independence?', 'status': 'live'},
    {'id': 'SS-P3', 'principle': 'Transparency', 'test': 'Can the funding relationship be publicly explained?', 'status': 'live'},
    {'id': 'SS-P4', 'principle': 'Long-Term Value', 'test': 'Does it strengthen the institution over time?', 'status': 'live'},
    {'id': 'SS-P5', 'principle': 'Public Trust', 'test': 'Would a reasonable visitor view it as mission-consistent?', 'status': 'live'},
]

FUNDING_PORTFOLIO = [
    {'id': 'SS-F1', 'category': 'Individual Supporters', 'description': 'Arkansans who value civic education', 'sources': 0, 'status': 'planned'},
    {'id': 'SS-F2', 'category': 'Foundation Grants', 'description': 'Civic education, research, technology, community engagement', 'sources': 0, 'status': 'planned'},
    {'id': 'SS-F3', 'category': 'Institutional Partnerships', 'description': 'Libraries, universities, museums, educational organizations', 'sources': 0, 'status': 'planned'},
    {'id': 'SS-F4', 'category': 'Coalition Contributions', 'description': 'Organizations supporting shared educational resources', 'sources': cn.get('summary', {}).get('organizations_total', 0), 'status': 'scaffolded'},
    {'id': 'SS-F5', 'category': 'Educational Sponsorships', 'description': 'Events or resource development — editorial separation required', 'sources': 0, 'status': 'planned'},
]

RESOURCE_ALLOCATION = [
    {'area': 'Research', 'route': '/mission-control/research-observatory.html', 'status': 'partial'},
    {'area': 'Education', 'route': '/mission-control/education-academy.html', 'status': 'partial'},
    {'area': 'Technology', 'route': '/mission-control/technical-architecture.html', 'status': 'partial'},
    {'area': 'Community Education', 'route': '/mission-control/neighborhood-organizing.html', 'status': 'partial'},
    {'area': 'Coalition Development', 'route': '/mission-control/coalition-network.html', 'status': 'partial'},
    {'area': 'Mission Control', 'route': '/mission-control/', 'status': 'live'},
    {'area': 'Media', 'route': '/mission-control/media-studio.html', 'status': 'planned'},
    {'area': 'Operations', 'route': '/mission-control/pmo.html', 'status': 'partial'},
]

FINANCIAL_TRANSPARENCY_SECTIONS = [
    'Revenue categories', 'Major expense categories', 'Program investments',
    'Technology investments', 'Research investments', 'Community education investments',
]

KNOWLEDGE_PRESERVATION = [
    'Research', 'Documentation', 'Editorial standards', 'Mission Control history',
    'Governance decisions', 'Educational resources', 'Institutional memory',
]

TECHNOLOGY_SUSTAINABILITY = [
    'Documented architecture', 'Automated backups', 'Disaster recovery planning',
    'Version control', 'Infrastructure documentation', 'Maintainable software',
]

LEADERSHIP_SUSTAINABILITY = [
    'Documentation', 'Mentorship', 'Shared decision-making',
    'Leadership development', 'Succession planning',
]

VOLUNTEER_STEWARDSHIP_METRICS = [
    {'id': 'SS-V1', 'metric': 'Volunteer onboarding', 'current': volunteers_onboarded, 'status': 'planned'},
    {'id': 'SS-V2', 'metric': 'Training completion', 'current': volunteer_training_completed, 'status': 'planned'},
    {'id': 'SS-V3', 'metric': 'Leadership development', 'current': 0, 'status': 'planned'},
    {'id': 'SS-V4', 'metric': 'Retention', 'current': volunteer_retention_pct, 'unit': 'percent', 'status': 'planned'},
    {'id': 'SS-V5', 'metric': 'Recognition', 'current': 0, 'status': 'planned'},
]

ANNUAL_REVIEW_SECTIONS = [
    'Mission alignment', 'Financial health', 'Volunteer health', 'Coalition health',
    'Research continuity', 'Technology resilience', 'Leadership development', 'Operational risks',
]

SUSTAINABILITY_DASHBOARD = [
    {'id': 'SS-D1', 'indicator': 'Institutional Health', 'current': cicc.get('summary', {}).get('institutional_health_score', 32), 'unit': 'percent', 'status': 'partial'},
    {'id': 'SS-D2', 'indicator': 'Research Capacity', 'current': ex.get('research_readiness', 26), 'unit': 'percent', 'status': 'partial'},
    {'id': 'SS-D3', 'indicator': 'Volunteer Capacity', 'current': volunteers_onboarded, 'status': 'planned'},
    {'id': 'SS-D4', 'indicator': 'Coalition Strength', 'current': cn.get('summary', {}).get('organizations_total', 0), 'status': 'live'},
    {'id': 'SS-D5', 'indicator': 'Technology Stability', 'current': ex.get('technical_architecture_readiness', 38), 'unit': 'percent', 'status': 'partial'},
    {'id': 'SS-D6', 'indicator': 'Operational Readiness', 'current': ex.get('pmo_readiness', 46), 'unit': 'percent', 'status': 'partial'},
    {'id': 'SS-D7', 'indicator': 'Documentation Completeness', 'current': builds_complete, 'target': 66, 'status': 'partial'},
    {'id': 'SS-D8', 'indicator': 'Leadership Pipeline', 'current': 0, 'status': 'planned'},
    {'id': 'SS-D9', 'indicator': 'Community Growth', 'current': 0, 'target': 200_000, 'status': 'planned'},
]

SYSTEM_CONNECTIONS = [
    {'system': 'Governance Constitution (#49)', 'route': '/mission-control/governance.html', 'status': 'live'},
    {'system': 'PMO (#54)', 'route': '/mission-control/pmo.html', 'status': 'live'},
    {'system': 'Institutional Roadmap', 'route': '/mission-control/institutional-roadmap.html', 'status': 'partial'},
    {'system': 'Civic Intelligence Command Center (#65)', 'route': '/mission-control/civic-intelligence-command-center.html', 'status': 'live'},
    {'system': 'Coalition Network (#61)', 'route': '/mission-control/coalition-network.html', 'status': 'live'},
    {'system': 'Arkansas Action Network (#64)', 'route': '/mission-control/arkansas-action-network.html', 'status': 'live'},
    {'system': 'Mission Control', 'route': '/mission-control/', 'status': 'live'},
]

documentation_pct = round(builds_complete / 66 * 100) if builds_complete else 0
sustainability_stewardship_readiness = min(
    44,
    14 + len(SUSTAINABILITY_PRINCIPLES) * 2 + len(FUNDING_PORTFOLIO) * 2 + 4,
)

out = {
    'version': '1.0',
    'build': 66,
    'updated': today,
    'title': 'Master Sustainability, Funding & Institutional Stewardship Blueprint v1.0',
    'subtitle': 'Building an Institution That Lasts — Financial Sustainability Without Compromising Trust',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/sustainability-stewardship.html',
    'constitution': '/docs/MASTER_SUSTAINABILITY_STEWARDSHIP.md',
    'purpose': (
        'Ensure the institution can serve Arkansas for decades while protecting '
        'educational integrity, transparency, and independence.'
    ),
    'governing_principle': (
        'Permanent institutions endure through trust, wise investment, careful documentation, '
        'future leader development, mission protection, and earned community confidence.'
    ),
    'core_philosophy': (
        'Never forced to choose between financial survival and educational integrity. '
        'Governance and funding reduce conflicts of interest and strengthen public trust.'
    ),
    'five_sustainability_principles': SUSTAINABILITY_PRINCIPLES,
    'funding_portfolio': {
        'title': 'Diversified Funding Portfolio',
        'avoid_single_source': True,
        'categories': FUNDING_PORTFOLIO,
        'total_active_sources': funding_sources_active,
        'all_documented_transparently': True,
        'status': 'planned',
    },
    'financial_transparency': {
        'title': 'Financial Transparency',
        'annual_reporting_sections': FINANCIAL_TRANSPARENCY_SECTIONS,
        'balance': 'Transparency without unnecessary private donor disclosure',
        'report_live': financial_transparency_report_live,
        'status': 'planned',
    },
    'resource_allocation': {
        'title': 'Resource Allocation',
        'areas': RESOURCE_ALLOCATION,
        'status': 'partial',
    },
    'institutional_reserve': {
        'title': 'Institutional Reserve',
        'objective': 'Resilience during financial uncertainty without sacrificing standards',
        'current_reserve': operational_reserve,
        'status': 'planned',
    },
    'volunteer_stewardship': {
        'title': 'Volunteer Stewardship',
        'metrics': VOLUNTEER_STEWARDSHIP_METRICS,
        'status': 'planned',
    },
    'knowledge_preservation': {
        'title': 'Knowledge Preservation',
        'items': KNOWLEDGE_PRESERVATION,
        'principle': 'Knowledge continuity as important as financial continuity',
        'builds_documented': builds_complete,
        'status': 'partial',
    },
    'technology_sustainability': {
        'title': 'Technology Sustainability',
        'requirements': TECHNOLOGY_SUSTAINABILITY,
        'version_control': True,
        'github_connected': ex.get('github_status') == 'connected',
        'status': 'partial',
    },
    'leadership_sustainability': {
        'title': 'Leadership Sustainability',
        'elements': LEADERSHIP_SUSTAINABILITY,
        'no_single_point_of_failure': True,
        'status': 'partial',
    },
    'annual_sustainability_review': {
        'title': 'Annual Institutional Sustainability Report',
        'sections': ANNUAL_REVIEW_SECTIONS,
        'auto_generated': False,
        'live': annual_sustainability_report_live,
        'status': 'planned',
    },
    'sustainability_dashboard': {
        'title': 'Sustainability Dashboard',
        'indicators': SUSTAINABILITY_DASHBOARD,
        'status': 'partial',
    },
    'integration': {
        'systems': SYSTEM_CONNECTIONS,
        'monitored_with_same_rigor_as': 'Research quality and educational impact',
    },
    'long_term_vision': (
        'Twenty years after launch: still researching, teaching, training, documenting, '
        'supporting communities. Sustainability from governance, stewardship, diversified '
        'support, and public trust — not one source or one leader.'
    ),
    'summary': {
        'principles_total': len(SUSTAINABILITY_PRINCIPLES),
        'funding_categories': len(FUNDING_PORTFOLIO),
        'funding_sources_active': funding_sources_active,
        'operational_reserve': operational_reserve,
        'volunteers_onboarded': volunteers_onboarded,
        'volunteer_retention_pct': volunteer_retention_pct,
        'annual_report_live': annual_sustainability_report_live,
        'financial_report_live': financial_transparency_report_live,
        'documentation_builds': builds_complete,
        'documentation_pct': documentation_pct,
        'governance_owners_assigned': pmo.get('summary', {}).get('owners_assigned', 0) if isinstance(pmo.get('summary'), dict) else 0,
        'sustainability_stewardship_readiness_pct': sustainability_stewardship_readiness,
        'governance_readiness_pct': ex.get('governance_readiness', 44),
        'institutional_maturity_pct': ex.get('institutional_maturity_pct', 32),
        'public_launch_readiness_pct': ex.get('public_launch_readiness', 8),
    },
    'catalog_gaps': [
        '0 active funding sources — no revenue tracking in Mission Control',
        'Financial transparency report not published — annual reporting planned only',
        'Operational reserve $0 — resilience planning not implemented',
        '0 volunteers onboarded — volunteer stewardship metrics not wired',
        'Annual Sustainability Report not auto-generated',
        'Resource allocation categories defined — no budget tracking per area',
        'Educational sponsorship policy not operational — editorial separation unspecified in UI',
        'Build #66 vs Governance (#49) annual stewardship report — unify workflows?',
        'Technology sustainability partial — backups/DR documented in architecture, not verified',
        'Leadership succession from Action Network (#64) not linked to stewardship dashboard',
        'Documentation completeness counts builds — not all operational systems',
        'PMO 0/10 department owners — stewardship roles undefined',
    ],
    'recommended_next_build': {
        'number': 67,
        'title': 'Implementation Translation Layer & Engineering Artifacts',
        'note': (
            'Funding registry schema, volunteer tracking, annual report generator, reserve policy, '
            'resource allocation dashboard, route inventory, COMP-* specs, GitHub backlog.'
        ),
    },
}

with open(root / 'data/sustainability-stewardship.json', 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')

print(
    f'Sustainability Stewardship: {len(FUNDING_PORTFOLIO)} funding categories, '
    f'{funding_sources_active} active sources, '
    f'{sustainability_stewardship_readiness}% readiness'
)
