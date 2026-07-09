"""
Generate data/arkansas-research-institute.json — Build #73.
Master Research Institute & Arkansas Policy Innovation Laboratory v1.0.
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
ex = mc.get('executive', {})

# Honest zeros
research_projects_underway = 0
completed_white_papers = 0
policy_comparisons = 0
research_requests = 0
citation_reviews = 0
divisions_operational = 0
research_dashboard_live = False
review_workflow_operational = False
repository_projects = 0

MISSION_TOPICS = [
    'Citizens United', 'Campaign finance', 'Constitutional law', 'Government transparency',
    'Ballot initiatives', 'Election administration', 'Civic participation', 'Public trust in institutions',
]

RESEARCH_PHILOSOPHY_QUESTIONS = [
    'What changed?', 'What remained the same?', 'What does the evidence show?',
    'What do different researchers conclude?',
    'What are the strengths and limitations of proposed reforms?',
]

RESEARCH_DIVISIONS = [
    {
        'id': 'ARI-D1', 'number': 1, 'title': 'Constitutional Research',
        'topics': [
            'First Amendment', 'Judicial reasoning', 'Supreme Court precedent',
            'Constitutional interpretation', 'Federalism', 'Historical constitutional development',
        ],
        'projects': 0, 'status': 'specified',
    },
    {
        'id': 'ARI-D2', 'number': 2, 'title': 'Campaign Finance Research',
        'topics': [
            'Historical spending', 'Reporting systems', 'Disclosure',
            'Independent expenditures', 'Campaign finance trends', 'Comparative research',
        ],
        'projects': 0, 'status': 'specified',
    },
    {
        'id': 'ARI-D3', 'number': 3, 'title': 'Arkansas Civic Research',
        'topics': [
            'Arkansas law', 'State constitutional provisions', 'Legislative processes',
            'Ballot initiative procedures', 'Public records', 'Arkansas-specific civic education',
        ],
        'projects': 0, 'status': 'specified',
    },
    {
        'id': 'ARI-D4', 'number': 4, 'title': 'Comparative Policy Research',
        'topics': [
            'Disclosure laws', 'Public financing models', 'Reporting systems',
            'Transparency reforms', 'Ethics structures', 'Educational initiatives',
        ],
        'comparison_not_endorsement': True, 'projects': 0, 'status': 'specified',
    },
    {
        'id': 'ARI-D5', 'number': 5, 'title': 'International Comparisons',
        'topics': [
            'Political spending', 'Campaign finance', 'Disclosure',
            'Election oversight', 'Constitutional protections',
        ],
        'educational_context': True, 'projects': 0, 'status': 'specified',
    },
    {
        'id': 'ARI-D6', 'number': 6, 'title': 'Public Opinion Research',
        'topics': [
            'Public understanding', 'Educational misconceptions', 'Knowledge growth',
            'Civic literacy', 'Community educational needs',
        ],
        'improves_curriculum': True, 'projects': 0, 'status': 'specified',
    },
    {
        'id': 'ARI-D7', 'number': 7, 'title': 'Policy Innovation Laboratory',
        'work_types': [
            'Educational models', 'Model legislation', 'Model constitutional amendments',
            'Educational analyses of ballot initiative concepts', 'Transparency proposals',
            'Congressional reform concepts', 'Arkansas legislative concepts',
        ],
        'distinguishes': ['Documented facts', 'Research findings', 'Possible policy options'],
        'projects': 0, 'status': 'specified',
    },
    {
        'id': 'ARI-D8', 'number': 8, 'title': 'Future Trends Observatory',
        'topics': [
            'Artificial intelligence and elections', 'Digital political communication',
            'Campaign finance technology', 'Transparency innovations',
            'Civic education technologies', 'Institutional trust',
        ],
        'projects': 0, 'status': 'specified',
    },
]

RESEARCH_STANDARDS = [
    'Purpose', 'Research question', 'Methodology', 'Sources', 'Evidence summary',
    'Limitations', 'Alternative viewpoints', 'Future research needs',
]

RESEARCH_REVIEW_WORKFLOW = [
    {'step': 1, 'id': 'research', 'title': 'Research', 'items': 0, 'status': 'planned'},
    {'step': 2, 'id': 'peer_review', 'title': 'Peer Review (where applicable)', 'items': 0, 'status': 'planned'},
    {'step': 3, 'id': 'editorial_review', 'title': 'Editorial Review', 'items': 0, 'status': 'planned'},
    {'step': 4, 'id': 'evidence_verification', 'title': 'Evidence Verification', 'items': 0, 'status': 'planned'},
    {'step': 5, 'id': 'publication', 'title': 'Publication', 'items': 0, 'status': 'planned'},
    {'step': 6, 'id': 'scheduled_review', 'title': 'Scheduled Review', 'items': 0, 'status': 'planned'},
]

RESEARCH_DASHBOARD = [
    {'id': 'ARI-DB1', 'indicator': 'Research projects underway', 'current': research_projects_underway, 'status': 'planned'},
    {'id': 'ARI-DB2', 'indicator': 'Completed white papers', 'current': completed_white_papers, 'status': 'planned'},
    {'id': 'ARI-DB3', 'indicator': 'Policy comparisons', 'current': policy_comparisons, 'status': 'planned'},
    {'id': 'ARI-DB4', 'indicator': 'Research requests', 'current': research_requests, 'status': 'planned'},
    {'id': 'ARI-DB5', 'indicator': 'Citation reviews', 'current': citation_reviews, 'status': 'planned'},
    {'id': 'ARI-DB6', 'indicator': 'Emerging topics', 'current': 0, 'status': 'planned'},
    {'id': 'ARI-DB7', 'indicator': 'Knowledge gaps', 'current': 0, 'status': 'planned'},
    {'id': 'ARI-DB8', 'indicator': 'Future priorities', 'current': 0, 'status': 'planned'},
]

REPOSITORY_FEATURES = [
    'Research history', 'Supporting sources', 'Revision history',
    'Related projects', 'Knowledge Graph relationships',
]

SYSTEM_CONNECTIONS = [
    {'system': 'Evidence Ledger (#41)', 'route': '/mission-control/evidence-ledger.html', 'status': 'live'},
    {'system': 'Claims Registry', 'route': '/mission-control/evidence-ledger.html', 'status': 'live'},
    {'system': 'Knowledge Graph', 'route': '/mission-control/knowledge-graph.html', 'status': 'planned'},
    {'system': 'Master Research Library (#37)', 'route': '/mission-control/research-library.html', 'status': 'live'},
    {'system': 'Master Curriculum (#35)', 'route': '/mission-control/curriculum.html', 'status': 'live'},
    {'system': 'Campaign Finance Observatory (#63)', 'route': '/mission-control/campaign-finance-observatory.html', 'status': 'live'},
    {'system': 'Research Observatory (#29)', 'route': '/mission-control/research-observatory.html', 'status': 'live'},
    {'system': 'Community Listening (#71)', 'route': '/mission-control/arkansas-community-listening.html', 'status': 'live', 'note': 'Research requests'},
    {'system': 'Citizen Action Center (#62)', 'route': '/mission-control/citizen-action-center.html', 'status': 'live'},
    {'system': 'Mission Control', 'route': '/mission-control/', 'status': 'live'},
]

arkansas_research_institute_readiness = min(
    43,
    10 + len(RESEARCH_DIVISIONS) * 3 + len(RESEARCH_REVIEW_WORKFLOW) * 2 + 3,
)

out = {
    'version': '1.0',
    'build': 73,
    'updated': today,
    'title': 'Master Research Institute & Arkansas Policy Innovation Laboratory v1.0',
    'subtitle': 'From Education to Better Ideas — The Arkansas Civic Research Institute',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/arkansas-research-institute.html',
    'constitution': '/docs/MASTER_ARKANSAS_RESEARCH_INSTITUTE.md',
    'purpose': (
        'Arkansas leading center for evidence-based research into campaign finance, '
        'constitutional governance, transparency, and civic participation — not predetermined answers.'
    ),
    'governing_principle': (
        'Expand knowledge, not certainty. Illuminate evidence, explain competing ideas fairly, '
        'equip Arkansans to think critically. Help them think more deeply — not tell them what to think.'
    ),
    'permanent_institutional_pillar': True,
    'not_advocacy_predetermined_answers': True,
    'mission': {
        'title': 'Institute Mission',
        'topics': MISSION_TOPICS,
        'distinguishes': ['Established facts', 'Competing viewpoints', 'Policy proposals'],
    },
    'research_philosophy': {
        'title': 'Research Philosophy',
        'begins_with_questions': True,
        'starter_questions': RESEARCH_PHILOSOPHY_QUESTIONS,
        'teaches_evidence_evaluation': True,
    },
    'research_divisions': {
        'title': 'Eight Research Divisions',
        'divisions_total': len(RESEARCH_DIVISIONS),
        'divisions_operational': divisions_operational,
        'divisions': RESEARCH_DIVISIONS,
    },
    'research_standards': {
        'title': 'Research Standards',
        'required_elements': RESEARCH_STANDARDS,
        'transparency_strengthens_credibility': True,
        'status': 'specified',
    },
    'research_review': {
        'title': 'Research Review',
        'mc_tracks_every_stage': True,
        'operational': review_workflow_operational,
        'workflow': RESEARCH_REVIEW_WORKFLOW,
        'status': 'planned',
    },
    'research_repository': {
        'title': 'Research Repository',
        'permanent_archive': True,
        'projects_archived': repository_projects,
        'features': REPOSITORY_FEATURES,
        'builds_on_prior_work': True,
        'status': 'planned',
    },
    'research_dashboard': {
        'title': 'Mission Control Research Dashboard',
        'live': research_dashboard_live,
        'indicators': RESEARCH_DASHBOARD,
        'status': 'planned',
    },
    'integration': {
        'chain': (
            'Evidence Ledger → Claims Registry → Knowledge Graph → Research Library → '
            'Curriculum → Campaign Finance Observatory → Citizen Action Center → Mission Control'
        ),
        'systems': SYSTEM_CONNECTIONS,
        'supports_every_function': True,
    },
    'long_term_vision': (
        'Widely respected for careful questions, transparent evidence, fair comparison, '
        'educational resources for citizens, educators, journalists, students, and officials. '
        'Reputation rests on scholarship, transparency, and intellectual honesty.'
    ),
    'summary': {
        'research_divisions': len(RESEARCH_DIVISIONS),
        'divisions_operational': divisions_operational,
        'research_projects_underway': research_projects_underway,
        'completed_white_papers': completed_white_papers,
        'policy_comparisons': policy_comparisons,
        'research_requests': research_requests,
        'citation_reviews': citation_reviews,
        'repository_projects': repository_projects,
        'research_dashboard_live': research_dashboard_live,
        'review_workflow_operational': review_workflow_operational,
        'arkansas_research_institute_readiness_pct': arkansas_research_institute_readiness,
        'research_observatory_readiness_pct': ex.get('observatory_readiness', 20),
        'campaign_finance_observatory_readiness_pct': ex.get('campaign_finance_observatory_readiness', 36),
        'public_launch_readiness_pct': ex.get('public_launch_readiness', 8),
    },
    'catalog_gaps': [
        '0 research projects underway — no project intake or pipeline',
        '0 completed white papers — Policy Innovation Lab not operational',
        '0/8 divisions operational — division pages and leads not assigned',
        'Research dashboard planned — not live in Mission Control',
        'Review workflow specified — 0 items through 6-stage process',
        'Research repository planned — 0 archived projects',
        'Policy Innovation Lab — facts vs options UI not built',
        'Knowledge Graph integration planned — research relationships not mapped',
        'Build #73 vs Research Observatory (#29) — reconcile institute vs observatory?',
        'Build #73 vs Campaign Finance Observatory (#63) — unify data research roles?',
        'Peer review process not defined — external reviewers not recruited',
        'Citation review workflow not built — 0 reviews completed',
        'Public opinion research division — no survey instrument',
    ],
    'recommended_next_build': {
        'number': 74,
        'title': 'Implementation Translation Layer & Engineering Artifacts',
        'note': (
            'Division pages, research pipeline UI, policy lab workspace, repository integration, '
            'review queue, standards checklist, COMP-* specs, GitHub backlog.'
        ),
    },
}

with open(root / 'data/arkansas-research-institute.json', 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')

print(
    f'Arkansas Research Institute: {research_projects_underway} projects, '
    f'{completed_white_papers} white papers, {divisions_operational}/8 divisions, '
    f'{arkansas_research_institute_readiness}% readiness'
)
