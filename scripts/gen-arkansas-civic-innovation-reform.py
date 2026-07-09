"""
Generate data/arkansas-civic-innovation-reform.json — Build #74.
Master Arkansas Civic Innovation & Reform Center v1.0.
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
ari = load_json(root / 'data/arkansas-research-institute.json')
ex = mc.get('executive', {})

# Honest zeros
reform_analyses_completed = 0
comparative_studies = 0
model_legislation_reviews = 0
ballot_initiative_resources = 0
congressional_resource_guides = 0
research_requests = 0
citizen_lab_submissions = 0
reform_libraries_operational = 0
civic_solution_builder_live = False
reform_dashboard_live = False

PHILOSOPHY_QUESTIONS = [
    'What problem is this trying to solve?',
    'What exactly is being proposed?',
    'How would it work?',
    'What constitutional questions arise?',
    'What arguments are commonly made in favor?',
    'What arguments are commonly made against it?',
]

REFORM_LIBRARIES = [
    {
        'id': 'ACIR-L1', 'number': 1, 'title': 'Congressional Actions',
        'topics': [
            'Disclosure requirements', 'Reporting modernization', 'Transparency improvements',
            'Ethics-related proposals', 'Election administration reforms', 'Constitutional amendment proposals',
        ],
        'note': 'Explains legislative process and constitutional constraints',
        'analyses': 0, 'status': 'specified',
    },
    {
        'id': 'ACIR-L2', 'number': 2, 'title': 'Arkansas Legislative Ideas',
        'topics': [
            'State disclosure laws', 'Public reporting improvements', 'Educational initiatives',
            'Transparency measures', 'Ethics proposals',
        ],
        'note': 'Distinguishes current law from potential future ideas',
        'analyses': 0, 'status': 'specified',
    },
    {
        'id': 'ACIR-L3', 'number': 3, 'title': 'Ballot Initiative Resource Center',
        'topics': [
            'How ballot initiatives work in Arkansas', 'Historical initiatives',
            'Current initiative process', 'Educational analyses of initiative concepts',
            'Implementation considerations',
        ],
        'no_institutional_policy': True, 'analyses': 0, 'status': 'specified',
    },
    {
        'id': 'ACIR-L4', 'number': 4, 'title': 'Constitutional Amendment Center',
        'topics': [
            'Federal amendment process', 'Arkansas constitutional amendment process',
            'Historical amendments', 'Campaign finance amendment proposals',
            'Arguments and constitutional implications',
        ],
        'analyses': 0, 'status': 'specified',
    },
    {
        'id': 'ACIR-L5', 'number': 5, 'title': 'Comparative State Reform Library',
        'topics': [
            'Transparency laws', 'Disclosure systems', 'Public financing approaches',
            'Ethics frameworks', 'Campaign finance reporting', 'Educational innovations',
        ],
        'analyses': 0, 'status': 'specified',
    },
    {
        'id': 'ACIR-L6', 'number': 6, 'title': 'International Models',
        'topics': [
            'Political spending', 'Campaign finance', 'Transparency',
            'Election oversight', 'Disclosure',
        ],
        'comparative_education': True, 'analyses': 0, 'status': 'specified',
    },
    {
        'id': 'ACIR-L7', 'number': 7, 'title': 'Local Government Innovations',
        'topics': [
            'Transparency initiatives', 'Open data projects', 'Public engagement models',
            'Educational outreach', 'Community participation strategies',
        ],
        'analyses': 0, 'status': 'specified',
    },
    {
        'id': 'ACIR-L8', 'number': 8, 'title': 'Citizen Innovation Lab',
        'submission_types': [
            'Questions', 'Research topics', 'Educational proposals',
            'Community suggestions', 'Model reforms',
        ],
        'editorial_review_before_public': True,
        'submissions': citizen_lab_submissions, 'status': 'planned',
    },
]

PROPOSAL_FRAMEWORK_SECTIONS = [
    'Background', 'Current law', 'Historical context', 'Research summary',
    'Supporting evidence', 'Potential benefits', 'Potential concerns',
    'Constitutional considerations', 'Comparison with other approaches',
    'Primary sources', 'Related lessons',
]

REFORM_DASHBOARD = [
    {'id': 'ACIR-D1', 'indicator': 'Reform analyses completed', 'current': reform_analyses_completed, 'status': 'planned'},
    {'id': 'ACIR-D2', 'indicator': 'Comparative studies', 'current': comparative_studies, 'status': 'planned'},
    {'id': 'ACIR-D3', 'indicator': 'Model legislation reviews', 'current': model_legislation_reviews, 'status': 'planned'},
    {'id': 'ACIR-D4', 'indicator': 'Ballot initiative educational resources', 'current': ballot_initiative_resources, 'status': 'planned'},
    {'id': 'ACIR-D5', 'indicator': 'Congressional resource guides', 'current': congressional_resource_guides, 'status': 'planned'},
    {'id': 'ACIR-D6', 'indicator': 'Research requests', 'current': research_requests, 'status': 'planned'},
    {'id': 'ACIR-D7', 'indicator': 'Public questions', 'current': 0, 'status': 'planned'},
    {'id': 'ACIR-D8', 'indicator': 'Future topics', 'current': 0, 'status': 'planned'},
]

SYSTEM_CONNECTIONS = [
    {'system': 'Research Institute (#73)', 'route': '/mission-control/arkansas-research-institute.html', 'status': 'live', 'note': 'Policy Innovation Lab'},
    {'system': 'Evidence Ledger (#41)', 'route': '/mission-control/evidence-ledger.html', 'status': 'live'},
    {'system': 'Campaign Finance Observatory (#63)', 'route': '/mission-control/campaign-finance-observatory.html', 'status': 'live'},
    {'system': 'Knowledge Graph', 'route': '/mission-control/knowledge-graph.html', 'status': 'planned'},
    {'system': 'Citizen Action Center (#62)', 'route': '/mission-control/citizen-action-center.html', 'status': 'live'},
    {'system': 'Community Education Academy (#28)', 'route': '/mission-control/education-academy.html', 'status': 'partial'},
    {'system': 'Community Listening (#71)', 'route': '/mission-control/arkansas-community-listening.html', 'status': 'live'},
    {'system': 'Mission Control', 'route': '/mission-control/', 'status': 'live'},
]

arkansas_civic_innovation_reform_readiness = min(
    44,
    10 + len(REFORM_LIBRARIES) * 3 + len(PROPOSAL_FRAMEWORK_SECTIONS) + 3,
)

out = {
    'version': '1.0',
    'build': 74,
    'updated': today,
    'title': 'Master Arkansas Civic Innovation & Reform Center v1.0',
    'subtitle': 'From Research to Responsible Reform — The Civic Solutions Laboratory',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/arkansas-civic-innovation-reform.html',
    'constitution': '/docs/MASTER_ARKANSAS_CIVIC_INNOVATION_REFORM.md',
    'purpose': (
        'Arkansas\'s most comprehensive educational library of civic reform ideas — '
        'objective study for citizens, legislators, researchers, educators, journalists, and students.'
    ),
    'governing_principle': (
        'Expand quality of civic conversation. Help Arkansans understand the full landscape of ideas, '
        'evaluate evidence, appreciate constitutional constraints, recognize competing viewpoints. '
        'Informed citizens evaluate reform better than those who hear only slogans.'
    ),
    'signature_educational_resource': True,
    'not_single_solution_advocacy': True,
    'center_explains_citizens_decide': True,
    'mission': {
        'title': 'Center Mission',
        'explains': [
            'What reforms have been proposed', 'Why they were proposed',
            'Who supports them', 'Who opposes them', 'Constitutional considerations',
            'Potential advantages', 'Potential disadvantages', 'Historical experience',
            'Implementation considerations',
        ],
    },
    'institutional_philosophy': {
        'title': 'Six Questions Every Proposal Answers',
        'questions': PHILOSOPHY_QUESTIONS,
        'same_educational_framework': True,
    },
    'reform_libraries': {
        'title': 'Eight Reform Libraries',
        'libraries_total': len(REFORM_LIBRARIES),
        'libraries_operational': reform_libraries_operational,
        'libraries': REFORM_LIBRARIES,
    },
    'proposal_framework': {
        'title': 'Proposal Framework',
        'standardized_sections': PROPOSAL_FRAMEWORK_SECTIONS,
        'consistent_structure': True,
        'status': 'specified',
    },
    'civic_solution_builder': {
        'title': 'Civic Solution Builder',
        'interactive_feature': True,
        'live': civic_solution_builder_live,
        'capabilities': [
            'Compare reform ideas', 'Study combinations of approaches',
            'Explore constitutional questions', 'Understand implementation challenges',
        ],
        'education_not_advocacy': True,
        'status': 'planned',
    },
    'reform_dashboard': {
        'title': 'Mission Control Reform Dashboard',
        'live': reform_dashboard_live,
        'indicators': REFORM_DASHBOARD,
        'status': 'planned',
    },
    'integration': {
        'chain': (
            'Research Institute → Evidence Ledger → Campaign Finance Observatory → '
            'Knowledge Graph → Citizen Action Center → Education Academy → Mission Control'
        ),
        'systems': SYSTEM_CONNECTIONS,
        'grounded_in_documented_research': True,
    },
    'long_term_vision': (
        'First place Arkansans visit to understand lawful, constitutional, historically informed '
        'options for improving campaign finance transparency and civic participation — examining '
        'ideas thoughtfully rather than promoting predetermined conclusions.'
    ),
    'summary': {
        'reform_libraries': len(REFORM_LIBRARIES),
        'libraries_operational': reform_libraries_operational,
        'reform_analyses_completed': reform_analyses_completed,
        'comparative_studies': comparative_studies,
        'model_legislation_reviews': model_legislation_reviews,
        'ballot_initiative_resources': ballot_initiative_resources,
        'congressional_resource_guides': congressional_resource_guides,
        'citizen_lab_submissions': citizen_lab_submissions,
        'civic_solution_builder_live': civic_solution_builder_live,
        'reform_dashboard_live': reform_dashboard_live,
        'arkansas_civic_innovation_reform_readiness_pct': arkansas_civic_innovation_reform_readiness,
        'research_institute_readiness_pct': ari.get('summary', {}).get('arkansas_research_institute_readiness_pct', 43),
        'public_launch_readiness_pct': ex.get('public_launch_readiness', 8),
    },
    'catalog_gaps': [
        '0 reform analyses completed — no reform library pages published',
        '0/8 reform libraries operational — scaffold only',
        '0 comparative studies — state/international libraries empty',
        '0 model legislation reviews — Arkansas legislative library not built',
        '0 ballot initiative educational resources — resource center not live',
        '0 congressional resource guides — congressional library not built',
        'Citizen Innovation Lab planned — 0 submissions, no intake form',
        'Civic Solution Builder planned — interactive compare not built',
        'Reform dashboard planned — not live in Mission Control',
        'Proposal framework specified — no standardized page template',
        'Build #74 vs Research Institute Policy Lab (#73) — reconcile roles?',
        'Build #74 vs Campaign Finance Observatory (#63) — unify reform data?',
        'No institutional neutrality badge on reform pages — design needed',
        'Current law vs proposed reform distinction — no UI pattern',
    ],
    'recommended_next_build': {
        'number': 75,
        'title': 'Implementation Translation Layer & Engineering Artifacts',
        'note': (
            'Reform library pages, proposal template, solution builder, citizen lab intake, '
            'reform dashboard, neutrality UI, COMP-* specs, GitHub backlog.'
        ),
    },
}

with open(root / 'data/arkansas-civic-innovation-reform.json', 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')

print(
    f'Arkansas Civic Innovation Reform: {reform_analyses_completed} analyses, '
    f'{reform_libraries_operational}/8 libraries, '
    f'{arkansas_civic_innovation_reform_readiness}% readiness'
)
