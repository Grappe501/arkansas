"""
Generate data/institutional-launch-certification.json — Build #97.
Master Institutional Launch Certification — The January 2027 Readiness Audit v1.0.
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


def domain_status(score):
    if score >= 56:
        return 'ready'
    if score >= 40:
        return 'in_progress'
    return 'not_started'


def certification_level(score):
    if score >= 70:
        return 4  # Launch Ready
    if score >= 55:
        return 3  # Operational
    if score >= 40:
        return 2  # Building
    return 1  # Planning


mc = load_json(root / 'data/mission-control.json')
mlp = load_json(root / 'data/master-launch-plan.json')
ex = mc.get('executive', {})

# Honest operational metrics
certification_dashboard_live = False
independent_review_completed = False
launch_recommendation_issued = False
domains_certified = 0
certification_archive_started = False

CERTIFICATION_LEVELS = [
    {'level': 1, 'name': 'Planning', 'description': 'Domain specified, not yet building'},
    {'level': 2, 'name': 'Building', 'description': 'Active development in progress'},
    {'level': 3, 'name': 'Operational', 'description': 'System functioning in private development'},
    {'level': 4, 'name': 'Launch Ready', 'description': 'Meets launch standards pending final audit'},
    {'level': 5, 'name': 'Certified', 'description': 'Independent review passed — launch certified'},
]

DOMAIN_STATUS_LABELS = ['not_started', 'in_progress', 'ready', 'certified']

CERTIFICATION_DOMAINS = [
    {
        'id': 'LCD-01',
        'domain': 'Research',
        'criteria': [
            'Core research library completed',
            'Evidence verified',
            'Sources documented',
            'Editorial review completed',
            'Claims Registry operational',
        ],
        'readiness_pct': ex.get('research_readiness', 43),
        'certification_level': certification_level(ex.get('research_readiness', 43)),
        'status': domain_status(ex.get('research_readiness', 43)),
        'certified': False,
    },
    {
        'id': 'LCD-02',
        'domain': 'Technology',
        'criteria': [
            'Website operational',
            'Mobile compatibility',
            'Search functioning',
            'User accounts working',
            'AI systems functioning',
            'Security review completed',
            'Backup systems verified',
        ],
        'readiness_pct': ex.get('technical_architecture_readiness', 38),
        'certification_level': certification_level(ex.get('technical_architecture_readiness', 38)),
        'status': domain_status(ex.get('technical_architecture_readiness', 38)),
        'certified': False,
    },
    {
        'id': 'LCD-03',
        'domain': 'Mission Control',
        'criteria': [
            'Executive dashboards',
            'County dashboards',
            'City dashboards',
            'Neighborhood dashboards',
            'PMO dashboards',
            'Reporting accuracy',
            'Digital Twin synchronization',
        ],
        'readiness_pct': ex.get('mc2_readiness', 42),
        'certification_level': certification_level(ex.get('mc2_readiness', 42)),
        'status': domain_status(ex.get('mc2_readiness', 42)),
        'certified': False,
    },
    {
        'id': 'LCD-04',
        'domain': 'Community Education Academy',
        'criteria': [
            'Curriculum complete',
            'Learning pathways operational',
            'Certification system functioning',
            'Education Leader training available',
        ],
        'readiness_pct': ex.get('education_academy_readiness', 26),
        'certification_level': certification_level(ex.get('education_academy_readiness', 26)),
        'status': domain_status(ex.get('education_academy_readiness', 26)),
        'certified': False,
    },
    {
        'id': 'LCD-05',
        'domain': 'Volunteer Network',
        'criteria': [
            'Volunteer onboarding',
            'Training materials',
            'Role documentation',
            'Leadership pathways',
            'Mentorship system',
        ],
        'readiness_pct': ex.get('outreach_readiness', 44),
        'certification_level': certification_level(ex.get('outreach_readiness', 44)),
        'status': domain_status(ex.get('outreach_readiness', 44)),
        'certified': False,
    },
    {
        'id': 'LCD-06',
        'domain': 'Coalition Network',
        'criteria': [
            'Organization onboarding',
            'Coalition directory',
            'Shared resources',
            'Partnership agreements',
            'Communication systems',
        ],
        'readiness_pct': ex.get('coalition_readiness', 44),
        'certification_level': certification_level(ex.get('coalition_readiness', 44)),
        'status': domain_status(ex.get('coalition_readiness', 44)),
        'certified': False,
    },
    {
        'id': 'LCD-07',
        'domain': 'Arkansas Coverage',
        'criteria': [
            'All 75 counties',
            '250 largest cities',
            'Neighborhood framework',
            'Education Leader recruitment',
            'Community conversation readiness',
        ],
        'readiness_pct': ex.get('statewide_growth_readiness', 48),
        'certification_level': certification_level(ex.get('statewide_growth_readiness', 48)),
        'status': domain_status(ex.get('statewide_growth_readiness', 48)),
        'certified': False,
    },
    {
        'id': 'LCD-08',
        'domain': 'Governance',
        'criteria': [
            'Constitution complete',
            'Operating Manual complete',
            'PMO operational',
            'Decision documentation',
            'Policies approved',
            'Leadership structure documented',
        ],
        'readiness_pct': ex.get('governance_readiness', 50),
        'certification_level': certification_level(ex.get('governance_readiness', 50)),
        'status': domain_status(ex.get('governance_readiness', 50)),
        'certified': False,
    },
    {
        'id': 'LCD-09',
        'domain': 'AI & LocalBrains',
        'criteria': [
            'LocalBrains operational',
            'Institutional knowledge connected',
            'AI assistants trained',
            'Knowledge Platform integrated',
            'Executive AI functioning',
        ],
        'readiness_pct': max(
            ex.get('localbrain_architecture_readiness', 60),
            ex.get('ai_institution_readiness', 57),
        ),
        'certification_level': certification_level(max(
            ex.get('localbrain_architecture_readiness', 60),
            ex.get('ai_institution_readiness', 57),
        )),
        'status': domain_status(max(
            ex.get('localbrain_architecture_readiness', 60),
            ex.get('ai_institution_readiness', 57),
        )),
        'certified': False,
    },
    {
        'id': 'LCD-10',
        'domain': 'Communications',
        'criteria': [
            'Public website',
            'Social media',
            'Educational videos',
            'Press materials',
            'Email communications',
            'Presentation resources',
        ],
        'readiness_pct': ex.get('arkansas_communications_readiness', 42),
        'certification_level': certification_level(ex.get('arkansas_communications_readiness', 42)),
        'status': domain_status(ex.get('arkansas_communications_readiness', 42)),
        'certified': False,
    },
    {
        'id': 'LCD-11',
        'domain': 'Trust & Transparency',
        'criteria': [
            'Citation review',
            'Public correction process',
            'Accessibility review',
            'Privacy review',
            'Transparency standards',
            'Annual review schedule',
        ],
        'readiness_pct': ex.get('trust_readiness', 50),
        'certification_level': certification_level(ex.get('trust_readiness', 50)),
        'status': domain_status(ex.get('trust_readiness', 50)),
        'certified': False,
    },
    {
        'id': 'LCD-12',
        'domain': 'Institutional Sustainability',
        'criteria': [
            'Documentation',
            'Knowledge preservation',
            'Leadership succession',
            'Volunteer capacity',
            'Financial readiness',
            'Long-term operating plan',
        ],
        'readiness_pct': ex.get('sustainability_stewardship_readiness', 38),
        'certification_level': certification_level(ex.get('sustainability_stewardship_readiness', 38)),
        'status': domain_status(ex.get('sustainability_stewardship_readiness', 38)),
        'certified': False,
    },
]

domains_certified = sum(1 for d in CERTIFICATION_DOMAINS if d['certified'])
overall_certification_score = sum(d['readiness_pct'] for d in CERTIFICATION_DOMAINS) // len(CERTIFICATION_DOMAINS)
overall_certification_level = certification_level(overall_certification_score)

EXEC_DASHBOARD_INDICATORS = [
    {'id': 'ILC-D01', 'indicator': 'Overall Certification Score', 'current': overall_certification_score, 'unit': '%', 'status': 'partial'},
    {'id': 'ILC-D02', 'indicator': 'Department Readiness', 'current': ex.get('executive_institution_readiness', 50), 'unit': '%', 'status': 'partial'},
    {'id': 'ILC-D03', 'indicator': 'County Readiness', 'current': ex.get('arkansas_county_operating_system_readiness', 47), 'unit': '%', 'status': 'partial'},
    {'id': 'ILC-D04', 'indicator': 'City Readiness', 'current': ex.get('arkansas_city_operating_system_readiness', 48), 'unit': '%', 'status': 'partial'},
    {'id': 'ILC-D05', 'indicator': 'Technology Readiness', 'current': ex.get('technical_architecture_readiness', 38), 'unit': '%', 'status': 'partial'},
    {'id': 'ILC-D06', 'indicator': 'Volunteer Readiness', 'current': ex.get('outreach_readiness', 44), 'unit': '%', 'status': 'partial'},
    {'id': 'ILC-D07', 'indicator': 'Research Readiness', 'current': ex.get('research_readiness', 43), 'unit': '%', 'status': 'partial'},
    {'id': 'ILC-D08', 'indicator': 'Trust Readiness', 'current': ex.get('trust_readiness', 50), 'unit': '%', 'status': 'partial'},
    {'id': 'ILC-D09', 'indicator': 'Governance Readiness', 'current': ex.get('governance_readiness', 50), 'unit': '%', 'status': 'partial'},
    {'id': 'ILC-D10', 'indicator': 'Overall Institutional Readiness', 'current': ex.get('overall_completion', mc.get('build', 96)), 'unit': '%', 'status': 'partial'},
]

LAUNCH_RECOMMENDATION_OPTIONS = [
    'Ready for Launch',
    'Launch with Limited Improvements Outstanding',
    'Delay Until Critical Issues Are Resolved',
]

CERTIFICATION_ARCHIVE_FIELDS = [
    'What was evaluated',
    'What standards existed',
    'What improvements were recommended',
    'When certification occurred',
]

total_criteria = sum(len(d['criteria']) for d in CERTIFICATION_DOMAINS)

institutional_launch_certification_readiness = min(
    66,
    14
    + len(CERTIFICATION_DOMAINS) // 2
    + total_criteria // 3
    + len(CERTIFICATION_LEVELS)
    + len(EXEC_DASHBOARD_INDICATORS) // 2
    + len(LAUNCH_RECOMMENDATION_OPTIONS)
    + len(CERTIFICATION_ARCHIVE_FIELDS) // 2
    + (2 if certification_dashboard_live else 0),
)

out = {
    'version': '1.0',
    'build': 97,
    'updated': today,
    'completion_target_date': completion_target_date,
    'title': 'Master Institutional Launch Certification v1.0',
    'subtitle': 'The January 2027 Readiness Audit',
    'tagline': 'Earn the Trust of Arkansas',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/institutional-launch-certification.html',
    'constitution': '/docs/MASTER_INSTITUTIONAL_LAUNCH_CERTIFICATION.md',
    'prior_launch_plan_route': '/mission-control/master-launch-plan.html',
    'purpose': (
        'Official Launch Certification Process — final quality gate before January 2027. '
        'Comprehensive audit determines whether every critical system is operational, '
        'trustworthy, documented, and ready for statewide use. Launch because earned '
        'confidence — not because the calendar says so.'
    ),
    'governing_principle': (
        'The institution launches only when it is ready to fulfill its promise. Not because '
        'the deadline arrives. Not because every feature is perfect. But because Citizens United '
        'Facts has demonstrated research, leadership, technology, governance, volunteers, '
        'transparency, and operational maturity necessary to become a trusted civic education '
        'institution for Arkansas.'
    ),
    'founders_principle': (
        'Trust is earned before launch—not after it. Preparation creates confidence. '
        'Discipline creates quality. Transparency creates credibility. Certification should '
        'represent months of careful work, thoughtful review, volunteer dedication, and '
        'unwavering commitment to serving Arkansas well.'
    ),
    'institutional_philosophy': {
        'title': 'Institutional Philosophy',
        'question_not_did_we_finish': True,
        'question_are_we_ready_for_trust': True,
        'supports_earning_trust': True,
    },
    'certification_domains': {
        'title': 'The Twelve Certification Domains',
        'domains': CERTIFICATION_DOMAINS,
        'status_labels': DOMAIN_STATUS_LABELS,
        'domains_total': len(CERTIFICATION_DOMAINS),
        'domains_certified': domains_certified,
        'total_criteria': total_criteria,
    },
    'certification_levels': {
        'title': 'Certification Levels',
        'levels': CERTIFICATION_LEVELS,
        'goal_all_domains_certified': True,
        'overall_level': overall_certification_level,
        'overall_level_name': CERTIFICATION_LEVELS[overall_certification_level - 1]['name'],
    },
    'executive_readiness_dashboard': {
        'title': 'Executive Readiness Dashboard',
        'indicators': EXEC_DASHBOARD_INDICATORS,
        'live': certification_dashboard_live,
        'identifies_remaining_work': True,
        'status': 'planned',
    },
    'independent_readiness_review': {
        'title': 'Independent Readiness Review',
        'invite_volunteers_and_advisors': True,
        'identify_blind_spots': True,
        'completed': independent_review_completed,
        'status': 'planned',
    },
    'launch_recommendation': {
        'title': 'Launch Recommendation',
        'options': LAUNCH_RECOMMENDATION_OPTIONS,
        'issued': launch_recommendation_issued,
        'current': None,
        'documented_rationale': True,
        'status': 'planned',
    },
    'certification_archive': {
        'title': 'Certification Archive',
        'fields': CERTIFICATION_ARCHIVE_FIELDS,
        'permanently_preserved': True,
        'started': certification_archive_started,
        'status': 'planned',
    },
    'integration': {
        'chain': (
            'Mission Control → PMO → Digital Twin → LocalBrains → Research Institute → '
            'Community Education Academy → Volunteer Network → Coalition Network → Operating Manual'
        ),
        'every_system_participates': True,
        'systems': [
            {'system': 'Master Launch Plan (#85)', 'route': '/mission-control/master-launch-plan.html', 'status': 'live'},
            {'system': 'Execution Schedule (#88)', 'route': '/mission-control/execution-schedule.html', 'status': 'live'},
            {'system': 'PMO (#89)', 'route': '/mission-control/pmo-execution-office.html', 'status': 'live'},
            {'system': 'Operating Manual (#90)', 'route': '/mission-control/institutional-operating-manual.html', 'status': 'live'},
            {'system': 'Digital Twin (#81)', 'route': '/mission-control/institutional-digital-twin.html', 'status': 'live'},
            {'system': 'ACOS 2.0 (#96)', 'route': '/mission-control/arkansas-civic-operating-system.html', 'status': 'live'},
        ],
    },
    'long_term_vision': (
        'When January 2027 arrives, Citizens United Facts demonstrates—with documentation, '
        'measurable standards, and transparent evidence—that it has prepared itself to '
        'responsibly serve Arkansas. That confidence becomes part of its reputation from day one.'
    ),
    'summary': {
        'completion_target_date': completion_target_date,
        'days_remaining': days_remaining,
        'institutional_launch_certification_readiness_pct': institutional_launch_certification_readiness,
        'master_launch_plan_readiness_pct': mlp.get('summary', {}).get('master_launch_plan_readiness_pct', 54),
        'overall_certification_score': overall_certification_score,
        'overall_certification_level': overall_certification_level,
        'overall_certification_level_name': CERTIFICATION_LEVELS[overall_certification_level - 1]['name'],
        'domains_certified': domains_certified,
        'domains_total': len(CERTIFICATION_DOMAINS),
        'certification_dashboard_live': certification_dashboard_live,
        'independent_review_completed': independent_review_completed,
        'launch_recommendation_issued': launch_recommendation_issued,
        'launch_checklist_items_complete': mlp.get('summary', {}).get('checklist_items_complete', 3),
        'launch_checklist_items_total': mlp.get('summary', {}).get('checklist_items_total', 36),
        'institutional_completion_pct': ex.get('overall_completion', mc.get('build', 96)),
    },
    'catalog_gaps': [
        'Certification dashboard not live',
        '0/12 domains certified',
        'No independent readiness review conducted',
        'Launch recommendation not yet issued',
        'Certification archive not started',
        'Domain criteria not tracked item-by-item in MC',
        'Statewide readiness map not operational',
        'No automated certification level promotion workflow',
        'Technology domain below launch threshold (accounts, search, AI)',
        'Academy and volunteer domains significantly below ready',
        'Digital Twin not synchronized for certification audit',
        'Annual review schedule not enforced',
    ],
    'recommended_next_build': {
        'number': 98,
        'title': 'Executive War Room & Countdown Dashboard Components',
        'note': (
            'War room UI, countdown dashboard, certification tracker, domain criteria '
            'checklist, launch recommendation workflow, COMP-* specs.'
        ),
    },
}

with open(root / 'data/institutional-launch-certification.json', 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')

print(
    f'Launch Certification: {len(CERTIFICATION_DOMAINS)} domains, '
    f'{domains_certified} certified, {overall_certification_score}% overall, '
    f'{institutional_launch_certification_readiness}% readiness'
)
